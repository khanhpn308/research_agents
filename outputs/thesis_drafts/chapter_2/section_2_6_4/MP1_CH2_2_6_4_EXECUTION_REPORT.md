# Báo cáo thực thi — §2.6.4

TASK_ID: MP1-CH2-2.6.4-RESEARCH-THESIS-DRAFT
STATUS: COMPLETED_WITH_DOCUMENTED_LIMITATIONS
OFFICIAL_HEADING: 2.6.4. Câu hỏi và tiêu chí chuyển sang Chương 3–4
WORKSPACE: /home/khanh/projects/mechanical-research-agents
BRANCH: main
HEAD: e66bb2f2339006e763cd60687cfc24680b945d97
REPORT_TIME_UTC: 2026-10-20T00:25:56.840048+00:00

ROOT_MODEL_REQUESTED: GPT-6.1 Sol High
ROOT_MODEL_ACTUAL: NOT_EXPOSED
WORKER_MODELS_REQUESTED: Sol Medium hoặc Luna, tùy nhiệm vụ
WORKER_MODELS_ACTUAL: NOT_VERIFIED_BACKEND
WORKERS_USED: 3 agents distinct, reused within task; dispatch selector is not backend telemetry.
REVIEW_AUTHORITY: SELF_REVIEW_ONLY
INDEPENDENT_ACCEPTANCE: REQUIRED_AFTER_DELIVERY; NOT_PERFORMED_BY_THIS_SESSION
AUTHOR_APPROVAL_STATUS: HUMAN_APPROVAL_PENDING

ROOT phê duyệt synthesis, trực tiếp viết và dựng DOCX; không dispatch worker soạn/định dạng riêng. Các worker kiểm nguồn/phản chứng/thuật ngữ/QA trong cùng nhiệm vụ; không quyết định bằng đa số và không khởi động Chương3–4.

## Phạm vi và preflight

Đã đọc AGENTS.md và các ngữ cảnh theo thứ tự docs/README.md; docs/project/PROJECT_HANDOFF_CURRENT.md; docs/project/RESEARCH_STATE.md; docs/project/research_state.json; docs/project/RESEARCH_LOG.md; docs/literature/LITERATURE_STRATEGY.md; docs/operations/KNOWN_ISSUES.md. Trạng thái D1/P1 lịch sử không ghi đè corpus/tiểu mục MP1 canonical. Không sửa scientific state.

ORIGINAL_OUTLINE_FILE: /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf
ORIGINAL_OUTLINE_SHA256: 18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e
ORIGINAL_OUTLINE_PHYSICAL_PAGE: 15; ROOT trực tiếp xem ảnh và đọc text.
OUTLINE_BULLETS: 3
READINESS_STATUS: BOUNDED_WRITING_READY
WEP_SOURCE_MATRIX_ROWS_FOR_264: 0
WEP_CITATION_CROSSWALK_ROWS_FOR_264: 0
WEP_FIGURE_TABLE_EQUATION_CANDIDATES_FOR_264: 0

Ba bullet Crosswalk là yêu cầu phương pháp nội bộ, không cần journal direct support giả. Source set được ROOT chọn theo các luận điểm thực sự dùng và nền tảng WEP/P3; không biến nguồn của tiểu mục khác thành binding264 có sẵn. Readiness cho phép viết đề xuất có điều kiện, không nghiệm thu thiết kế, source transfer hoặc kết quả MP1.

SCOPE/OUTLINE-01: bản data/LR-FORMATED-rewrite.docx có cấu trúc/tên mục/RQ khác PDF chính thức; nhiệm vụ dùng đúng PDF canonical và WEP. Không âm thầm hòa giải hay renumber. Tên §264 hiện khớp PDF15.

## Khôi phục sau mất scratch — giới hạn audit được công bố

Scratch cũ /tmp/mp1-264-077i5iye không còn khi tiếp tục. Chưa có final264 để ghi đè. Đã tạo scratch riêng và chạy lại snapshot, hashes, source workers và render; không dựa vào packet/render cũ đã mất. Manifest418inputs lưu trong accepted263 report được phân tích lại:418/418 khớp hiện tại. Raw git snapshot của chặng264 trước mất scratch không còn; regression byte-level dùng snapshot mới của lần tiếp tục này, không tuyên bố đã tái dựng byte-level toàn chặng cũ.

INPUT_CHECKSUM_STATUS: 423/423 inputs đã snapshot lúc tiếp tục giữ nguyên; 2notes được nhận diện bổ sung giữ nguyên từ mốc hash bổ sung đến cuối.
LATE_NOTES_BEFORE_FIRST_READ_HASH: NOT_VERIFIED (2notes đã mở trước khi nhận diện bổ sung; không hồi tố gọi pre-read hash).
INPUT_ATIME_METADATA_PRESERVATION: NOT_VERIFIED; không dùng touch/chmod hoặc tái xuất nguồn. Chỉ xác minh nội dung SHA-256; không tuyên bố kiểm atime.

## Các số lượng đếm trực tiếp từ bản cuối

SOURCE_PAPERS: 6 (M13, M16, M26, M31, M34, M38; gồm5journal papers và1GUM)
VERIFIED_PDFS: 7 (6content sources+M28 hỗ trợ metadata; trang chọn lọc ROOT kiểm trực tiếp)
ADDITIONAL_CONTEXT_PDF: M25, workerB đã mở; không dùng trongWord/claim/reference, không cộng vào7PDF phục vụtruyvết.
TOTAL_DISTINCT_REOPENED_CANONICAL_SCIENTIFIC_PDFS_INCLUDING_CONTEXT: 8 (7ROOT-selected used/support +1WORKER_REPORTED context)
UNVERIFIED_USED_PDFS: 0; không đồng nghĩa full-paper independent verification.
EVIDENCE_IDS: 19
BODY_PARAGRAPHS: 14
BODY_CLAIM_UNITS: 47
CLAIM_RECORDS: 57 (47body+10glossary)
TRACEABILITY_COLUMNS: 63 (53inherited263 +10new264)
TERMINOLOGY_ENTRIES: 10
GLOSSARY_ENTRIES: 10
REFERENCES: 6
UNIQUE_DOIS: 5 (GUM khôngDOI)
CITATION_OCCURRENCES: 12 =10body+2glossary; bibliography labels không đếm.
SCIENTIFIC_TABLES: 0
GLOSSARY_TABLES: 1
FIGURES: 0
OMML_EQUATIONS: 0
DOCX_ZIP_XML_STATUS: PASS (16XML/rels parsed; ZIPCRC pass)
UNRESOLVED_ANCHORS: 0
GLOSSARY_MISMATCHES: 0
DOCX_FINAL_SHA256: 607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45

SOURCE_GROUNDED_CLAIM không đồng nghĩa kết quả MP1; GUM method và calibration có nhãn riêng. INFERENCE gồm tổng hợp/định nghĩa biên tập gắn nguồn, không được nâng vì loại bằng chứng của bài gốc. Không đếm yêu cầu người viết thành thực nghiệm.

```json
{
  "CLAIM_CATEGORY_COUNTS": {
    "AUTHOR_PROPOSAL": 38,
    "INFERENCE": 10,
    "SOURCE_GROUNDED_CLAIM": 6,
    "PENDING_HUMAN_DECISION": 3
  },
  "EVIDENCE_CLASS_COUNTS": {
    "AUTHOR_PROPOSAL": 38,
    "CROSS_STUDY_INFERENCE": 10,
    "EXPERIMENTALLY_DEMONSTRATED": 4,
    "METHODOLOGY_GUIDE": 1,
    "PENDING_HUMAN_DECISION": 3,
    "EXPERIMENTALLY_DEMONSTRATED;CALIBRATION_SUPPORTED": 1
  },
  "SOURCE_ROLE_COUNTS": {
    "CONTEXT_ONLY": 39,
    "DIRECT_SUPPORT": 5,
    "COMPARATOR": 7,
    "METHODOLOGY": 6
  },
  "EVIDENCE_IDS_USED": [
    "M13-E01",
    "M13-E04",
    "M13-E06",
    "M16-E02",
    "M16-E04",
    "M16-E06",
    "M26-E01",
    "M26-E04",
    "M26-E07",
    "M31-E03",
    "M31-E06",
    "M31-E07",
    "M34-E02",
    "M34-E07",
    "M34-E08",
    "M34-E09",
    "M38-E01",
    "M38-E02",
    "M38-E03"
  ]
}
```

## Đội kiểm tra thực sự sử dụng

```json
[
  {
    "agent": "/root/gap_sources",
    "role": "A: M13/M31/M16 source verification; reused bounded static QA",
    "dispatch_selector": "gpt-6.1-sol",
    "dispatch_effort": "medium",
    "actual_backend": "NOT_VERIFIED_BACKEND"
  },
  {
    "agent": "/root/gap_counterevidence",
    "role": "B: M26/M34 and M28 metadata, M25 context; reused critical draft review",
    "dispatch_selector": "gpt-6.1-sol",
    "dispatch_effort": "medium",
    "actual_backend": "NOT_VERIFIED_BACKEND"
  },
  {
    "agent": "/root/gap_p3_audit",
    "role": "C: outline/WEP/P3/WP-E,12predecessor gap records,RQ andterminology; targeted closure",
    "dispatch_selector": "gpt-6.1-sol",
    "dispatch_effort": "medium",
    "actual_backend": "NOT_VERIFIED_BACKEND"
  }
]
```

## WEP_FILES_READ

```json
[
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md"
]
```

## P3_FILES_READ và WP-E

```json
[
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_CROSS_PAPER_CLAIMS.csv"
]
```

## B01_BENCH_A_COVERAGE / B02_BENCH_B_COVERAGE / B03_READINESS_GATE_COVERAGE

B01: COVERED_AS_CONDITIONAL_REQUIREMENTS.
B02: COVERED_AS_CONDITIONAL_REQUIREMENTS.
B03: COVERED_AS_PENDING_READINESS_CONDITIONS.

Không bullet nào là kết quả thực nghiệm đã đạt.

```json
[
  {
    "outline_bullet": "B01",
    "exact_original": "Bench A phải xác định pressure-only response, repeatability, pressure-transfer proxy và các metric M–κ.",
    "word_location": "P02–P06; P10; glossary rows1–6",
    "mechanical_question": "Áp suất gần mẫu → đáp ứng uốn trong miền xác định? Lặp lại và proxy có nghĩa gì?",
    "required_evidence": "Lịch sử áp suất, trạng thái vật liệu, tải/biên, M–κ và độ không đảm bảo; đại lượng đo/suy rõ.",
    "support_role": "M13, M31, M26 comparator; M38 methodology; yêu cầu PDF/WEP.",
    "observable_or_inference": "Áp suất nguồn/gần mẫu; lực/chuyển vị/độ cong nếu được phê duyệt; proxy không là local traction.",
    "dependency": "Hình học/giao diện/nhiệt-pha-lịch sử tải/mô hình đo chờ khóa.",
    "conclusion_scope": "Baseline có điều kiện, không nhận dạng duy nhất tiếp xúc hay loại trừ chuyển pha."
  },
  {
    "outline_bullet": "B02",
    "exact_original": "Bench B phải xác định response của SMA–piston độc lập và so sánh với Bench A ở cùng áp suất gần mẫu.",
    "word_location": "P07–P10; glossary rows7–8",
    "mechanical_question": "Nguồn hoạt động thế nào và hai hệ có tương thích ở cùng áp suất gần mẫu không?",
    "required_evidence": "Đặc trưng riêng nguồn trước; sau đó dữ liệu so sánh dưới điều kiện tương ứng; không phải thiết bị đã vận hành.",
    "support_role": "M34 comparator SMA→pressure; M16 comparator calibration/control; PDF/WEP yêu cầu.",
    "observable_or_inference": "Lực–hành trình–nhiệt–áp suất–thời gian cần cân nhắc; không phải danh sách kênh đo bắt buộc.",
    "dependency": "Tách tĩnh/lịch sử p(t), nhiệt mẫu/nguồn, biên, compliance/rò nếu đáng kể.",
    "conclusion_scope": "Không từ một chỉ số áp suất suy tương đương; không gán cơ chế mới cho residual."
  },
  {
    "outline_bullet": "B03",
    "exact_original": "Chỉ chuyển sang phần tích hợp khi geometry, interface, sensor placement, uncertainty và stop criteria đã được khóa.",
    "word_location": "P11–P14; glossary rows9–10",
    "mechanical_question": "Khi nào sẵn sàng thực hiện, so sánh, và đủ bằng chứng kết luận?",
    "required_evidence": "Phê duyệt hình học/giao diện/vị trí-vai trò đo/mô hình bất định/tiêu chí dừng trước tích hợp nghiên cứu.",
    "support_role": "PDF/WEP/P3 project requirement; M38 hỗ trợ mô hình đo, không chuẩn chấp nhận MP1.",
    "observable_or_inference": "Hồ sơ lựa chọn/mô hình phép đo/tiêu chí và dữ liệu đủ tương ứng; chưa đặt ngưỡng.",
    "dependency": "Cả năm nhóm quyết định mở; đủ vận hành không tự đủ so sánh/kết luận.",
    "conclusion_scope": "Cho phép kết quả chưa đủ dữ liệu; không zero-effect hay novelty proof."
  }
]
```

## P3_STATUS_PRESERVATION

H0b: NOT_FALSIFIED_LIVE_COMPETITOR. H1: INSUFFICIENT_EVIDENCE. G00 đóng; G01–G08 có điều kiện; G09 internal prerequisite; G10 chưa thiết lập; G11 không được dùng novelty. Không đổi canonical hoặc nâng local263statuses. Đã đọc12gap-adjudication records trong263; nguyên tắc và trạng thái được đối chiếu vớiP3.

