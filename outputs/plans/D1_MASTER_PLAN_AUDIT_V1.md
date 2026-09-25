# D1 MASTER PLAN AUDIT V1

## A. Audit target identified

Audited plan:

outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN.md

Plan SHA256:

4170A2607B7685EC94643B1FEB610B7CE698DCD245BA449EA30CD5EA9C8989E2

The audit covers the D1/M1 Master Execution Plan only. No scientific D1 audit, evidence extraction, literature search, worker launch, MP1 analysis, D1-vs-MP1 comparison, mentor report, or plan modification was performed.

## B. Repository-state consistency check

Repository HEAD:

0ade68e73d93c38618b366a000ac7a01215a3936

The repository context is consistent with the plan:

- selected_direction = D1_M1
- decision = LOCK_WITH_FEASIBILITY_GATE
- M1 = Zhang et al., A continuum-based model for a layer jamming beam
- DOI = 10.5194/ms-16-821-2025
- D1-V001 through D1-V009 are present
- D1-V008 = SURVIVES_FINAL_TARGET
- D1-V009 = SURVIVES_LATE_FOUND_TARGET

The worktree is dirty:

~~~text
M  docs/README.md
M  docs/project/MENTOR_PIVOT_STATUS.md
A  docs/project/NEXT_SESSION_START_HERE.md
?? outputs/plans/
~~~

The audited plan is untracked and not part of HEAD. Any future execution must record the plan hash and exact working-tree state.

## C. Overall audit verdict

MAJOR_REVISION_REQUIRED

The plan has a valid D1-only intent, a useful S0-S8 structure, evidence packets, claim evolution, threat mapping, adversarial review and stop conditions. It is not ready for execution because historical state, non-novelty and novelty-candidate registers, source precedence, contradiction handling and a mandatory K1-K9 falsification gate are absent. Additional high-severity gaps affect evidence fields, family coverage, search control, output schemas, model allocation and threshold/mechanism safeguards.

## D. Scope-discipline audit

Result: MINOR ISSUE

The plan excludes MP1, D1-vs-MP1 comparison, mentor persuasion and broad automatic searching. However, M1 reconstruction, reference credibility, accepted/rejected conditions and measurement precision could leak into scientific execution. Add an explicit boundary:

~~~text
The workflow may inspect whether M1, R and E are sufficiently specified to support a novelty claim.
It must not implement M1, run FE, design apparatus, collect data or execute experiments.
~~~

## E. Historical-lineage audit

Result: MAJOR ISSUE

The plan lists D1-V001 through D1-V009 and requires canonical artifacts, but it does not require a round-coverage matrix proving that every round and every important transition has been reconstructed. It does not explicitly require the initial discovery claim, the V007 unresolved state, the source that caused each transition, or bibliographic metadata attached to each transition. A final-title narrative could therefore replace an actual historical reconstruction.

## F. Historical state-at-time audit

Result: CRITICAL ISSUE

No Historical State Register is defined. The plan lacks:

~~~text
STATE_AT_TIME
CURRENT_CANONICAL_STATE
SUPERSEDED_INTERPRETATION
CORRECTED_INTERPRETATION
~~~

This permits later knowledge to be inserted into earlier rounds. D1-V007 was historically INCONCLUSIVE_MISSING_TARGET; later V008 and V009 cannot rewrite that historical state.

## G. Claim-evolution audit

Result: HIGH ISSUE

The Claim Evolution Matrix is directionally correct but does not make the following mandatory for every transition:

- historical stage;
- paper title, authors, year, DOI and paper_id;
- what the source proves;
- what it does not prove;
- evidence status;
- confidence;
- supersession or correction.

The transition must be integrity-linked to a complete evidence packet.

## H. Novelty-category audit

Result: HIGH ISSUE

The schema includes MODEL, MECHANISM, METHOD, VALIDATION, QUESTION and WORKFLOW, but omits SYSTEM, APPLICATION and the explicit SCIENTIFIC_QUESTION token. This allows rejected model novelty to reappear as application, system or workflow novelty. The plan must also reject exact-title novelty, threshold-by-itself novelty and automatic novelty from combining known methods.

## I. NON-NOVELTY register audit

Result: CRITICAL ISSUE

