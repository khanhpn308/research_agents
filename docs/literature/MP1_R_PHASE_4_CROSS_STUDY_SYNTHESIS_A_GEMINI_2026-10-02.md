# MP1-R PHASE 4: CROSS-STUDY SYNTHESIS (RUN A_GEMINI)

**Date:** 2026-10-02
**Run Label:** `A_GEMINI`
**Status:** `READY_FOR_PHASE_4_RECONCILIATION`

## A. CROSS-STUDY COMPARABILITY MATRIX

| Study A | Study B | Theory | Material | Geometry | Loading | Boundary | Interface | Measurement | Eligibility |
|---|---|---|---|---|---|---|---|---|---|
| S03 | MP1-R | Constant-E friction model vs transformation-aware candidate | Nylon vs TiNi | Rigid linked chain vs unknown flexible bundle | Bending overlap | Rigid cavities vs unresolved sleeve | Fiber–fiber modeled; MP1-R unresolved | F–δ slopes vs planned M–κ/local channels | CONDITIONALLY_COMPARABLE for state/pressure trends after geometry mapping; no pooled stiffness ratio |
| S04 | MP1-R | Energy/friction vs calibrated pressure/friction | Superelastic wires + thermal SMA vs TiNi | Disk-guided perimeter wires vs proposed bundle | Pull-out/bending overlap | Outer squeeze vs outward loading | Wire–rubber vs proposed wire–sleeve | Pull-out and bending | CONDITIONALLY_COMPARABLE if sleeve interface confirmed; no actuator equivalence assumed |
| S06 | MP1-R | Eigenstrain limits vs transformation/contact | Steel vs TiNi | Helical ropes vs unknown straight/helical bundle | Bending overlap | Slider/arms vs unknown clamps | Inter-wire vs unresolved dual interface | Force slopes vs M–κ | MECHANISTIC_ANALOGUE for stiffness bounds |
| S05 | V-W02 | Material response vs constitutive/contact FE | NiTi systems tied to literature calibration | 7×7/1×27 cable configurations | Tension overlap | Physical clamp vs idealized constraints | Internal cable contact | Load/strain/torque comparisons | CONDITIONALLY_COMPARABLE; shared calibration data are not independent replication |
| S05 | MP1-R | Transformation baseline | TiNi; lot/state mismatch | Helical cable vs unresolved bundle | Tension vs bending | Different end constraints | Internal contact vs sleeve/pressure | DIC/IR plus force vs planned measurements | MECHANISTIC_ANALOGUE |
| S06 | S11 | Limit-stiffness model vs fitted hysteresis model | Steel vs mixed NiTi/steel | Rope architecture differs | Cyclic bending overlaps | Both address tension suppression, other fixture differences | Rope contacts | Bounds vs loops/dynamic response | CONDITIONALLY_COMPARABLE for bounds only; no damping pooling |
| S07 | V-W02 | Frictionless UMAT vs Souza + friction | Both SMA cable | Simplified vs explicit helix construction | Axial tension | Different end treatment | Frictionless vs frictional contact | Global stress/strain | MECHANISTIC_ANALOGUE; not controlled friction-ablation evidence |
| S12 | MP1-R | FE constitutive/contact | Numerical SMA, steel physical tests | Rope vs bundle | Axial/seismic vs bending | Fasteners vs sleeve | Rope contact | Numerical loops vs future measured M–κ | MECHANISTIC_ANALOGUE |
| S13 | MP1-R | Mechanistic interpretation vs model discrimination | TiNi but thermal/phase domains differ | Microbraid vs macro bundle | DMA/tension vs bending | Braid confinement vs applied pressure | Inter-filament contact | tanδ/storage modulus vs stiffness/slip | MECHANISTIC_ANALOGUE; DMA loss is not bending-loop energy |
| S01 | S03 | Independent/composite-beam vs pressure-state model | Paper/hemp/nylon vs nylon | Envelope vs rigid chain | Bending overlap | Vacuum envelope vs positive bladder/rigid wall | Fiber contacts plus boundaries | F–δ | CONDITIONALLY_COMPARABLE qualitatively after pressure-path distinction |
| S02 | S03 | Equivalent granular beam vs fiber-state model | Particles vs fibers | Annulus vs linked fiber cavity | Bending, different fixtures | Fabric sleeve vs rigid links | Particle vs fiber contacts | Different F–δ definitions | MECHANISTIC_ANALOGUE |
| S09 | MP1-R Bench B | Wet SMA/fluid dynamics vs proposed spring/piston | SMA wire vs spring | Lever/diaphragm vs axial piston | Thermal/fluid operation | Hot/cold-water supply vs unresolved circuit | Fluid/seal pathways differ | Temperature, pumping vs force/stroke/pressure | MECHANISTIC_ANALOGUE |
| S10 | MP1-R Bench B | ECF pump vs thermal SMA | Different actuator | Integrated ECF device vs piston | Pressure/stiffening | Vacuum stiffening vs positive pressure | Granular vs wire system | No-flow inferred pressure vs desired specimen measurement | BACKGROUND_ONLY (not comparable for SMA timing) |
| S18 | S03 | Continuum layer stress/slip vs fitted fiber-chain model | PVC sheets vs nylon fibers | Flat laminae vs cylindrical bundle | Cantilever vs three-point bending | Vacuum membrane vs positive-pressure bladder/rigid links | Layer–layer vs fiber–fiber | Load–deflection and modeled stress vs segmented global F–δ | MECHANISTIC_ANALOGUE; no direct precursor demonstrated |
| S18 | MP1-R | Existing Coulomb/continuum baseline vs proposed TiNi contact/material response | PVC vs TiNi | Layer beam vs wire bundle | Bending, different fixtures | Vacuum confinement vs proposed pressure reaction path | Layer–layer vs wire–wire/wire–sleeve | Global response; local mechanisms not independently measured | MECHANISTIC_ANALOGUE; no numerical parameter transfer |
| S22 | MP1-R | Interface-specific testing principle | Steel cable vs TiNi | Helical layers vs proposed bundle | Axial slip vs planned bending | Dissected cable table vs unresolved sleeve | Internal layer interfaces vs wire–tube | Axial resistance; inferred N vs measured sliding resistance | MECHANISTIC_ANALOGUE for identification methodology |

