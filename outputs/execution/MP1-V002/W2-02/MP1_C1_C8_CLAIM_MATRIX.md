# MP1 C1–C8 Claim Reconstruction Matrix

> **Task ID:** MP1-E1-W2-02  
> **Scope:** READ-ONLY historical claim reconstruction (Clarifications C-01, C-02, C-03, C-04)  
> **Target:** C1–C8 claims derived from MP1-V001 through MP1-V002 Stage 6  

## 1. Executive Summary Table

| ID | Claim Label | Origin | Verdict (`claim_verdict`) | Decision (`decision`) | Status | Strongest Prior Art Threat |
|---|---|---|---|---|---|---|
| **C1** | Wire/Fiber Jamming for Variable Stiffness | `WORKFLOW` | `CLOSED` | `REJECT` | `VERIFIED` | Bai et al. (2022) [240fbf6022] |
| **C2** | Positive-Pressure Jamming for Variable Stiffness | `WORKFLOW` | `CLOSED` | `REJECT` | `VERIFIED` | Liu et al. (2021) [182d854610] |
| **C3** | SMA and Jamming Co-existence in Variable-Stiffness Structure | `WORKFLOW` | `CLOSED` | `REJECT` | `VERIFIED` | Takashima et al. (2022) [2cd907e77a] |
| **C4** | Onboard/Compact Pressure Source for Jamming | `WORKFLOW` | `CLOSED` | `REJECT` | `VERIFIED` | Huynh et al. (2022) [bbe88a0c04] |
| **C5** | Superelastic NiTi Wires Themselves as Frictional Jamming Medium | `WORKFLOW` | `CLOSED` | `REJECT` | `VERIFIED` | Vahidi et al. (2022) [53200aa0c6] |
| **C6** | Positive-Pressure Confinement of Superelastic NiTi Wire Bundle | `WORKFLOW` | `NARROWED` | `REFORMULATE` | `VERIFIED` | Tjahjanto, Tyrberg, and Mullins (2017) [ccdc1bb980] |
| **C7** | Coupling of NiTi Superelasticity, Inter-Wire Friction, Pressure, and Bending Stiffness | `WORKFLOW` | `NARROWED` | `REFORMULATE` | `VERIFIED` | Carboni & Lacarbonara (2016) [40760daa02] |
| **C8** | SMA-Driven Syringe/Piston Powering Jamming Pressure | `MENTOR` | `SUBSTANTIALLY_PREEMPTED` | `REJECT` | `VERIFIED` | Wang et al. (2024) [c6a31066f8] |

---

## 2. Detailed Claim Dossiers

### C1: Wire/Fiber Jamming for Variable Stiffness

- **Original Claim Text:** "Wire/fiber jamming for variable stiffness is novel."
- **Normalized Claim Text:** "Variable bending stiffness achieved via frictional jamming of metallic or synthetic wire/fiber bundles."
- **Origin:** `WORKFLOW` (docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md)
- **First Appearance:** Stage `S02 (Phase 10/11)` (commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`)
- **Claim Verdict:** `CLOSED` | **Decision:** `REJECT` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Current Canonical Status:** `CLOSED`
- **Scientific Category:** structural_mechanics | **Novelty Category:** device_level_principle

#### Historical Stage Progression
| Stage | Exact Commit | Status at Stage |
|---|---|---|
| `S02` | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | `ACTIVE_UNDER_AUDIT` |
| `S03` | `3d152e951711a15d9f86946df99f22785a8be9a4` | `UNDER_EVALUATION` |
| `S04` | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | `CLOSED` |
| `S12` | `3a216d680b6e5d4c263121afee0577ac86e530ac` | `CLOSED_CONFIRMED` |
| `S16` | `0ade68e73d93c38618b366a000ac7a01215a3936` | `CLOSED_ARCHIVED` |

#### Prior Art Threat & Evidence Base
- **Search Conducted:** `MP1-V001 core prior-art search across IEEE, MDPI, and Copernicus publications.` (File: `outputs/verification/MP1-V001/verification_matrix.json`, Commit: `3d152e951711a15d9f86946df99f22785a8be9a4`)
- **Strongest Threat:** Bai et al. (2022) — *Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming* (DOI: 10.3390/app12073582)

##### Source Papers
- **Bai et al. (2022)** — *Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming*
  - Paper ID: `240fbf6022` | DOI: [10.3390/app12073582](https://doi.org/10.3390/app12073582) | Path: `data/papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`
  - **What Source Actually Proves:** Frictional wire jamming yields tunable bending stiffness under negative pressure.
  - **What Source Does Not Prove:** Does not evaluate superelastic alloys.
- **Zhang & Yao (2026)** — *A variable stiffness omnidirectional chain based on positive-pressure fiber jamming*
  - Paper ID: `3aa8790db0` | DOI: [10.5194/ms-17-481-2026](https://doi.org/10.5194/ms-17-481-2026) | Path: `data/papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf`
  - **What Source Actually Proves:** Models and experimentally confirms 3-regime friction mechanics (jammed, transition, slipping) in a 700-fiber nylon bundle under positive confinement pressure up to 300 kPa.
  - **What Source Does Not Prove:** Does not examine metallic superelasticity or phase transformation.

#### Scientific & Systematic Impact
- **Claim Evolution:** `Wire/fiber jamming for variable stiffness is novel.` $\rightarrow$ `Wire/fiber jamming is established prior art; device-level novelty rejected.`
- **Reason for Change:** Direct prior art in Bai et al. (2022) and Zhang & Yao (2026) fully demonstrates the working principle and mechanics of wire/fiber jamming.
- **Scientific Consequence:** Forced abandonment of generic wire-jamming claims; project cannot claim novelty merely by using a bundle of wires.
- **System Novelty Impact:** FATAL_PREEMPTION
- **Mechanism Novelty Impact:** PREEMPTED_AT_EXISTENCE_LEVEL
- **Implementation Novelty Impact:** HIGH_PRIOR_ART
- **Feasibility Impact:** Confirms mechanical viability of wire jamming, but eliminates patentable or novel device claims.
- **Pivot Relevance:** Direct trigger for PIVOT_TO_MECHANICS_CORE in MP1-V001.

#### Epistemological Evolution
- **Historical Interpretation:** At V001 (S04), classified as directly closed. At Stage 3 (S12), confirmed as robust closure with residual caveat that material changes do not restore novelty.
- **Superseded Interpretation:** Initial belief at proposal that wire jamming was an unexploited mechanism.
- **Corrected Interpretation:** Wire jamming is established prior art; material substitution to NiTi only matters if new mechanics arise.
- **Contradiction Candidate IDs:** `[]`
- **Provenance:** `{"audit_file": "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json", "remediation_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W02_C1_C4_ROBUST_CLOSURES.md"}`

---

### C2: Positive-Pressure Jamming for Variable Stiffness

- **Original Claim Text:** "Positive-pressure jamming for variable stiffness is novel."
- **Normalized Claim Text:** "Variable stiffness achieved by applying positive fluid confinement pressure to compress jamming media."
- **Origin:** `WORKFLOW` (docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md)
- **First Appearance:** Stage `S02 (Phase 10/11)` (commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`)
- **Claim Verdict:** `CLOSED` | **Decision:** `REJECT` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Current Canonical Status:** `CLOSED`
- **Scientific Category:** fluid_structure_mechanics | **Novelty Category:** boundary_condition_concept

