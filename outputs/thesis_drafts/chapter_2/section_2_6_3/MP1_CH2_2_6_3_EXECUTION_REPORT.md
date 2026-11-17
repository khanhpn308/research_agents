# Báo cáo thực thi — §2.6.3

TASK_ID: MP1-CH2-2.6.3-RESEARCH-THESIS-DRAFT
STATUS: COMPLETED_WITH_DOCUMENTED_LIMITATIONS
EXECUTION_TIMESTAMP: 2026-10-19T21:43:51.863586+07:00
WORKSPACE: /home/khanh/projects/mechanical-research-agents
BRANCH: main
HEAD: e66bb2f2339006e763cd60687cfc24680b945d97

ROOT_MODEL_REQUESTED: GPT-6.1 Sol High
ROOT_MODEL_ACTUAL: NOT_EXPOSED
WORKER_MODELS_REQUESTED: Sol Medium hoặc Luna theo nhiệm vụ
WORKER_MODELS_ACTUAL: NOT_VERIFIED_BACKEND
DISPATCH_SELECTORS: gpt-6.1-sol / medium (3agents); selector không là telemetry xác nhận backend.
TASK_PEER_RUNNING_CONCURRENTLY: NONE
SECTION_2_6_4_STATUS: NOT_STARTED_BY_THIS_TASK
NO_SHARED_WRITES: CONFIRMED (chỉ5finalfiles263 và dữ liệu tạm riêng; không sửa input/script chung).
REVIEW_AUTHORITY: SELF_REVIEW
FINAL_SELF_REVIEW_DECISION: SELF_REVIEW
SELF_REVIEW_RESULT: COMPLETED_WITH_DOCUMENTED_LIMITATIONS
INDEPENDENT_ACCEPTANCE: NOT_YET_PERFORMED
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE_AND_LATER_2_6_INTEGRATION

## Phạm vi và kết quả khoa học của bản thảo

Đã tạo §2.6.3 tiếng Việt với tiêu đề chính thức từ PDF/WEP,13đoạn lập luận và9thuậtngữ. Trọng tâm là câu hỏi có điều kiện về áp suất gần mẫu, tiếp xúc, uốn và mức đầy đủ dự đoán trong cấu hình/miền sẽ được người nghiên cứu xác định. Các kết quả có thể chấp nhận gồm mô hình kế thừa dự đoán đủ, kết luận thu hẹp hoặc chưa phân biệt được giải thích; sai lệch không tự chứng minh luật mới. Không khẳng định đã làm thí nghiệmMP1, không nhận dạng tham sốMP1, không dùng literaturelimitations để chứng minh novelty.

Đã phán định12dòng canonical G00–G11 theo schema nội bộ, đính trong12object gap_adjudication của CSV. Tám vấn đềG01–G08 vẫn có điều kiện, không12phát hiện hay8noveltyproof. G09 là prerequisite; G10chưađượcxáclập;G11khônglàgap;G00giữđóng. Các localstatus là nhãn xử lý bản thảo, không sửa P3canonical.

Chỉ một tác vụ người dùng §2.6.3 được thực hiện. Không tạo/ghi/sửa/đánh dấu hoàn thành tệp§2.6.4, không giao agent làm§2.6.4, không tích hợp toàn§2.6. Đoạn cuối chỉ có một câu chuyển tiếp.

## WORKERS_USED

| Agent | Vai trò thực tế | Selector yêu cầu | Kết quả / giới hạn |
|---|---|---|---|
| gap_sources | A: xác minhM06/M10/M13; tái dùng vai tròH: staticQA | gpt-6.1-sol/medium | 3PDFmở; metadata/locators/counterevidence;21staticchecks cuối PASS. QA không kiểm lại nội dungPDF hoặc visual. |
| gap_counterevidence | B: M25/M31/M16/M34; xét phản chứng bản thảo | gpt-6.1-sol/medium | 4PDFmở; chỉ ra priorartđã xử lý một phần và phân biệtfit/validation;1chỉnh câuP10 đã sửa. |
| gap_p3_audit | C: toàn P3/WP-E/RQmapping; tái dùngF: thuậtngữ | gpt-6.1-sol/medium | Giữ12canonicalstatus, map4P3groups/5PDFRQs tạm thời, đề xuất9term được ROOT xét. Không kiểmPDFjournal. |
| ROOT | Preflight; adjudication; M26/M38/M28; đọc trangnguồn rủi ro; soạn/sửa; CSV/Word/render/7Gate/final | backendNOT_EXPOSED | Không có workerE/G riêng. ROOT viết bản cuối và dựng Word từ nội dung phê duyệt. |

Không quyết định khoa học theo đa số. WorkerB vàC cùng phát hiện câu “tập quan sát và độ không đảm bảo có đủ nhỏ”; ROOT sửa thành “tập quan sát có đủ thông tin và độ không đảm bảo có đủ nhỏ”. ROOT còn tách câu suy luận từ sourcegrounded để không nâng category; sửa mapping M26-E05→E04 cho DIC/IR/thermocouple đúng nguồn, thêm giới hạn coreM10/M13. Tất cả45bodyunits cuối đã qua ROOT đọc lại và staticQA.

Skills áp dụng tiếp trong phiên: academic-paper, academic-humanizer, unslop, ponytail. User contract về một tiểu mục/corpus/đúng5files có ưu tiên hơn workflow chung; không thêm khai báo/bìa/khảo sát ngoài phạm vi.

## PREFLIGHT / WEP_FILES_READ

Đã xác nhận pwd/reporoot,main,HEAD,gitstatus và snapshot trước. Context đọc theo thứ tự AGENTS: docs/README.md; docs/project/PROJECT_HANDOFF_CURRENT.md; RESEARCH_STATE.md; research_state.json; RESEARCH_LOG.md; docs/literature/LITERATURE_STRATEGY.md; docs/operations/KNOWN_ISSUES.md. Không sửa trạng thái nghiên cứu hoặc registry.

Chín tệp WEP bắt buộc đã truy xuất/đối chiếu theo thứ tự, đọc đầy đủ brief riêng§2.6.3 và các hàng thuộc phạm vi:

- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md
- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv
- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv
- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md
- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv
- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv
- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md
- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md
- /home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md

P3 canonical được đọc nguyên bản tại worktree nguồn:

- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv
- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md
- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md
- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md
- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md
- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md
- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md
- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md
- /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_CROSS_PAPER_CLAIMS.csv

Các JSONL/registry/EquationNotes/PaperNotes được dùng tìm nguồn và giữ provenance; inheritedFULLTEXTstatus không được giả thành lần auditđộc lập mới.

## OFFICIAL_OUTLINE / READINESS / SCOPE_FINDINGS

ORIGINAL_OUTLINE_FILE: /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf
OUTLINE_SHA256: 18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e
PHYSICAL_PDF_PAGE: 15
OFFICIAL_HEADING: 2.6.3. Khoảng trống có thể kiểm chứng
WORKING_TITLE_ONLY: Khoảng trống nghiên cứu có điều kiện (không thay officialheading)
OUTLINE_BULLETS: 2
READINESS_STATUS: BOUNDED_WRITING_READY
AUTHOR_APPROVAL_STATUS: PENDING; NOT_GRANTED_BY_THIS_TASK

| Bullet | Nguyên văn PDF/WEP | Câu hỏi và nội dung thực hiện | Evidence / nguồn nội bộ | Vị trí Word | Tình trạng |
|---|---|---|---|---|---|
| B01 | Khoảng trống làm việc là xây dựng và kiểm tra bản đồ interface-specific giữa áp suất gần mẫu, trạng thái tiếp xúc, đáp ứng M–κ và sai lệch mô hình trong miền bất định đã khai báo. | Xác định câu hỏi áp suất–tiếp xúc–uốn, giao diện/biên, vật liệu/lịch sử, mô hình đối chứng và điều kiện quan sát. | Core M06-E04/M10-E04/M13-E06; phản chứng M25/M31/M16/M34; M26/M38; P3/WP-E. | P01–P10, P12–P13; paragraph[1]–[10],[12]–[13]. | Câu hỏi/đề xuất có điều kiện; chưa là gap toàn lĩnh vực hoặc cấu hình đã chốt. |
| B02 | Đóng góp được chấp nhận nếu nghiên cứu phân biệt được cơ chế hoặc chỉ ra giới hạn của mô hình hiện hữu; kết quả không có hiệu ứng vượt bất định cũng được báo cáo như một kết luận thu hẹp. | Giữ mô hình kế thừa còn sống; phân biệt hiệu chuẩn/kiểm chứng; chấp nhận kết quả thu hẹp hoặc chưa phân biệt; residual không tự chứng minh luật mới. | P3_HYPOTHESIS_ASSESSMENT; P3_RESEARCH_QUESTIONS; M25-E06/M16-E04; M38-E02/E03/E04 chỉ phương pháp. | P05, P07–P08, P10–P13. | AUTHOR_PROPOSAL/INFERENCE/P3 nội bộ; phê duyệt khoa học còn chờ. |

OUTLINE-01: PDF trang15 và WEP khớp cả tiêu đề và2bullet. Không có thay tên cần giả định ủy quyền. Bản data/LR-FORMATED-rewrite.docx được đọc đối chiếu, có tên§2.6.3 “Câu hỏi nghiên cứu và phạm vi đóng góp dự kiến”, vị trí/nhómRQ khác. Không dùng bảnDOCXđó thay PDF được WEP chỉ định; không sửa hoặc hợp nhất. Dòng provenance của bảnDOCXso với bảnPDFvẫn chưa được người nghiên cứu quyết định, ghi rõ thay vì âm thầm lựa chọn.

AUTHOR_APPROVAL-01: WEP yêu cầu phê duyệt sau quyết địnhtopology/measurement. User đã ủy quyền soạn bản có điều kiện; đó không phải phê duyệt khoa học cuối cho câu hỏi hay năm quyết định. Vì vậy tiếp tục tạo bản reviewable nhưng giữ trạng thái approvalpending, không xin lại quyền soạn và không gọi selfreviewlàacceptedindependently.

ROLE-01: SourceMatrix§263 đặt M06/M10/M13 ởCONTEXT_ONLY; CitationCrosswalk07 liệt kêDIRECT_SUPPORT cho một sốnguồn. ROOT dùng vai trò ở cấpclaim: chính kết quả/giới hạn của nguồn có thể trực tiếp hỗ trợ mô tả hệnguồn; khi suy gapMP1 chỉcontext/comparator. M06luônreview, không primaryexperiment.

## RQ_MAPPING-01 — hai namespace giữ nguyên

PDF§1.4.1 ở trang vật lý6 có5RQ. P3_RESEARCH_QUESTIONS.md có4nhóm; không cùng cấu trúc hoặc ánh xạ1–1. Chỉ lập đối chiếu phân tích nhiều–nhiều dưới đây, không đổi nhãn, không hợp nhất/xóa/renumber.
RQ_RECONCILIATION_STATUS: HUMAN_DECISION_PENDING

| PDF RQ (nguyên nhãn) | Câu hỏi nguyên bản PDF6 | NhómP3 liên quan, chỉ phân tích tạm | Status |
|---|---|---|---|
| RQ1 | Interface chịu tải chính là wire–wire, wire–sleeve hay cả hai, và áp suất dương làm thay đổi traction ở interface đó theo chiều nào? | P3 RQ2, P3 RQ4 | HUMAN_DECISION_PENDING |
| RQ2 | Khi dùng nguồn áp ngoài, áp suất gần mẫu liên hệ thế nào với trạng thái stick, partial slip, full slip và các đại lượng M–κ? | P3 RQ1, P3 RQ2, P3 RQ4 | HUMAN_DECISION_PENDING |
| RQ3 | SMA–piston tạo, duy trì và hồi áp suất với force–stroke–temperature–volume–time và độ lặp lại nào? | P3 RQ3, P3 RQ4 | HUMAN_DECISION_PENDING |
| RQ4 | Ở cùng áp suất gần mẫu, Bench B có tái tạo được đáp ứng pressure-only của Bench A hay tạo sai khác do transient, nhiệt, rò hoặc compliance? | P3 RQ1, P3 RQ3, P3 RQ4 | HUMAN_DECISION_PENDING |
| RQ5 | Sau khi interface và pressure-transfer map được xác nhận, mô hình H0b có dự đoán được dữ liệu held-out trong phạm vi bất định không? | P3 RQ1, P3 RQ2, P3 RQ3, P3 RQ4 | HUMAN_DECISION_PENDING |

