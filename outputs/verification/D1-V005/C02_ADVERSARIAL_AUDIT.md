# D1-V005 C02 Adversarial Audit

- **Status:** SUBSTANTIALLY_NARROWED
- **Confidence:** high
- **Evidence bundle SHA256:** `4c9e286670a9bb372860a1e847336c3548d272b752244ce9aba0457cd494906e`
- **Final project novelty verdict allowed:** False

## Current P1

For one specified continuum or homogenized vacuum-layer-jamming beam model under quasi-static planar bending, establish an output-specific, predeclared-tolerance validity and breakdown map against an interface-resolving reference and independently calibrated experiments, restricted to pressure-dependent Coulomb coupling and contact variables not reducible to established linear partial-interaction parameters, effective-EI approximations, connector-discreteness rules, or numerical-locking criteria.

## Executive summary

C02 does not falsify P1. It does, however, remove broad claims around interaction parameters, effective bending stiffness, exact-versus-approximate benchmarking, criteria for neglecting partial interaction, and connector-discreteness effects. Faella et al. (2002) provide the closest model-validity rule: an alpha*L–omega boundary with g1*=0.95 for neglecting partial interaction, associated with less than 7% deflection change and only a few-percent moment-redistribution change. Sonoda (2013) adds a finite connector-count sweep against a rigorous discrete solution and a degree-of-imperfection rule for approximating complete interaction. Neither establishes a predeclared model-form error tolerance that classifies a continuum-versus-discrete parameter space, and neither transfers to vacuum-pressure-dependent Coulomb friction without materially new constitutive/contact mechanics. The corpus also contains a declared 2% tolerance, but it governs FEM/FDM spatial convergence only. Thus the complete transferable kill condition fails, while P1 must be narrowed to pressure/contact coupling, output-specific preregistered tolerances, and independently validated breakdown boundaries.

## Kill test

- **named_reduced_or_equivalent_model:** True
- **interface_resolving_or_exact_reference:** True
- **governing_interaction_parameter:** True
- **quantitative_model_form_error:** True
- **finite_parameter_or_discreteness_sweep:** True
- **predeclared_acceptance_tolerance:** False
- **tolerance_defined_validity_domain:** False
- **validated_breakdown_boundary:** False
- **transferable_to_pressure_dependent_friction_without_new_mechanics:** False
- **kill_condition_met:** False

The corpus collectively supplies named reduced models, exact partial-interaction solutions, discrete connector references, interaction parameters, quantitative output-specific errors, large parameter sweeps, and a finite connector-count sweep. Faella et al. and Sonoda provide genuine model-validity criteria, while Gara et al. provide a genuine predeclared 2% tolerance only for numerical convergence. No supplied source predeclares a physical model-form error tolerance and uses it to classify a continuum-versus-interface parameter domain with a validated breakdown boundary. All closest frameworks use continuous linear springs, discrete mechanical connectors, or adhesive layers; pressure-dependent Coulomb capacity, evolving normal contact, stick–slip, and vacuum calibration require materially new mechanics.

## High-threat criterion audit

### Adekola (1974), paper_id 8a6d33e527

- Criterion: Practical full interaction from stiffness/stress saturation around ks=0.015Es to 0.04Es.
- Type: **design_rule**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: True
- Transferability: weak
- Assessment: This is a practical saturation rule for treating interaction as effectively full. It is not derived from a predeclared reduced-versus-reference error tolerance and does not address finite interface discreteness.

### Wright (1990), paper_id 99721ae369

- Criterion: Minimum degree of shear connection around the code value of 50%.
- Type: **design_rule**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: True
- Transferability: weak
- Assessment: The threshold regulates structural connection provision and capacity; it is not a continuum-model breakdown boundary.

### Faella, Martinelli, and Nigro (2002), paper_id d0699583ac

- Criterion: An alpha*L–omega boundary using g1*=0.95 for neglecting partial interaction, associated with less than 7% deflection effect and only a few-percent moment-redistribution effect.
- Type: **model_validity**
- Predeclared tolerance based: False
- Model-form validity boundary: True
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: This is C02’s closest model-validity criterion because it explicitly decides when a simpler full-interaction representation may replace the partial-interaction model. The evidence does not show that 7% was predeclared as the acceptance tolerance, and the boundary assumes continuous linear connection rather than discrete frictional contact.

### Gara, Ranzi, and Leoni (2006), paper_id a577a30ffd

- Criterion: Relative numerical error below 2% against an exact closed-form solution.
- Type: **numerical_convergence**
- Predeclared tolerance based: True
- Model-form validity boundary: False
- Only numerical/design criterion: True
- Transferability: weak
- Assessment: The 2% criterion is explicitly used to select FEM element or FDM grid density. It validates spatial discretization, not the physical partial-interaction model or a homogenized interface law.

### Schnabl et al. (2007), paper_id f5bba53ef2

- Criterion: Slenderness, E/G, and K ranges for deciding whether transverse shear deformation can be neglected.
- Type: **model_validity**
- Predeclared tolerance based: False
- Model-form validity boundary: True
- Only numerical/design criterion: False
- Transferability: weak
- Assessment: The ranges expose an output-sensitive beam-theory validity problem but are based on reported percentage differences, not a declared acceptance tolerance, and concern member shear rather than frictional interface homogenization.

### Girhammar and Pan (2007), paper_id eeb0863c0d

