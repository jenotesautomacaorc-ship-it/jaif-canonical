# Governança canônica

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: autorização da Etapa 3 indicada no README.
Esta fundação não certifica o estado histórico ou operacional da JAIF.

CANONICAL significa artefato/conteúdo com identidade canônica controlada, proveniência
e evidência adequadas, que passou pelos gates aplicáveis e recebeu decisão competente
favorável de aceitação, registrada e rastreável. Submissão aos gates não basta.
Memória de IA, inferências, sugestões e conversas isoladas não são fonte canônica suficiente.

CANONICAL é classificação de conteúdo, não um novo estado. SOURCE não é CANONICAL;
EVIDENCE não é automaticamente CANONICAL. PROPOSED não é CANONICAL vigente e REJECTED
nunca deve ser tratado como CANONICAL vigente. A aceitação corresponde a ACCEPTED;
CURRENT exige adicionalmente designação de vigência autorizada pela autoridade humana
competente. Aprovação isolada não torna algo CURRENT. Um artefato CANONICAL pode
deixar de ser CURRENT e tornar-se SUPERSEDED, preservando sua identidade e histórico
canônico. Sem evidência ou autoridade suficientes, bloquear a classificação e a promoção
dependentes; não inferir aceitação ou vigência.

## Estados de governança

| Estado | Significado e condição de entrada |
| --- | --- |
| DISCOVERED | Fonte localizada, ainda sem recuperação validada. |
| RECOVERED | Conteúdo recuperado com origem e contexto registrados; não implica aceitação. |
| RECONCILED | Conflitos, duplicações, supersession e lacunas examinados e registrados. |
| PROPOSED | Delta e destino explicitados para avaliação e decisão. |
| VERIFIED | Verificações aplicáveis ao escopo passaram com método, resultado e evidência; não implica aceitação. |
| ACCEPTED | Autoridade humana competente aceitou a versão e seu escopo por decisão registrada. |
| CURRENT | Versão aceita e explicitamente designada vigente, com gates satisfeitos e versão anterior tratada. |
| SUPERSEDED | Versão substituída, preservando vínculo para sua sucessora e decisão. |
| REJECTED | Proposta recusada com justificativa e autoridade registradas. |

O fluxo esperado é DISCOVERED → RECOVERED → RECONCILED → PROPOSED → VERIFIED →
ACCEPTED → CURRENT. Não é automático. Rejeição ou supersession exige decisão;
revisões materiais de conteúdo vigente retornam como proposta de nova versão.
Uma verificação documental não verifica uma implementação física.

FOUNDATION/BOOTSTRAP indica escopo/maturidade deste pacote, não promoção canônica.
RECOVERY_REQUIRED indica lacuna histórica; NOT_VERIFIED indica ausência de verificação.
Esses marcadores não substituem os estados de governança nem são resultados aprovados.

### Escopo dos estados de governança

Os estados definidos nesta seção classificam o estado de governança de um
sujeito controlado e identificado no escopo deste repositório.

Governance state != domain operational state != temporal currentness.

A aplicação de qualquer estado DEVE identificar de forma inequívoca o sujeito
governado. Um estado atribuído a uma fonte histórica não se transfere
automaticamente ao registro que a referencia, ao claim extraído dela, ao
artefato candidato ou ao objeto de domínio representado.

`CURRENT`, neste contrato de governança, significa que uma versão ou sujeito
governado foi `ACCEPTED` e explicitamente autorizado como vigente por autoridade
competente no escopo declarado.

`CURRENT` NÃO pode ser inferido apenas de:

- maior número de versão;
- data ou timestamp mais recente;
- arquivo mais novo;
- ingestão mais recente;
- último commit;
- último valor observado;
- ausência de sucessor conhecido.

Currentness, vigência ou validade operacional de objetos de domínio continuam
subordinadas ao contrato temporal e ao owner competente do respectivo domínio.

`DISCOVERED` significa que o sujeito explicitamente identificado para aquela
classificação foi localizado. O estado não pode ser transferido silenciosamente
entre a fonte histórica e um registro, claim, evidência ou artefato que apenas
a referencia.

Esta clarificação NÃO cria novos estados, NÃO altera automaticamente os valores
permitidos nos campos de status dos registries e NÃO autoriza transições
implícitas.

## Autoridade

IA pode recuperar, comparar, propor, preparar e executar verificações autorizadas.
Promoções devem registrar responsável, versão, evidência e decisão. ACCEPTED e CURRENT
dependem da autoridade humana competente; a IA não pode atribuí-los unilateralmente.
A identificação nominal de owners e a matriz histórica de autoridade são RECOVERY_REQUIRED.
Sem autoridade identificada ou gate satisfeito, bloquear promoção. Autorização para
escrever este bootstrap não é aceitação da arquitetura histórica nem autorização de publicação.

## Princípios obrigatórios

| ID | Princípio | Regra de aplicação |
| --- | --- | --- |
| P01 | Discussion Is Not Canon | Discussão, análise ou sugestão não promove conteúdo. |
| P02 | Approval Is Not Implementation | Registrar aprovação separada da execução. |
| P03 | Implementation Is Not Verification | Exigir verificação independente da afirmação de execução. |
| P04 | Evidence Before Canonical Claim | Exigir evidência e proveniência adequadas para afirmações materiais. |
| P05 | Single Canonical Identity | Reconciliar IDs, aliases e duplicações; não criar taxonomias concorrentes. |
| P06 | No Proliferation by Convenience | Não criar Engine, domínio, família, metodologia ou fonte de verdade por conveniência. |
| P07 | Semantic Freeze Preservation | Explicitar, justificar, rastrear e revisar qualquer mudança semântica material. |
| P08 | Fail Closed | Bloquear promoção quando faltar evidência, autoridade, proveniência ou verificação necessária. |
| P09 | Least Authority | Limitar IA e automações à autoridade necessária e concedida para a ação. |
| P10 | Human Decision Authority | Reservar decisões materiais que exigem autoridade humana; proibir promoção unilateral para CURRENT. |
| P11 | Traceability | Manter a cadeia completa definida no gate HKR, inclusive execução, verificação e fechamento. |
| P12 | Representation Is Not Truth | Renders, painéis, documentos e visualizações não provam automaticamente estado real. |
| P13 | Secrets Never Enter Canon | Excluir credenciais e segredos de fontes, evidências, arquivos e histórico. |
| P14 | Historical Recovery Before Completeness Claims | Exigir fechamento formal e verificável do HKR antes de alegar recuperação completa. |
| P15 | Bootstrap Is Not Full Canon | Manter este pacote como fundação, sem declarar toda a arquitetura implementada ou verificada. |

Aplicar [controle de mudança](CHANGE-CONTROL.md) e [gate HKR](HKR-NON-OMISSION-GATE.md).
