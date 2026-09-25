# Worker W2-04-01: 16-Paper Registry and Deterministic Batch Mapping Report

> **Worker:** W2-04-01  
> **Nhiệm vụ:** Thiết lập danh mục xác định 16 bài báo, ánh xạ tệp PDF và JSON bằng chứng, đối soát commit và phân bổ lô xử lý (batch assignment)  
> **Trạng thái:** `COMPLETE`  

## 1. Kết quả Xác thực Danh mục Canonical
- **Tệp nguồn Canonical:** `outputs/verification/MP1-V002/verification_matrix.json` (commit `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d`).
- **Tổng số bài báo:** Đúng 16 bài báo được bao gồm (`paper_count = 16`).
- **Tính duy nhất:** 16 mã `paper_id` hoàn toàn phân biệt, 0 trùng lặp.
- **Trạng thái tệp PDF trên đĩa:** 16/16 tệp PDF tồn tại đầy đủ tại `data/papers/verification/MP1-V002/`.
- **Trạng thái tệp Evidence JSON:** 16/16 tệp JSON tồn tại đầy đủ tại `data/evidence/`.
- **Đường dẫn khuyết thiếu / mơ hồ:** `0` (Không có lỗ hổng đường dẫn).

## 2. Bảng Phân bổ Lô Xử lý Xác định (Deterministic Batches)

| Worker ID | Chỉ số Bài báo (Indices) | Paper IDs | Tiêu đề Rút gọn |
|---|---|---|---|
| **W2-04-02** | `01`, `02` | `00414aac4b`, `fac21c950e` | Reedlunn 2013 Part I & Part II (SMA Cables Isothermal Tension) |
| **W2-04-03** | `03`, `04` | `40760daa02`, `2f7fcf2f8f` | Carboni 2016 (Pinched Hysteresis Absorber) & Fang 2019 (SMA Cable Macromodel) |
| **W2-04-04** | `05`, `06` | `7f3f45407f`, `1c81b2d35c` | Salvatore 2021 (Wire Rope Isolator) & Narjabadifam 2024 (Steel/NiTi Wire Ropes) |
| **W2-04-05** | `07`, `08` | `9f4295be23`, `56793dea9b` | Barsi 2025 (Short Wire Ropes Bending) & Kang 2020 (SMA Cables FEM) |
| **W2-04-06** | `09`, `10` | `d9966f2f5e`, `9e15094d68` | Carboni 2015/2014 (Nitinol & Steel Strands Hysteresis) & Liu 2023 (Simplified FE Cable) |
| **W2-04-07** | `11`, `12` | `53200aa0c6`, `98fee47c04` | Vahidi 2022 (Single/Double Helix SMA Ropes) & Niu 2021 (Nitinol Rope Vibration) |
| **W2-04-08** | `13`, `14` | `aaad9c248c`, `ccdc1bb980` | Liu 2004 (Cable Internal Friction) & Tjahjanto 2017 (Submarine Cable Bending Mechanics) |
| **W2-04-09** | `15`, `16` | `e8462758c3`, `6dd1ca94d1` | Liu 2026 (Braided NiTi Microfilaments) & Silva 2022 (NiTi Micro Cables Dynamic Fatigue) |

## 3. Khóa Phạm vi
Worker W2-04-01 không đưa ra bất kỳ kết luận khoa học mới hay đánh giá tính mới nào.
