# D1/M1 NOVELTY RECONSTRUCTION AND FALSIFICATION
# MASTER EXECUTION PLAN V6

## V6-1. Plan identity and precedence

- `PLAN_VERSION`: V6
- `SOURCE_PLAN_VERSION`: V5
- `SOURCE_PLAN`: `outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V5.md`
- `SOURCE_PLAN_SHA256`: `A73C19F385F26C5E927B30112CD4F89B43367538057854B04C5DEF16F0F44580`
- `SOURCE_REAUDIT`: `outputs/plans/D1_MASTER_PLAN_REAUDIT_V5.md`
- `SOURCE_REAUDIT_SHA256`: `830A42DD59D588C10817A55657985BDEBE2E135209D9753EBBA9D5FA38935F6E`
- `REMEDIATION_TASK`: D1-R5 execution-architecture remediation
- `REVISION_DATE`: 2026-09-25
- `STATUS`: PENDING_REAUDIT
- `A5_NEW_HIGH_FINDINGS`: 2
- `A5_RESOLVED_HIGH_FINDINGS`: 2/2
- `READY_FOR_RE_AUDIT`: true
- `READY_TO_LAUNCH_GEMINI_WORKERS`: false

This is the complete V6 plan. The embedded V5 text below is historical source material and is read-only. **V6 worker and stage contracts, V6 ownership graph, V6 failure routes, V6 hard-gate copies and V6 package manifest are the only active execution controls. V6 supersedes V5 for execution architecture. No worker may follow an inherited V5 definition when a V6 replacement exists.**

This remediation repairs only A5-HI-01 (ownership consistency) and A5-HI-02 (worker failure routing). D1 scientific logic, K1–K9 definitions, prior-art families, thresholds, search controls, red-team logic, negative outcomes and scope locks remain unchanged.

## V6-2. Scope lock and scientific preservation

This is plan remediation only. No worker is launched; no literature is searched; no evidence is extracted; no Sol synthesis, Astra red-team or D1 novelty adjudication is performed; MP1 and D1-vs-MP1 remain out of scope.

The V5 scientific controls remain binding: state-at-time history, claim evolution, non-novelty and candidate registers, source precedence, provenance, contradictions, K1–K9 falsification, post-freeze bias control, threshold freeze, evidence-first search, human review, hard gates and negative outcome space.

## V6-3. Canonical ownership precedence

The ownership rule is:

`V6 canonical worker/stage contract → V6 derived ownership graph → V6 package manifest`

The ownership matrix is derived from the V6 contracts. The package manifest indexes the matrix; it cannot redefine an owner. Every execution artifact has exactly one primary writer. `shared_write=false` for all current artifacts. Reconciliation and QA may update only under the declared update permission and may not become an unrecorded second writer.

The superseded V5 definitions are recorded as `SUPERSEDED_OWNERSHIP_DEFINITION` in the V5→V6 remediation record. S9 is the sole writer of frozen `D1_K_CRITERIA_REGISTER`; W12 reads it and may append only `KILL_CRITERION_CHANGE_RECORD.jsonl` under human approval. S16 is the sole writer of canonical hard-gate, routing-QA, package and execution-QA artifacts; W11 supplies QA inputs and no longer claims those files as outputs.

## V6-4. Ownership graph and handoffs

`D1_ARTIFACT_OWNERSHIP_MATRIX_V6.json` is the complete graph. Each row contains artifact ID/name, creation stage, primary owner, writer, reconciliation owner, QA owner, final consumer, readers, write/update permissions, handoff stage, worker contract reference and stage contract reference. `D1_ARTIFACT_OWNERSHIP_QA_V6.json` independently compares worker contract owner, stage contract owner, matrix owner and canonical owner.

The graph includes W01 scope/hash outputs; W02 inventory outputs; W03 history; W04 transition draft; W05–W08 paper shards; W09 canonical packets, claims and registers; W10 threat/search outputs; W11 provenance, contradiction, threshold and human clearance; W12 criterion-change record, K matrix and red-team matrix; S9 frozen criteria; S14 final evidence map; S15 final adjudication; and S16 gates, routing, package and QA controls. Ownership QA must report `ownership_conflicts=0` and `ownership_verified_workers=12` before readiness can be true.

## V6-5. Worker contract correction

`D1_WORKER_EXECUTION_READINESS_MATRIX_V6.json` is authoritative for W01–W12. Every worker has complete contract fields, one output directory, one canonical owner, one reconciliation owner, one QA owner, one failure-route set and valid re-entry logic.

W11 outputs only provenance QA, contradiction register, threshold freeze and human review clearance. W12 consumes the frozen S9 K criteria and outputs only the append-only criterion-change record, K1–K9 matrix and red-team matrix. S9 and S16 stage contracts own their own canonical artifacts. This removes the W12/S9 and W11/S16 contradictions without changing scientific content.

## V6-6. Worker failure routing

`D1_WORKER_FAILURE_ROUTING_MATRIX.json` is mandatory for every W01–W12. It covers INPUT_MISSING, PROVENANCE_FAILURE, SCHEMA_FAILURE, EVIDENCE_CONFLICT, QA_FAILURE, CONTRADICTION_FOUND, KILL_CRITERION_CONFLICT, SEARCH_TRIGGER_REQUIRED, THRESHOLD_LEAKAGE, HUMAN_REVIEW_REQUIRED, RECONCILIATION_FAILURE, OUTPUT_INCOMPLETE and OTHER.

Each route names the failed artifact, failure severity, return stage, return worker or explicit stage owner, reconciliation stage, required correction, artifact to update, re-entry condition, re-entry gate, retry policy and human-review requirement. Worker-content failures return to the worker or scientific reconciliation stage that can repair them. S16 is used only for package-level readiness, manifest or final package QA defects.

No route permits indefinite retry. High-severity, contradiction, threshold, criterion and human-review routes use no automatic retry or one retry followed by human review. `D1_WORKER_ROUTING_HARD_GATE_QA.json` verifies every route against a valid stage, owner and hard-gate re-entry target and must report zero mismatches.

## V6-7. Hard-gate alignment

`D1_HARD_GATE_MATRIX_V6.json`, `D1_HARD_GATE_MATRIX_V6.md`, `D1_HARD_GATE_ROUTING_QA_V6.json` and `D1_REVISION_ROUTING_MATRIX_V6.json` are V6 copies of the approved HG-01–HG-15 controls. HG-11's `RR-WORKER-READINESS` is explicitly package-level; worker output failures use the worker failure matrix. All fifteen gates remain `NOT_REACHED` before execution.

The five required stress routes are preserved: provenance contradiction to S9, unresolved K evidence to S10, threshold leakage to S11, human revision to S13, and worker-specific QA to its originating worker/reconciliation stage. A route cannot bypass its re-entry gate.

## V6-8. Readiness, package and stop rules

`execution_ready=true` requires complete contract, existing directory, consistent ownership, failure routing, valid re-entry logic, reconciliation owner, QA owner, schemas and definition of done. Readiness is structural and does not authorize execution. `READY_TO_LAUNCH_GEMINI_WORKERS` remains false until independent D1-A6 approval.

The V6 manifest requires the canonical plan, finding register, remediation matrices, ownership graph and QA, worker failure routes and QA, worker readiness, V6 hard gates and routing QA, revision routing and physical W01–W12 directories. Future science outputs are explicitly deferred until execution. Required missing artifacts, ownerless artifacts, invalid paths, duplicate canonical artifacts, missing schemas, missing worker directories, missing hard-gate rows, ownership conflicts, routing mismatches and invalid generic S16-only worker routes must all be zero.

## V6-9. Embedded V5 source plan (historical, read-only)
# D1/M1 NOVELTY RECONSTRUCTION AND FALSIFICATION
# MASTER EXECUTION PLAN V5

## V5-1. Plan identity, source and precedence

- `PLAN_VERSION`: V5
- `SOURCE_PLAN_VERSION`: V4
- `SOURCE_PLAN`: `outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V4.md`
- `SOURCE_PLAN_SHA256`: `D431901CB7203A15930759D7DA37C95DE170A2F988D7C6F6B151A2B353AF7286`
- `SOURCE_REAUDIT`: `outputs/plans/D1_MASTER_PLAN_REAUDIT_V4.md`
- `REMEDIATION_TASK`: D1-R4 targeted execution-readiness remediation
- `REVISION_DATE`: 2026-09-25
- `STATUS`: PENDING_REAUDIT
- `AUDIT_VERDICT_BEING_REMEDIATED`: MAJOR_REVISION_REQUIRED
- `A4_NEW_HIGH_FINDINGS`: 2
- `A4_NEW_CRITICAL_FINDINGS`: 0
- `RESOLVED_CRITICAL_COUNT`: 0
- `RESOLVED_HIGH_COUNT`: 2
- `UNRESOLVED_REVISION_COUNT`: 0
- `SCIENTIFIC_EXECUTION`: NOT_STARTED
- `READY_TO_LAUNCH_GEMINI_WORKERS`: false

This file is the complete V5 plan. The embedded V4 text below is preserved as historical source material and is read-only. **The V5 sections after the historical source are the only active execution architecture. When an inherited V4/V3 clause conflicts with a V5 section, V5 controls, V5 JSON contracts, V5 ownership and V5 gates take precedence. A worker must never use an obsolete V1-V4 instruction when a V5 replacement exists.**

V5 resolves exactly the two distinct new HIGH findings in A4. No scientific verdict, D1 verification round, M1 implementation, literature search, worker run, MP1 analysis or D1-vs-MP1 comparison is performed by this plan remediation.

## V5-2. Scope and scientific objective

The scope is D1/M1 novelty reconstruction and falsification only. MP1, D1-vs-MP1, mentor reporting, thesis execution, FE execution, apparatus design, physical experiments and broad literature search are out of scope.

The scientific question remains: after reconstructing the complete D1 history and auditing relevant prior art, what exactly remains defensible in the candidate direction `Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams`? M1 is Zhang et al., *A continuum-based model for a layer jamming beam*, DOI `10.5194/ms-16-821-2025`; the proposed architecture is M→R→E. This is a candidate to falsify, never an assumed novelty result.

The workflow preserves the D1 logic from V4: state-at-time history, claim-before→threat→evidence→decision→claim-after transitions, novelty categories (SYSTEM, MECHANISM, MODEL, METHOD, VALIDATION, SCIENTIFIC_QUESTION, WORKFLOW, APPLICATION), a formal non-novelty register, a separate novelty-candidate register, source precedence, paper-level evidence, K1-K9 falsification, threshold freeze, mechanism-evidence limits, human review, negative outcomes and evidence-first search control.

## V5-3. Authoritative artifacts and precedence

The A4 finding register, V4→V5 remediation matrix, V5 worker readiness matrix, ownership matrix, V5 routing matrix, hard-gate matrix, routing QA and package manifest are the machine-readable controls for this remediation. Their paths are listed in `D1_PLAN_PACKAGE_MANIFEST_V5.json`.

For current state, a valid canonical JSON artifact outranks a narrative summary. For paper claims, original PDF outranks evidence JSON, which outranks an AI summary. Historical reports remain historical records and are never rewritten as if their earlier interpretation had not existed. An unsupported thesis-critical claim fails QA.

## V5-4. Historical integrity, registers and evidence requirements

`D1_HISTORICAL_STATE_REGISTER` must retain `state_id`, `date_or_phase`, `verification_round`, `claim_at_time`, `status_at_time`, `supporting_file`, `supporting_verdict`, `later_superseded`, `superseded_by`, `reason_for_change` and `current_status`, with explicit STATE_AT_TIME, CURRENT_CANONICAL_STATE, SUPERSEDED_INTERPRETATION and CORRECTED_INTERPRETATION labels.

`D1_CLAIM_EVOLUTION_MATRIX` must encode `claim_id`, stage, claim_before, threat, source/paper, what the source proves and does not prove, decision, claim_after, reason, evidence status, confidence and provenance. No “many papers exist” shortcut may become a novelty conclusion.

`D1_NON_NOVELTY_REGISTER` records layer jamming, vacuum-controlled stiffness, frictional stiffening, interlayer slip, partial/full slip, continuum and layered-beam modelling, Coulomb friction, full-layer FE, physical experimentation, model-vs-experiment comparison, error metrics and tolerances when established by prior art. `D1_NOVELTY_CANDIDATE_REGISTER` records only residual candidate contributions, known overlap, threats, evidence, kill conditions and status (`CANDIDATE`, `NARROWED`, `KILLED`, `SURVIVES_AUDIT`). No final statement bypasses either register.

Every paper packet must preserve title, authors, year, DOI, paper ID, repository path, reason investigated, threatened claim, model, method, experiment, domain, outputs, error metrics, validity/breakdown assessment, higher-fidelity comparison, failure mechanism, what it proves and does not prove, impact, page/section and evidence pointer. Full text is required for detailed mechanics claims when available; metadata-only status is explicit.

## V5-5. K1-K9 falsification and post-freeze controls

The mandatory K gate tests: K1 systematic validity-domain mapping; K2 reduced versus layer-resolved/full-contact comparison; K3 model-form error; K4 deliberate valid and breakdown regimes; K5 experiments on both sides of a predicted boundary; K6 contact/slip/separation mechanism attribution; K7 substantially equivalent M→R→E in vacuum layer-jamming beams; K8 routine-methodology collapse; K9 conceptual equivalence under different terminology. Each row requires a scientific question, direct-kill and partial-overlap criteria frozen before evaluation, required evidence, prior-art family, candidate papers, evidence status, verdict, confidence and human-review status. `UNRESOLVED` at high significance blocks final adjudication. Absence of a hit never proves global novelty.

The K criteria are immutable after freeze. Any necessary change is append-only in `KILL_CRITERION_CHANGE_RECORD.jsonl` with old/new criterion, evidence exposure, bias risk, human approval, versions and adjudication consequence. Evidence seen before a change forces `BIAS_RISK`; unqualified survival is forbidden and review remains blocking.

## V5-6. Canonical execution sequence

All stages are future execution stages. This remediation does not execute them.

