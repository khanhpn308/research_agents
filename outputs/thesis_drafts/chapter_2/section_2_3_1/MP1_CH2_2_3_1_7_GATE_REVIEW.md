# MP1-CH2-2.3.1 — Bảy cổng nghiệm thu sau remediation R1

**TASK_ID:** MP1-CH2-2.3.1-TARGETED-REMEDIATION-R1  
**Phạm vi:** Chương 2, Mục 2.3.1. Phân loại cơ chế  
**Ngày kiểm tra:** 2026-10-17 (Asia/Bangkok)

## Gate 1 — Tuân thủ dàn ý: PASS

- Hai tầng phân loại đã được thể hiện rõ. Tầng thứ nhất gồm nguyên lý cấp cao: tạo lực đối kháng, thay đổi tính chất vật liệu và thay đổi ràng buộc/cấu hình cơ khí. Tầng thứ hai là họ kiến trúc kẹt cơ học, gồm sợi/dây, lớp/tấm và hạt.
- Khóa bằng ma sát không còn được trình bày như nhóm đồng cấp loại trừ các kiến trúc jamming.
- Cơ chế thay đổi cấu hình/ràng buộc cơ khí được bổ sung ngắn gọn với cơ cấu khóa/mở, chốt, ống ràng buộc và can thiệp cơ học, có nguồn M05/M06.
- Đoạn cuối chuyển tiếp sang Mục 2.3.2.
- Bảng 2.3.1 có 6 dòng nội dung và cột “Cấp phân loại”.

## Gate 2 — Truy vết phát biểu kỹ thuật: PASS

- CSV truy vết có 10 claim, đúng cấu trúc cột bắt buộc.
- 7 claim có trạng thái `VERIFIED_FULL_TEXT`; 3 claim tổng hợp được đánh dấu `INFERENCE` và nêu giới hạn.
- C10 truy vết trực tiếp cho sơ đồ hai tầng trong bảng và được ghi là tổng hợp biên tập, không phải phân loại nguyên văn của một bài báo.
- M10 vẫn được giữ là `COMPARATOR`.
- Không có claim novelty hoặc suy luận topology MP1.
- Bằng chứng: `MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv`.

## Gate 3 — Kiểm chứng PDF gốc: PASS

Đã kiểm tra lại trực tiếp bằng PDF gốc và trích xuất văn bản tại locator đã ghi:

- M05: PDF trang 10 có Fig. 5 và Section 3.3.1; Table 4 bắt đầu trong cụm trang 10–12. Fig. 5(g) đúng là sơ đồ fibre/filament jamming. Locator cũ “Fig. 8” không được dùng.
- M06: PDF trang 3 ghi rõ dầm gồm các tấm mỏng; khóa làm các lớp cùng uốn, mở khóa cho phép trượt tương đối; Fig. 2 cùng trang.
- M09: PDF trang 4–5 ghi các môi trường kraft rope, hemp rope, nylon wire, bố trí dây và kích hoạt chân không; Fig. 2 được xác nhận.
- M10: PDF trang 2 ghi bóng cao su, hạt, bao ngoài và mẫu 26 mm × 50 mm; Fig. 1 được xác nhận.
- DOI và metadata của cả bốn nguồn vẫn giữ nguyên.

## Gate 4 — Tổng hợp liên công trình: PASS

- Bảng và thân bài phân biệt nguyên lý điều chỉnh độ cứng với medium/topology của jamming.
- Wire/rope, fibre/filament, layer/laminar và granular được đặt trong cùng họ kiến trúc nhưng ở các nhánh medium khác nhau, không bị coi là các nhóm đồng cấp với frictional locking.
- Positive pressure được giữ là phương thức kích hoạt của M10, không phải loại vật liệu và không phải lực pháp tuyến cục bộ.
- So sánh vẫn giữ các khác biệt về hình học, giao diện, đường truyền lực và điều kiện biên.

## Gate 5 — Giả định cơ học và giới hạn: PASS

- Không suy ra wire–wire hoặc wire–sleeve của bó TiNi.
- Không đồng nhất áp suất nguồn với lực pháp tuyến tại giao diện.
- Không đồng nhất jamming với biến dạng dẻo hoặc khóa tuyệt đối.
- Giới hạn chuyển giao từ layer, fibre, wire và granular sang MP1 được ghi rõ.
- Không có tuyên bố novelty.

