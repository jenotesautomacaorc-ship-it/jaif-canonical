# JAIF — AUTH OWNER-SPECIFIC CONTRACT — CONTEMPORARY FIRST FORMALIZATION — PROPOSAL v0.1

**Frozen baseline:** `main@3a38a354bcbb1440da5c749c757fc5b91da0bc7e`
**Git locator:** `contracts/AUTH.md`
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
- Recovered LCM owner evidence states AUTH owns authority rule/limit and authorization.
- Semantic owner != authority != role != person != assignment != executor.

Phase10 routing evidence: **9 primary claims** and **42 consumer references** involve `AUTH`.
Primary claim IDs: W10D-CLM-038, W10D-CLM-051, W10D-CLM-060, W10D-CLM-068, W10D-CLM-075, W10D-CLM-076, W10D-CLM-077, W10D-CLM-078, W10D-CLM-161
Post-cutoff G1 bundles routed here: G1-WB-002, G1-WB-004, G1-WB-005, G1-WB-007, G1-WB-008, G1-WB-009, G1-WB-010, G1-WB-012, G1-WB-013, G1-WB-016, G1-WB-017, G1-WB-018, G1-WB-019, G1-WB-020, G1-WB-022, G1-WB-023, G1-WB-024, G1-WB-026, G1-WB-028

## 2. Proposed semantic subject owned

- Authority-rule identity, allowed/forbidden action scope, decision/approval/authorization limits, consent/override/escalation/revocation conditions.
- Authorization semantics for human, role, agent/tool or external-adapter actions, including bounded subject/action/resource/context/time conditions.
- Least-authority requirements for bounded authorization.

## 3. Explicit non-ownership boundaries

- Role/capability identity itself.
- Process sequencing.
- Change object/delta.
- Evidence object/provenance.
- Technical/domain facts or acceptance criteria.
- Secrets/credentials as canonical content.

## 4. Consumed contracts / referenced owners

Consumed contract != shared ownership.
- `ROLE/CAPABILITY`
- `EVID`
- `PROCESS`
- `CHANGE`
- `EXTERNAL-ADAPTER`
- `AIF/EVAL`
- `applicable domain/TECH owners`

## 5. Proposed invariants

- Capability != authority.
- Role/job title != authority automatically.
- Declared tool/plugin capability or permission is not itself an authorization grant.
- Recommendation != authorization.
- Authorization to execute != verification or acceptance of result.
- Authority must be bounded, revocable where applicable, and attributable to a competent source.

## 6. Authority boundary

`AUTH` semantic ownership does not identify or grant the competent human authority required for ACCEPTED/CURRENT. Authority for future acceptance must be explicitly recorded and remains separate from semantic ownership.

## 7. Identity / version boundary

`contracts/AUTH.md` is the physical Git locator of this proposed first formalization, not a canonical ID. Version `0.1.0-CONTEMPORARY-PROPOSED` is a proposal version. Neither establishes CANONICAL, ACCEPTED or CURRENT.

## 8. Verification boundary

The proposal must pass G1-M0 boundary/adversarial tests and diff review. Passing those tests verifies only the documentary/semantic scope being tested; it does not verify operational implementation.

## 9. Open items / fail-closed conditions

- Named human/organizational authority matrix remains separate and may still be RECOVERY_REQUIRED; this contract must not invent people or titles.
- Effective Tool Authorization / execution-path verification remains a separately approved TRUE DELTA for a later wave; G1-M0 does not absorb it into this foundation.
- Any material conflict with a narrower owner-specific contract discovered later blocks promotion until reconciled.
- No new registry/schema/DDL/owner/domain/engine/lifecycle may be inferred from this proposal.

## 10. Promotion conditions

Before ACCEPTED/CURRENT can ever be considered: source/provenance, semantic owner subject, competent authority, target identity/version, delta, review, applicable verification evidence and supersession/currentness treatment must be explicit under existing governance.
