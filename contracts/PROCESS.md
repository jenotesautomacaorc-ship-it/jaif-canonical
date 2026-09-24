# JAIF — PROCESS OWNER-SPECIFIC CONTRACT — CONTEMPORARY FIRST FORMALIZATION — PROPOSAL v0.1

**Frozen baseline:** `main@3a38a354bcbb1440da5c749c757fc5b91da0bc7e`
**Git locator:** `contracts/PROCESS.md`
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
- PROCESS exists as an owner key/scope in recovered PREDDL/LCM owner evidence.
- Process Owner != Semantic Data Owner != Document Owner != Custodian != Authority automatically.
- PROCESS binding cannot be inferred merely because a document describes a procedure.

Phase10 routing evidence: **11 primary claims** and **12 consumer references** involve `PROCESS`.
Primary claim IDs: W10D-CLM-034, W10D-CLM-037, W10D-CLM-063, W10D-CLM-065, W10D-CLM-072, W10D-CLM-080, W10D-CLM-082, W10D-CLM-092, W10D-CLM-150, W10D-CLM-182, W10D-CLM-185
Post-cutoff G1 bundles routed here: G1-WB-002, G1-WB-003, G1-WB-005, G1-WB-006, G1-WB-007, G1-WB-012, G1-WB-013, G1-WB-014, G1-WB-015, G1-WB-024, G1-WB-025

## 2. Proposed semantic subject owned

- Identity and semantics of a governed process/procedure when explicitly typed as PROCESS.
- Process structure: stages/activities, sequencing, handoffs, entry/exit conditions, waiting/exception paths and required process checkpoints.
- References to required outputs/artifacts, evidence, authority and quality gates without taking ownership of those referenced subjects.

## 3. Explicit non-ownership boundaries

- Authority, consent, permission or approval semantics (AUTH).
- Evidence/provenance/capture semantics (EVID).
- Quality/test/verification criteria semantics (QUALITY).
- Controlled delta/baseline/change identity (CHANGE).
- Technical/domain facts, domain states, document/view identity or role/capability identity.

## 4. Consumed contracts / referenced owners

Consumed contract != shared ownership.
- `AUTH`
- `QUALITY`
- `EVID`
- `CHANGE`
- `ROLE/CAPABILITY`
- `DOCUMENT/VIEW`
- `applicable domain/TECH owners`

## 5. Proposed invariants

- Process step or gate existence does not grant authority.
- Process completion does not prove verification, acceptance, CURRENT or operational success.
- A process may require evidence but cannot redefine the represented fact.
- A process may route a change but cannot become the semantic owner of the changed domain fact.

## 6. Authority boundary

`PROCESS` semantic ownership does not identify or grant the competent human authority required for ACCEPTED/CURRENT. Authority for future acceptance must be explicitly recorded and remains separate from semantic ownership.

## 7. Identity / version boundary

`contracts/PROCESS.md` is the physical Git locator of this proposed first formalization, not a canonical ID. Version `0.1.0-CONTEMPORARY-PROPOSED` is a proposal version. Neither establishes CANONICAL, ACCEPTED or CURRENT.

## 8. Verification boundary

The proposal must pass G1-M0 boundary/adversarial tests and diff review. Passing those tests verifies only the documentary/semantic scope being tested; it does not verify operational implementation.

## 9. Open items / fail-closed conditions

- Exact authority competent to accept/promote the first PROCESS contract remains to be recorded at materialization review.
- Any material conflict with a narrower owner-specific contract discovered later blocks promotion until reconciled.
- No new registry/schema/DDL/owner/domain/engine/lifecycle may be inferred from this proposal.

## 10. Promotion conditions

Before ACCEPTED/CURRENT can ever be considered: source/provenance, semantic owner subject, competent authority, target identity/version, delta, review, applicable verification evidence and supersession/currentness treatment must be explicit under existing governance.
