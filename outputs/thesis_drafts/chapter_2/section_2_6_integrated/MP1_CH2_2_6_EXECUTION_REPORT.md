# Báo cáo thực thi tích hợp §2.6

Các trường dành cho máy đọc dưới đây mô tả kết quả thực tế. Chi tiết bằng tiếng Việt nằm trong changelog và báo cáo bảy Gate. Không xem kết quả tự kiểm là nghiệm thu độc lập.

```json
{
  "TASK_ID": "MP1-CH2-2.6-INTEGRATION",
  "STATUS": "COMPLETED_SELF_REVIEW_ONLY",
  "WORKSPACE": "/home/khanh/projects/mechanical-research-agents",
  "BRANCH": "main",
  "HEAD": "e66bb2f2339006e763cd60687cfc24680b945d97",
  "ROOT_MODEL_REQUESTED": "GPT-6.1 Sol High",
  "ROOT_MODEL_ACTUAL": "Codex, nền GPT-6 theo mô tả phiên; không có telemetry cho biến thể hoặc mức suy luận. Không xác nhận đã chạy GPT-6.1 Sol High.",
  "WORKER_MODELS_REQUESTED": "Sol Medium / Luna, theo nhiệm vụ",
  "WORKER_MODELS_ACTUAL": "A/B: gpt-6.1-sol, medium; C: gpt-6-luna, medium. Đây là cấu hình spawn được công cụ nhận; backend không được xác minh.",
  "WORKERS_USED": "A phụ trách baseline, nội dung và thử môi trường render; B phụ trách danh tính tài liệu, trích dẫn và locator; C phụ trách khoa học và thuật ngữ; root phụ trách tích hợp, phân xử và tự kiểm. Có ba worker.",
  "REVIEW_AUTHORITY": "SELF_REVIEW_ONLY",
  "INDEPENDENT_ACCEPTANCE_STATUS": "AWAIT_INDEPENDENT_ACCEPTANCE",
  "OUTLINE_FILE": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
  "OUTLINE_SHA256": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
  "OUTLINE_RECONCILIATION_STATUS": "PASS; giữ nguyên các tiêu đề đã nghiệm thu ở §2.6.1/§2.6.2; ghi khác biệt với PDF trong changelog.",
  "INPUT_FILE_COUNT": 20,
  "INPUT_SHA256_MANIFEST": "Đủ 20 mã băm trong changelog và bên dưới. Snapshot 565 đường dẫn cũng được ghi trong changelog.",
  "BASELINES_UNCHANGED": "20/20 tệp đã nghiệm thu giữ nguyên; các baseline §§2.3–2.5 trong snapshot cũng không đổi.",
  "OTHER_INPUTS_UNCHANGED": "565/565 đường dẫn trong snapshot giữ nguyên mã băm; bao gồm WEP, P3, WP-E và các tệp sửa đổi sẵn có chưa được Git theo dõi.",
  "GIT_CHANGE_SCOPE": "Chỉ có 7 tệp mới trong section_2_6_integrated; giữ nguyên 353 dòng git status đã có; staged diff trống.",
  "SOURCE_SECTIONS": "2.6.1;2.6.2;2.6.3;2.6.4",
  "SOURCE_PARAGRAPH_COUNTS": "Thân 15/16/13/14 = 58; đoạn cấp cao nhất 29/29/26/23 = 107; đoạn trong bảng 45/36/30/33 = 144; tổng cộng 251.",
  "INTEGRATED_PARAGRAPH_COUNTS": "Thân 58; đoạn cấp cao nhất 81; đoạn trong bảng 180; tổng cộng 261. Con số này không đồng nghĩa với số claim.",
  "SOURCE_CLAIM_RECORDS": 267,
  "MASTER_CLAIM_RECORDS": 267,
  "CLAIM_MAPPING_STATUS": "267/267 đạt; giữ nguyên JSON từng dòng nguồn; 267 anchor và bookmark chính xác.",
  "UNRESOLVED_CLAIM_MAPPINGS": 0,
  "SOURCE_TERMINOLOGY_ROWS": 44,
  "CONSOLIDATED_TERMINOLOGY_ROWS": 35,
  "TERMINOLOGY_MERGE_COUNT": "Gộp 6 nhóm, giảm 9 hàng; giữ nguyên lineage của cả 44 mục nguồn.",
  "UNRESOLVED_TERMINOLOGY_CONFLICTS": 0,
  "SOURCE_REFERENCE_ENTRY_COUNT": 34,
  "INTEGRATED_REFERENCE_COUNT": 16,
  "CITATION_OCCURRENCES": "107 biểu thức nguồn tương ứng 117 lần viện dẫn; bản đích có 117 số trích dẫn riêng; không tính số trong danh mục tài liệu tham khảo.",
  "CITATION_RENUMBERING_STATUS": "PASS; 34 dòng ánh xạ; đánh số theo lần xuất hiện đầu từ 1 đến 16; không có mục mồ côi; đã đối chiếu bảng thuật ngữ.",
  "DOI_COUNT": 15,
  "METADATA_ISSUES": "M25: bản trực tuyến 2021/bản xuất bản cuối 2022; M26: phân trang cuối dựa trên M28, PDF trang 19; JCGM hiệu chỉnh năm 2010; không thêm DOI hoặc số kỳ.",
  "SCIENTIFIC_TABLES": 0,
  "GLOSSARY_TABLES": 1,
  "FIGURES": 0,
  "OMML_EQUATIONS": 0,
  "P3_STATUS_PRESERVATION": "H0b vẫn là NOT_FALSIFIED_LIVE_COMPETITOR; H1 vẫn là INSUFFICIENT_EVIDENCE; giữ nguyên phân loại/trạng thái G00–G11; không sửa trạng thái khoa học.",
  "RQ_MAPPING_STATUS": "5 RQ trong PDF ↔ 4 nhóm RQ của P3; PROVISIONAL_MANY_TO_MANY; HUMAN_DECISION_PENDING; không đánh số lại.",
  "PENDING_HUMAN_DECISIONS": "Năm nhóm: hình học/giao diện; proxy tải pháp tuyến; miền trạng thái TiNi; độ cứng/bất định; phạm vi SMA–piston.",
  "DOCX_SHA256": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
  "DOCX_ZIP_XML_STATUS": "PASS; kiểm tra CRC/XML/relationships đạt",
  "WORD_RENDER_VALIDATION": "PASS",
  "RENDERED_PAGES": 18,
  "MICROSOFT_WORD_VALIDATION": "NOT_VERIFIED",
  "SEVEN_GATE_RESULT": "G1:PASS;G2:PASS;G3:PASS_WITH_DOCUMENTED_LIMITATIONS;G4:PASS;G5:PASS_WITH_DOCUMENTED_LIMITATIONS;G6:PASS_WITH_DOCUMENTED_LIMITATIONS;G7:PASS",
  "P1_P2_UNRESOLVED": 0,
  "DOCUMENTED_LIMITATIONS": "Xem mục giới hạn. Nội dung kế thừa không phải là lần tái kiểm tra toàn bộ 39 PDF; chưa kiểm tra bằng Microsoft Word; metadata M25/M26 có nguồn thứ cấp nội bộ.",
  "FILES_CREATED": [
    "MP1_CH2_2_6_INTEGRATED.docx",
    "MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv",
    "MP1_CH2_2_6_MASTER_TERMINOLOGY.csv",
    "MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv",
    "MP1_CH2_2_6_INTEGRATION_CHANGELOG.md",
    "MP1_CH2_2_6_7_GATE_REVIEW.md",
    "MP1_CH2_2_6_EXECUTION_REPORT.md"
  ],
  "COMMIT_STATUS": "NOT_PERFORMED",
  "PUSH_STATUS": "NOT_PERFORMED",
  "STAGE_STATUS": "NOT_PERFORMED",
  "PR_STATUS": "NOT_PERFORMED",
  "FINAL_SELF_REVIEW_DECISION": "Đủ điều kiện gửi người dùng nghiệm thu độc lập; chưa được chấp nhận.",
  "NEXT_ACTION": "AWAIT_INDEPENDENT_ACCEPTANCE"
}
```

