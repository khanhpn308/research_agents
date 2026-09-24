# MP1-V002 Interim Targeted-Threat Audit

- **Status:** SUBSTANTIALLY_NARROWED
- **Confidence:** high
- **Bundle SHA256:** 0895ca70135aab547cec8d894b54ab4065b751b0b8563d4c44b6817183900a17

## Executive summary

The V002 full texts close the broad premise that NiTi wires have not previously formed frictional, slipping bundles whose stiffness and hysteresis depend on inter-wire interaction. They also establish coupling between NiTi phase transformation and inter-wire friction through pinched hysteresis, localized transformation, frictional micro-slip, and friction-generated self-heating that shifts transformation stress and stiffens the cable. However, none establishes actively varied positive confinement pressure as an independent control variable for a NiTi bundle or maps that pressure to bending stiffness. The surviving question is therefore narrower: whether actively varied radial confinement produces pressure-dependent stick-slip, phase-transformation, hysteresis, and bending-stiffness behavior that cannot be represented by an elastic-fiber contact model with substituted properties. Citation coverage is not closed, so this is an interim result.

## Target audit

### T1 — closed_by_full_text

Directly established across NiTi strands, ropes, cables, and braided microfilaments. Carboni et al. link NiTi-strand response to inter-wire friction and phase transformation; Vahidi et al. explicitly model Coulomb contact in helical SMA ropes; Liu et al. show braid constraint and micro-slip changing storage modulus and damping; Silva et al. experimentally distinguish multifilament cables from equivalent solid wires through inter-filament friction. These are frictional NiTi bundles, although not pressure-controlled jamming systems.

**Evidence paper_ids:** d9966f2f5e, 53200aa0c6, e8462758c3, 6dd1ca94d1, 98fee47c04

**Missing mechanics:**
- None.

### T2 — open_in_current_full_text_set

The metallic-cable literature establishes that radial pressure and normal force participate in frictional slip mechanics. However, the reported pressure is manufacturing preforming pressure, passive load-induced contact pressure, or a fixed applied radial preload. No V002 paper actively varies positive confinement pressure as an independent control variable on a NiTi bundle and demonstrates a resulting stiffness change.

**Evidence paper_ids:** aaad9c248c, ccdc1bb980, 53200aa0c6

**Missing mechanics:**
- Actively varied positive/internal/transverse pressure applied to a NiTi bundle
- Pressure sweep establishing changes in inter-wire normal force or friction
- Pressure-dependent bending or torsional stiffness measurement for the NiTi bundle
- Separation of active confinement effects from helix geometry, axial-load-induced contact, and manufacturing preload

### T3 — substantially_preempted

Major non-pressure portions are established. Carboni et al. combine phase-transformation and inter-wire-friction effects in hysteretic structural response; Vahidi et al. couple an SMA constitutive law with Coulomb wire contact and show friction-related residual stresses; braided NiTi microfilaments exhibit localized transformation plus contact micro-slip with architecture-dependent storage modulus; Silva et al. show inter-filament frictional heating shifting transformation stress and dynamically stiffening a superelastic cable. None couples these effects to an actively varied confinement-pressure variable or pressure-dependent bundle bending stiffness.

**Evidence paper_ids:** d9966f2f5e, 53200aa0c6, e8462758c3, 6dd1ca94d1, 98fee47c04

**Missing mechanics:**
- Actively varied confinement pressure within the NiTi transformation-contact-slip coupling
- Pressure-dependent bending stiffness across stick, partial-slip, and gross-slip regimes
- Mechanistic validation distinguishing transformation-mediated contact behavior from parameter substitution
- Joint pressure-curvature-temperature or pressure-curvature-frequency experiments

## Paper threat assessments

### Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification

- paper_id: d9966f2f5e
- DOI: 10.1061/(ASCE)EM.1943-7889.0000852
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Experimental NiTi-strand assemblies whose structural restoring force and pinched hysteresis arise from inter-wire friction, geometry, and thermoelastic martensitic transformation; it also models wire/strand superelasticity and assembly hysteresis.
- Does not establish: Actively varied radial confinement, pressure-controlled friction, or pressure-dependent bending stiffness of a NiTi bundle.

