# D1-V007 C04 Adversarial Forward-Citation Audit

- **Status:** INCONCLUSIVE_MISSING_TARGET
- **Confidence:** high
- **Bundle SHA256:** cd61f9322d98217eedcc322722a04f96f871ef103d95f63801f7b526d0b67770
- **Kill condition met:** False
- **Final novelty lock allowed:** False

## Current P1

For one specified reduced/continuum vacuum-layer-jamming beam model under quasi-static planar bending, define output-specific predeclared model-form acceptance tolerances and determine experimentally validated validity/breakdown boundaries against an interface-resolving/full-layer reference, while explicitly accounting for vacuum-pressure-controlled normal contact, friction/slip evolution, and, where necessary, pressure redistribution or layer separation.

## Executive summary

All three currently identified forward citations of focal paper ca46dc062d were audited from verified full-text evidence. None kills the surviving P1. One paper directly reuses the focal multilayer continuum mechanics in an electromagnetic-mechanical coil model, but omits pressure-, preload-, surface-, and friction-dependent contact mechanics and supplies neither an interface-resolved mechanical comparator nor a tolerance-defined validity boundary. One is an adjacent global-local homogenization study for frictionless chiral helical structures; it contains detailed contact and finite-element comparisons but no friction/slip evolution or predeclared model-form acceptance boundary. The third uses Coulomb friction only as a mathematical analogy for superconducting critical-state electrodynamics and has no mechanical multilayer-contact study. Thus the current forward-citation branch is closed without a kill. However, DOI 10.1061/JSENDH.STENG-13096 is absent from the supplied verified full-text evidence, so C04 and the final novelty lock remain incomplete.

## Forward-citation closure

- Focal paper: ca46dc062d — The global-local mechanical behaviors of multilayered structure and applications to superconducting coils
- Expected current forward citations: 3
- Audited forward citations: 3
- All current forward citations audited: True
- Named DOI present in this round: False
- Missing named targets: 10.1061/JSENDH.STENG-13096

The three D1-V007 papers constitute the complete Scopus-reported forward-citation set supplied for the current search date, and each was audited exactly once. The focal forward-citation branch is therefore closed for this search date, without implying that future citations cannot appear. The separate named DOI remains outside the audited branch and prevents completion of the overall C04 falsification round.

## Four-link chain audit

### pressure_preload_to_friction_slip

- Supported: **True**
- Evidence: The focal paper and prior C03 evidence establish that normal contact stress enters Coulomb capacity and that pressure/preload can control frictional response. None of the three descendants materially strengthens this link for vacuum jamming: the direct coil extension omits pressure-dependent friction, the helical model is frictionless, and the critical-state paper is only an electromagnetic analogy.

### friction_slip_to_continuum_discrete_discrepancy

- Supported: **False**
- Evidence: The focal paper compares a frictional continuum model with a discrete-contact model, but the supplied evidence does not isolate pressure-driven stick/partial-slip/gross-slip evolution as the cause of a mapped model-form discrepancy. No descendant supplies that missing causal error map.

### discrepancy_to_predeclared_tolerance

- Supported: **True**
- Evidence: The focal paper applies a 5% maximum-displacement-error tolerance to continuum-versus-discrete discrepancies. The descendants introduce no additional physical model-form acceptance tolerance.

### tolerance_to_experimentally_validated_breakdown_boundary

- Supported: **False**
- Evidence: The focal 5% boundary is numerical, and its experiments do not intentionally sample accepted and rejected sides of that boundary. None of the descendants defines and experimentally crosses a comparable tolerance boundary.

### vacuum_to_contact_pressure_mapping

- Supported: **False**
- Evidence: No supplied descendant maps applied vacuum pressure to a spatial normal-contact-pressure field in a layer-jammed beam. The direct coil extension explicitly omits local contact pressure and preload effects.

### layer_separation_or_pressure_redistribution