- Criterion: Use of classical clamped-pinned buckling coefficient with at most 2.5% safe-side buckling-load deviation.
- Type: **design_rule**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: True
- Transferability: weak
- Assessment: The approximation is justified by a bounded, conservative design error, but the 2.5% value is not shown to be a predeclared acceptance threshold and does not classify EIeff validity for frictional layers.

### Ranzi (2008), paper_id 2ad029e62c

- Criterion: High-stiffness locking of the 10-dof element and recommendation of the 13-dof element.
- Type: **numerical_convergence**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: True
- Transferability: weak
- Assessment: This separates numerically locked and locking-free finite elements. It cannot be interpreted as physical continuum breakdown.

### Girhammar (2009), paper_id aa091ea74d

- Criterion: Reported generally-below-5% global-output error and larger 10–20% interface-output error for the effective-EI method.
- Type: **unclear**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: The paper uses acceptability language but supplies no explicit tolerance-crossing parameter boundary. The evidence is still important because it demonstrates that validity depends on the chosen output.

### Sonoda (2013), paper_id f8e8c7b1a4

- Criterion: RFmu below 5%, approximately beta*mu=20 for central loading or 6 for uniform loading, for minimally erroneous complete-interaction deformation.
- Type: **model_validity**
- Predeclared tolerance based: False
- Model-form validity boundary: True
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: This is a genuine criterion for neglecting incomplete interaction and is supported by a connector-count sweep against a rigorous discrete solution. RFmu=5% is an interaction threshold, however, not a predeclared prediction-error tolerance, and the model uses two layers with linear connectors.

### Sousa (2013), paper_id c9bf5cb21f

- Criterion: Exact-element freedom from slip, curvature, and shear locking at very high alpha*L.
- Type: **numerical_convergence**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: True
- Transferability: partial
- Assessment: The result provides a suitable numerical reference strategy but no physical acceptance or breakdown criterion.

### Atashipour et al. (2025), paper_id 8a4d5de33a

- Criterion: Interaction level and G* identify conditions where EBPC errors become severe and TEPC remains accurate.
- Type: **none**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: False
- Transferability: partial
- Assessment: The paper supplies strong regime-partitioning parameters and reported errors up to about 92%, but it does not convert them into a declared-tolerance accept/reject boundary.

### Atashipour et al. (2026), paper_id 71c8d5e2c7

- Criterion: The n→infinity, k=k* limit recovers HSDT behavior, while k=0 and perfect bonding define response limits.
- Type: **none**
- Predeclared tolerance based: False
- Model-form validity boundary: False
- Only numerical/design criterion: False
- Transferability: weak
- Assessment: These are asymptotic and physical limiting results, not tolerance-based validity criteria.

## Strongest threats

### Faella, Martinelli, and Nigro (2002), paper_id d0699583ac

- Threat: **high**
- Why it matters: It directly converts alpha*L and omega into a criterion for when partial interaction may be neglected and ties the criterion to bounded changes in deflection and moment redistribution.
- Remaining gap: The reported 7% effect is not established as a predeclared acceptance tolerance, the reference remains a continuous linear partial-interaction model, and transfer to pressure-dependent friction is absent.

### Sonoda (2013), paper_id f8e8c7b1a4

- Threat: **high**
- Why it matters: It compares continuous and discrete connection models over n=3–1000, quantifies deterioration at small connector counts, and provides an RFmu criterion for approximating complete interaction.
- Remaining gap: RFmu is an interaction threshold rather than a declared prediction-error tolerance; the system has two layers, linear discrete connectors, no Coulomb law, and no vacuum-pressure coupling.

### Girhammar and Pan (2007) plus Girhammar (2009), paper_ids eeb0863c0d and aa091ea74d

- Threat: **high**
- Why it matters: Together they provide named effective-EI approximations, exact analytical references, interaction parameters, multiple boundary conditions, and sharply output-dependent model-form errors.
- Remaining gap: They do not classify parameter space by a predeclared tolerance, do not resolve finite frictional interfaces, and exclude pressure-dependent contact.

### Atashipour et al. (2025), paper_id 8a4d5de33a

- Threat: **high**
- Why it matters: It extends partial-composite theory to arbitrary N, supplies explicit interaction and shear parameters, compares two reduced beam theories, and validates against 3-D FEA and published experiments.
- Remaining gap: The problem is buckling and vibration with linear shear springs; no predeclared validity boundary, quasi-static bending map, Coulomb stick–slip, or vacuum-pressure coupling is provided.

### Gara, Ranzi, and Leoni (2006), paper_id a577a30ffd

- Threat: **high**
- Why it matters: It demonstrates exactly how a declared 2% tolerance generates an output-specific resolution map and identifies a formulation that remains unacceptable even after heavy refinement.
- Remaining gap: The tolerance controls numerical convergence only and therefore cannot satisfy the physical model-form kill condition.

### Wright (1990), paper_id 99721ae369

- Threat: **high**
- Why it matters: Experiments show that discrete nonlinear connector behavior and confinement can invalidate a continuously smeared, independently calibrated connection law in bending.
- Remaining gap: No declared-error validity map is constructed, and stud dowel/confinement mechanics do not transfer directly to vacuum-clamped frictional sheets.

## Paper-by-paper audit

