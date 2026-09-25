# Báo cáo Thực thi Worker W2-05-04: Tái cấu trúc Nhánh Trích dẫn Ngược B09 và B11

- **Worker ID:** `W2-05-04`
- **Nhiệm vụ:** Tái cấu trúc B09 (Carboni 2016) và B11 (Kang et al. 2020), xác minh 22 tài liệu trích dẫn ngược của B11.
- **Trạng thái:** `COMPLETE`

---

## 1. Chi tiết Từng Nhánh

### Nhánh B09 — Carboni & Lacarbonara (2016)
- **Anchor:** `doi:10.1061/(asce)em.1943-7889.0001072` (`40760daa02`)
- **Tệp nguồn:** `data/search_exports/MP1-V002/raw/backward/B09.csv`
- **Số bản ghi:** 34 bản ghi thô.
- **Trạng thái:** `SCREENED_CANDIDATES_FOUND`. Kết nối tới Carboni 2015 (`d9966f2f5e`) và Carboni 2016 trên Nonlinear Dynamics (`7f3f45407f`). Cơ cấu tiêu hao dao động uốn thắt nút (pinched hysteresis) dựa trên tiếp xúc cơ học thuần túy.

### Nhánh B11 — Kang et al. (2020)
- **Anchor:** `doi:10.3901/jme.2020.14.065` (`56793dea9b`)
- **Tiêu đề:** *Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables*
- **Tệp nguồn:** `data/search_exports/MP1-V002/raw/backward/B11_kang2020.csv`
- **Số bản ghi:** 22 bản ghi thô trích dẫn ngược.
- **Trạng thái sàng lọc:** Toàn bộ 22 bản ghi được kiểm tra cẩn trọng:
  - 1 bản ghi trùng lặp với phả hệ Carboni 2015 (`d9966f2f5e`).
  - Các bản ghi khác bao gồm mô phỏng phần tử hữu hạn dầm/tiếp xúc cổ điển, nghiên cứu kéo xoắn cáp SMA.
  - **Kết luận:** Không có bất kỳ tài liệu nào đề cập tới cơ chế uốn bó sợi kim loại/NiTi dưới áp suất giam giữ chủ động.
