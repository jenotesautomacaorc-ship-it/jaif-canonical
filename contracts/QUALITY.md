# JAIF — QUALITY OWNER-SPECIFIC CONTRACT — CONTEMPORARY FIRST FORMALIZATION — PROPOSAL v0.1

**Frozen baseline:** `main@3a38a354bcbb1440da5c749c757fc5b91da0bc7e`
**Git locator:** `contracts/QUALITY.md`
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
- QUALITY exists as an owner key in recovered PREDDL ownership evidence.
- Phase10 routing repeatedly places hard-test, graceful-degradation, physical-result, UX and commissioning/acceptance criteria under QUALITY.
- Current governance explicitly separates verification from acceptance and operational proof.

Phase10 routing evidence: **15 primary claims** and **50 consumer references** involve `QUALITY`.
Primary claim IDs: W10D-CLM-031, W10D-CLM-032, W10D-CLM-033, W10D-CLM-035, W10D-CLM-039, W10D-CLM-053, W10D-CLM-055, W10D-CLM-057, W10D-CLM-059, W10D-CLM-134, W10D-CLM-135, W10D-CLM-144, W10D-CLM-149, W10D-CLM-151, W10D-CLM-157
Post-cutoff G1 bundles routed here: G1-WB-001, G1-WB-002, G1-WB-003, G1-WB-007, G1-WB-008, G1-WB-009, G1-WB-010, G1-WB-011, G1-WB-013, G1-WB-014, G1-WB-015, G1-WB-016, G1-WB-017, G1-WB-018, G1-WB-019, G1-WB-020, G1-WB-021, G1-WB-022, G1-WB-026, G1-WB-031

## 2. Proposed semantic subject owned

- Identity and semantics of quality/conformance requirements and criteria.
- Specification of verification/test/inspection/commissioning/acceptance criteria and required methods/conditions, where not owned by a narrower technical owner.
- Quality-gate semantics such as what must be demonstrated for conformance/readiness, while evidence records and acceptance authority remain external.

## 3. Explicit non-ownership boundaries

- Evidence objects or provenance (EVID).
- Authority to approve, waive, accept, release or promote (AUTH / competent human authority).
- Process sequence/handoff semantics (PROCESS).
- Change identity/delta/baseline (CHANGE).
- Underlying technical requirement/fact when a technical owner owns it.

## 4. Consumed contracts / referenced owners

Consumed contract != shared ownership.
- `EVID`
- `AUTH`
- `PROCESS`
- `CHANGE`
- `applicable domain/TECH owners`

## 5. Proposed invariants

- Criterion != evidence.
- Test execution != acceptance.
- PASS of a documentary/semantic test != physical commissioning or operational verification.
- Quality result cannot promote ACCEPTED or CURRENT by itself.
- Technical criteria remain with the applicable technical owner when owner-specific technical semantics exist; QUALITY governs conformance framing, not takeover.

## 6. Authority boundary

`QUALITY` semantic ownership does not identify or grant the competent human authority required for ACCEPTED/CURRENT. Authority for future acceptance must be explicitly recorded and remains separate from semantic ownership.

## 7. Identity / version boundary

`contracts/QUALITY.md` is the physical Git locator of this proposed first formalization, not a canonical ID. Version `0.1.0-CONTEMPORARY-PROPOSED` is a proposal version. Neither establishes CANONICAL, ACCEPTED or CURRENT.

## 8. Verification boundary

The proposal must pass G1-M0 boundary/adversarial tests and diff review. Passing those tests verifies only the documentary/semantic scope being tested; it does not verify operational implementation.

## 9. Open items / fail-closed conditions

- Exact boundary between owner-specific technical acceptance criteria and cross-cutting QUALITY criteria must be resolved claim-by-claim.
- Any material conflict with a narrower owner-specific contract discovered later blocks promotion until reconciled.
- No new registry/schema/DDL/owner/domain/engine/lifecycle may be inferred from this proposal.

## 10. Promotion conditions

Before ACCEPTED/CURRENT can ever be considered: source/provenance, semantic owner subject, competent authority, target identity/version, delta, review, applicable verification evidence and supersession/currentness treatment must be explicit under existing governance.
