# G1-M1 — Change-Control Hardening Evidence — PREPARATION v0.1

**Status:** PROPOSED EVIDENCE RECORD — NON-CANONICAL — NON-ACCEPTED — NON-CURRENT
**Frozen baseline:** `main@34ee5c49a84fa71473ac1059c9468f8ff2304aae`
**Planned branch:** `change/g1-m1-change-control-hardening-v0.1`
**Canonical ID:** NOT_ASSIGNED
**Historical relation:** CONTEMPORARY PREPARATION EVIDENCE; NOT A RECOVERED HISTORICAL SOURCE
**DDL / PostgreSQL / Notion / n8n / runtime:** NONE AUTHORIZED OR CLAIMED

## 1. Preparation authorization boundary

The current human instruction authorizes preparation of the G1-M1 change-control hardening package following successful G1-M0 materialization.

This preparation authorization permits:
- freezing the post-G1-M0 `main` as the working baseline;
- defining the bounded G1-M1 semantic delta;
- preparing exact candidate artifacts outside `main`;
- preparing a new non-`main` branch and preflight procedure.

It does not, by itself, grant:
- ACCEPTED;
- CURRENT;
- DDL/PostgreSQL/Notion/n8n/runtime mutation;
- automatic staging, commit, push, PR or merge;
- modification of PR #8;
- G1-M2+ materialization.

Any Git publication step remains separately fail-closed against exact hashes, diff and current remote state.

## 2. Baseline facts

Post-G1-M0 baseline:
`main@34ee5c49a84fa71473ac1059c9468f8ff2304aae`

At this baseline:
- G1-M0 has been merged by controlled merge commit;
- `contracts/CHANGE.md` exists as `0.1.0-CONTEMPORARY-PROPOSED`;
- its open-items section explicitly routes Minimum Necessary Change, downstream dependency coverage, blast radius and rollback/reversibility residuals to G1-M1;
- `governance/CHANGE-CONTROL.md` remains the bootstrap workflow control and is consumed as a reference.

G1-M1 must not reinterpret the G1-M0 merge as ACCEPTED/CURRENT.

## 3. Exact G1-M1 semantic objective

Harden the `CHANGE` owner-specific proposal so that a material change cannot silently:
- include unrelated delta;
- ignore materially relevant dependencies/consumers;
- understate blast radius;
- claim reversibility without a bounded rollback/reversal treatment;
- proceed when material impact or reversibility remains unknown.

This objective is deliberately narrower than general process governance.

## 4. Proposed exact materialization set

The minimum proposed Git delta is exactly:

1. modify `contracts/CHANGE.md`;
2. add `evidence/G1-M1-CHANGE-CONTROL-HARDENING-EVIDENCE.md`;
3. add `tests/G1-M1-CHANGE-HARDENING-TESTS.md`.

No other path is required to express this semantic delta at preparation time.

In particular, `governance/CHANGE-CONTROL.md` is **not** modified in this minimum set. It consumes `CHANGE` semantics but is not used as a duplicate semantic owner.

If later review proves an irreducible process-control gap, that must be handled as an explicit separately justified delta rather than silently copied here.

## 5. Minimum Necessary Change rationale

This three-path proposal is the smallest bounded set that can:
- carry the owner-specific semantic revision;
- record why the revision exists and what it does not authorize;
- specify adversarial tests for the new invariants.

Adding unrelated governance, registry, schema, runtime, AI, DDL or domain files would violate the G1-M1 objective unless separately proven necessary.

## 6. New semantic delta

The proposed true delta relative to G1-M0 is limited to:
- Minimum Necessary Change;
- objective-to-delta traceability;
- materially relevant dependency/consumer coverage;
- bounded blast-radius representation;
- explicit rollback/reversibility/irreversibility treatment;
- fail-closed handling of unknown material impact or reversibility.

Existing G1-M0 invariants remain in force.

## 7. Non-overlap boundary

- `CHANGE` owns change-scope/delta/impact/reversibility representation.
- `AUTH` owns approval/authorization/waiver/acceptance authority.
- `EVID` owns evidence/provenance semantics.
- `QUALITY` owns verification/test/conformance criteria where applicable.
- `PROCESS` owns workflow/sequence/handoff semantics.
- applicable TECH/domain owners retain the underlying technical facts.

Impact references and dependency links do not create shared semantic ownership.

## 8. Explicit anti-proliferation rules

G1-M1 must not create:
- a `Change Engine`;
- an `Impact Engine`;
- a rollback owner;
- a dependency owner;
- a sixth PRE-DDL gate;
- a new governance state;
- a new source of truth;
- a new registry merely to hold these concepts.

The required complexity belongs once in `CHANGE` and is consumed by other controls.

## 9. Verification requirements

Before any publication/merge decision, the exact candidate diff must demonstrate:
- only the authorized three paths;
- no silent G1-M2+ absorption;
- no ACCEPTED/CURRENT inference;
- no runtime/DDL inference;
- no overlap with AUTH/EVID/QUALITY/PROCESS/TECH owners;
- G1-M1 adversarial tests pass against the exact commit/diff under review;
- existing repository CI passes.

## 10. Holds

- Human/organizational acceptance authority remains separate.
- Canonical ID remains NOT_ASSIGNED.
- G1-M2+ remains non-materialized.
- PR #8 remains independent.
- Runtime/DDL/PostgreSQL/Notion/n8n remains unauthorized.
- Public-repository confidentiality remains a publication-time control.
- Preparation does not equal implementation, verification, acceptance or currentness.
