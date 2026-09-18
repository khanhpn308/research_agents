# D1-V006 C03 Adversarial Audit

- **Status:** SUBSTANTIALLY_NARROWED
- **Confidence:** high
- **Evidence bundle SHA256:** `9fdbe816ec7fcac69e545e970131d4a7ce0bbd1c47be7f68f5119927d2519f3f`
- **Final project novelty verdict allowed:** False

## Current P1

For one specified reduced or continuum vacuum-layer-jamming beam model under quasi-static planar bending, establish output-specific, predeclared model-form acceptance tolerances and independently validate tolerance-crossing validity and breakdown boundaries over vacuum pressure, layer count, and bending amplitude against an interface-resolving reference. The study must test whether vacuum-generated normal contact, Coulomb capacity, stick/partial-slip/gross-slip evolution, and contact redistribution invalidate assumptions such as zero gap, prescribed contact pressure, or friction that is not dominant; novelty cannot rest on frictional homogenization, discrete-contact benchmarking, a finite layer sweep, or an adopted percentage-error boundary alone.

## Executive summary

C03 does not satisfy the complete kill condition, but it substantially narrows P1. Wang et al. (2026), paper_id ca46dc062d, already provide the closest framework: a named continuum theory for multilayer structures, homogenized Coulomb friction driven by contact stress, a penalty-based discrete-contact reference, layer-count and deformation sweeps, quantitative displacement errors, an explicit 5% applicability threshold, resulting rotation limits, and experimental comparison for 35-, 50-, and 70-layer bending stacks. Therefore, frictional multilayer homogenization, continuum-versus-discrete error mapping, and even a declared percentage-based applicability boundary are not sufficient novelty. Flexible-pipe studies additionally connect pressure and initial contact stress to Coulomb capacity, stick-transition-slip bending, full-layer references, reduced helix-contact models, and experiments. Rough-contact, equivalent-thin-layer, Iwan, steel-polymer, and soft-hard-joint studies supply pressure/preload-dependent friction and experimentally supported slip evolution. The remaining kill components are nevertheless absent: no supplied framework experimentally validates the tolerance-crossing breakdown boundary itself, and no framework demonstrates transfer from vacuum pressure to spatially evolving layer contact without additional contact mechanics. The closest continuum model assumes negligible interlayer gaps, warns that large friction violates its Kirchhoff-Love basis, and does not sweep vacuum-driven pressure. The flexible-pipe reduced model shows that assuming constant contact pressure causes error, but supplies no predeclared model-form tolerance boundary. Thus P1 survives only as a vacuum-specific, experimentally validated boundary problem, not as a generic continuum-model or friction-homogenization contribution.

## Kill test

- **named_reduced_or_equivalent_model:** True
- **interface_resolving_or_exact_reference:** True
- **governing_interaction_parameter:** True
- **quantitative_model_form_error:** True
- **finite_parameter_or_discreteness_sweep:** True
- **predeclared_acceptance_tolerance:** True
- **tolerance_defined_validity_domain:** True
- **validated_breakdown_boundary:** False
- **transferable_to_pressure_dependent_friction_without_new_mechanics:** False
- **kill_condition_met:** False

Collectively, C03 establishes named reduced models, full-layer/discrete-contact references, pressure and friction parameters, quantitative model-form errors, and finite sweeps. Most importantly, ca46dc062d uses an explicit 5% displacement-error threshold to define layer-count-dependent rotation limits for a frictional multilayer continuum against a discrete contact model. Flexible-pipe and joint-contact papers separately establish pressure-dependent Coulomb capacity, stick-transition-slip evolution, contact redistribution, reduced representations, and experimental comparison. The chain still fails at items 8 and 9. The 5% continuum breakdown boundary is numerical rather than experimentally validated at tolerance crossing, while experiments demonstrate selected responses rather than the boundary. Direct transfer to vacuum layer jamming is also not established: ca46dc062d enforces negligible gaps, does not sweep vacuum pressure, and excludes friction-dominant regimes; flexible-pipe pressure/contact models use helical geometry, calibrated residual prestress, and no declared error boundary. Combining these families would require new vacuum-to-contact-field modeling and validation rather than a demonstrated transfer.

## High-threat criterion audit

### Wang and Yue (2021), paper_id afe2a3a310

- Criterion: Pressure, prestress, friction-coefficient, element, and contact sensitivities are compared while reproducing full-scale pipe hysteresis.
- Type: **none**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: This is a strong pressure-contact-friction analogue and full-layer experimental benchmark, but it does not define reduced-model acceptance or breakdown.

### Wang, Ye, and Yue (2022), paper_id a300a3b714

- Criterion: Elastic slip tolerance below 10^-3 is needed to avoid underpredicting stick stiffness and friction moment.
- Type: **numerical_convergence**
- Predeclared tolerance based: True
- Model-form validity boundary: False
- Only numerical/design criterion: True
- Transferability: weak
- Assessment: The threshold controls penalty-friction numerical behavior. It cannot be counted as a physical reduced-model acceptance tolerance.

### Yang, Xu, and Guo (2023), paper_id 8ce1db3bca

- Criterion: Microslip-to-macroslip transition and gross-slip capacity emerge from pressure-distributed Jenkins elements.
- Type: **physical_transition**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: It supplies pressure-to-capacity-to-slip mechanics and experiments, but a physical slip transition is not a continuum-model breakdown boundary.

### Messina and Miranda (2024), paper_id 13e407003a

- Criterion: Maximum absolute coefficient-of-friction error of 0.010 and R²=0.95 are reported for the fitted model.
- Type: **none**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: The values quantify fitted predictive performance but are not predeclared acceptance thresholds and do not delimit a continuum validity domain.

### Li et al. (2025), paper_id 7b85aadc84

- Criterion: Minimum tangential load for microslip and maximum load for full slip partition the physical contact state.
- Type: **physical_transition**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: The equivalent-thin-layer model closely matches the pressure-friction-slip chain, including pressure redistribution through wear, but the thresholds govern slip state rather than reduced-model validity.

### Wang et al. (2026), paper_id 20cee2210a

- Criterion: A 3% finite-element mesh-sensitivity target and formulation-specific iterative convergence tolerances are used.
- Type: **numerical_convergence**
- Predeclared tolerance based: True
- Model-form validity boundary: False
- Only numerical/design criterion: True
- Transferability: weak
- Assessment: These are numerical controls. The observed -13.21% second-mode error is a reported failure, not a predeclared tolerance boundary.

### Jin et al. (2026), paper_id 02d3360815

