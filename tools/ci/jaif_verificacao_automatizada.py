"""Verificação técnica delimitada; não atribui estados de governança."""

import argparse
import csv
import hashlib
import io
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

HKR = 'source_id,source_type,date,subject,domain,candidate_artifact,canonical_id,materiality,provenance,conflict_status,recovery_status,decision_status,implementation_status,verification_status'
ASSET = 'canonical_id,name,artifact_type,domain,owner,version,status,path,source_reference,criticality,last_reviewed'
CHAIN = 'SOURCE CLAIM EVIDENCE PROVENANCE INTERPRETATION MATERIALITY OWNER DELTA DECISION TARGET IMPLEMENTATION VERIFICATION CLOSURE'.split()
CHANGE = 'branch change evidence tests diff review PR merge'.split()
WORKFLOW = '.github/workflows/jaif-verificacao-automatizada.yml'
BOOTSTRAP = (WORKFLOW, 'tools/ci/jaif_verificacao_automatizada.py',
             'tools/ci/test_jaif_verificacao_automatizada.py', 'evidence/JAIF-CI-BOOTSTRAP.md')
PINS = {'actions/checkout': '11d5960a326750d5838078e36cf38b85af677262',
        'actions/setup-python': 'a26af69be951a213d495a4c3e4e4022e16d87065'}
# Template fechado: desvio não interpretável bloqueia; não é parser YAML.
WORKFLOW_TEMPLATE = """name: JAIF — Verificação Automatizada

on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main

permissions:
  contents: read

jobs:
  verificacao:
    name: Verificação automatizada JAIF
    runs-on: ubuntu-latest
    timeout-minutes: 10
    env:
      PYTHONDONTWRITEBYTECODE: '1'
    steps:
      - name: Obter repositório
        uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262
        with:
          fetch-depth: 0
          persist-credentials: false
      - name: Preparar Python
        uses: actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
        with:
          python-version: '3.13'
      - name: Testar validador
        run: python tools/ci/test_jaif_verificacao_automatizada.py
      - name: Verificar repositório
        run: python tools/ci/jaif_verificacao_automatizada.py --repo-root .
"""
SECRET_PATTERNS = {
    'GITHUB_PAT': r'\bgh[pousr]_[A-Za-z0-9]{36,}\b',
    'GITHUB_FINE_GRAINED': r'\bgithub_pat_[A-Za-z0-9_]{20,}\b',
    'AWS_ACCESS_KEY': r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
    'PRIVATE_KEY': r'-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----',
    'API_SECRET': r'\bsk-[A-Za-z0-9_-]{20,}\b',
    'BEARER_TOKEN': r'(?i)\bbearer\s+[A-Za-z0-9._~+/=-]{12,}',
    'TOKEN_ASSIGNMENT': r'''(?i)(?<!\w)["']?\b(?:token|api_key|apikey|access_token)\b["']?\s*[=:]''',
    'PASSWORD_ASSIGNMENT': r'''(?i)(?<!\w)["']?\b(?:password|passwd|senha)\b["']?\s*[=:]''',
}


def issue(kind, path, line=0, status='FAIL'):
    # Nenhum conteúdo capturado, exceção ou valor secreto entra na mensagem.
    return (status, kind, path, line)


def safe_path(path):
    p = PurePosixPath(path)
    return bool(path) and not p.is_absolute() and '\\' not in path and ':' not in path and '..' not in p.parts


def safe_display_path(path):
    if any(re.search(pattern, path) for pattern in SECRET_PATTERNS.values()):
        digest = hashlib.sha256(path.encode('utf-8', errors='surrogatepass')).hexdigest()[:16]
        return '[REDACTED:' + digest + ']'
    return ascii(path)


