# JAIF — CHANGE OWNER-SPECIFIC CONTRACT — CONTEMPORARY HARDENING REVISION — PROPOSAL v0.2

**Frozen baseline:** `main@34ee5c49a84fa71473ac1059c9468f8ff2304aae`
**Git locator:** `contracts/CHANGE.md`
**Proposed version:** `0.2.0-CONTEMPORARY-PROPOSED`
**Status:** PROPOSED — NON-CANONICAL — NON-ACCEPTED — NON-CURRENT
**Canonical ID:** NOT_ASSIGNED
**Contemporary relation:** REVISION_OF_G1_M0_PROPOSED_FIRST_FORMALIZATION; NO HISTORICAL PREDECESSOR/SUCCESSOR CLAIM
**DDL / PostgreSQL / runtime:** NOT APPLICABLE TO THIS DOCUMENTAL FORMALIZATION

## 1. Provenance and basis

This is a proposed contemporary hardening revision of the G1-M0 first formalization of the `CHANGE` semantic owner. It carries forward the G1-M0 owner boundary and adds only the G1-M1 change-control hardening residuals that G1-M0 explicitly left open.

Controlled references for this proposed revision:
- [G1-M1 change-control hardening evidence](../evidence/G1-M1-CHANGE-CONTROL-HARDENING-EVIDENCE.md)
- [G1-M1 change hardening tests](../tests/G1-M1-CHANGE-HARDENING-TESTS.md)
- [G1-M0 target-binding evidence](../evidence/G1-M0-TARGET-BINDING-EVIDENCE.md)
- [G1-M0 owner-boundary tests](../tests/G1-M0-OWNER-BOUNDARY-TESTS.md)
- [Canonical governance](../governance/CANONICAL-GOVERNANCE.md)
- [HKR non-omission gate](../governance/HKR-NON-OMISSION-GATE.md)
- [Change control](../governance/CHANGE-CONTROL.md)

G1-M0 established that `CHANGE` owns controlled-change semantics and explicitly deferred to G1-M1:
- Minimum Necessary Change;
- downstream dependency coverage;
- blast-radius treatment;
- rollback/reversibility treatment;
- fail-closed behavior when material impact or reversibility remains unknown.

This revision is not a recovered historical contract and does not claim historical continuity that has not been proven.

## 2. Proposed semantic subject owned

`CHANGE` owns:
- controlled change identity and bounded delta against an identified baseline;
- target reference, scope, semantic-change classification, materiality/impact references and supersession/version linkage for the change subject;
- the constraint that a proposed change set contains no more change than is necessary to satisfy the declared objective and its demonstrated necessary dependencies;
- impact/dependency coverage needed to bound the change set;
- blast-radius representation for the change subject;
- rollback/reversal/irreversibility representation for the change subject;
- links to decision, implementation, evidence and verification records without taking ownership of those external semantics.

## 3. Explicit non-ownership boundaries

`CHANGE` does not own:
- authority to approve, execute, waive, accept or promote (`AUTH` / competent human authority);
- evidence/provenance object semantics (`EVID`);
- quality, test, inspection, commissioning or acceptance criteria (`QUALITY`);
- process sequencing outside the controlled-change subject (`PROCESS`);
- the underlying technical/domain fact being changed;
- role/capability identity;
- secrets/credentials;
- a new umbrella owner, engine, lifecycle or source of truth.

Consumed contract != shared ownership.

## 4. Consumed contracts / referenced owners

- `AUTH`
- `EVID`
- `QUALITY`
- `PROCESS`
- `DOCUMENT/VIEW`
- applicable domain/TECH owners
- applicable consumer/dependency owners

A dependency or consumer reference does not transfer semantic ownership to `CHANGE`.

## 5. Proposed invariants

- Discussion/proposal != change implementation.
- Approval != implementation.
- Implementation != verification.
- Change document/diff != authority.
- Stale-base change cannot be applied as if current without reconciliation.
- Change must preserve semantic traceability and explicit target identity.
- Small diff != low materiality.
- Documentation-only != semantically immaterial automatically.
- Newer version != ACCEPTED/CURRENT.
- A rollback plan != verified rollback capability.
- Reversibility != authorization.
- Unknown material dependency, impact or reversibility fails closed.

## 6. Minimum Necessary Change

A change set must be no larger than necessary to satisfy:
1. the explicitly declared change objective; and
2. dependencies demonstrated as necessary to achieve that objective safely and coherently.