- Criterion: Critical lateral displacement marks macro-slip; reduced-versus-differential error below 0.5% and experimental loop-area error within 3.3% are reported.
- Type: **physical_transition**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: This strongly threatens any claim based only on preload-dependent soft-interface stick-slip or reduced hysteresis modeling, but neither percentage is established as an acceptance threshold or mapped breakdown boundary.

### Wang et al. (2026), paper_id ca46dc062d

- Criterion: A 5% maximum displacement-error threshold against a discrete contact model yields permissible rotations of about 20 degrees for 30 layers and 7.5 degrees for 150 layers.
- Type: **model_validity**
- Predeclared tolerance based: True
- Model-form validity boundary: True
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: This is C03's closest kill evidence. It supplies an explicit tolerance-based continuum-versus-discrete validity boundary for frictional multilayers and separately compares the model with experiments. The boundary itself is not experimentally validated, vacuum pressure is not swept, separation is prohibited, and large-friction regimes are excluded.

## Strongest threats

### Wang et al. (2026), paper_id ca46dc062d

- Threat: **high**
- Why it matters: It already combines frictional multilayer homogenization, a discrete-contact reference, layer-count and rotation sweeps, quantitative errors, an explicit 5% applicability threshold, a validity boundary, and multilayer bending experiments.
- Remaining gap: The tolerance-crossing boundary is not experimentally validated; vacuum pressure is not an input sweep; zero gap is assumed; and large-friction or separation regimes require different mechanics.

### Wang, Ye, and Yue (2022), paper_id a300a3b714

- Threat: **high**
- Why it matters: It links pressure and initial contact stress to Coulomb stick-transition-slip bending, compares a named reduced helix-contact model with a full-layer surface-contact model, and uses full-scale experiments.
- Remaining gap: No predeclared physical error tolerance or tolerance-defined breakdown surface is provided, and transfer from helical pipe contact to flat vacuum-clamped sheets is not demonstrated.

### Wang and Yue (2021), paper_id afe2a3a310

- Threat: **high**
- Why it matters: It provides a full-layer, pressure-dependent Coulomb-contact reference with experimentally observed quasi-static bending hysteresis across three pressure levels.
- Remaining gap: It is primarily a reference model rather than a reduced-versus-full validity framework; initial stress and friction inputs are calibrated, and no declared breakdown criterion exists.

### Jin et al. (2026), paper_id 02d3360815

- Threat: **high**
- Why it matters: It experimentally connects preload and preload degradation to a compact stick-slip model, micro-to-macro slip evolution, and quantitative hysteresis errors in a soft-hard interface.
- Remaining gap: It is a dynamic/harmonic single-interface law with uniform pressure, not a multilayer beam homogenization study, and its errors are not acceptance thresholds.

### Yang, Xu, and Guo (2023), paper_id 8ce1db3bca

- Threat: **high**
- Why it matters: It maps a resolved contact-pressure distribution into a reduced Iwan constitutive law and validates preload-dependent hysteresis and microslip-to-macroslip behavior experimentally.
- Remaining gap: Normal-contact redistribution during structural bending is not retained, no multilayer discrete reference is used, and no tolerance-defined validity domain is supplied.

### Li et al. (2025), paper_id 7b85aadc84

- Threat: **high**
- Why it matters: It combines an equivalent thin layer, a continuum beam, nonuniform preload, Coulomb microslip, evolving pressure redistribution, experiments, and quantitative prediction error.
- Remaining gap: The target is fretting wear in a single bolted interface; no full multilayer bending reference or predeclared model-form breakdown criterion is provided.

### Messina and Miranda (2024), DOI 10.1002/eqe.4128, paper_id 13e407003a

- Threat: **high**
- Why it matters: It experimentally supports a pressure-dependent steel-polymer friction law with explicit displacement-history-driven breakaway and quantitative error measures.
- Remaining gap: It is a calibrated lumped friction law without a multilayer continuum, discrete contact reference, contact redistribution, or tolerance-defined breakdown boundary.

## Paper-by-paper audit

### 7c3aac183e — The existence of a critical length scale in regularised friction

- Evidence: VERIFIED_FULL_TEXT
- Threat: **low**
- Physical analogue: Dynamic slip rupture along a two-dimensional deformable elastic half-space against a rigid flat surface.
- Interface/connection model: Classical Coulomb friction regularized by a simplified Prakash-Clifton evolution law; interface opening is suppressed.
- Reduced/equivalent model: Regularized friction law whose small-characteristic-length limit approaches classical Coulomb behavior.
- Normal/contact pressure role: Normal contact stress enters the evolving regularized frictional strength; nucleation is imposed through a transient reduction of contact pressure.
- Friction law/capacity: Coulomb friction with equal static and kinetic coefficients, filtered through Prakash-Clifton regularization.
- Stick-slip mechanism: Dynamic rupture and slip propagation are studied; the paper does not construct a quasi-static multilayer stick/partial-slip/gross-slip beam model.
- Contact redistribution: A prescribed spatiotemporal pressure reduction nucleates slip, but evolving multilayer contact redistribution is not modeled.
- Reference model: Mesh-refined explicit finite-element solutions and the classical-Coulomb limiting response.
- Experimental validation: None; an experimental identification procedure is proposed.
- Quantitative error: Relative propagation-distance error below 0.5% and arrival-time error below 0.1% are used for mesh convergence; Lc=10^-5 m is reported for the analyzed system.
- Criterion: A critical regularization length below which further reduction does not alter dynamic slip outputs, plus numerical mesh-error criteria.
- Criterion type: numerical_convergence
- Declared tolerance: 0.5% propagation-distance error and 0.1% arrival-time error, both numerical convergence tolerances rather than physical model-form acceptance tolerances.
- Validity domain: Dynamic two-dimensional plane-strain sliding of a linear elastic half-space against a rigid plane in a well-posed, no-opening regime.
- Breakdown boundary: The L-nd convergence map and critical regularization length delimit numerical and spectral influence, not reduced multilayer model breakdown.
- Transferability: weak
- Proves: A friction regularization length and event frequency can control dynamic slip predictions and mesh requirements.
- Does not prove: It does not establish quasi-static beam homogenization validity, a vacuum-pressure sweep, experiments, or a physical tolerance-defined continuum breakdown boundary.

**Governing parameters:**
- regularization length L
- interface node density nd
- input frequency f
- normal and shear tractions
- friction coefficient