## B. THEME-BY-THEME SYNTHESIS

### Theme 1: Pressure-Controlled Variable Stiffness
- **Established knowledge:** Controlled confinement (positive pressure or vacuum) modulates structural bending stiffness (S01, S02, S03, S18).
- **Comparison across studies:** S02 and S03 use positive bladder pressure on particles and nylon fibers, respectively. S01 and S18 use vacuum jamming on nonmetallic elements and PVC layers.
- **Important contrasts:** Positive pressure in S03 models fiber-fiber contact inside rigid cavities, while vacuum in S18 models layer-layer normal stress.
- **Mechanistic connections:** Pressure alters normal forces at interfaces, delaying the onset of macroscopic slip and increasing apparent structural stiffness prior to full yield/slip.
- **Methodological critique:** Most studies infer local contact forces from global structural tests (F-δ curves) rather than measuring interface normal forces independently.
- **MP1-R relevance:** Transfers conceptually to MP1-R's outward pressure mechanism, but TiNi bundle packing and exact pressure-to-normal-force scaling remain unquantified.
- **Remaining uncertainty:** It is unresolved how outward fluid pressure uniquely maps to wire-wire vs. wire-sleeve normal forces in a flexible TiNi bundle.

### Theme 2: Friction, Contact and Stick-Slip in Multi-Element Structures
- **Established knowledge:** Friction provides a bounded contribution to bending stiffness and hysteresis (S03, S04, S06, S18, S22).
- **Comparison across studies:** S06 provides eigenstrain-based stiffness bounds for steel ropes. S03 and S18 provide continuum/fiber stick-slip regime transitions. S22 measures internal cable layer sliding resistance directly. S04 measures wire-rubber sliding force.
- **Important contrasts:** S06 explicitly avoids hysteresis prediction, focusing on limits. S22 directly isolates an interface, whereas S03 fits effective friction from global bending.
- **Mechanistic connections:** S06’s upper (perfect stick) and lower (full slip) bounds connect conceptually with S03’s and S18’s state transitions, framing structural response as an evolution through slip states.
- **Methodological critique:** Parameter fitting (E, μ) from the same structural response data (S03) limits predictive validation on unseen geometries.
- **MP1-R relevance:** Highlights that a conventional Coulomb stick-slip model (H0b) is a robust baseline that must be explicitly evaluated and falsified before claiming a new coupling law.
- **Remaining uncertainty:** Whether full hysteresis loops in TiNi bundles can be accurately predicted by these established contact mechanics without a novel material-contact coupling term.

