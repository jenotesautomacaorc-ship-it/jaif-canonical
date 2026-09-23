# JAIF — EVID OWNER-SPECIFIC CONTRACT — CONTEMPORARY FIRST FORMALIZATION — PROPOSAL v0.1

**Frozen baseline:** `main@3a38a354bcbb1440da5c749c757fc5b91da0bc7e`
**Git locator:** `contracts/EVID.md`
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
- Recovered LCM owner evidence states EVID owns evidence/provenance/capture context.
- EVID does not own the represented fact/rule.
- HKR requires evidence and provenance as distinct traceable links and prohibits treating inventory/status as the event itself.

Phase10 routing evidence: **31 primary claims** and **123 consumer references** involve `EVID`.
Primary claim IDs: W10D-CLM-022, W10D-CLM-024, W10D-CLM-025, W10D-CLM-049, W10D-CLM-058, W10D-CLM-062, W10D-CLM-064, W10D-CLM-066, W10D-CLM-074, W10D-CLM-079, W10D-CLM-089, W10D-CLM-098, W10D-CLM-103, W10D-CLM-107, W10D-CLM-108, W10D-CLM-112, W10D-CLM-116, W10D-CLM-117, W10D-CLM-124, W10D-CLM-130, W10D-CLM-138, W10D-CLM-140, W10D-CLM-141, W10D-CLM-162, W10D-CLM-171, W10D-CLM-176, W10D-CLM-177, W10D-CLM-179, W10D-CLM-181, W10D-CLM-183, W10D-CLM-192
Post-cutoff G1 bundles routed here: G1-WB-001, G1-WB-002, G1-WB-003, G1-WB-005, G1-WB-006, G1-WB-007, G1-WB-008, G1-WB-009, G1-WB-010, G1-WB-011, G1-WB-012, G1-WB-014, G1-WB-015, G1-WB-016, G1-WB-017, G1-WB-018, G1-WB-019, G1-WB-020, G1-WB-021, G1-WB-022, G1-WB-023, G1-WB-024, G1-WB-025, G1-WB-026, G1-WB-027, G1-WB-028, G1-WB-029, G1-WB-030, G1-WB-031

## 2. Proposed semantic subject owned

- Evidence object identity and its provenance/capture context.
- Source/reference linkage, acquisition method, transformation/redaction lineage, timestamps/freshness where applicable, integrity/limitations and trace links.
- Evidence-chain semantics connecting observation/output/result to the claim/event it supports or refutes.

## 3. Explicit non-ownership boundaries

- The represented technical/domain fact.
- The source author's semantic ownership.
- Interpretation/decision merely because evidence is stored.
- Authority to accept/promote.
- Quality criterion or test specification.
- Change identity/delta.

## 4. Consumed contracts / referenced owners

Consumed contract != shared ownership.
- `applicable source/domain owners`
- `QUALITY`
- `AUTH`
- `PROCESS`
- `CHANGE`
- `DOCUMENT/VIEW`

## 5. Proposed invariants

- Evidence != truth by existence.
- Evidence != represented fact.
- Evidence != acceptance.
- Evidence transformations must remain traceable.
- Missing/weak provenance blocks dependent claims rather than being silently repaired.
- A view/dashboard/render can reference evidence but does not become evidence of physical state merely by rendering it.

## 6. Authority boundary

`EVID` semantic ownership does not identify or grant the competent human authority required for ACCEPTED/CURRENT. Authority for future acceptance must be explicitly recorded and remains separate from semantic ownership.

## 7. Identity / version boundary

`contracts/EVID.md` is the physical Git locator of this proposed first formalization, not a canonical ID. Version `0.1.0-CONTEMPORARY-PROPOSED` is a proposal version. Neither establishes CANONICAL, ACCEPTED or CURRENT.

## 8. Verification boundary

The proposal must pass G1-M0 boundary/adversarial tests and diff review. Passing those tests verifies only the documentary/semantic scope being tested; it does not verify operational implementation.

## 9. Open items / fail-closed conditions

- Exact machine-readable evidence schema remains outside G1-M0 and must not be invented here.
- Any material conflict with a narrower owner-specific contract discovered later blocks promotion until reconciled.
- No new registry/schema/DDL/owner/domain/engine/lifecycle may be inferred from this proposal.

## 10. Promotion conditions

Before ACCEPTED/CURRENT can ever be considered: source/provenance, semantic owner subject, competent authority, target identity/version, delta, review, applicable verification evidence and supersession/currentness treatment must be explicit under existing governance.
