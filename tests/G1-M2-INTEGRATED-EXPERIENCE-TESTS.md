# JAIF — G1-M2 INTEGRATED EXPERIENCE ENGINEERING TESTS — PROPOSED v0.1.3

Baseline: `main@97519dd1bc000422e6d7e9984dd25f97e626c141`
Status: PROPOSED TEST SPECIFICATION — NON-CANONICAL — CANDIDATE-BYTE-SPECIFIC PRE-STAGING REVIEW REQUIRED
Canonical ID: NOT_ASSIGNED

Namespace note: historical `tests/SCT-PREFLIGHT-001.md` already uses `M2-T01…M2-T05`. To avoid identity collision, this wave uses the distinct namespace `G1M2-Txx`. The v0.1.3 suite contains `G1M2-T01…G1M2-T38`.

| Test | Name | Adversarial case | Required result |
|---|---|---|---|
| `G1M2-T01` | TRANSVERSAL_CAPABILITY_NOT_OWNER | Integrated Experience Engineering é usada como owner abrangente. | FAIL. Deve permanecer competência empresarial transversal cujas process semantics são PROCESS-primary e consomem owners existentes. |
| `G1M2-T02` | ENTERPRISE_COMPETENCE_NOT_REDUCED_TO_OWNER | A competência transversal é reduzida a “apenas um owner/processo” ou usada para absorver fatos técnicos. | FAIL. Competência empresarial preservada; ownership continua distribuído. |
| `G1M2-T03` | INTENT_IS_NOT_REQUIREMENT | Desejo/intenção do cliente é tratado automaticamente como requisito técnico. | FAIL. Exigir transformação/rastreabilidade e owner aplicável. |
| `G1M2-T04` | CONTEXT_PREFERENCE_PROVENANCE | Contexto/preferência material influencia requisito/recomendação/decisão sem proveniência aplicável. | FAIL / fail closed; preservar gates existentes de Context/Preference Provenance. |
| `G1M2-T05` | REQUIREMENT_PROVENANCE_REQUIRED | Requisito material entra na coordenação sem origem/contexto rastreável. | FAIL / fail closed. |
| `G1M2-T06` | MULTIDISCIPLINARY_COORDINATION_NO_TAKEOVER | Coordenação entre disciplinas transfere ownership dos fatos técnicos ao PROCESS. | FAIL. |
| `G1M2-T07` | UNBOUND_TECH_FAILS_CLOSED | Handoff depende de disciplina técnica específica sem owner/rota suficientemente identificados. | Bloquear handoff dependente; não inventar owner. |
| `G1M2-T08` | MATERIAL_OPTIONS_REQUIRED_WHERE_RELEVANT | Decisão material é apresentada como única opção sem alternativas relevantes ou justificativa. | FAIL ou justificar explicitamente a inaplicabilidade de alternativas. |
| `G1M2-T09` | OPTION_ASSUMPTIONS_TRACEABLE | Alternativa usa cálculo/simulação sem premissas, inputs/versões ou limitações materiais. | FAIL. |
| `G1M2-T10` | SPECIALIZED_CALCULATION_BOUNDARY | Inferência genérica de IA substitui cálculo especializado necessário. | FAIL. |
| `G1M2-T11` | RENDER_IS_NOT_CALCULATION_OR_PHYSICAL_EVIDENCE | Render convincente é apresentado como cálculo/verificação ou prova automática de estado físico. | FAIL. Representation != truth. |
| `G1M2-T12` | RECOMMENDATION_IS_NOT_DECISION | Opção recomendada é tratada como decisão. | FAIL. |
| `G1M2-T13` | DECISION_IS_NOT_AUTHORIZATION | Decisão é usada como autorização sem competência/escopo que explicitamente una os eventos. | FAIL. |
| `G1M2-T14` | AUTHORIZATION_IS_NOT_EXECUTION | Autorização registrada é tratada como evidência de execução. | FAIL. |
| `G1M2-T15` | MATERIALIZATION_IS_NOT_OPERATIONAL_EXECUTION | Projeto/documento/materialização digital é tratado como execução física/operacional concluída. | FAIL. |
| `G1M2-T16` | EXECUTION_IS_NOT_VERIFICATION | Ação aplicada com sucesso é tratada como verificada. | FAIL. |
| `G1M2-T17` | EVIDENCE_PRECEDES_EVIDENCE_DEPENDENT_ACCEPTANCE | Acceptance dependente de evidência é concedido antes da evidência aplicável. | FAIL. |
| `G1M2-T18` | COMMISSIONING_IS_NOT_ACCEPTANCE | Teste/commissioning PASS é tratado como aceite humano ou CURRENT. | FAIL. |
| `G1M2-T19` | ACCEPTANCE_IS_NOT_CURRENT | Aceite delimitado é tratado automaticamente como CURRENT. | FAIL. |
| `G1M2-T20` | EVIDENCE_THROUGHOUT_CHAIN | Evidência é exigida somente no final e elos materiais anteriores ficam sem suporte. | FAIL quando o claim/handoff exige evidência anterior. |
| `G1M2-T21` | PASSPORT_IS_NOT_TRUTH | Passport/view agrega referências e passa a ser tratado como owner/verdade/evidência física por apresentação. | FAIL. |
| `G1M2-T22` | REQUIREMENT_TO_EVIDENCE_COVERAGE | Requisito material não possui deliverable/verification/evidence/acceptance/closure path aplicável nem gap explícito. | FAIL / gap visível; nenhum PASS implícito. |
| `G1M2-T23` | CONSTRAINT_PROPAGATION_NO_OWNER_TRANSFER | Constraint aceita atravessa artefatos e a propagação é tratada como co-ownership. | FAIL. Propagação preserva owner original. |
| `G1M2-T24` | CROSS_TOOL_DIVERGENCE_FAILS_CLOSED | Ferramentas divergem materialmente e o processo escolhe uma silenciosamente. | FAIL. Registrar conflito; authority/precedence aplicável deve resolver. |
| `G1M2-T25` | CHANGE_AFTER_BASELINE_ROUTES_TO_CHANGE | Alteração material após baseline/aceite é aplicada como edição local sem CHANGE. | FAIL. |
| `G1M2-T26` | PROCESS_CHAIN_DOES_NOT_REPLACE_HKR | A cadeia da experiência é tratada como lifecycle/traceability chain substituta da HKR. | FAIL. A cadeia PROCESS é subordinada e complementar. |
| `G1M2-T27` | NO_SIXTH_PREDDL_GATE | G1-M2 cria gate adicional para experience/coverage/design/AI. | FAIL. Os cinco PRE-DDL gates existentes permanecem únicos. |
| `G1M2-T28` | NO_NEW_ENGINE_DOMAIN_LIFECYCLE_SOT | G1-M2 cria Design Engine, Experience Owner, Coverage Engine, lifecycle paralelo, registry ou nova fonte de verdade. | FAIL. |
| `G1M2-T29` | TEST_ID_NAMESPACE_NON_COLLISION | IDs `G1M2-Txx` colidem com Test_IDs existentes no baseline. | FAIL. Namespace deve permanecer distinto; histórico `M2-T01…M2-T05` não é reutilizado. |
| `G1M2-T30` | BASELINE_PROCESS_PROVENANCE_PRESERVED | Revisão remove a base de proveniência/owner-boundary do PROCESS G1-M0 sem sucessão/justificativa. | FAIL. Supporting statements e routing basis devem permanecer rastreáveis. |
| `G1M2-T31` | G1M2_PASS_NOT_PROMOTION | Todos os testes documentais passam. | PASS_BOUNDED apenas; não concede ACCEPTED/CURRENT/runtime/DDL/merge. |
| `G1M2-T32` | G1M0_BOUNDARY_TESTS_NOT_SUPERSEDED | A revisão trata a suíte G1-M2 como substituta dos requisitos owner-boundary/adversarial do G1-M0. | FAIL. G1-M2 suplementa; não supersede ou enfraquece G1-M0. |
| `G1M2-T33` | GOVERNING_CONTROL_REFERENCE_CONTINUITY | A revisão remove/silencia controles governantes de G1-M0 por indirection, inclusive CHANGE-CONTROL ou os cinco PRE-DDL gates aplicáveis. | FAIL. Controles permanecem explicitamente referenciados/consumidos; nenhuma nova autoridade é criada. |
| `G1M2-T34` | ACCEPTANCE_CRITERIA_VS_AUTHORITY | “Acceptance semantics” são atribuídas de forma ampla ao AUTH, confundindo critérios de acceptance com autoridade/decisão de acceptance. | FAIL. QUALITY/TECH mantêm critérios; AUTH/autoridade competente mantém decisão/autoridade de acceptance. |
| `G1M2-T35` | G1M1_CHANGE_HARDENING_NOT_SUPERSEDED | O G1-M2 ignora Minimum Necessary Change, dependency coverage, blast radius ou reversibility porque “é só documentação”. | FAIL. Hardening G1-M1 continua aplicável. |
| `G1M2-T36` | BLAST_RADIUS_REQUIRED | O delta lista três arquivos mas não delimita o alcance semântico e consumidores potencialmente afetados. | FAIL. Blast radius deve declarar intended/may-affect/out-of-scope. |
| `G1M2-T37` | REVERSIBILITY_CLASSIFIED | Mudança semântica material não classifica reversibilidade nem identifica um caminho de reversão quando aplicável. | FAIL / fail closed. |
| `G1M2-T38` | ROLLBACK_PLAN_NOT_VERIFIED | Existe caminho Git de rollback e ele é tratado como rollback comprovado. | FAIL. Plano/plausibilidade != execução verificada; manter NOT_VERIFIED até teste real aplicável. |

## Execution boundary

- Resultado pré-staging pode ser registrado contra bytes exatos do candidato; após staging/commit, a verificação deve ser repetida/bound ao Git object/diff exato.
- PASS exige evidência da avaliação; definição do teste não é execução.
- Estes testes não substituem testes técnicos, cálculos especializados, commissioning físico, acceptance, verificação operacional ou testes de rollback.
- Nenhum PASS autoriza staging, commit, push, PR ou merge.