### ac9973e89e — Transition from stick to slip in Hertzian contact with “Griffith” friction: The Cattaneo–Mindlin problem revisited

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: Quasi-static tangential loading of an elastically similar Hertzian spherical contact.
- Interface/connection model: Hertz pressure combined with a Griffith mode-II slip-inception condition and Coulomb friction in the slip annulus.
- Reduced/equivalent model: Analytical Cattaneo-Mindlin-type contact model augmented by a fracture-energy stick-zone correction.
- Normal/contact pressure role: Normal load sets the Hertz pressure field and contact size; an optional pressure-dependent friction toughness changes the critical stick-zone scaling.
- Friction law/capacity: Coulomb sliding capacity in the slip annulus plus a Griffith fracture criterion at the stick-slip boundary.
- Stick-slip mechanism: Complete stick persists to a nonzero Qmin, partial slip follows, and global sliding occurs through unstable collapse at a critical stick-zone radius.
- Contact redistribution: The Hertz pressure distribution is explicit, but multilayer bending-induced redistribution is absent and elastic similarity decouples normal and tangential fields.
- Reference model: Classical Cattaneo-Mindlin theory and analytical limiting comparisons.
- Experimental validation: No new experiment; the paper discusses prior PMMA and oscillatory-contact observations.
- Quantitative error: No reduced-versus-interface-resolving model-form error map is supplied.
- Criterion: Critical stick-zone size and associated Qmin/Qmax define physical slip transitions.
- Criterion type: physical_transition
- Declared tolerance: None.
- Validity domain: Quasi-static, axisymmetric, linear-elastic, elastically similar Hertzian contacts with no normal adhesion.
- Breakdown boundary: The critical stick radius is a physical instability boundary, not a tolerance-defined reduced-model failure boundary.
- Transferability: weak
- Proves: Normal loading and pressure-dependent toughness can govern stick, partial slip, and abrupt gross sliding.
- Does not prove: It does not compare a multilayer continuum model with a discrete-layer reference or validate a model-form acceptance boundary for vacuum-jammed beams.

**Governing parameters:**
- normal load P
- tangential load Q
- friction coefficient f
- contact radius a
- friction fracture energy
- critical stick radius

### 79d1adc34c — Friction Characteristics of CFRP Plates in Contact with Copper Plates under High Contact Pressure

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: A unidirectional CFRP strip pulled between two copper clamping plates under high transverse pressure.
- Interface/connection model: Nominally uniform double-sided contact with experimentally characterized friction and wear.
- Reduced/equivalent model: Empirical Amontons linear law for hard copper and Howell-type pressure power law for annealed copper.
- Normal/contact pressure role: Pressure directly changes shear capacity, friction coefficient for annealed copper, sliding distance, wear mechanism, and failure mode.
- Friction law/capacity: For as-received copper, tau=0.31 sigma; for annealed copper, tau=1.02 sigma^0.76 with decreasing apparent friction coefficient.
- Stick-slip mechanism: Periodic stick-slip at 50–100 MPa is attributed to debris accumulation and release; high pressures produce ploughing and rupture.
- Contact redistribution: Not resolved; normal stress is assumed uniform over the nominal contact areas.
- Reference model: No interface-resolving or discrete-layer reference model.
- Experimental validation: Direct pullout experiments across six pressure levels and two copper conditions.
- Quantitative error: Regression fits are reported, including R²=0.97 and 0.92, but no reduced-model error against a reference.
- Criterion: Observed pressure regimes separate debris-mediated stick-slip from severe ploughing and premature rupture.
- Criterion type: physical_transition
- Declared tolerance: None.
- Validity domain: Dry CFRP-copper pullout at one displacement rate and 50–175 MPa nominal contact pressure.
- Breakdown boundary: Material rupture prevents characterization above 175 MPa; this is an experimental/material limit, not continuum-model breakdown.
- Transferability: weak
- Proves: Friction capacity and damage mechanism can depend nonlinearly on contact pressure and counterface condition.
- Does not prove: It does not provide a multilayer reduced model, discrete reference, model-form error map, or vacuum-pressure validity criterion.

**Governing parameters:**
- contact pressure 50–175 MPa
- copper hardness
- pullout displacement
- friction coefficient or power-law exponent

### afe2a3a310 — A full layered numerical model for predicting hysteretic behavior of unbonded flexible pipes considering initial contact pressure

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: A nine-layer unbonded flexible pipe under internal pressure and quasi-static cyclic cantilever bending.
- Interface/connection model: Full-layer three-dimensional hard normal contact with penalty enforcement and Coulomb tangential friction between adjacent layers and armor tendons.
- Reduced/equivalent model: Equivalent orthotropic shells are used for selected carcass and pressure-armor layers, but the principal bending model is full layered rather than a reduced-versus-full validity study.
- Normal/contact pressure role: Internal pressure and manufacturing-induced sheath prestress determine interlayer contact forces, friction moment, curvature, and hysteresis.
- Friction law/capacity: Coulomb friction capacity under hard normal contact; calibrated coefficients vary with the tested pressure cases.
- Stick-slip mechanism: Tendon slip initiates near the neutral axis and progresses toward intrados and extrados through stick, transition, and slip phases.
- Contact redistribution: Resolved by the full contact model; solid polymer layers change contact forces through Poisson effects.
- Reference model: The full-layer 3D Abaqus contact model is the highest-fidelity model, but no distinct reduced model is systematically error-mapped against it here.
- Experimental validation: Full-scale cyclic bending data at three internal pressures are reproduced; the 2 MPa initial prestress and other uncertain geometry parameters are calibrated, so independent validation is not established.
- Quantitative error: Agreement with measured moment-curvature loops is reported, but no common scalar reduced-versus-full model-form error or tolerance map is supplied.
- Criterion: No physical model-form acceptance criterion; friction coefficient above 0.2 affects solver choice and runtime.
- Criterion type: none
- Declared tolerance: None for physical model-form validity.
- Validity domain: One four-inch pipe geometry under 0.1 Hz cyclic bending, three internal pressures, room temperature, and no external effective tension.
- Breakdown boundary: No tolerance-defined reduced-model breakdown boundary; transfer of the calibrated initial prestress to other pipes is explicitly unresolved.
- Transferability: partial
- Proves: Pressure and initial contact stress can govern multilayer Coulomb stick-slip bending and experimental hysteresis in a full-layer structure.
- Does not prove: It does not establish an accepted reduced model, predeclared model-form tolerance, or experimentally validated continuum breakdown map transferable to vacuum-jammed sheets.

**Governing parameters:**
- internal pressure 0.7, 10, and 20 MPa
- outer-sheath prestress
- friction coefficient 0.05–0.35
- element representation
- normal contact stiffness
- bending amplitude

