# Nhật ký tích hợp mục 2.3

## Phạm vi và nguyên tắc

Tích hợp năm baseline đã được chấp nhận thành một DOCX mới. Các thư mục nguồn chỉ được đọc; không có baseline, PDF, registry hoặc mục khác của Chương 2 bị sửa. Nội dung khoa học của các đoạn được giữ nguyên, còn danh mục tham khảo và phụ lục thuật ngữ lặp được hợp nhất.

## Baseline và bất biến nguồn

- §2.3.1: `MP1_CH2_2_3_1_DRAFT.docx` — SHA-256 `6ded97f12de61cde7be319c865c3ea40cc6cbdc8d04e00cc648530ec718311a0`
- §2.3.2: `MP1_CH2_2_3_2_DRAFT.docx` — SHA-256 `7f614d06edca11ae573f27aeb5d277e5e7d74f3dc1d6ec9978dbe43f1795c8fb`
- §2.3.3: `MP1_CH2_2_3_3_DRAFT.docx` — SHA-256 `1727dd0eeb32da84135d094f34c443605060cfd3fa39d269d85f855ce731b563`
- §2.3.4: `MP1_CH2_2_3_4_DRAFT.docx` — SHA-256 `38be496eb71922f7165b916ac552f9b9bcb54dbfd94dc0f635acd55372ce793d`
- §2.3.5: `MP1_CH2_2_3_5_DRAFT.docx` — SHA-256 `a7a46894a3384cc519cdea0ab6b957cbb5e8fb130dd9b2073678a6d5513546e4`

Tất cả hash trên được ghi trước tích hợp và kiểm tra lại sau khi dựng đầu ra.

## Thay đổi biên tập có giới hạn

- Giữ thứ tự §2.3.1 → §2.3.5 và giữ năm bảng so sánh gốc.
- Loại 24 mục tài liệu tham khảo cục bộ, hợp nhất thành 11 nguồn DOI duy nhất; loại 13 bản ghi trùng. Vai trò nguồn vẫn được giữ theo từng claim và từng architecture.
- Chuyển toàn bộ citation trong đoạn và bảng sang số chung của mục 2.3. Dải citation không liên tục được tách thành các số riêng để tránh tạo dải sai.
- Giữ nguyên ba phương trình OMML của Zhang và Yao trong §2.3.4: τ_max(Q) = μp, Q_J = kμp và Q_S = Aμp. Không đổi số phương trình hoặc ý nghĩa biến.
- Không xóa các đoạn lặp về cơ chế giam giữ, ma sát, áp suất nguồn và giới hạn chuyển giao khi chúng còn làm rõ điều kiện áp dụng. Các lặp lại được phân loại là NECESSARY_REINFORCEMENT; các danh mục tham khảo/phụ lục lặp là DUPLICATED_SOURCE_SUMMARY và được gom lại.
- Hợp nhất 73 bản ghi thuật ngữ thành 58 khái niệm. Giữ riêng các cặp có nghĩa cơ học khác nhau, gồm stiffness/rigidity, calibration/validation và các biến thể wire/fibre. Ghi nhận xung đột “Hình thái tiếp xúc/Hình thái kết nối tiếp xúc” và “Chênh áp/Chênh lệch áp suất” trong CSV.
- Loại Paper ID/Evidence ID khỏi DOCX; các citation nguồn trong bảng thuật ngữ dùng số tham khảo chung.

## Các giới hạn còn lại

- Số tham khảo chỉ có hiệu lực trong mục 2.3 và phải đánh số lại khi ghép toàn bộ Chương 2.
- Không có trình kết xuất Word/LibreOffice trong môi trường này, nên kiểm tra bố cục trực quan chưa được xác minh. ZIP/XML, bảng, citation và OMML đã được kiểm tra tĩnh.
- Ba trường `scientific_assumptions` trong register được để trống khi baseline không cung cấp trường này; không suy diễn thêm giả định.

## Hotfix MP1-CH2-2.3-INTEGRATION-FINAL-HOTFIX

- Đã sửa mười trường `contextual_usage` của T033, T035, T037, T038, T039, T042, T044, T045, T046 và T047 theo mapping §2.3.4: [2]→[6] (M07), [4]→[7] (M13). Không thay đổi `canonical_citation_numbers` hay danh mục tài liệu.
- Đã sắp xếp các nhóm citation nhiều nguồn theo số tham khảo tích hợp tăng dần trong thân văn bản, bảng và glossary. Không đổi định danh nguồn, bibliography hoặc số phương trình.
- Đã bỏ cột trạng thái máy khỏi glossary Word. Glossary còn năm cột, giữ đủ 58 thuật ngữ; metadata xác minh vẫn nằm trong `MASTER_TERMINOLOGY.csv`.
- Đã chuyển ghi chú về đánh số tạm thời của §2.3 khỏi DOCX; ghi chú vẫn được lưu trong báo cáo tích hợp.
- Đã thay các Paper ID còn sót trong `contextual_usage` của glossary Word bằng citation tích hợp; các Paper ID vẫn được giữ trong cột metadata `source_paper_ids` của CSV.