The plan lists generic claims that should not be called novel but does not define a formal D1_NON_NOVELTY_REGISTER. The register must freeze the non-novel status of layer jamming, vacuum-controlled stiffness, frictional stiffening, interlayer slip, partial/full slip, continuum modeling, layered beam modeling, Coulomb friction, full-layer FE, experimentation, model-versus-experiment comparison, error metrics and acceptance tolerances.

## J. NOVELTY-CANDIDATE register audit

Result: CRITICAL ISSUE

The plan discusses a surviving gap but lacks a formal D1_NOVELTY_CANDIDATE_REGISTER. A claim must not become novel merely because other claims were eliminated. Candidates need explicit overlap, threats, kill conditions, status and confidence.

## K. Surviving-claim audit

Result: HIGH ISSUE

The plan generally treats the M1 validity/breakdown contribution as a candidate and attempts to attack it. It does not formally distinguish model validation from validity-domain research, workflow sophistication from scientific contribution, or tolerance-setting from a substantive mechanics question. These distinctions must be enforced through the candidate register and falsification gate.

## L. “Done many times” objection audit

Result: HIGH ISSUE

The plan names A, B and C but does not require structured fields for every paper:

~~~text
addresses_A
addresses_B
addresses_C
~~~

There is no dedicated acceptance test for proposition C. Paper counts, keywords and titles cannot substitute for conceptual-equivalence testing of the complete M → R → E contribution.

## M. Prior-art coverage audit

Result: HIGH ISSUE

The formal family vocabulary is too narrow: layer-jamming, homogenization, contact, partial-interaction and validation. Repository history also requires explicit coverage checks for vacuum layer-jamming, friction-controlled stiffness, interlayer slip, composite beam theory, Cosserat/generalized continuum, interface-resolved models, frictional-contact FE, full-layer models, experimental characterization, model verification, model-form error, validity-domain studies, reduced-model breakdown and uncertainty-aware validation.

## N. Evidence-quality audit

Result: HIGH ISSUE

The Evidence Packet lacks mandatory fields for method, experiment, parameter domain, error metrics, validity studied, breakdown studied, higher-fidelity comparison, physical failure mechanism and impact on D1. Acceptance criterion does not replace error metrics, and reference_used does not specify interface resolution or reference role.

## O. Provenance audit

Result: HIGH ISSUE

The plan requires paths, locators, status and confidence but does not enforce the full chain:

~~~text
summary/handoff
↓
canonical verdict JSON
↓
verification matrix
↓
evidence JSON
↓
original PDF
↓
raw prompt/output/provenance
~~~

Source precedence, source hash, locator validation and fail-closed handling are missing.

## P. Source-precedence audit

Result: CRITICAL ISSUE

The plan does not specify what wins when sources disagree. It must state that original PDF evidence outranks AI summaries for paper claims; latest valid canonical JSON outranks stale narrative for current workflow state; and historical reports remain historical even after correction.

## Q. Contradiction-control audit

Result: CRITICAL ISSUE

The plan says not to erase worker disagreement but defines no contradiction register or adjudication process. Required types include SUMMARY_VS_JSON, JSON_VS_PDF, ROUND_VS_ROUND, WORKER_VS_WORKER, HISTORICAL_VS_CURRENT and OTHER. Unresolved critical contradictions must block final adjudication.

## R. Falsification-power audit

Result: HIGH ISSUE

The plan has a credible kill-chain idea but uses the ambiguous phrase “most or all”. It does not state which conditions are mandatory for KILL, PARTIAL_OVERLAP, NO_KILL_FOUND and UNRESOLVED. It also lacks an explicit kill test for the case where D1 collapses into routine model validation without a substantive mechanics question.

## S. K1-K9 gate audit

Result: CRITICAL ISSUE

No mandatory K1-K9 gate exists. The gate must test:

K1 comparable continuum model with validity-domain mapping;

K2 reduced versus layer-resolved/full-contact comparison;

K3 model-form-error quantification;

K4 deliberate valid and breakdown regimes;

K5 experiments on both sides of a validity boundary;

K6 mechanistic attribution to contact, slip, separation or interface physics;

K7 substantially equivalent M → R → E applied to vacuum layer jamming;