### 8a6d33e527 — THE DEPENDENCE OF SHEAR LAG ON PARTIAL INTERACTION IN COMPOSITE BEAMS

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: A steel–concrete composite slab-beam system exhibiting both shear lag and partial interaction.
- Interface/connection model: A continuous, linear connector law with interface shear governed by constant shear-connector stiffness modulus ks.
- Reduced/equivalent model: A transformed-section representation using stress- or deflection-based effective width; the coupled Fourier-series shear-lag/partial-interaction solution is the more complete comparator.
- Quantitative error: The transformed-section bottom-flange stress is reported as more than 90% of the exact analytical value and slightly underestimates it. Deflection and stress approach saturation as ks increases, but no systematic model-form error surface is reported.
- Criterion: Practical full interaction is associated with stiffness saturation around ks=0.015Es to 0.04Es, despite theoretical full interaction requiring infinite ks.
- Criterion type: design_rule
- Declared tolerance: None. The stress ratio and saturation range are reported results, not a predeclared model-form acceptance tolerance.
- Validity domain: Linear-elastic, small-deflection steel–concrete composite beams with continuous linear connection, simply supported transverse edges, and the analyzed loading and aspect ratios.
- Breakdown boundary: No tolerance-defined breakdown boundary. The practical-full-interaction range is a saturation/design approximation rather than a validated reduced-model rejection boundary.
- Transferability: weak
- Proves: Interaction stiffness can organize the transition toward practically saturated composite stiffness, and an equivalent transformed section can be checked against a more complete shear-lag solution.
- Does not prove: It does not classify continuum-versus-discrete validity under a declared error tolerance or represent pressure-dependent Coulomb friction, finite sheet count, or vacuum-jamming experiments.

**Governing parameters:**
- ks or 100ks/Es
- slab width-to-span ratio b/a
- load distribution
- normalized span coordinates

### 99721ae369 — The Deformation of Composite Beams with Discrete Flexible Connection

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Full-scale steel–concrete composite beams joined by discrete, nonlinear through-deck welded studs.
- Interface/connection model: A free-slip interface with discrete longitudinal stud reactions taken from empirical nonlinear push-off load–slip curves; continuous linear connection models are also examined as approximations.
- Reduced/equivalent model: Closed-form continuous-connection partial-interaction models, transformed-section engineering theory, and empirical degree-of-interaction modifications.
- Quantitative error: Continuous linear models are shown to underestimate working-load beam stiffness and overestimate maximum end slip; the nonlinear discrete folded-plate method better reproduces measured stiffness and slip redistribution. The supplied evidence gives no general scalar model-form error map.
- Criterion: A 50% minimum degree of shear connection is identified as a code/design threshold whose possible reduction is discussed.
- Criterion type: design_rule
- Declared tolerance: None supported for reduced-versus-discrete model-form error.
- Validity domain: The tested simply supported, four-point-loaded composite beams and associated stud/deck configurations; no tolerance-defined model-validity domain is established.
- Breakdown boundary: The failure of continuous linear connection assumptions for discrete nonlinear connectors is demonstrated qualitatively and experimentally, but no tolerance-crossing boundary in connector count or spacing is validated.
- Transferability: partial
- Proves: Discrete nonlinear connection, confinement, and in-situ loading can materially change stiffness and slip relative to a smeared linear connection calibrated in isolated tests.
- Does not prove: It does not provide a transferable acceptance rule for a homogenized vacuum-jamming model; stud dowel mechanics and confinement are not vacuum-pressure-dependent sheet friction.

**Governing parameters:**
- degree of shear connection
- connector secant stiffness
- connector spacing and position
- deck profile
- applied load

### a28d4f1668 — A Rational Model for the Degree of Interaction in Composite Beams with Flexible Shear Connectors

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: A simply supported steel–concrete composite beam with elastic components and perfectly plastic shear connectors at ultimate capacity.
- Interface/connection model: Uniformly distributed mechanical connectors transmitting perfectly plastic shear without vertical separation.
- Reduced/equivalent model: A closed-form degree-of-interaction representation relating curvature, slip, neutral-axis separation, and degree of shear connection.
- Quantitative error: No reduced-versus-exact or continuous-versus-discrete prediction-error study is supported. The paper derives response relations, including phi=eta/eta_fi.
- Criterion: Degrees of interaction and shear connection partition the physical amount of composite action, but no error-based model acceptance criterion is supplied.
- Criterion type: design_rule
- Declared tolerance: None supported.
- Validity domain: Linear-elastic beam components, fully plastic distributed connectors, simply supported geometry, and uniform loading at ultimate capacity.
- Breakdown boundary: The paper notes an illusory low-moment prediction caused by assuming fully plastic connectors, but does not validate a reduced-model breakdown boundary.
- Transferability: weak
- Proves: Degree of interaction is distinct from connector quantity or strength and can parameterize slip, curvature, and neutral-axis separation.
- Does not prove: It does not quantify model-form error, connector-discreteness error, or transfer the degree-of-interaction relation to pressure-dependent Coulomb interfaces.

**Governing parameters:**
- degree of interaction phi
- degree of shear connection eta
- full-interaction connection degree eta_fi
- connector strength per unit length
- applied moment

