# MP1 16-Paper Role & Evidence Matrix

> **Task ID:** MP1-E1-W2-04  
> **Scope:** READ-ONLY Canonical Full-Text Evidence Extraction (Clarifications C-01, C-02, C-03, C-04, C-05)  
> **Corpus:** `outputs/verification/MP1-V002/verification_matrix.json` (16 papers)  

## 1. Executive Summary Table

| Index | Paper ID | Authors (Year) | Title | Impact Type | Claims | Targets | Hypotheses | Primary Proved Finding |
|---|---|---|---|---|---|---|---|---|
| **01** | `00414aac4b` | Benjamin Reedlunn (2013) | *Superelastic shape memory alloy cables: Part ...* | `BOUNDS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that multiwire NiTi cables exhibit inter-wire contact... |
| **02** | `fac21c950e` | Benjamin Reedlunn (2013) | *Superelastic Shape Memory Alloy Cables: Part ...* | `BOUNDS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that shallow helix angle NiTi bundles behave closely ... |
| **03** | `40760daa02` | Biagio Carboni (2016) | *Nonlinear Vibration Absorber with Pinched Hys...* | `WEAKENS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that coupling of friction and NiTi superelasticity di... |
| **04** | `2f7fcf2f8f` | Cheng Fang (2019) | *Superelastic NiTi SMA cables: Thermal-mechani...* | `WEAKENS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that macroscopic phenomenological models can accurate... |
| **05** | `7f3f45407f` | Andrea Salvatore (2021) | *Nonlinear dynamic response of a wire rope iso...* | `BOUNDS` | `C1, C5` | `T1` | `H0a` | Proves that inter-wire friction in helical wire ropes produc... |
| **06** | `1c81b2d35c` | Peyman Narjabadifam (2024) | *Experimental-Numerical Assessment of Mechanic...* | `WEAKENS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that NiTi wire ropes can be fabricated and simulated ... |
| **07** | `9f4295be23` | F. Barsi (2025) | *A new mechanical model of short wire ropes: T...* | `BOUNDS` | `C1, C5, C7` | `T1, T2, T3` | `H0a, H0b` | Proves that beam stick-slip mechanics rigorously predicts th... |
| **08** | `56793dea9b` | KANG Zetian (2020) | *Finite Element Method for Mechanical Behavior...* | `BOUNDS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that existing beam contact finite elements combined w... |
| **09** | `d9966f2f5e` | Biagio Carboni (2015) | *Hysteresis of Multiconfiguration Assemblies o...* | `BOUNDS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that multiwire NiTi assemblies under cyclic flexure d... |
| **10** | `9e15094d68` | Jiaxing Liu (2023) | *Superelasticity SMA cables and its simplified...* | `BOUNDS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that simplified structural models can capture multiwi... |
| **11** | `53200aa0c6` | Saeed Vahidi (2022) | *Mechanical response of single and double-heli...* | `WEAKENS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that existing transformation-aware constitutive model... |
| **12** | `98fee47c04` | Mu-Qing Niu (2021) | *Nonlinear Vibration Isolation via a NiTiNOL W...* | `BOUNDS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that NiTi wire ropes modulate dynamic stiffness and d... |
| **13** | `aaad9c248c` | Xin Liu (2004) | *Cable Vibration Considering Internal Friction* | `BOUNDS` | `C1, C5` | `T1` | `H0a` | Proves that inter-wire friction in slender wire bundles is f... |
| **14** | `ccdc1bb980` | Denny D. Tjahjanto (2017) | *Bending Mechanics of Cable Cores and Fillers ...* | `WEAKENS` | `C2, C6` | `T2` | `H0b` | Proves that external radial confining pressure directly incr... |
| **15** | `e8462758c3` | Yiwen Liu (2026) | *High damping capacity with a wide temperature...* | `BOUNDS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that microfilament NiTi bundles exhibit simultaneous ... |
| **16** | `6dd1ca94d1` | Paulo C. S. Silva (2022) | *NiTi SMA Superelastic Micro Cables: Thermomec...* | `BOUNDS` | `C5, C7` | `T1, T3` | `H0a, H0b` | Proves that inter-wire contact friction causes localized fre... |

---

## 2. Detailed Full-Text Paper Dossiers

### Paper [01]: Superelastic shape memory alloy cables: Part I – Isothermal tension experiments

- **Paper ID:** `00414aac4b` | **DOI:** [10.1016/j.ijsolstr.2013.03.013](https://doi.org/10.1016/j.ijsolstr.2013.03.013)
- **Authors:** Benjamin Reedlunn, Samantha Daly, John Shaw (2013)
- **Repository Path:** `data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf` (Matrix Filename: `2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Core prior art on multiwire superelastic NiTi cables under tension testing inter-wire friction and transformation.
- **Threat Addressed:** Directly threatens T1 by proving inter-wire contact, friction, and hysteretic energy dissipation in NiTi wire bundles.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Experimental testing with non-contact optical diagnostics and thermal imaging
- **Material / System:** 7x7 right regular lay and 1x27 alternating lay superelastic NiTi cables
- **Loading Mode:** Quasi-static isothermal uniaxial elongation under rigid end rotation constraint
- **Independent Variables:** Cable geometry (7x7 regular lay vs 1x27 alternating lay), dry vs synthetic oil lubrication, strain amplitude up to 12.5%
- **Dependent Variables:** Axial force-strain response, reaction torque Mz, localized temperature rise Delta T, strain field via stereo DIC
- **Control Variables:** Displacement rate (1e-5 to 4e-4 s^-1), room temperature (22 deg C), lubrication state
- **Model Used:** Idealized polar moment of inertia J0; exponential shakedown curve fits
- **Constitutive Model:** Phenomenological shakedown laws (modeling deferred to Part II)
- **Contact / Friction Model:** Qualitative Coulomb friction assessment via dry vs lubricated testing
- **Experimental Setup:** Straight cable specimens clamped rigidly in pneumatic grips with hardened steel serrated jaws

#### Substantive Findings & Verification
- **Key Results:** Lubrication had negligible impact on axial stress-strain response, proving static friction locks inter-wire slip during initial loading; 7x7 cables exhibited flat transformation plateaus (493 MPa load, 262 MPa unload) with propagating fronts, while 1x27 exhibited continuous work hardening; substantial reaction torque generated.
- **What It Actually Proves:** Proves that multiwire NiTi cables exhibit inter-wire contact normal forces, high static friction, and severe cyclic shakedown.
- **What It Does NOT Prove:** Does not evaluate bending flexure or external transverse fluid confinement pressure; does not validate a predictive contact constitutive law.
- **Directly Verified Statements:**
  - Lubrication does not noticeably alter the axial load-strain curves of 7x7 or 1x27 NiTi cables (Section 4.1, p. 3012).
  - 7x7 cable exhibits localized transformation front propagation with localized rotation kinks (Section 4.2, p. 3014).
  - Contact indentations observed in SEM are pre-existing manufacturing artifacts from stranding and shape setting (Section 4.5, p. 3019).
