# MP1-R Phase 4C — Cross-Model Reconciliation and Phase 5 Handoff

**Date:** 2026-10-02  
**Run:** `PHASE_4C_RECONCILIATION`  
**Release status:** `BLOCKED_FOR_RECONCILIATION`

## Gate and provenance

The supplied A_GEMINI and B_GPT artifacts were read in the required five-file order. B_GPT includes an explicit blindness receipt: no other Phase 4 run, reconciliation artifact, Chapter 2 prose or broad search was accessed. A_GEMINI’s supplied synthesis and handoff contain no explicit blindness receipt. Because the protocol requires each run to independently report these checks, the canonical Phase 5 handoff is retained as a provisional merge and is not released as authority. No scientific claim is upgraded to compensate for this provenance defect.

The Phase 3 handoff remains the evidence authority. S19 and S21 remain quarantined, S20 remains retired and unused as scientific evidence, and corrected S18 is treated as a vacuum-confined PVC layer-jamming analogue. No original papers were reopened and no broad literature search was performed.

## Run-to-run reconciliation matrix

The matrix classifies semantic content before comparing counts. A six-theme versus five-theme layout is a granularity difference; A’s two unresolved questions expand into B’s nested uncertainty structure.

| Item | A_GEMINI | B_GPT | Classification | Canonical resolution |
|---|---|---|---|---|
| Themes | 6 themes | 5 themes | GRANULARITY_DIFFERENCE | Five themes T01–T05; actuator/material and interface/Bench distinctions retained as subsections. |
| Approved sources | 16 | 17 | COMPATIBLE_EXTENSION | Retain S17 only for metric-definition caution and RP021/S15 only for review context; no effect on mechanics conclusions. |
| Unresolved questions | 2 broad | 10 decomposed | GRANULARITY_DIFFERENCE | Five parent UQs with ten subquestions. |
| Pressure stiffening strength | STRONG | MODERATE synthesis / STRONG narrow P401/P402 | EVIDENCE_STRENGTH_DISAGREEMENT | Strong only for tested architecture-scoped existence; moderate for cross-study transfer. |
| Interface identifiability | Methods can isolate interfaces | Methods exist; dominance not identifiable from global bending | MATERIAL_DISAGREEMENT | Method existence established; MP1-R dominance remains NOT_ESTABLISHED and is a system-identification requirement. |
| Pressure→local N | NOT_ESTABLISHED at one link | NOT_ESTABLISHED L04 | EXACT_CONSENSUS | Critical weakest link retained. |
| H0a/H0b/H1 | PLAUSIBLE/PLAUSIBLE/NOT_YET_DISTINGUISHABLE | same | EXACT_CONSENSUS | Retained. |


## Canonical theme structure

### T01 — Confinement architectures, pressure paths and local-force mapping
Establish architecture-scoped pressure/confinement effects and keep pressure, reaction load and local contact force distinct.
**Sources:** S01, S02, S03, S15, S18, S22. **A mapping:** Pressure-Controlled Variable Stiffness. **B mapping:** T01 — Pressure paths, confinement and the missing local-force map.

### T02 — Slip-conditioned bending and interface identifiability
Define friction/stick-slip baselines and the independent observations needed to distinguish wire–wire from wire–sleeve contributions.
**Sources:** S03, S04, S06, S11, S18, S22, V-W02. **A mapping:** Friction, Contact and Stick-Slip in Multi-Element Structures; Interface Identifiability. **B mapping:** T02 — Slip-conditioned bending and interface identifiability.

### T03 — Structural TiNi thermomechanics and competing material/contact explanations
Separate direct transformation evidence, aggregate hysteresis and existing transformation-aware contact formulations; preserve H0a/H0b/H1 competition.
**Sources:** S05, S07, S11, S12, S13, V-W02. **A mapping:** TiNi Material and Transformation Effects. **B mapping:** T03 — Structural TiNi state, hysteresis and conventional transformation-aware models; T05 — Competing explanations and claim boundaries.

### T04 — SMA actuation, fluid generation and Bench A/Bench B decomposition
Distinguish SMA-as-actuator from TiNi-as-structure and bound what separate source and structure characterization can establish.
**Sources:** S03, S04, S09, S10. **A mapping:** SMA as Actuator vs TiNi as Structural Material; Experimental Decoupling (Bench A vs Bench B). **B mapping:** T04 — SMA actuation, fluid generation and experimental decomposition.

### T05 — Evidence-bounded model adequacy and unresolved attribution
Compare conventional model capabilities and state what remains undetermined without declaring a gap or contribution.
**Sources:** S03, S05, S06, S12, S18, V-W02. **A mapping:** Friction, Contact and Stick-Slip in Multi-Element Structures; TiNi Material and Transformation Effects. **B mapping:** T05 — Competing explanations and claim boundaries.

## Canonical proposition register

