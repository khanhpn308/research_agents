# Tự rà soát bảy Gate của §2.1.1

TASK_ID: `MP1-CH2-2.1.1-RESEARCH-THESIS-DRAFT`  
STATUS: `SUCCESS`  
REVIEW_AUTHORITY: `SELF_REVIEW_ONLY`  
AUTHOR_APPROVAL_STATUS: `HUMAN_APPROVAL_PENDING`  
INDEPENDENT_ACCEPTANCE_STATUS: `REQUIRED_NOT_PERFORMED`

Các worker là thành phần của lượt tự rà soát. Không có nghiệm thu độc lập hoặc phê duyệt nghiên cứu trong gói này.

## Gate 1 — Dàn ý chính thức và phạm vi

| Trường | Kết quả |
|---|---|
| STATUS | PASS |
| METHOD | ROOT tính SHA-256 từ bytes; đọc text và xem trực tiếp ảnh PDF6/PDF10; đối chiếu văn bản cuối theo đoạn. |
| EVIDENCE | Canonical outline `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf`; hash `18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e`; B01/B02; Word P001–P006. |
| COUNTS | 22 trang outline; 2 bullet; 5 nhóm có lý do; 6 đoạn thân bài; 0 heading ngoài mục tiêu và Tài liệu tham khảo. |
| FINDINGS | Đúng heading. Không thêm parent §2.1 hoặc §2.1.1.1. Không viết lịch sử robot mềm, từ khóa, database, ngày tìm, số sàng lọc hoặc PRISMA. Câu về mức xác minh nguồn chỉ nêu mục đích, không triển khai quy ước §2.1.4. |
| SEVERITY | NONE |
| UNRESOLVED | Không có xung đột dàn ý. |
| FINAL_DECISION | Đạt phạm vi mục đích tổng quan. |

## Gate 2 — Toàn vẹn RQ và P3

| Trường | Kết quả |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đối chiếu PDF6 §1.4.1 với từng đoạn và đọc sáu tệp P3 canonical; phân biệt năm RQ PDF với bốn nhóm P3. |
| EVIDENCE | P002–P005; SOURCE_TRACEABILITY.csv rq_ids/rq_mapping_status; P3_HYPOTHESIS_ASSESSMENT.md; P3_GAP_ADJUDICATION.md; P3_RESEARCH_GAP_MATRIX.csv; P3_RESEARCH_QUESTIONS.md; P3_DECISION_REPORT.md; DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md. |
| COUNTS | 5/5 RQ có định hướng chức năng; 3 trạng thái H0a/H0b/H1 bảo toàn; 5 quyết định nghiên cứu còn mở. |
| FINDINGS | H0a chỉ REFUTED_IN_TRANSFORMATION_REGIME; H0b NOT_FALSIFIED_LIVE_COMPETITOR; H1 INSUFFICIENT_EVIDENCE. Không suy H0a sai thành H1 đúng. G00 đóng; G01–G08 có điều kiện; G09 prerequisite; G10–G11 không được nâng thành tính mới phổ quát. Không xác nhận Bench đã chạy hoặc được phê duyệt. |
| SEVERITY | LIMITATION_BY_DESIGN |
| UNRESOLVED | HUMAN_DECISION_PENDING đối với reconciliation PDF↔P3 và năm quyết định thiết kế; được giữ mở theo yêu cầu. |
| FINAL_DECISION | Đạt cho bản thảo định hướng; không phê duyệt nghiên cứu hoặc mapping. |

## Gate 3 — Nguồn và truy vết claim

| Trường | Kết quả |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Phân loại từng phát biểu; mở lại đoạn PDF nguồn; kiểm ID trong Evidence Records; parser chọn đúng w:p và kiểm lát ký tự start:end; kiểm phủ ký tự từng đoạn. |
| EVIDENCE | 30 record trong CSV; 3 PDF khoa học cùng hash; record M13-E01/E04, M26-E01, M34-E02/E07; internal_source_provenance; registered_evidence_record_locator_original. |
| COUNTS | 30/30 anchor resolve; 100% ký tự không trắng trong 6 đoạn có record; 24 scope, 3 source claim, 2 P3 statement, 1 pending decision; 0 orphan. |
| FINDINGS | Không gán Paper ID/DOI cho scope. M01 trong WEP là phương pháp viết, không làm bằng chứng cơ học và không được dẫn trong Word. Locator M01-E01/E02/E03 không tái hiện trên trang vật lý ghi trong WEP; đã cách ly khỏi hỗ trợ claim của bản thảo và ghi riêng bên dưới. Locator và fragment kiểm mới của nguồn được giữ tách với anchor gốc của Evidence Records; không sửa hồ sơ gốc. |
| SEVERITY | P3_INPUT_CAVEAT_CONTAINED_FOR_THIS_DRAFT |
| UNRESOLVED | M01 locator correction ngoài phạm vi vẫn cần một lượt source audit riêng; không có claim bản thảo phụ thuộc locator đó. |
| FINAL_DECISION | Đạt truy vết cho claim thực sự sử dụng; không chứng nhận toàn bộ WEP. |