- Supported: **False**
- Evidence: No descendant demonstrates how vacuum-induced pressure redistribution or local layer separation changes a reduced-model validity boundary. The direct coil extension suppresses separation with an overband, the chiral model is frictionless and assumes fixed winding radius, and the critical-state paper has no mechanical contact.

- **Complete chain:** False

The evidence retains the focal paper's numerical discrepancy-to-tolerance link but does not complete the pressure-driven friction-to-error link, experimental boundary-crossing link, or either vacuum-specific transfer link. The forward citations therefore do not remove the need for a vacuum-layer-jamming model-validity contribution.

## Kill test

- **pressure_or_preload_controls_contact:** True
- **friction_or_slip_is_explicit:** True
- **named_reduced_or_continuum_model:** True
- **interface_resolved_or_discrete_reference:** True
- **quantitative_model_form_error:** True
- **predeclared_acceptance_tolerance:** True
- **tolerance_defined_breakdown_boundary:** True
- **experiment_tests_both_sides_of_boundary:** False
- **transferable_to_vacuum_layer_jamming_without_new_mechanics:** False
- **kill_condition_met:** False

The focal paper and prior C03 evidence collectively satisfy the first seven structural elements: contact stress affects Coulomb capacity, friction/slip is explicit, named continuum and discrete-contact models exist, quantitative errors are evaluated, and a 5% tolerance defines numerical rotation limits. The three forward citations do not supply the two missing kill elements. None intentionally tests experiments on both sides of a tolerance-defined model-breakdown boundary, and none demonstrates transfer to vacuum layer jamming without new vacuum-to-pressure, redistribution, separation, or friction/contact mechanics.

## Paper-by-paper audit

### 6bdb4151e2 — A coupled electromagnetic-mechanical model for high temperature superconducting coils based on circuit model

- Evidence: VERIFIED_FULL_TEXT
- Citation role: **direct_mechanical_extension**
- Threat: **medium**
- Uses focal mechanical model: True
- Pressure/preload: No operational pressure or preload sweep controls the mechanical contact state. Turn separation is suppressed by a 0.5 mm overband, while the contact-resistance description explicitly omits local contact pressure, preload, surface condition, and inter-turn sliding.
- Friction/slip: The multilayer continuum representation incorporates interfacial slip kinematics, but practical inter-tape frictional behavior is explicitly omitted. No pressure-dependent Coulomb capacity or stick/partial-slip/gross-slip evolution is evaluated.
- Continuum/reduced model: A multilayer structural continuum model based on Kirchhoff-Love elastic thin shells and continuous displacement interpolation is coupled to an axisymmetric circuit/electromagnetic model.
- Discrete/reference model: Absent for the relevant mechanical model. The 2D axisymmetric T-A finite-element benchmark addresses electromagnetic computation, not a full-layer frictional mechanical-contact reference.
- Quantitative model-form error: Absent for reduced-versus-full-layer mechanical model form. The reported 15.5% strain-difference error is against an experiment, and the 0.01% inductance error concerns the ANN approximation; neither maps continuum-versus-interface-resolved mechanical discrepancy.
- Predeclared tolerance: Absent. ODE, split-field, and iteration tolerances are numerical-solver controls, not physical model-form acceptance tolerances.
- Validity boundary: Absent.
- Experiment crosses boundary: No. A three-turn insulated-coil strain comparison is reported, but no tolerance-defined breakdown boundary exists and no experiments intentionally sample both sides of one.
- Vacuum transferability: weak
- Proves: The focal-style multilayer continuum mechanics can be embedded in a bidirectionally coupled superconducting-coil model, and deformation-sensitive strain predictions can be compared with limited coil measurements.
- Does not prove: It does not establish vacuum-to-contact-pressure mechanics, pressure redistribution, separation, explicit frictional slip evolution, a full-layer mechanical comparator, predeclared model-form acceptance tolerances, or experimental validation across a breakdown boundary.

### 1502d9c1c6 — A global-local homogenization model for hierarchical chiral helical structures: Tension-torsion coupling and decoupling analysis

