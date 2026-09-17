# D1-V003 LITERATURE AUDIT PLAN

**Audit Round:** `D1-V003`  
**Baseline Evidence:** `outputs/verification/D1-V002/adversarial_evidence_synthesis.md`  
**Target Candidate Gap:**  
> *"Existing continuum representations for layer-jamming structures exist, but their quantitative validity and breakdown boundaries relative to discrete mechanics and experiment may not yet have been systematically established."*  

**Core Operating Principle:**  
**DO NOT DEFEND THIS GAP. ATTEMPT TO FALSIFY IT USING THE CLOSEST PRIOR WORK ACROSS SOFT ROBOTICS AND ADJACENT SOLID MECHANICS.**

---

## 1. Executive Context & Audit Objectives

Verification round `D1-V002` definitively established that:
1. **Continuum models for layer jamming already exist** in multiple publications:
   - Continuous-medium beam model (CLJM): Zhang et al. (2025, *Mechanical Sciences*, DOI: `10.5194/ms-16-821-2025`)
   - Closed-form curved-beam model with continuous sliding boundary: Zhang et al. (2025, *Frontiers of Mech. Eng.*, DOI: `10.1007/s11465-025-0843-5`)
   - 3D elastoplastic continuum constitutive model via RVE volume-averaging: Zhang et al. (2026, *Theoretical & Applied Mech. Letters*, DOI: `10.1016/j.taml.2025.100633`)
2. Therefore, proposing "a new continuum/homogenized model for layer jamming" is **unconditionally pre-empted and non-novel**.
3. A candidate gap provisionally survived *only* under a narrowed, adversarial framing: whether the quantitative validity domain and failure/breakdown boundaries of these continuum representations (relative to discrete interface mechanics and experiment) remain unmapped.

**Objective of Round D1-V003:**  
Execute a targeted three-track literature search to determine whether:
- Prior forward-citing authors have already mapped the validity limits of the Zhang continuum models;
- Direct 2025–2026 layer-jamming literature (especially Fan et al. 2026) has already solved this boundary problem;
- Adjacent, mature mechanics disciplines (partial-interaction composite beams, multi-leaf springs, asymptotic homogenization, frictional contact mechanics) have already established generalized breakdown criteria that make the layer-jamming problem a trivial or solved instance of existing theory.

---

## 2. Audit Structure Overview

```
+--------------------------------------------------------------------------------------------------+
|                                    D1-V003 THREE-TRACK AUDIT                                      |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   TRACK A: Forward Citations of Zhang Continuum Papers (2025–2026)                               |
|   --> Focus: Have citing authors already evaluated errors, limits, or validity boundaries?       |
|                                                                                                  |
|   TRACK B: Direct 2025–2026 Layer-Jamming Mechanics & Soft Robotics                              |
|   --> Focus: Screen Fan et al. (2026) and concurrent works for mechanics vs. control focus       |
|                                                                                                  |
|   TRACK C: Adjacent Mechanics Literature (Civil, Mechanical, Structural)                         |
|   --> Focus: Have composite beams, multi-leaf springs, or shear-lag models already formulated    |
|       the discrete-to-continuum transition and breakdown criteria for frictional layered stacks?|
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+
```

---

## 3. TRACK A: Forward Citations of the Zhang Continuum Papers

### Target Seeds
1. **Seed A1:** Zhang et al. (2025), *A continuum-based model for a layer jamming beam*, *Mechanical Sciences*, 16, 821–830. DOI: `10.5194/ms-16-821-2025`
2. **Seed A2:** Zhang et al. (2025), *Toward a deeper understanding of layer jamming structures*, *Frontiers of Mechanical Engineering*, DOI: `10.1007/s11465-025-0843-5`
3. **Seed A3:** Zhang et al. (2026), *Continuum modeling for layer jamming structures*, *Theoretical and Applied Mechanics Letters*, 16, 100633. DOI: `10.1016/j.taml.2025.100633`

### Specific Research Questions for Track A
- Have any citing papers compared Zhang's continuum predictions directly against Caruso's (2023) discrete progressive slip equations across varying layer counts ($n$)?
- Have citing authors quantified model prediction error as a function of layer count ($n$), aspect ratio ($L/h$), or vacuum pressure ($p$)?
- Has any paper derived a non-dimensional breakdown criterion predicting when the continuous sliding boundary assumption ($y_s(Q)$) diverges from discrete slip steps?
- Have citing authors performed structural-level experimental tests specifically assessing the RVE constitutive model from Seed A3?

### Search Queries & Execution Protocols