| stage | purpose | owner/model | required outputs | predecessor and stop condition |
|---|---|---|---|---|
| S0 | Scope, HEAD, hashes and exclusions | deterministic / none | scope lock, repository manifest, plan hash | Start; stop if identity unavailable. |
| S1 | Inventory D1 evidence and V001-V009 | Gemini 3.8 Flash High | evidence inventory, round coverage | S0; stop if a round is missing/unclassifiable. |
| S2 | Reconstruct state-at-time | Gemini Flash High + Sol High | historical state register | S1; stop if a state lacks contemporaneous source. |
| S3 | Extract paper-level packets | Gemini Flash High | evidence shards and canonical packet inputs | S1; stop if high-threat packet lacks locator/status. |
| S4 | Reconstruct claim evolution | Flash extraction + Sol High | claim matrix draft/canonical | S2,S3; stop if before/threat/after chain incomplete. |
| S5 | Map prior-art families and threats | Flash High + Sol High | family coverage, threat matrix, unresolved threats | S4; stop if a material family is omitted without reason. |
| S6 | Register non-novel components | Sol High | non-novelty register | S4,S5; stop if candidate contains unregistered generic component. |
| S7 | Register residual candidate claims | Sol High | novelty-candidate register | S6; stop if candidate is only routine workflow. |
| S8 | Provenance QA and contradiction detection | deterministic + Sol High | provenance QA, contradiction register | S5-S7; stop on orphan claim or invalid locator. |
| S9 | Freeze K1-K9 criteria | Sol High + Astra High review | K criteria register | S8; stop until nine criteria are frozen. |
| S10 | Evidence-first evaluation and bounded search | Flash High + Sol High | search log, updated threats, K evidence | S9; stop if trigger/stop condition missing. |
| S11 | Freeze thresholds and boundaries | Sol High + deterministic timing check | threshold freeze register | S10; stop on retrospective threshold. |
| S12 | Adversarial red-team attack | Astra High | K matrix, red-team matrix | S10,S11; stop on unresolved high-significance K or attack. |
| S13 | Human review and exact routing | human gate + deterministic QA | human clearance | S8,S10-S12; stop if required review is not CLEARED. |
| S14 | Scientific synthesis and independent challenge | Sol High + Astra High | final evidence map, synthesis draft | S13; stop if any prerequisite gate fails. |
| S15 | D1-only final adjudication | Sol High; Astra xHigh only material conflict | final JSON and Markdown outcome | S14; allowed outcomes remain negative or inconclusive. |
| S16 | Deterministic package and hard-gate QA | deterministic / none | manifest, execution QA, gate statuses | S15; stop on any missing/ownerless/invalid artifact. |

## V5-7. Worker contracts and physical output ownership

The complete contracts are in `D1_WORKER_EXECUTION_READINESS_MATRIX_V5.json`. W01-W12 each has exclusive scope, explicit input artifacts, a real physical output directory, required outputs, schema, dependencies, allowed and forbidden inference, reconciliation owner, QA owner, review trigger and definition of done. W05-W08 may extract in parallel; W09 owns canonical packet identity and deduplication; W10 searches only on a named trigger; W11 never silently repairs contradictions; W12 attacks candidates but does not adjudicate final novelty. Stage-owned outputs are explicit: S9 owns the frozen K criteria, S14 owns the final evidence map, S15 owns final adjudication files, and S16 owns package and gate QA.

The structural rule is hard: false `output_directory_exists`, false ownership, false schema/contract check or missing required output forces `execution_ready=false`. V5 has created all twelve directories, but `execution_started=false` and `launch_authorization=false`. A directory existing does not mean a worker has run.

## V5-8. Provenance, contradiction, search and human review controls

No worker output is itself a scientific conclusion. Every conclusion must traverse claim → evidence packet → source file → paper → page/section → original PDF where available → raw provenance. Contradictions use `D1_CONTRADICTION_REGISTER` with types SUMMARY_VS_JSON, JSON_VS_PDF, ROUND_VS_ROUND, WORKER_VS_WORKER, HISTORICAL_VS_CURRENT, METADATA_VS_FULLTEXT or OTHER. They are recorded and routed; critical unresolved rows block final adjudication.

Repository evidence is reviewed first. A targeted search requires a named K1-K9, provenance, high-threat or conceptual-equivalence gap, a query family, source/database, screening and dedup rules, full-text promotion rule, date, stop condition and closure record. `DO_NOT_OPEN`, `OPEN` and `CLOSE` decisions are durable; broad search and no-hit global-absence reasoning are forbidden.

Human review is mandatory for direct-kill papers, conceptual-equivalence claims, PDF/extraction conflicts, thesis-critical worker disagreement, material candidate changes, KILL or UNRESOLVED K results, absence-based reasoning, arbitrary thresholds, retrospective historical reinterpretation, post-freeze criterion changes and any rejected or revision-required route.

## V5-9. Complete hard-gate control

`D1_HARD_GATE_MATRIX.json` and its Markdown rendering contain exactly HG-01 through HG-15. Every row has required inputs, required artifacts, machine checks, pass/fail conditions, blocked stage, exact return route and stage, responsible owner, human-review fields, status, evidence, timestamp and repository commit. Pre-execution status is `NOT_REACHED`; it must not be changed to PASS by this remediation. `D1_HARD_GATE_ROUTING_QA.json` proves each route exists and has a valid return stage and re-entry gate. Failed gates cannot be bypassed.

The final gate requires all historical stages accounted for, all claims source-bound, high-threat papers resolved or explicitly unavailable, both novelty registers stable, critical contradictions cleared, K1-K9 resolved or explicitly blocking, thresholds frozen before visible validation data, red-team and human review cleared, unsupported thesis-critical claims equal zero, all twelve workers structurally ready, package QA passing and no unresolved critical route. Final outcomes remain `FALSIFIED`, `SUBSTANTIALLY_NARROWED`, `SURVIVES_TARGETED_NOVELTY_AUDIT` or `INCONCLUSIVE`; the workflow never forces survival.

## V5-10. Model and cost allocation

Gemini 3.8 Flash High handles inventory, chronology, paper extraction and bounded retrieval. GPT-6 Sol High handles claim reconciliation, category control, threat integration, provenance interpretation and synthesis. GPT-6 Astra High handles adversarial K and red-team critique. Astra xHigh is conditional only for a material unresolved final conflict. Deterministic checks handle hashes, paths, schemas, gate rows and package counts. Astra is not used for extraction, formatting, bibliography or routine QA. Qualitative cost is LOW for deterministic checks, LOW-MODERATE for Flash extraction, MODERATE-HIGH for Sol integration, HIGH for Astra attack, and VERY-HIGH only for conditional xHigh final conflict.

## V5-11. Residual risks and re-audit checklist

The four nonblocking A4 medium observations remain visible as residual risks: generic legacy route language in historical text, inherited V2/V3 presentation, future-output granularity and search-field alias normalization. They do not erase the V5 exact route and canonical schema controls; an A5 re-audit may test them. Full-text unavailability can still produce an unresolved K result and block survival. Human review and threshold timing remain real execution dependencies.

The independent re-auditor must verify: the A4 count is 0 Critical/2 High; both remediation records exist and are resolved; V4 hash is unchanged; all twelve directories exist; every readiness boolean and ownership record is complete; the package manifest has zero required missing/ownerless/invalid/duplicate artifacts; the hard-gate set is exactly HG-01..HG-15; route QA passes; no worker, search or scientific verdict was executed; launch remains false; MP1 remains out of scope.

## V5-12. Embedded V4 source plan (historical, read-only)
# D1/M1 NOVELTY RECONSTRUCTION AND FALSIFICATION
# MASTER EXECUTION PLAN V4

## 1. Plan identity and remediation provenance

- PLAN_VERSION: V4
- plan_version: V4
- source_plan: V3
- SOURCE_PLAN_VERSION: V3
- SOURCE_PLAN: outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V3.md
- SOURCE_REAUDIT: outputs/plans/D1_MASTER_PLAN_REAUDIT_V3.md
- REMEDIATION_TASK: D1-R3
- REVISION_DATE: 2026-09-25
- audit_source: outputs/plans/D1_MASTER_PLAN_REAUDIT_V3.md
- audit_verdict: MAJOR_REVISION_REQUIRED
- source_plan_version: V3
- resolved_critical_count: 1
- resolved_high_count: 2
- unresolved_revision_count: 0
- PREVIOUS_VERDICT: MAJOR_REVISION_REQUIRED
- REMAINING_CRITICAL_FINDINGS: 1
- REMAINING_HIGH_FINDINGS: 2
- REMAINING_MEDIUM_FINDINGS: 3
- RESOLVED_CRITICAL_FROM_REAUDIT: 1/1
- RESOLVED_HIGH_FROM_REAUDIT: 2/2
- RESOLVED_MEDIUM_FROM_REAUDIT: 3/3
- UNRESOLVED_CRITICAL_HIGH_COUNT: 0
- STATUS: PENDING_REAUDIT
- READY_FOR_RE_AUDIT: true
- READY_TO_LAUNCH_GEMINI_WORKERS: false

The remediation checklist is preserved in:

outputs/plans/D1_MASTER_PLAN_REMEDIATION_CHECKLIST_V1.md

This V4 is a plan artifact only. It does not execute the scientific audit, launch workers, search literature, extract paper evidence, implement M1, run FE, collect data, analyze MP1, compare D1 with MP1, or modify scientific verdicts.

V4 binding overlay sections 36 onward supersede conflicting inherited V3/V2 execution clauses. Earlier sections remain historical provenance; execution uses only the V4 overlay, JSON contracts and manifests.

## 2. Scope lock

### In scope

- D1 novelty;
- D1 scientific lineage;
- D1/M1 claim evolution;
- prior-art threat evaluation;
- provenance, contradiction and falsification controls;
- preparation of a D1-only adjudication workflow.

### Out of scope

- MP1;
- D1-vs-MP1 comparison;
- mentor persuasion;
- topic ranking;
- thesis execution;
- M1 implementation;
- FE implementation;
- apparatus design;
- physical experiments;
- broad literature search without a named trigger.

The workflow may inspect whether M1, R and E are sufficiently specified to support a novelty claim. It must not implement M1, run FE, design apparatus, collect data or execute experiments.

## 3. Scientific objective and current target

The workflow must answer:

> After reconstructing the complete D1 research history and auditing relevant prior art, what exactly remains scientifically defensible in the current D1/M1 direction?

Current candidate direction:

Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams

M1:

Zhang et al., A continuum-based model for a layer jamming beam

DOI:

10.5194/ms-16-821-2025

Architecture:

M → R → E

where M is the specified continuum/reduced model, R is a proposed higher-fidelity full-layer frictional-contact reference, and E is an independent physical experiment.

This is a candidate claim, not an accepted novelty conclusion.

## 4. Repository authority and evidence boundary

### Canonical current-state inputs

- docs/project/PROJECT_HANDOFF_CURRENT.md
- docs/project/RESEARCH_STATE.md
- docs/project/research_state.json
- docs/project/RESEARCH_LOG.md
- outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json

### Research-design inputs

- docs/research_design/M1_RESEARCH_ARCHITECTURE.md
- docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md
- docs/research_design/EXACT_MODEL_SELECTION.md
- docs/research_design/LAYER_JAMMING_MODEL_COMPARISON.md

### Historical D1 inputs

- outputs/verification/D1-V001/
- outputs/verification/D1-V002/
- outputs/verification/D1-V003/
- outputs/verification/D1-V004/
- outputs/verification/D1-V005/
- outputs/verification/D1-V006/
- outputs/verification/D1-V007/
- outputs/verification/D1-V008/
- outputs/verification/D1-V009/

### Original evidence

- data/evidence/
- data/papers/
- papers/
- data/search_exports/

MP1 files are excluded from the D1 evidence set.

## 5. Historical State Register

The first historical artifact is:

D1_HISTORICAL_STATE_REGISTER

It must preserve what was believed at the time and must never replace an earlier state with later knowledge.

Minimum fields:

~~~text
state_id
date_or_phase
verification_round
claim_at_time
scientific_question_at_time
status_at_time
supporting_source
supporting_verdict
evidence_available_at_time
later_superseded
superseded_by
reason_for_change
corrected_interpretation
current_canonical_state
confidence
~~~

Required coverage rows:

- discovery/original D1;
- D1-V001;
- D1-V002;
- D1-V003;
- D1-V004;
- D1-V005;
- D1-V006;
- D1-V007;
- D1-V008;
- D1-V009;
- current D1/M1 state.

Historical status tokens must remain distinct from current status:

~~~text
STATE_AT_TIME
CURRENT_CANONICAL_STATE
SUPERSEDED_INTERPRETATION
CORRECTED_INTERPRETATION
~~~

## 6. Claim Evolution Matrix

Every material transition must have:

~~~text
claim_id
historical_stage
claim_before
threat
source_id
paper_title
authors
year
DOI
paper_id
what_the_source_proves
what_the_source_does_not_prove
decision
claim_after
reason_for_transition
evidence_status
confidence
superseded_by
correction_status
provenance_pointer
~~~

The required logical sequence is:

~~~text
CLAIM BEFORE
→ THREAT
→ EVIDENCE
→ DECISION
→ CLAIM AFTER
~~~

No transition may be supported only by a later summary or a filename.

## 7. Novelty-category control

Every claim receives one primary novelty category:

~~~text
SYSTEM
MECHANISM
MODEL
METHOD
VALIDATION
SCIENTIFIC_QUESTION
WORKFLOW
APPLICATION
~~~

Secondary categories may be recorded but may not replace the primary category silently.

The workflow must explicitly reject:

- exact-title novelty;
- novelty from a different geometry, material or apparatus alone;
- novelty from an error metric alone;
- novelty from an acceptance tolerance alone;
- novelty from combining known methods without a new mechanics question;
- novelty from a different application when the mechanics are already established.

## 8. D1_NON_NOVELTY_REGISTER

This controlled register records what D1 must not claim as novel.

Minimum fields:

~~~text
item_id
concept
novelty_category
prior_art_source
paper_title
authors
year
DOI
paper_id
evidence_pointer
what_prior_art_establishes
reason_non_novel
affected_D1_claim
status
confidence
~~~

The register must test at least:

- layer jamming;
- vacuum-controlled stiffness;
- frictional stiffening;
- interlayer slip;
- partial/full slip;
- continuum modeling;
- layered beam modeling;
- Coulomb friction;
- full-layer finite-element modeling;
- physical experimentation;
- model-versus-experiment comparison;
- error metrics;
- acceptance tolerances.

## 9. D1_NOVELTY_CANDIDATE_REGISTER

No final novelty statement may bypass this register.

Minimum fields:

~~~text
candidate_id
candidate_claim
novelty_category
derived_from_claims
known_prior_art_overlap
supporting_evidence
unresolved_threats
kill_conditions
status
confidence
scientific_contribution
workflow_components_only
model_validation_only
validity_domain_question
~~~

Allowed status:

~~~text
CANDIDATE
NARROWED
KILLED
SURVIVES_AUDIT
~~~

A candidate that contains only workflow sophistication, ordinary validation, a new tolerance, or a new apparatus must be marked accordingly and cannot be promoted automatically.

## 10. Provenance, source precedence and contradiction control

### Evidence chain

Every thesis-critical claim must trace:

~~~text
claim
→ evidence packet
→ source file
→ paper
→ page or section
→ original PDF where available
→ raw prompt/output/provenance
~~~

### Source precedence

For paper-specific scientific claims:

~~~text
original PDF
>
evidence JSON
>
AI summary
~~~

For current workflow state:

~~~text
latest canonical JSON with valid provenance
>
stale narrative summary
~~~

Historical reports remain historical records even after later correction.

Every evidence row records:

