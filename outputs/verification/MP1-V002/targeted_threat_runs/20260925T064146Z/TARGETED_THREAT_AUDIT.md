# MP1-V002 Interim Targeted-Threat Audit

- **Status:** SUBSTANTIALLY_NARROWED
- **Confidence:** high
- **Bundle SHA256:** 4d76ea589d963bffca54f0688883cb8ba7222e9a9c0424f8c54aabce4fb2b5c7

## Executive summary

VERIFIED FULL TEXT: T1 is closed. NiTi/Nitinol strands, cables, and braided microfilaments are established contacting multi-wire structures whose inter-wire friction, slip or constrained engagement affects stiffness, hysteresis, damping, transformation response, and fatigue. Major parts of T3 are also closed: prior work directly combines NiTi phase transformation with inter-wire friction/contact and structural hysteresis under axial loading and cyclic bending. However, the matrix contains no direct demonstration in which actively varied positive confinement pressure is the independent control variable for a NiTi bundle and produces pressure-dependent bending stiffness. The metallic-cable pressure evidence uses passive manufacturing pressure or a fixed radial-pressure preload, which does not satisfy T2. The surviving question is therefore much narrower: whether actively varied transverse pressure changes NiTi-bundle stick-slip and bending stiffness in a transformation-dependent manner beyond existing NiTi cable/contact models. Citation coverage remains open.

## Target audit

### T1 — closed_by_full_text

Direct NiTi-bundle prior mechanics exists. Nitinol strands and mixed NiTi-steel ropes exhibit inter-wire frictional sliding, pinched bending hysteresis, amplitude-dependent equivalent stiffness, non-synchronous engagement, and contact-mediated transformation behavior. Braided NiTi microfilaments further show that contact density and micro-slip change storage modulus and damping. This closes NiTi wire bundles with mechanically important inter-wire interaction, although it does not establish pressure-controlled jamming.

**Evidence paper_ids:** d9966f2f5e, 40760daa02, 98fee47c04, e8462758c3, 6dd1ca94d1, 53200aa0c6, 00414aac4b, fac21c950e

**Missing mechanics:**
- None.

### T2 — open_in_current_full_text_set

The matrix establishes pressure-sensitive frictional cable mechanics but not the required active control mechanism. The cable-vibration thesis treats passive preforming pressure and relates radial pressure, slip thresholds, and curvature-dependent flexural rigidity. The submarine-cable model applies a single fixed 0.2 MPa radial-pressure preload before cyclic bending and predicts contact loads and slip. Neither actively varies confinement pressure to control metallic- or NiTi-bundle stiffness. No supplied NiTi paper applies active transverse pressure as an independent variable.

**Evidence paper_ids:** aaad9c248c, ccdc1bb980

**Missing mechanics:**
- Actively varied positive or transverse confinement pressure applied to a metallic or NiTi bundle
- Measured or modeled stiffness-versus-pressure relation for that bundle
- Demonstration that pressure changes inter-wire normal force and friction sufficiently to produce controllable bending stiffness

### T3 — substantially_preempted

NiTi phase transformation coupled with inter-wire contact or friction, hysteresis, and structural response is direct prior art. Mixed NiTi-steel ropes exhibit bending hysteresis attributed jointly to martensitic transformation and inter-wire friction; Nitinol strand assemblies exhibit configuration-dependent stiffness and pinching; three-dimensional SMA-rope models combine phase-transforming constitutive laws with Coulomb contact; braided microfilaments show architecture-dependent transformation and micro-slip effects on storage modulus; and dynamic micro-cables show frictional heating that shifts transformation stress and stiffens the response. What remains absent is actively varied confinement pressure coupled to the NiTi contact/slip system and pressure-dependent bending stiffness.

**Evidence paper_ids:** 40760daa02, d9966f2f5e, 53200aa0c6, e8462758c3, 6dd1ca94d1, 00414aac4b, fac21c950e

