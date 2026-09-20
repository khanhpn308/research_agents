# Research Review and Execution Roadmap — Post D1-V009

> **Status:** Current roadmap after D1-V009  
> **Purpose:** provide one causal, auditable reading order for the entire project and one execution roadmap from the current state forward.  
> **Current repository state:** 123 paper records = 54 seed papers + 69 verification papers; 122 included, 1 excluded, 0 pending.  
> **Current reduced model:** M1 — Zhang et al., *A continuum-based model for a layer jamming beam*, DOI 10.5194/ms-16-821-2025.  
> **Current novelty status:** provisional lock survives D1-V009; broad search remains stopped unless a concrete new high-threat source appears.

---

# 1. What this roadmap is for

The repository should not be reviewed by alphabetical file order.

It should be reviewed as a causal chain:

~~~text
primary evidence
→ extracted evidence
→ structured corpus
→ local reasoning
→ cross-corpus candidate generation
→ adversarial critique
→ provisional selection
→ independent falsification
→ repeated narrowing
→ final high-threat closure
→ late-found post-lock audit
→ exact model selection
→ research architecture
→ execution
~~~

At every arrow ask:

> Does the conclusion actually follow from the evidence before it?

The goal is to understand and personally defend the entire research logic rather than merely inherit the agent's conclusion.

---

# 2. Current project state in one diagram