### Superelasticity SMA cables and its simplified FE model

- paper_id: 9e15094d68
- DOI: 10.1007/s40430-022-03957-2
- Targets: T1, T3
- Threat: medium
- Backward-citation priority: medium
- Establishes: Superelastic SMA strands and ropes have structural hysteresis and stiffness dependent on cable construction; a refined model includes central-to-outer-wire contact.
- Does not establish: The simplified model deliberately removes contact, adjacent outer-wire contact is omitted, and neither model studies active confinement pressure, friction-controlled bending stiffness, or a fully coupled contact-slip law.

### Mechanical response of single and double-helix SMA wire ropes

- paper_id: 53200aa0c6
- DOI: 10.1080/15376494.2021.1955313
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: A three-dimensional SMA constitutive model combined with surface contact and Coulomb friction for single- and double-helix SMA ropes, including transformation, contact-related residual stresses, and load redistribution.
- Does not establish: Pressure-controlled jamming, externally varied radial pressure, or pressure-dependent flexural rigidity; contact pressure arises from cable geometry and axial loading.

### Nonlinear Vibration Isolation via a NiTiNOL Wire Rope

- paper_id: 98fee47c04
- DOI: 10.3390/app112110032
- Targets: T1, T3
- Threat: medium
- Backward-citation priority: medium
- Establishes: NiTi wire-rope friction and phase-transition hysteresis influence equivalent stiffness, damping, and nonlinear structural response under bending-related geometric constraints.
- Does not establish: An independently controlled confinement pressure, pressure-dependent inter-wire normal force, or a mechanistic pressure-contact-transformation model.

### Cable Vibration Considering Internal Friction

- paper_id: aaad9c248c
- DOI: 
- Targets: T2
- Threat: high
- Backward-citation priority: high
- Establishes: For a metallic multilayer cable, radial pressure sets frictional resistance, wire slip produces curvature-dependent flexural rigidity, and slip thresholds govern hysteresis and vibration damping.
- Does not establish: NiTi behavior or an actively swept confinement-pressure control variable; the radial pressure is associated with preforming and is treated as a fixed input rather than a variable-stiffness command.

### BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE

- paper_id: ccdc1bb980
- DOI: 
- Targets: T2
- Threat: medium
- Backward-citation priority: high
- Establishes: Combined radial pressure, axial tension, cyclic bending, Coulomb friction, and slip in a metallic-armoured cable model.
- Does not establish: NiTi, active pressure variation, or a causal pressure-versus-structural-stiffness relationship; radial pressure is fixed at 0.2 MPa.

### High damping capacity with a wide temperature window in braided NiTi microfilaments

- paper_id: e8462758c3
- DOI: 10.1016/j.matlet.2026.141544
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Direct experimental coupling of localized martensitic transformation, inter-wire contact micro-slip, architectural constraint, damping, and storage modulus in braided NiTi bundles.
- Does not establish: Active pressure confinement, macroscopic bending stiffness, or a quantitative constitutive-contact model for pressure-controlled stick-slip.

### NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings

- paper_id: 6dd1ca94d1
- DOI: 10.3390/s22208045
- Targets: T1, T3
- Threat: high
- Backward-citation priority: high
- Establishes: Experimental multifilament NiTi-cable hysteresis in which inter-filament friction adds dissipation and heating; accumulated heat shifts transformation stress and dynamically stiffens the cable, demonstrating coupling beyond fixed modulus and friction values.
- Does not establish: Active confinement pressure, bending loading, pressure-dependent slip transitions, or pressure-dependent flexural rigidity.

## Narrowed mechanics core

- **niti_interwire_friction_prior_art_exists:** True
- **niti_phase_transformation_plus_interwire_friction_prior_art_exists:** True
- **pressure_controlled_niti_bundle_established:** False
- **pressure_dependent_bending_stiffness_established_for_niti_bundle:** False
- **survives_current_full_text_set:** True
- **provisional_surviving_question:** Does actively varied radial positive confinement change NiTi-bundle stick-slip, phase transformation, hysteresis, and bending stiffness in ways that an established elastic-fiber/contact model cannot capture through substituted modulus and friction parameters alone?
- **assessment:** The defensible core is no longer NiTi wire-bundle friction or transformation-friction hysteresis generally. It is restricted to active pressure as the control variable and its coupled effect on bending mechanics. Survival is provisional because backward and forward citation coverage remains incomplete.