P3RQ1: pressure-conditionedbending/modelvalidity; P3RQ2: interface/localslip; P3RQ3: TiNistate/SMA/hysteresis; P3RQ4: identifiability/uncertainty. Tham chiếuP3 vàPDF dùng namespace riêng. Quan hệ với cácgap/prerequisite và locator đầy đủ được lưu dưới đây để không phụ thuộc tệp tạm.

```json
{
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
}
```

## BASELINE_PATHS / BASELINE_SHA256_BEFORE_AFTER

Đã đọc nămDOCX được user chỉ định; các kết luận liên quan §§2.3–2.5 và toàn thân§§2.6.1–2.6.2, kèm CSV/glossary/QA/execution. Baseline31file gồm21file§§2.3–2.5tích hợp và đủ10deliverables của§§2.6.1–2.6.2. HaiDOCXhash khớp hồ sơ người dùng. Trạng thái predecessor ACCEPTED_WITH_DOCUMENTED_LIMITATIONS là USER_REPORTED; các báo cáo cũ vẫn làselfreviewcủaphiên trước, không phải journal evidence mới.

§2.5 giữ nguyên minorerrataT015/T016vànhãnP3_CANONICAL ngoài trích; cụm “cấu hình tiếp xúc tiếp xúc”. Không mở hotfix. Không render hoặc tái xuất bất kỳ baseline nào.

| Baseline path | SHA-256 BEFORE | SHA-256 AFTER |
|---|---|---|
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx | bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec | bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv | 65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be | 65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md | 25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034 | 25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md | e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e | e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv | eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99 | eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv | 54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0 | 54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md | 84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed | 84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md | 09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc | 09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv | 3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23 | 3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md | 0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d | 0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md | 751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70 | 751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv | eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534 | eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx | d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea | d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv | d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49 | d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv | a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5 | a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md | b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d | b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv | 229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1 | 229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx | cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc | cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv | 70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff | 70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md | d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5 | d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md | 3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2 | 3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md | 03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97 | 03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx | 983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e | 983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv | bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a | bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv | b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c | b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md | 0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca | 0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md | e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d | e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx | fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63 | fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv | c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237 | c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md | c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866 | c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv | ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd | ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd |

BASELINES_UNCHANGED: YES (31/31)
INPUT_FILES_CHECKSUM_UNCHANGED: YES (418/418 snapshot input/support/pre-existing dirtyfiles)

SHA kiểm bằng bytes trước/sau; không gọi chmod/touch/ghi/re-export input. INPUT_ATIME_PRESERVATION: NOT_VERIFIED vì không snapshotatime, đọc chịu chính sách filesystem; không khẳng định mọi metadata chưa đo là bất biến.

## SOURCE_PAPERS / VERIFIED_PDFS / EVIDENCE_IDS

SOURCE_PAPERS: 9
SOURCE_PAPER_IDS: M06;M10;M13;M31;M25;M26;M16;M34;M38
VERIFIED_PDFS: 10 (9nội dung +M28metadata)
UNVERIFIED_PDFS: 0 trong tập nguồn dùng
EVIDENCE_IDS: 26
OTHER_OPENED_CORPUS_PDF: M01,3trang đầu, chỉ quyết định phạm vi phương pháp; không tính reference/claimcơhọc.
OUTLINE_PDF_OPENED: 1; trang15cho§263,trang6choRQ.

M06-E04/M10-E04/M13-E06 là corelimitationanchors. M01-E01 là sách hướng dẫn tổ chức tổngquan, không chứngminhgapcơhọc và không có claim cầntrích, nên không đặtreference thừa. M25/M31/M16/M34 được chọn từ P3/WP-E để xét phảnchứng thật; M26/M38 hỗ trợ trạng thái/đo lường. Không mặc nhiên nhập toàn bộ nguồn predecessor hoặc39bài. Không tìm nguồn ngoài corpus.

Bảng dưới ghi nguồn thực dùng và provenance metadata. Các số PDFmở là hồ sơ thực thi của ROOT/nhóm trong phiên, không independentexternalaudit toàn bài. ROOT tự mở lại selectedpages của9nguồn vàM28, đặc biệt các claimrủi ro; WorkerA/B trả gói đọc trực tiếp. CSV có verification_agent từng component và táchdirectPDFingredients khỏi inference/proposal.

| Citation | Paper | PDF canonical | SHA-256 | Metadata provenance |
|---:|---|---|---|---|
| 1 | M06 | data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf | f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b | First/final pages canonical PDF checked by workerA; ROOT inspected relevant content; no issue inferred. |
| 2 | M10 | data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf | 182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58 | First/final pages canonical PDF checked by workerA; ROOT inspected relevant content; no issue inferred. |
| 3 | M13 | data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf | 3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f | First/final pages canonical PDF checked by workerA; ROOT inspected relevant content; no issue inferred. |
| 4 | M31 | data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf | 65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03 | PDF first/finalpages checked |
| 5 | M25 | data/chap1-2_citations/M25__A3-2022-Mechanical response of single and double-helix.pdf | 53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a | Authors/title/DOI/online03Aug2021 directly canonicalM25 PDF1; finalyear2022,volume29,pages5393–5406 from canonicalM28 PDF19 ref28. Issue NOT_VERIFIED. Secondary internal pagination, not finalpublisherPDF. |
| 6 | M26 | data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf | 00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9 | CanonicalM26 PDF1 proof shows xxx; finalvolume/pages from canonicalM28 PDF19 ref14. Authors/order/title/DOI/year directlyM26 PDF1; issue NOT_VERIFIED. |
| 7 | M16 | data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf | 1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a | PDF first/finalpages checked |
| 8 | M34 | data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf | 55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782 | PDF first/finalpages checked |
| 9 | M38 | data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf | 41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c | ROOT reopened canonical PDF first page; M26 proof publication pagination from M28 PDF19 ref14; M38 PDF2–3 institutional author/title/year. |

USED_EVIDENCE_IDS: M06-E04, M10-E01, M10-E04, M13-E01, M13-E04, M13-E06, M16-E02, M16-E04, M16-E06, M25-E02, M25-E06, M26-E01, M26-E03, M26-E04, M26-E07, M31-E01, M31-E03, M31-E06, M31-E07, M34-E02, M34-E08, M34-E09, M38-E01, M38-E02, M38-E03, M38-E04

## Source verification và correction provenance

- M06: §6 ởPDF20–21/printed20–21of28. Fig19trước§6so stiffnessranges, không thí nghiệm primary về trượt. Reviewkhông baogồmparticle/fiber trongscope, không làm bằngchứng kiểmMP1.
- M10: physicalPDF7/printed8084,§VConclusionandFutureWork, locator cũ7đúng. Phân bốhạt/softbladder/abrasionsandpaper là giới hạncấu hình, khôngphát hiệnmònTiNi hoặc dynamicgap toàn ngành.
- M13: oneprototype/singlefiberconfiguration/phenomenologicaltransition/systemidentifiedE ởPDF11/in491; variability/possiblepressuretransmission ởPDF10/in490. Nguồn đã có pressure-to-state-to-bending, repeatedtesting vàvariability/modelcomparison. Không gọi thêm các thànhphần đó là novelty.
- M13Eq4: ROOTđọcPDF3/in483vàEquationNotesB06/B07. Noteskhông bao phủEq4 và SHA ghi choPDFtrongnotes kháccanonicalPDF. Giữ warningthứnguyên đã biết; không sao chép, tính số, tựsửa hoặc dùng anomaly đểbác bỏtoànnguồn. OMML=0. Không tính warningkhôngsửdụng thành claimkhoa học củaWord.
- M25: canonicalPDFonline2021 cócovernên physicalpage=printedpage+1 từnộidung. §4.2/PDF5giới thiệuSouzaUMAT vàfriction0.115choSMA; §5.1–5.2textcomparison PDF5–6/in4–5, figures8/12xuấthiệnPDF9/10. Khôngtrình bàynhưthínghiệmmới; tham sốvàdataReedlunnđượckếthừa. Khôngđưa %discrepancyvàophầnthân vìkhôngcầncho câu hỏi.
- M25metadata: online03Aug2021/tácgiả/title/DOItrực tiếpPDF1. Final2022volume29pages5393–5406từM28PDF19ref28; đây là đối chiếuthứcấp nội bộ, issueNOT_VERIFIED. Giữoriginal2021trongacceptedlookup, không sửa registry.
- M26: physicalproofpages5–7choLE/DIC/IR/thermocouples vàmatrix, phù hợpM26-E04; E05làdry/lubricated/plateaus nên khôngdùng nó thaychannel-evidence. DSCởPDF4,cyclehistoryPDF14–17. Proofchưaphântrangfinal; volume50/pages3009–3026từM28PDF19ref14. Khôngbịaissue và không suy kếtquảkéo sanguốnMP1.
- M31: phépma sátmộtdâyriêng ởPDF5–6/in6586–6587; bendingmodelxételastic/frictionwork và dùng cảmeanfriction lẫn martensitebendingworktrongso sánh. Khônggọi toànbộkiểmchứnglàheld-out độc lập. Wire–rubber không tự làwire–wireTiNi hoặc phân bốN.
- M16: pressuredependentpotential/functionđãcó, với identification/controltests. Vacuumngược dấu áp tươngđốiMP1. Fig7quan hệ sqrt-pressure/R².9216làmôhìnhmớitrênsource, còn3.7315uP+154.2731là đường comparatorcũ[32]; khônglẫncảhai, không đưa côngthứcsố vàoWord. Stiffnessdata được táidùngnhậndạngc4/c5; controltestskhácindependentMP1validation.
- M34: forcecompatibilitySMAcoil/siliconevàpressure ởPDF3; dynamics/displacement/flowPDF8–11; statichead/operationPDF11–13. Khôngsuy môhìnhđiểmđầu-cuốilàtoànbàibỏdynamics, khôngápđầu ra=localtraction.
- M38: scope/definitionPDF13–14/in1–2; modelPDF20–21/in8–9; covariancePDF31/33/in19/21; coveragePDF35–36/in23–24. Glossarydefinitionở§2.2.3làadditionalROOTfragment; E01canonicalchỉsupportscope vàkhôngđượcgiảcómụcdefinitionlocatornguyênbản. E02/E03hỗtrợmodel/covariance. Cácpagegốcsaiđượclưu, không dùnglàmcheckedlocator. GUMkhônglàMP1data hoặc modeldiscriminationthreshold.

Các gói kiểm chứng liên quan được nhúng trongCSV, gồm rawacceptedrecords/locators và componentkiểmtrực tiếp. Tên tệptạm trong gói chỉ là provenance lịch sử; không phải tài liệu canonicalmới hoặc tệp bắtbuộc để đọc đầu ra.

## GAP_ADJUDICATION_SUMMARY

| P3 ID | Canonical classification | Canonical status (nguyên bản) | Local draft treatment | Word location |
|---|---|---|---|---|
| G00 | SUPPORTED_WITHIN_REVIEWED_CORPUS | CLOSED_AS_GENERAL_MECHANISM; MP1 transfer remains open | CLOSED | DOCX paragraph[1] (0-based; title=0); P01 unit[3] |
| G01 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-IDENTIFICATION QUESTION | CONDITIONAL_OPEN | DOCX paragraph[3] (0-based; title=0); P03 unit[3] |
| G02 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-IDENTIFICATION QUESTION | ALREADY_PARTIALLY_ADDRESSED | DOCX paragraph[4] (0-based; title=0); P04 unit[2] |
| G03 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN BOUNDED EMPIRICAL CHARACTERIZATION | CONDITIONAL_OPEN | DOCX paragraph[2] (0-based; title=0); P02 unit[1] |
| G04 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN ENGINEERING/SYSTEM-IDENTIFICATION QUESTION | ALREADY_PARTIALLY_ADDRESSED | DOCX paragraph[9] (0-based; title=0); P09 unit[3] |
| G05 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN ATTRIBUTION/REPEATABILITY QUESTION | CONDITIONAL_OPEN | DOCX paragraph[6] (0-based; title=0); P06 unit[3] |
| G06 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN BOUNDED MODEL-DISCRIMINATION QUESTION | ALREADY_PARTIALLY_ADDRESSED | DOCX paragraph[8] (0-based; title=0); P08 unit[1] |
| G07 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN IDENTIFIABILITY GATE | CONDITIONAL_OPEN | DOCX paragraph[10] (0-based; title=0); P10 unit[3] |
| G08 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-CALIBRATION QUESTION | CONDITIONAL_OPEN | DOCX paragraph[4] (0-based; title=0); P04 unit[2] |
| G09 | OUT_OF_SCOPE | PROJECT PREREQUISITE, NOT A LITERATURE GAP | NOT_A_RESEARCH_GAP | DOCX paragraph[4] (0-based; title=0); P04 unit[1] |
| G10 | NOT_ESTABLISHED | CONDITIONAL STRETCH ONLY | NOT_ESTABLISHED_IN_CORPUS | DOCX paragraph[11] (0-based; title=0); P11 unit[3] |
| G11 | NOT_ESTABLISHED | PROHIBITED CLAIM | NOT_A_RESEARCH_GAP | DOCX paragraph[1] (0-based; title=0); P01 unit[3] |