### Theme 3: TiNi Material and Transformation Effects
- **Established knowledge:** Superelastic TiNi components exhibit transformation-dependent modulus, hysteresis, and temperature sensitivity (S05, S07, S11, S13).
- **Comparison across studies:** S05 uses DIC/IR to observe local transformation in tension. S07 models transformation-aware cables without friction. S11 and S13 test cyclic/dynamic responses of braided/mixed ropes.
- **Important contrasts:** S07 assumes frictionless contact to isolate material behavior, whereas S11 attributes unpartitioned losses to both friction and transformation.
- **Mechanistic connections:** The material state (phase) dictates the local compliance, which in turn influences the distribution of contact forces and slip (as suggested by H1-R).
- **Methodological critique:** No study cleanly partitions the bending dissipation into friction vs. transformation components through independent local measurements.
- **MP1-R relevance:** Proves that H0a-R (material-dominated response) is a viable hypothesis that requires single-wire control data to test.
- **Remaining uncertainty:** The exact ratio of transformation work to friction work during pressure-controlled bending of a TiNi bundle.

### Theme 4: SMA as Actuator vs TiNi as Structural Material
- **Established knowledge:** SMA components can actuate changes in structural interfaces (S04) and drive fluid systems (S09).
- **Comparison across studies:** S04 uses an SMA spring to squeeze a wire-rubber interface. S09 uses an SMA wire to drive a wet diaphragm pump.
- **Important contrasts:** S04’s SMA acts directly on the structural boundary (circumferential squeeze), whereas S09 uses SMA to generate fluid displacement remotely.
- **Mechanistic connections:** Thermal actuation drives a geometric change, which is converted (via contact in S04 or fluid in S09) into a reaction force.
- **Methodological critique:** Thermal response times (heating/cooling) are highly specific to the actuator geometry, environment, and fluid coupling; S04's 60s cooling time cannot be globally applied to MP1-R's piston.
- **MP1-R relevance:** MP1-R relies on an SMA-spring piston to generate fluid pressure. S04 confirms the viability of SMA-driven friction control, but MP1-R’s hydraulic decoupling requires separate dynamic validation.
- **Remaining uncertainty:** The actual pressure transients, thermal lag, and bandwidth of the proposed SMA-spring-driven piston against the specific MP1-R fluidic load.

### Theme 5: Interface Identifiability
- **Established knowledge:** Distinct internal interfaces can be experimentally isolated and measured (S04, S22).
- **Comparison across studies:** S22 dissects a steel cable to measure internal layer-to-layer axial sliding. S04 pulls a single structural wire through a rubber tube.
- **Important contrasts:** S22 investigates wire-wire (layer-layer) internal mechanics. S04 investigates wire-sleeve (wire-rubber) boundary mechanics.
- **Mechanistic connections:** Both approaches demonstrate that interface-specific controls are necessary when multiple contact paths exist.
- **Methodological critique:** Global bending tests (S03, S18) obscure which interface dominates the frictional loss.
- **MP1-R relevance:** MP1-R must disambiguate whether outward pressure increases wire-wire friction or wire-sleeve friction. Global bending alone cannot do this.
- **Remaining uncertainty:** Which interface actually dominates the frictional stiffening in the proposed MP1-R outward-pressure architecture.

