# jaif-canonical

Fundação do repositório canônico versionado da Jênotes Automação IA First (JAIF).

Escopo: **FOUNDATION / BOOTSTRAP V0.1**. Esta etapa organiza governança,
contratos estruturais, recuperação e revisão. Bootstrap não equivale à recuperação
histórica completa. O estado real da arquitetura JAIF permanece NOT_VERIFIED;
conhecimento histórico não fornecido permanece RECOVERY_REQUIRED.

## Como interpretar o conteúdo

- SOURCE: material de origem, preservado com contexto e proveniência; não é verdade aceita por existir.
- EVIDENCE: registro verificável que sustenta ou refuta uma afirmação delimitada.
- PROPOSED: estado de uma proposta aguardando os gates e a decisão aplicáveis.
- CURRENT: estado de uma versão aceita, vigente e explicitamente promovida pela autoridade humana competente.

SOURCE/EVIDENCE são classes de conteúdo; PROPOSED/CURRENT são estados de governança.
Documentar, aprovar, implementar e verificar são eventos distintos. Nenhum arquivo
deste bootstrap declara componentes operacionais ou promove a arquitetura para CURRENT.

## Organização

- `governance/`: princípios, mudança controlada e Historical Knowledge Recovery (HKR).
- `contracts/`: gates pré-DDL e contratos estruturais, sem implementação física.
- `registry/`: política de ingestão, registro da autorização parcial e inventário HKR ainda sem entradas.
- `eval/`: estrutura inicial de avaliação de IA, sem resultados.
- `tests/`: procedimento inicial de conformidade semântica.
- `evidence/`: orientação para evidências delimitadas e rastreáveis.

Consulte [governança](governance/CANONICAL-GOVERNANCE.md) e [segurança](SECURITY.md).
A branch `main` deverá representar estado aceito após governança; sua mera presença
em `main` não prova implementação ou verificação do objeto descrito.

## Proveniência e limites

Registro controlado da autorização desta fundação:
[BOOTSTRAP-AUTHORIZATION-001](evidence/BOOTSTRAP-AUTHORIZATION-001.md).
Ele registra a autorização humana para o bootstrap documental local, sem commit,
push, PR ou merge; não substitui a fonte histórica original nem concede promoção canônica.
Registro de autorização não equivale a fonte histórica recuperada. A fonte não foi
formalmente ingerida: Source ingestion status = RECOVERY_REQUIRED; Source durable
locator = NOT_VERIFIED. O registro contém evidência PARTIAL e verificação NOT_VERIFIED.
A fonte deverá receber source_id e locator recuperável pelo processo HKR; até isso
ocorrer, a dívida permanece RECOVERY_REQUIRED / NOT_VERIFIED.
Os procedimentos abaixo operacionalizam essa instrução e permanecem sujeitos à revisão.
Responsáveis nominais, fontes históricas e decisões não fornecidas: RECOVERY_REQUIRED.