**Missing mechanics:**
- Active confinement pressure as an independent variable in a NiTi wire bundle
- Pressure-dependent bending stiffness across stick, partial-slip, and gross-slip regimes
- Direct comparison showing whether transformation-dependent contact behavior exceeds an existing NiTi constitutive-plus-contact model

## Paper threat assessments

### Superelastic shape memory alloy cables: Part I – Isothermal tension experiments

- paper_id: 00414aac4b
- DOI: 10.1016/j.ijsolstr.2013.03.013
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Full-scale 7x7 and 1x27 superelastic NiTi cables exhibit architecture-dependent transformation plateaus, stiffness, torque, hysteresis, and shakedown. Lubrication produced virtually no axial-response change because static friction prevented relative wire sliding.
- Does not establish: It does not study bending stiffness or actively varied radial confinement pressure, and it does not provide a coupled structural contact model.

### Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses

- paper_id: fac21c950e
- DOI: 10.1016/j.ijsolstr.2013.03.015
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: NiTi cable architecture, contact indentations, helix angle, and layer-by-layer transformation materially alter compliance, localization, torque, and load sharing.
- Does not establish: Its main interpretation assumes monolithic cross-sectional motion without relative sliding and neglects average contact effects; it does not test bending or active confinement pressure.

### Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments

- paper_id: 40760daa02
- DOI: 10.1061/(ASCE)EM.1943-7889.0001072
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Mixed NiTi-steel wire ropes under cyclic bending exhibit pinched hysteresis attributed directly to the simultaneous action of inter-wire friction and martensitic transformation, with amplitude-dependent equivalent stiffness and damping.
- Does not establish: The rope is hybrid rather than an all-NiTi bundle, and its contact pressure arises passively from rope construction and deformation rather than actively varied confinement.

### Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application

- paper_id: 2f7fcf2f8f
- DOI: 10.1016/j.engstruct.2019.01.049
- Targets: T1, T3
- Threat: medium
- Backward-citation priority: medium
- Establishes: A 7x7 NiTi cable has non-synchronous wire engagement, transformation hysteresis, cyclic degradation, and architecture-dependent effective stiffness that can be represented by a reduced multilayer hysteretic model.
- Does not establish: It does not explicitly resolve frictional contact, bending slip, or externally controlled confinement pressure.

### Nonlinear dynamic response of a wire rope isolator: Experiment, identification and validation

- paper_id: 7f3f45407f
- DOI: 10.1016/j.engstruct.2021.112121
- Targets: T1
- Threat: medium
- Backward-citation priority: medium
- Establishes: For a stainless-steel wire rope, inter-wire friction and cable geometry generate amplitude-dependent stiffness and asymmetric hysteresis that a reduced Bouc-Wen model predicts dynamically.
- Does not establish: It contains no NiTi transformation mechanics and no active radial-pressure control.

### Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification

- paper_id: d9966f2f5e
- DOI: 10.1061/(ASCE)EM.1943-7889.0000852
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Nitinol strand assemblies exhibit stiffness and pinched hysteresis governed by inter-wire friction, superelastic phase transformation, geometric stretching, and boundary configuration. Pure-bending and bending-tension regimes were experimentally separated and modeled.
- Does not establish: Boundary reconfiguration is not transverse pressure control, and the study does not produce a confinement-pressure-dependent NiTi bending-stiffness law.

### Superelasticity SMA cables and its simplified FE model

- paper_id: 9e15094d68
- DOI: 10.1007/s40430-022-03957-2
- Targets: T1, T3
- Threat: medium
- Backward-citation priority: medium
- Establishes: Superelastic SMA strands and 7x7 ropes have architecture-dependent transformation hysteresis, and a reduced coupled-section model can reproduce the tensile loop of a more detailed contact model at much lower cost.
- Does not establish: The simplified model removes inter-wire contact and friction, the study is limited to axial tension, and no confinement-pressure variable is studied.

### Mechanical response of single and double-helix SMA wire ropes

