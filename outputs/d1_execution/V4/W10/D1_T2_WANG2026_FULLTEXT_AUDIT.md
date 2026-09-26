# D1-T2-P1 — Wang et al. 2026 full-text evidence packet

**Task:** controlled W10/W11 provenance remediation. **Successor W10 disposition:** `PARTIAL_OVERLAP`. **Evidence status:** `VERIFIED_FULL_TEXT`. **Authority limit:** this packet does not assign K1–K9 verdicts, decide D1 novelty, clear HG-06/HG-09, or authorize W12.

## Research question and source identity

**[REPOSITORY_CANONICAL_STATE]** The narrowed NC-04 question asks whether a reduced continuum layer-jamming model M, an interface-resolved reference R, and independent experiment E have already been combined to map accepted and breakdown regions and their mechanisms. The frozen K definitions remain in `outputs/d1_execution/V4/S09/D1_K_CRITERIA_REGISTER.json`; this is source material for later W12 evaluation.

**[FACT_FROM_FULL_TEXT]** Qinyu Wang, Peng Feng, Bo Wu, Mingrui Teng, Kaspar Jansen, Charun Bao (2026), “Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction,” *Materials & Design 268 (2026) 116573*, DOI [10.1016/j.matdes.2026.116573](https://doi.org/10.1016/j.matdes.2026.116573). The complete title, author list, journal and DOI occur on PDF p. 1. Local source: `data/inbox/2026-Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction.pdf`. SHA-256: `f77bc7b7d605e57e4bb7e11e468223ce7f670dc4e06072fd1ed99bb27062c5ca`. `pdfinfo` reports 17 pages; all pages were inspected.

**[REPOSITORY_CANONICAL_STATE]** Historical `D1-TH-015`, `D1-UT-001`, and `D1-SEARCH-W10-002` described T2 as metadata/abstract-only, unresolved, and blocking at the time of W10. They remain unchanged. This packet and its reconciliation file record the later transition to a page-grounded full-text audit.

## Audit method and evidence labels

**[FACT_FROM_FULL_TEXT]** The 17-page local PDF was checked by SHA-256 and `pdfinfo`, then extracted page by page with `pdftotext -layout`. The locators below use printed PDF page numbers. Equations, figures and tables are named only when visible in the source. The audit covers §§1–5 and Appendix A, including the model, pressure/layer/support/load tests, discrepancy discussion and source limitations.

**[UNRESOLVED]** The request specifies GPT-6 Sol High. The runtime does not expose a verifiable exact model identifier to this audit, so the artifacts record it as the requested model and leave actual model identity unverified.

`FACT_FROM_FULL_TEXT` records a statement supported by a PDF locator. `REPOSITORY_CANONICAL_STATE` records the repository’s historical or frozen state. `SCIENTIFIC_INFERENCE` is this audit’s interpretation, including bounded absence findings. `UNRESOLVED` means the inspected source does not settle the specified detail. Evidence IDs below are the cross-reference keys used in the JSON packet.

## Page-grounded evidence

| ID | Class | PDF page / locator | Source-grounded statement or bounded audit finding | D1 threat role (SCIENTIFIC_INFERENCE) |
|---|---|---|---|---|
| E01 | `FACT_FROM_FULL_TEXT` | pp. 2–3, §1.3 | The stated contributions are system integration, layer-stiffness selection, pressure/layer/loading experiments, cyclic energy dissipation, and preliminary analysis/design guidance. | Defines the paper’s research objective; no validity-map contribution is claimed. |
| E02 | `FACT_FROM_FULL_TEXT` | p. 1 Fig. 1; p. 9 Fig. 8 | Vacuum-induced interlayer friction changes coupling in an MLJ stack; the system couples an upper MLJ plate, inflatable airbeam, and optional aramid ropes. | Direct physical-system and mechanism overlap. |
| E03 | `FACT_FROM_FULL_TEXT` | p. 3 Eqs. (1)–(11) | The n-layer beam formulas give pre-slip deflection, interface shear, slip onset and load limits for simply supported and fixed-support cases. The authors expressly limit these expressions to the initial vacuum-on pre-slip stage and parameter estimation, not post-slip large-deformation prediction. | Reduced analytical M exists, but its stated prediction scope is limited. |
| E04 | `FACT_FROM_FULL_TEXT` | p. 4 §2.1.2 | The authors cite prior sequential-slip and DIC work and state that detailed nonlinear sliding evolution is not further elaborated for their application. | Post-slip interface evolution is not the studied model-validity object. |
| E05 | `FACT_FROM_FULL_TEXT` | p. 4 Fig. 3, Table 1 on p. 5 | The six material–structure regimes depend on slip-initiation, allowable, and material deformation. The figure is described as qualitative material-selection guidance with approximate rather than strict quantitative boundaries. | The regime map concerns physical/material suitability. |
| E06 | `FACT_FROM_FULL_TEXT` | p. 5 Eqs. (12)–(19), Fig. 4 | The load-enhancement expression approximates post-slip load by pre-slip load plus a full-slip contribution, neglecting the difficult-to-predict partial-slip contribution. A 20% minimum enhancement is given as an example design-benefit threshold. | Physical performance threshold must not be mistaken for model-error tolerance. |
| E07 | `FACT_FROM_FULL_TEXT` | p. 6 Fig. 5, §2.3.1 | Separate plates contain 10 or 20 SC-AF layers, each 600 × 200 mm with 1 mm TPU outer film. Dead weights and laser midspan deflection are used at vacuum settings 0, −20, −40, −60, −80, −100 kPa. Hinged/sliding and restrained-angle supports are tested. | E role: component tests span layer number, vacuum, support and load. |
| E08 | `FACT_FROM_FULL_TEXT` | p. 6 §2.3.2, Fig. 6 on p. 7 | Some intermediate points were skipped, deflections could exceed sensor range, vacuum control fluctuated within ±0.002 MPa, and sensor/control limits affected the pressure sweep. | Experimental resolution limits matter for any boundary claim. |
| E09 | `FACT_FROM_FULL_TEXT` | p. 7 Fig. 6 and Eq. (20); p. 8 Table 2 | The authors back-calculate an effective friction coefficient from stepped loading and say the exact instability-onset load cannot be identified accurately; the coefficient is an effective parameter, not a unique material constant. | Model parameters are extracted from experiment, limiting independence for model-form error isolation. |
| E10 | `FACT_FROM_FULL_TEXT` | p. 8 Fig. 7 and §2.3.3 | Hinged 20-layer plates show sudden kink/hinge-like deformation attributed to imperfections and slip redistribution; fixed-angle plates show smoother response, and pressure regulation produces history effects. | Physical slip/instability regimes and fixture effects are observed. |
| E11 | `FACT_FROM_FULL_TEXT` | p. 9 Fig. 9 and §3.2.1 | The integrated prototype is 1 m long, 200 mm wide, about 100 mm inflated height, with SC-AF layers of about 0.26 mm each and semi-cylindrical supports. | Geometry and boundary context for model–experiment comparison. |
| E12 | `FACT_FROM_FULL_TEXT` | pp. 9–11 Figs. 9–10, Table 3 | A 300 × 90 × 8 mm loading plate and four reference/vacuum/cable/combined configurations are used. Airbeam pressures are 5, 10, 20 kPa with ±1 kPa accuracy. Table 3 reports 3 mm chord stiffness and peak load. | E role and output definitions for structural response, distinct from D1 model-form errors. |
| E13 | `FACT_FROM_FULL_TEXT` | pp. 11–12 Eq. (21), Fig. 11, Table 4 | Quasi-static cycles at 5, 10, 20 kPa use imposed amplitudes 10–120 mm; the 10 mm case is excluded from loop-area analysis because of signal noise. Dissipated energy is the hysteresis-loop area; only lowest-point displacement is measured and energy values are described as conservative. | E role: cyclic physical response, not independent boundary-crossing model validation. |
| E14 | `FACT_FROM_FULL_TEXT` | pp. 13–14 Eqs. (22)–(26), Fig. 12 | The authors adapt a circular inflated-beam formulation to a rectangular airbeam through an equivalent radius and pressure-dependent reduction factor Cp; Eq. (25) is an approximate upper-bound scaling relation and Eq. (26) a deflection-trend approximation. | Additional simplified M; stated assumptions limit precision. |
| E15 | `FACT_FROM_FULL_TEXT` | p. 14 §3.3.2, Fig. 13 | Three response regimes are defined by relative MLJ sliding/yield and airbeam buckling loads: MLJ yields first, near-simultaneous mechanisms, or airbeam buckles first. The 10 kPa condition is interpreted as the most balanced coupling. | Physical failure-sequence boundary, not an accepted/rejected model-validity boundary. |
| E16 | `FACT_FROM_FULL_TEXT` | p. 15 Discussion bullet “Model–experiment comparison and interpretation”; Eqs. (8),(25) | The simplified predictions are about 27, 55, 110 N for airbeam buckling at 5, 10, 20 kPa and about 28 N for planar MLJ yield. Authors state these are significantly below experiments and that the simplified model misses load-transfer mechanisms. | Direct observed model–experiment discrepancy, with numerical examples but no defined error metric. |
| E17 | `FACT_FROM_FULL_TEXT` | p. 15 same bullet; Fig. 9 on p. 10 | The paper attributes discrepancy partly to finite distributed loading (estimated 18% effect) and chiefly to shallow curvature, semi-cylindrical-support restraint and contact confinement that create shell-like force paths. | Mechanistic hypothesis for discrepancy; strongest overlap with D1 why-model-fails question. |
| E18 | `FACT_FROM_FULL_TEXT` | p. 15 same bullet | A representative geometry-dependent factor range α≈0.2–0.5 is adopted, yielding an effective MLJ yield-load estimate of about 56–140 N; authors call the formulation conceptual rather than precise predictive and say advanced shell/cross-section/post-buckling models are needed. | Explicit model limitation; factor is not an independently validated interface-resolved reference. |
| E19 | `FACT_FROM_FULL_TEXT` | p. 15 Discussion bullet “Experimental setup and stiffness measurement” | The authors note pneumatic-control limits, a single repeatedly loaded prototype with gradual stiffness degradation, and complex low-pressure hysteresis. | Uncertainty and repeatability limitations. |
| E20 | `FACT_FROM_FULL_TEXT` | pp. 16–17 Eqs. (A1)–(A10) | TPU outer-membrane modifications to pre-slip deflection, interface shear and sliding limits are derived. | Clarifies analytical model scope; not a full-layer contact reference. |
| E21 | `SCIENTIFIC_INFERENCE` | PDF pp. 1–17; §§2.1–2.3, 3.2–3.3, 4, Appendix A inspected | No independent higher-fidelity, interface-resolved numerical reference or M-versus-R quantitative comparison is reported in the inspected full text. | Missing R role for D1-equivalent workflow. |
| E22 | `SCIENTIFIC_INFERENCE` | PDF pp. 1–17; especially p. 5 §2.2.2, p. 14 §3.3.2, p. 15 §4 | No output-specific model-form error metric, predeclared model-error acceptance tolerance, or deliberately sampled both-side model-validity boundary is reported. The p. 5 20% example is a design-benefit threshold. | Separates physical and model validity criteria. |
| E23 | `UNRESOLVED` | p. 9 §3.2.1 | The precise numeric layer count used in each integrated airbeam test is not explicit in the inspected description; do not transfer the 10/20-layer plate-test counts to the integrated prototype. | Prevents invented operating-domain metadata. |
| E24 | `REPOSITORY_CANONICAL_STATE` | D1_PRIOR_ART_THREAT_MATRIX.json#D1-TH-015; D1_UNRESOLVED_THREAT_REGISTER.json#D1-UT-001; D1_SEARCH_DECISION_LOG.json#D1-SEARCH-W10-002 | The original T2 disposition is metadata/abstract-only, unresolved and blocking at the time of W10. | Preserves the historical state-at-time. |

## Required T2 role analysis

**1. Model role — [FACT_FROM_FULL_TEXT, E03–E06, E14, E20].** The paper develops pre-slip n-layer beam expressions for deflection, interface shear and first sliding load (p. 3, Eqs. 1–11), a deliberately simplified post-slip load-enhancement approximation (pp. 4–5, Eqs. 12–19), and inflated-airbeam scaling/trend expressions (pp. 13–14, Eqs. 22–26). The TPU-covered beam variants are in Appendix A (pp. 16–17, Eqs. A1–A10). It explicitly limits the early beam expressions to initial vacuum-on pre-slip parameter estimation and calls the airbeam model approximate. **[SCIENTIFIC_INFERENCE, E21]** These are M-like models, not a Zhang-M1-versus-interface-resolved-R validity study.

**2. Experiment role — [FACT_FROM_FULL_TEXT, E07–E13, E19].** Plate tests use 10 and 20 layers; vacuum settings 0 to −100 kPa in 20 kPa steps; dead weights; laser midspan deflection; and hinged/sliding versus fixed-angle end support (p. 6, Fig. 5; p. 7, Fig. 6). The integrated 1 m airbeam uses a distributed steel loading plate, semi-cylindrical end supports, lower-airbeam pressures 5/10/20 kPa, and reference/vacuum/cable/combined configurations (pp. 9–11, Figs. 9–10, Table 3). Cyclic displacement tests at the same airbeam pressures span actuator amplitudes 10–120 mm (pp. 11–12, Fig. 11, Table 4). **[UNRESOLVED, E23]** The precise integrated-airbeam layer count is not explicit in §3.2.1; the plate-test counts must not be copied into that record.

**3. Reference role — [SCIENTIFIC_INFERENCE, E21].** The paper compares simplified estimates to physical measurements. Across §§2–4 and Appendix A, the audit found no layer-by-layer/contact-resolved numerical comparator used as R and no M–R output comparison.

**4. Operating domain — [FACT_FROM_FULL_TEXT, E07, E11–E13].** The pressure, layer and boundary ranges above define the reported tests. The integrated airbeam’s vacuum reinforcement is applied chiefly at full evacuation in the reported structural comparison; the 5/10/20 kPa values refer to positive internal airbeam pressure, not vacuum setpoints. **[SCIENTIFIC_INFERENCE]** These domains overlap D1 variables but do not themselves define a model-validity region.

**5. Slip/jamming regimes — [FACT_FROM_FULL_TEXT, E04–E06, E10, E15].** Pre-slip, partial-slip and full-slip physical behavior is discussed; the material map has six qualitative design regimes (Fig. 3, Table 1). A second three-way map compares MLJ sliding/yield with airbeam buckling (p. 14, §3.3.2). Detailed post-slip evolution is not modeled here. **[SCIENTIFIC_INFERENCE, E22]** Neither physical map is an accepted/rejected region for model-form error.

**6. Error/discrepancy evidence — [FACT_FROM_FULL_TEXT, E16–E18].** The Discussion reports approximate airbeam buckling predictions of 27, 55 and 110 N at 5, 10 and 20 kPa and a planar MLJ yield estimate near 28 N, well below experimental observations. It offers an estimated 18% effect of finite distributed loading and a representative geometry factor range α≈0.2–0.5, giving about 56–140 N for the adjusted MLJ estimate. **[SCIENTIFIC_INFERENCE, E22]** These are numerical discrepancies and explanatory adjustments, without a defined output-specific model-form error function over a domain.

**7. Validity/breakdown language — [FACT_FROM_FULL_TEXT, E05, E14, E18].** The authors call Fig. 3 qualitative, Eq. 25 approximate upper-bound scaling, Eq. 26 a trend approximation, and the combined formulation conceptual rather than precisely predictive. They call for advanced shell/cross-section/post-buckling models. **[SCIENTIFIC_INFERENCE, E22]** This is explicit recognition of model limits, not a predeclared tolerance-defined boundary map.

**8. Mechanism evidence — [FACT_FROM_FULL_TEXT, E10, E17–E18].** The paper connects observed plate kinks with imperfections/slip redistribution and explains integrated-model mismatch through curvature, finite loading area, semi-cylindrical support restraint, contact confinement and shell-like force paths. **[SCIENTIFIC_INFERENCE]** This explanation is plausible and material to D1, but the paper does not isolate each contribution with local interface-resolved evidence.

**9. Timing of criteria — [FACT_FROM_FULL_TEXT, E06, E15].** The illustrative 20% criterion on p. 5 concerns whether MLJ gives enough load enhancement to justify design complexity; the §3.3.2 load-order comparison concerns which physical mechanism activates first. **[SCIENTIFIC_INFERENCE, E22]** The source does not present a pre-outcome model-error tolerance or prospectively frozen accepted/rejected validity boundary. The audit cannot infer author intent beyond the paper’s documented sequence.

**10. Uncertainty and limitations — [FACT_FROM_FULL_TEXT, E08–E09, E13, E19].** Vacuum control fluctuated ±0.002 MPa; lower-airbeam pressure accuracy was ±1 kPa; stepped loads prevented exact onset identification; some points exceeded sensor range or were skipped; the 10 mm cyclic case had high noise; lowest-point displacement makes energy values conservative; and a repeatedly loaded single prototype developed gradual stiffness degradation. **[SCIENTIFIC_INFERENCE]** These constraints would complicate a quantified model-validity classification without a separate uncertainty budget.

**11. What the paper proves — [FACT_FROM_FULL_TEXT, E03, E07, E10, E12–E18].** Within its specimens and measurements, vacuum changes stiffness and collapse resistance, layer/support/pressure choices change observed response, cyclic tests show dissipation, and simple models help interpret mechanisms while displaying noticeable mismatch. “Proves” here means documented results and author analysis within this paper, not universal model validity.

**12. What the paper does not prove — [SCIENTIFIC_INFERENCE, E21–E22].** This full text does not establish an interface-resolved R benchmark, isolated output-specific model-form error, a predeclared model-acceptance tolerance, or an independent experiment designed around both sides of a predicted model-validity boundary. It does not prove D1 novel either.

**13. D1 conceptual overlap — [SCIENTIFIC_INFERENCE, E02–E03, E07, E12, E16–E18, E21–E22].** The overlap is material: same vacuum MLJ mechanism, an analytical model, pressure/layer/configuration tests, and explicit failure-of-simple-model discussion. The missing R and decision-boundary structure prevents classifying this paper as the complete NC-04 act. Geometry difference is not the deciding reason.

## Equations and symbol definitions relevant to the comparison

**[FACT_FROM_FULL_TEXT, pp. 3–5 and 13–14]** In the source’s initial pre-slip idealization, midspan deflection for a simply supported beam is `ω₀ = F L³/(48 E I)` (Eq. 1) and first sliding is set by peak interface shear equaling `μ ΔP` (Eq. 6), leading to `F_max = (4/3) n b h μ ΔP` for its stated simplified stack (Eq. 8). The p. 5 load-enhancement ratio `ΔF = F_jam,ult/F_unjam,ult − 1` (Eq. 18) is approximated in Eq. 19 after neglecting partial-slip load contribution. The integrated comparison uses an airbeam collapse estimate with pressure-dependent cross-section reduction `C_p` (Eq. 25). Here `F` is applied force, `L` span, `E` layer modulus, `I` second moment of area, `n` layer count, `b` width, `h` layer thickness, `μ` interlayer friction coefficient, and `ΔP` vacuum pressure differential; `ω₀` is midspan deflection. For the airbeam, `p` is internal positive pressure and `C_p` is a reduction factor for rectangular-section effects. These relations are the authors’ simplified physical-response models, not D1 output-error definitions.

## Q1–Q9 answers

### Q1

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E05, E15].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** The paper maps material/structural response regimes; it does not map a declared model-validity domain. **LIMITATION — [SCIENTIFIC_INFERENCE].** The physical response map may still motivate D1 operating-domain design.

