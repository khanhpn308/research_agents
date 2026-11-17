# MP1_CH2_2_4_1 — Execution Report

TASK_ID: MP1-CH2-2.4.1-FINAL-MICRO-HOTFIX-R2  
BASELINE_TASK_ID: MP1-CH2-2.4.1-RESEARCH-THESIS-DRAFT  
STATUS: PARTIAL_WITH_FINDINGS  
TARGET_SECTION: 2.4.1 — Chuyển pha và siêu đàn hồi của TiNi  
ACADEMIC_CONTEXT: HCMUT–VNU-HCM, Thạc sĩ Kỹ thuật Cơ khí  
DRAFT_LANGUAGE: Vietnamese only

## Orchestration
ROOT synthesized and reviewed the argument. Three bounded PDF workers ran in parallel: M25 (Sol Medium), M26+M27 (Sol Medium), and M28 (Luna). The fourth source assignment was combined by necessity because the session exposes four total agent slots including ROOT; no worker identity or telemetry was fabricated. Scratch reports remained outside the final directory.

## Source use and verification
- M25 / M25-E02, E04, E06, E11: physical PDF pp.2–15; model description pp.3–5; validation pp.6–8; SME/optimization pp.6–15. DOI 10.1080/15376494.2021.1955313. Online publication year verified as 2021; issue metadata is 2022, explaining the local filename.
- M26 / M26-E01, E03, E04: physical PDF pp.1–18; abstract pp.1–2; specimen/DSC pp.3–4; methods pp.5–7; results pp.8–17. DOI 10.1016/j.ijsolstr.2013.03.013.
- M27 / M27-E02, E08, E13, E16, E24: physical PDF pp.2–18, 30, 33–34; 37 physical pages verified. DOI 10.1016/j.ijsolstr.2013.03.015.
- M28 / M28-E01, E10, E15, E16: physical PDF pp.1–18; 19 pages verified. DOI 10.3390/buildings14061567.

## Scientific synthesis
The section explains phase state, stress-induced and thermal transformation, superelasticity, shape memory effect, loading/unloading branches, hysteresis, history, temperature and rate boundaries. It distinguishes material stress–strain, effective axial cable response and bending rigidity. M26/M27 supply near-isothermal experiments; M25 supplies combined constitutive/contact FE; M28 supplies the steel-experiment/NiTi-simulation boundary. No source is treated as a direct bending validation for MP1.

## Coverage matrix
| Required phenomenon | Source | Direct evidence | Conditions | Limitation | Coverage |
|---|---|---|---|---|---|
| Temperature and phase | M26, M25, M28 | phase definitions; DSC/model temperature cases | near-room-temperature tests; prescribed FE temperature | no MP1 state or full temperature sweep | PARTIAL/BOUNDED |
| Stress-induced transformation | M26, M27, M25 | plateaus/fronts; phenomenological FE | axial tension; specified model cases | not a bending law | SUPPORTED WITH LIMITS |
| Loading history | M26, M27 | shakedown, residual strain, layer sequence | repeated axial cycles | construction/material confounding | SUPPORTED WITH LIMITS |
| Rate | M26, M27, M28 | slow near-isothermal rates; low-frequency FE | source-specific rates | no general rate law | PARTIAL |
| Material hysteresis | M26, M27 | branches and cycle evolution | axial tension | not independently separated from contact | SUPPORTED WITH LIMITS |
| Contact/friction hysteresis | M25, M28 | contact included in FE; steel cyclic effects discussed | model-specific coefficients | no mechanism isolation | BOUNDED |

## Deliverables and counts
- `MP1_CH2_2_4_1_DRAFT.docx`: Vietnamese manuscript, comparison table, references and 15-entry editorial glossary.
- `MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv`: 20 claim records: 14 source-grounded, 3 inference, 2 author proposals, 1 document-coverage record.
- `MP1_CH2_2_4_1_TERMINOLOGY.csv`: 15 bilingual terminology entries.
- `MP1_CH2_2_4_1_7_GATE_REVIEW.md`: explicit seven-gate findings.
- `MP1_CH2_2_4_1_EXECUTION_REPORT.md`: this report.

## Tables, figures and equations
One six-column comparison table is included. No source figure was copied. No equation was inserted: B02 is met because the subsection does not adopt a constitutive law, and all source equations remain discussed only at the level needed to state assumptions.

