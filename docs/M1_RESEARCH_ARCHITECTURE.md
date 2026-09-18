# M1 Research Architecture

> **Status:** Working architecture after exact-model selection  
> **Selected reduced model:** M1 — Zhang et al., *A continuum-based model for a layer jamming beam*  
> **DOI:** 10.5194/ms-16-821-2025  
> **paper_id:** 95646b2cfc  
> **Evidence status:** VERIFIED FULL TEXT
>
> This document freezes the current thesis architecture after the literature-falsification pipeline reached its stop condition and the final novelty lock was allowed. It guides the next phase: reference-model selection, research-question lock, tolerance definition, model implementation, and experiment design.

---

## 1. Research premise now being executed

The surviving research premise is:

> For one specified reduced/continuum vacuum-layer-jamming beam model under quasi-static planar bending, define output-specific predeclared model-form acceptance tolerances and determine experimentally validated validity/breakdown boundaries against an interface-resolving/full-layer reference, while explicitly accounting for vacuum-pressure-controlled normal contact, friction/slip evolution, and, where necessary, pressure redistribution or layer separation.

The final adversarial audit concluded:

- the selected direction survives the final named-target check;
- no supplied source satisfies the complete kill chain;
- the currently identified forward-citation branch is closed;
- the final named high-threat DOI was audited from verified full text;
- no additional specifically named high-threat target remains;
- broad literature searching should stop;
- provisional final novelty lock is allowed.

This lock is **provisional for thesis execution**, not an absolute claim that no overlapping paper can ever exist.

---

# 2. Reduced model M — LOCKED

## M = Zhang et al. continuum layer-jamming beam model

~~~text
REDUCED MODEL M =
Zhang et al.
"A continuum-based model for a layer jamming beam"
DOI: 10.5194/ms-16-821-2025
paper_id: 95646b2cfc
~~~

### Why M1 is selected

M1 is selected because it already operates at the same structural level as the current P1:

~~~math
\text{vacuum pressure + friction + beam loading}
\rightarrow
\text{jam/slip state}
\rightarrow
\text{beam structural response}
~~~

Verified capabilities of M1 include:

- continuum treatment of a finite-height layer-jamming beam;
- explicit Coulomb slip condition;
- jammed / partially slipping / fully slipping states;
- cross-sectional slip boundary;
- internal stress distributions;
- critical slip thresholds;
- beam load–deflection response;
- comparison with finite-layer FEA;
- comparison with physical beam experiments.

Verified governing relations include:

~~~math
\tau(y,Q)
=
\frac{3}{2}\frac{Q}{A}
\left(
1-\frac{4y^2}{h^2}
\right)
~~~

~~~math
|\tau|=\mu p
~~~

and

~~~math
Q_{\mathrm{slip}}
=
\frac{2}{3}\mu p A
~~~

where:

- \(Q\): internal shear force;
- \(A=bh\): beam cross-sectional area;
- \(b\): beam width;
- \(h\): total stack height;
- \(y\): through-thickness coordinate;
- \(\mu\): interlayer friction coefficient;
- \(p\): vacuum/confining pressure.

---

# 3. What scientific reduction is being tested?

The central approximation in M1 is:

~~~math
\text{finite discrete layered beam}
\rightarrow
\text{continuum beam with continuous jam/slip representation}
~~~

The thesis is therefore **not** primarily asking whether a continuum model can be written. That has already been done.

The thesis asks:

> **When does this continuum approximation remain sufficiently accurate, and when does it stop being sufficiently accurate, relative to a higher-fidelity finite-layer reference and experiment?**

This is a model-validity question.

---

# 4. Reference architecture

## 4.1 Primary reference R — provisional lock

~~~text
PRIMARY REFERENCE R =
full-layer explicit-contact finite-element model
~~~

The intended high-fidelity reference should preserve as much of the omitted discrete mechanics as practically possible:

- every physical layer represented separately;
- individual interfaces represented explicitly;
- normal contact;
- Coulomb friction;
- stick/slip evolution;
- finite layer count;
- local contact-pressure redistribution;
- possible separation/lift-off where physically justified;
- the same beam geometry and boundary conditions used for M1 comparisons.

### Why this is the preferred reference

M1 removes discrete interfaces by replacing them with a continuum approximation. Therefore a useful reference should restore those interfaces:

~~~math
M:
\text{continuum approximation}
~~~

versus

~~~math
R:
\text{finite discrete layers + explicit frictional contact}
~~~

The reference should be treated as a **higher-fidelity numerical comparator**, not automatically as absolute physical truth.

Its own assumptions, mesh sensitivity, contact formulation, convergence behavior, and material parameters must also be documented.

---

## 4.2 Secondary reference

~~~text
SECONDARY REFERENCE =
Caruso et al. (2023)
"Layer jamming: Modeling and experimental validation"
paper_id: 652e62758f
~~~

Role:

- analytical/discrete mechanics benchmark;
- independent check on progressive interface slip;
- help verify critical slip transitions;
- help debug M1 and full-layer FE implementation.

Caruso 2023 should not replace the primary full-layer FE reference if the thesis objective is a structural validity/breakdown map with explicit contact mechanics.

---

# 5. Primary outputs — provisional lock

The first implementation should focus on a small number of outputs that are:

1. predicted by M1;
2. extractable from the reference model;
3. measurable experimentally;
4. directly relevant to structural performance.

## O1 — Beam deflection

~~~math
w
~~~

Recommended comparison quantity:

~~~math
e_w
=
\frac{|w_M-w_R|}
{|w_R|}
~~~

Why it matters:

- direct structural response;
- easy to obtain numerically;
- relatively easy to measure experimentally;
- intuitive for mentor/reporting;
- suitable for validity-map construction.

---

## O2 — Effective bending stiffness

~~~math
K
~~~

or an equivalent effective flexural rigidity:

~~~math
EI_{\mathrm{eff}}
~~~

Recommended comparison quantity:

~~~math
e_K
=
\frac{|K_M-K_R|}
{|K_R|}
~~~

Why it matters:

- variable stiffness is the central function of layer jamming;
- stiffness degradation reflects transition from jammed to slipping states;
- useful for comparing operating regions across pressure and layer count.

---

## O3 — Slip-transition load

A candidate quantity is:

~~~math
Q_{\mathrm{slip}}
~~~

or the corresponding externally applied load at first slip.

Recommended comparison quantity:

~~~math
e_Q
=
\frac{|Q_{\mathrm{slip},M}-Q_{\mathrm{slip},R}|}
{|Q_{\mathrm{slip},R}|}
~~~

Why it matters:

- tests whether M1 predicts the transition mechanism correctly;
- more mechanistic than deflection alone;
- directly connected to the Coulomb slip criterion.

### Secondary outputs for later consideration

These should not be promoted to primary outputs until the first implementation is stable:

- slip-zone extent \(y_s\);
- local interface slip;
- contact-pressure distribution;
- energy dissipation;
- hysteresis-loop area;
- local stress fields.

These may become useful for explaining *why* M1 fails after the main validity map is established.

---

# 6. Primary breakdown variables — provisional lock

The first validity study should avoid an excessively high-dimensional parameter space.

The initial three breakdown variables are:

## B1 — Finite layer count

~~~math
n
~~~

### Scientific reason

M1 relies on a continuum approximation of a layered structure.

Therefore finite layer count is one of the most direct variables for testing continuum validity.

Working hypothesis:

~~~math
n \uparrow
\quad\Rightarrow\quad
\text{discrete stack approaches continuum behavior}
~~~

but this must be tested rather than assumed.

Potential questions:

- Is there a minimum \(n\) above which deflection error remains acceptable?
- Does the required \(n\) depend on pressure?
- Does the required \(n\) increase near partial/full slip?

---

## B2 — Vacuum pressure

~~~math
p
~~~

### Scientific reason

Vacuum pressure directly controls frictional capacity in the M1 idealization:

~~~math
|\tau|_{\max}
=
\mu p
~~~

Pressure therefore affects:

- slip initiation;
- jammed/slipping region size;
- effective stiffness;
- structural response.

Potential breakdown mechanisms include:

- nonuniform contact pressure;
- deformation-induced pressure redistribution;
- local loss of contact;
- mismatch between ideal \(p\) and actual interface pressure.

---

## B3 — Bending severity

Candidate control variables:

~~~math
P
~~~

or

~~~math
\kappa
~~~

where \(P\) is applied transverse load and \(\kappa\) is beam curvature.