| ID | Canonical proposition | A equivalent | B equivalent | Phase 3 support | Final strength/status |
|---|---|---|---|---|---|
| RP001 | Confinement-based jamming changes bending response in the tested fiber and granular architectures. | Confinement pressure alters bending stiffness via friction. | P401: confinement-based jamming can change bending stiffness in tested fiber and granular structures. | S01, S02, S03 | STRONG / ESTABLISHED |
| RP002 | Positive-pressure jamming has been demonstrated in tested granular and nylon-fiber structures. | Confinement pressure alters bending stiffness via friction. | P402: positive-pressure jamming demonstrated in granular and nylon-fiber structures. | S02, S03 | STRONG / ESTABLISHED |
| RP003 | Pressure sensitivity can differ between bending/slip branches in the tested nylon-fiber chain. | Confinement pressure alters bending stiffness via friction. | P403: pressure sensitivity can depend on bending/slip branch. | S03 | MODERATE / ESTABLISHED |
| RP004 | SMA circumferential tightening changes wire–rubber sliding resistance and structural response in the tested robot. | SMA thermal actuation can modulate contact friction. | P404: SMA circumferential tightening changes wire–rubber sliding resistance and bending response. | S04 | MODERATE / ESTABLISHED |
| RP005 | Slip-state mechanics provide tested stiffness limits for short steel ropes. | Frictional interfaces create slip-dependent bounds. | P405: equivalent-beam mechanics predicts slip-state stiffness limits for tested short steel ropes. | S06 | MODERATE / ESTABLISHED |
| RP006 | NiTi cable/component tests show transformation-sensitive local response in their tension domain. | NiTi material phase influences structural compliance. | P406: NiTi cable/component tension measurements reveal transformation-sensitive local response. | S05 | MODERATE / ESTABLISHED |
| RP007 | Existing numerical formulations combine transformation-aware response with frictional cable contact. | NiTi material phase influences structural compliance. | P407: transformation-aware constitutive response and frictional contact can be combined numerically. | S12, V-W02 | MODERATE / ESTABLISHED |
| RP008 | A conventional continuum friction/slip model exists for vacuum-confined PVC layer beams. | Confinement pressure alters bending stiffness via friction. | P408: conventional continuum friction/slip modeling exists for vacuum-confined PVC layer beams. | S18 | MODERATE / ESTABLISHED |
| RP009 | Dedicated specimens can measure selected internal cable-layer or wire–tube sliding resistance. | Distinct internal interfaces can be experimentally isolated. | P409/P413: selected internal-layer and wire–tube resistance tests are methodological precedents. | S04, S22 | MODERATE / ESTABLISHED |
| RP010 | SMA-to-fluid displacement and coupled thermal/fluid/mechanical modeling have prior art. | SMA as actuator vs TiNi as structural material. | P410: SMA-to-fluid displacement and thermal/fluid/mechanical modeling have prior art. | S09 | MODERATE / ESTABLISHED |
| RP011 | Friction/slip constraints can bound or modulate bending response and provide a conventional baseline. | Frictional interfaces create slip-dependent bounds. | P411: slip-state bounds and continuum sliding models provide complementary conventional baselines. | S03, S04, S06, S18, S22, V-W02 | MODERATE / SUPPORTED_CONNECTION |
| RP012 | Transformation and contact losses can coexist; global hysteresis does not partition their contributions. | NiTi material phase influences structural compliance. | P412: transformation and contact losses can coexist; global hysteresis alone does not partition them. | S05, S11, S13 | LIMITED / SUPPORTED_CONNECTION |
| RP013 | Internal-layer and wire–sleeve resistance methods are distinct identification precedents. | Distinct internal interfaces can be experimentally isolated. | P413: internal cable-layer and wire–tube resistance tests are separate methodological precedents. | S04, S22 | ANALOGUE_ONLY / SUPPORTED_CONNECTION |
| RP014 | Independent pressure and actuator characterization supports attribution of structural versus source dynamics. | Experimental decoupling (Bench A vs Bench B). | P414: independent pressure and actuator characterization supports attribution. | S03, S04, S09, S10 | ANALOGUE_ONLY / SUPPORTED_CONNECTION |
| RP015 | Global force–deflection slopes, bending rigidity, DMA loss and loop work are not interchangeable stiffness/loss measures. | Friction, contact and stick-slip; metric caveat implicit. | P415: branch slopes, rigidity, DMA loss and loop work cannot be pooled. | S03, S06, S13, S17 | ANALOGUE_ONLY / SUPPORTED_CONNECTION |
| RP016 | Membrane, sleeve and reaction-path mechanics limit transfer of pressure/friction models between architectures. | Pressure-to-friction mapping differs by model assumption. | P416: membrane and reaction-path mechanics can limit transfer. | S02, S03, S18 | ANALOGUE_ONLY / SUPPORTED_CONNECTION |
| RP017 | The validated corpus does not establish that fluid pressure uniquely determines local wire contact forces or MP1-R bending stiffness. | Outward fluid pressure uniquely increases TiNi inter-wire friction (unresolved). | P417: fluid pressure uniquely determines local wire contact forces and bending stiffness (unresolved). | S02, S03, S18, S22 | NOT_ESTABLISHED / UNRESOLVED |
| RP018 | The validated corpus does not establish that global bending uniquely identifies wire–wire versus wire–sleeve dominance. | Which interface actually dominates remains unresolved. | P418: global bending uniquely identifies the dominant interface (unresolved). | S03, S04, S22 | NOT_ESTABLISHED / UNRESOLVED |
| RP019 | The adequacy of a locked conventional model, and any need for an additional coupling law, remains unestablished. | A novel constitutive coupling law is required (unresolved). | P419: conventional model adequacy or new-law necessity (unresolved). | S05, S06, S07, S12, S18, V-W02 | NOT_ESTABLISHED / UNRESOLVED |
| RP020 | It is unestablished whether the SMA spring/piston reproduces the externally imposed structural envelope under matched conditions. | Bench A/B integration losses remain uncertain. | P420: spring/piston reproduces external envelope under matched conditions (unresolved). | S03, S04, S09, S10 | NOT_ESTABLISHED / UNRESOLVED |
| RP021 | The laminar-jamming review provides scoped mechanism orientation but excludes fiber/particle coverage and is not primary mechanics replication. | Pressure-Controlled Variable Stiffness (review context). | S15 use in T01/BP01 as secondary orientation. | S15 | MODERATE / ESTABLISHED |


