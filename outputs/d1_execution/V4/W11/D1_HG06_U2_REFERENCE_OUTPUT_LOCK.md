# D1-HG06-U2 — Reference and output definition lock

**Date:** 2026-09-26 (Asia/Bangkok)  
**Role requested:** GPT-6 Sol High scientific mechanics design; runtime model identity is not independently attested here.  
**Scope:** D1 S11/HG-06 re-entry protocol only. No FE run, experiment, final validation/error-map inspection, threshold value, K1–K9 verdict, W12, novelty adjudication, broad search, or D1–MP1 comparison.  
**Gate state after U2:** HG-06 **BLOCKED**; HG-09 **BLOCKED**; W12 authorization **false**. Canonical threshold, clearance, K-criterion, W10 threat and historical verification files were not edited.

## 1. Authority and status language

This report consumes U1 as the authoritative immediately prior analysis [U1a–b]. U1 identifies the Zhang et al. paper/formulation but no implementation, an unspecified full-layer R, a precise proposed `w`, a chord-stiffness class without endpoints, and non-equivalent onset events. The current snapshot, state JSON, Plan V6, frozen S9 criteria and W11 gate records remain the canonical workflow authority [R1–R6]. The source paper PDF, its hash-matched page bundle and paper card are the evidence for statements about Zhang et al. [S1–S2].

Labels: **FACT FROM SOURCE** means the cited paper actually states or displays it; **CANONICAL STATE** means a repository gate/control fact; **PROPOSED LOCK** is a design choice made in this re-entry analysis and is not a completed implementation or human sign-off; **UNRESOLVED** is an input or test still needed. The words `LOCKED` below apply to a *definition or design contract*, not to validated numerical performance.

| Object | U2 result | Boundary of the result |
|---|---|---|
| M implementation contract | **LOCKABLE_NOW** | The contract can be versioned now; no code, reproduced case or executable hash exists yet. |
| R architecture | **PARTIALLY_LOCKED** | Primary physics and dimensionality chosen; contact enforcement/regularization, pressure/fixture realization and convergence need pilot or human specimen decisions. |
| `w` definition | **LOCKED** | Mathematical observable and extraction rules fixed for the selected cantilever family; experimental visibility/fixture feasibility still needs a pilot. |
| `K` definition | **PARTIALLY_LOCKED** | Service-window chord rule chosen; numerical service loads/endpoints await a use-case decision. |
| `Q_slip` correspondence | **PARTIALLY_LOCKED** | External onset-load carrier and three-level event hierarchy chosen; direct event domain/detection equivalence awaits a pilot. |
| Engineering use case | **PARTIALLY_LOCKED** | Decision types fixed; service window, deflection/stiffness limits and slip margin require the human project owner. |

## 2. Objective A — M implementation contract

### 2.1 Published object and scope

**FACT FROM SOURCE:** M is Zhang, Yao, Zhao and Wei (2025), *A continuum-based model for a layer jamming beam*, DOI `10.5194/ms-16-821-2025`, paper ID `95646b2cfc` [S1, PDF p. 1]. Implement the published continuum-based layer-jamming beam model (CLJM) as one versioned branch. Include curved-beam equilibrium for `N(s),Q(s),M_b(s)` (paper Eqs. 1–2), the fully jammed parabolic shear field (Eq. 3), partial/full slip section laws and `y_s` rules (Eqs. 4–9), jammed/sliding normal-stress and force/moment construction (Eqs. 10–18), `I_J` and incremental deformation (Eqs. 19–20), and the printed Algorithm [S1, PDF pp. 3–6]. The published model is distinct from the paper's layer-resolved Abaqus comparison and from the other Zhang RVE constitutive model [U1a; S1].

The implementation state record at each accepted external load step must contain `P_k,p_k,θ_k(s),r_k(s),N_k(s),Q_k(s),M_{b,k}(s),y_{s,k}(s),regime_k(s),I_{J,k}(s)` and any history required for unloading. For the primary monotonic study, retain the history state and do not silently replace the incremental model with a memoryless closed form. Inputs are `L,b,h,n,δ,E,μ`, initial centerline/angle, pressure history, support and load path, and integration/increment controls. The primary layer-count convention is `h=nδ` with `h,b,L` held fixed while varying `n` (Section 3); that convention is a **PROPOSED LOCK**, not a paper result.

### 2.2 Branch and update contract

**FACT FROM SOURCE:** A section is fully jammed below `Q_slip=(2/3)μpbh`; it is half slipping while its continuous `y_s` advances; the limiting full-slipping state retains outer jammed strips associated with `δ`, and the paper defines `Q_max` [S1, PDF p. 4, Eqs. 3–9]. The published incremental algorithm updates the load, `N,Q,M_b`, `y_s`, angle and configuration, with a displacement-change control parameter [S1, PDF p. 6, Algorithm].