## Gate 4 — Liên tục với Chương 2

| Trường | Kết quả |
|---|---|
| STATUS | PASS |
| METHOD | ROOT đọc các đoạn cần thiết từ cả năm DOCX và đối chiếu master terminology/traceability/citation maps; worker B đọc liên tục; kiểm chuỗi từ trùng. |
| EVIDENCE | §2.2 P004,P014–P015,P017–P030,P038–P042; §2.3 P001–P014,P038–P046; §2.4 P014–P017,P031–P034,P048–P074; §2.5 P035–P036,P107–P150; §2.6 P017–P062. P là chỉ số doc.paragraphs bắt đầu 0, gồm heading, không gồm bảng. |
| COUNTS | 5/5 baseline đã đối chiếu; trùng liên tiếp dài nhất theo token cách trắng: 5,5,6,6,12 cho §§2.2–2.6. |
| FINDINGS | Giữ riêng E/B/K, áp suất nguồn/gần mẫu/tải tiếp xúc, TiNi chịu lực/SMA nguồn áp, hiệu chuẩn/kiểm chứng. Ba ví dụ nguồn chỉ là câu chỉ dẫn ngắn, không lặp số liệu hay phép suy diễn chi tiết. Không sửa minor errata §2.5. |
| SEVERITY | NONE |
| UNRESOLVED | Không có thay đổi thuật ngữ có ý nghĩa cơ học được xác định trong phạm vi này. |
| FINAL_DECISION | Đạt tính liên tục; kiểm trùng chuỗi là trợ giúp biên tập, không phải chứng minh độc lập về chất lượng. |

## Gate 5 — Chất lượng văn viết khoa học

| Trường | Kết quả |
|---|---|
| STATUS | PASS |
| METHOD | ROOT sửa văn bản theo chức năng mục đích; tham khảo worker A/B/C và academic-humanizer/unslop; xét từng gợi ý, không quyết định theo đa số. |
| EVIDENCE | Word P001–P006; adjudication biên tập bên dưới. |
| COUNTS | 6 đoạn, 937 token cách trắng tiếng Việt; 3 câu ví dụ nguồn; 0 bảng khoa học, hình hay phương trình. |
| FINDINGS | Giải thích vì sao chọn nhóm và phục vụ câu hỏi nào. Không giả quá trình tìm kiếm, không đóng góp mới bị mặc định, không liệt kê từng bài thành catalog. Ranh giới mô hình/quan sát/nhận dạng/kiểm chứng thể hiện theo mục tiêu viết. |
| SEVERITY | NONE |
| UNRESOLVED | Người hướng dẫn/tác giả còn có thể hiệu đính giọng văn khi nghiệm thu. |
| FINAL_DECISION | Đạt ở mức tự rà soát. |

## Gate 6 — Trích dẫn và QA Word

| Trường | Kết quả |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Kiểm citation first-use, DOI/metadata từ PDF, ZIP CRC/XML, font/lề/styles, tái tạo bytes từ CSV; kết xuất bằng ứng dụng có thật và xem ảnh mọi trang khi tạo được PDF. |
| EVIDENCE | qa_result.json trong scratch; script QA và dựng Word được chép vào EXECUTION_REPORT.md; kết quả render bên dưới. |
| COUNTS | 3 references; 3 DOI duy nhất; 3 citation occurrences; 16 phần XML/rels parse; 0 bảng glossary; 0 ảnh; 0 OMML; rendered=2; reviewed=2. |
| FINDINGS | Native Microsoft Word opened the read-only draft and minimal control but PDF export stalled. Successful final render and visual QA use LibreOffice, not Microsoft Word. M01 locator caveat is outside manuscript support. Independent acceptance and five research decisions remain pending. Đã xem mọi trang; không thấy clipping, ký tự lỗi hoặc trang trắng bất thường. |
| SEVERITY | DOCUMENTED_LIMITATION |
| UNRESOLVED | MICROSOFT_WORD_VALIDATION=NOT_VERIFIED (không ngăn kiểm LibreOffice nếu đã hoàn tất). |
| FINAL_DECISION | Đạt với giới hạn ứng dụng đã ghi. |

## Gate 7 — Bất biến nền và gói bàn giao