### Theme 6: Experimental Decoupling (Bench A vs Bench B)
- **Established knowledge:** Fluidic dynamics (S09) and structural bending (S03, S06) operate on different time and state scales.
- **Comparison across studies:** Studies either focus on the structural mechanics under controlled confinement (S01, S02, S03, S18) or the actuator dynamics (S04, S09).
- **Important contrasts:** S04 mixes the actuator (SMA spring) and structure (wires) closely, making thermal cross-talk a risk. MP1-R separates them via a fluid line.
- **Mechanistic connections:** Separating the pressure source from the structural bundle allows independent steady-state stiffness measurements and transient actuator measurements.
- **Methodological critique:** Conflating actuator response time with structural stiffness limits the ability to model the underlying mechanics accurately.
- **MP1-R relevance:** Supports the Mentor's rescope to test the structure (Bench A) with an external pressure source, and the actuator (Bench B) separately, before integration.
- **Remaining uncertainty:** The integration losses, seal friction, and fluid compliance when Bench A and Bench B are connected.

## C. AGREEMENT / DISAGREEMENT MAP

### Agreement Map
| Proposition | Supporting Sources | Compatibility | Evidence Strength | Caveat |
|---|---|---|---|---|
| Confinement pressure alters bending stiffness via friction. | S01, S02, S03, S18 | High | STRONG | Uniform pressure distributions are typically assumed, not measured. |
| Frictional interfaces create slip-dependent bounds. | S03, S04, S06, S18 | High | STRONG | Specific values depend on the testing boundary and geometry. |
| Distinct internal interfaces can be experimentally isolated. | S04, S22 | High | MODERATE | Methods exist, but no joint partition experiment is reported in a TiNi bundle. |
| NiTi material phase influences structural compliance. | S05, S13 | High | STRONG | Often confounded with inter-wire friction in macroscopic tests. |
| SMA thermal actuation can modulate contact friction. | S04 | High | LIMITED | Demonstrated for wire-rubber only, not generalized. |

### Disagreement Map
| Issue | Source A | Source B | Difference | Type | Resolution |
|---|---|---|---|---|---|
| Hysteresis cycle prediction | S06 | S11 | S06 provides bounds and avoids cycle prediction; S11 fits phenomenological loops. | MEASUREMENT_DEFINITION_DIFFERENCE | Both valid; predictive constitutive loops remain an open challenge. |
| Interface dominance | S22 | S04 | S22 isolates internal wire-wire layers; S04 isolates wire-rubber boundary. | DIFFERENT_RESEARCH_QUESTION | Both methods are valid precedents; MP1-R must test both to find which dominates. |
| Pressure-to-friction mapping | S02 | S03 | S02 infers pressure-dependent equivalent E; S03 fits effective μ. | MODEL_ASSUMPTION_DIFFERENCE | Neither independently measures local N; both assume uniform transfer. |

## D. CAUSAL-CHAIN SYNTHESIS

| Causal Link | Supporting Sources | Evidence Type | Transferability to MP1-R | Status |
|---|---|---|---|---|
| fluid pressure → membrane/enclosure deformation | S02, S03 | Experiment | CONDITIONALLY_COMPARABLE | PARTIALLY_SUPPORTED |
| membrane/enclosure deformation → radial reaction | S02, S03 | Model | MECHANISTIC_ANALOGUE | MODEL_DEPENDENT |
| radial reaction → local contact normal force | S03 | Model | MECHANISTIC_ANALOGUE | NOT_ESTABLISHED |
| local contact normal force → friction capacity | S03, S04, S18, S22 | Exp/Model | CONDITIONALLY_COMPARABLE | ESTABLISHED |
| friction capacity → slip state | S03, S06, S18, S22 | Exp/Model | CONDITIONALLY_COMPARABLE | ESTABLISHED |
| slip state → bending stiffness | S01, S03, S04, S06, S18 | Exp/Model | DIRECTLY_COMPARABLE (conceptually) | ESTABLISHED |

**Critical weakest causal-chain link:** `radial reaction → local contact normal force`. It remains unresolved how outward fluid pressure uniquely maps to wire-wire versus wire-sleeve normal forces in a flexible TiNi bundle.

