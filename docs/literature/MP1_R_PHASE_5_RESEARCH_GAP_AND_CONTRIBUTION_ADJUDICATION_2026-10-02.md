# MP1-R Phase 5 — Research Gap and Contribution-Boundary Adjudication

**Date:** 2026-10-02  
**Workstream:** MP1-R — Rescope  
**Status:** `READY_FOR_PHASE_6_CHAPTER_2_DRAFTING`  
**Phase 4 authority:** `READY_FOR_PHASE_5_GAP_ADJUDICATION`

## Decision

The validated Phase 4 synthesis does not justify a G1 scientific knowledge-gap claim. The narrowest defensible MSc boundary is a quantitative, configuration-bounded characterization of pressure-conditioned bending in a defined TiNi wire bundle, paired with a locked conventional-model discrimination test. Interface attribution, material-state attribution and SMA/piston integration remain bounded system-identification or validation activities. An additional pressure–contact–material law is conditional only and is not required for thesis success.

The Phase 4 state is preserved: H0a-R = `PLAUSIBLE`, H0b-R = `PLAUSIBLE`, H1-R = `NOT_YET_DISTINGUISHABLE`; the critical weakest link remains `radial reaction → local wire–wire / wire–sleeve contact normal forces`.

## Inputs and decision boundary

The three required primary inputs were read in the prescribed order:

1. `outputs/plans/MP1_R_PHASE_4_RECONCILED_PHASE_5_HANDOFF_2026-10-02.json`
2. `docs/literature/MP1_R_PHASE_4_RECONCILED_SYNTHESIS_2026-10-02.md`
3. `docs/project/MP1_MENTOR_FEEDBACK_RESCOPE_2026-09-29_VI.md`

No broad literature search was performed, no original paper was reopened, and no Phase 4 artifact was modified. The mentor note was used only for active MP1-R scope and intended architecture; it was not treated as scientific evidence.

## A. Gap adjudication matrix

### UQ01 — What is the pressure-to-reaction-to-contact-force map in the proposed cross-section?

**Parent disposition:** Mixed: UQ01a is a project prerequisite; UQ01b/UQ01c are system-identification requirements.

| Sub-question | Primary classification | Why this classification | Can MP1-R answer it? | Minimum observations | Allowed wording |
|---|---|---|---|---|---|
| UQ01a: Which reaction surfaces and candidate wire–wire/wire–sleeve paths exist after geometry is fixed? | `G8_NOT_A_GAP` | The cross-section, reaction surfaces and interface candidates must be specified before a scientific claim can be posed. Their current absence is a scope/design condition, not evidence of a literature knowledge deficit. | Yes, by fixing and documenting the geometry; the result defines the system rather than closing a general scientific gap. | mentor-confirmed cross-section and force-direction sketch<br>packing, sleeve and reaction geometry<br>candidate interface map<br>boundary and seal locations | The study defines and controls the candidate reaction paths before interpreting pressure-conditioned response. |
| UQ01b: How does near-specimen pressure map to local N or defensible transmission bounds? | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | Pressure, reaction load and local normal force are distinct. Existing models provide routes or assumptions, but the MP1-R path and local distribution are not identified without independent constraints. | Yes, as a bounded system-identification result using synchronized pressure, geometry, resistance and a local-N proxy or calibrated bounds. It need not recover a unique field everywhere. | near-specimen and source pressure<br>confirmed reaction geometry<br>interface resistance with parasitic bounds<br>local-normal-force proxy or calibrated transmission bounds<br>bending force/moment and curvature | The study identifies or bounds the pressure-to-contact transmission for the defined configuration. |
| UQ01c: How much do sleeve compliance, packing, end and reaction motion contribute to apparent stiffness? | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | These alternative load paths can change the measured bending response and must be separated from pressure-conditioned contact. Their contribution is system-specific and not a demonstrated general literature gap. | Yes, by measuring geometry/deformation and bounding end, sleeve and packing effects in the tested regime. | sleeve/reaction deformation<br>packing and boundary geometry<br>end/reaction motion or a bound on it<br>pressure and M–κ/force–deflection histories<br>repeatability and drift | The experiment bounds the contribution of sleeve, packing and boundary motion in the tested configuration. |

### UQ02 — Can interface contributions and local slip be identified from augmented observations?

**Parent disposition:** G4 system-identification requirements; Phase 3 explicitly prevents upgrading interface disambiguation into a literature gap.