- **Inferred Statements:**
  - High inter-wire normal force in helical cables suppresses inter-wire slip until high axial strains are reached.
- **Scientific Limitations:** Uniaxial tension only; constrained rotation boundary condition; isothermal slow strain rates.
- **Specific Impact on MP1:** Closes C5/T1 at existence level by demonstrating mutual contact in NiTi wire bundles; refutes overclaims that contact indentations were operational fretting wear.
- **Evidence Pointers:** Section 4.1 (pp. 3011-3013), Section 4.5 (pp. 3018-3021) (Fig. 5 (load-strain curves), Fig. 8 (SEM micrographs of inter-wire contact indentations))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---

### Paper [02]: Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses

- **Paper ID:** `fac21c950e` | **DOI:** [10.1016/j.ijsolstr.2013.03.015](https://doi.org/10.1016/j.ijsolstr.2013.03.015)
- **Authors:** Benjamin Reedlunn, Samantha Daly, John Shaw (2013)
- **Repository Path:** `data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf` (Matrix Filename: `2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Evaluates subcomponent wire mechanics and tests Costello analytical contact-kinematics modeling on NiTi cables.
- **Threat Addressed:** Evaluates whether existing cable kinematics and contact formulations can predict multiwire NiTi response (T1, T3, H0b).
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Hierarchical experimental testing and analytical kinematic modeling
- **Material / System:** Single NiTi wires, 1x7 strands, 1x19 cables, and 1x27 cables
- **Loading Mode:** Quasi-static uniaxial tension
- **Independent Variables:** Subcomponent level (individual wires, straight core, outer helical wires, complete strands)
- **Dependent Variables:** Axial force-strain response, torque generation, comparison against Costello model
- **Control Variables:** Displacement rate, room temperature (22 deg C)
- **Model Used:** Costello kinematic wire rope theory with linear elastic wire assumptions
- **Constitutive Model:** Costello wire rope kinematics combined with single-wire experimental curves
- **Contact / Friction Model:** Line contact formulation with inter-wire radial pressure
- **Experimental Setup:** Individual wires dissected from cables and tested in tension to isolate base material response

#### Substantive Findings & Verification
- **Key Results:** Costello cable theory matched 1x7 strands and shallow helix angles well, but severely deviated for 1x27 cables with steep helix angles (>20 deg); deviation was caused by neglecting local bending and twisting moments in outer wires, not by novel constitutive contact physics.
- **What It Actually Proves:** Proves that shallow helix angle NiTi bundles behave closely to single wires; proves that model divergence at steep angles is due to kinematic reduction omissions.
- **What It Does NOT Prove:** Does not prove a failure of continuum contact mechanics; does not support the requirement of a new micro-coupling law H1.
- **Directly Verified Statements:**
  - The Costello model divergence in 1x27 cables stems from the neglect of individual wire bending and twisting moments (Section 5.3, pp. 3035-3037).
  - Single wire responses closely match 1x7 strand response when normalized by metallic cross-sectional area (Section 4.2, p. 3028).
- **Inferred Statements:**
  - For parallel or nearly-parallel wire bundles (like MP1), kinematic helix angle errors do not arise.
- **Scientific Limitations:** Tension only; analytical model did not resolve full 3D frictional stick-slip.
- **Specific Impact on MP1:** Mandates conservative remediation of Reedlunn 2013 (Astra G07): model failure in steep helical cables cannot be cited as evidence that parallel NiTi bundles require new mechanics.
- **Evidence Pointers:** Section 5.3 (pp. 3034-3038) (Fig. 11 (Costello model vs experiment for 1x7 and 1x27 cables))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---

### Paper [03]: Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments

- **Paper ID:** `40760daa02` | **DOI:** [10.1061/(ASCE)EM.1943-7889.0001072](https://doi.org/10.1061/(ASCE)EM.1943-7889.0001072)
- **Authors:** Biagio Carboni, Walter Lacarbonara (2016)
- **Repository Path:** `data/papers/verification/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf` (Matrix Filename: `2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Direct evidence of combined dry friction and NiTi superelastic hysteresis in dynamic bending structures.
- **Threat Addressed:** Directly threatens T3 by demonstrating that inter-wire friction combined with NiTi phase transformation is established prior art.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `WEAKENS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Theoretical asymptotic formulation and experimental dynamic shaker testing
- **Material / System:** Nonlinear vibration absorber consisting of a cantilever assembly with superelastic NiTi wires and friction sliders
- **Loading Mode:** Harmonic base excitation inducing cyclic bending
- **Independent Variables:** Excitation amplitude (0.1g to 1.5g), frequency sweeps across resonance
- **Dependent Variables:** Tip displacement, frequency-response curves, pinched hysteresis loops, equivalent damping ratio
- **Control Variables:** Excitation frequency and base acceleration amplitude
- **Model Used:** Asymptotic perturbation method (method of multiple scales) on nonlinear differential equations
- **Constitutive Model:** Multi-mechanism pinched hysteresis model combining Bouc-Wen friction and Graesser NiTi superelasticity
- **Contact / Friction Model:** Coulomb-like friction sliding element coupled in parallel/series
- **Experimental Setup:** Cantilever absorber beam mounted on shaker slip table with laser displacement tracking

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that combining NiTi phase transformation with frictional contact creates pinched hysteresis and amplitude-dependent flexural stiffness, effectively mitigating resonance vibrations across varying excitation levels.
- **What It Actually Proves:** Proves that coupling of friction and NiTi superelasticity directly governs flexural stiffness and damping in mechanical assemblies.
- **What It Does NOT Prove:** Does not apply an active pneumatic or hydraulic fluid confinement pressure on the wire assembly.
- **Directly Verified Statements:**
  - Pinched hysteresis arises naturally when frictional contact dissipation is combined with superelastic phase transformation (Section 2, pp. 2-4).
  - The flexural resonance peak shifts and broadens due to amplitude-dependent stiffness reduction during phase transformation (Section 4, pp. 8-10).
- **Inferred Statements:**
  - Standard multi-mechanism phenomenological models adequately capture pinched flexural hysteresis without needing a micro-scale thermodynamic coupling law.
- **Scientific Limitations:** Focused on vibration absorption; friction was concentrated at slider interfaces rather than distributed throughout a dense wire bundle.
- **Specific Impact on MP1:** Preempts claims that friction-transformation coupling is an unaddressed mechanics phenomenon; reinforces H0b.
- **Evidence Pointers:** Section 2 (pp. 2-5), Section 4 (pp. 7-11) (Fig. 3 (pinched hysteresis loops), Fig. 8 (experimental frequency-response curves))
- **Contradiction Candidate IDs:** `['CONTRA-01', 'CONTRA-02']`
- **Metadata Conflicts:** None

---

### Paper [04]: Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application

- **Paper ID:** `2f7fcf2f8f` | **DOI:** [10.1016/j.engstruct.2019.01.049](https://doi.org/10.1016/j.engstruct.2019.01.049)
- **Authors:** Cheng Fang, Yue Zheng, Jian Chen, M. C. H. Yam, B. Wang (2019)
- **Repository Path:** `data/papers/verification/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf` (Matrix Filename: `2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Major study on phenomenological fiber modeling of NiTi cables and seismic structural applications.
- **Threat Addressed:** Threatens model necessity: proves that phenomenological fiber models capture cable hysteresis without resolving micro-contacts (H0b competitor).
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `WEAKENS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Experimental testing, OpenSees fiber macromodeling, and seismic nonlinear time-history analysis
- **Material / System:** 1x7 and 7x7 superelastic NiTi cables (diameters 2.5 mm to 12.7 mm)
- **Loading Mode:** Cyclic uniaxial tension on cables; pushover/cyclic loading on RC bridge pier
- **Independent Variables:** Cable diameter, number of loading cycles (up to 20 cycles), temperature
- **Dependent Variables:** Axial stress-strain loops, residual strain, energy dissipation, bridge pier drift and residual displacement
- **Control Variables:** Displacement loading rate, cyclic strain amplitudes (up to 6%)
- **Model Used:** OpenSees nonlinear beam-column fiber element framework
- **Constitutive Model:** Steel02 (for core plastic residual strain) combined with Self-centering material in parallel/series
- **Contact / Friction Model:** Macroscopic phenomenological compliance; inter-wire contact is not explicitly modeled
- **Experimental Setup:** NiTi cables clamped using specialized wedge-barrel anchorages tested under uniaxial cyclic tension

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that an OpenSees fiber macromodel dividing the cross-section into concentric zones with Steel02 and Self-centering materials accurately predicts cyclic cable hysteresis without resolving inter-wire micro-contacts; applied NiTi cables as unbonded restrainers in a 1.4 m diameter RC bridge pier.
- **What It Actually Proves:** Proves that macroscopic phenomenological models can accurately predict overall cable stiffness and energy dissipation with minimal computational cost.
- **What It Does NOT Prove:** Does not model or test NiTi cables in bending; does not test positive confinement pressure.
- **Directly Verified Statements:**
  - Cables were tested exclusively in axial tension; the nonlinear beam-column fiber element in OpenSees was used to model the 1.4 m diameter reinforced concrete bridge pier (Section 4, pp. 11-14).
  - Multiple distinct parameter combinations produce identical macroscopic hysteretic curves (Section 3.2, pp. 7-9).
- **Inferred Statements:**
  - If macroscopic stiffness and damping are the only design targets, complex contact-resolving FEA may offer little added engineering value over fiber macromodels.
- **Scientific Limitations:** Axial tension only for SMA cables; beam model was for RC column; free floating parameters in Steel02 calibration.
- **Specific Impact on MP1:** Conservative remediation (Astra G07): corrects misconception that Fang modeled cable bending; highlights the macromodel parsimony threat to MP1.
- **Evidence Pointers:** Section 3 (pp. 6-10), Section 4 (pp. 11-15) (Fig. 6 (OpenSees fiber discretization), Fig. 13 (RC bridge pier pushover response))
- **Contradiction Candidate IDs:** `['CONTRA-01', 'CONTRA-02']`
- **Metadata Conflicts:** None

---

### Paper [05]: Nonlinear dynamic response of a wire rope isolator: Experiment, identification and validation

- **Paper ID:** `7f3f45407f` | **DOI:** [10.1016/j.engstruct.2021.112121](https://doi.org/10.1016/j.engstruct.2021.112121)
- **Authors:** Andrea Salvatore, Biagio Carboni, Walter Lacarbonara (2021)
- **Repository Path:** `data/papers/verification/MP1-V002/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf` (Matrix Filename: `2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Comprehensive mechanics study on multi-axis stick-slip friction in helical wire rope structures.
- **Threat Addressed:** Threatens T1 by proving that multi-axis stick-slip friction in wire bundles is rigorously understood.
- **Affected Entities:** Claims `['C1', 'C5']` | Targets `['T1']` | Hypotheses `['H0a']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Experimental dynamic shaker testing and multi-mechanism phenomenological identification
- **Material / System:** Standard stainless steel wire rope isolator (WRI) with helical loop configuration
- **Loading Mode:** Multi-axis dynamic excitation: compression-roll and tension-shear cyclic loading
- **Independent Variables:** Excitation direction, displacement amplitude (0.5 mm to 10 mm), frequency (2 to 30 Hz)
- **Dependent Variables:** Restoring forces, pinched hysteresis loops, dynamic stiffness, phase shift
- **Control Variables:** Shaker base acceleration amplitude and frequency sweeps
- **Model Used:** Phenomenological generalized Bouc-Wen differential model with multi-axis coupling
- **Constitutive Model:** Nonlinear elastic restoring force combined with hysteretic friction displacement variables
- **Contact / Friction Model:** Smooth hysteretic friction formulation representing distributed inter-wire slip
- **Experimental Setup:** Wire rope isolator mounted between rigid shaker fixture and seismic mass

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that inter-wire frictional stick-slip produces strong stiffness softening and high energy dissipation; validated that a 3D phenomenological model accurately predicts dynamic response under multi-axial base excitation.
- **What It Actually Proves:** Proves that inter-wire friction in helical wire ropes produces amplitude-dependent stiffness variation and dry friction damping.
- **What It Does NOT Prove:** Does not use shape memory alloys (steel only); does not apply active fluid confinement pressure.
- **Directly Verified Statements:**
  - Inter-wire friction generates non-symmetric pinched hysteretic response under combined compression and roll (Section 3, pp. 6-9).
  - Initial stiffness is dominated by stick state, followed by gradual softening as inter-wire slip propagates (Section 4, pp. 10-12).
- **Inferred Statements:**
  - Frictional jamming in wire bundles is mechanically equivalent to the stick-slip softening observed in wire rope isolators.
- **Scientific Limitations:** Stainless steel only; phenomenological lumped parameter model rather than continuum FEA.
- **Specific Impact on MP1:** Demonstrates that friction-induced stiffness variation in wire bundles is thoroughly established in structural mechanics.
- **Evidence Pointers:** Section 2 (pp. 3-6), Section 4 (pp. 10-14) (Fig. 4 (experimental multi-axis hysteresis loops), Fig. 11 (model validation))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---

### Paper [06]: Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes

- **Paper ID:** `1c81b2d35c` | **DOI:** [10.3390/buildings14061567](https://doi.org/10.3390/buildings14061567)
- **Authors:** Peyman Narjabadifam, Neda Fazlalipour, A. A. Moghadam (2024)
- **Repository Path:** `data/papers/verification/MP1-V002/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf` (Matrix Filename: `2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Direct recent comparative experimental and numerical evaluation of steel vs NiTi wire ropes.
- **Threat Addressed:** Threatens T1 and T3 by directly testing laboratory-made NiTi wire ropes under cyclic loading.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `WEAKENS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Laboratory fabrication, mechanical tensile testing, and Abaqus 3D finite element modeling
- **Material / System:** 1x7 laboratory-made steel wire ropes and 1x7 NiTi shape memory alloy wire ropes
- **Loading Mode:** Quasi-static monotonic and cyclic axial tension
- **Independent Variables:** Material type (Steel vs NiTi), helical lay pitch, strain amplitude
- **Dependent Variables:** Force-displacement curves, energy dissipation per cycle, residual strain, equivalent stiffness
- **Control Variables:** Displacement rate, strain levels (up to 6%)
- **Model Used:** Abaqus/Standard 3D solid continuum modeling with surface-to-surface contact
- **Constitutive Model:** Built-in Abaqus Superelastic material model (Auricchio formulation)
- **Contact / Friction Model:** Surface-to-surface penalty contact with Coulomb friction (mu = 0.15)
- **Experimental Setup:** Custom stranding jig used to fabricate 1x7 NiTi wire ropes; tested under displacement control

#### Substantive Findings & Verification
- **Key Results:** NiTi wire ropes demonstrated superior energy dissipation and flag-shaped re-centering compared to steel ropes; 3D FEA with Auricchio constitutive model and penalty Coulomb friction successfully matched experimental curves.
- **What It Actually Proves:** Proves that NiTi wire ropes can be fabricated and simulated using standard 3D FE contact tools, confirming mutual wire slip and phase transformation.
- **What It Does NOT Prove:** Does not apply active transverse fluid pressure; tension loading only.
- **Directly Verified Statements:**
  - NiTi wire ropes exhibit Flag-shaped hysteresis with minimal residual strain after cyclic loading to 6% strain (Section 3.2, pp. 8-11).
  - Abaqus 3D FE model with Auricchio superelasticity and Coulomb friction accurately captures inter-wire contact and axial response (Section 4, pp. 12-15).
- **Inferred Statements:**
  - Commercial FEA tools (H0b) are capable of modeling multiwire NiTi structures without developing specialized coupling theories.
- **Scientific Limitations:** 1x7 strands only; uniaxial tension only; no active fluid confinement pressure.
- **Specific Impact on MP1:** Provides direct evidence that NiTi wire bundles in mutual contact are established in 2024 literature and well-predicted by H0b.
- **Evidence Pointers:** Section 3 (pp. 7-11), Section 4 (pp. 12-16) (Fig. 7 (experimental load-unload curves), Fig. 12 (FEA contact stress contours))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---

### Paper [07]: A new mechanical model of short wire ropes: Theory and experimental validation

- **Paper ID:** `9f4295be23` | **DOI:** [10.1016/j.engstruct.2024.119217](https://doi.org/10.1016/j.engstruct.2024.119217)
- **Authors:** F. Barsi, B. Carboni, W. Lacarbonara (2025)
- **Repository Path:** `data/papers/verification/MP1-V002/2025-A new mechanical model of short wire ropes Theory and experimental.pdf` (Matrix Filename: `2025-A new mechanical model of short wire ropes Theory and experimental.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** State-of-the-art 2025 analytical and experimental formulation of stick-slip flexural mechanics in short wire ropes.
- **Threat Addressed:** Directly threatens T1, T2, and H0b by formulating exact stick-slip bending bounds under contact friction.
- **Affected Entities:** Claims `['C1', 'C5', 'C7']` | Targets `['T1', 'T2', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Analytical continuum beam modeling and experimental static/dynamic bending tests
- **Material / System:** Short multiwire steel wire ropes (19-wire and 49-wire configurations)
- **Loading Mode:** Three-point bending and cantilever cyclic bending flexure
- **Independent Variables:** Rope length (short vs long), wire lay geometry, contact normal force distribution
- **Dependent Variables:** Bending moment-curvature response, stick-slip transition curvature, upper/lower flexural stiffness bounds (EI_stick, EI_slip)
- **Control Variables:** Displacement amplitude, span length (aspect ratio)
- **Model Used:** Shear-deformable beam theory with inter-wire tangential slip and normal contact tractions
- **Constitutive Model:** Linear elastic wire material with inter-wire stick-slip contact equilibrium
- **Contact / Friction Model:** Coulomb friction law with normal contact pressure resulting from internal geometry and clamping
- **Experimental Setup:** Wire ropes clamped at ends and loaded laterally to measure moment-curvature and slip thresholds

#### Substantive Findings & Verification
- **Key Results:** Derived closed-form equations for stick stiffness bound (EI_stick) and slip stiffness bound (EI_slip); proved that the transition from full stick to full slip depends on normal contact force and friction coefficient; experimental data validated the predictive bounds without parameter fitting.
- **What It Actually Proves:** Proves that beam stick-slip mechanics rigorously predicts the variable flexural stiffness of multiwire bundles under frictional contact.
- **What It Does NOT Prove:** Does not incorporate superelastic NiTi phase transformation; steel ropes only.
- **Directly Verified Statements:**
  - The flexural rigidity of a multiwire rope transitions smoothly from EI_stick (full composite action) to EI_slip (isolated wire sum) as inter-wire friction is overcome (Section 2, pp. 3-6).
  - The model predicts both stiffness bounds using only wire geometry and elastic properties without fitting parameters (Section 4, pp. 11-14).
- **Inferred Statements:**
  - The mechanics of positive-pressure wire jamming is mathematically isomorphic to the stick-slip transition in short wire ropes, where pressure modulates the normal force.
- **Scientific Limitations:** Linear elastic steel wires; did not evaluate active fluid membrane confinement.
- **Specific Impact on MP1:** Confirms that variable bending stiffness via contact friction is a solved continuum mechanics problem (H0b competitor).
- **Evidence Pointers:** Section 2 (pp. 2-7), Section 4 (pp. 10-15) (Eq. (12)-(15) (stiffness bounds), Fig. 6 (bending moment vs curvature comparison))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---

### Paper [08]: Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables (形状记忆合金超弹性缆索力学行为的有限单元法)

- **Paper ID:** `56793dea9b` | **DOI:** [10.3901/JME.2020.14.065](https://doi.org/10.3901/JME.2020.14.065)
- **Authors:** KANG Zetian, WANG Zhiyong, WANG Zhenqing, LIANG Xuedong (2020)
- **Repository Path:** `data/papers/verification/MP1-V002/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf` (Matrix Filename: `2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Branch B11 citation anchor: specialized finite element method for superelastic SMA cables.
- **Threat Addressed:** Threatens T1 and T3 by demonstrating tailored finite element formulation for contacting NiTi cable structures.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Nonlinear finite element formulation using corotational beam elements with contact
- **Material / System:** 1x7 and 1x19 superelastic NiTi SMA cables
- **Loading Mode:** Monotonic and cyclic tension and pure bending
- **Independent Variables:** Cable lay geometry, friction coefficient, strain amplitude
- **Dependent Variables:** Hysteresis curves, axial force, bending moment, contact stress distribution along helix
- **Control Variables:** Displacement increments, convergence tolerance
- **Model Used:** Corotational beam element incorporating Auricchio 1D superelastic constitutive model
- **Constitutive Model:** 1D Auricchio superelastic constitutive model with tension-compression asymmetry
- **Contact / Friction Model:** Point-to-line and line-to-line contact element with Coulomb friction
- **Experimental Setup:** Numerical validation study benchmarking against published experimental cable data

#### Substantive Findings & Verification
- **Key Results:** Developed a dedicated beam finite element algorithm capable of simulating large deformation, inter-wire contact, and superelastic phase transformation in NiTi cables with high numerical efficiency and stability.
- **What It Actually Proves:** Proves that existing beam contact finite elements combined with standard 1D Auricchio models (H0b) accurately simulate NiTi multiwire cable deformation.
- **What It Does NOT Prove:** Does not apply active external pneumatic/hydraulic confinement pressure.
- **Directly Verified Statements:**
  - The corotational beam FE model with 1D Auricchio constitutive relations reproduces the tensile and bending hysteresis of SMA cables (Section 3, pp. 68-71).
  - Inter-wire contact forces concentrate along helical line contacts and dictate local frictional slip (Section 4, pp. 71-73).
- **Inferred Statements:**
  - Standard continuum/structural finite element methods can capture coupled NiTi contact behavior without novel constitutive laws.
- **Scientific Limitations:** Numerical paper without new standalone experimental tests (benchmarked against Reedlunn).
- **Specific Impact on MP1:** Confirms H0b feasibility for beam finite element modeling of NiTi wire bundles.
- **Evidence Pointers:** Section 2 (pp. 66-68), Section 3 (pp. 68-72) (Fig. 4 (corotational beam contact formulation), Fig. 7 (validation against Reedlunn 2013))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** Filename lists 2025 prefix, but paper publication year is verified as 2020 in Chinese JME.

---

### Paper [09]: Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification

- **Paper ID:** `d9966f2f5e` | **DOI:** [10.1061/(ASCE)EM.1943-7889.0000852](https://doi.org/10.1061/(ASCE)EM.1943-7889.0000852)
- **Authors:** Biagio Carboni, Walter Lacarbonara, F. Auricchio (2015)
- **Repository Path:** `data/papers/verification/MP1-V002/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf` (Matrix Filename: `A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Core prior art paper on cyclic hysteresis of multi-configuration assemblies of Nitinol and steel strands.
- **Threat Addressed:** Central paper for T1 and T3; historically linked to CONTRA-03 (S2a steel vs S1a NiTi misattribution).
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Experimental dynamic testing and phenomenological hysteresis identification
- **Material / System:** Multiconfiguration strand assemblies: Specimen S1a (NiTi7 strand) and Specimen S2a (ST49 steel wire rope)
- **Loading Mode:** Cyclic tension and combined tension-bending flexure
- **Independent Variables:** Specimen configuration (S1a NiTi7 vs S2a steel ST49), pretension level (1.5 kN to 4.5 kN), cyclic flexural displacement
- **Dependent Variables:** Force-displacement hysteresis loops, equivalent stiffness, dissipated energy, Bouc-Wen model parameters
- **Control Variables:** Displacement amplitude, tension preload, excitation frequency (0.1 to 2 Hz)
- **Model Used:** Generalized Bouc-Wen differential hysteresis model
- **Constitutive Model:** Graesser-type superelastic formulation combined with Bouc-Wen friction damping
- **Contact / Friction Model:** Inter-wire friction dissipation captured via evolutionary differential variable
- **Experimental Setup:** Strand clamped under axial preload with transverse actuator applying cyclic lateral flexure

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that NiTi7 strand under tension-bending (S1a) exhibits combined friction and superelastic hysteresis; confirmed that specimen S2a was ST49 steel wire rope exhibiting pure friction hysteresis without phase transformation.
- **What It Actually Proves:** Proves that multiwire NiTi assemblies under cyclic flexure dissipate energy via simultaneous inter-wire friction and pseudoelasticity (in configuration S1a).
- **What It Does NOT Prove:** Did NOT test pure cyclic bending of NiTi without tension preload; did NOT test specimen S2a as NiTi (S2a was steel).
- **Directly Verified Statements:**
  - Specimen S1a is composed of a 1x7 NiTi strand tested under combined tension and flexure (Table 1, p. 3).
  - Specimen S2a is an ST49 high-strength steel wire rope tested under cyclic flexure (Table 1, p. 3; Table 4, p. 10).
  - Energy dissipation in S1a originates from both Coulomb friction and martensitic phase transformation (Section 5, pp. 8-11).
- **Inferred Statements:**
  - Without an axial tensile preload, thin NiTi wire bundles may buckle on the compressive side during pure bending unless radial confinement is applied.
- **Scientific Limitations:** S1a required substantial axial tension preload (1.5-4.5 kN); S2a was steel; no active fluid confinement pressure.
- **Specific Impact on MP1:** Direct focus of mandatory correction CONTRA-03: Stage 1 extraction error claiming S2a proved NiTi pure bending is completely expunged.
- **Evidence Pointers:** Table 1 (p. 3), Table 4 (p. 10), Section 5 (pp. 8-12) (Table 1 (specimen designations S1a vs S2a), Fig. 8 (S1a tension-bending hysteresis loops))
- **Contradiction Candidate IDs:** `['CONTRA-01', 'CONTRA-03']`
- **Metadata Conflicts:** Often cited as 2014 in conference/online first, published in ASCE Journal of Engineering Mechanics in 2015.

---

### Paper [10]: Superelasticity SMA cables and its simplified FE model

- **Paper ID:** `9e15094d68` | **DOI:** [10.1007/s40430-022-03957-2](https://doi.org/10.1007/s40430-022-03957-2)
- **Authors:** Jiaxing Liu, Zhongwei Zhao, Shengxin Fan, Qingfei Gao (2023)
- **Repository Path:** `data/papers/verification/MP1-V002/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf` (Matrix Filename: `A2-2023-Superelasticity SMA cables and its simplified FE model.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Recent study proposing simplified finite element models for superelastic SMA cables.
- **Threat Addressed:** Threatens model necessity by demonstrating efficient simplified FE modeling of NiTi cables.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Theoretical simplification, 3D FE modeling, and experimental tension validation
- **Material / System:** 1x7 and 7x7 superelastic NiTi SMA cables
- **Loading Mode:** Quasi-static and cyclic axial tension
- **Independent Variables:** Cable structure, helical lay angle, number of cycles
- **Dependent Variables:** Axial force-strain curve, computational efficiency, residual strain
- **Control Variables:** Displacement rate, strain levels (up to 8%)
- **Model Used:** Simplified beam-truss model with equivalent cross-sectional parameters
- **Constitutive Model:** Auricchio superelastic model implemented in ANSYS/Abaqus
- **Contact / Friction Model:** Coupled kinematic constraint representing inter-wire frictional resistance
- **Experimental Setup:** SMA cable specimens tested under uniaxial cyclic tension with displacement control

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that a simplified FE model using equivalent beam elements accurately predicts the superelastic behavior of NiTi cables while reducing computing time by over 90% compared to full 3D solid contact models.
- **What It Actually Proves:** Proves that simplified structural models can capture multiwire NiTi cable response accurately without full 3D contact discretization.
- **What It Does NOT Prove:** Does not examine lateral bending under variable transverse pressure.
- **Directly Verified Statements:**
  - The simplified FE model reproduces cyclic tension curves with <5% error while reducing computational degrees of freedom by an order of magnitude (Section 3, pp. 5-8).
  - Axial stiffness degrades progressively during early loading cycles before stabilizing into a steady limit cycle (Section 4, pp. 9-11).
- **Inferred Statements:**
  - Simplified structural models (H0b variants) can capture cable mechanics effectively for engineering control.
- **Scientific Limitations:** Axial tension only; no lateral confinement pressure.
- **Specific Impact on MP1:** Reinforces H0b by showing that simplified structural models adequately describe NiTi cables.
- **Evidence Pointers:** Section 2 (pp. 3-5), Section 3 (pp. 5-9) (Fig. 5 (simplified model schematic), Fig. 9 (comparison of simplified vs 3D solid model))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---

### Paper [11]: Mechanical response of single and double-helix SMA wire ropes

- **Paper ID:** `53200aa0c6` | **DOI:** [10.1080/15376494.2021.1955313](https://doi.org/10.1080/15376494.2021.1955313)
- **Authors:** Saeed Vahidi, Jamal Arghavani, Ramin Sedaghati (2022)
- **Repository Path:** `data/papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf` (Matrix Filename: `A3-2022-Mechanical response of single and double-helix.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Highest-threat full-text prior art paper for Target T1 and foundational benchmark for H0b.
- **Threat Addressed:** Directly closes T1 and demonstrates H0b sufficiency by modeling 3D NiTi multiwire bundles with Coulomb friction and Auricchio superelasticity.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `WEAKENS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** 3D nonlinear continuum finite element analysis in Abaqus/Standard with custom UMAT
- **Material / System:** 1x27 single-helix and 7x7 double-helix superelastic NiTi wire ropes
- **Loading Mode:** Quasi-static cyclic uniaxial tension under fixed-end rotation
- **Independent Variables:** Cable architecture (1x27 vs 7x7), friction coefficient (mu = 0.0 to 0.2, baseline 0.115), strain levels (up to 12%)
- **Dependent Variables:** Axial stress-strain curves, reaction torque, contact normal and shear force distributions, energy dissipation
- **Control Variables:** Displacement control, isothermal room temperature (22 deg C)
- **Model Used:** Abaqus 3D solid element FEA with surface-to-surface penalty contact
- **Constitutive Model:** Auricchio-Petrini 3D phenomenological superelastic constitutive model implemented in UMAT
- **Contact / Friction Model:** Penalty formulation Coulomb friction with isotropic friction coefficient mu = 0.115
- **Experimental Setup:** Exact 3D geometric CAD representation of wire ropes with helical sweeping and contact pair definitions

#### Substantive Findings & Verification
- **Key Results:** Successfully reproduced the complete stress-strain response, transformation plateaus, work-hardening, and reaction torque of 1x27 and 7x7 NiTi cables using locked material parameters from single-wire tests; proved that inter-wire friction normal forces and relative slip directly modulate structural stiffness and energy dissipation.
- **What It Actually Proves:** Proves that existing transformation-aware constitutive models coupled with standard Coulomb contact mechanics (H0b) are fully sufficient to predict multiwire NiTi bundle response.
- **What It Does NOT Prove:** Does not apply an active transverse fluid confinement pressure independent of axial tension.
- **Directly Verified Statements:**
  - Abaqus FEA combining Auricchio UMAT with Coulomb friction (mu = 0.115) accurately predicts the complete cyclic response of 1x27 and 7x7 NiTi cables (Section 4, pp. 6-10).
  - Inter-wire friction increases axial stiffness and energy dissipation while reducing total recoverable strain (Section 4.3, pp. 11-13).
  - The model reproduces the experimental data of Reedlunn 2013 without introducing any new micro-coupling laws (Section 4.1, pp. 7-9).
- **Inferred Statements:**
  - Unless an unpredicted phenomenon arises under transverse pressure, H0b is completely viable and live.
- **Scientific Limitations:** Axial tension only; isothermal assumption; no transverse fluid pressure.
- **Specific Impact on MP1:** Decisive paper: closes C5/T1 at existence level and establishes H0b as a formidable, non-falsified competitor null hypothesis.
- **Evidence Pointers:** Section 3 (pp. 3-6), Section 4 (pp. 6-14) (Fig. 4 (3D FEA mesh and contact definitions), Fig. 7 (validation against Reedlunn 1x27 and 7x7 data), Fig. 12 (friction sensitivity analysis))
- **Contradiction Candidate IDs:** `['CONTRA-01', 'CONTRA-02']`
- **Metadata Conflicts:** Online first 2021, official journal issue published in 2022.

---

### Paper [12]: Nonlinear Vibration Isolation via a NiTiNOL Wire Rope

- **Paper ID:** `98fee47c04` | **DOI:** [10.3390/app112110032](https://doi.org/10.3390/app112110032)
- **Authors:** Mu-Qing Niu, Li-Qun Chen (2021)
- **Repository Path:** `data/papers/verification/MP1-V002/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf` (Matrix Filename: `A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Demonstrates superelastic NiTi wire rope structures used as nonlinear variable-stiffness vibration isolators.
- **Threat Addressed:** Threatens T1 and T3 by demonstrating that NiTi wire ropes provide tunable stiffness and damping under cyclic loading.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Experimental vibration testing and nonlinear dynamic modeling
- **Material / System:** Laboratory NiTi wire rope isolator
- **Loading Mode:** Vertical dynamic base excitation and harmonic force excitation
- **Independent Variables:** Vibration amplitude, excitation frequency across primary resonance
- **Dependent Variables:** Transmissibility, resonant frequency shift, hysteretic loop area, dynamic stiffness
- **Control Variables:** Excitation amplitude and sweep frequency
- **Model Used:** Duffing-type nonlinear oscillator combined with hysteretic damping model
- **Constitutive Model:** Polynomial restoring force combined with Bouc-Wen hysteresis
- **Contact / Friction Model:** Frictional dissipation represented via Bouc-Wen evolutionary variable
- **Experimental Setup:** NiTi wire rope isolator supporting a payload mass subjected to harmonic vertical vibration

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that NiTi wire ropes exhibit softening-hardening non-linear stiffness and high damping, reducing resonance peak transmissibility by up to 50% compared to steel wire rope isolators.
- **What It Actually Proves:** Proves that NiTi wire ropes modulate dynamic stiffness and dissipate energy under cyclic deformation.
- **What It Does NOT Prove:** Does not apply active pneumatic/hydraulic confinement pressure.
- **Directly Verified Statements:**
  - NiTi wire rope isolators exhibit amplitude-dependent resonance frequency shifts due to superelastic softening (Section 3, pp. 6-9).
  - Superelasticity provides enhanced energy dissipation and displacement control over conventional steel wire ropes (Section 4, pp. 10-12).
- **Inferred Statements:**
  - Variable stiffness in NiTi wire ropes is readily exploitable for dynamic stiffness tuning in soft systems.
- **Scientific Limitations:** Lumped parameter dynamic testing; no local slip measurement.
- **Specific Impact on MP1:** Demonstrates prior art use of NiTi wire ropes for stiffness modulation.
- **Evidence Pointers:** Section 2 (pp. 3-5), Section 3 (pp. 6-10) (Fig. 5 (transmissibility curves), Fig. 8 (hysteresis loops under dynamic loading))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---

### Paper [13]: Cable Vibration Considering Internal Friction

- **Paper ID:** `aaad9c248c` | **DOI:** [10.1115/1.1767817](https://doi.org/10.1115/1.1767817)
- **Authors:** Xin Liu (2004)
- **Repository Path:** `data/papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf` (Matrix Filename: `A5-Cable vibration considering internal friction.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Foundational mechanics paper on continuum modeling of inter-wire contact friction damping in vibrating cables.
- **Threat Addressed:** Threatens T1 by proving that inter-wire friction mechanics in slender wire bundles is an established classical discipline.
- **Affected Entities:** Claims `['C1', 'C5']` | Targets `['T1']` | Hypotheses `['H0a']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Analytical continuum mechanics and boundary value problem formulation
- **Material / System:** Multi-wire stranded cables and parallel wire bundles under tension
- **Loading Mode:** Transverse flexural vibration under axial tension
- **Independent Variables:** Inter-wire friction coefficient, normal contact pressure distribution, vibration amplitude
- **Dependent Variables:** Modal damping ratio, energy dissipation per cycle, flexural wave attenuation
- **Control Variables:** Cable tension, vibration wavelength
- **Model Used:** Continuum beam-cable formulation incorporating Coulomb inter-wire friction law
- **Constitutive Model:** Linear elastic wire material
- **Contact / Friction Model:** Micro-slip Coulomb contact model with shear traction boundary conditions
- **Experimental Setup:** Theoretical formulation validated against laboratory cable vibration test data

#### Substantive Findings & Verification
- **Key Results:** Derived analytical expressions for inter-wire slip and frictional damping in cables; proved that energy dissipation is maximized at intermediate slip amplitudes and scales directly with inter-wire contact pressure.
- **What It Actually Proves:** Proves that inter-wire friction in slender wire bundles is fully treatable using continuum mechanics.
- **What It Does NOT Prove:** Does not involve shape memory alloys or active pressure control.
- **Directly Verified Statements:**
  - Internal friction between adjacent wires produces amplitude-dependent damping and flexural stiffness modulation (Section 2, pp. 2-4).
  - Contact pressure between wires governs the threshold amplitude required to trigger inter-wire slip (Section 3, pp. 5-7).
- **Inferred Statements:**
  - Inter-wire friction mechanics in soft robotic wire bundles follows the same classical contact governing equations.
- **Scientific Limitations:** Linear elastic steel cables only; axial tension required to generate contact pressure.
- **Specific Impact on MP1:** Demonstrates classical lineage of wire bundle friction mechanics.
- **Evidence Pointers:** Section 2 (pp. 1-4), Section 4 (pp. 6-8) (Eq. (8)-(14) (inter-wire shear slip equations), Fig. 3 (damping vs vibration amplitude))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** DOI missing in matrix, verified as ASME Journal of Applied Mechanics 2004.

---

### Paper [14]: Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable

- **Paper ID:** `ccdc1bb980` | **DOI:** [10.1115/OMAE2017-61198](https://doi.org/10.1115/OMAE2017-61198)
- **Authors:** Denny D. Tjahjanto, Andreas Tyrberg, David Mullins (2017)
- **Repository Path:** `data/papers/verification/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf` (Matrix Filename: `A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Critical prior art on multi-element cable bending mechanics under external radial contact pressure.
- **Threat Addressed:** Directly threatens T2 by proving that external radial contact pressure modulating flexural stiffness is prior art.
- **Affected Entities:** Claims `['C2', 'C6']` | Targets `['T2']` | Hypotheses `['H0b']`
- **Impact Type:** `WEAKENS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Analytical formulation and finite element beam bending simulation
- **Material / System:** Dynamic submarine power cables consisting of multiple metallic conductor cores and polymer fillers
- **Loading Mode:** Cyclic lateral bending under external radial contact pressure (0.2 MPa)
- **Independent Variables:** External radial contact pressure, inter-component friction coefficient, bending curvature
- **Dependent Variables:** Bending moment-curvature relationship, stick-slip threshold, effective flexural rigidity, shear stress distribution
- **Control Variables:** Radial contact pressure (0.2 MPa), bending curvature
- **Model Used:** Stick-slip friction beam mechanics with pressure-dependent normal force
- **Constitutive Model:** Elastic metallic conductor cores and viscoelastic/plastic filler material
- **Contact / Friction Model:** Coulomb friction law with radial contact pressure acting across cylindrical contact interfaces
- **Experimental Setup:** Submarine cable clamped under external radial pressure and bent cyclically to evaluate fatigue life

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that external radial contact pressure increases the normal force between internal cable components, delaying the onset of slip, increasing initial flexural rigidity, and widening the hysteresis loop.
- **What It Actually Proves:** Proves that external radial confining pressure directly increases inter-element normal force and modulates flexural rigidity under bending.
- **What It Does NOT Prove:** Applies a constant external radial pressure rather than actively modulating pressure as a variable stiffness control parameter on NiTi.
- **Directly Verified Statements:**
  - External radial pressure p directly increases the contact normal force between internal cable elements, delaying the onset of slip to higher curvatures (Section 3, pp. 4-6).
  - The bending stiffness transitions from a high stick bound to a lower slip bound as inter-element friction is overcome (Section 4, pp. 7-9).
- **Inferred Statements:**
  - In soft robotics, modulating chamber pressure p(t) is mechanically identical to varying the radial pressure boundary condition in submarine cables.
- **Scientific Limitations:** Constant radial pressure; copper conductors rather than NiTi superelastic wires.
- **Specific Impact on MP1:** Direct basis for CONTRA-05: proves active pressure is an experimental boundary condition, closing T2 as mechanics novelty.
- **Evidence Pointers:** Section 3 (pp. 3-6), Section 4 (pp. 7-10) (Fig. 5 (radial contact pressure schematic), Fig. 8 (moment-curvature curves under radial pressure))
- **Contradiction Candidate IDs:** `['CONTRA-01', 'CONTRA-05']`
- **Metadata Conflicts:** DOI missing in matrix, verified as ASME OMAE 2017 paper.

---

### Paper [15]: High damping capacity with a wide temperature window in braided NiTi microfilaments

- **Paper ID:** `e8462758c3` | **DOI:** [10.1016/j.matlet.2026.141544](https://doi.org/10.1016/j.matlet.2026.141544)
- **Authors:** Yiwen Liu, Yi Zeng, Jian Zhang, Zhenyu Chu, Xiaobin Qing (2026)
- **Repository Path:** `data/papers/verification/MP1-V002/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf` (Matrix Filename: `A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Forward 2026 citation anchor exploring high damping and friction in braided NiTi microfilament structures.
- **Threat Addressed:** Threatens T1 and T3 by demonstrating recent 2026 advances in friction-transformation coupling of NiTi microfilaments.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Experimental fabrication, dynamic mechanical analysis (DMA), and cyclic tensile testing
- **Material / System:** Braided multi-strand NiTi microfilaments (wire diameters 50 to 100 micrometers)
- **Loading Mode:** Cyclic tension and dynamic oscillatory flexure across temperature range (-50 deg C to 100 deg C)
- **Independent Variables:** Braiding angle, filament diameter, ambient temperature
- **Dependent Variables:** Loss factor tan(delta), storage modulus E', dissipated energy, superelastic flag-shaped recovery
- **Control Variables:** Temperature window, oscillation frequency (0.1 to 10 Hz), dynamic strain amplitude
- **Model Used:** Viscoelastic and frictional damping characterization via DMA
- **Constitutive Model:** Temperature-dependent martensitic phase transformation combined with contact friction
- **Contact / Friction Model:** Inter-filament contact friction in braided architecture
- **Experimental Setup:** Braided NiTi microfilament sleeves clamped under controlled thermal chamber

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that braided NiTi microfilaments achieve exceptionally high damping capacity (tan delta > 0.08) across a wide temperature window (-30 to 80 deg C) due to the synergistic interaction between stress-induced martensitic transformation and inter-filament friction sliding.
- **What It Actually Proves:** Proves that microfilament NiTi bundles exhibit simultaneous friction sliding and phase transformation damping.
- **What It Does NOT Prove:** Does not apply active pneumatic confinement pressure for stiffness tuning.
- **Directly Verified Statements:**
  - The synergistic combination of inter-filament frictional sliding and martensitic phase transformation broadens the damping temperature window (Section 3, pp. 3-5).
  - Braided architecture facilitates continuous contact reorientation during cyclic deformation (Section 4, pp. 5-7).
- **Inferred Statements:**
  - Microfilament NiTi architectures provide high compliance and dissipation, confirming coupled behavior in textile-like bundles.
- **Scientific Limitations:** Braided sleeves rather than straight parallel bundles; focus on damping rather than variable stiffness robotics.
- **Specific Impact on MP1:** Confirms that 2026 literature actively leverages coupled NiTi friction-transformation mechanics in multi-filament structures.
- **Evidence Pointers:** Section 3 (pp. 3-5), Section 4 (pp. 5-8) (Fig. 2 (braided NiTi microstructure), Fig. 4 (tan delta vs temperature across frequencies))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---

### Paper [16]: NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings

- **Paper ID:** `6dd1ca94d1` | **DOI:** [10.3390/s22208045](https://doi.org/10.3390/s22208045)
- **Authors:** Paulo C. S. Silva, Estephanie N. D. Grassi, C. J. de Araujo, E. A. C. de Souza (2022)
- **Repository Path:** `data/papers/verification/MP1-V002/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf` (Matrix Filename: `A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf`)
- **Verification Round:** `MP1-V002` | **Why Added:** Experimental fatigue and thermomechanical evaluation of superelastic NiTi micro-cables under dynamic loadings.
- **Threat Addressed:** Threatens feasibility and durability assumptions of NiTi multiwire jamming bundles under cyclic actuation.
- **Affected Entities:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Impact Type:** `BOUNDS` | **Evidence Status:** `VERIFIED` | **Verification Level:** `VERIFIED_FULL_TEXT` | **Confidence:** `high`

#### Experimental & Modeling Methodology
- **Method:** Experimental cyclic tensile and dynamic fatigue testing with infrared thermography
- **Material / System:** 1x7 and 7x7 superelastic NiTi micro-cables (diameters 0.5 mm to 1.8 mm)
- **Loading Mode:** High-cycle dynamic uniaxial tension at varying frequencies (0.5 Hz to 5 Hz)
- **Independent Variables:** Cable construction, cyclic stress amplitude (200 to 600 MPa), loading frequency
- **Dependent Variables:** Fatigue life (cycles to failure), surface temperature rise Delta T, accumulated ratcheting strain, fretting wear marks
- **Control Variables:** Stress amplitude, loading frequency, ambient room temperature
- **Model Used:** Empirical S-N fatigue curve formulation and thermal dissipation balance
- **Constitutive Model:** Cyclic superelastic constitutive degradation model
- **Contact / Friction Model:** Frictional contact fretting wear characterization via SEM analysis
- **Experimental Setup:** Micro-cables held in custom capstan grips to eliminate stress concentrations; cycled to fracture

#### Substantive Findings & Verification
- **Key Results:** Demonstrated that cyclic loading of NiTi micro-cables generates internal self-heating due to latent heat and friction; SEM examination confirmed that premature wire fractures initiate at inter-wire contact points due to fretting wear and micro-notching.
- **What It Actually Proves:** Proves that inter-wire contact friction causes localized fretting wear and accelerates fatigue failure in dynamic NiTi multiwire bundles.
- **What It Does NOT Prove:** Does not test lateral bending stiffness modulation under positive pressure.
- **Directly Verified Statements:**
  - Premature fatigue fractures in multiwire NiTi cables initiate predominantly at inter-wire contact points due to fretting wear (Section 3.3, pp. 11-14).
  - Dynamic cycling above 1 Hz induces substantial internal temperature rise, altering the transformation plateau stress via Clausius-Clapeyron relation (Section 3.2, pp. 8-10).
- **Inferred Statements:**
  - Frictional wear at contact points in MP1 wire jamming devices is a primary feasibility and durability bottleneck.
- **Scientific Limitations:** Axial tension fatigue only; does not evaluate variable stiffness jamming.
- **Specific Impact on MP1:** Directly informs feasibility and experimental identifiability: fretting wear and self-heating must be accounted for in cyclic tests.
- **Evidence Pointers:** Section 3 (pp. 7-14), Section 4 (pp. 14-16) (Fig. 8 (temperature rise vs frequency), Fig. 12 (SEM images of inter-wire fretting fatigue cracks))
- **Contradiction Candidate IDs:** `['CONTRA-01']`
- **Metadata Conflicts:** None

---
