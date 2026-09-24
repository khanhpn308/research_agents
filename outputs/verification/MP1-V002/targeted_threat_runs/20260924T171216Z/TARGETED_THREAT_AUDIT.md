# MP1-V002 Interim Targeted-Threat Audit

- **Status:** SUBSTANTIALLY_NARROWED
- **Confidence:** high
- **Bundle SHA256:** 036fb11d60fb2b2cb15cd22f29df91c970e86c50ab7c6b8356a6d7f772537cfe

## Executive summary

The V002 full-text set closes T1 and major portions of T3. Prior work directly establishes contacting NiTi strands/cables whose inter-wire friction, slip, helical constraints, and martensitic transformation jointly affect hysteresis, damping, effective stiffness, and structural response. It does not establish the surviving pressure-controlled core: none of the supplied studies actively varies external positive/transverse confinement pressure on a NiTi bundle and demonstrates the resulting pressure-dependent bending stiffness. T2 therefore remains open in this full-text set, and T3 remains open only in the narrower sense of coupling active confinement pressure to NiTi transformation, stick-slip, hysteresis, and bending stiffness. Citation coverage is not closed, so this is an interim substantially-narrowed verdict rather than a survival verdict.

## Target audit

### T1 — closed_by_full_text

Direct prior mechanics exists. Carboni et al. experimentally attribute the pure-bending response of Nitinol strands to inter-wire friction and show coupled frictional and transformation-related hysteresis in other configurations. Vahidi et al. explicitly model NiTi rope contact and Coulomb friction with an SMA constitutive law. Liu et al. show that braid architecture, contact density, and micro-slip alter storage modulus and damping, while Silva et al. demonstrate additional inter-filament frictional dissipation and thermomechanical stiffening in a 1×7 NiTi micro-cable. NiTi as a contacting frictional wire assembly is therefore not an open claim.

**Evidence paper_ids:** d9966f2f5e, 53200aa0c6, e8462758c3, 6dd1ca94d1, 98fee47c04

**Missing mechanics:**
- None.

### T2 — open_in_current_full_text_set

The set contains adjacent but non-closing evidence. The submarine-cable model applies a fixed 0.2 MPa radial pressure together with tension and cyclic bending, but it neither sweeps pressure as an active stiffness-control variable nor uses a NiTi bundle. The cable-vibration thesis relates passive manufacturing/preforming radial pressure to inter-layer friction, slip thresholds, and curvature-dependent flexural rigidity, but that pressure is not actively varied. NiTi cable papers use helical geometry, axial-load-induced contact, manufacturing constraint, or passive internal pressure rather than controlled external confinement.

**Evidence paper_ids:** ccdc1bb980, aaad9c248c, 53200aa0c6, fac21c950e

**Missing mechanics:**
- A NiTi bundle radially or transversely compressed by an actively varied external positive-pressure control variable
- A demonstrated pressure-to-normal-force-to-friction/stick-slip causal chain
- Measured or modeled NiTi-bundle bending stiffness as a function of confinement pressure
- Separation of active confinement effects from helix geometry, axial tension, manufacturing preload, and passive contact pressure

### T3 — substantially_preempted

NiTi phase transformation coupled with inter-wire friction, slip, hysteresis, damping, and effective stiffness is already established in several forms. Carboni et al. combine Nitinol transformation and inter-wire friction in bending/tension assemblies; Vahidi et al. couple an SMA constitutive model with explicit contact and Coulomb friction; braided microfilament experiments connect localized martensitic transformation, contact micro-slip, storage modulus, and damping; and dynamic micro-cable tests connect inter-filament frictional heating to transformation-stress shifts and stiffening. What is not established is active confinement pressure as the independent variable controlling that coupled response and pressure-dependent bending stiffness.

**Evidence paper_ids:** d9966f2f5e, 53200aa0c6, e8462758c3, 6dd1ca94d1, 98fee47c04

**Missing mechanics:**
- Actively varied external confinement pressure in a superelastic NiTi bundle
- Direct measurement of pressure-dependent bending stiffness across stick, partial-slip, and gross-slip regimes
- Joint mapping of pressure, curvature, transformation state, hysteresis, and structural stiffness
- A controlled comparison showing whether pressure-dependent NiTi behavior exceeds an elastic-fiber/contact model with substituted material and friction parameters

## Paper threat assessments

### Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses

- paper_id: fac21c950e
- DOI: 10.1016/j.ijsolstr.2013.03.015
- Targets: T1, T3
- Threat: medium
- Backward-citation priority: high
- Establishes: NiTi cable architecture and manufacturing contact indentations materially affect transformation localization, compliance, torque, and layer-by-layer engagement under axial loading.
- Does not establish: It assumes no relative sliding between adjacent layers for its simplified interpretation, neglects contact effects on average, and does not apply or vary external confinement pressure or measure pressure-dependent bending stiffness.

### Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application