| Sub-question | Primary classification | Why this classification | Can MP1-R answer it? | Minimum observations | Allowed wording |
|---|---|---|---|---|---|
| UQ02a: Which interface dominates pressure-conditioned resistance under independent interface constraints? | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | Wire–wire and wire–sleeve resistance can both contribute. Existing dedicated tests are precedents, but global bending alone is confounded. | Yes, if independent interface constraints and resistance measurements are feasible; otherwise it must report bounded non-identifiability. | separate wire–wire and wire–sleeve resistance tests or constraints<br>near-specimen pressure<br>local slip/strain or equivalent interface proxy<br>global bending response and parasitic bounds | The study identifies the pressure-conditioned interface contribution within the tested geometry, or reports that dominance remains bounded but unresolved. |
| UQ02b: Do global branches correspond to local slip onset/progression rather than sleeve or end motion? | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | Branch changes and hysteresis can arise from local slip, sleeve compliance, end motion or material state. The question concerns pathway attribution in the actual system. | Yes, with synchronized local relative-slip/strain observations and sleeve/end controls; otherwise retain branch labels as phenomenological. | local relative slip or structural-wire strain<br>sleeve/end motion bound<br>pressure and M–κ paths<br>cycle order, rate and repeatability | Observed global branches are associated with local slip only when independent local and boundary evidence supports that attribution. |

### UQ03 — How should TiNi state and aggregate hysteresis be interpreted?

**Parent disposition:** G2 material-domain characterization plus G4 attribution; transformation is not assumed from the material name.

| Sub-question | Primary classification | Why this classification | Can MP1-R answer it? | Minimum observations | Allowed wording |
|---|---|---|---|---|---|
| UQ03a: Does structural TiNi transformation occur in the accessible bending domain? | `G2_EMPIRICAL_CHARACTERIZATION_GAP` | Transformation-sensitive TiNi response is established in other material domains, but activation in the same-lot strain/temperature/rate/history domain of this bending test is not established. This is a bounded material-domain characterization question, not a new mechanism claim. | Yes, by same-lot constitutive and temperature/history measurements matched to the accessed domain; a phase-sensitive measurement is useful if ordinary calibration cannot distinguish alternatives. | same-lot stress/strain response<br>wire temperature and rate/history<br>accessible bending strain/temperature domain<br>phase-sensitive measurement when needed | The study characterizes whether transformation is active in the accessed same-lot domain. |
| UQ03b: Can transformation, friction and sleeve losses be partitioned beyond aggregate loop work? | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | Aggregate loop work is not an identifiable partition. Separate material, interface and boundary observations are required; the question is attribution in one system rather than discovery of a new loss law. | Partly. MP1-R can produce bounded attribution or show that full partition is not identifiable with available observables. | same-lot material baseline<br>interface resistance and local slip<br>sleeve/end motion bounds<br>temperature and loading histories<br>defined loop-work metric; phase-sensitive data if required | The study partitions or bounds the measured contributions within the tested regime. |

### UQ04 — What model capability and coupling claim are justified?

**Parent disposition:** G2 empirical model-adequacy characterization plus G9 for any additional-law claim.

| Sub-question | Primary classification | Why this classification | Can MP1-R answer it? | Minimum observations | Allowed wording |
|---|---|---|---|---|---|
| UQ04a: Can an appropriate locked conventional model predict reserved pressure–curvature paths and available local observables? | `G2_EMPIRICAL_CHARACTERIZATION_GAP` | Conventional contact, slip and transformation-aware formulations exist, but their predictive adequacy for the defined MP1-R configuration is not quantified. The missing result is model discrimination in a bounded system, not a new constitutive principle. | Yes, with locked parameters, predeclared metrics, calibration/validation separation and reserved pressure–curvature paths. | locked conventional baseline<br>source and near-specimen pressure<br>M–κ or declared stiffness metric<br>independent local/interface observations where claimed<br>reserved paths and uncertainty-aware error | The study tests the predictive adequacy and validity limits of a conventional model for the defined configuration. |
| UQ04b: After alternatives are bounded, is an additional state-conditioned pressure/contact/material term identifiable and predictively necessary? | `G9_GAP_NOT_DEMONSTRATED` | The validated corpus does not justify claiming a broader scientific gap or a new law. This can become a conditional result only after H0a/H0b, confounders and reserved predictions are tested. | Only conditionally. MP1-R can support a residual/additional-term claim if it is repeatable, identifiable, transferable beyond a fit and required by held-out prediction; otherwise report no need for a new term. | all core pressure/material/interface controls<br>locked H0a/H0b alternatives<br>reserved predictions<br>repeatable residual pattern<br>identifiability and uncertainty analysis | An additional term is considered only if conventional alternatives fail predictively under bounded conditions. |

### UQ05 — Can Bench B reproduce the controlled-pressure structural envelope when integrated?

**Parent disposition:** G6 actuator validation plus G7 integration validation; not automatically scientific novelty.

| Sub-question | Primary classification | Why this classification | Can MP1-R answer it? | Minimum observations | Allowed wording |
|---|---|---|---|---|---|
| UQ05a: Can the SMA spring/piston reach and recover the connected-load pressure–volume envelope? | `G6_ENGINEERING_VALIDATION_NEED` | This is a capability and operating-envelope question for the proposed source. SMA-to-fluid precedents exist; a different arrangement does not create scientific novelty by itself. | Yes, by measuring stroke, force, temperature, source/near-specimen pressure and recovery under known load/compliance. | piston stroke and return<br>spring/actuator force and temperature<br>source and specimen pressure<br>connected-load pressure–volume behavior<br>repeatability and drift | The study characterizes the reachable and recoverable pressure–volume envelope of the proposed source. |
| UQ05b: At matched pressure, temperature, loading and history, does integrated response agree with externally pressurized response? | `G7_INTEGRATION_VALIDATION_NEED` | Agreement or mismatch between Bench A and Bench B tests whether separately characterized components integrate consistently. It is an integration-validation result unless a generalizable mechanism is established. | Yes, with matched specimen pressure, temperature, loading, history and synchronized response metrics. | matched near-specimen pressure<br>temperature and history controls<br>common geometry and protocol<br>external and integrated M–κ/force–deflection response<br>source transient records | The integrated source is validated against the externally controlled structural envelope within stated conditions. |