## E. H0a / H0b / H1 SYNTHESIS

| Hypothesis | Collective Supporting Evidence | Collective Counter-Evidence | Current Status | Critical Missing Observation |
|---|---|---|---|---|
| H0a-R (Material-dominated explanation) | S05, S13 | S03, S04 (show contact matters in other architectures) | PLAUSIBLE | Single-wire material calibration vs bundle response under matched conditions. |
| H0b-R (Conventional contact/friction explanation) | S03, S06, S12, V-W02 | None locked to MP1-R | PLAUSIBLE | High-fidelity local slip and independent interface resistance tests. |
| H1-R (Coupled response) | S11, S13 (interpretations) | None locked to MP1-R | NOT_YET_DISTINGUISHABLE | Orthogonal pressure/material-state contrasts showing residuals beyond H0b uncertainty. |

## F. EVIDENCE TRIANGULATION MATRIX

| Mechanism | Experiment | Analytical | Numerical | Review | Triangulation Strength |
|---|---|---|---|---|---|
| Pressure-controlled stiffening | STRONG (S01, S02, S03) | MODERATE (S03, S18) | NONE | LIMITED (S15) | MODERATE |
| Friction/stick-slip bending bounds | STRONG (S04, S06, S22) | STRONG (S06, S18) | MODERATE (S12) | NONE | STRONG |
| TiNi thermomechanics / transformation | STRONG (S05, S13) | MODERATE (S07) | MODERATE (S07, S12) | NONE | STRONG |
| Interface disambiguation | STRONG (S04, S22) | NONE | NONE | NONE | MODERATE |

## G. ESTABLISHED / SUPPORTED-CONNECTION / UNRESOLVED REGISTER

| Proposition | Class | Sources | Reason | Allowed Wording |
|---|---|---|---|---|
| Confinement pressure alters bending stiffness via friction. | ESTABLISHED | S01, S02, S03, S18 | Verified across multiple materials and boundary types. | "Multiple compatible studies demonstrate..." |
| Distinct internal interfaces can be experimentally isolated. | ESTABLISHED | S04, S22 | Verified via wire-rubber pull-out and cable-layer slip tests. | "Existing methodologies establish..." |
| NiTi material phase influences structural compliance. | ESTABLISHED | S05, S13 | Verified via DIC and DMA tests on cables/braids. | "Evidence from several studies indicates..." |
| SMA thermal actuation can modulate contact friction. | SUPPORTED CONNECTION | S04 | Verified for wire-rubber; theoretically extends to other boundaries. | "Available evidence suggests..." |
| Outward fluid pressure uniquely increases TiNi inter-wire friction. | UNRESOLVED | None | No source directly measures this specific geometric reaction path. | "It remains unresolved whether..." |
| A novel constitutive coupling law is required. | UNRESOLVED | None | H0b-R remains a live, unfalsified baseline. | "It remains unresolved whether..." |

## H. MP1-R TESTABLE QUESTION REGISTER

| Question | Type |
|---|---|
| Under externally controlled pressure, how does effective bending stiffness of the TiNi bundle vary? | CORE |
| Which interface (wire-wire or wire-sleeve) dominates the pressure-induced friction change? | CORE |
| Can the measured M-κ response be explained by a conventional contact/friction baseline (H0b-R) without an additional coupling law? | CORE |
| What is the thermal lag, actuation speed, and pressure limit of the SMA-spring-driven piston? | SUPPORTING |
| Does the actuator's heating cycle conductively alter the structural bundle's material phase? | OPTIONAL |

## I. OBSERVABLE / IDENTIFIABILITY REGISTER

