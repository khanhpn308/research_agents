# PROJECT HANDOFF — CURRENT RESEARCH STATE

> **Purpose:** Fast handoff for a new chat/agent.  
> **Use this file as the current project entry point.**  
> For any thesis-critical claim, drill down into the referenced canonical files and original evidence rather than trusting this summary alone.

---

# 1. Current thesis title

## English

**Validity Assessment of a Continuum Model for Vacuum Layer-Jamming Beams through Full-Layer Simulation and Experimental Validation**

## Vietnamese

**Đánh giá giới hạn hiệu lực của mô hình liên tục cho dầm kẹt lớp chân không bằng mô phỏng toàn lớp và kiểm chứng thực nghiệm**

This is the current working thesis title and should be treated as the default title unless deliberately revised later.

---

# 2. Research direction in one sentence

The thesis asks:

> **Under what conditions is a selected continuum model for a vacuum layer-jamming beam sufficiently accurate, and under what conditions does it break down when compared against a higher-fidelity full-layer reference and physical experiments?**

The thesis is therefore a **model-validity / model-form-error study**, not a project to invent a new continuum model.

---

# 3. Core research architecture

Use the shorthand:

~~~text
M → R → E
~~~

where:

## M — Reduced / continuum model

The selected model is:

**M1 — Zhang et al., _A continuum-based model for a layer jamming beam_**  
DOI: **10.5194/ms-16-821-2025**

M1 replaces an explicitly layered stack with a continuum beam representation and predicts quantities such as:

- shear stress distribution;
- jammed / partial-slip / full-slip state;
- slip-zone boundary;
- bending response;
- load-deflection behavior.

## R — Reference model

Current provisional reference:

> **Full-layer explicit-contact finite-element model**

R should explicitly represent:

- individual layers;
- interfaces between layers;
- normal contact;
- Coulomb friction;
- stick/slip;
- possible separation/lift-off;
- vacuum-pressure-related normal contact mechanics.

R is a **higher-fidelity numerical reference**, not "truth."

## E — Experiment

Physical layer-jamming beam experiments are used to test whether the conclusions from M-vs-R comparison hold in reality.

The intended logic is:

~~~text
M1 prediction
→ compare with R
→ quantify model-form error
→ classify valid / invalid region
→ experimentally test predicted-valid and predicted-invalid conditions
~~~

---

# 4. Current surviving contribution

After D1-V001 through D1-V009, the surviving contribution is:

> For one specified reduced/continuum vacuum-layer-jamming beam model under quasi-static bending, define output-specific acceptance tolerances before final validation/error inspection, then determine experimentally supported validity/breakdown regions against an interface-resolving/full-layer reference, while accounting for vacuum-pressure-controlled contact, friction/slip evolution, and—where relevant—pressure redistribution or layer separation.

Important:

- The contribution is **not** "continuum modeling of layered media."
- The contribution is **not** "frictional slip in layered structures."
- The contribution is **not** "Cosserat continuum."
- The contribution is **not** "large-deformation layered continuum."
- The contribution is **not** "FE modeling of multilayer friction."

Those mechanics already exist in prior literature.

---

# 5. Current novelty / falsification status

## Discovery phase

54 seed papers were used to generate 5 candidate research directions.

D1 was initially selected, but the broad D1 was later falsified/narrowed.

## Verification rounds

### D1-V001

Broad D1 was challenged using Narang 2018, Caruso 2023, Atakuru 2024.

Result:

~~~text
PIVOT
confidence: high
~~~

Broad novelty around pressure/friction/slip/bending-stiffness modeling was not defensible.

### D1-V002

Established that continuum layer-jamming models already exist.

Therefore:

> **Do not propose a new continuum model as the thesis contribution.**

The research question shifted to validity limits of an existing model.

### D1-V003

Direct validity-gap audit.

Result:

~~~text
SURVIVES_WITH_REVISED_SCOPE
~~~

Existence of a continuum model does not equal systematic mapping of when that model is valid.

### D1-V004 / C01

Adjacent frictional multilayer mechanics.

Result:

~~~text
SUBSTANTIALLY_NARROWED
~~~

### D1-V005 / C02

Partial-interaction composite beam literature.

Result:

~~~text
SUBSTANTIALLY_NARROWED
~~~

### D1-V006 / C03

Imperfect-interface / friction-contact literature.

Strongest generic threat included a 2026 multilayer continuum/discrete-contact study with quantitative error and an adopted 5% criterion.

Important semantic guardrail:

> An adopted or observed 5% threshold is **not automatically a predeclared acceptance tolerance**.

### D1-V007 / C04

Forward-citation closure of the strongest generic threat.

Key correction:

~~~text
PREDECLARED
=
fixed a priori before the relevant validation/model-error results are inspected
~~~

### D1-V008

Final named high-threat target audit.

Result:

~~~text
SURVIVES_FINAL_TARGET
kill condition: false
broad search stop: true
final novelty lock allowed: true
~~~

This was a **protocol stopping condition**, not proof that no overlapping paper exists anywhere.

### D1-V009

Late-found post-lock audit of:

