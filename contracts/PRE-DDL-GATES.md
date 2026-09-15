# Gates pré-DDL

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: cinco gates autorizados na Etapa 3.
Este documento não autoriza DDL nem define schemas, tabelas ou implementação física.

| Gate | Pergunta estrutural para revisão | Lacunas |
| --- | --- | --- |
| Context Provenance | A origem, o contexto e as transformações do contexto estão rastreáveis? | Detalhes históricos e critérios específicos: RECOVERY_REQUIRED. |
| Preference Provenance | A preferência tem fonte, titular/autoridade, escopo e versão identificados? | Detalhes históricos e critérios específicos: RECOVERY_REQUIRED. |
| Decision Authority | A decisão possui autoridade competente e autorização delimitada? | Matriz e responsáveis: RECOVERY_REQUIRED. |
| AI→Execution Lineage | A contribuição de IA está ligada à decisão, à execução e à evidência do resultado? | Mecanismos históricos: RECOVERY_REQUIRED. |
| Cross-domain Ownership | Os responsáveis pelos domínios envolvidos e suas fronteiras estão reconciliados? | Domínios, owners e acordos: RECOVERY_REQUIRED. |

As perguntas são estrutura de revisão deste bootstrap, não reconstrução de contratos
históricos ausentes. Para cada gate, registrar fonte, evidência, owner, decisão,
verificação e pendências. Situação atual dos gates em sistemas reais: NOT_VERIFIED.
Nenhum gate passa por estar documentado. Ausência de requisito necessário bloqueia
avanço; critérios não recuperados não podem ser inventados para liberar execução.
