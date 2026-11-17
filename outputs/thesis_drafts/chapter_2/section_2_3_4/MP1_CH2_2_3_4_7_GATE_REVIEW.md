# MP1-CH2-2.3.4 — BÁO CÁO BẢY CỔNG NGHIỆM THU

## Trạng thái

**Sắp xếp:** PASS_ALL_7_GATES về nội dung và cấu trúc; `WORD_RENDER_VALIDATION: NOT_VERIFIED` vì môi trường không có trình kết xuất DOCX khả dụng.

## Gate 1 — Outline compliance: PASS

- B01 được bao phủ bằng đối chiếu M06, M07, M10 và M13, gồm công trình trước áp suất dương năm 2026.
- B02 được bao phủ bằng phân biệt áp suất nguồn, áp suất hiệu dụng p, Q_J, Q_S, độ cứng và ba miền trạng thái.
- B03 được bao phủ: áp suất dương, bó sợi, mô hình chuyển trạng thái và kiểm chứng uốn đã có tiền lệ ở kiến trúc khác; không tuyên bố novelty MP1.
- Phạm vi dừng ở áp suất dương jamming và state regimes, có chuyển tiếp sang §2.3.5.

## Gate 2 — Source traceability: PASS

- 11 technical claims (C01–C11) và 2 document-coverage records (D01–D02).
- M06/M07/M10/M13 được gắn đúng vai trò DIRECT_SUPPORT, COMPARATOR, CONTEXT_ONLY hoặc INFERENCE.
- Phương trình có locator Eqs. (1)–(3), biến, đơn vị và giới hạn trong CSV.

## Gate 3 — Original PDF and equation verification: PASS

- Đã mở và kiểm tra trực tiếp bốn PDF gốc.
- M13 Eqs. (1)–(3) được đối chiếu: Q [N], τ [Pa], μ không thứ nguyên, p [Pa], k và A [m²]; các tích cho ra lực.
- M13 p được giữ là áp suất kẹt hiệu dụng theo giả thiết của tác giả; không đổi thành áp suất nguồn hay lực pháp tuyến.
- Không sử dụng Eq. (4) của M13 vì bản in thể hiện biểu thức mô men quán tính có vấn đề thứ nguyên; phương trình không cần thiết cho §2.3.4.

## Gate 4 — Scientific synthesis: PASS

- Vacuum laminar, áp suất dương granular và áp suất dương fibre được so sánh theo đường truyền áp suất, topology tiếp xúc, đại lượng quan sát và miền trạng thái.
- M07 chỉ dùng làm comparator vacuum; M10 làm precedent granular; M13 là direct áp suất dương fibre precedent; M06 là review-level mechanism source.
- Bảng 2.3.4 là bảng tổng hợp do tác giả xây dựng.

## Gate 5 — Mechanical limitations: PASS

- Không đồng nhất áp suất nguồn với lực pháp tuyến cục bộ.
- Không đồng nhất Q_J/Q_S với độ cứng hoặc định luật vật liệu.
- Không đồng nhất trượt hoàn toàn với biến dạng dẻo.
- Giữ rõ giới hạn M13: một nguyên mẫu, một loại/kích thước/số sợi, áp suất không đều, tham số hiệu dụng và nội suy hiện tượng học.
- Không suy diễn topology, luật truyền áp suất hoặc novelty của MP1.

## Gate 6 — Citation and reference integrity: PASS

- Bốn citation [1]–[4] đều có reference; không có reference không được dùng.
- DOI và metadata đối chiếu với Source Matrix và PDF gốc.
- Số hiệu equation (1)–(3) được quy về M13 trong prose và traceability.

## Gate 7 — Vietnamese MSc writing quality: PASS

- Prose, bảng, chú thích và diễn giải phương trình bằng tiếng Việt; tên bài báo/DOI giữ nguyên.
- Thuật ngữ được lập thành 18 mục, CSV giữ đầy đủ định nghĩa và trạng thái.
- Không có Paper IDs, Evidence IDs, outline IDs, locator logs hay workflow notes trong manuscript prose.
- Bảng có caption Word-native, header lặp, hàng không tách và cỡ chữ bảng đặt tường minh.

## Kiểm tra tài liệu

- DOCX ZIP integrity: PASS.
- Unicode tiếng Việt: PASS.
- 4 DOI strings và citation closure: PASS.
- Tables: 2; figures: 0; equations: 3 (M13 Eqs. 1–3).
- Render trực quan từng trang: NOT_VERIFIED (thiếu LibreOffice/soffice/pandoc).

## Giới hạn còn lại

- Không có kiểm tra trực quan trang; cần render bên ngoài trước khi hợp nhất chương.
- M06 là review và không thay thế dữ liệu gốc của các nghiên cứu mà review trích dẫn.
- M13 chỉ kiểm chứng một kiến trúc và một nguyên mẫu; không đủ để chuyển mô hình sang bó dây TiNi hoặc dầm kẹt lớp.

## Targeted hotfix R1

- Đổi tiêu đề thành “2.3.4. Cơ chế kẹt dưới áp suất dương và các miền trạng thái”.
- Xác minh và sửa thứ tự tác giả tài liệu [3] theo trang tiêu đề PDF: T. Liu, H. Xia, D.-Y. Lee, A. Firouzeh, Y.-L. Park và K.-J. Cho.
- Thay ba biểu thức M13 bằng phương trình Word OMML có chỉ số dưới chỉnh sửa được; đánh số (1)–(3) là đánh số tạm thời trong bản mục độc lập.
- Làm rõ trong prose rằng Q = F/2 là quy đổi của phép uốn ba điểm; E được nhận dạng từ đáp ứng uốn p = 0, còn μ được nhận dạng từ độ dốc Q_S–p của ngưỡng trượt hoàn toàn. Không coi E hoặc μ là phép đo vật liệu độc lập.
- Bảng thuật ngữ vẫn giữ 18 mục; DOCX dùng ghi chú tiếng Việt ngắn, CSV giữ nguyên trường chi tiết.
- DOCX ZIP, OMML, citation/DOI closure, traceability, 18 thuật ngữ và định dạng bảng: PASS.
- M13 dùng Q = F/2 cho cấu hình uốn ba điểm; E lấy từ đáp ứng p = 0, còn μ lấy từ độ dốc Q_S–p; cả hai là tham số hiệu dụng, không phải phép đo vật liệu độc lập.
- Vị trí trang của bốn tài liệu tham khảo đã được làm gọn bằng keep-with-next, nhưng chưa thể xác nhận trực quan.
- WORD_RENDER_VALIDATION: NOT_VERIFIED; không có LibreOffice/soffice/pandoc.

## Final micro-hotfix R2

- Đã xóa đoạn trống mang page break trùng ngay trước tiêu đề phụ lục; chỉ còn một page break trước glossary.
- Đã sửa riêng nguồn T01 trong DOCX thành `[3], [4]`, khớp với TERMINOLOGY.csv; 17 mục còn lại không thay đổi.
- Ba phương trình OMML, 11 technical claims, 2 document-coverage records và 18 thuật ngữ được giữ nguyên.
- Seven-gate scientific/document checks: PASS; WORD_RENDER_VALIDATION: NOT_VERIFIED.