~~~text
source_hash
source_type
source_precedence
locator_validation_status
primary_source_available
evidence_status
confidence
~~~

### D1_CONTRADICTION_REGISTER

Minimum fields:

~~~text
contradiction_id
claim_id
source_A
source_B
source_type_A
source_type_B
interpretation_A
interpretation_B
contradiction_type
severity
adjudication_required
adjudicator
resolution
resolved_source
residual_uncertainty
status
~~~

Contradiction types:

~~~text
SUMMARY_VS_JSON
JSON_VS_PDF
ROUND_VS_ROUND
WORKER_VS_WORKER
HISTORICAL_VS_CURRENT
METADATA_VS_FULLTEXT
OTHER
~~~

Critical unresolved contradictions block final adjudication.

## 11. Paper evidence standard

The controlled artifact is:

D1_PAPER_EVIDENCE_PACKETS

Every thesis-critical paper must eventually contain:

~~~text
paper_id
title
authors
year
DOI
repository_path
reason_investigated
D1_claim_threatened
model
method
experiment
parameter_domain
outputs
error_metrics
validity_assessment
breakdown_assessment
higher_fidelity_reference
reference_resolution_level
failure_mechanism_analysis
addresses_A
addresses_B
addresses_C
what_it_proves
what_it_does_not_prove
impact_on_D1
page_or_section
evidence_pointer
evidence_status
confidence
~~~

When full text exists, title or abstract evidence alone is insufficient for detailed mechanics claims.

## 12. Prior-art family coverage

The controlled artifact is:

D1_PRIOR_ART_FAMILY_COVERAGE

Relevant families must be selected from repository history and recorded with:

~~~text
family_id
family_name
why_relevant
repository_sources
covered_claims
unresolved_threats
coverage_status
inclusion_reason
exclusion_reason
targeted_search_required
~~~

Candidate families include:

- layer-jamming mechanics;
- vacuum layer-jamming;
- friction-controlled stiffness;
- partial-interaction beam mechanics;
- interlayer-slip models;
- layered/composite beam theory;
- continuum models for layered structures;
- Cosserat/generalized continuum;
- interface-resolved models;
- frictional-contact FE;
- full-layer models;
- experimental layer-jamming characterization;
- model verification;
- model validation;
- model-form error;
- validity-domain studies;
- reduced-model breakdown;
- uncertainty-aware validation.

No family may be silently omitted. A family may be excluded only with an explicit reason.

## 13. Search control and search-bias control

### Search order

1. Existing repository evidence.
2. Named unresolved threats.
3. Targeted search only when a defined trigger exists.
4. No broad search by default.

### Targeted-search triggers

A targeted search may start only when:

- a K1-K9 test remains unresolved;
- a historical transition lacks provenance;
- a named high-threat source lacks full text;
- a conceptual-equivalence threat appears;
- a specific evidence gap blocks adjudication.

### Search record

Every search receives:

~~~text
search_id
trigger
scientific_question
concept_family
query_terms
synonyms
database_or_source
date
screening_rule
dedup_rule
full_text_promotion_rule
stop_condition
human_review_trigger
closure_reason
~~~

Searches must expand terminology beyond the current title. Search families must include equivalent composite-beam, partial-interaction, reduced-order, homogenized, interface-contact, slip, model-form-error and applicability terminology when scientifically justified.

No search may be open-ended or use absence of hits as proof of global absence.

## 14. K1-K9 falsification gate

The controlled artifact is:

D1_K1_K9_FALSIFICATION_MATRIX

The gate is mandatory before final D1 adjudication.

Each row contains:

~~~text
kill_test_id
scientific_question
conceptual_equivalence_rule
what_counts_as_direct_kill
what_counts_as_partial_overlap
required_evidence
existing_repository_evidence
targeted_search_trigger
relevant_prior_art_family
candidate_sources
evidence_status
verdict
confidence
human_review_required
resolution_notes
~~~

Allowed verdict:

~~~text
KILL
PARTIAL_OVERLAP
NO_KILL_FOUND
UNRESOLVED
~~~

### K1

Does a comparable continuum layer-jamming model already have a systematic validity-domain map?

### K2

Does a prior study compare a reduced model with a layer-resolved or full-contact reference across a meaningful operating domain?

### K3

Does a prior study quantify model-form error for the same or equivalent mechanics problem?

### K4

Does a prior study deliberately identify valid and invalid/breakdown regimes?

### K5

Does a prior experiment intentionally sample both sides of a predicted validity boundary?

### K6

Does a prior study attribute reduced-model failure to contact, slip, separation or related interface physics?

### K7

Has a substantially equivalent M → R → E workflow already been applied to vacuum layer-jamming beams?

### K8

Does prior methodology make the proposed D1 contribution routine rather than scientifically substantive?

### K9

Does conceptually equivalent prior work use different terminology but directly pre-empt the surviving question?

Final adjudication is blocked if any high-significance K-test remains UNRESOLVED.

## 15. Threshold, mechanism and causal-evidence controls

The controlled artifact is:

D1_THRESHOLD_FREEZE_RECORD

It must contain:

~~~text
freeze_id
claim_id
output
error_metric
tolerance
justification
decision_date
decision_stage
reviewer
pre_error_inspection
version
change_log
~~~

Tolerances, validity boundaries and breakdown criteria must be frozen before final error inspection. Changes create a new version and cannot overwrite the prior commitment.

Mechanism evidence is classified as:

~~~text
CORRELATION
MECHANISTIC_CONSISTENCY
CAUSAL_EVIDENCE
HYPOTHESIS
~~~

Pressure/error or slip/error correlation alone cannot be reported as causal failure mechanism.

## 16. Revised execution stages

All stages below are future execution stages. None is being executed by this remediation.

### S0 — Plan, repository and scope lock

- Objective: bind execution to V2, repository HEAD and a clean provenance manifest.
- Inputs: V2, HEAD, git status, file hashes.
- Outputs: repository_manifest, scope_lock, plan_hash_record.
- MODEL: deterministic validation; no model call.
- REASONING: none.
- WHY THIS MODEL: hashes and path checks are deterministic.
- WHY NOT CHEAPER: no model is cheaper than a deterministic check.
- WHY NOT MORE EXPENSIVE: Astra adds no value.
- COST: LOW.
- Dependency: none.
- Acceptance: plan hash, HEAD, status and excluded paths recorded.
- Failure: plan hash or canonical input status unavailable.
- Human review: scope boundary confirmation.

### S1 — Evidence inventory and round coverage

- Objective: inventory all D1 artifacts and verify discovery plus D1-V001…D1-V009 coverage.
- Inputs: repository authority paths and D1 rounds.
- Outputs: D1_EVIDENCE_INVENTORY, D1_ROUND_COVERAGE.
- MODEL: Gemini 3.8 Flash.
- REASONING: High.
- WHY THIS MODEL: bulk file and provenance extraction.
- WHY NOT CHEAPER: lower effort risks missed artifacts.
- WHY NOT MORE EXPENSIVE: Astra is unnecessary for inventory.
- COST: LOW–MODERATE.
- Dependency: S0.
- Acceptance: every expected round and artifact has path, type, hash and status.
- Failure: missing or unclassifiable artifact.
- Human review: inventory completeness.

### S2 — Historical State Register

- Objective: reconstruct the state believed at each D1 phase.
- Inputs: S1 inventory, handoff, research log, round verdicts and prompts.
- Outputs: D1_HISTORICAL_STATE_REGISTER.
- MODEL: Gemini 3.8 Flash, followed by GPT-6 Sol reconciliation.
- REASONING: High.
- WHY THIS MODEL: Flash extracts chronology; Sol reconciles state transitions.
- WHY NOT CHEAPER: chronology errors are thesis-critical.
- WHY NOT MORE EXPENSIVE: Astra is reserved for adversarial judgment.
- COST: MODERATE.
- Dependency: S1.
- Acceptance: discovery plus V001–V009 and current state are represented without hindsight rewriting.
- Failure: state-at-time or supporting evidence missing.
- Human review: every supersession and correction.

### S3 — Paper-level evidence packets

- Objective: extract source-bound evidence for material papers.
- Inputs: PDFs, evidence JSON, matrices, source provenance.
- Outputs: D1_PAPER_EVIDENCE_PACKETS.
- MODEL: Gemini 3.8 Flash.
- REASONING: High.
- WHY THIS MODEL: repeated full-text extraction.
- WHY NOT CHEAPER: detailed fields require high extraction reliability.
- WHY NOT MORE EXPENSIVE: Astra is not needed for repetitive extraction.
- COST: MODERATE.
- Dependency: S1.
- Acceptance: all high-threat papers have full fields and locators; metadata-only status is explicit.
- Failure: source claims exceed available text.
- Human review: direct-kill and high-threat packets.

### S4 — Claim evolution and A/B/C objection classification

- Objective: bind each claim change to evidence and classify the three “done many times” propositions.
- Inputs: S2 state register, S3 packets, historical verdicts.
- Outputs: D1_CLAIM_EVOLUTION_MATRIX, claim_A_B_C_map.
- MODEL: GPT-6 Sol.
- REASONING: High.
- WHY THIS MODEL: cross-source reconciliation and scientific synthesis.
- WHY NOT CHEAPER: simple extraction cannot resolve claim meaning.
- WHY NOT MORE EXPENSIVE: Astra is not yet needed for final attack.
- COST: MODERATE.
- Dependency: S2, S3.
- Acceptance: every material transition has complete evidence linkage and addresses_A/B/C fields.
- Failure: transition lacks source or claim-before/after.
- Human review: disputed transitions.

### S5 — Non-novelty registration

- Objective: freeze components that D1 must not claim as novel.
- Inputs: S3 packets, S4 matrix, repository prior-art evidence.
- Outputs: D1_NON_NOVELTY_REGISTER.
- MODEL: GPT-6 Sol.
- REASONING: High.
- WHY THIS MODEL: category and scope judgment.
- WHY NOT CHEAPER: simple extraction cannot determine claim boundaries.
- WHY NOT MORE EXPENSIVE: no final adversarial decision yet.
- COST: MODERATE.
- Dependency: S4.
- Acceptance: every generic non-novel component has source, pointer, reason and status.
- Failure: component appears in candidate without register status.
- Human review: disputed category or direct prior-art claim.

### S6 — Novelty-candidate registration

- Objective: define only residual candidate contributions.
- Inputs: S4 claim evolution, S5 non-novelty register, S3 packets.
- Outputs: D1_NOVELTY_CANDIDATE_REGISTER.
- MODEL: GPT-6 Sol.
- REASONING: High.
- WHY THIS MODEL: candidate synthesis after elimination.
- WHY NOT CHEAPER: candidate scope is a scientific judgment.
- WHY NOT MORE EXPENSIVE: adversarial kill is a later stage.
- COST: MODERATE.
- Dependency: S5.
- Acceptance: every candidate has overlap, threats, kill conditions, category and confidence.
- Failure: candidate is only an ordinary workflow or validation step.
- Human review: every material candidate revision.

### S7 — Prior-art family and threat mapping

- Objective: map relevant literature families and threats without open-ended searching.
- Inputs: S3 packets, S5 register, S6 candidates, repository search logs.
- Outputs: D1_PRIOR_ART_FAMILY_COVERAGE, D1_PRIOR_ART_THREAT_MATRIX, D1_UNRESOLVED_THREAT_REGISTER.
- MODEL: Gemini 3.8 Flash plus GPT-6 Sol.
- REASONING: Flash High; Sol High.
- WHY THIS MODEL: Flash screens; Sol consolidates conceptual overlap.
- WHY NOT CHEAPER: conceptual equivalence needs synthesis.
- WHY NOT MORE EXPENSIVE: Astra is reserved for K-tests.
- COST: MODERATE–HIGH.
- Dependency: S6.
- Acceptance: each relevant family has inclusion/exclusion rationale and each threat has status.
- Failure: threat family omitted without reason.
- Human review: high-threat and conceptual-equivalence cases.

### S8 — Provenance QA and contradiction detection

- Objective: validate evidence chains and register conflicts.
- Inputs: S1–S7 artifacts, source hashes and locators.
- Outputs: D1_PROVENANCE_QA, D1_CONTRADICTION_REGISTER.
- MODEL: deterministic validator plus GPT-6 Sol for typed interpretation.
- REASONING: High for interpretation.
- WHY THIS MODEL: deterministic checks catch structural failures; Sol classifies scientific conflicts.
- WHY NOT CHEAPER: unresolved conflict typing can alter claims.
- WHY NOT MORE EXPENSIVE: Astra is not needed for all contradictions.
- COST: MODERATE.
- Dependency: S7.
- Acceptance: every thesis-critical claim has a valid evidence chain; all conflicts are registered.
- Failure: orphan claim, invalid locator or missing source precedence.
- Human review: every critical contradiction.

### S9 — Contradiction adjudication

- Objective: resolve or block contradictions without silent reconciliation.
- Inputs: D1_CONTRADICTION_REGISTER, source hierarchy, human review records.
- Outputs: resolved contradiction records and updated unresolved-threat register.
- MODEL: GPT-6 Sol.
- REASONING: High.
- WHY THIS MODEL: cross-source adjudication.
- WHY NOT CHEAPER: contradiction resolution is not routine extraction.
- WHY NOT MORE EXPENSIVE: Astra is reserved for final adversarial issues.
- COST: MODERATE–HIGH.
- Dependency: S8.
- Acceptance: every critical conflict resolved or explicitly blocking.
- Failure: unresolved critical contradiction is passed forward.
- Human review: mandatory for JSON/PDF and historical/current conflicts.

### S10 — Conditional targeted search

- Objective: resolve only named evidence gaps.
- Inputs: unresolved threats, unresolved K-test prerequisites, missing full texts.
- Outputs: search records, promoted source packets or documented unavailability.
- MODEL: Gemini 3.8 Flash plus GPT-6 Sol.
- REASONING: Flash High; Sol High.
- WHY THIS MODEL: Flash retrieves/screens; Sol decides whether the gap is closed.
- WHY NOT CHEAPER: search closure requires scientific interpretation.
- WHY NOT MORE EXPENSIVE: no Astra for retrieval.
- COST: MODERATE–HIGH, conditional.
- Dependency: S9.
- Acceptance: every search has trigger, query family, stop condition and closure reason.
- Failure: broad or indefinite search.
- Human review: every new high-threat source.

### S11 — K1-K9 falsification and red-team gate

- Objective: attempt to kill every novelty candidate.
- Inputs: candidates, family matrix, threat matrix, evidence packets, contradictions.
- Outputs: D1_K1_K9_FALSIFICATION_MATRIX, D1_RED_TEAM_MATRIX.
- MODEL: GPT-6 Astra.
- REASONING: High.
- WHY THIS MODEL: adversarial scientific critique and fatal-gap detection.
- WHY NOT CHEAPER: this is the highest-risk reasoning stage.
- WHY NOT MORE EXPENSIVE: xHigh is reserved for final unresolved adjudication.
- COST: HIGH.
- Dependency: S10.
- Acceptance: K1–K9 have verdicts, evidence, confidence and human-review status.
- Failure: high-significance K-test remains UNRESOLVED.
- Human review: every KILL and UNRESOLVED result.

