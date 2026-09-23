# JAIF — G1-M1 CHANGE HARDENING TESTS — PROPOSED v0.1

Baseline: `main@34ee5c49a84fa71473ac1059c9468f8ff2304aae`
Status: PROPOSED TEST SPECIFICATION — NON-CANONICAL — EXECUTION RESULT IS COMMIT-SPECIFIC
Canonical ID: NOT_ASSIGNED

These tests detect scope inflation, hidden dependency omission, impact understatement, false reversibility and accidental promotion.

| Test | Name | Adversarial case | Required result |
|---|---|---|---|
| `M1-T01` | MINIMUM_NECESSARY_CHANGE | A change includes unrelated cleanup or adjacent feature work. | FAIL. Split or separately justify/authorize the unrelated delta. |
| `M1-T02` | OBJECTIVE_TO_DELTA_TRACEABILITY | A materially changed subject cannot be tied to the declared objective or a demonstrated necessary dependency. | FAIL. |
| `M1-T03` | CONVENIENCE_REFACTOR_NOT_NECESSARY | Refactoring is bundled because it is convenient while touching the same files. | FAIL unless independently necessary to the authorized objective and evidenced. |
| `M1-T04` | SMALL_DIFF_NOT_LOW_MATERIALITY | A one-line change alters authority, identity, semantics, security or operational behavior. | Materiality review remains required; diff size is insufficient. |
| `M1-T05` | DOC_ONLY_NOT_AUTOMATICALLY_IMMATERIAL | A Markdown-only change materially changes meaning. | Treat semantic impact independently of file type. |
| `M1-T06` | DEPENDENCY_COVERAGE_REQUIRED | A material target has known dependencies/consumers but the change record omits them. | FAIL. |
| `M1-T07` | UNKNOWN_MATERIAL_DEPENDENCY_FAILS_CLOSED | A materially relevant dependency is reasonably expected but cannot be determined with sufficient evidence. | Block dependent implementation/promotion; do not infer absence. |
| `M1-T08` | DOWNSTREAM_CONSUMER_RECHECK | A changed contract is consumed downstream. | Re-evaluate materially affected consumers before claiming bounded impact. |
| `M1-T09` | BLAST_RADIUS_REQUIRED | A material change describes the file diff but not what semantics/operations may be affected. | FAIL. |
| `M1-T10` | BLAST_RADIUS_NOT_OWNER_TAKEOVER | Impact spans multiple owners. | Record impact/reference only; do not transfer semantic ownership to CHANGE. |
| `M1-T11` | ROLLBACK_WHERE_APPLICABLE | A material reversible change has no rollback/reversal path. | FAIL. |
| `M1-T12` | ROLLBACK_PLAN_NOT_VERIFIED | A rollback procedure is documented but never tested/verified. | Keep rollback capability NOT_VERIFIED; plan existence is insufficient. |
| `M1-T13` | IRREVERSIBLE_CHANGE_ESCALATION | A materially irreversible change is treated as routine reversible work. | FAIL; require explicit rationale, authority and mitigation/containment. |
| `M1-T14` | REVERSIBILITY_UNKNOWN_FAILS_CLOSED | Reversibility is material but unknown. | Block dependent implementation/promotion. |
| `M1-T15` | ROLLBACK_IS_NOT_AUTHORITY | A rollback path exists. | It does not grant execution, waiver, acceptance or promotion authority. |
| `M1-T16` | IMPLEMENTATION_IS_NOT_VERIFICATION | The change was applied successfully. | Still require applicable verification evidence. |
| `M1-T17` | STALE_BASE_RECONCILIATION | The proposal was prepared against a baseline that changed materially. | Block direct application until reconciliation proves the intended delta. |
| `M1-T18` | NO_DUPLICATE_SEMANTIC_OWNER | Core G1-M1 semantics are copied into a new Impact/Dependency/Rollback owner or engine. | FAIL. Reuse CHANGE; references are consumption, not co-ownership. |
| `M1-T19` | NO_SIXTH_PREDDL_GATE | G1-M1 introduces a new PRE-DDL gate for impact, rollback or technology admission. | FAIL. Existing five PRE-DDL gates remain unchanged. |
| `M1-T20` | M1_PASS_NOT_PROMOTION | All G1-M1 documentary tests pass. | PASS contributes only to scoped verification; no automatic ACCEPTED/CURRENT/runtime claim. |

## Execution boundary

- Results must be recorded against the exact Git baseline/head and complete diff under review.
- Missing material dependency, impact, authority, evidence or reversibility information fails closed.
- These tests do not replace technical tests, commissioning, acceptance, rollback execution testing or operational verification.
- Test PASS does not authorize merge.
