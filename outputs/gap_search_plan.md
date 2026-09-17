# Gap Verification Search Plan

## Candidate Gap

The corpus supports investigating whether a single experimentally calibrated, geometrically nonlinear model incorporating hyperelastic elastomer behavior, passive envelope/heater layers, and frictional interlayer contact can predict force and stiffness across both unjammed and jammed states more accurately than the simplified models represented here. This is a candidate gap within the supplied corpus, not a claim of global novelty.

## Research Question

For one hybrid SMP–layer-jamming continuum finger, does a geometrically nonlinear finite-element model incorporating hyperelastic elastomer behavior, explicit passive envelope/heater layers, and frictional interlayer contact reduce held-out normalized RMSE in tip force and tangent bending stiffness by at least 30% relative to a simplified E(T)I(P) baseline across 25–75 °C, 0 to −100 kPa vacuum, and both jammed and unjammed loading states?

# A. Literature Searches

## Search 1

**Priority:** critical

**Search seed:**

Search IEEE Xplore, Scopus, Web of Science, and Google Scholar for: ("layer jamming" OR "laminar jamming" OR "sheet jamming") AND ("finite element" OR "analytical model" OR "mechanics model") AND ("soft robot" OR "continuum robot" OR "soft actuator").

**Purpose:**

Search for prior work that may already address or close the candidate research gap.

**Decision rule:**

If equivalent prior work already solves the same technical problem under comparable conditions, the candidate gap must be revised or rejected.

## Search 2

**Priority:** critical

**Search seed:**

Search for passive-layer treatment using: ("layer jamming" OR "laminar jamming") AND (envelope OR membrane OR encapsulation OR heater) AND (friction OR contact OR hyperelastic).

**Purpose:**

Search for prior work that may already address or close the candidate research gap.

**Decision rule:**

If equivalent prior work already solves the same technical problem under comparable conditions, the candidate gap must be revised or rejected.

## Search 3

**Priority:** critical

**Search seed:**

Search for state-spanning models using: ("layer jamming" OR "laminar jamming") AND (jammed AND unjammed) AND (prediction OR validation OR stiffness model).

**Purpose:**

Search for prior work that may already address or close the candidate research gap.

**Decision rule:**

If equivalent prior work already solves the same technical problem under comparable conditions, the candidate gap must be revised or rejected.

## Search 4

**Priority:** critical

**Search seed:**

Search for large-deformation formulations using: ("variable stiffness" AND "soft actuator") AND ("large deformation" OR hyperelastic OR Ogden OR Mooney-Rivlin) AND (jamming OR frictional contact).

**Purpose:**

Search for prior work that may already address or close the candidate research gap.

**Decision rule:**

If equivalent prior work already solves the same technical problem under comparable conditions, the candidate gap must be revised or rejected.

## Search 5

**Priority:** critical

**Search seed:**

Search for thermomechanical hybrid models using: ("shape memory polymer" AND "layer jamming") AND (thermomechanical OR viscoelastic OR finite-element OR multiphysics).

**Purpose:**

Search for prior work that may already address or close the candidate research gap.

**Decision rule:**

If equivalent prior work already solves the same technical problem under comparable conditions, the candidate gap must be revised or rejected.

## Search 6

**Priority:** critical

**Search seed:**

Conduct backward and forward citation searches from DOI 10.1109/LRA.2024.3357035 and DOI 10.1109/TMECH.2024.3352643, screening titles, abstracts, methods, and supplementary material for models that include envelope/heater layers, nonlinear elastomers, and frictional slip.

**Purpose:**

Search for prior work that may already address or close the candidate research gap.

**Decision rule:**

If equivalent prior work already solves the same technical problem under comparable conditions, the candidate gap must be revised or rejected.

## Search 7

**Priority:** critical

**Search seed:**

For each potentially overlapping study, extract mechanism, geometry, constitutive laws, passive layers, contact formulation, jammed/unjammed coverage, validation conditions, held-out prediction errors, and availability of reusable parameters or code.

**Purpose:**

Search for prior work that may already address or close the candidate research gap.

**Decision rule:**

If equivalent prior work already solves the same technical problem under comparable conditions, the candidate gap must be revised or rejected.

## Search 8

**Priority:** high

**Search seed:**

Artifact of narrow corpus boundary: The candidate gap is synthesized from an artificially restricted five-paper sample; multi-layer frictional contact and hyperelastic encapsulation modeling are established in broader solid mechanics.

**Purpose:**

Determine whether the apparent gap is genuinely scientific or only an implementation issue.

**Decision rule:**

If the concern is already resolved by established literature, revise or reject the gap.

## Search 9

**Priority:** high

**Search seed:**

Standard engineering simulation vs scientific gap: Implementing existing commercial FEA contact and hyperelastic formulations for a specific actuator geometry constitutes routine engineering application rather than an open scientific gap.

**Purpose:**

Determine whether the apparent gap is genuinely scientific or only an implementation issue.

**Decision rule:**

If the concern is already resolved by established literature, revise or reject the gap.

## Search 10

**Priority:** high

**Search seed:**

Evaluation against a strawman baseline: The research question benchmarks against an oversimplified 1D scaling heuristic (K proportional to E(T)I(P)), guaranteeing an artificial 30% improvement without advancing mechanics theory.