- Evidence: VERIFIED_FULL_TEXT
- Citation role: **adjacent_method_extension**
- Threat: **low**
- Uses focal mechanical model: False
- Pressure/preload: Normal line-contact forces arise from deformation of helical wires, but vacuum pressure and externally controlled interlayer preload are absent. The model assumes a constant winding radius and neglects some contact-deformation and Poisson effects.
- Friction/slip: Tangential friction and stick-slip are absent. Contact is explicitly frictionless, and the authors identify frictional cyclic behavior as future work.
- Continuum/reduced model: A named global-local analytical homogenization model based on Love thin-rod theory and strain linearization provides closed-form stiffness and contact quantities for hierarchical chiral helices.
- Discrete/reference model: Three-dimensional solid finite-element simulations and a plane-strain two-cylinder contact model provide geometry-resolved comparisons for the helical system.
- Quantitative model-form error: Limited percentage discrepancies are reported, including less than 7% against the Argatov analytical model and about 6% against a kinematic-analogy method. The evidence does not establish a systematic homogenized-versus-full-contact model-form error surface over the relevant frictional parameter space.
- Predeclared tolerance: Absent. Reported percentage differences are validation results, not predeclared accept/reject tolerances.
- Validity boundary: Absent. Small-strain limits, laying-angle restrictions, and the eta=0 coupling-decoupling condition are assumptions or physical/design boundaries, not tolerance-defined model-validity boundaries.
- Experiment crosses boundary: No. Prior stiffness measurements are compared with predictions, but no predeclared model-form boundary is tested on both sides.
- Vacuum transferability: weak
- Proves: Global-local homogenization can retain normal line-contact effects and efficiently predict stiffness and local stresses in hierarchical chiral helical structures, with finite-element and prior experimental comparisons.
- Does not prove: It does not address flat vacuum-jammed layers, Coulomb friction, stick/partial-slip/gross-slip evolution, vacuum-controlled pressure fields, separation, or a tolerance-defined and experimentally crossed model-breakdown boundary.

### a32f8501d6 — Critical state model for superconductivity: features and numerical implementation

- Evidence: VERIFIED_FULL_TEXT
- Citation role: **other**
- Threat: **low**
- Uses focal mechanical model: False
- Pressure/preload: Absent. The governing variables are electromagnetic field, current density, critical current, and numerical regularization parameters, not mechanical contact pressure or preload.
- Friction/slip: Coulomb friction and stick-slip appear only as a physical and mathematical analogy used to formulate and regularize superconducting vortex pinning. No mechanical frictional interface or layer slip is modeled.
- Continuum/reduced model: A continuum electromagnetic critical-state finite-element A-formulation is provided; it is not a reduced or continuum mechanical model of a multilayer beam.
- Discrete/reference model: Absent for mechanical contact. References are analytical and alternative numerical electromagnetic formulations.
- Quantitative model-form error: Absent for mechanical model form. Electromagnetic agreement, R-squared measures, runtime comparisons, and numerical convergence do not quantify reduced-versus-interface-resolved multilayer mechanics error.
- Predeclared tolerance: Absent for mechanical model validity. Regularization and penalty parameters are numerical controls.
- Validity boundary: Absent.
- Experiment crosses boundary: No experiments are reported, and no mechanical model-validity boundary is defined.
- Vacuum transferability: not_demonstrated
- Proves: A maximum-dissipation and yield-function framework analogous to Coulomb friction can regularize and solve non-smooth superconducting critical-state electrodynamics.
- Does not prove: A mathematical analogy does not establish mechanical transferability. The paper proves nothing about pressure-controlled layer contact, frictional slip, vacuum jamming, continuum-versus-full-layer discrepancy, or experimentally validated breakdown boundaries.

## Strongest threats

### Wang et al. (2026), paper_id ca46dc062d