## Phạm vi tệp và bảo toàn

Chỉ tạo đúng bảy tệp trong thư mục final. Không thay đổi callers, tests, fixtures, cấu hình, exports, script build chung hoặc scientific registry vì nhiệm vụ chỉ tích hợp tài liệu. Script tạm, bộ LibreOffice portable, profile, PDF/PNG/JSON kiểm tra đều ở /tmp. Không stage, commit, push, merge, đổi branch hoặc tạo PR. Ở bước preflight không phát hiện tác vụ nào ghi vào cùng thư mục output; snapshot cuối cũng không cho thấy thay đổi baseline.

## Manifest đầu vào

| Tệp nguồn | Byte | SHA-256 |
|---|---:|---|
| `outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx` | 45034 | `983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e` |
| `outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv` | 995489 | `b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c` |
| `outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv` | 151643 | `bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a` |
| `outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md` | 20466 | `03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97` |
| `outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md` | 68789 | `0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca` |
| `outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx` | 44577 | `fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63` |
| `outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv` | 1451117 | `ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd` |
| `outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv` | 97866 | `c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237` |
| `outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md` | 20769 | `c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866` |
| `outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md` | 156089 | `e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d` |
| `outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx` | 43191 | `5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d` |
| `outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv` | 952237 | `badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d` |
| `outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv` | 12162 | `3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13` |
| `outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md` | 18673 | `5a9b1e21647777cb2855490d42e553a92f56906dad609522cc92841c4c59a9c9` |
| `outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md` | 212508 | `1d12b07ae29792e7ae547576468134926e6acefde9ccc740dd670cea084f70cd` |
| `outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx` | 43261 | `607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45` |
| `outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv` | 856158 | `636a5acb7514ccd8309a6e786280252847bdbd5c6674264069866a772429275b` |
| `outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv` | 42808 | `346ffdf77c8e5b60680d7fb57ee9992765a7112de12673a4328ce3c8149a64f5` |
| `outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md` | 78663 | `efc42a239b43168aa4f24fe938892cc7969bf062827e92103e3587dc0379bf2d` |
| `outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md` | 250103 | `93abadee17152b5e6eef625915ea7b828ee54f69124335a2de215e11b62ae65a` |

