# JAIF — PROCESS OWNER-SPECIFIC CONTRACT — CONTEMPORARY INTEGRATED-EXPERIENCE REVISION — PROPOSAL v0.2

**Frozen baseline:** `main@97519dd1bc000422e6d7e9984dd25f97e626c141`
**Git locator:** `contracts/PROCESS.md`
**Proposed version:** `0.2.0-CONTEMPORARY-PROPOSED`
**Status:** PROPOSED — NON-CANONICAL — NON-ACCEPTED — NON-CURRENT
**Canonical ID:** NOT_ASSIGNED
**Contemporary relation:** REVISION_OF_G1_M0_PROPOSED_FIRST_FORMALIZATION; NO HISTORICAL PREDECESSOR/SUCCESSOR CLAIM
**DDL / PostgreSQL / runtime:** NOT APPLICABLE TO THIS DOCUMENTAL FORMALIZATION

## 1. Provenance and basis

This is a proposed contemporary revision of the G1-M0 first owner-specific formalization of `PROCESS`.

It preserves the G1-M0 owner boundary and adds only the process semantics required to represent Integrated Experience Engineering and Design-to-Evidence as a transversal enterprise capability.

Controlled references for this proposed revision:
- [G1-M2 integrated-experience evidence](../evidence/G1-M2-INTEGRATED-EXPERIENCE-ENGINEERING-EVIDENCE.md)
- [G1-M2 integrated-experience tests](../tests/G1-M2-INTEGRATED-EXPERIENCE-TESTS.md)
- [G1-M0 target-binding evidence](../evidence/G1-M0-TARGET-BINDING-EVIDENCE.md)
- [G1-M0 owner-boundary tests](../tests/G1-M0-OWNER-BOUNDARY-TESTS.md)
- [G1-M1 change-control hardening evidence](../evidence/G1-M1-CHANGE-CONTROL-HARDENING-EVIDENCE.md)
- [Canonical governance](../governance/CANONICAL-GOVERNANCE.md)
- [HKR non-omission gate](../governance/HKR-NON-OMISSION-GATE.md)
- [Change control](../governance/CHANGE-CONTROL.md)
- [Change contract](CHANGE.md)
- [Quality contract](QUALITY.md)
- [Evidence contract](EVID.md)
- [Authority contract](AUTH.md)
- [Observability lineage](OBSERVABILITY-LINEAGE.md)
- [PRE-DDL gates](PRE-DDL-GATES.md)

Carried-forward G1-M0 supporting statements:
- `PROCESS` exists as an owner key/scope in recovered PREDDL/LCM owner evidence.
- Process Owner != Semantic Data Owner != Document Owner != Custodian != Authority automatically.
- PROCESS binding cannot be inferred merely because a document describes a procedure.
- The G1-M0 source routing recorded 11 primary PROCESS claims and 12 consumer references.
- G1-M0 primary claim IDs: W10D-CLM-034, W10D-CLM-037, W10D-CLM-063, W10D-CLM-065, W10D-CLM-072, W10D-CLM-080, W10D-CLM-082, W10D-CLM-092, W10D-CLM-150, W10D-CLM-182, W10D-CLM-185.
- G1-M0 post-cutoff bundles routed to PROCESS: G1-WB-002, G1-WB-003, G1-WB-005, G1-WB-006, G1-WB-007, G1-WB-012, G1-WB-013, G1-WB-014, G1-WB-015, G1-WB-024, G1-WB-025.

These statements are carried forward to prevent the G1-M2 revision from erasing the provenance basis of the first formalization.

This revision is not a reconstruction of an unavailable historical PROCESS contract and does not claim historical continuity that has not been proven.

## 2. Proposed semantic subject owned

`PROCESS` owns:
- identity and semantics of a governed process/procedure when explicitly typed as PROCESS;
- process stages/activities, sequencing, handoffs, entry/exit conditions, waiting/exception paths and required process checkpoints;
- process-level obligations that required coverage checkpoints and unresolved gaps are explicit, without taking ownership of quality criteria or evidence semantics;
- references to required artifacts, evidence, authority, quality gates and applicable technical owners without taking ownership of those referenced subjects.

## 3. Explicit non-ownership boundaries

