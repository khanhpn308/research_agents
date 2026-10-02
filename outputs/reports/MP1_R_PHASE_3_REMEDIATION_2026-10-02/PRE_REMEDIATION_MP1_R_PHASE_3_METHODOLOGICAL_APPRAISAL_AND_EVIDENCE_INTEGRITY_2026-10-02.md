# MP1-R — Phase 3: Independent Methodological Appraisal and Evidence Integrity

**Date:** 2026-10-02, Asia/Bangkok. **Exit gate:** `BLOCKED_FOR_EVIDENCE`.

**Objective:** determine which retrieved studies support comparable mechanics arguments and approve claim boundaries for a later Phase 4. This report appraises evidence; it does not synthesize Chapter 2, declare novelty, endorse H1, or lock MP1-R as the final topic.

**Main finding:** the verified core supports pressure-controlled frictional stiffening, SMA-controlled wire–tube friction, transformation-sensitive NiTi cable response, and existing modeling competitors. It does not establish a new coupling law or either proposed gap as an independent scientific knowledge gap. Phase 2 contains material source-identity and mechanism errors. Its claimed S18 comparator and S20 interface-isolation study cannot presently be appraised as the intended papers. Those two deficits block completion of the explicitly requested core appraisal. The remaining appraisals and a conditional Phase 4 handoff are complete.

## 1. Authority, inputs, and audit protocol

The five primary inputs were read in the requested order:

1. `docs/literature/MP1_R_PHASE_2_DEEP_SEARCH_AND_CORPUS_MAP_2026-10-02.md` — search/corpus assertions, not scientific authority.
2. `outputs/plans/MP1_R_CH1_CH2_EVIDENCE_MATRIX_2026-09-29.json` — claim-to-evidence boundaries; no wording was loosened without original evidence.
3. `outputs/execution/MP1-V002/W2/MP1_W02_CLAIM_TARGET_HYPOTHESIS_MATRIX.json` — historical/current claim state.
4. `docs/project/MP1_MENTOR_FEEDBACK_RESCOPE_2026-09-29_VI.md` — authoritative active task scope, a rescope proposal.
5. `docs/project/MP1_CHAPTERS_1_2_WORKING_DRAFT_2026-09-29_VI.md` — current scientific narrative, not source authority.

The later, task-specific access policy superseded the older generic instruction to reload project-history files. No D1/M1 evidence or discovery snapshot was used. Scientific and registry state were not changed. Original papers override extraction and narrative. Source IDs S01–S21 remain stable; invalid identities are quarantined rather than silently replaced. S05 retains E07's two-paper identity. `V-W02` denotes an already cited W02 source inspected to resolve H0b, not a new discovery source.

Access labels apply to the actual evidence inspected in this audit: **E1 — FULL TEXT VERIFIED**, **E2 — ABSTRACT ONLY**, **E3 — METADATA / ABSTRACT**, **E4 — UNVERIFIED**. E1 does not mean every author interpretation was experimentally identified. Scientific statements below distinguish **VERIFIED FULL TEXT**, **METADATA ONLY**, and **INFERENCE**. Proposed MP1-R measurements are requirements or inferences, never completed experiments.

Local PDFs were converted with `pdftotext -layout`; PDF hashes matched the original extraction records for the 12 registry PDFs inspected. S04's original external PDF was accessible and its hash matched the mentor provenance; Fig. 1 was also inspected visually. The historical `pypdf` preflight failure does not imply missing full text now. Formula glyphs can be corrupted in extraction: dimensional definitions below are reviewer definitions unless explicitly described as a paper's result. Source evidence locations and hashes are archived in `outputs/reports/MP1_R_PHASE_3_2026-10-02/source_provenance.json` and the provenance appendix.

## 2. A — Source Access Register

“Available” means actually accessible in this session. A historical FULL_TEXT label alone was not accepted for new Phase 2 sources.

| Source ID | Access Level | Full Text Available? | Safe Uses | Restrictions |
|---|---|---|---|---|
| S01 / E01 | E1 | Yes, local PDF | Nonmetallic wire/rope jamming; vacuum bending/torsion response | Not steel-wire evidence; interfaces not independently partitioned |
| S02 / E02 | E1 | Yes, local PDF | Positive-pressure granular chamber, bending and architectural controls | Particle contacts; no NiTi inference; pressure range depends on test |
| S03 / E03 | E1 | Yes, local PDF | Nylon-fiber positive-pressure prototype; model, fitted state transitions | Local contact pressure/slip are modeled, not independently measured |
| S04 / E04 | E1 | Yes, original mentor PDF | SMA circumferential tightening, wire–rubber pull-out and robot bending | Actuator transformation is distinct from structural-wire transformation |
| S05 / E07, Parts I and II | E1 | Yes, two local PDFs | Isothermal cable/subcomponent tension, DIC/IR, transformation | Not a 1×7-only study; no pressured bending; Part II is accepted-manuscript version |
| S06 / E10 | E1 | Yes, local PDF | Short steel-rope stiffness bounds, eigenstrain kinematics, bending validation | No predictive hysteresis-cycle law or explicit pressure/contact-force solution |
| S07 / E09 | E1 | Yes, local PDF | NiTi transformation-aware UMAT and frictionless cable contact | Cannot support a frictional Coulomb implementation; metadata year 2020 |
| S08 / E13 | E3 | Not reopened | Identity and inherited MRI wording restriction | No new regulatory interpretation or prototype safety result |
| S09 / E05 | E1 | Yes, local PDF | SMA-to-fluid displacement, wet-actuator thermofluidic modeling | Pump architecture; not the proposed axial SMA-spring piston |
| S10 / E06 | E1 | Yes, local PDF | Embedded electro-conjugate-fluid micropump and negative-pressure jamming | Positive pressure produces bending actuation, not the reported jamming stiffening |
| S11 / E08 | E1 | Yes, local PDF | Mixed NiTiNOL–steel rope hysteresis and absorber experiments | Mechanism attribution/phenomenology does not separately measure each loss term |
| S12 / E11 | E1 | Yes, local PDF | Steel experimental validation; SMA numerical/contact comparison | Do not call the SMA shake-table response experimentally demonstrated |
| S13 / E12 | E1 | Yes, local PDF | Braided NiTi DMA/thermal response and geometry comparisons | Microslip contribution is interpreted; no macro pressure-controlled bending |
| S14 / E14 | E3 | No | Inherited existence-only MRI/SMA robot citations | Composite 2015/2018 entry; no transfer of device validation |
| S15 | E1 | Yes, university-hosted PDF through web tool | Review orientation, with use boundary in §12 | Local download failed; no primary-test attribution |
| S16 | E2 | No | Abstract-level objective, broad variable-stiffness scope | No detailed taxonomy, cited-primary-study list, or architecture proof |
| S17 | E1 | Yes, publisher PDF saved locally | Surgical flexible-robot taxonomy and measurement-definition caution | Correct authors are Lin, Song, Wang; not Li et al.; no prototype MRI validation |
| S18 | E4 | Intended paper unavailable | Identity discrepancy only | Supplied DOI is an AGV/SLAM paper; no layer-jamming claims |
| S19 | E4 | Intended paper unavailable | Identity discrepancy only | Supplied DOI is a steel–concrete composite-beam paper; no NiTi survey claims |
| S20 | E4 | No identified original | Retrieval deficit only | DOI checks returned Crossref 404; no fixture/mechanism attribution |
| S21 | E4 | Intended paper unavailable | Identity discrepancy only | Supplied DOI is a Scalet shape-memory-polymer review; no Copaci/SMA-coil dynamics |
| V-W02 / `53200aa0c6` | E1 | Yes, local PDF | Existing Souza UMAT + frictional contact as a live baseline | Existing W02 evidence; axial loading; no new MP1-R validation |

**Revised distribution for S01–S21:** E1 = 14, E2 = 1, E3 = 2, E4 = 4. This replaces the Phase 2 claim of 18 verified full texts for appraisal purposes only. It does not alter any historical corpus file.

## 3. Artifact and source conflicts

### AC01 — H0a meaning

**[ARTIFACT CONFLICT]**

**Artifact A:** W02 defines H0a as constant-modulus elastic substitution, already refuted in transformation-active regimes.

**Artifact B:** the Phase 3 request defines H0a as material-dominated *thermomechanical* response.

**Scientific consequence:** refuting constant E does not refute a nonlinear, temperature-aware material explanation.

**Phase 3 resolution:** preserve `H0a-W02` as history; use `H0a-R` for the material-dominated competitor. No universal strain onset, including W02's 0.75%, is transferred to the unspecified MP1-R wire lot.

### AC02 — H0b and S06

**[ARTIFACT CONFLICT]**

**Artifact A:** Phase 2 calls Barsi the primary homogenized Coulomb/hysteresis competitor.

**Artifact B:** W02 defines H0b as existing transformation-aware NiTi constitutive behavior plus frictional contact; S06 original §6 states hysteresis-cycle prediction remains future work.

**Scientific consequence:** fitting a pressure-dependent loop cannot be tested against S06 alone; its failure outside scope cannot prove H1.

**Phase 3 resolution:** S06 is a stiffness-bound competitor. `H0b-R` is the broader conventional model family; V-W02 supplies a directly inspected transformation/contact precedent. S07 is frictionless, not proof of that family by itself.

### AC03 — Positive-pressure range for S02

**[ARTIFACT CONFLICT]**

**Artifact A:** Phase 2 lists 0–150 kPa.

**Artifact B:** W02 says up to 200 kPa; original experiments use multiple ranges, including 69, 103, 138, 172 kPa for one bending series and 100.5, 195.6, 290.1 kPa for the wearable system.

**Scientific consequence:** neither inherited maximum describes every test.

**Phase 3 resolution:** use test-specific ranges from S02, not a single pooled maximum. Quantitative comparison requires the matching configuration.

### AC04 — S01 material and metallic-jamming wording

**[ARTIFACT CONFLICT]**

**Artifact A:** Phase 2 calls S01 steel; W02 uses Bai to support metallic wire jamming.

**Artifact B:** S01 original §2.2 and §3.1 describe kraft rope, hemp rope, and nylon wire; kraft rope is selected subsequently.

**Scientific consequence:** S01 proves nonmetallic wire/fiber jamming, not steel or NiTi jamming.

**Phase 3 resolution:** tighten E01/C1's source attribution. The historical broad novelty rejection is not resurrected; metallic/NiTi statements require the relevant cable sources.

### AC05 — S10 pressure sign and bibliography

**[ARTIFACT CONFLICT]**

**Artifact A:** Phase 2 puts positive pressure in S10's jamming mechanism; W02 C4 assigns a different Nature Communications DOI to Huynh, and C8 assigns another DOI to Pierce.

**Artifact B:** the chapter matrix supplies the intended titles and DOIs; S10 original stiffness tests use negative pressure, with positive pressure used for bending actuation. S09's original DOI is `10.1109/TMECH.2012.2211032`.

**Scientific consequence:** pressure sign and DOI substitution change the claimed precedent.

**Phase 3 resolution:** retain the engineering precedent with the chapter-matrix/original identities; prohibit the wrong DOI pairings and positive-pressure-jamming attribution to S10.

### AC06 — Priority-1 S18 identity

**[ARTIFACT CONFLICT]**

**Artifact A:** Phase 2 assigns `10.5194/ms-16-1-2025` to Zhang & Yao layer-jamming/homogenized-beam prior art.