### 444793969c — Experimental validation of the applicability of effective spring boundary conditions for modelling damaged interfaces in laminate structures

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: Three-layer aluminium-epoxy laminates with manufactured interfacial damage interrogated by ultrasonic guided waves.
- Interface/connection model: Zero-thickness effective spring boundary conditions with equal normal and tangential stiffness and traction continuity.
- Reduced/equivalent model: Effective Spring Boundary Conditions derived from quasi-static micromechanical crack-density relations.
- Normal/contact pressure role: Curing pressure is reported, but operational pressure-dependent friction capacity is absent.
- Friction law/capacity: No Coulomb friction or gross-slip capacity; displacement jump is linearly related to traction.
- Stick-slip mechanism: None.
- Contact redistribution: None; static damaged adhesive interfaces are represented by springs.
- Reference model: Micromechanical crack models and measured guided-wave dispersion; no frictional discrete-contact model.
- Experimental validation: Guided-wave measurements across pristine, scratched, cut, and abraded interfaces support inferred stiffness ranges.
- Quantitative error: Theoretical and measured dispersion curves and inferred defect measures are compared, but no scalar model-form acceptance-error map is supplied.
- Criterion: Stiffness ranges classify damage severity, including kappa below 1 GPa/mm approaching debonded behavior.
- Criterion type: design_rule
- Declared tolerance: None.
- Validity domain: Linear, time-harmonic guided waves in flat isotropic laminates with small defects relative to wavelength.
- Breakdown boundary: Restrictions on defect shape and the quasi-static microcrack approximation are stated, but no tolerance-defined ESBC breakdown boundary is validated.
- Transferability: weak
- Proves: An effective interface spring can be related to measurable defect geometry and experimentally checked in a layered structure.
- Does not prove: It does not model pressure-controlled friction, stick-slip bending, contact redistribution, or continuum-versus-discrete vacuum-jamming validity.

**Governing parameters:**
- spring stiffness kappa
- crack density-width product Cl
- frequency
- damage type and severity

### 202fd05d8f — A barrier method for frictional contact on embedded interfaces

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: A stationary embedded frictional interface in a two-dimensional linear-elastic continuum.
- Interface/connection model: Barrier normal-contact energy with smoothed Coulomb friction and enriched finite-element displacement jumps.
- Reduced/equivalent model: No physical homogenized beam model; the contribution is a contact-algorithm formulation.
- Normal/contact pressure role: Barrier contact generates normal pressure, which sets Coulomb tangential capacity and affects initialization and conditioning.
- Friction law/capacity: C1-smoothed Coulomb friction.
- Stick-slip mechanism: A smoothed transition between stick and slip is introduced for differentiability and Newton robustness.
- Contact redistribution: Interface tractions are spatially resolved; averaged integration suppresses oscillations, but only one stationary interface is studied.
- Reference model: Analytical inclusion benchmark, Lagrange-multiplier solutions, penalty solutions, and mesh refinement.
- Experimental validation: None.
- Quantitative error: Contact-pressure and displacement-jump error norms and asymptotic convergence are reported, but they measure numerical accuracy.
- Criterion: Barrier parameters control maximum separation error and Newton convergence; no physical model-form acceptance criterion is given.
- Criterion type: numerical_convergence
- Declared tolerance: No physical model-form tolerance.
- Validity domain: Quasi-static, infinitesimal-strain, two-dimensional linear elasticity with a single stationary embedded interface.
- Breakdown boundary: Early-step Newton failure and accuracy changes are numerical boundaries, not continuum homogenization breakdown.
- Transferability: weak
- Proves: Normal contact, Coulomb capacity, and mixed stick-slip can be solved robustly on embedded interfaces.
- Does not prove: It does not reduce many layers, compare homogenized and discrete physical models, perform experiments, or define a vacuum-jamming validity boundary.

**Governing parameters:**
- barrier thickness
- barrier stiffness
- maximum microslip displacement
- friction coefficient
- mesh size
- stiffness contrast

### a300a3b714 — A novel helix contact model for predicting hysteretic behavior of unbonded flexible pipes

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: A multilayer unbonded flexible pipe under internal pressure and quasi-static cyclic bending.
- Interface/connection model: Node-to-surface double-helix contact beams with hard normal contact and Coulomb penalty friction; the full comparator uses surface-to-surface contact.
- Reduced/equivalent model: Named equivalent layered double helix contact beam model EQUI_SHCONT2B, plus analytical plane-section and shear-interaction models.
- Normal/contact pressure role: Internal pressure and manufacturing prestress generate interlayer pressure and friction moment; assuming constant pressure in analytical models overpredicts high-pressure hysteresis.
- Friction law/capacity: Coulomb penalty friction with return-mapping stick-slip formulations.
- Stick-slip mechanism: Stick, transition, and slip determine stick stiffness, slip stiffness, friction moment, and dissipated energy.
- Contact redistribution: The numerical models resolve pressure distributions and ovalization; simplified analytical models assume constant pressure and thereby exhibit error.
- Reference model: Full surface-to-surface, full-layer finite-element contact model and full-scale bending measurements.
- Experimental validation: Comparison with full-scale tests at 0.7, 10, and 20 MPa; independence from calibration is not demonstrated because friction coefficients and initial prestress are pressure-case/model calibration inputs.
- Quantitative error: Global hysteresis agreement, local penetration/deformation deviations, and 95–98% runtime reduction are reported; no uniform scalar model-form error map is provided.
- Criterion: Elastic slip tolerance below 10^-3 is recommended to avoid underestimating stick stiffness and friction moment.
- Criterion type: numerical_convergence
- Declared tolerance: The elastic-slip setting is a contact-algorithm tolerance, not a predeclared physical model-form acceptance tolerance.
- Validity domain: One four-inch pipe under cyclic pure bending and three internal pressure levels.
- Breakdown boundary: Local normal-stress and transverse-slip deviations, ovalization differences, and constant-pressure analytical error are identified without a tolerance-crossing validity surface.
- Transferability: partial
- Proves: A reduced contact model can reproduce pressure-dependent multilayer Coulomb hysteresis against full-layer contact and experiments while preserving key slip mechanisms.
- Does not prove: It does not provide a predeclared output-specific model-form tolerance, a tolerance-defined parameter domain, or an experimentally validated breakdown boundary transferable without adapting helical-pipe mechanics.

**Governing parameters:**
- internal pressure
- initial sheath prestress
- friction coefficient
- curvature
- helix contact angle
- elastic slip tolerance
- core equivalence
- mesh density

