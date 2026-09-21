# HKR-INVENTORY — CHANGE documental de encoding

Baseline: 884d6db9b0d7d9dfa33fa14585f0f6ce24b61573.
Branch: change/hkr-inventory-encoding-v0.1.
Filename é locator de trabalho. Canonical ID: NOT_ASSIGNED.
Origem da dívida: HKR_INVENTORY_ENCODING_BLOCKED, registrada na Wave 01.
Autorização: instrução humana desta execução, limitada a policy/evidence pré-commit.
Locator durável da autorização: NOT_VERIFIED. Não atribui owner ou autoridade de promoção.

## Universo analisado integralmente

- [HKR-INVENTORY](../registry/HKR-INVENTORY.csv).
- [INGESTION-POLICY](../registry/INGESTION-POLICY.md).
- [HKR-NON-OMISSION-GATE](../governance/HKR-NON-OMISSION-GATE.md).
- [CHANGE-CONTROL](../governance/CHANGE-CONTROL.md).
- [CANONICAL-GOVERNANCE](../governance/CANONICAL-GOVERNANCE.md).
- [CANONICAL-MATERIALIZATION-CLOSURE-GATE](../governance/CANONICAL-MATERIALIZATION-CLOSURE-GATE.md).
- [Decisão de indisponibilidade](HKR-SOURCE-PERMANENT-UNAVAILABILITY-DECISION.md).
- [Preparação de sucessão](HKR-CONTROLLED-CONTEMPORARY-SUCCESSION.md).

## Problema e fundamento

O baseline define HKR-INVENTORY como índice de fontes históricas e já permite
referências complementares; nenhum *_status substitui evento material. O CSV tem
somente cabeçalho. A Wave 01 conhece assuntos e disposições, não identidades
suficientes das fontes originais. Histórico/subject ≠ instância de fonte identificada.
source_id ≠ subject label ≠ canonical_id ≠ successor id ≠ evidence locator ≠ disposition id.
Uma nova coluna não recupera identidade, autoridade ou contratos ausentes.
provenance referencia somente conteúdo que seja provenance da fonte/claim:
autor/origem, contexto, cadeia de obtenção, transformações e locators/evidence pertinentes.
PROVENANCE != DECISION; PROVENANCE != AUTHORITY; PROVENANCE != CONFLICT;
PROVENANCE != RECOVERY DISPOSITION; PROVENANCE != CANDIDATE RELATIONSHIP.
Complementary record != provenance field. PROVENANCE != GENERIC LINK BAG.
Outros eventos ficam em registros semanticamente próprios, sem serem deslocados
para provenance por falta de coluna. candidate_artifact não confirma sucessão.
PERMANENTLY UNAVAILABLE não é identidade, estado ou recovery_status automático.
Portanto, admissibilidade + referência resolvem a ambiguidade documental deste
caso sem coluna nova; não resolvem a recuperação histórica ou autorizam ingestão.

## Alternativas

| Alternativa | Disposição nesta análise e fundamento |
| --- | --- |
| A. Inventar source_id | Rejeitada: fabricação de identidade sem evidência. |
| B. Usar subject como source_id | Rejeitada: assunto não distingue instâncias de fonte. |
| C. Usar successor/canonical_id | Rejeitada: mistura fonte, candidato e identidade canônica. |
| D. Adicionar coluna imediatamente | Rejeitada neste escopo: necessidade irredutível não demonstrada; não supre identidade ausente. Caso futuro exige CHANGE próprio. |
| E. Criar novo registry | Rejeitada: proliferação sem necessidade; registros complementares já são admitidos. |
| F. Admissibilidade + evidence reference | Selecionada como proposta convention-first: delimita linhas válidas e referências sem sobrecarregar campos. |

## TRUE DELTA, materialidade e limites

