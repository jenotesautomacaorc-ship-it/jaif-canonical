# JAIF — Verificação Automatizada: bootstrap técnico

Baseline: `884d6db9b0d7d9dfa33fa14585f0f6ce24b61573`.
Branch: `hardening/jaif-verificacao-automatizada-v0.1`.
Autorização: solicitação Phase 2A nesta execução; somente preparação precommit.
Este registro não cria identidade canônica, owner, domínio, registry, lifecycle,
estado ou gate canônico. A implementação técnica permanece subordinada a
[governança](../governance/CANONICAL-GOVERNANCE.md),
[controle de mudança](../governance/CHANGE-CONTROL.md),
[HKR](../governance/HKR-NON-OMISSION-GATE.md) e
[SCT preflight](../tests/SCT-PREFLIGHT-001.md).

## Objetivo e delta delimitado

Primeira camada de inspeção técnica automatizada, sem execução operacional JAIF.
Somente quatro arquivos novos são autorizados:

- `.github/workflows/jaif-verificacao-automatizada.yml`
- `tools/ci/jaif_verificacao_automatizada.py`
- `tools/ci/test_jaif_verificacao_automatizada.py`
- `evidence/JAIF-CI-BOOTSTRAP.md`

Nenhum registry/schema é alterado; nenhuma ingestão ou promoção é executada.
PR #8 permanece separado e congelado; esta branch nasce da main, não do PR #8.
Nenhum conhecimento proprietário novo é necessário para estes controles genéricos.

## Execução e autoridade técnica

Python standard library only; sem instalação, download, rede ou API no validador.
Git local é necessário para `git ls-files --stage -z`. O universo rastreado é o index;
o conteúdo inspecionado é o working tree, não uma certificação de blobs staged.
Para precommit sem staging, os quatro caminhos bootstrap são adicionalmente
inspecionados de maneira explícita e contados separadamente. Outros untracked
não são cobertos pelo script; a allowlist final exige inspeção Git separada.
Arquivos e index nunca são corrigidos automaticamente.

Workflow em pull_request para main e push em main, runner ubuntu-latest,
timeout de dez minutos e Python 3.13. Os testes precedem o validador; uma falha
impede o passo seguinte. Permissão global somente contents: read, sem permissão
write, segredo customizado, PAT ou persistência de credencial no checkout.
O token efêmero padrão da plataforma não é uma credencial customizada/persistente.
Actions externas permitidas e refs revalidadas por GitHub API nesta preparação:

- actions/checkout v4: `11d5960a326750d5838078e36cf38b85af677262`
- actions/setup-python v5: `a26af69be951a213d495a4c3e4e4022e16d87065`

Somente os SHAs completos são usados; nenhuma tag mutável ou cache externo.
Não se configura required check nesta fase. Execução remota permanece NOT_VERIFIED.

## Cobertura e limites

Checks: paths sensíveis, symlinks, UTF-8/BOM/NUL, conflitos, whitespace final,
padrões conhecidos de segredo sem imprimir valores, cabeçalhos/contagens CSV,
identidade/path único do único asset, presença P01-P15, ordem integral HKR e fluxo
de mudança, links Markdown locais e workflow restrito. CRLF e LF são aceitos.
Todo arquivo rastreado deste baseline é textual; binários futuros exigem CHANGE
explícito, sem exclusão silenciosa da inspeção.

HKR permanece com zero linhas de dados; futura ingestão exige CHANGE e atualização
explícita do teste nessa mudança. O script não cria IDs nem infere identidades.
ASSET permanece com uma linha BOOTSTRAP-AUTHORIZATION-001; os marcadores existentes
não são promovidos ou reinterpretados. Ausência mecânica de princípio/elo bloqueia;
presença textual não comprova aplicação, autoridade, veracidade ou correção semântica.

Links: subset conservador de inline simples e referências, com exclusão de fences
delimitadas e código inline. Não valida anchors internos nem conteúdo externo.
Sintaxe ambígua produz NOT_VERIFIED e bloqueio, podendo exigir revisão manual.
Não é parser completo de Markdown. Workflow usa comparação com template fechado
além de inspeção de Actions; qualquer desvio não demonstrável produz NOT_VERIFIED
e exit não-zero. Isso evita aceitar YAML complexo/ambíguo sem parser externo,
mas até alterações cosméticas exigirão revisão explícita do template técnico.

PASS/FAIL/NOT_VERIFIED são resultados de inspeção técnica, não novos estados.
Exit zero significa apenas aprovação das verificações técnicas aplicáveis.
Violação ou propriedade material não verificável bloqueia com exit não-zero.
Segredos ofuscados, formatos desconhecidos, histórico Git e PII não são cobertos
exaustivamente. O precheck complementa, não substitui GitHub Secret Scanning,
Push Protection ou SECURITY.md. Nenhuma garantia absoluta de segurança.

CI != HUMAN REVIEW

MECHANICAL PASS != SEMANTIC ACCEPTANCE