- Threat: **high**
- Why it matters: The focal paper already occupies frictional multilayer homogenization, discrete-contact benchmarking, quantitative model-form error, a declared 5% tolerance, and a numerically defined validity boundary.
- Remaining gap: Its boundary is not experimentally crossed, vacuum pressure is not mapped to the contact field, separation is prohibited, and friction-dominant regimes remain outside the formulation.

### Chang et al. (2026), paper_id 6bdb4151e2

- Threat: **medium**
- Why it matters: This direct descendant demonstrates continued use of the focal multilayer continuum mechanics in a coupled coil application and includes a limited experimental strain comparison.
- Remaining gap: It explicitly omits pressure-, preload-, surface-, sliding-, and friction-dependent contact behavior; it has no full-layer mechanical comparator, model-form tolerance, or experimentally crossed validity boundary.

### Han et al. (2026), paper_id 1502d9c1c6

- Threat: **low**
- Why it matters: It shows that global-local homogenization can retain line-contact effects and be compared with detailed finite elements and prior experiments in a hierarchical structure.
- Remaining gap: Its helical geometry, frictionless contact, small-strain assumptions, and absence of a predeclared validity tolerance prevent direct transfer to vacuum-jammed beam validity mapping.

## Surviving gap

P1 survives only as a model-specific vacuum-layer-jamming validity study. The remaining contribution must map applied vacuum to the evolving spatial normal-contact field, determine how redistribution or separation changes friction capacity and stick/partial-slip/gross-slip behavior, quantify output-specific error against an interface-resolving/full-layer reference, apply predeclared acceptance tolerances, and deliberately test experiments on both accepted and rejected sides of the predicted boundary. Generic continuum development, discrete benchmarking, percentage-error reporting, or experiments at selected operating points remain insufficient.

## Stop-search decision

- Forward-citation branch closed: True
- Named DOI audit complete: False
- Additional named high-threat target remaining: True
- Stop broad search: True

All three current forward citations were audited and none meets the kill condition, so another broad keyword or citation sweep is not justified. The sole remaining literature action is the specifically named high-threat DOI 10.1061/JSENDH.STENG-13096: obtain and audit its full text, or document a full-text-unavailable decision.

## Recommended next action

Audit DOI 10.1061/JSENDH.STENG-13096 from verified full text. If full text cannot be obtained, record a documented full-text-unavailable decision. Do not begin another broad literature sweep.

## Evidence provenance

- outputs/verification/D1-V006/C03_ADVERSARIAL_AUDIT.json — PRIOR_C03_ADVERSARIAL_RESULT — 1ec49efca8eba6e59e487fef08c89b59c3990d8050b126535657edcb53ac2166
- data/evidence/2026-The global-local mechanical behaviors of multilayered structure and_ca46dc062d.json — FOCAL_VERIFIED_FULL_TEXT_EVIDENCE — 850139a1a6dcc0c34d2c8c9aff56d3c4881121b929e015435f7bc2a87d7cbad3
- outputs/verification/D1-V007/verification_matrix.json — CURRENT_C04_MATRIX — 9365810ca0c310855a92d087c219c6e3e98639770b7df3162d11ba8f17bd3666
- data/evidence/2026-A coupled electromagnetic-mechanical model for high temperature_6bdb4151e2.json — CURRENT_C04_FORWARD_CITATION_VERIFIED_FULL_TEXT_EVIDENCE — c97535539589b4b6ecac0aa967dc8e07fe00dd2cc10ab65ff6a9960d184efb77
- data/evidence/2026-A global-local homogenization model for hierarchical chiral_1502d9c1c6.json — CURRENT_C04_FORWARD_CITATION_VERIFIED_FULL_TEXT_EVIDENCE — 0ad9c9f8d66b788153d13909dc0bcd328a72ac09d0723e9201e2b69b55cfa958
- data/evidence/2026-Critical state model for superconductivity features and_a32f8501d6.json — CURRENT_C04_FORWARD_CITATION_VERIFIED_FULL_TEXT_EVIDENCE — 79fd6d829d76951b27740e34a882dc824a845f4f18020fa67bea29e2c4eaccd9