~~~text
54 SEED PAPERS
│
├─ evidence extraction
▼
data/evidence/*.json
│
├─ corpus normalization
▼
outputs/discovery_snapshot/literature_matrix_54papers.json
│
├─ 54 papers → 9 batches × 6
▼
outputs/reasoning_batches/
│
├─ within-batch synthesis
▼
outputs/batch_syntheses/
│
├─ cross-batch reasoning
▼
5 candidate directions
│
├─ adversarial critique
▼
direction critique
│
├─ final discovery adjudication
▼
D1 selected with revision
│
├─ independent verification
▼
D1-V001  → broad D1 PIVOT
│
▼
P1 = validity limits of continuum / homogenized layer-jamming mechanics
│
├─ direct recent threats
▼
D1-V002
│
├─ direct LJ + forward-citation + target audits
▼
D1-V003
│
├─ adjacent mechanics: frictional multilayers
▼
D1-V004 / C01
│
├─ adjacent mechanics: partial interaction
▼
D1-V005 / C02
│
├─ adjacent mechanics: imperfect interface / friction-contact
▼
D1-V006 / C03
│
├─ forward citations of strongest threat
▼
D1-V007 / C04
│
├─ final named target
▼
D1-V008
│
├─ broad-search stop condition reached
▼
PROVISIONAL NOVELTY LOCK
│
├─ exact reduced-model comparison
▼
M1 vs M2
│
├─ user selects M1
▼
M1 RESEARCH ARCHITECTURE
│
├─ late-found high-relevance adjacent mechanics paper
▼
D1-V009 — Adhikary et al. 1999
│
└─ result:
   SURVIVES_LATE_FOUND_TARGET
   confidence: high
   kill condition: false
   novelty lock survives: true
   reopen broad search: false
   targeted follow-up: false
│
▼
CURRENT PHASE:
RECONSTRUCT M1 → LOCK R → LOCK RQ/HYPOTHESIS/TOLERANCES → IMPLEMENT → VALIDATE → EXPERIMENT
~~~

---

# 3. Backward review path — from raw evidence to current topic

## Phase A — Understand the repository's research logic

Read first:

1. `docs/project/RESEARCH_STATE.md`
2. `docs/project/RESEARCH_LOG.md`

Use these only as historical orientation. They are not the latest source of truth for the current state.

Question to answer:

> What was the pipeline designed to do, and why was it adversarial rather than confirmatory?

---

## Phase B — Audit the 54-paper discovery foundation

Start with:

1. `data/paper_registry.json`
2. the 54 seed evidence JSON files under `data/evidence/`
3. `outputs/discovery_snapshot/literature_matrix_54papers.json`

For each seed paper, review:

~~~text
paper metadata
→ extracted objective
→ model/method
→ variables
→ evidence claims
→ assumptions
→ author-stated limitations
→ inferred limitations
→ future work
→ gap implications
~~~

Audit question:

> Did extraction preserve what the paper actually says, or did inference get promoted into fact?

When a claim matters, return to the original PDF stored locally.

---

## Phase C — Audit the 9 reasoning batches

Read:

1. `outputs/reasoning_batches/manifest.json`
2. `outputs/reasoning_batches/batch_001.json` through `batch_009.json`
3. `outputs/batch_syntheses/manifest.json`
4. `outputs/batch_syntheses/B001.json` through `B009.json`

The reasoning batches are inputs; the batch syntheses are the first major inference layer.

For each proposed gap:

~~~text
agent gap claim
→ supporting paper_ids
→ evidence JSON
→ original paper if necessary
~~~

Audit question:

> Does the claimed gap follow from the supplied batch, or is it only absence within a small local subset?

---

## Phase D — Audit generation of the five candidate directions

Read in this order:

1. `outputs/discovery_snapshot/candidate_directions.json`
2. `outputs/candidate_directions.md`
3. `outputs/discovery_snapshot/direction_critique.json`
4. `outputs/direction_critique.md`
5. `outputs/discovery_snapshot/final_adjudication.json`
6. `outputs/final_adjudication.md`

The five actual discovery candidates were:

- D1 — vacuum layer-jamming: friction / warping / cyclic stiffness degradation, later revised toward interlayer slip + bending stiffness.
- D2 — positive-pressure layer jamming under flexural loading.
- D3 — phase-change soft finger thermal mechanics.
- D4 — membrane–granulate interaction in vacuum jamming grippers.
- D5 — higher-order shear model of fluidic prestressed composite actuators.

Audit questions:

> Why did D1 emerge from the batch evidence?

> Why did the critic retain D1/D2 and reject or weaken the others?

> Why did final adjudication prefer D1?

Important conclusion:

~~~text
D1 at this stage was only the best candidate within the 54-paper corpus.
It was NOT yet proven novel.
~~~

---

# 4. Verification history — how D1 became the current P1

## D1-V001 — Broad D1 falsified

Read:

1. `outputs/verification/D1-V001/verification_matrix.md`
2. `outputs/verification/D1-V001/direction_verification.md`

Key papers:

- Narang et al. 2018
- Caruso et al. 2023
- Atakuru et al. 2024

Result:

~~~text
VERDICT = PIVOT
CONFIDENCE = high
~~~

Meaning:

- pressure/friction/slip mechanics already existed;
- bending-stiffness evolution had already been modeled;
- transition loads had already been characterized;
- modeling + FEA + experiment already existed.

The original D1 novelty claim was therefore substantially closed.

---

## D1-V002 — Continuum models already exist

Read:

1. `outputs/verification/D1-V002/verification_matrix.md`
2. `outputs/verification/D1-V002/adversarial_evidence_synthesis.md`

This round established that the contribution could not be:

> create a new continuum/homogenized layer-jamming model.

Continuum beam and constitutive formulations already existed.

The surviving question shifted to:

> When is a specified reduced/continuum model accurate enough, and where does it break down?

This is the conceptual birth of the current thesis.

---

## D1-V003 — Direct validity-gap attack

Read protocol first:

1. `docs/protocols/D1-V003_LITERATURE_AUDIT_PLAN.md`
2. `docs/protocols/D1-V003_VALIDITY_GAP_SEARCH_PROTOCOL.md`

Then read:

3. `outputs/verification/D1-V003/FAN_2026_MODEL_AUDIT.md`
4. `outputs/verification/D1-V003/ZHANG_2025_DEEPER_UNDERSTANDING_AUDIT.md`
5. `outputs/verification/D1-V003/D1-V003_EVIDENCE_MATRIX.md`
6. `outputs/verification/D1-V003/D1-V003_SEARCH_LOG.md`
7. `outputs/verification/D1-V003/cross_round_adversarial_synthesis.md`

Result:

~~~text
SURVIVES_WITH_REVISED_SCOPE
~~~

Key lesson:

Existence of a continuum model is not the same as a quantitative validity-domain study.

---

## D1-V004 / C01 — Frictional multilayer mechanics

Read:

1. `outputs/verification/D1-V004/verification_matrix.md`
2. `outputs/verification/D1-V004/C01_ADVERSARIAL_AUDIT.md`

Result:

~~~text
SUBSTANTIALLY_NARROWED
~~~

This removed broad novelty claims based on:

- discrete-to-continuum transition;
- asymptotic continuum limits;
- finite-layer error comparisons;
- generic homogenization of layered structures.

---

## D1-V005 / C02 — Partial-interaction composite beams

Read:

1. `outputs/verification/D1-V005/verification_matrix.md`
2. `outputs/verification/D1-V005/C02_ADVERSARIAL_AUDIT.md`

This literature already supplied:

- interaction parameters;
- effective EI concepts;
- exact-vs-approximate benchmarking;
- partial-interaction criteria;
- connector-discreteness studies.

Therefore these ideas alone cannot carry novelty.

---

## D1-V006 / C03 — Imperfect interfaces, friction and contact

Read:

1. `outputs/verification/D1-V006/verification_matrix.md`
2. `outputs/verification/D1-V006/C03_ADVERSARIAL_AUDIT.md`

This round produced the strongest generic threat:

> Wang et al. 2026, paper_id `ca46dc062d`

It already contained much of the generic validity framework:

- continuum multilayer model;
- Coulomb friction/contact;
- discrete-contact comparison;
- quantitative error;
- finite layer/deformation sweeps;
- an adopted 5% applicability threshold;
- experiments.

The surviving contribution therefore became narrower still.

---

## D1-V007 / C04 — Forward-citation closure

Read:

1. `outputs/verification/D1-V007/verification_matrix.md`
2. `outputs/verification/D1-V007/C04_ADVERSARIAL_AUDIT.md`
3. `outputs/verification/D1-V007/C04_SEMANTIC_CORRECTION.md`

The semantic correction is mandatory reading.

Core distinction:

~~~text
observed/adopted/post-hoc threshold
≠
predeclared acceptance tolerance
~~~

For this project, PREDECLARED means:

> fixed before the relevant validation/model-error results are inspected.

This distinction is now part of the methodological guardrail.

---

## D1-V008 — Final named-target closure

Read:

1. `outputs/verification/D1-V008/verification_matrix.md`
2. `outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.md`
3. `outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json`

Result:

~~~text
SURVIVES_FINAL_TARGET
kill_condition_met = false
broad_search_should_stop = true
final_novelty_lock_allowed = true
~~~

Interpretation:

The search protocol reached its defined stopping condition.

This is not proof of universal novelty. It is permission to stop indefinite broad searching and begin thesis execution.

---

# 5. Exact model selection

After the novelty search stopped, read:

1. `docs/research_design/LAYER_JAMMING_MODEL_COMPARISON.md`
2. `docs/learning/CURRENT_RESEARCH_DIRECTION_TUTORIAL.md`
3. `docs/research_design/EXACT_MODEL_SELECTION.md`

The two final model candidates were:

~~~text
M1 = Zhang 2025 continuum beam model
M2 = Zhang 2025/2026 RVE-derived constitutive continuum model
~~~

The user selected:

~~~text
M1
~~~

because the current thesis is a beam-scale validity study rather than an RVE-to-continuum constitutive-validation study.

---

# 6. D1-V009 — late-found post-lock audit

Read:

1. `docs/protocols/D1-V009_LATE_FOUND_ADJACENT_AUDIT_PLAN.md`
2. `outputs/verification/D1-V009/verification_matrix.md`
3. `data/evidence/Mech Cohesive Frict Material - 1999 - Adhikary - Modelling the large deformation_d75a3e82bc.json`
4. `outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.md`
5. `outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.json`

Target:

> Adhikary, Mühlhaus, and Dyskin (1999), *Modelling the large deformations in stratified media—the Cosserat continuum approach*.

Result:

~~~text
STATUS = SURVIVES_LATE_FOUND_TARGET
CONFIDENCE = high
KILL CONDITION = false
FINAL NOVELTY LOCK SURVIVES = true
REOPEN BROAD SEARCH = false
TARGETED FOLLOW-UP = false
~~~

What D1-V009 removes from novelty language:

- equivalent/smeared continuum modeling of frictional layered media;
- Cosserat/generalized continuum treatment;
- couple stresses and independent rotations for layer bending stiffness;
- large-deformation layered continua;
- frictional/plastic interlayer slip;
- interface opening/delamination;
- FE implementation of those mechanics.

What remains defensible:

- one specified reduced vacuum-layer-jamming model;
- output-specific acceptance tolerances fixed before final error inspection;
- quantitative reduced-vs-full-layer model-form error mapping;
- layer-count/discreteness and vacuum-pressure validity variables;
- tolerance-defined valid/invalid regions;
- experiments intentionally probing both sides of the predicted boundary;
- vacuum-specific normal-contact / friction / pressure-redistribution / separation mechanics where relevant.

---

# 7. Theoretical lineage after D1-V009

The literature should now be understood as two converging lineages.

## Lineage A — General layered-media mechanics

~~~text
classical layered / partial-interaction mechanics
        ↓
Cosserat / generalized continuum approaches
        ↓
Adhikary et al. 1999
equivalent continuum
+ independent rotations
+ couple stresses
+ large deformation
+ frictional/plastic interfaces
+ opening / delamination
        ↓
modern multilayer homogenization / imperfect-interface / contact mechanics
~~~

## Lineage B — Layer-jamming-specific mechanics

~~~text
Narang 2018
two-layer analytical mechanics
+ explicit frictional-contact FEA
+ experiments
        ↓
Caruso 2023
arbitrary multilayer discrete-interface progressive slip
+ pressure
+ friction
+ stiffness degradation
+ FEA
+ experiments
        ↓
Zhang 2025
continuum beam representation
+ continuous slip-zone description
+ stress fields
+ load-deflection prediction
        ↓
CURRENT QUESTION
When, quantitatively, is Zhang M1 valid?
~~~

The thesis contribution is not the invention of continuum layered mechanics. It is the quantitative, experimentally tested validity architecture for a specified vacuum layer-jamming reduced model.

---

# 8. Current research architecture

Read the current canonical architecture:

1. `docs/research_design/M1_RESEARCH_ARCHITECTURE.md`
2. `docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md`

## Locked

~~~text
RESEARCH DIRECTION =
quantitative validity / breakdown of a vacuum layer-jamming beam model

REDUCED MODEL M =
Zhang et al. 2025 continuum beam model
DOI 10.5194/ms-16-821-2025

GENERAL CONTRIBUTION =
determine when M1 is acceptably accurate and when it is not
~~~

## Still provisional

~~~text
PRIMARY REFERENCE R
PRIMARY OUTPUTS
PRIMARY BREAKDOWN VARIABLES
FINAL RESEARCH QUESTION
FINAL HYPOTHESIS
ERROR METRICS
ERROR TOLERANCES
PARAMETER-SPACE BOUNDS
CALIBRATION / VALIDATION SPLIT
EXPERIMENTAL BOUNDARY-SAMPLING PLAN
~~~

The current working title is:

> **Quantitative Validity Limits of a Continuum Model for Vacuum Layer-Jamming Beams under Quasi-Static Bending**

Treat it as a working thesis title until the exact RQ and reference architecture are frozen.

---

# 9. Forward execution roadmap — what to do next

From D1-V009 onward, do not return to broad topic discovery unless a concrete high-threat source appears.

The research now proceeds through execution gates.

---

## Gate 1 — Reconstruct M1 completely

Goal:

> understand M1 well enough to derive, explain, implement, and challenge it without relying on the paper line by line.

Create an M1 reconstruction record containing:

- physical system;
- notation;
- state variables;
- governing equations;
- assumptions;
- jammed / partial-slip / full-slip logic;
- load regimes;
- incremental algorithm;
- published numerical examples;
- published experiments;
- reported discrepancies;
- every assumption that could generate breakdown.

Required conceptual chain:

~~~text
physical mechanism
→ assumption
→ governing equation
→ state transition
→ predicted output
→ validation evidence
→ possible failure mode
~~~

**Exit criterion:** you can reproduce the computational flow of M1 from a blank page.

---

## Gate 2 — Lock the primary reference R

Current provisional choice:

> full-layer explicit-contact finite-element model.

The exact formulation must be frozen:

- FE software/solver;
- 2D vs 3D;
- layer representation;
- element type;
- interface/contact formulation;
- friction law;
- pressure application;
- membrane representation or justified omission;
- contact separation/lift-off treatment;
- boundary conditions;
- nonlinear geometry;
- convergence criteria;
- mesh-convergence protocol;
- numerical uncertainty estimate.

Do not call R "truth." It is a higher-fidelity reference with its own assumptions.

**Exit criterion:** a written, reproducible reference-model specification exists.

---

## Gate 3 — Lock primary outputs

Current candidates:

~~~text
O1 = beam deflection w
O2 = effective bending stiffness K or EI_eff
O3 = slip-transition load Q_slip or equivalent applied load
~~~

For each output define:

- exact mathematical definition;
- where it is measured;
- how M1 produces it;
- how R produces it;
- how experiment measures it;
- units;
- uncertainty;
- treatment near zero denominator.

**Exit criterion:** the same output can be extracted consistently from M1, R, and experiment.

---

## Gate 4 — Lock breakdown variables

Current candidates:

~~~text
B1 = finite layer count n
B2 = vacuum pressure p
B3 = bending severity P, kappa, or a normalized equivalent
~~~

Possible secondary variables later:

- friction coefficient;
- layer thickness;
- aspect ratio;
- boundary condition;
- initial curvature;
- membrane/sheath effects;
- pressure redistribution;
- separation/lift-off.

Do not expand dimensionality until the primary three-variable study is feasible.

**Exit criterion:** each variable has a physical rationale, controllable range, and measurable implementation.

---

## Gate 5 — Freeze research question and hypothesis

Working RQ:

> Under what combinations of finite layer count, vacuum pressure, and bending severity does the Zhang et al. continuum layer-jamming beam model remain within predeclared output-specific model-form error tolerances relative to an explicit full-layer frictional-contact reference and physical experiments?

Working hypothesis:

> M1 should approach the finite-layer reference as layer count increases, but model-form error may increase for small layer count, stronger slip/bending states, and conditions where contact-pressure redistribution or separation becomes important.

These remain provisional until Gates 1–4 are complete.

**Exit criterion:** RQ and hypothesis are falsifiable and map directly to measurable variables and outputs.

---

## Gate 6 — Define error metrics and PREDECLARE tolerances

Candidate relative errors:

~~~math
e_w = |w_M-w_R|/|w_R|
~~~

~~~math
e_K = |K_M-K_R|/|K_R|
~~~

~~~math
e_Q = |Q_{slip,M}-Q_{slip,R}|/|Q_{slip,R}|
~~~

Alternative absolute or normalized metrics may be necessary near zero denominators.

Tolerance workflow:

~~~text
define output
→ define error metric
→ justify acceptable error
→ freeze tolerance
→ only then inspect final validation map
~~~

Do not choose 5% simply because another paper uses 5%.

Tolerance justification may use:

- engineering use-case;
- experimental uncertainty;
- reference-model uncertainty;
- numerical uncertainty;
- sensitivity of decisions to prediction error.

**Exit criterion:** tolerance values and justification are timestamped/frozen before final validation.

---

## Gate 7 — Define parameter space and study design

Specify:

- ranges and levels for (n);
- ranges and levels for (p);
- load/curvature domain;
- geometry/material constants;
- friction calibration plan;
- calibration subset;
- validation subset;
- experimental subset.

Prefer nondimensional groups where physically meaningful, but do not force nondimensionalization before M1 mechanics are understood.

**Exit criterion:** a finite run matrix exists and can be executed within MSc time/resources.

---

## Gate 8 — Implement and verify M1

Recommended order:

~~~text
reproduce one published M1 case
→ reproduce stress/slip-state quantities
→ reproduce load-deflection case
→ test incremental convergence
→ freeze implementation
~~~

Do not tune M1 using the final validation cases.

**Exit criterion:** implementation reproduces published M1 benchmarks within documented numerical error.

---

## Gate 9 — Build and verify R

Recommended order:

~~~text
single layer sanity check
→ two-layer contact benchmark
→ frictionless / fully bonded limits
→ mesh convergence
→ contact convergence
→ finite-layer reference cases
→ freeze R
~~~

Where possible, use Narang/Caruso or other verified analytical limits as debugging benchmarks.

**Exit criterion:** R passes independent verification and its numerical uncertainty is quantified.

---

## Gate 10 — Generate model-form error surfaces

For each parameter point:

~~~text
run M1
run R
extract identical outputs
compute error
compare with predeclared tolerance
classify VALID / INVALID per output
~~~

Validity may be output-specific:

~~~text
VALID for deflection
INVALID for slip-transition load
~~~

Do not force a single universal boundary unless evidence supports one.

**Exit criterion:** preliminary validity/breakdown surfaces exist without post-hoc tolerance changes.

---

## Gate 11 — Diagnose WHY breakdown occurs

Use secondary quantities only after the primary validity map exists:

- slip-zone position;
- discrete interface slip;
- contact-pressure redistribution;
- local opening/separation;
- shear stress distributions;
- energy dissipation;
- boundary effects.

Goal:

> explain the physical mechanism behind validity loss, not merely report error.

**Exit criterion:** each major invalid region has a defensible mechanics explanation.

---

## Gate 12 — Design experiments to test the boundary

Experiments must intentionally include:

~~~text
predicted-valid points
AND
predicted-invalid points
AND, if feasible,
near-boundary points
~~~

Do not only test cases where M1 already agrees with R.

Experimental plan must specify:

- specimen geometry;
- number of layers;
- material;
- membrane/envelope;
- vacuum regulation;
- pressure measurement;
- loading fixture;
- force measurement;
- displacement/curvature measurement;
- slip observation if feasible;
- uncertainty;
- repeats;
- calibration vs validation specimens.

**Exit criterion:** experiment can falsify the predicted boundary.

---

## Gate 13 — Final adjudication of the research hypothesis

After experiments, determine:

- which outputs remain valid;
- where numerical boundary survives experiment;
- where it shifts;
- whether M1 fails for the predicted reason;
- whether new mechanics are needed;
- whether one or several output-specific validity maps are required.

Possible scientifically valid outcomes include:

~~~text
hypothesis supported
hypothesis partly supported
hypothesis rejected
boundary exists but differs from prediction
no simple monotonic boundary exists
~~~

A rejected hypothesis is not a failed thesis if the study design is sound.

---

# 10. 80/20 learning roadmap after M1 lock

Learn only what the implementation requires.

Priority chain:

~~~text
Euler-Bernoulli beam mechanics
→ shear force / bending moment / curvature
→ cross-sectional shear-stress distribution
→ Coulomb friction
→ stick / partial slip / full slip
→ layered-beam / partial-interaction mechanics
→ continuum approximation
→ incremental nonlinear solution
→ finite-element contact mechanics
→ model verification and validation
→ uncertainty and error metrics
~~~

Add Cosserat/generalized continuum mechanics as theoretical lineage and as a comparison framework where useful, but it is not automatically required for implementing M1.

---

# 11. Evidence-audit ladder for every important conclusion

Use this hierarchy:

| Level | Source | Question |
|---|---|---|
| L0 | summary / markdown verdict | What did the agent conclude? |
| L1 | structured JSON | Which exact fields define the conclusion? |
| L2 | verification matrix | Which papers support it? |
| L3 | evidence JSON | What was extracted from each paper? |
| L4 | original PDF | Does the primary source actually support the extraction? |
| L5 | prompt/raw/provenance | What did the model see, and could the prompt have biased the result? |

Never stop at L0 for a thesis-critical claim.

---

# 12. Current stop/search rule

Broad searching remains stopped after D1-V009.

Reopen literature search only if one of the following occurs:

1. a concrete paper is discovered that appears to satisfy a missing kill-chain link;
2. a forward citation or reference directly names a high-threat predecessor;
3. implementation reveals a governing theory or model family that the prior audit did not cover;
4. mentor/reviewer raises a specific prior-art challenge that can be operationalized into a targeted search.

Do not reopen broad search merely because more papers exist.

---

# 13. Current source-of-truth files

For current status, prefer:

1. `outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.md`
2. `outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.md`
3. `docs/research_design/EXACT_MODEL_SELECTION.md`
4. `docs/research_design/M1_RESEARCH_ARCHITECTURE.md`
5. `docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md`
6. this roadmap.

Historical files such as `docs/project/RESEARCH_STATE.md`, `docs/project/RESEARCH_LOG.md`, and `docs/literature/LITERATURE_STRATEGY.md` remain useful for chronology but are not the latest current-state authority.

---

# 14. Immediate next action

The next scientific task is:

> **Reconstruct M1 completely before locking R.**

Do not yet finalize:

- tolerance values;
- exact parameter ranges;
- experiment points;
- final hypothesis wording.

First understand the selected reduced model deeply enough to know:

- what physics it keeps;
- what physics it removes;
- what assumptions make the reduction possible;
- which assumptions are plausible breakdown mechanisms;
- which outputs are actually available and experimentally measurable.

Only then lock the reference model and the final research design.