**PROPOSED LOCK — executable sequence:** (1) equilibrate the pressure-only state at the declared `p`, no transverse load; (2) advance the *externally applied, global transverse dead-force resultant* `P` monotonically along the laboratory load axis; (3) from the current centerline and boundary conditions solve the paper's internal equilibrium; (4) classify each section using the published `Q_slip`, `Q_max` and `y_s` branch, preserving exact equality conventions in a source-implementation note; (5) compute `I_J`, the paper's deformation increment and updated angle; (6) reconstruct the centerline by integrating its tangent from the root, then re-solve internal equilibrium until the step's configuration and force balance converge; (7) accept the state and record branch transitions, or reduce the step and retry; (8) extract `w`, service-window `K`, and analytical onset from the same accepted path. When the published Algorithm leaves a numerical operation underspecified, record the chosen operation as a project numerical method rather than attributing it to the authors.

**PROPOSED LOCK — numerical convention:** parameterize the undeformed centerline by material arc coordinate `s∈[0,L]`, integrate its tangent `(cosθ,sinθ)` from the clamped material root, and integrate force/angle equations with a documented order-consistent quadrature. Use refinement in spatial stations, quadrature order, load step and nonlinear iteration to establish converged outputs; do not set convergence values by observed M–R errors. Prefer an adaptive force step that refines at regime changes, with a recorded maximum attempted and accepted step. The exact quadrature implementation, algorithm tolerance and step-control constants are **UNRESOLVED** until the implementation pilot; they are numerical verification settings, not model-fit parameters. The paper's own Algorithm should be transcribed line by line into a source-to-code mapping before implementation, including any notation ambiguity, without silently changing its mechanics [S1, PDF p. 6].

**PROPOSED LOCK — common boundary/input convention:** straight rectangular equal-layer cantilever, nominal root `s=0` fixed against translation and rotation after pressure equilibration, free material end `s=L`, first monotonic planar bending branch, nominal vacuum magnitude `p≥0` as a prescribed uniform pressure input in the source friction law, and one independently measured constant `μ` per declared surface/pressure condition. A pressure-dependent `μ`, re-fit to R, or re-fit to validation E is a *different model version*. The physical root clamp and end-load fixture must be represented consistently in R/E or their effects separately reported (Section 3). Pressure equilibrium precedes transverse loading. No unloading/cyclic output is a primary U2 metric.

**Reproduction gate before use:** (i) reproduce the source's full-jamming shear parabola and its analytical onset relation exactly; (ii) reproduce section branch continuity/limits at `Q_slip` and `Q_max`; (iii) reconstruct published FEA stress comparison configurations (10/25 layers, pressure/load/material values as reported) as source checks, not project calibration; (iv) reconstruct the published 20-layer, 60-kPa experimental load–deflection curve using the source's reported inputs, recording digitization and parameter-provenance uncertainty [S1, PDF pp. 4, 7–8, Figs. 6–7]. Published graphical agreement is not a numerical pass tolerance. Define a reproduction pass rule from equation consistency, source-digitization uncertainty and solver refinement **before** looking at project final error maps. If reproduction fails, correct or version the implementation and do not use it in the validity map.

**Version record:** source PDF SHA-256 `95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd`; record implementation commit/hash, dependency/solver versions, input deck hash, source-to-code equation map, ambiguity decisions, numerical settings, calibration provenance, published-case reproduction report and change log. A later physics change creates a new M version and re-opens comparability/freeze review.

**M_IMPLEMENTATION_LOCK = LOCKABLE_NOW** for this written contract. Actual executable M remains **UNRESOLVED** until the code version and reproduction gate exist. This distinction prevents a written specification from masquerading as verified implementation.

## 3. Objective B — R architecture and the twenty implementation choices

### 3.1 Primary comparator decision

**PROPOSED LOCK:** Use a **2D plane-stress structural FE model in the beam length–height plane**, with each physical layer represented by its own elastic continuum domain and each neighboring pair joined only by unilateral frictional contact. Apply a nominal uniform compressive pressure through the outer top/bottom surfaces in the idealized primary model. Let interface normal tractions vary with position and deformation through contact equilibrium. Use finite-rotation geometry and the same first monotonic transverse load path as M. This is the minimum interface-resolving counterpart to M's planar beam idealization and supports a controlled sweep of `n,p,P` without adding unquantified 3D membrane/edge physics to the *primary* comparator [U1a; S1, PDF pp. 2–4, 8].

2D plane stress is a **design inference**, not proof that the real vacuum-enclosed specimen is 2D. A targeted 3D/membrane/widthwise check is required before treating the 2D R as adequate for experiment E. If widthwise traction, membrane tension, edge opening or the fixture changes `w`, `K`, or onset beyond their independent numerical/measurement resolution, upgrade the primary R to 3D and version the comparison protocol before final validation. The 2D R remains a higher-fidelity *interface comparator*, never ground truth. A matched-physics auxiliary R with constrained/uniform interface pressure may help attribute discrepancies, but it cannot silently replace the primary R.