## Agreement register

| ID | Canonical consensus | A evidence | B evidence | Phase 3 check | Strength |
|---|---|---|---|---|---|
| AC01 | Confinement effects are architecture-scoped and alter structural bending response in tested systems. | A agreement map; S01/S02/S03/S18 | P401/P402 and T01 | C001-C004, C023-C024; pressure-path restrictions retained | STRONG |
| AC02 | Friction/slip mechanics provide bounds or branches relevant to bending, but do not by themselves identify local forces or a dominant interface. | A friction theme/agreement map | P405/P411, T02 | C008/C013/C023/C024 | MODERATE |
| AC03 | Interface-specific resistance methods exist in separate internal and wire–sleeve systems. | A interface-identifiability theme; S04/S22 | P409/P413 | G1 reframed as system-identification requirement | MODERATE |
| AC04 | NiTi state influences response in tested material domains, while transformation/friction loss partition in MP1-R is unresolved. | A TiNi theme; S05/S13 | P406/P412/T03 | C007/C010/C011/C012/C019 | MODERATE |
| AC05 | SMA actuation has prior friction-control and fluid-generation precedents, but the proposed source and structural TiNi roles remain distinct. | A S04/S09 comparison | P404/P410/T04 | C005/C015/C016/C018 | MODERATE |
| AC06 | No true cross-study contradiction is established after pressure-path, metric, material and interface restrictions are applied. | A disagreement map classifies differences as model/research-question differences | B counts true_cross_study_contradictions=0 | Comparability classifications prohibit pooling | MODERATE |
| AC07 | H0a-R and H0b-R remain plausible and H1-R is not yet distinguishable. | A H0/H1 table | B hypothesis_state | Phase 3 hypothesis matrix and remaining gaps | MODERATE |


## Material disagreement register

| ID | Issue | A position | B position | Resolution |
|---|---|---|---|---|
| MD01 | Strength of pressure-controlled stiffening as a cross-study proposition | STRONG | MODERATE for the synthesis theme (while P401/P402 narrow direct claims are STRONG) | Split the claim: RP001/RP002 STRONG within tested architectures; cross-study transfer and pressure-to-local-force inference are RP016/RP017 and ANALOGUE_ONLY/NOT_ESTABLISHED. |
| MD02 | Status of interface identifiability | Distinct interfaces can be isolated; MP1-R must test both | Methods exist, but dominance is not identifiable from global bending and G1 is a system-identification requirement | Retain RP009 as ESTABLISHED method existence; RP018 remains NOT_ESTABLISHED; do not call it a literature knowledge gap. |
| MD03 | Status of causal links between pressure and local contact | Pressure→normal force NOT_ESTABLISHED; later friction/slip links ESTABLISHED | N→friction and friction→slip are model-dependent/partially supported for MP1-R | Use conservative chain statuses: local N map NOT_ESTABLISHED; downstream capacity and slip are MODEL_DEPENDENT; slip→bending PARTIALLY_SUPPORTED. |
| MD04 | TiNi evidence strength | NiTi phase influence STRONG | Cross-study TiNi theme ANALOGUE_ONLY; P406 is MODERATE in transfer and P412 LIMITED | RP006 MODERATE for tested material finding; RP012 LIMITED for coexistence; no claim that transformation dominates MP1-R hysteresis. |
| MD05 | Theme granularity | Six themes, separating actuator/material and interface/Bench A-B | Five themes, combines pressure/local-force and slip/interface and adds competing explanations | Adopt five minimum themes T01-T05; retain actuator/structural distinction inside T03/T04 and model competition in T05. |
| MD06 | Source count | 16 approved sources used | 17 approved sources used, adding S17 | S17 is a compatible extension for metric-definition caution (RP015), not a new mechanics replication. Canonical source use is 17 IDs including S17; count difference does not alter core conclusions. |


