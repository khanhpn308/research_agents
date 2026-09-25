# Báo cáo Thực thi Worker W2-05-01: Thiết lập Registry Giao thức & Phủ Trích dẫn Chuẩn

- **Worker ID:** `W2-05-01`
- **Nhiệm vụ:** Thiết lập registry phủ trích dẫn chuẩn hóa (canonical coverage registry) và phân định ranh giới nhánh lịch sử theo giao thức MP1-V002.
- **Trạng thái:** `COMPLETE`
- **Mẫu số chuẩn định nghĩa (Canonical Denominator):** **15/15** hướng (9 nhánh ngược, 6 nhánh xuôi).
- **Ngày chốt tìm kiếm (Search Cutoff Date):** `2026-09-25`
- **Điều kiện dừng (Stop Condition):** `satisfied = true` trích xuất trực tiếp từ `outputs/verification/MP1-V002/citation_coverage.json`.

---

## 1. Bản đồ Phủ Trích dẫn Chuẩn hóa (15 Nhánh Chuẩn)

| Nhánh ID | Hướng | Yêu cầu | Anchor Tiêu đề | Database | Bản ghi thô | Trạng thái chuẩn |
|---|---|---|---|---|---|---|
| **B01** | BACKWARD | Bắt buộc | Carboni et al. (2015) — Hysteresis of Nitinol & Steel Strands | Scopus | 57 | `screened_candidates_found` |
| **B02** | BACKWARD | Bắt buộc | Vahidi et al. (2021) — Single & double-helix SMA wire ropes | Scopus | 33 | `screened_candidates_found` |
| **B03** | BACKWARD | Bắt buộc | Xin Liu (2004) — Cable Vibration Internal Friction | Scopus | 4 | `screened_no_high_threat` |
| **B04** | BACKWARD | Bắt buộc | Tjahjanto et al. (2016) — Bending Mechanics of Cable Cores | Scopus | 9 | `screened_no_high_threat` |
| **B05** | BACKWARD | Bắt buộc | Liu et al. (2026) — Braided NiTi microfilaments | Scopus | 10 | `screened_no_high_threat` |
| **B06** | BACKWARD | Bắt buộc | Silva et al. (2022) — NiTi SMA Superelastic Micro Cables | PubRef | 22 | `screened_candidates_found` |
| **B09** | BACKWARD | Bắt buộc | Carboni & Lacarbonara (2016) — Pinched Hysteresis Absorber | Scopus | 34 | `screened_candidates_found` |
| **B11** | BACKWARD | Bắt buộc | Kang et al. (2020) — FEM of SMA Superelastic Cables | Scopus | 22 | `screened_candidates_found` |
| **B12** | BACKWARD | Bắt buộc | Barsi et al. (2025) — Short Wire Ropes Mechanics | Scopus | 46 | `screened_candidates_found` |
| **F01** | FORWARD | Bắt buộc | Bai et al. (2022) — Wire Jamming Tunable Stiffness | Scopus | 14 | `screened_candidates_found` |
| **F02** | FORWARD | Bắt buộc | Liu et al. (2021) — Positive Pressure Jamming Wearable Robots | Scopus | 51 | `screened_candidates_found` |
| **F03** | FORWARD | Bắt buộc | Zhang & Yao (2026) — Positive-Pressure Fiber Jamming | Scopus | 0 | `screened_no_high_threat` |
| **F04** | FORWARD | Bắt buộc | Takashima et al. (2022) — SMA & Jamming Transition Link | Scopus | 9 | `screened_no_high_threat` |
| **F05** | FORWARD | Bắt buộc | Matsumoto et al. (2024) — R-phase SMA Wire Jamming | ResearchGate | 1 | `screened_no_high_threat` |
| **F06** | FORWARD | Bắt buộc | Wang et al. (2024) — Piston-like Particle Jamming | Scopus | 0 | `screened_no_high_threat` |

---

## 2. Nhánh Phụ Lịch sử (Historical Auxiliary Branches)

Giao thức bảo lưu 8 nhánh phụ lịch sử phát sinh từ đợt mở rộng 13 bài báo (13-paper chase) nhưng **KHÔNG** làm tăng mẫu số chuẩn 15/15:
- **B10:** 28 bản ghi xuất từ Scopus khám phá phả hệ cáp SMA lịch sử.
- **F07–F13:** 7 nhánh xuôi trung gian khảo sát các bài báo toàn văn mới (Carboni 2015, Carboni 2016, Reedlunn Part I, Reedlunn Part II, Vahidi 2021, Silva 2022, Liu 2026).

---

## 3. Quy tắc Diễn giải Nghiêm ngặt (Interpretation Guardrail)

1. Mẫu số chuẩn xác lập tuyệt đối là 15/15 (9 ngược, 6 xuôi).
2. Việc đạt độ phủ 15/15 chỉ xác nhận giao thức truy quét trích dẫn có mục tiêu đã hoàn tất điều kiện dừng, không có nguồn đe dọa cao nào chưa được xử lý bên trong ranh giới giao thức.
3. Độ phủ 15/15 KHÔNG đồng nghĩa với chứng minh tính mới toàn cục (universal novelty).