- paper_id: 2f7fcf2f8f
- DOI: 10.1016/j.engstruct.2019.01.049
- Targets: T1, T3
- Threat: medium
- Backward-citation priority: medium
- Establishes: Multi-wire NiTi cables exhibit flag-shaped hysteresis, non-synchronous wire engagement, cycle-dependent stiffness, and cyclic degradation that can be represented by an empirical layered phenomenological model.
- Does not establish: It does not resolve explicit wire-wire friction or slip, actively vary confinement pressure, or address pressure-dependent bending stiffness.

### Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification

- paper_id: d9966f2f5e
- DOI: 10.1061/(ASCE)EM.1943-7889.0000852
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Experiments directly link Nitinol strand response to inter-wire friction, geometric stretching, and thermoelastic martensitic transformation. Pure-bending configurations exhibit friction-governed softening hysteresis, while bending-tension configurations exhibit transformation-related pinched hysteresis and tunable restoring stiffness.
- Does not establish: Its constraints are kinematic and geometric; it does not use actively varied radial/transverse confinement pressure or characterize pressure-dependent bundle stiffness.

### Superelasticity SMA cables and its simplified FE model

- paper_id: 9e15094d68
- DOI: 10.1007/s40430-022-03957-2
- Targets: T1, T3
- Threat: medium
- Backward-citation priority: medium
- Establishes: Superelastic NiTi strand and rope hysteresis under axial tension can be reproduced efficiently with coupled-section models, and a simplified model without explicit contact closely matches a refined contact model for the studied response.
- Does not establish: Inter-wire friction is omitted, adjacent outer-wire contact is incomplete, and neither bending nor actively controlled confinement pressure is studied. Its reduced-model success therefore does not prove parameter substitution is sufficient for pressure-controlled bending.

### Mechanical response of single and double-helix SMA wire ropes

- paper_id: 53200aa0c6
- DOI: 10.1080/15376494.2021.1955313
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: A three-dimensional SMA model with explicit normal contact and Coulomb friction predicts component-level stress, slip-related residual stress, phase transformation, and hysteretic response in single- and double-helix SMA ropes.
- Does not establish: Contact pressure arises from rope geometry and axial loading rather than an actively varied external confinement control. The work does not establish pressure-dependent bending stiffness.

### Nonlinear Vibration Isolation via a NiTiNOL Wire Rope

- paper_id: 98fee47c04
- DOI: 10.3390/app112110032
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: A NiTi wire-rope structural model combines beam flexure with phenomenological internal-friction and phase-transition hysteresis, producing amplitude-dependent equivalent stiffness, softening-hardening behavior, and damping.
- Does not establish: It relies substantially on phenomenological and secondary evidence, does not independently manipulate inter-wire normal force, and contains no external confinement-pressure variable.

### Cable Vibration Considering Internal Friction

- paper_id: aaad9c248c
- DOI: 
- Targets: T1, T2
- Threat: high
- Backward-citation priority: high
- Establishes: For a metallic helical cable, passive inter-layer radial pressure controls frictional slip thresholds, curvature-dependent flexural rigidity, hysteresis, and vibration damping. The thesis also measures passive inter-layer pressure through push-out tests.
- Does not establish: The cable is linearly elastic rather than NiTi, and radial pressure is manufacturing/preforming pressure rather than an actively swept control input. It therefore establishes core cable mechanics but not pressure-controlled NiTi jamming.

### BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE

- paper_id: ccdc1bb980
- DOI: 
- Targets: T2
- Threat: high
- Backward-citation priority: high
- Establishes: A metallic cable model combines an externally applied radial pressure, axial tension, Coulomb friction, cyclic bending, and stick-slip mechanics, making it the closest supplied pressure/contact precedent for T2.
- Does not establish: Radial pressure is fixed at 0.2 MPa rather than actively varied, the structure includes polymeric sheaths and fillers, the conductors are not NiTi, and pressure-dependent structural stiffness is not demonstrated.

### High damping capacity with a wide temperature window in braided NiTi microfilaments

- paper_id: e8462758c3
- DOI: 10.1016/j.matlet.2026.141544
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Experiments explicitly couple localized martensitic transformations with inter-wire contact micro-sliding. Wire count and braid density alter contact constraint, slip distance, storage modulus, and damping, closing much of the proposed NiTi-friction coupling claim.
- Does not establish: Braiding density is a manufactured geometric constraint, not actively varied confinement pressure. The study addresses small-amplitude tensile DMA and damping rather than pressure-controlled bending stiffness.

### NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings

- paper_id: 6dd1ca94d1
- DOI: 10.3390/s22208045
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: A 1×7 NiTi micro-cable exhibits inter-filament frictional dissipation, friction-enhanced self-heating, transformation-stress shifts, dynamic stiffening, hysteresis, and fretting-related fatigue beyond the response of an equal-area monolithic wire.
- Does not establish: The experiments are uniaxial tensile tests without controlled external confinement pressure, bending stiffness measurements, or pressure-induced stick-slip transitions.

## Narrowed mechanics core