The classifications are intentionally narrow. UQ01a is a project prerequisite, not a gap; UQ01b/UQ01c and all UQ02 attribution questions require system identification; UQ03a and UQ04a are bounded empirical characterization questions; UQ04b is not demonstrated; and UQ05a/UQ05b are engineering/integration validation needs.

## B. Research-gap register

| Gap ID | Source UQ | Classification | Exact adjudicated wording | Generalizability | Testability | Contribution enabled |
|---|---|---|---|---|---|---|
| GAP01 | UQ01a | `G8_NOT_A_GAP` | Defined reaction surfaces and candidate interfaces must be fixed before interpreting pressure-conditioned mechanics. | None as a gap; the fixed geometry defines the domain of any later result. | Directly testable as a design/control prerequisite. | Enables valid interpretation of C1–C4; no standalone contribution. |
| GAP02 | UQ01b | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | Pressure-to-local-contact transmission bounds for the defined TiNi-bundle configuration are not established. | Moderate if expressed as a transferable measurement/bounding procedure; numerical values remain configuration-bounded. | Yes, with independent pressure, geometry, resistance and local-N constraints. | C1 and conditional C2/C4. |
| GAP03 | UQ01c | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | The contributions of sleeve compliance, packing, end motion and reaction-path motion to apparent stiffness are not separated for the defined system. | Low-to-moderate; method may transfer, parameter values do not automatically transfer. | Yes, by geometry/deformation measurements and bounded alternative paths. | C1 and C3. |
| GAP04 | UQ02a | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | The pressure-conditioned contribution of wire–wire versus wire–sleeve resistance is not identified from global response alone. | Moderate as an identification protocol; dominance result is configuration-specific. | Yes if independent interface constraints are feasible; otherwise report non-identifiability. | C2 and conditional C4. |
| GAP05 | UQ02b | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | The association between global branches and local slip, rather than sleeve/end motion, is not established for MP1-R. | Moderate for the branch-identification method; result is system-bounded. | Yes with local slip/strain and boundary-motion observations. | C2 and C3. |
| GAP06 | UQ03a | `G2_EMPIRICAL_CHARACTERIZATION_GAP` | Whether same-lot TiNi transformation is active in the accessible bending strain/temperature/history domain is not characterized. | Moderate across matched same-lot regimes, not universal across TiNi products. | Yes with same-lot constitutive, temperature and history measurements; phase-sensitive data if needed. | C1 and supporting material-state interpretation. |
| GAP07 | UQ03b | `G4_SYSTEM_IDENTIFICATION_REQUIREMENT` | Transformation, friction and sleeve losses cannot be partitioned from aggregate loop work without independent observations. | Moderate as an attribution procedure; fractions remain regime-specific. | Partly; MP1-R may bound rather than fully partition contributions. | Conditional C2/C4. |
| GAP08 | UQ04a | `G2_EMPIRICAL_CHARACTERIZATION_GAP` | Predictive adequacy of a locked conventional contact/friction/transformation-aware model for MP1-R is not quantitatively established. | Moderate if the validity protocol and boundary variables are reported; model parameters remain configuration-specific. | Yes with locked parameters, reserved paths and uncertainty-aware metrics. | C3, with C1 as the empirical base. |
| GAP09 | UQ04b | `G9_GAP_NOT_DEMONSTRATED` | Whether an additional state-conditioned pressure/contact/material term is identifiable and predictively necessary is not demonstrated. | Potentially high only if a repeatable, transferable, held-out residual survives all controls; currently unproven. | Conditional and high burden; not required for thesis success. | Conditional C7 only. |
| GAP10 | UQ05a | `G6_ENGINEERING_VALIDATION_NEED` | The reachable and recoverable pressure–volume envelope of the proposed SMA-spring/piston under connected load is uncharacterized. | Low-to-moderate; operating-envelope characterization may support design transfer. | Yes with actuator, piston, pressure and load measurements. | C5 supporting. |
| GAP11 | UQ05b | `G7_INTEGRATION_VALIDATION_NEED` | Matched integrated and externally pressurized bending responses are not validated for the proposed system. | Low-to-moderate as a validated integration protocol. | Yes with matched pressure, temperature, loading, history and response metrics. | C6 supporting. |

No G1 row is approved. GAP06 and GAP08 are G2 because they quantify a bounded material-domain/model-adequacy relationship without implying a new mechanism. GAP09 remains G9 because the evidence does not justify a broader gap or a required new law.

### G1 scientific-gap quality test

