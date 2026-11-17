# MP1-CH2-2.3.1 — Báo cáo thực thi remediation R1

## Định danh

- **TASK_ID:** MP1-CH2-2.3.1-TARGETED-REMEDIATION-R1
- **Mục tiêu:** Sửa có mục tiêu Mục 2.3.1, không tái trích xuất toàn corpus
- **Bối cảnh:** HCMUT / VNU-HCM / Khoa Cơ khí / Thạc sĩ định hướng nghiên cứu
- **Đề tài:** Đặc trưng độ cứng uốn của bó dây TiNi dưới cơ cấu ma sát điều khiển bằng áp suất dương từ piston dẫn động bằng lò xo SMA
- **Ngôn ngữ:** Tiếng Việt

## Nguồn và PDF đã kiểm tra lại

- Giữ nguyên bốn PDF gốc M05, M06, M09 và M10 cùng DOI metadata.
- M05: PDF pp.10–12, Fig. 5(g), Section 3.3.1 và Table 4.
- M06: PDF p.3, định nghĩa layer jamming và Fig. 2.
- M09: PDF pp.4–5, Section 2.2 và Fig. 2.
- M10: PDF p.2, Design/Fig. 1.
- Không tìm kiếm tài liệu mới và không sửa source registry, PDF, evidence record hoặc verification round.

## Các sửa đổi đã thực hiện

1. Chuyển Bảng 2.3.1 từ danh sách đồng cấp sang phân loại hai tầng.
2. Ghi rõ frictional locking là cơ chế ràng buộc có thể xuất hiện trong nhiều kiến trúc.
3. Bổ sung thay đổi ràng buộc/cấu hình cơ khí và các ví dụ có nguồn.
4. Giữ nguyên so sánh cơ học và các giới hạn về áp suất, lực pháp tuyến, giao diện và topology MP1.
5. Chuẩn hóa 14 thuật ngữ trong DOCX và CSV; giải quyết T11 có điều kiện.
6. Sửa bố cục bảng: hàng không tách, tiêu đề lặp, cột cố định, trạng thái gọn hơn.
7. Xóa thông báo template và citation numbering khỏi thân luận văn.
8. Cập nhật traceability từ 9 lên 10 claim, thêm C10 cho tổng hợp hai tầng.

## Kết quả nội dung

- **Papers read/verified:** 4.
- **Evidence IDs:** M05-E01, M05-E02, M06-E01, M09-E01, M10-E01.
- **Technical claims in traceability:** 10; 7 `VERIFIED_FULL_TEXT`, 3 `INFERENCE`.
- **Citations:** 4, đánh số tạm thời [1]–[4].
- **Bảng:** 1 bảng phân loại hai tầng; 1 bảng thuật ngữ 14 dòng.
- **Hình:** 0.
- **Phương trình:** 0.
- **TERMINOLOGY_REVIEW_REQUIRED:** 0; T11 chuyển thành `VERIFIED_FROM_SOURCE_CONTEXT` có điều kiện.

## Orchestration and QA

- `ROOT_MODEL_REQUESTED: GPT-6.1 SOL HIGH`
- `ROOT_MODEL_ACTUAL: NOT_VERIFIED`
- `WORKERS_SPAWNED: 0 in R1; bounded remediation executed from existing evidence`
- `PARALLEL_EXECUTION: NO`
- `SOURCE_VERIFICATION_COMPLETED: YES, independently rechecked from local PDFs`
- `SCIENTIFIC_SYNTHESIS_APPROVED: YES`
- `DOCX_GENERATION: UPDATED`
- `WORD_RENDER_VALIDATION: NOT_VERIFIED (no DOCX renderer available)`
- `SEVEN_GATE_RESULT: PASS_ALL_7_GATES`
- `FINAL_STATUS: PARTIAL_WITH_FINDINGS`

## Kiểm tra file

- Năm file bắt buộc đều tồn tại và không rỗng.
- DOCX mở được, ZIP integrity đạt, A4, hai bảng Word thật.
- Mọi hàng bảng được đánh dấu không tách; hàng đầu được đánh dấu lặp tiêu đề.
- Citation [1]–[4] và DOI vẫn khớp danh mục tài liệu tham khảo.

## Giới hạn còn lại

Không thể render và kiểm tra trực quan từng trang vì môi trường không có LibreOffice/soffice hoặc công cụ tương đương. Cần thực hiện bước render bên ngoài trước khi dùng bản thảo trong luận văn chính thức.
