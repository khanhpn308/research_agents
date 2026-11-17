# MP1 — Gate review tích hợp mục 2.3

## GATE 1 — OUTLINE AND STRUCTURE

**PASS.** Có đủ năm tiêu đề theo thứ tự 2.3.1. Phân loại cơ chế → 2.3.2. Kẹt dây/sợi → 2.3.3. Kẹt lớp/tấm và kẹt hạt như nhóm so sánh → 2.3.4. Cơ chế kẹt dưới áp suất dương và các miền trạng thái → 2.3.5. Tổng hợp các nghiên cứu về cơ chế jamming; năm bảng so sánh được giữ và các đoạn chuyển mục gốc vẫn còn.

## GATE 2 — CLAIM TRACEABILITY

**PASS.** Register hợp nhất có 55 claim-level records, giữ original section/claim ID, integrated claim ID, source/evidence locator, role, category và limitation. Phân loại: Counter({'SOURCE_GROUNDED_CLAIM': 33, 'INFERENCE': 13, 'DOCUMENT_COVERAGE': 8, 'AUTHOR_PROPOSAL': 1}). Không có document-coverage record nào được tính như claim kỹ thuật.

## GATE 3 — ORIGINAL SOURCE AND EQUATION INTEGRITY

**PASS.** Ba phần tử OMML được giữ trong `word/document.xml`; không có bitmap equation. Các quan hệ và ký hiệu của Zhang–Yao không bị thay đổi. Không thêm claim định lượng mới.

## GATE 4 — CROSS-SECTION SYNTHESIS

**PASS WITH NOTES.** Chuỗi lập luận đi từ phân loại → dây/sợi → lớp/hạt → áp suất dương và miền trạng thái → tổng hợp. Lặp lại về giam giữ, áp suất nguồn và giới hạn topology được giữ ở nơi cần cho lập luận; danh mục nguồn và bảng thuật ngữ lặp đã được hợp nhất.

## GATE 5 — SCIENTIFIC LIMITATIONS

**PASS.** Văn bản giữ các phân biệt E/EI, độ cứng kết cấu, slope lực–độ võng, moment–curvature, áp suất nguồn/mẫu/hiệu dụng, lực ma sát và sức kháng ma sát cực đại; không khẳng định topology MP1, luật áp suất–lực cục bộ hoặc tính mới đã xác minh.

## GATE 6 — CITATION AND REFERENCE INTEGRITY

**PASS.** 24 citation mappings cục bộ ánh xạ vào 11 DOI duy nhất. Các số [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] xuất hiện trước danh mục tham khảo; danh mục có 11 mục và không có mục không được trích dẫn. Citation trong bảng và glossary đã đổi theo mapping.

## GATE 7 — VIETNAMESE MSc WRITING AND DOCUMENT QUALITY

**PARTIAL_WITH_FINDINGS.** Văn bản và nhãn bảng/thuật ngữ dùng tiếng Việt; DOCX có bảng Word-native, font Times New Roman và OMML. Kiểm tra bố cục trực quan chưa xác minh vì không có renderer.

## Kiểm tra tích hợp bắt buộc

- **INTEGRATION_SOURCE_IMMUTABILITY: PASS** — hash năm baseline không đổi sau tích hợp.
- **CITATION_MAPPING_CLOSURE: PASS** — citation trước bibliography = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]; bibliography = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
- **EQUATION_PRESERVATION: PASS** — OMML count = 3; expected = 3.
- **TERMINOLOGY_DEDUPLICATION: PASS** — 58 khái niệm duy nhất trong master CSV và một bảng glossary.
- **CROSS_SECTION_REDUNDANCY_REVIEW: PASS WITH NOTES** — lặp khoa học cần thiết được giữ; lặp bibliography/glossary được bỏ.
- **TABLE_CAPTION_INTEGRITY: PASS** — năm caption Bảng 2.3.1–2.3.5 và một caption Bảng A.1; tổng 6 bảng.
- **WORD_RENDER_VALIDATION: NOT_VERIFIED** — không có renderer khả dụng.
- **DOCX_ZIP_INTEGRITY: PASS** — `testzip()` = None; page-break XML còn lại = 0.

## Kết luận

Đầu ra đạt các cổng khoa học và dữ liệu ở mức tĩnh, nhưng trạng thái tổng thể là **PARTIAL_WITH_FINDINGS** vì chưa thể kiểm tra kết xuất trang thực tế.

## Re-evaluation sau hotfix

- **GLOSSARY_CITATION_RECONCILIATION: PASS** — mười contextual_usage stale citations đã ánh xạ tường minh tới [6]/[7]; không còn citation cục bộ [2]/[4] trong các trường bị ảnh hưởng.
- **GLOSSARY_PRESENTATION: PASS_STATIC** — glossary có 5 cột, 58 thuật ngữ, không còn mã `VERIFIED_FROM_*`, hàng tiêu đề lặp và hàng không tách.
- **MULTI_CITATION_ORDERING: PASS_STATIC** — các nhóm citation nhiều nguồn trong thân văn bản, bảng và glossary được sắp theo số tích hợp tăng dần.
- **EDITORIAL_NOTICE_REMOVAL: PASS** — ghi chú đánh số tạm thời không còn trong DOCX.
- **WORD_RENDER_VALIDATION: NOT_VERIFIED** — vẫn không có renderer Word/LibreOffice khả dụng.

Kết luận bảy gate vẫn là **PARTIAL_WITH_FINDINGS** chỉ vì kiểm tra kết xuất trực quan chưa thực hiện được; các sửa lỗi citation và glossary đạt kiểm tra tĩnh.