No candidate satisfies all of Q1–Q7 at the current evidence boundary. Pressure-to-contact mapping and interface dominance are system-specific identification questions; transformation activation is a same-lot characterization question; conventional-model adequacy is a bounded validation question; and an additional coupling law is only a conditional hypothesis. Therefore no G1 claim is released to Phase 6.

## C. Contribution-boundary register

| ID | Category | Priority | Contribution | Required evidence | H1 dependence | Failure-safe interpretation |
|---|---|---|---|---|---|---|
| CONTRIB01 | `C1_EMPIRICAL_CHARACTERIZATION` | **PRIMARY** | Quantitative pressure-conditioned bending characterization of the defined TiNi bundle. | repeatable near-specimen pressure and M–κ/declared stiffness maps<br>controlled geometry, temperature and history<br>uncertainty-resolved pressure-conditioned effects or bounded null result | Does not require H1; valid under H0a or H0b. | If pressure has no repeatable effect, report the measured null/limit and the conditions under which modulation was not observed. |
| CONTRIB02 | `C3_MODEL_DISCRIMINATION` | **SECONDARY** | Discrimination of a locked conventional model against reserved MP1-R response. | predeclared conventional model and parameters<br>calibration/validation separation<br>reserved pressure–curvature paths<br>uncertainty-aware prediction error and residual analysis | H0b may be supported; H1 is not required. | If H0b predicts well, the result is a positive model-adequacy/validity-boundary finding. |
| CONTRIB03 | `C2_MECHANISM_SYSTEM_IDENTIFICATION` | **SECONDARY** | Interface and local-slip system identification under independent constraints. | wire–wire and wire–sleeve constraints or tests<br>local slip/strain and boundary-motion observations<br>pressure/contact bounds independent of the resistance fit | Supports interpretation of H0b/H1 but does not require H1. | If interfaces cannot be separated, report non-identifiability and retain the broader C1/C3 contribution. |
| CONTRIB04 | `C4_METHODOLOGICAL_CONTRIBUTION` | **CONDITIONAL** | Validated measurement/decomposition method for separating source, pressure-path, interface and material effects. | synchronized Bench A/Bench B observations<br>independent controls and repeatable decomposition<br>demonstrated improvement in claim identifiability over global bending alone | Independent of H1; it can support H0b or a bounded null. | If decomposition is not validated, treat the benches as controls/objectives only. |
| CONTRIB05 | `C5_ACTUATOR_CHARACTERIZATION` | **SUPPORTING** | Operating-envelope characterization of the SMA-spring-driven piston source. | stroke/force/temperature<br>source and near-specimen pressure<br>connected-load reach/recovery and repeatability | Independent of H1; supports Bench B feasibility. | If the source misses the envelope, retain Bench A structural characterization and report integration infeasibility. |
| CONTRIB06 | `C6_SYSTEM_INTEGRATION` | **SUPPORTING** | Matched validation of integrated SMA/piston and externally pressurized structural response. | matched p, temperature, load, history and geometry<br>common response metric and uncertainty comparison | Independent of H1; agreement can support H0b. | If integration fails, report source/transport limits without converting them into a material mechanism. |
| CONTRIB07 | `C7_NEW_CONSTITUTIVE_THEORETICAL_CONTRIBUTION` | **CONDITIONAL** | Additional state-conditioned pressure/contact/material law, only if independently necessary. | H0a/H0b alternatives bounded<br>repeatable residual on held-out data<br>identifiable additional state variable/term<br>predictive improvement beyond refit and transfer test | Requires evidence supporting H1; never a thesis prerequisite. | If H0b suffices or the term is not identifiable, no theoretical-law contribution is claimed. |

C1 is the primary contribution. C3 is the model-discrimination support needed to keep the result scientifically interpretable. C2 is a stronger secondary contribution if independent interface observations are obtained. C4 and C7 are conditional. C5 and C6 support feasibility and integration and are not used as standalone novelty claims.

## D. Minimum, stronger and stretch contribution map

**Minimum defensible MSc contribution.** C1 quantitative pressure-conditioned bending characterization of the defined TiNi bundle, supported by C3 discrimination of a locked conventional baseline. This remains valid if H0b explains the data, H1 is not supported and no new law is required. It requires CONTRIB01, CONTRIB02 and does not require CONTRIB03, CONTRIB04, CONTRIB07.

**Stronger contribution.** C1 plus C2 interface/local-slip system identification and, where needed, C4 validated decomposition of pressure, boundary, interface and material effects. It requires independent interface constraints, local slip/boundary observations, same-lot material controls, uncertainty-aware attribution and still does not require H1 or a new law.

**Stretch contribution.** A generalizable additional pressure/contact/material term or law (C7), only if conventional alternatives fail predictively after all controls. It is available only under the stated conditions and is explicitly **not** a thesis success criterion.

## E. H0a-R / H0b-R / H1-R thesis role

