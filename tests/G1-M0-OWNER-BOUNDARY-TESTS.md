# JAIF — G1-M0 OWNER BOUNDARY TESTS — PROPOSED v0.1

Baseline: `main@3a38a354bcbb1440da5c749c757fc5b91da0bc7e`
Status: PROPOSED TEST SPECIFICATION — NON-CANONICAL — EXECUTION RESULT IS COMMIT-SPECIFIC
Canonical ID: NOT_ASSIGNED

These tests detect owner collapse, hidden shared ownership, authority leakage, evidence/truth collapse and accidental promotion. The test specification is stable; each execution result must identify the exact commit and evidence trail being reviewed.

| Test | Name | Adversarial case | Required result |
|---|---|---|---|
| `M0-T01` | SINGLE_SEMANTIC_OWNER | A semantic subject is proposed as jointly owned by two of PROCESS/QUALITY/AUTH/EVID/CHANGE. | FAIL. Consumed contract/reference is allowed; shared semantic ownership is not. |
| `M0-T02` | PROCESS_IS_NOT_AUTH | A workflow contains an approval step and therefore grants approval power. | FAIL. PROCESS may locate the step; AUTH defines authority. |
| `M0-T03` | PROCESS_COMPLETION_IS_NOT_ACCEPTANCE | A process reaches its last step. | No automatic ACCEPTED/CURRENT/operational success. |
| `M0-T04` | QUALITY_IS_NOT_AUTHORITY | All quality checks pass. | PASS does not grant acceptance/release/promotion authority. |
| `M0-T05` | QUALITY_SPEC_IS_NOT_EVIDENCE | A test/inspection/commissioning method is documented. | Method existence is not execution evidence. |
| `M0-T06` | EVID_IS_NOT_TRUTH | An evidence object or dashboard exists. | Existence does not prove the represented fact; claim limits/provenance still apply. |
| `M0-T07` | EVID_IS_NOT_ACCEPTANCE | Strong evidence supports a claim. | Acceptance still requires applicable authority/decision. |
| `M0-T08` | AUTH_IS_NOT_ROLE | A user has a job title or role/capability. | Role/capability does not automatically grant authority. |
| `M0-T09` | TOOL_CAPABILITY_IS_NOT_AUTHORIZATION | A connector/tool advertises a capability or permission. | The declaration must not itself grant AUTH; execution-path verification remains a later-wave delta. |
| `M0-T10` | AUTHORIZATION_IS_NOT_VERIFICATION | A competent authority authorizes execution. | Result remains unverified until criteria/method/evidence pass. |
| `M0-T11` | CHANGE_IS_NOT_APPROVAL | A bounded change/diff exists. | A change cannot self-authorize; AUTH/decision is separate. |
| `M0-T12` | CHANGE_IMPLEMENTATION_IS_NOT_VERIFICATION | Files/runtime target changed successfully. | Implementation does not prove verification. |
| `M0-T13` | STALE_BASE_FAILS_CLOSED | A proposed change was prepared against a stale baseline. | Block direct application until reconciliation/rebase proves the intended delta. |
| `M0-T14` | DOCUMENT_VIEW_NOT_SEMANTIC_OWNER | A Markdown file contains rules for multiple subjects. | File/document identity does not make DOCUMENT/VIEW or one owner the blanket semantic owner. |
| `M0-T15` | CONSUMED_CONTRACT_NOT_SHARED_OWNER | PROCESS consumes AUTH/QUALITY/EVID/CHANGE. | Consumption creates references, not co-ownership. |
| `M0-T16` | TECH_FACT_STAYS_TECH_OWNER | A QUALITY or PROCESS contract references an electrical/network/AV/lighting fact. | Underlying technical fact remains with applicable TECH owner. |
| `M0-T17` | FIRST_FORMALIZATION_NOT_RECOVERED_HISTORY | A new owner-specific contract is created from recovered owner scope plus current evidence. | It must be labeled contemporary first formalization, never recovered original/successor unless proven. |
| `M0-T18` | NO_CANONICAL_ID_INFERENCE | A proposed path/version is known. | Canonical ID remains NOT_ASSIGNED until identity convention/authority grants it. |
| `M0-T19` | NO_SIXTH_PREDDL_GATE | One of the five contracts introduces Technology Admission or another new PRE-DDL gate. | FAIL. The five PRE-DDL gates remain the only defined PRE-DDL gates. |
| `M0-T20` | NO_NEW_UMBRELLA_OWNER | A cross-cutting concept spans several owners. | Do not create GOV/Integrated Experience/Lab/AI umbrella owner for convenience. |
| `M0-T21` | NO_RUNTIME_OR_DDL_INFERENCE | The five contracts are documented in Git. | No runtime, PostgreSQL/DDL, implementation or operational verification is implied. |
| `M0-T22` | SCT_IS_NOT_ACCEPTANCE | All M0 negative tests pass. | Test PASS contributes to verification only; it does not grant ACCEPTED/CURRENT. |
| `M0-T23` | MISSING_REQUIRED_BINDING_FAILS_CLOSED | A claim needs an owner/target not formally bound. | Dependent materialization remains blocked; do not infer the missing target. |
| `M0-T24` | RECENCY_IS_NOT_CURRENT | A new first-formalization contract has a later date/version. | Newer does not mean ACCEPTED/CURRENT. |

## Execution boundary

- PASS/FAIL/NOT_VERIFIED results must be recorded against the exact Git commit/diff under review.
- These tests do not replace technical tests, commissioning, acceptance or operational verification.
- Missing evidence or ambiguous ownership must fail closed.
## Controlled references

- [Target-binding evidence](../evidence/G1-M0-TARGET-BINDING-EVIDENCE.md)
- [Canonical governance](../governance/CANONICAL-GOVERNANCE.md)
- [HKR non-omission gate](../governance/HKR-NON-OMISSION-GATE.md)
- [SCT preflight](SCT-PREFLIGHT-001.md)