```json
{
  "canonical_hypotheses": {
    "H0a": "REFUTED_IN_TRANSFORMATION_REGIME",
    "H0b": "NOT_FALSIFIED_LIVE_COMPETITOR",
    "H1": "INSUFFICIENT_EVIDENCE",
    "source": {
      "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md",
      "line": 7,
      "text_anchor": "## Canonical and candidate hypotheses"
    },
    "reconciliation": {
      "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md",
      "line": 22,
      "text_anchor": "## Classification reconciliation"
    },
    "boundaries": "No status update; H0a restricted verdict does not prove H1; H0b remains live and H1 is not required thesis success."
  },
  "canonical_gap_statuses_unchanged": [
    {
      "gap_id": "G00",
      "classification": "SUPPORTED_WITHIN_REVIEWED_CORPUS",
      "status": "CLOSED_AS_GENERAL_MECHANISM; MP1 transfer remains open",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 2,
        "key": "G00"
      }
    },
    {
      "gap_id": "G01",
      "classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "OPEN SYSTEM-IDENTIFICATION QUESTION",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 3,
        "key": "G01"
      }
    },
    {
      "gap_id": "G02",
      "classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "OPEN SYSTEM-IDENTIFICATION QUESTION",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 4,
        "key": "G02"
      }
    },
    {
      "gap_id": "G03",
      "classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "OPEN BOUNDED EMPIRICAL CHARACTERIZATION",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 5,
        "key": "G03"
      }
    },
    {
      "gap_id": "G04",
      "classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "OPEN ENGINEERING/SYSTEM-IDENTIFICATION QUESTION",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 6,
        "key": "G04"
      }
    },
    {
      "gap_id": "G05",
      "classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "OPEN ATTRIBUTION/REPEATABILITY QUESTION",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 7,
        "key": "G05"
      }
    },
    {
      "gap_id": "G06",
      "classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "OPEN BOUNDED MODEL-DISCRIMINATION QUESTION",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 8,
        "key": "G06"
      }
    },
    {
      "gap_id": "G07",
      "classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "OPEN IDENTIFIABILITY GATE",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 9,
        "key": "G07"
      }
    },
    {
      "gap_id": "G08",
      "classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "OPEN SYSTEM-CALIBRATION QUESTION",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 10,
        "key": "G08"
      }
    },
    {
      "gap_id": "G09",
      "classification": "OUT_OF_SCOPE",
      "status": "PROJECT PREREQUISITE, NOT A LITERATURE GAP",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 11,
        "key": "G09"
      }
    },
    {
      "gap_id": "G10",
      "classification": "NOT_ESTABLISHED",
      "status": "CONDITIONAL STRETCH ONLY",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 12,
        "key": "G10"
      }
    },
    {
      "gap_id": "G11",
      "classification": "NOT_ESTABLISHED",
      "status": "PROHIBITED CLAIM",
      "canonical_locator": {
        "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
        "csv_record_including_header": 13,
        "key": "G11"
      }
    }
  ],
  "predecessor_12_nested_gap_records_read": [
    {
      "p3_gap_id": "G00",
      "p3_canonical_status": "CLOSED_AS_GENERAL_MECHANISM; MP1 transfer remains open",
      "p3_canonical_classification": "SUPPORTED_WITHIN_REVIEWED_CORPUS",
      "status": "CLOSED",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Chỉ xét chuyển giao qua những gap cấu hình còn điều kiện.",
      "open_question": "Không mở lại câu hỏi cơ chế chung; câu hỏi MP1 được giới hạn ở G01–G08.",
      "competing_explanation": "Cơ học tiếp xúc và ma sát thông thường.",
      "discriminating_observation": "NOT_APPLICABLE: cơ chế đã có bằng chứng trong hệ nguồn.",
      "falsifiability_boundary": "Không dùng cấu hình khác để suy luật MP1.",
      "reason_not_novelty_proof": "Đã có prior art, nên không phải novelty.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 4,
        "claim_id": "263-C003",
        "manuscript_anchor": "Do đó, câu hỏi chỉ dừng ở việc áp suất có thể làm thay đổi độ cứng hoặc khả năng chống trượt không còn đủ để xác định khoảng trống của đề tài."
      }
    },
    {
      "p3_gap_id": "G11",
      "p3_canonical_status": "PROHIBITED CLAIM",
      "p3_canonical_classification": "NOT_ESTABLISHED",
      "status": "NOT_A_RESEARCH_GAP",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Chỉ đặc trưng/kiểm chứng trong miền cấu hìnhMP1.",
      "open_question": "NOT_APPLICABLE: không phát biểu gapchung hoặc tínhmớituyệtđối.",
      "competing_explanation": "Cơhọccontact/friction/geometryhiệnhành.",
      "discriminating_observation": "NOT_APPLICABLEcho noveltyproof; dữliệuMP1 chỉ hỗ trợ phạmvicụthể.",
      "falsifiability_boundary": "Không ngoại suy từ9nguồn đã đối chứng sang sự vắng mặt toàn ngành.",
      "reason_not_novelty_proof": "Priorart đã bao phủ cơ chếchung; khácgeometry/material/actuator khôngđủ.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 4,
        "claim_id": "263-C003",
        "manuscript_anchor": "Do đó, câu hỏi chỉ dừng ở việc áp suất có thể làm thay đổi độ cứng hoặc khả năng chống trượt không còn đủ để xác định khoảng trống của đề tài."
      }
    },
    {
      "p3_gap_id": "G03",
      "p3_canonical_status": "OPEN BOUNDED EMPIRICAL CHARACTERIZATION",
      "p3_canonical_classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "CONDITIONAL_OPEN",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Định nghĩa B/M–κ hoặcK, geometry, tải, biên, miền nhiệt/lịch sử.",
      "open_question": "Biểu diễn uốn nào đủ trong cấu hình/miền xét và ở đâu sai lệch được phân biệt?",
      "competing_explanation": "Mô hình giảm bậc kế thừa với trạng thái và điều kiện biên thích hợp.",
      "discriminating_observation": "Mô men/độ cong hoặc lực/độ võng có mô hình quy đổi, nhánh tải, điều kiện áp và bất định.",
      "falsifiability_boundary": "Chưa biết phạm vi khi metric/biên chưa chọn; không coi cận nguồn là cận MP1.",
      "reason_not_novelty_proof": "Đặc trưng cấu hình và miền hợp lệ không tự là luật mới.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 5,
        "claim_id": "263-C004",
        "manuscript_anchor": "Khoảng trống làm việc được giới hạn ở khả năng xây dựng và kiểm tra mối liên hệ giữa áp suất gần mẫu, trạng thái tiếp xúc theo từng giao diện, đáp ứng mô men–độ cong và sai lệch dự đoán trong một cấu hình bó dây TiNi xác định."
      }
    },
    {
      "p3_gap_id": "G01",
      "p3_canonical_status": "OPEN SYSTEM-IDENTIFICATION QUESTION",
      "p3_canonical_classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "CONDITIONAL_OPEN",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Xác định geometry/giao diện/reaction và đầu vào áp gần mẫu.",
      "open_question": "Có thể ràng buộc tải pháp tuyến hữu hiệu đủ để dự đoán uốn tới mức nào?",
      "competing_explanation": "H0b; sai khác do truyền áp, sleeve/packing hoặc tham số ma sát.",
      "discriminating_observation": "Áp gần mẫu, lực cản độc lập, chuyển vị tương đối và ràng buộc cân bằng/contact phù hợp.",
      "falsifiability_boundary": "Nếu chỉ đo áp và globalcurve, chưa phân biệt trường pháp tuyến/hệ số ma sát; không nói bất khả nguyên lý.",
      "reason_not_novelty_proof": "Vấn đề nhận dạng theo cấu hình, không chứng minh vắng mặt toàn lĩnh vực.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 11,
        "claim_id": "263-C010",
        "manuscript_anchor": "Hai cách quan sát này bổ sung cho nhau, song số đo áp suất và lực kéo dây chưa tự xác định phân bố ứng suất pháp tuyến hoặc hệ số ma sát riêng tại tiếp xúc dây–dây của MP1."
      }
    },
    {
      "p3_gap_id": "G09",
      "p3_canonical_status": "PROJECT PREREQUISITE, NOT A LITERATURE GAP",
      "p3_canonical_classification": "OUT_OF_SCOPE",
      "status": "NOT_A_RESEARCH_GAP",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Phê duyệt tiết diện/giao diện, phản lực/bao trước kết luận cơ học.",
      "open_question": "NOT_APPLICABLE: quyết định thiết kế, không câu hỏi gapđã chứng minh.",
      "competing_explanation": "NOT_APPLICABLE: chưa định nghĩa hệ để so mô hình.",
      "discriminating_observation": "Xác định cấu hình và hướng lực; không đặt giao thức thí nghiệm ở mục này.",
      "falsifiability_boundary": "Thiếu cấu hình thì không chốt diễn giải/tham số, không suy literatureabsence.",
      "reason_not_novelty_proof": "Humanchoice không phải khoảng trống tri thức công bố.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 13,
        "claim_id": "263-C012",
        "manuscript_anchor": "Việc chọn giao diện dây–dây, dây–ống bao hay tổ hợp cả hai là điều kiện xác định bài toán, chưa phải một khoảng trống của tài liệu."
      }
    },
    {
      "p3_gap_id": "G02",
      "p3_canonical_status": "OPEN SYSTEM-IDENTIFICATION QUESTION",
      "p3_canonical_classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "ALREADY_PARTIALLY_ADDRESSED",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Giao diện và trạng thái assembledcontact phải được xác định; so cùng miền tải/nhiệt.",
      "open_question": "Thay đổi nhánh uốn có đi cùng trượt tại giao diện nào, hay do bao/gá chuyển động?",
      "competing_explanation": "H0b; lực cản cuối, chuyển động bao hoặc packing.",
      "discriminating_observation": "Chuyển vị tương đối, lực cản giao diện, chuyển động bao/gá, đồng thời với đáp ứng tổng thể.",
      "falsifiability_boundary": "Chỉ globalcurve không chứng minh giao diện chi phối; phép đo rời có thể không tái hiện assembledstate.",
      "reason_not_novelty_proof": "Đã giải quyết một phần ở kiến trúc khác, chuyển giao vẫn phải kiểm tra.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 14,
        "claim_id": "263-C013",
        "manuscript_anchor": "Sau lựa chọn đó, câu hỏi cơ học mới là sự thay đổi nhánh uốn có đi cùng trượt tại giao diện được xét, hay còn có thể được giải thích bởi chuyển động đầu mẫu, độ mềm của ống bao và tái sắp xếp bó."
      }
    },
    {
      "p3_gap_id": "G08",
      "p3_canonical_status": "OPEN SYSTEM-CALIBRATION QUESTION",
      "p3_canonical_classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "CONDITIONAL_OPEN",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Geometry/biên/reaction được xác định; đưa bất địnhnhiễu cấu hình vào miền diễn giải.",
      "open_question": "Thay đổi nhánh có thể phân biệt với chuyển động đầu mẫu/sleeve/packing tới đâu?",
      "competing_explanation": "Cơ họccontacthiệnhành với điều kiệnbiên/compliance đúng.",
      "discriminating_observation": "Chuyển độngbao/gá, geometry và tươngđốitrượt cùng dữ liệu tổng thể.",
      "falsifiability_boundary": "Không có correctionbiênphổquát hoặc attribution khi nuisancechưa ràngbuộc.",
      "reason_not_novelty_proof": "Một geometrykhác khôngtựtạo câu hỏi mới hoặc novelty.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 14,
        "claim_id": "263-C013",
        "manuscript_anchor": "Sau lựa chọn đó, câu hỏi cơ học mới là sự thay đổi nhánh uốn có đi cùng trượt tại giao diện được xét, hay còn có thể được giải thích bởi chuyển động đầu mẫu, độ mềm của ống bao và tái sắp xếp bó."
      }
    },
    {
      "p3_gap_id": "G05",
      "p3_canonical_status": "OPEN ATTRIBUTION/REPEATABILITY QUESTION",
      "p3_canonical_classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "CONDITIONAL_OPEN",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Cùng mẫu/miềnphase,T,rate,history và quan sát đủ cho claim.",
      "open_question": "Dữ liệu có phân biệt nguyên nhân đổi nhánh/vòngtrễ/độtrôi qua chu trình hay không?",
      "competing_explanation": "Chuyển pha thông thường, ma sát, packing, thermalhistory và wear.",
      "discriminating_observation": "Thông tin vật liệu/nhiệt, tải–dỡ tải, tương đối trượt và histories có ràng buộc.",
      "falsifiability_boundary": "Global loop có thể đủ đặc trưng tổng thể nhưng không unique loss partition; không ép phân chia đầy đủ.",
      "reason_not_novelty_proof": "Cơ chế riêng đã có, vấn đề còn là attribution có điều kiện.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 23,
        "claim_id": "263-C022",
        "manuscript_anchor": "Câu hỏi có điều kiện là liệu thông tin trạng thái vật liệu, nhiệt độ và trượt tương đối có phân biệt được các giải thích về thay đổi nhánh và độ trôi qua chu trình trong cùng miền tải hay không."
      }
    },
    {
      "p3_gap_id": "G06",
      "p3_canonical_status": "OPEN BOUNDED MODEL-DISCRIMINATION QUESTION",
      "p3_canonical_classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "ALREADY_PARTIALLY_ADDRESSED",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Tham số material/contact hiệu chuẩn độc lập, modelconditions và miền đánhgiá được xác định.",
      "open_question": "Mô hình đối chứng kế thừa dự đoán dữ liệu dành riêng trong bất định hay không?",
      "competing_explanation": "H0b NOT_FALSIFIED_LIVE_COMPETITOR.",
      "discriminating_observation": "Residual dự đoán tổng thể và quan sát cục bộ nếu claim cần, với dữ liệu không dùng để điều chỉnh.",
      "falsifiability_boundary": "Fit hoặc một mô hình thất bại không bác bỏ mọi mô hình thông thường hoặc chứng minh H1.",
      "reason_not_novelty_proof": "Thành phần đã tồn tại; chỉ là câu hỏi mức đầy đủ, không nhu cầu bắt buộc lawnew.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 29,
        "claim_id": "263-C028",
        "manuscript_anchor": "Trong phán định này, mô hình dùng quan hệ cấu thành TiNi có chuyển pha đã có, tiếp xúc ma sát Coulomb và áp suất giam giữ như điều kiện biên vẫn là giải thích đối chứng cần được kiểm tra."
      }
    },
    {
      "p3_gap_id": "G04",
      "p3_canonical_status": "OPEN ENGINEERING/SYSTEM-IDENTIFICATION QUESTION",
      "p3_canonical_classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "ALREADY_PARTIALLY_ADDRESSED",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Áp gần mẫu, nhiệt và lịch sử tương thích; phạm vi nguồn do người nghiên cứu quyết định.",
      "open_question": "Đường truyền SMA–piston có để lại sai khác uốn phân biệt được với biến thiên áp/nhiệt/compliance không?",
      "competing_explanation": "H0b kèm động họcnguồn/traođổinhiệt/độmềmnguồn thông thường.",
      "discriminating_observation": "Đáp ứng áp, lực/hànhtrìnhnguồn, nhiệt/lịch sử và uốn trong điều kiện tương thích; không chọn sensor/protocol.",
      "falsifiability_boundary": "Nếu áp/nhiệt/lịch sử không match thì khác biệt không quy duy nhất cho nguồn hoặc cơ chế mới.",
      "reason_not_novelty_proof": "Tích hợp nguồn là validation/system-ID có tiền lệ, không novelty tự thân.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 34,
        "claim_id": "263-C033",
        "manuscript_anchor": "Phần cần làm rõ cho MP1 là khi áp suất gần mẫu, nhiệt độ và lịch sử tải tương thích, đường truyền SMA–piston có để lại khác biệt về đáp ứng uốn được phân biệt với biến thiên áp suất, độ mềm nguồn hoặc điều kiện nhiệt hay không."
      }
    },
    {
      "p3_gap_id": "G07",
      "p3_canonical_status": "OPEN IDENTIFIABILITY GATE",
      "p3_canonical_classification": "PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE",
      "status": "CONDITIONAL_OPEN",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Chọn metric/measurementmodel, miền, independentparameters và rule được người nghiên cứu phê duyệt.",
      "open_question": "Tập quan sát có đủ thông tin và bất định có đủ nhỏ để phân biệt mô hình trong miền xét?",
      "competing_explanation": "Parametercompensation, nhiễu/độkhôngđảmbảo, sai biên/nguồn thay vì newmechanism.",
      "discriminating_observation": "Input/response và bất định, covariance cần thiết, repeatability và khoảng prediction phù hợp.",
      "falsifiability_boundary": "GUM không cung cấp sensorcapability hay tolerance; thiếu phân biệt không là zeroeffect/impossibility.",
      "reason_not_novelty_proof": "Chuẩn phương pháp không phải dữ liệuMP1 và không là noveltyproof.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 38,
        "claim_id": "263-C037",
        "manuscript_anchor": "Trên cơ sở đó, câu hỏi nhận dạng của đề tài là liệu tập quan sát có đủ thông tin và độ không đảm bảo có đủ nhỏ so với khác biệt dự đoán để phân biệt các mô hình trong miền xét, thay vì chỉ tìm được nhiều bộ tham số cùng khớp một đáp ứng toàn cục."
      }
    },
    {
      "p3_gap_id": "G10",
      "p3_canonical_status": "CONDITIONAL STRETCH ONLY",
      "p3_canonical_classification": "NOT_ESTABLISHED",
      "status": "NOT_ESTABLISHED_IN_CORPUS",
      "status_scope": "LOCAL_DRAFT_ADJUDICATION_ONLY; NO_P3_STATUS_CHANGE",
      "transfer_condition": "Chỉ xét bổ sung sau độc lập hiệu chuẩn/kiểm chứng và residuallặp lại có thể nhận dạng.",
      "open_question": "Nếu residualcòn sau kiểm soát thì có cần xét mô tả bổ sung hay vẫn do tham số/biên/nhiệt?",
      "competing_explanation": "H0b NOT_FALSIFIED_LIVE_COMPETITOR; H1 INSUFFICIENT_EVIDENCE.",
      "discriminating_observation": "Residual được phân biệt với bất định và yếu tốnhiễu, quan sát trạng thái có thể nhận dạng nếu cần.",
      "falsifiability_boundary": "Residual hoặcH0afailure khôngtự chứng minh lawnew, fit-only term khôngđủ.",
      "reason_not_novelty_proof": "Chưa được xác lập; luận văn không cần đạt H1 để có kết quả hợp lệ.",
      "predecessor_locator": {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
        "csv_record_including_header": 42,
        "claim_id": "263-C041",
        "manuscript_anchor": "Nếu còn sai lệch lặp lại sau kiểm chứng, trước hết cần xét tham số, đường truyền áp suất, điều kiện biên và lịch sử nhiệt; sự xuất hiện sai lệch chưa tự xác lập nhu cầu về một luật ghép mới."
      }
    }
  ]
}
```