MECHANICAL PASS != ACCEPTED

MECHANICAL PASS != CURRENT

MECHANICAL PASS != OPERATIONAL VERIFICATION

MECHANICAL PASS != CLOSURE

## Testes e verificação

Fixtures temporárias sintéticas cobrem casos positivos e negativos de CSVs,
IDs duplicados, destino ausente, segredos com saída sanitizada, paths proibidos,
UTF-8/BOM/NUL, conflitos, whitespace, refs mutáveis, permissões/trigger indevidos,
cadeias, princípios, links, template e tolerância CRLF. Não contêm credenciais reais.
Os testes não atribuem resultado a si mesmos: resultados efetivamente executados
e inspeção do working tree são apresentados no relatório desta execução.
Fixtures usam diretório temporário fora do repositório e são removidas ao terminar.
O runtime local disponível é Python 3.12.14 no Windows; o workflow especifica
Python 3.13 no Linux. Execução nessa combinação remota permanece NOT_VERIFIED.
Na primeira tentativa local, a sandbox negou acesso às fixtures temporárias;
isso foi erro de ambiente, seguido de reexecução com acesso autorizado.

## Rollback e riscos residuais

Nesta etapa nada é staged/publicado: eventual descarte dos quatro novos arquivos
depende de autorização própria. Após publicação futura, reversão requer mudança
controlada/revisão; nenhum rollback automático ou modificação de main é autorizado.

PUBLIC_REPOSITORY_CONFIDENTIALITY_BOUNDARY_REQUIRES_EXPLICIT_DECISION

Reviewer humano independente ainda ausente. Credencial CLI ainda possui autoridade
ampla. Disaster recovery externo ainda não foi testado. CI obrigatório continua
pendente; criação do workflow não prova execução remota. Runner ubuntu-latest e
patch de Python 3.13 variam; fixação das Actions não fixa toda a plataforma.
Validação mecânica não elimina revisão adversarial ou risco de alteração conjunta
do validador e das suas expectativas. O teste completo local não prova execução Linux.
Nenhum commit, push, PR, merge ou alteração de branch protection está autorizado aqui.

## Phase 2C — correções precommit delimitadas

Entrada: JAIF_CI_PHASE2B_INDEPENDENT_REVIEW_CORRECTION_REQUIRED.
R01 demonstrou sobrescrita de definições Markdown duplicadas; R02 demonstrou
omissão de extensões em caixa alta; R03 demonstrou exposição de padrão sensível
no path de saída; R04 demonstrou assignment JSON com chave entre aspas não detectado.
Adicionalmente, existência no filesystem Windows não prova identidade exata do
path Git nem inclusão no universo inspecionado.

EXISTENCE ON LOCAL FILESYSTEM != TRACKED/INSPECTED PATH IDENTITY

Correções, sem alterar workflow ou qualquer arquivo do baseline:

- C1: labels normalizados por whitespace/casefold, duplicidade explicitamente
  bloqueada, primeira definição preservada e todos os destinos suportados examinados.
- C2: somente extensões .md e .markdown são suportadas, case-insensitivamente;
  nenhuma cobertura é alegada para outras extensões.
- C3: padrões conhecidos também inspecionam paths; safe_display_path substitui
  o path inteiro por REDACTED e hash SHA-256 truncado determinístico quando sensível.
  Os valores encontrados no conteúdo não entram no relatório.
- C4: assignments aceitam chaves/valores opcionalmente entre aspas simples ou
  duplas, separadores dois-pontos/igual e caixa variável. Permanecem heurísticas
  originalmente com mínimos de comprimento: 12 para token e 8 para senha;
  essa limitação foi removida na Phase 2E abaixo.
- C5: links resolvidos lexicalmente em POSIX, percent-decoding UTF-8 estrito,
  comparação case-sensitive com paths inspecionados; filesystem não concede
  identidade. Escape da raiz, barras invertidas e destinos não inspecionados falham.
  O universo inclui o suplemento explícito dos quatro arquivos bootstrap, não
  qualquer arquivo untracked encontrado localmente. A resolução não segue symlinks;
  validação geral continua bloqueando tipos Git/symlinks não permitidos.
- C6: definições suportam destino simples sem espaços ou entre sinais angulares.
  Títulos e espaços literais não suportados produzem NOT_VERIFIED/bloqueio,
  mesmo sem uso posterior da definição. Espaços percent-encoded são permitidos
  somente quando a identidade decodificada corresponde exatamente ao universo.

Regressões adicionadas: test_33_duplicate_definitions, test_34_markdown_extensions,
test_35_secret_paths_redacted, test_36_assignment_syntax, test_37_exact_inspected_paths,
test_38_definitions_fail_closed, test_39_inventory_git_end_to_end e
test_40_encoded_escape_and_external. Os 32 testes anteriores foram preservados.
Somente testes 19, 24 e 31 tiveram chamadas refinadas: passam explicitamente
o conjunto da fixture à nova interface Markdown, em vez do root do filesystem;
suas expectativas de aprovação/bloqueio não mudaram.
O teste 39 inicializa Git e adiciona somente um arquivo em repositório temporário
externo, sem commit, comprovando descoberta rastreada e exclusão de untracked.
Isso não faz staging neste repositório de trabalho.

