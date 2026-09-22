# MP1-V001 Core Prior-Art Audit

- **Status:** PIVOT_TO_MECHANICS_CORE
- **Confidence:** high
- **Bundle SHA256:** 6002f768a69cfa62032b783ec086884d6330955270f2ac89eaae29dea4446352

## Candidate architecture

Superelastic NiTi/metal wire bundle with positive-pressure confinement, inter-wire frictional jamming, variable bending stiffness, and an optional compact SMA-driven syringe/piston pressure source.

## Executive summary

The supplied full-text corpus defeats the broad architecture claims: wire/fiber jamming, positive-pressure jamming, SMA combined with jamming, and compact or embedded jamming pressure sources all have direct prior art. It does not establish a fatal conflict for C5-C7: none of the supplied systems uses superelastic NiTi wires themselves as the frictionally jammed medium under positive-pressure confinement, nor models the resulting coupling among NiTi constitutive response, inter-wire slip, pressure, and bending stiffness. MP1 should therefore abandon component-combination novelty and pivot to that narrow mechanics question. This is an open-in-this-corpus finding, not proof of universal novelty. The SMA-driven syringe/piston variant is strongly exposed as an implementation substitution and should not carry the scientific contribution.

## Claim audit

### C1 — closed

**Claim:** Wire/fiber jamming for variable stiffness is novel.

Directly closed. Bai et al. demonstrate vacuum-controlled wire/fiber jamming with inter-wire friction and variable bending stiffness. Zhang and Yao subsequently demonstrate positive-pressure fiber jamming with pressure-dependent slip transitions and bending stiffness.

**Evidence paper_ids:** 240fbf6022, 3aa8790db0

### C2 — closed

**Claim:** Positive-pressure jamming for variable stiffness is novel.

Directly closed. Liu et al. demonstrate positive-pressure granular jamming for variable stiffness, while Zhang and Yao demonstrate positive-pressure confinement of a frictional fiber bundle up to 300 kPa.

**Evidence paper_ids:** 182d854610, 3aa8790db0

### C3 — closed

**Claim:** SMA and jamming in the same variable-stiffness device is novel.

Directly closed by the Takashima lineage, which integrates NiTi SMA wires with vacuum granular jamming in variable-stiffness links. Matsumoto et al. further examine Ti-Ni recovery behavior within that architecture. The NiTi wires are backbones/recovery elements, not the jamming medium, so these papers do not close C5-C7.

**Evidence paper_ids:** 2cd907e77a, 7ce492505d, 99fe24da8b, d3b3b6963f

### C4 — closed

**Claim:** An onboard/compact pressure source for jamming is novel.

Closed at the compact/integrated-source level. Huynh et al. embed a bidirectional flexible micropump directly into a soft actuator and use its negative pressure to activate granular jamming. Wang et al. also present a compact modular motor-and-ball-screw piston mechanism for particle jamming. Huynh's external reservoir and high-voltage supply limit untethered operation but do not preserve the broad compact-source claim.

**Evidence paper_ids:** bbe88a0c04, c6a31066f8

### C5 — open_in_supplied_corpus

**Claim:** Superelastic NiTi wires themselves as the frictional jamming medium remain open.

No supplied paper makes superelastic NiTi wires the contacting, mutually slipping jamming medium. Bai et al. use kraft rope, hemp rope, and nylon wire; Zhang and Yao use nylon fibers. Takashima's NiTi wires are embedded backbones inside coffee-ground granular jamming, and Wang's superelastic NiTi wires are tendons around a particle-jamming core. C5 therefore remains open only within the supplied corpus. Material substitution by itself is not a defensible contribution.

**Evidence paper_ids:** 240fbf6022, 2cd907e77a, c6a31066f8, 3aa8790db0

### C6 — open_in_supplied_corpus

**Claim:** Positive-pressure confinement of a superelastic NiTi wire bundle remains open.

No supplied paper positively confines a superelastic NiTi wire bundle to create inter-wire jamming. Zhang and Yao are the closest direct architectural threat because they positively confine a nylon fiber bundle and model its frictional bending regimes. Replacing nylon with NiTi is not sufficient novelty unless the superelastic constitutive behavior materially changes the mechanics.

**Evidence paper_ids:** 182d854610, 3aa8790db0

### C7 — open_in_supplied_corpus

**Claim:** Coupling among NiTi superelastic response, inter-wire slip/friction, pressure and bending stiffness remains open.