## Kiểm kê

| Tiểu mục | Đoạn thân nguồn | Đoạn thân đích | Tổng đoạn cấp thân XML nguồn | Claim | Thuật ngữ | Entry cục bộ |
|---|---:|---:|---:|---:|---:|---:|
| 2.6.1 | 15 | 15 | 29 | 84 | 14 | 10 |
| 2.6.2 | 16 | 16 | 29 | 72 | 11 | 9 |
| 2.6.3 | 13 | 13 | 26 | 54 | 9 | 9 |
| 2.6.4 | 14 | 14 | 23 | 57 | 10 | 6 |


## Mức độ xác minh bằng chứng

Đã kiểm tra trực tiếp trong phiên: 20 mã băm; cấu trúc/267 dòng; 44 thuật ngữ; văn bản/runs/styles của DOCX; bảng ánh xạ danh tính tài liệu; dàn ý gốc ở các trang vật lý 6, 14 và 15; các mục được chỉ định trong P3/WP-E/WEP; văn bản PDF M26 ở các trang vật lý 1, 4, 6, 8, 15, 16 và 17, cùng ảnh trang 4. Worker B kiểm tra metadata PDF của M13/M25/M26/M34/M38, nguồn thứ cấp M28 trang vật lý 19 và nhóm locator GUM 20/21/31/33/35/36/47. Các claim khác kế thừa trạng thái accepted evidence; không tái kiểm toàn bộ 39 PDF.

VERIFIED FULL TEXT chỉ mô tả đoạn nguồn đã mở hoặc trạng thái hồ sơ kế thừa có provenance. METADATA ONLY mô tả việc xác minh danh tính tài liệu, không phải kiểm chứng claim cơ học. Các trường INFERENCE, proposal và pending giữ nguyên mức độ bằng chứng của nguồn. Không nâng metadata thứ cấp thành xác minh từ nhà xuất bản.

## Mô hình và worker

ROOT_MODEL_ACTUAL: Codex, nền GPT-6 theo mô tả phiên; không có telemetry cho biến thể hoặc mức suy luận. Không xác nhận đã chạy GPT-6.1 Sol High.

WORKER_MODELS_ACTUAL: A/B: gpt-6.1-sol, medium; C: gpt-6-luna, medium. Đây là cấu hình spawn được công cụ nhận; backend không được xác minh.

Công cụ nhận cấu hình A/B = gpt-6.1-sol medium, C = gpt-6-luna medium, mỗi worker chạy trong fork riêng. Không có telemetry để xác minh backend. Root chịu trách nhiệm về kết luận; worker không cấp acceptance. Worker C từng diễn giải nhầm năm quyết định thành phần của RQ mapping trong báo cáo nháp; root yêu cầu sửa trước bản cuối. Bản cuối phân biệt rõ 5 RQ trong PDF ↔ 4 nhóm RQ của P3 với 5 quyết định của con người và không thêm ánh xạ mới vào manuscript.

## Kết quả worker đã được root đối chiếu

A: 20 mã băm, 4 tiêu đề, 58 đoạn thân, 4 bảng thuật ngữ, 34 mục tài liệu tham khảo; không có OMML/ảnh. B: 267/267 dòng lossless, anchor/bookmark phân giải được, 34 → 16 danh tính tài liệu, 117 lần trích dẫn, 9 hiệu chỉnh locator/7 claim. C: 44/44 thuật ngữ có lineage, 35/35 hàng bảng/CSV khớp; gộp 6 nhóm tương đương, giữ riêng E/B/K và các cấp kiểm chứng. Worker B/C kiểm bản ứng viên trước sửa font, hash 2d809fe836e49ad382f15cd8f39184ae1c262b8bc79906203a7dcfaf622bebea. Sau hiệu chỉnh định dạng FMT-002, root chạy lại QA bằng parser riêng trên hash cuối, xác nhận toàn bộ anchor/citation/nội dung bảng vẫn khớp và xem đủ 18 trang render. A thử môi trường LibreOffice nhưng không hoàn tất; root xử lý bootstrap và xuất PDF cuối. Tất cả vai trò vẫn thuộc SELF_REVIEW_ONLY.

## Kết quả QA

```json
{
  "qa_status": "PASS",
  "docx_sha256": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
  "master_records": 267,
  "original_rows_lossless": 267,
  "anchors_resolved": 267,
  "body_paragraphs_preserved": 58,
  "source_terminology_lineage": 44,
  "master_terms": 35,
  "local_reference_mappings": 34,
  "integrated_references": 16,
  "doi_unique": 15,
  "reference_incidences": 117,
  "first_use_order": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16
  ],
  "source_union_columns": 63,
  "zip_crc_xml_relationships": "PASS",
  "native_tables": 1,
  "figures": 0,
  "omml": 0,
  "top_level_paragraphs": 81,
  "integration_locator_correction_claims": 7
}
```

