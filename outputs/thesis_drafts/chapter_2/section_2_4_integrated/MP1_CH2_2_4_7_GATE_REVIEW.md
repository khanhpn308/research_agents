# Rà soát bảy cổng tích hợp mục 2.4

TASK_ID: MP1-CH2-2.4-INTEGRATION-AND-CONSISTENCY-REVIEW  
STATUS: PARTIAL_WITH_FINDINGS  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: PARTIAL_LIBREOFFICE_VERIFIED_MS_WORD_NOT_VERIFIED

## Thẩm quyền và phạm vi xác minh

ROOT chịu trách nhiệm quyết định cuối; kiểm tra độc lập tài liệu sau dựng được báo riêng. Kế thừa mức chấp nhận của bốn baseline, không coi sự tồn tại tệp là PASS khoa học. Kiểm tra trực tiếp mới giới hạn ở định danh 13 DOI/PDF, xung đột metadata và phương trình OMML M33 thực sự được giữ. Các nhận định còn lại giữ nguyên trạng thái/locator và giới hạn từ hồ sơ được chấp nhận. Không tìm kiếm tài liệu, không xác minh lại toàn bộ PDF hoặc dữ liệu thô. Thuật ngữ `VERIFIED FULL TEXT`, `METADATA ONLY`, `INFERENCE` được dùng đúng phạm vi đó.

## Bảy cổng khoa học và tài liệu

| Cổng | Kết quả | Kiểm tra hoàn tất và giới hạn |
|---|---|---|
| 1. Dàn ý và cấu trúc | PARTIAL_WITH_FINDINGS | Đủ 2.4.1–4 đúng thứ tự, bốn câu chuyển logic, không có 2.4.5 hoặc nội dung 2.5/2.6 mới. Mọi ý đã có giữ lại. Bảo lưu hạn chế bao phủ nhiệt độ/tốc độ 2.4.1 và bện/bao 2.4.2; không nâng baseline thành bằng chứng đầy đủ. |
| 2. Truy xuất | PASS, phạm vi tích hợp | 123/123 hồ sơ, ID gốc và toàn trường gốc còn trong JSON, 123 ID tích hợp duy nhất; gắn vị trí Word/hoặc nói rõ chỉ ở hồ sơ. Nguồn 79, suy luận 28, đề xuất 9, bao phủ 7 theo nhãn gốc; metadata/glossary không tính kết quả kỹ thuật. Vai trò claim-specific giữ nguyên. |
| 3. Nguồn và phương trình | PASS, có giới hạn kế thừa | Không sửa nguồn; M27 7×7 right regular lay/1×27 alternating lay được giữ; M23 k_i chưa rõ đơn vị; M31 dây–cao su; M12 ECF áp âm tạo kẹt/áp dương tạo uốn. Một OMML Q_out ≥ Q_in của M33 khớp PDF trang vật lý 3/trang in 538 và XML gốc; không nâng trạng thái nhóm khác. |
| 4. Tổng hợp khoa học giữa các mục | PASS | Chuỗi vật liệu → kết cấu/tiếp xúc → SMA siết giao diện → tạo và truyền áp được giữ qua sáu sửa giới hạn và hợp nhất tài liệu/thuật ngữ. Rút ba phần lặp thật, giữ nhắc lại phục vụ lập luận riêng. Không coi các kiến trúc nguồn tương đương MP1. |
| 5. Giả định và giới hạn cơ học | PASS | E/EI/K, lực/ứng suất, nguồn/mẫu/tiếp xúc, ma sát thực/khả năng truyền, tự do/chịu tải/lực khóa, nhiệt chấp hành/bó, trễ vật liệu/tiếp xúc/độ trễ thời gian và hiệu chuẩn/hiệu chỉnh/kiểm chứng được phân biệt. Topology, miền hoạt động và tham số MP1 vẫn mở; không H1, novelty hoặc luật mới. |
| 6. Trích dẫn và danh mục | PASS | 14 mapping/13 DOI, lần đầu 1–13 kể cả bảng; body/table/định nghĩa/ngữ cảnh/nguồn glossary đóng kín. 186 kiểm tra đoạn/ô xác nhận đúng danh tính và locator, số trang không bị đổi. Một bibliography, không mất nguồn. Metadata M25 và M33 được quyết định theo PDF. |
| 7. Tiếng Việt MSc và DOCX | PARTIAL_WITH_FINDINGS | Văn xuôi và định nghĩa Việt, trừ thuật ngữ Anh/tên xuất bản cần thiết; không ID audit trong thân. Word-native, A4/TNR, năm bảng, chú thích duy nhất, hàng lặp/không tách, một glossary, OMML chỉnh sửa được. Chưa xác minh trực quan từng trang vì không có renderer. Không tuyên bố bảng dễ đọc/trang trắng/không mồ côi đã PASS. |

