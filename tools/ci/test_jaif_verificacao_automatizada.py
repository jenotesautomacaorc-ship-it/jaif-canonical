"""Fixtures sintéticas em diretório temporário; nenhuma credencial real."""
import contextlib
import io
import sys
import tempfile
import subprocess
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
import jaif_verificacao_automatizada as v


class TechnicalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.files = {
            'registry/HKR-INVENTORY.csv': v.HKR + '\n',
            'registry/ASSET-REGISTRY.csv': v.ASSET + '\n' + self.asset_row(),
            'evidence/BOOTSTRAP-AUTHORIZATION-001.md': 'Registro\n',
            'governance/CANONICAL-GOVERNANCE.md': ' '.join(f'P{i:02}' for i in range(1, 16)),
            'governance/HKR-NON-OMISSION-GATE.md': ' →\n'.join(v.CHAIN),
            'governance/CHANGE-CONTROL.md': ' → '.join(v.CHANGE),
            v.WORKFLOW: v.WORKFLOW_TEMPLATE,
            v.BOOTSTRAP[1]: '# fixture\n',
            v.BOOTSTRAP[2]: '# fixture\n',
            v.BOOTSTRAP[3]: '# Evidência\n',
        }
        self.write_files()

    def asset_row(self):
        return 'BOOTSTRAP-AUTHORIZATION-001,n,t,d,o,v,DISCOVERED,evidence/BOOTSTRAP-AUTHORIZATION-001.md,NOT_VERIFIED,c,r\n'

    def write_files(self):
        for path, text in self.files.items():
            dest = self.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(text.encode('utf-8'))

    def hkr(self, text):
        return v.csv_checks('registry/HKR-INVENTORY.csv', text, self.root)

    def asset(self, text):
        return v.csv_checks('registry/ASSET-REGISTRY.csv', text, self.root)

    def test_01_hkr_valid(self):
        self.assertEqual([], self.hkr(v.HKR + '\n'))

    def test_02_hkr_header(self):
        self.assertTrue(self.hkr(v.HKR.replace('subject', 'other')))

    def test_03_hkr_data(self):
        self.assertTrue(self.hkr(v.HKR + '\n' + ','.join(['x'] * 14)))

    def test_04_asset_header(self):
        self.assertTrue(self.asset(v.ASSET.replace('owner', 'other') + '\n' + self.asset_row()))

    def test_05_duplicate(self):
        self.assertIn('ASSET_ID_DUPLICADO', str(self.asset(v.ASSET + '\n' + self.asset_row() * 2)))

    def test_06_missing_asset(self):
        (self.root / 'evidence/BOOTSTRAP-AUTHORIZATION-001.md').unlink()
        self.assertTrue(self.asset(v.ASSET + '\n' + self.asset_row()))

    def test_07_synthetic_pat_redacted(self):
        synthetic = 'gh' + 'p_' + 'SYNTHETIC0' * 4
        problems, _ = v.text_checks('fixture.md', synthetic.encode())
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            v.report(problems)
        self.assertIn('GITHUB_PAT', output.getvalue())
        self.assertNotIn(synthetic, output.getvalue())

    def test_08_private_key(self):
        value = '-----BEGIN ' + 'PRIVATE KEY-----'
        self.assertIn('PRIVATE_KEY', str(v.text_checks('fixture.md', value.encode())[0]))

    def test_09_env(self):
        self.assertTrue(v.path_checks('.env'))

    def test_10_trailing(self):
        self.assertTrue(v.text_checks('fixture.md', b'bad \n')[0])

    def test_11_conflict(self):
        self.assertTrue(v.text_checks('fixture.md', ('<' * 7 + ' HEAD').encode())[0])

    def test_12_mutable(self):
        self.assertTrue(v.pin_checks(v.WORKFLOW_TEMPLATE.replace(v.PINS['actions/checkout'], 'v4')))

    def test_13_pinned(self):
        self.assertEqual([], v.pin_checks(v.WORKFLOW_TEMPLATE))

    def test_14_unsafe_trigger(self):
        self.assertTrue(v.workflow_checks(v.WORKFLOW_TEMPLATE.replace('pull_request:', 'pull_request_target:')))

    def test_15_write(self):
        self.assertTrue(v.workflow_checks(v.WORKFLOW_TEMPLATE.replace('contents: read', 'contents: write')))

    def test_16_hkr_missing(self):
        self.assertTrue(v.mechanical_checks('governance/HKR-NON-OMISSION-GATE.md', ' → '.join(v.CHAIN[:-1])))

    def test_17_principles(self):
        path = 'governance/CANONICAL-GOVERNANCE.md'
        self.assertEqual([], v.mechanical_checks(path, self.files[path]))

    def test_18_principle_missing(self):
        path = 'governance/CANONICAL-GOVERNANCE.md'
        self.assertTrue(v.mechanical_checks(path, self.files[path].replace('P09', '')))

    def test_19_broken_link(self):
        self.assertTrue(v.markdown_checks('a.md', '[bad](missing.md)', set(self.files)))

    def test_20_complete_valid(self):
        self.assertEqual([], v.validate(self.root, {p: '100644' for p in self.files}))

    def test_21_crlf(self):
        for p in self.files:
            self.files[p] = self.files[p].replace('\n', '\r\n')
        self.write_files()
        self.assertEqual([], v.validate(self.root, {p: '100644' for p in self.files}))

    def test_22_utf8_bom_nul(self):
        for data in (b'\xff', b'\xef\xbb\xbfhello', b'hello\0'):
            with self.subTest(data_type=len(data)):
                self.assertTrue(v.text_checks('fixture', data)[0])

    def test_23_paths_and_symlink_mode(self):
        for p in ('/absolute', '../escape', 'C:/absolute', '.secrets/a', 'secrets.local/a', 'a.pem', 'a.key', 'a.p12', 'a.pfx', '.env.test'):
            self.assertTrue(v.path_checks(p))
        self.assertTrue(v.path_checks('a.md', '120000'))

    def test_24_markdown_fences_and_references(self):
        self.assertEqual([], v.markdown_checks('a.md', '```md\n[x](absent.md)\n```', set(self.files)))
        self.assertEqual([], v.markdown_checks('a.md', '[x][ref]\n[ref]: evidence/BOOTSTRAP-AUTHORIZATION-001.md', set(self.files)))
        self.assertTrue(v.markdown_checks('a.md', '[x][absent]', set(self.files)))
        self.assertTrue(v.markdown_checks('a.md', '[x](../escape.md)', set(self.files)))
        self.assertTrue(v.markdown_checks('a.md', '```\n', set(self.files)))

    def test_25_secret_classes_redacted(self):
        values = ('github_' + 'pat_' + 'SYNTHETIC' * 5,
                  'AK' + 'IA' + 'A' * 16,
                  'sk' + '-' + 'SYNTHETIC' * 5,
                  'Bearer ' + 'SYNTHETIC' * 5,
                  'token' + '=' + 'SYNTHETIC' * 5,
                  'password' + '=' + 'SYNTHETIC' * 5)
        for value in values:
            problems, _ = v.text_checks('fixture', value.encode())
            self.assertTrue(problems)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                v.report(problems)
            self.assertNotIn(value, output.getvalue())

    def test_26_workflow_ambiguity_closed(self):
        for extra in ('\npermissions: {}\n', '\n# extra\n', '\n  secrets: inherit\n'):
            self.assertTrue(v.workflow_checks(v.WORKFLOW_TEMPLATE + extra))

    def test_27_chain_order(self):
        self.assertTrue(v.mechanical_checks('governance/HKR-NON-OMISSION-GATE.md', ' → '.join(reversed(v.CHAIN))))
        self.assertTrue(v.mechanical_checks('governance/CHANGE-CONTROL.md', 'missing'))

    def test_28_missing_required(self):
        self.assertTrue(v.validate(self.root, {}))

    def test_29_unauthorized_sha_and_action(self):
        self.assertTrue(v.pin_checks(v.WORKFLOW_TEMPLATE.replace(v.PINS['actions/checkout'], '0' * 40)))
        self.assertTrue(v.pin_checks(v.WORKFLOW_TEMPLATE.replace('actions/checkout@', 'unknown/action@')))

    def test_30_missing_tracked_and_git_mode(self):
        self.assertTrue(v.validate(self.root, {'missing.md': '100644'}))
        self.assertTrue(v.path_checks('submodule', '160000'))

    def test_31_ambiguous_markdown_blocked(self):
        for text in ('[x](name(with).md)', '<a href="absent.md">x</a>', '[x](data:example)'):
            findings = v.markdown_checks('a.md', text, set(self.files))
            self.assertTrue(findings)
            self.assertIn('NOT_VERIFIED', str(findings))

    def test_32_hkr_blank_row_blocked(self):
        self.assertTrue(self.hkr(v.HKR + '\n\n'))

    def test_33_duplicate_definitions(self):
        paths = {'README.md', 'other.md'}
        self.assertEqual([], v.markdown_checks('a.md', '[r]: README.md\n[x][r]', paths))
        for first, second, label in [('README.md', 'other.md', 'r'),
                                     ('missing.md', 'README.md', 'r'),
                                     ('README.md', 'missing.md', 'r'),
                                     ('README.md', 'other.md', 'R')]:
            findings = v.markdown_checks('a.md', f'[r]: {first}\n[{label}]: {second}\n[x][r]', paths)
            self.assertIn('MARKDOWN_REFERENCIA_DUPLICADA', str(findings))
            if 'missing.md' in (first, second):
                self.assertIn('MARKDOWN_LINK_INVALIDO', str(findings))

    def test_34_markdown_extensions(self):
        for suffix in ('.md', '.MD', '.Md', '.mD', '.markdown', '.MARKDOWN'):
            p = 'extra' + suffix
            (self.root / p).write_text('[x](missing.md)', encoding='utf-8')
            findings = v.validate(self.root, {**{f: '100644' for f in self.files}, p: '100644'})
            self.assertTrue(any(f[1] == 'MARKDOWN_LINK_INVALIDO' and f[2] == p for f in findings))

    def test_35_secret_paths_redacted(self):
        values = ('gh' + 'p_' + 'SYNTHETIC0' * 4,
                  'github_' + 'pat_' + 'SYNTHETIC' * 5,
                  'AK' + 'IA' + 'A' * 16,
                  'password' + '=' + 'SYNTHETIC' * 5)
        for value in values:
            path = 'folder/' + value + '.md'
            findings = v.path_checks(path)
            self.assertTrue(findings)
            stdout, stderr = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                v.report(findings)
            self.assertNotIn(value, stdout.getvalue() + stderr.getvalue())
            self.assertIn('REDACTED', stdout.getvalue())
            self.assertEqual(v.safe_display_path(path), v.safe_display_path(path))

    def test_36_assignment_syntax(self):
        value = 'SYNTHETIC' * 4
        for key in ('token', 'api_key', 'apikey', 'access_token', 'password', 'passwd', 'senha'):
            for quote in ('', "'", '"'):
                for separator in (':', '='):
                    for value_quote in ('', "'", '"'):
                        text = quote + key.upper() + quote + separator + value_quote + value + value_quote
                        findings, _ = v.text_checks('fixture', text.encode())
                        self.assertTrue(findings)
                        stdout = io.StringIO()
                        with contextlib.redirect_stdout(stdout):
                            v.report(findings)
                        self.assertNotIn(value, stdout.getvalue())
        for prose in ('A palavra password aparece aqui.', 'token e senha são conceitos.',
                      'Nenhum api_key foi fornecido.', 'access_token não é autoridade.'):
            self.assertEqual([], v.text_checks('fixture', prose.encode())[0])

    def test_37_exact_inspected_paths(self):
        paths = {'README.md', 'sub/file.md'}
        (self.root / 'untracked-local.md').write_text('local', encoding='utf-8')
        for target in ('README.md', 'READ%4dE.md', 'sub/file.md'):
            self.assertEqual([], v.markdown_checks('a.md', f'[x]({target})', paths))
        for target in ('readme.md', 'untracked-local.md', '../escape.md', '%2e%2e/escape.md', 'READ%4de.md'):
            self.assertTrue(v.markdown_checks('a.md', f'[x]({target})', paths))
        self.assertEqual([], v.markdown_checks('sub/a.md', '[x](../README.md)', paths))

    def test_38_definitions_fail_closed(self):
        paths = {'file.md'}
        self.assertEqual([], v.markdown_checks('a.md', '[ref]: <file.md>\n[x][ref]', paths))
        for text in ('[ref]: file.md "title"', '[ref]: file name.md', '[ref]:', '[ref]: <>'):
            findings = v.markdown_checks('a.md', text, paths)
            self.assertTrue(findings)
            self.assertIn('NOT_VERIFIED', str(findings))

    def test_39_inventory_git_end_to_end(self):
        def git(*args):
            return subprocess.run(['git', '-C', str(self.root), *args], check=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        git('init', '--quiet')
        (self.root / 'tracked.md').write_text('tracked\n', encoding='utf-8')
        (self.root / 'untracked.md').write_text('untracked\n', encoding='utf-8')
        git('add', '--', 'tracked.md')
        self.assertEqual({'tracked.md': '100644'}, v.inventory(self.root))

    def test_40_encoded_escape_and_external(self):
        paths = {'file name.md'}
        self.assertEqual([], v.markdown_checks('a.md', '[x](file%20name.md)', paths))
        self.assertEqual([], v.markdown_checks('a.md', '[x](<https://example.com>)', paths))
        for target in ('%2Ffile.md', '%5cfile.md', '%00file.md', 'file%zz.md', '%ff.md'):
            self.assertTrue(v.markdown_checks('a.md', f'[x]({target})', paths))

    def test_41_cli_secret_argument_redacted(self):
        script = Path(v.__file__).resolve()
        synthetic = 'gh' + 'p_' + 'SYNTHETIC0' * 4
        for unknown in (synthetic, 'unknown-ordinary'):
            result = subprocess.run([sys.executable, '-B', str(script), '--repo-root', '.',
                                     '--unknown', unknown], capture_output=True, text=True,
                                    encoding='utf-8', errors='replace')
            self.assertEqual(2, result.returncode)
            self.assertNotIn(unknown, result.stdout + result.stderr)
            self.assertEqual('', result.stdout)
            self.assertIn('ERRO: argumentos de linha de comando', result.stderr)
        result = subprocess.run([sys.executable, '-B', str(script), '--help'], capture_output=True)
        self.assertEqual(0, result.returncode)
        self.assertIn(b'--repo-root', result.stdout)

    def test_42_raw_html_fail_closed(self):
        for html in ('<a href="x">', '<a\thref="x">', '<A href="x">',
                     '<img src="x">', '<img\tsrc="x">', '<div>', '<span>', '</a>',
                     '<a\nhref="x">', '<\ndiv>', '<!-- comment -->', '<a/>'):
            findings = v.markdown_checks('a.md', html, set())
            self.assertTrue(any(f[0] == 'NOT_VERIFIED' and
                                f[1] == 'MARKDOWN_SINTAXE_NAO_VERIFICADA' for f in findings))
        for text in ('<https://example.com>', '<http://example.com>',
                     '<mailto:test@example.com>', '```html\n<div>\n```', '`<div>`'):
            self.assertEqual([], v.markdown_checks('a.md', text, set()))

    def test_43_short_sensitive_assignments(self):
        for key in ('token', 'api_key', 'apikey', 'access_token', 'password', 'passwd', 'senha'):
            for value in ('x', 'abc', '1', 'SYNTHETIC' * 5, '', '☃'):
                for quote in ('', "'", '"'):
                    for separator in (':', '='):
                        text = quote + key + quote + separator + quote + value + quote
                        findings, _ = v.text_checks('fixture', text.encode())
                        self.assertTrue(findings)
        for text in ('the password policy is strong', 'tokenization',
                     'password must be rotated', 'token e senha são conceitos',
                     'access_token não é autoridade'):
            self.assertEqual([], v.text_checks('fixture', text.encode())[0])

    def test_44_cli_unexpected_exception_sanitized(self):
        synthetic = 'gh' + 'p_' + 'SYNTHETIC0' * 4
        code = ("import runpy,sys; from unittest.mock import patch; "
                "secret='gh'+'p_'+'SYNTHETIC0'*4; "
                "sys.argv=['validator','--repo-root','.']; "
                "p=patch('subprocess.run',side_effect=RuntimeError(secret)); p.start(); "
                "runpy.run_path(" + repr(str(Path(v.__file__).resolve())) +
                ",run_name='__main__')")
        result = subprocess.run([sys.executable, '-B', '-c', code], capture_output=True)
        self.assertEqual(1, result.returncode)
        self.assertNotIn(synthetic.encode(), result.stdout + result.stderr)
        self.assertNotIn(b'Traceback', result.stderr)
        self.assertIn(b'NOT_VERIFIED', result.stderr)


    def test_45_html_inside_inline_link_text_fail_closed(self):
        paths = {'README.md'}
        for text in ('[<img src="missing.png">](README.md)',
                     '[<span>text</span>](README.md)',
                     '[<a href="x">link</a>](README.md)',
                     '[<A\thref="x">x</A>](README.md)',
                     '![<span>alt</span>](README.md)', '![<div>](README.md)'):
            with self.subTest(text=text):
                findings = v.markdown_checks('a.md', text, paths)
                self.assertTrue(any(f[0] == 'NOT_VERIFIED' and
                                    f[1] == 'MARKDOWN_SINTAXE_NAO_VERIFICADA' for f in findings))
        for text in ('[texto normal](README.md)',
                     '[<https://example.com>](README.md)',
                     '[<http://example.com>](README.md)',
                     '[<mailto:test@example.com>](README.md)',
                     '`[<div>](README.md)`', '```md\n[<div>](README.md)\n```'):
            with self.subTest(text=text):
                self.assertEqual([], v.markdown_checks('a.md', text, paths))


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(TechnicalTests))
    print('PASS: testes técnicos.' if result.wasSuccessful() else 'FAIL: testes técnicos.')
    raise SystemExit(not result.wasSuccessful())
