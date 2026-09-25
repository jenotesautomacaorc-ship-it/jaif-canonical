# G1-M2 — Evidência de Preparação da Engenharia da Experiência Integrada — v0.1.3

**Status:** WORKING / PROPOSED EVIDENCE — NON-CANONICAL — NON-ACCEPTED — NON-CURRENT
**Frozen baseline:** `main@97519dd1bc000422e6d7e9984dd25f97e626c141`
**Planned branch:** `change/g1-m2-integrated-experience-engineering-v0.1`
**Canonical ID:** NOT_ASSIGNED
**Git mutation at initial package preparation time:** NONE; subsequent local working-tree materialization occurred only under separate human authorization and remained unstaged/uncommitted/unpushed during the audits recorded here.
**DDL / PostgreSQL / Notion / n8n / runtime:** NONE AUTHORIZED OR CLAIMED

## 1. Entrada e finalidade

A próxima onda segura após G1-M1 permanece G1-M2, com foco em **Integrated Experience Engineering + Design-to-Evidence**, conforme o registro de disposição G1.

A materialização G1-M0 estabeleceu PROCESS, QUALITY, AUTH, EVID e CHANGE como propostas owner-specific contemporâneas. G1-M1 endureceu CHANGE sem conceder ACCEPTED/CURRENT.

O baseline efetivo para esta preparação é:
`main@97519dd1bc000422e6d7e9984dd25f97e626c141`.

G1-M2 não promove G1-M0/G1-M1 para ACCEPTED/CURRENT e não altera seus limites.

## 2. Fontes de trabalho preservadas

Esta preparação consome como working evidence, não como canon automático:

- `JAIF_G1_GLOBAL_CANONICAL_RECONCILIATION_WORKING_v0.1.md`
  - SHA-256 conhecido: `95078b01943e7d08cebd8e1768fbac036dbfeb21c81f07fe57509110bb892588`
- `JAIF_G1_G_HUMAN_DISPOSITION_DECISION_WORKING_v0.1.json`
  - SHA-256 conhecido: `7c3db7a7b40829367366b7b576e4f7e4a23704ed18591237c3acf2018e9bbfb9`
- estado atual do repositório em `main@97519dd1bc000422e6d7e9984dd25f97e626c141`.

A presença dessas fontes não concede CANONICAL, ACCEPTED ou CURRENT.

## 3. Reconciliação adversarial do plano anterior

O plano G1 original agrupava em G1-M1, além do hardening efetivamente materializado, WB-011 (Semantic Diff), WB-015 (Continuous Coverage) e WB-026 (research provenance/contradiction) “as applicable”.

O merge real G1-M1 foi deliberadamente mais estreito:
- Minimum Necessary Change;
- objective-to-delta traceability;
- dependency/downstream coverage;
- blast radius;
- rollback/reversibility/irreversibility;
- fail-closed para impacto/dependência/reversibilidade materiais desconhecidos.

Isso não invalida G1-M1 porque o próprio pacote materializado declarou seu escopo exato. Porém, os resíduos não podem ser considerados encerrados por inferência.

Disposição controlada:
- `WB-011 Semantic Diff / cross-tool consistency`: **PRESERVED / DEFER TO G1-M4**. G1-M2 exige apenas que divergência material permaneça explícita e bloqueie o handoff; não cria o mecanismo Semantic Diff.
- `WB-015 Continuous Coverage / constraint propagation / evidence completeness`: **MERGE AS NECESSARY G1-M2 DEPENDENCY**. A cobertura requisito→deliverable→verification→evidence é necessária para Design-to-Evidence e não cria Coverage Engine.
- `WB-026 Research provenance and contradiction handling`: **PRESERVED / DEFER TO G1-M4 EVID/HKR DEPENDENCY**. A especialização de pesquisa não é necessária ao PROCESS G1-M2.

Nenhum resíduo é apagado, promovido ou tratado como já implementado.

## 4. Achados do adversarial audit pré-staging sobre v0.1

A primeira materialização local do pacote v0.1 permaneceu sem staging/commit/push e revelou quatro classes de correção antes de qualquer publicação:

1. **TEST-ID COLLISION — BLOCKER:** o arquivo histórico `tests/SCT-PREFLIGHT-001.md` já usa `M2-T01…M2-T05`; o pacote v0.1 também usava `M2-T01…M2-T24`. Identidade de teste concorrente é proibida. v0.1.1 muda o namespace para `G1M2-T01…`.
2. **SEQUENCE AMBIGUITY — BLOCKER:** a cadeia v0.1 agrupava `decision/authorization` apesar do invariante `recommendation != decision != authorization`. v0.1.1 separa decisão de autorização.
3. **EVIDENCE/ACCEPTANCE ORDER — BLOCKER:** a cadeia linear v0.1 colocava acceptance antes de `evidence/Passport`, embora a própria seção de acceptance exigisse evidência dos resultados. v0.1.1 coloca evidência aplicável antes de acceptance e mantém evidence throughout.
4. **CAPABILITY/PROVENANCE PRESERVATION — HARDENING:** a formulação “only as a transversal process competence” poderia ser lida como redução da competência empresarial transversal, e a revisão não carregava explicitamente os supporting statements/routing do G1-M0. v0.1.1 preserva a competência empresarial e formaliza somente suas process semantics, carregando a proveniência de G1-M0.

Nenhum desses achados exige novo path, owner, domain, Engine, registry, lifecycle, source of truth ou PRE-DDL gate.

## 4A. Binding do audit v0.1.1 aos bytes locais e segunda leitura adversarial

A execução humana local confirmou que os três arquivos v0.1.1 no working tree possuem exatamente os SHA-256 do pacote corrigido, com staging vazio, HEAD ainda no baseline e nenhum push.

Portanto, por identidade byte-a-byte:
`G1M2-T01…G1M2-T31 = 31/31 PASS_BOUNDED_LOCAL_BYTES`

Esse PASS é documental/semântico e não equivale a Git-object binding, runtime, acceptance ou CURRENT.

A segunda leitura adversarial contra o baseline PROCESS identificou duas lacunas de continuidade que a suíte v0.1.1 não tornava explícitas:

1. **GOVERNING CONTROL REFERENCE CONTINUITY:** o PROCESS G1-M0 referenciava diretamente `governance/CHANGE-CONTROL.md`; v0.1.1 mantinha CHANGE por contrato owner-specific, mas removia a referência direta ao controle de governança. Para evitar erosão por indirection, v0.1.2 restaura a referência direta.
2. **G1-M0 VERIFICATION CONTINUITY:** v0.1.1 dizia que a revisão deveria passar os testes G1-M2, mas não dizia explicitamente que os requisitos owner-boundary/adversarial do G1-M0 continuavam obrigatórios. v0.1.2 congela que G1-M2 suplementa e não substitui G1-M0.

Também foi reforçada a enumeração explícita dos cinco PRE-DDL gates existentes, sem criação de sexto gate.

Disposição:
`G1_M2_V0_1_1_LOCAL_BYTE_AUDIT = PASS_BOUNDED_WITH_TEST_COVERAGE_GAP`
`G1_M2_V0_1_2_CORRECTION_REQUIRED_BEFORE_STAGING = YES`

## 5. Escopo semântico exato do G1-M2

G1-M2 propõe somente a semântica PROCESS necessária para coordenar a competência empresarial transversal:

`{intenção, contexto, preferência, necessidade} → requisitos → coordenação/compatibilização multidisciplinar → alternativas → cálculo/simulação especializados → recomendação → decisão → autorização quando requerida → materialização/projeto → execução determinística → commissioning/verificação → evidência → acceptance quando requerido → Passport/view controlada → operação/observabilidade → lifecycle/evolução`

A cadeia:
- é PROCESS-primary no que diz respeito a sequência/handoffs;
- consome QUALITY, EVID, AUTH, CHANGE, DOCUMENT/VIEW e TECH owners;
- não transfere ownership;
- não substitui HKR;
- não cria umbrella owner;
- não cria Engine/domínio/lifecycle/SoT;
- não cria sexto PRE-DDL gate.

## 6. Minimum Necessary Change

O conjunto Git corrigido permanece exatamente:

1. MODIFY `contracts/PROCESS.md`
2. ADD `evidence/G1-M2-INTEGRATED-EXPERIENCE-ENGINEERING-EVIDENCE.md`
3. ADD `tests/G1-M2-INTEGRATED-EXPERIENCE-TESTS.md`

Nenhum path adicional é necessário para corrigir os achados v0.1.

Em particular, não são modificados:
- `contracts/QUALITY.md`;
- `contracts/EVID.md`;
- `contracts/AUTH.md`;
- `contracts/CHANGE.md`;
- `contracts/OBSERVABILITY-LINEAGE.md`;
- `contracts/PRE-DDL-GATES.md`;
- `governance/*`;
- registries;
- CI;
- PostgreSQL/DDL/runtime.

Esses contratos/controles são consumidos ou referenciados, não duplicados.

## 7. Binding e dependências

`PROCESS` já existe como first formalization contemporânea G1-M0; G1-M2 propõe sua revisão `0.2.0-CONTEMPORARY-PROPOSED`.

Exact current source blob at `97519dd1bc000422e6d7e9984dd25f97e626c141`:
`contracts/PROCESS.md` = `651519ec0e411674058d63558ffb2933cc2e5acc`.