### d0699583ac — Steel and concrete composite beams with flexible shear connection: ‘‘exact’’ analytical expression of the stiffness matrix and applications

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Two-layer steel–concrete composite beams with a continuous flexible shear connection, including continuous members, creep, shrinkage, and simplified cracking cases.
- Interface/connection model: Continuous linear shear flow proportional to interface slip through stiffness k; discrete physical connectors are replaced by an assumed secant stiffness.
- Reduced/equivalent model: The full-interaction beam approximation and an exact Newmark-based displacement element; the neglect criterion is expressed through alpha*L, omega, and g1*.
- Quantitative error: For the stated g1*=0.95 boundary, neglecting partial interaction changes deflection by less than 7% and moment redistribution by only a few percent in the analyzed cases.
- Criterion: An analytical alpha*L–omega boundary with g1*=0.95 identifies cases where partial interaction may be neglected.
- Criterion type: model_validity
- Declared tolerance: The g1*=0.95 criterion is declared, but the supplied evidence does not establish that 7% was a predeclared prediction-error acceptance tolerance; 7% is reported as the resulting maximum deflection effect.
- Validity domain: Uniform, geometrically linear two-layer beams with continuous linear connection and the covered static, creep, shrinkage, and simplified cracking cases.
- Breakdown boundary: The criterion separates cases where a full-interaction approximation is considered usable from cases where partial interaction matters. It is not validated against discrete connectors or frictional contact and is not a vacuum-jamming breakdown boundary.
- Transferability: partial
- Proves: Partial-interaction literature already contains an interaction-parameter rule explicitly tied to the error incurred by neglecting slip.
- Does not prove: It does not supply a predeclared error-tolerance map against an interface-resolving reference or transfer to pressure-dependent Coulomb stick–slip without new mechanics.

**Governing parameters:**
- alpha*L
- omega=EIabs/EIfull
- connection stiffness k
- creep coefficient
- sectional cracking state

### a577a30ffd — Time analysis of composite beams with partial interaction using available modelling techniques: A comparative study

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: Steel–concrete composite beams with linear partial interaction and time-dependent concrete creep.
- Interface/connection model: A continuous linear-elastic connection with shear flow proportional to slip.
- Reduced/equivalent model: Eight- and ten-degree-of-freedom displacement finite elements, finite differences, and a direct stiffness method compared with an exact closed-form solution.
- Quantitative error: A declared 2% relative-error target is used to determine required spatial discretization. The 10-dof element needs 4 to 30 elements depending on output; the FDM needs 9 points for curvature and 31 for localized end slip at high stiffness; the 8-dof element fails to reach 2% curvature error even with 100 elements.
- Criterion: A 2% numerical error criterion classifies mesh adequacy for each numerical formulation and response output.
- Criterion type: numerical_convergence
- Declared tolerance: 2%, explicitly for numerical discretization accuracy against the exact solution.
- Validity domain: Linear partial interaction with the specified beam systems, uniform meshes, instantaneous and AEMM creep analyses.
- Breakdown boundary: Mesh-size and formulation-specific convergence or failure boundaries are established, including nodal-jump behavior. They are numerical boundaries, not physical continuum-model breakdown boundaries.
- Transferability: weak
- Proves: A predeclared tolerance can generate an output-specific discretization map, and required resolution depends strongly on the response quantity and interaction stiffness.
- Does not prove: The 2% threshold does not validate a homogenized physical model, connector smearing, or transfer to vacuum-pressure-dependent friction.

**Governing parameters:**
- alpha*L
- mesh element or grid-point count
- boundary condition
- analysis time
- numerical interpolation order

### f5bba53ef2 — Analytical Solution of Two-Layer Beam Taking into account Interlayer Slip and Shear Deformation

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: A two-layer linear-elastic beam with both continuous interlayer slip and layer shear deformation.
- Interface/connection model: A continuous constant slip modulus K, with no friction, opening, or discrete connectors.
- Reduced/equivalent model: Euler–Bernoulli and Eurocode-type approximations are compared with an exact Timoshenko partial-interaction solution.
- Quantitative error: Reported differences include shear contributions from 0.3% to more than 250%, Eurocode-versus-beam discrepancies up to 22.5% in the intermediate-K range, and stress differences up to 25%.
- Criterion: Ranges of L/h, E/G, and K are used to state when shear deformation is small or significant, including generally negligible effects for many slender isotropic beams.
- Criterion type: model_validity
- Declared tolerance: None. The percentage differences used to describe significance are reported results rather than a predeclared acceptance tolerance.
- Validity domain: Small-displacement, linear-elastic, simply supported two-layer beams under uniform loading with continuous constant K and no separation.
- Breakdown boundary: Short/thick, high-E/G, and stiff-connection cases show major failure of shear-rigid approximations, but no tolerance-defined accept/reject surface is supplied.
- Transferability: weak
- Proves: Interaction stiffness alone is insufficient to judge a reduced beam theory; slenderness, material shear flexibility, and output choice can dominate approximation error.
- Does not prove: It does not address connector discreteness, Coulomb friction, pressure-dependent contact, high layer count, or a predeclared vacuum-jamming validity boundary.

**Governing parameters:**
- L/h
- K
- E/G
- layer-depth ratio

### eeb0863c0d — Exact static analysis of partially composite beams and beam-columns

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Two-component partially composite beams and beam-columns under transverse and axial loading.
- Interface/connection model: Discrete physical connectors are smeared into a continuous linear-elastic slip modulus K; friction and uplift are neglected.
- Reduced/equivalent model: A generalized effective bending stiffness EIeff and classical buckling-coefficient approximations are benchmarked against exact sixth-order partial-interaction solutions.
- Quantitative error: EIeff gives about 0.4% deflection error and 2.9% moment error in evaluated cases but about 15.1% error for differentiated shear or slip forces. A classical clamped-pinned buckling coefficient gives at most 2.5% safe-side buckling-load deviation.
- Criterion: No formal tolerance-based acceptance criterion for EIeff is supplied; the clamped-pinned classical coefficient is justified as a safe engineering approximation by its bounded deviation.
- Criterion type: design_rule
- Declared tolerance: None supported as a predeclared model-form acceptance tolerance.
- Validity domain: Uniform, linear-elastic, small-deflection beam-columns with continuous K, no friction or uplift, and the analyzed Euler boundary conditions.
- Breakdown boundary: Output-dependent loss of EIeff accuracy is demonstrated, especially for slip and shear, but no tolerance-crossing interaction boundary is mapped.
- Transferability: partial
- Proves: An effective-EI approximation can be highly accurate for global outputs while remaining poor for interface-sensitive outputs, even under the same interaction parameter.
- Does not prove: It does not validate smearing of finite connectors or frictional sheets under a predeclared tolerance and does not include vacuum-pressure coupling.