## QA and document validation
DOCX was generated with Word-native paragraphs and tables, Times New Roman, A4 portrait, repeated table headers, non-splitting rows and Vietnamese Unicode. Static XML validation confirmed a readable Word document with no embedded workflow IDs in the manuscript body. LibreOffice/soffice was unavailable in the environment, so `WORD_RENDER_VALIDATION: NOT_VERIFIED`. Static XML checks confirmed the Word structure, Unicode text, tables, references and glossary; visual layout remains unverified.

## Remaining limitations
The four required papers do not identify a universal temperature dependence, a general rate law, a unique phase regime for MP1, or a separable material/contact hysteresis contribution. M26/M27 are axial tension studies; M25 and M28 include numerical assumptions. Wire geometry, packing, sleeve interaction, pressure transmission, material parameter identification and the primary bending observable remain unresolved.

NEXT_ACTION: Proceed to §2.4.2 for wire-rope geometry, interwire contact and relative sliding; do not treat this subsection as an MP1 operating-state decision or novelty claim.

## Final execution fields
ROOT_MODEL_REQUESTED: GPT-6.1 SOL HIGH  
ROOT_MODEL_ACTUAL: not exposed by the orchestration interface; no identity fabricated  
WORKERS_SPAWNED: 3 bounded workers  
WORKER_TASKS: M25; M26+M27; M28  
WORKER_MODELS_REQUESTED: Sol Medium; Sol Medium; Luna  
WORKER_MODELS_ACTUAL: not independently exposed; no identity fabricated  
PARALLEL_EXECUTION: yes, three source checks in parallel; ROOT synthesis followed

OUTLINE_BULLETS_COVERED: B01 bounded; B02 covered  
PAPERS_READ: M25, M26, M27, M28  
PDF_PAGES_VERIFIED: M25 15; M26 18; M27 37; M28 19 physical pages  
EVIDENCE_IDS_USED: M25-E02/E04/E06; M26-E01/E03/E04; M27-E02/E13/E16/E24; M28-E01/E10/E15  
ADDITIONAL_ACCEPTED_SOURCES_USED: none

TEMPERATURE_COVERAGE: PARTIAL/BOUNDED  
STRESS_TRANSFORMATION_COVERAGE: SUPPORTED_WITH_LIMITS  
LOADING_HISTORY_COVERAGE: SUPPORTED_WITH_LIMITS  
RATE_DEPENDENCE_COVERAGE: PARTIAL  
MATERIAL_HYSTERESIS_COVERAGE: SUPPORTED_WITH_LIMITS  
CONTACT_HYSTERESIS_DISTINCTION: BOUNDED; not independently identified

M25_MATERIAL_CONTACT_MODEL: 3-D phenomenological SMA + Abaqus/UMAT + interwire contact/friction; numerical only  
M26_ISOTHERMAL_TENSION: two NiTi cable constructions; slow near-isothermal tension with DIC/IR  
M27_COMPONENT_TOPOLOGY: corrected 7×7 right regular lay and 1×27 alternating multilayer; axial subcomponent tests  
M28_EXPERIMENT_NUMERICAL_BOUNDARY: steel experiments; NiTi response from FE with borrowed parameters

TECHNICAL_CLAIMS: 20 traceability records  
SOURCE_GROUNDED_CLAIMS: 14  
INFERENCE_CLAIMS: 3  
AUTHOR_PROPOSAL_CLAIMS: 2  
DOCUMENT_COVERAGE_RECORDS: 1  
CROSS_STUDY_SYNTHESIS: completed with observable and evidence-type boundaries  
TABLES: 1 comparison table + 1 editorial glossary table  
FIGURES: none  
EQUATIONS: none  
CITATIONS: 4 numbered references, all used; first-appearance order [1] M26, [2] M25, [3] M27, [4] M28  
TERMINOLOGY_ENTRIES: 15  
TERMINOLOGY_REVIEW_REQUIRED: completed; all 15 entries have source-specific attribution or explicit editorial-synthesis status

GATE_1: PARTIAL  
GATE_2: PASS  
GATE_3: PASS  
GATE_4: PASS  
GATE_5: PASS  
GATE_6: PASS  
GATE_7: PARTIAL (visual render unavailable)  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: NOT_VERIFIED

DOCX_PATH: `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx`  
TRACEABILITY_PATH: `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv`  
TERMINOLOGY_PATH: `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv`  
QA_REPORT_PATH: `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md`  
EXECUTION_REPORT_PATH: `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md`