def path_checks(path, mode='100644'):
    out = []
    for kind, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, path):
            out.append(issue(kind, path))
    if not safe_path(path):
        out.append(issue('CAMINHO_INSEGURO', path))
    if mode not in ('100644', '100755'):
        out.append(issue('TIPO_GIT_NAO_PERMITIDO', path))
    p = PurePosixPath(path.lower())
    if (p.name == '.env' or p.name.startswith('.env.') or
            p.suffix in ('.pem', '.key', '.p12', '.pfx') or
            any(x in ('.secrets', 'secrets.local') for x in p.parts)):
        out.append(issue('CAMINHO_SENSIVEL', path))
    return out


def text_checks(path, data):
    out = []
    if data.startswith(b'\xef\xbb\xbf'):
        out.append(issue('BOM_UTF8', path))
    if b'\0' in data:
        out.append(issue('NUL', path))
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        return [issue('UTF8_INVALIDO', path)], None
    for number, line in enumerate(text.splitlines(), 1):
        if line.rstrip(' \t') != line:
            out.append(issue('WHITESPACE_FINAL', path, number))
        if re.match(r'^(?:<{7,}(?: |$)|={7,}$|>{7,}(?: |$)|\|{7,}(?: |$))', line):
            out.append(issue('CONFLITO_GIT', path, number))
        for kind, pattern in SECRET_PATTERNS.items():
            if re.search(pattern, line):
                out.append(issue(kind, path, number))
    return out, text


def csv_checks(path, text, root):
    expected = HKR if path.endswith('HKR-INVENTORY.csv') else ASSET
    try:
        rows = list(csv.reader(io.StringIO(text, newline=''), strict=True))
    except csv.Error:
        return [issue('CSV_INVALIDO', path)]
    out = []
    if not rows or rows[0] != expected.split(','):
        out.append(issue('CSV_CABECALHO', path))
    data = rows[1:]
    if expected == HKR:
        if data:
            out.append(issue('HKR_INGESTAO_NAO_AUTORIZADA', path))
        return out
    if len(data) != 1:
        out.append(issue('ASSET_CONTAGEM', path))
    ids = set()
    for row in data:
        if len(row) != len(ASSET.split(',')):
            out.append(issue('ASSET_COLUNAS', path))
            continue
        if row[0] in ids:
            out.append(issue('ASSET_ID_DUPLICADO', path))
        ids.add(row[0])
        if row[0] != 'BOOTSTRAP-AUTHORIZATION-001':
            out.append(issue('ASSET_IDENTIDADE', path))
        if row[7] != 'evidence/BOOTSTRAP-AUTHORIZATION-001.md':
            out.append(issue('ASSET_PATH_BASELINE', path))
        if not safe_path(row[7]) or not (root / row[7]).is_file():
            out.append(issue('ASSET_DESTINO_AUSENTE', path))
    return out


def mechanical_checks(path, text):
    if path == 'governance/CANONICAL-GOVERNANCE.md':
        return [issue('PRINCIPIO_AUSENTE_' + f'P{i:02}', path) for i in range(1, 16)
                if not re.search(r'\b' + f'P{i:02}' + r'\b', text)]
    chains = {'governance/HKR-NON-OMISSION-GATE.md': CHAIN,
              'governance/CHANGE-CONTROL.md': CHANGE}
    if path in chains and not re.search(r'\s*→\s*'.join(chains[path]), text):
        return [issue('CADEIA_AUSENTE', path)]
    return []


def pin_checks(text):
    out = []
    refs = re.findall(r'^\s*(?:-\s*)?uses:\s*(\S+)\s*$', text, re.M)
    for ref in refs:
        action, _, sha = ref.partition('@')
        if action not in PINS or not re.fullmatch('[a-f0-9]{40}', sha) or PINS.get(action) != sha:
            out.append(issue('ACTION_REF_NAO_AUTORIZADA', WORKFLOW))
    if len(refs) != 2 or set(refs) != {k + '@' + v for k, v in PINS.items()}:
        out.append(issue('ACTION_SET', WORKFLOW))
    return out