## Omission / extension register

| ID | Content | Present / absent | Decision | Reason |
|---|---|---|---|---|
| OE01 | Branch-specific pressure sensitivity and explicit pressure-path/local-N distinction from B | B_GPT / A_GEMINI | RETAIN | Prevents endpoint stiffening from being generalized to every branch and sharpens RP003/RP017. |
| OE02 | Metric discipline separating F–δ slope, M–κ rigidity, DMA loss and loop work from S17 | B_GPT / A_GEMINI | RETAIN | Scientifically material for cross-study comparison and observable definitions. |
| OE03 | Explicit conventional transformation/contact formulations and adequacy criterion | B_GPT / A_GEMINI | RETAIN | Needed to preserve H0b as a live baseline and avoid premature new-law claims. |
| OE04 | A’s explicit separation of SMA actuator versus structural TiNi and thermal cross-talk | A_GEMINI / B_GPT | RETAIN | Compatible extension that clarifies T03/T04 and Bench B confounding. |
| OE05 | A’s phrase that distinct internal interfaces can be experimentally isolated | A_GEMINI / B_GPT wording | RETAIN_NARROWED | Retain as method existence RP009; narrow away from any claim of MP1-R dominance or literature gap. |


## Reconciled causal chain

| Link | A | B | Canonical | Evidence | Reason |
|---|---|---|---|---|---|
| fluid pressure → membrane/enclosure response | PARTIALLY_SUPPORTED | MODEL_DEPENDENT | MODEL_DEPENDENT | S02, S03, S18 | Confinement response is demonstrated/modelled in other architectures, but MP1-R material, compliance, fluid and pressure reference differ. |
| membrane/enclosure response → radial reaction | MODEL_DEPENDENT | INFERRED | INFERRED | S02, S03, S04 | Reaction follows an architecture-specific boundary model; outward MP1-R force path is not measured. |
| radial reaction → local wire–wire / wire–sleeve contact normal forces | NOT_ESTABLISHED | NOT_ESTABLISHED | NOT_ESTABLISHED | S03, S18, S22 | Uniform confinement or F/μ inversion is not independent local-N calibration; contact distribution and interface sign remain unknown. |
| local contact normal force → friction capacity | ESTABLISHED | MODEL_DEPENDENT | MODEL_DEPENDENT | S03, S04, S18, S22 | Coulomb relation and resistance observations provide a conventional route, but μ, N, area, parasitics and history are not jointly identified in MP1-R. |
| friction capacity → slip regime | ESTABLISHED | MODEL_DEPENDENT | MODEL_DEPENDENT | S03, S06, S18, S22 | Branches, prescribed limits and sliding regions are model/measurement-specific; they are not local slip fields for MP1-R. |
| slip regime → bending stiffness | ESTABLISHED | PARTIALLY_SUPPORTED | PARTIALLY_SUPPORTED | S01, S03, S04, S06, S18 | Global response effects are observed in related systems, but material, sleeve, end and boundary contributions remain confounded for MP1-R. |
| source operation → specimen pressure (Bench B) | MODELLED/UNRESOLVED | PARTIALLY_SUPPORTED; MP1-R not established | PARTIALLY_SUPPORTED | S09, S10, S03 | Actuator/source precedents exist, but connected-load pressure-volume and two-location transients are not validated for the proposed spring/piston. |


**Critical weakest causal-chain link:** `radial reaction → local wire–wire / wire–sleeve contact normal forces`.

## H0a-R / H0b-R / H1-R state

| Hypothesis | A | B | Canonical | Supporting evidence | Missing observation |
|---|---|---|---|---|---|
| H0a-R | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | S05, S13 | Same-lot state/rate/history-matched material baseline plus pressure contrasts with sleeve/end effects bounded. |
| H0b-R | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | S03, S06, S12, S18, V-W02 | Locked, calibrated conventional baseline tested on reserved pressure–curvature paths with independent contact/slip constraints. |
| H1-R | NOT_YET_DISTINGUISHABLE | NOT_YET_DISTINGUISHABLE | NOT_YET_DISTINGUISHABLE | S11, S13 | Orthogonal pressure/material-state contrasts with local slip/strain and temperature, compared with defined H0a/H0b predictions. |


## Hierarchical unresolved-question register

### UQ01 — What is the pressure-to-reaction-to-contact-force map in the proposed cross-section?
**Evidence:** S02, S03, S18, S22. **Material for Phase 5:** True.

| Sub-question | A mapping | B mapping | Material for Phase 5? |
|---|---|---|---|
| UQ01a: Which reaction surfaces and candidate wire–wire/wire–sleeve paths exist after geometry is fixed? | A remaining uncertainty on wire–wire versus wire–sleeve scaling | U01 | NO — scope/identifiability prerequisite |
| UQ01b: How does near-specimen pressure map to local N or defensible transmission bounds? | A unresolved outward pressure→inter-wire friction | U02 | YES |
| UQ01c: How much do sleeve compliance, packing, end and reaction motion contribute to apparent stiffness? | A pressure-transfer caveat | U03 | YES |