### a9cd14eca9 — A Single-Variable Zigzag Approach to Model Imperfect Interfaces in Layered Beams

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: Two- and three-layer orthotropic beams with linear sliding-compliant interfaces under transverse loading.
- Interface/connection model: Zero-thickness interfaces with no opening and linear tangential traction-displacement-jump stiffness.
- Reduced/equivalent model: Named single-variable homogenized zigzag beam theory.
- Normal/contact pressure role: Absent.
- Friction law/capacity: Linear interfacial springs; no Coulomb capacity.
- Stick-slip mechanism: No stick-slip transition; sliding compliance is linear.
- Contact redistribution: Asymmetric interface stiffness redistributes displacement jumps and shear tractions, but normal contact is not modeled.
- Reference model: Pagano two-dimensional exact elasticity solutions obtained through a transfer-matrix method.
- Experimental validation: None.
- Quantitative error: Strong overlap with exact elasticity is reported for local fields, without a scalar error surface.
- Criterion: Response nearly reaches perfect bonding around KS h/ET=10 for two layers and 5 for three layers.
- Criterion type: design_rule
- Declared tolerance: None; the near-overlap stiffness levels are not tolerance-defined acceptance limits.
- Validity domain: Small-strain, simply supported, identical-material two- and three-layer beams with zero normal separation.
- Breakdown boundary: Known restrictions include elastic mismatch, nonlinear intralayer kinematics, finite-thickness interfaces, and other boundary conditions; no validated error boundary is supplied.
- Transferability: weak
- Proves: An efficient homogenized layered-beam model can retain interface displacement jumps and reproduce exact linear imperfect-interface solutions.
- Does not prove: It does not include normal pressure, Coulomb friction, finite-layer contact, experiments, or a vacuum-controlled breakdown map.

**Governing parameters:**
- nondimensional tangential stiffness KS h/ET
- layer count
- interface-stiffness asymmetry
- load distribution
- aspect ratio

### 8ce1db3bca — Modelling tangential friction considering contact pressure distribution of rough surfaces

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Rough flat contacts and bolted joints subjected to normal preload and cyclic tangential displacement.
- Interface/connection model: Elastoplastic rough-surface finite elements generate pressure distributions that are mapped to a continuous Iwan distribution of Coulomb spring-slider elements.
- Reduced/equivalent model: Physics-based adjusted Iwan model with a twofold-Weibull slider-strength distribution and residual stiffness.
- Normal/contact pressure role: The pressure distribution sets local normal forces, slider capacities, initial tangential stiffness, microslip-to-macroslip evolution, and energy dissipation.
- Friction law/capacity: Constant local Coulomb coefficient maps each normal force to a critical slip force.
- Stick-slip mechanism: Distributed Jenkins elements progressively slip from microslip to macroslip, producing stiffness softening and hysteresis.
- Contact redistribution: Asperity-scale pressure statistics are resolved off-line, but the bolted-joint application assumes a uniform spatial pressure distribution and does not evolve normal contact during shear.
- Reference model: Three-dimensional elastoplastic rough-contact finite elements, Mindlin analytical contact, classic Iwan variants, and experiments.
- Experimental validation: Published flat-contact and bolted-joint experiments across three and four preload levels; model parameters are optimized at discrete loads, so fully independent validation is not established.
- Quantitative error: Contact-pressure CDF maximum error below 0.06 and relative energy-dissipation comparisons are reported; no predeclared accept/reject map is supplied.
- Criterion: Microslip-to-macroslip transition and gross-slip force are physical transition measures.
- Criterion type: physical_transition
- Declared tolerance: None for model-form acceptance.
- Validity domain: Rough metal contacts under constant preload and cyclic tangential loading with fixed local friction and no dynamic separation.
- Breakdown boundary: Test-rig compliance and assumed uniform joint pressure cause discrepancies, but no tolerance-defined breakdown locus is validated.
- Transferability: partial
- Proves: Contact-pressure distributions can be reduced to a frictional constitutive model that predicts preload-dependent stick-slip hysteresis.
- Does not prove: It does not homogenize a bending stack, compare against a full multilayer contact reference over vacuum pressure, or validate a tolerance-defined breakdown boundary.

**Governing parameters:**
- normal load
- contact-pressure distribution
- surface roughness and fractal parameters
- friction coefficient
- tangential amplitude

### 13e407003a — A novel friction model for steel-polymer interfaces in sliding seismic isolation bearings

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Unidirectional cyclic sliding of steel-polymer seismic-isolation interfaces.
- Interface/connection model: A lumped parallel friction law combining Coulomb, logarithmic velocity dependence, displacement-dependent breakaway, pressure modification, and thermal degradation.
- Reduced/equivalent model: Named modular five-parameter steel-polymer friction model.
- Normal/contact pressure role: A hyperbolic-tangent factor represents reduction of friction coefficient with increasing pressure; pressure is treated as separable from velocity.
- Friction law/capacity: Coulomb base capacity modified by pressure, velocity, temperature, and an exponential reversal-dependent breakaway increment.
- Stick-slip mechanism: Breakaway peaks occur at direction reversal and decay exponentially with accumulated displacement; nonreversing stops do not reinitiate them for the tested interfaces.
- Contact redistribution: Absent; apparent contact pressure and contact area are lumped, and true area is assumed equal to apparent area.
- Reference model: Alternative lumped friction laws and measured force-displacement histories; no interface-resolving reference.
- Experimental validation: Specialized cyclic tests support the reversal rule, but parameter fitting and evaluation use the experimental histories; independent validation is not demonstrated.
- Quantitative error: For oil-filled UHMWPE, R²=0.95 and maximum absolute coefficient-of-friction error=0.010 are reported after fitting.
- Criterion: Goodness-of-fit metrics compare friction formulations; no acceptance boundary is declared.
- Criterion type: none
- Declared tolerance: None; 0.010 is a reported fitted error, not a predeclared threshold.
- Validity domain: Fully reversed, steady, unidirectional steel-thermoplastic sliding under the tested pressure, velocity, and thermal conditions.
- Breakdown boundary: Bidirectional motion, transitions to and from rest, and other materials are outside the demonstrated domain; no tolerance-crossing boundary is validated.
- Transferability: partial
- Proves: A pressure-dependent steel-polymer friction law can experimentally reproduce reversal-driven breakaway and cyclic hysteresis more accurately than simpler laws.
- Does not prove: It does not supply a multilayer beam continuum model, an interface-resolving reference, contact redistribution, or a predeclared validity/breakdown map.

**Governing parameters:**
- sliding displacement and reversal point
- velocity
- normal pressure
- temperature
- polymer type