The source's Abaqus CPS4R example shows that 2D plane-stress layers are feasible, but does not freeze this project's contact method or certify its reference accuracy [S1, PDF p. 8]. No software brand is chosen here. A solver is eligible only if it can satisfy and export the physics, contact diagnostics, path and convergence contract below.

### 3.2 Decision register

The category says what the **remaining execution choice** requires. `CAN_FREEZE_FROM_CURRENT_EVIDENCE` means this report freezes the design rule, while the numerical result still needs verification. The other categories do not authorize guessing a value.

| # | Choice and U2 design rule | Category / missing test or decision |
|---|---|---|
| 1 | **2D primary**, targeted 3D challenge when width/envelope effects may matter. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE** for the idealized primary; 3D adequacy **REQUIRES_PILOT**. |
| 2 | **Plane-stress continuum** layers in length–height plane, thickness parameter `b`; no plane strain or shell in primary. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE** because M is planar/plane stress; element family verification remains. |
| 3 | One separate deformable domain for **every physical layer**; no tied interlayer nodes. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE**. |
| 4 | Equal layers `δ=h/n`; hold `L,b,h` fixed when varying `n` to isolate finite-layer approximation. Manufacturing/material equivalence needs checking. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE** for comparison geometry; E manufacturability **REQUIRES_PILOT**. |
| 5 | Unilateral normal hard-contact target: nonpenetration, compressive traction only, opening allowed, and no artificial cohesive/tensile traction. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE**. |
| 6 | Prefer symmetric surface-to-surface augmented-Lagrange normal enforcement, or an equivalent verified method; choose final algorithm on penetration/traction/output convergence, not solver convenience. | **REQUIRES_PILOT**; enforcement sensitivity and solver availability. |
| 7 | Rate-independent Coulomb tangential target `|t_t|≤μ t_n` in stick, sliding at limit; identical independently measured `μ` as M for matched physics. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE**. |
| 8 | Numerical tangential regularization, if solver needs it, must tend toward the rate-independent limit under a documented sensitivity study; do not make regularization a fit parameter. | **REQUIRES_PILOT**; scale and event bias. |
| 9 | Finite-rotation geometric nonlinearity throughout the intended bending-severity range; material layers initially linear elastic unless independent data justify another law. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE** for kinematics; material adequacy **REQUIRES_PILOT**. |
| 10 | Primary idealized pressure: gauge vacuum magnitude `p` represented as outer top/bottom compressive traction after pressure equilibration, with no imposed uniform interface traction. Physical sheath/side/edge transfer is a separate fidelity check. | **REQUIRES_PILOT** to establish equivalence to the selected E pressure realization; nominal convention can be frozen now. |
| 11 | Solve local `t_n(s)` from contact equilibrium at all interfaces; export distributions, not only section averages. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE**. |
| 12 | Permit lift-off wherever unilateral contact predicts it; do not numerically force layers closed. If a real sheath precludes opening, model that sheath in the 3D/physical check. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE** for primary idealized R; physical exclusion **REQUIRES_PILOT**. |
| 13 | Apply global transverse dead-force resultant `P` at free material ends without rigidly tying layer tips; preserve the same resultant and moment about the M centerline. Force-distribution device must be explicit in R/E. | **REQUIRES_PILOT**; experimentally feasible load transfer and end artifact. |
| 14 | Define root clamp footprint, translational/rotational restraints, axial release/rail policy and fixture compliance identically across M/R/E. | **REQUIRES_HUMAN_DECISION** for actual specimen/fixture; compliance measurement **REQUIRES_PILOT**. |
| 15 | Refine each layer through thickness and along length, with focused contact/end regions and element distortion checks; use more than one through-thickness element and demonstrate convergence. No mesh count is borrowed from the source. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE** for strategy; final density **REQUIRES_PILOT**. |
| 16 | Two-sided surface-to-surface interface discretization with no tied constraints; output relative slip, stick/slip state, `t_n`, `t_t` along every interface; test master/slave or symmetric bias. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE** for representation; discretization bias **REQUIRES_PILOT**. |
| 17 | Pressure equilibration first, adaptive quasi-static force increments second; refine steps before/near first slip and when contact status changes, preserving the same continuous loading branch. | **REQUIRES_PILOT** for usable increment and event bracket. |
| 18 | Require force/moment residual and contact penetration/constraint residual to decrease under solver tightening; reject steps with non-equilibrium or artificial energy dominating the response. Store diagnostics. | **REQUIRES_PILOT** for numeric convergence limits and solver-specific diagnostics. |
| 19 | Independently refine bulk mesh, interface/contact discretization, enforcement/regularization, load increments and solver tolerance for each output, especially onset; run selected 3D/fixture checks. | **REQUIRES_PILOT** for completed convergence evidence; protocol frozen now. |
| 20 | Report per-output residual reference uncertainty, including numerical envelope, input-parameter distribution, pressure/fixture idealization and unresolved 2D/3D effects. Do not call R exact truth. | **CAN_FREEZE_FROM_CURRENT_EVIDENCE** for reporting contract; numerical budgets **REQUIRES_PILOT**. |

