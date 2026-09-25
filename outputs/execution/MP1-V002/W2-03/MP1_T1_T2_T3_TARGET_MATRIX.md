# MP1 T1/T2/T3 Mechanics Target Matrix

> **Task ID:** MP1-E1-W2-03  
> **Scope:** READ-ONLY Historical Target Reconstruction (Clarifications C-01, C-02, C-03, C-04, C-05)  

## 1. Executive Summary Table

| Target ID | Target Label | Initial Status (S05) | Status Post-Remediation (S12) | Canonical Status (S16) | Primary Threat Source |
|---|---|---|---|---|---|
| **T1** | Superelastic / NiTi / Nitinol metallic wires form the bundle... | `open_in_current_full_text_set` | `CLOSED_EXISTENCE_LEVEL_MAPPED_TO_H0b` | `CLOSED` | Vahidi et al. (2022) [53200aa0c6] |
| **T2** | Positive/internal/confining pressure radially or transversel... | `open_in_current_full_text_set` | `DEMOTED_TO_EXPERIMENTAL_BOUNDARY_CONDITION` | `NARROWED_TO_EXPERIMENTAL_BC` | Tjahjanto, Tyrberg, and Mullins (2017) [ccdc1bb980] |
| **T3** | Material coupling involving stress-induced martensitic trans... | `open_in_current_full_text_set` | `REFORMULATED_AS_H0b_DISCRIMINATION_HYPOTHESIS` | `REFORMULATED_TO_MODEL_DISCRIMINATION` | Carboni & Lacarbonara (2016) [40760daa02] |

---

## 2. Detailed Target Dossiers

### T1: Superelastic / NiTi / Nitinol metallic wires form the bundle itself, contact/slip against one another, friction is intentionally modulated, bundle stiffness changes.

- **Scientific Purpose:** Determine whether utilizing superelastic NiTi wires as the mutual contacting and frictionally slipping elements to achieve variable stiffness is an established physical phenomenon in literature.
- **Kill Condition:** Finding prior work where multiwire NiTi bundles, cables, ropes, or strands rely on inter-wire contact friction to alter stiffness or energy dissipation under external loading.
- **Canonical Status:** `CLOSED` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Status Evolution:** `open_in_current_full_text_set` $\rightarrow$ `CLOSED_CONFIRMED_AT_EXISTENCE_LEVEL` $\rightarrow$ `CLOSED_EXISTENCE_LEVEL_MAPPED_TO_H0b` $\rightarrow$ `CLOSED`
- **Remaining Uncertainty:** Inter-wire friction in NiTi bundles is thoroughly closed at the physical existence level; narrow remaining inquiry migrated to model discrimination (H0b).