**Purpose:**

Determine whether the apparent gap is genuinely scientific or only an implementation issue.

**Decision rule:**

If the concern is already resolved by established literature, revise or reject the gap.

## Search 11

**Priority:** high

**Search seed:**

Neglect of thermoviscoelastic phase transition: Framing the issue as geometric non-linearity and passive layer omission neglects the dominant physics of the SMP glass transition (Tg approx 50 °C), which requires thermoviscoelasticity.

**Purpose:**

Determine whether the apparent gap is genuinely scientific or only an implementation issue.

**Decision rule:**

If the concern is already resolved by established literature, revise or reject the gap.

## Search 12

**Priority:** high

**Search seed:**

Platform-specific confinement: Restricting the study to a single hybrid finger prototype fails to establish generalizable mechanics principles transferable across other variable-stiffness architectures.

**Purpose:**

Determine whether the apparent gap is genuinely scientific or only an implementation issue.

**Decision rule:**

If the concern is already resolved by established literature, revise or reject the gap.

# B. Paper Screening Criteria

- [critical] Reject the proposed accuracy advantage if the nonlinear model fails to reduce held-out tip-force and tangent-stiffness NRMSE by at least 30% relative to the baseline.
- [critical] Test whether improvement persists on load cases excluded from calibration; failure on held-out conditions indicates overfitting rather than better mechanics.
- [critical] Perform ablation models that separately remove the passive layers, hyperelasticity, and frictional contact. If removal does not materially degrade held-out prediction, the corresponding proposed mechanism is not supported.
- [critical] Repeat validation separately in jammed and unjammed states. A pooled improvement that masks failure in either state does not support the unified-model claim.
- [critical] Use repeated specimens and propagate measurement uncertainty. If improvement is smaller than inter-specimen or sensor uncertainty, treat it as practically unsupported.
- [critical] Check residuals against displacement, temperature, vacuum, and loading direction. Systematic residual structure falsifies model adequacy even when aggregate RMSE improves.
- [critical] Compare predicted and observed hysteresis. If a rate-independent contact model cannot reproduce loading–unloading behavior, test a viscoelastic extension or narrow the model's claimed domain.
- [critical] Verify that fitted friction and constitutive parameters remain physically plausible and do not require separate unconstrained values for every test condition.
- [critical] Coupon-level parameter prediction failure: Falsified if constitutive and contact parameters measured via independent ASTM tensile, DMA, and tribometer tests fail to predict assembled finger response within 30% NRMSE without in situ tuning.
- [critical] Passive-layer ablation invariance: Falsified if an ablated FEA model omitting explicit heater and envelope layers predicts held-out force and stiffness with accuracy statistically indistinguishable from the full model.
- [critical] Strain-rate sensitivity divergence: Falsified if varying experimental displacement rates across an order of magnitude produces force deviations that exceed the model's prediction error margin.
- [critical] Systematic residual structure across glass transition: Falsified if force and stiffness prediction residuals exhibit structured, non-random error peaks in the 45–55 °C SMP glass transition regime.
- [critical] State-specific error divergence: Falsified if held-out NRMSE in the compliant unjammed state degrades relative to existing soft actuator models, demonstrating that aggregate improvements stem from error pooling.
- [high] Broad systematic literature synthesis: Exhaustive search across solid mechanics and soft robotics literature outside the 5-paper corpus to verify whether hyperelastic layer-jamming FEA models already exist.
- [high] Independent coupon-level material characterization: Temperature-dependent DMA for SMP, biaxial tensile data for elastomer and envelope membranes, and tribometric friction data across 25–75 °C.
- [high] Component-level sensitivity analysis: Numerical and experimental sensitivity tests establishing whether passive envelope and heater stiffness contributions are statistically distinguishable from silicone batch variability.
- [high] Formulation of non-trivial reduced-order benchmarks: Derivation of an intermediate composite beam model with interlayer slip to serve as a scientifically meaningful baseline rather than a 1D scaling heuristic.
- [high] Through-thickness thermal distribution measurements: Experimental thermocouple profiling across the multi-layer cross-section during heating and cooling cycles to validate thermal modeling assumptions.

# C. Methodology / Experiment Checks

- [medium] Inadequate SMP constitutive modeling: Purely hyperelastic models cannot capture the severe rate-dependent modulus relaxation, yield, and three-order-of-magnitude stiffness drop of SMP across 25–75 °C.
- [medium] Static friction coefficient assumption: Modeling interlayer contact with a constant Coulomb friction coefficient fails to represent polymer softening, stick-slip, and adhesion changes across Tg.
- [medium] Neglect of spatial and transient thermal gradients: Embedded heaters generate non-uniform through-thickness temperature distributions; assuming uniform isothermal states will cause severe prediction errors.
- [medium] Unmodeled envelope boundary conditions and membrane pretension: Atmospheric pressure clamping induces biaxial membrane tension that prestresses the stack, which cannot be captured without modeling seal compliance and pretension.
- [medium] Rate-independent formulation for hysteretic dissipation: Paper f28f2201b8 proves hysteresis enlarges under vacuum and heating; rate-independent contact formulations cannot capture this history- and rate-dependent dissipation.