- **niti_interwire_friction_prior_art_exists:** True
- **niti_phase_transformation_plus_interwire_friction_prior_art_exists:** True
- **pressure_controlled_niti_bundle_established:** False
- **pressure_dependent_bending_stiffness_established_for_niti_bundle:** False
- **survives_current_full_text_set:** True
- **provisional_surviving_question:** Under actively varied positive radial/transverse confinement, how do pressure and curvature govern stick-slip transitions and bending stiffness in a superelastic NiTi wire bundle, and can those responses be predicted by an existing elastic-fiber/contact framework with substituted NiTi properties?
- **assessment:** The broad NiTi-bundle and NiTi-plus-friction propositions no longer survive. Only the actively pressure-controlled bending-mechanics question remains open in this full-text set. Its defensibility depends on demonstrating either pressure-dependent transformation/contact coupling or a validated limit of existing elastic-fiber models; using NiTi in place of nylon or steel is not itself novel.

## Parameter-substitution test

- **existing_elastic_fiber_model_appears_sufficient:** False
- **niti_requires_distinct_constitutive_contact_coupling:** False
- **evidence_status:** insufficient
- **assessment:** The supplied evidence does not establish either kill-test outcome for actively confined bending. Simplified and phenomenological models reproduce some axial NiTi cable responses without resolving frictional contact, which raises a serious substitution/reduced-order risk. Conversely, dynamic micro-cable and braided-microfilament studies show frictional heating, transformation-stress shifts, localized transformations, and constraint-dependent micro-slip that cannot be represented by merely assigning one constant elastic modulus. Those effects occur under tensile, thermal, or braided conditions, however; the matrix does not show that a distinct constitutive-contact coupling is required for quasi-static pressure-dependent bending. A direct baseline comparison remains necessary.

## Citation-chase plan

- **required:** True
- **backward_priority_paper_ids:** ['d9966f2f5e', '53200aa0c6', '98fee47c04', 'aaad9c248c', 'ccdc1bb980', 'e8462758c3', '6dd1ca94d1', 'fac21c950e']
- **forward_core_anchor_dois:** ['10.3390/app12073582', '10.5194/ms-17-481-2026', '10.1109/LRA.2021.3097255', '10.20965/jrm.2022.p0466', '10.1299/mej.24-00130', '10.1108/IR-11-2023-0305', '10.1061/(ASCE)EM.1943-7889.0000852', '10.1080/15376494.2021.1955313', '10.3390/app112110032', '10.1016/j.matlet.2026.141544', '10.3390/s22208045', '10.1016/j.ijsolstr.2013.03.015']
- **named_high_threat_sources:** ['d9966f2f5e — Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification — 10.1061/(ASCE)EM.1943-7889.0000852', '53200aa0c6 — Mechanical response of single and double-helix SMA wire ropes — 10.1080/15376494.2021.1955313', '98fee47c04 — Nonlinear Vibration Isolation via a NiTiNOL Wire Rope — 10.3390/app112110032', 'aaad9c248c — Cable Vibration Considering Internal Friction — thesis, DOI not supplied', 'ccdc1bb980 — BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE — DOI not supplied', 'e8462758c3 — High damping capacity with a wide temperature window in braided NiTi microfilaments — 10.1016/j.matlet.2026.141544', '6dd1ca94d1 — NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings — 10.3390/s22208045']
- **stop_condition_satisfied:** False
- **rationale:** Citation chasing remains mandatory because the supplied full texts substantially narrow but do not directly falsify the active-pressure mechanics core. Screen backward references of the listed NiTi strand, cable-friction, radial-pressure, and braided-microfilament sources, and screen forward citations of the preserved anchors through the audit date. Priority is specifically any named work that varies radial/transverse pressure on metallic or NiTi bundles and reports contact/slip-dependent bending stiffness; broad keyword searching is not recommended.

## Recommended next action

Proceed to the protocol-bounded backward and forward citation chase, prioritizing the listed V002 papers and anchor DOIs. In parallel, define the eventual kill experiment/model comparison: fit an established elastic-fiber/contact model using measured NiTi tangent properties and friction, then test whether it predicts bending moment-curvature and hysteresis across confinement pressure. Reject the remaining mechanics claim if direct pressure-controlled NiTi prior art is found or if parameter substitution adequately explains the response; retain only a narrower coupling question if reproducible transformation-dependent deviations remain.

## Provenance

- V002_PROTOCOL — docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md — SHA256 5f72a12e1052cda57e6f7e9d57a6f6e2311b118f6b0c49c24bf7a40cd253e30e
- V001_BASELINE_AUDIT — outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json — SHA256 0f7d8dfc4aae78139a483a9132b54e2eb1ada0a69304f96c3f1b0e2c197a7e81
- V002_FULL_TEXT_EVIDENCE_MATRIX — outputs/verification/MP1-V002/verification_matrix.json — SHA256 1b4e420f80e678b358f8f28a76ef04bfa752d0b01206049346f583f8e5a14316