### Q2

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E03, E14, E20].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** No M-to-interface-resolved-R comparison is documented. **LIMITATION — [SCIENTIFIC_INFERENCE].** This is a bounded finding about this 17-page PDF, not an assertion about unpublished work.

### Q3

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E16].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** Numerical prediction/measurement differences are discussed, but no defined output-specific model-form error over a domain is quantified. **LIMITATION — [SCIENTIFIC_INFERENCE].** The reported load numbers permit external calculations but such calculations would be our derivation, not an author metric.

### Q4

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E06, E15].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** No predeclared model-error acceptance/breakdown criterion is reported. **LIMITATION — [SCIENTIFIC_INFERENCE].** The example 20% design enhancement and physical load-crossing regimes are different criteria.

### Q5

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E07, E12, E13].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** Experiments vary pressure, layers, supports and cyclic amplitude, but do not deliberately sample both sides of a predicted model-validity boundary. **LIMITATION — [SCIENTIFIC_INFERENCE].** Physical mechanism transitions are observed and can inform future boundary sampling.

### Q6

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E16, E17, E18].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** The paper proposes plausible discrepancy mechanisms—curvature, distributed loading, contact confinement and shell-like load paths—but does not isolate them with an interface-resolved reference or local causality tests. **LIMITATION — [SCIENTIFIC_INFERENCE].** Author causal explanation is distinguished from independently demonstrated cause.