## Render cuối

```json
{
  "status": "PASS",
  "renderer": "LibreOffice 24.2.7.2 420(Build:2), headless writer_pdf_Export",
  "docx_sha256": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
  "pdf_sha256": "3e3f09928a71fb2fe29d84a575589a2cbcb22e023718d3432c6f4f04773f26f5",
  "pages": 18,
  "pages_visually_reviewed": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18
  ],
  "profile": "/tmp/mp1-ch26-integration/lo-final-profile3",
  "all_scratch_outside_final_directory": true,
  "command": "env DCONF_PROFILE=/dev/null XDG_RUNTIME_DIR=/tmp/mp1-ch26-integration/runtime LD_LIBRARY_PATH=/tmp/mp1-ch26-integration/lo-root/usr/lib/libreoffice/program:/tmp/mp1-ch26-integration/lo-root/usr/lib/x86_64-linux-gnu SAL_USE_VCLPLUGIN=svp /tmp/mp1-ch26-integration/lo-root/usr/lib/libreoffice/program/soffice.bin -env:UserInstallation=file:///tmp/mp1-ch26-integration/lo-final-profile3 --headless --convert-to pdf --outdir /tmp/mp1-ch26-integration/render /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx",
  "portable_setup": "52 Ubuntu deb giải nén /tmp, không cài hệ thống; chuẩn lại absolute rc/symlinks, dùng unorc đúng thư mục thư viện, chép .registry vào registry scratch; bỏ dconf khỏi cấu hình scratch. Chạy render ngoài sandbox với quyền đã cho phép; khởi tạo profile trả81 rồi chạy lại thành công0.",
  "render_warning": "liblangtag báo thiếu /usr/share/liblangtag/language-subtag-registry.xml trong portable setup. Xuất PDF kết thúc0; kiểm đối chiếu toàn bộ text và fonts không thấy nội dung/glyph mất. Không dùng render này để đánh giá spellcheck/language tagging.",
  "text_checks": {
    "pdf_sha256": "3e3f09928a71fb2fe29d84a575589a2cbcb22e023718d3432c6f4f04773f26f5",
    "pages": 18,
    "body_missing": [],
    "glossary_missing": [],
    "fonts": {
      "TimesNewRomanPS-BoldMT": 968,
      "TimesNewRomanPSMT": 53365
    },
    "replacement_glyphs": 0
  },
  "MICROSOFT_WORD_VALIDATION": "NOT_VERIFIED",
  "page_audit": [
    {
      "page": 1,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        81.42,
        541.75,
        738.24
      ],
      "png_sha256": "b7b32541cd1b85a931af3ed91139091dda617b012f81c218ae3c6412a6391b49",
      "text_sha256": "f927389d2ceba0da6ae2e5b66e1ad2562b2e5fd19bba24006cabdd67cbed0052",
      "findings": "Trang đầu, heading cha và §2.6.1; font Times New Roman đúng.",
      "severity": "NONE"
    },
    {
      "page": 2,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        758.49
      ],
      "png_sha256": "9de5bde7af64ee7b8e82a0fa46cac5475a1fea4875f0dcb0899700329f0ff84a",
      "text_sha256": "aee06dad2cdd19ce28a2dbe34ed5e5396f974d8d98b9eb58d3dbe21857e51efc",
      "findings": "Nội dung liên tục, citation/Unicode rõ; không clipping hoặc tràn lề.",
      "severity": "NONE"
    },
    {
      "page": 3,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        710.94
      ],
      "png_sha256": "48182da5ca742897ea071aae0f533b632eb4785136726b59bdac3d9b3d97c7be",
      "text_sha256": "74b99343dbff735c0db23eefd5191e759bed3237ae3bb6a9b7bca37a64724386",
      "findings": "Cuối §2.6.1; không mất câu chuyển tiếp sang §2.6.2.",
      "severity": "NONE"
    },
    {
      "page": 4,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        770.49
      ],
      "png_sha256": "ec1d87f97835dd02fd9da0918ce6e5b0b6e8d3adb0b2724f3ced7ba7140efab6",
      "text_sha256": "bca8980453e61b08ef67c86d32ecdc453d24b86ec047a8b309b8ba5f27f8ce02",
      "findings": "Heading §2.6.2 và citation 11–13 đúng; tiếp nối đoạn qua trang bình thường.",
      "severity": "NONE"
    },
    {
      "page": 5,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        764.49
      ],
      "png_sha256": "a9709f3b79853b9055fef081f08271e5c574cf425ac8ebf408e384b29310b8b3",
      "text_sha256": "ab30f97b305bf9544168929b4899f20ba679c0e09886b9fc8a44c018c865cb69",
      "findings": "Nội dung liên tục, citation/Unicode rõ; không clipping hoặc tràn lề.",
      "severity": "NONE"
    },
    {
      "page": 6,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        732.79
      ],
      "png_sha256": "4694b4c55906dee289342270d57631c2dd04d27b15e5cc953f2d0bedac16c486",
      "text_sha256": "5d38b0b8059684d364c204cae580744de474be6d0fd56f293a16a4ed0867f195",
      "findings": "Cuối §2.6.2; giữ H0b và quyết định mở.",
      "severity": "NONE"
    },
    {
      "page": 7,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        770.49
      ],
      "png_sha256": "eff9a0e56c6e527a8ffc76e1a3755ac75a5b3aca8c0212571a8f6d5f65a6a592",
      "text_sha256": "89583487f410a91a39c864ab1565fdb9453805818b601c8869ef3ec23790fe7d",
      "findings": "Heading §2.6.3; prior art và câu hỏi có điều kiện.",
      "severity": "NONE"
    },
    {
      "page": 8,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        764.49
      ],
      "png_sha256": "161de63a6fd6935cb49034a5f0b619d2cf9e4f24e49632a1ab73eacad17c670a",
      "text_sha256": "6d589058894746178172562412f9e9fa54d086e2347f527e9cb1c8aa49e301d3",
      "findings": "Nối đoạn từ trang7; citation đầu trang thuộc cùng đoạn, còn đầy đủ.",
      "severity": "NONE"
    },
    {
      "page": 9,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        764.64
      ],
      "png_sha256": "3744e62020592a49651c7ee8055c41f3cffbaf64551931a26e9232149e886e1b",
      "text_sha256": "c4736492c75d63afb91222bfeaf0494ee814e0e4a25dd8ff5699462e87ddfee9",
      "findings": "Cuối §2.6.3 và heading §2.6.4; không mất đoạn.",
      "severity": "NONE"
    },
    {
      "page": 10,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        764.49
      ],
      "png_sha256": "9fa3d7017a03bb0f0412dc58bae7a372cbcf84d8fecad4d5615b35282b13864d",
      "text_sha256": "fbcfe16593c6037baef2b1a15acfb3013547766f89c52ad83cca2a19270c7508",
      "findings": "Ký hiệu M–κ, E, B/EI, K và đơn vị đọc được.",
      "severity": "NONE"
    },
    {
      "page": 11,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        669.39
      ],
      "png_sha256": "b4d9c1c67a6c9d05712cf0252a67c9e3132631f16068b96c608185059bdd237a",
      "text_sha256": "e9db78d6db1c6132cfcfdc566631432bef9bdf12ac35e19e43f64798dda24038",
      "findings": "Cuối §2.6.4; năm nhóm quyết định còn mở.",
      "severity": "NONE"
    },
    {
      "page": 12,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        514.41,
        697.16
      ],
      "png_sha256": "014ce062dddeb41983b766151a79dbc09bfe36a4af2724d34a11a3637610c419",
      "text_sha256": "879a3b8e3f5fbe0d9a5c467498bf3ee662a848e2ca25c49f194afcd1f0853cec",
      "findings": "Heading bảng chung cùng header; hàng thuật ngữ native không clipping.",
      "severity": "NONE"
    },
    {
      "page": 13,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        492.61,
        591.96
      ],
      "png_sha256": "eb0a53fa0f3cc4216940161b764e07f4e47bc718cf6cb8cfa8ce8eadb58521ea",
      "text_sha256": "81e4bee4e9f5fe1cd1e90a6ad8f2598235f03d65477564292396e30de1ba5d59",
      "findings": "Header lặp; khoảng trắng cuối trang do giữ nguyên hàng cao kế tiếp, có chủ đích.",
      "severity": "NONE"
    },
    {
      "page": 14,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        526.48,
        711.26
      ],
      "png_sha256": "807e19f23b371189ff2c48c190a75468bca0ca8c9006e5c9b593c7780f819116",
      "text_sha256": "cd070d57e9f1f958b6279e94d80b47d0fe61b7df8fb6648aeebe9f1a941cf1f2",
      "findings": "Hàng độ không đảm bảo bốn định nghĩa cùng trang; không tách/mất nội dung.",
      "severity": "NONE"
    },
    {
      "page": 15,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        528.05,
        739.46
      ],
      "png_sha256": "444c02c989727b858332415ef24905c89383bb3e5219ade90d90fea9144e6273",
      "text_sha256": "b0d1d3c29d938ae29836553b32191111fcd693db28e69b77c7f1938d62261bd8",
      "findings": "Gộp local traction và independent predictive validation; đủ các nhãn tiểu mục.",
      "severity": "NONE"
    },
    {
      "page": 16,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        524.84,
        717.61
      ],
      "png_sha256": "a408d79d0a7bde7e5b400598ac4a969dc06b93a25e4f0fa1f0e0398bdccc19f7",
      "text_sha256": "0922e9e1ca18a5d2eaf881d8e80f789d37d1906d4eb66f7457acd62d74a61642",
      "findings": "Các mục composite E/B/K giữ riêng; chữ/đơn vị không tràn ô.",
      "severity": "NONE"
    },
    {
      "page": 17,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        541.75,
        768.69
      ],
      "png_sha256": "0134742133fad64400c3f0e9a8822019699d96a0da8979e6a49e026ac493d099",
      "text_sha256": "27d7c97f12a3446d478421e88489b9d9fad93f92816f93165ab75bb582acd0f2",
      "findings": "Header lặp, hai hàng cuối glossary và bibliography[1]–[9].",
      "severity": "NONE"
    },
    {
      "page": 18,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        453.49
      ],
      "png_sha256": "4f3c2716a1f8b7babfe8be2e8872e7df6f4e6225996c0091e31991b96299963a",
      "text_sha256": "09ae527f35c3285d73f0e8f2153b2f0d2b1beb624ee83ab108d26adf1a564090",
      "findings": "Trang cuối bibliography[10]–[16]; không có nội dung ngoài §2.6.",
      "severity": "NONE"
    }
  ]
}
```