TECH discipline contracts específicos não são inventados aqui.

G1-M2 pode formalizar a rota genérica `applicable TECH owners`, mas qualquer claim/projeto que dependa de um binding técnico específico deve falhar fechado enquanto esse binding não estiver disponível.

`DOCUMENT/VIEW` é referenciado, mas seu owner-specific binding não é criado ou inferido aqui.

## 7A. G1-M1 change-hardening compliance for this material semantic change

G1-M2 is a material semantic revision even though its Git delta is Markdown-only. Therefore the G1-M1 CHANGE hardening remains governing.

### Objective-to-delta traceability

Declared objective:
formalize the PROCESS semantics required for Integrated Experience Engineering + Design-to-Evidence, including the necessary Continuous Coverage dependency, without creating a new owner/Engine/domain/lifecycle/source of truth.

Exact proposed Git delta remains:
- MODIFY `contracts/PROCESS.md`;
- ADD `evidence/G1-M2-INTEGRATED-EXPERIENCE-ENGINEERING-EVIDENCE.md`;
- ADD `tests/G1-M2-INTEGRATED-EXPERIENCE-TESTS.md`.

No unrelated cleanup/refactor is included.

### Dependency and downstream-consumer coverage

Known semantic dependencies/consumers considered for this proposal include:
- `AUTH`;
- `QUALITY`;
- `EVID`;
- `CHANGE`;
- existing PRE-DDL gates;
- HKR non-omission governance;
- `OBSERVABILITY-LINEAGE`;
- `DOCUMENT/VIEW` references;
- `ROLE/CAPABILITY` references;
- applicable TECH/domain owners;
- later-wave consumers G1-M3 through G1-M7.

Exact TECH, DOCUMENT/VIEW and ROLE/CAPABILITY owner-specific bindings are not inferred. Any dependent claim requiring a missing material binding fails closed.

No claim of globally complete dependency discovery is made beyond the bounded G1/repository/working-evidence universe reviewed for this wave.

### Bounded blast radius

**Intended semantic change:**
- revise PROCESS from the G1-M0 first-formalization proposal to a G1-M2 proposal that explicitly coordinates the integrated-experience chain, Design-to-Evidence, coverage checkpoints and fail-closed handoffs.

**May affect:**
- future interpretation of PROCESS sequencing/handoffs;
- future reviews that consume PROCESS;
- future G1-M3+ designs/orchestrations that rely on this PROCESS surface;
- how later tools/ASTRA/representations are constrained when they consume this process.

**Explicitly outside this blast radius:**
- acceptance or CURRENT promotion;
- canonical-ID assignment;
- runtime implementation;
- physical/project execution;
- PostgreSQL/DDL/Notion/n8n;
- modification of AUTH/QUALITY/EVID/CHANGE/PRE-DDL/OBSERVABILITY-LINEAGE contracts;
- technical discipline calculations/facts;
- ASTRA/tool/runtime/adapters;
- Productization/Radar/Visual Evidence implementation;
- AV/Lighting/vendor qualification.

A three-file diff does not prove a three-subject semantic blast radius; the affected consumers above remain explicit.

### Reversibility / rollback classification

`REVERSIBILITY = REVERSIBLE_WITH_DEFINED_GIT_REVERSAL_PATH`

Before commit:
- restore `contracts/PROCESS.md` exactly from baseline `97519dd1bc000422e6d7e9984dd25f97e626c141`;
- remove the two G1-M2 added files;
- verify exact baseline/worktree state.

After a future commit/merge:
- perform a separately authorized CHANGE that reverts the exact G1-M2 commit/merge or restores the prior PROCESS blob and removes/supersedes the two G1-M2 additions as appropriate;
- reconcile any later dependent change that may already consume G1-M2 before rollback.

Expected runtime/data loss from this documentary proposal: none claimed because G1-M2 authorizes no runtime/DDL/data migration.

`ROLLBACK_TECHNICAL_PLAUSIBILITY = SUPPORTED_BY_GIT_CONTENT_VERSIONING`

`ROLLBACK_EXECUTION_VERIFICATION = NOT_VERIFIED`

A documented Git reversal path is not proof that rollback has been executed successfully in a future repository state. If later waves consume G1-M2, rollback blast radius must be re-evaluated rather than assuming isolation.

### Inherited hardening

The G1-M0 owner-boundary tests and G1-M1 change-hardening tests remain applicable as inherited controls. G1-M2-specific tests supplement them and do not replace them.

## 8. Regras congeladas nesta proposta