## RQ_MAPPING_STATUS

PROVISIONAL_MANY_TO_MANY; HUMAN_DECISION_PENDING. Giữ riêng5RQPDF§1.4.1physical6 và4P3groups; không gộp/xóa/renumber hoặc tuyên bố reconciliation hoàn tất.

```json
{
  "source": {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md",
    "line": 97,
    "text_anchor": "## RQ_MAPPING-01"
  },
  "mapping_preserved": {
    "status": "HUMAN_DECISION_PENDING",
    "canonical_p3_group_count": 4,
    "original_pdf_question_count": 5,
    "relation": "provisional many-to-many analytical links only",
    "rows": [
      {
        "original_pdf_rq": "RQ1",
        "topic": "interface/traction",
        "original_question": "Interface chịu tải chính là wire–wire, wire–sleeve hay cả hai, và áp suất dương làm thay đổi traction ở interface đó theo chiều nào?",
        "p3_groups": [
          "RQ2",
          "RQ4"
        ],
        "canonical_gaps": [
          "G01",
          "G02",
          "G07",
          "G08"
        ],
        "prerequisites": [
          "G09"
        ],
        "original_locator": {
          "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
          "physical_page": 6,
          "section": "1.4.1"
        },
        "mapping_status": "PROVISIONAL_ANALYTICAL_MANY_TO_MANY; HUMAN_DECISION_PENDING",
        "no_canonical_renumbering": true
      },
      {
        "original_pdf_rq": "RQ2",
        "topic": "external-pressure/contact-state/bending",
        "original_question": "Khi dùng nguồn áp ngoài, áp suất gần mẫu liên hệ thế nào với trạng thái stick, partial slip, full slip và các đại lượng M–κ?",
        "p3_groups": [
          "RQ1",
          "RQ2",
          "RQ4"
        ],
        "canonical_gaps": [
          "G01",
          "G02",
          "G03",
          "G06",
          "G07",
          "G08"
        ],
        "original_locator": {
          "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
          "physical_page": 6,
          "section": "1.4.1"
        },
        "mapping_status": "PROVISIONAL_ANALYTICAL_MANY_TO_MANY; HUMAN_DECISION_PENDING",
        "no_canonical_renumbering": true
      },
      {
        "original_pdf_rq": "RQ3",
        "topic": "SMA–piston source",
        "original_question": "SMA–piston tạo, duy trì và hồi áp suất với force–stroke–temperature–volume–time và độ lặp lại nào?",
        "p3_groups": [
          "RQ3",
          "RQ4"
        ],
        "canonical_gaps": [
          "G01",
          "G04",
          "G05",
          "G07"
        ],
        "original_locator": {
          "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
          "physical_page": 6,
          "section": "1.4.1"
        },
        "mapping_status": "PROVISIONAL_ANALYTICAL_MANY_TO_MANY; HUMAN_DECISION_PENDING",
        "no_canonical_renumbering": true
      },
      {
        "original_pdf_rq": "RQ4",
        "topic": "matched-pressure source equivalence",
        "original_question": "Ở cùng áp suất gần mẫu, Bench B có tái tạo được đáp ứng pressure-only của Bench A hay tạo sai khác do transient, nhiệt, rò hoặc compliance?",
        "p3_groups": [
          "RQ1",
          "RQ3",
          "RQ4"
        ],
        "canonical_gaps": [
          "G04",
          "G05",
          "G07",
          "G08"
        ],
        "original_locator": {
          "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
          "physical_page": 6,
          "section": "1.4.1"
        },
        "mapping_status": "PROVISIONAL_ANALYTICAL_MANY_TO_MANY; HUMAN_DECISION_PENDING",
        "no_canonical_renumbering": true
      },
      {
        "original_pdf_rq": "RQ5",
        "topic": "H0b reserved-data prediction",
        "original_question": "Sau khi interface và pressure-transfer map được xác nhận, mô hình H0b có dự đoán được dữ liệu held-out trong phạm vi bất định không?",
        "p3_groups": [
          "RQ1",
          "RQ2",
          "RQ3",
          "RQ4"
        ],
        "canonical_gaps": [
          "G01",
          "G02",
          "G03",
          "G05",
          "G06",
          "G07",
          "G08"
        ],
        "prerequisites": [
          "G09"
        ],
        "note": "RQ2 and RQ3 are supporting mechanism/state prerequisites rather than equivalent wording; no new coupling claim.",
        "original_locator": {
          "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
          "physical_page": 6,
          "section": "1.4.1"
        },
        "mapping_status": "PROVISIONAL_ANALYTICAL_MANY_TO_MANY; HUMAN_DECISION_PENDING",
        "no_canonical_renumbering": true
      }
    ],
    "p3_locators": [
      {
        "id": "RQ1",
        "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md",
        "line": 7
      },
      {
        "id": "RQ2",
        "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md",
        "line": 21
      },
      {
        "id": "RQ3",
        "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md",
        "line": 35
      },
      {
        "id": "RQ4",
        "file": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md",
        "line": 49
      }
    ],
    "rule": "Preserve both source namespaces and exact original PDF labels. No canonical merging, replacement, renumbering or claim of reconciliation."
  },
  "rule": "Analytical aid only. No merging, renumbering, silent replacement or canonical reconciliation."
}
```

## PENDING_HUMAN_DECISIONS

1. Hình học, topology vàcác giao diện thực tế; giao diện chi phối phải dựa bằng chứng.
2. Biểu diễn/quan sát pháp tuyến hữu hiệu hoặc proxy cùnggiới hạn suy luận.
3. Miền nhiệt độ, pha, tốc độ vàlịch sử tảiTiNi.
4. Đại lượng độ cứng chính,mô hình đo/ngân sách bất định/tiêu chí đánh giá.
5. Phạm vi đóng góp core/support vàkiểm chứngSMA–piston.

Sensor placement,geometry,interface,uncertainty,stopcriteria chưa khóa; không đưa sensor/range/dimensions/repetitions/threshold/operating protocol cuối. Quyền cho viết264 không phải phê duyệt thiết kế.

## SOURCE_VERIFICATION và metadata provenance

ROOT kiểm các đoạn dùng từPDF gốc bằngPyMuPDF; workers độc lập về phân công trong cùngphiên, không externalacceptance. M26proofxxx giữ nguyên; volume50/pages3009–3026 có nguồn thứ cấpM28PDF19ref14. IssueM13/M26/M34 chưa xác minh/không chèn. M38khôngDOI. Source correction M31tenrepeats/Dt vàM16fit provenance chỉ ghi output mới; không sửa nguồn. M13Eq4PDF3 có cảnh báo thứ nguyên (in dạng tích phân y dA có thứ nguyên m³, trong khi mô men quán tính diện tích phải có thứ nguyên m⁴); không sao chép/sửa hoặc dùng nó để bác bỏ toàn bài. EquationNotes B06/B07 liên quanEq10/11, không làmEq4hợp lệ. Không sử dụng phương trình nguồn trongWord.

