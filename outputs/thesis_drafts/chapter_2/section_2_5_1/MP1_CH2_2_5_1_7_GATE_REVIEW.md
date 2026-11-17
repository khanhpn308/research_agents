# MP1 §2.5.1 — Báo cáo rà soát bảy cổng

**TASK_ID:** MP1-CH2-2.5.1-RESEARCH-THESIS-DRAFT  
**Trạng thái:** `PARTIAL_WITH_FINDINGS`  
**Phạm vi:** Chỉ mục 2.5.1; không mở rộng sang §2.5.2.

## GATE 1 — OUTLINE

**PASS.** B01 nêu điều kiện ma sát tĩnh/động, lực pháp tuyến và ứng suất tiếp tuyến bằng hai mức mô tả lực và traction. B02 công khai giả định về μ, phân bố p_n, biến dạng, topology và lịch sử tải. B03 nêu rõ full slip không đồng nhất với các dây uốn độc lập khi sleeve, ma sát động, normal interaction hoặc biên còn tác động. Đoạn đầu nối trực tiếp với giới hạn áp suất ở cuối §2.4.4; đoạn cuối chỉ chuyển sang cận tham chiếu của §2.5.2.

## GATE 2 — CLAIM TRACEABILITY

**PASS.** Ma trận nguồn xác nhận đúng các ánh xạ 2.5.1-A01→M07-E01, A02→M09-E03, A03→M11-E02 và A04→M13-E02. Bản traceability có 18 bản ghi: 7 `SOURCE_GROUNDED_CLAIM`, 4 `INFERENCE`, 5 `AUTHOR_PROPOSAL`, 2 `DOCUMENT_COVERAGE`. Các locator được kiểm tra trên PDF gốc; suy luận và đề xuất được gắn nhãn riêng.

## GATE 3 — PDF VÀ PHƯƠNG TRÌNH

**PASS_WITH_FINDING.** Bốn PDF gốc đã mở và đối chiếu. Các phương trình giữ lại là hai điều kiện Coulomb tổng quát và ba phương trình M13 (1)–(3), với đơn vị và giả định được khai báo. Quan hệ Q=F/2 chỉ được nêu như quy ước uốn ba điểm của M13. Phương trình M13 in cho I_J = ∫_D y dA có bất nhất thứ nguyên (m³ thay vì m⁴); phương trình này bị loại khỏi bản thảo và được ghi trong execution report. Tất cả phương trình đã đưa vào DOCX là OMML chỉnh sửa được.

## GATE 4 — TỔNG HỢP LIÊN NGHIÊN CỨU

**PASS.** Bản thảo tổng hợp theo cơ chế và mức quan sát, không viết bốn bản tóm tắt nối tiếp. M07 là lớp giấy hút chân không; M09 là dây trong bao HDPE; M11 là lớp áp suất dương ở cấp ngón; M13 là bó sợi áp suất dương trong vỏ cứng. Miền chuyển tiếp của M09 và “không thấy trượt rõ” của M11 được giữ ở cấp force–deflection, không nâng thành phép đo vi mô. Không có ngưỡng áp suất phổ quát.

## GATE 5 — GIẢ ĐỊNH VÀ GIỚI HẠN

**PASS.** Bản thảo phân biệt μ_s/μ_k, lực/traction, N/p_n, áp suất nguồn/p, full slip/independent wires và trượt/biến dạng dẻo. M13 được mô tả là mô hình sức chứa ma sát tĩnh hiệu dụng, không phải luật động. Topology MP1, đường truyền tải pháp tuyến và miền nhiệt–pha TiNi vẫn để mở.

## GATE 6 — TÍCH HỢP TRÍCH DẪN

**PASS.** Bốn nguồn có DOI và thứ tự trích dẫn lần đầu [1]–[4]. Tài liệu tham khảo, bảng và glossary dùng cùng thứ tự. Không có Paper ID/Evidence ID trong phần văn bản luận văn; các ID chỉ nằm trong tệp traceability và execution report.

## GATE 7 — CHẤT LƯỢNG TIẾNG VIỆT VÀ WORD

**PASS_WITH_FINDING.** Nội dung DOCX viết bằng tiếng Việt, có bảng Word native, header lặp, hàng không tách và glossary ba cột. Kiểm tra tĩnh xác nhận DOCX mở được, có 5 OMML equations, 2 bảng và đủ 4 tài liệu tham khảo. `WORD_RENDER_VALIDATION: NOT_VERIFIED` vì môi trường không có LibreOffice/soffice renderer; cần kiểm tra trực quan trước khi nộp.

## Findings còn lại

1. M13 có bất nhất thứ nguyên ở Eq. (4), đã không chép vào bản thảo.
2. M11 và M09 đều chỉ cung cấp quan sát cấp kết cấu; chưa có local slip mapping.
3. M13 dùng một nguyên mẫu, một loại sợi và tham số hiệu dụng; độ tổng quát còn giới hạn.
4. MP1 contact topology và phép đo/proxy lực pháp tuyến vẫn cần quyết định của người nghiên cứu.

**Kết quả bảy cổng:** `PARTIAL_WITH_FINDINGS`.


## R1 targeted DOCX hotfix

- Equations (2.5.1-1) and (2.5.1-2) now use native OMML `m:d` delimiters with `m:begChr` and `m:endChr` set to `|`; no standalone vertical-bar math runs remain in those equations.
- Inline variables in the manuscript body and Word-native tables use run-level subscript formatting for `F_t`, `μ_s`, `μ_k`, `t_t(x)`, `p_n(x)`, `τ_max`, `Q_J`, `Q_S` and `I_S`.
- The first Coulomb paragraph now reads “một tiếp xúc không có lực bám dính pháp tuyến”.
- The glossary heading and introduction use keep-with-next/page-break controls so they begin with the glossary table.
- Static checks after the hotfix: five OMML equations, two Word-native tables, 18 traceability rows and 12 terminology rows preserved.

`WORD_RENDER_VALIDATION: NOT_VERIFIED`  
`MICROSOFT_WORD_VALIDATION: NOT_VERIFIED`