### Scientific reason

Increasing bending severity can move the structure through:

~~~text
fully jammed
→ partial slip
→ progressive slip
→ near/full slip
~~~

The continuum model is most likely to reveal model-form limits around these transitions and at large deformation.

The exact choice between load \(P\), curvature \(\kappa\), normalized deflection, or another nondimensional measure should be frozen only after M1 is fully reconstructed and the reference model is defined.

---

# 7. Initial research question

## English

> **Under what combinations of finite layer count, vacuum pressure, and bending severity does the Zhang et al. continuum layer-jamming beam model remain within predeclared output-specific model-form error tolerances relative to an explicit full-layer frictional-contact reference and physical experiments?**

## Vietnamese

> **Trong phạm vi nào của số lớp hữu hạn, áp suất chân không và mức độ uốn, mô hình continuum cho dầm layer-jamming của Zhang và cộng sự vẫn duy trì sai số mô hình trong các giới hạn chấp nhận được đã định trước khi so với mô hình full-layer có tiếp xúc–ma sát tường minh và thực nghiệm?**

This question is still a **working research question**. It should be frozen only after the exact reference formulation, outputs, and parameter definitions are locked.

---

# 8. Initial falsifiable hypothesis

> As the number of layers increases, M1 will generally approach the finite-layer reference more closely; however, model-form error is expected to increase for small layer counts, stronger bending/slip states, and conditions where local normal-contact pressure redistribution or separation becomes important.

This is a **hypothesis to test and potentially falsify**, not a conclusion.

The thesis should remain scientifically valid if one or more parts of this hypothesis are rejected.

---

# 9. Error metrics and predeclared tolerances

## 9.1 Error metrics

At minimum:

~~~math
e_w
=
\frac{|w_M-w_R|}
{|w_R|}
~~~

~~~math
e_K
=
\frac{|K_M-K_R|}
{|K_R|}
~~~

~~~math
e_Q
=
\frac{|Q_{\mathrm{slip},M}-Q_{\mathrm{slip},R}|}
{|Q_{\mathrm{slip},R}|}
~~~

Alternative normalized or absolute metrics may be needed near zero-valued denominators.

## 9.2 Predeclared tolerance rule

A tolerance is **predeclared** only if it is fixed before the final validation/error map is inspected.

Therefore the workflow must be:

~~~text
define output
→ define error metric
→ justify tolerance
→ freeze tolerance
→ run final validation
→ classify VALID / INVALID
~~~

Not:

~~~text
run validation
→ inspect errors
→ choose a convenient tolerance afterward
~~~

No value such as 5% should be adopted merely because another paper used 5%.

The final tolerances should be justified by some combination of:

- engineering relevance;
- experimental measurement uncertainty;
- numerical/reference uncertainty;
- intended model-use case;
- sensitivity of structural decisions to prediction error.

---

# 10. Validity-map concept

For each operating point:

~~~math
\mathbf{x}
=
\{n,p,\text{bending severity},\ldots\}
~~~

calculate one or more output errors:

~~~math
e_w(\mathbf{x}),
\quad
e_K(\mathbf{x}),
\quad
e_Q(\mathbf{x})
~~~

Then classify according to predeclared tolerances:

~~~math
e_i(\mathbf{x})
\le
\varepsilon_i
\quad\Rightarrow\quad
\text{VALID for output }i
~~~

and

~~~math
e_i(\mathbf{x})
>
\varepsilon_i
\quad\Rightarrow\quad
\text{INVALID for output }i
~~~

An important consequence is that model validity may be **output-specific**.

For example, the same operating point might be:

~~~text
VALID for deflection
INVALID for slip-transition load
~~~

Therefore the thesis should avoid speaking about a single universal validity boundary unless the evidence supports one.

---

# 11. Intended validation hierarchy

~~~text
Level 1
Reproduce M1 analytical results

        ↓

Level 2
Verify implementation against published M1 cases

        ↓

Level 3
Build and verify explicit full-layer FE reference R

        ↓

Level 4
Generate model-form error maps:
M1 vs R

        ↓

Level 5
Preselect experimental points on both sides
of predicted validity/breakdown boundaries

        ↓

Level 6
Run physical experiments

        ↓

Level 7
Assess whether the predicted boundary
survives experimental validation
~~~

