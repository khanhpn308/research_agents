# D1/M1 NOVELTY RECONSTRUCTION AND FALSIFICATION
# MASTER EXECUTION PLAN V2

## 1. Plan identity and remediation provenance

- PLAN_VERSION: V2
- SOURCE_PLAN_VERSION: V1
- SOURCE_PLAN: outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN.md
- AUDIT_SOURCE: outputs/plans/D1_MASTER_PLAN_AUDIT_V1.md
- REMEDIATION_TASK: D1-R1
- REVISION_DATE: 2026-09-25
- AUDIT_VERDICT: MAJOR_REVISION_REQUIRED
- RESOLVED_CRITICAL_COUNT: 4/4
- RESOLVED_HIGH_COUNT: 8/8
- RESOLVED_MEDIUM_COUNT: 5/5
- UNRESOLVED_CRITICAL_HIGH_COUNT: 0
- READY_FOR_RE_AUDIT: true
- READY_TO_LAUNCH_GEMINI_WORKERS: false

The remediation checklist is preserved in:

outputs/plans/D1_MASTER_PLAN_REMEDIATION_CHECKLIST_V1.md

This V2 is a plan artifact only. It does not execute the scientific audit, launch workers, search literature, extract paper evidence, implement M1, run FE, collect data, analyze MP1, compare D1 with MP1, or modify scientific verdicts.

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

## 23. Remediation completion

The V2 remediation status is:

~~~text
CRITICAL: 4/4 resolved
HIGH: 8/8 resolved
MEDIUM: 5/5 resolved
LOW: 0
UNRESOLVED CRITICAL/HIGH: 0
~~~

Residual risks do not invalidate re-audit readiness, but they must remain visible:

- full-text unavailability can keep a K-test unresolved;
- causal mechanism may remain hypothesis-level;
- human review availability is external;
- targeted search cannot prove global absence;
- final xHigh use remains conditional.

## 24. Expected D1-only deliverables

- repository_manifest.json
- scope_lock.json
- plan_hash_record.json
- D1_EVIDENCE_INVENTORY.json
- D1_ROUND_COVERAGE.json
- D1_HISTORICAL_STATE_REGISTER.json
- D1_CLAIM_EVOLUTION_MATRIX.json
- D1_PAPER_EVIDENCE_PACKETS.jsonl
- D1_PRIOR_ART_FAMILY_COVERAGE.json
- D1_PRIOR_ART_THREAT_MATRIX.json
- D1_NON_NOVELTY_REGISTER.json
- D1_NOVELTY_CANDIDATE_REGISTER.json
- D1_CONTRADICTION_REGISTER.json
- D1_K1_K9_FALSIFICATION_MATRIX.json
- D1_UNRESOLVED_THREAT_REGISTER.json
- D1_PROVENANCE_QA.json
- D1_THRESHOLD_FREEZE_RECORD.json
- D1_HUMAN_REVIEW_RECORD.json
- D1_RED_TEAM_MATRIX.json
- D1_FINAL_EVIDENCE_MAP.json
- D1_PLAN_REMEDIATION_MATRIX.json
- FINAL_D1_NOVELTY_ADJUDICATION.json
- FINAL_D1_NOVELTY_ADJUDICATION.md

No D1-V001…D1-V009 directory may be overwritten.

## 25. Final scope lock

~~~text
PLAN_VERSION = V2
STAGE 1 SCOPE = D1 NOVELTY ONLY
MP1 ANALYSIS = NOT STARTED
D1-vs-MP1 COMPARISON = NOT STARTED
MENTOR REPORT = OUT OF SCOPE
SCIENTIFIC EXECUTION = NOT STARTED
THIS TASK = PLAN REMEDIATION ONLY
~~~

## 26. Required next action

Re-audit D1 Master Plan V2 with GPT-6 Astra High. Do not launch Gemini workers until the re-audit confirms that all four Critical and all eight High findings remain resolved.

# D1 MASTER PLAN VERSION

V2

# CRITICAL AUDIT FINDINGS RESOLVED

4/4

# HIGH AUDIT FINDINGS RESOLVED

8/8

# UNRESOLVED CRITICAL/HIGH FINDINGS

0

# READY FOR RE-AUDIT

true

# READY TO LAUNCH GEMINI WORKERS

false

# NEXT ACTION

RE-AUDIT D1 MASTER PLAN V2 WITH GPT-6 ASTRA HIGH