| Trường | Kết quả |
|---|---|
| STATUS | PASS |
| METHOD | Tính lại manifest và hash các tệp có sẵn; so git status/diff/cached trước/sau; kiểm đúng danh sách năm tệp; đọc lại các deliverable. |
| EVIDENCE | Manifest đầu vào và trạng thái Git trước tác vụ lưu bền ở EXECUTION_REPORT.md; trạng thái sau và hash DOCX bên dưới. |
| COUNTS | 456 tệp được bảo vệ bằng manifest; 382 tệp thay đổi/chưa theo dõi có sẵn giữ nguyên bytes; 5 DOCX nền đúng expected hashes; đúng 5 deliverable cuối. |
| FINDINGS | Chỉ thêm thư mục section_2_1_1. WEP/P3/WP/registry/PDF và baseline bất biến. Không cài đặt trong repository. Script/PDF/PNG/cache nằm scratch. Không stage/commit/push/merge/PR. |
| SEVERITY | NONE |
| UNRESOLVED | Nghiệm thu độc lập và human approval còn chờ. |
| FINAL_DECISION | Đạt bảo toàn và phạm vi gói; không thay thế Gate 6 hoặc nghiệm thu độc lập. |

## B01 và B02

B01: P002 giải thích ma sát phụ thuộc áp suất và kẹt dây/sợi cùng các kiến trúc đối chiếu; P003 giải thích cơ học bó TiNi và mô hình tiếp xúc; P005 giải thích phép đo, nhận dạng, độ không đảm bảo và kiểm chứng. B02: liên kết chức năng với năm RQ ở PDF6 thể hiện trong bảng dưới. Đây là `PROVISIONAL_WRITING_ORIENTATION`, `NOT_APPROVED_RQ_RECONCILIATION`; không phải quan hệ đã được WEP/P3 phê duyệt.

| RQ PDF | Đoạn | Nội dung phục vụ |
|---|---|---|
| RQ1 | P002–P003 | Giao diện dây–dây/dây–ống bao/cả hai và chiều thay đổi ứng suất tiếp xúc; không xác định trước giao diện chi phối. |
| RQ2 | P002–P003 | Nguồn áp ngoài, áp suất gần mẫu, dính/trượt một phần/toàn phần và M–κ; chưa công bố số đo MP1. |
| RQ3 | P004 | Tạo, duy trì, hồi áp; lực, hành trình, nhiệt độ, thể tích, thời gian, độ lặp lại; M34 là đối chiếu nguồn khác kiến trúc. |
| RQ4 | P004 | Bench B so với pressure-only Bench A ở cùng áp suất gần mẫu; quá độ, nhiệt, rò, độ mềm là khả năng phải xét, chưa phải nguyên nhân đã xác định. |
| RQ5 | P003,P005 | Xác nhận giao diện và truyền áp trước; khóa mô hình/tham số rồi kiểm dữ liệu dành riêng cho dự báo có xét bất định; H0b còn sống. |

## WEP của riêng §2.1.1

`WEP_211_CROSSWALK`: 01 CSV hàng dữ liệu ở dòng vật lý 60–61 là B01/B02. B01 được WEP phân loại SCIENTIFIC_CLAIM/SUPPORTED_WITH_LIMITATIONS nhưng vai trò nguồn METHODOLOGY_ONLY; tác vụ này phân loại phát biểu định hướng phạm vi là AUTHOR_SCOPE_DECLARATION theo nội dung thực tế, không sửa WEP. B02 HUMAN_DECISION_PENDING.

`WEP_211_SOURCE_BINDINGS`: 02 CSV dòng33–35 chỉ có M01-E01/E02/E03, vai trò METHODOLOGY. Ba nguồn M13/M26/M34 do ROOT chọn lại từ nguồn đã dùng trong các baseline, không được báo thành binding sẵn có của WEP §2.1.1.

`WEP_211_READINESS`: EVIDENCE_READY ở brief dòng407–434, báo cáo09 dòng30 và gate11 dòng14. Đây là readiness cho đoạn mục đích có giới hạn, không là nghiệm thu tiểu mục, cơ học hoặc RQ mapping.

`WEP_211_EVIDENCE_GAPS`: binding kỹ thuật trực tiếp tại leaf §2.1.1 và ma trận topic×PDF-RQ đã phê duyệt là NOT_DOCUMENTED. 05 không có mục so sánh riêng §2.1.1; 06 chỉ có ứng viên M01; 07 cho metadata M01 và ba nguồn trích thực tế. Không bịa binding mới để lấp chỗ trống.

`WEP_211_HUMAN_DEPENDENCIES`: reconciliation năm RQ PDF với bốn nhóm P3 và năm quyết định nghiên cứu ở WEP08 dòng35–41 vẫn pending.