Local ALREADY_PARTIALLY_ADDRESSED ởG02/G04/G06 không đóng những câu hỏiMP1canonical; chỉ thừa nhận phần nguồn đãxửlý. canonical8classification vẫn PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE. G00đóng cơchếchung nhưngtransferMP1cóđiềukiện, khôngmởlạiG00.

Mỗi objectCSV có đầy đủ GAP_CANDIDATE/P3_GAP_ID/OUTLINE_BULLET/P3source/DOI/EIDs;ESTABLISHED_PRIOR_ART;PREVIOUSLY_ADDRESSED;OBSERVED_LIMITATIONvàattribution;TRANSFER_CONDITION;OPEN_QUESTION;COMPETING_EXPLANATION;DISCRIMINATING_OBSERVATION;FALSIFIABILITY_BOUNDARY;EVIDENCE_CLASSIFICATION;STATUSvàscope;REASON_NOT_NOVELTY_PROOF;manuscriptanchor. Khôngbịa canonicalIDmới. G09designprerequisite cójournalfields trống đúngvaitrò.

H0b=NOT_FALSIFIED_LIVE_COMPETITOR;H1=INSUFFICIENT_EVIDENCE theoP3đãđọc. H0a nếu nhắc trongreport chỉREFUTED_IN_TRANSFORMATION_REGIME, không suy từđóH1. Word mô tả đối chứngbằngtiếngViệt, không chứa machineH/G/RQcodes. Một luậnvăn hợp lệkhông cần constitutivelawnew.

## ACTUAL_COUNTS

Sốđếm từfilecuối, DIRECTLY_VERIFIED qua parsing. Các số đọcPDF là CURRENT_TASK_TEAM_REPORTED cùngdấu vếtcheckcomponents, khôngchứngnhận độc lập bênngoài.

```json
{
  "prose_paragraphs": 13,
  "body_claim_records": 45,
  "glossary_claim_records": 9,
  "claim_records": 54,
  "claim_category_counts": {
    "SOURCE_GROUNDED_CLAIM": 11,
    "INFERENCE": 25,
    "AUTHOR_PROPOSAL": 11,
    "PENDING_HUMAN_DECISION": 4,
    "P3_INTERNAL_DEFINITION": 1,
    "DOCUMENT_COVERAGE": 2
  },
  "source_role_counts": {
    "CONTEXT_ONLY": 23,
    "DIRECT_SUPPORT": 9,
    "COMPARATOR": 18,
    "METHODOLOGY": 4
  },
  "source_papers": 9,
  "evidence_ids": 26,
  "gap_adjudication_records": 12,
  "canonical_conditional_questions": 8,
  "local_gap_status_counts": {
    "CLOSED": 1,
    "CONDITIONAL_OPEN": 5,
    "ALREADY_PARTIALLY_ADDRESSED": 3,
    "NOT_A_RESEARCH_GAP": 2,
    "NOT_ESTABLISHED_IN_CORPUS": 1
  },
  "terminology_entries": 9,
  "glossary_entries": 9,
  "references": 9,
  "unique_dois": 8,
  "citation_occurrences": 18,
  "body_citation_occurrences": 17,
  "glossary_citation_occurrences": 1,
  "scientific_tables": 0,
  "glossary_tables": 1,
  "figures": 0,
  "omml_equations": 0,
  "prose_whitespace_tokens": 1786,
  "docx_zip_xml_status": "VALID",
  "docx_sha256": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d",
  "verified_content_pdfs": 9,
  "verified_metadata_pdfs": 1,
  "verified_pdfs": 10,
  "unverified_used_pdfs": 0,
  "methodology_pdf_opened_excluded": 1
}
```

AUTHOR_DERIVATION: 0. 54claimrecords=45body+9glossary. 25INFERENCEgồm9địnhnghĩa/ngữcảnh biêntập;11AUTHOR_PROPOSALlàcâu hỏi/điềukiện/khả năng kếtluận, khôngkếtquả. BốnPENDINGrecordbao gồmđủ5nhómquyếtđịnh; khôngđếmcoverage/P3definitionnhưkếtquảthựcnghiệm. 12gapobjectlồngkhôngthêm12claimrows vàkhônglà12noveltyproof.

SOURCE_ROLE_COUNTS: {"CONTEXT_ONLY": 23, "DIRECT_SUPPORT": 9, "COMPARATOR": 18, "METHODOLOGY": 4}
EVIDENCE_CLASS_COUNTS_MULTI_LABEL: {"REVIEW_SYNTHESIS": 2, "EXPERIMENTALLY_DEMONSTRATED": 23, "P3_INTERNAL_OR_AUTHOR_EDITORIAL": 20, "SOURCE_REPORTED_LIMITATION": 8, "CALIBRATION_SUPPORTED": 9, "NUMERICALLY_DEMONSTRATED": 6, "MODEL_DERIVED": 13, "COMPARISON_TO_PUBLISHED_EXPERIMENTS": 5, "METHODOLOGY_GUIDANCE": 4}

Các cột limitation_* của schema§2.6.2 được giữ để tương thích; tác vụ§2.6.3 không tái đếm loại giới hạn thànhgap. is_limitation_claim ghi NOT_APPLICABLE_SECTION_2_6_3, không giảfalse/true để tạo sốđếm. Phán định dùnggap_adjudication vàp3_gap_ids. Categories/roles/evidenceclasses là các chiều khác nhau, khôngthang xếp hạng.

CITATION_OCCURRENCES: 18 (17body+1glossary,khôngtính9nhãnbibliography). REFERENCES:9;UNIQUE_DOIS:8;M38khôngDOI. Támtermsourcecelllà “Tổng hợp của tác giả”, cóinternalprovenanceCSV, khôngcitationjournalgiả. SCIENTIFIC_TABLES:0;GLOSSARY_TABLES:1;FIGURES:0;OMML_EQUATIONS:0.

## Word engineering / rendering

DOCX_ZIP_XML_STATUS: VALID
WORD_RENDER_VALIDATION: PASS_LIBREOFFICE_VISUAL
MICROSOFT_WORD_VALIDATION: NOT_VERIFIED
RENDERED_PAGES: 5
DOCX_SHA256: 5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d

A4;TNR12ptprose/refs;heading12bold;lềtop/bottom2.5cm,left3cm,right2cm;line1.15,spaceafter6pt.GlossaryTNR10,1nativetable3cột10hànginclheader,repeatheader/nosplit/fixedwidth/captionkeepwithnext. Khôngcovers/header/footer hoặcstatusmetadata trongmanuscript. KhôngphươngtrìnhnênOMML0hợplệ.

HệthốngkhôngcóLibreOfficecài sẵn. ROOTtải52góiapt (95,194,284bytes) và chỉ giải nén trongtasktemp, không cài/đổi hệthống hoặc input. Cấu hình/librariesđượcrelocate trongtemp; một symlinkresource riêng /tmp/mp263-v81f8h7m được dùngvàdọn khi kếtthúc. Dùngprofile riêng -env:UserInstallation=file:///.../renderer/final-profile,khôngprofileđanghoạtđộng. FontTimesNewRoman thực fc-matchtrả times.ttf. Javaldxwarningkhôngchặnconvert;exit0/PDF5trang. Khôngtìmhoặcthêmnguồn khoa họcbênngoài;networkchỉphụcvụrenderer.

ROOTđãxemcả5trangrendercuối, khôngcắtchữ,trànbảng,mấtkýhiệuvàtrangtrắng. Bảnđầu cócitationvắtquatrang; chỉthêmlayoutkeepTogetherP06/P11rồirender/staticQA lại, khôngđổi khoa học hoặc tạoR2/R3. Chi tiết quan sát:

```json
{
  "reviewer": "ROOT",
  "authority": "SELF_REVIEW",
  "renderer": "LibreOffice 24.2.7.2 420(Build:2)",
  "docx_sha256": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d",
  "pdf_sha256": "73ee5b9e539deb6922390aab9b1b42b9174911cb38ef151d0b590d7570a917be",
  "rendered_pages": 5,
  "status": "PASS_LIBREOFFICE_VISUAL",
  "microsoft_word": "NOT_VERIFIED",
  "pages_viewed": [
    1,
    2,
    3,
    4,
    5
  ],
  "observations": {
    "1": "Official title and prior-art-to-question argument legible; P06 starts next page intact.",
    "2": "P06–P10 paragraphs/citations intact; no cropped text; P11 starts next page intact.",
    "3": "P11–P13 bounded outcome, human decisions and single short264transition; intentional space before glossary.",
    "4": "Glossary caption and all9terms fit one native3column table; source cells distinct editorial vs[9].",
    "5": "All9bibliographic entries legible and kept intact; DOI text and names visible."
  },
  "blank_pages": 0,
  "clipped_text_observed": 0,
  "table_overflow_observed": 0,
  "lost_symbols_observed": 0
}
```

## BOUNDED_STATIC_QA_ARCHIVE

21checks củaworkerA tái dùngH, saucùnghash đãkhớp. WorkerkhôngcertifyPDF/visual;ROOTlàmhai phầnđó theo phạmvi đãnêu.