### Q7

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E03, E07, E12, E14].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** The paper contains simplified M and physical E roles, without D1-equivalent R or validity/error-map logic; a complete equivalent M→R→E workflow is not demonstrated. **LIMITATION — [SCIENTIFIC_INFERENCE].** M and E are substantive overlaps.

### Q8

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E01, E03, E07, E12, E16].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** It makes analytical modeling, parameter sweeps, and model–experiment discussion established practice in MLJ systems; it alone does not show D1’s surviving narrow scientific act is merely routine. **LIMITATION — [SCIENTIFIC_INFERENCE].** No final novelty judgment is made; W12 must evaluate the full corpus.

### Q9

**FULL_TEXT_EVIDENCE — [FACT_FROM_FULL_TEXT; E03, E05, E07, E12, E16, E17, E18].** See the page-grounded evidence table above; bounded absence findings remain labeled `SCIENTIFIC_INFERENCE`. **INTERPRETATION — [SCIENTIFIC_INFERENCE].** Conceptual overlap is material in system, slip mechanism, reduced model, experiment and failure discussion; the paper does not answer the same validity-boundary question with interface-resolved R and predeclared error criteria. **LIMITATION — [SCIENTIFIC_INFERENCE].** Different airbeam geometry alone is not the basis for distinction.