#### Query A.1: Broad Forward Harvesting
- **Target Databases:** Scopus, Web of Science, Google Scholar
- **Harvest Method:**  
  1. Retrieve all publications citing DOIs `10.5194/ms-16-821-2025`, `10.1007/s11465-025-0843-5`, or `10.1016/j.taml.2025.100633`.
  2. For Google Scholar, query exact titles in quotes to capture preprint and early-access citations:
     - `"A continuum-based model for a layer jamming beam"`
     - `"Toward a deeper understanding of layer jamming structures"`
     - `"Continuum modeling for layer jamming structures"`
- **Inclusion Criteria:**  
  - Any paper citing at least one seed.
  - Formulates, implements, modifies, or benchmarks a continuum or homogenized model for layer jamming.
  - Investigates layer count scaling, boundary constraints, or prediction error.
- **Exclusion Criteria:**  
  - Generic review or application papers citing the seeds merely as variable-stiffness examples without mechanical analysis.
  - Unrelated soft actuator designs citing the seeds only for fabrication background.
- **What Threatens the Gap:**  
  Any citing paper that publishes an experimental or numerical comparison between continuum and discrete models showing the exact parameter boundaries where continuum models fail.
- **What Supports Continued Investigation:**  
  Citing papers that adopt the continuum model blindly for robotics control or design, explicitly confirming that its physical limits of validity remain uncharacterized.

#### Query A.2: Targeted Keyword Intersections within Citing Corpus
- **Exact Search String (Scholar / Crossref):**  
  `("10.5194/ms-16-821-2025" OR "10.1007/s11465-025-0843-5" OR "10.1016/j.taml.2025.100633") AND ("validity" OR "limitation" OR "discrete" OR "breakdown" OR "layer count" OR "error")`
- **Target Database:** Google Scholar / Publish or Perish
- **Threat Threshold:** Presence of a parametric error map across $n \in [2, 50]$ and $p \in [10, 100]\text{ kPa}$.

---

## 4. TRACK B: Direct 2025–2026 Layer-Jamming Literature

### High-Priority Seed: Fan et al. (2026)
- **Title:** *Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots*
- **Authors:** Yeman Fan, Bowen Yi, Dikai Liu
- **Journal:** *IEEE Transactions on Control Systems Technology* (2026)
- **DOI:** `10.1109/TCST.2026.3690756`

### Specific Screening Mandate for Fan et al. (2026)
Determine with full-text evidence whether the paper:
1. Formulates a continuum beam mechanics model or uses an empirical/lumped model;
2. Accounts for progressive interlayer slip or assumes idealized piecewise rigid/jammed states;
3. Quantifies mechanics breakdown limits or restricts its scope to controller design, closed-loop tracking, and task-space stiffness regulation.

### Additional 2025–2026 Targeted Queries

#### Query B.1: Continuum & Reduced-Order Layer Jamming (2025–2026)
- **Exact Search String:**  
  `("layer jamming" OR "laminar jamming") AND ("continuum model" OR "homogenized" OR "homogenization" OR "equivalent beam" OR "reduced-order" OR "constitutive model")`
- **Target Databases:** Scopus (2025–2026), Web of Science (2025–2026), IEEE Xplore (2025–2026)
- **Inclusion Criteria:**  
  - Peer-reviewed articles or conference papers published in 2025 or 2026.
  - Proposes, evaluates, or reviews mechanics formulations for layer/sheet jamming beams, plates, or shells.
- **Exclusion Criteria:**  
  - Granular/particle jamming.
  - Pure control or application papers without structural mechanics modeling.
- **Threat to Gap:**  
  A paper presenting a higher-order continuum beam theory (e.g., Cosserat, micropolar, or strain-gradient) that explicitly resolves interfacial slip localization and maps error bounds.
- **Support for Gap:**  
  Papers relying on simplified discrete formulations (e.g., Caruso 2023) or complaining of FEA computational costs, showing lack of awareness or lack of trust in continuum models due to unmapped accuracy limits.

#### Query B.2: Breakdown, Limitations, and Interface Constraints
- **Exact Search String:**  
  `("layer jamming" OR "laminar jamming") AND ("validity limit" OR "breakdown" OR "model limitation" OR "boundary effect" OR "end effect" OR "contact pressure" OR "slip localization")`
- **Target Databases:** Scopus, Google Scholar
- **Threat to Gap:**  
  Explicit analytical or experimental derivation of boundary constraint correction factors or edge-peeling criteria in layer-jamming beams.

---

## 5. TRACK C: Adjacent Mechanics Literature (Non-Soft Robotics)

