# Exact Model Selection — Comparison of the Two Candidate Reduced Models

> **Purpose.** This document compares the two remaining candidate reduced/continuum models $M$ for the locked research premise P1. It is **not yet the final model-selection decision**. The comparison is restricted to locally verified full-text evidence already present in this repository.
>
> **Current P1:** For one specified reduced/continuum vacuum-layer-jamming beam model under quasi-static planar bending, define output-specific predeclared model-form acceptance tolerances and determine experimentally validated validity/breakdown boundaries against an interface-resolving/full-layer reference, while explicitly accounting for vacuum-pressure-controlled normal contact, friction/slip evolution, and, where necessary, pressure redistribution or layer separation.

---

## 1. Candidate models

| Label | Candidate model | DOI | paper_id | Evidence status |
|---|---|---|---|---|
| **M1** | Zhang et al., *A continuum-based model for a layer jamming beam* | \`10.5194/ms-16-821-2025\` | \`95646b2cfc\` | **VERIFIED FULL TEXT** |
| **M2** | Zhang et al., *Continuum modeling for layer jamming structures* | \`10.1016/j.taml.2025.100633\` | \`a792efc445\` | **VERIFIED FULL TEXT** |

### Core conceptual distinction

- **M1 is a structural beam model.** It treats the layer-jamming beam as a continuum elastoplastic beam and directly predicts quantities such as cross-sectional slip-zone boundary, stress distribution, shear-force thresholds, and beam deflection.
- **M2 is a constitutive/material model.** It homogenizes a discrete two-layer RVE into a macroscopic continuum constitutive relation using average-field techniques, then predicts macroscopic stress, plastic slip, tangent stiffness, and energy dissipation under general multiaxial loading.

Therefore the two models operate at different modeling levels:

```math
\text{M2: micro/RVE}
\rightarrow
\text{macroscopic constitutive law}
```

versus

```math
\text{M1: continuum beam mechanics}
\rightarrow
\text{structural response}
```

This difference is central to the final selection.

---

# 2. Seven-question evidence comparison

## Q1. What are the governing equations?

### M1 — Continuum beam model

The model uses Euler–Bernoulli-type beam mechanics together with a continuum description of a jammed/sliding cross-section.

A verified shear-stress field is

```math
\tau(y,Q)
=
\frac{3}{2}\frac{Q}{A}
\left(
1-\frac{4y^2}{h^2}
\right)
```

where $Q$ is internal shear force, $A=bh$ is section area, $h$ is total beam height, and $y$ is the through-thickness coordinate.

The Coulomb slip limit is governed by

```math
|\tau|=\mu p
```

and the verified slip-initiation shear-force threshold is

```math
Q_{\mathrm{slip}}
=
\frac{2}{3}\mu p A
```

A cross-sectional boundary $y_s$ separates jammed and sliding regions. The model then derives stress distributions and internal resultants $N,Q,M$, and integrates the structural equations to obtain beam deformation.

The model assumes, among other things:

- infinitely many sufficiently thin layers / continuum limit;
- plane-stress / Euler–Bernoulli beam behavior;
- radius of curvature much larger than beam height;
- constant Coulomb friction coefficient;
- deformation-induced interlaminar normal pressure is neglected in the analytical formulation;
- small deformation within each incremental loading step for large-deformation calculations.

**Interpretation:** M1 already contains the structural mapping

```math
\{p,\mu,\text{geometry},\text{load}\}
\rightarrow
\{\text{slip state},\text{stress field},\text{deflection}\}
```

### M2 — RVE / average-field constitutive model

M2 begins at the layer/interface scale and performs explicit homogenization.

Macroscopic stress is defined by volume averaging:

```math
\boldsymbol{\Sigma}
=
\frac{1}{V}
\int_V
\boldsymbol{\sigma}\,dV
```

The macroscopic displacement gradient is obtained from a boundary-surface average:

```math
D_{ij}
=
\frac{1}{V}
\int_{\partial V}
u_i n_j\,dS
```

The microscopic layer is linearly elastic:

```math
\boldsymbol{\sigma}
=
\lambda_L
\operatorname{tr}(\boldsymbol{\varepsilon})
\mathbf{I}
+
2G\boldsymbol{\varepsilon}
```

The verified interlayer slip/yield criterion is

```math
f(\boldsymbol{\Sigma})
=
\sqrt{\sigma_{13}^2+\sigma_{23}^2}
-
\mu(p-\sigma_{33})
=
0
```

After yielding, the formulation uses an elastoplastic stress-update framework with a plastic multiplier and a tangent constitutive operator.

**Interpretation:** M2 supplies a macroscopic constitutive relation

```math
d\boldsymbol{\Sigma}
=
\mathbf{C}^{ep}
:
d\mathbf{E}
```

derived from a discrete RVE with frictional contact.

---

## Q2. What are the exact inputs?

| Input category | M1 — continuum beam | M2 — homogenized RVE |
|---|---|---|
| Vacuum/confining pressure | $p$ | $p$ |
| Friction | $\mu$ | $\mu$ |
| Elastic properties | primarily $E$ and beam/layer properties | Lamé constants $\lambda_L,G$, equivalently elastic constants |
| Layer geometry | total $h$, width $b$, layer thickness / count through continuum assumption and validation cases | RVE spanning two layer thicknesses; layer thickness enters the RVE |
| Layer count | relevant to whether continuum assumption is valid; explicit finite-layer FEA comparisons exist | not an explicit macroscopic state variable; represents an effectively periodic/infinite stack |
| Structural geometry | beam length, section geometry, support configuration | no complete beam geometry is required at constitutive-material level |
| Loading | transverse beam loading / internal $N,Q,M$ | arbitrary prescribed macroscopic strain/loading path |
| Deformation mode | planar beam bending | multiaxial shear/normal loading |

### Important consequence

M1's inputs are already close to the parameter space needed by P1.

M2 must first be embedded into a structural beam/shell/solid solver before it can map vacuum pressure and beam loading to a complete force–deflection response.

---

## Q3. What outputs can the model predict?

### M1

Verified outputs include:

- internal shear stress \(\tau(y,s)\);
- normal stress \(\sigma(y,s)\);
- jammed/sliding boundary $y_s$;
- critical shear-force thresholds for slip regimes;
- internal $N,Q,M$;
- cantilever/load–deflection response;
- beam deformation under the tested structural configurations.

The paper also compares continuum predictions with finite-layer FEA and physical beam experiments.

### M2

Verified outputs include:

- macroscopic stress tensor and increments;
- macroscopic elastoplastic tangent stiffness $\mathbf{C}^{ep}$;
- interlayer/plastic sliding displacement variables;
- yield/slip surface evolution;
- elastic strain-energy density;
- frictional dissipation-energy density;
- microscopic RVE stress/displacement distributions in the numerical reference.

However, M2 does **not by itself** directly output a full layer-jamming beam force–deflection curve until it is embedded in a structural solver.

---

## Q4. What physics are homogenized or omitted?

### M1 — what is reduced

M1 replaces the discrete stack by a continuum beam and replaces discrete layer-by-layer slip states by a continuous jammed/sliding description through the cross-section.

Important assumptions/omissions supported by the verified source include:

1. continuum limit of many thin layers;
2. ideal constant Coulomb friction;
3. Euler–Bernoulli-type beam assumptions;
4. deformation-induced interlayer normal pressure is neglected in the analytical model;
5. finite-layer discreteness is not represented exactly;
6. boundary/end effects are imperfectly represented;
7. full-slip/extreme-load behavior is less reliable;
8. local pressure redistribution can therefore become a source of model error.

This creates a direct candidate breakdown problem for P1:

```math
\text{When does the continuum beam approximation cease to match a finite-layer/contact-resolved beam?}
```

### M2 — what is homogenized

M2 performs an explicit RVE-to-continuum homogenization using average-field techniques.

The source assumes:

1. isotropic linear-elastic layer material;
2. first-order displacement approximation through the layer thickness;
3. approximately constant stress/strain state within the discrete RVE under that approximation;
4. small contact displacement before sliding;
5. hydrostatic vacuum pressure represented as a constant initial stress state;
6. ideal Coulomb friction with constant $\mu$;
7. periodic RVE behavior.

The verified evidence identifies or implies missing physics such as:

- structural boundary/end effects;
- membrane/sheath mechanics;
- nonuniform vacuum-pressure fields;
- pressure redistribution at structural scale;
- finite-layer-count effects;
- severe large deformation outside the first-order RVE assumptions;
- physical material-level experimental validation.

This creates a different breakdown problem:

```math
\text{When does an ideal periodic RVE constitutive law cease to represent a finite vacuum-jammed structure?}
```

---

## Q5. Can it be implemented independently in MATLAB/Python?

### M1 — implementation assessment

**Yes, likely with moderate complexity.**

The governing variables are beam-scale quantities and the analytical formulation is already expressed in terms of $N,Q,M$, stress fields, slip boundary $y_s$, and beam deformation.

A plausible independent implementation architecture is:

```math
\text{load increment}
\rightarrow
Q(s),M(s)
\rightarrow
y_s(s)
\rightarrow
\sigma,\tau
\rightarrow
\kappa(s)
\rightarrow
w(s)
```

A MATLAB or Python implementation would require reconstruction and verification of the paper's equations and incremental algorithm, but no evidence in the repository is being interpreted here as proof that the authors supply reusable code.

**Implementation burden:** beam solver + slip-state/update logic.

### M2 — implementation assessment

**Yes, but with higher integration complexity.**

At material-point level the workflow would resemble:

```math
d\mathbf{E}
\rightarrow
\boldsymbol{\Sigma}^{\mathrm{trial}}
\rightarrow
f(\boldsymbol{\Sigma}^{\mathrm{trial}})
\rightarrow
\begin{cases}
\text{elastic update}, & f<0 \\
\text{plastic/slip return}, & f\ge 0
\end{cases}
\rightarrow
\mathbf{C}^{ep}
```

This can be coded in MATLAB/Python as a constitutive-point solver. But to obtain the beam-level outputs required by P1, the constitutive model must then be coupled to a structural discretization such as:

- custom beam/continuum solver;
- finite-element code;
- Abaqus UMAT/material implementation.

The paper's own future-work/gap discussion supports the need to move from constitutive RVE behavior to structural-level implementation and validation.

**Implementation burden:** constitutive integration **plus** structural solver/coupling.

---

## Q6. Is there an interface-resolved reference model available for benchmarking?

### M1

**Yes.**

The verified corpus provides several suitable reference routes:

1. the M1 paper itself compares its continuum prediction with finite-layer FEA for 10- and 25-layer cantilevers;
2. Caruso et al. (2023), \`paper_id 652e62758f\`, retains discrete interlayer slip states and provides a natural analytical/discrete benchmark;
3. an explicit finite-layer frictional-contact FEA can serve as the full-layer reference $R$.

For P1, the exact reference still needs to be frozen, but M1 already has a very direct structural reduced-vs-discrete comparison path.

### M2

**Yes at RVE level, but not yet fully at structural level.**

The paper validates the constitutive theory against a 3D Abaqus RVE array with:

- finite-sliding surface-to-surface contact;
- periodic boundary conditions;
- C3D8H elements.

Therefore there is an interface-resolved numerical reference for the **constitutive point/RVE**.

However, the verified source explicitly lacks structural-level physical experimental validation. To use M2 for P1, a second bridge is needed:

```math
\text{RVE constitutive model}
\rightarrow
\text{beam implementation}
\rightarrow
\text{full finite-layer beam reference}
\rightarrow
\text{experiment}
```

That bridge is substantially larger than for M1.

---

## Q7. Is there a parameter space in which the model may break down?

### M1 — likely breakdown dimensions

The verified evidence already identifies several plausible axes:

- finite/small layer count versus continuum limit;
- layer thickness;
- vacuum pressure $p$;
- applied shear force / bending load;
- curvature / large deformation;
- proximity to full slip;
- beam boundaries and supports;
- pressure redistribution / local normal stress;
- assumptions that neglect interlaminar normal-stress effects.

The paper itself reports finite-layer FEA differences, end/boundary discrepancies, and a tendency to overestimate parts of the slipping region when omitted normal stress becomes important.

This is highly compatible with a P1-style map

```math
e
=
e
\left(
n,p,\kappa,\text{load},\text{boundary condition},\ldots
\right)
```

### M2 — likely breakdown dimensions

Plausible breakdown axes supported by the verified assumptions/limitations include:

- violation of periodic/RVE scale separation;
- small versus finite layer count;
- large curvature / large local deformation;
- boundary and end regions;
- nonuniform normal pressure;
- membrane/sheath coupling;
- pressure redistribution;
- separation/lift-off;
- departure from ideal constant-$\mu$ Coulomb friction;
- structural loading paths not represented by the ideal RVE assumptions.

M2 therefore also has a rich validity problem, but the validity boundary would initially concern the **constitutive homogenization** and only later the full beam.

---

# 3. Direct comparison for P1

| Criterion | M1 — continuum beam | M2 — RVE constitutive continuum |
|---|---|---|
| Modeling level | Structural beam | Material/RVE constitutive |
| Directly predicts beam deflection | **Yes** | Not without structural embedding |
| Direct vacuum-pressure parameter | Yes | Yes |
| Explicit Coulomb slip | Yes | Yes |
| Explicit homogenization derivation | No RVE homogenization; continuum beam idealization | **Yes, average-field RVE homogenization** |
| Finite layer-count sensitivity | Directly relevant | Largely removed by periodic continuum idealization |
| Existing discrete/contact reference | **Yes, structural FEA/discrete literature** | Yes, primarily RVE-level FEA |
| Existing physical experiment | **Yes** | **No physical validation in the source** |
| Natural breakdown variables for beam P1 | **Very direct** | Indirect until embedded in a beam solver |
| Implementation complexity | Lower | Higher |
| Generality of constitutive loading | Lower; beam-focused | **Higher; multiaxial continuum loading** |
| Direct fit to current quasi-static planar-bending P1 | Strong | Possible, but requires an additional structural-model layer |

---

# 4. What each model would make the thesis actually study

## If M1 is selected

The thesis question becomes structurally direct:

> For the selected continuum layer-jamming beam model, over what combinations of finite layer count, vacuum pressure, friction/slip state, load/curvature, and boundary condition do its beam-scale predictions remain within predeclared error tolerances relative to an interface-resolving finite-layer reference and experiment?

Typical outputs could be:

- deflection $w$;
- bending stiffness $K$;
- transition/slip load;
- slip-zone extent $y_s$;
- possibly dissipated energy if the chosen implementation supports cyclic loading.

The central reduction being tested is:

```math
\text{finite discrete layered beam}
\rightarrow
\text{continuous beam/slip-zone representation}
```

## If M2 is selected

The thesis question shifts one modeling level downward:

> Over what loading, pressure, finite-layer, deformation, and boundary conditions does the average-field RVE constitutive law remain an acceptable representation of explicit frictional-contact layer mechanics, and does that constitutive validity carry to beam-scale bending?

Typical outputs could be:

- macroscopic stress components;
- tangent shear stiffness;
- yield/slip threshold;
- residual/plastic shear strain;
- dissipation-energy density;
- later, beam deflection after structural embedding.

The central reduction being tested is:

```math
\text{explicit interface RVE}
\rightarrow
\text{homogenized elastoplastic constitutive law}
```

This is a more fundamental homogenization study, but it creates an additional implementation and structural-validation layer before reaching the current beam-focused P1.

---

# 5. Decision-relevant interpretation — no final lock yet

Based only on the verified repository evidence:

- **M1 is structurally closer to the current P1.** It already operates at beam scale, already exposes slip-zone and load–deflection quantities, already has finite-layer FEA and physical beam comparison, and naturally permits a reduced-vs-full-layer validity map.
- **M2 is constitutively deeper and more general.** It has the stronger formal homogenization foundation and handles multiaxial stress states, but it is a material-point/RVE model rather than a complete beam solver and currently lacks physical structural validation in the source.

This is **not yet a final model selection**. Before locking $M$, the next decision should explicitly choose which scientific object the thesis wants to validate:

1. **beam-scale reduction validity** → favors the M1 research architecture;
2. **RVE-to-continuum homogenization validity** → favors the M2 research architecture.

The current P1 wording is beam-focused, so changing from M1 to M2 would require deciding whether P1 should be reformulated around constitutive homogenization rather than merely treating M2 as an interchangeable beam model.

---

# 6. Exact items still to lock after this comparison

The model-selection step is complete only when the following four entries are frozen:

\`\`\`text
REDUCED MODEL M = ...
REFERENCE MODEL R = ...
PRIMARY OUTPUTS = ...
PRIMARY BREAKDOWN VARIABLES = ...
\`\`\`

For either candidate, the following must then be defined **before validation errors are inspected**:

- output-specific error metrics;
- output-specific acceptance tolerances;
- parameter-space bounds;
- calibration/validation split;
- accepted-side and rejected-side experimental test points.

---

# 7. Evidence provenance

This comparison uses the following locally verified records:

- \`data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json\`
- \`data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json\`
- \`docs/LAYER_JAMMING_MODEL_COMPARISON.md\`
- \`outputs/verification/D1-V002/adversarial_evidence_synthesis.md\`
- \`outputs/verification/D1-V003/ZHANG_2025_DEEPER_UNDERSTANDING_AUDIT.md\`
- \`outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json\`

**Evidence rule:** claims above that concern paper mechanics, assumptions, validation, or limitations are grounded in the verified full-text evidence already extracted in the repository. Statements about implementation architecture or suitability for P1 are explicit synthesis/inference from those verified records, not claims attributed to the original authors.