The experiment should **not** merely test a few convenient points where the model already appears accurate.

At least some experimental points should intentionally probe:

~~~text
predicted-valid region
AND
predicted-invalid region
~~~

---

# 12. Current thesis architecture in one diagram

~~~text
INPUT SPACE
n, p, bending severity, geometry, μ, boundary condition
        │
        ├─────────────────────────────┐
        │                             │
        ▼                             ▼
M1: Zhang continuum model       R: full-layer FE model
        │                             │
        ▼                             ▼
   predictions                   reference outputs
        │                             │
        └──────────────┬──────────────┘
                       ▼
                  ERROR METRICS
             ew, eK, eQ, ...
                       │
                       ▼
          PREDECLARED TOLERANCES
             εw, εK, εQ, ...
                       │
                       ▼
              VALID / INVALID MAP
                       │
                       ▼
             PHYSICAL EXPERIMENTS
          on both sides of boundary
                       │
                       ▼
      EXPERIMENTALLY TESTED VALIDITY MAP
~~~

---

# 13. Items that are locked vs. still provisional

## Locked

~~~text
RESEARCH DIRECTION =
vacuum layer-jamming beam model validity

REDUCED MODEL M =
Zhang et al. continuum beam model
DOI 10.5194/ms-16-821-2025

GENERAL RESEARCH OBJECT =
validity/breakdown boundaries of M1
~~~

## Provisional — must still be frozen

~~~text
PRIMARY REFERENCE R =
full-layer explicit-contact FE model
(exact formulation not yet frozen)

SECONDARY REFERENCE =
Caruso 2023 discrete mechanics

PRIMARY OUTPUTS =
1. deflection
2. bending stiffness
3. slip-transition load

PRIMARY BREAKDOWN VARIABLES =
1. layer count
2. vacuum pressure
3. bending severity

RESEARCH QUESTION =
working version only

HYPOTHESIS =
working version only

ERROR TOLERANCES =
not yet defined
~~~

---

# 14. Immediate next tasks

The next work should proceed in this order:

1. **Reconstruct M1 completely**
   - every governing equation;
   - every state/variable;
   - all assumptions;
   - every loading regime;
   - the numerical/incremental algorithm;
   - published validation cases.

2. **Freeze exact reference model R**
   - software / solver;
   - dimensionality;
   - element type;
   - layer representation;
   - contact formulation;
   - friction law;
   - pressure application;
   - boundary conditions;
   - mesh-convergence protocol.

3. **Freeze primary outputs**
   - confirm \(w\), \(K\), and slip-transition load are all extractable from both M and R.

4. **Freeze parameter space**
   - define candidate values/ranges for \(n\), \(p\), and bending severity.

5. **Define error metrics and tolerances**
   - before final validation runs.

6. **Only then begin the final validation map.**

---

# 15. 80/20 knowledge-learning consequence

Because M1 is now selected, background study should be driven by the equations and implementation needs of M1.

The first 80/20 knowledge chain is expected to be:

~~~text
Euler–Bernoulli beam mechanics
        ↓
bending moment / shear force / curvature
        ↓
cross-sectional shear-stress distribution
        ↓
Coulomb friction
        ↓
stick / partial slip / full slip
        ↓
continuum approximation of layered beams
        ↓
incremental nonlinear beam solution
        ↓
contact mechanics needed for reference R
        ↓
finite-element validation
~~~

Do **not** study the whole fields of continuum mechanics, FEM, contact mechanics, or soft robotics before reconstructing M1.

Learn each concept only when it is required to understand, implement, challenge, or validate a specific part of the selected model.

---

# 16. Evidence provenance

This architecture is grounded in the current repository state, especially:

- docs/EXACT_MODEL_SELECTION.md
- data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json
- data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json
- docs/LAYER_JAMMING_MODEL_COMPARISON.md
- outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json

### Evidence / inference distinction

- Statements about what M1 predicts, its governing mechanics, assumptions, prior numerical comparison, and prior experiments are derived from the verified repository evidence.
- The choice of primary outputs, primary breakdown variables, reference architecture, hypothesis, and validation hierarchy are **research-design decisions / synthesis**, not claims made by Zhang et al.
- The exact FE reference formulation, tolerance values, experimental design, and final parameter ranges remain unresolved and must not be presented as already validated facts.