| Hypothesis | Thesis role | What supports it | What weakens it | Success dependency |
|---|---|---|---|---|
| H0a-R | Live explanatory alternative and material-control branch, not a required result. | same-lot transformation-sensitive response in accessed domain<br>pressure contrasts with sleeve/end effects bounded<br>material baseline predicts relevant response features | no transformation in accessed domain<br>pressure effect persists after material state is controlled<br>contact/interface evidence explains response better | **NO; a negative or weak H0a result still supports C1/C3.** |
| H0b-R | Primary baseline comparator; it must be tested before any added-law claim. | locked conventional model predicts reserved paths within predeclared bounds<br>independent interface and boundary observations are consistent<br>no repeatable residual requiring added coupling | repeatable held-out residual after all confounders are bounded<br>independent observations show omitted state dependence | **NO; supporting H0b is a valid thesis outcome.** |
| H1-R | Conditional stretch hypothesis and optional extension; never the success criterion. | orthogonal pressure/material contrasts<br>H0a/H0b locked and tested<br>repeatable residual on reserved data<br>identifiable and predictive additional term | H0b predicts within uncertainty<br>residual disappears under interface/temperature/boundary controls<br>additional term is non-identifiable or only refits data | **NO** |

H1-R is an optional, evidence-dependent outcome. A result supporting H0b, showing no transformation in the accessed domain, or showing no identifiable added term remains scientifically valid.

## F. RQ adjudication

| ID | Disposition | Rationale | Gap IDs | Contribution IDs |
|---|---|---|---|---|
| RQ01 | **RETAIN_AS_CORE_RQ** | Directly supports C1 and the primary pressure-conditioned response map. | GAP02, GAP03 | CONTRIB01 |
| RQ02 | **RETAIN_AS_SECONDARY_RQ** | Core mechanism-identification question if independent interface constraints are feasible. | GAP04 | CONTRIB03, CONTRIB04 |
| RQ03 | **RETAIN_AS_CORE_RQ** | Necessary model-discrimination test; merge with RQ01 in the final compact set. | GAP08, GAP09 | CONTRIB02, CONTRIB07 |
| RQ04 | **CONVERT_TO_OBJECTIVE** | Actuator operating-envelope validation is supporting engineering work, not a standalone research question. | GAP10 | CONTRIB05 |
| RQ05 | **CONVERT_TO_OBJECTIVE** | Bench A/Bench B matched comparison is an integration-validation objective. | GAP11 | CONTRIB06 |
| RQ06 | **RETAIN_AS_SUPPORTING_RQ** | Material-state characterization is needed to interpret H0a/H0b but should not become a universal transformation claim. | GAP06 | CONTRIB01, CONTRIB02 |
| RQ07 | **CONVERT_TO_CONTROL / IDENTIFIABILITY CHECK** | It validates interpretation of RQ01/RQ02 rather than standing alone as a thesis RQ. | GAP05 | CONTRIB03 |
| RQ08 | **OPTIONAL_EXTENSION** | Only activated after H0a/H0b and confounders are bounded; it cannot define the required thesis outcome. | GAP09 | CONTRIB07 |
| RQ09 | **OPTIONAL_EXTENSION** | Full loss partition exceeds the minimum burden and is not identifiable from aggregate work alone. | GAP07 | CONTRIB03, CONTRIB04 |

RQ01 and RQ03 are retained as core candidates but merged into one primary RQ. RQ04 and RQ05 become objectives. RQ07 becomes an identifiability control. RQ08 and RQ09 remain optional extensions.

## G. Final RQ lock candidate

**Primary research question — PRQ01**  
For a fixed TiNi-bundle geometry, material lot and loading history, how does controlled near-specimen pressure change the bending response, and how accurately does a locked conventional contact/friction/transformation-aware model predict reserved pressure–curvature paths?

**Secondary research question — SRQ01**  
Which pressure-conditioned resistance pathway—wire–wire, wire–sleeve, or sleeve/end motion—can be identified or bounded using independent interface and local-slip observations?
Maps to `GAP04, GAP05` and `CONTRIB03, CONTRIB04`; required observables: `OBS06, OBS07, OBS08, OBS09`.

**Secondary research question — SRQ02**  
Does the same-lot TiNi undergo transformation in the accessed strain/temperature/history domain, and what material-state control is required to interpret the measured response?
Maps to `GAP06, GAP07` and `CONTRIB01, CONTRIB02`; required observables: `OBS04, OBS05, OBS10, OBS13`.

This is a candidate lock for Phase 6 drafting, not a claim that the experiments have been performed.

## H. Objective set

**Overall objective:** Quantify and interpret pressure-conditioned bending of a defined TiNi wire bundle by combining controlled structural characterization with conservative interface/material controls and a locked conventional-model test, while treating SMA/piston integration as supporting validation.