Solver brand and operating system are **NOT_THESIS_CRITICAL** if an implementation passes this contract, exports the required fields and has a versioned input/output record. The actual specimen and fixture are thesis critical because they affect pressure transfer, bending and onset. The normal enforcement and slip regularization remain pilot-gated because contact onset is especially sensitive to them. Neither can be chosen merely to produce a clean curve.

**R_ARCHITECTURE_LOCK = PARTIALLY_LOCKED.** The unresolved primary blockers are: physical pressure-transfer and load-fixture equivalence; the human-selected clamp/rail/fixture configuration; contact enforcement/regularization sensitivity; output-specific mesh/contact/increment convergence; and residual uncertainty. A 3D/membrane check may trigger re-lock to a 3D primary R.

## 4. Objective C — `w` definition

**PROPOSED LOCK, now adopted at definition level:** the test family is a straight, equal-layer rectangular vacuum-jammed cantilever with a material root section `s=0` and free material end `s=L`, quasi-static planar bending by an external global transverse force resultant `P` applied along fixed laboratory unit vector `e_y`. Pressure is equilibrated before P ramps. Define

\[
w(P;p,n)= e_y\cdot\left[\bar r_{\rm tip}(P,p,n)-\bar r_{\rm tip}(0,p,n)\right],
\]

where `\bar r_tip` is the through-thickness **thickness-weighted mean of the initial free-end material section centerline points of all layers**. This initial-material-label convention survives relative axial slip: compare the *same layer-end labels*, not the current geometric cross-section at a shifted axial coordinate. In M, `\bar r_tip` is its centerline tip at material `s=L`. Positive `w` is along `e_y`, with the vacuum-only equilibrated state as zero. Units: metres. This is incremental rather than total lab-frame displacement. `P` is externally measured applied force in newtons, not internal `Q(s)`. Use first monotonic loading only, after a specified pressure dwell and preconditioning history.

Extraction: **M**—interpolate its accepted equilibrium states in `P`; **R**—thickness-weighted average of layer-end centerline material-point displacements after removing the pressure-only baseline; **future E**—track visible free-end layer-edge fiducials or a validated optical centroid tied to those material points, subtract fixture motion and pressure-only baseline. If the membrane or loading fixture hides/moves those fiducials so their mapping is unverified, E's `w` is `NOT_COMPARABLE` until the measurement pilot resolves it. For all branches use **linear interpolation in external P between adjacent converged first-branch states**, with no extrapolation and a refinement check near jumps. A discontinuous jump is reported with its bracketing force interval, not smoothed into an arbitrary value.

Primary M–R discrepancy is `Δw(P)=w_M(P)-w_R(P)` [m], and its magnitude in metres is the primary gate metric. Optional normalized reporting may use a positive `W_use` fixed by a future engineering decision, `|Δw|/W_use`; no `|w_R|` denominator is used at or near zero. Thus the near-zero rule is exact without an arbitrary switch point. The P-domain/evaluation grid and an allowable error remain pending; defining the response function does not define an acceptance tolerance. Loading fixture geometry, physical end markers and visibility remain pilot/human implementation dependencies, but do not change this observable.

**W_DEFINITION_LOCK = LOCKED** as a definition contract. A physical E route must still show that the prescribed signal can be observed without changing beam mechanics; otherwise the project must re-lock the definition before validation.

## 5. Objective D — `K` service-window chord decision

**Candidate-rule audit:** all rows assume the same `w(P)` from Section 4. Noise is amplified when the endpoint displacement difference approaches its uncertainty, regardless of selection rule [U1a].

| Rule | Physical meaning / M–R–E comparability | Circularity and onset sensitivity | Measurement, noise and engineering relevance |
|---|---|---|---|
| A. Fixed absolute `[P_a,P_b]` | Common force interval across all models/specimens, easy to reproduce. | No model-onset circularity; may span different slip regimes as `n,p` vary. | Measurable; meaningful only if the absolute range is tied to a real service load and `Δw` resolves above noise. |
| B. Fixed fraction of independently defined service load | Common scaled operating interval if the same independently specified service load is used for all branches. | Independent of final errors and onset; could cross slip in some conditions, which must be reported. | Good screening relevance, but arbitrary fractions would still need human physical rationale and sensor-resolution check. |
| C. Fraction of measured/predicted first-slip load | Targets comparable relative proximity to slip only if onset meanings match. | Circular while Q correspondence is unresolved; model-specific endpoints create different absolute loads and can hide onset error. | Detectability varies near onset; not suitable as primary K definition now. |
| D. Explicit pre-slip interval | Targets jammed stiffness alone. | Requires independent evidence that both endpoints precede local slip in all three branches; otherwise reclassifies points after seeing outcomes. | Useful secondary mechanism diagnostic, but cannot be primary use-case stiffness until onset protocol works. |
| E. Separate `K_pre` and `K_post` | Captures variable-stiffness contrast and transition. | Needs two separately fixed intervals and credible onset/region definitions; otherwise post-hoc window movement. | Potentially important later, with higher measurement burden and noise near the transition. |