### UQ02 — Can interface contributions and local slip be identified from augmented observations?
**Evidence:** S03, S04, S06, S18, S22. **Material for Phase 5:** True.

| Sub-question | A mapping | B mapping | Material for Phase 5? |
|---|---|---|---|
| UQ02a: Which interface dominates pressure-conditioned resistance under independent interface constraints? | A interface-dominance uncertainty | UQ05 | YES |
| UQ02b: Do global branches correspond to local slip onset/progression rather than sleeve or end motion? | A stick-slip mechanism uncertainty | UQ05/UQ07 | YES |


### UQ03 — How should TiNi state and aggregate hysteresis be interpreted?
**Evidence:** S05, S11, S13, V-W02. **Material for Phase 5:** True.

| Sub-question | A mapping | B mapping | Material for Phase 5? |
|---|---|---|---|
| UQ03a: Does structural TiNi transformation occur in the accessible bending domain? | A material calibration requirement | UQ04 | YES |
| UQ03b: Can transformation, friction and sleeve losses be partitioned beyond aggregate loop work? | A transformation/friction ratio uncertainty | UQ06 | YES |


### UQ04 — What model capability and coupling claim are justified?
**Evidence:** S03, S05, S06, S12, S18, V-W02. **Material for Phase 5:** True.

| Sub-question | A mapping | B mapping | Material for Phase 5? |
|---|---|---|---|
| UQ04a: Can an appropriate locked conventional model predict reserved pressure–curvature paths and available local observables? | A H0b missing observation | UQ07 | YES |
| UQ04b: After alternatives are bounded, is an additional state-conditioned pressure/contact/material term identifiable and predictively necessary? | A H1 not distinguishable | UQ08 | YES |


### UQ05 — Can Bench B reproduce the controlled-pressure structural envelope when integrated?
**Evidence:** S03, S04, S09, S10. **Material for Phase 5:** True.

| Sub-question | A mapping | B mapping | Material for Phase 5? |
|---|---|---|---|
| UQ05a: Can the SMA spring/piston reach and recover the connected-load pressure–volume envelope? | A actuator lag/pressure limit uncertainty | UQ09 | YES |
| UQ05b: At matched pressure, temperature, loading and history, does integrated response agree with externally pressurized response? | A Bench A/B integration uncertainty | UQ10 | YES |


## Testable question register

| ID | Question | Class | Maps to | Evidence |
|---|---|---|---|---|
| RQ01 | At controlled material, geometry and history, how does imposed specimen pressure change TiNi-bundle bending branches and repeatability? | CORE | RP001, RP003 | S02, S03, S04 |
| RQ02 | Which candidate interface resistance changes with pressure when independent interface constraints are introduced? | CORE | RP009, RP018 | S04, S22, S03 |
| RQ03 | Can a calibrated conventional contact/friction and transformation-aware baseline predict reserved pressure–curvature response without an additional coupling law? | CORE | RP011, RP019 | S03, S06, S12, S18, V-W02 |
| RQ04 | Does the SMA spring/piston reach and recover the connected specimen pressure–volume envelope? | SUPPORTING | RP010, RP020 | S04, S09, S10 |
| RQ05 | At matched specimen pressure, temperature, loading and history, do integrated and external-source bending responses agree? | SUPPORTING | RP014, RP020 | S03, S04, S09, S10 |
| RQ06 | Does same-lot TiNi exhibit transformation in the strain/temperature domain actually accessed? | SUPPORTING | RP006, RP012 | S05, S13 |
| RQ07 | Are global transition proxies associated with local slip onset rather than sleeve or end motion? | SUPPORTING | RP003, RP005, RP016 | S03, S06, S18, S22 |
| RQ08 | After conventional predictions and confounders are bounded, is an additional material/contact term identifiable and predictively necessary? | OPTIONAL | RP012, RP019 | S05, S11, S12, S13, V-W02 |
| RQ09 | Can transformation and interface contributions be partitioned beyond aggregate bending work? | OPTIONAL | RP012 | S05, S11, S13 |


## Observable / identifiability register