- **OBJ01:** Fix and document the cross-section, reaction surfaces, interface candidates, packing, sleeve and boundary conditions before interpreting pressure effects. (supports GAP01, GAP03)
- **OBJ02:** Measure repeatable pressure-conditioned bending response with near-specimen pressure, calibrated force/moment/curvature, temperature and loading-history controls. (supports GAP02, GAP03, GAP08)
- **OBJ03:** Establish same-lot material and interface/local-slip controls sufficient to distinguish material state, friction and boundary alternatives to the extent feasible. (supports GAP04, GAP05, GAP06, GAP07)
- **OBJ04:** Lock, calibrate and test a conventional baseline on reserved pressure–curvature paths with uncertainty-aware comparison. (supports GAP08, GAP09)
- **OBJ05:** Characterize the SMA-spring/piston pressure–volume envelope and compare integrated and external-source responses under matched conditions. (supports GAP10, GAP11)

These objectives remain achievable if H1 is not supported.

## I. Observable and evidence-burden register

| ID | Phase 5 classification | Observable | Mechanism | Maps to |
|---|---|---|---|---|
| OBS01 | **REQUIRED_FOR_CORE_CONTRIBUTION** | Near-specimen pressure p(t), reference location and synchronization | Boundary input / pressure path | PRQ01, SRQ01 |
| OBS02 | **REQUIRED_ONLY_FOR_MECHANISM_CLAIM** | Source pressure p_source(t) alongside specimen pressure | Bench B source-to-specimen dynamics | OBJ05 |
| OBS03 | **REQUIRED_FOR_CORE_CONTRIBUTION** | Bending force and calibrated moment with deflection/rotation/curvature | Global bending response | PRQ01, SRQ01 |
| OBS04 | **REQUIRED_FOR_CORE_CONTRIBUTION** | Actuator and structural-wire temperatures, time-aligned | Thermal actuation versus material state | PRQ01, SRQ02, OBJ05 |
| OBS05 | **REQUIRED_FOR_CORE_CONTRIBUTION** | Loading/unloading paths, repeatability, drift, cycle order and rate | Hysteresis and history | PRQ01, SRQ02 |
| OBS06 | **REQUIRED_FOR_CORE_CONTRIBUTION** | Confirmed packing, sleeve deformation and reaction geometry | Pressure transmission and alternative load paths | PRQ01, SRQ01 |
| OBS07 | **REQUIRED_ONLY_FOR_MECHANISM_CLAIM** | Interface-specific sliding resistance with fixture/parasitic bounds | Wire–wire and wire–sleeve friction | SRQ01, EXT02 |
| OBS08 | **REQUIRED_ONLY_FOR_MECHANISM_CLAIM** | Representative local relative slip and structural-wire strain | Slip versus material deformation | SRQ01, SRQ02 |
| OBS09 | **REQUIRED_ONLY_FOR_MECHANISM_CLAIM** | Independent local-normal-force proxy or calibrated pressure-to-contact bounds | N mapping and Coulomb capacity | SRQ01, EXT01 |
| OBS10 | **REQUIRED_ONLY_FOR_MECHANISM_CLAIM** | Same-lot constitutive response in matched strain/temperature/rate/history domain | Structural TiNi material baseline | PRQ01, SRQ02 |
| OBS11 | **HIGH_VALUE** | Piston stroke/return, force and pressure rise/recovery under known connected load/compliance | Bench B pressure–volume envelope | OBJ05 |
| OBS12 | **HIGH_VALUE** | Electrical input and spring force/bias/seal-load evidence | Actuator force/energy balance | OBJ05 |
| OBS13 | **OPTIONAL** | Direct phase-sensitive or expanded local-field measurements | Transformation/loss partition | SRQ02, EXT02 |

The core burden is OBS01, OBS03, OBS04, OBS05 and OBS06. OBS07–OBS10 become mandatory only for interface/material mechanism claims. OBS02, OBS11 and OBS12 support Bench B integration. OBS13 is optional and should be added only when ordinary same-lot calibration cannot distinguish alternatives.

## J. Success, null and kill conditions

| Contribution | Success condition | Null/baseline success | Kill condition |
|---|---|---|---|
| CONTRIB01 | Repeatable pressure-conditioned M–κ/declared stiffness branches are resolved beyond measurement and history uncertainty for the defined geometry and regime. | A small or absent pressure effect, when uncertainty-resolved, is a valid bounded characterization and can still support C3 by defining a null regime. | Pressure/specimen state cannot be measured or controlled, geometry remains ambiguous, or repeatability is below the declared uncertainty so no quantitative response map is defensible. |
| CONTRIB02 | A locked conventional model either predicts reserved paths within predeclared bounds or fails with a repeatable, uncertainty-resolved residual after confounders are bounded. | H0b predicts well; model adequacy and validity boundary are positive results, and no new law is claimed. | No parameter lock, no reserved paths, or no independent observations sufficient to distinguish fit quality from leakage/confounding. |
| CONTRIB03 | Independent interface/local-slip observations identify a dominant contribution or produce defensible bounds on competing pathways. | No dominance can be identified; report non-identifiability while retaining C1/C3. | Only global bending is measured, or interface tests cannot be made independent of the same unknowns. |
| CONTRIB05 | The source reaches and recovers a characterized connected-load pressure–volume envelope with repeatable timing and force/temperature records. | The envelope is insufficient; Bench A can remain the structural study and the source limitation is reported as engineering validation failure. | No reliable pressure/stroke/force record or no connected-load characterization. |
| CONTRIB06 | Integrated and external responses agree within declared uncertainty under matched p, temperature, load, history and geometry, or the mismatch is traced to a bounded source/path effect. | No integration claim is required if the source cannot reproduce the envelope; C1/C3 remain possible. | Conditions cannot be matched or the source/structural clocks cannot be synchronized. |
| CONTRIB07 | Only after H0a/H0b controls, a repeatable held-out residual requires an identifiable additional term that improves prediction beyond refitting. | H0b suffices or the term is not identifiable; no new-law contribution is made. | Residual disappears with controls, is fit-only, or cannot be separated from parameter/boundary uncertainty. |