**PROPOSED LOCK:** Primary `K_service` is the **chord stiffness over the independently specified service-load window** `[P_service,low,P_service,high]` in the selected pressure state:

\[
K_{\rm service}(p,n)=\frac{P_{\rm service,high}-P_{\rm service,low}}
{w(P_{\rm service,high};p,n)-w(P_{\rm service,low};p,n)}\quad[\mathrm{N/m}].
\]

This selects the engineering content of A/B without inventing load fractions: a human-designed operating window, fixed in newtons before M–R/E outcomes are inspected and common to M, R and E. `P_service,low` may be zero only if the intended service task genuinely includes zero load; no automatic zero-point secant. The interval is **not** moved to remain pre-slip for each pressure; if it straddles slip, report that it is a mixed-regime service chord. A separate `K_pre` or `K_post` requires a distinct protocol/version and cannot replace `K_service` retrospectively. Interpolate `w` endpoints by the Section 4 rule; if a jump contains an endpoint, report interval-censored/undefined chord rather than smoothing it away. If `|Δw|` is not resolved against propagated endpoint uncertainty, mark `K` `NOT_ESTIMABLE`. Primary discrepancy is `|K_M-K_R|` [N/m]; optional normalization uses an independently specified positive `K_use`, not a near-zero `K_R` denominator.

**K_DEFINITION_LOCK = PARTIALLY_LOCKED — DEFINITION LOCKED, NUMERICAL INTERVAL PENDING.** Human project owner must specify the service task and its common `[P_service,low,P_service,high]`; sensor/reference pilot must show the denominator is resolvable. Until then the physical K output and `epsilon_K` cannot be frozen numerically.

## 6. Objective E — onset correspondence and event hierarchy

### 6.1 Three epistemic levels and common carrier

| Level | Quantity and evidence | What it is not |
|---|---|---|
| **1 — analytical yield** | M's first eligible section at which its full-jamming law reaches `|Q(s)|=Q_slip^{section}=(2/3)μpbh`; record station `s_M` and associated external force `P_M` from the same equilibrium state [S1, PDF p. 4, Eq. 5]. | It is a model-predicted onset, not direct relative-layer motion. |
| **2 — numerical contact slip initiation** | R's first persistent, spatially resolved interface relative motion/contact transition under its converged unilateral/frictional law; record event patch, station/interface and external-load bracket `[P_R^-,P_R^+]`. | One slipping node, regularization micro-slip or solver chatter is not a physical event. |
| **3 — experimentally detectable physical slip** | E's first directly observed relative-layer motion within an accessible registered interface patch; record sensor-defined external-load bracket `[P_E^-,P_E^+]`. | A global force–deflection kink alone is `P_apparent`, not first local slip. |

**PROPOSED LOCK:** The common primary *carrier* is **external applied force at onset**, `P_onset` [N], not the paper's section capacity `Q_slip`, displacement at onset, or a global curve kink. This carrier can be recorded by every branch with the same force sensor/sign convention, while the level tag preserves what was actually detected. `Q_slip^{section}` remains a Level-1 diagnostic; `w_onset` is a secondary consequence because the three branches can predict different deflections at the same event. This does not assert that Levels 1–3 are physically equivalent.

### 6.2 Event protocol requiring pilot freeze

**Observation domain:** use only layer interfaces in an *interior material span* `D=[s_a,s_b]` that excludes the root clamp footprint, the free-end load-transfer footprint and independently mapped fixture-pressure boundary zones. The two stations `s_a,s_b` and a common physical spatial gauge length `ℓ_g` must be chosen from geometry/visibility and a targeted boundary-influence pilot, then frozen across M/R/E and the final map. A global first slip outside `D` must be reported separately, not silently counted as interior onset. If M's earliest yield occurs outside `D`, search its earliest eligible yield in `D` and label it `INTERIOR_ONSET`, not global first slip.

