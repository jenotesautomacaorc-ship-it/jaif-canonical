# Inventário de reconciliação do Closure Gate

Lista de trabalho documental; filename é locator, não identidade canônica.
Canonical ID: NOT_ASSIGNED. Baseline: 1f8e4ba7e7c52ed51253e0030c7ce913b9b88a48.
Escopo: os 18 arquivos rastreados desse baseline. Não é inventário histórico
completo nem substitui ASSET-REGISTRY ou HKR-INVENTORY. Nenhuma linha promove estado.
18/18 caminhos Git ≠ 18 ativos JAIF ≠ inventário empresarial completo ≠ recuperação
histórica completa ≠ completude arquitetural. Os caminhos representam somente o
universo Git do baseline desta execução; arquivos não se tornam ativos canônicos
automaticamente.
Fonte desta lista: conteúdo local do baseline; originais externos não consultados.
Método: leitura e comparação documental; existência de texto não prova seu objeto.
Orientação: [controle do gate](../governance/CANONICAL-MATERIALIZATION-CLOSURE-GATE.md).

## Pre-flight observado em 2026-09-20

main, origin/main e HEAD inicial: 1f8e4ba7e7c52ed51253e0030c7ce913b9b88a48.
Working tree inicial limpo; staging vazio; main vs origin/main: 0 ahead / 0 behind.
Consulta git ls-remote confirmou main nesse SHA. A tentativa restrita falhou por
helper HTTPS indisponível; a mesma consulta somente leitura fora da sandbox passou.
Branch preservada recovery/gov-hkr-owner-binding-v0.1, local e remota:
00a9575d2b3f538f5e6a26904ffe20ebfc164988. O baseline já contém o merge PR #5;
esse fato é anterior a este lote e não representa merge executado nesta etapa.

## Reconciliação inicial por caminho existente

Os caminhos abaixo são relativos à raiz. As lacunas não atribuem novos estados
de governança. Identidade de owner não equivale a contrato exato recuperado.

| Caminho no baseline | Conteúdo observado / disposição | Lacuna ou limite |
| --- | --- | --- |
| README.md | Fundação e limites históricos; preservar | Arquitetura real NOT_VERIFIED; recuperação RECOVERY_REQUIRED |
| .gitignore | Exclusões locais; preservar | Não comprova ausência de segredos |
| SECURITY.md | Política documental; preservar | Eficácia operacional NOT_VERIFIED; responsáveis RECOVERY_REQUIRED |
| governance/CANONICAL-GOVERNANCE.md | Estados e princípios existentes; preservar | Semantic owner NOT FORMALLY BOUND / RECOVERY_REQUIRED |
| governance/CHANGE-CONTROL.md | Controle de mudança existente; reutilizar | Autoridade nominal histórica RECOVERY_REQUIRED |
| governance/HKR-NON-OMISSION-GATE.md | Cadeia HKR e persistência; reutilizar | Semantic owner e recuperação histórica RECOVERY_REQUIRED |
| contracts/PRE-DDL-GATES.md | Cinco gates existentes; preservar | Critérios históricos RECOVERY_REQUIRED; execução real NOT_VERIFIED |
| contracts/JAIF-VIC-001.md | Skeleton documental; preservar | Contratos históricos e integração RECOVERY_REQUIRED / NOT_VERIFIED |
| contracts/OBSERVABILITY-LINEAGE.md | Cadeia documental; preservar | Mecanismos/owners RECOVERY_REQUIRED; funcionamento NOT_VERIFIED |
| registry/ASSET-REGISTRY.csv | Uma entrada de autorização bootstrap; preservar | Não é inventário completo nem promoção do registro |
| registry/HKR-INVENTORY.csv | Somente cabeçalho; preservar | Fontes ainda não inventariadas; RECOVERY_REQUIRED |
| registry/INGESTION-POLICY.md | Classes e limites de ingestão; reutilizar | Não substitui recuperação de originais |
| eval/JAIF-AI-EVAL-PILOT-001.md | Estrutura sem resultados; preservar | Amostras/limiares RECOVERY_REQUIRED; resultados NOT_VERIFIED |
| tests/SCT-PREFLIGHT-001.md | Procedimento e fixtures existentes; reutilizar | Definição não prova execução; não criar novos SCTs |
| evidence/README.md | Orientação com escopo bootstrap; preservar | Texto histórico não deve ser lido como inventário atualizado de evidências |
| evidence/BOOTSTRAP-AUTHORIZATION-001.md | Autorização parcial registrada; preservar | Fonte original RECOVERY_REQUIRED; locator NOT_VERIFIED |
| evidence/M1-M2-CLOSURE-EVIDENCE.md | Fechamento documental/Git delimitado registrado; preservar | Não resolve ownership, dívida residual ou CURRENT |
| evidence/GOV-HKR-OWNER-BINDING-RECOVERY.md | Evidência fornecida de recovery; preservar | Contratos exatos NOT RECOVERED / P1 OPEN; binding bloqueado |

## Bloqueios e próximos elementos de reconciliação

- Fontes históricas originais, versões e locators faltantes: RECOVERY_REQUIRED /
  NOT_VERIFIED. Resumos referenciados não são recuperação independente de originais.
- Owner/contrato exato, autoridade e granularidade por assunto: RECOVERY_REQUIRED.
  Não atribuir GOV, DOCUMENT/VIEW, AUTH, CHANGE, EVID ou PROCESS como owner abrangente.
- Target necessário, mas ainda não recuperado: RECOVERY_REQUIRED. Implementação
  ainda não verificada: NOT_VERIFIED, quando pertinente. Target realmente não
  aplicável exige justificativa explícita e revisável, não novo estado ou omissão.
  Não exigir PostgreSQL para artefatos exclusivamente documentais ou objetos fora
  do modelo de dados. Nenhum target operacional é inferido do caminho de um Markdown.
- Conflitos/supersession históricos não examinados em originais: NOT_VERIFIED.
  A formulação de evidence/README.md pertence ao bootstrap; sua reconciliação
  editorial futura não foi executada e não reabre o fechamento M1/M2.
- Para cada materialização futura, reconstruir a cadeia HKR por claim e aplicar
  decisão, evidência e verificação exigidas pelo controle existente. Esta lista
  não satisfaz esses elos nem permite fechamento por preenchimento de tabela.

Delta deste lote: somente este inventário e a estrutura de controle vinculada.
Nenhum conteúdo histórico é reconstruído. Nenhuma lacuna recebe PASS por presença
em main. Closure global e promoção dependentes permanecem bloqueados; CURRENT
não concedido. A dívida residual M1/M2 e a branch de recovery são preservadas.