The physical phenomenon in layer jamming—a stack of elastic sheets held together by normal traction and resisting bending through friction until interlayer shear exceeds Coulomb friction—is closely related to classical structural mechanics problems. We must prove whether our proposed gap is merely soft-robotics ignorance of solved classical mechanics.

### C.1. Partial-Interaction Composite Beams
- **Background:** Initiated by Newmark (1951), extended by Schnabl (2007) and Nguyen (2012). Models two- or multi-layer beams with compliant or frictional shear connectors.
- **Exact Query C.1 (Scopus / Compendex):**  
  `TITLE-ABS-KEY(("partial interaction" OR "incomplete interaction") AND ("multilayer beam" OR "laminated beam" OR "layered beam") AND ("interlayer slip" OR "frictional slip" OR "Coulomb friction"))`
- **Targeted Mechanics Question:**  
  Have partial-interaction models solved the asymptotic transition from $n$ discrete layers to a continuous shear-lag medium, and did they define an exact validity boundary for the continuum approximation?
- **What Threatens the Gap:**  
  A classical civil/structural mechanics paper demonstrating that for $n > n_{\text{crit}}$, discrete partial-interaction equations converge to a homogenized slip beam within $\epsilon\%$ error, where $n_{\text{crit}}$ is explicitly derived from beam aspect ratio and shear stiffness.

### C.2. Multi-Leaf Automotive & Locomotive Springs
- **Background:** Multi-leaf springs are stacks of curved steel sheets pressed together and subjected to bending, undergoing interlayer frictional slip, stiffness degradation, and hysteresis.
- **Exact Query C.2 (Scopus / SAE Mobilus):**  
  `TITLE-ABS-KEY(("leaf spring" OR "multi-leaf spring") AND ("interlayer slip" OR "interleaf friction" OR "Coulomb friction") AND ("continuum model" OR "homogenization" OR "equivalent beam" OR "validity"))`
- **Targeted Mechanics Question:**  
  Do leaf spring engineers use homogenized beam formulations, and have they established the exact limits where continuous models fail to capture discrete leaf-end slip?
- **What Threatens the Gap:**  
  Standardized SAE or mechanical engineering literature proving that leaf-end friction and discrete slip cannot be homogenized, or conversely, that a known homogenization criterion has been standard since the 1970s–1990s.

### C.3. Asymptotic Homogenization & Micropolar Limits of Frictional Laminates
- **Background:** Continuum modeling of layered rocks, geology, and layered composites with frictional contact (e.g., Mindlin, Biot, Christensen, de Borst).
- **Exact Query C.3 (Web of Science / Scopus):**  
  `TS=(("layered media" OR "laminated structure" OR "frictional interfaces") AND ("asymptotic homogenization" OR "continuum limit" OR "micropolar" OR "Cosserat") AND ("slip" OR "Coulomb friction") AND ("validity" OR "breakdown" OR "internal length scale"))`
- **Targeted Mechanics Question:**  
  Does asymptotic homogenization of frictional layers require a Cosserat/micropolar continuum (incorporating layer thickness $\delta$ as an intrinsic material length scale), and is the breakdown of classical Cauchy continuum models already rigorously bounded by the ratio $\delta/L$ or bending strain gradient?
- **What Threatens the Gap:**  
  If the breakdown of classical continuum representations for frictional stacks is already mathematically established as a classical length-scale breakdown governed by $\delta/h$ or $\delta/L$, leaving no open scientific question for layer jamming.

---

## 6. Detailed Query Matrix