| Required Observable | Category | Mechanism | Hypothesis | Identifiability Purpose |
|---|---|---|---|---|
| Fluid pressure at specimen | ESSENTIAL | Confinement | All | Normal force baseline. |
| Interface-specific slip resistance | ESSENTIAL | Friction/Contact | H0b-R | Disambiguate wire-wire vs wire-sleeve. |
| Bundle M-κ hysteresis loops | ESSENTIAL | Bending stiffness | All | Quantify macroscopic dissipation and tangent rigidity. |
| Single-wire material response | HIGH_VALUE | TiNi Phase | H0a-R | Establish material-only baseline to isolate friction. |
| Piston displacement/force | HIGH_VALUE | SMA Actuation | N/A | Characterize actuator efficiency and limits. |
| Bundle temperature | OPTIONAL | TiNi Phase | H0a-R, H1-R | Isolate actuator thermal cross-talk. |

## J. CHAPTER 2 SYNTHESIS BLUEPRINT

### 1. Pressure-Controlled Variable Stiffness
- **Scientific purpose:** Establish confinement-induced stiffening.
- **Primary claim:** Controlled pressure modulates apparent structural stiffness via friction.
- **Supporting sources:** S01, S02, S03, S18.
- **Comparison required:** Positive pressure in S02/S03 versus vacuum in S01/S18.
- **Contrast required:** Fiber contacts vs particle contacts vs layer contacts.
- **Critical limitation:** Previous studies rely on uniform pressure assumptions and lack direct TiNi bundle normal-force measurements.
- **Connection to next subsection:** Connects bulk pressure to the frictional stick-slip mechanisms that dictate structural stiffness.
- **Prohibited wording:** "First positive-pressure variable-stiffness structure."

### 2. Friction and Contact in Multi-Element Structures
- **Scientific purpose:** Define the stick-slip mechanistic baseline.
- **Primary claim:** Frictional interfaces create slip-dependent bounds and hysteresis in bending.
- **Supporting sources:** S04, S06, S22.
- **Comparison required:** Eigenstrain limits (S06) versus isolated sliding tests (S04, S22).
- **Contrast required:** Internal cable layers (S22) versus wire-sleeve boundary (S04).
- **Critical limitation:** Global M-κ tests obscure which interface dominates the loss.
- **Connection to next subsection:** Introduces the need to consider material properties alongside friction.
- **Prohibited wording:** "Conventional models are insufficient."

### 3. TiNi Thermomechanics and Bending
- **Scientific purpose:** Introduce the material-level complexity.
- **Primary claim:** NiTi components exhibit transformation-dependent properties that interact with structural kinematics.
- **Supporting sources:** S05, S07, S11, S13.
- **Comparison required:** Frictionless models (S07) versus lumped-parameter experiments (S11, S13).
- **Contrast required:** DIC local evidence (S05) versus global modulus changes (S13).
- **Critical limitation:** No study cleanly partitions transformation loss from friction loss in a pressure-controlled bending setup.
- **Connection to next subsection:** Distinguishes the structural TiNi wires from the separate SMA actuator.
- **Prohibited wording:** "NiTi transformation necessarily dominates hysteresis."

### 4. Experimental Decoupling and Interface Identifiability
- **Scientific purpose:** Justify the MP1-R experimental architecture (Bench A / Bench B).
- **Primary claim:** Separating the pressure source from the structure, and isolating specific interfaces, is necessary for valid mechanistic attribution.
- **Supporting sources:** S04, S09, S22.
- **Comparison required:** Thermal actuator lag (S04, S09) versus structural response.
- **Contrast required:** Integrated setups (S04) versus isolated tests (S22).
- **Critical limitation:** Interface isolation requires dedicated fixtures; SMA thermal dynamics cannot be assumed instantaneous.
- **Connection to next subsection:** Sets up the testable questions for Phase 5.
- **Prohibited wording:** "Interface disambiguation is a scientific knowledge gap."

## K. PROHIBITED CLAIM REGISTER

- First positive-pressure variable-stiffness structure.
- First SMA-friction mechanism.
- First NiTi wire-jamming system.
- Fluid pressure directly equals inter-wire normal force.
- Global bending proves inter-wire jamming.
- NiTi transformation necessarily dominates hysteresis.
- Conventional models (H0b) are insufficient or definitively falsified.
- A new constitutive coupling law is required.
- Interface disambiguation is a newly discovered scientific knowledge gap.
- No prior work combines relevant mechanisms.
