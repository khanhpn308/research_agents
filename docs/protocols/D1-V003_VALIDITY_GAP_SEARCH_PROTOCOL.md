# D1-V003 Validity-Gap Search Protocol

**Verification round:** `D1-V003`  
**Protocol date:** 2026-09-15  
**Scientific posture:** adversarial falsification, not topic defense  
**Novelty status:** unadjudicated; this protocol makes no novelty claim

## 1. Falsification target

The surviving candidate question is:

> For one explicitly named mechanics-level continuum/reduced model and one fixed layer-jamming beam/material family, can the quantitative prediction error relative to explicit-interface mechanics and independently calibrated experiments be mapped over independently controlled layer count, pressure, load/curvature, and slip regime, so that a predeclared tolerance-defined validity/breakdown boundary can be identified?

The purpose of this search is to find the closest paper capable of making that question already answered, derivative, or unnecessary. It is not enough to find another continuum model, another layer-jamming experiment, or another model–experiment plot. The strongest target paper contains all four elements below in one coherent validation study:

1. an explicit-interface or otherwise demonstrably discrete mechanics reference;
2. an experiment not reused to fit every tested prediction;
3. a numerical prediction-error metric or a declared acceptance tolerance; and
4. a parameter-dependent validity or breakdown boundary.

### 1.1 Operational definitions

| Term | Required evidence for a positive screen |
|---|---|
| Explicit-interface/discrete reference | Individual layers and interfaces are mechanically resolved, or a discrete layer/interface formulation is solved and compared with a named reduced model. Merely using finite elements is insufficient. |
| Independent experiment | At minimum, the calibration data and validation data are distinguishable. A curve fit and comparison to the same curve is calibration, not independent validation. |
| Numerical error metric | A quantity such as RMSE, MAE, normalized error, maximum error, confidence interval, or explicitly defined residual is reported or can be reconstructed from deposited data. “Good agreement” alone does not qualify. |
| Declared tolerance | The acceptable error is specified before interpreting the resulting boundary. A threshold chosen after viewing the results must be marked post hoc. |
| Validity domain | A set of parameter combinations for which a named model satisfies the declared error criterion. |
| Breakdown boundary | A quantitative boundary separating accepted and rejected predictions, together with the parameter coordinates and, ideally, the first omitted mechanism responsible. |
| Independently controlled variables | Physical layer count, pressure, and load/curvature are varied without silently substituting layer thickness for layer count or changing several geometric/material variables at once. |

### 1.2 Evidence labels

- **[VERIFIED FULL TEXT]**: supported by a repository evidence JSON that passed validation and, where necessary, the corresponding inspected PDF.
- **[METADATA ONLY]**: supported only by a title, abstract, citation index, publisher record, or other bibliographic record.
- **[INFERENCE]**: a reasoned classification not stated by the source.

Metadata can nominate or rank a paper. It cannot establish that the paper satisfies the four-part falsification target.

## 2. Existing evidence that the new search must not rediscover as a “gap”

The following starting points are already established in the repository:

- Zhang et al., *A continuum-based model for a layer jamming beam*, DOI `10.5194/ms-16-821-2025`, presents a continuous-medium beam model, explicit layered FEA comparisons, and experiments. **[VERIFIED FULL TEXT]**
- Zhang et al., *Toward a deeper understanding of layer jamming structures*, DOI `10.1007/s11465-025-0843-5`, treats pressure, physical layer thickness/count, curvature, progressive/full slip, large-configuration updates, cyclic loading, and experimental comparison. Its D1-V003 audit concluded that it substantially narrows but does not provide a declared-tolerance error domain. **[VERIFIED FULL TEXT]**
- Zhang et al., *Continuum modeling for layer jamming structures*, DOI `10.1016/j.taml.2025.100633`, derives an average-field continuum elastoplastic constitutive model from a discrete RVE and validates it against periodic-cell FEA, but reports no physical experiment. **[VERIFIED FULL TEXT]** The publisher describes the RVE, average-field model, FEA load cases, and absence of experiments in its [article record](https://doi.org/10.1016/j.taml.2025.100633).
- Fan et al. (2026) uses a reduced, control-oriented layer-jamming continuum-robot model. It does not validate the reduced layer mechanics against an explicit-interface reference or map a tolerance-defined breakdown boundary. **[VERIFIED FULL TEXT]**

Therefore, the search must not treat any of the following alone as a successful research gap: existence of a continuum model; treatment of pressure; treatment of slip regimes; testing more than one pressure or sheet thickness; an experiment; or qualitative model–data agreement.

## 3. Decision rule before searching

Each retrieved work receives exactly one provisional outcome after full-text screening:

| Outcome | Rule |
|---|---|
| **KILL** | The paper contains all four target elements and applies them either to the named layer-jamming model/family or through a general result that transfers without a new mechanics problem. |
| **NARROW** | The paper answers a material portion of the question—normally two or three target elements, or all four under materially different interface/loading assumptions—but leaves a specific nontrivial axis unresolved. |
| **ORTHOGONAL** | The work concerns variable stiffness, robotics, layered structures, or friction but does not test the validity of a mechanics-level continuum/reduced layer-stack representation. |
| **SUPPORTING** | The work explicitly documents a discrepancy, unvalidated assumption, or need for such a validity study without itself solving it. This outcome is not proof of novelty. |

When two labels seem plausible, use the more damaging one provisionally and record the uncertainty. A KILL classification requires full text; metadata alone can be tagged only `potential KILL`.

## 4. Track A — 2025–2026 forward citations of the three Zhang seeds

### 4.1 Seed identity

| Seed | Bibliographic identity | Repository status |
|---|---|---|
| `A1` | Zhang, Yao, Zhao, and Wei (2025), *A continuum-based model for a layer jamming beam*, DOI `10.5194/ms-16-821-2025` | **[VERIFIED FULL TEXT]** |
| `A2` | Zhang, Yao, Zhao, and Zhu (2025), *Toward a deeper understanding of layer jamming structures*, DOI `10.1007/s11465-025-0843-5` | **[VERIFIED FULL TEXT]** |
| `A3` | Zhang, Yao, Li, and Chen, *Continuum modeling for layer jamming structures*, online 2025 / volume 16 issue 1 (2026), DOI `10.1016/j.taml.2025.100633` | **[VERIFIED FULL TEXT]** |

The mixed 2025/2026 dating of `A3` must be retained rather than silently normalized: the repository PDF records online availability in 2025, while the publisher issue record is 2026.

### 4.2 Public-index snapshot on 2026-09-15

This is a candidate-discovery snapshot, not an exhaustive citation census.

OpenAlex and Semantic Scholar each reported citation counts of `1`, `1`, and `0` for `A1`, `A2`, and `A3`, respectively, and agreed on the identities of the two indexed citing works. Copernicus independently lists one Crossref-recorded citation for `A1`. ResearchGate lists one citation for `A3`, creating an unresolved index disagreement. These counts must never be summed. The authoritative search round must use the union of Scopus, Web of Science, Google Scholar/Publish or Perish, Crossref/publisher citing pages, OpenAlex, and Semantic Scholar, preserving each source independently.

Sources: [Copernicus citation metrics for A1](https://ms.copernicus.org/articles/16/821/2025/ms-16-821-2025-metrics.html), [OpenAlex A1 record](https://api.openalex.org/works/https://doi.org/10.5194/ms-16-821-2025), [OpenAlex A2 record](https://api.openalex.org/works/https://doi.org/10.1007/s11465-025-0843-5), [OpenAlex A3 record](https://api.openalex.org/works/https://doi.org/10.1016/j.taml.2025.100633), and Semantic Scholar Graph API records for the same DOI identities.

### 4.3 Candidates currently visible

| Priority | Candidate and citation relationship | Continuum vs discrete | Layer-count convergence | Explicit interlayer slip | Prediction error | Validity domain | Breakdown boundary | Experiment | Provisional threat |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **A3 itself**, citing `A2`: Zhang et al., *Continuum modeling for layer jamming structures*, DOI `10.1016/j.taml.2025.100633`. OpenAlex identifies it as the one forward citation of `A2`. | Yes: average-field model versus discrete periodic RVE FEA **[VERIFIED FULL TEXT]** | No systematic physical-layer-count convergence map found **[VERIFIED FULL TEXT]** | Yes at RVE/constitutive level **[VERIFIED FULL TEXT]** | Comparisons and deviations, but no declared-tolerance error surface **[VERIFIED FULL TEXT]** | No **[VERIFIED FULL TEXT]** | No **[VERIFIED FULL TEXT]** | No physical experiment **[VERIFIED FULL TEXT]** | **MEDIUM** against the surviving gap; very high against any broader “continuum model does not exist” claim. Already ingested—do not re-register. |
| 2 | Cheng et al. (2026), *A Review of Variable Stiffness in Continuum Robots: Mechanisms, Modeling and Control*, DOI `10.3390/machines14050572`, citing `A1` according to OpenAlex and Copernicus. | Review-level discussion only **[METADATA ONLY]** | Unclear | Unclear | No original benchmark apparent | No original domain apparent | No original boundary apparent | No original layer-jamming validation apparent | **LOW** as a direct technical threat; **MEDIUM** as a bibliography-mining source. The publisher labels it a review and describes its mechanism/model/control synthesis in the [article record](https://www.mdpi.com/2075-1702/14/5/572). |
| 3 | Chen et al. (2026), *Design Characteristics of Continuum Robots Based on TSA Variable Stiffness Method*, DOI `10.3390/act15030154`, alleged by ResearchGate to cite `A3`; OpenAlex reports zero forward citations for `A3`. | No target comparison apparent **[METADATA ONLY]** | No | No layer-jamming interface model apparent | No target-model error apparent | No | No | Robot stiffness experiments, but on a TSA force-locking spine **[METADATA ONLY]** | **LOW / ORTHOGONAL**. Verify the reference list because the citation relation is index-dependent. The [publisher record](https://www.mdpi.com/2076-0825/15/3/154) describes TSA cable tension and substrate friction, not a vacuum-jammed sheet stack. |

No other 2025–2026 forward-citing work was visible in the public sources checked on the protocol date. This statement means “not found in this snapshot,” not “does not exist.” Scopus, Web of Science, and a reproducible Scholar export remain mandatory evidence gaps.

### 4.4 Exact Track A searches

Run every seed separately so that provenance and cited seed remain recoverable.

#### A1 — DOI `10.5194/ms-16-821-2025`

```text
"10.5194/ms-16-821-2025"
"A continuum-based model for a layer jamming beam"
("10.5194/ms-16-821-2025" OR "A continuum-based model for a layer jamming beam") AND (discrete OR interface OR interlayer OR convergence OR error OR accuracy OR validity OR limitation OR breakdown OR experiment)
```

Why: the first two strings maximize recall across indexed and non-indexed citations; the intersection ranks papers that do more than cite the model as background.

- Include every genuine 2025–2026 citation as a metadata candidate.
- Prioritize full text if the title/abstract mentions benchmarking, discrete layers/interfaces, layer count, model error, or validation.
- Deprioritize reviews and application papers that only list jamming mechanisms, but mine their references.
- **Expected threat:** HIGH for a technical follow-on; LOW for the currently visible review.
- **Stop condition:** stop the A1 harvest only after the complete 2025–2026 citing sets from Scopus, WoS, Scholar/PoP, OpenAlex, Semantic Scholar, and the Copernicus/Crossref page have been exported, deduplicated, and every discrepancy has a provenance note.

#### A2 — DOI `10.1007/s11465-025-0843-5`

```text
"10.1007/s11465-025-0843-5"
"Toward a deeper understanding of layer jamming structures"
("10.1007/s11465-025-0843-5" OR "Toward a deeper understanding of layer jamming structures") AND (continuum OR discrete OR interface OR slip OR convergence OR error OR validity OR breakdown OR calibration OR validation)
```

Why: `A2` already covers most physical axes, so its descendants are the most likely to quantify the remaining approximation error or repair a documented limitation.

- Include every genuine 2025–2026 forward citation.
- Do not treat `A3` as a new acquisition; update only the screening matrix with its existing verified evidence.
- Exclude a result only after confirming it is a false citation/identity match.
- **Expected threat:** HIGH because an author follow-on could operationalize the continuous-slip-boundary approximation.
- **Stop condition:** same complete-source union as A1, plus author-profile and exact-title searches for all four A2 authors through 2026.

#### A3 — DOI `10.1016/j.taml.2025.100633`

```text
"10.1016/j.taml.2025.100633"
"Continuum modeling for layer jamming structures"
("10.1016/j.taml.2025.100633" OR "Continuum modeling for layer jamming structures") AND (RVE OR experiment OR structural OR bending OR beam OR discrete OR error OR accuracy OR validity OR breakdown)
```

Why: the A3 paper explicitly leaves structural experimental validation for future work. A citing paper that performs that validation and adds an error boundary is a direct kill candidate.

- Include every genuine forward citation from online publication through 2026, including early-access and preprint records.
- Prioritize papers that implement the named A3 constitutive law in a structural beam/robot model.
- Deprioritize papers that cite A3 only as a generic jamming technique.
- **Expected threat:** HIGH—the highest Track A threat—if a structural experiment plus discrete-RVE comparison appears.
- **Stop condition:** reconcile the present `0` versus `1` citation-index conflict, search both 2025 and 2026 bibliographic years, and screen all citing records from every source; absence in one index is never a stopping rule.

### 4.5 Track A candidate priority rule

Rank each forward citation by the count of independently supported target elements, then break ties in this order:

1. implements the exact `A1`, `A2`, or `A3` equations;
2. compares that implementation with explicit interface mechanics;
3. separates calibration and experiment;
4. reports a numerical error over more than one independent parameter axis;
5. names a tolerance or locates failure onset;
6. identifies the omitted mechanism at failure.

A paper meeting items 1–4 is immediate full-text priority even if its abstract never uses “validity domain.”

## 5. Track B — adjacent solid mechanics

### 5.1 Search strategy

Adjacent mechanics is dangerous precisely because the decisive theory may not use the phrase “layer jamming.” Search in three passes:

1. **phenomenon pass:** retrieve the family without requiring validity vocabulary;
2. **comparison pass:** add discrete/continuum, interface, and experimental terms;
3. **kill pass:** add error, tolerance, convergence, validity, and boundary terms.

Do not start with one overconstrained query and interpret zero results as absence. Search all years for foundational theory, then filter the validation/benchmarking follow-ons with emphasis on 2010–2026 and a final alert window for 2025–2026.

Portable strings below can be used in Google Scholar, Dimensions, Lens, or Compendex. For Scopus, wrap the expression in `TITLE-ABS-KEY(...)`; for Web of Science, wrap it in `TS=(...)` while preserving parentheses.

### 5.2 B1 — partial-interaction multilayer beams

```text
("partial interaction" OR "incomplete interaction") AND ("multilayer beam" OR "multi-layer beam" OR "layered beam" OR "built-up beam") AND ("interlayer slip" OR "interface slip" OR "shear connection")

("partial interaction" OR "incomplete interaction") AND ("multilayer beam" OR "layered beam") AND (discrete OR continuum OR homogenization) AND (experiment OR validation OR "error bound" OR convergence OR validity OR breakdown)
```

Why: partial-interaction theory explicitly connects interface transfer to global bending stiffness and may already contain dimensionless interaction parameters or continuum limits.

- Include multilayer formulations with recoverable interface laws, bending response, and a discrete or layerwise comparator.
- Exclude conventional two-component steel–concrete beams if their connector law cannot represent distributed frictional activation; retain foundational transferable theory as background.
- **Expected threat:** HIGH. A general interaction parameter with a verified error threshold could reduce the proposed work to application.
- **Stop condition:** screen all papers cited by and citing the nearest mathematical formulation until two successive 20-record relevance-ranked batches produce no new transferable interface law or validation criterion.

### 5.3 B2 — laminated beams with interlayer slip

```text
("laminated beam" OR "laminated composite beam" OR "layerwise beam") AND ("interlayer slip" OR "interface slip" OR "imperfect interface" OR "interface compliance") AND (bending OR flexure OR curvature)

("laminated beam" OR "layerwise beam") AND ("Coulomb friction" OR stick-slip OR "partial slip" OR "imperfect interface") AND (discrete OR continuum OR homogenization) AND (experiment OR error OR convergence OR validity)
```

Why: laminated-beam models may quantify when equivalent single-layer theories cease to reproduce layerwise kinematics or interface stresses.

- Include debond-free models with finite interfacial relative displacement and a comparison between layerwise and equivalent representations.
- Exclude perfectly bonded classical laminate theory unless it explicitly tests loss of validity caused by imperfect interfaces; exclude fracture-only delamination work without a pre-failure slip regime.
- **Expected threat:** HIGH for the representation/error methodology; MEDIUM for direct Coulomb/vacuum transfer.
- **Stop condition:** stop after the principal layerwise-versus-equivalent benchmark families and their experimental descendants have been screened, with no new frictional validity criterion in two successive query variants.

### 5.4 B3 — frictional layered beams and stacked sheets

```text
("frictional layered beam" OR "layered beam with friction" OR "frictional laminate" OR "stacked sheets" OR "stack of sheets") AND (bending OR curvature) AND ("Coulomb friction" OR stick-slip OR "partial slip")

("frictional layered beam" OR "stacked sheets") AND (discrete OR "explicit interface" OR continuum OR homogenization OR "equivalent beam") AND (experiment OR validation) AND (error OR tolerance OR validity OR breakdown OR boundary)
```

Why: this is the closest physics outside jamming terminology: elastic sheets, normal compression, Coulomb traction, progressive sliding, and bending.

- Include models resolving individual contacts or comparing an equivalent continuum with a stacked-sheet experiment.
- Exclude bonded laminates, granular beds, and sliding without normal-contact/friction mechanics.
- **Expected threat:** HIGH—the most direct physical analogue in Track B.
- **Stop condition:** do not stop at keyword saturation; trace all references and citations of any paper containing Coulomb-contact bending of three or more sheets. Stop only when each such lineage has been screened through its latest citing work.

### 5.5 B4 — multi-leaf springs

```text
("multi-leaf spring" OR "multi leaf spring" OR "leaf-spring stack" OR "leaf spring stack") AND ("interleaf friction" OR "inter-leaf friction" OR "interlayer slip" OR stick-slip) AND (model OR simulation OR experiment)

("multi-leaf spring" OR "leaf spring stack") AND ("equivalent beam" OR continuum OR homogenization OR reduced-order) AND ("interleaf friction" OR slip) AND (error OR validation OR validity OR limitation OR convergence)
```

Why: multi-leaf springs are frictional curved stacks with progressive contact/slip, hysteresis, end effects, and a long engineering modeling history.

- Include analytical, FEA, and experimental papers that compare explicit leaves/contact with an equivalent model.
- Exclude fatigue/life/design optimization papers that use a black-box stiffness without testing interface mechanics.
- **Expected threat:** HIGH, especially for error metrics and boundary/end effects; transfer may be limited by nonuniform preload, tapered leaves, clamps, and steel elasticity.
- **Stop condition:** screen the dominant analytical, FE-contact, and experimental model families plus standards/handbooks they cite; stop when no study links model error to leaf count, preload, curvature/load, or slip state.

### 5.6 B5 — shear-lag with imperfect interfaces

```text
("shear lag" OR shear-lag) AND ("imperfect interface" OR "interface slip" OR "interfacial slip" OR "partial interaction") AND ("multilayer beam" OR laminate OR "layered structure") AND (bending OR flexure)

("shear lag" OR shear-lag) AND (discrete OR layerwise OR continuum OR homogenization) AND ("imperfect interface" OR slip) AND (experiment OR validation OR "error estimate" OR "range of validity")
```

Why: shear-lag theory creates a characteristic load-transfer length. A published scale ratio comparing that length with layer thickness or specimen length could supply the missing validity criterion.

- Include models with a defined internal length/transfer length and quantitative layerwise comparison.
- Exclude adhesive-joint strength studies without bending or without any reduced-versus-discrete comparison.
- **Expected threat:** MEDIUM to HIGH. The mathematics may transfer, but linear cohesive/shear-spring interfaces are not automatically equivalent to pressure-dependent Coulomb friction.
- **Stop condition:** identify the canonical nondimensional shear-lag parameters and screen every paper that attaches a numerical error range to them; stop if later variants only change materials or geometry without changing the criterion.

### 5.7 B6 — homogenization of layered beams with friction or slip

```text
("layered beam" OR "laminated beam" OR "stacked layers") AND (homogenization OR "asymptotic homogenization" OR "effective medium" OR "equivalent continuum") AND ("frictional slip" OR "Coulomb friction" OR stick-slip OR "imperfect interface")

("layered beam" OR "stacked layers") AND (homogenization OR "effective continuum") AND (RVE OR "representative volume element" OR multiscale) AND (experiment OR "error estimate" OR convergence OR validity OR breakdown)
```

Why: a rigorous homogenization result may already define scale separation and an error estimate, directly challenging any claim that mapping the discrete-to-continuum boundary is a new mechanics problem.

- Include formal asymptotic, computational homogenization, and effective-continuum studies with slipping/frictional interfaces.
- Exclude perfectly bonded homogenization unless it explicitly gives an imperfect-interface limit that can be specialized to friction.
- **Expected threat:** HIGH theoretically; it remains HIGH against the complete four-part target only if independent experiments or a validated finite-layer-count error boundary are also present.
- **Stop condition:** stop after the principal homogenization theorem/model, its finite-cell numerical verification, and experimental applications have been connected. A theorem without a usable finite-layer-count error criterion does not by itself stop the whole audit.

### 5.8 B7 — asymptotic convergence of multilayer systems

```text
("multilayer system" OR "multilayer beam" OR "periodic layers" OR "stacked elastic layers") AND ("continuum limit" OR "discrete-to-continuum" OR "asymptotic convergence" OR "convergence rate" OR "Gamma convergence" OR "Γ-convergence") AND (slip OR friction OR "imperfect interface")

("multilayer beam" OR "stacked elastic layers") AND ("continuum limit" OR "discrete-to-continuum") AND ("error estimate" OR "convergence rate" OR "critical layer thickness" OR "validity range") AND (friction OR slip)
```

Why: a convergence rate in layer thickness or layer count could mathematically define when discrete oscillations become negligible, even if developed outside robotics.

- Include finite-layer-count convergence estimates, asymptotic limits retaining an internal length, and numerical confirmation.
- Exclude pure existence proofs with no mechanically identifiable error norm or no interface slip, but retain them as theoretical background if they define the correct limit model.
- **Expected threat:** HIGH to the conceptual gap, MEDIUM to the all-four target because independent experiments are uncommon.
- **Stop condition:** identify whether a finite-layer-count error estimate exists. If it does, immediately search all experimental applications of that exact model; if not, stop the family after the main theorem line and its citations are exhausted.

### 5.9 B8 — discrete-to-continuum transition with Coulomb friction

```text
("discrete-to-continuum" OR "continuum approximation" OR "continuum limit") AND ("Coulomb friction" OR "frictional contact" OR stick-slip) AND (multilayer OR laminated OR "layered beam" OR "stacked sheets")

("discrete-to-continuum" OR "continuum approximation") AND ("Coulomb friction" OR "frictional contact") AND (experiment OR validation) AND (error OR tolerance OR convergence OR "validity domain" OR "breakdown boundary")
```

Why: this names the exact mathematical transition and interface law without requiring layer-jamming vocabulary.

- Include any geometry if the discrete objects, continuum limit, friction law, error norm, and parameterized failure criterion are transferable to a beam stack.
- Exclude granular-flow continuum limits unless the state variables and friction/contact scaling can be mapped to ordered elastic layers.
- **Expected threat:** HIGH—the highest-priority adjacent family.
- **Stop condition:** screen all exact phrase matches, then replace “multilayer” with `lamellar`, `laminar`, `sheet stack`, `book`, and `stratified`. Stop only after no transferable ordered-layer result appears in two consecutive 20-record blocks for every synonym branch.

## 6. Cross-cutting query modifiers

Apply these modifiers as separate searches rather than joining all of them at once:

### Error and validity

```text
("model error" OR "prediction error" OR RMSE OR MAE OR "relative error" OR "error bound" OR tolerance OR "range of validity" OR "validity domain" OR breakdown)
```

### Finite layer count and scale separation

```text
("layer count" OR "number of layers" OR "finite number of layers" OR "layer thickness" OR "scale separation" OR "size effect" OR convergence)
```

### Interface mechanism

```text
("explicit interface" OR "interface-resolved" OR "interlayer slip" OR "partial slip" OR "progressive slip" OR stick-slip OR "Coulomb friction")
```

### Validation independence

```text
(experiment OR validation OR benchmark) AND (calibration OR identification OR "training data" OR "held-out" OR "blind prediction")
```

“Held-out” is only a search synonym here. Held-out testing alone is not a novelty contribution and does not satisfy the target unless the mechanics question and tolerance boundary are present.

## 7. Inclusion and exclusion gates

### 7.1 Metadata candidate

Retain a record when its title, abstract, keywords, or citation context suggests at least one of:

- a continuum/effective/reduced representation of an ordered layered structure;
- discrete layer or explicit interface mechanics;
- interlayer friction, slip, partial interaction, or imperfect interfaces;
- a model comparison, error estimate, validity range, or experiment involving bending.

### 7.2 Full-text priority

Acquire full text when metadata indicates either:

- any three of the four target elements; or
- an explicit discrete-to-continuum derivation with Coulomb friction; or
- a finite-layer convergence/error theorem; or
- implementation or experimental validation of one of the three Zhang models.

### 7.3 Exclude or deprioritize

Exclude only with a recorded reason. Typical reasons are:

- granular/fiber jamming with no ordered-layer mechanics transferable to sheets;
- perfectly bonded laminates with no slip/imperfect-interface limit;
- delamination/fracture only, with no pre-failure relative sliding model;
- controller or robot design using fitted stiffness but no mechanics-level layer representation;
- application demonstration with no model comparison;
- pure material substitution, geometry variation, extra pressure levels, or extra FEA without a new error/validity question;
- review articles as primary scientific evidence. Reviews remain citation maps.

Do not exclude a metadata record merely because the abstract omits an error metric; methods and supplementary files may contain it.

## 8. Literature-screening matrix

Use one row per bibliographic work and preserve multiple provenance records separately. The minimum decision matrix is:

| Field | Allowed content / purpose |
|---|---|
| `candidate_id` | Stable local screening identifier; not a paper registry ID. |
| `title`, `authors`, `year`, `doi` | Bibliographic identity as supplied and normalized. |
| `provenance[]` | Database, cited seed, export/query, date, record ID, URL, and unsummed citation count. |
| `evidence_status` | metadata candidate / screened relevant / full text acquired / verified full text / excluded-deprioritized. |
| `evidence_label` | VERIFIED FULL TEXT / METADATA ONLY / INFERENCE. |
| `system` | Layer-jamming beam, other sheet stack, leaf spring, laminate, partial-interaction beam, etc. |
| `named_reduced_model` | Exact reduced/continuum/effective model being evaluated. |
| `reference_model` | Exact discrete, layerwise, explicit-interface, or high-fidelity comparator. |
| `reference_resolves_interfaces` | yes / no / unclear, with location. |
| `interface_law` | Coulomb, regularized Coulomb, elastic connector, cohesive, viscous, mixed, unclear. |
| `normal_loading` | Vacuum pressure, imposed pressure/force, connector stiffness, contact solution, none. |
| `physical_layer_count_values` | Values tested; distinguish from robot discretization/model segments. |
| `layer_thickness_values` | Values and whether total thickness was held fixed. |
| `total_stack_thickness` | Values and control status. |
| `pressure_values` | Values and whether independently varied. |
| `load_or_curvature_values` | Values, loading path, and control status. |
| `slip_regimes` | Pre-slip / onset / progressive or partial / full / unloading / cyclic. |
| `geometry_and_boundary_conditions` | Span, thickness, supports, clamp/contact/end treatment. |
| `experiment_present` | yes / no; measured outputs. |
| `calibration_data` | Parameters and data used for fitting. |
| `validation_data` | Data not used for fitting; state whether independence is demonstrated. |
| `compared_outputs` | Force, displacement, curvature, stress, slip-front position, dissipation, etc. |
| `error_metric` | Formula/name, normalization, reported values, uncertainty. |
| `tolerance_predeclared` | yes / no / unclear; value and provenance. |
| `parameter_grid` | Actual combinations tested, not just min/max. |
| `error_map_present` | yes / no; dimensionality and coverage. |
| `validity_domain_present` | yes / no; exact criterion. |
| `breakdown_boundary_present` | yes / no; boundary coordinates or equation. |
| `first_failure_mechanism` | Identified mechanism and evidence, or unresolved. |
| `four_target_elements` | Four booleans plus a count; never inferred from keywords alone. |
| `transferability_to_fixed_LJ_family` | direct / conditional / weak / none, with assumption mismatch. |
| `decision` | KILL / NARROW / ORTHOGONAL / SUPPORTING. |
| `decision_rationale` | Short falsification-centered rationale with page/equation/figure provenance. |
| `unresolved_checks` | Missing supplementary data, calibration ambiguity, inaccessible full text, etc. |

### 8.1 Minimum full-text extraction questions

For every HIGH candidate, answer:

1. What exact representation is being tested, and what is the independent reference?
2. Are individual interfaces genuinely resolved?
3. Which parameters are independently varied and which covary by construction?
4. Which data fit material/friction/contact parameters?
5. Which data test predictions after calibration?
6. What error norm and denominator are used?
7. Was the acceptance tolerance declared before examining the map?
8. Is the “boundary” an error crossing, a physical slip transition, or merely the edge of the tested range?
9. Does the paper locate why the reduced model fails?
10. Can its result transfer to vacuum-driven, ordered elastic sheets without adding a new mechanics problem?

## 9. Falsification sequence

1. **Freeze provenance.** Export each citation source separately with retrieval date, database, seed DOI/title, query, and database-specific citation count.
2. **Complete Track A first.** Reconcile the public `1/1/0` OpenAlex/Semantic Scholar snapshot with Scopus, WoS, Scholar/PoP, publisher/Crossref, and ResearchGate records. Do not infer absence from any one source.
3. **Deduplicate bibliographic works.** Use normalized DOI first, then title conflict review; preserve all source occurrences and citation counts. Do not merge solely on fuzzy title or file hash.
4. **Screen citation context.** Rank exact model implementation and validation above reviews or application mentions.
5. **Run Track B in risk order:** B8 discrete-to-continuum Coulomb friction; B3 frictional stacked sheets; B6 homogenization; B1 partial interaction; B7 asymptotic convergence; B4 leaf springs; B2 laminated beams; B5 shear-lag.
6. **Use citation chaining.** For every HIGH-threat work, screen its references and forward citations, including terminology used by the authors rather than only this protocol's vocabulary.
7. **Acquire full text only after metadata approval.** Metadata remains candidate evidence and cannot support KILL/NARROW scientific claims.
8. **Extract against the matrix.** Separate calibration, validation, error, tolerance, and parameter-boundary fields; do not collapse them into “validated.”
9. **Apply the damaging decision first.** Test KILL, then NARROW, then ORTHOGONAL/SUPPORTING. Record assumption mismatches rather than dismissing adjacent work by field name.
10. **Stop on falsification.** If one verified paper satisfies all four elements and transfers directly, halt gap-defense work and prepare a formal adversarial adjudication. Do not keep searching for supportive exceptions.

## 10. Search-family and global stop conditions

The family-specific stop conditions in Section 5 prevent premature termination. The whole search stops under one of these conditions:

### Immediate KILL stop

Stop and escalate for adjudication as soon as verified full text establishes all four target elements for the named model/fixed family, or establishes a general criterion whose specialization is mechanically routine. One paper is sufficient.

### NARROW stop

Stop and reformulate only if the union of verified studies covers all four elements but splits them across incompatible models or assumptions, leaving one precisely identified coupling unresolved. The surviving question must name that coupling; it cannot remain the original broad four-axis map.

### Saturation stop without a kill

Track A must be exhaustively exported for 2025–2026. Track B reaches provisional saturation only when:

- all eight search families and their synonym branches have been run in at least two scholarly indexes;
- all HIGH-threat candidates have been backward- and forward-chained;
- two consecutive 20-record relevance-ranked batches per family yield no new eligible model family or validation criterion;
- unresolved inaccessible full texts are listed explicitly; and
- citation alerts remain configured for the three rapidly aging 2025 seeds.

Saturation means no further candidate was found under the protocol. It does not prove novelty.

## 11. Adversarial failure checks

The following apparent successes do **not** kill the gap and must not be misclassified:

- A slip-transition threshold such as onset of sliding is not a model-breakdown boundary unless tied to prediction error.
- A statement that a continuum assumption applies for “many layers” is not a finite-layer-count validity boundary without a defined error and tolerance.
- A continuum-versus-FEA plot is not a continuum-versus-discrete validation unless the FEA resolves the relevant layers/interfaces.
- An experiment is not independent validation when the same curve supplies all fitted parameters.
- Variation of sheet thickness at fixed stack height is not automatically independent variation of layer count; both quantities and controls must be recorded.
- A maximum error reported at a few selected points is not a parameter-domain map.
- The edge of the tested pressure/load range is not a breakdown boundary.
- A general homogenization theorem is not automatically transferable if it assumes perfect bonding, linear interface springs, infinitesimal deformation, or rate-independent monotonic loading unlike the target family.
- A controller's tracking error is not mechanics-model error.
- A review can identify a kill candidate but cannot substitute for auditing the primary paper.

## 12. Deliverable from the search round

The completed search should produce:

1. a deduplicated, provenance-preserving candidate set;
2. the screening matrix in Section 8;
3. full-text audits for every potential KILL and HIGH-threat NARROW candidate;
4. a compact evidence table showing the four target elements independently;
5. a final adversarial finding of KILL, NARROW, ORTHOGONAL, or SUPPORTING for each paper; and
6. a round-level conclusion that either identifies the already-solved result or states the narrowest residual question without claiming novelty.

## 13. Current unresolved evidence gaps

- Scopus and Web of Science forward-citation exports for all three seeds have not yet been obtained.
- A reproducible Google Scholar/Publish or Perish forward-citation export has not yet been obtained.
- The `A3` citation disagreement—OpenAlex zero versus ResearchGate one—has not been resolved against the citing article's reference list.
- The Cheng et al. review has not been screened as a bibliography map against every cited primary mechanics paper.
- No adjacent-mechanics search family in Section 5 has yet been executed under this protocol.
- No newly identified metadata candidate has been upgraded to verified full-text evidence by this planning task.

These gaps are reasons to execute the search, not evidence that the surviving question is novel.

## 14. Provenance used to construct this protocol

### Repository verified full text

- `data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json`.
- `data/evidence/2025-Toward a deeper understanding of layer jamming structures_7cb387b88d.json`.
- `data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json`.
- `data/evidence/2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming_1f05cf83bc.json`.
- `outputs/verification/D1-V002/adversarial_evidence_synthesis.md`.
- `outputs/verification/D1-V003/FAN_2026_MODEL_AUDIT.md`.
- `outputs/verification/D1-V003/ZHANG_2025_DEEPER_UNDERSTANDING_AUDIT.md`.

### Live metadata and publisher records consulted on 2026-09-15

- [A1 publisher article](https://ms.copernicus.org/articles/16/821/2025/)
- [A1 publisher/Crossref metrics](https://ms.copernicus.org/articles/16/821/2025/ms-16-821-2025-metrics.html)
- [A2 publisher record](https://journal.hep.com.cn/fme/EN/10.1007/s11465-025-0843-5)
- [A3 publisher record](https://doi.org/10.1016/j.taml.2025.100633)
- [Cheng et al. review](https://www.mdpi.com/2075-1702/14/5/572)
- [Chen et al. TSA paper](https://www.mdpi.com/2076-0825/15/3/154)
- OpenAlex seed and forward-citation API records for `W4416304414`, `W4413337166`, and `W4416229131`.
- Semantic Scholar Graph API DOI and citation records for all three seeds.

Citation-index records are discovery metadata. Scientific classifications in a future adjudication must be based on verified primary full text.