### S12 — Scientific synthesis and final adjudication

- Objective: produce the D1-only outcome without forcing survival.
- Inputs: all registers, matrices, contradiction records, K1-K9 gate and review records.
- Outputs: D1_FINAL_EVIDENCE_MAP, D1_PROVENANCE_QA, final D1 adjudication draft and final challenge record.
- MODEL: GPT-6 Sol draft plus GPT-6 Astra High final challenge; Astra xHigh only if justified.
- REASONING: Sol High; Astra High; xHigh conditional.
- WHY THIS MODEL: Sol integrates; Astra attacks the final conclusion.
- WHY NOT CHEAPER: final scientific judgment is high stakes.
- WHY NOT MORE EXPENSIVE: xHigh is used only for unresolved material conflict.
- COST: HIGH–VERY_HIGH, conditional.
- Dependency: S11.
- Acceptance: no unresolved high-significance K-test, no unsupported thesis-critical claim, all human gates cleared.
- Failure: forced survival, missing evidence, or blocked contradiction.
- Human review: final D1-only sign-off.

### S13 — Deterministic packaging and QA

- Objective: validate schemas, hashes, counts and non-overwrite rules.
- Inputs: all S0–S12 artifacts.
- Outputs: D1_PLAN_EXECUTION_QA, artifact manifest and report package.
- MODEL: deterministic validator.
- REASONING: none.
- WHY THIS MODEL: schema and file checks are deterministic.
- WHY NOT CHEAPER: no model is cheaper than a validator.
- WHY NOT MORE EXPENSIVE: Astra adds no value.
- COST: LOW.
- Dependency: S12.
- Acceptance: all required files exist, parse, contain provenance and preserve historical rounds.
- Failure: missing artifact, duplicate ID, unresolved critical issue or overwrite.
- Human review: package completeness.

## 17. Revised worker architecture

The V1 groups are redefined into 12 non-overlapping logical roles. No worker is launched by this remediation.

| Worker | Exclusive responsibility | Inputs | Outputs | Dependency | Parallelizable | Model |
|---|---|---|---|---|---|---|
| W01 | Scope, plan hash and repository provenance | V2, HEAD, git status | scope_lock, repository_manifest | S0 | false | Deterministic |
| W02 | Artifact and round inventory | D1 directories, evidence paths | evidence_inventory, round_coverage | W01 | true | Gemini Flash High |
| W03 | Historical state reconstruction | handoff, log, V001-V009 | historical_state_register | W02 | false | Gemini Flash High |
| W04 | Claim transition extraction | state register, verdicts, prompts | claim_evolution_matrix | W03 | false | Gemini Flash High |
| W05 | Direct layer-jamming evidence | relevant PDFs and packets | paper packets, family rows | W02 | true | Gemini Flash High |
| W06 | Continuum, homogenization and Cosserat evidence | relevant PDFs and packets | paper packets, family rows | W02 | true | Gemini Flash High |
| W07 | Contact, partial-interaction and full-layer evidence | relevant PDFs and packets | paper packets, family rows | W02 | true | Gemini Flash High |
| W08 | Validity, model-form error and uncertainty evidence | relevant PDFs and packets | paper packets, family rows | W02 | true | Gemini Flash High |
| W09 | Non-novelty and candidate registration | W04-W08 outputs | non_novelty_register, candidate_register | W04-W08 | false | GPT-6 Sol High |
| W10 | Targeted search and threat integration | candidate register, unresolved threats | search log, threat matrix, unresolved register | W09 | conditional | Gemini Flash High plus Sol High |
| W11 | Provenance, contradiction and threshold QA | W01-W10 outputs | provenance_QA, contradiction_register, threshold_freeze | W10 | false | Deterministic plus Sol High |
| W12 | K1-K9 adversarial gate and final challenge | all prior artifacts | K1_K9_matrix, red_team_matrix, final challenge | W11 | false | Astra High; xHigh conditional |

Worker rules:

- W05-W08 may run in parallel only after W02.
- W09 must wait for all paper families.
- W10 may not search unless a trigger exists.
- W11 may not silently repair conflicts.
- W12 cannot return SURVIVES_AUDIT when a high-significance K-test is UNRESOLVED.

## 18. Model allocation and cost ledger

| Stage | Model | Reasoning | Why this model | Why not cheaper | Why not more expensive | Cost |
|---|---|---|---|---|---|---|
| S0 | deterministic | none | hashes and scope are mechanical | no model is cheaper | Astra adds no value | LOW |
| S1-S3 | Gemini Flash | High | bulk extraction and chronology | lower effort risks omissions | Astra is wasteful | LOW–MODERATE |
| S4-S7 | Sol plus Flash | High | claim synthesis and family integration | simple extraction cannot reconcile claims | Astra not yet needed | MODERATE–HIGH |
| S8-S10 | deterministic plus Sol/Flash | High where interpretive | provenance and targeted closure | conflicts need reasoning | Astra not used for retrieval | MODERATE–HIGH |
| S11 | Astra | High | adversarial kill testing | cheaper model risks confirmation bias | xHigh reserved for unresolved final issue | HIGH |
| S12 | Sol plus Astra | High; xHigh conditional | synthesis followed by final challenge | final gate is high stakes | xHigh only if material disagreement | HIGH–VERY_HIGH |
| S13 | deterministic | none | schema and hash QA | no model is cheaper | Astra adds no value | LOW |

Astra must not be used for routine extraction, formatting, bibliography construction, table generation or simple QA.

## 19. Human review and escalation

The controlled artifact is:

D1_HUMAN_REVIEW_RECORD

Minimum fields:

~~~text
review_id
trigger
items_reviewed
disagreement
human_disposition
evidence_changed
claim_changed
reviewer_scope
timestamp
next_action
~~~

Review is mandatory when:

- a direct kill paper is found;
- a conceptually equivalent paper is found;
- PDF conflicts with extraction;
- canonical state conflicts with historical report;
- workers disagree on a thesis-critical claim;
- a candidate materially changes;
- K1-K9 returns KILL or UNRESOLVED;
- novelty depends mainly on absence;
- a threshold appears retrospective;
- a historical state is corrected.

## 20. Stop conditions and definitions of done

### Stage completion

Each stage is complete only when its output exists, parses, has provenance and passes its acceptance criteria.

### Final gate

Final adjudication is prohibited until:

- all historical stages are accounted for;
- all material claims have provenance;
- all high-threat papers are resolved or explicitly unavailable;
- D1_NON_NOVELTY_REGISTER is stable;
- D1_NOVELTY_CANDIDATE_REGISTER is stable;
- critical contradictions are resolved;
- all significant K1-K9 tests are resolved;
- no thesis-critical claim relies only on title/abstract when full text exists;
- unsupported thesis-critical claims equal zero;
- human-review gates are cleared.

### Allowed final outcomes

~~~text
FALSIFIED
SUBSTANTIALLY_NARROWED
SURVIVES_TARGETED_NOVELTY_AUDIT
INCONCLUSIVE
~~~

The workflow must never force SURVIVES.

## 21. Required structured artifacts

V2 defines the following machine-readable artifacts:

- D1_HISTORICAL_STATE_REGISTER
- D1_CLAIM_EVOLUTION_MATRIX
- D1_PAPER_EVIDENCE_PACKETS
- D1_PRIOR_ART_FAMILY_COVERAGE
- D1_PRIOR_ART_THREAT_MATRIX
- D1_NON_NOVELTY_REGISTER
- D1_NOVELTY_CANDIDATE_REGISTER
- D1_CONTRADICTION_REGISTER
- D1_K1_K9_FALSIFICATION_MATRIX
- D1_UNRESOLVED_THREAT_REGISTER
- D1_PROVENANCE_QA
- D1_FINAL_EVIDENCE_MAP
- D1_THRESHOLD_FREEZE_RECORD
- D1_HUMAN_REVIEW_RECORD
- D1_RED_TEAM_MATRIX
- D1_PLAN_REMEDIATION_MATRIX

The human-readable report must link every major claim to one of these artifacts.

## 22. Schema minimums

### D1_UNRESOLVED_THREAT_REGISTER

~~~text
threat_id
claim_id
threat_description
source_or_missing_source
why_material
required_resolution
search_trigger
status
blocking
owner
~~~

### D1_PROVENANCE_QA

~~~text
qa_id
claim_id
evidence_packet_id
source_chain
source_hash
locator_validation_status
source_precedence_check
unsupported_claim
result
reviewer
~~~

### D1_FINAL_EVIDENCE_MAP

~~~text
claim_id
claim_text
claim_category
claim_status
supporting_sources
supporting_packets
contradictions
K_test_rows
confidence
allowed_wording
prohibited_wording
~~~

### D1_PLAN_REMEDIATION_MATRIX

~~~text
audit_revision_id
severity
audit_problem
audit_required_change
V1_section
V2_change
V2_section
affected_artifacts
affected_workers
affected_models
resolved
deferred
defer_reason
residual_risk
re_audit_required
~~~

The complete matrix is provided in D1_MASTER_PLAN_REMEDIATION_CHECKLIST_V1.md and must be copied or linked into an execution package.


## 23. D1_V2_REAUDIT_FINDING_REGISTER

The authoritative source for this register is `outputs/plans/D1_MASTER_PLAN_REAUDIT_V2.md`. This register preserves every remaining blocking finding and every additional implementation finding identified by that re-audit.

### Register schema

```text
finding_id
origin: ORIGINAL_AUDIT | NEW_REAUDIT_FINDING
severity: CRITICAL | HIGH | MEDIUM | LOW
original_requirement
V2_defect
scientific_risk
exact_required_change
affected_stage
affected_worker
affected_schema
blocking: true | false
resolved_in_V3: true | false
V3_location
residual_risk
```

| finding_id | origin | severity | V2 defect and scientific risk | exact required change | affected stage/worker/schema | blocking | resolved_in_V3 | V3 location | residual risk |
|---|---|---|---|---|---|---|---|---|---|
| RA-01 | ORIGINAL_AUDIT | CRITICAL | CR-04 remained generic: K1-K9 had no per-test frozen kill or partial-overlap criteria; high-significance could be assigned after evidence. | Define and freeze separate K1-K9 criteria before evidence evaluation; require all nine rows to resolve or block adjudication. | S9-S10, S14-S15, W12, `D1_K1_K9_FALSIFICATION_MATRIX` | true | true | §§24, 29-31 | Criteria quality still depends on full-text access and human review. |
| RA-02 | ORIGINAL_AUDIT | HIGH | HI-06 remained incomplete: worker contracts lacked allowed/forbidden inference and reconciliation ownership; W04 Flash/Sol boundary was ambiguous. | Add a complete contract to every worker, assign one reconciliation and QA owner, and separate W04 extraction from Sol reconciliation. | S2-S13, W01-W12, `D1_WORKER_CONTRACT_REGISTER` | true | true | §25, §§30-31 | Human availability can still delay clearance. |
| RA-03 | ORIGINAL_AUDIT | HIGH | HI-08 remained incomplete: threat/red-team schemas were only named, and threshold freeze lacked boundary/data-timing fields. | Add concrete threat, red-team, search-log, threshold and clearance schemas; make S14/S16 validate them. | S5, S10-S16, W09-W12, schemas in §§26-29 | true | true | §§26-29, §§30-32 | Future data systems may expose additional schema details. |
| ME-05 | ORIGINAL_AUDIT | MEDIUM | Red-team artifact remained prose-capable without a row contract. | Add the complete `D1_RED_TEAM_MATRIX` schema and require one row per attack. | S12-S14, W12, `D1_RED_TEAM_MATRIX` | true | true | §26, §30 | New attack modes can still be added under `OTHER`. |
| RA-04 | NEW_REAUDIT_FINDING | MEDIUM | Human clearance and contradiction status were not machine-checkable. | Add enumerated statuses, sign-off fields and hard downstream blocking logic. | S8, S13-S16, W11-W12, `D1_HUMAN_REVIEW_CLEARANCE`, `D1_CONTRADICTION_REGISTER` | true | true | §§28-29, §30 | A blocked stage remains blocked until a human disposition exists. |
| NEW-MED-01 | NEW_REAUDIT_FINDING | MEDIUM | Search records were defined but not a named persistent deliverable. | Add `D1_SEARCH_DECISION_LOG` to outputs and make S10/S16 validate it. | S10, W10, `D1_SEARCH_DECISION_LOG` | false | true | §§30-32 | No broad search is permitted by this plan. |
| NEW-LOW-01 | NEW_REAUDIT_FINDING | LOW | Claim transitions used `provenance_pointer` without a dedicated evidence-packet ID. | Add `evidence_packet_ids` to the V3 transition contract. | S4, W04/W09, `D1_CLAIM_EVOLUTION_MATRIX` | false | true | §§25, 32 | A packet can still be unavailable and marked accordingly. |

V3 resolution counts are: remaining Critical 1/1 resolved, remaining High 2/2 resolved, remaining Medium 3/3 resolved or bounded, and remaining Low 1/1 resolved. `READY_TO_LAUNCH_GEMINI_WORKERS` remains false until D1-A3 independently re-audits V3.

## 24. K1-K9 operational falsification criteria

The K-test criteria are defined in V3 before any targeted evidence evaluation. For every row, `criterion_defined_at = V3 design freeze`, `criterion_frozen_at = S9 before S10`, `criterion_frozen_before_evidence_evaluation = true`, and `criterion_version = K-CRITERIA-V3.1`. Existing repository evidence may be inventoried earlier, but it may not be evaluated against a K-test until S9 has frozen that test's criteria.

Every row uses this schema:

```text
kill_test_id
scientific_question
candidate_claim_affected
test_scope
conceptual_equivalence_rule
DIRECT_KILL_CRITERION
PARTIAL_OVERLAP_CRITERION
NO_KILL_CRITERION
UNRESOLVED_CRITERION
required_evidence
minimum_evidence_quality
source_precedence
existing_repository_sources
targeted_search_trigger
human_review_trigger
criterion_defined_at
criterion_frozen_at
criterion_frozen_before_evidence_evaluation
criterion_version
verdict: KILL | PARTIAL_OVERLAP | NO_KILL_FOUND | UNRESOLVED
confidence
adjudication_notes
```

### K1

