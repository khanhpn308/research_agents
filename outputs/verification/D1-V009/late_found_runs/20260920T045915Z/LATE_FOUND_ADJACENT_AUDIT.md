# D1-V009 Late-Found Adjacent-Mechanics Audit

- **Status:** SURVIVES_LATE_FOUND_TARGET
- **Confidence:** high
- **Bundle SHA256:** f5827a02b195823c442e73d3ac3716be6e8571b664395fab39d5ff72a64e1ade
- **Kill condition met:** False
- **Final novelty lock survives:** True

## Current P1

For one specified reduced/continuum vacuum-layer-jamming beam model under quasi-static planar bending, define output-specific PREDECLARED model-form acceptance tolerances and determine experimentally validated validity/breakdown boundaries against an interface-resolving/full-layer reference, while explicitly accounting for vacuum-pressure-controlled normal contact, friction/slip evolution, and, where necessary, pressure redistribution or layer separation.

## Target identity

- paper_id: d75a3e82bc
- Title: Modelling the large deformations in stratified media—the Cosserat continuum approach
- Year: 1999
- DOI: 
- Verified full text: True

## Executive summary

Adhikary, Mühlhaus, and Dyskin (1999) is strong theoretical precedent for representing stratified media as an equivalent Cosserat continuum with independent rotations, couple stresses representing layer bending stiffness, large-deformation kinematics, elastic and frictional/plastic interface behavior, tensile opening, and finite-element implementation. It quantitatively verifies selected buckling cases against analytical Euler solutions and examines mesh refinement, interlayer shear stiffness, friction angle, load level, bending-stiffness inclusion, and small- versus large-deformation formulations. It does not falsify final P1. The supplied evidence establishes no interface-resolving or full-layer numerical reference, no reduced-versus-discrete model-form error study, no relevant layer-count/discreteness validity sweep, no predeclared output-specific acceptance tolerance, no tolerance-defined boundary, and no physical experiments intentionally sampling both sides of such a boundary. Its Mohr-Coulomb joint treatment also does not establish vacuum-generated normal contact, pressure redistribution, or transfer to vacuum layer jamming without materially new mechanics. The paper defeats broad novelty claims about layered Cosserat modeling, but the specifically framed P1 remains materially intact.

## Mechanics overlap

- **equivalent_or_smeared_continuum:** True
- **cosserat_or_generalized_continuum:** True
- **large_deformation:** True
- **layer_bending_stiffness:** True
- **frictional_or_plastic_interface_slip:** True
- **interface_opening_or_separation:** True
- **finite_element_implementation:** True
- **quantitative_validation:** True
- **assessment:** The overlap is extensive. The paper uses an equivalent/smeared Cosserat continuum with independent rotations and couple stresses, incorporates layer flexural rigidity, supplies an incremental large-deformation formulation, represents interfaces through elastic stiffness or Mohr-Coulomb plastic sliding with a zero-normal-stress tension cut-off, permits delamination/opening, and implements the formulation in AFENA with eight-node finite elements and Newton-Raphson solution. Quantitative support consists of analytical Euler-buckling comparisons, eigen-deflection-shape comparisons, and mesh convergence. This is formulation verification and numerical mechanics evidence, not experimental validation or reduced-continuum-versus-explicit-interface validation.

## Kill test

- **named_reduced_or_continuum_model:** True
- **interface_resolved_or_discrete_reference:** False
- **quantitative_model_form_error:** False
- **finite_parameter_or_discreteness_sweep:** False
- **predeclared_acceptance_tolerance:** False
- **tolerance_defined_breakdown_boundary:** False
- **experiment_tests_both_sides_of_boundary:** False
- **vacuum_specific_contact_mechanics:** False
- **transferable_to_vacuum_layer_jamming_without_new_mechanics:** False
- **kill_condition_met:** False
- **evidence_summary:** The named model is a large-deformation equivalent Cosserat continuum for stratified media. Its analytical Euler solutions are limiting-solution benchmarks, not interface-resolved or discrete-layer references. The approximately 1.5% buckling-load discrepancy therefore does not establish the required reduced-versus-interface-resolved model-form error. Sweeps over mesh density, joint shear stiffness, friction angle, applied load, boundary conditions, bending-stiffness inclusion, and kinematic formulation investigate numerical convergence and physical response; they do not constitute a finite layer-count/discreteness validity sweep against a stronger reference. The approximately 50%-of-critical-load observation for divergence between small- and large-deformation results is a physical or assumption transition, not a predeclared tolerance-defined boundary. No physical experiment is reported, and no evidence establishes an a priori output-specific acceptance tolerance. The Mohr-Coulomb joint law lacks the demonstrated vacuum-to-normal-pressure relation, evolving pressure redistribution, and vacuum-jamming-specific multilayer contact mechanics required for direct transfer. Multiple mandatory links are absent, so the complete kill condition is not met.

## What the paper proves

- Equivalent Cosserat-continuum modeling of statistically homogeneous layered media predates P1.
- Independent rotations and couple stresses can embed individual-layer bending stiffness in a smeared layered-medium formulation.
- Large-deformation layered-continuum finite elements can represent buckling, frictional/plastic interlayer slip, tensile opening or delamination, and joint-state evolution.
- Interlayer shear stiffness and friction angle can materially affect predicted buckling capacity, while suppressing layer bending stiffness can cause instability or ill-conditioning after separation.
- The finite-element formulation reproduces analytical Euler buckling loads and eigen-deflection shapes quantitatively for the studied limiting cases.
- Small-deformation and large-deformation predictions can diverge as compressive loading approaches buckling.