## Kiểm tra bắt buộc bổ sung

| Kiểm tra | Trạng thái | Bằng chứng |
|---|---|---|
| BASELINE_IMMUTABILITY | PASS | 20 hash trước/sau giống nhau; 193 tệp hỗ trợ cũng không đổi. |
| CITATION_MAP_CLOSURE / CITATION_MAPPING_CLOSURE | PASS | 14 khóa section+old number, cùng 13 DOI và 13 số tham khảo. |
| GLOSSARY_CONTEXT_CITATION_CHECK | PASS | Đối chiếu mọi ô định nghĩa/ngữ cảnh/nguồn với master; marker nguồn chuyển số thật, không chỉ đổi cột Nguồn. |
| TRACEABILITY_COMPLETENESS | PASS | 123 record giữ nguyên JSON gốc, không khóa gốc thiếu/trùng; trạng thái hiện diện nêu rõ. |
| CROSS_SECTION_CONTRADICTION_REVIEW | PASS, phạm vi tích hợp | Không còn mâu thuẫn vật lý mới; sửa hiệu chuẩn/kiểm chứng và metadata, giữ bất định nguồn. |
| SCIENCE_CONTENT_PRESERVATION / SCIENTIFIC_CONTENT_PRESERVED | PASS, phạm vi bản thảo | 82 phần tử và 186 đoạn/ô giữ nội dung/số liệu ngoài sáu chỉnh sửa duyệt. Không đồng nghĩa tái kiểm chứng kết quả nguồn. |
| TABLE_CAPTION_INTEGRITY | PASS_STATIC | Bốn bảng 2.4.1–4 và một Bảng A.2, năm caption duy nhất; mapping giữ mọi hàng khoa học. |
| EQUATION_PRESERVATION / EQUATION_INTEGRITY | PASS, compatibility remediation | Một OMML editable giữ Q_out ≥ Q_in; R1 thêm m:nor cho hai nhãn chỉ số, không đổi ký hiệu/ý nghĩa/nguồn. XML không còn byte-identical với baseline do sửa có chủ đích. |
| GLOSSARY_CITATION_CLOSURE | PASS | 88 mục, đủ 93 ánh xạ; không còn citation cục bộ sai danh tính hoặc marker M trong Word. |
| WORD_RENDER_VALIDATION | PARTIAL_LIBREOFFICE_VERIFIED_MS_WORD_NOT_VERIFIED | LibreOffice 24.2.7 render và visual review đã hoàn tất; MS Word chưa chạy. |

## QA độc lập sau dựng

Trạng thái: PASS_STATIC_BOUNDED.

# QA độc lập sau dựng — tích hợp mục 2.4

Trạng thái: PASS_STATIC_BOUNDED (kiểm tra tĩnh có giới hạn). Không còn phát hiện chặn. Trực quan: NOT_VERIFIED.

## Phạm vi và cách kiểm tra