No supplied paper directly couples all four elements. Zhang and Yao couple elastic-fiber friction, positive pressure, progressive slip, and bending stiffness, but not NiTi superelasticity. The Takashima/Matsumoto lineage studies NiTi transformation or recovery behavior in granular-jamming devices, but not inter-NiTi frictional jamming. Wang combines superelastic NiTi tendons with piston-compressed particles, but the tendons are not the jammed bundle. INFERENCE: a defensible question remains only if it tests whether transformation plateaus, hysteresis, or phase-dependent tangent stiffness alter pressure-dependent stick-slip and composite bending beyond an elastic-fiber model with substituted material parameters.

**Evidence paper_ids:** 3aa8790db0, 2cd907e77a, 7ce492505d, c6a31066f8

### C8 — substantially_preempted

**Claim:** SMA-driven syringe/piston specifically powering jamming pressure remains open.

The exact SMA-to-syringe-to-jamming hookup is absent from the supplied corpus, but its component basis is heavily pre-empted: SMA robotic pumps and capsule micropumps generate fluid pressure, while embedded micropumps and motorized pistons already power jamming. Without evidence of a distinct coupled mechanics problem, using SMA instead of an existing pump or motor is actuator substitution rather than scientific novelty.

**Evidence paper_ids:** de64029540, 55457a97c6, bbe88a0c04, c6a31066f8

## Closest prior art

### A variable stiffness omnidirectional chain based on positive-pressure fiber jamming

- paper_id: 3aa8790db0
- DOI: 10.5194/ms-17-481-2026
- Threat: high
- Overlap: Positive-pressure confinement of a fiber bundle; Coulomb inter-fiber friction; jammed, transitional, and fully slipping regimes; pressure-dependent bending mechanics; experimental validation up to 300 kPa.
- Critical difference: Uses nominally elastic nylon fibers rather than superelastic NiTi wires and does not couple phase-transforming NiTi constitutive behavior to contact and slip.

### Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming

- paper_id: 240fbf6022
- DOI: 10.3390/app12073582
- Threat: high
- Overlap: Wire/fiber bundles act as the frictional jamming medium and provide tunable bending stiffness in soft robotic actuators.
- Critical difference: Uses vacuum confinement and polymeric/rope media rather than positive-pressure confinement of superelastic NiTi wires.

### Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon

- paper_id: 2cd907e77a
- DOI: 10.20965/jrm.2022.p0466
- Threat: high
- Overlap: Combines NiTi SMA wires, jamming, variable bending stiffness, and beam-level mechanics in one device.
- Critical difference: The NiTi wires are shape-memory backbones surrounded by vacuum-jammed coffee grounds; they are not the frictionally jammed medium.

### Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm

- paper_id: c6a31066f8
- DOI: 10.1108/IR-11-2023-0305
- Threat: high
- Overlap: Combines superelastic NiTi wires, piston-driven jamming, and variable stiffness in a compact continuum arm.
- Critical difference: NiTi wires are tendons, while a motorized piston axially compresses particles. It does not apply positive fluid pressure to radially confine a NiTi bundle.

### A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots

- paper_id: 182d854610
- DOI: 10.1109/LRA.2021.3097255
- Threat: high
- Overlap: Direct positive-pressure jamming for pressure-controlled bending stiffness and portable wearable operation using miniature pumps.
- Critical difference: The jammed medium is granular material between a bladder and sleeve, not a NiTi wire bundle.

### Soft actuator with switchable stiffness using a micropump-activated jamming system

- paper_id: bbe88a0c04
- DOI: 10.1016/j.sna.2022.113449
- Threat: high
- Overlap: An embedded compact bidirectional micropump directly activates granular jamming and changes bending stiffness.
- Critical difference: Uses an electro-conjugate-fluid micropump and negative-pressure particle jamming rather than an SMA syringe and positive-pressure wire confinement.

### Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon

- paper_id: 7ce492505d
- DOI: 10.1299/mej.24-00130
- Threat: medium
- Overlap: Examines Ti-Ni transformation behavior, recovery stress, tangential stiffness, training, and performance inside an SMA-jamming variable-stiffness mechanism.
- Critical difference: Studies recovery of a NiTi backbone in granular jamming, not pressure-dependent inter-wire friction in a jammed NiTi bundle.

### A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump

- paper_id: de64029540
- DOI: 10.1109/TMECH.2012.2211032
- Threat: medium
- Overlap: Demonstrates SMA actuation of positive-displacement pumping chambers and develops coupled SMA, piston, thermal, and fluid-pressure models.
- Critical difference: The pump powers fluid output rather than a jamming structure and is not the proposed compact syringe implementation.