**Governing parameters:**
- alpha*L
- EI0/EIinfinity
- K
- boundary condition
- axial-load ratio
- loading distribution

### d87b4ad44d — Composite beam–columns with interlayer slip—Approximate analysis

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Partially composite beam-columns with continuous elastic connection under combined axial compression and transverse loading.
- Interface/connection model: Uniformly distributed linear-elastic slip force with constant K representing evenly spaced fasteners.
- Reduced/equivalent model: An effective-EI and magnification-factor approximation compared with exact first- and second-order partial-interaction solutions.
- Quantitative error: For simply supported cases, errors are below 0.2% for deflection, 0.5% for moment, 1.2% for axial force, and 1.4% for shear. Slip-force error falls from about 9% to 1.3% when the deflection magnification factor is used.
- Criterion: The approximation is recommended for simply supported members with connection stiffness of structural significance, but the supplied evidence gives no numerical parameter boundary defining that phrase.
- Criterion type: unclear
- Declared tolerance: None supported. The reported error maxima are not identified as predeclared acceptance tolerances.
- Validity domain: Primarily simply supported, linear-elastic beam-columns over the evaluated practical interaction and load ranges; other supports and asymmetric cases require re-evaluation.
- Breakdown boundary: Deterioration for very flexible connections, applied end moments, and asymmetric loading is identified without a tolerance-defined locus.
- Transferability: weak
- Proves: A named effective-stiffness approximation can have small, output-dependent error against an exact partial-interaction solution over practical parameter ranges.
- Does not prove: It does not provide a declared accept/reject map, a discrete-interface reference, or pressure-dependent frictional transfer.

**Governing parameters:**
- alpha*L
- EI0/EIN
- P/Pcr
- boundary condition
- loading distribution

### 2ad029e62c — Locking problems in the partial interaction analysis of multi-layered composite beams

- Evidence: VERIFIED_FULL_TEXT
- Threat: **medium**
- Physical analogue: Three-layer composite beams with continuous linear partial interaction.
- Interface/connection model: Continuous linear-elastic shear flow proportional to interface slip, with no layer separation.
- Reduced/equivalent model: Ten-dof and thirteen-dof displacement finite elements based on different axial interpolation orders.
- Quantitative error: The 10-dof element becomes artificially stiff and gives severe slip and moment errors at gamma_j*L=50; the 13-dof element remains accurate with four elements relative to a refined 50-element solution. No scalar tolerance is supplied.
- Criterion: High connection rigidity exposes curvature locking in the low-order element; parabolic axial interpolation removes the locking mechanism.
- Criterion type: numerical_convergence
- Declared tolerance: None supported.
- Validity domain: Linear-elastic three-layer Euler–Bernoulli beams under uniform loading for the tested supports, interaction levels, and meshes.
- Breakdown boundary: A numerical locking regime is demonstrated at high interface stiffness. It is a finite-element formulation boundary, not physical homogenization breakdown.
- Transferability: weak
- Proves: Apparent breakdown at strong interaction may be a numerical interpolation artifact and must be separated from physical model-form failure.
- Does not prove: It does not establish a physical continuum-versus-interface validity boundary or frictional vacuum-jamming transfer.

**Governing parameters:**
- gamma_j*L
- finite-element formulation
- mesh count
- boundary condition

### aa091ea74d — A simplified analysis method for composite beams with interlayer slip

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Two-layer beams joined by uniformly distributed mechanical fasteners with linear slip response.
- Interface/connection model: A continuous constant slip modulus K, or a static secant modulus, representing uniformly spaced fasteners.
- Reduced/equivalent model: A simplified effective composite bending stiffness EIeff based on the corresponding column buckling length, benchmarked against exact partial-composite beam solutions.
- Quantitative error: Deflection errors are generally below 5%; normal-stress errors are usually below 5%; some shear-stress errors reach about 11%; slip-force errors are about 14–18%; Eurocode errors reach roughly 27–30% in some clamped or propped cases.
- Criterion: The paper describes global-output agreement as acceptable and recommends sensitivity study before design use, but supplies no explicit parameter-space acceptance boundary.
- Criterion type: unclear
- Declared tolerance: None. The 5%, 10–20%, and related values are reported error levels, not shown to be predeclared acceptance tolerances.
- Validity domain: Two-layer, linear-elastic Euler–Bernoulli beams with constant K over the analyzed supports and load cases.
- Breakdown boundary: Higher errors for differentiated interface quantities, unsymmetric supports, and point-load discontinuities are documented without a tolerance-classified boundary.
- Transferability: partial
- Proves: Effective-EI approximations and exact partial-interaction solutions can be compared quantitatively across interaction level, supports, loads, and multiple outputs.
- Does not prove: It does not define a preregistered accept/reject boundary or validate the linear connector representation for pressure-dependent frictional sheets.

