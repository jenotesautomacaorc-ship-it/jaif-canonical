# JAIF CANONICAL MATERIALIZATION & CLOSURE GATE

Estrutura de controle para revisão; não promulga contrato ou invariante novo.
Baseline: 1f8e4ba7e7c52ed51253e0030c7ce913b9b88a48.
Autorização: solicitação humana nesta conversa, em 2026-09-20.
Locator durável da mensagem: NOT_VERIFIED. Canonical ID: NOT_ASSIGNED.

## Escopo e referências

Somente controle documental e inventário de reconciliação local. Aplicam-se
[CANONICAL-GOVERNANCE](CANONICAL-GOVERNANCE.md),
[CHANGE-CONTROL](CHANGE-CONTROL.md), [HKR-NON-OMISSION-GATE](HKR-NON-OMISSION-GATE.md),
[PRE-DDL-GATES](../contracts/PRE-DDL-GATES.md),
[SCT-PREFLIGHT existente](../tests/SCT-PREFLIGHT-001.md) e
[INGESTION-POLICY](../registry/INGESTION-POLICY.md).
O [inventário de reconciliação](../evidence/CLOSURE-GATE-RECONCILIATION.md)
é uma lista de trabalho por caminho, não um novo registry ou fonte canônica.

## Controle da revisão

1. Fixar baseline, branch, universo consultado e delta autorizado. Comparar
   main com origin/main e com consulta remota; ausência de consulta é NOT_VERIFIED.
2. Para cada claim, preservar a cadeia existente sem abreviação:
   SOURCE → CLAIM → EVIDENCE → PROVENANCE → INTERPRETATION → MATERIALITY → OWNER →
   DELTA → DECISION → TARGET → IMPLEMENTATION → VERIFICATION → CLOSURE.
3. Referenciar fonte/versão/locator efetivamente disponíveis. Separar fonte
   original, resumo fornecido, evidência local e interpretação. Registrar conflitos,
   aliases, duplicações, supersession e omissões; ausência não prova inexistência.
4. Registrar semantic owner e autoridade competente separadamente quando
   aplicáveis, além do target concreto e contrato aplicável, somente com suporte.
   Ausentes quando requeridos: RECOVERY_REQUIRED; verificação ausente: NOT_VERIFIED.
   A lacuna bloqueia a materialização ou closure dependente, não autoriza invenção.
5. Comparar delta com os controles existentes; aplicar o SCT já materializado
   somente ao escopo pertinente. Método, resultado, executor e limitações devem
   acompanhar cada verificação. Não criar SCT ou alegar execução inexistente.
6. Separar decisão, implementação, verificação e fechamento. Exigir revisão e
   autoridade aplicáveis antes de qualquer promoção; aprovação não implementa,
   implementação não verifica e verificação não concede CURRENT automaticamente.

## Registro necessário por assunto em revisão

Correção AUD-01: semantic owner ≠ authority ≠ role ≠ person ≠ assignment ≠ executor.
Nenhum desses conceitos concede os demais automaticamente. Ausência de semantic
owner ou de autoridade requerida não pode ser preenchida por inferência.

Usar os elos HKR acima como roteiro, por referências controladas, sem preencher
uma fonte, identidade, evidência ou target ausente por suposição. Registrar também
o conflito/lacuna, a disposição fundamentada e o que falta para a decisão.
Os caminhos do inventário localizam documentos; não atribuem ownership semântico
nem identificam automaticamente targets operacionais. Contratos históricos exatos,
binding e autoridade ainda ausentes permanecem RECOVERY_REQUIRED.

Correção AUD-02: target necessário, mas ainda não recuperado → RECOVERY_REQUIRED;
implementação de target ainda não verificada → NOT_VERIFIED, quando pertinente.
Target realmente não aplicável ao objeto exige justificativa explícita, revisável
e submetida à revisão aplicável; inaplicabilidade não é estado de governança nem
omissão silenciosa. Não exigir PostgreSQL para artefato exclusivamente documental
ou objeto que não pertença ao modelo de dados.