**Spatial persistence:** in R and E, require a connected patch of physical length at least `ℓ_g` on one interface with coherent signed relative motion; do not accept one contact node or one camera pixel. Choose `ℓ_g` above the shared spatial resolution and check that onset bracket is stable as mesh/pixel resolution changes. **Temporal/load persistence:** motion must exceed a predeclared displacement floor `d_g` and continue/cumulate in the same direction over a resolved loading increment after first detection, or be bracketed as unresolved when contact mode reverses. Fix the observation frequency, load-step cap and `d_g` using pre-validation zero-load/no-slip noise and R regularization/convergence pilots, not final onset differences. No number is supplied in current evidence.

**Numerical detector:** use relative tangential displacement increment and traction/stick status together; inspect normal contact pressure to exclude open interfaces; require convergence under mesh, contact enforcement, tangential regularization and force-step refinement. The regularization micro-slip floor must not be mistaken for physical slip. **Experimental detector:** calibrated direct layer fiducials/DIC, synchronized load and pressure records, a no-slip noise/false-event assessment, and evidence that the observed interface patch lies in `D`. If only the membrane/global curve is measurable, Level 3 first-slip onset is unavailable; label `P_apparent` separately.

**Interval censoring:** for R/E, report `[P^-,P^+]` from the last resolved no-event load and first resolved persistent-event load, enlarged where detector/synchronization uncertainty requires. If onset occurs before the first detectable load, use a left-censored interval. If no event is found by the tested load maximum, right-censor it. Do not substitute interval midpoints as measured truths. For a point prediction `P_M`, the discrepancy to an observed onset interval may be represented by `d(P_M,[P^-,P^+])=max(P^-−P_M,0,P_M−P^+)` [N], alongside the full bracket; a zero distance means only interval compatibility, not proof of equivalent mechanisms.

**P↔Q mapping:** compute `Q_M(s,P)` from M equilibrium at its Level-1 event station; if a Q-based secondary comparison is desired, integrate R section tractions/reactions at the *same initial material station and external P* and specify sign/projection. For an end-loaded curved beam, do not assume `Q=P`. Different event stations and different spatial domains prohibit a scalar internal-Q first-slip comparison. The primary carrier remains external `P_onset`.

**NON-COMPARABLE:** any branch lacks the registered `D`, direct E slip measurement, common pressure/load history, synchronized load, converged R event, sufficiently resolved onset bracket, or a Level-1/Level-2/Level-3 mapping that addresses different locations. Report the failing reason. A global kink, contact chatter, detected slip only at excluded boundaries, or an interface hidden by the membrane cannot be promoted to first local slip. An independent pilot must test whether M Level-1 onset predicts the same latent transition as R Level-2 and E Level-3 within their event-resolution intervals.

**Q_SLIP_CORRESPONDENCE = PARTIALLY_LOCKED.** `P_onset` and the hierarchy are fixed at protocol level, but the domain, patch/detector thresholds, contact formulation and direct E visibility are **UNRESOLVED**. `epsilon_Q` stays undefined, and the canonical `Q_slip` threshold row requires a reviewed metric revision before any freeze; do not silently relabel `Q` as `P`.

## 7. Objective F — minimum engineering use case

**PROPOSED LOCK:** M is intended for *preliminary screening of straight vacuum layer-jamming cantilever beam designs/pressure settings under a specified quasi-static transverse service-load window*. It predicts whether a candidate beam and pressure state meet a displacement limit, a service-window chord-stiffness requirement and an onset reserve before committing to full-contact R and physical E. This makes no claim of real-time control, universal robot design, or novelty. R/E remain needed to test M's limits.

| Output | Decision type fixed now | Missing human engineering criterion |
|---|---|---|
| `w` | At a declared service load, accept/reject a pressure/beam choice against an allowable tip displacement or clearance. | Actual task geometry, `P_service`, allowable `w_limit`, decision margin and load domain. |
| `K_service` | Choose a vacuum pressure/beam that supplies enough resistance over a declared service-load window. | `[P_service,low,P_service,high]`, required minimum/contrast of `K_service`, whether interval crossing slip is acceptable. |
| `P_onset` | Choose a pressure/operating load so first interior slip is avoided with a specified reserve, or deliberately reached if the task calls for compliant transition. | Whether slip avoidance or deliberate onset is intended, maximum operating load, required reserve, observable interior domain and direct detector feasibility. |

**ENGINEERING_USE_CASE = PARTIALLY_LOCKED.** The three decision *types* are coherent and sufficient to organize uncertainty studies. Numerical decision limits are not in the repository and must be supplied/approved by the human project owner before `epsilon_w`, `epsilon_K` or `epsilon_Q` is derived. If the uncertainty floor exceeds the independent decision margin, the associated validity classification is infeasible at the available resolution [U1a].

## 8. Objective G — T2 provenance and human review route

