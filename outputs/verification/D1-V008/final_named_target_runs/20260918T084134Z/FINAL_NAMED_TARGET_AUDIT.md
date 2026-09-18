# D1-V008 Final Named-Target Adversarial Audit

- **Status:** SURVIVES_FINAL_TARGET
- **Confidence:** high
- **Bundle SHA256:** 16ad90f9782ffebd411486f4b97b610da29989f811a2697c36ba902037e4220b
- **Kill condition met:** False
- **Final novelty lock allowed:** True

## Current P1

For one specified reduced/continuum vacuum-layer-jamming beam model under quasi-static planar bending, define output-specific predeclared model-form acceptance tolerances and determine experimentally validated validity/breakdown boundaries against an interface-resolving/full-layer reference, while explicitly accounting for vacuum-pressure-controlled normal contact, friction/slip evolution, and, where necessary, pressure redistribution or layer separation.

## Target identity

- DOI: 10.1061/JSENDH.STENG-13096
- paper_id: 53d328abaa
- Title: Analytical Solution for Bending Deformation of Steel–Concrete Composite Beams Considering Nonlinear Interfacial Slip
- Verified full text: True

## Executive summary

The final named target is a high-threat adjacent mechanics paper because it provides a closed-form Euler–Bernoulli composite-beam model with an explicit nonlinear interfacial load–slip law, comparison with four experimental beams, a three-dimensional finite-element model with discrete stud elements, and an applicability statement at L/H>=10. It does not falsify P1. Its slip is governed by headed-stud connector behavior rather than vacuum-pressure-controlled Coulomb contact; interface friction, uplift, pressure redistribution, and separation are neglected. The reported 3%, 5%, less-than-8%, 0.02 mm, and 20% quantities are observed discrepancies or sensitivity results, not predeclared acceptance tolerances. The L/H>=10 statement is an applicability limit associated with omission of shear deformation, not a tolerance-defined model-form boundary experimentally tested on both sides. Together with C04, the strict kill chain remains incomplete. Because the prior forward-citation branch is closed, the expected DOI has now been audited from verified full text, and the supplied evidence names no additional concrete high-threat target capable of completing the missing chain, broad searching should stop and provisional final novelty lock is allowed.

## Target audit

- **explicit_nonlinear_interfacial_slip:** True
- **pressure_or_preload_controls_contact_state:** False
- **named_reduced_or_continuum_model:** True
- **interface_resolved_or_discrete_reference:** True
- **quantitative_model_form_error:** False
- **predeclared_acceptance_tolerance:** False
- **predeclared_tolerance_evidence:** not established
- **tolerance_defined_breakdown_boundary:** False
- **experiments_intentionally_cross_boundary:** False
- **vacuum_specific_contact_mechanics:** False
- **transferable_to_vacuum_layer_jamming_without_new_mechanics:** False
- **threat_to_p1:** high
- **what_it_proves:** A closed-form Euler–Bernoulli analytical model can represent nonlinear longitudinal slip in a two-component steel–concrete composite beam through an energy-based headed-stud load–slip relation, reproduce selected serviceability experiments, and expose sensitivity to omitted transverse shear at low L/H.
- **what_it_does_not_prove:** It does not establish vacuum-pressure-controlled normal contact, a distributed interlayer pressure field, Coulomb stick/partial-slip/gross-slip evolution, many-layer contact, pressure redistribution, lift-off or separation, a jamming-appropriate full-layer reference, a predeclared model-form tolerance, or experiments deliberately crossing a tolerance-defined validity boundary.

## Observed-error interpretation

- **analytical_deflection_3_percent:** Observed analytical-model-versus-experiment disagreement under serviceability loading; it is not established as a predeclared model-form acceptance tolerance and is not reduced-versus-interface-resolved model-form error.
- **fe_deflection_5_percent:** Observed finite-element-versus-experiment disagreement; it is not a predeclared tolerance and does not quantify reduced-model-versus-FE model-form discrepancy.
- **bending_strain_8_percent:** Observed prediction-versus-experiment discrepancy; it is not established as a predeclared acceptance criterion or a reduced-versus-interface-resolved model-form error.
- **slip_difference_0_02_mm:** Observed maximum prediction-versus-experiment slip difference under lower loading; it is not a predeclared acceptance tolerance or a model-form breakdown criterion.
- **lh5_deflection_effect_20_percent:** A numerical sensitivity result attributed to transverse shear deformation omitted from the Euler–Bernoulli derivation. It is a known-omitted-mechanism comparison, not automatically the required reduced-versus-interface-resolved model-form error and not a predeclared tolerance.
- **are_any_predeclared_acceptance_tolerances:** False
- **assessment:** The supplied evidence reports several quantitative discrepancies and effects, but none has the required temporal evidence showing that an acceptance threshold was fixed before validation or error inspection. None establishes the output-specific, predeclared reduced-model-versus-interface-resolved error criterion required by P1.