Failure to demonstrate a new coupling law does not kill the thesis because C1 and C3 are approved without H1.

## K. Novelty boundary

| Type | Status | Boundary |
|---|---|---|
| Scientific Novelty | **NOT_DEMONSTRATED_AT_PHASE_5_START** | No generalizable new pressure–contact–material law or mechanism is currently established. A scientific novelty claim is conditional on a repeatable, transferable, held-out result beyond H0a/H0b. |
| System Novelty | **POSSIBLE_ENGINEERING_COMBINATION_ONLY** | The SMA-spring/piston, fluid path and TiNi structure may form a new implementation combination, but combination alone is not scientific novelty. |
| Empirical Novelty | **DEFENSIBLE_BOUNDED** | New quantitative characterization of pressure-conditioned bending in the defined TiNi-bundle regime may be claimed without a universal or first-ever statement. |
| Methodological Novelty | **CONDITIONAL** | A validated decomposition/identification protocol may be a methodological contribution if it demonstrably enables claims unavailable from global bending alone. |
| Engineering Novelty | **SUPPORTING_ONLY** | Source operating envelope, packaging and integration performance may be engineering contributions and must be labelled accordingly. |

Scientific novelty is not demonstrated at Phase 5 start. Empirical, methodological (conditional) and engineering contributions remain available without a universal first-ever claim.

## L. Claim-wording register

### Claims allowed before experiment

- **Allowed:** Validated related architectures show architecture-scoped pressure/confinement effects on bending response. **Boundary:** No universal pressure–stiffness law or MP1-R transfer. **Basis:** RP001, RP002.
- **Allowed:** Conventional contact/slip and transformation-aware formulations exist and can serve as locked comparators. **Boundary:** Existence is not adequacy proof. **Basis:** RP005, RP007, RP008, RP011.
- **Allowed:** The pressure-to-local-contact map, interface dominance, TiNi-state activation in the accessed domain and matched source integration are not established for MP1-R. **Boundary:** These are unresolved/project-specific questions, not automatically literature gaps. **Basis:** RP017, RP018, RP019, RP020.
- **Allowed:** Bench A/B separation is a design rationale for attribution. **Boundary:** It is not evidence that two benches are uniquely novel or mandatory. **Basis:** RP014.

### Claims allowed only after a specific result

- **Pressure changes bending response in the defined TiNi bundle.** only after: Repeatable, uncertainty-resolved near-specimen pressure and bending response under fixed geometry/history.
- **A particular interface dominates or contributes a bounded fraction.** only after: Independent interface constraints and local/boundary observations.
- **TiNi transformation is active in the accessed domain.** only after: Same-lot matched constitutive/temperature/history or phase-sensitive evidence.
- **A conventional model predicts or fails on MP1-R.** only after: Locked parameters, reserved paths, declared metrics and uncertainty-aware comparison.
- **An additional coupling term is necessary.** only after: H0a/H0b and confounders bounded, repeatable held-out residual, identifiable predictive improvement.
- **Integrated SMA/piston response reproduces or fails to reproduce external-pressure response.** only after: Matched pressure, temperature, load, history, geometry and synchronized response.

### Claims currently prohibited

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
- No previous research has studied this mechanism.
- The unresolved pressure/contact map is itself a demonstrated scientific knowledge gap.
- The project contribution requires H1-R to be supported.
- A null pressure effect or successful H0b result makes the thesis scientifically invalid.
- The current working title can be used as causal evidence that pressure-controlled friction has already been demonstrated in MP1-R.

## M. Working-title audit

**Decision:** **REVISE**. The current title, *Characterization of Bending Stiffness in TiNi Wire Bundles Using Pressure-Controlled Friction Generated by an SMA-Spring-Driven Piston*, presupposes pressure-controlled friction and a causal piston role before the pressure-to-interface map and matched integration are established.

**Conservative title:** *Pressure-Conditioned Bending Characterization of TiNi Wire Bundles with an SMA-Spring-Driven Pressure Source*

**Mechanism-focused conditional title:** *Interface-Resolved Pressure–Friction–Bending Response of TiNi Wire Bundles under SMA-Spring-Driven Pressurization* — use only after independent interface and pressure/contact evidence.

## N. Chapter 2 gap-wording register