```yaml
kill_test_id: K1
scientific_question: Does a comparable continuum layer-jamming model already map its validity domain?
candidate_claim_affected: D1-CANDIDATE-M1-VALIDITY-DOMAIN
test_scope: Vacuum or mechanically equivalent layered-beam continuum/reduced models.
conceptual_equivalence_rule: Same reduced mechanics question and comparable interface/layer interaction, even with different terminology.
DIRECT_KILL_CRITERION: Full text maps accepted and breakdown regimes for an equivalent continuum layer-jamming model using a declared domain and quantitative comparison.
PARTIAL_OVERLAP_CRITERION: Equivalent model and applicability study exist, but domain, output, uncertainty or breakdown mapping is incomplete.
NO_KILL_CRITERION: Model description, qualitative applicability statement, or generic validation without a domain map.
UNRESOLVED_CRITERION: Full text or model meaning is unavailable or cannot distinguish validity mapping from ordinary case validation.
required_evidence: Model equations/assumptions, operating domain, validity criterion, breakdown evidence and source locators.
minimum_evidence_quality: VERIFIED_FULL_TEXT for direct or partial classification.
source_precedence: Original PDF > evidence JSON > AI summary; canonical JSON controls current repository state.
existing_repository_sources: D1-V001..D1-V009, data/evidence, data/papers, papers, data/search_exports.
targeted_search_trigger: Named K1 gap after repository screening or inaccessible high-threat source.
human_review_trigger: Direct/partial equivalent, KILL or UNRESOLVED.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder; execution must replace the verdict with an allowed final state.
```

### K2

```yaml
kill_test_id: K2
scientific_question: Does prior work compare a reduced model with a layer-resolved or full-contact reference over a meaningful domain?
candidate_claim_affected: D1-CANDIDATE-M-R-COMPARISON
test_scope: Reduced/continuum versus interface-resolved, discrete-layer or frictional-contact reference.
conceptual_equivalence_rule: The reference must resolve interface/layer physics relevant to the proposed reduced-model limitation, regardless of software name.
DIRECT_KILL_CRITERION: Prior full text compares an equivalent reduced model and higher-fidelity reference across pressure, layer count, loading or equivalent dimensions with quantitative outputs.
PARTIAL_OVERLAP_CRITERION: Comparison exists but lacks meaningful domain breadth, interface resolution, shared outputs or independent verification.
NO_KILL_CRITERION: Two models are merely mentioned, or a high-fidelity model is used without reduced-model comparison.
UNRESOLVED_CRITERION: Reference resolution or shared output cannot be verified.
required_evidence: Both model formulations, interface resolution, domain, shared outputs, quantitative comparison and locators.
minimum_evidence_quality: VERIFIED_FULL_TEXT.
source_precedence: Original PDF > evidence JSON > AI summary.
existing_repository_sources: D1-V001..D1-V009 and inventoried paper packets.
targeted_search_trigger: K2 comparison fields remain missing for a named threat.
human_review_trigger: Any claim that a different model is conceptually equivalent.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder.
```

### K3

```yaml
kill_test_id: K3
scientific_question: Is comparable model-form error already quantified for the same or equivalent mechanics problem?
candidate_claim_affected: D1-CANDIDATE-MODEL-FORM-ERROR
test_scope: Error attributable to model form rather than calibration, parameter fitting or measurement noise.
conceptual_equivalence_rule: Error decomposition and output definition must answer the same reduced-model validity question.
DIRECT_KILL_CRITERION: Full text isolates and quantifies output-specific model-form error against a higher-fidelity or independently justified reference over a declared domain.
PARTIAL_OVERLAP_CRITERION: Quantitative error exists but model-form isolation, output specificity, domain or uncertainty is incomplete.
NO_KILL_CRITERION: Generic percentage error, fit quality or calibration residual without model-form identification.
UNRESOLVED_CRITERION: The paper does not permit separation of model-form error from calibration or measurement error.
required_evidence: Error definition, reference, parameter treatment, uncertainty, domain, numerical values and locators.
minimum_evidence_quality: VERIFIED_FULL_TEXT.
source_precedence: Original PDF > evidence JSON > AI summary.
existing_repository_sources: D1-V001..D1-V009, evidence packets and canonical matrices.
targeted_search_trigger: A named error-comparison threat lacks full-text resolution.
human_review_trigger: Calibration/model-form ambiguity, KILL or UNRESOLVED.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder.
```

### K4

```yaml
kill_test_id: K4
scientific_question: Were valid and invalid/breakdown regimes deliberately identified before final outcomes were observed?
candidate_claim_affected: D1-CANDIDATE-VALIDITY-BREAKDOWN-MAP
test_scope: Predeclared regime classification and deliberate sampling of both regimes.
conceptual_equivalence_rule: A regime map counts only when classification is tied to an explicit criterion, not retrospective narrative.
DIRECT_KILL_CRITERION: Prior work predeclares valid/breakdown criteria and deliberately tests both sides over a meaningful operating domain.
PARTIAL_OVERLAP_CRITERION: Two regimes are discussed, but one side is absent, criteria are incomplete, or the boundary is retrospective.
NO_KILL_CRITERION: Single-regime validation or qualitative failure report without a declared boundary.
UNRESOLVED_CRITERION: Timing of criteria or regime selection cannot be established.
required_evidence: Predeclared criterion, sampling plan/domain, results on both sides, timing and uncertainty.
minimum_evidence_quality: VERIFIED_FULL_TEXT with temporal evidence.
source_precedence: Original PDF > evidence JSON > AI summary.
existing_repository_sources: D1-V001..D1-V009 and verified full-text packets.
targeted_search_trigger: Regime-boundary timing or two-sided testing is unresolved.
human_review_trigger: Retrospective-boundary allegation, KILL or UNRESOLVED.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder.
```

### K5

```yaml
kill_test_id: K5
scientific_question: Did an independent experiment deliberately sample both sides of a predicted validity boundary?
candidate_claim_affected: D1-CANDIDATE-EXPERIMENTAL-BOUNDARY-TEST
test_scope: Experiment independent of model calibration and spanning predicted accepted and breakdown regimes.
conceptual_equivalence_rule: Both sides requires a boundary predicted before final validation data are inspected and a shared measurable output.
DIRECT_KILL_CRITERION: Prior study predicts a boundary, freezes the criterion, and independently measures the same output on both sides with uncertainty.
PARTIAL_OVERLAP_CRITERION: Independent experiment exists but samples only one side, uses a post-hoc boundary, or lacks shared-output/uncertainty evidence.
NO_KILL_CRITERION: Experiment validates isolated points or tests a different question without boundary sampling.
UNRESOLVED_CRITERION: Independence, prediction timing or side-of-boundary classification cannot be verified.
required_evidence: Prediction timing, experimental design, shared output, both-side samples, uncertainty and locators.
minimum_evidence_quality: VERIFIED_FULL_TEXT.
source_precedence: Original PDF > evidence JSON > AI summary.
existing_repository_sources: D1-V001..D1-V009 and experiment-related packets.
targeted_search_trigger: Named boundary-crossing experiment remains unresolved.
human_review_trigger: Independence or post-hoc-boundary dispute, KILL or UNRESOLVED.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder.
```

### K6

```yaml
kill_test_id: K6
scientific_question: Is reduced-model failure mechanistically attributed to contact, slip, separation or related interface physics?
candidate_claim_affected: D1-CANDIDATE-MECHANISTIC-FAILURE-EXPLANATION
test_scope: Local interface/contact evidence connected to model discrepancy.
conceptual_equivalence_rule: The mechanism must be relevant to the same interface physics, not merely share a word such as slip.
DIRECT_KILL_CRITERION: Prior work links discrepancy to locally evidenced contact, slip, separation or pressure-redistribution behavior with a defensible causal chain.
PARTIAL_OVERLAP_CRITERION: Mechanism is discussed or consistently correlated but lacks local evidence or causal discrimination.
NO_KILL_CRITERION: Pressure/error or slip/error correlation alone, or a generic mechanism assertion.
UNRESOLVED_CRITERION: Mechanism evidence is inaccessible, contradictory or only inferential.
required_evidence: Local mechanism observation/field, discrepancy linkage, alternative explanations and locators.
minimum_evidence_quality: VERIFIED_FULL_TEXT; causal claims require stronger evidence than correlation.
source_precedence: Original PDF > evidence JSON > AI summary.
existing_repository_sources: D1-V001..D1-V009 and mechanism packets.
targeted_search_trigger: Mechanism attribution is named as a surviving claim but not resolved.
human_review_trigger: Causal-evidence claim, KILL or UNRESOLVED.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder.
```

### K7

```yaml
kill_test_id: K7
scientific_question: Has an equivalent M → R → E workflow already been applied to vacuum layer-jamming beams?
candidate_claim_affected: D1-CANDIDATE-M-R-E-WORKFLOW
test_scope: Vacuum layer-jamming beam studies using a specified reduced model, higher-fidelity reference and independent experiment.
conceptual_equivalence_rule: Terminology may differ, but all three roles and the same validity/breakdown question must be substantively present.
DIRECT_KILL_CRITERION: One paper or defensible paper chain performs the equivalent M→R→E workflow for vacuum layer-jamming beams and evaluates validity/breakdown.
PARTIAL_OVERLAP_CRITERION: Two roles or an adjacent application are equivalent, but the complete workflow or scientific question is incomplete.
NO_KILL_CRITERION: Generic model validation or separate experiments without M→R→E structure.
UNRESOLVED_CRITERION: One role or conceptual equivalence cannot be verified from full text.
required_evidence: Role mapping for M, R and E, beam/vacuum context, validity question, outputs and locators.
minimum_evidence_quality: VERIFIED_FULL_TEXT for direct kill; adjacent evidence may only support partial overlap.
source_precedence: Original PDF > evidence JSON > AI summary.
existing_repository_sources: D1-V001..D1-V009, named-target audits and paper packets.
targeted_search_trigger: Named M→R→E threat is unresolved.
human_review_trigger: Conceptual-equivalence claim, KILL or UNRESOLVED.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder.
```

### K8

```yaml
kill_test_id: K8
scientific_question: Does prior methodology make D1 routine rather than scientifically substantive?
candidate_claim_affected: D1-CANDIDATE-SCIENTIFIC-CONTRIBUTION
test_scope: Whether the proposed combination adds a new mechanics question beyond ordinary validation workflow.
conceptual_equivalence_rule: A method is equivalent only when it resolves the same scientific validity/breakdown question, not merely uses the same tools.
DIRECT_KILL_CRITERION: Prior methodology already supplies the same substantive mechanics question, evidence structure and decision logic, leaving only routine implementation.
PARTIAL_OVERLAP_CRITERION: Prior methodology makes much of the workflow routine but leaves a distinct unresolved mechanics question or interface regime.
NO_KILL_CRITERION: Prior work shares ordinary methods but not the same scientific question or falsifiable boundary.
UNRESOLVED_CRITERION: Scientific contribution cannot be separated from workflow sophistication using available evidence.
required_evidence: Prior method purpose, scientific question, model/reference/experiment roles, decision logic and contribution limits.
minimum_evidence_quality: VERIFIED_FULL_TEXT plus Sol synthesis; absence alone cannot yield a kill.
source_precedence: Original PDF > evidence JSON > AI summary.
existing_repository_sources: D1-V001..D1-V009 and cross-family packets.
targeted_search_trigger: Candidate remains supported only by method combination.
human_review_trigger: Novelty migration, KILL or UNRESOLVED.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder.
```

### K9

```yaml
kill_test_id: K9
scientific_question: Does conceptually equivalent work under different terminology directly pre-empt D1?
candidate_claim_affected: D1-CANDIDATE-CROSS-TERMINOLOGY-NOVELTY
test_scope: Adjacent mechanics terminology including composite/partial-interaction, homogenized, reduced-order, interface-contact, slip and applicability studies.
conceptual_equivalence_rule: Structural mechanics question and evidence chain control equivalence; exact title or keyword match is unnecessary.
DIRECT_KILL_CRITERION: Different terminology hides a study that substantively answers the same surviving D1 question with comparable model, reference, domain, boundary and evidence.
PARTIAL_OVERLAP_CRITERION: Adjacent study covers material components of D1 but leaves a distinct vacuum/layer-jamming or boundary-crossing question.
NO_KILL_CRITERION: Superficial terminology, different mechanics question or generic analogy without the required evidence chain.
UNRESOLVED_CRITERION: Terminology translation or full-text meaning remains ambiguous.
required_evidence: Synonym map, model/question mapping, domain, outputs, evidence status and locators.
minimum_evidence_quality: VERIFIED_FULL_TEXT for direct equivalence; metadata can only nominate a source.
source_precedence: Original PDF > evidence JSON > AI summary.
existing_repository_sources: D1-V001..D1-V009 and adjacent-family packets.
targeted_search_trigger: Current-title search is insufficient for a named K9 threat.
human_review_trigger: Conceptual equivalence, KILL or UNRESOLVED.
criterion_defined_at: V3 design freeze
criterion_frozen_at: S9
criterion_frozen_before_evidence_evaluation: true
criterion_version: K-CRITERIA-V3.1
verdict: UNRESOLVED
confidence: UNRESOLVED
adjudication_notes: Pre-execution placeholder.
```

### KILL_CRITERION_CHANGE_RECORD

No K criterion may be edited after S9. Any necessary change must create a `KILL_CRITERION_CHANGE_RECORD` before further classification:

```text
change_id
kill_test_id
reason
old_criterion
new_criterion
evidence_already_seen
bias_risk
human_approval
approved_at
criterion_version_before
criterion_version_after
```

If human approval is absent, the affected K-test is `UNRESOLVED` and its dependent adjudication is blocked. The sequence `inspect evidence -> modify criterion -> classify result` is forbidden.

## 25. Worker contract register

Every worker uses this contract. `allowed_inference`, `forbidden_inference` and `must_not_conclude` are binding; every output must label statements `VERIFIED`, `INFERENCE` or `HYPOTHESIS`.

```text
worker_id
role
scientific_question
exclusive_scope
input_files
input_papers
required_outputs
output_schema
dependencies
parallelizable
allowed_inference
forbidden_inference
must_not_conclude
reconciliation_owner
QA_owner
human_review_trigger
model
reasoning_effort
clearance_status
```

Global forbidden inferences: absence of a discovered paper -> global novelty; abstract-only result -> full mechanics conclusion; correlation -> causation; better fit -> new mechanics; H0a rejected -> H1 true; citation coverage closed -> scientific threat resolved.