Permanecem limites: parser Markdown conservador, ausência de garantia de cobertura
de toda sintaxe Markdown, detecção de segredos por padrões, whitespace final limitado
a espaço/tab, template de workflow fechado e checks semânticos apenas mecânicos.
Nenhum claim de segurança absoluta. Linux/Python 3.13 permanece NOT_VERIFIED até
execução real; testes locais usam Python 3.12.14 no Windows. Os riscos residuais e
as distinções entre PASS mecânico e autoridade humana acima permanecem íntegros.

## Phase 2E — segurança final da interface e do subset

Entrada: JAIF_CI_PHASE2D_INDEPENDENT_REVIEW_CORRECTION_REQUIRED.
D01: argparse reproduzia argumentos desconhecidos, inclusive conteúdo sensível.
A CLI agora usa SafeArgumentParser com error fixo, sem eco da mensagem recebida,
dos argumentos ou do namespace, com exit 2. Help permanece disponível com prog
fixo. Exceções inesperadas na execução de main recebem mensagem fixa e exit 1,
sem exception bruta ou traceback; exceções previstas continuam fail-closed.

D02: a detecção literal de HTML deixava passar whitespace alternativo.
Agora inícios plausíveis de tags, fechamentos e declarações recebem NOT_VERIFIED,
inclusive com TAB, caixa variável e quebra de linha. Não é parser HTML.
Autolinks inequívocos http/https/mailto são deliberadamente ignorados; fences
fechadas e inline code continuam excluídos. Outras sintaxes Markdown ainda exigem
revisão humana; não há claim de cobertura universal do subset.

D03: comprimentos mínimos deixavam assignments sensíveis curtos fora da inspeção.
A presença da chave sensível seguida de dois-pontos/igual agora basta para bloquear,
inclusive valor curto, vazio, Unicode ou conteúdo não classificado. Prosa sem
estrutura de assignment não é marcada. Documentação com exemplos de assignment
também pode bloquear deliberadamente; fixtures os constroem em runtime.

Testes 1–40 preservados sem alterações. Adicionados test_41_cli_secret_argument_redacted,
test_42_raw_html_fail_closed e test_43_short_sensitive_assignments; adicionalmente,
test_44_cli_unexpected_exception_sanitized cobre erro inesperado em subprocesso real.
Nenhum segredo real é utilizado, impresso ou necessário aos testes.

Rotas de saída: report imprime classes/linhas e paths via safe_display_path;
mensagens de resultado e contagens são fixas/numéricas. Argparse inválido e erros
capturados não materializam dados brutos. Git usa stdout/stderr capturados, nunca
propagados pelo relatório. A barreira de exceção não certifica falhas do interpretador
antes de carregar o programa nem falhas do sistema operacional.

Riscos residuais preservados: detecção por padrões não equivale a segurança absoluta;
Markdown conservador, template fechado, whitespace final limitado a espaço/tab,
validação mecânica não semântica e verificação local do working tree.
LINUX_PYTHON_3_13 = NOT_VERIFIED
Reviewer humano independente ausente, credencial CLI ampla e disaster recovery
externo não testado continuam pendentes, assim como a decisão explícita sobre
PUBLIC_REPOSITORY_CONFIDENTIALITY_BOUNDARY_REQUIRES_EXPLICIT_DECISION.
As seis declarações CI/MECHANICAL PASS acima continuam válidas, sem promoção.
O arquivo em disco já continha "cobrem"; "cobremrem" ocorreu na transcrição da
Phase 2D, não no evidence record. Nenhuma alteração cosmética foi necessária.

## Phase 2G — correção limitada F2F-01

A superfície lexical de inspeção HTML agora preserva o texto visível de links
e imagens inline simples, removendo somente sua estrutura e destino reconhecidos.
A variável de análise de referências permanece separada e com a lógica anterior.
HTML no texto visível resulta em NOT_VERIFIED / MARKDOWN_SINTAXE_NAO_VERIFICADA.
Não há interpretação de HTML, parser externo ou dependência nova.
Autolinks externos explicitamente suportados, inline code e fences fechadas
mantêm suas exclusões anteriores. Fence não fechada continua fail-closed.

O teste 45 cobre HTML em labels de links e imagens, TAB/case, texto normal,
autolinks HTTP/HTTPS/mailto e exclusões de código. Os testes 1–44 são preservados.
Esta correção não altera workflow, baseline, registries ou autoridade de promoção.
As limitações e dívidas já declaradas permanecem; execução Linux/Python 3.13
continua NOT_VERIFIED. A correção lexical não equivale a verificação semântica,
segurança absoluta, aprovação humana, ACCEPTED ou CURRENT.