| ID | Observable | Priority | Mechanism | Hypotheses | Purpose |
|---|---|---|---|---|---|
| OBS01 | Near-specimen pressure p(t), reference location and synchronization | ESSENTIAL | Boundary input / pressure path | H0a-R, H0b-R, H1-R | Distinguish specimen intervention from source command and align matched histories. |
| OBS02 | Source pressure p_source(t) alongside specimen pressure | ESSENTIAL | Bench B source-to-specimen dynamics | H0b-R, H1-R | Separate source waveform, storage, transport and leakage from structural response. |
| OBS03 | Bending force and calibrated moment with deflection/rotation/curvature | ESSENTIAL | Global bending response | H0a-R, H0b-R, H1-R | Define M–κ or declared stiffness metric and detect fixture contributions. |
| OBS04 | Actuator and structural-wire temperatures, time-aligned | ESSENTIAL | Thermal actuation versus material state | H0a-R, H1-R | Prevent heat leakage or phase change being misread as pressure/contact effect. |
| OBS05 | Loading/unloading paths, repeatability, drift, cycle order and rate | ESSENTIAL | Hysteresis and history | H0a-R, H0b-R, H1-R | Separate state dependence and drift; compute defined loop work. |
| OBS06 | Confirmed packing, sleeve deformation and reaction geometry | HIGH_VALUE | Pressure transmission and alternative load paths | H0b-R, H1-R | Bound sleeve expansion, packing rearrangement and end effects. |
| OBS07 | Interface-specific sliding resistance with fixture/parasitic bounds | HIGH_VALUE | Wire–wire and wire–sleeve friction | H0b-R, H1-R | Add independent constraints for dominance claims; do not equate resistance with μ or N separately. |
| OBS08 | Representative local relative slip and structural-wire strain | HIGH_VALUE | Slip versus material deformation | H0a-R, H0b-R, H1-R | Validate branch labels and distinguish local slip from global hysteresis. |
| OBS09 | Independent local-normal-force proxy or calibrated pressure-to-contact bounds | HIGH_VALUE | N mapping and Coulomb capacity | H0b-R, H1-R | Avoid fitting μ and N from the same resistance; constrain RP017. |
| OBS10 | Same-lot constitutive response in matched strain/temperature/rate/history domain | HIGH_VALUE | Structural TiNi material baseline | H0a-R, H0b-R, H1-R | Test material-dominated explanation without importing unrelated lot parameters. |
| OBS11 | Piston stroke/return, force and pressure rise/recovery under known connected load/compliance | ESSENTIAL | Bench B pressure–volume envelope | H0b-R, H1-R | Characterize source reach/recovery and distinguish dead-head from connected loading. |
| OBS12 | Electrical input and spring force/bias/seal-load evidence | HIGH_VALUE | Actuator force/energy balance | H0b-R, H1-R | Constrain source work and separate SMA, bias, seal and inertia terms. |
| OBS13 | Direct phase-sensitive or expanded local-field measurements | OPTIONAL | Transformation/loss partition | H0a-R, H1-R | Strengthen phase attribution if simpler calibration cannot distinguish alternatives. |


## Established / supported connection / unresolved map

### Established

| ID | Proposition | Sources | Strength | Boundary |
|---|---|---|---|---|
| E01 | Confinement changes bending response in tested fiber/granular architectures. | S01, S02, S03 | STRONG | Architecture-scoped; not a universal pressure law. |
| E02 | Positive-pressure jamming exists in tested granular and nylon-fiber systems. | S02, S03 | STRONG | No TiNi or MP1-R transfer asserted. |
| E03 | Slip-state limits, frictional resistance and pressure-conditioned branches are established in related systems. | S03, S04, S06, S18, S22 | MODERATE | Different interfaces/metrics; no local MP1-R attribution. |
| E04 | NiTi transformation-sensitive response is directly observed in tested material domains. | S05, S13 | MODERATE | Active transformation and dominance in MP1-R bending are not established. |
| E05 | SMA friction-control and SMA-to-fluid precedents exist at their stated architectures. | S04, S09 | MODERATE | Proposed spring/piston and structural TiNi integration remain unvalidated. |

### Supported connection

| ID | Connection | Sources | Strength |
|---|---|---|---|
| C01 | Pressure-conditioned bending should be interpreted through architecture-specific reaction paths, not universal p→stiffness transfer. | S02, S03, S18 | ANALOGUE_ONLY |
| C02 | Interface-specific tests can provide independent constraints for global bending attribution. | S04, S22 | ANALOGUE_ONLY |
| C03 | Material state can alter wire response and thereby contact loading through ordinary coupled mechanics. | S05, S11, S13, V-W02 | LIMITED |
| C04 | Separate Bench A structural and Bench B source characterization supports causal attribution when observations are synchronized. | S03, S04, S09, S10 | ANALOGUE_ONLY |
| C05 | Existing conventional contact/slip and transformation-aware formulations are viable baselines to test before any new law is proposed. | S06, S12, S18, V-W02 | ANALOGUE_ONLY |

### Unresolved

| ID | Proposition | Sources | Status |
|---|---|---|---|
| U01 | Pressure-to-local-contact map in proposed geometry. | S02, S03, S18, S22 | NOT_ESTABLISHED |
| U02 | Dominant interface and local slip progression cannot be inferred from global bending alone. | S03, S04, S22 | NOT_ESTABLISHED |
| U03 | Accessible TiNi transformation domain and quantitative friction/material loss partition. | S05, S11, S13 | NOT_ESTABLISHED |
| U04 | Adequacy of a locked conventional model versus need for an added coupling term. | S03, S05, S06, S12, S18, V-W02 | NOT_ESTABLISHED |
| U05 | Spring/piston source envelope and matched integrated/external structural response. | S03, S04, S09, S10 | NOT_ESTABLISHED |