## Giới hạn

- Chỉ SELF_REVIEW_ONLY. Ba worker nằm trong cùng phiên, không phải hội đồng nghiệm thu độc lập và không bỏ phiếu quyết định.
- MICROSOFT_WORD_VALIDATION: NOT_VERIFIED. LibreOffice không bảo đảm phân trang giống Microsoft Word.
- Nhãn VERIFIED FULL TEXT trong các trường nguồn được kế thừa từ baseline; không phải xác minh mới toàn bộ 267 claim hoặc 39 PDF. Tái kiểm trực tiếp chỉ gồm nhóm metadata/locator rủi ro được liệt kê.
- Metadata xuất bản cuối của M25 và M26 có xuất xứ thứ cấp nội bộ từ danh mục tài liệu tham khảo M28, trang vật lý 19. Không tuyên bố đã kiểm tra metadata với nhà xuất bản cho toàn bộ tài liệu; không tự bổ sung số kỳ hoặc DOI.
- RQ_MAPPING là 5 RQ của PDF ↔ 4 nhóm P3, PROVISIONAL_MANY_TO_MANY, HUMAN_DECISION_PENDING. Năm nhóm quyết định của con người là danh sách riêng.
- Các lựa chọn hình học, đại diện tải pháp tuyến, miền trạng thái TiNi, đại lượng độ cứng/bất định và phạm vi SMA–piston còn mở. Nghiệm thu văn bản không phê duyệt thí nghiệm.
- Việc giữ nguyên định nghĩa theo từng tiểu mục làm một số hàng thuật ngữ dài và có lặp có chủ đích. Không rút gọn để đổi lấy số trang.