## K-test materiality for later W12

**[REPOSITORY_CANONICAL_STATE]** The names and tests are frozen in the S09 register. The table below flags relevance only. `MATERIAL_FOR_Kx` is not a K verdict, and every final K verdict remains `NOT_PERFORMED` in this task.

| K test | Materiality | Evidence | Why it matters |
|---|---|---|---|
| K1 | `MATERIAL_FOR_K1` | E03, E05, E15, E22 | Reduced model and regime language; distinguish physical regimes from model validity. |
| K2 | `MATERIAL_FOR_K2` | E03, E14, E21 | M exists; no interface-resolved R comparison. |
| K3 | `MATERIAL_FOR_K3` | E16, E22 | Numerical discrepancy is reported; model-form error is not isolated. |
| K4 | `MATERIAL_FOR_K4` | E05, E06, E15, E22 | Physical boundaries and example benefit threshold need timing/role separation. |
| K5 | `MATERIAL_FOR_K5` | E07, E12, E13, E22 | Substantial experiments, without both-side model-validity sampling. |
| K6 | `MATERIAL_FOR_K6` | E10, E16, E17, E18 | Discussion supplies mechanistic hypotheses for discrepancy. |
| K7 | `MATERIAL_FOR_K7` | E03, E12, E21 | M and E overlap; R and validity workflow absent in inspected PDF. |
| K8 | `MATERIAL_FOR_K8` | E01, E07, E12, E16 | Analytical/experimental steps are precedented; full scientific act unresolved to W12. |
| K9 | `MATERIAL_FOR_K9` | E02, E03, E16, E17, E21, E22 | Conceptual equivalence must weigh substantial system/mechanism overlap and missing R/validity elements. |