## Caveat nguồn M01 và cách xử lý

ROOT đọc lại M01 physical3/25/93. PDF hash `5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0` khớp nguồn đã ghi. Physical3 là trang nhan đề; physical25 là ORIENTATIONS, printed9; physical93 là Constructing an Original Discussion of Previous Work: Using Your Own Words. Các exact-anchor WEP ghi cho E01/E02/E03 không xuất hiện ở những trang ấy. Findings được worker A phát hiện và ROOT tái kiểm text; không suy rằng nội dung phương pháp không tồn tại ở chỗ khác.

Disposition: không dùng M01 làm citation, claim support hoặc định nghĩa cơ học trong bản thảo. Mục đích tổ chức chương được coi là phạm vi tác giả từ outline. WEP và Evidence Records được giữ nguyên. Cảnh báo còn mở ở cấp đầu vào; đã loại phụ thuộc của bản thảo vào locator sai, nên không phải P1/P2 khoa học chưa xử lý trong bản thảo.

## Phân xử gợi ý của worker

A: chấp nhận làm rõ chiều thay đổi ứng suất tiếp xúc ở P002. C: chấp nhận đổi cách diễn đạt quyết định tải pháp tuyến thành lựa chọn phép đo/đại lượng đại diện; nêu phạm vi H0a lịch sử không xác định miền vận hành MP1; chuyển câu về kiến trúc đối chiếu thành mục tiêu đọc. Giữ một mệnh đề ngắn về mức xác minh nguồn vì đây là mục tiêu người dùng yêu cầu; không đưa quy ước chi tiết của §2.1.4. B: giữ ba ví dụ khoa học ngắn để neo phạm vi vào nguồn, không lặp số liệu/chi tiết ở các mục sau. Cả ba worker không cấp independent acceptance. Các số đếm dòng/raw CSV của worker B không dùng làm số record; ROOT dùng csv.DictReader và parser Word cho counts cuối.

## Kết xuất và kiểm hiển thị

```json
{
  "status": "PASS",
  "engine": "LibreOffice 24.2.7.2 420(Build:2), writer_pdf_Export",
  "docx_sha256": "c1b3571740bd20774e83fd88fab68bf0daf385ece04e7c0ed05d8f58ca12f5f5",
  "pdf_sha256": "1a20a36a1c0360dea906aafbe30c64fc52b50f0c1f4459ac3bcb78b2d7612efa",
  "rendered_pages": 2,
  "pages_visually_reviewed": 2,
  "visual_review_method": "ROOT opened full-page PNGs of both final pages after the font fix. No visible clipping, broken Vietnamese glyphs, blank page or displaced references. Heading and body fonts verified from embedded PDF fonts.",
  "fonts": [
    "TimesNewRomanPS-BoldMT",
    "TimesNewRomanPSMT"
  ],
  "rendered_text_comparison": "EXACT_AFTER_WHITESPACE_REMOVAL",
  "microsoft_word_validation": "NOT_VERIFIED",
  "limitation": "Native Microsoft Word opened the read-only draft and minimal control but PDF export stalled. Successful final render and visual QA use LibreOffice, not Microsoft Word. M01 locator caveat is outside manuscript support. Independent acceptance and five research decisions remain pending.",
  "renderer_authorization": "User explicitly allowed LibreOffice in scratch in the active conversation.",
  "renderer_scope": "52 downloaded Ubuntu packages extracted under scratch only; no system install. Portable configuration points to scratch registry; liblangtag data redirected through scratch constructor shim. Windows Times New Roman fonts used via existing fontconfig.",
  "scratch_pdf_path": "/tmp/mp1-ch211-20261020/render_final/MP1_CH2_2_1_1_DRAFT.pdf",
  "visual_page_sha256": {
    "1": "954ae65683740d17a50974512d76458a07e0cf747c49937c2e4e39785f9d33a0",
    "2": "90bc74a994e173e53c32da25b3679b40a69bf5d7d18bac9638a75b9bdea8cacd"
  },
  "first_render_finding": "Heading inherited font theme; fixed by removing theme font attributes in Word styles. Reran all anchors and XML checks, rebuilt byte-identically, rerendered and reviewed both final pages."
}
```

## Kết luận

FINAL_SELF_REVIEW_DECISION: `SELF_REVIEW_COMPLETE; AWAIT_INDEPENDENT_ACCEPTANCE`  
P1_P2_UNRESOLVED: `0`  
NEXT_ACTION: `AWAIT_INDEPENDENT_ACCEPTANCE`

Chỉ hoàn thành gói tự rà soát; tác giả và người nghiệm thu chưa chấp thuận bản thảo.