**Adhikary, Mühlhaus, Dyskin (1999), _Modelling the large deformations in stratified media—the Cosserat continuum approach_**

Result:

~~~text
SURVIVES_LATE_FOUND_TARGET
confidence: high
kill condition: false
final novelty lock survives: true
reopen broad search: false
targeted follow-up required: false
~~~

D1-V009 established that the following are old mechanics and cannot be claimed as novel:

- equivalent/smeared continuum treatment of layered media;
- Cosserat/generalized continuum mechanics;
- independent rotations and couple stresses;
- layer-bending stiffness in continuum representation;
- large-deformation layered continua;
- frictional/plastic interlayer slip;
- interface opening/delamination;
- FE implementation of those mechanics.

---

# 6. What is currently LOCKED

~~~text
RESEARCH DOMAIN
=
vacuum layer-jamming beam validity

REDUCED MODEL M
=
Zhang et al. continuum beam model
DOI 10.5194/ms-16-821-2025

GENERAL SCIENTIFIC QUESTION
=
when is M1 acceptably accurate and when does it break down?

BROAD SEARCH STATUS
=
stopped unless a concrete new high-threat source appears
~~~

---

# 7. What is NOT yet fully locked

The following remain provisional and must be finalized through research design:

~~~text
PRIMARY REFERENCE R
exact FE formulation
FE solver/software
2D vs 3D
contact formulation
friction law
vacuum-pressure representation
separation/lift-off treatment

PRIMARY OUTPUTS
deflection?
effective stiffness?
slip-transition load?
other output-specific quantities?

PRIMARY BREAKDOWN VARIABLES
finite layer count n
vacuum pressure p
bending severity/load/curvature
possibly secondary variables later

FINAL RESEARCH QUESTION
FINAL HYPOTHESIS
ERROR METRICS
ERROR TOLERANCES
PARAMETER SPACE
CALIBRATION / VALIDATION SPLIT
EXPERIMENTAL BOUNDARY-SAMPLING PLAN
~~~

---

# 8. Current working research question

Current working version:

> **Under what combinations of finite layer count, vacuum pressure, and bending severity does the Zhang et al. continuum layer-jamming beam model remain within predeclared output-specific model-form error tolerances relative to an explicit full-layer frictional-contact reference and physical experiments?**

This is still a **working RQ**, not yet final.

---

# 9. Current working hypothesis

Current provisional hypothesis:

> As layer count increases, M1 should generally approach the finite-layer reference. Model-form error is expected to increase for small layer count, stronger bending/slip conditions, and conditions where local contact-pressure redistribution or layer separation becomes important.

This is a **hypothesis**, not a conclusion.

It may be rejected without invalidating the thesis.

---

# 10. Current candidate outputs

Provisional candidates:

~~~text
O1 = beam deflection w
O2 = effective bending stiffness K or EI_eff
O3 = slip-transition load Q_slip or equivalent external load
~~~

Possible model-form error metrics:

~~~math
e_w = |w_M - w_R| / |w_R|
~~~

~~~math
e_K = |K_M - K_R| / |K_R|
~~~

~~~math
e_Q = |Q_{slip,M} - Q_{slip,R}| / |Q_{slip,R}|
~~~

These are not yet final.

Near-zero denominators may require absolute or normalized alternatives.

---

# 11. Current candidate breakdown variables

Primary candidates:

~~~text
B1 = finite layer count n
B2 = vacuum pressure p
B3 = bending severity P, kappa, or a normalized equivalent
~~~

Possible secondary variables later:

- friction coefficient;
- layer thickness;
- aspect ratio;
- boundary conditions;
- membrane/sheath effects;
- pressure redistribution;
- separation/lift-off.

Do not expand the parameter space prematurely.

---

# 12. Immediate next scientific task

The next task is **NOT broad literature search**.

The next task is:

> **Reconstruct M1 completely.**

The user should understand M1 well enough to explain and eventually implement:

~~~text
physical mechanism
→ assumptions
→ governing equations
→ shear stress
→ Coulomb condition
→ jammed / partial-slip / full-slip states
→ slip-zone boundary
→ bending response
→ load-deflection prediction
→ incremental update
→ possible breakdown mechanisms
~~~

Only after M1 is deeply understood should the exact reference model R be frozen.

---

# 13. Minimal knowledge needed to start

The current 80/20 learning stack is:

~~~text
1. Euler-Bernoulli beam mechanics
2. shear force / bending moment / curvature
3. cross-sectional shear stress
4. Coulomb friction
5. stick / partial slip / full slip
6. layered-beam and partial-interaction intuition
7. M1 continuum beam model
8. incremental nonlinear mechanics
9. FEM fundamentals
10. contact + frictional FE
11. verification / validation
12. uncertainty / model-form error
13. experimental mechanics
~~~

Learn only what is required by M1 and R.

Do not drift into broad soft-robotics theory unless directly needed.

---

# 14. Conceptual meaning of the thesis

The physical system is:

~~~text
many finite layers
+ many interfaces
+ normal contact
+ friction
+ slip
+ possible separation
~~~

