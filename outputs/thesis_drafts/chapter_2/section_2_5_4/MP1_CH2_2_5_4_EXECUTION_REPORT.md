# MP1 CH2 §2.5.4 — Execution report

TASK_ID: MP1-CH2-2.5.4-RESEARCH-THESIS-DRAFT  
STATUS: PARTIAL_WITH_FINDINGS  
TARGET_SECTION: 2.5.4 — Bất định đo lường và khả năng nhận dạng tham số  
ACADEMIC_CONTEXT: Thạc sĩ Kỹ thuật Cơ khí, Khoa Cơ khí, HCMUT–VNU-HCM  
DRAFT_LANGUAGE: Vietnamese only

ROOT_MODEL_REQUESTED: GPT-6.1 SOL HIGH  
ROOT_MODEL_ACTUAL: Codex root model (model telemetry not exposed)  
WORKERS_SPAWNED: 3 bounded source workers  
WORKER_TASKS: M10 verification; M12 verification; M13 verification; root verified M15 and conducted synthesis, drafting, QA  
WORKER_MODELS_ACTUAL: M10 GPT-6.1 SOL MEDIUM; M12 GPT-6.1 SOL MEDIUM; M13 GPT-6 LUNA; root actual model telemetry not exposed  
PARALLEL_EXECUTION: Source verification workers ran in bounded parallel slots; root handled M15 and final integration

OUTLINE_BULLETS_COVERED: B01 parameter compensation; B02 wire–wire versus wire–sleeve evidence; B03 uncertainty, repeatability and detection threshold  
PAPERS_READ: M10, M12, M13, M15, plus accepted §2.5.2 baseline and WEP brief/crosswalk/matrix  
PDF_PAGES_VERIFIED: M10 pp. 1–8; M12 pp. 1–10; M13 pp. 1–13; M15 pp. 1–9; Fig. 3 range checked at 0–80 kPa and Fig. 4/6 shape-locking pressures checked at −30/80 kPa  
EVIDENCE_IDS_USED: M10-E03; M12-E02; M13-E04; M15-E04  
ADDITIONAL_ACCEPTED_METHODOLOGY_SOURCES: None

M10_REPEATS_AND_CONFIDENCE: Eight repeats are reported; Fig. 6 labels shaded bands as 95% CI. Construction method and sensor uncertainty are not reported.  
M12_PRESSURE_MEASUREMENT: Pump pressure/flow were characterized on a separate sealed pump; integrated specimen pressure was not measured directly. Negative jamming pressure was inferred from the separate no-flow calibration.  
M12_FIXED_DEFLECTION_FORCE: At 3 mm, force changes from 0.134 N to 0.743 N at −50 kPa; 5.5× is a force-at-fixed-deflection ratio.  
M13_PIECEWISE_REGRESSION: Adaptive piecewise linear fits on aligned F–δ curves identify FJ, FS, KH and KL.  
M13_CRITICAL_LOAD_INTERPRETATION: FJ and FS are global transition loads extracted by a regression rule, not direct local traction or universal friction parameters.  
M15_STIFFNESS_VALIDATION: OctRobot-I shape-locking at −30 kPa and transverse stiffness over 0–80 kPa were tested; three stiffness repeats were reported, but full internal contact states were not independently observed. The accepted matrix wording “up to 40 kPa” was checked against the PDF Fig. 3 axis and not used as the primary range statement.

PARAMETER_COMPENSATION: Conditional inference involving TiNi state/modulus, friction, normal-force transmission, sleeve and fixture compliance, packing and contact geometry.  
STRUCTURAL_IDENTIFIABILITY: Unresolved for MP1; no formal analysis was claimed.  
PRACTICAL_IDENTIFIABILITY: Unresolved; depends on finite noisy measurements and pending observable/topology choices.  
SENSITIVITY_ANALYSIS: Conditional Jacobian S_ij = ∂y_i/∂θ_j introduced without numerical matrix; local rank does not prove global uniqueness.  
REPEATABILITY: Kept source-specific: M10 eight repeats; M13 five per condition; M15 three stiffness repeats; M12 no repeat/error bars for fixed-deflection force curve.  
MEASUREMENT_UNCERTAINTY: Instrument resolution, calibration, random repeatability, specimen variability, history, pressure, temperature, processing and model discrepancy are distinguished; not all are reported by sources.  
STATISTICAL_INTERVALS: M10 CI construction unspecified; M13 reports ±1 SD and selected 95% CIs; no pooled metric or universal k = 2.  
DETECTION_THRESHOLD: Defined as a future criterion requiring observable, baseline, noise, repeatability, resolution, fit rule and decision rule; no numeric MP1 threshold.  
CALIBRATION_VS_VALIDATION: Same-data fit is separated from independent validation; M13 and M15 validation scopes are bounded.  
WIRE_WIRE_VS_WIRE_SLEEVE: Conditional proposals include bare-bundle/sleeve-controlled comparisons, sleeve-only response where meaningful, near-specimen pressure comparison, separate TiNi temperature, loading/unloading and boundary comparisons.  
MP1_ADDITIONAL_MEASUREMENT_PROPOSALS: Proposals are conceptual only; no sensors, models, rates, dimensions, benches or acceptance limits were frozen.  
MP1_PENDING_HUMAN_DECISIONS: Interface topology; normal-force proxy; TiNi state domain; primary bending metric and uncertainty criterion; SMA–piston scope.