**CANONICAL STATE:** Historical W10 threat `D1-TH-015` and unresolved row `D1-UT-001` were written when Wang et al. 2026 (Qinyu Wang et al., *Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction*, DOI `10.1016/j.matdes.2026.116573`) had metadata/abstract evidence only [R7]. U1 preserves a later **user-reported human/ChatGPT full-text audit** claiming material `PARTIAL_OVERLAP` without direct equivalent M→R→E validity/breakdown workflow; U1 did not inspect its PDF or assign K verdicts [U1a–b].

**Local availability check, 2026-09-26 — VERIFIED FULL TEXT (source identity only):** the 17-page PDF is present at `data/inbox/2026-Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction.pdf`. Its SHA-256 is `f77bc7b7d605e57e4bb7e11e468223ce7f670dc4e06072fd1ed99bb27062c5ca`. The PDF's first page identifies the title, Qinyu Wang and coauthors, *Materials & Design* 268 (2026) 116573 and DOI `10.1016/j.matdes.2026.116573`. This confirms that a local full-text source exists; U2 has **not** completed a page-grounded scientific audit of its model, experiments or claims. Historical W10 remains metadata/abstract-only state-at-time [R7]. The TU Delft repository UUID in W10 is a source pointer, not a substitute for a source hash and page-level audit.

**Exact route:** (1) use the identified local PDF and register its complete bibliographic identity, version, source/retrieval URI if recoverable, local path, SHA-256 and page count; (2) write a **new, append-only W10 T2 full-text re-entry packet** linked to `D1-TH-015`, `D1-UT-001`, `D1-SEARCH-W10-002` and affected candidate claims, with page/section locators for model formulation, R/FE fidelity, experiments, error metrics, validity/breakdown criteria, criterion timing and M→R→E roles; (3) distinguish source facts, prior metadata inference and new scientific interpretation, recording whether the supplied human audit and independent read agree; (4) use W10's named-threat return route to issue a **versioned successor disposition** while preserving the old metadata-only W10 files as state-at-time; (5) have W11 verify source identity/hash/locators and update provenance/contradiction routing; (6) only then route `D1-REVIEW-003` as `READY_FOR_HUMAN_REVIEW`, without signing or applying K1–K9. The blocker is the absent auditable full-text *packet and review*, rather than access to the PDF. The W10/W11 provenance update is separate from this HG-06 design analysis.

## 9. Remaining uncertainty studies, threshold readiness and review routing

### 9.1 Minimum studies in order

1. **Human protocol inputs:** actual cantilever specimen/fixture, pressure-source/sheath arrangement, clamp/rail policy, service-load window and the three engineering decision limits/reserves.
2. **M reproduction pilot:** source equation/Algorithm transcription, published cases, spatial/load/quadrature refinement and an implementation hash.
3. **R reference pilot:** contact enforcement/regularization, mesh and interface refinement, pressure equilibration, load-transfer feasibility, finite-rotation solver and per-output residual numerical envelopes.
4. **3D/physical fidelity pilot:** compare selected pressure/width/membrane/fixture effects with the idealized 2D R; re-lock R if they materially affect the outputs relative to independently established resolution.
5. **E measurement pilot:** displacement and load calibration, pressure control, tip fiducial mapping, direct slip observability, false-event/noise floor, `D,ℓ_g,d_g`, onset interval resolution and specimen repeatability.
6. **Independent decision/uncertainty derivation:** propagate shared parameter covariance and separate R/E numerical/measurement uncertainty for `w`, `K_service` and `P_onset`; if each decision margin is resolvable, derive output-specific tolerances and obtain human threshold review *before* any final D1 error-map inspection.

| Threshold | U2 readiness | Reason |
|---|---|---|
| `epsilon_w` | **NOT_READY_REFERENCE_NOT_FROZEN** | `w` definition is locked, but R contact/pressure/fixture implementation and uncertainty are not. Engineering displacement limit also missing. |
| `epsilon_K` | **NOT_READY_OUTPUT_DEFINITION_AMBIGUOUS** | Chord rule is locked, but its independently specified numerical service interval is absent; R/uncertainty/use margin also pending. |
| `epsilon_Q` | **NOT_READY_OUTPUT_DEFINITION_AMBIGUOUS** | The canonical Q metric cannot be used as a cross-platform scalar; `P_onset` carrier is proposed but event domain/detection correspondence and reviewed metric revision are incomplete. |

No tolerance value has been proposed. The canonical threshold register remains `BLOCKED_NOT_FROZEN`, with no final project validation data seen according to its recorded state [R5]. An actual S11 threshold update needs output/metric lock, quantified uncertainty, engineering criterion, human review and timestamped pre-error freeze.

### 9.2 Six human reviews