**Artifact B:** publisher and archived Crossref metadata identify Wei Wang, Zhenhao Bao, Jiqiang Zheng, Tianbo Wang, *Research on automated guided vehicle (AGV) path tracking control based on laser simultaneous localization and mapping (SLAM)*, 2025, 16, 1–24. [Publisher record](https://ms.copernicus.org/articles/16/1/2025/).

**Scientific consequence:** the claimed P1 precursor/model cannot be evaluated, and its mechanism cells are unsupported.

**Phase 3 resolution:** quarantine S18; require the actual intended citation/full text. Do not import the AGV paper as a mechanics source.

### AC07 — S19/S20/S21 integrity

**[ARTIFACT CONFLICT]**

**Artifact A:** Phase 2 calls these verified NiTi survey, interface-isolation experiment, and SMA spring-dynamics sources.

**Artifact B:** S19's DOI identifies Ye et al., a 2024 steel–concrete nonlinear-interface-slip article; S20's exact DOI returns Crossref 404, with no intended original found by exact-string checks; S21's DOI identifies Scalet's 2020 shape-memory-polymer overview. [S19 publisher](https://ascelibrary.com/doi/10.1061/JSENDH.STENG-13096), [S21 publisher citation](https://doi.org/10.3390/act9010010?urlappend=%3Futm_source%3Dresearchgate.net%26utm_medium%3Darticle).

**Scientific consequence:** S20 cannot prove established separation fixtures; S21 cannot support SMA time constants. A Crossref 404 is a failed identity verification, not proof no intended study exists.

**Phase 3 resolution:** quarantine all three. S19/S21 are non-blocking after deleting their unsupported contributions; S20 remains blocking for the specifically requested material method appraisal.

### AC08 — Review identities and access

**[ARTIFACT CONFLICT]**

**Artifact A:** Phase 2 names S17 as Li et al. and gives detailed primary references/taxonomy for abstract-only S16.

**Artifact B:** S17 original cover names Botao Lin, Shuang Song, Jiaole Wang; S16's Crossref abstract establishes only broad review scope.

**Scientific consequence:** wrong authors and abstract-to-full-text promotion undermine attribution.

**Phase 3 resolution:** correct S17 within this report; limit S16 to E2. No inferred primary-reference list is approved. [S17 publisher PDF](https://journal.hep.com.cn/bir/EN/PDF/10.1016/j.birob.2024.100168).

### AC09 — Scope, pressure direction, and H1 burden

**[ARTIFACT CONFLICT]**

**Artifact A:** Phase 2's MP1-R row says controlled normal force and describes flexible pressure/TiNi coupling as the remaining gap; W02 ties scientific value to a new coupling law.

**Artifact B:** the authoritative rescope states that pressure acts outward, the reaction surface/interface is unknown, and characterization can be the MSc contribution; H1 is optional.

**Scientific consequence:** outward loading may increase wire–sleeve resistance without increasing inter-wire contact; a new law is not required for a valid characterization thesis.

**Phase 3 resolution:** keep MP1-R interface-neutral; mark its force mapping UNKNOWN. H0b success limits a constitutive novelty claim but does not erase controlled engineering characterization value.

### SC01 — S03's own parameter-identification inconsistency

**Original source conflict:** S03 abstract groups E and μ as identified from zero-pressure bending; §5.1 identifies E from zero-pressure data but μ from the full-slip-load versus pressure regression over pressurized tests.

**Resolution:** detailed methods govern the appraisal: E is a structural effective fit, and μ is an effective pressure-series fit. The same regression is later described as validation. Treat that as consistency with calibration, not independent verification of local Coulomb friction.

## 4. B — Core Source Appraisal Table

All scientific descriptions in the following verified rows are **VERIFIED FULL TEXT** at the locators in §19. Transfer assessments and identifiability criticism are **INFERENCE**. NR means not reported/verified here, not zero.

| Source | Actual objective and material/geometry | Loading, boundary, interface, normal-force origin | Constitutive/contact treatment | Outcome and design appropriateness |
|---|---|---|---|---|
| S01 | Characterize detachable soft actuators with nonmetallic wire/rope jamming; kraft/hemp/nylon alternatives | Bending/torsion; sealed compliant envelope; fiber contacts; atmospheric compression under vacuum | Independent versus composite-beam idealization; structural friction locking | Force–deflection/torque response; appropriate for structural tunability, not interface force isolation |
| S02 | Positive-pressure granular structure and wearable support | Cantilever bending; inner bladder expands against particles within fabric sleeve; particle–particle and particle–boundary contact | Equivalent beam/modulus and geometric scaling; average contact-force assumptions | Pressure-dependent force–deflection plus architecture controls; supports PPJ in that system |
| S03 | Pressure-dependent fiber-chain response; 700 nylon fibers, 0.4 mm diameter | Three-point bending, 100 mm span, two axes, 20 mm/min; resin links; polyethylene bladder; fiber–fiber modeled, wall reaction present | Constant effective E and μ; Coulomb threshold; equivalent-section and transition interpolation | F–δ branch slopes and critical loads; appropriate prototype model assessment, limited mechanism identification |
| S04 | Circumferential SMA friction control of a multi-backbone robot; eight 0.5 mm superelastic wires, TPU center, disks, rubber tube | One-wire pull-out and end-loaded bending; wires slide through disks; spring squeezes wire–rubber contact | Actuator thermal transformation; structural baseline energy plus friction work; arc/sliding approximation | Pull-out force, F–δ slope, inferred EI, heating/cooling; direct interface-oriented precedent |
| S05 (pair) | Nearly isothermal response of 7×7 and 1×27 NiTi cables and extracted hierarchical components | Axial tension, constrained end rotation, torque; helical contacts generated by construction/load | Transformation-sensitive observations; component compatibility simplifications; lubrication comparison | Load/strain/torque with stereo DIC and IR; strong local material-response evidence, no pressure-bending validation |
| S06 | Analytical stiffness limits for short steel single-/multi-strand ropes | Quasi-static 0.2 Hz bending loops; ends clamped to arms with horizontal slider to suppress tension; helical wire contacts | Linear-elastic Timoshenko/curved-wire eigenstrain states; whole-section regime assumption | Upper/lower measured cycle slopes compared to analytical limits; appropriate for bounds, not cycle prediction |
| S07 | Incremental NiTi UMAT/cable simulation and comparison with published tension data | Simplified 7×7 cable, fixed/axially displaced ends; **smooth frictionless contact** | Transformation-dependent modulus; isothermal tension/contact | Stress–strain and phase variable; valid transformation/contact precedent with known friction omission |
| S11 | Pinched-hysteretic vibration absorber using mixed NiTiNOL/steel ropes | Cyclic bending/displacement, sliding supports and later dynamic absorber rig; inter-wire contact | Phenomenological hysteresis; authors attribute loss to friction and transformation | Force loops and dynamic performance; mechanism partition remains unresolved |
| S12 | Experimental–numerical steel/SMA rope assessment | Axial cyclic/seismic response with end fasteners; physical steel shake-table tests; SMA simulations | Superelastic constitutive parameters; hard contact and constant penalty friction μ=0.5 | Steel experiment/model comparisons and numerical SMA response; not a new physical NiTi validation |
| S13 | Wide-temperature damping of braided NiTi microfilaments; braid count/density variants | Small-amplitude DMA/thermal cycling, cyclic tension; braid confinement/contact | Material transformation and microslip interpretation; no predictive coupled mechanics law | Loss tangent/storage modulus versus temperature/frequency/geometry; no direct loss partition |
| S15 | Review-level appraisal: taxonomy orientation only; see §12 | Reviewed studies have heterogeneous test conditions | Not an original experiment | Method appraisal cannot validate MP1-R quantitatively |
| S18 | Intended Priority-1 layer-jamming study unidentified | NR | NR | Appraisal attempted; unavailable; no scientific method judgment possible |
| S20 | Intended P2 interface-isolation study unidentified | NR | NR | Appraisal attempted; unavailable; no apparatus or necessity claim possible |

**Ancillary appraisals:** S09 examines wet SMA actuators driving positive-displacement diaphragm pumping chambers via a lever and thermofluidic/bond-graph modeling; it establishes SMA-to-fluid precedent, not a universal passive-cooling time. S10 characterizes an ECF micropump and jamming/bending actuator; stiffness uses vacuum and assembled-device pressure is inferred from separate no-flow calibration. S17 reviews surgical variable-stiffness methods; its printed §1.2 calls d/F and θ/τ stiffness, although these have compliance dimensions. These formulas must not be copied as MP1-R stiffness definitions.

### 4.1 Methodological quality and measurement validity

| Source | Design/internal validity | Measurement validity | Mechanism identifiability and transfer assumption |
|---|---|---|---|
| S01 | Vacuum-on/off comparison supports a structural effect; material and packing alter response | Global F–δ/torque measure the whole assembly | Inter-fiber versus membrane contribution not separated; no metal substitution warranted |
| S02 | Bladder/airbag and granular controls strengthen architecture attribution | Cantilever stiffness is configuration-specific | Equivalent E includes packing/boundary effects; local particle normal force not directly measured |
| S03 | Repeats and two bending modes are strengths; E/μ identification shares response data with model assessment | Slopes/critical loads valid structural observables; regime labels depend on segmentation | Local slip/normal stress not directly observed; uniform p, constant μ/E, negligible membrane effects limit transfer |
| S04 | Pull-out provides an extra observable beyond bending | One-wire sliding force better identifies tube resistance than global hysteresis | Does not directly measure normal force or backbone transformation; equal friction and arc assumptions constrain attribution |
| S05 | Whole-cable and extracted-component measurements plus DIC/IR reveal local transformation | Load/torque/strain/temperature are multiple channels | Lubrication insensitivity does not imply no friction; tensile clenching differs from externally pressured bending |
| S06 | Tailored slider reduces tension confounding; multiple lengths/amplitudes test stiffness bounds | Cycle slopes are not local slip or μ measurements | Assumed simultaneous regimes and linear wires; no contact-pressure or hysteresis evolution law |
| S07 | Comparison uses external experiments; geometry is simplified | Agreement tests global tensile response | Friction omission biases response; its failure cannot be attributed to missing new coupling |
| S11 | Quasi-static characterization then dynamic validation | Loop area is total dissipation; guide friction contaminates dynamics | **MECHANISM NOT IDENTIFIABLE FROM THIS TEST ALONE** for separate transformation/friction losses |
| S12 | Steel experiment/FE comparison is useful; clamping slip and missing loops weaken validation | Numerical NiTi response is not experimental measurement | Constant friction and imported SMA parameters cannot prove pressure/bending sufficiency |
| S13 | Thermal/geometry comparisons support braid-dependent response | DMA loss/modulus are global frequency/temperature-dependent proxies | **MECHANISM NOT IDENTIFIABLE FROM THIS TEST ALONE** for microslip versus transformation contribution |
| S15 | Review orientation, no primary mechanism experiment | Cross-study metrics require original definitions | Analogue-only transfer; see review-use boundary |
| V-W02 | Existing material/contact formulation compared with published axial data | Global cable response with material inputs from existing data | Souza UMAT plus friction; ignores some end constraints and tension/compression asymmetry; reported discrepancies remain |

**No unreported design feature was presumed:** homogeneous packing, isothermal conditions, perfect stick, full slip, small deformation, constant μ, and uniform pressure are source-specific assumptions, not a common validated property of all systems. Rate dependence and thermal effects require separate calibration when transferring quasi-static studies.

## 5. C — Methodological Comparability Matrix

Eligibility is for the stated argument, not permission to pool every result. No current study is DIRECTLY COMPARABLE to a physically unspecified MP1-R cross-section. A future direct comparison requires the same specimen, boundary, pressure/thermal history, loading path, and metric.

| Study A | Study B | Theory | Material | Geometry | Loading | Boundary | Interface | Measurement | Eligibility |
|---|---|---|---|---|---|---|---|---|---|
| S03 | MP1-R | Constant-E friction model versus transformation-aware candidate | Nylon versus TiNi | Rigid linked chain versus unknown flexible bundle | Bending overlap | Rigid cavities versus unresolved sleeve | Fiber–fiber modeled; MP1-R unresolved | F–δ slopes versus planned M–κ/local channels | CONDITIONALLY COMPARABLE for state/pressure trends after geometry mapping; no pooled stiffness ratio |
| S04 | MP1-R wire–sleeve option | Energy/friction versus calibrated pressure/friction | Superelastic structural wires plus thermal SMA; MP1-R lot unknown | Disk-guided perimeter wires versus proposed bundle | Pull-out/bending overlap | Outer squeeze versus outward loading | Wire–rubber versus proposed wire–sleeve | Pull-out and bending | CONDITIONALLY COMPARABLE if sleeve interface confirmed; no actuator equivalence assumed |
| S06 | MP1-R | Eigenstrain limits versus transformation/contact | Steel versus NiTi | Helical ropes versus unknown straight/helical bundle | Bending overlap | Slider/arms versus unknown clamps | Inter-wire versus unresolved dual interface | Force slopes versus M–κ | MECHANISTIC ANALOGUE for stiffness bounds |
| S05 | V-W02 | Material response versus constitutive/contact FE | NiTi systems tied to literature calibration | 7×7/1×27 cable configurations | Tension overlap | Physical clamp versus idealized constraints | Internal cable contact | Load/strain/torque comparisons | CONDITIONALLY COMPARABLE; shared calibration data are not independent replication |
| S05 | MP1-R | Transformation baseline | NiTi; lot/state mismatch | Helical cable versus unresolved bundle | Tension versus bending | Different end constraints | Internal contact versus sleeve/pressure | DIC/IR plus force versus planned measurements | MECHANISTIC ANALOGUE |
| S06 | S11 | Limit-stiffness model versus fitted hysteresis model | Steel versus mixed NiTi/steel | Rope architecture differs | Cyclic bending overlaps | Both address tension suppression, other fixture differences | Rope contacts | Bounds versus loops/dynamic response | CONDITIONALLY COMPARABLE for bounds only; no damping pooling |
| S07 | V-W02 | Frictionless UMAT versus Souza + friction | Both SMA cable | Simplified versus explicit helix construction | Axial tension | Different end treatment | Frictionless versus frictional contact | Global stress/strain | MECHANISTIC ANALOGUE; not controlled friction-ablation evidence |
| S12 | MP1-R | FE constitutive/contact | Numerical SMA, steel physical tests | Rope versus bundle | Axial/seismic versus bending | Fasteners versus sleeve | Rope contact | Numerical loops versus future measured M–κ | MECHANISTIC ANALOGUE |
| S13 | MP1-R | Mechanistic interpretation versus model discrimination | NiTi but thermal/phase domains differ | Microbraid versus macro bundle | DMA/tension versus bending | Braid confinement versus applied pressure | Inter-filament contact | tanδ/storage modulus versus stiffness/slip | MECHANISTIC ANALOGUE; DMA loss is not bending-loop energy |
| S01 | S03 | Independent/composite-beam idealization versus pressure-state model | Paper/hemp/nylon versus nylon | Envelope versus rigid chain | Bending overlap | Vacuum envelope versus positive bladder/rigid wall | Fiber contacts plus boundaries | F–δ | CONDITIONALLY COMPARABLE qualitatively after pressure-path distinction |
| S02 | S03 | Equivalent granular beam versus fiber-state model | Particles versus fibers | Annulus versus linked fiber cavity | Bending, different fixtures | Fabric sleeve versus rigid links | Particle versus fiber contacts | Different F–δ definitions | MECHANISTIC ANALOGUE |
| S09 | MP1-R Bench B | Wet SMA/fluid dynamics versus proposed spring/piston | SMA wire versus spring | Lever/diaphragm versus axial piston | Thermal/fluid operation | Hot/cold-water supply versus unresolved circuit | Fluid/seal pathways differ | Temperature, pumping versus force/stroke/pressure | MECHANISTIC ANALOGUE |
| S10 | MP1-R Bench B | ECF pump versus thermal SMA | Different actuator | Integrated ECF device versus piston | Pressure/stiffening | Vacuum stiffening versus positive pressure | Granular versus wire system | No-flow inferred pressure versus desired specimen measurement | NOT COMPARABLE for SMA timing; engineering precedent only |
| S18 | Any core source | Unknown intended paper | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | NOT COMPARABLE — E4 |
| S20 | S04 or MP1-R | Unknown intended method | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | NOT COMPARABLE — E4 |

**Metrics policy — INFERENCE:** translational stiffness `kδ=dF/dδ` has units N/m; secant `F/δ` depends on the path and origin. Bending tangent rigidity `Btan=dM/dκ` has units N·m²; secant `M/κ` needs its stated reference. Effective EI from cantilever or three-point bending requires the corresponding boundary/beam assumptions. Neither d/F nor a dimensionless stiffness ratio is interchangeable with Btan. Loop work is `∮M dθ` for an end rotation θ, or `∫∮M dκ ds` for a beam; `∮M dκ` alone is energy per length, not total work.

## 6. D — P1 Competitor Dossiers

### 6.1 S03 — Zhang & Yao (2026)

**Verified implementation:** §3–4, resin shell links (R=6 mm, h=4 mm, a=3 mm); 700 nylon fibers of 0.4 mm diameter; links spaced 12 mm; an internal polyethylene bladder, 10 mm wide and 0.1 mm thick, pushes fibers toward the cavity wall. Air pump, gauge, valve; 0–300 kPa in 50 kPa steps. Three-point bending on a 100 mm span, dry support contacts, flat indenter, 20 mm/min; two bending axes, five repetitions per condition. The 60 pressurized curves exclude the zero-pressure state from three-regime segmentation.

**Model/contact:** Euler–Bernoulli fiber rod, pressure-dependent equivalent section, constant effective E and μ, Coulomb shear capacity, jamming/transition/slipping states. Pressure in the bladder is assumed to equal effective uniform confinement. Membrane bending and nonuniform transmission are neglected. The transition-area law is phenomenological quadratic interpolation. Local contact forces and individual slip events are not directly resolved. Critical loads and stiffnesses are algorithmically extracted from F–δ curves.

**What S03 Demonstrates — A, direct:** one prototype has a pressure-dependent bending response; fitted transition loads and slipping-state stiffness rise approximately with pressure, while the jammed branch is relatively geometry-dominated within its tested domain. The study develops and assesses an architecture-specific analytical model. It uses **nylon**, not glass fiber or TiNi.

**Authors' inference — B:** transitions are associated with inter-fiber slip; regression consistency supports Coulomb-type resistance. These interpretations are not independent local-interface measurements. E=4.85 GPa is fitted from zero-pressure structural bending; μ=0.3665 is fitted from the pressurized full-slip-load slope. Reuse of that slope is not external validation, and fitted “effective” parameters can absorb packing, wall contact, support effects, and pressure-transfer error.

**What S03 Does NOT Demonstrate — D:** individual contact normal force; wall-versus-fiber loss partition; directly imaged slip-state fields; material-independent μ/E; cross-specimen generality; NiTi transformation; an SMA pressure source; integrated hydraulic dynamics; a universal pressure-to-stiffness law. Repeated tests on a prototype are not independent specimen replication.

**Which MP1-R Claims S03 Preempts:** positive-pressure fiber confinement for variable bending stiffness; pressure-dependent friction/slip modeling; using multiple bending-state branches as a new principle; a first analytical pressure–fiber–bending model. These preemptions do not depend on whether MP1-R uses another actuator/material.

**What Remains Open After S03 — C, analogy:** transfer to a confirmed TiNi/contact/sleeve geometry, independently calibrated pressure transfer and interface observables, and whether conventional material/contact laws explain its response. These are unresolved for MP1-R, not established literature-wide gaps.

**What MP1-R Must Measure to Distinguish Itself:** same-lot wire response, specimen pressure, sleeve deformation/reaction-path evidence, relevant interface sliding resistance/local slip, and M–κ at controlled temperature, rate, history, and end constraints. A calibrated model should be evaluated on reserved conditions. Such tests establish transferability and attribution; held-out testing alone does not establish novelty.

### 6.2 S04 — Jeon et al. (2022)

**Verified topology:** §II and Fig. 1 show a central TPU backbone and eight spaced peripheral superelastic wires guided by disks. The wires are attached at the base and slide through other disks; this is not a densely packed cable. A rubber tube covers the center segment and a 1.5-turn SMA spring surrounds it. Heating makes the spring seek a smaller circumference, squeezing the tube inward. Structural wires are stated to be superelastic; a separate alloy/phase characterization of them is not provided in the inspected methods. Do not treat actuator transformation as measured backbone transformation.

**Interface/measurements:** §IV.A pulls one peripheral wire 5 mm at 10 mm/min while the others remain fixed, measuring sliding force against the rubber arrangement. §IV.B displaces the end disk by up to 5 mm, also at 10 mm/min, and defines stiffness from F–δ slope. The model uses friction work and a circular-arc sliding geometry, with effective EI inferred using cantilever assumptions. These independently measured pull-out forces strengthen friction attribution compared with bending alone, while contact normal-force and all potential parasitic losses are not directly separated.

**What S04 Demonstrates — A:** thermal SMA-spring actuation changes sliding resistance at a wire–rubber interface and the robot's bending response. Reported stiffness ratios are 1.45, 1.50, 1.41 for the three specified backbone-envelope diameters. §IV.C reports heating from 25 to 60 °C in approximately 18, 21, 115 s at 0.5, 0.4, 0.3 A, and natural cooling around 60 s. These are specimen-specific thermal timings, not piston pressure t10–t90 measurements.

**Authors' inference — B:** friction work accounts for the observed stiffness increase under assumed geometry and similar wire friction. Thermal states refer primarily to the actuator. No new structural-wire constitutive law is identified.

**What S04 Does NOT Demonstrate — D:** pressure-actuated piston control; inter-wire jamming in a packed TiNi bundle; a independently quantified transformation contribution of the structural wires; direct normal-force mapping; general thermal speed limits; MRI validation of MP1-R.

**Claims S04 Preempts:** SMA-actuated friction modulation of wire-based flexible structures and ensuing stiffness change. The future-work discussion already proposes fluidics for greater friction range and faster SMA cooling; a fluidic substitution cannot be presented as an unanticipated mechanics principle.

**Questions Still Open — C:** outward-pressure transmission in MP1-R; its actual reaction interface; pressure-versus-temperature effects; whether the same near-specimen pressure trajectory yields the same structural response across sources.

**Required MP1-R Discriminating Evidence:** interface-specific resistance or another validated local observable, actual force direction/reaction surface, temperature at actuator and structural wires, pressure at source/specimen, and matched structural paths. A spring topology change alone is insufficient scientific distinction. **SMA AS ACTUATOR** is verified; **NiTi AS STRUCTURAL LOAD-BEARING MATERIAL undergoing transformation in this bending test** is not independently demonstrated.

### 6.3 S06 — Barsi et al. (2025)

**Verified formulation:** steel helical single-/multi-strand ropes modeled as a shear-deformable Timoshenko beam, constituent wires as curved rods, incompatible eigenstrains encoding limiting kinematics. §2 distinguishes perfect stick, partial stick, full slip, plus axial–torsional response. Wires are linear elastic and infinitesimal kinematics are used; all wires are assumed to occupy the same regime. The paper derives generalized section stiffness and solves boundary-value problems. “Homogenized” is appropriate as equivalent-beam description; it must not imply a locally resolved friction law.

**Validation:** §3 and Fig. 3 use rigid end arms/clamps with a horizontal slider to suppress tension during 0.2 Hz cyclic bending, varying rope lengths and amplitudes. Cycle data provide minimum/maximum slopes; §4 compares these with model predictions. The theoretical perfect-stick limit is not automatically the experimentally attained upper branch; partial-stick comparisons matter. Clamp accuracy, effective length, and short-length/torsional effects limit transfer. These are controlled-end tests, not a free rope.

**What it demonstrates — A:** existing eigenstrain/beam mechanics predicts useful stiffness limits for tested steel ropes and compares with axial–torsional literature data. Experimental hysteresis exists.

**What it does not demonstrate — D:** a predictive hysteresis-cycle evolution/dissipation law; explicit calibrated Coulomb μ; pressure-to-normal-force distribution; gradual wire-by-wire slipping; NiTi thermomechanics; active transverse pressure. §6 explicitly leaves hysteresis-cycle prediction and combined bending/tension to further work. Coulomb/contact studies discussed in the introduction must not be laundered into the paper's own formulation.

**Conditions under which H0b may be sufficient — INFERENCE:** conventional geometry/contact laws with independently calibrated normal-force transmission and friction plus a same-lot NiTi law predict measured stiffness, loops, and local slip within declared uncertainty. S06 may supply a low-strain limit check when its rope kinematics/boundaries are justified. It is not the entire H0b model.

**Conditions under which H0b fails — INFERENCE:** a specified, adequately resolved conventional model with locked material/contact/pressure-transfer parameters produces systematic reserved-condition errors beyond its uncertainty, after thermal/rate/fixture/sleeve effects are bounded. Exceeding S06's linear-elastic scope, or finding a loop S06 does not attempt to predict, demonstrates inapplicability of S06, not failure of all conventional mechanics.

**Experimental measurements required to reject H0b:** independent wire constitutive response, actual pressure-transfer/contact bounds, interface friction/local slip, M–κ loops and temperature/history with held-out pressure–curvature paths. Failure of one model is insufficient to establish a new law; reasonable conventional alternatives must also be evaluated and the proposed coupling needs a local discriminating observable.

**V-W02 check:** *Mechanical response of single and double-helix SMA wire ropes*, DOI `10.1080/15376494.2021.1955313`, uses a **Souza** model and frictional contact, not the Auricchio implementation asserted in W02 prose. It is numerical axial-cable work compared with existing experiments, with reported stress discrepancies and end-condition limitations. Thus H0b remains plausible and unvalidated for MP1-R; “already adequately explains MP1-R” is prohibited.

## 7. E — Corrected Mechanism Matrix

Cell format: **status: content**. `V=VERIFIED`, `C=SUPPORTED_WITH_CAVEAT`, `N=NOT_ESTABLISHED`, `I=INCORRECT` (inherited cell corrected), `NA=NOT_APPLICABLE`. Multi-element does not automatically mean metallic multi-wire. “Controlled N” distinguishes controlling an input from measuring local normal force. “Phase” distinguishes actuator from structural transformation.

| Source | NiTi | Multi-wire/element | Bending | Controlled N | Positive pressure | Inter-wire/fiber friction | Sleeve/boundary friction | Active phase transformation | SMA actuation |
|---|---|---|---|---|---|---|---|---|---|
| S01 | V: no | I: nonmetal rope/nylon, not steel | V: yes | C: vacuum input; local N not measured | V: no for jamming | C: locking model; interface losses not isolated | N: membrane loss not independently shown | NA | V: no |
| S02 | V: no | NA: particles | V: cantilever | C: bladder p controlled; local N inferred | V: yes | NA: particle contact, not wire | C: boundary present; friction partition not measured | NA | V: no |
| S03 | I: nylon, not glass/TiNi | V: 700 fibers | V: two modes | C: bladder p, assumed uniform confinement | V: yes | C: model/fitted μ, not direct microslip | N: wall shear not isolated | NA | V: no |
| S04 | C: NiTi SMA actuator; structural wires called superelastic | V: eight peripheral wires | V: end-loaded | C: spring-state squeeze, not measured local N | V: no | N: no inter-wire mechanism demonstrated | V: wire–rubber sliding test | V: actuator; N: backbone contribution | V: circumferential spring |
| S05 | V: yes | I: 7×7/1×27 plus components, not 1×7 alone | V: no, tension | C: internally generated contact; no external control | V: no | C: contact/lubrication inference; no friction-loss partition | NA | V: local transformation evidence under tension | V: no thermal actuator |
| S06 | V: steel | V: helical ropes | V: cyclic | N: no pressure/contact-N solution | V: no | C: eigenstrain slip states; no fitted Coulomb law | NA | NA | V: no |
| S07 | V: NiTi | V: cable | V: no, tension | N: no external pressure control | V: no | I: friction omitted | NA | V: modeled and compared, not original measurement | V: no |
| S09 | V: SMA wire | NA: not bundle | V: no | C: pump pressure, not bundle N | V: fluid displacement | NA | N: MP1 seal loss not measured by this source | V: actuator model/operation | V: wet SMA wire, not MP1 spring |
| S10 | V: no | NA: granular | V: bending tests | C: pressure inferred from separate calibration | I: yes for actuation; no for jamming | NA: particles | N: wall loss not isolated | NA | V: no, ECF |
| S11 | V: NiTi/steel | V: rope | V: cyclic/absorber | N: no applied pressure | V: no | C: authors' attribution/phenomenology | NA: no sleeve | C: superelastic attribution, loss partition unresolved | V: no |
| S12 | V: numerical NiTi | V: rope | V: no direct MP1-type bending | N: no pressure control | V: no | V: FE friction; N: local experimental partition | NA | V: numerical constitutive response | V: no |
| S13 | V: NiTi | V: braid | I: DMA/tension, not macro bending | C: packing confinement, not controlled local N | V: no | C: microslip interpretation, not isolated measurement | NA | C: thermal/transformation evidence; contribution not isolated | V: no |
| S18 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 |
| S20 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 |
| S21 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 | N: E4 |
| MP1-R | Proposal: TiNi | Proposal: bundle | Planned | N: actual interface N unknown | Planned; fluid unresolved | N: unresolved | N: unresolved | N: backbone phase unmeasured | Planned SMA spring/piston |

S19 remains E4 background and contributes no mechanism evidence. E1 denotes source access, while C versus V distinguishes modeled/author-inferred mechanisms from direct measurements. A NiTi specimen is never sufficient for a “phase transformation active” cell.

## 8. F — Pressure-to-Normal-Force Chain

The status below refers to the strongest evidence actually available, with a separate MP1-R limitation. All proposed calibrations are **INFERENCE**. Pressure is a distributed boundary input; local contact force requires geometry and equilibrium.

| Link | Evidence | Status | Source | Remaining Uncertainty |
|---|---|---|---|---|
| Source → specimen fluid pressure | S03 gauge/valve sets bladder p; S10 uses separate no-flow pressure calibration | DIRECTLY MEASURED at the reported gauge / EXPERIMENTALLY CALIBRATED in S10 | S03 §4.1; S10 stiffness methods | MP1-R needs actual two-location transient data; gauge location alone does not establish transfer equality |
| Fluid pressure → chamber/sleeve deformation | Bladder expansion provides force path; S03 neglects membrane nonuniformity | MODELED / ASSUMED | S02; S03 §3 | MP1-R membrane compliance, residual stress, voids, fluid type and direction UNKNOWN |
| Deformation → radial/reaction load | Reaction against enclosing structure follows architecture | MODELED / INFERRED | S02; S03; rescope | Outward versus inward force paths differ; reaction sleeve may bend or stretch |
| Radial load → local wire–wire/wire–sleeve N | S03 equates effective uniform confinement to bladder p | ASSUMED | S03 §3 | No independently measured local N distribution; MP1-R UNKNOWN, possibly opposite trends at two interfaces |
| N → friction capacity | Coulomb threshold in S03; tube sliding force in S04 | MODELED in S03 / DIRECTLY MEASURED resistance in S04 | S03 §2/5.1; S04 §IV.A | Pull-out estimates μN plus parasitics, not N alone; μ may depend on surface/state/history |
| Friction capacity → slip state | S03 branch segmentation; S06 prescribed eigenstrain states | INFERRED / MODELED | S03 §4.2; S06 §2 | Transition load is not direct local slip observation; interface attribution unresolved |
| Slip/material/sleeve state → bending response | Global F–δ measured; model links to effective section or friction work | DIRECTLY MEASURED global response / MODELED mechanism | S03; S04; S06 | MP1-R material transformation, sleeve rigidity, axial force and boundary loss remain confounded |

**Equations and assumptions — INFERENCE, not experimental results:**

\[
\mathbf t=-p\mathbf n,\qquad |F_{t,i}|\leq\mu_iN_i,
\qquad F_{\rm pull}=\sum_i F_{t,i}+F_{\rm parasitic}.
\]

Here t is fluid traction on a chosen wetted body surface, p the pressure difference referenced to the opposing pressure, and n its outward normal. `N_i` is the normal contact force at interface i; `F_{t,i}` is tangential contact resistance and μi its friction coefficient. The contact inequality is a Coulomb assumption, not a measured MP1-R property. The pressure traction acts on the membrane/chamber surface; it is not automatically the traction on every wire interface.

For a chosen piston force orientation,

\[
A_p\Delta p=F_{\rm SMA}-F_{\rm bias}-F_{\rm seal}-m_p\ddot x,
\qquad Q\simeq A_p\dot x-C_h\dot p-Q_{\rm leak}.
\]

Ap is piston area; Δp is pressure across it; spring, return, seal forces carry their signed directions; mp is moving mass, x stroke, Q delivered volume flow, Ch effective hydraulic/pneumatic volume compliance, Qleak leakage. These lumped balances need a defined circuit and fluid; compressible gas cannot be silently modeled as incompressible liquid. Quasi-static p≈Fnet/Ap and ΔV≈ApΔx omit those losses/storage terms. No source justifies identifying applied p with all local Ni.

## 9. G — H0a / H0b / H1 Competition

**Logical calibration:** the request's H1 “meaningful interaction” can be produced by conventional laws and therefore overlaps H0b. It is not automatically W02's H1 requiring a new law. Use `H1-R` for observable coupled response and `H1-new` for an additional constitutive coupling. These aliases do not modify W02. Material-dominated and conventional-contact explanations need declared adequacy criteria; no numerical thresholds are invented here.

| Hypothesis | Supporting Evidence | Counter-Evidence | Required Measurements | Falsification Criterion |
|---|---|---|---|---|
| H0a-R: intrinsic TiNi thermomechanics sufficiently explains measured stiffness/hysteresis | S05 local transformation; S13 thermally dependent braided response | S03/S04 show contact-driven modulation in other architectures; no MP1-R counter-data | Same-lot single-wire/material calibration; backbone T, rate, strain/history; sleeve-only baseline; matched p/curvature paths | Reproducible pressure-dependent residual above declared uncertainty with material/temperature/history matched and interface slip/resistance co-varying; excludes material-only sufficiency, not proves new law |
| H0b-R: conventional contact/stick-slip plus appropriate NiTi/material/boundary mechanics suffices | S03 friction model; S06 elastic bounds; V-W02 Souza/contact precedent; S12 numerical contact | No locked MP1-R validation; pressure transfer, sleeve and boundary assumptions not resolved | Independently calibrate geometry, material, friction/contact transmission; local slip and M–κ; reserve validation paths | A specified adequate baseline fails systematically beyond combined measurement/model uncertainty on reserved paths after known alternatives/confounders are bounded; rejection of one simplification does not reject the entire family |
| H1-R: confinement/contact/slip and TiNi state interact materially in measured response | S11/S13 authors' interpretations suggest coexistence; S05 shows material state matters | Coexistence or a nonlinear global loop is not an identified interaction; no MP1-R data | Orthogonal pressure/material-state contrasts, local slip/strain and T, independently bounded sleeve/contact terms | Within the declared accessible domain, state-conditioned pressure effects are accounted for by separable material/contact components or remain below detection; then additional claimed interaction is unsupported |
| H1-new: a new constitutive/contact coupling is necessary (optional W02 extension) | None decisive in this corpus | V-W02 shows conventional formulation exists; H0b remains live | All H0b tests plus a defined additional law and local predictions distinguishable from conventional alternatives | Conventional locked model succeeds, or added coupling is unidentifiable/not predictively necessary; H0a-W02 failure alone never supports H1-new |

`H0a-W02` constant-E substitution can be inadequate when transformation occurs; it may be useful in a independently established low-strain phase-stable domain. Rejection of constant E is not rejection of material-dominated H0a-R. A pressure-induced response (`H1P` in the draft) is only an engineering effect test, not proof of H1-new. Global bending alone cannot distinguish all three mechanisms: **MECHANISM NOT IDENTIFIABLE FROM THIS TEST ALONE**.

## 10. Confounder Register

No confounder is documented as already controlled in the unbuilt MP1-R system. “Measurable” describes feasibility; uncontrolled factors become interpretation-threatening when correlated with p, temperature, or cycle order. Source anchors show why the factor matters, not a validated MP1-R correction.

| Confounder | MP1-R classification now | Threat and required control/measurement | Evidence anchor |
|---|---|---|---|
| Wire diameter | Measurable; uncontrolled | Alters individual bending rigidity and contact/strain; same lot and measured diameter | S04 dimensions; S05 cable geometry |
| Wire count | Measurable; uncontrolled | Changes contact network and section; record count, do not compare unmatched ratios | S03; S05 |
| Packing / helix geometry | Interpretation-threatening | Pressure can rearrange geometry rather than change μ; document section and evolution | S01; S03; S06 |
| Sleeve material | Interpretation-threatening | Changes friction and adds structural response; material/surface specified | S04; S02 |
| Sleeve thickness | Measurable; uncontrolled | Changes membrane tension/pressure transfer and bending contribution | S03 membrane assumption |
| Sleeve compliance | Interpretation-threatening | Applied p may be stored in sleeve expansion; deformation/baseline needed | S02; S03 |
| Initial preload | Interpretation-threatening | Determines contact before p; retain assembly/end preload records | S06 clamp uncertainty; reviewer inference |
| Pressure | Measurable; uncontrolled | Source/specimen differences and equilibrium dwell; record reference/location | S03; S10 |
| Friction coefficient / surface | Interpretation-threatening | Pull-out may identify μN, not μ separately; surface/roughness/lubrication/history | S05 lubrication; S03 fitted μ |
| Temperature | Interpretation-threatening | SMA heat and material transformation can shift mechanical response | S05; S04 |
| Loading rate | Measurable; uncontrolled | Thermal equilibration and friction dynamics differ; matched paths | S05 isothermal tests; S06 0.2 Hz |
| Curvature / strain | Interpretation-threatening | Slip and transformation have different onset domains; measure local strain when claiming transformation | S03; S05 |
| Phase state | Interpretation-threatening | NiTi presence is not phase activity; same-lot calibration/phase-sensitive evidence | S05; S13 |
| Heat treatment / training | Measurable history; uncontrolled | Different lots/processes invalidate imported material parameters | S05 material differences; reviewer inference |
| Cycling history / wear | Interpretation-threatening | Shakedown, contact wear, rearrangement drift may mimic pressure effect | S05; S02 joint wear |
| End constraints / axial force | Interpretation-threatening | Clamps and tension alter apparent bending stiffness and hysteresis | S06 slider; S12 slippage; V-W02 end limitations |

“Controlled” may only be assigned after a protocol and records establish it. A correction fitted after viewing the validation set cannot retrospectively count as independent calibration.

## 11. H — Gap Validity Report

| Candidate Gap | Knowledge Gap? | Method Gap? | Engineering Requirement? | Evidence | Verdict |
|---|---|---|---|---|---|
| G1: wire–wire versus wire–sleeve disambiguation | Literature-wide gap NOT_DEMONSTRATED; MP1-R interface contribution unresolved | Applicable measurement/identification requirement, not proof no method exists | Yes: geometry, contact isolation, validation of attribution | S04 shows interface-oriented pull-out; S05 component decomposition; S20 unavailable | REFRAME_REQUIRED |
| G2: SMA-piston dynamics versus pure-pressure envelope | Literature absence NOT_DEMONSTRATED | Dynamic system identification and experimental decomposition | Yes: actuator/load/circuit matching and controls | S09 thermofluidic dynamics; S04 specific thermal lag; S10 calibration caution; S21 invalid | REFRAME_REQUIRED |

### 11.1 G1 questions

1. **Have other fields already separated these interfaces?** Current verified evidence demonstrates wire–tube resistance testing (S04) and cable component decomposition (S05). It does not verify Phase 2's alleged dedicated core-versus-sheath isolation fixture in S20. A general statement that Bowden/cable fields have completely solved this exact partition is not approved.
2. **Is the unresolved issue specifically a pressured TiNi bundle?** Yes as a system-specific identification question, conditional on a confirmed geometry. The corpus does not establish it as an untouched scientific question.
3. **Can global bending identify the dominant interface?** Without constraints or additional measurements, multiple contact/material/sleeve combinations can reproduce the same curve. **MECHANISM NOT IDENTIFIABLE FROM THIS TEST ALONE**. This is not a proof of impossibility for every augmented bending protocol.
4. **Are pull-out tests necessary?** They are a defensible option, not a unique logically necessary method. Local slip imaging, interface-isolating controls, or validated direct-shear/traction measurements may also discriminate mechanisms. The rescope asks for both-interface tests; keep that implementation requirement unless physical nonexistence/inaccessibility of an interface is documented and claims reduced. Pull-out itself can change packing and include seal/guide/end friction.
5. **Knowledge or parameter estimation?** A force measurement generally estimates resistance/parameters. It creates a scientific result only if it tests a defined unresolved relation or model boundary. Simply adding two pull-out fixtures is methodological work, not automatic novelty.

### 11.2 G2 questions

Joule heating/cooling, force–stroke hysteresis, bias return, seal friction, compliance, leakage and pressure transients form a dynamic chain. S09 already models coupled thermal/fluid/mechanical dynamics. S04's passive-cooling time is specific to its spring and thermal environment. S10 contains no SMA actuator and S21 cannot support SMA timing. Neither a universal 30–60 s cooling time nor instantaneous pressure equilibration across all bending models is established.

Bench A/B separation is scientifically **justified for attribution**, but the physical implementation need not be exactly two standalone rigs. A single setup with independent pressure control and synchronized observables can implement the same interventions. The need is to isolate actuator and specimen responses under a known load/compliance; no literature-wide decoupling gap is approved.

## 12. I — Bench Identifiability and Review Usage

### 12.1 Bench A

External pressure can identify an empirical pressure-conditioned structural envelope: F–δ or M–κ branches, repeatability, drift, transition proxies, and time dependence at a specified thermal/rate/geometry state. With suitable interface controls it can estimate wire–sleeve and wire–wire sliding resistance and pressure-transfer bounds.

It cannot determine μ and N separately from only their product, prove backbone transformation from hysteresis alone, or partition all sleeve/end/interface contributions from global stiffness. Without local measurements or an independent interface perturbation, fitting two friction coefficients to one curve is not identifiability. Material baseline and sleeve/fixture controls must match the claim being made.

### 12.2 Bench B

Under a known mechanical/fluid load it can characterize spring force–stroke–temperature, electrical input/energy, piston displacement, pressure rise/recovery, overshoot/settling, return force and cyclic drift. Two-location pressure shows source/specimen transfer. Seal loss cannot be uniquely estimated from p and stroke alone if SMA force and bias are unmeasured.

A blocked/dead-head piston test gives an actuator limit, not the connected specimen pressure waveform. A calibrated load/compliance representing Bench A is needed to interpret integrated behavior. Bench B identifies source dynamics; it does not identify wire interfaces.

### 12.3 Integrated A+B validation

Compare at matched **near-specimen pressure trajectory**, curvature/loading path, structural-wire temperature, initial packing/preload, and cycle history. Equality of steady p alone is insufficient when pressure/temperature transients or sleeve geometry differ. Demonstrate that Bench B reaches the Bench A pressure–volume envelope and that any structural difference can be separated from temperature, rate, leakage, sleeve deformation and history. If responses match, the SMA source is an implementation choice; if they differ, first test those conventional explanations. No new law follows automatically.

These are identifiability conditions, not a hardware redesign. Geometry confirmation and future pilot data are execution gates; they do not by themselves block a cautious literature handoff. The blocking deficits here are missing source identities/methods.

### 12.4 Review-paper usage audit

| Source | Taxonomy / history / search vocabulary | Mechanism classification | Gap claims | Quantitative mechanics |
|---|---|---|---|---|
| S15 | Allowed within its review scope | Review orientation only | Does not prove MP1-R absence | Trace primary experiment first |
| S16 | Abstract-level broad orientation | Detailed taxonomy not approved | No MP1-R gap proof | Prohibited from E2 |
| S17 | Allowed for surgical flexible-robot methods | Classifications are secondary evidence | Application challenges do not establish MP1-R novelty | Trace primary source; printed inverse-stiffness definitions need dimensional correction |
| S19 | Quarantined | Prohibited | Prohibited | Prohibited |

S15 actually focuses on 2001–2023 laminar-jamming publications and excludes fiber/particle jamming. Its categories include friction, mechanical interference and miscellaneous mechanisms. Positive-pressure shape actuation must be distinguished from vacuum locking. These limits prevent its use as a comprehensive fiber-jamming review. [Original review](https://opus.lib.uts.edu.au/bitstream/10453/181920/2/Review%20paper-Laminar%20Jamming-published%20version.pdf), Introduction, §§3, 4.1, 7.

No numerical result from a review is treated as the review's own experiment. No primary-reference list claimed by Phase 2 for abstract-only S16 is approved without inspection.

## 13. Search Coverage and P0 Audit

Search-log counts alone do not establish saturation: saved hit lists, exclusion decisions, reproducible database/date coverage, and traceable citation-chase stops are absent from the supplied Phase 2 report. This appraisal did not repeat discovery.

| Stream | Revised assessment | Reason / allowable boundary |
|---|---|---|
| Recent reviews | SEARCH_COVERAGE_ADEQUATE_FOR_CURRENT_THESIS_SCOPE for orientation only | Verified review access plus S16 abstract allows background mapping; detailed scope corrected; not exhaustive |
| Coupled NiTi mechanics | PARTIAL_SATURATION | Strong local material/contact analogues exist; missing unified theory is not demonstrated; S19 invalid |
| Interface decoupling | SATURATION_NOT_DEMONSTRATED | Central S20 method source unidentified; standard-fixture claim lacks verified support |
| Positive-pressure jamming | SEARCH_COVERAGE_ADEQUATE_FOR_CURRENT_THESIS_SCOPE for broad prior-art boundary | S02/S03 preempt principle claims; S18 claimed precursor invalid; no group monopoly or complete forward coverage established |
| SMA piston actuation | PARTIAL_SATURATION | S09 precedent and S04 thermal example suffice for cautious framing; S21 invalid and no exact MP1-R source dynamics available |

**P0 classification:** `NO DIRECT OVERLAP IDENTIFIED IN SEARCHED CORPUS`. This is a report of identification, not evidence of global absence or an exhaustive P0=0 count. Source-identity errors weaken the auditability of Phase 2's inventory further. No claim that one laboratory is the unique/primary active group is approved. No “unified theory does not exist” statement is approved.

## 14. J — Contradiction Register

| ID | Apparent disagreement | Classification | Evidence / Phase 3 disposition |
|---|---|---|---|
| CR01 | S03 says pressure raises slip-branch stiffness but jammed branch is comparatively insensitive; broad “p raises stiffness” prose | DIFFERENT_RESEARCH_QUESTION | Load regime matters within the same source; qualify branch/geometry rather than enforce monotonicity everywhere |
| CR02 | S01 vacuum jamming versus S02/S03 positive-pressure jamming | METHOD_EXPLAINED_DIFFERENCE | Different pressure paths compress confined media; no contradiction about pressure sign in isolation |
| CR03 | S04 thermal SMA states versus S05 stress-induced transformation | DIFFERENT_RESEARCH_QUESTION | Actuator thermal transformation and structural material response must be separated |
| CR04 | S07 underpredicts tensile response; V-W02 has friction but residual discrepancy | INSUFFICIENT_EVIDENCE | Models differ in geometry, law and boundary; not a controlled friction-effect comparison |
| CR05 | S11/S13 assign hysteresis/damping to combined transformation/friction | INSUFFICIENT_EVIDENCE | Loss partition not directly measured; cannot declare agreement on dominance |
| CR06 | W02/Phase 2 imply S06 predicts loops; original leaves that prediction open | TRUE_CONTRADICTION (artifact versus source, not study versus study) | Original §6 wins; bounds-only wording |
| CR07 | S03 abstract versus §5.1 identification of μ | TRUE_CONTRADICTION (within source wording) | Detailed methods win; calibration/validation dependence retained |
| CR08 | Outward mentor pressure versus inward historical cuff assumption | DIFFERENT_RESEARCH_QUESTION | Distinct interfaces/load paths; no hidden substitution of old geometry |
| CR09 | S12 title/abstract sounds experimentally SMA validated; methods separate steel experiment/SMA FE | INSUFFICIENT_EVIDENCE for physical NiTi validation | Detailed methods delimit claim; do not use title as proof |
| CR10 | S17 d/F or θ/τ labeled stiffness versus EI formula | TRUE_CONTRADICTION in measurement terminology | First two ratios are compliance dimensions; independently define metrics |
| CR11 | Phase 2 says remaining discrepancies arise from boundary and transformation ranges | INSUFFICIENT_EVIDENCE | Attribution not established by matched comparisons; keep alternatives explicit |

No TRUE_CONTRADICTION between comparable primary studies was established. This does not warrant “no meaningful contradictions remain”; several apparent disagreements are untestable with current comparability and observables.

## 15. Cross-Study Evidence Questions

This table records evidence eligibility, not a pooled cross-study synthesis.

| Question | Supporting Sources | Limiting Sources | Comparability | Evidence Strength | Remaining Uncertainty |
|---|---|---|---|---|---|
| Does confinement increase bending stiffness in multi-element structures? | S01–S04 | S03 regime specificity; material/geometry differences | Conditional structural analogues | STRONG for existence in tested architectures | Not guaranteed for outward-loaded MP1-R; no universal ratio |
| Can positive pressure control friction-induced bending stiffness? | S03; S02 granular analogue | Local N/friction inferred; rigid versus compliant reactions | S03 strongest partial overlap | MODERATE for architecture-specific mechanism interpretation | Pressure can change geometry and wall resistance; local force not isolated |
| Does TiNi transformation materially contribute to bundle hysteresis? | S05 local transformation; S11/S13 author interpretations | Tension/mixed rope/microbraid differ | Mechanistic analogues | MECHANISTIC_ANALOGUE_ONLY for MP1-R bending | Lot/strain/T domain, slip and phase contributions unmeasured |
| Can existing stick-slip mechanics explain expected MP1-R response? | S06 bounds; V-W02 material/contact | Neither validates MP1-R; S07 frictionless | Mechanistic analogues | MECHANISTIC_ANALOGUE_ONLY | Adequacy awaits independently calibrated tests |
| Can global bending distinguish wire–wire and wire–sleeve friction? | S04 extra interface test motivates additional observable | S03 global fitted mechanism; S20 missing | Identification argument, not pooled data | NOT_ESTABLISHED for global-only attribution | Multiple mechanisms fit same curve unless independent constraints supplied |
| Can SMA thermal dynamics be separated from structural mechanics? | S09 dynamics; S04 thermal/pull-out/bending channels | No MP1-R transient measurements | Analogue plus methodological inference | MODERATE for feasibility of decomposition | Requires intervention, synchronized channels, load matching |
| Is fluid p a reliable proxy for local interface N? | S03 assumes transmission; S02 architecture model | S10 calibration limitation; no local MP1 N | Geometry-dependent | NOT_ESTABLISHED as universal proxy | Membrane, packing, contact location and curvature mapping |
| Does prior art integrate major MP1-R mechanisms? | S03 pressure/fiber/bending; S04 SMA/friction/wires; V-W02 NiTi/contact; S09 fluid actuation | No verified exact full-chain identity | Strong partial overlaps, not direct matching | LIMITED for absence of exact combination | No direct overlap identified; invalid new records and nonexhaustive search prevent global absence |

## 16. K — Stable Phase 3 Claim Register and Wording Map

IDs C001–C022 belong only to Phase 3, not W02 C1–C8. A strength rating is scoped to the wording in that row. Methodological requirements are marked **INFERENCE**; they must not be cited as an experiment.

| Claim ID | Candidate Scientific Claim | Supporting Source IDs | Evidence Strength | Caveat | Allowed Wording |
|---|---|---|---|---|---|
| C001 | Wire/fiber jamming changes structural stiffness | S01, S03 | STRONG | Nonmetallic media; tested architectures | Multiple studies demonstrate tunable stiffness through wire/fiber jamming in their tested structures. |
| C002 | Positive-pressure jamming exists | S02, S03 | STRONG | Granular and fiber mechanisms differ | Positive-pressure jamming has been demonstrated in granular and fiber-based structures. |
| C003 | S03 demonstrates pressure-conditioned fiber-chain bending | S03 | MODERATE | Single nylon prototype; fitted effective parameters | Zhang and Yao report pressure-dependent critical loads and slipping-branch stiffness in a nylon-fiber chain over 0–300 kPa. |
| C004 | S03 locally verifies pressure equals fiber normal traction | S03 | NOT_ESTABLISHED | Uniform transmission assumed | The conversion of bladder pressure into local interface normal force is not independently established in this study. |
| C005 | S04 SMA actuation changes wire–tube friction and stiffness | S04 | MODERATE | Direct inward squeeze; spaced wires | Jeon et al. demonstrate SMA-spring modulation of wire–rubber sliding resistance and structural stiffness. |
| C006 | S04 establishes backbone phase-transformation contribution | S04 | NOT_ESTABLISHED | Actuator and backbone states differ | It remains unclear whether transformation of the structural wires contributed materially to the tested bending response. |
| C007 | NiTi cable local transformation matters beyond constant E | S05 pair | STRONG for its tension domain | Not a universal bending/strain threshold | Isothermal NiTi cable and component tests demonstrate transformation-sensitive local response; a constant-E substitution is inadequate in those transformation-active regimes. |
| C008 | Existing equivalent-beam models provide slip-state stiffness limits | S06 | MODERATE | Linear steel ropes; whole-section regime assumption | Barsi et al. validate limit-stiffness predictions for tested short steel ropes. |
| C009 | S06 predicts hysteresis cycles via Coulomb friction | S06 | NOT_ESTABLISHED | Original explicitly leaves cycle prediction open | Its experiments contain hysteresis, but its formulation does not predict the hysteresis cycle. |
| C010 | Transformation-aware material/contact models exist | V-W02; S12 numerical | MODERATE | Axial/cable scope and imperfect validation | Existing numerical formulations combine transformation-aware SMA response with frictional contact. |
| C011 | H0b sufficiently predicts MP1-R | V-W02, S06 analogues | MECHANISTIC_ANALOGUE_ONLY | No MP1-R measured validation | Related cable mechanics provides a conventional baseline whose adequacy for MP1-R remains to be tested. |
| C012 | Transformation and friction can coexist in hysteretic assemblies | S11, S13; S05 material evidence | MODERATE for interpretation | Contributions not independently partitioned | Available mixed-rope and braid studies attribute response to combined material and contact mechanisms; their individual contributions are not fully isolated. |
| C013 | MP1-R bending alone establishes dominant wire interface | S03/S04; identification analysis | NOT_ESTABLISHED | Inference: underdetermined without constraints | Global bending alone does not establish which interface dominates in the proposed unresolved geometry. |
| C014 | Pull-out directly identifies N or μ separately | S04; reviewer force balance | NOT_ESTABLISHED | Pull-out resistance includes μN and parasitics | Pull-out measures sliding resistance; separate normal-force or friction calibration is needed to infer its components. |
| C015 | SMA-to-fluid actuation has prior art | S09 | MODERATE | Wet wire/lever/diaphragm, not exact spring piston | SMA-actuated fluid displacement and coupled pump modeling have prior art. |
| C016 | Onboard pressure-source integration with jamming exists | S10 | MODERATE | Negative-pressure ECF jamming | Micropump integration with negative-pressure jamming is an engineering precedent. |
| C017 | Passive SMA cooling always takes over 30 s | S04 example; S21 invalid | NOT_ESTABLISHED | Geometry/environment specific | Jeon's tested spring cooled naturally in approximately 60 s; this does not define MP1-R response time. |
| C018 | Bench decomposition supports attribution | S09/S04; methodological inference | MODERATE | No claim two separate rigs are uniquely necessary | Independent pressure and actuator characterization is a justified way to separate structural response from source dynamics. |
| C019 | H1-new follows from hysteresis or constant-E failure | W02 guardrail; S05; V-W02 | NOT_ESTABLISHED | Conventional material/contact may produce both | Neither global hysteresis nor rejection of constant E establishes a new constitutive/contact law. |
| C020 | Exact MP1-R full-chain study absent worldwide | Phase 2 identification report | NOT_ESTABLISHED | Invalid records; search not exhaustive | NO DIRECT OVERLAP IDENTIFIED IN THE SEARCHED CORPUS. |
| C021 | Interface disambiguation is a proven scientific gap | S04/S05; S20 E4 | NOT_ESTABLISHED | System identification requirement verified only as inference | The interface contribution remains unresolved for the proposed MP1-R configuration; a literature-wide knowledge gap is not demonstrated. |
| C022 | MP1-R is MRI compatible or final topic locked | Scope input; S08/S14 restricted | NOT_ESTABLISHED | No prototype validation or global topic lock | MP1-R is the active rescope being evaluated; MRI remains an application-oriented design constraint. |

**Allowable wording map:** STRONG permits “demonstrate” with the exact studied system; MODERATE permits “indicate/report” and configuration limits; LIMITED permits “available evidence suggests”; MECHANISTIC_ANALOGUE_ONLY requires “related cable/rope mechanics suggests” and explicit non-equivalence; NOT_ESTABLISHED requires “it remains unclear,” a tested-domain boundary, or removal of the affirmative claim. “Multiple studies demonstrate” is forbidden when there is only one direct source, or merely a review plus its cited primary study.

## 17. L — Method / Limitation Register

| Source ID | Methodological Strength | Key Limitation | Why It Matters | MP1-R Consequence |
|---|---|---|---|---|
| S01 | Multiple jamming media, vacuum/bending/torsion contrasts | Envelope and packing move; nonmetallic materials | Geometry and boundary resistance contribute to stiffness | Do not use as a steel/NiTi calibration or interface partition |
| S02 | Bladder/airbag controls, pressure and geometry tests | Equivalent granular modulus; bladder compliance and unverified transition timing | Pressure effect belongs to a constrained architecture | Need actual specimen pressure/contact mapping; no imported response time |
| S03 | Explicit pressure-state model, repeats, two axes | Rigid reaction wall; assumed uniform pressure; fitted E/μ; single prototype | Transfer and fitted parameters can absorb boundary/contact effects | Independent calibration, local channels and reserved tests; no universal pressure–N equality |
| S04 | Single-wire sliding measurement plus bending | Arc geometry, average friction, unknown backbone transformation | Pull-out is useful but not full normal-force/loss partition | Match interface and distinguish actuator T from structural T |
| S05 pair | Component dissection and simultaneous DIC/IR | Nearly isothermal axial cable domain; alloy/construction differences | Local tensile transformation does not prove macro bending coupling | Same-lot structural baseline and actual strain/T domain required |
| S06 | Analytical geometry-based bounds; tension-reducing fixture | Linear material, common slip regime, no loop evolution/contact-pressure solution | Bounds can succeed while mechanism/transient prediction remains unresolved | Use as scoped limit competitor, not full H0b |
| S07 | Transformation-aware UMAT | Smooth frictionless contact and simplified section | Missing friction changes nominal stress | Do not claim it implemented conventional friction successfully |
| S11 | Quasi-static plus dynamic absorber validation | Phenomenological response and parasitic dynamic guide friction | Loop area combines multiple losses | Identify local state if attributing transformation/friction fractions |
| S12 | Steel tests plus contact FE | SMA results numerical; clamping/data loss; constant μ | SMA validation is not an independent physical experiment | Use as model precedent, not MP1-R adequacy proof |
| S13 | Temperature/frequency/braid comparisons | Small-amplitude DMA; unpartitioned loss interpretation | Damping response differs from macro stiffness and active confinement | Analogue only; no direct microslip-force calibration |
| S15 | Secondary orientation | No primary experiment | Review classification cannot calibrate mechanics | Review-use restrictions apply |
| S18 | None appraisable for intended study | Wrong DOI identity | Supposed comparator's methods unavailable | Blocking retrieval |
| S20 | None appraisable | Intended source unidentified | Claimed fixture evidence cannot be reconstructed | Blocking retrieval |
| V-W02 | Explicit existing material/contact formulation | Axial tests, boundary simplifications, stress mismatch | Existence does not prove all conventional models are accurate here | Test a locked appropriate baseline rather than presume success/failure |

## 18. M — Corrected Phase 2 Claims: Mandatory Overclaim Audit

Each row provides the requested original statement, assessment, evidence, problem, safer formulation, and future wording. Counts apply only to these 20 units: **3 retained, 11 weakened/reframed, 6 rejected**. Mechanism-cell corrections are not counted a second time. Rejected means rejected as an evidential assertion, not the research project.

| ID | Original Phase 2 statement | Phase 3 assessment / disposition | Evidence | Problem, if any | Safer formulation / allowed future wording |
|---|---|---|---|---|---|
| P2A01 | Wire/fiber jamming is established | SUPPORTED / retained | S01, S03 | Specify nonmetal media for Bai | Use C001 |
| P2A02 | Positive-pressure jamming is established | SUPPORTED / retained | S02, S03 | Architecture-specific | Use C002 |
| P2A03 | Jeon preempts broad SMA-controlled wire friction novelty | SUPPORTED / retained | S04 §II/IV | Tube interface | Use C005; no inter-wire substitution |
| P2A04 | No unified constitutive theory coupling positive pressure and transformation exists | NOT_DEMONSTRATED / weakened | No exhaustive absence evidence; V-W02 conventional coupling | Existence of no retrieved exact theory is not nonexistence | No such unified theory was established by the verified sources inspected here. |
| P2A05 | P0=0; no study implements full chain | PARTIALLY_SUPPORTED / weakened | Phase 2 inventory report | Identity errors and nonexhaustive coverage | Use C020's corpus-limited formulation |
| P2A06 | Interface gap strengthened as valid engineering/mechanics gap | OVERSTATED / weakened | S04/S05; S20 unavailable | Requirement conflated with knowledge gap | System-specific interface attribution remains unresolved; G1 REFRAME_REQUIRED. |
| P2A07 | Mechanically impossible to infer inter-wire jamming without separate pull-out rigs | OVERSTATED / weakened | Identifiability analysis; S04 | Global-only problem is real; unique-test necessity not proved | Global bending alone is insufficient in this unresolved geometry; independent interface evidence is required. |
| P2A08 | Piston dynamic transients strengthened as a decoupling gap | PARTIALLY_SUPPORTED / weakened | S09; S04; S21 invalid | Dynamics/integration requirement is not absent theory | G2 is dynamic identification and experimental decomposition. |
| P2A09 | Bench A architecture strongly validated | OVERSTATED / weakened | S03 pressure-controlled setup; no MP1 test | Literature supports logic, not this apparatus/performance | Bench A is methodologically justified and remains unvalidated for MP1-R. |
| P2A10 | Barsi is primary Coulomb/hysteresis H0b formulation | CONTRADICTED / rejected | S06 §2/6; W02 H0b definition | No cycle evolution law; no explicit calibrated contact-N law | S06 supplies linear slip-state stiffness bounds; full H0b needs material/contact/pressure treatment. |
| P2A11 | S09/S10/S21 demonstrate SMA passive cooling >30 s and seal/stroke limits | CONTRADICTED / rejected | S10 ECF; S21 wrong identity; S09 wet actuation | Non-SMA source and invalid DOI; universal timing ungrounded | Use S04-specific times; MP1-R timing/seal loss must be measured. |
| P2A12 | No unresolved contradictions; differences explained by boundaries/transformation ranges | NOT_DEMONSTRATED / rejected | CR01–CR11 | No matched causal comparison; source/artifact contradictions exist | Retain the contradiction register and unresolved mechanism attribution. |
| P2A13 | All 18 full-text sources are verified; no blocking retrieval deficit | CONTRADICTED / rejected | Access register; AC06–08 | Wrong identity and unsupported availability labels | 14 E1 sources verified here; two blocking intended-source deficits remain. |
| P2A14 | S18 is Zhang & Yao's 2025 continuum layer-jamming precursor | CONTRADICTED / rejected | Publisher DOI and Crossref record | DOI maps to AGV/SLAM | S18 quarantined pending actual intended source. |
| P2A15 | S20 proves dedicated core/sheath separation rigs | CANNOT_VERIFY_FROM_CURRENT_CORPUS / rejected | DOI 404, intended paper absent | No reconstructable method | S20 supplies no scientific evidence until identity/full text restored. |
| P2A16 | Review stream SATURATED | OVERSTATED / weakened | Review access and supplied search log | No reproducible stop/hit evidence | Coverage adequate for current orientation, not exhaustive saturation. |
| P2A17 | Coupled NiTi stream SATURATED | OVERSTATED / weakened | S05/S11/V-W02; S19 invalid | Unification/absence not established | PARTIAL_SATURATION; conventional competitors remain live. |
| P2A18 | Interface-decoupling stream SATURATED | NOT_DEMONSTRATED / weakened | S20 retrieval deficit | Core method assertion unverified | SATURATION_NOT_DEMONSTRATED. |
| P2A19 | Positive-pressure stream SATURATED; Zhang/Yao group primary | OVERSTATED / weakened | S02/S03; S18 invalid | No reproducible group/forward-chase completeness | Coverage adequate for broad prior-art boundary only. |
| P2A20 | SMA piston stream SATURATED | OVERSTATED / weakened | S09; S21 invalid | Partial actuator analogues, no universal dynamics | PARTIAL_SATURATION; exact actuator envelope unresolved. |

### 18.1 Current narrative scientific audit

The working draft already keeps interfaces neutral, H0b live, H1 unproven, MRI as a constraint, and physical experiments prospective. These boundaries are retained. Its E07 tension limitation and E10 steel/pressure limitation also stand.

Scientific calibration needed before future writing: replace any S06 “hysteresis prediction” implication with measured loops and predicted stiffness limits; do not say Kang itself models Coulomb friction; use Souza for the inspected Vahidi implementation; do not describe S12 as physical NiTi experimental validation; distinguish author-attributed microslip from measured partition in S11/S13. “Valid gap” language in §1.3/§2.8 must become a system-specific identification problem pending gap evidence. Bench separation is a justified method, not already validated architecture, and H0b success does not invalidate the rescope's characterization contribution. No working-draft prose was changed.

## 19. N — Novelty Boundary

### 19.1 Already Established

Wire/fiber jamming tunability (S01/S03), positive-pressure jamming (S02/S03), SMA-spring friction modulation of a wire–tube structure (S04), NiTi cable transformation response (S05), slip-state beam stiffness limits (S06), conventional transformation/contact formulations (V-W02/S12 numerical), and SMA-to-fluid displacement (S09). These are established at their stated scopes, not universal proof of the full MP1-R chain.

### 19.2 Strong Partial Prior Art

S03 overlaps positive pressure, confined fibers, bending and pressure-state modeling. S04 overlaps SMA actuation, structural wires, friction modulation and bending. S06 overlaps analytical equivalent-beam/slip-state modeling and stiffness-bound validation, with narrower predictive capability than Phase 2 claimed. None alone resolves the exact proposed TiNi/piston/sleeve system.

### 19.3 Mechanistic Analogues

S05 tension/local transformation; S11 mixed-rope hysteresis; S12 numerical NiTi/contact; S13 microbraid DMA; V-W02 conventional NiTi/contact FE; S09 thermofluidic pump; S01/S02 different media/confinement. Analogy motivates controls and models, not equivalent parameter values.

### 19.4 Currently Unresolved in the Searched Corpus

For the proposed MP1-R geometry: actual interface and reaction path, pressure-to-contact map, accessible coexistence of structural transformation and slip, relative sleeve/material/contact effects, and whether an SMA spring/piston reproduces an externally imposed specimen-pressure envelope. The verified set does not establish exact full-chain overlap. Missing intended S18/S20 identities prevent completion of their requested appraisal. These unresolved items are not a final scientific-gap statement.

### 19.5 PROHIBITED NOVELTY CLAIMS

- First positive-pressure variable-stiffness or fiber-jamming principle/model (S02/S03 preempt).
- First SMA-controlled friction modulation of wire-based flexible structures (S04 preempts).
- First multi-wire slip-state beam/stiffness-bound model (S06 preempts).
- First wire/fiber jamming system (S01/S03 preempt).
- NiTi presence, another geometry/material, another pressure level, more FEA/measurements, or held-out testing as novelty by themselves.
- First SMA-to-fluid actuator solely because an SMA spring replaces another drive (S09 and historical closed component claims).
- First simultaneous transformation/contact response solely from a loop (V-W02/S11/S13 provide prior precedents/interpretations).
- First wire–wire versus wire–sleeve separation method based on unverified S20 or corpus absence.
- No unified theory exists; no exact competitor exists worldwide; “all five searches saturated.”
- MRI-safe/compatible/conditional prototype without device-specific validation; MP1-R officially locked as the final topic.
- H1 established because H0a-W02 fails, because S06 cannot predict a loop, or because the integrated actuator response differs at unmatched thermal/pressure histories.

## 20. What MP1-R Must Prove

### MUST DEMONSTRATE

Confirmed cross-section/reaction path and the actual pressure/fluid reference; reproducible pressure-dependent bending response or an honest null result with uncertainty; measurements sufficient for the chosen interface claim; externally controlled-pressure envelope and achievable SMA-source force/stroke/pressure/volume/recovery; matched-condition integrated comparison. These are requirements for the rescope characterization, not demands for a new law.

### MUST DISTINGUISH

If assigning a mechanism: material/temperature versus contact/sleeve/fixture contributions; wire–wire versus wire–sleeve where both exist; source transient versus specimen response. If pursuing H1-new: conventional locked H0b prediction versus a defined additional coupling with independently distinguishable local consequences. H1-new is optional for the current scope.

### SHOULD MEASURE

Sleeve deformation, local slip/strain at representative interfaces, same-lot thermal/material behavior, assembly preload, cycling history/drift, synchronized two-location pressure and temperatures. Direct N measurement is valuable but a validated bounded transfer estimate may suffice for narrower claims. Predetermine metrics and uncertainty; do not import another paper's pass threshold.

### OPTIONAL EXTENSION

New constitutive coupling, expanded fatigue/wear/rate domain, complete robot integration, MRI validation, and extensive local phase imaging beyond what the actual mechanism claim needs. They must not silently expand a MSc characterization project.

## 21. Evidence Gaps and Exit Gate

| Gap ID / class | Missing information | Affected claim/source | Required evidence | User retrieval required? |
|---|---|---|---|---|
| EG01 — BLOCKING | Actual intended Zhang/Yao 2025 layer-jamming comparator identity and text | S18; Priority-1 appraisal, comparability, Phase 2 precursor/model assertions | Correct title/DOI plus original PDF or accessible primary link; reconcile against wrong supplied DOI | Yes; intended identity cannot be inferred safely |
| EG02 — BLOCKING | Actual intended Wang 2023 core/sheath isolation source and test methods | S20; G1 precedent, P2 method appraisal | Correct title/authors/DOI and original methods/fixture description with locators | Yes; exact supplied DOI cannot verify this source |
| EG03 — IMPORTANT_BUT_NON_BLOCKING | Intended S19/S21 identities | Supplementary review/dynamics assertions | Correct citation/full text only if those assertions will be restored | Only if restoring their use; otherwise keep excluded |
| EG04 — IMPORTANT_BUT_NON_BLOCKING | S16 detailed review taxonomy | Review taxonomy/history beyond abstract | Original review full text | No immediate action; stay E2 |
| EG05 — IMPORTANT_BUT_NON_BLOCKING for Phase 4, execution gate later | Mentor geometry, fluid, reaction interface and load path | MP1-R mechanism specificity | Confirmed drawing and physical calibration | Mentor/researcher input required before mechanism-specific experiment; not a literature absence claim |
| EG06 — IMPORTANT_BUT_NON_BLOCKING for Phase 4, empirical gate later | Pressure/contact/μ transfer, same-lot material response and reserved-condition prediction | C004/C011/C013/H1-new | Future pilot/independent calibrations/local observations | Future experiment; not a paper download |
| EG07 — IMPORTANT_BUT_NON_BLOCKING | Reproducible Phase 2 hit/exclusion/forward-chase provenance | Saturation/P0 assertions | Existing raw search/export/stop records if available | Not needed for cautious corpus-limited wording; no broad re-search authorized here |
| EG08 — OPTIONAL | MRI device validation and detailed direct N/phase imaging | C022; expanded mechanisms | Device protocol/data or local sensors appropriate to later claim | No action in this phase |

**Why EG01/EG02 are blocking:** the task explicitly requires every relevant Priority-1/P1/P2 study to be methodologically appraised, including S18 and S20. Their intended originals are unavailable; evaluating the unrelated DOI targets or inventing their methods would falsely complete the gate. Quarantine permits cautious use of other evidence but does not satisfy those two required appraisals. S03/S04/S06 conclusions are independently available and do not await those retrievals.

**Exit gate:** `BLOCKED_FOR_EVIDENCE`. No conclusion that prior art kills the characterization rescope is warranted; there is therefore no basis to select `BLOCKED_FOR_METHOD_REASSESSMENT`. Current mechanism identifiability requires added observations/controls already allowed by the rescope. Broad H1-new claims would remain unsupported without those observations, but their absence does not prevent a bounded characterization question.

```text
Missing evidence: Intended 2025 layer-jamming/homogenized-beam paper; supplied DOI identifies AGV/SLAM.
Affected Source ID: S18
Affected claim: Priority-1 comparator appraisal and precursor/model comparison.
Why blocking: The required original comparator cannot be identified or methodologically checked.
Required user action: Provide the intended paper's correct citation/DOI and original PDF or primary full-text link.

Missing evidence: Intended 2023 wire-core/sheath interface-isolation paper and methods.
Affected Source ID: S20
Affected claim: Interface-isolation precedent and materially relevant P2 methodology.
Why blocking: The supplied DOI cannot verify the intended paper, so the required methods appraisal is unavailable.
Required user action: Provide the correct title/authors/DOI and original PDF or primary methods link.
```

## 22. O — Conditional Phase 4 Handoff Package

**Release status: HOLD — not authorized as READY.** Self-contained companion: `outputs/plans/MP1_R_PHASE_3_PHASE_4_HANDOFF_2026-10-02.json`. It embeds all controlled tables and the three competitor dossiers; this report is the human-readable handoff. No repository rescan is necessary to recover conclusions, restrictions, missing evidence or source paths.

| Required component | Contents / report location |
|---|---|
| 1. Approved source set | E1 sources S01–S07, S09–S13, S15, corrected S17; E2 S16 for abstract only; E3 S08/S14 for inherited background only; V-W02 for scoped H0b precedent; exclude E4 S18–S21 |
| 2. Source access levels | §2, including restrictions and E1 versus mechanism evidence distinction |
| 3. Corrected mechanism matrix | §7 |
| 4. Comparability classifications | §5; no quantitative pooling authorization |
| 5. P1 conclusions | §6; S03/S04 partial preemption, S06 bounds-only competitor |
| 6. Hypothesis matrix | §9; preserve H0a aliases and H1-R/H1-new distinction |
| 7. Gap statuses | §11; both REFRAME_REQUIRED, no final scientific-gap declaration |
| 8. Pressure-to-N chain | §8; MP1-R local force UNKNOWN |
| 9. Claim register | §16, C001–C022 |
| 10. Contradiction register | §14, CR01–CR11 plus AC/SC provenance |
| 11. Method/limitation register | §17 |
| 12. Wording map | §16 plus row-specific text; no E2/E3 mechanics promotion |
| 13. Remaining gaps | §21, EG01–EG08; two blocking |
| 14. Prohibited novelty claims | §19.5 |

**Resumption instruction:** recover the intended S18/S20 originals, appraise only those missing records and their dependent claims, then reevaluate the Phase 3 exit gate in a new revision. Do not automatically restore Phase 2 cells or saturation language after correcting a DOI. Other approved claims may be used for planning within their restrictions, but Phase 4 synthesis must wait for gate reassessment.

## 23. TARGETED EVIDENCE CHECK — External Audit Log

Seven exact-source checks (S15–S21) were performed, including seven exact-DOI query strings across search calls; direct opens/downloads and retries are retrieval operations, not corpus expansion. No broad literature search, forward-citation discovery, new source ID, or optional-gap discovery was performed. All checks concern claimed sources whose methods/access could not be recovered from the supplied files or the relevant V002 records. Publisher/university/Crossref records were used; third-party search snippets were not scientific authority.

| Check | Question / why corpus insufficient / exact missing evidence | Targeted query/source | Result | Impact |
|---|---|---|---|---|
| TEC01 S15 | Can the review's actual scope support Phase 2 orientation? New source has no extraction/locator in primary package | Exact DOI `10.3390/act13020064`; MDPI then university PDF | E1 PDF through web; Introduction/§§3,4.1,7 inspected. Local DNS failed even after escalated retry; MDPI PDF 403 | Scope/use corrected; web-access receipt archived |
| TEC02 S16 | Is detailed taxonomy justified by abstract-only access? Need authentic abstract | Exact DOI `10.1088/1361-665X/ad0753`; Crossref work record | Primary metadata/abstract saved; no full methods read | E2 maintained; detailed taxonomy/ref lists removed |
| TEC03 S17 | Does source identity match Li et al.? Need cover and methods/metric definitions | Exact DOI `10.1016/j.birob.2024.100168`; publisher-hosted PDF | Lin, Song, Wang; full PDF saved; §1.2 measurement definitions checked | Authors corrected, inverse-stiffness caution recorded |
| TEC04 S18 | Does alleged comparator DOI actually identify layer-jamming? Need source identity | Exact publisher URL and DOI `10.5194/ms-16-1-2025`; Crossref | Wang et al. AGV/SLAM, 1–24 | Quarantined; blocking intended comparator |
| TEC05 S19 | Is alleged NiTi survey identity sound? Need bibliographic record | Exact DOI `10.1061/JSENDH.STENG-13096`; ASCE/Crossref | Ye et al. steel–concrete interface-slip article, 2024 | Quarantined; no NiTi-review contribution |
| TEC06 S20 | Does claimed fixture source exist under supplied identity? Need actual methods paper | Exact DOI `10.1016/j.ijmecsci.2023.108312`; DOI open, exact-string search, encoded and direct Crossref requests | No intended original; Crossref HTTP 404 response saved | E4; no dedicated-fixture claim; blocking |
| TEC07 S21 | Can it support SMA coil dynamics? Need source identity | Exact DOI `10.3390/act9010010`; publisher citation/award record | Scalet, shape-memory polymers overview; Crossref retry 429 | E4 for intended Copaci study; thermal generalization removed |

No guessed corrected DOI was assigned to S18/S20/S21. The real papers behind wrong DOI strings are identity evidence only and were not silently admitted as new MP1-R studies.

## 24. References, Locators, and Provenance

The following reference identities come from original PDFs or the named primary identity checks. No page/figure/equation locator is invented. Local text files in `outputs/reports/MP1_R_PHASE_3_2026-10-02/` preserve PDF pagination/form feeds; source paths and hashes are in `source_provenance.json`. Quantitative source claims above should be checked at these locators before use outside the approved wording.

| ID | Reference / DOI | Verified locator and version |
|---|---|---|
| S01 | Bai et al. (2022), *Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming*. [DOI](https://doi.org/10.3390/app12073582) | Original §2.2, §3.1, Fig. 2d; material choices and vacuum tests; local S01 text |
| S02 | Liu et al. (2021), *A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots*. [DOI](https://doi.org/10.1109/LRA.2021.3097255) | Original bending/pressure-modulation/dimensional/wearable test methods and stated limitations; local S02 text |
| S03 | Zhang & Yao (2026), *A variable stiffness omnidirectional chain based on positive-pressure fiber jamming*. [DOI](https://doi.org/10.5194/ms-17-481-2026) | §§2–5; §4.1 materials/setup; §4.2 segmentation; §5.1 calibration; conclusion limitations; local S03 text |
| S04 | Jeon et al. (2022), *Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism*. [DOI](https://doi.org/10.1109/LRA.2022.3174363) | §II, Fig. 1 visually checked; §III; §IV.A–C; §V; original SHA-256 `65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03` |
| S05a | Reedlunn, Daly & Shaw (2013), *Superelastic shape memory alloy cables: Part I – Isothermal tension experiments*. [DOI](https://doi.org/10.1016/j.ijsolstr.2013.03.013) | Original experiment descriptions and summary/conclusions; DIC/IR, lubrication, cable constructions; local S05a text |
| S05b | Same authors (2013), *Part II – Subcomponent isothermal responses*. [DOI](https://doi.org/10.1016/j.ijsolstr.2013.03.015) | Accepted manuscript, cover/abstract and subcomponent methods/conclusions; use its version, not inferred publisher pagination |
| S06 | Barsi, Carboni & Lacarbonara (2025), *A new mechanical model of short wire ropes: Theory and experimental validation*. [DOI](https://doi.org/10.1016/j.engstruct.2024.119217) | §2 eigenstrain/linear hypotheses, §3 fixture, §4 comparisons, §6 future predictive limitations; Fig. 3; publication 2025, online 2024 |
| S07 | Kang et al. (2020), *Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables*. [DOI](https://doi.org/10.3901/JME.2020.14.065) | Original Chinese pp. 68–71: smooth contact and explicit friction omission; filename 2025 is not publication year |
| S09 | Pierce & Mascaro (2013), *A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump*. [DOI](https://doi.org/10.1109/TMECH.2012.2211032) | Original pump architecture and bond-graph/thermal-fluid equations; local S09 text |
| S10 | Huynh et al. (2022), *Soft actuator with switchable stiffness using a micropump-activated jamming system*. [DOI](https://doi.org/10.1016/j.sna.2022.113449) | Original stiffness methods/Fig. 11 and positive-pressure bending/Fig. 13; assembled pressure limitation, local S10 text |
| S11 | Carboni & Lacarbonara (2016), *Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments*. [DOI](https://doi.org/10.1061/(ASCE)EM.1943-7889.0001072) | Original mixed-rope characterization/absorber methods, model and dynamic discussion; local S11 text |
| S12 | Narjabadifam et al. (2024), *Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes*. [DOI](https://doi.org/10.3390/buildings14061567) | Original abstract, FE contact, experimental steel setup and conclusions; SMA experimental limitation retained |
| S13 | Liu et al. (2026), *High damping capacity with a wide temperature window in braided NiTi microfilaments*. [DOI](https://doi.org/10.1016/j.matlet.2026.141544) | Original braid/DMA methods and thermal/geometry response discussion; microslip attribution; local S13 text |
| S15 | Caro & Carmichael (2024), review identity in TEC01 | University-hosted full PDF; access receipt and §12 restrictions; no primary quantitative claims |
| S16 | Li et al. (2024), *Variable stiffness methods for robots: a review*. [DOI](https://doi.org/10.1088/1361-665X/ad0753) | Archived Crossref metadata/abstract; `S16_crossref.json` |
| S17 | Lin, Song & Wang (2024), *Variable stiffness methods of flexible robots for minimally invasive surgery: A review*. [DOI](https://doi.org/10.1016/j.birob.2024.100168) | Original publisher PDF cover and §1.2; `S17_fulltext.pdf` / `.txt` |
| V-W02 | Vahidi et al. (2022), *Mechanical response of single and double-helix SMA wire ropes*. [DOI](https://doi.org/10.1080/15376494.2021.1955313) | Existing `53200aa0c6`, V002 extraction; original §§2,4.2,5.1; Souza model/contact and comparison limitations; archived W02_VAHIDI text |

S08/S14 remain inherited E3 context with the primary chapter-matrix restrictions. Quarantined S18–S21 have their claimed identities preserved in the Phase 2 input; only the identity-check outcomes are used here. New source-response receipts are in the report directory. No unrelated wrong-DOI primary result is used as MP1-R mechanics evidence.

## 25. Completion Receipt and Limits

Primary inputs: **5/5**. Successfully methodologically appraised core IDs: **11** (S01–S07, S11–S13, S15; S05 pair counts once). Intended additional core appraisals S18/S20: **attempted but unavailable**, not counted as successfully appraised. Ancillary S09/S10/S17 and existing V-W02 were also assessed. P1 dossiers: **3/3**. Overclaim audit: **20 units**, retained **3**, weakened/reframed **11**, rejected **6**. Candidate scientific gaps supported: **0**; requiring reframing: **2**. Blocking evidence deficits: **2**. Targeted external source checks: **7**; broad discovery searches: **0**.

The durable report and conditional handoff contain the complete methodological decisions, claim restrictions and evidence gaps. Historical verification matrices, Phase 1/2 artifacts, working draft, scientific state and registry remain unchanged. The exit status governs Phase 4 release; creation of a handoff file is not a READY verdict. Stop after Phase 3.
