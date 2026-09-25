# Báo cáo Thực thi Worker W2-05-09: Hòa giải Bản ghi Thô / Bản ghi Duy nhất / Khử trùng lặp

- **Worker ID:** `W2-05-09`
- **Nhiệm vụ:** Hòa giải toán học và nguồn gốc dữ liệu giữa số lượng bản ghi thô, bản ghi duy nhất, các đợt sàng lọc siêu dữ liệu và phát biểu lịch sử "68 thô / 67 duy nhất".
- **Trạng thái:** `COMPLETE`

---

## 1. Bảng Tổng hợp Hòa giải Phạm vi Bản ghi

| Phạm vi Đối soát | Bản ghi thô | Bản ghi trùng lặp | Bản ghi duy nhất | Ghi chú & Ranh giới áp dụng |
|---|---|---|---|---|
| **B11 + B12 (Stage 4 closure)** | **68** | **1** | **67** | Khớp chính xác phát biểu lịch sử trong Handoff Stage 4 (22 + 46). Trùng duy nhất bài Carboni 2015. |
| **Sàng lọc Siêu dữ liệu đợt 1 (2026-09-24)** | **187** | **9** | **178** | 8 CSV: B01–B05, F01, F02, F04. Báo cáo trong `citation_screening/METADATA_SCREENING.json`. |
| **Sàng lọc đợt 2 (13-paper chase, 2026-09-25)** | **372** | **85** | **287** | 8 CSV: B09, B10, F07–F12. Báo cáo trong `citation_screening_13paper_chase/METADATA_SCREENING.json`. |
| **Toàn bộ 15 Nhánh Chuẩn (Canonical 15)** | **312** | **54** | **258** | 9 nhánh ngược (237 thô) + 6 nhánh xuôi (75 thô). Phủ trích dẫn chuẩn hóa chính thức của MP1-V002. |

---

## 2. Chi tiết Trùng lặp giữa B11 và B12
- Bản ghi B11: `row_1` của `B11_kang2020.csv` trích dẫn Carboni et al. (2015), DOI `10.1061/(ASCE)EM.1943-7889.0000852`.
- Bản ghi B12: `row_2` của `B12_barsi.csv` cũng trích dẫn cùng bài báo Carboni et al. (2015).
- Đây là bài báo trùng lặp duy nhất giữa 2 nhánh, xác nhận tính toán $22 + 46 = 68$ thô và $68 - 1 = 67$ duy nhất là tuyệt đối chính xác về mặt số học.

---

## 3. Không có sự ghi đè tệp chuẩn
Tất cả các con số trên phản ánh các góc nhìn và giai đoạn kiểm toán khác nhau. Worker W2-05-09 ghi nhận đầy đủ bản chất của từng phạm vi và **KHÔNG** sửa đổi giá trị trong `citation_coverage.json`.