### 8daa38176d — Modeling of Stick-Slip Contact Mechanics Based on Improved Continuous-Scale Fractal-Discrete Iwan Model

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: Rough steel interfaces under combined normal loading and cyclic tangential displacement.
- Interface/connection model: Continuous-scale fractal asperity contact coupled to discrete Jenkins/Iwan spring-slider elements.
- Reduced/equivalent model: Improved continuous-scale fractal-discrete Iwan model.
- Normal/contact pressure role: Normal force controls real contact, normal stiffness, slider-force distribution, gross-slip displacement, and saturation force.
- Friction law/capacity: Uniform macroscopic Coulomb coefficient assigns slip capacities to Jenkins units.
- Stick-slip mechanism: Progressive microslip softens stiffness, followed by macroslip with constant residual stiffness.
- Contact redistribution: Normal force is statistically distributed among asperities, but mutual asperity interaction and evolving surface morphology are neglected.
- Reference model: Earlier fractal contact models and literature steel-contact experiments; no full structural interface-resolving reference.
- Experimental validation: Comparison with secondary experimental hysteresis loops at approximately 200–600 N.
- Quantitative error: Close curve agreement is stated, but no general scalar model-form error surface or declared acceptance tolerance is supported.
- Criterion: Critical macroslip displacement and saturation force mark a physical transition.
- Criterion type: physical_transition
- Declared tolerance: None.
- Validity domain: Unidirectional rough steel contact with fixed topology, uniform friction, simplified elastic/plastic asperity states, and no wear.
- Breakdown boundary: Model assumptions fail for interacting asperities, evolving wear, localized friction variation, or soft viscoelastic materials; no validated threshold is supplied.
- Transferability: weak
- Proves: Normal load and roughness can be linked to distributed stick-slip response and macroslip onset.
- Does not prove: It does not establish multilayer bending homogenization error, vacuum actuation transfer, or a tolerance-defined continuum breakdown boundary.

**Governing parameters:**
- normal load
- friction coefficient
- fractal dimension
- fractal roughness
- tangential displacement
- number of Jenkins elements

### 7b85aadc84 — Fretting wear modeling of bolted joint interface with microscopic roughness using the 1D microslip friction model and equivalent thin layer

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: A preloaded bolted lap-joint interface represented along its contact length and subjected to cyclic fretting.
- Interface/connection model: Nonuniform exponent-law pressure, Coulomb shear capacity, Greenwood-Williamson microcontact compliance, and Archard wear.
- Reduced/equivalent model: One-dimensional continuum elastic-beam microslip model with an equivalent thin interfacial layer.
- Normal/contact pressure role: Preload sets a nonuniform pressure field and Coulomb capacity; cyclic wear reduces pressure in the slip region while the stuck region retains initial pressure.
- Friction law/capacity: Constant-coefficient Coulomb friction combined with pressure- and roughness-dependent tangential stiffness.
- Stick-slip mechanism: The model predicts stuck length, slip length, microslip initiation, full slip, hysteresis, and wear localized to the slip region.
- Contact redistribution: Pressure redistribution evolves through wear-induced separation in the microslip region.
- Reference model: Published joint hysteresis data and direct plane-contact wear tests; no explicit three-dimensional interface-resolving model-form reference is supplied.
- Experimental validation: Published hysteresis experiments and new 60–120 N fretting-wear tests are used, but validation targets differ and independent validation of the entire reduced model is not established.
- Quantitative error: Average relative wear-depth error of 13.54% and hysteresis displacement/energy comparisons are reported.
- Criterion: Minimum force for microslip and maximum force for full slip are physical thresholds.
- Criterion type: physical_transition
- Declared tolerance: None; 13.54% is a reported prediction error.
- Validity domain: One-dimensional metal lap contact with elastic GW asperities, constant friction, prescribed pressure shape, and cyclic fretting.
- Breakdown boundary: No tolerance-defined reduced-versus-full breakdown boundary; elastoplastic asperities, debris, and multidirectional behavior are excluded.
- Transferability: partial
- Proves: A reduced continuum/equivalent-layer model can connect nonuniform preload, Coulomb capacity, stick-slip extent, evolving pressure, and experimentally measured wear or hysteresis.
- Does not prove: It does not provide a multilayer bending discrete reference, predeclared model-form tolerance, or experimentally validated vacuum-pressure breakdown boundary.

**Governing parameters:**
- preload
- pressure-distribution exponent
- surface roughness
- tangential force
- cycle count
- friction coefficient

### fb057ab3b2 — Theoretical, experimental, and numerical simulation studies on interface slip in steel-concrete composite continuous beams with high-strength bolted connectors

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: Steel-concrete composite beams connected by preloaded high-strength bolts under static bending.
- Interface/connection model: Uniformly distributed linear-elastic bolt shear stiffness relating interface shear to slip.
- Reduced/equivalent model: Analytical second-order interface-slip equation and slip-induced deflection correction.
- Normal/contact pressure role: Bolt preload is specified, but it does not explicitly drive a Coulomb stick-slip capacity in the analytical law.
- Friction law/capacity: The evidence describes linear connector stiffness rather than a pressure-dependent Coulomb friction law.
- Stick-slip mechanism: Continuous elastic slip is predicted; stick, partial slip, and gross slip are not resolved.
- Contact redistribution: No evolving normal-contact redistribution in the analytical model.
- Reference model: Three-dimensional Abaqus model with bolts, concrete damage, and steel plasticity.
- Experimental validation: One inverted simply supported beam test validates overall structural behavior; analytical service-stage slip comparisons are principally against FEA.
- Quantitative error: Peak slip differences of 2.03–2.09% and deflection errors of 0.773–2.714% versus FEA are reported; ignoring slip gives much larger errors.
- Criterion: No predeclared acceptance criterion; reported percentages compare analytical and numerical outputs.
- Criterion type: none
- Declared tolerance: None.
- Validity domain: Elastic service-stage steel-concrete composite response with uniformly distributed linear bolt connectors.
- Breakdown boundary: Cracking, yielding, and failure stages are observed physically, but they are not linked to failure of the reduced model under a declared tolerance.
- Transferability: weak
- Proves: A reduced slip-inclusive beam equation can substantially improve deflection and slip predictions against a detailed model.
- Does not prove: It does not supply pressure-dependent Coulomb slip evolution, a multilayer frictional reference, or a tolerance-defined applicability map.

**Governing parameters:**
- bolt preload
- connector stiffness and spacing
- load magnitude and distribution
- span position