```json
{
  "status": "PASS",
  "scope": "Bounded static QA for internal §2.6.3 only. No PDF content reread certification or visual/layout certification.",
  "artifact_hashes": {
    "candidate.docx": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d",
    "traceability.csv": "badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d",
    "terminology.csv": "3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13",
    "stats.json": "0c899c2f299356d94f8f59238799c20505af8eacba243d966dfbb96ddba7f376",
    "approved_draft.json": "ebb82fb7ddaa383930c697ae5e17aad51ca10e1892ced959a83973fc08bdea1c",
    "gap_adjudications.json": "133aaa3ed8ff958293097a3a9656d6ead69f232491c88629ea2942477fd8b4dc",
    "approved_terms.json": "174b9209b28c8d8b713a13178b4ba9a78674f5d92f7bfebc89e1a07bac6dd529"
  },
  "recomputed": {
    "prose_paragraphs": 13,
    "body_claim_records": 45,
    "glossary_claim_records": 9,
    "claim_records": 54,
    "claim_category_counts": {
      "SOURCE_GROUNDED_CLAIM": 11,
      "INFERENCE": 25,
      "AUTHOR_PROPOSAL": 11,
      "PENDING_HUMAN_DECISION": 4,
      "P3_INTERNAL_DEFINITION": 1,
      "DOCUMENT_COVERAGE": 2
    },
    "source_role_counts": {
      "CONTEXT_ONLY": 23,
      "DIRECT_SUPPORT": 9,
      "COMPARATOR": 18,
      "METHODOLOGY": 4
    },
    "source_papers": 9,
    "evidence_ids": 26,
    "gap_adjudication_records": 12,
    "canonical_conditional_questions": 8,
    "local_gap_status_counts": {
      "CLOSED": 1,
      "NOT_A_RESEARCH_GAP": 2,
      "CONDITIONAL_OPEN": 5,
      "ALREADY_PARTIALLY_ADDRESSED": 3,
      "NOT_ESTABLISHED_IN_CORPUS": 1
    },
    "terminology_entries": 9,
    "glossary_entries": 9,
    "references": 9,
    "unique_dois": 8,
    "citation_occurrences": 18,
    "body_citation_occurrences": 17,
    "glossary_citation_occurrences": 1,
    "scientific_tables": 0,
    "glossary_tables": 1,
    "figures": 0,
    "omml_equations": 0,
    "prose_whitespace_tokens": 1786,
    "docx_zip_xml_status": "VALID",
    "docx_sha256": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d"
  },
  "checks": [
    {
      "check": "trace record totals",
      "pass": true,
      "detail": {
        "all": 54,
        "body": 45,
        "glossary": 9
      }
    },
    {
      "check": "trace claim IDs unique",
      "pass": true,
      "detail": [
        "263-C001",
        "263-C002",
        "263-C003",
        "263-C004",
        "263-C005",
        "263-C006",
        "263-C007",
        "263-C008",
        "263-C009",
        "263-C010",
        "263-C011",
        "263-C012",
        "263-C013",
        "263-C014",
        "263-C015",
        "263-C016",
        "263-C017",
        "263-C018",
        "263-C019",
        "263-C020",
        "263-C021",
        "263-C022",
        "263-C023",
        "263-C024",
        "263-C025",
        "263-C026",
        "263-C027",
        "263-C028",
        "263-C029",
        "263-C030",
        "263-C031",
        "263-C032",
        "263-C033",
        "263-C034",
        "263-C035",
        "263-C036",
        "263-C037",
        "263-C038",
        "263-C039",
        "263-C040",
        "263-C041",
        "263-C042",
        "263-C043",
        "263-C044",
        "263-C045",
        "263-C046",
        "263-C047",
        "263-C048",
        "263-C049",
        "263-C050",
        "263-C051",
        "263-C052",
        "263-C053",
        "263-C054"
      ]
    },
    {
      "check": "all manuscript anchors resolve once at recorded locations",
      "pass": true,
      "detail": {
        "checked": 54,
        "resolved": 54
      }
    },
    {
      "check": "approved prose identity",
      "pass": true,
      "detail": {
        "approved_paragraphs": 13,
        "Word_body_paragraphs": 13
      }
    },
    {
      "check": "two outline bullets covered",
      "pass": true,
      "detail": [
        "B01",
        "B02"
      ]
    },
    {
      "check": "body unit and trace anchor identity",
      "pass": true,
      "detail": {
        "approved_units": 45
      }
    },
    {
      "check": "glossary identity content and source attribution",
      "pass": true,
      "detail": {
        "entries": 9,
        "exact_three_cell_content_matches": 9,
        "unique_term_ids": 9
      }
    },
    {
      "check": "canonical evidence IDs and accepted lookup identity",
      "pass": true,
      "detail": {
        "unique_used": 26,
        "lookup_mismatches": [],
        "canonical_paths_checked": [
          "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl",
          "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl",
          "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
          "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl"
        ],
        "all_lookup_records_exact_at_recorded_path_and_line": true
      }
    },
    {
      "check": "references local sequence and verified metadata identity",
      "pass": true,
      "detail": {
        "references": 9,
        "metadata_papers": 9,
        "errors": [],
        "ordered_paper_ids": [
          "M06",
          "M10",
          "M13",
          "M31",
          "M25",
          "M26",
          "M16",
          "M34",
          "M38"
        ]
      }
    },
    {
      "check": "eight unique DOI references",
      "pass": true,
      "detail": [
        "10.1016/j.ijsolstr.2013.03.013",
        "10.1080/15376494.2021.1955313",
        "10.1109/LRA.2021.3097255",
        "10.1109/LRA.2022.3174363",
        "10.1109/TCST.2026.3690756",
        "10.3390/act13020064",
        "10.3390/mi12050520",
        "10.5194/ms-17-481-2026"
      ]
    },
    {
      "check": "citations resolve and first occurrence order",
      "pass": true,
      "detail": {
        "body": 17,
        "glossary": 1,
        "all": 18,
        "first_occurrence": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9
        ]
      }
    },
    {
      "check": "twelve complete nested gap adjudications preserve canonical status",
      "pass": true,
      "detail": {
        "count": 12,
        "local_status_counts": {
          "CLOSED": 1,
          "NOT_A_RESEARCH_GAP": 2,
          "CONDITIONAL_OPEN": 5,
          "ALREADY_PARTIALLY_ADDRESSED": 3,
          "NOT_ESTABLISHED_IN_CORPUS": 1
        },
        "errors": [],
        "extra_nested_fields": "manuscript_anchor and manuscript_location exactly match their parent trace row"
      }
    },
    {
      "check": "ZIP integrity and all XML parse",
      "pass": true,
      "detail": {
        "zip_bad_member": null,
        "xml_errors": []
      }
    },
    {
      "check": "native glossary nine terms three columns header repeat no row split",
      "pass": true,
      "detail": {
        "native_tables": 1,
        "rows_including_header": 10,
        "columns": 3,
        "repeat_headers": 1,
        "no_split_rows": 10
      }
    },
    {
      "check": "A4 page dimensions",
      "pass": true,
      "detail": [
        {
          "w": "11906",
          "h": "16838"
        }
      ]
    },
    {
      "check": "intended typography body TNR12 glossary TNR10",
      "pass": true,
      "detail": {
        "body_and_references_pt": 12,
        "glossary_pt": 10,
        "family": "Times New Roman",
        "errors": [],
        "scope_clarification": "Root confirms user A7 requires prose12; glossary10 preserves accepted §2.6.2 baseline."
      }
    },
    {
      "check": "Word has no internal markers or hypothesis IDs",
      "pass": true,
      "detail": {}
    },
    {
      "check": "no section 2.6.4 content beyond transition pointer",
      "pass": true,
      "detail": [
        "Khoảng trống có thể kiểm chứng được giữ ở mức câu hỏi có điều kiện về chuỗi áp suất–tiếp xúc–uốn và mức đầy đủ của mô hình đối với một cấu hình được xác định rõ, với khả năng kết luận bị thu hẹp nếu dữ liệu không phân biệt được các giải thích. Từ phạm vi đó, §2.6.4 sẽ xem xét các yêu cầu chuyển sang kiểm chứng."
      ]
    },
    {
      "check": "no equations or figures",
      "pass": true,
      "detail": {
        "OMML": 0,
        "drawings_or_picts": 0,
        "body_equal_signs": 0
      }
    },
    {
      "check": "all statically recomputable claimed counts match",
      "pass": true,
      "detail": {
        "matched_fields": 25
      }
    },
    {
      "check": "final rebuild bounded recheck",
      "pass": true,
      "detail": {
        "docx_sha256": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d",
        "all_54_anchors_checked": true,
        "legacy_limitation_field_values": {
          "NOT_APPLICABLE_SECTION_2_6_3": 54
        },
        "keepTogether_P06_P11": true,
        "approved_content_identical": true,
        "errors": []
      }
    }
  ],
  "issues": [],
  "not_certified": {
    "source_reading_activity_counts": {
      "verified_content_pdfs": 9,
      "verified_metadata_pdfs": 1,
      "verified_pdfs": 10,
      "unverified_used_pdfs": 0,
      "methodology_pdf_opened_excluded": 1
    },
    "reason": "Historical PDF-opening/verification activity cannot be independently recomputed from these seven deliverables. Content and visual verification remain root responsibilities.",
    "PDF_rendering": "NOT_PERFORMED",
    "LibreOffice_visual_review": "NOT_PERFORMED",
    "scientific_novelty_or_protocol_approval": "NOT_GRANTED"
  },
  "final_recheck_note": "All source files read-only. The root confirms only layout and inherited limitation-label edits; content hashes on this report identify the exact checked artifacts. No PDF content reread or visual/layout certification."
}
```

## SEVEN_GATE_RESULT

| Gate | Status |
|---|---|
| GATE_1 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_2 | PASS |
| GATE_3 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_4 | PASS |
| GATE_5 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_6 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_7 | PASS_WITH_DOCUMENTED_LIMITATIONS |

Checklist đầy đủ, METHOD/EVIDENCE/COUNT/FINDINGS/SEVERITY/UNRESOLVED/STATUS cho từngGate nằm trongMP1_CH2_2_6_3_7_GATE_REVIEW.md. KhôngcopyPASSbaseline.

## UNRESOLVED_FINDINGS / PENDING_HUMAN_DECISIONS

P1_UNRESOLVED: NONE_IDENTIFIED_WITHIN_SELF_REVIEW
P2_UNRESOLVED: NONE_IDENTIFIED_WITHIN_SELF_REVIEW
MINOR: NONE_IDENTIFIED_REMAINING; khôngđồngnghĩabảothẩmđịnhkhôngthểcònlỗi.

Các giới hạn hợp lệ còn mở:

1. AUTHOR_APPROVAL-01: người nghiên cứu/người hướng dẫn chưa phê duyệt khunggap cuối sau quyết địnhtopology/measurement.
2. RQ_MAPPING-01: 5RQPDF và4nhómP3chưađược reconciliation; giữ cảhai, chỉmaptạm.
3. OUTLINE-01: DOCXgốc khácPDF/WEP, không âm thầmcoicùngphiênbản.
4. META-01: M25/M26finalpagination từM28nộibộ; issuekhôngxácminh thìbỏ. Khôngpublisherfinalmetadata/Crossrefmới.
5. SOURCE-01: tasksource-selectednarrativereview,khôngsystematiccompleteness hoặc kiểmđộc lập39PDF/toànproof/rawdata.
6. APPLICABILITY-01: khôngdữliệuMP1đểchốtlocalpressure/contactslip/modeladequacy;missingobservationskhôngprovenimpossibility.
7. MSWORD-01: LibreOfficevisualPASS,MicrosoftWordNOT_VERIFIED;ứngdụng/fontkhác cóthểdàntrangkhác.
8. INPUT_ATIME: chỉ checksumcontent đượckiểm,atime không được snapshot.

Năm nhóm quyết định không tự chốt: topology/giao diện và hướng phản lực; biểu diễn/quan sát pháp tuyến cục bộ; miềnnhiệt/pha/tốcđộ/lịchsửTiNi;metricđộcứng/bấtđịnh;phạm viSMA–piston. RQreconciliation là việcphêduyệtbổsung, khôngđếmthànhgap khoa học. Khôngchọnsensor/tolerance/sốmẫu/geometry hoặc khóaBenchprotocol.

## FILES_CREATED

- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx
- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv
- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv
- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md
- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md

Đúng5finalfiles. KhôngrenderPDF/PNG/JSON/scriptthứ6trongoutputfinal. Cácnộidungnghiêncứu/provenancecầngiữđãđưaWord/CSV/report; dữliệutạm được dọn antoàn saukhikiểmcuối.

## GIT_CHANGE_SCOPE / COMMIT_STATUS / PUSH_STATUS

GIT_CHANGE_SCOPE: ONLY_FIVE_NEW_SECTION_2_6_3_FILES
COMMIT_STATUS: NOT_PERFORMED
PUSH_STATUS: NOT_PERFORMED
STAGE_STATUS: NOT_PERFORMED
PR_STATUS: NOT_PERFORMED
SECTION_2_6_4_STATUS: NOT_STARTED_BY_THIS_TASK

Gitstatusngoài5pathmới263đượcsovớisnapshottrước;gitdiffbinaryvàdiffcached giữ byteskhôngđổi. Cácfilemodified/untrackedcósẵn củauserkhôngbịxóa,sửa,revert. Khônggiảđịnhcópeer đangchạy264.

Preflightgitstatusentries: 343
PREFLIGHT_GIT_DIFF_SHA256: 6a5d7bf90c5c7973677a22d6c781178a2d43daf4d5383595fb3806ca4b6dc1ba
PREFLIGHT_GIT_CACHED_DIFF_SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
PREFLIGHT_GIT_STATUS_RAW_SHA256: 0a8fc6ad49cb542e07eef6b93997497902f9a365fa015ef308f923d6d0123695

<details><summary>Danh sách gitstatus có sẵn trước tác vụ</summary>

