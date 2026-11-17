# Checkpoint — MP1-R: tô sáng bằng chứng trích dẫn Chương 2 trên PDF

**Trạng thái hiện tại: COMPLETED.** Đã tiếp tục theo yêu cầu “tiep tuc cong viec tu checkpoint”. Xem phần bàn giao cuối file. Nội dung checkpoint bên dưới ghi lại trạng thái lịch sử khi người dùng yêu cầu: “ngừng lại, tạo checkpoint” (`PAUSED_BY_USER`).

Thời điểm lưu: 2026-10-03 14:44, Asia/Bangkok (07:44 UTC).

## Nhiệm vụ đang thực hiện

Tô sáng trên 18 PDF do người dùng chỉ định những đoạn hỗ trợ các ý được trích dẫn trong:

`docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx`

Tạo bản PDF mới có annotation highlight và ghi chú tiếng Việt. Giữ nguyên PDF gốc, DOCX và các hồ sơ khoa học Phase 3–6. Đây là nhiệm vụ định vị/tô sáng bằng chứng, **không phải thực hiện Phase 7**, không tìm tài liệu mới hoặc xét lại khoa học.

## Công việc đã lưu

Thư mục kết quả:

`outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/`

Đã tạo:

- `pdf/`: **18 bản PDF đã tô**, với **90 vùng highlight** gốc có thể chỉnh sửa. Ghi chú mỗi vùng có ý tiếng Việt, số IEEE, mục chương, mã tra cứu và giới hạn suy luận.
- `README.md`: bảng liên kết đủ 18 PDF, trang được tô, bảng 90 vùng tô, cách đọc màu và giới hạn đối chiếu.
- `HIGHLIGHT_REGISTER.json`: từng vùng tô, trích đoạn, trang PDF, hình học dòng, mã ý và hash đầu vào/đầu ra.
- `CLAIM_SOURCE_MAP.json`: **53 mục ý có nguồn**, **145 cặp ý–nguồn**; phân biệt đoạn hỗ trợ, phần tổng hợp/suy luận và bối cảnh cấp bảng.
- `VALIDATION.json`: kết quả kiểm tra kỹ thuật và bảo toàn đầu vào.
- `inputs.json`: đường dẫn, số IEEE, mã nguồn và SHA-256 của đủ 18 PDF gốc; đây là manifest nguồn của nhiệm vụ này.
- `curated_passages.json`: 90 vùng chọn có trang, block, chỉ số dòng và chú thích.
- `pdf_text_geometry.json`, các file `*_search_text.txt`: văn bản và tọa độ được trích từ PDF gốc để định vị.
- `previews/`: bốn ảnh kiểm tra vị trí tô.
- `prepare_inputs.py`, `curate_annotations.py`, `build_highlighted_pdfs.py`: script tái tạo dữ liệu và đầu ra.

**Chưa tạo ZIP. Chưa gửi phản hồi hoàn tất cho nhiệm vụ highlight.**

## Đối chiếu nguồn IEEE

| IEEE | Mã nguồn | Vùng tô đã lưu |
|---|---|---:|
| [1] | S01 | 6 |
| [2] | S02 | 5 |
| [3] | S03 | 10 |
| [4] | S15 | 2 |
| [5] | S18 | 8 |
| [6] | S06 | 6 |
| [7] | V-W02 | 4 |
| [8] | S13 | 4 |
| [9] | S17 | 1 |
| [10] | S04 | 8 |
| [11] | S22 | 6 |
| [12] | S05a | 5 |
| [13] | S05b | 5 |
| [14] | S09 | 4 |
| [15] | S07 | 4 |
| [16] | S11 | 3 |
| [17] | S12 | 4 |
| [18] | S10 | 5 |

PDF đầu ra đặt tên `NN_SOURCE_HIGHLIGHTED.pdf` trong thư mục `pdf/`. S05 được tách thành S05a và S05b theo hai công trình thực tế trong thư mục tài liệu tham khảo. V-W02 là bài đã xuất bản, dùng năm online 2021; tên PDF có 2022 không thay đổi danh tính bài.

## Kiểm tra đã hoàn tất

- Mở lại thành công đủ 18 PDF đầu ra bằng PyMuPDF.
- Số trang và văn bản trích xuất không đổi so với bản gốc.
- Đủ 90 annotation mới, có ghi chú tiếng Việt; giữ annotation có sẵn của bản gốc.
- Hash của 18 PDF gốc không đổi.
- Hash DOCX hiện tại vẫn là:

  `3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45`

- Hash file traceability Phase 6 không đổi trong quá trình tạo đầu ra.
- Đã render và xem trực quan bốn trang: S03 trang PDF 9; S07 trang PDF 6; S22 trang PDF 71; S04 trang PDF 5. Highlight khớp các dòng được chọn và văn bản vẫn đọc được.
- Chưa xem trực quan mọi trang được tô; không ghi nhận việc đó là đã hoàn tất.
- Không tìm kiếm tài liệu, không thêm nguồn, không thay đổi nội dung khoa học.

Màu: **vàng** = kết quả/mô tả nguồn; **xanh** = phương pháp/mô hình; **cam** = giả thiết/phạm vi/giới hạn.

Các trang trong register là **thứ tự trang PDF, tính từ 1**, không mặc định là số trang in. Ví dụ S22 trang PDF 71 là trang in 63.

## Giới hạn cần giữ khi tiếp tục

145 cặp ý–nguồn được phân loại:

- 59: tìm được đoạn cho thành phần phát biểu có trích dẫn (`SOURCE_PASSAGES_LOCATED_FOR_CITED_COMPONENT`).
- 62: bằng chứng nền cộng suy luận về MP1-R (`SOURCE_COMPONENT_PLUS_PROJECT_INFERENCE`).
- 8: định nghĩa/phân tích thước đo của chương, có nguồn làm bối cảnh.
- 5: hỗ trợ một phần đại lượng của hàng bảng.
- **11: chỉ là bối cảnh nhóm nguồn của bảng, không trực tiếp chứng minh hàng tương ứng** (`TABLE_LEVEL_CONTEXT_ONLY_NOT_ROW_EVIDENCE`).

Không diễn đạt rằng toàn bộ các mệnh đề đã được kiểm toán hoặc mọi câu có đối ứng nguyên văn trong nguồn. Không tô đoạn chỉ có từ khóa gần giống để tạo độ phủ giả. Các kết luận về phần chưa xác định của MP1-R hoặc yêu cầu nhận dạng không phải kết quả nguyên văn của bài gốc.

Giữ các giới hạn: S18 là PVC layer-jamming hút chân không; S15 chỉ là tổng quan; S17 hỗ trợ thận trọng về đại lượng/đơn vị; S07 bỏ qua ma sát giữa tao trong mô hình; S22 suy N từ lực cản, hệ số ma sát tham khảo và diện tích xấp xỉ; S12 có thí nghiệm thép và mô phỏng SMA. Không dùng S20/S19/S21.

## Phần còn lại khi người dùng yêu cầu tiếp tục

1. Đọc checkpoint này, `README.md`, `VALIDATION.json` và register; kiểm tra file/hashes hiện tại trước khi ghi lại đầu ra. Không bắt đầu lại việc trích toàn bộ nguồn.
2. Có hai vùng bổ sung đang được cân nhắc, **chưa áp dụng**:
   - **S01, trang PDF 9, block 3**: kết quả xoắn hỗ trợ rõ hơn CH2C005 và CH2C010. Đã đọc đủ block; có thể chọn dòng 0–18 (chỉ số dòng bắt đầu từ 0, cuối exclusive là 19) cho phương pháp/kết quả xoắn. Hiện S01 đã có highlight phương pháp thử xoắn, nhưng chưa tô đoạn kết quả xoắn này.
   - **S09, trang PDF 9, block 9**: so sánh kết quả bơm thực nghiệm với mô phỏng. Hiện đã tô kiến trúc, mô hình và prototype; có thể bổ sung kết quả để làm rõ tiền lệ SMA–chất lưu cho CH2C046/CH2C055. Không cần đưa số mới vào DOCX.
3. Nếu bổ sung: chỉnh `curate_annotations.py`, chạy lại script curation rồi build; các script chỉ ghi lại PDF bản sao và register trong thư mục annotation. Điều chỉnh tổng số vùng tô trong hồ sơ và mô tả cuối theo kết quả thực tế.
4. Kiểm tra trực quan phần bổ sung nếu có; ghi kết quả đúng mức đã kiểm tra. Không thực hiện kiểm toán Phase 7.
5. Tạo ZIP chứa 18 PDF đã tô, README và các register để người dùng tải/mở thuận tiện; kiểm tra ZIP đọc được và đủ file. ZIP chưa tồn tại tại checkpoint này.
6. Mở lại các file hồ sơ cần bàn giao, xác nhận đầu vào vẫn nguyên vẹn, rồi trả lời ngắn bằng tiếng Việt, liên kết tới ZIP và README. Nêu các ý tổng hợp/bối cảnh được ghi riêng; không tuyên bố mọi trích dẫn đều là bằng chứng trực tiếp.

Lệnh tái tạo, chỉ chạy nếu thật sự thay đổi vùng chọn:

```bash
python outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py
python outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py
```

PyMuPDF đã có trong môi trường (`import pymupdf`); script tạo PDF đã chạy thành công. Không cần cài lại nếu import vẫn hoạt động.

## Những file không được đụng tới

Giữ nguyên DOCX Chương 2, PDF gốc và các artifact Phase 3–6. Có file khóa Word `docs/project/~$1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx` và thư mục `outputs/reports/MP1_R_PHASE_7_2026-10-03/` trong trạng thái git hiện tại; không xóa hoặc sửa chúng để phục vụ nhiệm vụ highlight. Không thay đổi registry nghiên cứu, không commit nếu chưa được yêu cầu.

**Phần trên là checkpoint lịch sử; các việc còn lại đã hoàn tất trong lần tiếp tục.**

## Bàn giao sau khi tiếp tục

Trạng thái cuối: **COMPLETED**.

- Đã bổ sung S01-H07 (kết quả xoắn, trang PDF 9) và S09-H05 (bơm SMA thực nghiệm, trang PDF 9).
- Kết quả cuối: **18 PDF, 92 vùng highlight**; 53 mục ý có nguồn và 145 cặp ý–nguồn vẫn được phân biệt theo ranh giới đối chiếu.
- Đã kiểm tra trực quan hai trang bổ sung, nâng số trang được xem trực quan lên sáu. Không tuyên bố mọi trang đã được xem thủ công.
- Đã tạo ZIP, kiểm tra CRC và đối chiếu hash mọi thành viên với file đã lưu: **PASS**, đủ 18 PDF và bảy file hồ sơ.
- PDF gốc, DOCX và file traceability không đổi; không thực hiện Phase 7.

Gói bàn giao:

`outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip`

Báo cáo cuối:

`outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md`

Kiểm tra ZIP:

`outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json`