Đã mở lại đủ bảy tệp giao nộp trong `outputs/thesis_drafts/chapter_2/section_2_4_integrated`, bốn DOCX và tám CSV đầu vào cùng ba báo cáo Markdown tích hợp. Đối chiếu trực tiếp ZIP/XML DOCX, các dòng CSV và hash tệp thực; không chỉ đọc kết quả ROOT. Không sửa bảy tệp cuối, không tìm tài liệu mới, không trích lại toàn bộ PDF. Script kiểm độc lập: `/tmp/MP1-CH2-2.4-INTEGRATION/qa_independent_check.py`.

## Phát hiện đã được khắc phục và kiểm lại

F02 — ĐÃ KHẮC PHỤC VÀ KIỂM LẠI. Bản dựng trước: `MP1_CH2_2_4_INTEGRATED.docx`, `word/document.xml`, thuộc tính hàng của bốn bảng khoa học: có bốn node `w:tblHeader` thừa và 18 node `w:cantSplit` thừa. Mỗi hàng tiêu đề khoa học có hai node đánh dấu lặp; tất cả 18 hàng khoa học có hai node không tách hàng. Nội dung/chiều rộng bảng đúng, nhưng cần chuẩn hóa còn một node mỗi loại để không dựa vào cách Word xử lý thuộc tính singleton lặp. Đây là sửa cấu trúc, không sửa khoa học.

N01 — ĐÃ KHẮC PHỤC VÀ KIỂM LẠI. Bản dựng trước: glossary, hàng dữ liệu 38, cột ngữ cảnh, còn hai literal `k_i`. Nên dùng chỉ số dưới Word cho `i` để thống nhất cách trình bày ký hiệu. Điều này không xác minh hoặc gán đơn vị cho k_i.

F01 — ĐÃ KHẮC PHỤC khi kiểm lại CSV: cột `verified_physical_page` từng có `2, A`, `18, ana`, `D`, `a` do regex bắt cả chữ trong locator. ROOT đã sửa bộ tách; đọc lại tệp thực không còn các giá trị này. Locator và toàn bộ JSON gốc vẫn giữ nguyên. Không coi F01 là phát hiện còn mở.

## Kết quả xác nhận

| Kiểm tra | Kết quả độc lập |
|---|---|
| Số tệp cuối | Đúng 7, tất cả không rỗng, mở đọc được. |
| Citation | 14 ánh xạ cục bộ → 13 nguồn/DOI; thứ tự lần đầu 1–13 đúng theo thứ tự thân và bảng; 13 bibliography DOI đóng kín. |
| Bảo toàn nội dung | 82 phần tử nguồn, 186 đoạn/ô đối chiếu trực tiếp bản gốc hoặc đúng sáu sửa S01–S06 đã duyệt; danh tính citation và locator giữ nguyên. |
| Glossary CSV | 1.056 trường của 88 mục khớp approved_terminology sau đổi marker nguồn; gồm định nghĩa, ngữ cảnh, quy nguồn và giới hạn, không chỉ cột nguồn. |
| Glossary Word | 440 ô hiển thị (88×5), gồm 88 ô Nguồn, khớp CSV/approved và quy nguồn/ngữ cảnh tương ứng; 93 khóa thuật ngữ gốc đủ, không trùng khóa hoặc mất khóa. |
| Traceability | 123 `original_record_json` khớp toàn bộ record của từng CSV gốc; claim_summary giữ nguyên. Phân loại: 79 theo nguồn, 28 suy luận, 9 đề xuất, 7 bao phủ. |
| Phân biệt thống kê | Metadata 2.4.4 C14 và ghi chú glossary C35 không là kết quả kỹ thuật; giữ nhãn gốc, không làm thành kết quả mới. |
| Bất biến | SHA-256 của 20 đầu vào và 193 tệp hỗ trợ khớp baseline; không có mismatch. |
| Phương trình | Một OMML chỉnh sửa được; XML chính xác như bản 2.4.4 gốc, SHA-256 `98fb9a6775e1874ece4728d56f6d084e9e4ce8e4925e12f493bc0faf0549ca0f`. |
| Chỉ số dưới | Run Word `out`, `in` của Q được giữ; không thay dấu ≥ nguồn. |
| Bảng | 4 bảng khoa học 5×6,5×6,4×6,4×6; glossary 89×5; năm bảng native, mỗi grid 9.071 twip; 107 hàng có cantSplit; header được đánh dấu lặp. Đã chuẩn hóa: 0 node thuộc tính hàng thừa. |
| Phạm vi Word | Bốn tiểu mục 2.4.1–4, không có 2.4.5/2.5; không process ID nguồn Mxx/WEP/ROOT/TASK_ID trong thân kể cả bảng/glossary. |
| Báo cáo | Ba Markdown giữ QA PENDING tại thời điểm đọc; kết quả chung PARTIAL_WITH_FINDINGS, render NOT_VERIFIED, không tự nâng kiểm chứng nguồn kế thừa thành kiểm lại toàn văn. |