### Shape Memory Alloy Capsule Micropump for Drug Delivery Applications

- paper_id: 55457a97c6
- DOI: 10.3390/mi12050520
- Threat: medium
- Overlap: Demonstrates a compact NiTi-actuated pump capable of generating fluid pressure and controlled displacement.
- Critical difference: It is not connected to jamming and does not address bundle-confinement mechanics.

## Fatal conflicts

- C1 is fatally conflicted by Bai et al. 2022 and Zhang and Yao 2026: wire/fiber jamming for variable stiffness is established.
- C2 is fatally conflicted by Liu et al. 2021 and Zhang and Yao 2026: positive-pressure jamming for variable stiffness is established, including positive-pressure fiber jamming.
- C3 is fatally conflicted by the 2022-2026 Takashima lineage: SMA and jamming already coexist in variable-stiffness devices.
- C4 is fatally conflicted by Huynh et al. 2022: an embedded compact micropump already activates jamming.
- No supplied paper is a fatal direct conflict for the combined C5-C7 core.

## Remaining mechanics core

- **niti_as_jamming_medium:** True
- **positive_pressure_niti_bundle:** True
- **coupled_superelastic_friction_mechanics:** True
- **scientifically_defensible:** True
- **assessment:** C5 and C6 remain open in this corpus but are not independently sufficient because they can reduce to material and confinement substitutions. C7 supplies the potentially defensible mechanics core: determine whether positive confinement produces pressure- and curvature-dependent transitions among independent-wire bending, partial stick-slip, transformation-mediated response, and composite bending, and whether an elastic Coulomb-fiber model remains valid for a superelastic NiTi bundle. This remains provisional until targeted citation chasing closes the direct NiTi-bundle lineage.

## Implementation-only novelty risk

- **sma_syringe_only_difference:** True
- **risk_level:** high
- **assessment:** SMA pumps, compact embedded jamming pumps, and motorized piston jamming all exist in the supplied corpus. The exact SMA syringe connection may be unreported here, but that absence does not create a scientific contribution. C8 should be treated as optional packaging unless it introduces and tests a separately justified pressure-generation or coupled-mechanics hypothesis.

## Targeted follow-up

- **required:** True
- **targets:** ['T1 — Backward and forward citations of Bai et al. 2022 and Zhang and Yao 2026 for metallic-wire, steel-wire, SMA-wire, or NiTi-wire bundles used as the actual frictional jamming medium.', 'T2 — Backward and forward citations of Liu et al. 2021 and Zhang and Yao 2026 for positive-pressure radial confinement of metallic or superelastic wire bundles, including bladder-confined and pressure-vessel variants.', 'T3 — Backward and forward citations spanning Zhang and Yao 2026, Takashima et al. 2022, Matsumoto et al. 2024, and Wang et al. 2024 for models or experiments coupling NiTi superelasticity/phase transformation with inter-wire contact, Coulomb slip, confinement pressure, hysteresis, and bending stiffness.']
- **named_sources:** ['Bai et al. 2022 — Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming — 10.3390/app12073582', 'Liu et al. 2021 — A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots — 10.1109/LRA.2021.3097255', 'Zhang and Yao 2026 — A variable stiffness omnidirectional chain based on positive-pressure fiber jamming — 10.5194/ms-17-481-2026', 'Takashima et al. 2022 — Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon — 10.20965/jrm.2022.p0466', 'Matsumoto et al. 2024 — Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon — 10.1299/mej.24-00130', 'Wang et al. 2024 — Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm — 10.1108/IR-11-2023-0305']
- **reopen_broad_search:** False

## Recommended next action

Reject C1-C4 as novelty claims and remove C8 from the primary contribution. Reframe MP1 around C7: a falsifiable comparison between an elastic-fiber positive-pressure model and a superelastic NiTi contact/slip model, supported by bending experiments across pressure, curvature, and transformation regime. First perform only the specified T1-T3 backward/forward citation chasing. Kill the pivot if that chase finds direct positive-pressure NiTi wire-jamming mechanics, or if the NiTi system can be explained by the existing elastic-fiber framework using only substituted modulus and friction parameters.

## Provenance

- AUDIT_PROTOCOL — docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md — SHA256 a4022362286cde0c6a5764ab0cea7e7c37449bec54059b3e56a592d43d1e0173
- FULL_TEXT_EVIDENCE_MATRIX — outputs/verification/MP1-V001/verification_matrix.json — SHA256 84c3499d5318fd952466f5ec27d9c09fa5e03a001f9170e943d3e2fe9d4839d0