| Review | U2 routing state | Reason and human decision |
|---|---|---|
| `D1-REVIEW-001` | **READY_FOR_HUMAN_REVIEW** | W09 narrowed candidate package exists; human confirms residual question is an object to attack, not a novelty verdict. |
| `D1-REVIEW-002` | **READY_FOR_HUMAN_REVIEW** | W10 T1 package exists; human confirms physical slip regimes are not model-validity boundaries. |
| `D1-REVIEW-003` | **BLOCKED_BY_CURRENT_TASK** | The T2 PDF is local, but no page-grounded W10 full-text packet or W11 provenance review is registered. Route after that registration; no K verdict here. |
| `D1-REVIEW-004` | **BLOCKED_BY_UNCERTAINTY** | Design definitions have advanced, but no output-specific uncertainty budgets, numerical decision margins or tolerances exist for human threshold review. |
| `D1-REVIEW-005` | **BLOCKED_BY_W12** | Frozen K attack on the strongest same-act threat has not run. |
| `D1-REVIEW-006` | **BLOCKED_BY_FINAL_SYNTHESIS** | K/red-team/final evidence map package does not yet exist. |

No review is marked approved or cleared. `HG09_status=BLOCKED`, `W12_authorized=false`.

## 10. Final U2 disposition and references

**U2 delivers a controlled definition/protocol lock, not HG-06 clearance.** The next scientific work is **human selection of actual service/fixture inputs followed by a targeted M/R/E feasibility and uncertainty pilot**. The T2 full-text provenance packet is a separate named W10/W11 route and can proceed using the located PDF. No final validity classification can be computed before the three metrics, uncertainty bases and acceptance tolerances are independently frozen.

- **[U1a]** `outputs/d1_execution/V4/W11/D1_HG06_U1_ANALYSIS.md`, exact comparator/uncertainty analysis, 2026-09-26.
- **[U1b]** `outputs/d1_execution/V4/W11/D1_HG06_U1_STATE.json`, machine state.
- **[S1] FACT FROM SOURCE / VERIFIED FULL TEXT:** Zhang, S., Yao, J., Zhao, W. and Wei, C. (2025), *A continuum-based model for a layer jamming beam*, *Mechanical Sciences* 16, 821–830, DOI [10.5194/ms-16-821-2025](https://doi.org/10.5194/ms-16-821-2025), `paper_id=95646b2cfc`; `data/papers/verification/D1-V002/2025-A continuum-based model for a layer jamming beam.pdf`, SHA-256 `95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd`. Paper locations cited inline.
- **[S2]** `docs/literature/paper_cards/zhang_2025_continuum_beam/source_bundle.json` and `paper-card.md`, derivative page-grounded record; source PDF has precedence.
- **[S3] VERIFIED FULL TEXT (identity only):** Wang, Q. et al. (2026), *Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction*, *Materials & Design* 268, 116573, DOI [10.1016/j.matdes.2026.116573](https://doi.org/10.1016/j.matdes.2026.116573); `data/inbox/2026-Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction.pdf`, 17 pages, SHA-256 `f77bc7b7d605e57e4bb7e11e468223ce7f670dc4e06072fd1ed99bb27062c5ca`. Identity checked against PDF p. 1; body claims await the named W10 audit.
- **[R1] CANONICAL STATE:** `docs/project/CURRENT_EXECUTION_SNAPSHOT.md`, D1 execution and gate state.
- **[R2] CANONICAL STATE:** `docs/project/research_state.json`, `d1` branch and W12 authorization.
- **[R3] CANONICAL PLAN:** `outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V6.md`, V6 control sections; `outputs/plans/D1_HARD_GATE_MATRIX_V6.json#HG-06` and `D1_REVISION_ROUTING_MATRIX_V6.json#RR-T`.
- **[R4] CANONICAL K FREEZE:** `outputs/d1_execution/V4/S09/D1_K_CRITERIA_REGISTER.json` (criteria only; no U2 verdict).
- **[R5] CANONICAL THRESHOLD STATE:** `outputs/d1_execution/V4/W11/D1_THRESHOLD_FREEZE_REGISTER.json`.
- **[R6] CANONICAL HUMAN STATE:** `outputs/d1_execution/V4/W11/D1_HUMAN_REVIEW_CLEARANCE.json`.
- **[R7] HISTORICAL NAMED THREAT:** `outputs/d1_execution/V4/W10/D1_PRIOR_ART_THREAT_MATRIX.json#D1-TH-015`, `D1_UNRESOLVED_THREAT_REGISTER.json#D1-UT-001`, `D1_SEARCH_DECISION_LOG.json#D1-SEARCH-W10-002`.
- **[R8] RESEARCH DESIGN:** `docs/research_design/EXACT_MODEL_SELECTION.md` and `M1_RESEARCH_ARCHITECTURE.md`; these make R/outputs/tolerances provisional.

**Unresolved:** source-to-code M implementation/reproduction; R and E fixture/pressure/contact pilots; service loads and engineering margins; `K_service` numeric endpoints; interior onset domain and directly measured slip; page-grounded T2 W10/W11 provenance registration; human dispositions. These are explicit prerequisites, not inferred numerical values.