`PROCESS` does not own:
- authority, consent, permission, approval and acceptance-decision/authorization semantics (`AUTH`);
- evidence/provenance/capture semantics (`EVID`);
- quality/test/verification/commissioning/acceptance criteria semantics (`QUALITY` or narrower TECH owner);
- controlled delta/baseline/change identity (`CHANGE`);
- underlying technical/domain facts, calculations, simulation models or acceptance values;
- document/view/representation identity;
- role/capability identity;
- a new Integrated Experience owner, Design Engine, Option Engine, Coverage Engine, lifecycle, domain or source of truth.

Consumed contract != shared ownership.

## 4. Consumed contracts / controlled references

- `AUTH`
- `QUALITY`
- `EVID`
- `CHANGE`
- `DOCUMENT/VIEW`
- `ROLE/CAPABILITY`
- controlled reference: `OBSERVABILITY-LINEAGE`
- applicable domain/TECH owners
- applicable consumer/dependency owners

References or handoffs do not transfer semantic ownership to `PROCESS`.

## 5. Proposed invariants

- Process step or gate existence does not grant authority.
- Process completion does not prove verification, acceptance, CURRENT or operational success.
- A process may require evidence but cannot redefine the represented fact.
- A process may route a change but cannot become the semantic owner of the changed domain fact.
- Intention != requirement.
- Recommendation != decision.
- Decision != authorization unless the competent authority and scope explicitly establish them as the same recorded event.
- Authorization != execution.
- Execution != verification.
- Commissioning/verification != acceptance.
- Applicable evidence must exist before an evidence-dependent acceptance can be granted.
- Acceptance != CURRENT.
- Specialized calculation/simulation output != acceptance or truth by existence.
- Render/view/dashboard/Passport != physical truth by existence.
- Unknown material owner, dependency, authority or coverage fails closed for the dependent handoff.
- This process chain does not replace the HKR non-omission chain or create a parallel governance lifecycle.
- The existing five PRE-DDL gates remain the only PRE-DDL gates; G1-M2 creates no sixth gate.

## 6. Integrated Experience Engineering — enterprise competence and PROCESS semantics

Integrated Experience Engineering is a transversal enterprise competence of JAIF.

This `PROCESS` contract formalizes only the process semantics needed to coordinate that competence. The competence itself is not promoted into an umbrella semantic owner.

It coordinates the end-to-end movement from human intention to an evidenced, operable and evolvable result while consuming the contracts and semantics of existing owners without transferring ownership or authority.

It is not:
- a semantic owner;
- an umbrella technical domain;
- an Engine;
- a parallel lifecycle;
- a database;
- a source of truth;
- an authority to approve technical, commercial, financial, legal or acceptance decisions.

The process may coordinate multiple owners and tools while each subject remains owned by its applicable contract/domain owner.

## 7. Governed end-to-end chain

Material inputs may include intention, context, preference and need, each retaining provenance where applicable.

The governed process chain is:

`{intention, context, preference, need} → requirements → multidisciplinary coordination/compatibility → alternatives → specialized calculation/simulation → recommendation → decision → authorization where required → project/materialization → deterministic execution → commissioning/verification → evidence → acceptance where required → Passport/controlled evidence view → operation/observability → lifecycle/evolution`

The braces identify an input set; they do not assert that intention, context, preference and need are semantically equivalent.

This chain is a process-ordering and handoff model. It is not:
- a governance state machine;
- an ownership map;
- a replacement for the HKR chain `SOURCE → CLAIM → EVIDENCE → PROVENANCE → INTERPRETATION → MATERIALITY → OWNER → DELTA → DECISION → TARGET → IMPLEMENTATION → VERIFICATION → CLOSURE`.

Evidence may be generated throughout the chain. Its placement immediately before acceptance in the linear representation means only that evidence required to support an acceptance must be available before that acceptance; it does not imply that evidence starts there.

For each material handoff, the process must make explicit, where applicable:
- input identity/version;
- output/deliverable identity;
- applicable semantic owner;
- responsible execution surface or tool;
- authority required for the next material action;
- evidence/provenance required for the claim being carried forward;
- unresolved material dependencies, conflicts or assumptions;
- entry/exit condition for the handoff.