## What the paper does NOT prove

- It does not provide an interface-resolving or explicit full-layer reference against which the Cosserat approximation is quantitatively benchmarked.
- It does not quantify reduced-continuum model-form error over layer count, layer discreteness, vacuum pressure, or another governing parameter against a stronger reference.
- It does not establish that any acceptance tolerance was fixed before validation or error results were inspected.
- It does not define a validity or breakdown boundary using a predeclared output-specific model-form tolerance.
- It does not report physical experiments validating the proposed continuum model or experiments intentionally chosen on both accepted and rejected sides of a tolerance-defined boundary.
- It does not establish vacuum-pressure-controlled normal contact, a vacuum-to-contact-pressure mapping, pressure redistribution within a jammed stack, or vacuum-jamming-specific slip evolution.
- It does not establish transferability to vacuum layer jamming without materially new contact mechanics.
- It does not establish novelty for applying equivalent, Cosserat, couple-stress, large-deformation, frictional-slip, or opening mechanics to layered media in general.

## Effect on final claims

### Claims no longer safe

- A broad claim that equivalent or smeared continuum modeling of frictional layered media is novel.
- A broad claim that Cosserat kinematics or couple stresses are newly used to represent individual-layer bending stiffness.
- A broad claim that combining large deformation, frictional/plastic interlayer slip, opening or delamination, and finite-element analysis in a layered continuum is novel.
- A broad claim that analytical buckling verification or parameter studies alone constitute a new layered-model validity framework.

### Claims still defensible

- Defining output-specific acceptance tolerances before inspecting the relevant model-error or validation results.
- Quantitatively mapping validity and breakdown of one specified reduced vacuum-layer-jamming beam model against an interface-resolving or full-layer reference.
- Testing layer-count/discreteness and vacuum-pressure effects as model-form validity variables rather than merely as physical-response variables.
- Experimentally sampling intentionally selected points on both accepted and rejected sides of a tolerance-defined boundary.
- Explicitly connecting applied vacuum pressure to normal contact, friction/slip evolution, pressure redistribution, and possible layer separation in a vacuum-jammed stack.

- **Scope change required:** False
- **Assessment:** The current P1 is already narrow enough to survive because its substantive contribution is the predeclared, output-specific, reduced-versus-interface-resolved validity framework with deliberate experimental boundary testing and vacuum-specific contact mechanics. No material title or research-question revision is required. The theoretical framing must nevertheless acknowledge Adhikary et al. as prior mechanics lineage and must not present Cosserat homogenization, couple-stress bending, large deformation, frictional slip, or opening as independently novel.

## New named threats

None.

## Lock decision

- **final_novelty_lock_survives:** True
- **reopen_broad_search:** False
- **targeted_followup_required:** False
- **threat_to_final_p1:** medium
- **rationale:** The target is a high-threat precedent for the mechanics backbone but only a medium threat to the precisely locked P1. It removes broad mechanics-novelty language without supplying the interface-resolved comparison, predeclared tolerance, tolerance-defined boundary, boundary-crossing experiment, or vacuum-specific transfer needed to close the final contribution. The supplied evidence names no concrete additional source and identifies no specific unresolved issue requiring a targeted full-text audit; therefore neither targeted follow-up nor renewed broad searching is justified.

## Recommended next action

Retain the provisional final lock, incorporate Adhikary et al. (1999) explicitly into the theoretical lineage, and revise all novelty language to locate the contribution in the predeclared validity/breakdown protocol and vacuum-specific reduced-versus-full-layer validation—not in Cosserat homogenization or frictional layered-continuum mechanics themselves. Proceed by naming the reduced model and interface-resolving reference, preregistering output-specific tolerances before inspecting errors, and designing experiments on both predicted-valid and predicted-invalid sides.

## Provenance

- PRIOR_D1_V008_FINAL_AUDIT — outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json — SHA256 b888cfe083888aa0b2859ee97046f60e2c4d505cc4882f258fd29e305f28cd3a
- PREDECLARED_TOLERANCE_SEMANTIC_GUARDRAIL — outputs/verification/D1-V007/C04_SEMANTIC_CORRECTION.md — SHA256 0c3a8ddc186edd1884ce9329f5a2053a55198087d2df269234d83503149bc0ac
- D1_V009_AUDIT_PROTOCOL — docs/D1-V009_LATE_FOUND_ADJACENT_AUDIT_PLAN.md — SHA256 25dd679749a9a164a3297e0aeb773f5e818835c553d8b276da7c0d9a3149c574
- CURRENT_D1_V009_MATRIX — outputs/verification/D1-V009/verification_matrix.json — SHA256 c3fcde1131039130bbaeca8a0884b814023fea6a3c6a7883ac1ec5b8a7aa44d1
- TARGET_VERIFIED_FULL_TEXT_EVIDENCE — data/evidence/Mech Cohesive Frict Material - 1999 - Adhikary - Modelling the large deformation_d75a3e82bc.json — SHA256 c95d5c7de50a1368564efc847fffa5e634fe011f18583065cf2b385f86241678