TRACEABILITY_CATEGORY_COUNTS: SOURCE_GROUNDED=12; INFERENCE=4; AUTHOR_DERIVATION=3; AUTHOR_PROPOSAL=2; PENDING_HUMAN_DECISION=1
TRACEABILITY_RECORDS: 22
EVIDENCE_ID_NORMALIZATION: T001 normalized from “M10 / [1]” to canonical M10-E03; all 22 rows audited; no additional Evidence IDs created.
AUTHOR_PROPOSAL_CLAIMS: 2  
AUTHOR_DERIVATION_RECORDS: 3
TERMINOLOGY_CSV_ENTRIES: 20
TERMINOLOGY_DOCX_ENTRIES: 20
GLOSSARY_CLOSURE: PASS; all 20 unique terminology entries are present once in the DOCX glossary.
TERMINOLOGY_RECORDS: 20  
TOTAL_TRACEABILITY_RECORDS: 22

CROSS_STUDY_SYNTHESIS: The four studies are compared by observable, independent input, architecture, pressure location, loading mode, repetition/statistics, fitted/model-derived parameters, validation scope and contact-state observability. Their results are not pooled.  
TABLES: One five-column scientific comparison table and one three-column editorial glossary table.  
EDITABLE_OMML_EQUATIONS: None. The conditional sensitivity expression uses editable Word-native subscript runs; no numerical matrix or additional equation was added.  
CITATIONS: IEEE provisional order [1] Liu 2021, [2] Huynh 2022, [3] Zhang and Yao 2026, [4] Yi, Fan and Liu 2024; all four DOI identities retained.  
TERMINOLOGY_ENTRIES: 20

TABLE_CAPTION_PAGINATION: PASS_STATIC_KEEP_WITH_NEXT; caption remains above and attached to the five-row scientific table.
VIETNAMESE_TERMINOLOGY: PASS_TARGETED_REMEDIATION; core manuscript terms are Vietnamese, with parenthetical English only at first use where needed.
SENSITIVITY_NOTATION: PASS_WORD_NATIVE_SUBSCRIPTS; i and j are editable Word-native subscript runs in y_i, θ_j and S_ij.
SCIENTIFIC_CONTENT_PRESERVED: PASS; no source claim, parameter boundary, pressure range, statistical limitation or pending MP1 decision was changed.
M15_PRESSURE_RANGE: Fig. 3 remains 0–80 kPa.
M10_CI_LIMITATION: 95% CI construction remains unreported.
M12_FORCE_RATIO: 5.5 remains force-at-3-mm ratio, not stiffness ratio.
M13_REGRESSION_SCOPE: Piecewise regression remains global transition extraction, not local-contact identification.

GATE_1: PASS_WITH_LIMITATIONS  
GATE_2: PASS  
GATE_3: PASS_WITH_LIMITATIONS  
GATE_4: PASS  
GATE_5: PASS_WITH_FINDINGS  
GATE_6: PASS_WITH_LIMITATIONS  
GATE_7: PARTIAL_WITH_FINDINGS

SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: NOT_VERIFIED  
MICROSOFT_WORD_VALIDATION: NOT_VERIFIED

DOCX_PATH: outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx  
TRACEABILITY_PATH: outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv  
TERMINOLOGY_PATH: outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv  
QA_REPORT_PATH: outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md  
EXECUTION_REPORT_PATH: outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md

UNRESOLVED_LIMITATIONS: M10 CI construction and sensor uncertainty are unreported; M12 integrated pressure and repeatability are unreported; M13 is a single-prototype effective-parameter study; M15 does not observe all internal contact states; MP1 topology, observable and calibration/validation split are pending; visual Word rendering was unavailable.  
NEXT_ACTION: Supervisor/human approval of the five MP1 decisions, then define a model-specific identifiability and uncertainty plan before any protocol is frozen.