```json
{
  "ROOT_DIRECTLY_VERIFIED_SELECTED_PAGES": {
    "M13": {
      "path": "data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf",
      "sha256": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
      "pages": [
        1,
        3,
        7,
        8,
        10,
        11
      ]
    },
    "M31": {
      "path": "data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf",
      "sha256": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03",
      "pages": [
        1,
        4,
        5,
        6,
        7
      ]
    },
    "M26": {
      "path": "data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf",
      "sha256": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
      "pages": [
        1,
        4,
        6,
        14,
        17
      ]
    },
    "M34": {
      "path": "data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf",
      "sha256": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
      "pages": [
        1,
        3,
        8,
        11,
        12
      ]
    },
    "M16": {
      "path": "data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf",
      "sha256": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a",
      "pages": [
        1,
        4,
        5,
        11,
        12,
        13
      ]
    },
    "M28": {
      "path": "data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf",
      "sha256": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
      "pages": [
        19
      ]
    },
    "M38": {
      "path": "data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf",
      "sha256": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c",
      "pages": [
        2,
        3,
        13,
        14,
        20,
        21,
        31,
        33,
        35,
        36,
        47
      ]
    }
  },
  "WORKER_A_REPORTED_SELECTED_PAGES": {
    "M13": [
      1,
      7,
      8,
      9,
      10,
      11,
      13
    ],
    "M31": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8
    ],
    "M16": [
      1,
      2,
      3,
      4,
      5,
      10,
      11,
      12,
      13,
      15
    ]
  },
  "WORKER_B_COMPONENT_PAGES": [
    {
      "evidence_id": "M34-E02",
      "physical_pdf_pages": [
        3
      ],
      "printed_pages": [
        "3"
      ],
      "exact_locator": "§2.1–2.2 Fig.1"
    },
    {
      "evidence_id": "M34-E04",
      "physical_pdf_pages": [
        4,
        5
      ],
      "printed_pages": [
        "4",
        "5"
      ],
      "exact_locator": "§3 Table1 and Eqs.(1)–(3)"
    },
    {
      "evidence_id": "M34-E07",
      "physical_pdf_pages": [
        8
      ],
      "printed_pages": [
        "8"
      ],
      "exact_locator": "§4.3 Characterization"
    },
    {
      "evidence_id": "M34-E08",
      "physical_pdf_pages": [
        8,
        9,
        10,
        11
      ],
      "printed_pages": [
        "8",
        "9",
        "10",
        "11"
      ],
      "exact_locator": "§5.1–5.3 Figs.5–10"
    },
    {
      "evidence_id": "M34-E09",
      "physical_pdf_pages": [
        11,
        12,
        13
      ],
      "printed_pages": [
        "11",
        "12",
        "13"
      ],
      "exact_locator": "§5.4–5.5 Figs.11–12 Table3"
    },
    {
      "evidence_id": "M26-E01",
      "physical_pdf_pages": [
        1
      ],
      "printed_pages": [
        "1 in proof"
      ],
      "exact_locator": "Abstract"
    },
    {
      "evidence_id": "M26-E03",
      "physical_pdf_pages": [
        4
      ],
      "printed_pages": [
        "4 in proof"
      ],
      "exact_locator": "§3.2 Fig.3"
    },
    {
      "evidence_id": "M26-E04",
      "physical_pdf_pages": [
        4,
        5,
        6,
        7
      ],
      "printed_pages": [
        "4",
        "5",
        "6",
        "7"
      ],
      "exact_locator": "§3.3–3.4 Figs.4–5 Table1"
    },
    {
      "evidence_id": "M26-E07",
      "physical_pdf_pages": [
        14,
        15,
        16,
        17
      ],
      "printed_pages": [
        "14",
        "15",
        "16",
        "17"
      ],
      "exact_locator": "§5.4 Figs.13–15 and §6"
    },
    {
      "evidence_id": "M25-E02",
      "physical_pdf_pages": [
        3,
        4,
        5
      ],
      "printed_pages": [
        "2",
        "3",
        "4"
      ],
      "exact_locator": "§2–4.2"
    },
    {
      "evidence_id": "M25-E06",
      "physical_pdf_pages": [
        5,
        6
      ],
      "printed_pages": [
        "4",
        "5"
      ],
      "exact_locator": "§5.1–5.2 Table3"
    }
  ],
  "M26_SECONDARY_METADATA_PROVENANCE": {
    "path": "data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf",
    "sha256": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
    "physical_pdf_page": 19,
    "printed_page": "19 of19",
    "M26_reference": 14,
    "M25_reference": 28,
    "role": "SECONDARY INTERNAL BIBLIOGRAPHIC METADATA ONLY",
    "directly_reopened_this_task": true
  },
  "references": [
    {
      "number": 1,
      "paper_id": "M13",
      "text": "[1] Shuai Zhang, Jiantao Yao, “A variable stiffness omnidirectional chain based on positive-pressure fiber jamming,” Mechanical Sciences, 17, 481–493, 2026. DOI: 10.5194/ms-17-481-2026.",
      "metadata": {
        "authors_ordered": [
          "Shuai Zhang",
          "Jiantao Yao"
        ],
        "title": "A variable stiffness omnidirectional chain based on positive-pressure fiber jamming",
        "journal": "Mechanical Sciences",
        "volume": "17",
        "issue": "NOT_REPORTED",
        "pages": "481–493",
        "year": 2026,
        "doi": "10.5194/ms-17-481-2026",
        "metadata_provenance": "Canonical PDF first and final pages reopened after environment restart. Author order, venue and printed pagination checked. Missing issue not inferred."
      }
    },
    {
      "number": 2,
      "paper_id": "M31",
      "text": "[2] Hyerim Jeon, Quang Ngoc Le, Sanghun Jeong, Sujin Jang, Hoeryong Jung, Handdeut Chang, Hardik J Pandya, Yeongjin Kim, “Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism,” IEEE Robotics and Automation Letters, 7(3), 6582–6589, 2022. DOI: 10.1109/LRA.2022.3174363.",
      "metadata": {
        "authors_ordered": [
          "Hyerim Jeon",
          "Quang Ngoc Le",
          "Sanghun Jeong",
          "Sujin Jang",
          "Hoeryong Jung",
          "Handdeut Chang",
          "Hardik J Pandya",
          "Yeongjin Kim"
        ],
        "title": "Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism",
        "journal": "IEEE Robotics and Automation Letters",
        "volume": "7",
        "issue": "3",
        "pages": "6582–6589",
        "year": 2022,
        "doi": "10.1109/LRA.2022.3174363",
        "metadata_provenance": "Canonical PDF first and final pages reopened after environment restart. Author order, venue and printed pagination checked. Missing issue not inferred."
      }
    },
    {
      "number": 3,
      "paper_id": "M26",
      "text": "[3] Benjamin Reedlunn, Samantha Daly, John Shaw, “Superelastic shape memory alloy cables: Part I – Isothermal tension experiments,” International Journal of Solids and Structures, 50, 3009–3026, 2013. DOI: 10.1016/j.ijsolstr.2013.03.013.",
      "metadata": {
        "authors_ordered": [
          "Benjamin Reedlunn",
          "Samantha Daly",
          "John Shaw"
        ],
        "journal": "International Journal of Solids and Structures",
        "year": 2013,
        "volume": 50,
        "issue": null,
        "pages": "3009–3026",
        "doi": "10.1016/j.ijsolstr.2013.03.013",
        "provenance": "Canonical PDF1 title/ordered authors/year/DOI, article-in-press proof uses xxx volume/pages. Final volume/pages verified SECONDARY INTERNAL in M28 PDF19 ref14; issue unverified.",
        "title": "Superelastic shape memory alloy cables: Part I – Isothermal tension experiments",
        "canonical_pdf_path": "data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf",
        "sha256": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
        "hash_matches_evidence": true
      }
    },
    {
      "number": 4,
      "paper_id": "M38",
      "text": "[4] Joint Committee for Guides in Metrology, “Evaluation of measurement data — Guide to the expression of uncertainty in measurement,” JCGM 100:2008, 2008 (bản hiệu chỉnh năm 2010).",
      "metadata": {
        "authors_ordered": [
          "Joint Committee for Guides in Metrology"
        ],
        "title": "Evaluation of measurement data — Guide to the expression of uncertainty in measurement",
        "year": 2008,
        "identifier": "JCGM 100:2008",
        "doi": null,
        "metadata_provenance": "Canonical PDF2 institutional authorship/PDF3 title+year; corrected version2010, not a DOI publication."
      }
    },
    {
      "number": 5,
      "paper_id": "M34",
      "text": "[5] Youssef Kotb, Islam Elgamal, Mohamed Serry, “Shape Memory Alloy Capsule Micropump for Drug Delivery Applications,” Micromachines, 12, bài 520, 2021. DOI: 10.3390/mi12050520.",
      "metadata": {
        "authors_ordered": [
          "Youssef Kotb",
          "Islam Elgamal",
          "Mohamed Serry"
        ],
        "journal": "Micromachines",
        "year": 2021,
        "volume": 12,
        "issue": null,
        "article_number": "520",
        "pages": "1–15 article-internal",
        "doi": "10.3390/mi12050520",
        "provenance": "Direct canonical PDF1 and page headers; issue unverified and not inferred from DOI.",
        "title": "Shape Memory Alloy Capsule Micropump for Drug Delivery Applications",
        "canonical_pdf_path": "data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf",
        "sha256": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
        "hash_matches_evidence": true
      }
    },
    {
      "number": 6,
      "paper_id": "M16",
      "text": "[6] Yeman Fan, Bowen Yi, Dikai Liu, “Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots,” IEEE Transactions on Control Systems Technology, 34(5), 2219–2233, 2026. DOI: 10.1109/TCST.2026.3690756.",
      "metadata": {
        "authors_ordered": [
          "Yeman Fan",
          "Bowen Yi",
          "Dikai Liu"
        ],
        "title": "Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots",
        "journal": "IEEE Transactions on Control Systems Technology",
        "volume": "34",
        "issue": "5",
        "pages": "2219–2233",
        "year": 2026,
        "doi": "10.1109/TCST.2026.3690756",
        "metadata_provenance": "Canonical PDF first and final pages reopened after environment restart. Author order, venue and printed pagination checked. Missing issue not inferred."
      }
    }
  ],
  "used_evidence_fragments": {
    "M13-E01": [
      {
        "physical_pages": [
          1
        ],
        "printed_pages": [
          "481"
        ],
        "exact_locator": "Abstract",
        "anchor": "prototype-level experimental assessment"
      }
    ],
    "M13-E04": [
      {
        "physical_pages": [
          7
        ],
        "printed_pages": [
          "487"
        ],
        "exact_locator": "4 Experimental methods; 4.1 Prototype fabrication and test setup; 4.2 Data processing and parameter extraction algorithm",
        "anchor": "700 nylon"
      },
      {
        "physical_pages": [
          8
        ],
        "printed_pages": [
          "488"
        ],
        "exact_locator": "Figs.4 and5; Section4.2 continued",
        "anchor": "Specimen geometry"
      },
      {
        "physical_pages": [
          9
        ],
        "printed_pages": [
          "489"
        ],
        "exact_locator": "4.2 continued; 5.1 Identification of material parameters; 5.2 Validation of critical load models",
        "anchor": "independent material test"
      }
    ],
    "M13-E06": [
      {
        "physical_pages": [
          10
        ],
        "printed_pages": [
          "490"
        ],
        "exact_locator": "5.2 continued, before 5.3 Pressure dependence of bending stiffness",
        "anchor": "non-uniform jamming pressure transmission"
      },
      {
        "physical_pages": [
          11
        ],
        "printed_pages": [
          "491"
        ],
        "exact_locator": "6 Conclusion",
        "anchor": "single VSOC prototype"
      }
    ],
    "M16-E02": [
      {
        "physical_pages": [
          4
        ],
        "printed_pages": [
          "2222"
        ],
        "exact_locator": "II.A continued; II.B Key Assumptions and Frictional Model With LJ",
        "anchor": "additional input"
      },
      {
        "physical_pages": [
          5
        ],
        "printed_pages": [
          "2223"
        ],
        "exact_locator": "II.B continued; Assumptions3 and4",
        "anchor": "uniformly distributed"
      }
    ],
    "M16-E04": [
      {
        "physical_pages": [
          10
        ],
        "printed_pages": [
          "2228"
        ],
        "exact_locator": "V. Experiments and Results, A. Test Rig; Fig.5",
        "anchor": "pressure gauge"
      },
      {
        "physical_pages": [
          11
        ],
        "printed_pages": [
          "2229"
        ],
        "exact_locator": "V.C Open-Loop Stiffening; Fig.7; V.D Parameter Identification starts",
        "anchor": "better ﬁtting performance"
      },
      {
        "physical_pages": [
          12
        ],
        "printed_pages": [
          "2230"
        ],
        "exact_locator": "V.D continued; V.E Closed-Loop Control Experiments; Fig.8; TableI",
        "anchor": "By ﬁtting the stiﬀness data"
      }
    ],
    "M16-E06": [
      {
        "physical_pages": [
          12
        ],
        "printed_pages": [
          "2230"
        ],
        "exact_locator": "V.D continued; V.E Closed-Loop Control Experiments; Fig.8; TableI",
        "anchor": "By ﬁtting the stiﬀness data"
      },
      {
        "physical_pages": [
          13
        ],
        "printed_pages": [
          "2231"
        ],
        "exact_locator": "V.E continued; Figs.9/10; TableII",
        "anchor": "closed-loop stiﬀness"
      }
    ],
    "M26-E01": [
      {
        "physical_pages": [
          1
        ],
        "printed_pages": [
          "1 in proof"
        ],
        "exact_locator": "Abstract",
        "anchors": [
          "nearly isothermal",
          "stereo digital image correlation and infrared imaging"
        ]
      }
    ],
    "M26-E04": [
      {
        "physical_pages": [
          4,
          5,
          6,
          7
        ],
        "printed_pages": [
          "4",
          "5",
          "6",
          "7"
        ],
        "exact_locator": "§3.3–3.4 Figs.4–5 Table1",
        "anchors": [
          "Temperature was monitored simultaneously",
          "laser extensometry and stereo DIC",
          "spurious strains"
        ]
      }
    ],
    "M26-E07": [
      {
        "physical_pages": [
          14,
          15,
          16,
          17
        ],
        "printed_pages": [
          "14",
          "15",
          "16",
          "17"
        ],
        "exact_locator": "§5.4 Figs.13–15 and §6",
        "anchors": [
          "We do not have DIC data for this experiment",
          "six",
          "predicted asymptotic"
        ]
      }
    ],
    "M31-E03": [
      {
        "physical_pages": [
          3
        ],
        "printed_pages": [
          "6584"
        ],
        "exact_locator": "III. Stiffness Model starts",
        "anchor": "work-energy equation"
      },
      {
        "physical_pages": [
          4
        ],
        "printed_pages": [
          "6585"
        ],
        "exact_locator": "III. Stiffness Model continued; Fig.3",
        "anchor": "cantilever beam"
      }
    ],
    "M31-E06": [
      {
        "physical_pages": [
          5
        ],
        "printed_pages": [
          "6586"
        ],
        "exact_locator": "IV. Experiment Setup and Result; A. Friction Force Characterization; Fig.4",
        "anchor": "repeated ten times"
      },
      {
        "physical_pages": [
          6
        ],
        "printed_pages": [
          "6587"
        ],
        "exact_locator": "IV.A continued; TableI; IV.B Stiffness Characterization of the Robot; TableII",
        "anchor": "slope of the resistive force"
      }
    ],
    "M31-E07": [
      {
        "physical_pages": [
          6
        ],
        "printed_pages": [
          "6587"
        ],
        "exact_locator": "IV.A continued; TableI; IV.B Stiffness Characterization of the Robot; TableII",
        "anchor": "slope of the resistive force"
      },
      {
        "physical_pages": [
          7
        ],
        "printed_pages": [
          "6588"
        ],
        "exact_locator": "IV.B continued; TableIII",
        "anchor": "modeled ﬂexural rigidity"
      }
    ],
    "M34-E02": [
      {
        "physical_pages": [
          3
        ],
        "printed_pages": [
          "3"
        ],
        "exact_locator": "§2.1–2.2 Fig.1",
        "anchors": [
          "instantaneous SMA material phase",
          "difference in force"
        ]
      }
    ],
    "M34-E07": [
      {
        "physical_pages": [
          8
        ],
        "printed_pages": [
          "8"
        ],
        "exact_locator": "§4.3 Characterization",
        "anchors": [
          "displacement, discharge, volume flow rate, static pressure head",
          "force-displacement responses"
        ]
      }
    ],
    "M34-E08": [
      {
        "physical_pages": [
          8,
          9,
          10,
          11
        ],
        "printed_pages": [
          "8",
          "9",
          "10",
          "11"
        ],
        "exact_locator": "§5.1–5.3 Figs.5–10",
        "anchors": [
          "Pump displacement vs. time",
          "Volume flow rate vs. frequency"
        ]
      }
    ],
    "M34-E09": [
      {
        "physical_pages": [
          11,
          12,
          13
        ],
        "printed_pages": [
          "11",
          "12",
          "13"
        ],
        "exact_locator": "§5.4–5.5 Figs.11–12 Table3",
        "anchors": [
          "static head pressure",
          "43 mm3",
          "6.5 kPa"
        ]
      }
    ],
    "M38-E01": [
      {
        "physical_pages": [
          13
        ],
        "printed_pages": [
          "1"
        ],
        "exact_locator": "§1 Scope",
        "anchor": "general rules"
      },
      {
        "physical_pages": [
          47
        ],
        "printed_pages": [
          "35"
        ],
        "exact_locator": "Annex B.2.15–B.2.16",
        "anchor": "same conditions of measurement",
        "ADDITIONAL_FRAGMENT_NOT_IN_ORIGINAL_RECORD": true
      }
    ],
    "M38-E02": [
      {
        "physical_pages": [
          20,
          21
        ],
        "printed_pages": [
          "8",
          "9"
        ],
        "exact_locator": "§4.1.1–4.1.3 model of measurement; Eq.(1)",
        "anchor": "mathematical model"
      },
      {
        "physical_pages": [
          14
        ],
        "printed_pages": [
          "2"
        ],
        "exact_locator": "§2.2.3 uncertainty definition",
        "ADDITIONAL_FRAGMENT_NOT_IN_ORIGINAL_RECORD": true
      }
    ],
    "M38-E03": [
      {
        "physical_pages": [
          31,
          33
        ],
        "printed_pages": [
          "19",
          "21"
        ],
        "exact_locator": "§5.1.2 and §5.2.2 covariance/correlated inputs",
        "anchor": "correlated"
      }
    ]
  }
}
```

## BASELINE_PATHS / BASELINE_SHA256_BEFORE_AFTER

36baseline/supportfiles thực tế:7file mỗiintegrated2.3/2.4/2.5 và5file mỗi261/262/263. CácDOCX261/262/263 khớp cả3hash người dùng cung cấp. 6baselineDOCX vàsupportrecords được đọc, không render/re-export baseline.

Trạng thái nghiệm thu do người dùng cung cấp:2.3ACCEPTED,2.4ACCEPTED,2.5ACCEPTED_WITH_MINOR_ERRATA,261/262/263ACCEPTED_WITH_DOCUMENTED_LIMITATIONS (USER_REPORTED). Báo cáo lịch sử263 cònghi chờnghiệmthu là trạng thái lịch sử; không sửa hoặc nâng thành review của phiên này. Haierrata2.5 đãbiết không sửa.