## Canonical Chapter 2 synthesis blueprint

| ID | Subsection | Purpose | Claim boundary | Sources | Comparison / contrast | Critique / transition | Prohibited wording |
|---|---|---|---|---|---|---|---|
| BP01 | Confinement architectures and pressure-conditioned bending | Establish prior art for architecture-scoped tunability. | Multiple systems show pressure/confinement-dependent response; do not claim universal p–stiffness behavior or MP1-R transfer. | S01, S02, S03, S15, S18 | Positive pressure in granular/fiber systems versus vacuum fiber/layer systems.; Contact topology, pressure path, metric and boundary. | Global response and model assumptions do not measure local contact force. Move from endpoint tunability to the missing pressure/contact intermediate map. | First positive-pressure variable-stiffness or fiber-jamming principle; every branch stiffens. |
| BP02 | Pressure transmission, local contact and measurable resistance | Keep distributed pressure, reaction load, local N and friction capacity distinct. | Applied pressure is a boundary input; local N requires geometry/equilibrium/calibration. | S02, S03, S04, S18, S22 | S03 effective confinement, S18 μp continuum, S04 wire–rubber resistance, S22 internal-layer resistance.; Measured resistance versus inferred N; inward versus outward reaction. | Do not fit μ and N from the same resistance or call p=N. Set up interface attribution and slip-state limits. | Pressure directly equals contact force; pull-out uniquely identifies μ and N. |
| BP03 | Stick/slip limits, hysteresis and interface attribution | Define conventional bounds and what global loops cannot identify. | Friction/slip can bound or modulate bending; interface dominance requires independent constraints. | S03, S04, S06, S11, S18, S22 | Bounds, continuum regions, pull-out and cyclic loops.; Internal cable layers versus wire–sleeve; bounds versus loop prediction. | S06 does not predict full loops; loop area does not partition losses. Introduce structural TiNi state as a competing explanation. | Global bending proves inter-wire dominance; interface gap established. |
| BP04 | TiNi thermomechanics and conventional material/contact alternatives | Separate local transformation evidence from aggregate hysteresis and numerical precedent. | NiTi state influences tested response; transformation dominance or new-law necessity is unestablished. | S05, S07, S11, S12, S13, V-W02 | Local DIC/IR, DMA/tension, mixed-rope loops, frictionless and frictional formulations.; Direct material state versus author-attributed aggregate loss. | Do not pool tension, DMA and bending-loop measures. Distinguish structural TiNi from SMA source dynamics. | NiTi implies active transformation; transformation dominates hysteresis; conventional models are disproved. |
| BP05 | SMA actuation, fluid sources and Bench A/Bench B decomposition | Bound source precedents and justify synchronized decomposition for attribution. | SMA friction and SMA fluid precedents exist; proposed source performance and integration are unestablished. | S03, S04, S09, S10 | Integrated SMA-friction versus SMA-fluid source and external-pressure structural tests.; Actuator thermal clock versus structural pressure/material clock. | S04 timing is specimen-specific; two rigs are not intrinsically novel or mandatory. Prepare competing hypotheses and bounded questions for Phase 5. | First SMA-friction mechanism; universal cooling time; unmatched integration proves coupling. |
| BP06 | Evidence-bounded competing explanations and unresolved questions | Keep H0a/H0b/H1 live and define the boundary for later gap adjudication. | H0a/H0b plausible; H1 not yet distinguishable; unresolved is not a gap or novelty claim. | S03, S05, S06, S09, S12, S18, S22, V-W02 | Material-only, conventional contact and added-coupling explanations.; Observed precedent versus MP1-R-specific missing observations. | Require calibrated baselines, reserved paths and identifiability controls. Hand bounded decisions to Phase 5. | H1 proven/best/winner; new constitutive law required; no relevant prior work. |


## Prohibited claim register

- First positive-pressure variable-stiffness structure or first positive-pressure fiber-jamming principle/model.
- First SMA/friction mechanism or first SMA-controlled friction modulation of wire-based structures.
- First NiTi wire-jamming system or first wire/fiber jamming system.
- Fluid pressure directly equals every inter-wire or wire–sleeve normal force.
- Global bending proves wire–wire jamming or identifies interface dominance.
- NiTi transformation necessarily dominates MP1-R hysteresis.
- NiTi identity alone proves active transformation in the accessible bending domain.
- Conventional models are insufficient, definitively falsified, or rejected because one simplification fails.
- A new constitutive pressure–contact–material coupling law is required.
- Interface disambiguation is already a demonstrated literature-wide scientific knowledge gap.
- No relevant prior work combines any of the MP1-R mechanisms.
- S18 proves positive-pressure fiber jamming or is a direct S03 precursor.
- S19, S20 or S21 supplies scientific mechanics evidence; S20's retired identity may not be restored.
- SMA spring-to-fluid displacement is novel solely because the drive or geometry differs.
- Universal SMA cooling/response time inferred from S04.
- Integrated response differences at unmatched pressure, temperature or history prove H1.
- Different geometry, material, pressure levels, more FEA/measurements or held-out testing alone establish novelty.
- A global loop, DMA loss tangent or F–δ slope directly equals M–κ bending work or local friction loss.
- A source pressure gauge alone establishes specimen pressure or contact force.

