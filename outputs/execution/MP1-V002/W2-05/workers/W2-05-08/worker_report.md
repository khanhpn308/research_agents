# Báo cáo Thực thi Worker W2-05-08: Tái cấu trúc Các Nhánh Phụ Lịch sử F07–F13

- **Worker ID:** `W2-05-08`
- **Nhiệm vụ:** Tái cấu trúc các nhánh trích dẫn xuôi phụ lịch sử hình thành trong đợt khảo sát 13 bài báo (13-paper chase).
- **Trạng thái:** `COMPLETE`

---

## 1. Nguồn gốc và Lý do Tồn tại của F07–F13

Trong giai đoạn Stage 3 (Phase 24), khi mở rộng tập bài báo toàn văn từ 10 lên 13 bài, hệ thống đã thực hiện xuất trích dẫn xuôi tự động cho các bài báo mới nạp:
- **F07:** Xuất xuôi từ Carboni et al. (2015) — 98 bản ghi.
- **F08:** Xuất xuôi từ Carboni & Lacarbonara (2016) — 58 bản ghi.
- **F09:** Xuất xuôi từ Reedlunn et al. Part I (2013) — 92 bản ghi.
- **F10:** Xuất xuôi từ Reedlunn et al. Part II (2013) — 37 bản ghi.
- **F11:** Xuất xuôi từ Vahidi et al. (2021) — 15 bản ghi.
- **F12:** Xuất xuôi từ Silva et al. (2022) — 10 bản ghi.
- **F13:** Xuất xuôi từ Liu et al. (2026) — 0 bản ghi (`F13.txt`).

Cùng với B09 và B10, 8 tệp CSV này đã được đưa vào đợt sàng lọc `outputs/verification/MP1-V002/citation_screening_13paper_chase/METADATA_SCREENING.json` (372 bản ghi thô, 287 ứng viên duy nhất).

---

## 2. Ranh giới Giao thức và Phân định Mẫu số

- Các nhánh F07–F13 đã chứng minh rằng các công trình trích dẫn tiếp theo của nhóm tác giả Carboni, Reedlunn, Vahidi, Silva không phát triển cơ chế buồng áp suất chủ động uốn bó dây NiTi.
- Tuy nhiên, giao thức chuẩn MP1-V002 định nghĩa 6 nhánh xuôi cốt lõi (F01–F06) dựa trên các bài báo anchor phương án (Bai, Liu, Zhang, Takashima, Matsumoto, Wang).
- **Quy tắc phân định:** Các nhánh F07–F13 được bảo tồn làm tài liệu lịch sử chứng minh độ cẩn trọng của quá trình rà soát, nhưng **TUYỆT ĐỐI KHÔNG** được tự ý gộp vào làm phình mẫu số trích dẫn xuôi chuẩn (mẫu số chuẩn vẫn giữ nguyên 6/6).