## Gate 6 — Toàn vẹn trích dẫn và tài liệu tham khảo: PASS

- Citation [1]–[4] có đủ trong nội dung và mỗi citation có mục tài liệu tham khảo tương ứng.
- Bốn DOI, tiêu đề, tác giả, năm và nguồn xuất bản không thay đổi.
- C10 là claim tổng hợp nên được đánh dấu `INFERENCE`, không tạo reference mới.
- Không trích Writing Brief, Evidence Pack hoặc báo cáo agent như bài báo khoa học.

## Gate 7 — Văn phong thạc sĩ, tiếng Việt và thuật ngữ: PASS

- Thân bài hoàn toàn bằng tiếng Việt; tiếng Anh chỉ giữ trong ngoặc ở lần xuất hiện cần đối chiếu và trong tên bài báo.
- Bảng thuật ngữ đã chuẩn hóa các mục: kẹt cơ học, khóa bằng ma sát, kẹt sợi/filament, kẹt dây/cáp, kẹt lớp/tấm, kẹt hạt, gân kéo, truyền động chất lưu và can thiệp cơ học.
- T11 “Contact mechanics” đã được giải quyết có điều kiện thành “Cơ học tiếp xúc”. CSV ghi `VERIFIED_FROM_SOURCE_CONTEXT` và nêu rõ đây là diễn giải tổng hợp, không phải định nghĩa nguyên văn hay chuẩn HCMUT.
- Glossary có 14 thuật ngữ và không còn mục `TERMINOLOGY_REVIEW_REQUIRED`.
- Không còn thông báo template hoặc citation numbering trong thân bài.

## Layout remediation

- Đã xóa ghi chú biên tập khỏi thân bài.
- Đã đặt `cantSplit` cho mọi hàng của hai bảng.
- Đã đặt `tblHeader` cho hàng đầu của bảng so sánh và glossary.
- Đã cố định chiều rộng cột trong vùng nội dung A4; rút gọn cột trạng thái glossary.
- Đã dùng cỡ chữ nhỏ hơn cho bảng và giữ các hàng glossary không bị chia giữa trang.
- Kiểm tra XML: 2 bảng, mọi ô có nội dung, hàng đầu có cờ lặp tiêu đề, hàng có cờ không tách.

## Remediation changelog R1

1. Tái cấu trúc Bảng 2.3.1 thành hai tầng phân loại.
2. Bổ sung cơ chế thay đổi ràng buộc/cấu hình cơ khí với M05/M06.
3. Chuẩn hóa thuật ngữ và thêm tendon, fluidic, mechanical interference.
4. Giải quyết T11 theo ngữ cảnh nguồn.
5. Sửa bố cục bảng và bỏ thông báo biên tập khỏi thân bài.
6. Cập nhật traceability từ 9 lên 10 claim, thêm C10 cho bảng tổng hợp hai tầng.


## Final minor hotfix validation

- Đoạn mở đầu hiện chỉ đặt tạo lực đối kháng, thay đổi tính chất vật liệu và thay đổi ràng buộc/cấu hình cơ khí ở tầng nguyên lý cấp cao; các kiến trúc kẹt cơ học được chuyển rõ sang tầng thứ hai.
- Ô M10 trong Bảng 2.3.1 hiện ghi rõ bóng cao su, môi trường hạt bao quanh và bao ngoài không dãn.
- 42/42 run trong các ô của Bảng 2.3.1 được đặt tường minh Times New Roman 8.5 pt; hàng tiêu đề cũng dùng cùng cỡ chữ và font.
- C01 và C06 trong traceability đã được cập nhật tương ứng; các nguồn, DOI và giới hạn khoa học khác không thay đổi.

## Giới hạn còn lại

- Môi trường không có LibreOffice, soffice hoặc renderer DOCX tương đương. Vì vậy `WORD_RENDER_VALIDATION: NOT_VERIFIED`; chưa thể xác nhận trực quan số trang, tràn/cắt bảng và hiển thị font sau render.
- Cần render bên ngoài môi trường này trước khi đưa bản thảo vào luận văn chính thức.

## Final acceptance

**SEVEN_GATE_RESULT: PASS_ALL_7_GATES**  
**OVERALL_STATUS: PARTIAL_WITH_FINDINGS** do `WORD_RENDER_VALIDATION` chưa thể thực hiện trong môi trường hiện tại.