| Baseline/support input | SHA-256 trước | SHA-256 sau | Trạng thái |
|---|---|---|---|
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx | `bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec` | `bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv | `65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be` | `65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md | `25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034` | `25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md | `e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e` | `e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv | `eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99` | `eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv | `54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0` | `54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md | `84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed` | `84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md | `09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc` | `09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv | `3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23` | `3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md | `0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d` | `0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md | `751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70` | `751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv | `eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534` | `eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx | `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea` | `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv | `d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49` | `d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv | `a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5` | `a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md | `b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d` | `b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv | `229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1` | `229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx | `cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc` | `cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv | `70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff` | `70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md | `d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5` | `d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md | `3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2` | `3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md | `03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97` | `03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx | `983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e` | `983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv | `bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a` | `bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv | `b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c` | `b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md | `0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca` | `0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md | `e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d` | `e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx | `fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63` | `fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv | `c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237` | `c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md | `c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866` | `c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv | `ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd` | `ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md | `1d12b07ae29792e7ae547576468134926e6acefde9ccc740dd670cea084f70cd` | `1d12b07ae29792e7ae547576468134926e6acefde9ccc740dd670cea084f70cd` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv | `3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13` | `3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv | `badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d` | `badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md | `5a9b1e21647777cb2855490d42e553a92f56906dad609522cc92841c4c59a9c9` | `5a9b1e21647777cb2855490d42e553a92f56906dad609522cc92841c4c59a9c9` | UNCHANGED |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx | `5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d` | `5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d` | UNCHANGED |

BASELINES_UNCHANGED: YES (36/36 SHA-256 trực tiếp trước/sau bằng nhau).

## INPUT_SHA256_MANIFEST — các đầu vào đã snapshot

423hàng cóbefore/after; allunchanged. Gồm sources,context,WEP/P3/WP-E/baselines vàcácpre-existingdirtyfiles trongsnapshot. Không gọi sốfilehash là sốPDFđãđọc.

```json
[
  {
    "path": "/home/khanh/projects/mechanical-research-agents/.agents/skills.json",
    "before": "5a932ffcd3c3c31ebb6d0353d8a381a1f5cb3d470ab372309097a16c73e89acb",
    "after": "5a932ffcd3c3c31ebb6d0353d8a381a1f5cb3d470ab372309097a16c73e89acb"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/LR-FORMATED-rewrite.docx",
    "before": "7bff33afc673816984cbe417bcf513e2fbafd9243301de3aa37ff57c4102eee5",
    "after": "7bff33afc673816984cbe417bcf513e2fbafd9243301de3aa37ff57c4102eee5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv",
    "before": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
    "after": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv",
    "before": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
    "after": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md",
    "before": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
    "after": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md",
    "before": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
    "after": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md",
    "before": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
    "after": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv",
    "before": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
    "after": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv",
    "before": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
    "after": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md",
    "before": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
    "after": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md",
    "before": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
    "after": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md",
    "before": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
    "after": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md",
    "before": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
    "after": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md",
    "before": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
    "after": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md:Zone.Identifier",
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf",
    "before": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0",
    "after": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf",
    "before": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b",
    "after": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf",
    "before": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2",
    "after": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf",
    "before": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12",
    "after": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf",
    "before": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7",
    "after": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf",
    "before": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
    "after": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.pdf",
    "before": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5",
    "after": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt",
    "before": "f75d24bd867f9b5f9ac749f607f43f6c657f57d95517f3a7258127dac8f82db7",
    "after": "f75d24bd867f9b5f9ac749f607f43f6c657f57d95517f3a7258127dac8f82db7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf",
    "before": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933",
    "after": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt",
    "before": "32cbdee2a368ec60d02d949c36791624d4de4106778945b9ac95cd190af41db1",
    "after": "32cbdee2a368ec60d02d949c36791624d4de4106778945b9ac95cd190af41db1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf",
    "before": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
    "after": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt",
    "before": "1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db",
    "after": "1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf",
    "before": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
    "after": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt",
    "before": "413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac",
    "after": "413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf",
    "before": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827",
    "after": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt",
    "before": "5b3cbae0cb08f21b907c572a04df5a36312b08cc4c9e9701440ddbceb3421d8f",
    "after": "5b3cbae0cb08f21b907c572a04df5a36312b08cc4c9e9701440ddbceb3421d8f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf",
    "before": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
    "after": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf",
    "before": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
    "after": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt",
    "before": "ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d",
    "after": "ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf",
    "before": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807",
    "after": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt",
    "before": "1fbd2bb1fe12bf775f2c82229ab5f3a692d255fc86dc4dc60f32aea4c2676837",
    "after": "1fbd2bb1fe12bf775f2c82229ab5f3a692d255fc86dc4dc60f32aea4c2676837"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf",
    "before": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63",
    "after": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf",
    "before": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a",
    "after": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf",
    "before": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee",
    "after": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt",
    "before": "89fede501f2cd30bff4b6532d7ba4584556f8434738a67a4416d3caef3c473a7",
    "after": "89fede501f2cd30bff4b6532d7ba4584556f8434738a67a4416d3caef3c473a7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M18__2025-A continuum-based model for a layer jamming beam.pdf",
    "before": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
    "after": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M19__2025-Toward a deeper understanding of layer jamming structures.pdf",
    "before": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
    "after": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M20__2025-Continuum modeling for layer jamming structures.pdf",
    "before": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
    "after": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M21__An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf",
    "before": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752",
    "after": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf",
    "before": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe",
    "after": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M23__2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf",
    "before": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a",
    "after": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.pdf",
    "before": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
    "after": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt",
    "before": "db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2",
    "after": "db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M25__A3-2022-Mechanical response of single and double-helix.pdf",
    "before": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
    "after": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf",
    "before": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
    "after": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M27__2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf",
    "before": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
    "after": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf",
    "before": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
    "after": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M29__2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf",
    "before": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
    "after": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M30__A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf",
    "before": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
    "after": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf",
    "before": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03",
    "after": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M32__2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf",
    "before": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
    "after": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M33__2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf",
    "before": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
    "after": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf",
    "before": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
    "after": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M35__A5-Cable vibration considering internal friction.pdf",
    "before": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
    "after": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M36__2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf",
    "before": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
    "after": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M37__2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf",
    "before": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
    "after": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf",
    "before": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c",
    "after": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf",
    "before": "24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a",
    "after": "24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/MANIFEST.json",
    "before": "9d3c70e3a1f267c51fb87a77f504f6eb2e0d99d3dbd2ccc14b557aad9e017eda",
    "after": "9d3c70e3a1f267c51fb87a77f504f6eb2e0d99d3dbd2ccc14b557aad9e017eda"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/README.md",
    "before": "a82bd095dbbd8ec46c5576bec7f3870bc86d64f7748a7767d6a7306993eb4f7c",
    "after": "a82bd095dbbd8ec46c5576bec7f3870bc86d64f7748a7767d6a7306993eb4f7c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md",
    "before": "a948bd201fda61b29de142e40a95606cf47a7c83d05c2a81e7683db371e9453c",
    "after": "a948bd201fda61b29de142e40a95606cf47a7c83d05c2a81e7683db371e9453c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md",
    "before": "4dd71b45f52a0e5bb18f92c3a76064aa4e395bc4a9feee19f827d6f463140f08",
    "after": "4dd71b45f52a0e5bb18f92c3a76064aa4e395bc4a9feee19f827d6f463140f08"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md",
    "before": "e5650636b3c8858394b619bf3f06386b65a9827bdf8e73d18f777144d57d6f7c",
    "after": "e5650636b3c8858394b619bf3f06386b65a9827bdf8e73d18f777144d57d6f7c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md",
    "before": "2d26d9cbd7883442428585de82b53b320f28a275937f94d724097a61723ac166",
    "after": "2d26d9cbd7883442428585de82b53b320f28a275937f94d724097a61723ac166"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx",
    "before": "833344a5d64632ff9336832dbfccb2a8ae98dec45df046278e26d229b189ca9b",
    "after": "833344a5d64632ff9336832dbfccb2a8ae98dec45df046278e26d229b189ca9b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx",
    "before": "3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45",
    "after": "3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/project/almost done/LR-FORMATED.docx",
    "before": "a63016590d98ff10636895166307603e2b3095ee5b632a30891b71c21190986c",
    "after": "a63016590d98ff10636895166307603e2b3095ee5b632a30891b71c21190986c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md",
    "before": "af57cc6a53c38ea430b4369d6afe7df86f61956d3320d7ce3977f957f5de3145",
    "after": "af57cc6a53c38ea430b4369d6afe7df86f61956d3320d7ce3977f957f5de3145"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md",
    "before": "f53f896801113150bd83e84d6c68dd542804fc65a619ae34fd568e7f7c276a99",
    "after": "f53f896801113150bd83e84d6c68dd542804fc65a619ae34fd568e7f7c276a99"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/LR-FORMATED-rewrite-outline-de-xuat.docx",
    "before": "3053b2649293ac1841de835a15687392beef1648a5de26faf6f78b5b3d78b0e4",
    "after": "3053b2649293ac1841de835a15687392beef1648a5de26faf6f78b5b3d78b0e4"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/LR-FORMATED-rewrite.docx",
    "before": "ee5b700f8dc6701eea44dd4679519049fa95d45a299b39ed411a58793ca3652d",
    "after": "ee5b700f8dc6701eea44dd4679519049fa95d45a299b39ed411a58793ca3652d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/LR-FORMATED.docx",
    "before": "d61c30a5973f3bd2f0314bcb3df253fe1707ad4dedfeb2bf1f76a5d895eb8a1c",
    "after": "d61c30a5973f3bd2f0314bcb3df253fe1707ad4dedfeb2bf1f76a5d895eb8a1c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx",
    "before": "e41e3638abfd27d3c7b7f60c538cbecf719651d22fa8efd27da8ee2b4b52ef26",
    "after": "e41e3638abfd27d3c7b7f60c538cbecf719651d22fa8efd27da8ee2b4b52ef26"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json",
    "before": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84",
    "after": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md",
    "before": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f",
    "after": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json",
    "before": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51",
    "after": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md",
    "before": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131",
    "after": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json",
    "before": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c",
    "after": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json",
    "before": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435",
    "after": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json",
    "before": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc",
    "after": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip",
    "before": "d2128a711f4c3a2be4bb0841415f532413c462a0aeafed0b3321d7f3713194b3",
    "after": "d2128a711f4c3a2be4bb0841415f532413c462a0aeafed0b3321d7f3713194b3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL.zip",
    "before": "d33cbdddda00f38e63c2bbec38658d4c13f183b026f2442a361f2fbc2ea141af",
    "after": "d33cbdddda00f38e63c2bbec38658d4c13f183b026f2442a361f2fbc2ea141af"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv",
    "before": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
    "after": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv",
    "before": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
    "after": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md",
    "before": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
    "after": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md",
    "before": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
    "after": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md",
    "before": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
    "after": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv",
    "before": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
    "after": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv",
    "before": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
    "after": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md",
    "before": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
    "after": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md",
    "before": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
    "after": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md",
    "before": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
    "after": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md",
    "before": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
    "after": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md",
    "before": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
    "after": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/ma-tran-tong-quan-tai-lieu.docx",
    "before": "ead3fb5c00004f7444545d622760430673a7bd787c84df456d8239ad4823bfc9",
    "after": "ead3fb5c00004f7444545d622760430673a7bd787c84df456d8239ad4823bfc9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json",
    "before": "c26a9c15561b3f9c58d175f4197e074b7a833faa9533cf6f9240f302cea497a2",
    "after": "c26a9c15561b3f9c58d175f4197e074b7a833faa9533cf6f9240f302cea497a2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/~$-FORMATED-rewrite.docx",
    "before": "9e62bab38175dd43e2235fd8e880726f73509c57fb3f36fce2c7a0b3776f0dd2",
    "after": "9e62bab38175dd43e2235fd8e880726f73509c57fb3f36fce2c7a0b3776f0dd2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/literature review/~$-FORMATED.docx",
    "before": "84e28127f73d6d6e2ef9b1d4a7838978fc4dc03cb00b586b7ff687a3c39828f3",
    "after": "84e28127f73d6d6e2ef9b1d4a7838978fc4dc03cb00b586b7ff687a3c39828f3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/CLAIM_SOURCE_MAP.json",
    "before": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84",
    "after": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md",
    "before": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f",
    "after": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/HIGHLIGHT_REGISTER.json",
    "before": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51",
    "after": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip",
    "before": "6f40ffb40b5fbc3aaa381d20f28c12b87f39111faf877e046aff27326eb97de1",
    "after": "6f40ffb40b5fbc3aaa381d20f28c12b87f39111faf877e046aff27326eb97de1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json",
    "before": "45bfdd81445f9ad3c95f1fc50bb4bc9140b25d0b422ac91f23e6565074a834c3",
    "after": "45bfdd81445f9ad3c95f1fc50bb4bc9140b25d0b422ac91f23e6565074a834c3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/README.md",
    "before": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131",
    "after": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S01_search_text.txt",
    "before": "4c6b07960eec03bee4baf0582065e2cd5c3cdcaed357ee7a66c42d71e79b09a5",
    "after": "4c6b07960eec03bee4baf0582065e2cd5c3cdcaed357ee7a66c42d71e79b09a5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S02_search_text.txt",
    "before": "02f77f8e301d4045d31e7fcd579badd261c34ef8148a96519b3bb88d36f74f41",
    "after": "02f77f8e301d4045d31e7fcd579badd261c34ef8148a96519b3bb88d36f74f41"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S03_search_text.txt",
    "before": "356de27f1e83ccb27a37f1ffd9be9321ca7887db1288d45c1adc1a5cf83ca1e9",
    "after": "356de27f1e83ccb27a37f1ffd9be9321ca7887db1288d45c1adc1a5cf83ca1e9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S04_search_text.txt",
    "before": "f47ba51263ffb69505356db6455a781730d7d01ab48bfdb214e793b1d434b6cb",
    "after": "f47ba51263ffb69505356db6455a781730d7d01ab48bfdb214e793b1d434b6cb"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05a_search_text.txt",
    "before": "982911acc87b715ead5ddcafa25f73f50937f92276417358c99ae1bbb9f4b11f",
    "after": "982911acc87b715ead5ddcafa25f73f50937f92276417358c99ae1bbb9f4b11f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05b_search_text.txt",
    "before": "0938ee9bef68cc3f7f8231129e6e383871065c16595b8d46f12331326e6b1942",
    "after": "0938ee9bef68cc3f7f8231129e6e383871065c16595b8d46f12331326e6b1942"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S06_search_text.txt",
    "before": "a1fafc05606f28715e59d86fc646c5151f28501dda722056b60ffbfb289b4b63",
    "after": "a1fafc05606f28715e59d86fc646c5151f28501dda722056b60ffbfb289b4b63"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S07_search_text.txt",
    "before": "e661bd66ac3bc591d25d133ce7b5185f9290fafa2121a4ccff4c22be44ff9057",
    "after": "e661bd66ac3bc591d25d133ce7b5185f9290fafa2121a4ccff4c22be44ff9057"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S09_search_text.txt",
    "before": "9045945be238ffc81d121d178485e1fcb5bf478e0b8f6b8492c0e9dc6a7a4936",
    "after": "9045945be238ffc81d121d178485e1fcb5bf478e0b8f6b8492c0e9dc6a7a4936"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S10_search_text.txt",
    "before": "6640478481b84b7c5aa93656f82e646bf333ead8ba6afa5c612a14e93397dbb0",
    "after": "6640478481b84b7c5aa93656f82e646bf333ead8ba6afa5c612a14e93397dbb0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S11_search_text.txt",
    "before": "29ee1cd95525b8e187408d9588156039a1b3f635e9a608dd3c43a9a9167ef147",
    "after": "29ee1cd95525b8e187408d9588156039a1b3f635e9a608dd3c43a9a9167ef147"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S12_search_text.txt",
    "before": "b6e8d5f5195364f3c9fbbedfde63460bc3beac3706bd9929e5aec1d06b3bef55",
    "after": "b6e8d5f5195364f3c9fbbedfde63460bc3beac3706bd9929e5aec1d06b3bef55"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S13_search_text.txt",
    "before": "d614f809da314316213905d05e8242736841de9f01cecaf04ec9b6fe61291c2d",
    "after": "d614f809da314316213905d05e8242736841de9f01cecaf04ec9b6fe61291c2d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S15_search_text.txt",
    "before": "7f694619b4377fc61b1a00fe3435945651983296b8c5e83f47f971734f70bc2f",
    "after": "7f694619b4377fc61b1a00fe3435945651983296b8c5e83f47f971734f70bc2f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S17_search_text.txt",
    "before": "5e36642dbc07e11c2c93dfa8c50e0c33efdf80d677fa8dc98ab1f1e8d0014d8c",
    "after": "5e36642dbc07e11c2c93dfa8c50e0c33efdf80d677fa8dc98ab1f1e8d0014d8c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S18_search_text.txt",
    "before": "f83f01d5c89461a62c290e1238bdba1d0be5d566a4d10162849a72cee905c610",
    "after": "f83f01d5c89461a62c290e1238bdba1d0be5d566a4d10162849a72cee905c610"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S22_search_text.txt",
    "before": "3f86f47c7a279935989a13297c5f17eaa4a5b5c819ca1935ca96513265d6b895",
    "after": "3f86f47c7a279935989a13297c5f17eaa4a5b5c819ca1935ca96513265d6b895"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/V-W02_search_text.txt",
    "before": "7a5b5bed75fe60dc1eb36eec69f5e19c4ab5a3a9e7a1fb69b107f6e4aa61a71a",
    "after": "7a5b5bed75fe60dc1eb36eec69f5e19c4ab5a3a9e7a1fb69b107f6e4aa61a71a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/VALIDATION.json",
    "before": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c",
    "after": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py",
    "before": "d7e2b3eb9c9cb70dcf9ec6bcd4291edd683bce4220b172177a3ec0271543aed4",
    "after": "d7e2b3eb9c9cb70dcf9ec6bcd4291edd683bce4220b172177a3ec0271543aed4"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py",
    "before": "cd0bd1d5437f2e3f2f43a13d0e55abb9c3fe583bb4637256fa62314431603320",
    "after": "cd0bd1d5437f2e3f2f43a13d0e55abb9c3fe583bb4637256fa62314431603320"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curated_passages.json",
    "before": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435",
    "after": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/inputs.json",
    "before": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc",
    "after": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/package_highlights.py",
    "before": "d12846bf434cae00cdd88aa4907ab1b498b419cb600ca1500d11b470bb7fb416",
    "after": "d12846bf434cae00cdd88aa4907ab1b498b419cb600ca1500d11b470bb7fb416"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf_text_geometry.json",
    "before": "fc09e94857f1dae49ba360d749a72483513a380ea08427ed4b87620c7830a750",
    "after": "fc09e94857f1dae49ba360d749a72483513a380ea08427ed4b87620c7830a750"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/prepare_inputs.py",
    "before": "0106dbcd0cc378824724a1b5acec9e287387372aebc7a2566ca6cd13fca648a3",
    "after": "0106dbcd0cc378824724a1b5acec9e287387372aebc7a2566ca6cd13fca648a3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S01_P9.png",
    "before": "35ed651167faff4e3aa4efd2a8fc56c8adc91e2ca81eb17a05cd27a23b2979be",
    "after": "35ed651167faff4e3aa4efd2a8fc56c8adc91e2ca81eb17a05cd27a23b2979be"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S03_P9.png",
    "before": "db5a71d9a613da2e51976c5a80f7a6b9e94237506c5b2bd4b07971d69947145c",
    "after": "db5a71d9a613da2e51976c5a80f7a6b9e94237506c5b2bd4b07971d69947145c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S04_P5.png",
    "before": "0ce4fa6d45c23b437747406f90f8f62ddb640ef4cb44c0faa02cbaba1ac4d175",
    "after": "0ce4fa6d45c23b437747406f90f8f62ddb640ef4cb44c0faa02cbaba1ac4d175"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S07_P6.png",
    "before": "8080514df725ffb4dee57fe6caad48ae52a6cb5c108d2cdfed3d48317cbd740c",
    "after": "8080514df725ffb4dee57fe6caad48ae52a6cb5c108d2cdfed3d48317cbd740c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S09_P9.png",
    "before": "9e9634334a7019114182b8ff182ae197d38ec13498d3b5d936dec9b5fd3b61ec",
    "after": "9e9634334a7019114182b8ff182ae197d38ec13498d3b5d936dec9b5fd3b61ec"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S22_P71.png",
    "before": "e6d0f7e7de7fb3922397919cb5949365433f63fe78b5bbdd92c0d689d037eead",
    "after": "e6d0f7e7de7fb3922397919cb5949365433f63fe78b5bbdd92c0d689d037eead"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/LR_CITATION_MATRIX_2026-10-14.md",
    "before": "2bb833a7bbb3dc0d77521e81ca68445af0d4b455e099994ff2acde9e7c1aab2a",
    "after": "2bb833a7bbb3dc0d77521e81ca68445af0d4b455e099994ff2acde9e7c1aab2a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md",
    "before": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2",
    "after": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv",
    "before": "942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6",
    "after": "942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md",
    "before": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79",
    "after": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md",
    "before": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8",
    "after": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md",
    "before": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2",
    "after": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md",
    "before": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406",
    "after": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json",
    "before": "0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06",
    "after": "0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md",
    "before": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38",
    "after": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md",
    "before": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7",
    "after": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json",
    "before": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1",
    "after": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json",
    "before": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7",
    "after": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md",
    "before": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da",
    "after": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md",
    "before": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e",
    "after": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv",
    "before": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9",
    "after": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md",
    "before": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5",
    "after": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv",
    "before": "3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23",
    "after": "3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md",
    "before": "5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e",
    "after": "5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv",
    "before": "2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9",
    "after": "2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md",
    "before": "1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a",
    "after": "1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md",
    "before": "6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca",
    "after": "6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md",
    "before": "c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02",
    "after": "c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md",
    "before": "a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037",
    "after": "a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md",
    "before": "227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72",
    "after": "227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip",
    "before": "fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e",
    "after": "fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md",
    "before": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d",
    "after": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv",
    "before": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34",
    "after": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl",
    "before": "a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba",
    "after": "a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md",
    "before": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1",
    "after": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md",
    "before": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a",
    "after": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md",
    "before": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d",
    "after": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md",
    "before": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996",
    "after": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md",
    "before": "59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde",
    "after": "59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md",
    "before": "86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059",
    "after": "86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md",
    "before": "2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d",
    "after": "2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md",
    "before": "da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a",
    "after": "da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md",
    "before": "7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864",
    "after": "7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md",
    "before": "76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f",
    "after": "76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md",
    "before": "f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c",
    "after": "f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md",
    "before": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101",
    "after": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md",
    "before": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907",
    "after": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md",
    "before": "99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8",
    "after": "99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip",
    "before": "fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14",
    "after": "fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md",
    "before": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a",
    "after": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv",
    "before": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be",
    "after": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl",
    "before": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033",
    "after": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md",
    "before": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda",
    "after": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md",
    "before": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09",
    "after": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md",
    "before": "9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65",
    "after": "9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md",
    "before": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba",
    "after": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md",
    "before": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087",
    "after": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md",
    "before": "c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec",
    "after": "c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md",
    "before": "fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2",
    "after": "fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md",
    "before": "d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160",
    "after": "d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md",
    "before": "6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80",
    "after": "6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md",
    "before": "37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844",
    "after": "37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md",
    "before": "6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46",
    "after": "6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md",
    "before": "58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11",
    "after": "58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md",
    "before": "2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf",
    "after": "2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md",
    "before": "77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930",
    "after": "77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md",
    "before": "4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d",
    "after": "4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md",
    "before": "561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a",
    "after": "561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md",
    "before": "b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad",
    "after": "b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md",
    "before": "0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad",
    "after": "0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md",
    "before": "99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d",
    "after": "99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md",
    "before": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213",
    "after": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json",
    "before": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6",
    "after": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md",
    "before": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1",
    "after": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip",
    "before": "ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4",
    "after": "ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md",
    "before": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109",
    "after": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv",
    "before": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7",
    "after": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv",
    "before": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0",
    "after": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl",
    "before": "a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2",
    "after": "a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md",
    "before": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753",
    "after": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md",
    "before": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed",
    "after": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md",
    "before": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7",
    "after": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md",
    "before": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c",
    "after": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md",
    "before": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8",
    "after": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md",
    "before": "287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151",
    "after": "287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md",
    "before": "0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284",
    "after": "0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md",
    "before": "f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee",
    "after": "f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md",
    "before": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034",
    "after": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md",
    "before": "5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a",
    "after": "5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md",
    "before": "31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c",
    "after": "31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md",
    "before": "2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344",
    "after": "2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md",
    "before": "0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a",
    "after": "0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md",
    "before": "98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8",
    "after": "98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md",
    "before": "3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c",
    "after": "3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md",
    "before": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6",
    "after": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md",
    "before": "65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05",
    "after": "65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md",
    "before": "4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894",
    "after": "4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip",
    "before": "9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c",
    "after": "9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md",
    "before": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2",
    "after": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv",
    "before": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2",
    "after": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
    "before": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd",
    "after": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md",
    "before": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2",
    "after": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md",
    "before": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09",
    "after": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md",
    "before": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0",
    "after": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md",
    "before": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79",
    "after": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json",
    "before": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3",
    "after": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md",
    "before": "a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f",
    "after": "a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md",
    "before": "a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195",
    "after": "a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md",
    "before": "d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24",
    "after": "d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md",
    "before": "613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8",
    "after": "613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md",
    "before": "4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf",
    "after": "4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md",
    "before": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6",
    "after": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md",
    "before": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513",
    "after": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv",
    "before": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd",
    "after": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
    "before": "e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c",
    "after": "e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md",
    "before": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1",
    "after": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md",
    "before": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b",
    "after": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv",
    "before": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e",
    "after": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md",
    "before": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24",
    "after": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md",
    "before": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8",
    "after": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md",
    "before": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b",
    "after": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md",
    "before": "e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d",
    "after": "e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md",
    "before": "f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9",
    "after": "f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md",
    "before": "bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca",
    "after": "bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md",
    "before": "e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880",
    "after": "e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md",
    "before": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40",
    "after": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md",
    "before": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682",
    "after": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md",
    "before": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003",
    "after": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json",
    "before": "3bef4fb970e65913196e9772e22384dd5e7d040373afdef378eac78f81ac5b45",
    "after": "3bef4fb970e65913196e9772e22384dd5e7d040373afdef378eac78f81ac5b45"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json",
    "before": "cd99c169e1f925756746d0e49422d30fd325b7c5ffb9191175bbf8a8970a2f3e",
    "after": "cd99c169e1f925756746d0e49422d30fd325b7c5ffb9191175bbf8a8970a2f3e"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json",
    "before": "4c43ba1f67921c857f0ab50190e227b1ad7221f6a9b6f0a15f5af9ca1c7ff0e8",
    "after": "4c43ba1f67921c857f0ab50190e227b1ad7221f6a9b6f0a15f5af9ca1c7ff0e8"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json",
    "before": "5a5bc1912919a022e37f5a544be7aec25880523ded14ae4b0455125a1ac045ae",
    "after": "5a5bc1912919a022e37f5a544be7aec25880523ded14ae4b0455125a1ac045ae"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_8_CHAPTER_2_RELEASE_MANIFEST_2026-10-04.json",
    "before": "86bd644523dafbd66c4a887fdbcd4127f82986aa9d366d5c16b21255a7e56800",
    "after": "86bd644523dafbd66c4a887fdbcd4127f82986aa9d366d5c16b21255a7e56800"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_8_FINALIZATION_CHANGELOG_2026-10-04.json",
    "before": "e6690ef5f0b214935e493597ecce089f780ed198f22fcc12346ce50f7759f558",
    "after": "e6690ef5f0b214935e493597ecce089f780ed198f22fcc12346ce50f7759f558"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_8_FINAL_CITATION_REGISTER_2026-10-04.json",
    "before": "a5e7efaa88155129f27eec425caf7b83521c600e4c41d491932198aab0d8c6ed",
    "after": "a5e7efaa88155129f27eec425caf7b83521c600e4c41d491932198aab0d8c6ed"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_8_FINAL_CLAIM_TRACEABILITY_2026-10-04.json",
    "before": "c3ea4d1eddc144cf8474746c0eed87262b1a4298589ff01ddfe181f8bf968cd2",
    "after": "c3ea4d1eddc144cf8474746c0eed87262b1a4298589ff01ddfe181f8bf968cd2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_GLOSSARY_C2_3_1_REPORT_2026-10-16.md",
    "before": "25462069e0667a67ce680d3fbb3c6879a8d7959a8da3973e9a289706c9638ab3",
    "after": "25462069e0667a67ce680d3fbb3c6879a8d7959a8da3973e9a289706c9638ab3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py",
    "before": "d82086830d47d966856159e60eda1a083a65476353c5e3842866b464fcdbfad6",
    "after": "d82086830d47d966856159e60eda1a083a65476353c5e3842866b464fcdbfad6"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md",
    "before": "7c2154b025b7f260d3f4414c58e684e1a3e1289270be9e298a33557030025acf",
    "after": "7c2154b025b7f260d3f4414c58e684e1a3e1289270be9e298a33557030025acf"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/actual_docx_inventory.json",
    "before": "45d74f31bb450ea97bf235c690bf08f83cd1829fcc64a2cde5df4ca7f2d52347",
    "after": "45d74f31bb450ea97bf235c690bf08f83cd1829fcc64a2cde5df4ca7f2d52347"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/artifact_integrity_original.json",
    "before": "d72596925b96f026fdc73f37c2fdf870f30733cce5a27e916877e3c700be4c1d",
    "after": "d72596925b96f026fdc73f37c2fdf870f30733cce5a27e916877e3c700be4c1d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/citation_appearances_original.json",
    "before": "38e8809b3de36209ac614c684f57331ce6e8d38e742cfb5105a46fc11dc56120",
    "after": "38e8809b3de36209ac614c684f57331ce6e8d38e742cfb5105a46fc11dc56120"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/inspect_artifact.py",
    "before": "ac39da773a40c472040b723bc79649c01b913b6b4b0eb53dbe4b15da0cb8b21e",
    "after": "ac39da773a40c472040b723bc79649c01b913b6b4b0eb53dbe4b15da0cb8b21e"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05a_crossref.json",
    "before": "96fd249c10471dd90ed45041388c8700ff583a777a8307c6fd6dc9bba9f6e31b",
    "after": "96fd249c10471dd90ed45041388c8700ff583a777a8307c6fd6dc9bba9f6e31b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05b_crossref.json",
    "before": "d88f96fd0dc2781302fc91ecdd5575c4609ee1f002bbf1c65b44d7be43a7af0f",
    "after": "d88f96fd0dc2781302fc91ecdd5575c4609ee1f002bbf1c65b44d7be43a7af0f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S11_crossref.json",
    "before": "2058beabf11fbafc397818f2bc533cd6b70d4ca8fc94a9e57630b8845b2c34a9",
    "after": "2058beabf11fbafc397818f2bc533cd6b70d4ca8fc94a9e57630b8845b2c34a9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/V-W02_crossref.json",
    "before": "c93b664692e0e539895548d87e7ac1d50689eb09654841c89f45bb5b2d0fde7c",
    "after": "c93b664692e0e539895548d87e7ac1d50689eb09654841c89f45bb5b2d0fde7c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md",
    "before": "402f6fc7c9d279b6b0c1fb6af3d72c5d42d131eeb0d8994a61c71c21cbc902cb",
    "after": "402f6fc7c9d279b6b0c1fb6af3d72c5d42d131eeb0d8994a61c71c21cbc902cb"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx",
    "before": "6ded97f12de61cde7be319c865c3ea40cc6cbdc8d04e00cc648530ec718311a0",
    "after": "6ded97f12de61cde7be319c865c3ea40cc6cbdc8d04e00cc648530ec718311a0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md",
    "before": "91947d11eea09cac56f882936218d690458b1cbbbe431bd7f854be6a172ac9b7",
    "after": "91947d11eea09cac56f882936218d690458b1cbbbe431bd7f854be6a172ac9b7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv",
    "before": "08202df03396abf83a4d320b56bd91abface6535c0379c1b75ec0c4ff89f3649",
    "after": "08202df03396abf83a4d320b56bd91abface6535c0379c1b75ec0c4ff89f3649"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv",
    "before": "f917c23d7dc2a404dbbbfa38874ede6dd10a50fac598cf7e3cfd880fdce83a2f",
    "after": "f917c23d7dc2a404dbbbfa38874ede6dd10a50fac598cf7e3cfd880fdce83a2f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md",
    "before": "4ca60c29585ed5a364ae526397fe7120976a3912ea9342996ba105f05e56e9ba",
    "after": "4ca60c29585ed5a364ae526397fe7120976a3912ea9342996ba105f05e56e9ba"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx",
    "before": "7f614d06edca11ae573f27aeb5d277e5e7d74f3dc1d6ec9978dbe43f1795c8fb",
    "after": "7f614d06edca11ae573f27aeb5d277e5e7d74f3dc1d6ec9978dbe43f1795c8fb"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md",
    "before": "b6e59281460fcf9a88df683bebcebef1007c232ce9497da1ce3952b46402f622",
    "after": "b6e59281460fcf9a88df683bebcebef1007c232ce9497da1ce3952b46402f622"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv",
    "before": "ec210ec6bf5bd02798db60db8a9366b3981efc23a9ddff0303051d7220f2523f",
    "after": "ec210ec6bf5bd02798db60db8a9366b3981efc23a9ddff0303051d7220f2523f"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv",
    "before": "287da4a23314f4a98d0ce9a9bbd84946ec235af7fd6a147e95f02b85e81f4984",
    "after": "287da4a23314f4a98d0ce9a9bbd84946ec235af7fd6a147e95f02b85e81f4984"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md",
    "before": "557429b44c0a0dfb8036e3aa734c8bcffc04bafbfd0be6f47bda207148ff3531",
    "after": "557429b44c0a0dfb8036e3aa734c8bcffc04bafbfd0be6f47bda207148ff3531"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx",
    "before": "1727dd0eeb32da84135d094f34c443605060cfd3fa39d269d85f855ce731b563",
    "after": "1727dd0eeb32da84135d094f34c443605060cfd3fa39d269d85f855ce731b563"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md",
    "before": "757ba0ea8e15d71d2a9bbe2ba1bc2add412122ef610753b898871038a109bfc4",
    "after": "757ba0ea8e15d71d2a9bbe2ba1bc2add412122ef610753b898871038a109bfc4"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv",
    "before": "c075ca7049f5cb81ea7fe997a9f29a0d0cc07971af52594f4560d2e659991826",
    "after": "c075ca7049f5cb81ea7fe997a9f29a0d0cc07971af52594f4560d2e659991826"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv",
    "before": "d79fa7a1611883a9ad6dfb5d4f02a58622c48e7533d0efc20ea4e3bd04b3bb76",
    "after": "d79fa7a1611883a9ad6dfb5d4f02a58622c48e7533d0efc20ea4e3bd04b3bb76"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md",
    "before": "bfedc08e96e0163ce64b75a967f6327e42e49bee87dad55fcf522f9747ea22db",
    "after": "bfedc08e96e0163ce64b75a967f6327e42e49bee87dad55fcf522f9747ea22db"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx",
    "before": "38be496eb71922f7165b916ac552f9b9bcb54dbfd94dc0f635acd55372ce793d",
    "after": "38be496eb71922f7165b916ac552f9b9bcb54dbfd94dc0f635acd55372ce793d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md",
    "before": "7d3b803e0d690dacd49997861769e218186b6719f11c2337b5ebff813864bfb3",
    "after": "7d3b803e0d690dacd49997861769e218186b6719f11c2337b5ebff813864bfb3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv",
    "before": "7b3105acf012369a2c3a7ee4426ef66d457c874da38d2dd2d6fc8f518daed630",
    "after": "7b3105acf012369a2c3a7ee4426ef66d457c874da38d2dd2d6fc8f518daed630"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv",
    "before": "735c2ad438e0a2ae0c05e83483ed51b6aeba2e49e372d59dc89bf6c6d9f1c223",
    "after": "735c2ad438e0a2ae0c05e83483ed51b6aeba2e49e372d59dc89bf6c6d9f1c223"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md",
    "before": "15537e97652af58e55a85bf001a604205953111db06dafb17243f481f266eec1",
    "after": "15537e97652af58e55a85bf001a604205953111db06dafb17243f481f266eec1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx",
    "before": "a7a46894a3384cc519cdea0ab6b957cbb5e8fb130dd9b2073678a6d5513546e4",
    "after": "a7a46894a3384cc519cdea0ab6b957cbb5e8fb130dd9b2073678a6d5513546e4"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md",
    "before": "c0aed9db3f084398feda73059135071c66d453e204afe08ed7fb6eef78cc4c10",
    "after": "c0aed9db3f084398feda73059135071c66d453e204afe08ed7fb6eef78cc4c10"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv",
    "before": "4c97bff4f998a10c465abde26731e236759599a17a32923a6459e6fc6bff73fa",
    "after": "4c97bff4f998a10c465abde26731e236759599a17a32923a6459e6fc6bff73fa"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv",
    "before": "a86e1e9c781a788bea9de40bdb4a0186abf5a5f4c4382a74edeff02ad8ea6463",
    "after": "a86e1e9c781a788bea9de40bdb4a0186abf5a5f4c4382a74edeff02ad8ea6463"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md",
    "before": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed",
    "after": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv",
    "before": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99",
    "after": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md",
    "before": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e",
    "after": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx",
    "before": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
    "after": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md",
    "before": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034",
    "after": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv",
    "before": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0",
    "after": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv",
    "before": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be",
    "after": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md",
    "before": "1191dfd41f394d76ed933c3805c69ad4be1a47ac69e4494f19743a414696136a",
    "after": "1191dfd41f394d76ed933c3805c69ad4be1a47ac69e4494f19743a414696136a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx",
    "before": "a58cf37dee216f2e193f9ee607fa15ba4987cf49b66c4a884dab895172ebf6d4",
    "after": "a58cf37dee216f2e193f9ee607fa15ba4987cf49b66c4a884dab895172ebf6d4"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md",
    "before": "9f60f4434b1699bc38ad23fbe7f5e7ae8c816957f4885caae3cd83dd6c0d5d7b",
    "after": "9f60f4434b1699bc38ad23fbe7f5e7ae8c816957f4885caae3cd83dd6c0d5d7b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv",
    "before": "dacb3c6ad632a1ec7e3aab167f614cddaa00c7a76850506616060c332eac7890",
    "after": "dacb3c6ad632a1ec7e3aab167f614cddaa00c7a76850506616060c332eac7890"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv",
    "before": "d9bcd231bfb43ed223b8db6b270060196d5f485aa9f848cc5459d64ae857ba91",
    "after": "d9bcd231bfb43ed223b8db6b270060196d5f485aa9f848cc5459d64ae857ba91"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md",
    "before": "d87a902881e1d5d2161172d2db700c261a8ba653af2f7cff1722ea5213206e19",
    "after": "d87a902881e1d5d2161172d2db700c261a8ba653af2f7cff1722ea5213206e19"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx",
    "before": "35a6842cd1513cb2ac91328ebadc1de0feacb2c6d421c5c4170d7ddce3c7e4e5",
    "after": "35a6842cd1513cb2ac91328ebadc1de0feacb2c6d421c5c4170d7ddce3c7e4e5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md",
    "before": "72a9556ed438ef126da2d186add01b053970cae41df9b3e151d1b6e443621128",
    "after": "72a9556ed438ef126da2d186add01b053970cae41df9b3e151d1b6e443621128"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv",
    "before": "f3778953f446e71e61ae192a3021b02407b13c35b11df2d30ab5914da49181dc",
    "after": "f3778953f446e71e61ae192a3021b02407b13c35b11df2d30ab5914da49181dc"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv",
    "before": "ca606e7804945c1ac719f8088b4a9965525078033cced17e08364c45705a31b7",
    "after": "ca606e7804945c1ac719f8088b4a9965525078033cced17e08364c45705a31b7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md",
    "before": "cb02fffbe114df41dd6068c908f8e53d5de323c296b2b43a903f33519c027832",
    "after": "cb02fffbe114df41dd6068c908f8e53d5de323c296b2b43a903f33519c027832"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx",
    "before": "2ecd6ccd690b0285e3414faa52135aaeb2db738e3b69df773548a597a4230da2",
    "after": "2ecd6ccd690b0285e3414faa52135aaeb2db738e3b69df773548a597a4230da2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md",
    "before": "932a5705b875d978a2158d4b1a590d4c2170cae3a60d4385a0b5cbc3b03466f4",
    "after": "932a5705b875d978a2158d4b1a590d4c2170cae3a60d4385a0b5cbc3b03466f4"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv",
    "before": "4eaae31d939e4fe3a64c2ae2afac173eafa843a22f86d9d88befc62d14bc98c5",
    "after": "4eaae31d939e4fe3a64c2ae2afac173eafa843a22f86d9d88befc62d14bc98c5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv",
    "before": "aa372e9fa39f91b4bfb04c9342831cd90e9ecd530c537c2361c35d45de1548c5",
    "after": "aa372e9fa39f91b4bfb04c9342831cd90e9ecd530c537c2361c35d45de1548c5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md",
    "before": "675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff",
    "after": "675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx",
    "before": "0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376",
    "after": "0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md",
    "before": "543a25380b524439bcb97253e4531aefff28a6a50912b16a23e9815f154e98e9",
    "after": "543a25380b524439bcb97253e4531aefff28a6a50912b16a23e9815f154e98e9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv",
    "before": "49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550",
    "after": "49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv",
    "before": "a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7",
    "after": "a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md",
    "before": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70",
    "after": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv",
    "before": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23",
    "after": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md",
    "before": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc",
    "after": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx",
    "before": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
    "after": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md",
    "before": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d",
    "after": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv",
    "before": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49",
    "after": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv",
    "before": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534",
    "after": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md",
    "before": "78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec",
    "after": "78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx",
    "before": "a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d",
    "after": "a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md",
    "before": "31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97",
    "after": "31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv",
    "before": "e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61",
    "after": "e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv",
    "before": "3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b",
    "after": "3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md",
    "before": "c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d",
    "after": "c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx",
    "before": "8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da",
    "after": "8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md",
    "before": "d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52",
    "after": "d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv",
    "before": "c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169",
    "after": "c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv",
    "before": "5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b",
    "after": "5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md",
    "before": "ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2",
    "after": "ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx",
    "before": "024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1",
    "after": "024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md",
    "before": "256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0",
    "after": "256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv",
    "before": "8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec",
    "after": "8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv",
    "before": "baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b",
    "after": "baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md",
    "before": "a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817",
    "after": "a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx",
    "before": "8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7",
    "after": "8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md",
    "before": "945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea",
    "after": "945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv",
    "before": "6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c",
    "after": "6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv",
    "before": "336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84",
    "after": "336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md",
    "before": "86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7",
    "after": "86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx",
    "before": "9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead",
    "after": "9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md",
    "before": "eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648",
    "after": "eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv",
    "before": "0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc",
    "after": "0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv",
    "before": "de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3",
    "after": "de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md",
    "before": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d",
    "after": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv",
    "before": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5",
    "after": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md",
    "before": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2",
    "after": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx",
    "before": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
    "after": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md",
    "before": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5",
    "after": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv",
    "before": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1",
    "after": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv",
    "before": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff",
    "after": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md",
    "before": "03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97",
    "after": "03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx",
    "before": "983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e",
    "after": "983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md",
    "before": "0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca",
    "after": "0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv",
    "before": "b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c",
    "after": "b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv",
    "before": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a",
    "after": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md",
    "before": "c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866",
    "after": "c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx",
    "before": "fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63",
    "after": "fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md",
    "before": "e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d",
    "after": "e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv",
    "before": "ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd",
    "after": "ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv",
    "before": "c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237",
    "after": "c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md",
    "before": "5a9b1e21647777cb2855490d42e553a92f56906dad609522cc92841c4c59a9c9",
    "after": "5a9b1e21647777cb2855490d42e553a92f56906dad609522cc92841c4c59a9c9"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx",
    "before": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d",
    "after": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md",
    "before": "1d12b07ae29792e7ae547576468134926e6acefde9ccc740dd670cea084f70cd",
    "after": "1d12b07ae29792e7ae547576468134926e6acefde9ccc740dd670cea084f70cd"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
    "before": "badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d",
    "after": "badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d"
  },
  {
    "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv",
    "before": "3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13",
    "after": "3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md",
    "before": "cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda",
    "after": "cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_CROSS_PAPER_CLAIMS.csv",
    "before": "235765674f4ac445fa2001cb301ab4f4aabd79d05914eba2f08738e76ae98a25",
    "after": "235765674f4ac445fa2001cb301ab4f4aabd79d05914eba2f08738e76ae98a25"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_EXECUTION_REPORT.md",
    "before": "631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e",
    "after": "631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_MODEL_APPLICABILITY_MATRIX.csv",
    "before": "06a7179fdef9f5bb82adea8ef06ded04082e18ec956f1f008f45b4e7fec44d4a",
    "after": "06a7179fdef9f5bb82adea8ef06ded04082e18ec956f1f008f45b4e7fec44d4a"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_P3_HANDOFF.md",
    "before": "bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c",
    "after": "bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_SOURCE_MAP.csv",
    "before": "2d80ff743568128c2af7f52576569db1589c422a5d8210bb705761bcf8153959",
    "after": "2d80ff743568128c2af7f52576569db1589c422a5d8210bb705761bcf8153959"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md",
    "before": "5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3",
    "after": "5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_DECISION_MATRIX.md",
    "before": "4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d",
    "after": "4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md",
    "before": "5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33",
    "after": "5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_PROTOCOL_FREEZE_CHECKLIST.md",
    "before": "cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55",
    "after": "cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_R2_REPORT.md",
    "before": "a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5",
    "after": "a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md",
    "before": "e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9",
    "after": "e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_EXPERIMENTAL_VALIDATION_PLAN.md",
    "before": "f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1",
    "after": "f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md",
    "before": "f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3",
    "after": "f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md",
    "before": "2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90",
    "after": "2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_MODEL_STRATEGY.md",
    "before": "61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58",
    "after": "61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
    "before": "9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011",
    "after": "9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md",
    "before": "09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f",
    "after": "09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_SYSTEM_IDENTIFICATION_MATRIX.csv",
    "before": "894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201",
    "after": "894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/AGENT_PROMPT.md",
    "before": "91e1fdebe210f01236c0f64f6b9c5bb49fff0fc855967f8a7b45ed470f8e3284",
    "after": "91e1fdebe210f01236c0f64f6b9c5bb49fff0fc855967f8a7b45ed470f8e3284"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
    "before": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
    "after": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_OUTLINE_2026-10-14.json",
    "before": "55e15a0425dbde3ec3eb54c1e1a769c52717f03ca5d16c5fdfa8ab326d8217cd",
    "after": "55e15a0425dbde3ec3eb54c1e1a769c52717f03ca5d16c5fdfa8ab326d8217cd"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_OUTLINE_2026-10-14.md",
    "before": "45542951080f66859241e7ee3c9666b7d22df2348d3236e7560f59aef955f605",
    "after": "45542951080f66859241e7ee3c9666b7d22df2348d3236e7560f59aef955f605"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_SECTION_INDEX.csv",
    "before": "ac0a8bf828c9e69362112c6d8282f9de25cb3616ee36fd0448d741dccba59633",
    "after": "ac0a8bf828c9e69362112c6d8282f9de25cb3616ee36fd0448d741dccba59633"
  }
]
```

### Notes nhận diện bổ sung — không pre-first-read claim

```json
[
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQ_R2_SCIENTIFIC_AUDIT.md",
    "identified_late_hash": "30b9daf6fd0a4c0ad5e65eec20f7a03f2932240ffe0526e0250f3ed1b8eb0703",
    "final_hash": "30b9daf6fd0a4c0ad5e65eec20f7a03f2932240ffe0526e0250f3ed1b8eb0703",
    "before_first_read": "NOT_VERIFIED"
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md",
    "identified_late_hash": "a18aacb7fc9e670f56d96e7899e0d59e6d16273b673e31883268386410714907",
    "final_hash": "a18aacb7fc9e670f56d96e7899e0d59e6d16273b673e31883268386410714907",
    "before_first_read": "NOT_VERIFIED"
  }
]
```

## Word engineering và kiểm từng trang

WORD_RENDER_VALIDATION: PASS_LIBREOFFICE_VISUAL
MICROSOFT_WORD_VALIDATION: NOT_VERIFIED
RENDERED_PAGES: 4

LibreOffice24.2.7.2,420(Build:2) task-local extracted packages,52packages/95,194,284bytes; không cài hệ thống/không sửa profile người dùng. Dùng task-local UserInstallation vàsvp. Renderer tải quaHTTPS từpackage repositories chỉ để kiểm định dạng; không tìmthêm vănliệukhoa học. javaldxwarning không ngăn xuấtPDF, không dùngJava feature.

A4,TNR12body/headingbold12,glossary10pt,lề3/2/2.5/2.5cm,line1.15. Chỉcandidate sửa fontthemed fallback; PDF cuối toàn bộspansTimesNewRomanPSMT/BoldMT. Khôngheader/footer/covers/watermark. CaptionkeepWithNext,headerrepeat,rowcantSplit,1nativeglossarytable.

```json
{
  "render_input_docx_sha256": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
  "render_pdf_sha256": "f8bb8ca175e0dbd837c11a20b1b5a0c174143e82931d2578e722e0ce3ae6d15e",
  "root_viewed_all_pages": true,
  "visual_observations": [
    {
      "page": 1,
      "finding": "Đọc heading/P01–P06 đầu; TNR12,κ vàđơn vị hiển thị đủ, đoạn nối trang hợp lý."
    },
    {
      "page": 2,
      "finding": "ĐọcP06tiếp–P10; citation[2],[3],sourceB vàcalibration/validation đầy đủ; không cắt chữ/tràn."
    },
    {
      "page": 3,
      "finding": "ĐọcP11–P14 vàglossaryrows1–5;captionđi cùngbảng; không splitrow hoặc trắng."
    },
    {
      "page": 4,
      "finding": "Headerglossarylặp;rows6–10 và6refs; entrieskhôngtáchvôlý, khôngtràn/mấtkýhiệu."
    }
  ],
  "pages": [
    {
      "page": 1,
      "text_chars": 3576,
      "fonts": [
        "TimesNewRomanPS-BoldMT",
        "TimesNewRomanPSMT"
      ],
      "min_x": 85.1500015258789,
      "max_x": 541.75,
      "min_y": 81.35877990722656,
      "max_y": 764.6427612304688,
      "top": "2.6.4. Câu hỏi và tiêu chí chuyển sang Chương 3–4\nCác câu hỏi có điều kiện ở tiểu mục trướ",
      "bottom": "rạng thái vật liệu và điều kiện biên tương ứng, thay vì chỉ một giá trị độ cứng. GUM yêu \n",
      "png_sha256": "dd47b30bbf1dc2d779b8361d60cbeb7690ac6f43da9682b0b1d942f7c2f67883"
    },
    {
      "page": 2,
      "text_chars": 3532,
      "fonts": [
        "TimesNewRomanPSMT"
      ],
      "min_x": 85.1500015258789,
      "max_x": 541.75,
      "min_y": 71.35877990722656,
      "max_y": 758.4927368164062,
      "top": "cầu mô hình phép đo thể hiện các đại lượng đầu vào có liên quan và xem xét tương quan khi ",
      "bottom": "ô hình riêng chưa đủ để bác bỏ cả lớp giải thích ấy hoặc đòi hỏi một luật cấu \nthành mới.\n",
      "png_sha256": "38782e195c5de70a74f66be9c2674686bafc3d625fdc0f9dbfaa86117d6098d0"
    },
    {
      "page": 3,
      "text_chars": 3360,
      "fonts": [
        "TimesNewRomanPS-BoldMT",
        "TimesNewRomanPSMT"
      ],
      "min_x": 85.1500015258789,
      "max_x": 541.75,
      "min_y": 71.35877990722656,
      "max_y": 760.5607299804688,
      "top": "Trước bước tích hợp nghiên cứu, cần phân biệt ba mức điều kiện: đủ sẵn sàng để thiết kế ho",
      "bottom": "hất quán giữa các mẫu hoặc dưới điều kiện đã thay đổi.\nGUM [4], \nPhụ lục \nB.2.15–\nB.2.16.\n",
      "png_sha256": "d11ca38732df955e07a3a19bc6f73cfe6aeb0fbecadd626181a13e2ad14aa77f"
    },
    {
      "page": 4,
      "text_chars": 3042,
      "fonts": [
        "TimesNewRomanPS-BoldMT",
        "TimesNewRomanPSMT"
      ],
      "min_x": 85.1500015258789,
      "max_x": 536.3860473632812,
      "min_y": 71.79074096679688,
      "max_y": 757.8927612304688,
      "top": "Thuật ngữ tiếng Anh / \ntiếng Việt\nĐịnh nghĩa và ngữ cảnh cơ học\nNguồn\nMeasurement uncertai",
      "bottom": "s on Control Systems \nTechnology, 34(5), 2219–2233, 2026. DOI: 10.1109/TCST.2026.3690756.\n",
      "png_sha256": "8ece10d13f3618d3cfca7af4feec3651537b37b383697683b63f6909f1efa632"
    }
  ]
}
```

## SEVEN_GATE_RESULT

```json
{
  "GATE_1": "PASS",
  "GATE_2": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_3": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_4": "PASS",
  "GATE_5": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_6": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_7": "PASS_WITH_DOCUMENTED_LIMITATIONS"
}
```

## UNRESOLVED_FINDINGS và lỗi đã xử lý

P1_UNRESOLVED: 0
P2_UNRESOLVED: 0
MINOR_EDITORIAL_UNRESOLVED: 0

DOCUMENTED_LIMITATIONS:
- Human approval5groups vàRQmapping chưahoàn tất; không phải bằng chứng gap/novelty.
- M26volume/pages secondaryinternal; một sốissue bỏtrống có chủ đích, chưa xácminh publisher-final metadata.
- Chỉkiểm PDFcác trang liênquan, không externalfullcorpusreverification.
- GUMadditionalfragments được kiểmtrực tiếp, không giảlàlocatororiginalEID.
- Rawgit_snapshot chặng trước mất scratch không khôi phục;423currentinputssnapshot và418manifestinheritedmatch, cùng2lateidentifiednotes được côngbố riêng. Atimekhôngkiểm.
- MSWord vàindependentacceptance NOT_VERIFIED/NOT_PERFORMED.

Đã sửa2P2 trong cùngbản: actualinterfaces≠phêduyệtdominance; reserveddata không dùng modelselection. Đãlàmrõ flexuralmeaning/modeldependentinference vàsửafontfallback trước finalrender. Hồ sơresolution/selfreview được lưu trong7Gate; khônggiấuinitialfindings vàkhôngtạoR2/R3.

## GIT_CHANGE_SCOPE / regression

So với snapshot đầu lần tiếp tục: trackedworkingdiff binary khôngđổi; indexdiff binarykhôngđổi; porcelain entriesngoàisection_2_6_4 byte-levelkhôngđổi. Hai trackedfilesđãdirtytừtrước là outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py vàchapter2_readable_draft.md đượcgiữnguyên. Untrackedđãcó khôngxóa/sửa/revert. Output5file làuntrackedmới chỉtrongdirectoryriêng. Khônggiảđịnhtaskkhác đangchạy.

PREEXISTING_GIT_STATUS_SNAPSHOT:

```json
[
  " M outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py",
  " M outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md",
  "?? .agents/skills.json",
  "?? data/LR-FORMATED-rewrite.docx",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md",
  "?? data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md",
  "?? data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt",
  "?? data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt",
  "?? data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt",
  "?? data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt",
  "?? data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt",
  "?? data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt",
  "?? data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt",
  "?? data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt",
  "?? data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt",
  "?? data/chap1-2_citations/MANIFEST.json",
  "?? data/chap1-2_citations/README.md",
  "?? docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md",
  "?? docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md",
  "?? docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md",
  "?? docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md",
  "?? docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx",
  "?? docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx",
  "?? docs/project/almost done/LR-FORMATED.docx",
  "?? docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md",
  "?? docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md",
  "?? literature review/LR-FORMATED-rewrite-outline-de-xuat.docx",
  "?? literature review/LR-FORMATED-rewrite.docx",
  "?? literature review/LR-FORMATED.docx",
  "?? literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx",
  "?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json",
  "?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md",
  "?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json",
  "?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md",
  "?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json",
  "?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json",
  "?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json",
  "?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL.zip",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md",
  "?? literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md",
  "?? literature review/ma-tran-tong-quan-tai-lieu.docx",
  "?? literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json",
  "?? literature review/~$-FORMATED-rewrite.docx",
  "?? literature review/~$-FORMATED.docx",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/CLAIM_SOURCE_MAP.json",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/HIGHLIGHT_REGISTER.json",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/README.md",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S01_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S02_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S03_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S04_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05a_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05b_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S06_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S07_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S09_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S10_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S11_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S12_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S13_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S15_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S17_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S18_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S22_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/V-W02_search_text.txt",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/VALIDATION.json",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curated_passages.json",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/inputs.json",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/package_highlights.py",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf_text_geometry.json",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/prepare_inputs.py",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S01_P9.png",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S03_P9.png",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S04_P5.png",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S07_P6.png",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S09_P9.png",
  "?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S22_P71.png",
  "?? outputs/literature/LR_CITATION_MATRIX_2026-10-14.md",
  "?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md",
  "?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv",
  "?? outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md",
  "?? outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md",
  "?? outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md",
  "?? outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json",
  "?? outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md",
  "?? outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json",
  "?? outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json",
  "?? outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md",
  "?? outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv",
  "?? outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md",
  "?? outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md",
  "?? outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json",
  "?? outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json",
  "?? outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json",
  "?? outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json",
  "?? outputs/plans/MP1_R_PHASE_8_CHAPTER_2_RELEASE_MANIFEST_2026-10-04.json",
  "?? outputs/plans/MP1_R_PHASE_8_FINALIZATION_CHANGELOG_2026-10-04.json",
  "?? outputs/plans/MP1_R_PHASE_8_FINAL_CITATION_REGISTER_2026-10-04.json",
  "?? outputs/plans/MP1_R_PHASE_8_FINAL_CLAIM_TRACEABILITY_2026-10-04.json",
  "?? outputs/reports/MP1_GLOSSARY_C2_3_1_REPORT_2026-10-16.md",
  "?? outputs/reports/MP1_R_PHASE_7_2026-10-03/actual_docx_inventory.json",
  "?? outputs/reports/MP1_R_PHASE_7_2026-10-03/artifact_integrity_original.json",
  "?? outputs/reports/MP1_R_PHASE_7_2026-10-03/citation_appearances_original.json",
  "?? outputs/reports/MP1_R_PHASE_7_2026-10-03/inspect_artifact.py",
  "?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05a_crossref.json",
  "?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05b_crossref.json",
  "?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S11_crossref.json",
  "?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/V-W02_crossref.json",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv",
  "?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv"
]
```

## FILES_CREATED

```json
[
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md"
]
```

OUTPUT_FILE_COUNT: 5

COMMIT_STATUS: NOT_PERFORMED
PUSH_STATUS: NOT_PERFORMED
STAGE_MERGE_RESET_CHECKOUT_PR: NOT_PERFORMED
SHARED_WRITES: NONE

Không viết Chương3–4,khôngtíchhợp§2.6,khôngsửabaselines/WEP/P3/WP-E/registry/PDF/sharedscripts. Scratch/PDF/PNG/renderer/profile task-local được dọn sau kiểmtra, không làmfile6. Provenance cần thiết đãlưu ở5deliverables.

FINAL_SELF_REVIEW_DECISION: SELF_REVIEW_COMPLETED_WITH_DOCUMENTED_LIMITATIONS
REVIEW_AUTHORITY: SELF_REVIEW_ONLY
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE_AND_LATER_2_6_INTEGRATION

## FINAL_REOPEN_AND_REGRESSION — kiểm lại sau khi tạo đủ năm file

```json
{
  "reopened_all_final_files": 5,
  "claim_anchors_verified": 57,
  "glossary_rows_verified_by_identity_content_context_source": 10,
  "csv_json_fields_parse": "PASS",
  "markdown_json_appendices_parse": "PASS",
  "required_report_fields": "PASS",
  "docx_final_sha256": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
  "rendered_exact_same_docx": "PASS",
  "input_hashes_unchanged": 423,
  "late_notes_unchanged_since_identification": 2,
  "baseline_hashes_unchanged": 36,
  "git_status_outside_264": "BYTE_IDENTICAL_TO_RESUMED_PREFLIGHT",
  "working_diff": "BYTE_IDENTICAL",
  "index_diff": "BYTE_IDENTICAL",
  "new_untracked_264_files": 5,
  "docx_csv_gate_hashes": {
    "MP1_CH2_2_6_4_DRAFT.docx": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
    "MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv": "636a5acb7514ccd8309a6e786280252847bdbd5c6674264069866a772429275b",
    "MP1_CH2_2_6_4_TERMINOLOGY.csv": "346ffdf77c8e5b60680d7fb57ee9992765a7112de12673a4328ce3c8149a64f5",
    "MP1_CH2_2_6_4_7_GATE_REVIEW.md": "efc42a239b43168aa4f24fe938892cc7969bf062827e92103e3587dc0379bf2d"
  },
  "no_other_writes_detected": "PASS_WITH_REPORTED_OLD_SCRATCH_SNAPSHOT_LIMIT"
}
```

Không có sửa đổi DOCX/CSV sau render cuối. Baselines/input nội dung không đổi. Chỉ còn dọn scratch riêng, không tạo deliverable mới.

SCRATCH_CLEANUP: task-local scratch/renderer/PDF/PNG/profile vàsymlink riêng đã được dọn ở bước cuối; không dọn dữ liệu người dùng.

FINAL_SELF_REVIEW_DECISION: SELF_REVIEW_COMPLETED_WITH_DOCUMENTED_LIMITATIONS
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE_AND_LATER_2_6_INTEGRATION