| worker_id | role and exclusive scope | inputs / input_papers | required output / schema | dependencies / parallel | allowed inference | forbidden inference / must_not_conclude | reconciliation_owner / QA_owner | human-review trigger | model / reasoning | clearance |
|---|---|---|---|---|---|---|---|---|---|---|
| W01 | Scope, plan hash and repository provenance only. | V3, HEAD, git status, authority paths / none. | `scope_lock`, `repository_manifest`, `plan_hash_record`. | none / false. | Verify paths, hashes, scope and dirty-state identity. | Must not interpret novelty or paper meaning. | W11 / deterministic S16. | Scope or hash conflict. | Deterministic / none. | PENDING |
| W02 | Artifact inventory and D1-V001...V009 round coverage only. | D1 directories, manifests / none. | `D1_EVIDENCE_INVENTORY`, `D1_ROUND_COVERAGE`. | W01 / true. | Classify artifact type, source status and round presence. | Must not infer scientific coverage from filenames. | W11 / W11. | Missing or unclassifiable round. | Gemini Flash / High. | PENDING |
| W03 | Historical state-at-time reconstruction only. | Handoff, log, state JSON, V001-V009 / none. | `D1_HISTORICAL_STATE_REGISTER`. | W02 / false. | Bind historical claims to contemporaneous evidence and status. | Must not rewrite a prior state using later verdicts or adjudicate novelty. | W09 / W11. | Supersession or historical/current conflict. | Gemini Flash / High. | PENDING |
| W04 | Claim-transition extraction only; no scientific synthesis. | W03 register, round verdicts, prompts / papers cited by transitions. | Draft `D1_CLAIM_EVOLUTION_MATRIX` with `evidence_packet_ids`. | W03 / false. | Extract claim-before/threat/source/decision/claim-after and provenance. | Must not decide survival, global novelty or causal mechanism. | W09 Sol reconciliation / W11. | Missing source or disputed transition. | Gemini Flash / High. | PENDING |
| W05 | Direct layer-jamming evidence packet extraction. | PDFs and repository packets / assigned papers only. | `D1_PAPER_EVIDENCE_PACKETS` rows and family tags. | W02 / true. | Report paper-level model, method, experiment and evidence status. | Must not adjudicate D1 or generalize absence. | W09 / W11. | Direct kill or conceptual-equivalence candidate. | Gemini Flash / High. | PENDING |
| W06 | Continuum, homogenization, Cosserat/generalized-continuum evidence. | PDFs and packets / assigned papers only. | Evidence packets and family rows. | W02 / true. | Extract equations, assumptions, domain and overlap. | Must not promote mathematical similarity to scientific equivalence. | W09 / W11. | Ambiguous model equivalence. | Gemini Flash / High. | PENDING |
| W07 | Contact, partial-interaction and full-layer evidence. | PDFs and packets / assigned papers only. | Evidence packets and family rows. | W02 / true. | Identify interface resolution, contact/slip and reference role. | Must not treat any FE result as unquestioned truth or a kill by itself. | W09 / W11. | Reference fidelity or mechanism ambiguity. | Gemini Flash / High. | PENDING |
| W08 | Validity, model-form error and uncertainty evidence. | PDFs and packets / assigned papers only. | Evidence packets and validity/error rows. | W02 / true. | Extract declared metrics, thresholds, regimes and uncertainty. | Must not choose thresholds after outcomes or infer causality from correlation. | W09 / W11. | Retrospective threshold or calibration/model-form ambiguity. | Gemini Flash / High. | PENDING |
| W09 | Cross-worker claim, non-novelty and candidate reconciliation. | W03-W08 outputs / all assigned papers. | `D1_CLAIM_EVOLUTION_MATRIX`, `D1_NON_NOVELTY_REGISTER`, `D1_NOVELTY_CANDIDATE_REGISTER`. | W03-W08 / false. | Reconcile verified packets into claims and categories; preserve disagreement. | Must not erase conflicts, bypass provenance or declare final novelty. | W11 / W11. | Worker disagreement or material candidate change. | GPT-6 Sol / High. | PENDING |
| W10 | Conditional targeted search and threat integration. | Candidate register, unresolved threats, frozen K criteria / only named triggered sources. | `D1_SEARCH_DECISION_LOG`, `D1_PRIOR_ART_THREAT_MATRIX`, unresolved register. | W09 and S9 / conditional. | Screen triggered sources using frozen criteria and synonym families. | Must not launch broad search or treat no hit as global absence. | W11 / W11. | New high-threat or conceptual-equivalence source. | Gemini Flash + Sol / High. | PENDING |
| W11 | Provenance, contradiction, threshold and gate QA. | W01-W10 artifacts / all cited sources. | `D1_PROVENANCE_QA`, `D1_CONTRADICTION_REGISTER`, `D1_THRESHOLD_FREEZE_REGISTER`, gate statuses. | W10 / false. | Validate chains, locators, statuses and freeze timing; classify conflicts. | Must not silently reconcile or change K criteria after S9. | W12/S14 / deterministic S16. | Critical contradiction, threshold change or missing clearance. | Deterministic + Sol / High for interpretation. | PENDING |
| W12 | Astra adversarial K1-K9 and red-team challenge only. | All prior artifacts and frozen criteria / high-threat packets. | `D1_K1_K9_FALSIFICATION_MATRIX`, `D1_RED_TEAM_MATRIX`. | W11 / false. | Attempt KILL, PARTIAL_OVERLAP and failure classifications using cited evidence. | Must not approve survival with unresolved K-test or human gate; must not extract routine packets. | S14 Sol draft / S16. | KILL, UNRESOLVED, candidate collapse or material conflict. | GPT-6 Astra / High; xHigh only S15 conflict. | PENDING |
```

W04 is explicitly two-step: Flash extracts rows; W09/S4 Sol reconciles them. W05-W08 may share a paper, but W09 owns deduplication and packet identity. W11 owns structural QA; W12 owns adversarial interpretation; S14 owns synthesis. No worker may conclude final novelty alone.

### V3 transition linkage override

Every V3 claim-transition row must include `evidence_packet_ids` in addition to `provenance_pointer`. Each ID must resolve to a row in `D1_PAPER_EVIDENCE_PACKETS`; an unavailable packet must be explicitly marked `UNAVAILABLE` and cannot support a survival claim.
## 26. D1_PRIOR_ART_THREAT_MATRIX schema

```json
{
  "threat_id": "D1-TH-001",
  "candidate_claim_id": "D1-CANDIDATE-001",
  "paper_id": "string",
  "title": "string",
  "authors": ["string"],
  "year": 2025,
  "DOI": "string|null",
  "repository_path": "string",
  "prior_art_family": "string",
  "reason_investigated": "string",
  "conceptual_overlap": "string",
  "system_overlap": "string",
  "mechanism_overlap": "string",
  "model_overlap": "string",
  "method_overlap": "string",
  "validation_overlap": "string",
  "scientific_question_overlap": "string",
  "operating_domain_overlap": "string",
  "higher_fidelity_reference_present": false,
  "experiment_present": false,
  "validity_domain_mapped": false,
  "breakdown_deliberately_tested": false,
  "model_form_error_quantified": false,
  "mechanism_failure_explained": false,
  "what_it_proves": "string",
  "what_it_does_not_prove": "string",
  "direct_kill_candidate": false,
  "partial_overlap": false,
  "K_test_links": ["K1"],
  "evidence_pointer": "repository/path#page-or-section",
  "evidence_status": "VERIFIED_FULL_TEXT|METADATA_ONLY|INFERENCE|HYPOTHESIS|UNAVAILABLE",
  "confidence": "low|medium|high",
  "human_review_required": false,
  "final_disposition": "OPEN|PARTIAL_OVERLAP|KILL|NO_KILL|UNRESOLVED"
}
```

Every threat row must feed both `D1_NOVELTY_CANDIDATE_REGISTER` and the linked K1-K9 rows. A row cannot kill a candidate without source-level evidence and, where required, human clearance.

## 27. D1_RED_TEAM_MATRIX schema

```json
{
  "red_team_id": "D1-RT-001",
  "candidate_claim_id": "D1-CANDIDATE-001",
  "attack_type": "NOVELTY_MIGRATION|CONCEPTUAL_EQUIVALENCE|SEARCH_BIAS|ABSENCE_OF_EVIDENCE|METHOD_COMBINATION|MODEL_VALIDATION_VS_VALIDITY|THRESHOLD_LEAKAGE|CAUSAL_OVERCLAIM|PROVENANCE_FAILURE|HISTORICAL_HINDSIGHT|WORKER_DISAGREEMENT|OTHER",
  "attack_question": "string",
  "assumption_attacked": "string",
  "supporting_evidence": ["packet-or-source-id"],
  "counter_evidence": ["packet-or-source-id"],
  "logical_failure_mode": "string",
  "prior_art_dependency": "string",
  "provenance_dependency": "string",
  "threshold_dependency": "string",
  "mechanism_dependency": "string",
  "potential_outcome": "SURVIVES|NARROWS|KILLS|INCONCLUSIVE",
  "severity": "LOW|MEDIUM|HIGH|CRITICAL",
  "Astra_assessment": "string",
  "Sol_reconciliation": "string",
  "human_review_required": true,
  "resolution": "string",
  "residual_risk": "string",
  "status": "OPEN|ADJUDICATED|BLOCKED|CLEARED"
}
```

S12/W12 must create at least one row for each applicable attack type. S14 must consume every HIGH or CRITICAL row, and S16 must reject a package with an open blocking row.

## 28. D1_THRESHOLD_FREEZE_REGISTER

```json
{
  "threshold_id": "D1-THRESHOLD-001",
  "metric": "string",
  "physical_meaning": "string",
  "used_for": "VALIDITY_CLASSIFICATION|BREAKDOWN_CLASSIFICATION|OTHER",
  "justification_source": ["source-or-design-record"],
  "uncertainty_basis": "string",
  "acceptance_threshold": "number-or-rule",
  "breakdown_threshold": "number-or-rule",
  "validity_boundary_definition": "string",
  "breakdown_criterion": "string",
  "defined_at_stage": "S11",
  "frozen_at_stage": "S11",
  "frozen_before_final_validation_data": true,
  "validation_data_seen_before_freeze": false,
  "version": "TF-V3.1",
  "change_allowed": true,
  "change_requires_human_review": true,
  "change_record": "D1-THRESHOLD-CHANGE-001|null"
}
```

Hard rules: acceptance tolerance, validity boundary and breakdown criterion are frozen before final validation data used for classification are inspected; seeing data before freeze creates `BIAS_RISK`, blocks a survival classification and requires cleared human review; every change creates a versioned record and never overwrites the prior commitment.

## 29. Human review clearance and hard gates

### D1_HUMAN_REVIEW_CLEARANCE schema

```json
{
  "review_id": "D1-REVIEW-001",
  "gate": "K_TEST|CONTRADICTION|THRESHOLD|FINAL_ADJUDICATION|OTHER",
  "trigger": "string",
  "artifact_under_review": "string",
  "claim_id": "string|null",
  "K_test_id": "K1..K9|null",
  "review_required": true,
  "reviewer": "string|null",
  "review_date": "ISO-8601|null",
  "decision": "APPROVED|REJECTED|REVISION_REQUIRED|NOT_REVIEWED",
  "conditions": ["string"],
  "evidence_reviewed": ["source-or-packet-id"],
  "sign_off_status": "PENDING|CLEARED|BLOCKED",
  "notes": "string"
}
```

If `review_required = true` and `sign_off_status != CLEARED`, the dependent stage is `BLOCKED`. Required clearance applies to direct-kill candidates, conceptual equivalents, critical contradictions, KILL or UNRESOLVED K-tests, material candidate changes, threshold changes after freeze and final pre-adjudication sign-off. S16 validates that no required review is PENDING or BLOCKED.

### V3 contradiction status control

`D1_CONTRADICTION_REGISTER.status` is restricted to `OPEN`, `ADJUDICATED`, `BLOCKED` or `WAIVED_WITH_JUSTIFICATION`. A row may be `WAIVED_WITH_JUSTIFICATION` only when a human clearance record cites the evidence, reason and residual uncertainty. Any `OPEN` or `BLOCKED` critical row fails HG-03. `resolved_source`, `resolution` and `residual_uncertainty` are mandatory when status is `ADJUDICATED`.
### D1_HARD_GATE_MATRIX schema and gates

```text
gate_id
gate_name
required_inputs
pass_condition
fail_condition
blocked_stage
machine_checkable
human_clearance_required
status: OPEN | PASSED | BLOCKED | WAIVED_WITH_JUSTIFICATION
```

| gate_id | gate_name | required_inputs | pass condition | fail condition | blocked stage | machine-checkable | human clearance |
|---|---|---|---|---|---|---|---|
| HG-01 | Historical completeness | `D1_ROUND_COVERAGE`, `D1_HISTORICAL_STATE_REGISTER` | Discovery, V001-V009 and current rows complete with evidence. | Missing round, state-at-time or source. | S4 onward | true | true for corrections |
| HG-02 | Provenance QA | `D1_PROVENANCE_QA` | No orphan thesis-critical claim; locators and precedence pass. | Unsupported claim, invalid locator or missing hash. | S8 onward | true | false unless exception |
| HG-03 | Critical contradiction clearance | `D1_CONTRADICTION_REGISTER`, clearances | No critical row open or blocked. | Any critical unresolved row. | S14 onward | true | true |
| HG-04 | K1-K9 criterion freeze | nine criterion rows, change records | All nine criteria frozen before S10 evaluation. | Missing or modified criterion without approved change record. | S10 onward | true | true for changes |
| HG-05 | K1-K9 resolution | K matrix | Every K1-K9 row has KILL, PARTIAL_OVERLAP or NO_KILL_FOUND, or cleared review classifies the candidate INCONCLUSIVE. | Any unresolved row used for survival or missing row. | S14 onward | true | true |
| HG-06 | Threshold freeze | Threshold register | Boundary, criterion and tolerance frozen before final validation data. | Data seen before freeze or missing uncertainty basis. | S12 onward | true | true |
| HG-07 | Prior-art threat completion | Threat matrix, unresolved register | Every material threat has disposition and evidence status. | High-threat row open without documented unavailability. | S9 onward | true | true for direct kills |
| HG-08 | Red-team completion | Red-team matrix | Applicable attack types closed; high/critical rows reconciled. | Open blocking attack or missing matrix row. | S14 onward | true | true |
| HG-09 | Human review clearance | Human clearance register | All required reviews are CLEARED. | Any required review pending, blocked or rejected. | S14 onward | true | true |
| HG-10 | Final adjudication readiness | HG-01...HG-09 and final evidence map | All gates pass; no unsupported claim; outcome space remains open. | Any blocking gate fails. | S15 | true | true |

At initialization every gate row has `status = OPEN`; S16 computes and writes `PASSED`, `BLOCKED` or `WAIVED_WITH_JUSTIFICATION` only under the rules above. Gate status is computed, not narrated. A failed gate may not be bypassed by a worker or by S14 prose.

### D1_SEARCH_DECISION_LOG schema

```json
{
  "search_id": "D1-SEARCH-001",
  "trigger": "K1-K9 gap|historical provenance gap|named high-threat full-text gap|conceptual-equivalence threat",
  "scientific_question": "string",
  "query_family": "string",
  "query_terms": ["string"],
  "synonyms": ["string"],
  "database_or_source": "string",
  "date": "ISO-8601",
  "screening_rule": "string",
  "dedup_rule": "SHA256|DOI|normalized-title",
  "full_text_promotion_rule": "string",
  "stop_condition": "string",
  "human_review_trigger": "string",
  "closure_reason": "string",
  "status": "OPEN|CLOSED|BLOCKED|NO_SOURCE_AVAILABLE",
  "sources_promoted": ["paper-or-packet-id"]
}
```

S10 may create this artifact only after a named trigger. A search row with no trigger, stop condition or closure reason fails HG-07 and HG-10.
## 30. V3 dependency graph and execution stages

The V3 graph supersedes conflicting V2 sequencing:

```text
S0 scope/provenance lock
  ↓