## Mã băm của các tệp nội dung và báo cáo đồng hành

Không nhúng SHA-256 của chính báo cáo này vào trong nó để tránh vòng lặp mã băm. Gate 7 kiểm tra tệp tồn tại, không rỗng, đã được đọc lại và thuộc đúng phạm vi bảy tệp.

| Tệp | SHA-256 |
|---|---|
| `MP1_CH2_2_6_INTEGRATED.docx` | `d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b` |
| `MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv` | `987fb13dda00f2d62abb4da346f2c6da7e3cbd3857749edc3f72725b59049a13` |
| `MP1_CH2_2_6_MASTER_TERMINOLOGY.csv` | `ec725c4206ac2854febc16f7ddb882802c1d71e53037792dd6ad6383869bca09` |
| `MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv` | `019d4780f896a73b3b85400675d394dcfdda1c13e8404d7a0ff9723db4887944` |
| `MP1_CH2_2_6_INTEGRATION_CHANGELOG.md` | `15fc8d6380b20bff447626adff74034251ab633c548dea0893a836d7f0f28fc0` |
| `MP1_CH2_2_6_7_GATE_REVIEW.md` | `b066121b47c37197b10d2bed2fa9709d5688d4973b5d13e23121c7bbf6ed275a` |

## Git status có sẵn trước tác vụ

353 dòng được giữ nguyên sau tác vụ. Dữ liệu dưới đây là snapshot trước, không phải danh sách thay đổi do tích hợp.

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
?? "data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt"
?? "data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt"
?? "data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt"
?? "data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt"
?? data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt
?? "data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt"
?? data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt
?? data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt
?? "data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt"
?? data/chap1-2_citations/MANIFEST.json
?? data/chap1-2_citations/README.md
?? docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md
?? docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md
?? docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md
?? docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md
?? docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx
?? docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx
?? "docs/project/almost done/LR-FORMATED.docx"
?? docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md
?? docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md
?? "literature review/LR-FORMATED-rewrite-outline-de-xuat.docx"
?? "literature review/LR-FORMATED-rewrite.docx"
?? "literature review/LR-FORMATED.docx"
?? "literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL.zip"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md"
?? "literature review/ma-tran-tong-quan-tai-lieu.docx"
?? "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json"
?? "literature review/~$-FORMATED-rewrite.docx"
?? "literature review/~$-FORMATED.docx"
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
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv
```

## QA có thể chạy lại

Lưu khối Python sau ở scratch ngoài thư mục final rồi chạy bằng Python có python-docx và lxml. Nó đọc lại nguồn và gói final, không ghi baseline. Bản mã là mã đã chạy ở phiên này; kết quả JSON ở trên. Kiểm visual phải render lại đúng DOCX hash và xem từng trang, không được dùng ảnh cũ nếu DOCX đổi.

```python
from pathlib import Path
from collections import Counter
import csv, hashlib, json, re, zipfile, posixpath
from lxml import etree
from docx import Document
from docx.oxml.ns import qn