## Disposition, provenance and remaining gaps

**[SCIENTIFIC_INFERENCE]** `PARTIAL_OVERLAP` is the W10 source disposition. The model, experiments and discrepancy discussion are important enough to carry into W12, especially for conceptual equivalence. The inspected paper does not document the full narrowed M→R→E validity/breakdown workflow. This is neither a K1–K9 verdict nor a novelty verdict.

**[REPOSITORY_CANONICAL_STATE]** The historical W10 record remains `METADATA_ABSTRACT_ONLY_UNRESOLVED`. The append-only reconciliation is `D1_T2_WANG2026_THREAT_RECONCILIATION.json`; W11 identity/locator QA is `../W11/D1_T2_WANG2026_PROVENANCE_REVIEW.json`; review-003 routing is `../W11/D1_T2_WANG2026_REVIEW_ROUTING.json`. The old search decision and threat IDs are retained. HG-06 and HG-09 remain blocked; W12 remains unauthorized.

**[UNRESOLVED]** The exact integrated prototype layer count is not stated in the inspected §3.2.1 description. This audit also does not have raw experiment data or independent uncertainty/reference outputs needed to compute a defensible model-form error map. Human review of D1-REVIEW-003 is pending.

## References

**[FACT_FROM_FULL_TEXT]** Wang, Q., Feng, P., Wu, B., Teng, M., Jansen, K., & Bao, C. (2026). Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction. *Materials & Design, 268*, 116573. [10.1016/j.matdes.2026.116573](https://doi.org/10.1016/j.matdes.2026.116573). Source of all PDF facts above: local 17-page PDF at SHA-256 `f77bc7b7d605e57e4bb7e11e468223ce7f670dc4e06072fd1ed99bb27062c5ca`.

**[REPOSITORY_CANONICAL_STATE]** Repository comparison and historical provenance: W09 `D1_NOVELTY_CANDIDATE_REGISTER.json` (NC-04); S09 `D1_K_CRITERIA_REGISTER.json`; historical W10 `D1_PRIOR_ART_THREAT_MATRIX.json` (D1-TH-015), `D1_UNRESOLVED_THREAT_REGISTER.json` (D1-UT-001), and `D1_SEARCH_DECISION_LOG.json` (D1-SEARCH-W10-002); W11 `D1_HUMAN_REVIEW_CLEARANCE.json` (D1-REVIEW-003).

**AI assistance disclosure — [REPOSITORY_CANONICAL_STATE].** This source audit and prose were prepared with AI assistance; source identity, hash, page text, and locators were checked against the local PDF. The scientific inferences remain subject to human review.
