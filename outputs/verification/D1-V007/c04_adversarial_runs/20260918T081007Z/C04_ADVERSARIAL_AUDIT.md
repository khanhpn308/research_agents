# D1-V007 C04 Adversarial Forward-Citation Audit

- **Status:** INCONCLUSIVE_MISSING_TARGET
- **Confidence:** high
- **Bundle SHA256:** cd61f9322d98217eedcc322722a04f96f871ef103d95f63801f7b526d0b67770
- **Kill condition met:** False
- **Final novelty lock allowed:** False

## Current P1

For one specified reduced/continuum vacuum-layer-jamming beam model under quasi-static planar bending, define output-specific predeclared model-form acceptance tolerances and determine experimentally validated validity/breakdown boundaries against an interface-resolving/full-layer reference, while explicitly accounting for vacuum-pressure-controlled normal contact, friction/slip evolution, and, where necessary, pressure redistribution or layer separation.

## Executive summary

All three currently identified forward citations of focal paper ca46dc062d were audited. None closes the remaining vacuum-layer-jamming validity chain. Paper 6bdb4151e2 directly reuses the multilayer continuum mechanics framework in a coupled superconducting-coil model, but omits pressure/preload-dependent contact and practical inter-tape friction, supplies no full-layer mechanical comparator, uses no predeclared model-form tolerance, and does not test a breakdown boundary. Paper 1502d9c1c6 is an adjacent global-local homogenization study for frictionless hierarchical helical structures; its reported errors and small-strain limits do not constitute a predeclared acceptance boundary. Paper a32f8501d6 transfers a Coulomb-friction mathematical analogy to superconducting electrodynamics, not mechanical layer contact. The focal branch is therefore closed for the current search date without a kill. However, DOI 10.1061/JSENDH.STENG-13096 remains unaudited, so the overall C04 conclusion is inconclusive and final novelty lock is not allowed. The focal paper's adopted 5% threshold is explicitly not counted as predeclared.

## Forward-citation closure

- Focal paper: ca46dc062d — The global-local mechanical behaviors of multilayered structure and applications to superconducting coils
- Expected current forward citations: 3
- Audited forward citations: 3
- All current forward citations audited: True
- Named DOI present in this round: False
- Missing named targets: 10.1061/JSENDH.STENG-13096

The three supplied D1-V007 verified-full-text papers match the complete current Scopus forward-citation count of three, so the focal forward-citation branch is closed as of the stated current search date. This closure does not cover future citations or the separately named DOI 10.1061/JSENDH.STENG-13096.

## Four-link chain audit

### pressure_preload_to_friction_slip

- Supported: **True**
- Evidence: The supplied focal and prior C03 evidence establishes that normal contact stress, internal pressure, or preload controls Coulomb capacity and slip evolution in multilayer or contact analogues. The three descendants add no vacuum-specific demonstration of this link.

### friction_slip_to_continuum_discrete_discrepancy

- Supported: **True**
- Evidence: The focal paper compares a frictional/slip-aware continuum formulation with a discrete-contact model and quantifies displacement discrepancies; it also shows large errors when slip-related kinematics are omitted. The descendants do not extend this into a vacuum-pressure-dependent discrepancy map.

### discrepancy_to_predeclared_tolerance

- Supported: **False**
- Evidence: No supplied source explicitly establishes that its physical model-form acceptance tolerance was fixed before the relevant validation or error results were examined. In particular, the focal paper's 5% threshold is explicit and adopted but not established as predeclared a priori.

### tolerance_to_experimentally_validated_breakdown_boundary

- Supported: **False**
- Evidence: No experiment deliberately samples points on both accepted and rejected sides of a boundary defined by a predeclared model-form tolerance. Selected response agreement and physical transition thresholds do not satisfy this link.

### vacuum_to_contact_pressure_mapping

- Supported: **False**
- Evidence: No supplied descendant models or measures the mapping from applied vacuum pressure to the spatial interlayer normal-contact-pressure field in a vacuum-jammed beam.