## Metadata và nguồn chứng cứ

Đã đọc các trích xuất trang đầu có sẵn `M25_front.txt`, `M33_front.txt`, `M22_front.txt` và đối chiếu bibliography thực trong DOCX. M25: trang bìa xác nhận tạp chí *Mechanics of Advanced Materials and Structures*, tác giả Vahidi/Arghavani/Choi/Ostadrahimi, DOI `10.1080/15376494.2021.1955313`, online 03/08/2021; bản tích hợp dùng online 2021, không suy năm số báo 2022 từ tên tệp. M33: tiêu đề/tác giả và DOI `10.1109/TMECH.2012.2211032` khớp; header số báo tập 18 số 2 tháng 4/2013, ghi công bố trực tuyến 20/08/2012; bibliography phân biệt đúng hai mốc. M22: DOI đầy đủ có dấu ngoặc `(ASCE)`, không giữ dạng trường metadata bị cắt.

Đây là kiểm tra tính nhất quán của gói tích hợp đối với chứng cứ đã có; không phải kiểm chứng lại toàn bộ 123 nhận định với PDF. Trạng thái VERIFIED_FULL_TEXT của các record khoa học được kế thừa hồ sơ gốc. Trích xuất trang đầu là chứng cứ văn bản được cung cấp trong phiên, không phải kiểm tra trực quan độc lập PDF. Không đưa ra phán quyết tính mới.

## Giới hạn trực quan

Đây là trạng thái trước remediation R1. R1 đã render bằng LibreOffice 24.2.7 và kiểm tra các bảng/glossary/equation; Microsoft Word vẫn chưa chạy. WORD_RENDER_VALIDATION cuối cùng được ghi ở phần Layout remediation R1.

F03 — ĐÃ KHẮC PHỤC VÀ KIỂM LẠI: hai ô Nguồn glossary hàng 71/73 hiện chỉ ghi “Tổng hợp biên soạn”; ví dụ [12]/[11] giữ trong ngữ cảnh. Không nâng ví dụ ngữ cảnh thành quy nguồn cho định nghĩa. F02 có 0 thuộc tính thừa, N01 có hai i subscript, F01 không tái xuất hiện. Đã chạy lại toàn bộ script độc lập trên DOCX cuối 71.857 bytes và CSV thực: mọi kiểm tra tĩnh PASS, số kỹ thuật 78/27/9 chính xác. Không còn findings/blocking_findings. ROOT cần cập nhật ba báo cáo tạm và hash sau khi nhận QA này; QA PENDING trong bản đọc trước không phải lỗi khoa học.

## Hash hiện vật đã kiểm lần cuối

- `MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv`: `3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23`
- `MP1_CH2_2_4_MASTER_TERMINOLOGY.csv`: `eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534`
- `MP1_CH2_2_4_INTEGRATED.docx`: `4d6bdbb0d189a86214044f108c9e1e809f022c980874d8acd9dbae3e690777c7`
- `MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv`: `d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49`


## Giới hạn và kết luận ROOT