### 20cee2210a — A novel frictional contact correction transfer matrix method for bolted vibration systems: modeling, simulation, and experimental validation

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: Preloaded bolted beam-like assemblies under piezoelectrically excited vibration.
- Interface/connection model: An equivalent angular frictional-contact correction represents interface compliance and lifting; tangential microslip is omitted.
- Reduced/equivalent model: Named Frictional Contact Correction Transfer Matrix Method.
- Normal/contact pressure role: Torque is calibrated to preload and a first-slip friction coefficient is measured, but detailed pressure-dependent tangential mechanics are not included in the reduced state equations.
- Friction law/capacity: Static frictional contact is represented through a correction coefficient rather than explicit evolving Coulomb partial slip.
- Stick-slip mechanism: Local tangential microslip and partial slip are explicitly neglected.
- Contact redistribution: Interface separation/compliance is represented in aggregate; spatial pressure redistribution is not resolved.
- Reference model: Frictional-contact finite elements, bonded finite elements, other transfer-matrix variants, and modal experiments.
- Experimental validation: Three physical assemblies are tested with scanning laser vibrometry; friction and torque-preload are separately characterized.
- Quantitative error: First-mode errors of about 1.27–3.07% and second-mode errors up to -13.21% are reported, with speedups of 117–601 times.
- Criterion: A 3% finite-element mesh-sensitivity criterion and iterative convergence tolerances are used; higher-mode overcorrection is observed.
- Criterion type: numerical_convergence
- Declared tolerance: The 3% and iteration tolerances govern numerical convergence, not physical model-form acceptance.
- Validity domain: Small-motion bending-dominated vibration of the three tested bolted configurations, chiefly the first mode.
- Breakdown boundary: Second-mode overcorrection demonstrates output-dependent deterioration, but no predeclared tolerance boundary over preload or contact state is constructed.
- Transferability: weak
- Proves: A low-order contact-correction model can match first-mode experiments and contact FEM while failing more strongly in another mode.
- Does not prove: It does not model multilayer Coulomb stick-slip, quasi-static planar bending, vacuum-pressure coupling, or a tolerance-defined breakdown map.

**Governing parameters:**
- correction coefficient
- bolt preload
- measured friction coefficient
- mode number
- system configuration
- iteration tolerance

### 02d3360815 — Stick-slip friction model for soft-hard joints under preload degradation

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Precompressed soft-hard damping interfaces under cyclic tangential shear with viscoelastic preload decay.
- Interface/connection model: Uniform parallel-plate contact with a physics-informed algebraic hysteretic law and a differential Jenkins/Iwan comparator.
- Reduced/equivalent model: Closed-form algebraic stick-slip friction model for harmonic loading.
- Normal/contact pressure role: Normal pressure enters the dynamic friction scaling and evolves through viscoelastic relaxation; hysteresis evolution is predicted without recalibration.
- Friction law/capacity: Pressure-, velocity-, roughness-, adhesion-, and viscoelasticity-dependent friction with power-law slip-area evolution and Masing-type cyclic mapping.
- Stick-slip mechanism: Local microslip grows to global macroslip at a critical displacement, with stiffness softening and later friction-induced stiffening.
- Contact redistribution: A uniform nominal pressure is used; spatial redistribution among multiple layers is absent.
- Reference model: A 15-element differential Jenkins/Iwan model and experimental rubber/granite and silicone-foam/steel data.
- Experimental validation: Published steady sliding data and cyclic foam experiments across pressure, velocity, and frequency; some reduced parameters remain empirically fitted.
- Quantitative error: Algebraic-versus-differential amplitude error is below 0.5%; experimental loop-area error is within 3.3%.
- Criterion: Critical displacement defines macroslip; reported 0.5% and 3.3% errors quantify performance but are not declared acceptance limits.
- Criterion type: physical_transition
- Declared tolerance: None demonstrated as a predeclared model-form acceptance tolerance.
- Validity domain: Soft-hard, one-dimensional tangential contact under steady sliding or symmetric harmonic loading with constant or slowly degrading compression.
- Breakdown boundary: General loading, strong adhesion-edge effects, high-speed thermal damage, wear, and multiaxial contact require additional mechanics; no tolerance-defined failure boundary is validated.
- Transferability: partial
- Proves: A compact reduced friction model can couple preload degradation to micro-to-macro slip and reproduce soft-interface hysteresis experimentally.
- Does not prove: It does not model a bending multilayer stack, compare continuum and full-layer contact models, or validate a vacuum-pressure-dependent breakdown boundary.

**Governing parameters:**
- normal pressure and its decay
- critical lateral displacement
- slip-area exponent
- velocity
- frequency
- roughness
- adhesion energy
- viscoelastic modulus

### ca46dc062d — The global-local mechanical behaviors of multilayered structure and applications to superconducting coils

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Large stacks of dry contacting plates and wound superconducting tapes under bending or electromagnetic loading.
- Interface/connection model: Negligible-gap adjacent-shell contact with Coulomb friction formulated as an internal yield condition and homogenized into continuum shear/internal forces.
- Reduced/equivalent model: Named continuum theory for multilayered structures with continuous through-stack interpolation, modified strain kinematics, and homogenized contact/friction.
- Normal/contact pressure role: Local normal contact stress enters Coulomb capacity through the yield condition; applied loading generates the contact field, but vacuum pressure is not separately modeled or swept.
- Friction law/capacity: Coulomb yield function with maximum dissipation and associative-flow-style update.
- Stick-slip mechanism: Stick and slip produce path-dependent frictional dissipation and stiffness enhancement; explicit gross-slip boundary mapping is not reported.
- Contact redistribution: Normal stress and homogenized friction are fields in the continuum and discrete reference, but separation is prohibited by the negligible-gap assumption.
- Reference model: Penalty-based discrete contact model with individual layers, supplemented by multilayer bending and coil experiments.
- Experimental validation: Force-displacement response for 35-, 50-, and 70-layer plate stacks and hoop strain for a five-turn coil are reproduced; experiments support response predictions but do not sample both sides of the derived 5% breakdown boundary.
- Quantitative error: For 30 layers at 27 degrees, out-of-plane and in-plane displacement errors are about 3% and 6%. A 5% maximum-displacement threshold gives permissible rotations of about 20 degrees for 30 layers and 7.5 degrees for 150 layers.
- Criterion: A 5% maximum displacement-error threshold against the discrete contact model defines layer-count-dependent permissible rotation limits.
- Criterion type: model_validity
- Declared tolerance: 5% maximum displacement error relative to the discrete contact model.
- Validity domain: Quasi-static axisymmetric or two-dimensional multilayer deformation with negligible gaps, moderate rotations, and friction not dominant enough to violate Kirchhoff-Love kinematics; the mapped rotation limit decreases with layer count.
- Breakdown boundary: Numerically established 5% error-crossing boundaries include about 20 degrees at n=30 and 7.5 degrees at n=150. The supplied experiments validate responses within selected cases but do not experimentally validate the boundary crossing itself.
- Transferability: partial
- Proves: Frictional multilayer homogenization can be compared quantitatively with discrete contact, classified by an explicit error tolerance, swept over layer count and deformation, and checked against multilayer bending experiments.
- Does not prove: It does not show that vacuum-generated and spatially evolving normal contact satisfies the zero-gap assumptions, sweep vacuum pressure, independently validate the tolerance-crossing breakdown boundary, or cover regimes where friction becomes dominant or layers separate.

