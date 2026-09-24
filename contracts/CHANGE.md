# JAIF — CHANGE OWNER-SPECIFIC CONTRACT — CONTEMPORARY FIRST FORMALIZATION — PROPOSAL v0.1

**Frozen baseline:** `main@3a38a354bcbb1440da5c749c757fc5b91da0bc7e`
**Git locator:** `contracts/CHANGE.md`
**Proposed version:** `0.1.0-CONTEMPORARY-PROPOSED`
**Status:** PROPOSED — NON-CANONICAL — NON-ACCEPTED — NON-CURRENT
**Canonical ID:** NOT_ASSIGNED
**Historical relation:** FIRST_FORMALIZATION_CONTEMPORARY; NO HISTORICAL PREDECESSOR/SUCCESSOR CLAIM
**DDL / PostgreSQL / runtime:** NOT APPLICABLE TO THIS DOCUMENTAL FORMALIZATION

## 1. Provenance and basis

This is a proposed contemporary first owner-specific formalization. It is derived from recovered owner-key/scope evidence, current repository governance, the bounded Phase10 routing corpus and G1/G1-G working decisions. It is not a reconstruction of an unavailable historical owner-specific contract.

Controlled references for this proposed formalization:
- [Target-binding evidence](../evidence/G1-M0-TARGET-BINDING-EVIDENCE.md)
- [Owner-boundary tests](../tests/G1-M0-OWNER-BOUNDARY-TESTS.md)
- [Canonical governance](../governance/CANONICAL-GOVERNANCE.md)
- [HKR non-omission gate](../governance/HKR-NON-OMISSION-GATE.md)
- [Change control](../governance/CHANGE-CONTROL.md)

Recovered/supporting statements:
- Recovered LCM owner evidence states CHANGE owns controlled change.
- Current CHANGE-CONTROL requires branch→change→evidence→tests→diff→review→PR→merge and requires origin, owner, identity and destination.
- Current change governance requires prior/proposed meaning comparison, materiality, impacts, sources, conflicts, owner and decision.

Phase10 routing evidence: **8 primary claims** and **19 consumer references** involve `CHANGE`.
Primary claim IDs: W10D-CLM-026, W10D-CLM-027, W10D-CLM-028, W10D-CLM-029, W10D-CLM-036, W10D-CLM-041, W10D-CLM-042, W10D-CLM-168
Post-cutoff G1 bundles routed here: G1-WB-001, G1-WB-002, G1-WB-003, G1-WB-004, G1-WB-007, G1-WB-008, G1-WB-009, G1-WB-010, G1-WB-011, G1-WB-012, G1-WB-014, G1-WB-015, G1-WB-016, G1-WB-017, G1-WB-023, G1-WB-024, G1-WB-028

## 2. Proposed semantic subject owned

- Controlled change identity and bounded delta against an identified baseline.
- Target reference, scope, semantic-change classification, materiality/impact references and supersession/version linkage for the change subject.
- Change-set representation and links to decision, implementation and verification records without owning those external semantics.

## 3. Explicit non-ownership boundaries

- Authority to approve/execute/accept (AUTH / competent human).
- Evidence/provenance object semantics (EVID).
- Quality/test criteria (QUALITY).
- Process semantics outside the controlled-change subject (PROCESS).
- Underlying domain fact being changed.

## 4. Consumed contracts / referenced owners

Consumed contract != shared ownership.
- `AUTH`
- `EVID`
- `QUALITY`
- `PROCESS`
- `DOCUMENT/VIEW`
- `applicable domain/TECH owners`

## 5. Proposed invariants

- Discussion/proposal != change implementation.
- Approval != implementation.
- Implementation != verification.
- Change document/diff != authority.
- Stale-base change cannot be applied as if current without reconciliation.
- Change must preserve semantic traceability and explicit target identity.

## 6. Authority boundary

`CHANGE` semantic ownership does not identify or grant the competent human authority required for ACCEPTED/CURRENT. Authority for future acceptance must be explicitly recorded and remains separate from semantic ownership.

## 7. Identity / version boundary

`contracts/CHANGE.md` is the physical Git locator of this proposed first formalization, not a canonical ID. Version `0.1.0-CONTEMPORARY-PROPOSED` is a proposal version. Neither establishes CANONICAL, ACCEPTED or CURRENT.

## 8. Verification boundary

The proposal must pass G1-M0 boundary/adversarial tests and diff review. Passing those tests verifies only the documentary/semantic scope being tested; it does not verify operational implementation.

## 9. Open items / fail-closed conditions

- G1-M1 will decide/add Minimum Necessary Change and the true-delta residuals for downstream dependency coverage, blast radius and rollback/reversibility; G1-M0 does not pre-accept them into this contract.
- Any material conflict with a narrower owner-specific contract discovered later blocks promotion until reconciled.
- No new registry/schema/DDL/owner/domain/engine/lifecycle may be inferred from this proposal.

## 10. Promotion conditions

Before ACCEPTED/CURRENT can ever be considered: source/provenance, semantic owner subject, competent authority, target identity/version, delta, review, applicable verification evidence and supersession/currentness treatment must be explicit under existing governance.