- Đây là trạng thái trước remediation R1. R1 đã render bằng LibreOffice 24.2.7 và kiểm tra các trang bảng/glossary/equation; Microsoft Word vẫn chưa chạy. Kiểm tra Word riêng vẫn còn cần thiết.
- Đơn vị k_i ở phương trình (15) của M23 giữ `UNVERIFIED_UNITS_EQUATION_TEXT_VERIFIED`; không gán đơn vị, không sử dụng phương trình hay đồng nhất với k của M22.
- Giới hạn nhiệt độ/tốc độ của M26/M27; kéo khác uốn; thí nghiệm thép khác mô phỏng NiTi; hiệu chỉnh và dữ liệu Chen được dùng lại không thành kiểm chứng độc lập.
- M31 đo tiếp xúc dây–cao su; M32 tách nguyên mẫu SMP/SMA; M37 chưa tách độc lập pha R, nguồn dây, xử lý nhiệt và Af. Bất nhất nhãn xử lý nhiệt M37 và tiêu chí tỷ số phục hồi M32 không được tự giải quyết.
- M12 là ECF, áp âm tạo kẹt hạt còn áp dương tạo uốn; nhãn áp từ bơm riêng không thành áp khoang đo trực tiếp. M33 là bơm SMA ướt; M34 là cuộn SMA–vỏ mềm, không tự thành piston MP1.
- M33 chỉ có (1) được giữ và kiểm tra lại trong lần tích hợp. Giới hạn và dấu hiệu sai khác hệ số ở nhóm (8)/(9) đã ghi trong hồ sơ gốc vẫn ngoài phạm vi sử dụng; không tuyên bố toàn bộ phương trình M33 đã xác minh.
- Năm số báo 2022 của M25 chưa được PDF cung cấp xác nhận; bản tích hợp dùng trực tuyến 03/08/2021, không suy năm từ tên tệp.
- Topology dây–dây/dây–bao, môi chất, miền pha/nhiệt của dây chịu tải và SMA chấp hành, đường truyền áp suất, thông số phớt/rò/độ mềm, tải pháp tuyến cục bộ, hệ số ma sát, đại lượng uốn và khả năng nhận dạng MP1 vẫn mở. Không có luật áp suất–tiếp xúc–độ cứng hoặc kết luận tính mới/H1 mới.

Chấp nhận bản tích hợp như bản thảo tổng quan có giới hạn bằng chứng. Không có sai sót nguồn hoặc phương trình trọng yếu mới chưa xử lý trong phần được giữ. Không chấp nhận mọi yêu cầu bảy cổng ở mức PASS_ALL_7_GATES khi cổng 1 còn giới hạn kế thừa và cổng 7 chưa kết xuất. Bước tiếp theo là kiểm tra trình bày từng trang bằng renderer; dừng ở bảy tệp này.


## Layout remediation R1 — visual review

**GATE 7 update:** PARTIAL_WITH_FINDINGS. LibreOffice 24.2.7 rendered the baseline and three layout candidates. The selected candidate is the `m:nor` variant.

- Baseline: 29 A4 pages; rendered equation shows a malformed red right-hand subscript glyph.
- Selected candidate: 23 A4 pages; four comparison tables and glossary pages were visually inspected at rendered zoom. The tables have no visible clipping or mid-word breaks; the glossary has three readable columns, repeated headers and no visible clipping.
- Equation: `Q_out ≥ Q_in` renders correctly in LibreOffice with both subscripts. The selected candidate retains one editable OMML object and adds only normal-text math-run properties to the subscript labels.
- Candidate choice: the layout-only and Cambria variants did not correct the LibreOffice equation. Cambria Math is unavailable on the host.
- Microsoft Word was not executed. `WORD_RENDER_VALIDATION` is therefore not a full cross-renderer PASS.

The layout change does not alter the four subsection headings, source claims, citations, references, traceability, terminology meanings, tables' cell information, or source limitations.

FINAL_DOCX_SHA256: `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea`