**Governing parameters:**
- layer count n
- friction coefficient
- normal contact stress
- rotation or deformation amplitude
- applied pressure or electromagnetic load
- zero-gap and Kirchhoff-Love assumptions

## Surviving gap

The generic method has largely been occupied: frictional multilayer continuum theories, discrete-contact comparators, layer-count sweeps, quantitative output error, and even a declared 5% applicability boundary already exist. P1 survives only if it demonstrates a vacuum-specific failure mechanism or transfer limit that these frameworks do not already resolve. The required contribution is an independently validated, output-specific tolerance boundary showing how vacuum pressure generates and redistributes normal contact across many flat layers and how that field changes Coulomb capacity and stick/partial-slip/gross-slip during quasi-static planar bending. The boundary must test assumptions already exposed as fragile in the corpus—negligible gap, prescribed or constant pressure, friction remaining nondominant, and calibration of contact parameters—and experiments must sample accepted and rejected sides of the boundary rather than merely agree with the model at selected conditions.

## C04 decision

- **C04 search needed:** True
- A narrow C04 is justified by two specific unresolved threats, not by a generic demand for more literature. First, DOI 10.1061/JSENDH.STENG-13096 remains unavailable despite being previously identified as high threat and must be obtained and audited. Second, ca46dc062d reveals a precise forward-citation family to test: frictional multilayer continuum-versus-discrete studies that experimentally validate an explicit tolerance-crossing boundary while varying externally imposed normal pressure or preload and permitting contact opening/redistribution. Search should be limited to that family and forward citations of ca46dc062d and the flexible-pipe reduced-contact work.

## Recommended next action

Run a tightly scoped C04 retrieval and forward-citation audit for DOI 10.1061/JSENDH.STENG-13096 and for successors to ca46dc062d that combine pressure/preload sweeps, frictional multilayer homogenization, discrete contact, declared error tolerance, and experimental validation of the boundary. In parallel, preregister P1's exact reduced model, full-layer reference, calibration/validation split, outputs, tolerances, and test points on both sides of the predicted boundary; explicitly include vacuum-to-contact-pressure mapping, possible layer separation, and pressure redistribution.

## Evidence provenance

- `outputs/verification/D1-V005/C02_ADVERSARIAL_AUDIT.json` — PRIOR_C02_ADVERSARIAL_RESULT — `8f443316487072f5a1233089c72cca5b86bfa302bce49571ac82539cfe7c367a`
- `outputs/verification/D1-V006/verification_matrix.json` — CURRENT_C03_MATRIX — `97816a1f23cc73ec22dcf005387e6f79c337778a83c3086f959a9b553a4542df`
- `data/evidence/2014-The existence of a critical length scale in regularised friction_7c3aac183e.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `dabcbd09f5caeec4b75fc8fd206391e923427f1300b644c8fad0cc1200565d03`
- `data/evidence/2015-Transition from stick to slip in Hertzian contact with_ac9973e89e.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `7b18bcb0e5bf25b218744ab961cad31ad2f38ddc6e2c8be5c01fe2196466a842`
- `data/evidence/2016-Friction Characteristics of CFRP Plates in Contact with_79d1adc34c.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `c0a7e4971f7a1d2a30e2560714fdc77aeb0295bdd4facad2fa7cb7a9af16029f`
- `data/evidence/2021-A full layered numerical model for predicting hysteretic behavior of unbonded flexible pipes considering initial contact pressure_afe2a3a310.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `5ff2b58b0763a999244a3f169575d083d976a370cd0b7155f68151338e889ad3`
- `data/evidence/2021-Experimental validation of the applicability of effective spring boundary conditions for modelling damaged interfaces in laminate structures_444793969c.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `202cfbfc61d6c36d3fbac3f48c37e8734e3bc7b0cefaa2670b4a946988db3afd`
- `data/evidence/2022-A barrier method for frictional contact on embedded interfaces_202fd05d8f.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `bee1f2e34e22c631767fde5777508b104b0d39e44fa35b8c637a1fed1b48b6ab`
- `data/evidence/2022-A novel helix contact model for predicting hysteretic behavior of unbonded flexible pipes_a300a3b714.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `f70e5e1c24828e03650bc444f4562ba32cc54d5459c2054cd8fb159a100c1b7a`
- `data/evidence/2023-A Single-Variable Zigzag Approach to Model Imperfect Interfaces in Layered Beams_a9cd14eca9.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `b8886c67e49886b7c8e406bf32445091ad918a9e28957aad9c9eefb001f99325`
- `data/evidence/2023-Modelling tangential friction considering contact pressure distribution of rough surfaces_8ce1db3bca.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `4a08eee6e3ec5bfa4586674ce82b447c7aa05ff5678350d4678bd200440a660f`
- `data/evidence/2024-Messina-A_novel_friction_model_for_steel-polymer_interfaces_13e407003a.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `c19d9d3629f955565021fc5bba829be560a4d46b98c4cda5318058d72d9a5928`
- `data/evidence/2024-Modeling of Stick-Slip Contact Mechanics Based on Improved Continuous-Scale Fractal-Discrete Iwan Model_8daa38176d.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `2e2f7d31236896bd11bcc04933e0318f869608af344abaff85963fb0a045e1cf`
- `data/evidence/2025-Fretting wear modeling of bolted joint interface with microscopic roughness usin_7b85aadc84.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `588567280e85e964c2fb7330d6d51af0ab051a6e35c5a444539a6494bcbcb0f3`
- `data/evidence/2025-Theoretical, experimental, and numerical simulation studies on interface slip in steel-concrete_fb057ab3b2.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `2abab9bf794d3746678699fb66dc2daa7fa5bd2ad56da3ee0f62b3a7613dfe85`
- `data/evidence/2026-A novel frictional contact correction transfer matrix method for bolted vibration systems_20cee2210a.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `bf53944f8e7314af0e8d48b0388c29afeae58699e517c553a2f8eb5800a8e9ed`
- `data/evidence/2026-Stick-slip friction model for soft-hard joints under preload degradation_02d3360815.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `6b243d846091c460ff42a7835cb2539e42c61d3d37bccc0ea034bcae513d8dd2`
- `data/evidence/2026-The global-local mechanical behaviors of multilayered structure and_ca46dc062d.json` — CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE — `850139a1a6dcc0c34d2c8c9aff56d3c4881121b929e015435f7bc2a87d7cbad3`