A stage cannot silently fill a missing material output from a prior stage by inference.

## 8. Requirements, context/preference provenance and multidisciplinary compatibility

Human intention, context, preference and need may initiate or influence the process, but they do not become technical requirements automatically.

When context or preference materially contributes to a requirement, recommendation or decision, its provenance must remain traceable under the existing `Context Provenance` and `Preference Provenance` PRE-DDL gates where applicable.

G1-M2 does not modify, replace or add to the five PRE-DDL gates.

Where applicable, all five existing PRE-DDL controls remain governing:
- Context Provenance;
- Preference Provenance;
- Decision Authority;
- AI→Execution Lineage;
- Cross-domain Ownership.

A requirement entering multidisciplinary coordination must retain its source/provenance and applicable owner.

Coordination must identify materially affected disciplines/consumers and preserve their boundaries.

If an applicable technical owner/routing is materially required but not sufficiently identified, the dependent coordination handoff remains blocked rather than inventing a cross-domain owner.

Multidisciplinary coordination may detect a conflict but cannot resolve semantic precedence merely because the conflict was detected.

## 9. Alternatives and Design-to-Evidence

Before a material recommendation or authorization, materially distinct alternatives must be represented when alternatives are relevant to the decision.

For each material alternative, the process must require traceable references, where applicable, to:
- objective/requirement addressed;
- assumptions and constraints;
- input/version basis;
- specialized tool/calculation/simulation used;
- result and material trade-offs;
- limitations/uncertainties;
- applicable owner;
- evidence supporting the comparison.

The process owns the requirement that alternatives are traceably compared; it does not own the technical truth of the calculations or the decision authority.

Recommendation is not decision.

A preferred option is not authorized merely because it ranks better under a model or recommendation.

## 10. Specialized calculation, simulation and representation boundary

Specialized software may calculate, simulate or materialize outputs within its competence.

The process must preserve the link from requirements/assumptions to the specialized result and onward to the decision that consumes it.

A generic AI output, render, diagram, view or narrative is not a substitute for a specialized calculation or verification when the claim requires one.

Representation may explain an option or result but does not become evidence of physical state merely by being visually persuasive.

Cross-tool disagreement that is material to a handoff must remain explicit and blocks dependent progression until disposition under the applicable owners/authority. This section does not define the future Semantic Diff mechanism.

## 11. Decision, authorization and deterministic execution boundary

Decision and authorization are separate events unless a competent authority explicitly records a bounded decision that also constitutes the required authorization.

Where material responsibility, risk or accountability requires human authority, the process must stop at the authorization boundary until competent authorization is explicit.

Interpretive or probabilistic tooling may prepare plans, options, comparisons or recommendations.

Material execution must use a bounded, attributable and verifiable execution path appropriate to the target and authorization.

This requirement does not designate ASTRA, any LLM, Computer Use, API, script, adapter or vendor platform as the executor. Tool/runtime execution semantics remain outside G1-M2.

## 12. Commissioning, evidence, verification and acceptance separation

The process must keep distinct:
- execution of the intended change;
- technical test/inspection/commissioning and applicable verification against governing criteria;
- evidence of those results;
- human acceptance where required;
- governance promotion/currentness.

A successful execution does not prove verification.
A successful test/commissioning result does not itself grant acceptance.
An evidence-dependent acceptance cannot be granted before the applicable evidence exists and is available to the competent authority.
Acceptance does not itself establish CURRENT.

Criteria remain with `QUALITY` or the applicable narrower TECH owner; evidence remains with `EVID`; acceptance authority remains with `AUTH` / competent human authority.

## 13. Continuous coverage and fail-closed handoffs

For each material requirement in scope, the process must be able to determine whether there is an applicable downstream:
- deliverable/materialization target;
- implementation/execution step where applicable;
- verification/test/commissioning criterion where applicable;
- evidence requirement;
- acceptance condition where applicable;
- closure condition where applicable.

Missing required coverage is a visible gap, not an implicit PASS.

Accepted constraints must remain traceable through dependent handoffs; propagation does not transfer ownership.