**Governing parameters:**
- alpha*L
- EI0/EIinfinity
- effective-length coefficient
- boundary condition
- load type
- fastener K and spacing

### 14958e37b2 — Analytical and numerical analysis of multilayered beams with interlayer slip

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Three- and four-layer beams with several continuously compliant slip interfaces.
- Interface/connection model: Zero-thickness interfaces with linear shear force Si=Ki si and no explored uplift.
- Reduced/equivalent model: A slip-based analytical multilayer formulation plus Euler–Bernoulli and Timoshenko beam/interface finite-element variants.
- Quantitative error: Finite-element slips and deflections are compared with closed-form solutions over 4, 8, and 20 elements. Linear axial interpolation locks at high connection stiffness, while quadratic interpolation converges without that failure; no common scalar tolerance is stated.
- Criterion: Quadratic or higher axial interpolation is required to avoid slip and curvature locking at high connection stiffness.
- Criterion type: numerical_convergence
- Declared tolerance: None supported.
- Validity domain: Small-displacement, linear-elastic, statically determinate multilayer beams with known shear-force distributions and zero transverse separation.
- Breakdown boundary: Locking of linear-interpolation interface elements at high stiffness is a numerical failure boundary, not a physical reduced-model boundary.
- Transferability: partial
- Proves: Multilayer slip equations, finite layer count, explicit zero-thickness interfaces, and interaction-stiffness sweeps are established tools; numerical locking must be controlled.
- Does not prove: It does not establish an error-tolerance map for homogenizing frictional sheets or incorporate vacuum-controlled Coulomb contact.

**Governing parameters:**
- layer count
- gamma_i*L or Ki
- beam kinematics
- mesh count
- interpolation order
- load type

### f8e8c7b1a4 — Analysis of Composite Beams with Incomplete Interaction I. Theoretical study of bending stiffness of two-layered composite beams

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: A simply supported two-layer timber-type composite beam with a finite number of equally spaced shear connectors.
- Interface/connection model: A rigorous discrete recurrence model with individual linear connectors, compared with Newmark’s continuous connection and a non-iterative approximation.
- Reduced/equivalent model: Newmark’s smeared partial-interaction theory, an improved Kamiya approximation, and the complete-interaction beam approximation.
- Quantitative error: The sweep covers beta*mu=0.1–25 and n=3–1000. Continuous/discrete discrepancies grow as n decreases. For RFmu below 5%, complete-interaction deformation has small error, including a reported 2.2% example. The approximate method gives deflection errors within a few percent and axial-force/slip errors around 10% for realistic cases up to RFmu about 40%.
- Criterion: RFmu<5%, corresponding approximately to beta*mu=20 for central load and 6 for uniform load, is proposed as a regime where complete-interaction deformation is minimally erroneous; connector-count dependence is explicitly evaluated.
- Criterion type: model_validity
- Declared tolerance: No predeclared prediction-error tolerance is supported. RFmu=5% is an interaction/imperfection threshold, while 2.2% and about 10% are reported errors.
- Validity domain: Linear-connector, symmetric, simply supported two-layer beams under central or uniform loading over the analyzed beta*mu and connector-count ranges.
- Breakdown boundary: Accuracy deteriorates for few connectors, high imperfection, and concentrated loading. These trends are mapped, but not converted into a declared-error accept/reject boundary.
- Transferability: partial
- Proves: Partial-interaction literature directly relates connector discreteness and an interaction parameter to error in smeared or complete-interaction approximations.
- Does not prove: It does not provide a tolerance-defined boundary for many frictional layers or show that RFmu transfers to pressure-dependent Coulomb coupling.

**Governing parameters:**
- beta*mu
- degree of imperfection RFmu
- connector count n
- connector stiffness K
- loading configuration

### c9bf5cb21f — Exact finite elements for multilayered composite beam-columns with partial interaction

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Three- to five-layer composite beams and beam-columns with multiple compliant interfaces.
- Interface/connection model: Continuous linear slip springs Ki between layers, with equal transverse displacement and no separation.
- Reduced/equivalent model: A flexibility-based exact multilayer finite element compared with conventional displacement-based Euler–Bernoulli and Timoshenko elements.
- Quantitative error: A single exact element is benchmarked against conventional elements over layer counts and stiffnesses up to alpha*L=383.246; conventional elements require refinement and may lock, whereas the exact element gives exact nodal solutions. No predeclared scalar error threshold is supplied.
- Criterion: Locking-free exact interpolation is recommended when high connection stiffness makes conventional elements unreliable.
- Criterion type: numerical_convergence
- Declared tolerance: None supported.
- Validity domain: Linear-elastic multilayer beams with linear connection, common transverse displacement and rotation, and the covered static load and support cases.
- Breakdown boundary: Slip, curvature, and shear locking of conventional finite elements at high stiffness is demonstrated, but it is not physical continuum breakdown.
- Transferability: partial
- Proves: An exact multilayer partial-interaction reference can eliminate mesh and locking error over large stiffness ranges and arbitrary layer count.
- Does not prove: It does not assess homogenization error, declare a physical tolerance boundary, or incorporate friction, normal pressure, or vacuum actuation.

**Governing parameters:**
- layer count
- Ki or alpha*L
- beam kinematics
- mesh count
- interpolation order
- boundary condition