```text
 M outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py
 M outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md
?? .agents/skills.json
?? data/LR-FORMATED-rewrite.docx
?? data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md
?? data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md
?? data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md
?? data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md
?? data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt
?? data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt
?? data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt
?? data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt
?? data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt
?? data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt
?? data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt
?? data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt
?? data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt
?? data/chap1-2_citations/MANIFEST.json
?? data/chap1-2_citations/README.md
?? docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md
?? docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md
?? docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md
?? docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md
?? docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx
?? docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx
?? docs/project/almost done/LR-FORMATED.docx
?? docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md
?? docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md
?? literature review/LR-FORMATED-rewrite-outline-de-xuat.docx
?? literature review/LR-FORMATED-rewrite.docx
?? literature review/LR-FORMATED.docx
?? literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx
?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json
?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md
?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json
?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md
?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json
?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json
?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json
?? literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip
?? literature review/MP1_WRITING_EVIDENCE_FINAL.zip
?? literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv
?? literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv
?? literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md
?? literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md
?? literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md
?? literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv
?? literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv
?? literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md
?? literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md
?? literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md
?? literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md
?? literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md
?? literature review/ma-tran-tong-quan-tai-lieu.docx
?? literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json
?? literature review/~$-FORMATED-rewrite.docx
?? literature review/~$-FORMATED.docx
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/CLAIM_SOURCE_MAP.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/HIGHLIGHT_REGISTER.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/README.md
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S01_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S02_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S03_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S04_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05a_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05b_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S06_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S07_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S09_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S10_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S11_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S12_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S13_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S15_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S17_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S18_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S22_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/V-W02_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/VALIDATION.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curated_passages.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/inputs.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/package_highlights.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf_text_geometry.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/prepare_inputs.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S01_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S03_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S04_P5.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S07_P6.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S09_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S22_P71.png
?? outputs/literature/LR_CITATION_MATRIX_2026-10-14.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv
?? outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv
?? outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv
?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md
?? outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_8_CHAPTER_2_RELEASE_MANIFEST_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINALIZATION_CHANGELOG_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINAL_CITATION_REGISTER_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINAL_CLAIM_TRACEABILITY_2026-10-04.json
?? outputs/reports/MP1_GLOSSARY_C2_3_1_REPORT_2026-10-16.md
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/actual_docx_inventory.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/artifact_integrity_original.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/citation_appearances_original.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/inspect_artifact.py
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05a_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05b_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S11_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/V-W02_crossref.json
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv
```

</details>

## INPUT_HASH_MANIFEST_BEFORE_AFTER

418input/support/pre-existingdirtyfiles được kiểm bytestrước/sau;fileZone.Identifier làphụWindows, khôngnguồnhọc thuật vàkhôngtính làfileđãđọcnộidung. Baseline31fileđãtáchbảngtrên. Khôngsuy sốmanifestthànhsốnguồnđãkiểm.