| Track | Query ID | Exact Search String | Target Database | Expected Yield | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A** | `Q-A1` | Forward citations of DOI `10.5194/ms-16-821-2025` | Scopus / Scholar | High relevance | Critical |
| **A** | `Q-A2` | Forward citations of DOI `10.1007/s11465-025-0843-5` | Scopus / Scholar | High relevance | Critical |
| **A** | `Q-A3` | Forward citations of DOI `10.1016/j.taml.2025.100633` | Scopus / Scholar | High relevance | Critical |
| **B** | `Q-B1` | `DOI 10.1109/TCST.2026.3690756` (Fan et al. 2026 full-text audit) | IEEE Xplore / Repo | 1 paper | Critical |
| **B** | `Q-B2` | `("layer jamming" OR "laminar jamming") AND ("continuum model" OR "homogenized" OR "equivalent beam" OR "reduced-order")` [Year: 2025-2026] | Scopus / WoS | ~15–30 papers | High |
| **B** | `Q-B3` | `("layer jamming" OR "laminar jamming") AND ("validity" OR "breakdown" OR "end effect" OR "boundary layer")` [Year: 2024-2026] | Scopus / Scholar | ~10–20 papers | High |
| **C** | `Q-C1` | `TITLE-ABS-KEY(("partial interaction" OR "incomplete interaction") AND ("multilayer beam" OR "laminated beam") AND ("slip" OR "friction") AND ("continuum" OR "homogenization"))` | Scopus | ~20–40 papers | Critical |
| **C** | `Q-C2` | `TITLE-ABS-KEY(("leaf spring" OR "multi-leaf") AND ("interlayer slip" OR "interleaf friction") AND ("homogenization" OR "continuum" OR "equivalent"))` | Scopus / Compendex | ~15–30 papers | High |
| **C** | `Q-C3` | `TS=(("layered media" OR "laminated structure") AND ("asymptotic homogenization" OR "micropolar" OR "Cosserat") AND ("frictional slip" OR "interface slip") AND ("validity" OR "breakdown"))` | Web of Science | ~20–50 papers | High |

---

## 7. Explicit Stop Conditions for Verification Round D1-V003

To maintain complete objectivity and prevent confirmation bias, D1-V003 must terminate with an explicit verdict based on the following pre-defined falsification criteria:

### Stop Condition 1: REJECT (Full Falsification of Direction P1)
Terminate and **REJECT** the direction if any of the following is discovered:
1. **Prior Exact Solution:** A 2025–2026 paper (in soft robotics or solid mechanics) has already derived, plotted, and experimentally validated a non-dimensional phase diagram or error map delineating the validity boundaries of continuum vs. discrete models for frictionally jammed layer stacks.
2. **Classical Theory Equivalence:** Classical partial-interaction composite beam or multi-leaf spring mechanics has already established a generalized dimensionless criterion (e.g., based on shear parameter $\alpha L$ and layer count $n$) that directly dictates model breakdown, such that applying it to layer jamming is purely incremental application with no new mechanics insight.
3. **Insignificant Breakdown Phenomenon:** Literature or high-fidelity contact FEA benchmarks prove that continuum models match discrete behavior within $< 5\%$ across all physically realizable layer counts ($n \ge 4$), demonstrating that no meaningful breakdown regime exists under engineering conditions.

### Stop Condition 2: PIVOT (Candidate Gap Unfeasible or Methodological Only)
Terminate and **PIVOT** away from P1 if:
1. Model discrepancies are driven entirely by unpredictable manufacturing artifacts (e.g., random envelope wrinkles, friction variability, localized air pockets) rather than deterministic mechanics, precluding systematic scientific modeling at an MSc level.
2. The breakdown is strictly localized to numerical singularities at boundary supports that require empirical calibration factors rather than exposing a fundamental continuum mechanics limitation.

### Stop Condition 3: NARROW (Survives for Focused Adjudication)
Proceed to final adjudication under a **strictly narrowed** scope if and only if:
1. Tracks A and B confirm that existing layer-jamming authors (Zhang et al., Fan et al.) rely on continuum models whose physical breakdown limits at intermediate layer counts ($n \in [4, 16]$) and boundary-clamped constraints remain uncharacterized.
2. Track C confirms that classical composite and leaf-spring theories address constant-normal-force or linear-spring interfaces, but do **not** cover the state-dependent, vacuum-coupled normal force distribution and large-rotation kinematics characteristic of vacuum soft robotics.
3. A testable, non-obvious mechanics hypothesis can be stated: e.g., *"Continuum models break down when the characteristic shear-slip boundary layer width $L_{\text{slip}}$ approaches the discrete layer thickness $\delta$, causing discrete localized slip steps to dominate global bending compliance."*

---

## 8. Protocol for Citation Ingestion and Evidence Traceability

To ensure compliance with the repository's file-first and clean-state operating rules:
1. All raw search exports from queries `Q-A1` through `Q-C3` will be saved exclusively in isolated directory:
   `data/search_exports/D1-V003/raw/`
2. Normalized candidate metadata will be generated via audited parsers into:
   `outputs/search_results/D1-V003/`
3. Screened full-text PDFs selected for detailed evaluation will be registered into `data/paper_registry.json` strictly with:
   `--type verification --verification-id D1-V003`
4. Ingested evidence JSON files will be generated into `data/evidence/` and validated via `python -m app.ingestion.validate_evidence`.
5. Historical outputs in `outputs/discovery_snapshot/`, `outputs/verification/D1-V001/`, and `outputs/verification/D1-V002/` will remain strictly read-only and unaltered.