- paper_id: 53200aa0c6
- DOI: 10.1080/15376494.2021.1955313
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: A three-dimensional phase-transforming SMA constitutive model combined with normal contact and Coulomb friction predicts stress, torque, residual stress, and recovery in 1x27 and 7x7 SMA ropes.
- Does not establish: Loading is axial or thermally driven rather than pressure-controlled bending; contact pressure is generated by cable geometry and loading, not an actively varied external control input.

### Nonlinear Vibration Isolation via a NiTiNOL Wire Rope

- paper_id: 98fee47c04
- DOI: 10.3390/app112110032
- Targets: T1, T3
- Threat: medium
- Backward-citation priority: medium
- Establishes: A NiTi rope model combining beam geometry with phenomenological friction/transformation hysteresis predicts amplitude-dependent equivalent stiffness, damping, and softening-hardening behavior.
- Does not establish: It relies on secondary experimental data, does not resolve contact pressure explicitly, and contains no active confinement-pressure control.

### Cable Vibration Considering Internal Friction

- paper_id: aaad9c248c
- DOI: 
- Targets: T1, T2
- Threat: high
- Backward-citation priority: high
- Establishes: This thesis establishes curvature-dependent flexural rigidity in a multilayer metallic cable, with slip transitions determined by inter-layer friction and passive radial preforming pressure; it also reports experimental estimates of inter-layer pressure.
- Does not establish: The cable is linearly elastic rather than NiTi, and radial pressure is a passive manufacturing condition rather than an actively varied stiffness-control variable.

### BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE

- paper_id: ccdc1bb980
- DOI: 
- Targets: T2
- Threat: high
- Backward-citation priority: high
- Establishes: A metallic cable model combines externally applied 0.2 MPa radial pressure, axial preload, Coulomb contact, cyclic bending, and stick-slip prediction.
- Does not establish: Pressure is a single fixed preload rather than an actively swept control variable; the paper does not establish pressure-dependent structural stiffness and contains no NiTi transformation mechanics.

### High damping capacity with a wide temperature window in braided NiTi microfilaments

- paper_id: e8462758c3
- DOI: 10.1016/j.matlet.2026.141544
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Braided NiTi microfilaments directly couple localized martensitic transformation with inter-wire contact micro-sliding. Wire count and braid density alter storage modulus and damping, demonstrating that structural constraint changes both transformation and frictional response.
- Does not establish: It studies small-amplitude tensile DMA and passive geometric constraint, not bending stiffness controlled by actively varied external pressure.

### NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings

- paper_id: 6dd1ca94d1
- DOI: 10.3390/s22208045
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: A 1x7 superelastic NiTi micro-cable exhibits inter-filament frictional heating, increased damping, fretting fatigue, and frequency-dependent thermomechanical stiffening as temperature shifts transformation stresses.
- Does not establish: Testing is uniaxial and unconstrained by an externally controlled pressure; no pressure-dependent bending-stiffness relation is reported.

## Narrowed mechanics core

- **niti_interwire_friction_prior_art_exists:** True
- **niti_phase_transformation_plus_interwire_friction_prior_art_exists:** True
- **pressure_controlled_niti_bundle_established:** False
- **pressure_dependent_bending_stiffness_established_for_niti_bundle:** False
- **survives_current_full_text_set:** True
- **provisional_surviving_question:** Under actively varied transverse confinement pressure, do superelastic NiTi bundles exhibit pressure- and curvature-dependent stick-slip and bending-stiffness transitions that cannot be predicted by existing NiTi cable constitutive/contact mechanics?
- **assessment:** The broad NiTi-bundle mechanics premise is no longer open: NiTi inter-wire friction, contact, phase transformation, hysteresis, and stiffness effects are established. The only surviving mechanics core is the active-pressure dimension and its interaction with bending. This is narrower than material substitution and must be tested against both positive-pressure elastic-fiber models and established nonlinear NiTi cable/contact models.