### bdf95f0602 — Derivation of the exact stiffness matrix of shear-deformable multi-layered beam element in partial interaction

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Three- and four-layer shear-deformable beams with multiple compliant connections.
- Interface/connection model: Continuous linear shear connectors with stiffness ksc; discrete connectors are smeared and uplift is excluded.
- Reduced/equivalent model: An exact Timoshenko multilayer stiffness element, compared with shear-rigid Bernoulli models and prior exact formulations.
- Quantitative error: Sweeps cover ksc from 0.1 to 100000 MPa and L/H to 20. A four-layer benchmark gives 19.0288 versus 19.0306 kN·m and slip agreement within tenths of a percent. Deflection and slip ratios expose shear-rigid error, but no acceptance threshold is declared.
- Criterion: No formal accept/reject criterion; the shear-deformable/shear-rigid discrepancy approaches unity with increasing slenderness, while exact elements are reported mesh-independent and locking-free.
- Criterion type: none
- Declared tolerance: None supported.
- Validity domain: Geometrically linear, isotropic multilayer beams with continuous linear connections, common transverse displacement, and constant distributed loading per element.
- Breakdown boundary: Large shear-rigid discrepancies for low L/H and numerical ill-conditioning addressed by reformulation are shown, without a tolerance-defined model boundary.
- Transferability: partial
- Proves: Exact multilayer references can sweep interface stiffness, slenderness, and layer count while separating member-shear effects from interlayer slip.
- Does not prove: It does not establish a transferable physical acceptance rule for nonlinear frictional contact or independently validate such a rule experimentally.

**Governing parameters:**
- ksc
- L/H
- layer count
- Timoshenko versus Bernoulli kinematics
- element count
- boundary condition

### 8a4d5de33a — Flexible N-layer composite beam/column elements with interlayer partial interaction imperfection–A novel approach to structural stability and dynamic analyses

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Identical-layer composite beams and columns with linear interlayer slip, studied in buckling and vibration.
- Interface/connection model: Linear interfacial shear springs with slip modulus k; published experiments use discrete rubber, polyethylene, or nylon connectors.
- Reduced/equivalent model: Named Euler–Bernoulli partial-composite and Timoshenko/Engesser partial-composite models with explicit conversion coefficients.
- Quantitative error: The TEPC model agrees within 2% with five-layer 3-D FEA and within 1.4–7.8% with published three-layer vibration tests. EBPC error reaches about 92% for higher modes under full interaction. Sweeps include N up to 100 and varying interaction.
- Criterion: Interaction level and G* partition regimes of small or severe Euler–Bernoulli error, but no declared error tolerance converts the sweep into an accept/reject validity map.
- Criterion type: none
- Declared tolerance: None. The 2%, 7.8%, 92%, and 3.7% values are reported discrepancies, not predeclared acceptance limits.
- Validity domain: Identical, linear-elastic layers with linear slip springs, small motions, common transverse deflection and rotation, and the covered stability and vibration problems.
- Breakdown boundary: Severe EBPC failure at high interaction, low shear rigidity, and higher mode number is demonstrated, but no tolerance-crossing boundary is validated.
- Transferability: partial
- Proves: Modern N-layer theory already supplies named reduced models, interaction parameters, large layer-count sweeps, exact solutions, 3-D references, and experimental comparison.
- Does not prove: It does not address quasi-static planar bending validity, pressure-dependent friction, stick–slip, contact redistribution, or a predeclared physical model-form tolerance.

**Governing parameters:**
- layer count N
- dimensionless slip modulus
- dimensionless shear parameter G*
- effective length
- boundary condition
- vibration mode

### 71c8d5e2c7 — Laminated Partially-Composite Plate Theory (LPCPT)—An extension of the classical laminated plate theory for flexible n-layer plates with partial interlayer interaction

- Evidence: VERIFIED_FULL_TEXT
- Threat: **high**
- Physical analogue: Flexible multilayer plates bonded by soft adhesive films or represented by shear-slip imperfections.
- Interface/connection model: Linear-elastic interfacial shear springs with zero normal separation.
- Reduced/equivalent model: Named Laminated Partial-Composite Plate Theory with arbitrary-layer analytical solutions, compared with 3-D adhesive-layer finite elements and limiting HSDT behavior.
- Quantitative error: Analytical predictions are reported to agree strongly with 3-D FEA for four- and six-layer panels; zero interaction gives a 1/n² buckling-load factor relative to perfect bonding, and parameter sweeps show mode shifting. The supplied evidence gives no common scalar error tolerance.
- Criterion: The k=0 and perfect-bonding limits and the n→infinity, k=k* equivalence with HSDT are limiting-model results, not acceptance criteria.
- Criterion type: none
- Declared tolerance: None supported.
- Validity domain: Small-deformation, linear-elastic, specially orthotropic, simply supported plates with zero opening and the stated layer-symmetry requirements.
- Breakdown boundary: Mode shifts and sensitivity to interaction are physical response changes; extremely thick-plate and omitted-shear limitations are stated, but no tolerance-defined breakdown map is provided.
- Transferability: weak
- Proves: Layer count and interaction modulus can be handled analytically in an N-layer reduced theory and checked against a 3-D interface-material reference, including an asymptotic continuum connection.
- Does not prove: It does not treat beam bending, dry friction, vacuum-generated normal pressure, stick–slip, experiments, or a declared accept/reject boundary.

**Governing parameters:**
- layer count n
- dimensionless interlayer shear modulus k
- plate aspect ratio
- thickness-to-length ratio
- orthotropy
- mode and loading type

## Surviving gap