S1 historical inventory and round coverage
  ↓
S2 historical state reconstruction
  ↓
S3 repository paper evidence packets
  ↓
S4 claim evolution
  ↓
S5 prior-art threat matrix
  ↓
S6 non-novelty register
  ↓
S7 novelty-candidate register
  ↓
S8 provenance QA and contradiction detection/resolution
  ↓
S9 K1-K9 criterion freeze (before K-test evidence evaluation)
  ↓
S10 conditional targeted evidence/search and K-test evaluation
  ↓
S11 threshold freeze before final validation-data classification
  ↓
S12 red-team matrix
  ↓
S13 human-review clearance
  ↓
S14 Sol scientific synthesis and Astra challenge
  ↓
S15 final D1 adjudication
  ↓
S16 deterministic packaging and hard-gate QA
```

No downstream stage may bypass a failed hard gate. S3 may inventory existing repository evidence before S9, but S10 is the first stage allowed to classify evidence against frozen K1-K9 criteria. S11 is a planning/control stage only; it does not execute experiments or inspect future validation data in this remediation task.

| stage | objective | output | model/reasoning | dependency | pass condition |
|---|---|---|---|---|---|
| S0 | Bind V3, HEAD, dirty state and scope. | Manifest, scope lock, hashes. | Deterministic / none. | none | HG-01 inputs identified. |
| S1 | Inventory D1 artifacts and rounds. | Evidence inventory, round coverage. | Gemini Flash / High. | S0 | All rounds and paths accounted for. |
| S2 | Preserve state-at-time history. | Historical register. | Gemini Flash + Sol / High. | S1 | No hindsight rewrite; HG-01 pass. |
| S3 | Extract source-bound repository packets. | Paper packets. | Gemini Flash / High. | S1-S2 | Required fields and locators present. |
| S4 | Reconstruct claim transitions. | Claim evolution matrix. | Flash extraction; Sol reconciliation / High. | S2-S3 | Every transition links packet IDs. |
| S5 | Build complete threat matrix. | Threat matrix, family coverage. | Flash screening + Sol integration / High. | S3-S4 | Every material threat has a row. |
| S6 | Register established non-novel components. | Non-novelty register. | Sol / High. | S4-S5 | Components cannot migrate silently. |
| S7 | Register candidate surviving claims. | Candidate register. | Sol / High. | S6 | Every candidate has threats and kill conditions. |
| S8 | Validate provenance and resolve contradictions. | Provenance QA, contradiction register. | Deterministic + Sol / High. | S5-S7 | HG-02 and HG-03 pass or block. |
| S9 | Freeze K1-K9 criteria. | K criteria rows and change-record baseline. | Sol + Astra High review / High. | S8 | HG-04 pass before K evaluation. |
| S10 | Evaluate existing evidence; run only triggered targeted search. | K matrix, search log, updated threat rows. | Flash retrieval + Sol integration / High. | S9 | No open-ended search; K rows populated. |
| S11 | Freeze thresholds and boundary definitions. | Threshold freeze register. | Sol + deterministic timing check / High. | S10 | HG-06 pass; no pre-freeze validation data. |
| S12 | Attack candidates and assumptions. | Red-team matrix. | Astra / High. | S10-S11 | HG-08 pass. |
| S13 | Obtain explicit human clearance. | Human clearance records. | Human gate; deterministic status check. | S8, S10-S12 | HG-09 pass. |
| S14 | Integrate evidence and adversarial challenge. | Final evidence map, synthesis draft. | Sol High + Astra High; xHigh only material conflict. | S13 | HG-01...HG-09 pass. |
| S15 | Issue a D1-only outcome. | Final adjudication JSON/MD. | Sol High with Astra challenge; xHigh conditional. | S14 | HG-10 pass; negative outcomes remain allowed. |
| S16 | Validate schemas, counts, hashes and non-overwrite. | Execution QA and package manifest. | Deterministic / none. | S15 | All required artifacts parse and gates pass. |

## 31. Updated model allocation and cost control

| work | model | reasoning | justification | cost |
|---|---|---|---|---|
| Scope, hashes, schema and gate checks | Deterministic | none | No scientific inference is needed. | LOW |
| Inventory, history and paper packet population | Gemini 3.8 Flash | High | High-volume structured extraction. | LOW-MODERATE |
| Claim evolution, threat integration and contradiction synthesis | GPT-6 Sol | High | Cross-worker scientific reconciliation. | MODERATE-HIGH |
| K-criteria review and red-team attack | GPT-6 Astra | High | Adversarial fatal-gap analysis. | HIGH |
| Final high-stakes conflict only | GPT-6 Astra | xHigh conditional | Use only for unresolved material disagreement at S15. | VERY_HIGH conditional |

Astra is forbidden for routine extraction, schema population, formatting or bibliography construction. Existing repository evidence is consumed before any triggered search. Deduplicate by SHA256, DOI and normalized title; cache packets; pass only source-bound packets to reasoning stages; and stop each targeted search when its named trigger is closed or documented unavailable.

## 32. Required V3 artifacts and schema linkage

The execution package must contain:

- `D1_V2_REAUDIT_FINDING_REGISTER.json`
- `D1_V2_TO_V3_REMEDIATION_MATRIX.json`
- `D1_V2_TO_V3_REMEDIATION_MATRIX.md`
- `D1_V2_REAUDIT_FINDING_REGISTER.json`
- `D1_WORKER_CONTRACT_REGISTER.json`
- `KILL_CRITERION_CHANGE_RECORD.jsonl`
- `repository_manifest.json`
- `scope_lock.json`
- `plan_hash_record.json`
- `D1_EVIDENCE_INVENTORY.json`
- `D1_ROUND_COVERAGE.json`
- `D1_HISTORICAL_STATE_REGISTER.json`
- `D1_CLAIM_EVOLUTION_MATRIX.json`
- `D1_PAPER_EVIDENCE_PACKETS.jsonl`
- `D1_PRIOR_ART_FAMILY_COVERAGE.json`
- `D1_PRIOR_ART_THREAT_MATRIX.json`
- `D1_NON_NOVELTY_REGISTER.json`
- `D1_NOVELTY_CANDIDATE_REGISTER.json`
- `D1_CONTRADICTION_REGISTER.json`
- `D1_K1_K9_FALSIFICATION_MATRIX.json`
- `D1_SEARCH_DECISION_LOG.json`
- `D1_THRESHOLD_FREEZE_REGISTER.json`
- `D1_RED_TEAM_MATRIX.json`
- `D1_HUMAN_REVIEW_CLEARANCE.json`
- `D1_HARD_GATE_MATRIX.json`
- `D1_UNRESOLVED_THREAT_REGISTER.json`
- `D1_PROVENANCE_QA.json`
- `D1_FINAL_EVIDENCE_MAP.json`
- `FINAL_D1_NOVELTY_ADJUDICATION.json`
- `FINAL_D1_NOVELTY_ADJUDICATION.md`

No D1-V001...D1-V009 directory may be overwritten. No final artifact may claim universal novelty, and no artifact may promote `UNRESOLVED` to `SURVIVES_TARGETED_NOVELTY_AUDIT`.

## 33. V2->V3 remediation matrix summary

The machine-readable and Markdown matrices are the authoritative change ledger. Each record includes the re-audit requirement, exact V2 defect, V3 location, affected schema/stage/worker, resolved status and residual risk.

| remediation_id | severity | source finding | V3 correction | resolved |
|---|---|---|---|---|
| RA-01 | CRITICAL | CR-04 / generic K gate | Nine frozen, individually specified K criteria; change record; all-row hard gate. | true |
| RA-02 | HIGH | HI-06 / incomplete worker contract | Full W01-W12 contract, inference limits, owners and W04 split. | true |
| RA-03 | HIGH | HI-08 / missing schemas and threshold timing | Threat, red-team, search, threshold and clearance schemas plus graph gates. | true |
| ME-05 | MEDIUM | Original red-team schema omission | Concrete red-team matrix and S12/S16 validation. | true |
| RA-04 | MEDIUM | Human/contradiction clearance gap | Machine-checkable review and contradiction status/clearance. | true |
| NEW-MED-01 | MEDIUM | Search-log packaging gap | Named search decision log in S10 and deliverables. | true |
| NEW-LOW-01 | LOW | Packet-link refinement | Dedicated packet IDs in transitions. | true |

## 34. Remaining risks and scope lock

Residual risks after V3 remediation:

- Full-text unavailability can still force a K-test to `UNRESOLVED` and block survival.
- Human review is an external dependency; missing clearance blocks downstream work.
- Targeted search cannot prove global literature absence.
- Mechanistic attribution may remain `HYPOTHESIS` or `MECHANISTIC_CONSISTENCY` rather than causal evidence.
- A threshold change after freeze creates a new version and bias review; it cannot silently update the prior record.
- The final adjudicator may return `FALSIFIED`, `SUBSTANTIALLY_NARROWED`, `SURVIVES_TARGETED_NOVELTY_AUDIT` or `INCONCLUSIVE`.

```text
PLAN_VERSION = V3
SOURCE_PLAN = V2
SOURCE_REAUDIT = D1_MASTER_PLAN_REAUDIT_V2
STATUS = PENDING_REAUDIT
STAGE 1 SCOPE = D1 NOVELTY ONLY
MP1 ANALYSIS = NOT STARTED
D1-vs-MP1 COMPARISON = NOT STARTED
MENTOR REPORT = OUT OF SCOPE
SCIENTIFIC EXECUTION = NOT STARTED
THIS TASK = PLAN REMEDIATION ONLY
```

## 35. Required next action

Run an independent D1-A3 re-audit of this V3 with GPT-6 Astra at High reasoning. Do not launch Gemini workers or execute any scientific evidence workflow before that re-audit passes.

Historical V3 status block retained for provenance only; the final V4 status block at end of file is authoritative.

# D1 MASTER PLAN VERSION

V3

# SOURCE PLAN

V2

# SOURCE RE-AUDIT

D1_MASTER_PLAN_REAUDIT_V2

# REMAINING CRITICAL FINDINGS RESOLVED

1/1

# REMAINING HIGH FINDINGS RESOLVED

2/2

# REMAINING MEDIUM FINDINGS RESOLVED OR ACCEPTABLY DEFERRED

3/3

# NEW BLOCKING FINDINGS UNRESOLVED

0

# READY FOR RE-AUDIT

true

# READY TO LAUNCH GEMINI WORKERS

false

# NEXT ACTION

INDEPENDENT RE-AUDIT OF D1 MASTER PLAN V3 USING GPT-6 ASTRA HIGH

# MP1 ANALYSIS

NOT PART OF THIS TASK

# D1-vs-MP1 COMPARISON

NOT STARTED

## 36. V4 remediation identity and authoritative precedence

This overlay is the V4 correction of the exact V3 plan audited in
`D1_MASTER_PLAN_REAUDIT_V3.md`. V3 remains preserved and read-only. Sections
36 onward are the only authoritative execution controls for V4; inherited V3
controls remain historical provenance and are not a second executable graph.

`PLAN_VERSION: V4
SOURCE_PLAN_VERSION: V3
SOURCE_PLAN: outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V3.md
SOURCE_REAUDIT: outputs/plans/D1_MASTER_PLAN_REAUDIT_V3.md
REMEDIATION_TASK: D1-R3
PREVIOUS_VERDICT: MAJOR_REVISION_REQUIRED
REVISION_DATE: 2026-09-25
STATUS: PENDING_REAUDIT
READY_FOR_RE_AUDIT: true
READY_TO_LAUNCH_GEMINI_WORKERS: false
SCIENTIFIC_EXECUTION: NOT_STARTED
MP1_ANALYSIS: OUT_OF_SCOPE
D1_VS_MP1: OUT_OF_SCOPE
`

The complete finding inventory is `D1_V3_REAUDIT_FINDING_REGISTER.json`.
The complete remediation ledger is
`D1_V3_TO_V4_REMEDIATION_MATRIX.json` with its rendered `.md` companion.
The register retains every D1-A2 finding, every D1-A3 revision ID and every
A3 subfinding. Linked residuals are deduplicated only for primary counts.

### 36.1 Audit count reconciliation

The D1-A3 final block reports one remaining D1-A2 Critical, two remaining
D1-A2 High and three remaining D1-A2 Medium findings. A3-CR-01 is the linked
residual expression of RA-01 rather than a second independent Critical.
A3-HI-02 is the linked residual expression of RA-03 rather than a second
independent High. The distinct new blocking High is NEW-HIGH-01, represented
by the V4 record `NEW-HIGH-01` (revision alias `A3-HI-01`).

`yaml
d1_a2_remaining_critical: 1
d1_a2_remaining_high: 2
d1_a2_remaining_medium: 3
d1_a2_remaining_low: 1
d1_a3_distinct_new_critical: 0
d1_a3_distinct_new_high: 1
d1_a3_distinct_new_medium: 3
linked_a3_residuals: [A3-CR-01, A3-HI-02]
primary_critical_resolved: 1/1
primary_high_resolved: 3/3
new_blocking_findings_unresolved: 0
`

## 37. Post-freeze K-criterion control

### 37.1 KILL_CRITERION_CHANGE_RECORD_V4

Every K1-K9 criterion is frozen before evaluation. If any criterion changes
after evidence evaluation begins, the append-only record must contain:

`text
change_id
kill_test_id
criterion_version_before
criterion_version_after
criterion_before
criterion_after
criterion_originally_frozen_at
change_requested_at
evidence_seen_before_change
evidence_seen_description
reason_for_change
scientific_justification
bias_risk: NONE | LOW | MEDIUM | HIGH
human_review_required
human_review_id
approval_status: PENDING | APPROVED | REJECTED
adjudication_consequence
`

After evidence evaluation begins, `bias_risk` cannot be `NONE`. If evidence
was seen before the change, the old criterion, evidence set, evidence
snapshot hash and exposure history remain immutable; human review is
mandatory; and `final_adjudication_bias_status` must be `BIAS_RISK`. Approval
does not remove this status.

An unqualified `SURVIVES_TARGETED_NOVELTY_AUDIT` is forbidden for a candidate
affected by a post-evidence criterion change. Under the fixed outcome
vocabulary, the allowed routes are `FALSIFIED`, `SUBSTANTIALLY_NARROWED` or
`INCONCLUSIVE`; a future workflow change would be required to permit a
qualified survival outcome. If review is pending or rejected,
`FINAL_ADJUDICATION = BLOCKED`.

Both `D1_FINAL_EVIDENCE_MAP` and the final adjudication must include:

`json
{
  "final_adjudication_bias_status": "NONE|BIAS_RISK",
  "criterion_change_ids": ["change-id"],
  "bias_qualification": "string",
  "unqualified_survival_permitted": false
}
`

`NONE` is valid only when no applicable bias event exists. HG-13 checks the
sticky status across candidate narrowing, summaries and version changes.

## 38. W01-W12 execution contracts and readiness

The authoritative machine-readable contracts are in
`D1_WORKER_EXECUTION_READINESS_MATRIX.json`. Every worker record contains:

`text
worker_id
role
scientific_question
exclusive_scope
input_files
input_artifacts
output_directory
required_outputs
output_schema
dependencies
parallelizable
allowed_inference
forbidden_inference
must_not_conclude
reconciliation_owner
QA_owner
human_review_trigger
model
reasoning_effort
definition_of_done
`

Each W01-W12 owns a unique directory
`outputs/d1_execution/V4/W01/` through `W12/`. Shared logical artifacts are
written only by their named owner; downstream workers write versioned
derivatives in their own directory. The readiness matrix also records
`inputs_exist`, `dependencies_satisfied`, path/schema/owner checks,
`structurally_execution_ready`, `execution_ready` and `blocking_reason`.
Structural readiness is a contract test, not a claim that runtime outputs
exist. All twelve structural rows pass; runtime execution remains false
until A4 approval and actual dependencies exist.

W04 extracts and W09 reconciles. W05-W08 use one primary extractor per source
hash; W09 owns deduplication and packet identity. W10 has separate S5
repository-threat and S10 conditional-search passes. W11 has separate S8
provenance, S10 search QA, S11 threshold and S13 clearance passes. W12 has
separate S9 criterion-review and S12 adversarial passes.

## 39. Evidence-first Search Decision Log

Every search decision, including a no-search decision, is one durable row:

`text
search_id
trigger
scientific_question
related_K_test
related_candidate_claim
existing_repository_evidence_checked
existing_evidence_summary
evidence_gap
why_existing_evidence_is_insufficient
search_needed
decision: DO_NOT_OPEN | OPEN | CLOSE
reason_for_decision
query_family
databases
screening_rule
stop_condition
human_review_required
opened_at
closed_at
result_summary
`

`existing_repository_evidence_checked` must be true before `OPEN`. If
evidence is sufficient, `search_needed=false` and `decision=DO_NOT_OPEN`.
Confidence alone is not a trigger. An OPEN row requires a named K1-K9,
provenance or high-threat gap, query family, database, screening rule and
stop condition. CLOSE requires closure evidence. S16 rejects an incomplete
row or a literal escaped-newline artifact name.

## 40. Human review and REVISION_REQUIRED routing

The V4 clearance record adds:

`text
decision: APPROVED | REJECTED | REVISION_REQUIRED | NOT_REVIEWED
return_stage
return_artifact
required_revision
responsible_owner
reentry_gate
reentry_condition
revised_artifact_hash
`

`REVISION_REQUIRED` is a blocking decision, never an implicit approval.
`D1_REVISION_ROUTING_MATRIX.json` gives exact routes: criterion changes return
to S9; provenance and critical contradiction to S8; prior-art threat to S5
or S10; search authorization to S10; threshold to S11; red-team to S12;
worker defects to the originating pass; clearance revisions to the named
stage; and package defects to S16. Every route names its artifact, owner,
required revision and re-entry gate. Generic “previous stage” is invalid.

## 41. V4 hard-gate matrix

Every gate row contains:

`text
gate_id
required_inputs
machine_check
pass_condition
fail_condition
return_route
blocked_stage
human_review_requirement
status
`

V4 uses HG-01 through HG-15. HG-01 covers historical completeness; HG-02
provenance; HG-03 contradictions; HG-04 K freeze; HG-05 K resolution; HG-06
threshold freeze; HG-07 threats; HG-08 red-team; HG-09 human clearance;
HG-10 final readiness; HG-11 worker readiness; HG-12 package QA; HG-13
post-freeze bias; HG-14 search opening; and HG-15 revision routing.

HG-13 fails if a post-freeze change has `bias_risk=NONE`, missing exposure,
missing review, missing final bias status or unqualified survival. HG-14
fails if OPEN precedes repository evidence review or lacks a necessary gap.
HG-15 fails if a REVISION_REQUIRED row lacks an exact route. Gate status is
computed by S16 and cannot be bypassed by prose.

## 42. V4 authoritative dependency graph

The only executable graph is:

`text
S0 scope/hash lock
→ S1 inventory and round coverage
→ S2 historical state
→ S3 paper packets (W05-W08 parallel)
→ S4 claim extraction/reconciliation
→ S5 repository threat integration
→ S6 non-novelty register
→ S7 novelty-candidate register
→ S8 provenance and contradiction QA
→ S9 K1-K9 criterion definition/freeze
→ S10 evidence-first decision and conditional targeted search
→ S11 threshold/boundary freeze
→ S12 red-team attack
→ S13 human review and routing
→ S14 Sol synthesis/Astra challenge
→ S15 final D1 adjudication
→ S16 package and hard-gate QA
`

Feedback is explicit and acyclic after re-entry: K defects→S9, provenance or
contradiction→S8, prior-art threat→S5/S10, search decision→S10, threshold→S11,
red-team→S12, worker defect→originating pass, human
`REVISION_REQUIRED`→routing matrix→named pass, and package defect→S16.
Re-entry requires a new artifact hash and a passing gate. No route is a
dead-end or silently resumes downstream.

## 43. V4 model, reasoning and cost controls

| stage | model | reasoning | why this model | why not cheaper | why not more expensive | cost |
|---|---|---|---|---|---|---|
| S0,S16 | deterministic | none | hashes, paths and schemas are mechanical | no model needed | Astra adds no value | LOW |
| S1-S3 | Gemini 3.8 Flash | High | bulk inventory, history and packets | lower effort risks omissions | Astra is wasteful for extraction | LOW-MODERATE |
| S4-S8 | GPT-6 Sol | High | cross-worker reconciliation and provenance | Flash cannot safely reconcile claims | Astra is reserved for attack | MODERATE-HIGH |
| S9 | Sol + Astra review | High | freeze criteria and challenge leakage | Flash is insufficient for criterion integrity | xHigh is premature | HIGH |
| S10-S11 | Flash + Sol | High | bounded retrieval and temporal checks | deterministic checks cannot interpret gaps | Astra is unnecessary for retrieval | MODERATE |
| S12 | GPT-6 Astra | High | adversarial falsification | cheaper calls risk confirmation bias | xHigh is held for material conflict | HIGH |
| S13 | human + deterministic | none | sign-off is human authority | model cannot fabricate approval | xHigh cannot substitute sign-off | LOW-MODERATE |
| S14 | Sol + Astra | High | synthesis plus independent attack | Flash is too weak | xHigh only for material conflict | HIGH |
| S15 | Sol; Astra xHigh conditional | High/xHigh | final D1-only decision | Flash cannot adjudicate critical conflict | xHigh every run is wasteful | HIGH/VERY-HIGH |

Astra is forbidden for repetitive extraction, formatting, bibliography or
routine QA. No model call is made in this remediation.

## 44. V4 package manifest and schema QA

`D1_PLAN_PACKAGE_MANIFEST.json` is the sole active V4 index. It contains:

`text
artifact_id
artifact_name
artifact_type
required
owner
consumer
schema_defined
exists
version
QA_status
`

The seven plan-remediation artifacts due now are the V4 plan, finding
register, JSON remediation matrix, Markdown remediation matrix, worker
readiness matrix, revision routing matrix and package manifest. V3 and A3 are
read-only source artifacts. Future W01-W12 and final-adjudication outputs are
explicitly `DEFERRED_PRE_EXECUTION`, with
`required_at_execution=true` and `exists=false`; they are not missing
plan artifacts.

Package QA requires unique IDs and names, zero orphan/duplicate/missing due
artifacts, valid schemas, nonempty files, explicit JSON/Markdown pairing and
no literal escaped-newline-plus-hyphen path. The malformed V3 deliverable entry is corrected in V4
and the manifest is the canonical list.

## 45. Stop conditions and final outcomes

Do not proceed to final adjudication until historical stages are complete,
material claims have provenance, high-threat papers are resolved or explicitly
unavailable, both novelty registers are stable, critical contradictions are
cleared, K1-K9 are resolved or visibly blocking, thresholds were frozen before
visible validation data, red-team rows are closed, human reviews are cleared,
all revision routes re-enter through their gates, W01-W12 structural checks
pass, and unsupported thesis-critical claims equal zero.

The final outcome remains `FALSIFIED`, `SUBSTANTIALLY_NARROWED`,
`SURVIVES_TARGETED_NOVELTY_AUDIT` only when no bias rule prohibits it, or
`INCONCLUSIVE`. The workflow never forces survival.

## 46. Re-audit checklist and scope

The D1-A4 auditor must verify every A2 and A3 record, all twelve contracts,
unique directories, evidence-first search controls, exact revision routes,
HG-01..HG-15, manifest QA, unchanged V3 hash and no execution. This V4
remediation changes workflow architecture only. D1 scientific status,
D1-V001...D1-V009 verdicts, M1, MP1 and mentor reporting remain unchanged.

## 47. Required next action

Run an independent D1-A4 re-audit of Master Plan V4 with GPT-6 Astra at High
reasoning. Do not launch Gemini workers before that re-audit passes.
# D1 MASTER PLAN VERSION

V4

# SOURCE PLAN

V3

# SOURCE RE-AUDIT

D1_MASTER_PLAN_REAUDIT_V3

# REMAINING CRITICAL FINDINGS RESOLVED

1/1

# REMAINING HIGH FINDINGS RESOLVED

2/2

# REMAINING MEDIUM FINDINGS RESOLVED/ACCEPTABLY_DEFERRED

3/3

# NEW HIGH FINDINGS RESOLVED

1/1

# NEW BLOCKING FINDINGS UNRESOLVED

0

# WORKERS W01-W12 STRUCTURALLY EXECUTION-READY

true

# READY FOR RE-AUDIT

true

# READY TO LAUNCH GEMINI WORKERS

false

# NEXT ACTION

INDEPENDENT D1-A4 RE-AUDIT OF MASTER PLAN V4 USING GPT-6 ASTRA HIGH

# MP1 ANALYSIS

NOT PART OF THIS TASK

# D1-vs-MP1 COMPARISON

NOT STARTED








## V5-13. V5 authoritative machine-control references

The following files are part of the V5 package and override similarly named inherited artifacts:

- `D1_V4_REAUDIT_FINDING_REGISTER.json`
- `D1_V4_TO_V5_REMEDIATION_MATRIX.json` and `.md`
- `D1_WORKER_EXECUTION_READINESS_MATRIX_V5.json`
- `D1_ARTIFACT_OWNERSHIP_MATRIX.json`
- `D1_REVISION_ROUTING_MATRIX_V5.json`
- `D1_HARD_GATE_MATRIX.json` and `.md`
- `D1_HARD_GATE_ROUTING_QA.json`
- `D1_PLAN_PACKAGE_MANIFEST_V5.json`

These files are the executable-control surface for a future run. Historical V4/V3 artifacts remain read-only source inputs and cannot override V5 paths, owners, statuses, route IDs or schemas.

## V5-14. Remediation status

No worker, search, evidence extraction, K test, threshold selection, novelty adjudication, M1 analysis, MP1 analysis or D1-vs-MP1 comparison has been performed. The package only establishes that a future execution can be audited structurally.

# D1 MASTER PLAN VERSION

V5

# SOURCE PLAN

V4

# SOURCE RE-AUDIT

D1_MASTER_PLAN_REAUDIT_V4

# A4 NEW HIGH FINDINGS RESOLVED

2/2

# NEW CRITICAL FINDINGS UNRESOLVED

0

# NEW HIGH FINDINGS UNRESOLVED

0

# W01-W12 OUTPUT DIRECTORIES EXIST

true

# W01-W12 ARTIFACT OWNERSHIP COMPLETE

true

# W01-W12 STRUCTURALLY EXECUTION-READY

12/12

# HG-01-HG-15 COMPLETE

15/15

# HARD-GATE ROUTING QA

PASS

# CANONICAL V5 PACKAGE VALID

true

# READY FOR RE-AUDIT

true

# READY TO LAUNCH GEMINI WORKERS

false

# NEXT ACTION

INDEPENDENT D1-A5 RE-AUDIT OF MASTER PLAN V5 USING GPT-6 ASTRA HIGH

# MP1 ANALYSIS

NOT PART OF THIS TASK

# D1-vs-MP1 COMPARISON

NOT STARTED

# MENTOR REPORT

OUT OF SCOPE

# SCIENTIFIC EXECUTION

NOT STARTED

# THIS TASK

PLAN REMEDIATION ONLY

## V6-10. V6 authoritative artifacts

- `D1_V5_REAUDIT_FINDING_REGISTER.json`
- `D1_V5_TO_V6_REMEDIATION_MATRIX.json` and `.md`
- `D1_ARTIFACT_OWNERSHIP_MATRIX_V6.json`
- `D1_ARTIFACT_OWNERSHIP_QA_V6.json`
- `D1_WORKER_FAILURE_ROUTING_MATRIX.json`
- `D1_WORKER_ROUTING_HARD_GATE_QA.json`
- `D1_WORKER_EXECUTION_READINESS_MATRIX_V6.json`
- `D1_REVISION_ROUTING_MATRIX_V6.json`
- `D1_HARD_GATE_MATRIX_V6.json` and `.md`
- `D1_HARD_GATE_ROUTING_QA_V6.json`
- `D1_PLAN_PACKAGE_MANIFEST_V6.json`

These artifacts are the only active V6 execution-control surface. V5 files remain read-only historical inputs.

## V6-11. Regression and re-audit scope

Before re-audit, verify HG-01–HG-15, physical directories, search log, revision routing, human review, threshold freeze, K1–K9 controls, negative outcomes, source precedence and package integrity. No scientific execution is permitted in this remediation.

# D1 MASTER PLAN VERSION

V6

# SOURCE PLAN

V5

# SOURCE RE-AUDIT

D1_MASTER_PLAN_REAUDIT_V5

# A5 NEW HIGH FINDINGS RESOLVED

2/2

# OWNERSHIP CONFLICTS UNRESOLVED

0

# W01-W12 OWNERSHIP VERIFIED

12/12

# W01-W12 FAILURE ROUTING VERIFIED

12/12

# INVALID GENERIC S16 ROUTES

0

# WORKER-TO-HARD-GATE ROUTING QA

PASS

# W01-W12 STRUCTURALLY EXECUTION-READY

12/12

# CANONICAL V6 PACKAGE VALID

true

# READY FOR RE-AUDIT

true

# READY TO LAUNCH GEMINI WORKERS

false

# NEXT ACTION

INDEPENDENT TARGETED D1-A6 RE-AUDIT OF MASTER PLAN V6 USING GPT-6 ASTRA HIGH