Each material changed path/subject must be attributable to the objective or to a documented necessary dependency.

Unrelated cleanup, opportunistic refactoring, convenience edits, taxonomy changes or adjacent feature work are outside the change unless separately justified and authorized.

If an unrelated delta can be separated without defeating the authorized objective, it must be split into a separate change.

`Minimum Necessary Change` is a constraint on change scope. It does not authorize execution and does not replace materiality review.

## 7. Dependency coverage and impact boundary

For a material change, the change record must identify, to the extent applicable:
- direct dependencies required by the target;
- known downstream consumers materially affected by the delta;
- owner/contract boundaries crossed by the change;
- artifacts or operational surfaces whose meaning or behavior may change;
- known conflicts, stale assumptions and unresolved dependency questions.

Absence of a known dependency is not proof that no dependency exists.

If a material dependency or consumer relationship is reasonably expected but cannot be determined with sufficient evidence, dependent implementation or promotion remains blocked.

Dependency coverage is evidence-bounded and must not be represented as globally complete unless the reviewed universe and search/reconciliation method justify that claim.

## 8. Blast radius

A material change must state its bounded blast radius: what is intended to change, what may be affected, and what is explicitly outside scope.

Blast radius is an impact representation of the change subject. It is not a new owner, domain, engine, registry or lifecycle.

A narrow file diff does not by itself prove a narrow semantic or operational blast radius.

Where impact crosses owner boundaries, the applicable owners remain authoritative for their own semantic subjects.

## 9. Rollback, reversibility and irreversibility

For a material change, reversibility must be explicitly classified as one of:
- reversible with a defined rollback/reversal path;
- intentionally irreversible with explicit rationale, competent authority and mitigation/containment;
- not applicable, with justification;
- NOT_VERIFIED / unknown, which blocks dependent implementation or promotion when reversibility is material.

Where rollback is applicable, the change record must identify:
- the rollback/reversal target or prior state;
- preconditions and dependencies needed for rollback;
- material data/state loss or compatibility consequences;
- evidence that the rollback method is technically plausible;
- verification status of the rollback method.

A documented rollback plan is not proof that rollback will work.

An untested or unverified rollback path must remain `NOT_VERIFIED`.

## 10. Fail-closed conditions

The change remains blocked from dependent implementation/promotion when any of the following is material and unresolved:
- objective or target identity is ambiguous;
- baseline is stale or uncertain;
- unexplained delta exists;
- required dependency coverage is materially incomplete;
- blast radius cannot be bounded sufficiently;
- reversibility/irreversibility is materially unknown;
- rollback requirements are applicable but not defined;
- owner/authority conflict remains unresolved;
- evidence needed for the intended claim is missing.

Fail-closed treatment is a control response, not a new governance state.

## 11. Authority boundary

`CHANGE` semantic ownership does not grant competent human authority.

The authority to approve scope, accept irreversibility, authorize implementation, waive a control, promote `ACCEPTED` or designate `CURRENT` remains separate and must be explicitly recorded under `AUTH` and applicable governance.

## 12. Identity / version boundary

`contracts/CHANGE.md` is the physical Git locator of this proposed revision, not a canonical ID.

Version `0.2.0-CONTEMPORARY-PROPOSED` identifies this proposal revision only.

It does not establish CANONICAL, ACCEPTED, CURRENT, implemented runtime state or historical succession.

## 13. Verification boundary

The proposal must pass G1-M1 change-hardening tests and complete diff review against the exact baseline/head under review.

Passing those documentary/semantic tests verifies only the tested proposal scope.

It does not prove:
- production/runtime implementation;
- operational behavior;
- physical commissioning;
- rollback execution in a real target;
- acceptance;
- CURRENT designation.

## 14. Open items / later-wave boundary

G1-M1 does not create a machine-readable change schema, new registry, new owner, new engine, new lifecycle or PostgreSQL/DDL target.

If later implementation requires machine-readable fields, workflow automation, execution-path enforcement or runtime observability, those are separately authorized deltas and must reuse these semantics rather than duplicate them.

Any material conflict with a narrower owner-specific contract discovered later blocks promotion until reconciled.

## 15. Promotion conditions

Before ACCEPTED/CURRENT can ever be considered, the applicable chain must make explicit:
source/provenance, owner subject, competent authority, exact target identity/version, baseline, minimum necessary delta, materiality, dependency/impact coverage, blast radius, reversibility treatment, decision, implementation evidence, verification evidence and supersession/currentness treatment.

No step is automatic.