`PROCESS` owns the requirement that the coverage checkpoint exists and that a missing required link remains visible. `QUALITY` owns applicable conformance criteria; `EVID` owns evidence/provenance semantics; applicable domain owners own their represented facts.

This does not create a Coverage Engine or independent source of truth.

## 14. Evidence, Passport and representation boundary

Evidence may be required throughout the chain; it is not only a final-stage artifact.

`PROCESS` may require evidence at a handoff, but `EVID` owns evidence/provenance semantics.

A Passport or other controlled evidence view may aggregate references for human use, but the view does not become physical truth, evidence merely by presentation, or owner of represented facts.

A missing/weak material evidence link blocks dependent claims according to applicable governance.

## 15. Operation, observability and lifecycle continuity

Where the delivered result proceeds into operation, the process hands off to the existing observability/lineage controls and applicable domain owners.

Operational signals, state, anomaly, decision, action and evidence remain subject to the controlled `OBSERVABILITY-LINEAGE` reference and narrower owner semantics.

Evolution after an accepted baseline must route material changes through `CHANGE`; lifecycle continuity does not permit silent semantic mutation.

## 16. Explicit later-wave boundary

G1-M2 does not materialize or decide:
- ASTRA governed orchestration;
- Tool/Capability Contracts;
- Minimum Intelligence Necessary;
- concrete Semantic Diff implementation;
- Technology Admission;
- Edge/adapter execution semantics;
- MQTT/ESP-NOW/ABB/BACnet/WhatsApp integration specifics;
- Electrical or Network/IP foundation non-degradation;
- Productization/Value Packaging;
- Pre-Diagnosis/Radar/client journey;
- renders/Digital Showroom/Visual Evidence product surfaces;
- AV or Lighting discipline contracts;
- PostgreSQL schema/DDL;
- Notion/n8n/runtime automation;
- physical commissioning or operational implementation.

Those items remain separate controlled waves/targets.

## 17. Authority boundary

`PROCESS` semantic ownership does not identify or grant the competent human authority required for ACCEPTED/CURRENT.

The exact competent authority for a future acceptance/promotion of this PROCESS revision remains to be explicitly recorded. It is not inferred from authorship, ownership, Git access, review participation or tool execution.

## 18. Identity / version boundary

`contracts/PROCESS.md` is the physical Git locator of this proposed revision, not a canonical ID.

Version `0.2.0-CONTEMPORARY-PROPOSED` identifies this proposal revision only.

It does not establish CANONICAL, ACCEPTED, CURRENT, implemented runtime state or historical succession.

## 19. Verification boundary

The proposal must pass the G1-M2 integrated-experience adversarial tests and complete diff review against the exact baseline/head under review.

The applicable G1-M0 owner-boundary/adversarial requirements remain in force. The G1-M2 suite supplements them; it does not supersede, weaken or reinterpret them.

Passing those documentary/semantic tests verifies only the tested proposal scope.

It does not prove:
- production/runtime implementation;
- specialized technical correctness in a real project;
- physical commissioning;
- operational performance;
- real-target rollback;
- acceptance;
- CURRENT designation.

## 20. Open items / fail-closed conditions

- Exact discipline-specific TECH contracts/bindings remain required before claims that depend on those disciplines can be promoted or executed.
- Exact `DOCUMENT/VIEW` owner-specific contract/binding is not created by this revision.
- Exact `ROLE/CAPABILITY` owner-specific contract/binding is not created by this revision; references do not imply binding or authority.
- Tool/runtime orchestration remains a later-wave concern.
- Any material conflict with a narrower owner-specific contract discovered later blocks dependent progression until reconciled.
- No new registry/schema/DDL/owner/domain/engine/lifecycle may be inferred from this proposal.
- Repository-language harmonization is not performed here; changing the entire existing contract language would exceed Minimum Necessary Change for G1-M2.

## 21. Promotion conditions

Before ACCEPTED/CURRENT can ever be considered for this proposal, the applicable chain must make explicit:
source/provenance, owner subject, competent authority, exact target identity/version, baseline, minimum necessary delta, requirement coverage, dependencies, alternatives/assumptions where applicable, decision, authorization where separately required, implementation evidence, verification evidence, applicable acceptance evidence and supersession/currentness treatment.

No step is automatic.