#### Tested Prior Art Papers
- **Vahidi et al. (2022)** — *Mechanical response of single and double-helix SMA wire ropes*
  - Paper ID: `53200aa0c6` | DOI: [10.1080/15376494.2021.1955313](https://doi.org/10.1080/15376494.2021.1955313) | Path: `data/papers/verification/MP1-V002/2022-Mechanical response of single and double-helix SMA wire ropes.pdf`
  - **Method & Model:** 3D nonlinear finite element modeling (Abaqus UMAT) and simulation (Auricchio-Petrini 3D superelasticity + surface-to-surface penalty Coulomb friction)
  - **Loading & System:** Superelastic NiTi 1x27 and 7x7 wire ropes under Quasi-static axial tension
  - **What Source Proves:** Proves that multiwire NiTi bundles exhibit inter-wire contact normal forces, relative slip, and frictional dissipation that directly modify rope stiffness and hysteretic response.
  - **What Source Does Not Prove:** Does not apply an active fluid/membrane confinement pressure independent of axial tension.
- **Carboni et al. (2015)** — *Damping and Constitutive Response of Superelastic SMA Wire Ropes*
  - Paper ID: `90209df957` | DOI: [10.1061/(ASCE)EM.1943-7889.0000852](https://doi.org/10.1061/(ASCE)EM.1943-7889.0000852) | Path: `data/papers/verification/MP1-V002/2015-Damping and Constitutive Response of Superelastic SMA Wire Ropes.pdf`
  - **Method & Model:** Experimental cyclic testing and dynamic modeling (Modified Graesser constitutive model + friction damping)
  - **Loading & System:** NiTi7 and ST49 wire ropes under Cyclic tension and combined tension-bending (specimen S1a)
  - **What Source Proves:** Proves that cyclic deformation of NiTi wire ropes produces energy dissipation from both inter-wire friction and pseudoelastic hysteresis.
  - **What Source Does Not Prove:** Did not demonstrate pure cyclic bending of NiTi (S2a was steel, S1a required tension preload).
- **Reedlunn et al. (2013)** — *Superelastic shape memory alloy cables: Part I—isothermal tension experiments*
  - Paper ID: `00414aac4b` | DOI: [10.1016/j.ijsolstr.2013.05.028](https://doi.org/10.1016/j.ijsolstr.2013.05.028) | Path: `data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part I isothermal tension experiments.pdf`
  - **Method & Model:** Experimental testing and scanning electron microscopy (Costello wire rope kinematics)
  - **Loading & System:** 1x7, 1x19, 1x27, 7x7 superelastic NiTi cables under Isothermal quasi-static tension
  - **What Source Proves:** Proves mutual contacting and frictional interaction in NiTi multiwire bundles, revealing contact indentations and inter-wire wear.
  - **What Source Does Not Prove:** Does not test bending stiffness modulation via fluid jamming.

- **Provenance:** `{"source_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W04_T1_REAUDIT_CARBONI_CORRECTION.md", "commit": "3a216d680b6e5d4c263121afee0577ac86e530ac"}`

---

### T2: Positive/internal/confining pressure radially or transversely compresses a metallic wire bundle, increases inter-wire normal force/friction, changes bending/torsional/axial stiffness.

- **Scientific Purpose:** Determine whether applying external positive fluid or mechanical confinement pressure to compress a metallic/NiTi wire bundle to modulate stiffness constitutes a novel mechanics principle.
- **Kill Condition:** Finding prior work applying transverse/radial confining pressure to multi-element bundles, or demonstrating that pressure acts as an experimental boundary condition rather than a novel constitutive mechanism.
- **Canonical Status:** `NARROWED_TO_EXPERIMENTAL_BC` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Status Evolution:** `open_in_current_full_text_set` $\rightarrow$ `CRITIQUED_AS_BOUNDARY_CONDITION` $\rightarrow$ `DEMOTED_TO_EXPERIMENTAL_BOUNDARY_CONDITION` $\rightarrow$ `NARROWED_TO_EXPERIMENTAL_BC`
- **Remaining Uncertainty:** Soft robotic positive-pressure fluid confinement on NiTi bundles has no direct full-text match, but mathematically pressure enters as a standard boundary condition p(t) rather than a new constitutive principle.

#### Tested Prior Art Papers
- **Tjahjanto, Tyrberg, and Mullins (2017)** — *Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable*
  - Paper ID: `ccdc1bb980` | DOI: [10.1115/OMAE2017-61198](https://doi.org/10.1115/OMAE2017-61198) | Path: `data/papers/verification/MP1-V002/2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf`
  - **Method & Model:** Analytical and finite element beam bending formulation (Stick-slip friction beam mechanics with pressure-dependent normal force)
  - **Loading & System:** Dynamic submarine power cable with multi-component metallic cores and fillers under Cyclic bending under external radial contact pressure
  - **What Source Proves:** Proves that external radial confining pressure directly increases inter-element normal force, delaying slip and modulating dynamic flexural rigidity.
  - **What Source Does Not Prove:** Applies a constant radial pressure rather than actively varying pressure as a dynamic control input on NiTi.
- **Liu et al. (2021)** — *A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots*
  - Paper ID: `182d854610` | DOI: [10.1109/LRA.2021.3097255](https://doi.org/10.1109/LRA.2021.3097255) | Path: `data/papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`
  - **Method & Model:** Experimental fabrication and mechanical testing (Empirical pressure-stiffness scaling law)
  - **Loading & System:** Granular jamming chamber under positive pneumatic pressure (up to 200 kPa) under Cantilever bending and tensile stiffness modulation
  - **What Source Proves:** Proves positive pneumatic pressure modulates bending stiffness via normal confinement.
  - **What Source Does Not Prove:** Uses granular media instead of metallic NiTi wires.

- **Provenance:** `{"source_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W05_T2_MECHANICS_P1_P2_P3_TEST.md", "commit": "3a216d680b6e5d4c263121afee0577ac86e530ac"}`

---

### T3: Material coupling involving stress-induced martensitic transformation / superelastic plateau, hysteresis / recoverable strain, wire-wire contact, inter-wire slip/friction, confining pressure, structural stiffness.

- **Scientific Purpose:** Determine whether the simultaneous occurrence of NiTi martensitic phase transformation and inter-wire frictional slip yields coupled behavior that necessitates a brand-new constitutive coupling law.
- **Kill Condition:** Finding prior work demonstrating that existing transformation-aware constitutive models coupled with standard contact mechanics (H0b) adequately capture the response, or that coupling reduces to disjoint regimes.
- **Canonical Status:** `REFORMULATED_TO_MODEL_DISCRIMINATION` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Status Evolution:** `open_in_current_full_text_set` $\rightarrow$ `CRITIQUED_FOR_UNVERIFIED_COEXISTENCE_AND_H0_CONFUSION` $\rightarrow$ `REFORMULATED_AS_H0b_DISCRIMINATION_HYPOTHESIS` $\rightarrow$ `REFORMULATED_TO_MODEL_DISCRIMINATION`
- **Remaining Uncertainty:** Material coupling exists in literature; the sole open question is whether H0b is quantitatively sufficient or if a distinct coupling law H1 is required.

#### Tested Prior Art Papers
- **Carboni & Lacarbonara (2016)** — *Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments*
  - Paper ID: `40760daa02` | DOI: [10.1061/(ASCE)EM.1943-7889.0001072](https://doi.org/10.1061/(ASCE)EM.1943-7889.0001072) | Path: `data/papers/verification/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis.pdf`
  - **Method & Model:** Asymptotic analysis and experimental vibration testing (Multi-mechanism pinched hysteresis model combining Coulomb friction and phase transformation)
  - **Loading & System:** Nonlinear absorbers with NiTi wires exhibiting friction and superelasticity under Dynamic cyclic flexure
  - **What Source Proves:** Proves that combining NiTi phase transformation with frictional contact creates pinched hysteresis and amplitude-dependent flexural stiffness.
  - **What Source Does Not Prove:** Does not incorporate actively variable fluid confinement pressure.
- **Vahidi et al. (2022)** — *Mechanical response of single and double-helix SMA wire ropes*
  - Paper ID: `53200aa0c6` | DOI: [10.1080/15376494.2021.1955313](https://doi.org/10.1080/15376494.2021.1955313) | Path: `data/papers/verification/MP1-V002/2022-Mechanical response of single and double-helix SMA wire ropes.pdf`
  - **Method & Model:** Abaqus 3D FEA with Auricchio UMAT (Standard Auricchio model + Coulomb contact)
  - **Loading & System:** NiTi multiwire ropes under Tensile loading/unloading cycles
  - **What Source Proves:** Proves that existing transformation-aware models (H0b) coupled with Coulomb friction successfully capture the combined hysteretic response without a new coupling law.
  - **What Source Does Not Prove:** Did not explore variable radial pressure paths.

- **Provenance:** `{"source_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md", "commit": "3a216d680b6e5d4c263121afee0577ac86e530ac"}`

---