M1 replaces this with a simplified continuum representation.

The thesis asks:

> **How far can that simplification be trusted?**

A useful mental model is:

~~~text
M1 = fast simplified model
R  = detailed full-layer numerical reference
E  = physical experiment
~~~

The thesis studies:

~~~text
M ↔ R ↔ E
~~~

---

# 15. Evidence hierarchy

For any important claim, use:

~~~text
L0 — markdown summary / verdict
↓
L1 — structured JSON result
↓
L2 — verification matrix
↓
L3 — evidence JSON
↓
L4 — original PDF
↓
L5 — prompt / raw output / provenance
~~~

Core audit question:

> **Does the inference at this level actually follow from the evidence below it?**

Never rely only on L0 for thesis-critical claims.

---

# 16. Search-stop rule

Broad search remains stopped after D1-V009.

Reopen only if:

1. a concrete new paper appears to satisfy a missing kill-chain link;
2. a forward citation/reference names a direct high-threat predecessor;
3. implementation exposes a relevant theory/model family not previously covered;
4. mentor/reviewer raises a specific prior-art challenge suitable for targeted search.

Do not reopen broad search just because more literature exists.

---

# 17. Current theoretical lineage

## General layered-media mechanics

~~~text
classical layered / partial-interaction mechanics
→ Cosserat / generalized continuum approaches
→ Adhikary et al. 1999
→ modern imperfect-interface / homogenization / contact mechanics
~~~

## Layer-jamming-specific mechanics

~~~text
Narang 2018
→ Caruso 2023
→ Zhang 2025 continuum beam model
→ current question: quantitative validity limits of M1
~~~

The thesis contribution is **not** the invention of continuum layered mechanics.

---

# 18. Canonical files to read in a new chat

Use these as source of truth:

1. `docs/project/POST_D1_V009_RESEARCH_ROADMAP_VI.md`
2. `docs/project/POST_D1_V009_RESEARCH_ROADMAP.md`
3. `docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md`
4. `docs/research_design/M1_RESEARCH_ARCHITECTURE.md`
5. `docs/research_design/EXACT_MODEL_SELECTION.md`
6. `outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.md`
7. `outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.md`

Historical files are useful for chronology but are not the latest authority.

---

# 19. Recommended prompt for a new chat/agent

Copy this into a new chat:

~~~text
I am continuing an MSc research project titled:

Validity Assessment of a Continuum Model for Vacuum Layer-Jamming Beams through Full-Layer Simulation and Experimental Validation

Use docs/project/PROJECT_HANDOFF_CURRENT.md as the primary project handoff.

Then, when needed, drill into:
- docs/project/POST_D1_V009_RESEARCH_ROADMAP_VI.md
- docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md
- docs/research_design/EXACT_MODEL_SELECTION.md
- outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.md

Working rules:
1. Distinguish verified evidence, inference, and hypothesis.
2. Do not defend the topic by default.
3. Challenge incorrect assumptions directly.
4. Trace thesis-critical claims back to paper/evidence.
5. Help me understand and decide; do not decide for me.
6. Do not restart broad literature searching unless a concrete high-threat reason appears.
7. The current reduced model is M1: Zhang et al. 2025 continuum layer-jamming beam model.
8. The immediate task is to reconstruct and understand M1 before freezing reference model R.

Start by summarizing the research direction in no more than 7 sentences, then question me one step at a time to test whether I actually understand the topic.
~~~

---

# 20. Current bottom line

~~~text
TOPIC:
Validity Assessment of a Continuum Model for Vacuum Layer-Jamming Beams
through Full-Layer Simulation and Experimental Validation

M:
Zhang et al. 2025 continuum beam model

R:
full-layer explicit-contact FE reference
(exact implementation not yet frozen)

E:
physical experiment

NOVELTY POSITION:
validity/breakdown assessment of M1
not invention of continuum layered mechanics

SEARCH STATUS:
broad search stopped after D1-V009

NEXT TASK:
reconstruct M1 completely
→ then freeze R
→ then finalize outputs / variables / RQ / hypothesis / tolerances
→ implement
→ compare
→ experimentally test the predicted validity boundary
~~~


---

# 21. Active mentor-pivot audit branch

A mentor-proposed alternative direction is currently under adversarial novelty audit. It has **not** replaced the current D1/M1 thesis.

Candidate concept:

~~~text
superelastic NiTi / metal wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven syringe/piston pressure source
~~~

Current status:

- broad component novelty is already heavily pre-empted;
- the strongest surviving hypotheses concern NiTi wires themselves as the jamming medium, positive-pressure confinement of that metallic wire bundle, and possible coupling between superelastic response and inter-wire friction/slip;
- formal repository audit begins with `MP1-V001`;
- if the core mechanics survives, continue with `MP1-V002` targeted citation chasing;
- do not change the official thesis title or abandon D1/M1 until the MP1 branch reaches formal adjudication.

Entry points:

1. `docs/project/MENTOR_PIVOT_STATUS.md`
2. `docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md`
3. `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
4. `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`
5. `app/ingestion/mp1_v001_core_prior_art_audit.py`