### layer_separation_or_pressure_redistribution

- Supported: **False**
- Evidence: No supplied descendant establishes how vacuum-driven pressure redistribution or local layer separation changes a reduced-model validity boundary. The direct coil descendant suppresses separation and omits contact pressure and preload from its contact-resistance mechanics.

- **Complete chain:** False

Links 1 and 2 are supported in non-vacuum multilayer/contact evidence, but the chain fails at the strict predeclaration requirement, experimental testing across the resulting boundary, and both vacuum-specific transfer links. None of the three forward citations repairs those failures.

## Kill test

- **pressure_or_preload_controls_contact:** True
- **friction_or_slip_is_explicit:** True
- **named_reduced_or_continuum_model:** True
- **interface_resolved_or_discrete_reference:** True
- **quantitative_model_form_error:** True
- **predeclared_acceptance_tolerance:** False
- **tolerance_defined_breakdown_boundary:** True
- **experiment_tests_both_sides_of_boundary:** False
- **transferable_to_vacuum_layer_jamming_without_new_mechanics:** False
- **kill_condition_met:** False

Across the focal and supplied prior evidence, pressure/preload-controlled contact, explicit friction/slip, named continuum or reduced models, discrete/full-layer references, quantitative model-form errors, and an adopted 5% tolerance-defined numerical boundary exist. The strict kill condition nevertheless fails because no evidence establishes that the physical acceptance tolerance was fixed a priori, no experiment deliberately tests both sides of that boundary, and transfer to vacuum layer jamming still requires new vacuum-to-contact-pressure, redistribution/separation, and friction/contact mechanics. The three descendants do not supply any of these missing elements.

## Paper-by-paper audit

### 6bdb4151e2 — A coupled electromagnetic-mechanical model for high temperature superconducting coils based on circuit model

- Evidence: VERIFIED_FULL_TEXT
- Citation role: **direct_mechanical_extension**
- Threat: **medium**
- Uses focal mechanical model: True
- Pressure/preload: No pressure or preload is used to control a mechanical contact state. Turn separation is suppressed by an outer overband, while the contact-resistance description explicitly omits local contact pressure and preload.
- Friction/slip: The multilayer structural continuum includes interfacial-slip kinematics, but practical inter-tape frictional behavior and pressure-dependent friction capacity are omitted. No stick/partial-slip/gross-slip evolution is demonstrated.
- Continuum/reduced model: A Kirchhoff-Love multilayer structural continuum is coupled bidirectionally to an axisymmetric circuit/electromagnetic model.
- Discrete/reference model: Absent for the relevant mechanical question. The 2D axisymmetric T-A finite-element benchmark is electromagnetic, not a discrete/full-layer mechanical contact reference.
- Quantitative model-form error: Absent for reduced-versus-full-layer mechanical model form. The reported 15.5% strain-difference error is against an experiment, the 70% value concerns an uncoupled model, and the 0.01% ANN error concerns inductance evaluation.
- Predeclared tolerance: Absent. ODE and split-field solver tolerances are numerical controls, not predeclared physical model-form acceptance criteria.
- Validity boundary: Absent. No mechanical parameter boundary is defined by crossing an acceptance tolerance.
- Experiment crosses boundary: No. A three-turn insulated-coil strain comparison is reported, but it neither defines nor deliberately samples both sides of a model-validity boundary.
- Vacuum transferability: weak
- Proves: The focal multilayer continuum framework can be embedded in a coupled electromagnetic-mechanical coil analysis and can improve agreement with one literature strain measurement relative to an uncoupled calculation.
- Does not prove: It does not establish pressure-controlled frictional contact, a full-layer mechanical reference, quantitative reduced-model error mapping, a predeclared tolerance, experimental boundary crossing, or vacuum-layer-jamming transfer mechanics.

### 1502d9c1c6 — A global-local homogenization model for hierarchical chiral helical structures: Tension-torsion coupling and decoupling analysis