## Parameter-substitution test

- **existing_elastic_fiber_model_appears_sufficient:** False
- **niti_requires_distinct_constitutive_contact_coupling:** True
- **evidence_status:** established
- **assessment:** The V002 evidence shows effects beyond replacing a constant elastic modulus and friction coefficient: localized martensitic transformation interacts with braid constraint and micro-slip, while inter-filament frictional heating changes temperature, shifts transformation stresses, and dynamically stiffens the cable. Thus a fixed-parameter elastic-fiber model is not generally sufficient for the demonstrated NiTi cable regimes. This does not yet prove that such coupling materially changes pressure-controlled bending; that narrower question remains untested in the current full-text set.

## Citation-chase plan

- **required:** True
- **backward_priority_paper_ids:** ['d9966f2f5e', '53200aa0c6', 'aaad9c248c', 'ccdc1bb980', 'e8462758c3', '6dd1ca94d1']
- **forward_core_anchor_dois:** ['10.3390/app12073582', '10.5194/ms-17-481-2026', '10.1108/IR-11-2023-0305', '10.20965/jrm.2022.p0466', '10.1299/mej.24-00130', '10.1109/LRA.2021.3097255']
- **named_high_threat_sources:** ['Carboni, Lacarbonara, and Auricchio — Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands — 10.1061/(ASCE)EM.1943-7889.0000852', 'Vahidi et al. — Mechanical response of single and double-helix SMA wire ropes — 10.1080/15376494.2021.1955313', 'Liu et al. — High damping capacity with a wide temperature window in braided NiTi microfilaments — 10.1016/j.matlet.2026.141544', 'Silva et al. — NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings — 10.3390/s22208045', 'Xin Liu — Cable Vibration Considering Internal Friction — thesis/full-text prior-mechanics source with no DOI in the supplied matrix', 'Tjahjanto, Tyrberg, and Mullins — Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable — no DOI in the supplied matrix', 'Reedlunn et al. experimental SMA-cable source cited by Vahidi et al. — full bibliographic identity unresolved in the supplied matrix', 'Carboni and Lacarbonara 2016 NiTi wire-rope damper experiments cited by Niu and Chen — full bibliographic identity unresolved in the supplied matrix']
- **stop_condition_satisfied:** False
- **rationale:** Backward references of the strongest NiTi transformation-friction and metallic radial-pressure papers have not yet been screened, and forward citations of the core jamming anchors have not been closed through the audit date. These directed citation paths are mandatory; broad keyword searching is not recommended.

## Recommended next action

Narrow MP1 to the active-pressure coupling question and conduct only the prescribed citation chase: screen backward references of d9966f2f5e, 53200aa0c6, aaad9c248c, ccdc1bb980, e8462758c3, and 6dd1ca94d1, then screen forward citations of the preserved jamming-anchor DOIs. Resolve the specifically named experimental cable sources. Falsify the direction if this chase finds actively pressure-controlled NiTi bundle stiffness prior art or shows that pressure-dependent bending is adequately reproduced by an existing elastic-fiber/contact framework using only substituted parameters.

## Provenance

- V002_PROTOCOL — docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md — SHA256 5f72a12e1052cda57e6f7e9d57a6f6e2311b118f6b0c49c24bf7a40cd253e30e
- V001_BASELINE_AUDIT — outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json — SHA256 0f7d8dfc4aae78139a483a9132b54e2eb1ada0a69304f96c3f1b0e2c197a7e81
- V002_FULL_TEXT_EVIDENCE_MATRIX — outputs/verification/MP1-V002/verification_matrix.json — SHA256 3d71d5a9fb85487e69d5469b8f5dfdd9b06ae7d16c2df3479f35de6739b8de9b