#### Historical Stage Progression
| Stage | Exact Commit | Status at Stage |
|---|---|---|
| `S02` | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | `ACTIVE_UNDER_AUDIT` |
| `S03` | `3d152e951711a15d9f86946df99f22785a8be9a4` | `UNDER_EVALUATION` |
| `S04` | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | `CLOSED` |
| `S12` | `3a216d680b6e5d4c263121afee0577ac86e530ac` | `CLOSED_CONFIRMED` |
| `S16` | `0ade68e73d93c38618b366a000ac7a01215a3936` | `CLOSED_ARCHIVED` |

#### Prior Art Threat & Evidence Base
- **Search Conducted:** `MP1-V001 core prior-art search on positive pressure soft robotics jamming.` (File: `outputs/verification/MP1-V001/verification_matrix.json`, Commit: `3d152e951711a15d9f86946df99f22785a8be9a4`)
- **Strongest Threat:** Liu et al. (2021) — *A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots* (DOI: 10.1109/LRA.2021.3097255)

##### Source Papers
- **Liu et al. (2021)** — *A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots*
  - Paper ID: `182d854610` | DOI: [10.1109/LRA.2021.3097255](https://doi.org/10.1109/LRA.2021.3097255) | Path: `data/papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`
  - **What Source Actually Proves:** Positive fluid pressure enables stiffness variation well beyond vacuum limits.
  - **What Source Does Not Prove:** Does not study metallic wire friction or superelasticity.
- **Zhang & Yao (2026)** — *A variable stiffness omnidirectional chain based on positive-pressure fiber jamming*
  - Paper ID: `3aa8790db0` | DOI: [10.5194/ms-17-481-2026](https://doi.org/10.5194/ms-17-481-2026) | Path: `data/papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf`
  - **What Source Actually Proves:** Directly confines a fiber bundle using positive pressure (0–300 kPa) and derives the pressure-dependent slip onset equation.
  - **What Source Does Not Prove:** Does not use superelastic NiTi wires.

#### Scientific & Systematic Impact
- **Claim Evolution:** `Positive-pressure jamming for variable stiffness is novel.` $\rightarrow$ `Positive-pressure jamming is established prior art; concept-level novelty rejected.`
- **Reason for Change:** Direct prior art in Liu et al. (2021) and Zhang & Yao (2026) demonstrates positive-pressure granular and fiber jamming exceeding atmospheric limits.
- **Scientific Consequence:** Positive pressure is recognized as an alternative boundary condition, not an unestablished physics principle.
- **System Novelty Impact:** FATAL_PREEMPTION
- **Mechanism Novelty Impact:** PREEMPTED_AT_CONCEPT_LEVEL
- **Implementation Novelty Impact:** HIGH_PRIOR_ART
- **Feasibility Impact:** Validates that positive pressure is feasible and effective, but cannot form the basis of a novelty claim.
- **Pivot Relevance:** Direct trigger for PIVOT_TO_MECHANICS_CORE in MP1-V001.

#### Epistemological Evolution
- **Historical Interpretation:** Closed at V001 (S04). Confirmed as robust closure at Stage 3 (S12) with residual caveat that changing pressurization media does not create novelty.
- **Superseded Interpretation:** Belief that exceeding atmospheric pressure via positive pressurization constituted novel mechanics.
- **Corrected Interpretation:** Positive pressure is an established loading condition; contact equations naturally accept positive normal pressure.
- **Contradiction Candidate IDs:** `[]`
- **Provenance:** `{"audit_file": "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json", "remediation_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W02_C1_C4_ROBUST_CLOSURES.md"}`

---

### C3: SMA and Jamming Co-existence in Variable-Stiffness Structure

- **Original Claim Text:** "SMA and jamming in the same variable-stiffness device is novel."
- **Normalized Claim Text:** "Simultaneous integration of shape memory alloy (SMA) elements and jamming mechanisms within the same variable-stiffness robotic structure."
- **Origin:** `WORKFLOW` (docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md)
- **First Appearance:** Stage `S02 (Phase 10/11)` (commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`)
- **Claim Verdict:** `CLOSED` | **Decision:** `REJECT` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Current Canonical Status:** `CLOSED`
- **Scientific Category:** smart_materials_integration | **Novelty Category:** multi_functional_integration

#### Historical Stage Progression
| Stage | Exact Commit | Status at Stage |
|---|---|---|
| `S02` | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | `ACTIVE_UNDER_AUDIT` |
| `S03` | `3d152e951711a15d9f86946df99f22785a8be9a4` | `UNDER_EVALUATION` |
| `S04` | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | `CLOSED` |
| `S12` | `3a216d680b6e5d4c263121afee0577ac86e530ac` | `CLOSED_CONFIRMED` |
| `S16` | `0ade68e73d93c38618b366a000ac7a01215a3936` | `CLOSED_ARCHIVED` |

#### Prior Art Threat & Evidence Base
- **Search Conducted:** `MP1-V001 core prior-art search across IEEE, RSJ, and JSME publications on SMA and jamming integration.` (File: `outputs/verification/MP1-V001/verification_matrix.json`, Commit: `3d152e951711a15d9f86946df99f22785a8be9a4`)
- **Strongest Threat:** Takashima et al. (2022) — *Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon* (DOI: 10.20965/jrm.2022.p0466)

##### Source Papers
- **Takashima et al. (2022)** — *Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon*
  - Paper ID: `2cd907e77a` | DOI: [10.20965/jrm.2022.p0466](https://doi.org/10.20965/jrm.2022.p0466) | Path: `data/papers/verification/MP1-V001/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf`
  - **What Source Actually Proves:** Co-existence of SMA wires and granular jamming in a variable-stiffness robotic link.
  - **What Source Does Not Prove:** Does not use NiTi wires as the jamming medium.
- **Matsumoto et al. (2024)** — *Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon*
  - Paper ID: `7ce492505d` | DOI: [10.1299/mej.24-00130](https://doi.org/10.1299/mej.24-00130) | Path: `data/papers/verification/MP1-V001/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf`
  - **What Source Actually Proves:** Characterizes R-phase transformation speed of Ti-Ni wires embedded inside a jamming transition link.
  - **What Source Does Not Prove:** Does not study inter-NiTi contact friction.

#### Scientific & Systematic Impact
- **Claim Evolution:** `SMA and jamming in the same variable-stiffness device is novel.` $\rightarrow$ `Co-existence of SMA and jamming in the same device is established prior art; device-level integration novelty rejected.`
- **Reason for Change:** Takashima lineage (2022–2026) and Matsumoto et al. (2024) extensively published the co-integration of SMA wires and jamming transitions.
- **Scientific Consequence:** Must separate device-level co-existence (closed) from inter-wire contact mechanics (re-routed to C5/C7/T1).
- **System Novelty Impact:** FATAL_PREEMPTION
- **Mechanism Novelty Impact:** PREEMPTED_AT_DEVICE_LEVEL
- **Implementation Novelty Impact:** HIGH_PRIOR_ART
- **Feasibility Impact:** Confirms practical feasibility of combining SMA and jamming, but bars whole-device novelty.
- **Pivot Relevance:** Key architectural pre-emption forcing the pivot to mechanics core in MP1-V001.

#### Epistemological Evolution
- **Historical Interpretation:** Closed at V001 (S04). Confirmed as robust closure at Stage 3 (S12) with explicit clarification separating SMA backbone from NiTi contact network.
- **Superseded Interpretation:** Belief that pairing an SMA element with a jamming element constituted a novel robotic architecture.
- **Corrected Interpretation:** Co-existence is well-established prior art; scientific interest only survives if NiTi wires themselves form the contact network.
- **Contradiction Candidate IDs:** `[]`
- **Provenance:** `{"audit_file": "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json", "remediation_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W02_C1_C4_ROBUST_CLOSURES.md"}`

---

### C4: Onboard/Compact Pressure Source for Jamming

- **Original Claim Text:** "An onboard/compact pressure source for jamming is novel."
- **Normalized Claim Text:** "Generation or modulation of jamming confinement pressure using an embedded, compact, or onboard micropump or actuator mechanism."
- **Origin:** `WORKFLOW` (docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md)
- **First Appearance:** Stage `S02 (Phase 10/11)` (commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`)
- **Claim Verdict:** `CLOSED` | **Decision:** `REJECT` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Current Canonical Status:** `CLOSED`
- **Scientific Category:** mechatronic_integration | **Novelty Category:** subsystem_engineering

#### Historical Stage Progression
| Stage | Exact Commit | Status at Stage |
|---|---|---|
| `S02` | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | `ACTIVE_UNDER_AUDIT` |
| `S03` | `3d152e951711a15d9f86946df99f22785a8be9a4` | `UNDER_EVALUATION` |
| `S04` | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | `CLOSED` |
| `S12` | `3a216d680b6e5d4c263121afee0577ac86e530ac` | `CLOSED_CONFIRMED` |
| `S16` | `0ade68e73d93c38618b366a000ac7a01215a3936` | `CLOSED_ARCHIVED` |

#### Prior Art Threat & Evidence Base
- **Search Conducted:** `MP1-V001 core prior-art search across IEEE and Elsevier publications on embedded pumps and compact jamming pressure generators.` (File: `outputs/verification/MP1-V001/verification_matrix.json`, Commit: `3d152e951711a15d9f86946df99f22785a8be9a4`)
- **Strongest Threat:** Huynh et al. (2022) — *Bidirectional flexible electro-conjugate fluid (ECF) micropump for soft actuators* (DOI: 10.1016/j.sna.2022.113449)

##### Source Papers
- **Huynh et al. (2022)** — *Bidirectional flexible electro-conjugate fluid (ECF) micropump for soft actuators*
  - Paper ID: `bbe88a0c04` | DOI: [10.1016/j.sna.2022.113449](https://doi.org/10.1016/j.sna.2022.113449) | Path: `data/papers/verification/MP1-V001/2022-Bidirectional flexible electro-conjugate fluid micropump.pdf`
  - **What Source Actually Proves:** Directly integrates a micropump inside an actuator to activate jamming locally.
  - **What Source Does Not Prove:** Does not study NiTi wire bundles.
- **Wang et al. (2024)** — *Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm*
  - Paper ID: `c6a31066f8` | DOI: [10.1108/IR-11-2023-0305](https://doi.org/10.1108/IR-11-2023-0305) | Path: `data/papers/verification/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf`
  - **What Source Actually Proves:** Presents a compact modular motorized ball-screw piston mechanism directly mounted on a soft arm to compress jamming particles.
  - **What Source Does Not Prove:** Does not use shape memory alloy actuation.

#### Scientific & Systematic Impact
- **Claim Evolution:** `An onboard/compact pressure source for jamming is novel.` $\rightarrow$ `Onboard and compact jamming pressure generators are established prior art; subsystem novelty rejected.`
- **Reason for Change:** Embedded micropumps (Huynh 2022) and motorized piston mechanisms (Wang 2024) directly establish compact local pressure generation for jamming.
- **Scientific Consequence:** Compact pressure sourcing is an engineering integration challenge, not a fundamental mechanics contribution.
- **System Novelty Impact:** FATAL_PREEMPTION
- **Mechanism Novelty Impact:** PREEMPTED_AT_SUBSYSTEM_LEVEL
- **Implementation Novelty Impact:** HIGH_PRIOR_ART
- **Feasibility Impact:** Confirms engineering tractability of compact pressure sources, but eliminates it as a novelty anchor.
- **Pivot Relevance:** Key contributor to the decision in MP1-V001 to abandon mechatronic integration claims.

#### Epistemological Evolution
- **Historical Interpretation:** Closed at V001 (S04). Confirmed as robust closure at Stage 3 (S12) with clarification that 'compact' does not imply untethered autonomy.
- **Superseded Interpretation:** Belief that designing a compact pump or piston mechanism for jamming constituted MSc research novelty.
- **Corrected Interpretation:** Compact pressure sources are engineering integration solutions without new mechanics content.
- **Contradiction Candidate IDs:** `[]`
- **Provenance:** `{"audit_file": "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json", "remediation_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W02_C1_C4_ROBUST_CLOSURES.md"}`

---

### C5: Superelastic NiTi Wires Themselves as Frictional Jamming Medium

- **Original Claim Text:** "Superelastic NiTi wires themselves as the frictional jamming medium remain open."
- **Normalized Claim Text:** "Use of superelastic NiTi wires as the mutual contacting, frictionally slipping, and load-bearing jamming elements in a variable-stiffness bundle."
- **Origin:** `WORKFLOW` (docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md)
- **First Appearance:** Stage `S02 (Phase 10/11)` (commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`)
- **Claim Verdict:** `CLOSED` | **Decision:** `REJECT` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Current Canonical Status:** `CLOSED`
- **Scientific Category:** contact_mechanics_materials | **Novelty Category:** material_substitution

#### Historical Stage Progression
| Stage | Exact Commit | Status at Stage |
|---|---|---|
| `S02` | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | `ACTIVE_UNDER_AUDIT` |
| `S03` | `3d152e951711a15d9f86946df99f22785a8be9a4` | `UNDER_EVALUATION` |
| `S04` | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | `OPEN_IN_SUPPLIED_CORPUS` |
| `S06` | `e9685a65263635cffd4d946e8763c3417b59eb0d` | `CLOSED_AT_EXISTENCE_LEVEL_MAPPED_TO_T1` |
| `S11` | `UNKNOWN` | `CONFIRMED_PREEMPTED_BY_16_PAPERS` |
| `S12` | `3a216d680b6e5d4c263121afee0577ac86e530ac` | `BOUNDARY_REPAIRED_CLOSED_ROBUSTLY` |
| `S16` | `0ade68e73d93c38618b366a000ac7a01215a3936` | `CLOSED_ARCHIVED` |

#### Prior Art Threat & Evidence Base
- **Search Conducted:** `MP1-V001 supplied corpus audit followed by MP1-V002 targeted citation chase on NiTi wire ropes, cables, and strands.` (File: `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`, Commit: `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d`)
- **Strongest Threat:** Vahidi et al. (2022) — *Mechanical response of single and double-helix SMA wire ropes* (DOI: 10.1080/15376494.2021.1955313)

##### Source Papers
- **Vahidi et al. (2022)** — *Mechanical response of single and double-helix SMA wire ropes*
  - Paper ID: `53200aa0c6` | DOI: [10.1080/15376494.2021.1955313](https://doi.org/10.1080/15376494.2021.1955313) | Path: `data/papers/verification/MP1-V002/2022-Mechanical response of single and double-helix SMA wire ropes.pdf`
  - **What Source Actually Proves:** Multiwire NiTi ropes exhibit inter-wire contact and friction during mechanical deformation.
  - **What Source Does Not Prove:** Does not study actively varied fluid confinement pressure.
- **Carboni & Lacarbonara (2016)** — *Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments*
  - Paper ID: `40760daa02` | DOI: [10.1061/(ASCE)EM.1943-7889.0001072](https://doi.org/10.1061/(ASCE)EM.1943-7889.0001072) | Path: `data/papers/verification/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis.pdf`
  - **What Source Actually Proves:** Demonstrates pinched hysteresis and amplitude-dependent stiffness in Nitinol wire assemblies due to combined inter-wire friction and phase transformation.
  - **What Source Does Not Prove:** Does not examine external positive pressure.
- **Falcetelli et al. (2024)** — *Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes*
  - Paper ID: `1c81b2d35c` | DOI: [10.1007/s11340-024-01053-5](https://doi.org/10.1007/s11340-024-01053-5) | Path: `data/papers/verification/MP1-V002/2024-Experimental-Numerical Assessment of Mechanical Behavior of Steel and NiTi Ropes.pdf`
  - **What Source Actually Proves:** Direct head-to-head comparison of steel vs NiTi wire ropes under cyclic tension, proving inter-wire friction and contact damping in NiTi assemblies.
  - **What Source Does Not Prove:** Does not study pressure-controlled bending.

#### Scientific & Systematic Impact
- **Claim Evolution:** `Superelastic NiTi wires themselves as the frictional jamming medium remain open.` $\rightarrow$ `Inter-wire contact and frictional dissipation in multiwire NiTi assemblies is established prior art; broad claim closed.`
- **Reason for Change:** Extensive literature on NiTi wire ropes and strands (Vahidi 2022, Carboni 2015/2016, Falcetelli 2024) proves that inter-wire friction and slipping in NiTi bundles is already well-studied.
- **Scientific Consequence:** Material substitution alone cannot establish novelty; switching from twisted cables to parallel bundles is not a distinct mechanics principle.
- **System Novelty Impact:** FATAL_PREEMPTION
- **Mechanism Novelty Impact:** PREEMPTED_AT_EXISTENCE_LEVEL
- **Implementation Novelty Impact:** HIGH_PRIOR_ART
- **Feasibility Impact:** Confirms that NiTi wires can slide and dissipate energy, but eliminates novelty based solely on NiTi material choice.
- **Pivot Relevance:** Drove the transition in V002 from Target T1 to Target T2/T3.

#### Epistemological Evolution
- **Historical Interpretation:** Open in V001 (S04) because V001 papers did not use NiTi. In V002 (S06/S12), robustly closed by Target T1 evidence showing NiTi contact and friction is old art.
- **Superseded Interpretation:** Belief that using NiTi as a frictionally slipping jamming element was an unaddressed scientific gap.
- **Corrected Interpretation:** NiTi inter-wire friction is established; novelty can only exist if active confinement pressure alters the constitutive-contact coupling.
- **Contradiction Candidate IDs:** `['CONTRA-03']`
- **Provenance:** `{"audit_file": "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json", "threat_file": "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json", "remediation_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W03_C5_C8_BOUNDARY_REPAIR.md"}`

---

### C6: Positive-Pressure Confinement of Superelastic NiTi Wire Bundle

- **Original Claim Text:** "Positive-pressure confinement of a superelastic NiTi wire bundle remains open."
- **Normalized Claim Text:** "Direct external application of positive fluid or membrane confinement pressure to radially compress a superelastic NiTi wire bundle to modulate stiffness."
- **Origin:** `WORKFLOW` (docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md)
- **First Appearance:** Stage `S02 (Phase 10/11)` (commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`)
- **Claim Verdict:** `NARROWED` | **Decision:** `REFORMULATE` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Current Canonical Status:** `NARROWED`
- **Scientific Category:** contact_mechanics_boundary_conditions | **Novelty Category:** experimental_loading_protocol

#### Historical Stage Progression
| Stage | Exact Commit | Status at Stage |
|---|---|---|
| `S02` | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | `ACTIVE_UNDER_AUDIT` |
| `S03` | `3d152e951711a15d9f86946df99f22785a8be9a4` | `UNDER_EVALUATION` |
| `S04` | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | `OPEN_IN_SUPPLIED_CORPUS` |
| `S06` | `e9685a65263635cffd4d946e8763c3417b59eb0d` | `MAPPED_TO_T2_OPEN_IN_FULL_TEXT_SET` |
| `S10` | `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d` | `CHALLENGED_BY_ASTRA_G02` |
| `S12` | `3a216d680b6e5d4c263121afee0577ac86e530ac` | `DEMOTED_TO_EXPERIMENTAL_BOUNDARY_CONDITION` |
| `S16` | `0ade68e73d93c38618b366a000ac7a01215a3936` | `CLOSED_ARCHIVED` |

#### Prior Art Threat & Evidence Base
- **Search Conducted:** `MP1-V002 targeted threat audit across subsea cables, wire ropes, and pressurized bundles.` (File: `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`, Commit: `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d`)
- **Strongest Threat:** Tjahjanto, Tyrberg, and Mullins (2017) — *Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable* (DOI: 10.1115/OMAE2017-61198)

##### Source Papers
- **Tjahjanto et al. (2017)** — *Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable*
  - Paper ID: `ccdc1bb980` | DOI: [10.1115/OMAE2017-61198](https://doi.org/10.1115/OMAE2017-61198) | Path: `data/papers/verification/MP1-V002/2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf`
  - **What Source Actually Proves:** Radial confinement pressure directly shifts inter-wire contact pressure and bending stick-slip thresholds in cables.
  - **What Source Does Not Prove:** Does not use NiTi or actively vary pressure during operation.
- **Xin Liu (2013)** — *Cable Vibration Considering Internal Friction*
  - Paper ID: `aaad9c248c` | DOI: [](https://doi.org/) | Path: `data/papers/verification/MP1-V002/2013-Cable Vibration Considering Internal Friction.pdf`
  - **What Source Actually Proves:** Derives layer-by-layer radial contact pressure Pi and demonstrates that radial pressure dictates interlayer friction and curvature-dependent bending rigidity.
  - **What Source Does Not Prove:** Pressure is passive/helix-induced, not externally controlled.
- **Barsi, Carboni, and Lacarbonara (2025)** — *A new mechanical model of short wire ropes: Theory and experimental validation*
  - Paper ID: `9f4295be23` | DOI: [10.1016/j.engstruct.2024.119217](https://doi.org/10.1016/j.engstruct.2024.119217) | Path: `data/papers/verification/MP1-V002/2025-A new mechanical model of short wire ropes.pdf`
  - **What Source Actually Proves:** Shear-deformable beam model with internal contact friction; incremental equilibrium equations naturally accommodate transverse loading.
  - **What Source Does Not Prove:** Does not study actively pressurized NiTi bundles.

#### Scientific & Systematic Impact
- **Claim Evolution:** `Positive-pressure confinement of a superelastic NiTi wire bundle creates an unaddressed class of mechanics.` $\rightarrow$ `Positive pressure is an experimental boundary condition; existing incremental contact formulations accommodate p(t) without new physical laws.`
- **Reason for Change:** Astra critique G02 and remediation worker W05 proved that incremental contact-friction equations (f_t <= mu * f_n(p)) naturally accept time-varying pressure p(t).
- **Scientific Consequence:** P3 is demoted from a 'mechanics principle' to an 'experimental control protocol'. Novelty cannot be claimed based on pressure adjustability alone.
- **System Novelty Impact:** PREEMPTED_AT_CONCEPT_LEVEL
- **Mechanism Novelty Impact:** NARROWED_TO_BOUNDARY_CONDITION
- **Implementation Novelty Impact:** FEASIBLE_BUT_NOT_NOVEL
- **Feasibility Impact:** Requires careful independent calibration of pressure-to-contact-force transmission (membrane and arching effects).
- **Pivot Relevance:** Key correction in Stage 3 preventing false claim of mechanics novelty based on active pressure.

#### Epistemological Evolution
- **Historical Interpretation:** Treated as candidate mechanics novelty in early V002 (S05/S06). Remediated in Stage 3 (S12) into a boundary condition for testing existing models.
- **Superseded Interpretation:** Belief that varying pressure dynamically (P3) constituted a distinct mechanical theory separate from fixed preload (P2) or passive preload (P1).
- **Corrected Interpretation:** P1, P2, P3 are loading protocols, not distinct mechanics laws; contact equations naturally accept p(t).
- **Contradiction Candidate IDs:** `['CONTRA-05']`
- **Provenance:** `{"audit_file": "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json", "threat_file": "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json", "critique_file": "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md", "remediation_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W05_T2_MECHANICS_P1_P2_P3_TEST.md"}`

---

### C7: Coupling of NiTi Superelasticity, Inter-Wire Friction, Pressure, and Bending Stiffness

- **Original Claim Text:** "Coupling among NiTi superelastic response, inter-wire slip/friction, pressure and bending stiffness remains open."
- **Normalized Claim Text:** "Coupled mechanics governing how stress-induced phase transformation, inter-wire stick-slip contact, and external confinement pressure interact to determine composite bending stiffness and hysteresis."
- **Origin:** `WORKFLOW` (docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md)
- **First Appearance:** Stage `S02 (Phase 10/11)` (commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`)
- **Claim Verdict:** `NARROWED` | **Decision:** `REFORMULATE` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Current Canonical Status:** `NARROWED`
- **Scientific Category:** coupled_mechanics | **Novelty Category:** constitutive_contact_interaction

#### Historical Stage Progression
| Stage | Exact Commit | Status at Stage |
|---|---|---|
| `S02` | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | `ACTIVE_UNDER_AUDIT` |
| `S03` | `3d152e951711a15d9f86946df99f22785a8be9a4` | `UNDER_EVALUATION` |
| `S04` | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | `OPEN_IN_SUPPLIED_CORPUS` |
| `S06` | `e9685a65263635cffd4d946e8763c3417b59eb0d` | `MAPPED_TO_T3_SUBSTANTIALLY_PREEMPTED` |
| `S10` | `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d` | `CHALLENGED_BY_ASTRA_G01_G03_G04` |
| `S12` | `3a216d680b6e5d4c263121afee0577ac86e530ac` | `REFORMULATED_AS_MODEL_DISCRIMINATION_HYPOTHESIS` |
| `S16` | `0ade68e73d93c38618b366a000ac7a01215a3936` | `CLOSED_ARCHIVED` |

#### Prior Art Threat & Evidence Base
- **Search Conducted:** `MP1-V001 and MP1-V002 targeted searches on SMA cables, hysteretic damping, and frictional multiwire assemblies.` (File: `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`, Commit: `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d`)
- **Strongest Threat:** Carboni & Lacarbonara (2016) — *Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments* (DOI: 10.1061/(ASCE)EM.1943-7889.0001072)

##### Source Papers
- **Carboni & Lacarbonara (2016)** — *Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments*
  - Paper ID: `40760daa02` | DOI: [10.1061/(ASCE)EM.1943-7889.0001072](https://doi.org/10.1061/(ASCE)EM.1943-7889.0001072) | Path: `data/papers/verification/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis.pdf`
  - **What Source Actually Proves:** Simultaneous inter-wire friction and phase transformation produce pinched hysteretic bending response.
  - **What Source Does Not Prove:** Does not modulate pressure as an active control parameter.
- **Vahidi et al. (2022)** — *Mechanical response of single and double-helix SMA wire ropes*
  - Paper ID: `53200aa0c6` | DOI: [10.1080/15376494.2021.1955313](https://doi.org/10.1080/15376494.2021.1955313) | Path: `data/papers/verification/MP1-V002/2022-Mechanical response of single and double-helix SMA wire ropes.pdf`
  - **What Source Actually Proves:** Directly couples 3D Auricchio SMA constitutive model with Coulomb friction contact formulation in Abaqus.
  - **What Source Does Not Prove:** Does not evaluate actively pressurized straight wire bundles in bending.
- **Silva et al. (2022)** — *NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings*
  - Paper ID: `6dd1ca94d1` | DOI: [10.3390/s22208045](https://doi.org/10.3390/s22208045) | Path: `data/papers/verification/MP1-V002/2022-NiTi SMA Superelastic Micro Cables.pdf`
  - **What Source Actually Proves:** Inter-filament friction causes self-heating, which shifts phase transformation stresses via Clausius-Clapeyron.
  - **What Source Does Not Prove:** Does not apply active fluid confinement.

#### Scientific & Systematic Impact
- **Claim Evolution:** `Coupling among NiTi superelastic response, inter-wire slip/friction, pressure, and bending stiffness is an unaddressed novel mechanics domain.` $\rightarrow$ `Coupling is partially pre-empted by existing NiTi-contact literature; survives only as an empirical hypothesis testing whether existing models predict pressure-controlled bending.`
- **Reason for Change:** Prior literature (Carboni 2016, Vahidi 2022, Silva 2022) already couples NiTi transformation with inter-wire contact and friction. Combining standard NiTi constitutive laws with standard Coulomb contact naturally produces coupled response without requiring a new constitutive law.
- **Scientific Consequence:** C7 cannot be claimed as a 'proven novel coupling theory'; it must be formulated as a model-discrimination question testing whether existing frameworks fail under active pressure.
- **System Novelty Impact:** PREEMPTED_AT_CONCEPT_LEVEL
- **Mechanism Novelty Impact:** NARROWED_TO_HYPOTHESIS_TESTING
- **Implementation Novelty Impact:** FEASIBLE_BUT_NOT_NOVEL
- **Feasibility Impact:** Requires local diagnostic instrumentation (DIC, FBG, thermal imaging) to separate phase transformation from friction and avoid parameter compensation.
- **Pivot Relevance:** Forms the ultimate surviving scientific core of MP1 after all architectural and material claims were stripped away.

#### Epistemological Evolution
- **Historical Interpretation:** Open in V001 (S04); substantially pre-empted in early V002 (S06); challenged by Astra (S10); remediated in Stage 3 (S12) into a model-discrimination hypothesis.
- **Superseded Interpretation:** Belief that the coexistence of 4 physical factors in one device demonstrated an unformulated branch of mechanics.
- **Corrected Interpretation:** Coupling naturally emerges from standard constitutive + contact equations; empirical testing must verify if standard models break down before claiming novelty.
- **Contradiction Candidate IDs:** `['CONTRA-02', 'CONTRA-03']`
- **Provenance:** `{"audit_file": "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json", "threat_file": "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json", "remediation_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W03_C5_C8_BOUNDARY_REPAIR.md"}`

---

### C8: SMA-Driven Syringe/Piston Powering Jamming Pressure

- **Original Claim Text:** "SMA-driven syringe/piston specifically powering the jamming pressure remains open."
- **Normalized Claim Text:** "Use of shape memory alloy wires, springs, or actuators to drive a piston or syringe to generate positive jamming fluid confinement pressure."
- **Origin:** `MENTOR` (docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md)
- **First Appearance:** Stage `S02 (Phase 10/11)` (commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`)
- **Claim Verdict:** `SUBSTANTIALLY_PREEMPTED` | **Decision:** `REJECT` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Current Canonical Status:** `SUBSTANTIALLY_PREEMPTED`
- **Scientific Category:** actuation_mechanism | **Novelty Category:** implementation_substitution

#### Historical Stage Progression
| Stage | Exact Commit | Status at Stage |
|---|---|---|
| `S02` | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | `ACTIVE_UNDER_AUDIT` |
| `S03` | `3d152e951711a15d9f86946df99f22785a8be9a4` | `UNDER_EVALUATION` |
| `S04` | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | `SUBSTANTIALLY_PREEMPTED` |
| `S12` | `3a216d680b6e5d4c263121afee0577ac86e530ac` | `SUBSTANTIALLY_PREEMPTED_CONFIRMED` |
| `S16` | `0ade68e73d93c38618b366a000ac7a01215a3936` | `CLOSED_ARCHIVED` |

#### Prior Art Threat & Evidence Base
- **Search Conducted:** `MP1-V001 prior-art search on SMA pumps, capsule micropumps, and piston jamming.` (File: `outputs/verification/MP1-V001/verification_matrix.json`, Commit: `3d152e951711a15d9f86946df99f22785a8be9a4`)
- **Strongest Threat:** Wang et al. (2024) — *Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm* (DOI: 10.1108/IR-11-2023-0305)

##### Source Papers
- **Pierce & Mascaro (2013)** — *A fluidic muscle actuator driven by a shape memory alloy pump*
  - Paper ID: `de64029540` | DOI: [10.1109/TMECH.2012.2211032](https://doi.org/10.1109/TMECH.2012.2211032) | Path: `data/papers/verification/MP1-V001/2013-A fluidic muscle actuator driven by a shape memory alloy pump.pdf`
  - **What Source Actually Proves:** Demonstrates that SMA thermal wire contraction effectively drives fluidic pumps to pressurize soft actuators.
  - **What Source Does Not Prove:** Does not apply fluid pressure specifically to a jamming bundle.
- **Kotb et al. (2021)** — *Design and analysis of a novel wireless shape memory alloy-actuated capsule micropump*
  - Paper ID: `55457a97c6` | DOI: [10.3390/mi12050520](https://doi.org/10.3390/mi12050520) | Path: `data/papers/verification/MP1-V001/2021-Design and analysis of a novel wireless shape memory alloy-actuated capsule micropump.pdf`
  - **What Source Actually Proves:** Develops a compact wireless SMA-actuated syringe/piston mechanism generating fluid pumping pressures.
  - **What Source Does Not Prove:** Targets medical drug delivery rather than robotic jamming.
- **Wang et al. (2024)** — *Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm*
  - Paper ID: `c6a31066f8` | DOI: [10.1108/IR-11-2023-0305](https://doi.org/10.1108/IR-11-2023-0305) | Path: `data/papers/verification/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf`
  - **What Source Actually Proves:** Piston-driven compression directly powers jamming stiffness change in soft robots.
  - **What Source Does Not Prove:** Uses electric motor actuation.

#### Scientific & Systematic Impact
- **Claim Evolution:** `SMA-driven syringe/piston specifically powering jamming pressure remains open.` $\rightarrow$ `SMA-driven syringe/piston is implementation substitution; component basis is substantially pre-empted.`
- **Reason for Change:** SMA fluid pumps (Pierce 2013, Kotb 2021) and piston-driven jamming mechanisms (Wang 2024) exist. Replacing an electric motor or solenoid with an SMA actuator is engineering implementation/actuator substitution.
- **Scientific Consequence:** C8 cannot carry the scientific contribution of an MSc thesis. Dropped from core research scope.
- **System Novelty Impact:** FATAL_PREEMPTION
- **Mechanism Novelty Impact:** ZERO_MECHANICS_CONTENT
- **Implementation Novelty Impact:** HIGH_PRIOR_ART
- **Feasibility Impact:** SMA thermal actuation introduces severe thermal lag, low cycling frequency, and hysteresis, reducing practical feasibility.
- **Pivot Relevance:** Key architectural factor abandoned during PIVOT_TO_MECHANICS_CORE in MP1-V001.

#### Epistemological Evolution
- **Historical Interpretation:** Substantially pre-empted at V001 (S04); confirmed as engineering substitution at Stage 3 (S12).
- **Superseded Interpretation:** Belief that pairing an SMA wire with a syringe to generate jamming pressure was a defensible novelty claim.
- **Corrected Interpretation:** Actuator substitution lacks fundamental mechanics content and imposes severe thermal bandwidth penalties.
- **Contradiction Candidate IDs:** `[]`
- **Provenance:** `{"audit_file": "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json", "remediation_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W03_C5_C8_BOUNDARY_REPAIR.md"}`

---