def workflow_checks(text):
    out = pin_checks(text)
    if re.search(r'pull_request_target|\bwrite\b|secrets\s*[.\[]|\bPAT\b', text, re.I):
        out.append(issue('WORKFLOW_PRIVILEGIO', WORKFLOW))
    if text.replace('\r\n', '\n') != WORKFLOW_TEMPLATE:
        out.append(issue('WORKFLOW_FORA_DO_TEMPLATE_VERIFICAVEL', WORKFLOW, status='NOT_VERIFIED'))
    return out


def markdown_checks(path, text, inspected_paths):
    """Subset conservador: inline simples e referências; sintaxe ambígua bloqueia."""
    out, visible, fence = [], [], None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if marker:
            mark, tail = marker.groups()
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence) and not tail.strip():
                fence = None
            continue
        if fence is None:
            # Código inline é removido conservadoramente apenas quando delimitado.
            clean = re.sub(r'(`+).*?\1', '', line)
            visible.append((number, clean))
    if fence:
        out.append(issue('MARKDOWN_FENCE_ABERTO', path, status='NOT_VERIFIED'))
    definitions, targets = {}, []
    for number, line in visible:
        m = re.match(r'^\s*\[([^]]+)\]:\s*(.*)$', line)
        if m:
            label = ' '.join(m[1].split()).casefold()
            if label in definitions:
                out.append(issue('MARKDOWN_REFERENCIA_DUPLICADA', path, number))
            else:
                definitions[label] = number
            destination = m[2].strip()
            if not re.fullmatch(r'(?:<[^<>\s]+>|[^<>\s]+)', destination):
                out.append(issue('MARKDOWN_DEFINICAO_NAO_VERIFICADA', path, number, 'NOT_VERIFIED'))
            else:
                targets.append((destination, number))
    html_lines = []
    for number, line in visible:
        if re.match(r'^\s*\[[^]]+\]:', line):
            continue
        matches = list(re.finditer(r'!?\[([^]\n]*)\]\(([^()\n]*)\)', line))
        for m in matches:
            targets.append((m[2], number))
        remaining = re.sub(r'!?\[[^]\n]*\]\([^()\n]*\)', '', line)
        for m in re.finditer(r'!?\[([^]]+)\](?:\[([^]]*)\])?', remaining):
            label = ' '.join((m[2] or m[1]).split()).casefold()
            if label not in definitions:
                out.append(issue('MARKDOWN_REFERENCIA_AMBIGUA', path, number, 'NOT_VERIFIED'))
        html_surface = re.sub(r'!?\[([^]\n]*)\]\(([^()\n]*)\)', lambda m: m[1], line)
        html_lines.append((number, re.sub(r'<(?:https?://|mailto:)[^<>\s]+>', '', html_surface)))
        if '](' in remaining:
            out.append(issue('MARKDOWN_SINTAXE_NAO_VERIFICADA', path, number, 'NOT_VERIFIED'))
    html_text = '\n'.join(line for _, line in html_lines)
    for match in re.finditer(r'<\s*/?\s*(?:[A-Za-z]|[!?])', html_text):
        number = html_lines[html_text[:match.start()].count('\n')][0]
        out.append(issue('MARKDOWN_SINTAXE_NAO_VERIFICADA', path, number, 'NOT_VERIFIED'))
    for target, number in targets:
        target = target.strip()
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1]
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        if not target or re.search(r'\s', target) or urlsplit(target).scheme:
            out.append(issue('MARKDOWN_DESTINO_NAO_VERIFICADO', path, number, 'NOT_VERIFIED'))
            continue
        if re.search(r'%(?![0-9a-fA-F]{2})', target):
            out.append(issue('MARKDOWN_DESTINO_NAO_VERIFICADO', path, number, 'NOT_VERIFIED'))
            continue
        try:
            local = unquote(urlsplit(target).path, errors='strict')
        except UnicodeDecodeError:
            out.append(issue('MARKDOWN_DESTINO_NAO_VERIFICADO', path, number, 'NOT_VERIFIED'))
            continue
        parts = list(PurePosixPath(path).parent.parts)
        invalid = not local or local.startswith('/') or '\\' in local or ':' in local or any(ord(c) < 32 for c in local)
        for part in local.split('/'):
            if part == '..':
                if not parts:
                    invalid = True
                else:
                    parts.pop()
            elif part not in ('', '.'):
                parts.append(part)
        if invalid or '/'.join(parts) not in inspected_paths:
            out.append(issue('MARKDOWN_LINK_INVALIDO', path, number))
    return out