```json
{
  "/home/khanh/projects/mechanical-research-agents/.agents/skills.json": {
    "before": "5a932ffcd3c3c31ebb6d0353d8a381a1f5cb3d470ab372309097a16c73e89acb",
    "after": "5a932ffcd3c3c31ebb6d0353d8a381a1f5cb3d470ab372309097a16c73e89acb"
  },
  "/home/khanh/projects/mechanical-research-agents/data/LR-FORMATED-rewrite.docx": {
    "before": "7bff33afc673816984cbe417bcf513e2fbafd9243301de3aa37ff57c4102eee5",
    "after": "7bff33afc673816984cbe417bcf513e2fbafd9243301de3aa37ff57c4102eee5"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv": {
    "before": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
    "after": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv": {
    "before": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
    "after": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md": {
    "before": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
    "after": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md": {
    "before": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
    "after": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md": {
    "before": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
    "after": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv": {
    "before": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
    "after": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv": {
    "before": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
    "after": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md": {
    "before": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
    "after": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md": {
    "before": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
    "after": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md": {
    "before": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
    "after": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md": {
    "before": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
    "after": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md": {
    "before": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
    "after": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf": {
    "before": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0",
    "after": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf": {
    "before": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b",
    "after": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf": {
    "before": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2",
    "after": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf": {
    "before": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12",
    "after": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf": {
    "before": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7",
    "after": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf": {
    "before": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
    "after": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.pdf": {
    "before": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5",
    "after": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt": {
    "before": "f75d24bd867f9b5f9ac749f607f43f6c657f57d95517f3a7258127dac8f82db7",
    "after": "f75d24bd867f9b5f9ac749f607f43f6c657f57d95517f3a7258127dac8f82db7"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf": {
    "before": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933",
    "after": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt": {
    "before": "32cbdee2a368ec60d02d949c36791624d4de4106778945b9ac95cd190af41db1",
    "after": "32cbdee2a368ec60d02d949c36791624d4de4106778945b9ac95cd190af41db1"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": {
    "before": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
    "after": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt": {
    "before": "1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db",
    "after": "1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": {
    "before": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
    "after": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt": {
    "before": "413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac",
    "after": "413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf": {
    "before": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827",
    "after": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt": {
    "before": "5b3cbae0cb08f21b907c572a04df5a36312b08cc4c9e9701440ddbceb3421d8f",
    "after": "5b3cbae0cb08f21b907c572a04df5a36312b08cc4c9e9701440ddbceb3421d8f"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": {
    "before": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
    "after": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": {
    "before": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
    "after": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt": {
    "before": "ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d",
    "after": "ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf": {
    "before": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807",
    "after": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt": {
    "before": "1fbd2bb1fe12bf775f2c82229ab5f3a692d255fc86dc4dc60f32aea4c2676837",
    "after": "1fbd2bb1fe12bf775f2c82229ab5f3a692d255fc86dc4dc60f32aea4c2676837"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf": {
    "before": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63",
    "after": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf": {
    "before": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a",
    "after": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf": {
    "before": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee",
    "after": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt": {
    "before": "89fede501f2cd30bff4b6532d7ba4584556f8434738a67a4416d3caef3c473a7",
    "after": "89fede501f2cd30bff4b6532d7ba4584556f8434738a67a4416d3caef3c473a7"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M18__2025-A continuum-based model for a layer jamming beam.pdf": {
    "before": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
    "after": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M19__2025-Toward a deeper understanding of layer jamming structures.pdf": {
    "before": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
    "after": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M20__2025-Continuum modeling for layer jamming structures.pdf": {
    "before": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
    "after": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M21__An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf": {
    "before": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752",
    "after": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf": {
    "before": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe",
    "after": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M23__2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf": {
    "before": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a",
    "after": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.pdf": {
    "before": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
    "after": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt": {
    "before": "db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2",
    "after": "db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M25__A3-2022-Mechanical response of single and double-helix.pdf": {
    "before": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
    "after": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": {
    "before": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
    "after": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M27__2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": {
    "before": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
    "after": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": {
    "before": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
    "after": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M29__2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": {
    "before": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
    "after": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M30__A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": {
    "before": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
    "after": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf": {
    "before": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03",
    "after": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M32__2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": {
    "before": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
    "after": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M33__2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": {
    "before": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
    "after": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": {
    "before": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
    "after": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M35__A5-Cable vibration considering internal friction.pdf": {
    "before": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
    "after": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M36__2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": {
    "before": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
    "after": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M37__2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": {
    "before": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
    "after": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf": {
    "before": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c",
    "after": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf": {
    "before": "24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a",
    "after": "24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/MANIFEST.json": {
    "before": "9d3c70e3a1f267c51fb87a77f504f6eb2e0d99d3dbd2ccc14b557aad9e017eda",
    "after": "9d3c70e3a1f267c51fb87a77f504f6eb2e0d99d3dbd2ccc14b557aad9e017eda"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/README.md": {
    "before": "a82bd095dbbd8ec46c5576bec7f3870bc86d64f7748a7767d6a7306993eb4f7c",
    "after": "a82bd095dbbd8ec46c5576bec7f3870bc86d64f7748a7767d6a7306993eb4f7c"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md": {
    "before": "a948bd201fda61b29de142e40a95606cf47a7c83d05c2a81e7683db371e9453c",
    "after": "a948bd201fda61b29de142e40a95606cf47a7c83d05c2a81e7683db371e9453c"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md": {
    "before": "4dd71b45f52a0e5bb18f92c3a76064aa4e395bc4a9feee19f827d6f463140f08",
    "after": "4dd71b45f52a0e5bb18f92c3a76064aa4e395bc4a9feee19f827d6f463140f08"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md": {
    "before": "e5650636b3c8858394b619bf3f06386b65a9827bdf8e73d18f777144d57d6f7c",
    "after": "e5650636b3c8858394b619bf3f06386b65a9827bdf8e73d18f777144d57d6f7c"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md": {
    "before": "2d26d9cbd7883442428585de82b53b320f28a275937f94d724097a61723ac166",
    "after": "2d26d9cbd7883442428585de82b53b320f28a275937f94d724097a61723ac166"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx": {
    "before": "833344a5d64632ff9336832dbfccb2a8ae98dec45df046278e26d229b189ca9b",
    "after": "833344a5d64632ff9336832dbfccb2a8ae98dec45df046278e26d229b189ca9b"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx": {
    "before": "3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45",
    "after": "3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/project/almost done/LR-FORMATED.docx": {
    "before": "a63016590d98ff10636895166307603e2b3095ee5b632a30891b71c21190986c",
    "after": "a63016590d98ff10636895166307603e2b3095ee5b632a30891b71c21190986c"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md": {
    "before": "af57cc6a53c38ea430b4369d6afe7df86f61956d3320d7ce3977f957f5de3145",
    "after": "af57cc6a53c38ea430b4369d6afe7df86f61956d3320d7ce3977f957f5de3145"
  },
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md": {
    "before": "f53f896801113150bd83e84d6c68dd542804fc65a619ae34fd568e7f7c276a99",
    "after": "f53f896801113150bd83e84d6c68dd542804fc65a619ae34fd568e7f7c276a99"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/LR-FORMATED-rewrite-outline-de-xuat.docx": {
    "before": "3053b2649293ac1841de835a15687392beef1648a5de26faf6f78b5b3d78b0e4",
    "after": "3053b2649293ac1841de835a15687392beef1648a5de26faf6f78b5b3d78b0e4"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/LR-FORMATED-rewrite.docx": {
    "before": "ee5b700f8dc6701eea44dd4679519049fa95d45a299b39ed411a58793ca3652d",
    "after": "ee5b700f8dc6701eea44dd4679519049fa95d45a299b39ed411a58793ca3652d"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/LR-FORMATED.docx": {
    "before": "d61c30a5973f3bd2f0314bcb3df253fe1707ad4dedfeb2bf1f76a5d895eb8a1c",
    "after": "d61c30a5973f3bd2f0314bcb3df253fe1707ad4dedfeb2bf1f76a5d895eb8a1c"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx": {
    "before": "e41e3638abfd27d3c7b7f60c538cbecf719651d22fa8efd27da8ee2b4b52ef26",
    "after": "e41e3638abfd27d3c7b7f60c538cbecf719651d22fa8efd27da8ee2b4b52ef26"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json": {
    "before": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84",
    "after": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md": {
    "before": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f",
    "after": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json": {
    "before": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51",
    "after": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md": {
    "before": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131",
    "after": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json": {
    "before": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c",
    "after": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json": {
    "before": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435",
    "after": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json": {
    "before": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc",
    "after": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip": {
    "before": "d2128a711f4c3a2be4bb0841415f532413c462a0aeafed0b3321d7f3713194b3",
    "after": "d2128a711f4c3a2be4bb0841415f532413c462a0aeafed0b3321d7f3713194b3"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv": {
    "before": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
    "after": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv": {
    "before": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
    "after": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md": {
    "before": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
    "after": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md": {
    "before": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
    "after": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md": {
    "before": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
    "after": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv": {
    "before": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
    "after": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv": {
    "before": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
    "after": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md": {
    "before": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
    "after": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md": {
    "before": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
    "after": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md": {
    "before": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
    "after": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md": {
    "before": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
    "after": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md": {
    "before": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
    "after": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/MP1_WRITING_EVIDENCE_FINAL.zip": {
    "before": "d33cbdddda00f38e63c2bbec38658d4c13f183b026f2442a361f2fbc2ea141af",
    "after": "d33cbdddda00f38e63c2bbec38658d4c13f183b026f2442a361f2fbc2ea141af"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/ma-tran-tong-quan-tai-lieu.docx": {
    "before": "ead3fb5c00004f7444545d622760430673a7bd787c84df456d8239ad4823bfc9",
    "after": "ead3fb5c00004f7444545d622760430673a7bd787c84df456d8239ad4823bfc9"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json": {
    "before": "c26a9c15561b3f9c58d175f4197e074b7a833faa9533cf6f9240f302cea497a2",
    "after": "c26a9c15561b3f9c58d175f4197e074b7a833faa9533cf6f9240f302cea497a2"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/~$-FORMATED-rewrite.docx": {
    "before": "9e62bab38175dd43e2235fd8e880726f73509c57fb3f36fce2c7a0b3776f0dd2",
    "after": "9e62bab38175dd43e2235fd8e880726f73509c57fb3f36fce2c7a0b3776f0dd2"
  },
  "/home/khanh/projects/mechanical-research-agents/literature review/~$-FORMATED.docx": {
    "before": "84e28127f73d6d6e2ef9b1d4a7838978fc4dc03cb00b586b7ff687a3c39828f3",
    "after": "84e28127f73d6d6e2ef9b1d4a7838978fc4dc03cb00b586b7ff687a3c39828f3"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/CLAIM_SOURCE_MAP.json": {
    "before": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84",
    "after": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md": {
    "before": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f",
    "after": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/HIGHLIGHT_REGISTER.json": {
    "before": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51",
    "after": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip": {
    "before": "6f40ffb40b5fbc3aaa381d20f28c12b87f39111faf877e046aff27326eb97de1",
    "after": "6f40ffb40b5fbc3aaa381d20f28c12b87f39111faf877e046aff27326eb97de1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json": {
    "before": "45bfdd81445f9ad3c95f1fc50bb4bc9140b25d0b422ac91f23e6565074a834c3",
    "after": "45bfdd81445f9ad3c95f1fc50bb4bc9140b25d0b422ac91f23e6565074a834c3"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/README.md": {
    "before": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131",
    "after": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S01_search_text.txt": {
    "before": "4c6b07960eec03bee4baf0582065e2cd5c3cdcaed357ee7a66c42d71e79b09a5",
    "after": "4c6b07960eec03bee4baf0582065e2cd5c3cdcaed357ee7a66c42d71e79b09a5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S02_search_text.txt": {
    "before": "02f77f8e301d4045d31e7fcd579badd261c34ef8148a96519b3bb88d36f74f41",
    "after": "02f77f8e301d4045d31e7fcd579badd261c34ef8148a96519b3bb88d36f74f41"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S03_search_text.txt": {
    "before": "356de27f1e83ccb27a37f1ffd9be9321ca7887db1288d45c1adc1a5cf83ca1e9",
    "after": "356de27f1e83ccb27a37f1ffd9be9321ca7887db1288d45c1adc1a5cf83ca1e9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S04_search_text.txt": {
    "before": "f47ba51263ffb69505356db6455a781730d7d01ab48bfdb214e793b1d434b6cb",
    "after": "f47ba51263ffb69505356db6455a781730d7d01ab48bfdb214e793b1d434b6cb"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05a_search_text.txt": {
    "before": "982911acc87b715ead5ddcafa25f73f50937f92276417358c99ae1bbb9f4b11f",
    "after": "982911acc87b715ead5ddcafa25f73f50937f92276417358c99ae1bbb9f4b11f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05b_search_text.txt": {
    "before": "0938ee9bef68cc3f7f8231129e6e383871065c16595b8d46f12331326e6b1942",
    "after": "0938ee9bef68cc3f7f8231129e6e383871065c16595b8d46f12331326e6b1942"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S06_search_text.txt": {
    "before": "a1fafc05606f28715e59d86fc646c5151f28501dda722056b60ffbfb289b4b63",
    "after": "a1fafc05606f28715e59d86fc646c5151f28501dda722056b60ffbfb289b4b63"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S07_search_text.txt": {
    "before": "e661bd66ac3bc591d25d133ce7b5185f9290fafa2121a4ccff4c22be44ff9057",
    "after": "e661bd66ac3bc591d25d133ce7b5185f9290fafa2121a4ccff4c22be44ff9057"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S09_search_text.txt": {
    "before": "9045945be238ffc81d121d178485e1fcb5bf478e0b8f6b8492c0e9dc6a7a4936",
    "after": "9045945be238ffc81d121d178485e1fcb5bf478e0b8f6b8492c0e9dc6a7a4936"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S10_search_text.txt": {
    "before": "6640478481b84b7c5aa93656f82e646bf333ead8ba6afa5c612a14e93397dbb0",
    "after": "6640478481b84b7c5aa93656f82e646bf333ead8ba6afa5c612a14e93397dbb0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S11_search_text.txt": {
    "before": "29ee1cd95525b8e187408d9588156039a1b3f635e9a608dd3c43a9a9167ef147",
    "after": "29ee1cd95525b8e187408d9588156039a1b3f635e9a608dd3c43a9a9167ef147"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S12_search_text.txt": {
    "before": "b6e8d5f5195364f3c9fbbedfde63460bc3beac3706bd9929e5aec1d06b3bef55",
    "after": "b6e8d5f5195364f3c9fbbedfde63460bc3beac3706bd9929e5aec1d06b3bef55"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S13_search_text.txt": {
    "before": "d614f809da314316213905d05e8242736841de9f01cecaf04ec9b6fe61291c2d",
    "after": "d614f809da314316213905d05e8242736841de9f01cecaf04ec9b6fe61291c2d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S15_search_text.txt": {
    "before": "7f694619b4377fc61b1a00fe3435945651983296b8c5e83f47f971734f70bc2f",
    "after": "7f694619b4377fc61b1a00fe3435945651983296b8c5e83f47f971734f70bc2f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S17_search_text.txt": {
    "before": "5e36642dbc07e11c2c93dfa8c50e0c33efdf80d677fa8dc98ab1f1e8d0014d8c",
    "after": "5e36642dbc07e11c2c93dfa8c50e0c33efdf80d677fa8dc98ab1f1e8d0014d8c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S18_search_text.txt": {
    "before": "f83f01d5c89461a62c290e1238bdba1d0be5d566a4d10162849a72cee905c610",
    "after": "f83f01d5c89461a62c290e1238bdba1d0be5d566a4d10162849a72cee905c610"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S22_search_text.txt": {
    "before": "3f86f47c7a279935989a13297c5f17eaa4a5b5c819ca1935ca96513265d6b895",
    "after": "3f86f47c7a279935989a13297c5f17eaa4a5b5c819ca1935ca96513265d6b895"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/V-W02_search_text.txt": {
    "before": "7a5b5bed75fe60dc1eb36eec69f5e19c4ab5a3a9e7a1fb69b107f6e4aa61a71a",
    "after": "7a5b5bed75fe60dc1eb36eec69f5e19c4ab5a3a9e7a1fb69b107f6e4aa61a71a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/VALIDATION.json": {
    "before": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c",
    "after": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py": {
    "before": "d7e2b3eb9c9cb70dcf9ec6bcd4291edd683bce4220b172177a3ec0271543aed4",
    "after": "d7e2b3eb9c9cb70dcf9ec6bcd4291edd683bce4220b172177a3ec0271543aed4"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py": {
    "before": "cd0bd1d5437f2e3f2f43a13d0e55abb9c3fe583bb4637256fa62314431603320",
    "after": "cd0bd1d5437f2e3f2f43a13d0e55abb9c3fe583bb4637256fa62314431603320"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curated_passages.json": {
    "before": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435",
    "after": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/inputs.json": {
    "before": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc",
    "after": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/package_highlights.py": {
    "before": "d12846bf434cae00cdd88aa4907ab1b498b419cb600ca1500d11b470bb7fb416",
    "after": "d12846bf434cae00cdd88aa4907ab1b498b419cb600ca1500d11b470bb7fb416"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf_text_geometry.json": {
    "before": "fc09e94857f1dae49ba360d749a72483513a380ea08427ed4b87620c7830a750",
    "after": "fc09e94857f1dae49ba360d749a72483513a380ea08427ed4b87620c7830a750"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/prepare_inputs.py": {
    "before": "0106dbcd0cc378824724a1b5acec9e287387372aebc7a2566ca6cd13fca648a3",
    "after": "0106dbcd0cc378824724a1b5acec9e287387372aebc7a2566ca6cd13fca648a3"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S01_P9.png": {
    "before": "35ed651167faff4e3aa4efd2a8fc56c8adc91e2ca81eb17a05cd27a23b2979be",
    "after": "35ed651167faff4e3aa4efd2a8fc56c8adc91e2ca81eb17a05cd27a23b2979be"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S03_P9.png": {
    "before": "db5a71d9a613da2e51976c5a80f7a6b9e94237506c5b2bd4b07971d69947145c",
    "after": "db5a71d9a613da2e51976c5a80f7a6b9e94237506c5b2bd4b07971d69947145c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S04_P5.png": {
    "before": "0ce4fa6d45c23b437747406f90f8f62ddb640ef4cb44c0faa02cbaba1ac4d175",
    "after": "0ce4fa6d45c23b437747406f90f8f62ddb640ef4cb44c0faa02cbaba1ac4d175"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S07_P6.png": {
    "before": "8080514df725ffb4dee57fe6caad48ae52a6cb5c108d2cdfed3d48317cbd740c",
    "after": "8080514df725ffb4dee57fe6caad48ae52a6cb5c108d2cdfed3d48317cbd740c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S09_P9.png": {
    "before": "9e9634334a7019114182b8ff182ae197d38ec13498d3b5d936dec9b5fd3b61ec",
    "after": "9e9634334a7019114182b8ff182ae197d38ec13498d3b5d936dec9b5fd3b61ec"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S22_P71.png": {
    "before": "e6d0f7e7de7fb3922397919cb5949365433f63fe78b5bbdd92c0d689d037eead",
    "after": "e6d0f7e7de7fb3922397919cb5949365433f63fe78b5bbdd92c0d689d037eead"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/LR_CITATION_MATRIX_2026-10-14.md": {
    "before": "2bb833a7bbb3dc0d77521e81ca68445af0d4b455e099994ff2acde9e7c1aab2a",
    "after": "2bb833a7bbb3dc0d77521e81ca68445af0d4b455e099994ff2acde9e7c1aab2a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md": {
    "before": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2",
    "after": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv": {
    "before": "942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6",
    "after": "942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md": {
    "before": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79",
    "after": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md": {
    "before": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8",
    "after": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md": {
    "before": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2",
    "after": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md": {
    "before": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406",
    "after": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json": {
    "before": "0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06",
    "after": "0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md": {
    "before": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38",
    "after": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md": {
    "before": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7",
    "after": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json": {
    "before": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1",
    "after": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json": {
    "before": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7",
    "after": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md": {
    "before": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da",
    "after": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md": {
    "before": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e",
    "after": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv": {
    "before": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9",
    "after": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md": {
    "before": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5",
    "after": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv": {
    "before": "3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23",
    "after": "3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md": {
    "before": "5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e",
    "after": "5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv": {
    "before": "2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9",
    "after": "2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md": {
    "before": "1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a",
    "after": "1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md": {
    "before": "6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca",
    "after": "6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md": {
    "before": "c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02",
    "after": "c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md": {
    "before": "a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037",
    "after": "a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md": {
    "before": "227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72",
    "after": "227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md": {
    "before": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d",
    "after": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv": {
    "before": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34",
    "after": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl": {
    "before": "a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba",
    "after": "a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md": {
    "before": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1",
    "after": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md": {
    "before": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a",
    "after": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md": {
    "before": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d",
    "after": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md": {
    "before": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996",
    "after": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md": {
    "before": "59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde",
    "after": "59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md": {
    "before": "86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059",
    "after": "86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md": {
    "before": "2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d",
    "after": "2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md": {
    "before": "da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a",
    "after": "da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md": {
    "before": "7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864",
    "after": "7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md": {
    "before": "76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f",
    "after": "76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md": {
    "before": "f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c",
    "after": "f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md": {
    "before": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101",
    "after": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md": {
    "before": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907",
    "after": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md": {
    "before": "99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8",
    "after": "99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip": {
    "before": "fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e",
    "after": "fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md": {
    "before": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a",
    "after": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv": {
    "before": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be",
    "after": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl": {
    "before": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033",
    "after": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md": {
    "before": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda",
    "after": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md": {
    "before": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09",
    "after": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md": {
    "before": "9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65",
    "after": "9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md": {
    "before": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba",
    "after": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md": {
    "before": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087",
    "after": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md": {
    "before": "c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec",
    "after": "c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md": {
    "before": "fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2",
    "after": "fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md": {
    "before": "d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160",
    "after": "d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md": {
    "before": "6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80",
    "after": "6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md": {
    "before": "37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844",
    "after": "37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md": {
    "before": "6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46",
    "after": "6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md": {
    "before": "58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11",
    "after": "58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md": {
    "before": "2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf",
    "after": "2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md": {
    "before": "77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930",
    "after": "77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md": {
    "before": "4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d",
    "after": "4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md": {
    "before": "561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a",
    "after": "561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md": {
    "before": "b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad",
    "after": "b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md": {
    "before": "0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad",
    "after": "0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md": {
    "before": "99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d",
    "after": "99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md": {
    "before": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213",
    "after": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json": {
    "before": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6",
    "after": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md": {
    "before": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1",
    "after": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip": {
    "before": "fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14",
    "after": "fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md": {
    "before": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109",
    "after": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv": {
    "before": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7",
    "after": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv": {
    "before": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0",
    "after": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl": {
    "before": "a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2",
    "after": "a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md": {
    "before": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753",
    "after": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md": {
    "before": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed",
    "after": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md": {
    "before": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7",
    "after": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md": {
    "before": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c",
    "after": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md": {
    "before": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8",
    "after": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md": {
    "before": "287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151",
    "after": "287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md": {
    "before": "0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284",
    "after": "0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md": {
    "before": "f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee",
    "after": "f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md": {
    "before": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034",
    "after": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md": {
    "before": "5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a",
    "after": "5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md": {
    "before": "31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c",
    "after": "31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md": {
    "before": "2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344",
    "after": "2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md": {
    "before": "0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a",
    "after": "0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md": {
    "before": "98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8",
    "after": "98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md": {
    "before": "3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c",
    "after": "3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md": {
    "before": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6",
    "after": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md": {
    "before": "65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05",
    "after": "65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md": {
    "before": "4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894",
    "after": "4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip": {
    "before": "ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4",
    "after": "ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md": {
    "before": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2",
    "after": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv": {
    "before": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2",
    "after": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl": {
    "before": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd",
    "after": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md": {
    "before": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2",
    "after": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md": {
    "before": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09",
    "after": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md": {
    "before": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0",
    "after": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md": {
    "before": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79",
    "after": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json": {
    "before": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3",
    "after": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md": {
    "before": "a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f",
    "after": "a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md": {
    "before": "a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195",
    "after": "a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md": {
    "before": "d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24",
    "after": "d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md": {
    "before": "613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8",
    "after": "613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md": {
    "before": "4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf",
    "after": "4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md": {
    "before": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6",
    "after": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip": {
    "before": "9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c",
    "after": "9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md": {
    "before": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513",
    "after": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv": {
    "before": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd",
    "after": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl": {
    "before": "e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c",
    "after": "e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md": {
    "before": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1",
    "after": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md": {
    "before": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b",
    "after": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv": {
    "before": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e",
    "after": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md": {
    "before": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24",
    "after": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md": {
    "before": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8",
    "after": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md": {
    "before": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b",
    "after": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md": {
    "before": "e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d",
    "after": "e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md": {
    "before": "f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9",
    "after": "f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md": {
    "before": "bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca",
    "after": "bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md": {
    "before": "e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880",
    "after": "e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md": {
    "before": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40",
    "after": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md": {
    "before": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682",
    "after": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md": {
    "before": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003",
    "after": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json": {
    "before": "3bef4fb970e65913196e9772e22384dd5e7d040373afdef378eac78f81ac5b45",
    "after": "3bef4fb970e65913196e9772e22384dd5e7d040373afdef378eac78f81ac5b45"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json": {
    "before": "cd99c169e1f925756746d0e49422d30fd325b7c5ffb9191175bbf8a8970a2f3e",
    "after": "cd99c169e1f925756746d0e49422d30fd325b7c5ffb9191175bbf8a8970a2f3e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json": {
    "before": "4c43ba1f67921c857f0ab50190e227b1ad7221f6a9b6f0a15f5af9ca1c7ff0e8",
    "after": "4c43ba1f67921c857f0ab50190e227b1ad7221f6a9b6f0a15f5af9ca1c7ff0e8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json": {
    "before": "5a5bc1912919a022e37f5a544be7aec25880523ded14ae4b0455125a1ac045ae",
    "after": "5a5bc1912919a022e37f5a544be7aec25880523ded14ae4b0455125a1ac045ae"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_8_CHAPTER_2_RELEASE_MANIFEST_2026-10-04.json": {
    "before": "86bd644523dafbd66c4a887fdbcd4127f82986aa9d366d5c16b21255a7e56800",
    "after": "86bd644523dafbd66c4a887fdbcd4127f82986aa9d366d5c16b21255a7e56800"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_8_FINALIZATION_CHANGELOG_2026-10-04.json": {
    "before": "e6690ef5f0b214935e493597ecce089f780ed198f22fcc12346ce50f7759f558",
    "after": "e6690ef5f0b214935e493597ecce089f780ed198f22fcc12346ce50f7759f558"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_8_FINAL_CITATION_REGISTER_2026-10-04.json": {
    "before": "a5e7efaa88155129f27eec425caf7b83521c600e4c41d491932198aab0d8c6ed",
    "after": "a5e7efaa88155129f27eec425caf7b83521c600e4c41d491932198aab0d8c6ed"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/plans/MP1_R_PHASE_8_FINAL_CLAIM_TRACEABILITY_2026-10-04.json": {
    "before": "c3ea4d1eddc144cf8474746c0eed87262b1a4298589ff01ddfe181f8bf968cd2",
    "after": "c3ea4d1eddc144cf8474746c0eed87262b1a4298589ff01ddfe181f8bf968cd2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_GLOSSARY_C2_3_1_REPORT_2026-10-16.md": {
    "before": "25462069e0667a67ce680d3fbb3c6879a8d7959a8da3973e9a289706c9638ab3",
    "after": "25462069e0667a67ce680d3fbb3c6879a8d7959a8da3973e9a289706c9638ab3"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py": {
    "before": "d82086830d47d966856159e60eda1a083a65476353c5e3842866b464fcdbfad6",
    "after": "d82086830d47d966856159e60eda1a083a65476353c5e3842866b464fcdbfad6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md": {
    "before": "7c2154b025b7f260d3f4414c58e684e1a3e1289270be9e298a33557030025acf",
    "after": "7c2154b025b7f260d3f4414c58e684e1a3e1289270be9e298a33557030025acf"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/actual_docx_inventory.json": {
    "before": "45d74f31bb450ea97bf235c690bf08f83cd1829fcc64a2cde5df4ca7f2d52347",
    "after": "45d74f31bb450ea97bf235c690bf08f83cd1829fcc64a2cde5df4ca7f2d52347"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/artifact_integrity_original.json": {
    "before": "d72596925b96f026fdc73f37c2fdf870f30733cce5a27e916877e3c700be4c1d",
    "after": "d72596925b96f026fdc73f37c2fdf870f30733cce5a27e916877e3c700be4c1d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/citation_appearances_original.json": {
    "before": "38e8809b3de36209ac614c684f57331ce6e8d38e742cfb5105a46fc11dc56120",
    "after": "38e8809b3de36209ac614c684f57331ce6e8d38e742cfb5105a46fc11dc56120"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/inspect_artifact.py": {
    "before": "ac39da773a40c472040b723bc79649c01b913b6b4b0eb53dbe4b15da0cb8b21e",
    "after": "ac39da773a40c472040b723bc79649c01b913b6b4b0eb53dbe4b15da0cb8b21e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05a_crossref.json": {
    "before": "96fd249c10471dd90ed45041388c8700ff583a777a8307c6fd6dc9bba9f6e31b",
    "after": "96fd249c10471dd90ed45041388c8700ff583a777a8307c6fd6dc9bba9f6e31b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05b_crossref.json": {
    "before": "d88f96fd0dc2781302fc91ecdd5575c4609ee1f002bbf1c65b44d7be43a7af0f",
    "after": "d88f96fd0dc2781302fc91ecdd5575c4609ee1f002bbf1c65b44d7be43a7af0f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S11_crossref.json": {
    "before": "2058beabf11fbafc397818f2bc533cd6b70d4ca8fc94a9e57630b8845b2c34a9",
    "after": "2058beabf11fbafc397818f2bc533cd6b70d4ca8fc94a9e57630b8845b2c34a9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/V-W02_crossref.json": {
    "before": "c93b664692e0e539895548d87e7ac1d50689eb09654841c89f45bb5b2d0fde7c",
    "after": "c93b664692e0e539895548d87e7ac1d50689eb09654841c89f45bb5b2d0fde7c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md": {
    "before": "402f6fc7c9d279b6b0c1fb6af3d72c5d42d131eeb0d8994a61c71c21cbc902cb",
    "after": "402f6fc7c9d279b6b0c1fb6af3d72c5d42d131eeb0d8994a61c71c21cbc902cb"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx": {
    "before": "6ded97f12de61cde7be319c865c3ea40cc6cbdc8d04e00cc648530ec718311a0",
    "after": "6ded97f12de61cde7be319c865c3ea40cc6cbdc8d04e00cc648530ec718311a0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md": {
    "before": "91947d11eea09cac56f882936218d690458b1cbbbe431bd7f854be6a172ac9b7",
    "after": "91947d11eea09cac56f882936218d690458b1cbbbe431bd7f854be6a172ac9b7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv": {
    "before": "08202df03396abf83a4d320b56bd91abface6535c0379c1b75ec0c4ff89f3649",
    "after": "08202df03396abf83a4d320b56bd91abface6535c0379c1b75ec0c4ff89f3649"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv": {
    "before": "f917c23d7dc2a404dbbbfa38874ede6dd10a50fac598cf7e3cfd880fdce83a2f",
    "after": "f917c23d7dc2a404dbbbfa38874ede6dd10a50fac598cf7e3cfd880fdce83a2f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md": {
    "before": "4ca60c29585ed5a364ae526397fe7120976a3912ea9342996ba105f05e56e9ba",
    "after": "4ca60c29585ed5a364ae526397fe7120976a3912ea9342996ba105f05e56e9ba"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx": {
    "before": "7f614d06edca11ae573f27aeb5d277e5e7d74f3dc1d6ec9978dbe43f1795c8fb",
    "after": "7f614d06edca11ae573f27aeb5d277e5e7d74f3dc1d6ec9978dbe43f1795c8fb"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md": {
    "before": "b6e59281460fcf9a88df683bebcebef1007c232ce9497da1ce3952b46402f622",
    "after": "b6e59281460fcf9a88df683bebcebef1007c232ce9497da1ce3952b46402f622"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv": {
    "before": "ec210ec6bf5bd02798db60db8a9366b3981efc23a9ddff0303051d7220f2523f",
    "after": "ec210ec6bf5bd02798db60db8a9366b3981efc23a9ddff0303051d7220f2523f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv": {
    "before": "287da4a23314f4a98d0ce9a9bbd84946ec235af7fd6a147e95f02b85e81f4984",
    "after": "287da4a23314f4a98d0ce9a9bbd84946ec235af7fd6a147e95f02b85e81f4984"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md": {
    "before": "557429b44c0a0dfb8036e3aa734c8bcffc04bafbfd0be6f47bda207148ff3531",
    "after": "557429b44c0a0dfb8036e3aa734c8bcffc04bafbfd0be6f47bda207148ff3531"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx": {
    "before": "1727dd0eeb32da84135d094f34c443605060cfd3fa39d269d85f855ce731b563",
    "after": "1727dd0eeb32da84135d094f34c443605060cfd3fa39d269d85f855ce731b563"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md": {
    "before": "757ba0ea8e15d71d2a9bbe2ba1bc2add412122ef610753b898871038a109bfc4",
    "after": "757ba0ea8e15d71d2a9bbe2ba1bc2add412122ef610753b898871038a109bfc4"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv": {
    "before": "c075ca7049f5cb81ea7fe997a9f29a0d0cc07971af52594f4560d2e659991826",
    "after": "c075ca7049f5cb81ea7fe997a9f29a0d0cc07971af52594f4560d2e659991826"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv": {
    "before": "d79fa7a1611883a9ad6dfb5d4f02a58622c48e7533d0efc20ea4e3bd04b3bb76",
    "after": "d79fa7a1611883a9ad6dfb5d4f02a58622c48e7533d0efc20ea4e3bd04b3bb76"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md": {
    "before": "bfedc08e96e0163ce64b75a967f6327e42e49bee87dad55fcf522f9747ea22db",
    "after": "bfedc08e96e0163ce64b75a967f6327e42e49bee87dad55fcf522f9747ea22db"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx": {
    "before": "38be496eb71922f7165b916ac552f9b9bcb54dbfd94dc0f635acd55372ce793d",
    "after": "38be496eb71922f7165b916ac552f9b9bcb54dbfd94dc0f635acd55372ce793d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md": {
    "before": "7d3b803e0d690dacd49997861769e218186b6719f11c2337b5ebff813864bfb3",
    "after": "7d3b803e0d690dacd49997861769e218186b6719f11c2337b5ebff813864bfb3"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv": {
    "before": "7b3105acf012369a2c3a7ee4426ef66d457c874da38d2dd2d6fc8f518daed630",
    "after": "7b3105acf012369a2c3a7ee4426ef66d457c874da38d2dd2d6fc8f518daed630"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv": {
    "before": "735c2ad438e0a2ae0c05e83483ed51b6aeba2e49e372d59dc89bf6c6d9f1c223",
    "after": "735c2ad438e0a2ae0c05e83483ed51b6aeba2e49e372d59dc89bf6c6d9f1c223"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md": {
    "before": "15537e97652af58e55a85bf001a604205953111db06dafb17243f481f266eec1",
    "after": "15537e97652af58e55a85bf001a604205953111db06dafb17243f481f266eec1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx": {
    "before": "a7a46894a3384cc519cdea0ab6b957cbb5e8fb130dd9b2073678a6d5513546e4",
    "after": "a7a46894a3384cc519cdea0ab6b957cbb5e8fb130dd9b2073678a6d5513546e4"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md": {
    "before": "c0aed9db3f084398feda73059135071c66d453e204afe08ed7fb6eef78cc4c10",
    "after": "c0aed9db3f084398feda73059135071c66d453e204afe08ed7fb6eef78cc4c10"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv": {
    "before": "4c97bff4f998a10c465abde26731e236759599a17a32923a6459e6fc6bff73fa",
    "after": "4c97bff4f998a10c465abde26731e236759599a17a32923a6459e6fc6bff73fa"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv": {
    "before": "a86e1e9c781a788bea9de40bdb4a0186abf5a5f4c4382a74edeff02ad8ea6463",
    "after": "a86e1e9c781a788bea9de40bdb4a0186abf5a5f4c4382a74edeff02ad8ea6463"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md": {
    "before": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed",
    "after": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv": {
    "before": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99",
    "after": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md": {
    "before": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e",
    "after": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx": {
    "before": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
    "after": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md": {
    "before": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034",
    "after": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv": {
    "before": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0",
    "after": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv": {
    "before": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be",
    "after": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md": {
    "before": "1191dfd41f394d76ed933c3805c69ad4be1a47ac69e4494f19743a414696136a",
    "after": "1191dfd41f394d76ed933c3805c69ad4be1a47ac69e4494f19743a414696136a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx": {
    "before": "a58cf37dee216f2e193f9ee607fa15ba4987cf49b66c4a884dab895172ebf6d4",
    "after": "a58cf37dee216f2e193f9ee607fa15ba4987cf49b66c4a884dab895172ebf6d4"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md": {
    "before": "9f60f4434b1699bc38ad23fbe7f5e7ae8c816957f4885caae3cd83dd6c0d5d7b",
    "after": "9f60f4434b1699bc38ad23fbe7f5e7ae8c816957f4885caae3cd83dd6c0d5d7b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv": {
    "before": "dacb3c6ad632a1ec7e3aab167f614cddaa00c7a76850506616060c332eac7890",
    "after": "dacb3c6ad632a1ec7e3aab167f614cddaa00c7a76850506616060c332eac7890"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv": {
    "before": "d9bcd231bfb43ed223b8db6b270060196d5f485aa9f848cc5459d64ae857ba91",
    "after": "d9bcd231bfb43ed223b8db6b270060196d5f485aa9f848cc5459d64ae857ba91"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md": {
    "before": "d87a902881e1d5d2161172d2db700c261a8ba653af2f7cff1722ea5213206e19",
    "after": "d87a902881e1d5d2161172d2db700c261a8ba653af2f7cff1722ea5213206e19"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx": {
    "before": "35a6842cd1513cb2ac91328ebadc1de0feacb2c6d421c5c4170d7ddce3c7e4e5",
    "after": "35a6842cd1513cb2ac91328ebadc1de0feacb2c6d421c5c4170d7ddce3c7e4e5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md": {
    "before": "72a9556ed438ef126da2d186add01b053970cae41df9b3e151d1b6e443621128",
    "after": "72a9556ed438ef126da2d186add01b053970cae41df9b3e151d1b6e443621128"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv": {
    "before": "f3778953f446e71e61ae192a3021b02407b13c35b11df2d30ab5914da49181dc",
    "after": "f3778953f446e71e61ae192a3021b02407b13c35b11df2d30ab5914da49181dc"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv": {
    "before": "ca606e7804945c1ac719f8088b4a9965525078033cced17e08364c45705a31b7",
    "after": "ca606e7804945c1ac719f8088b4a9965525078033cced17e08364c45705a31b7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md": {
    "before": "cb02fffbe114df41dd6068c908f8e53d5de323c296b2b43a903f33519c027832",
    "after": "cb02fffbe114df41dd6068c908f8e53d5de323c296b2b43a903f33519c027832"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx": {
    "before": "2ecd6ccd690b0285e3414faa52135aaeb2db738e3b69df773548a597a4230da2",
    "after": "2ecd6ccd690b0285e3414faa52135aaeb2db738e3b69df773548a597a4230da2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md": {
    "before": "932a5705b875d978a2158d4b1a590d4c2170cae3a60d4385a0b5cbc3b03466f4",
    "after": "932a5705b875d978a2158d4b1a590d4c2170cae3a60d4385a0b5cbc3b03466f4"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv": {
    "before": "4eaae31d939e4fe3a64c2ae2afac173eafa843a22f86d9d88befc62d14bc98c5",
    "after": "4eaae31d939e4fe3a64c2ae2afac173eafa843a22f86d9d88befc62d14bc98c5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv": {
    "before": "aa372e9fa39f91b4bfb04c9342831cd90e9ecd530c537c2361c35d45de1548c5",
    "after": "aa372e9fa39f91b4bfb04c9342831cd90e9ecd530c537c2361c35d45de1548c5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md": {
    "before": "675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff",
    "after": "675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx": {
    "before": "0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376",
    "after": "0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md": {
    "before": "543a25380b524439bcb97253e4531aefff28a6a50912b16a23e9815f154e98e9",
    "after": "543a25380b524439bcb97253e4531aefff28a6a50912b16a23e9815f154e98e9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv": {
    "before": "49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550",
    "after": "49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv": {
    "before": "a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7",
    "after": "a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md": {
    "before": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70",
    "after": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv": {
    "before": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23",
    "after": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md": {
    "before": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc",
    "after": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx": {
    "before": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
    "after": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md": {
    "before": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d",
    "after": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv": {
    "before": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49",
    "after": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv": {
    "before": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534",
    "after": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md": {
    "before": "78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec",
    "after": "78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx": {
    "before": "a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d",
    "after": "a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md": {
    "before": "31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97",
    "after": "31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv": {
    "before": "e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61",
    "after": "e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv": {
    "before": "3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b",
    "after": "3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md": {
    "before": "c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d",
    "after": "c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx": {
    "before": "8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da",
    "after": "8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md": {
    "before": "d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52",
    "after": "d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv": {
    "before": "c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169",
    "after": "c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv": {
    "before": "5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b",
    "after": "5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md": {
    "before": "ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2",
    "after": "ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx": {
    "before": "024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1",
    "after": "024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md": {
    "before": "256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0",
    "after": "256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv": {
    "before": "8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec",
    "after": "8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv": {
    "before": "baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b",
    "after": "baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md": {
    "before": "a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817",
    "after": "a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx": {
    "before": "8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7",
    "after": "8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md": {
    "before": "945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea",
    "after": "945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv": {
    "before": "6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c",
    "after": "6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv": {
    "before": "336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84",
    "after": "336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md": {
    "before": "86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7",
    "after": "86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx": {
    "before": "9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead",
    "after": "9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md": {
    "before": "eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648",
    "after": "eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv": {
    "before": "0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc",
    "after": "0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv": {
    "before": "de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3",
    "after": "de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md": {
    "before": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d",
    "after": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv": {
    "before": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5",
    "after": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md": {
    "before": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2",
    "after": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx": {
    "before": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
    "after": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md": {
    "before": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5",
    "after": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv": {
    "before": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1",
    "after": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv": {
    "before": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff",
    "after": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md": {
    "before": "03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97",
    "after": "03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx": {
    "before": "983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e",
    "after": "983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md": {
    "before": "0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca",
    "after": "0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv": {
    "before": "b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c",
    "after": "b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv": {
    "before": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a",
    "after": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md": {
    "before": "c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866",
    "after": "c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx": {
    "before": "fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63",
    "after": "fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md": {
    "before": "e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d",
    "after": "e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv": {
    "before": "ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd",
    "after": "ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv": {
    "before": "c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237",
    "after": "c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md": {
    "before": "cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda",
    "after": "cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_CROSS_PAPER_CLAIMS.csv": {
    "before": "235765674f4ac445fa2001cb301ab4f4aabd79d05914eba2f08738e76ae98a25",
    "after": "235765674f4ac445fa2001cb301ab4f4aabd79d05914eba2f08738e76ae98a25"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_EXECUTION_REPORT.md": {
    "before": "631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e",
    "after": "631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_MODEL_APPLICABILITY_MATRIX.csv": {
    "before": "06a7179fdef9f5bb82adea8ef06ded04082e18ec956f1f008f45b4e7fec44d4a",
    "after": "06a7179fdef9f5bb82adea8ef06ded04082e18ec956f1f008f45b4e7fec44d4a"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_P3_HANDOFF.md": {
    "before": "bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c",
    "after": "bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_SOURCE_MAP.csv": {
    "before": "2d80ff743568128c2af7f52576569db1589c422a5d8210bb705761bcf8153959",
    "after": "2d80ff743568128c2af7f52576569db1589c422a5d8210bb705761bcf8153959"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md": {
    "before": "5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3",
    "after": "5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_DECISION_MATRIX.md": {
    "before": "4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d",
    "after": "4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md": {
    "before": "5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33",
    "after": "5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_PROTOCOL_FREEZE_CHECKLIST.md": {
    "before": "cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55",
    "after": "cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_R2_REPORT.md": {
    "before": "a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5",
    "after": "a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md": {
    "before": "e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9",
    "after": "e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_EXPERIMENTAL_VALIDATION_PLAN.md": {
    "before": "f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1",
    "after": "f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md": {
    "before": "f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3",
    "after": "f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md": {
    "before": "2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90",
    "after": "2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_MODEL_STRATEGY.md": {
    "before": "61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58",
    "after": "61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv": {
    "before": "9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011",
    "after": "9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md": {
    "before": "09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f",
    "after": "09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_SYSTEM_IDENTIFICATION_MATRIX.csv": {
    "before": "894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201",
    "after": "894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/AGENT_PROMPT.md": {
    "before": "91e1fdebe210f01236c0f64f6b9c5bb49fff0fc855967f8a7b45ed470f8e3284",
    "after": "91e1fdebe210f01236c0f64f6b9c5bb49fff0fc855967f8a7b45ed470f8e3284"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf": {
    "before": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
    "after": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_OUTLINE_2026-10-14.json": {
    "before": "55e15a0425dbde3ec3eb54c1e1a769c52717f03ca5d16c5fdfa8ab326d8217cd",
    "after": "55e15a0425dbde3ec3eb54c1e1a769c52717f03ca5d16c5fdfa8ab326d8217cd"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_OUTLINE_2026-10-14.md": {
    "before": "45542951080f66859241e7ee3c9666b7d22df2348d3236e7560f59aef955f605",
    "after": "45542951080f66859241e7ee3c9666b7d22df2348d3236e7560f59aef955f605"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_SECTION_INDEX.csv": {
    "before": "ac0a8bf828c9e69362112c6d8282f9de25cb3616ee36fd0448d741dccba59633",
    "after": "ac0a8bf828c9e69362112c6d8282f9de25cb3616ee36fd0448d741dccba59633"
  }
}
```

## FINAL_REGRESSION_RESULT

Đãmởlạitoànbộ5filecuối vàDOCX,parseCSV/JSON/XML;54anchor/9glossarykhớp;26EIDtồntạicanonical;12gaprecordgiữcanonicalstatuses;citation/reference/DOIđốichiếunộidung;5trangrendercuốiđãxem. Baseline31/31vàinput418/418hashkhôngđổi. Ngoài5filemới263,gitstatus/diff/indexgiữnguyên. Khôngkhởiđộng264/khôngcommit/push/PR.

FINAL_SELF_REVIEW_DECISION: SELF_REVIEW
SELF_REVIEW_RESULT: COMPLETED_WITH_DOCUMENTED_LIMITATIONS
REVIEW_AUTHORITY: SELF_REVIEW
INDEPENDENT_ACCEPTANCE: NOT_YET_PERFORMED
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE_AND_LATER_2_6_INTEGRATION