- Evidence: VERIFIED_FULL_TEXT
- Citation role: **adjacent_method_extension**
- Threat: **low**
- Uses focal mechanical model: False
- Pressure/preload: Normal line-contact force and pressure arise from helical deformation and geometry, but no vacuum pressure or independently controlled preload is swept as a contact-state variable.
- Friction/slip: Tangential friction and stick-slip are absent. Contact is assumed frictionless, and the authors identify frictional cyclic contact as future work.
- Continuum/reduced model: A named global-local analytical homogenization model based on Love thin-rod theory and strain linearization represents hierarchical helical structures.
- Discrete/reference model: Three-dimensional solid finite elements and a two-dimensional plane-strain cylinder-contact model provide detailed numerical comparisons for helical geometry and normal contact.
- Quantitative model-form error: The paper reports less than 7% difference from the Argatov analytical model and about 6% difference from a kinematic-analogy method in specified comparisons, but it does not provide the required frictional reduced-versus-interface-resolved model-form error map.
- Predeclared tolerance: Absent. Small-strain ranges and reported percentage differences are assumptions or observed comparisons, not criteria shown to have been fixed before validation results were examined.
- Validity boundary: Absent. The coupling-decoupling condition is a physical/design boundary, while the stated strain and laying-angle restrictions are assumption domains rather than tolerance-crossing model-validity boundaries.
- Experiment crosses boundary: No. Prior stiffness measurements are used for selected comparisons, but experiments do not intentionally sample accepted and rejected sides of a predicted error boundary.
- Vacuum transferability: weak
- Proves: A computationally efficient global-local homogenization model can retain normal line-contact effects and predict stiffness and coupling behavior of hierarchical helical structures within stated linearized assumptions.
- Does not prove: It does not model Coulomb friction or slip evolution, vacuum-controlled contact, flat multilayer-beam mechanics, a predeclared model-form tolerance, or experimental validation of a breakdown boundary.

### a32f8501d6 — Critical state model for superconductivity: features and numerical implementation

- Evidence: VERIFIED_FULL_TEXT
- Citation role: **other**
- Threat: **low**
- Uses focal mechanical model: False
- Pressure/preload: Absent. The governing variables are electromagnetic field, transport current, and critical current density, not mechanical pressure or preload.
- Friction/slip: Coulomb friction and stick-slip appear only as a mathematical analogy used to regularize a superconducting critical-state constitutive law. No mechanical interface friction or layer slip is modeled.
- Continuum/reduced model: A continuum finite-element A-formulation represents superconducting electrodynamics through a yield-function and maximum-dissipation framework; it is not a reduced mechanical multilayer model.
- Discrete/reference model: No mechanical interface-resolving reference exists. Comparators are analytical superconductivity solutions and alternative electromagnetic formulations.
- Quantitative model-form error: Absent for mechanical model form. Reported agreement, convergence, and runtimes concern electromagnetic numerical formulations.
- Predeclared tolerance: Absent. The critical electric-field threshold is a physical constitutive parameter, while regularization and penalty settings are numerical parameters, not model-form acceptance tolerances.
- Validity boundary: Absent for multilayer mechanics or vacuum layer jamming.
- Experiment crosses boundary: No experiments are reported.
- Vacuum transferability: not_demonstrated
- Proves: Coulomb-friction-inspired continuum algorithms can regularize a nonsmooth electromagnetic critical-state model and reproduce superconductivity benchmarks efficiently.
- Does not prove: A mathematical friction analogy does not establish mechanical pressure-contact-friction transferability, multilayer slip mechanics, reduced-versus-full-layer error, or a vacuum-jamming validity boundary.

## Strongest threats

### Wang et al. (2026), paper_id ca46dc062d

- Threat: **high**
- Why it matters: The focal paper already combines a frictional multilayer continuum, a discrete-contact reference, quantitative displacement error, an adopted 5% boundary, layer-count/deformation sweeps, and multilayer experiments.
- Remaining gap: The supplied evidence does not establish prior declaration of the 5% tolerance, experimental sampling across its boundary, vacuum-pressure mapping, or validity under pressure redistribution and separation.

