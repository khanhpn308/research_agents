# MP1 CH2 §2.5.4 — 7 gate review

**TASK_ID:** MP1-CH2-2.5.4-RESEARCH-THESIS-DRAFT  
**STATUS:** `PARTIAL_WITH_FINDINGS`  
**TARGET_SECTION:** 2.5.4 — Bất định đo lường và khả năng nhận dạng tham số  
**Evidence status:** Four mandatory PDFs were read in full for the retained claims. Direct source findings, inference, author derivation, proposals and pending decisions are separated in the traceability CSV.


## Traceability and editorial hotfix reconciliation

The CSV was checked directly: `SOURCE_GROUNDED=12`, `INFERENCE=4`, `AUTHOR_DERIVATION=3`, `AUTHOR_PROPOSAL=2`, `PENDING_HUMAN_DECISION=1`, total `22`. T001 now uses canonical `M10-E03`; the provisional citation `[1]` remains manuscript-only. Non-source rows retain descriptive non-ID text and no Evidence IDs were invented.

The DOCX glossary now contains all 20 unique terminology records exactly once, with the complete definitions and readable source attribution. The scientific table retains four source rows, and its caption paragraph has `keep_with_next` set so the caption follows the table to the next page when needed.

## Gate 1 — Outline compliance: PASS_WITH_LIMITATIONS

- B01 addresses compensation among TiNi modulus/state, friction, normal force, sleeve and fixture compliance.
- B02 gives conditional controlled comparisons and added measurements for wire–wire versus wire–sleeve contributions.
- B03 distinguishes uncertainty, repeatability, statistical intervals, model discrepancy and detection threshold.
- No MP1 topology, primary observable, Bench A/B, sensor, calibration procedure or acceptance threshold is frozen.
- No unfinished §2.5.3 output was used.

**Finding:** the subsection deliberately leaves the primary MP1 bending metric and control topology for human approval.

## Gate 2 — Claim traceability: PASS

M10-E03, M12-E02, M13-E04 and M15-E04 are mapped to original PDF locators. Every quantitative source claim in the draft has a traceability record. Formal MP1 identifiability is not attributed to any source.

## Gate 3 — Original PDF and method verification: PASS_WITH_LIMITATIONS

- M10 repeats, first-1-mm stiffness definition, equivalent modulus assumptions and 95% CI wording were checked at PDF pp. 3–5.
- M12 separate pump characterization, pressure-location limitation, negative/positive pressure paths and 3-mm force values were checked at PDF pp. 2–10.
- M13 700 fibers, 0–300 kPa, five repeats, piecewise regression, parameter extraction and validation limits were checked at PDF pp. 7–11.
- M15 OctRobot-I shape locking at −30 kPa, Fig. 3 transverse-stiffness range 0–80 kPa, three repeats and the lumped-pressure assumption were checked at PDF pp. 3–9; the accepted matrix wording “up to 40 kPa” was reconciled against the figure.

**Finding:** M10 does not state how its 95% CI was constructed; the draft preserves that limitation.

## Gate 4 — Scientific synthesis: PASS

The studies are compared by đại lượng quan sát, pressure location, loading mode, repetition/statistics, fitted parameter and validation scope. Global structural response is separated from local contact state. CI, SD, repeat count and model discrepancy are not pooled.

## Gate 5 — Mechanical and identifiability limits: PASS_WITH_FINDINGS

Material/effective stiffness, friction coefficient/normal force, source pressure/specimen pressure/local traction and sleeve/fixture compliance remain distinct. Structural and practical identifiability are defined as unresolved MP1 questions. No numerical threshold or universal pressure–stiffness law is introduced.

**Finding:** a global curve can constrain a structural response, but the precise identifiability result remains model-dependent and pending the five human decisions.

## Gate 6 — Citation and statistical integrity: PASS_WITH_LIMITATIONS

The four DOI identities and first-appearance order [1]–[4] are reconciled across body, table, glossary and references. The draft does not call M12's 5.5× force ratio a stiffness ratio, does not call M10's CI an expanded uncertainty, and does not treat repeated cycles as independent specimens.

**Finding:** the source papers use different statistical outputs; no common uncertainty metric is defensible.

## Gate 7 — Vietnamese MSc and DOCX quality: PARTIAL_WITH_FINDINGS

Vietnamese academic prose, a five-column comparison table, four references and a complete 20-entry three-column glossary are included. The caption is kept with the scientific table by paragraph-level `keep_with_next`. The DOCX is editable, A4 portrait, Times New Roman, and has repeated table headers and non-splitting rows. ZIP/XML integrity and text-level structure checks passed.

`WORD_RENDER_VALIDATION: NOT_VERIFIED` because no DOCX renderer was available in the environment.  
`MICROSOFT_WORD_VALIDATION: NOT_VERIFIED` because Microsoft Word was not run.

## Dedicated findings

### Parameter compensation

The strongest risk is compensation between effective TiNi stiffness, friction, normal-force transmission, sleeve/fixture compliance and packing/contact geometry. This is a conditional model inference, not an MP1 result.

### Structural and practical identifiability

Neither property is formally established for MP1. A rank or condition analysis would require an approved model, input set and observable set.

### Repeatability and intervals

M10 reports eight repeats and 95% CI without construction details; M13 reports five repeats, ±1 SD and selected 95% CIs; M15 reports three stiffness repeats; M12 gives no repeat/error bars for the fixed-deflection force curve. These results remain source-specific.

### Detection threshold

No numerical threshold is invented. The decision rule must state the observable, baseline, noise, repeatability, resolution, fit criterion and decision threshold after MP1's primary metric is approved.

### Model discrepancy

M13 reports pressure-dependent dispersion; the relative contributions of dính–trượt, pressure transmission, specimen geometry and model inadequacy are not separately quantified. M10 and M15 use simplifying pressure/contact assumptions. These are reasons to separate model discrepancy from instrument noise.

### Sensitivity notation

The local definition uses editable Word-native subscripts for y_i, θ_j and S_ij. Its interpretation remains conditional on the selected model, observation set, measurement weighting and estimation procedure.

### Pending MP1 decisions

Topology and reaction surfaces; normal-force measurement/proxy; TiNi temperature/phase/rate/history domain; primary bending metric and uncertainty rule; SMA–piston scope. These remain pending human decisions.

## Seven-gate result

`PARTIAL_WITH_FINDINGS` is the appropriate status. Scientific traceability and synthesis are ready for supervisor review. Visual Word acceptance and the final MP1 measurement choices remain open.