| Gap | Safe strongest wording | More conservative wording | Prohibited wording |
|---|---|---|---|
| GAP02 | The validated literature establishes pressure-dependent response in related architectures, but does not establish the pressure-to-local-contact transmission for the defined TiNi-bundle configuration. | The pressure-to-contact relation remains unestablished for this configuration and must be bounded experimentally. | No previous research has studied pressure-to-contact transmission. |
| GAP04 | Interface-specific resistance tests provide precedents, while pressure-conditioned wire–wire versus wire–sleeve contribution remains a system-identification question for MP1-R. | The dominant interface cannot be inferred from global bending alone. | Interface disambiguation is a literature-wide scientific gap. |
| GAP06 | NiTi state-sensitive response is established in tested domains, but transformation activity in the accessed same-lot bending domain is not established. | The study will characterize whether transformation is active in the measured domain. | TiNi necessarily transforms and dominates hysteresis. |
| GAP08 | Existing conventional formulations provide a comparator, but their predictive adequacy for the defined MP1-R configuration has not been quantitatively tested on reserved paths. | A locked conventional baseline is required before any stronger coupling claim. | The literature lacks the exact equation, so a new law is required. |
| GAP10/GAP11 | The proposed source operating envelope and matched integrated/external response remain to be validated for the selected architecture. | Actuator and integration performance are supporting validation tasks. | A different spring/piston arrangement is automatically a new scientific mechanism. |

Chapter 2 must describe unresolved questions as bounded, configuration-specific and evidence-controlled. It must not turn corpus absence into a universal literature claim.

## O. Chapter 3 implication boundary

- **Intervention:** Controlled near-specimen pressure applied to a fixed, mentor-confirmed cross-section; Bench B source operation is a separate intervention clock.
- **Control:** Geometry, packing, reaction/sleeve path, material lot, temperature, loading rate, history, source versus specimen pressure, and cycle order.
- **Measurement:** M–κ or predeclared stiffness metric, near-specimen pressure, temperature, histories, boundary motion, local/interface observations and source records as required by the claim.
- **Comparison:** Externally pressurized Bench A versus integrated SMA/piston Bench B only at matched p, temperature, load, history and geometry.
- **Validation:** Uncertainty-aware repeatability, calibration/validation separation, independent interface/material controls and explicit null handling.
- **Held_Out_Test:** Reserved pressure–curvature paths for the locked conventional model; no post-hoc threshold or term selection.
- **Claim_Mapping:** C1: OBS01/03/04/05/06; C2: OBS07/08/09; C3: locked model + OBS01/03/05/06/08/10; C5/C6: OBS02/04/11/12

This is an evidence-burden boundary, not a hardware redesign.

## P. Phase 6 handoff

Phase 6 is released to draft Chapter 2 within the following boundary:

- **Scope:** pressure-conditioned bending characterization of a fixed TiNi-bundle configuration; external-pressure structure characterization is primary, SMA/piston integration is supporting.
- **Approved classifications:** 0 G1; 2 G2; 0 G3; 5 G4; 0 G5; 1 G6; 1 G7; 1 G8; 1 G9.
- **Primary contribution:** C1, supported by C3.
- **Secondary/supporting contributions:** C2 conditional on independent observations; C5 and C6 supporting.
- **Conditional stretch:** C7 only after held-out, uncertainty-resolved failure of simpler alternatives; never required.
- **Final RQs:** PRQ01, SRQ01 and SRQ02 above.
- **Hypotheses:** H0a-R and H0b-R remain live; H1-R is optional and not a success criterion.
- **Minimum evidence:** OBS01, OBS03, OBS04, OBS05, OBS06 plus a locked conventional baseline and reserved paths for C3.
- **Novelty language:** bounded empirical and conditional methodological/system claims only; no universal first claim.
- **Prohibited claims:** the complete Phase 4 prohibition union plus the Phase 5 additions in the claim-wording register.

### Canonical Phase 4 provenance

- Authority: `outputs/plans/MP1_R_PHASE_4_RECONCILED_PHASE_5_HANDOFF_2026-10-02.json`; gate `READY_FOR_PHASE_5_GAP_ADJUDICATION`; release `READY`.
- Reconciled synthesis: `docs/literature/MP1_R_PHASE_4_RECONCILED_SYNTHESIS_2026-10-02.md`.
- Reconciliation matrix: `outputs/plans/MP1_R_PHASE_4_RECONCILIATION_MATRIX_2026-10-02.json`.
- Canonical Phase 4 themes/propositions: 5 / 21.
- Preserved hypothesis state: H0a-R `PLAUSIBLE`, H0b-R `PLAUSIBLE`, H1-R `NOT_YET_DISTINGUISHABLE`.
- Critical weakest link: `radial reaction → local wire–wire / wire–sleeve contact normal forces`.
- No secondary material was reopened; original papers reopened: 0; broad literature searches: 0.

## Release gate

`READY_FOR_PHASE_6_CHAPTER_2_DRAFTING`

The gate is released because a defensible contribution exists, gap/need classifications are explicit, the RQ set is bounded, H1 is not required, no unsupported G1 claim remains, and the Chapter 2 claim boundary is stable. Phase 6 must stop at the approved literature-review boundary and must not convert these decisions into experimental results or novelty claims.