## L/H boundary analysis

- **lh_ge_10_statement_present:** True
- **boundary_type:** physical_assumption_limit
- **source_basis:** The analytical derivation neglects transverse shear under Euler–Bernoulli theory. A numerical sensitivity study over L/H=5–20 reports an approximately 20% deflection effect at L/H=5, and the paper consequently states applicability to relatively slender beams with L/H>=10. This supports an assumption-based applicability limit, with a post-hoc recommendation character, rather than a tolerance-defined model-form boundary.
- **derived_from_predeclared_model_form_tolerance:** False
- **validated_by_experiments_on_both_sides:** False
- **relevance_to_p1:** It illustrates how an omitted mechanism can delimit an analytical beam model, but it does not supply P1's boundary because no a priori model-form tolerance is established and experiments are not shown to intentionally sample accepted and rejected sides.

## Kill test

- **pressure_or_preload_controls_contact:** True
- **friction_or_slip_is_explicit:** True
- **named_reduced_or_continuum_model:** True
- **interface_resolved_or_discrete_reference:** True
- **quantitative_model_form_error:** True
- **predeclared_acceptance_tolerance:** False
- **tolerance_defined_breakdown_boundary:** False
- **experiment_tests_both_sides_of_boundary:** False
- **transferable_to_vacuum_layer_jamming_without_new_mechanics:** False
- **kill_condition_met:** False
- **evidence_summary:** Across the target and authoritative C04 evidence, the literature collectively contains pressure/preload-sensitive contact analogues, explicit friction or slip, reduced/continuum models, discrete references, and quantitative model-form comparisons. The target adds a nonlinear headed-stud slip model and an assumption-based L/H applicability limit but does not repair the decisive gaps. No supplied source establishes an a priori physical model-form acceptance tolerance; therefore no boundary is defined by such a predeclared tolerance, and no experiment intentionally tests both sides of it. Transfer also requires materially new vacuum-to-contact-pressure, many-layer Coulomb-contact, pressure-redistribution, and separation mechanics.

## New named threats

None.

## Stop-search decision

- **prior_forward_citation_branch_closed:** True
- **target_doi_audit_complete:** True
- **additional_high_threat_named_target_remaining:** False
- **broad_search_should_stop:** True
- **final_novelty_lock_allowed:** True
- **decision_rationale:** C04 authoritatively closed the current focal forward-citation branch. D1-V008 contains the expected paper_id and DOI and supplies verified-full-text evidence, completing the final named-target audit. The kill condition remains false, and the target supplies no specifically identified new paper with a concrete prospect of satisfying the missing predeclaration, boundary-crossing experiment, and vacuum-transfer links. The documented search protocol has therefore reached its stop condition; this permits provisional thesis-execution lock, not an absolute claim that no overlapping paper can ever exist.

## Final surviving contribution

For one specified reduced/continuum vacuum-layer-jamming beam model in quasi-static planar bending, predeclare output-specific model-form acceptance tolerances and experimentally map accepted and rejected regions against an interface-resolving/full-layer reference that represents vacuum-generated normal-pressure fields, Coulomb slip evolution, and, where relevant, pressure redistribution and layer separation.

## Recommended next action

Stop broad literature searching, freeze P1 provisionally, and move to thesis execution: select and name the reduced model and full-layer reference, pre-register output-specific tolerances before inspecting validation errors, define the parameter space, and design independent experiments that intentionally sample both predicted-valid and predicted-invalid regions.

## Provenance

- `PRIOR_C04_CANONICAL_RESULT` — `outputs/verification/D1-V007/C04_ADVERSARIAL_AUDIT.json` — SHA256 `6c5e5cabbde641cc827bb7561248d41f1e01b256290c78105225ff2e07d79ec1`
- `PREDECLARED_TOLERANCE_SEMANTIC_GUARDRAIL` — `outputs/verification/D1-V007/C04_SEMANTIC_CORRECTION.md` — SHA256 `0c3a8ddc186edd1884ce9329f5a2053a55198087d2df269234d83503149bc0ac`
- `CURRENT_D1_V008_MATRIX` — `outputs/verification/D1-V008/verification_matrix.json` — SHA256 `2ea246ae302c6cf0b91575f1b4db177d189e608991136d3b05cbf45d26d5b178`
- `TARGET_VERIFIED_FULL_TEXT_EVIDENCE` — `data/evidence/2024-Ye-Analytical Solution for Bending Deformation of Steel-Concrete Composite Beams Considering Nonlinear Interfacial Slip_53d328abaa.json` — SHA256 `0d58585a7d09e29196ed8d7a6582a57beef37032432240a513baeaad015b516d`
