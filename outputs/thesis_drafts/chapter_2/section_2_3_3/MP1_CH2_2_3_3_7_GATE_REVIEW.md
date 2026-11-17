# MP1-CH2-2.3.3 — Bảy cổng nghiệm thu

**TASK_ID:** MP1-CH2-2.3.3-RESEARCH-THESIS-DRAFT  
**Phạm vi:** Chương 2, Mục 2.3.3. Kẹt lớp/tấm và kẹt hạt như nhóm so sánh  
**Bối cảnh:** HCMUT–VNU-HCM, Khoa Cơ khí, Thạc sĩ Kỹ thuật Cơ khí định hướng nghiên cứu  
**Ngày kiểm tra:** 2026-10-17 (Asia/Bangkok)

## Gate 1 — Tuân thủ dàn ý: PASS

- B01 được đáp ứng bằng nguyên lý giam giữ, tiếp xúc ma sát và hạn chế chuyển động tương đối.
- B02 được đáp ứng bằng so sánh topology tiếp xúc, pressure path, medium, confinement và failure/transition behavior.
- Phạm vi chỉ gồm layer/laminar và granular comparator architectures, không viết trước §2.3.4.
- Đoạn cuối chuyển tiếp trực tiếp sang §2.3.4.

## Gate 2 — Truy vết nguồn: PASS

- CSV có 7 technical claims, 2 bản ghi `DOCUMENT_COVERAGE` cho B01/B02.
- 4 claim source-grounded và 3 claim tổng hợp được đánh dấu `INFERENCE`.
- M06/M10/M11/M12 được truy vết theo đúng Evidence IDs và PDF locators.
- Không có claim topology, constitutive law hoặc novelty của MP1.

## Gate 3 — Kiểm chứng PDF gốc: PASS

Đã mở và kiểm tra bốn PDF gốc:

- M06-E02: PDF p.5, §3.1.3; Fig. 3c minh họa chồng lớp, khoang kín khí và đường chân không. Locator này chỉ hỗ trợ cơ chế định tính, không hỗ trợ local pressure field hoặc failure law.
- M10-E01: PDF p.2, Fig. 1; bóng cao su nằm trong môi trường hạt SMP và được giữ bởi bao vải không dãn; prototype 26 mm × 50 mm được giữ như thông tin architecture-specific.
- M11-E01: PDF p.2, Fig. 1; lớp Mylar, khung PETG, túi TPU, áp suất dương và bố trí lớp trong vùng cong; các trang kết quả xác nhận trượt là giới hạn/chuyển tiếp.
- M12-E01: PDF p.3, Figs. 2–3; áp suất âm ECF dùng cho kẹt hạt, áp suất dương ECF dùng cho uốn; các phép đo tích hợp và giới hạn hiệu chuẩn được kiểm tra thêm ở các trang kết quả.

## Gate 4 — Tổng hợp khoa học: PASS

- M06 và M11 được so sánh như hai pressure paths của layer jamming.
- M10 và M12 được so sánh như granular architectures, trong đó M12 tách rõ hai chức năng áp suất.
- M10 được diễn giải đúng: tải uốn bên ngoài tạo độ võng, còn mạng hạt và biên giam giữ chi phối độ cứng/đáp ứng.
- Bảng so sánh phân biệt medium, contact topology, confinement, pressure path và chuyển trạng thái.
- Prose là tổng hợp liên công trình, không phải danh sách tóm tắt riêng lẻ.

## Gate 5 — Giả định và giới hạn cơ học: PASS

- Không đồng nhất pressure source với local normal contact force.
- “Sức kháng ma sát truyền được” được tách khỏi actual friction force.
- Không đồng nhất interlayer slip với granular contact rearrangement.
- Không đồng nhất positive-pressure actuation với positive-pressure granular locking trong M12.
- Buckling và interfacial slip được giữ là các hiện tượng khác nhau.
- Không chuyển mô hình, pressure range, stiffness ratio hoặc failure mode sang MP1.

## Gate 6 — Toàn vẹn citation: PASS

- Citation [1]–[4] khớp bốn reference entries.
- DOI, tác giả, năm, tiêu đề và nguồn xuất bản đã được đối chiếu.
- Không có reference không được trích dẫn hoặc citation không có reference.
- Citation numbering là provisional cho bản thảo độc lập.

## Gate 7 — Văn phong thạc sĩ, tiếng Việt và thuật ngữ: PASS

- Thân bài viết bằng tiếng Việt; thuật ngữ Anh chỉ giữ trong ngoặc hoặc tên riêng cần thiết.
- Glossary có 13 thuật ngữ và được trình bày dạng bảng 6 cột rút gọn; CSV vẫn giữ đầy đủ định nghĩa, trạng thái và giới hạn.
- Các thuật ngữ “kẹt lớp/tấm”, “kẹt hạt”, “giam giữ”, “chênh áp”, “đường truyền áp suất”, “lực tiếp xúc pháp tuyến” và “oằn” được dùng nhất quán.
- Không có Paper ID, Evidence ID, QA note hoặc lịch sử kiểm chứng PDF trong thân bản thảo.

## Kiểm tra cấu trúc DOCX

- A4 portrait, 6 đoạn thân bài, caption Word-native trước bảng.
- Bảng so sánh 6 cột và glossary 6 cột.
- Header lặp lại, hàng không tách, page break trước glossary.
- Font các run trong bảng được đặt tường minh Times New Roman 8.5 pt.
- ZIP integrity và mở lại DOCX đạt.


## Targeted hotfix R1

- Đã xóa B01/B02 khỏi thân prose; các mã này chỉ còn trong Gate Review và Source Traceability.
- Đã đổi attribution M06 thành phần tổng quan của Caro và Carmichael.
- Đã sửa diễn giải ma sát theo sức kháng truyền được, không khẳng định actual friction force tăng.
- Đã sửa M10 để tách tải uốn bên ngoài khỏi ảnh hưởng của mạng tiếp xúc hạt.
- Đã rút gọn các câu giới hạn lặp nhưng giữ các khác biệt architecture-specific.
- Đã rút glossary DOCX còn 6 cột, giảm padding và văn bản hiển thị; giữ đủ 13 thuật ngữ và CSV đầy đủ.
- C01, C02 và C04 đã được cập nhật trong traceability; số technical claims vẫn là 7 và document-coverage records là 2.

## Giới hạn còn lại

- Không có LibreOffice, soffice hoặc renderer DOCX trong môi trường. Vì vậy `WORD_RENDER_VALIDATION: NOT_VERIFIED`.
- Các nguồn là architecture-specific; không xác lập contact topology hoặc constitutive law cho bó dây TiNi.

## Final acceptance

**SEVEN_GATE_RESULT: PASS_ALL_7_GATES**  
**OVERALL_STATUS: PARTIAL_WITH_FINDINGS** do chưa thể render và kiểm tra trực quan từng trang.