K8 methodology that makes D1 routine;

K9 conceptual equivalent under different terminology.

A high-significance unresolved K-test must block final adjudication.

## T. Search-strategy audit

Result: HIGH ISSUE

The plan says that broad search should stop without a concrete target, but it does not define search trigger, scientific question, query family, source, date, screening, full-text promotion or branch closure.

## U. Search-bias audit

Result: HIGH ISSUE

Conceptual equivalence is mentioned but synonym expansion is not required. The plan remains vulnerable to current-title bias, “validity domain” phrase bias, “breakdown” phrase bias, layer-jamming-only bias and dismissal of equivalent mechanics in another application domain.

## V. Worker-architecture audit

Result: MEDIUM ISSUE

The groups are plausible but lack a dependency DAG and worker contract. Potential overlaps include S1 versus S3, S2 versus S5 and S4 versus S6. Ownership, allowed inference, forbidden inference and reconciliation owner must be explicit.

## W. Model/reasoning audit

Result: HIGH ISSUE

S0 uses GPT-6 Sol for deterministic provenance work. S7 uses GPT-6 Sol for final high-stakes adjudication after Astra performs only an adversarial stage. Recommended allocation is deterministic S0, Gemini Flash for S1-S3, Flash plus Sol for S4, Sol for S5, Astra High for S6, and Sol draft plus Astra High final challenge for S7. Astra xHigh should be conditional on an unresolved material conflict.

## X. Cost audit

Result: MEDIUM ISSUE

Caching and deduplication are present, but no qualitative cost estimate is given. Estimated total cost is HIGH. S0 should become deterministic and only high-threat packets should reach Astra.

## Y. Human-review audit

Result: MEDIUM ISSUE

Review checkpoints exist but no human-review record or escalation artifact exists. Review must be mandatory for direct kills, conceptual equivalents, PDF conflicts, worker disagreement, material candidate changes, KILL/UNRESOLVED K-tests, absence-based claims, arbitrary thresholds and historical reinterpretation.

## Z. Stop-condition audit

Result: MEDIUM ISSUE

Global stop rules exist but stage-level definition-of-done criteria are incomplete. The workflow must explicitly confirm complete round coverage, complete claim provenance, high-threat resolution, stable registers, resolved contradictions, resolved K-tests and zero unsupported thesis-critical claims.

## AA. Output-schema audit

Result: HIGH ISSUE

The plan defines Evidence Packet, Claim Evolution and Threat Matrix schemas but not:

- D1_HISTORICAL_STATE_REGISTER;
- D1_NON_NOVELTY_REGISTER;
- D1_NOVELTY_CANDIDATE_REGISTER;
- D1_CONTRADICTION_REGISTER;
- D1_K1_K9_FALSIFICATION_MATRIX;
- D1_UNRESOLVED_THREAT_REGISTER;
- D1_PROVENANCE_QA;
- D1_FINAL_EVIDENCE_MAP.

## AB. Parameter/threshold leakage audit

Result: HIGH ISSUE

The plan says tolerances must be predeclared but does not define the freeze artifact, responsible reviewer, freeze timestamp, versioning rule or adjudication of arbitrary tolerances. The same problem applies to validity boundaries and breakdown criteria.

## AC. Causal-overclaim audit

Result: HIGH ISSUE

The plan requests contact/slip mechanism explanations but does not distinguish correlation, mechanistic consistency, causal evidence and hypothesis. Error growth near pressure or slip is not sufficient to prove causal failure.

## AD. Red-team findings

Execution could produce false novelty through:

1. anchoring on LOCK_WITH_FEASIBILITY_GATE;
2. citation-selection bias;
3. searching only the current title;
4. exact-phrase bias;
5. assuming different terminology means different science;
6. overcounting one research lineage;
7. confusing method combination with novelty;
8. treating lack of direct match as novelty;
9. treating full-layer FE as unquestioned truth;
10. selecting tolerances after results;
11. defining breakdown retrospectively;
12. claiming mechanisms without local evidence;
13. treating workflow sophistication as scientific contribution;
14. rewriting D1-V007 after V008/V009;
15. allowing worker synthesis to override primary sources;
16. confusing calibration error with model-form error;
17. treating a negative search result as proof of global absence.

