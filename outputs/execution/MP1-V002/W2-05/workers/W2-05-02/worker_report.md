# Báo cáo Thực thi Worker W2-05-02: Tái cấu trúc Nhánh Trích dẫn Ngược B01–B03

- **Worker ID:** `W2-05-02`
- **Nhiệm vụ:** Tái cấu trúc nguồn gốc tìm kiếm, tệp xuất thô và trạng thái sàng lọc của 3 nhánh ngược: B01, B02, B03.
- **Trạng thái:** `COMPLETE`

---

## 1. Chi tiết Từng Nhánh

### Nhánh B01 — Carboni, Lacarbonara & Auricchio (2015)
- **Anchor:** `doi:10.1061/(asce)em.1943-7889.0000852` (`d9966f2f5e`)
- **Tệp nguồn:** `data/search_exports/MP1-V002/raw/backward/B01.csv`
- **Số bản ghi thô / duy nhất:** 57 / 57
- **Kết quả sàng lọc:** Phát hiện trích dẫn quan trọng tới Reedlunn et al. Part II (2013, `fac21c950e`). Toàn bộ 56 bản ghi còn lại là cơ học cáp cổ điển, dao động kết cấu, hoặc vật liệu khối SMA. Không có bài báo nào sử dụng áp suất khí nén chủ động.

### Nhánh B02 — Vahidi et al. (2021)
- **Anchor:** `doi:10.1080/15376494.2021.1955313` (`53200aa0c6`)
- **Tệp nguồn:** `data/search_exports/MP1-V002/raw/backward/B02.csv`
- **Số bản ghi thô / duy nhất:** 33 / 33
- **Kết quả sàng lọc:** Tái xác nhận phả hệ Reedlunn et al. (2013). Các bài báo tập trung vào dây cáp xoắn kép SMA dưới tải kéo dọc trục, ma sát tiếp xúc nội tại phát sinh thuần túy do hình học xoắn.

### Nhánh B03 — Xin Liu (2004)
- **Anchor:** `paper:aaad9c248c` (Luận án tiến sĩ, DOI không cung cấp)
- **Tệp nguồn:** `data/search_exports/MP1-V002/raw/backward/B03.csv`
- **Số bản ghi thô / duy nhất:** 4 / 4
- **Kết quả sàng lọc:** Không có mối đe dọa cao nào (`screened_no_high_threat`). Tài liệu thiết lập tiêu chuẩn trượt ma sát tiếp xúc trong cáp dao động uốn dưới tải trọng tĩnh/động mà không có áp suất chủ động.
