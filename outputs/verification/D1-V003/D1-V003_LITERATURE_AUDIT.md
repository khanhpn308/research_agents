# D1-V003 Literature Audit

## 1. Executive Verdict
**VERDICT: SURVIVED (WITH PRECISION REFINEMENT)**

The narrowed hypothesis has survived the adversarial literature audit. While continuum and homogenized models for layer jamming definitely exist (Zhang 2025, 2026), no work has been found that systematically maps the *validity domain* or establishes the *breakdown boundaries* of these models against discrete mechanics and physical experiments. 

## 2. Hypothesis Under Audit
**P1 Narrowed Gap:**
"Existing continuum representations for layer-jamming structures exist, but their quantitative validity and breakdown boundaries relative to discrete mechanics and experiment may not yet have been systematically established."

## 3. Audit Constraints & Execution Scope
The audit was constrained to search for the strongest falsifying evidence that could defeat the narrowed gap. 
- **Methodology:** API-based citation traversal (Semantic Scholar) and web-based literature searches for adjacent mechanics.
- **Scope:** 2025-2026 direct layer-jamming literature (Zhang et al., Fan et al.), forward citations of D1-V002 papers, and adjacent solid mechanics fields (multi-leaf springs, partial-interaction composite beams).
- **Evaluation:** Evaluated against 9 Threat Tests designed to identify any work that quantifies homogenization error or maps validity domains.

## 4. Track A Results (Forward Citations)
- **Sources Checked:** Forward citations for Zhang et al. 2025 (Mech. Sci.), Zhang et al. 2025 (FME), and Zhang et al. 2026 (TAML).
- **Findings:** The citations primarily consist of review papers (e.g., "A Review of Variable Stiffness in Continuum Robots") or self-citations ("Continuum modeling for layer jamming structures"). 
- **Verdict:** `[METADATA ONLY]` / `[INFERENCE]`. None of the forward citations conduct a rigorous error analysis comparing continuum assumptions to discrete layer-by-layer slip behavior. The mathematical limits of homogenization in this context remain unaddressed.

## 5. Track B Results (Direct Layer-Jamming Models)
- **Sources Checked:** Fan et al. 2026 (TCST) and cited 2023-2025 control-focused papers.
- **Findings:** Fan et al. proposes a port-Hamiltonian formulation for simultaneous position-and-stiffness control of layer-jammed continuum robots. 
- **Verdict:** `[METADATA ONLY]`. This literature focuses on real-time, passivity-based control rather than solid mechanics. It does not map the breakdown boundary where continuum assumptions fail (e.g., at low layer counts or extreme curvatures). 

## 6. Track C Results (Adjacent Mechanics)
- **Sources Checked:** Literature on multi-leaf spring homogenization and partial-interaction composite beams.
- **Findings:** In vehicle dynamics (multi-leaf springs), it is widely recognized that homogenization is generally *invalid* for capturing the hysteretic, history-dependent nature of interleaf slip and stiction. Explicit contact mechanics (discrete modeling) is preferred. In composite beams, the validity of simplified analytical models is strictly bound by threshold values of "slip stiffness".
- **Verdict:** `[INFERENCE]`. The adjacent mechanics literature actually strengthens the proposed gap. It confirms that whenever discrete interface friction dominates, continuum approximations have severe limits. Yet, the robotics layer-jamming literature has not yet imported this critical rigor to define those limits.

## 7. Strongest Falsifying Evidence
No falsifying evidence was found that defeats the narrowed gap. The strongest "threats" were papers proposing new continuum models (Zhang 2025, 2026), but they only establish the *existence* of such models, not their *limits*. They fail Threat Tests T4 through T9.

## 8. Strongest Surviving Gap
**The Breakdown Boundary of Homogenized Layer Jamming:**
While continuum models can approximate layer-jammed beams, there exists no quantitative framework defining *when* and *why* these models fail. Specifically, the field lacks a non-dimensional mapping (e.g., relating layer count $N$, curvature $\kappa$, and pressure $P$) that delineates the boundary between regimes where a homogenized slip model is accurate and regimes where discrete, layer-by-layer stick-slip mechanics must be explicitly resolved.

## 9. Scope Revision for P1
**Revised P1:**
"Defining the Breakdown Boundary of Homogenized Mechanics in Vacuum Layer-Jammed Beams: A Quantitative Mapping Between Continuum Approximations and Discrete Frictional Regimes."

## 10. Recommended Next Experiment
To exploit this gap, the immediate next step must be a comparative mechanical study (numerical or physical) designed to force the continuum model to fail.
- **Proposed Test:** A three-point bending or cantilever deflection experiment/FEA across a parametrically varied number of layers (e.g., $N = 3, 5, 10, 20, 50$) under constant total thickness and varying vacuum pressures.
- **Objective:** Measure the divergence in force-deflection hysteresis between a discrete multi-body frictional contact model (or physical prototype) and the theoretical predictions of a continuum homogenized model. Identify the critical layer count and curvature at which the continuum assumption diverges by more than an acceptable error threshold (e.g., 10%).