## AE. Required revisions ranked by severity

### Critical

CR-01: Add Historical State Register with state-at-time, current state, superseded and corrected interpretation fields. Plan sections C, D/S2, H, L, M. Model: Gemini Flash High plus Sol High. Re-audit: true.

CR-02: Add D1_NON_NOVELTY_REGISTER and D1_NOVELTY_CANDIDATE_REGISTER, with complete novelty category enum. Plan sections B, H, J, M. Model: GPT-6 Sol High. Re-audit: true.

CR-03: Add provenance chain, source precedence, source hashes, locator validation and D1_CONTRADICTION_REGISTER. Plan sections C, G, K, M. Model: deterministic validator plus GPT-6 Sol High. Re-audit: true.

CR-04: Add mandatory D1_K1_K9_FALSIFICATION_MATRIX with KILL, PARTIAL_OVERLAP, NO_KILL_FOUND and UNRESOLVED states; block final adjudication on high-significance unresolved tests. Plan sections J, S6, S7, L. Model: GPT-6 Astra High; xHigh conditional. Re-audit: true.

### High

HI-01: Complete every Claim Evolution transition with stage, paper metadata, proves/does-not-prove, evidence status, confidence and supersession. Plan sections H, S2, S5. Model: Gemini Flash High plus Sol High. Re-audit: true.

HI-02: Add complete novelty category control and explicit model-validation versus validity-domain fields. Plan sections B, H, S5. Model: Sol High. Re-audit: true.

HI-03: Add D1_PRIOR_ART_FAMILY_COVERAGE with inclusion, exclusion and unresolved-threat reasons. Plan sections C, I, S3, S4. Model: Gemini Flash High plus Sol High. Re-audit: true.

HI-04: Expand Paper Evidence Packet with method, experiment, parameter domain, error metrics, validity/breakdown flags, comparison role, mechanism evidence and D1 impact. Plan sections G, S3. Model: Gemini Flash High. Re-audit: true.

HI-05: Add search protocol and decision log with trigger, query family, source, date, screening, promotion and closure. Require synonym expansion. Plan sections S4, L. Model: Gemini Flash High plus Sol High. Re-audit: true.

HI-06: Add worker registry and dependency DAG with exclusive responsibilities, output schemas, allowed/forbidden inference and reconciliation owner. Plan sections D, F. Model: Gemini Flash High coordinator plus Sol High reconciliation. Re-audit: true.

HI-07: Make S0 deterministic and require Sol draft plus Astra High final challenge for S7; reserve Astra xHigh for unresolved material conflict. Plan sections E, S0, S6, S7. Re-audit: true.

HI-08: Add missing output schemas, threshold-freeze record and evidence-class fields distinguishing correlation, mechanism consistency, causal evidence and hypothesis. Plan sections G-I, L, M, S5-S8. Model: Sol High plus deterministic validation. Re-audit: true.

### Medium

ME-01: Add explicit non-execution scope fence for M1, R, FE, apparatus and experiments. Plan sections A, D, O. Re-audit: false if integrated with V2.

ME-02: Add qualitative stage-level cost ledger. Plan section E. Re-audit: false.

ME-03: Add human_review_record.json and escalation rules. Plan section K. Re-audit: false if integrated with high revisions.

ME-04: Add stage-level definition-of-done checklist. Plan sections D, L. Re-audit: false if integrated with high revisions.

ME-05: Add structured red-team matrix. Plan sections N, S6. Re-audit: false if incorporated into K1-K9.

## AF. Exact next action

Do not execute the plan and do not launch Gemini workers. Remediate CR-01 through CR-04 and HI-01 through HI-08, then reaudit the resulting V2. The plan must remain D1-only and must not alter scientific verdicts in the repository.

## Final status

D1 MASTER PLAN AUDIT
=
MAJOR_REVISION_REQUIRED

CRITICAL REVISIONS
=
4

HIGH REVISIONS
=
8

MEDIUM REVISIONS
=
5

LOW REVISIONS
=
0

RE-AUDIT REQUIRED
=
true

READY TO LAUNCH GEMINI WORKERS
=
false

MP1 ANALYSIS
=
NOT STARTED

D1-vs-MP1 COMPARISON
=
NOT STARTED