def validate(root, entries):
    out, texts = [], {}
    for path, mode in sorted(entries.items()):
        problems = path_checks(path, mode)
        out.extend(problems)
        dest = root / path
        if problems:
            continue
        if dest.is_symlink() or not dest.resolve().is_relative_to(root.resolve()):
            out.append(issue('SYMLINK_OU_ESCAPE', path))
            continue
        try:
            problems, text = text_checks(path, dest.read_bytes())
        except OSError:
            out.append(issue('ARQUIVO_ILEGIVEL', path, status='NOT_VERIFIED'))
            continue
        out.extend(problems)
        if text is not None:
            texts[path] = text
            out.extend(mechanical_checks(path, text))
            if PurePosixPath(path).suffix.casefold() in ('.md', '.markdown'):
                out.extend(markdown_checks(path, text, set(entries)))
    required = ('registry/HKR-INVENTORY.csv', 'registry/ASSET-REGISTRY.csv',
                'governance/CANONICAL-GOVERNANCE.md', 'governance/HKR-NON-OMISSION-GATE.md',
                'governance/CHANGE-CONTROL.md', *BOOTSTRAP)
    for path in required:
        if path not in texts:
            out.append(issue('ARQUIVO_OBRIGATORIO_AUSENTE', path))
    for path in required[:2]:
        if path in texts:
            out.extend(csv_checks(path, texts[path], root))
    if WORKFLOW in texts:
        out.extend(workflow_checks(texts[WORKFLOW]))
    return sorted(set(out))


def inventory(root):
    result = subprocess.run(['git', '-C', str(root), 'ls-files', '--stage', '-z'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    entries = {}
    for record in result.stdout.split(b'\0'):
        if not record:
            continue
        meta, path = record.decode('utf-8').split('\t', 1)
        mode, _, stage = meta.split()
        if stage != '0':
            raise ValueError('Index em conflito')
        entries[path] = mode
    return entries


def report(problems):
    for status, kind, path, line in problems:
        print(f'{status} | {kind} | {safe_display_path(path)} | linha {line}')
    print('FAIL: verificação técnica bloqueada.' if problems else
          'PASS: verificações técnicas aplicáveis passaram no universo inspecionado.')
    print('NOT_VERIFIED: correção semântica humana e operação; nenhuma promoção ou closure.')
    print('Padrões locais não substituem GitHub Secret Scanning, Push Protection ou SECURITY.md.')


class SafeArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(2, 'ERRO: argumentos de linha de comando inválidos.\n')


def main():
    parser = SafeArgumentParser(prog='jaif_verificacao_automatizada', description=__doc__)
    parser.add_argument('--repo-root', type=Path, required=True)
    args = parser.parse_args()
    try:
        entries = inventory(args.repo_root)
        print(f'Universo Git rastreado: {len(entries)} arquivos.')
        # Exceção explícita de inspeção precommit, sem adicionar ao index.
        supplemental = [p for p in BOOTSTRAP if p not in entries]
        for path in supplemental:
            entries[path] = '100644'
        print(f'Arquivos bootstrap adicionais inspecionados: {len(supplemental)}.')
        problems = validate(args.repo_root, entries)
    except (OSError, ValueError, subprocess.SubprocessError):
        problems = [issue('INVENTARIO_NAO_VERIFICADO', '.', status='NOT_VERIFIED')]
    report(problems)
    return bool(problems)


if __name__ == '__main__':
    try:
        result = main()
    except Exception:
        # Barreira CLI: não materializar mensagem, argv, namespace ou traceback.
        print('NOT_VERIFIED: erro interno; verificação técnica bloqueada.', file=sys.stderr)
        result = 1
    raise SystemExit(result)