## Parameter-substitution test

- **existing_elastic_fiber_model_appears_sufficient:** False
- **niti_requires_distinct_constitutive_contact_coupling:** True
- **evidence_status:** established
- **assessment:** The matrix does not support reducing NiTi to a constant substituted modulus and friction coefficient. Transformation plateaus, transformation localization, cyclic degradation, architecture-dependent sequential transformation, frictional self-heating, temperature-shifted transformation stress, and contact-mediated residual stresses are history- and state-dependent effects absent from a simple elastic-fiber substitution. Existing NiTi constitutive-plus-contact and phenomenological cable models already address much of this complexity, however. The unestablished part is whether active pressure creates an additional pressure-dependent bending coupling beyond those existing formulations.

## Citation-chase plan

- **required:** True
- **backward_priority_paper_ids:** ['d9966f2f5e', '40760daa02', '00414aac4b', 'fac21c950e', '53200aa0c6', 'aaad9c248c', 'ccdc1bb980', '6dd1ca94d1', 'e8462758c3']
- **forward_core_anchor_dois:** ['10.3390/app12073582', '10.5194/ms-17-481-2026', '10.1109/LRA.2021.3097255', '10.20965/jrm.2022.p0466', '10.1299/mej.24-00130', '10.1108/IR-11-2023-0305', '10.1061/(ASCE)EM.1943-7889.0000852', '10.1061/(ASCE)EM.1943-7889.0001072', '10.1016/j.ijsolstr.2013.03.013', '10.1016/j.ijsolstr.2013.03.015', '10.1080/15376494.2021.1955313', '10.3390/s22208045', '10.1016/j.matlet.2026.141544']
- **named_high_threat_sources:** ['Reedlunn, Daly and Shaw — Superelastic shape memory alloy cables, Parts I and II', 'Carboni, Lacarbonara and Auricchio — Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands', 'Carboni and Lacarbonara — Nonlinear Vibration Absorber with Pinched Hysteresis', 'Vahidi et al. — Mechanical response of single and double-helix SMA wire ropes', 'Xin Liu — Cable Vibration Considering Internal Friction', 'Tjahjanto, Tyrberg and Mullins — Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable', 'Silva et al. — NiTi SMA Superelastic Micro Cables', 'Yiwen Liu et al. — High damping capacity with a wide temperature window in braided NiTi microfilaments']
- **stop_condition_satisfied:** False
- **rationale:** Backward screening should trace the NiTi strand/rope friction lineage and the metallic-cable radial-pressure lineage for any actively confined variants. Forward screening should cover the established wire-jamming, positive-pressure jamming, SMA-jamming, NiTi-cable, and 2026 braided-NiTi anchors through the audit date. No final survival verdict is permitted until both directions are documented and all named high-threat candidates are resolved.

## Recommended next action

Perform only the protocol-defined citation chase: screen backward references of the listed high-priority V002 papers for externally confined NiTi or metallic bundles, and screen forward citations of the listed anchor DOIs for active pressure-dependent NiTi bending mechanics. If no direct kill emerges, formulate the MSc contribution as a model-discrimination study between an elastic positive-pressure fiber model and an established nonlinear NiTi constitutive/contact model under controlled pressure and curvature—not as novelty of NiTi wires, friction, hysteresis, or bundling.

## Provenance

- V002_PROTOCOL — docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md — SHA256 5f72a12e1052cda57e6f7e9d57a6f6e2311b118f6b0c49c24bf7a40cd253e30e
- V001_BASELINE_AUDIT — outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json — SHA256 0f7d8dfc4aae78139a483a9132b54e2eb1ada0a69304f96c3f1b0e2c197a7e81
- V002_FULL_TEXT_EVIDENCE_MATRIX — outputs/verification/MP1-V002/verification_matrix.json — SHA256 4fc8a11d7a9fb9c2bdb225838c4335c05c400a14c239c4316b5760ca7a4706c3