## Phase 5 adjudication questions

| ID | Unresolved proposition | Supporting evidence | Limiting evidence | Why it matters | Phase 5 decision |
|---|---|---|---|---|---|
| P5Q01 | Whether the proposed pressure/reaction geometry can be bounded sufficiently to interpret local contact claims. | RP016, RP017, UQ01 | S03/S18 model assumptions; S22 inferred N; no MP1-R local calibration | Determines whether contribution language can be mechanistic or must remain an empirical structural characterization. | Set the defensible pressure-to-contact claim boundary. |
| P5Q02 | Whether wire–wire versus wire–sleeve dominance is identifiable with independent constraints. | RP009, RP013, UQ02 | Global bending is confounded; separate methods are not a joint MP1-R partition | Controls whether an interface-specific contribution can be claimed. | Classify the strongest defensible interface attribution and evidence requirement. |
| P5Q03 | Whether TiNi transformation is active and separable from friction/sleeve losses in the accessible domain. | RP006, RP012, UQ03 | Tension/DMA/rope evidence is nonidentical to pressured bending; no partition | Sets the boundary for material-mechanism claims. | Decide whether material-state characterization is central, supporting or outside contribution scope. |
| P5Q04 | Whether a calibrated conventional model is an adequate comparator before any added law is considered. | RP005, RP007, RP008, RP011, RP019, UQ04 | No locked MP1-R baseline or reserved-path validation | Prevents an engineering fit or model omission from being framed as novelty. | Specify the minimum adequacy test and whether added coupling remains a live optional claim. |
| P5Q05 | Whether Bench B reproduces the externally controlled structural envelope under matched conditions. | RP010, RP014, RP020, UQ05 | S09/S10/S04 use different actuator/load paths; no integrated MP1-R data | Sets the contribution boundary for actuator integration versus structural mechanics. | Decide whether integration is a validation/control objective or a defensible scientific contribution. |


## Source usage reconciliation

A reports 16 sources; B reports 17. The difference is S17, used by B for metric-definition caution and not for an independent mechanics result; S15 remains contextual review evidence only. It is retained as a compatible extension with analogue-only strength. S19/S21 remain quarantined and S20 remains retired; none has a scientific support role.

## Validation receipt

| Check | Result |
|---|---|
| Primary files read | 5 / 5 |
| A blindness receipt | MISSING — blocking |
| B blindness receipt | PASS |
| Phase 3 authority | PASS; hash matches |
| Source IDs resolve | PASS |
| S20 scientific support | NONE |
| S19/S21 restrictions | PRESERVED |
| S18 identity | CORRECTED identity retained |
| Every proposition has sources | PASS |
| Every UQ maps to evidence | PASS |
| Original papers reopened | 0 |
| Broad literature searches | 0 |
| Phase 5 authority released | NO — blocked |


## Provenance paths

- A_GEMINI synthesis: `docs/literature/MP1_R_PHASE_4_CROSS_STUDY_SYNTHESIS_A_GEMINI_2026-10-02.md` (sha256 `d05459d657f90365f8465e9b3fa893cca1f72c8afa3cd1bb2aaf86558245f0d3`); handoff: `outputs/plans/MP1_R_PHASE_4_PHASE_5_HANDOFF_A_GEMINI_2026-10-02.json` (sha256 `ab5e1a362cc64d1d089ceb9bce59a985d25b548ebb4a3e247072b1fca839cb22`).
- B_GPT synthesis: `docs/literature/MP1_R_PHASE_4_CROSS_STUDY_SYNTHESIS_B_GPT_2026-10-02.md` (sha256 `4a5793ef4e7df3d62b898d729cc1be7e1d60d738926b0faeabd985a65b75949d`); handoff: `outputs/plans/MP1_R_PHASE_4_PHASE_5_HANDOFF_B_GPT_2026-10-02.json` (sha256 `dcf11b693b0f4080fdfc07d949f2085b34b925aa3cf0fd75e90fbc30095e3194`).
- Phase 3 authority: `outputs/plans/MP1_R_PHASE_3_PHASE_4_HANDOFF_2026-10-02.json` (sha256 `d47c33316e92397f0c4a0ba0512562fb8e06665f41bfe0b56471d415a81a854b`); appraisal: `docs/literature/MP1_R_PHASE_3_METHODOLOGICAL_APPRAISAL_AND_EVIDENCE_INTEGRITY_2026-10-02.md` (sha256 `98cb37bc018a42fd5682964606a3ba0d66f43176c8d132778abcea2b5d3f1d2b`).

The reconciliation stops here. It does not declare a research gap, novelty, contribution, H1, final thesis question or Chapter 2 prose.