ROOT=Path('/home/khanh/projects/mechanical-research-agents')
OUT=ROOT/'outputs/thesis_drafts/chapter_2/section_2_6_integrated'
def rows(name):
    with (OUT/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
master=rows('MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv')
terms=rows('MP1_CH2_2_6_MASTER_TERMINOLOGY.csv')
cmap=rows('MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv')
p=OUT/'MP1_CH2_2_6_INTEGRATED.docx';d=Document(p)
assert all(r['target_integrated_docx_sha256']==sha(p) for r in master+terms+cmap)
rx=re.compile(r'\[(\d+(?:\s*[,;]\s*\d+)*)\](?:\s*[–−-]\s*\[(\d+)\])?')
def nums(m):
    v=[int(x) for x in re.split(r'\s*[,;]\s*',m[1])]
    return list(range(v[0],int(m[2])+1)) if m[2] else v
maps={}
for r in cmap:maps.setdefault(r['source_section'],{})[int(r['source_reference_number'])]=int(r['target_reference_number'])
def trans(t,s):return rx.sub(lambda m:', '.join(f'[{maps[s][n]}]' for n in nums(m)),t)
assert len(master)==267 and len({x['target_master_claim_id'] for x in master})==267
assert len({x['source_record_id'] for x in master})==267
assert len(cmap)==34
source_rows={};source_terms={};source_units=[];body_indices=set()
for i,expected in enumerate([84,72,54,57],1):
    sec=f'2.6.{i}';base=ROOT/f'outputs/thesis_drafts/chapter_2/section_2_6_{i}'
    src=Document(base/f'MP1_CH2_2_6_{i}_DRAFT.docx')
    with (base/f'MP1_CH2_2_6_{i}_SOURCE_TRACEABILITY.csv').open(encoding='utf-8-sig') as f: rr=list(csv.DictReader(f))
    with (base/f'MP1_CH2_2_6_{i}_TERMINOLOGY.csv').open(encoding='utf-8-sig') as f: tt=list(csv.DictReader(f))
    assert len(rr)==expected
    for r in rr:source_rows[r['original_claim_id']]=r
    for r in tt:source_terms[r['integrated_term_id']]=r
    end=next(n for n,x in enumerate(src.paragraphs) if 'Thuật ngữ sử dụng' in x.text or 'Bảng thuật ngữ' in x.text)
    expected_heading=src.paragraphs[0].text
    h=[n for n,x in enumerate(d.paragraphs) if x.text==expected_heading]
    assert len(h)==1 and d.paragraphs[h[0]].style.name=='Heading 2'
    for n in range(1,end):
        tgt=d.paragraphs[h[0]+n]
        assert tgt.text==trans(src.paragraphs[n].text,sec)
        # Trạng thái italic/bold/chỉ số trên-dưới của từng ký tự khoa học còn nguyên.
        def signature(pp):
            text=pp.text;excluded=set()
            for m in re.finditer(r'\[\d+(?:\s*[,;]\s*\d+)*\](?:\s*[,;–−-]\s*\[\d+\])*',text):excluded.update(range(m.start(),m.end()))
            sig=[];pos=0
            for r in pp.runs:
                for c in r.text:
                    if pos not in excluded and not c.isspace():
                        sig.append((c,r.bold,r.italic,r.font.subscript,r.font.superscript))
                    pos+=1
            return sig
        assert signature(src.paragraphs[n])==signature(tgt),(sec,n,'scientific run formatting')
        source_units.append((sec,n,h[0]+n));body_indices.add(h[0]+n)
    for rn,row in enumerate(src.tables[0].rows[1:],1):
        for ci,cell in enumerate(row.cells):
            hits=[x for x in cmap if x['source_section']==sec]
            for m in rx.finditer(cell.text):assert all(n in maps[sec] for n in nums(m))
for r in master:
    old=source_rows[r['source_claim_id']]
    assert json.loads(r['source_original_record_json'])==old
    assert all(r[k]==v for k,v in old.items()),r['source_claim_id']
    sec=r['source_section']
    f=ROOT/f'outputs/thesis_drafts/chapter_2/section_2_6_{sec[-1]}/MP1_CH2_2_6_{sec[-1]}_DRAFT.docx'
    assert r['source_docx_sha256']==sha(f)
    a=r['target_manuscript_anchor'];loc=r['target_integrated_document_location']
    if loc.startswith('paragraph'):
        n=int(re.search(r'\[(\d+)\]',loc)[1]);container=d.paragraphs[n];scope=container.text
    else:
        t,rn,ci=map(int,re.findall(r'\[(\d+)\]',loc));container=d.tables[t].rows[rn].cells[ci];scope=container.text
    aa,bb=json.loads(r['target_anchor_char_range']);assert scope[aa:bb]==a
    assert a==trans(old['manuscript_sentence_anchor'],sec)
    marks=container._element.xpath('.//w:bookmarkStart')
    assert sum(m.get(qn('w:name'))==r['target_bookmark'] for m in marks)==1
assert len(source_units)==58
assert len(d.tables)==1 and len(d.tables[0].rows)-1==len(terms)==35
seen=[]
for r in terms:
    tr=d.tables[0].rows[int(r['integrated_glossary_row'])]
    assert all(tr.cells[i].text==r[f'integrated_glossary_cell_{i}'] for i in range(3))
    assert r['mechanical_definition']==tr.cells[1].text and r['source_attribution']==tr.cells[2].text
    for item in json.loads(r['original_records_json']):
        assert item['record']==source_terms[item['id']]
        seen.append(item['id'])
assert len(seen)==44 and set(seen)==set(source_terms) and len(set(seen))==44
bibidx=next(i for i,x in enumerate(d.paragraphs) if x.text=='Tài liệu tham khảo')
bib={int(re.match(r'^\[(\d+)\]',x.text)[1]):x.text for x in d.paragraphs[bibidx+1:]}
assert set(bib)==set(range(1,17))
order=[];new_counter=Counter()
for text in [x.text for x in d.paragraphs[:bibidx]]+[c.text for row in d.tables[0].rows[1:] for c in row.cells]:
    for m in rx.finditer(text):
        for n in nums(m):
            assert n in bib;new_counter[n]+=1
            if n not in order:order.append(n)
assert order==list(range(1,17))
expected_counter=Counter();occ=0
for r in cmap:
    n=int(r['target_reference_number']);expected_counter[n]+=int(r['citation_occurrence_count'])
    assert r['target_reference_text']==bib[n]
    details=json.loads(r['target_integrated_location'])
    assert len(details)==int(r['citation_occurrence_count'])
    occ+=len(details)
assert new_counter==expected_counter and occ==117
dois={n:re.search(r'DOI:\s*(\S+)',t).group(1).rstrip('.') for n,t in bib.items() if 'DOI:' in t}
assert len(dois)==len(set(v.lower() for v in dois.values()))==15
sec=d.sections[0]
assert len(d.sections)==1
for actual,cm in [(sec.page_width,21),(sec.page_height,29.7),(sec.left_margin,3),(sec.right_margin,2),(sec.top_margin,2.5),(sec.bottom_margin,2.5)]:assert abs(actual.cm-cm)<.01
assert not d._element.xpath('.//w:headerReference|.//w:footerReference|.//w:pict|.//m:oMath|.//w:drawing')
assert d.tables[0].rows[0]._tr.xpath('./w:trPr/w:tblHeader')
for row in d.tables[0].rows[1:]:assert row._tr.xpath('./w:trPr/w:cantSplit')
allpars=d.paragraphs+[p for row in d.tables[0].rows for c in row.cells for p in c.paragraphs]
for p0 in allpars:
    for run in p0.runs:
        if run.text:
            font=run.font.name or p0.style.font.name
            size=run.font.size or p0.style.font.size
            assert font=='Times New Roman' and size.pt in [10,12,13]
with zipfile.ZipFile(p) as z:
    assert z.testzip() is None
    names=set(z.namelist())
    for n in names:
        if n.endswith(('.xml','.rels')):etree.fromstring(z.read(n))
        if n.endswith('.rels'):
            folder=posixpath.dirname(posixpath.dirname(n))
            for rel in etree.fromstring(z.read(n)):
                if rel.get('TargetMode')=='External':continue
                target=rel.get('Target');path=posixpath.normpath(posixpath.join(folder,target)) if not target.startswith('/') else target[1:]
                assert path in names,(n,path)
result={'qa_status':'PASS','docx_sha256':sha(p),'master_records':267,'original_rows_lossless':267,
        'anchors_resolved':267,'body_paragraphs_preserved':58,'source_terminology_lineage':44,'master_terms':35,
        'local_reference_mappings':34,'integrated_references':16,'doi_unique':15,
        'reference_incidences':occ,'first_use_order':order,'source_union_columns':len(set(k for r in source_rows.values() for k in r)),
        'zip_crc_xml_relationships':'PASS','native_tables':1,'figures':0,'omml':0,
        'top_level_paragraphs':len(d.paragraphs),'integration_locator_correction_claims':sum(bool(r['integration_verified_locator']) for r in master)}
print(json.dumps(result,ensure_ascii=False,indent=2))

```

## Quyết định tự rà soát

Đủ điều kiện gửi người dùng nghiệm thu độc lập; chưa được chấp nhận.

NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE. Dừng ở §2.6; không tự bắt đầu Chương 3–4 hoặc tích hợp vào các mục khác.