UNRESOLVED_LIMITATIONS: MP1 temperature/phase/rate domain, wire packing/contact topology, pressure transfer, material identification, and bending observable remain open.  
NEXT_ACTION: stop after §2.4.1; §2.4.2 is the next separate section.


## R1 targeted hotfix
TASK_ID: MP1-CH2-2.4.1-TARGETED-HOTFIX-R1  
STATUS: PARTIAL_WITH_FINDINGS

CITATION_FIRST_APPEARANCE_ORDER: [1] Reedlunn Part I; [2] Vahidi et al.; [3] Reedlunn Part II; [4] Narjabadifam et al.  
REFERENCES: four entries; bibliography and comparison table remapped consistently  
DOI_CLOSURE: PASS; all four required DOI identities retained

TERMINOLOGY_ATTRIBUTION: individually reviewed; direct source support is separated from editorial synthesis  
TERMINOLOGY_ENTRIES: 15, preserved  
ACADEMIC_PROSE_CORRECTED: capitalization, final transition paragraph, DIC/IR expansion, near-isothermal/quasi-static terminology and plateau wording  
DIC_IR_TERMS: defined on first manuscript use  
TECHNICAL_CLAIMS: 14 source-grounded  
AUTHOR_PROPOSALS: 2  
DOCUMENT_COVERAGE: 1

M27_TOPOLOGY: preserved corrected 7×7 and 1×27 topology  
M28_EXPERIMENT_NUMERICAL_BOUNDARY: preserved steel-experiment/NiTi-simulation distinction  
B01_EVIDENCE_LIMITATION: preserved; no universal rate law, complete temperature parameters, MP1 transformation range or independent material/contact hysteresis separation

GATE_1: PARTIAL  
GATE_2: PASS  
GATE_3: PASS  
GATE_4: PASS  
GATE_5: PASS  
GATE_6: PASS  
GATE_7: PARTIAL (visual render unavailable)  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: NOT_VERIFIED

FILES_CHANGED: all five existing §2.4.1 deliverables only  
UNRESOLVED_LIMITATIONS: unchanged; MP1 temperature/phase/rate domain, contact topology, pressure transfer, material identification and bending observable remain open  
NEXT_ACTION: stop after targeted corrections; no new literature search or section expansion

## R2 — Final micro hotfix
TASK_ID: MP1-CH2-2.4.1-FINAL-MICRO-HOTFIX-R2  
STATUS: PARTIAL_WITH_FINDINGS  
REFERENCE_4_PAGINATION: đã đặt keep_together cho toàn bộ đoạn [4]; chưa kết xuất độc lập trong R2. Diagnostic render bốn trang là thông tin do người dùng cung cấp.  
UMAT_TERMINOLOGY: chương trình con vật liệu do người dùng định nghĩa (UMAT)  
CITATION_INTEGRITY: PASS; bốn DOI và thứ tự [1] M26, [2] M25, [3] M27, [4] M28 giữ nguyên  
TRACEABILITY_RECORDS: 20 (14 SOURCE_GROUNDED, 3 INFERENCE, 2 AUTHOR_PROPOSAL, 1 DOCUMENT_COVERAGE)  
TERMINOLOGY_ENTRIES: 15; CSV không đổi  
GATE_1: PARTIAL — giới hạn bằng chứng nhiệt độ/tốc độ giữ nguyên  
GATE_7: PARTIAL — chưa kiểm tra trực quan độc lập  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: NOT_VERIFIED  
FILES_CHANGED: MP1_CH2_2_4_1_DRAFT.docx; MP1_CH2_2_4_1_7_GATE_REVIEW.md; MP1_CH2_2_4_1_EXECUTION_REPORT.md  
NEXT_ACTION: dừng sau hai hiệu chỉnh; kiểm tra trực quan độc lập khi có renderer.

Validation: ZIP hợp lệ; bảng Word-native, hàng tiêu đề lặp và hàng không tách trang được bảo toàn. Đối chiếu XML xác nhận chỉ cụm từ UMAT và thuộc tính keepLines của tài liệu [4] thay đổi; mọi phần khác của DOCX không đổi. Không thay đổi số liệu, locator, topology M27, ranh giới thí nghiệm thép/mô phỏng NiTi M28 hoặc claim khoa học. Hai CSV giữ nguyên.