DELTA: adicionar somente a seção de admissibilidade/referências em INGESTION-POLICY
e criar este registro de análise. TARGET: esses dois documentos na branch acima.
Materialidade: impede falsas identidades e falsa representação de eventos no índice.
Não altera significado histórico desconhecido nem inventa fonte, contrato ou invariante.
Semantic owner/binding e autoridade de promoção ausentes permanecem RECOVERY_REQUIRED;
autorização humana para preparar este delta não os substitui. owner ≠ authority.
O CSV não muda porque nenhuma das três fontes satisfaz a admissibilidade.
O schema não muda neste caso: os três objetos ainda não são elegíveis a linha.
Para futura source instance válida, a admissão exige identidade suficiente e
source_id sustentado; registros complementares podem apontar para esse source_id
por referência controlada inequívoca, recuperável e auditável. provenance permanece
restrito à provenance; outros eventos permanecem nos registros complementares e
campos de status continuam índices/resumos. Não é necessário duplicar artificialmente
o vínculo no CSV; nenhuma necessidade irredutível de reverse-link genérico foi demonstrada.
Não se define protocolo de parsing, migração, backfill ou enumeração de status.
Consumidor que exija representação por máquina deve demonstrar necessidade em CHANGE
posterior; não se presume compatibilidade técnica ou implementação desse consumidor.

## Aplicação documental aos três objetos

| Objeto histórico | Evidência e identidade | Resultado da regra |
| --- | --- | --- |
| AIF/EVAL histórico original | Subject conhecido; fonte identificável não recuperada; source_id não fabricável; decisão de indisponibilidade existente preserva disposition. | NOT ELIGIBLE FOR HKR-INVENTORY ROW por identidade de fonte insuficiente. |
| JAIF-VIC-001 histórico original | Subject conhecido; fonte identificável não recuperada; source_id não fabricável; decisão de indisponibilidade existente preserva disposition. | NOT ELIGIBLE FOR HKR-INVENTORY ROW por identidade de fonte insuficiente. |
| Automation Execution & Observability histórico original | Subject conhecido; fonte identificável não recuperada; source_id não fabricável; decisão de indisponibilidade existente preserva disposition. | NOT ELIGIBLE FOR HKR-INVENTORY ROW por identidade de fonte insuficiente. |

O resultado é somente aplicação da regra nesta análise, não governance state,
CSV status, enum ou lifecycle. Não significa inexistência ou rejeição da fonte.
Os evidence records preservados não se tornam os originais; candidatos continuam
não confirmados. Nenhuma linha foi ingerida. Nenhuma ausência foi reconstruída.
ROW ABSENCE != DEBT ABSENCE: os registros existentes preservam a disposição e a
dívida explicitamente rastreada; a ausência de linha não apaga informação registrada.
SOURCE_ID != SUBJECT; SOURCE_ID != SUCCESSOR ID; SOURCE_ID != CANONICAL_ID;
DISPOSITION != STATUS AUTOMATICALLY; EVIDENCE RECORD != HISTORICAL SOURCE.

## Verificação documental e reversibilidade

Executor: assistente nesta execução autorizada. Método: leitura cruzada dos oito
arquivos, aplicação aos três casos, inspeção do diff e verificações locais de
escopo, integridade dos CSVs, whitespace e segredo/PII. Não é verificação operacional.
Critérios separados: Schema Proliferation; Source-vs-Subject; Source-vs-Successor;
Status-vs-Event; Recovery-Disposition; HKR Non-Omission; Semantic Freeze;
Scope Containment; Secret/PII; git diff --check. Resultados são reportados no gate
pré-commit desta execução; definição dos critérios não equivale ao seu PASS.
Rollback proposto: remover/reverter a clarificação documental e este registro sob
controle de mudança, sem migração de dados, pois nenhuma linha/schema foi alterado.

## Dívidas e não promoção

HKR_INVENTORY_ENCODING_BLOCKED tem resolução documental proposta neste CHANGE;
não é declarado encerrado por escrita, teste ou presença em Git. Revisão/decisão
competentes continuam necessárias. Identidade/versionamento históricos, locators,
contratos, binding de owner, autoridade, sucessão e targets requeridos ausentes
permanecem RECOVERY_REQUIRED / NOT_VERIFIED conforme aplicável.
Implementação desta mudança: somente policy/evidence documental.
Verification: documental, sem prova de funcionamento físico ou operacional.
ACCEPTED: NOT_GRANTED. CURRENT: NOT_GRANTED.
Registry ingestion: NOT_EXECUTED. Closure global: NOT_GRANTED.
M1/M2 e Semantic Freeze preservados; não há nova máquina de estados, registry,
schema, PostgreSQL, n8n ou runtime. Nenhum PASS documental concede promoção.
A cadeia SOURCE → CLAIM → EVIDENCE → PROVENANCE → INTERPRETATION → MATERIALITY →
OWNER → DELTA → DECISION → TARGET → IMPLEMENTATION → VERIFICATION → CLOSURE
permanece integralmente exigida; lacunas não são omitidas nem convertidas em PASS.