- Necessary complexity exists once, in the correct owner, and is consumed many times.
- REUSE → EXTEND/MERGE → RECONCILE → CREATE only after irreducible gap.
- owner != authority != role != person != assignment != executor.
- Process Owner != Semantic Data Owner != Document Owner != Custodian != Authority automatically.
- representation != truth.
- recommendation != decision != authorization != execution != verification != acceptance.
- specialized calculation/simulation != generic AI inference.
- render/view/Passport != physical truth.
- evidence-dependent acceptance requires applicable evidence first.
- unknown material owner/dependency/authority/coverage fails closed.
- no silent cross-tool conflict resolution.
- process chain != HKR chain and does not replace it.
- exactly five PRE-DDL gates; no sixth gate.
- no owner/domain/engine/lifecycle/registry/SoT by convenience.

## 9. ASTRA boundary

ASTRA is deliberately **not materialized in G1-M2**.

G1-M2 creates the governed process surface that a later ASTRA/tool wave may consume.

Preserved inputs for later G1-M4 revalidation, not decisions newly granted by G1-M2:
- ASTRA != source of truth;
- ASTRA != semantic owner;
- ASTRA != acceptance authority;
- specialized software performs calculations/simulations within competence;
- professional/human authority remains where responsibility/risk/judgment requires;
- deterministic/authorized execution and independent verification remain explicit;
- structured/API-first interfaces are preferred where reliable.

## 10. Visual, commercial and technical boundaries

Not materialized in G1-M2:
- Pre-Diagnosis/Radar;
- renders/Visual Evidence/Digital Showroom;
- Productization/Value Packaging;
- “automação que desaparece” acceptance/interaction specifics;
- Economic Traceability & Project Economics;
- Electrical + Network/IP non-degradation;
- AV;
- Lighting/Expolux/SIMPOLED;
- vendor/tool-specific integrations.

These remain preserved for later waves/owner binding. Absence from this three-file delta is deliberate scope control, not loss.

## 11. Post-G1 routing ledger

- G1-M3: Foundation non-degradation — Electrical + Network/IP + commercial non-degradation constraint.
- G1-M4: ASTRA, Tool/Capability Contracts, Minimum Intelligence, Semantic Diff mechanism, Technology Admission, Edge/Adapters, integration/runtime surfaces, and research-provenance dependency.
- G1-M5: commercial/interaction/representation — Pre-Diagnosis/Radar, Visual Evidence/renders/showroom, Productization/Value Packaging, governed communication, Opportunity Continuity; Economic Traceability candidate must be reconciled in the correct existing owners before any write.
- G1-M6: AV, Lighting/Expolux/SIMPOLED, LTECH/ABB/vendor qualification and discipline-specific technical materialization.
- G1-M7: remaining REFERENCE_ONLY/DEFER/source-debt closure without promotion.

No later wave may leapfrog exact owner/target/authority requirements.

## 12. Linguagem

A prioridade de operação humana em português permanece válida.

Este pacote não traduz integralmente o contrato PROCESS existente porque isso ampliaria a superfície do delta e dificultaria distinguir mudança semântica de mudança editorial. A harmonização linguística do repositório deve ser tratada como mudança controlada própria, sem alterar significado.

## 13. Gate de preparação corrigido

`G1_M2_V0_1_ADVERSARIAL_AUDIT = BLOCKED_CORRECTED_BEFORE_STAGING`

`G1_M2_V0_1_1_CORRECTION_SCOPE = SAME_3_PATHS_ONLY`

`G1_M2_V0_1_2_CORRECTION_SCOPE = SAME_3_PATHS_ONLY`

`G1_M2_V0_1_3_CORRECTION_SCOPE = SAME_3_PATHS_ONLY`

`G1_M2_MINIMUM_CHANGE_SET = EXACT_3_PATHS_PROPOSED`

`TECH_SPECIFIC_BINDING = NOT_CLAIMED`

`TEST_ID_COLLISION = CORRECTED_IN_V0_1_1`

`G1_M0_VERIFICATION_CONTINUITY = EXPLICIT_IN_V0_1_2`

`CHANGE_CONTROL_REFERENCE_CONTINUITY = EXPLICIT_IN_V0_1_2`

`ACCEPTANCE_OWNER_BOUNDARY = CLARIFIED_IN_V0_1_3`

`M1_BLAST_RADIUS = EXPLICIT_IN_V0_1_3`

`M1_REVERSIBILITY_ROLLBACK = EXPLICIT_IN_V0_1_3`

`GIT_WRITE = NOT_AUTHORIZED_BY_THIS_PACKAGE`

`ACCEPTED = NOT_GRANTED`

`CURRENT = NOT_GRANTED`

`DDL_RUNTIME = NOT_AUTHORIZED`

`G1_M3_PLUS = NOT_AUTHORIZED`