P1 cannot claim novelty from introducing an interaction parameter, effective EI, exact-versus-approximate error comparison, finite layer or connector sweep, criterion for neglecting partial interaction, or locking-free numerical reference. The residual question is whether one specified vacuum-layer-jamming continuum model can be assigned output-specific, predeclared acceptance tolerances and experimentally validated breakdown boundaries when vacuum pressure controls normal contact and hence Coulomb capacity, stick–slip evolution, and possibly contact redistribution. The scientific contribution must arise from that pressure/contact/friction coupling and its effect on transferability of established partial-interaction criteria, not from recreating those criteria with different geometry or materials.

## C03 decision

- **C03 search needed:** True
- C02 supplies close but incomplete model-validity rules. C03 should test whether shear-lag, imperfect-interface, cohesive-zone, or related adjacent mechanics already contains a predeclared-tolerance model-form validity boundary based on interaction or transfer length and whether any such framework includes normal-pressure-dependent Coulomb coupling. The search must continue to separate physical model validity from design limits, physical slip transitions, and numerical convergence.

## Recommended next action

Proceed to C03 with targeted searches for tolerance-defined shear-lag or imperfect-interface validity criteria, especially discrete-to-continuous transfer-length rules and pressure-dependent frictional interfaces. In parallel, preregister P1’s specific reduced model, reference model, calibrated parameters, response outputs, and separate acceptance tolerances before generating the validation map; do not treat the generic methodology as novel.

## Evidence provenance

- `outputs/verification/D1-V004/C01_ADVERSARIAL_AUDIT.json` — PRIOR_C01_ADVERSARIAL_RESULT — `f1e56ea84df8add3d5b280ad6d223cf9d0a6732cc4e59d76cd01c148cc1940ec`
- `outputs/verification/D1-V005/verification_matrix.json` — CURRENT_C02_MATRIX — `6e60ab14d04a49b9c73876327ba5c1b97ebd0b557e8a0eef441a0c72db300ba8`
- `data/evidence/1974-The dependence of shear lag on partial interaction in composite beams_8a6d33e527.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `0b6126f54086b40d089a4dfc0589f5b49abff50809c3037c888920a37c6aba12`
- `data/evidence/1990-The deformation of composite beams with discrete flexible connection_99721ae369.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `8e54b44d9b0889d77dcd362d634538311b4c41beec2365c752c82e409b5936ce`
- `data/evidence/1998-A rational model for the degree of interaction in composite beams with flexible shear connector_a28d4f1668.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `bc8e7b22df22f75f450517649b782a8bb76a78ddade94ef57226f0978cab990c`
- `data/evidence/2002-Steel and concrete composite beams with flexible_d0699583ac.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `2eff6465480631264ee5e68ea44642cf4c11d6ef625f671c574c59f0bad973a9`
- `data/evidence/2006-Time analysis of composite beams with partial interaction using available modelling techniques A comparative study_a577a30ffd.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `4015c9dddea2b4b318b0c9023e4b69109b0ead12a083a0887bf2f76f85f5a601`
- `data/evidence/2007-Analytical Solution of Two-Layer Beam Taking into account Interlayer Slip and Shear Deformation_f5bba53ef2.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `4889d5cb1eae40b22fff31478c03c69f68c52a826e6ed626eed0a56f72652520`
- `data/evidence/2007-Exact static analysis of partially composite beams and beam-columns_eeb0863c0d.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `33c63f0d7a9bbb0dc13933fdc8410bd7fb4a7d8289e5e273849f14aa611fb4df`
- `data/evidence/2008-Composite beam–columns with interlayer slip—Approximate analysis_d87b4ad44d.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `36e630e0cfd7b179f05f53c35a615210f1eb9cfc5c30f07c0b8beda77361e446`
- `data/evidence/2008-Locking problems in the partial interaction analysis of multi-layered_2ad029e62c.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `e059db178d6db6559a244b084eb1d2fc273a2982ee5051edbc78f118aaac7f7c`
- `data/evidence/2009-A simplified analysis method for composite beams with interlayer slip_aa091ea74d.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `89a80a5767282ae6c81d7caff746c6b59a3a06a1e08482c93ff8fcad061758a4`
- `data/evidence/2010-Analytical and numerical analysis of multilayered beams with interlayer slip_14958e37b2.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `f66547e1ce4ac7e3e800c2ec35599c8f3cbcf99e56b344662633017db6f4d4f4`
- `data/evidence/2013-Analysis of Composite Beams with Incomplete Interaction I_f8e8c7b1a4.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `93383a73f953862ae089b9da7c56b87f29d5995bc767dec22338ed85b166e9c5`
- `data/evidence/2013-Exact finite elements for multilayered composite beam-columns with partial interaction_c9bf5cb21f.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `54171298cabad8b0898711aaedcf12400accc9e8f0db7a9f8369c20134e8d90a`
- `data/evidence/2016-Derivation of the exact stiffness matrix of shear-deformable multi-layered beam element in partial interaction_bdf95f0602.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `964cf59ff0f6c54662ed8242803711079e12e3068632be09ac5a07ab3d34cca0`
- `data/evidence/2025-Flexible N-layer composite beam-column elements with interlayer partial interaction imperfectio_8a4d5de33a.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `258a001ad36e45e14ec03af8e641d3dde056049d34aab8f74ae5c49c9d5665d5`
- `data/evidence/2026-Laminated Partially-Composite Plate Theory_71c8d5e2c7.json` — CURRENT_C02_VERIFIED_FULL_TEXT_EVIDENCE — `1543d55fb14822ade8cbb4063fe58134e7e39098ca2dfc7e8113c0beb84593c0`