Correção AUD-03: SCT pode contribuir para VERIFICATION dentro de seu escopo.
SCT ≠ technical test ≠ commissioning ≠ acceptance ≠ operational verification.
A existência ou PASS de um SCT não comprova funcionamento físico, commissioning,
acceptance ou estado operacional; não substitui verificações técnicas aplicáveis.

## Visão complementar de materialização/execução

DECISION → OWNER → CONTRACT → INVARIANT → SCT → ARTIFACT → GIT → POSTGRESQL TARGET → IMPLEMENTATION → TEST → EVIDENCE → ACCEPTANCE

Esta visão é subordinada à cadeia superior de rastreabilidade e não omissão HKR,
preservada integralmente no controle da revisão. Não é máquina de estados,
substituta da cadeia HKR, fluxo universal obrigatório, equivalência biunívoca
com seus elos ou autorização automática de implementação ou promoção.
Aplica-se somente aos elementos pertinentes ao objeto em análise. Elementos
inaplicáveis exigem justificativa explícita e revisável, sem apagar elos HKR.

| Elemento da visão | Limite de aplicação subordinado ao HKR |
| --- | --- |
| DECISION | Exige sustentação pelos elos anteriores da cadeia HKR; não dispensa fonte, claim, evidência, proveniência, interpretação, materialidade, owner ou delta. |
| OWNER | Não concede autoridade automaticamente; observar a separação da AUD-01. |
| CONTRACT / INVARIANT | Referenciar artefatos existentes ou manter RECOVERY_REQUIRED quando requeridos e ausentes; não sintetizar contratos ou invariantes históricos. |
| SCT / TEST | Métodos/contribuições para verificação, segundo seu escopo; definição de teste não significa execução nem PASS. Observar AUD-03. |
| ARTIFACT / GIT | Identidade, versionamento e materialização documental; presença em Git não concede CANONICAL, VERIFIED, ACCEPTED, CURRENT ou IMPLEMENTED. |
| POSTGRESQL TARGET | Especialização de TARGET somente quando aplicável ao modelo de dados; observar AUD-02. |
| IMPLEMENTATION | Exige mudança efetiva no alvo autorizado; autorização e documentação não bastam. |
| EVIDENCE | Existe ao longo da cadeia, não apenas ao final; deve sustentar cada afirmação no escopo pertinente. |
| ACCEPTANCE | Exige autoridade humana competente sobre versão e escopo; não equivale automaticamente a CURRENT nem CLOSURE. |

## Critério de closure e limites das classificações

O gate não pode produzir PASS global quando um elo materialmente requerido estiver
sem identidade, origem/proveniência suficiente, owner requerido, autoridade
requerida, decisão, target aplicável definido, implementação quando reivindicada,
verificação aplicável ou evidência compatível com a afirmação; conflito material
não disposto também bloqueia o fechamento. Justificar e revisar elementos
verdadeiramente não aplicáveis, sem simplesmente omiti-los.

RECOVERY_REQUIRED e NOT_VERIFIED são marcadores de lacuna/verificação.
EXISTING, MERGE, TRUE DELTA, REJECT e DEFER são disposições/classificações de
reconciliação, não estados canônicos. Severidades e aplicabilidade também não são
estados. Nenhum desses termos altera a máquina de governança existente.
PASS de cobertura ou não regressão deste documento não é PASS global de closure.

## Limites de saída

Este controle não declara closure completo JAIF, recuperação histórica completa,
arquitetura operacional ou CURRENT. O fechamento M1/M2 permanece delimitado como
registrado em [sua evidência](../evidence/M1-M2-CLOSURE-EVIDENCE.md).
O [registro de owner recovery](../evidence/GOV-HKR-OWNER-BINDING-RECOVERY.md)
continua documentando binding bloqueado e contratos exatos não recuperados.
Não são criados owners, contratos, invariantes, estados, fontes ou targets.
Os cinco PRE-DDL gates existentes permanecem os únicos definidos no contrato;
este roteiro não acrescenta gate PRE-DDL nem autoriza DDL.
Push, PR e merge dependem de autorização explícita posterior.
