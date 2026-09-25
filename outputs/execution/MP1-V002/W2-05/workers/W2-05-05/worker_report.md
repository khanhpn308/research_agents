# Báo cáo Thực thi Worker W2-05-05: Tái cấu trúc Nhánh B12 và Hòa giải B10 Lịch sử

- **Worker ID:** `W2-05-05`
- **Nhiệm vụ:** Tái cấu trúc nhánh B12 (Barsi et al.), hòa giải nhánh lịch sử B10 và làm rõ phát biểu "68 bản ghi thô / 67 bản ghi duy nhất" giữa B11 và B12.
- **Trạng thái:** `COMPLETE`

---

## 1. Chi tiết Nhánh B12 — Barsi, Carboni & Lacarbonara (2024/2025)
- **Anchor:** `doi:10.1016/j.engstruct.2024.119217` (`9f4295be23`)
- **Tệp nguồn:** `data/search_exports/MP1-V002/raw/backward/B12_barsi.csv`
- **Số bản ghi thô:** 46 bản ghi.
- **Trạng thái:** `SCREENED_CANDIDATES_FOUND`. Tái hiện phả hệ cáp ngắn chịu uốn của Carboni và Reedlunn. Giải quyết áp lực pháp tuyến và trượt cục bộ từ biến dạng uốn, không có áp suất chất lưu chủ động. Là nhánh ngược chuẩn thứ 9/9.

---

## 2. Hòa giải Phát biểu Lịch sử B11 + B12 (68 thô / 67 duy nhất)
Trong tài liệu bàn giao `docs/project/MP1-V002_CURRENT_HANDOFF.md` và nhật ký Stage 4 có ghi nhận:
- B11 = 22 bản ghi
- B12 = 46 bản ghi
- Tổng số bản ghi thô = $22 + 46 = 68$ bản ghi.
- Kiểm tra trùng lặp phát hiện chính xác **1 bài trùng**:
  - `DOI: 10.1061/(ASCE)EM.1943-7889.0000852` (Carboni et al. 2015).
- Do đó số bản ghi duy nhất là $68 - 1 = 67$ bản ghi.
Phát biểu này phản ánh đúng phạm vi sàng lọc bổ sung đợt cuối của Stage 4 nhằm đóng điều kiện dừng.

---

## 3. Trạng thái Nhánh B10 Lịch sử
- **Tệp nguồn:** `data/search_exports/MP1-V002/raw/backward/B10.csv` (28 bản ghi).
- **Bản chất:** Là nhánh xuất ngược trung gian trong đợt khảo sát 13 bài báo nhằm dò tìm nguồn gốc sâu của tinh thể học TiNi và dầm SMA.
- **Quy tắc chuẩn hóa:** `citation_coverage.json` không đặt B10 là nhánh bắt buộc. Nhánh này được bảo tồn nguyên vẹn làm bằng chứng nguồn gốc lịch sử, không gộp vào mẫu số 9 nhánh ngược chuẩn.