### Chang et al. (2026), paper_id 6bdb4151e2

- Threat: **medium**
- Why it matters: This direct descendant demonstrates continued use of the focal multilayer continuum in a coupled multiphysics coil model and supplies a quantitative experimental strain comparison.
- Remaining gap: It omits pressure/preload-dependent contact and practical inter-tape friction, has no mechanical full-layer reference or predeclared tolerance, and does not test a breakdown boundary.

### Han et al. (2026), paper_id 1502d9c1c6

- Threat: **low**
- Why it matters: It demonstrates another efficient global-local homogenization framework with explicit normal contact, detailed finite-element comparators, quantitative discrepancies, and experimental stiffness comparisons.
- Remaining gap: Its helical geometry and frictionless small-strain mechanics do not provide pressure-controlled slip, a predeclared model-validity criterion, boundary-crossing experiments, or vacuum-jamming transfer.

## Surviving gap

The forward citations do not remove the need for a vacuum-specific model-validity study. The surviving contribution is not generic homogenization, friction modeling, discrete benchmarking, percentage-error reporting, or selected experimental agreement. It is the prior declaration of output-specific acceptance tolerances for one specified vacuum-layer-jamming beam model, followed by independent experiments intentionally spanning the resulting accepted and rejected regions, with an interface-resolving reference that captures vacuum-generated normal-pressure fields, Coulomb slip evolution, pressure redistribution, and possible layer separation.

## Stop-search decision

- Forward-citation branch closed: True
- Named DOI audit complete: False
- Additional named high-threat target remaining: True
- Stop broad search: True

All three current forward citations have been audited without a kill, so further broad keyword or exploratory forward-citation searching should stop. The only recommended literature action is the already named target DOI 10.1061/JSENDH.STENG-13096, followed by either a verified-full-text audit or a documented full-text-unavailable decision.

## Recommended next action

Obtain and audit DOI 10.1061/JSENDH.STENG-13096 using verified full text. If full text cannot be obtained, document that unavailability and make an explicit evidence-limited decision. Do not begin another broad keyword sweep.

## Evidence provenance

- outputs/verification/D1-V006/C03_ADVERSARIAL_AUDIT.json — PRIOR_C03_ADVERSARIAL_RESULT — 1ec49efca8eba6e59e487fef08c89b59c3990d8050b126535657edcb53ac2166
- data/evidence/2026-The global-local mechanical behaviors of multilayered structure and_ca46dc062d.json — FOCAL_VERIFIED_FULL_TEXT_EVIDENCE — 850139a1a6dcc0c34d2c8c9aff56d3c4881121b929e015435f7bc2a87d7cbad3
- outputs/verification/D1-V007/verification_matrix.json — CURRENT_C04_MATRIX — 9365810ca0c310855a92d087c219c6e3e98639770b7df3162d11ba8f17bd3666
- data/evidence/2026-A coupled electromagnetic-mechanical model for high temperature_6bdb4151e2.json — CURRENT_C04_FORWARD_CITATION_VERIFIED_FULL_TEXT_EVIDENCE — c97535539589b4b6ecac0aa967dc8e07fe00dd2cc10ab65ff6a9960d184efb77
- data/evidence/2026-A global-local homogenization model for hierarchical chiral_1502d9c1c6.json — CURRENT_C04_FORWARD_CITATION_VERIFIED_FULL_TEXT_EVIDENCE — 0ad9c9f8d66b788153d13909dc0bcd328a72ac09d0723e9201e2b69b55cfa958
- data/evidence/2026-Critical state model for superconductivity features and_a32f8501d6.json — CURRENT_C04_FORWARD_CITATION_VERIFIED_FULL_TEXT_EVIDENCE — 79fd6d829d76951b27740e34a882dc824a845f4f18020fa67bea29e2c4eaccd9
