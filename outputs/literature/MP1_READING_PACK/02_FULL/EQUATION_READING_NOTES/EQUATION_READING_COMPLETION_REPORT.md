# MP1 READING PACK — EQUATION READING COMPLETION REPORT
## Selective Mechanical Equation Reading Notes

- **TASK_ID:** MP1-LR-P2-EQ-R1
- **ACTION:** SELECTIVE_EQUATION_EXPLANATION
- **TARGET:** EQUATION_READING_NOTES_READY
- **DATE:** 2026-10-15
- **STATUS:** PASS

---

## 1. PRECONDITIONS VERIFICATION

- [x] P0/P1/P2 Pilot: `PASS`
- [x] WP-B: `PASS` (71 new evidence records, 84 total in JSONL)
- [x] WP-D: `PASS` (41 evidence records in JSONL)
- [x] WP-C-R1: `COMPLETE` (M23 Evidence Records M23-E01 đến M23-E10 đã được tạo đầy đủ, schema validation PASS, trạng thái `VERIFIED_FULL_TEXT`, mâu thuẫn nhận dạng P0-R2 đã được đóng).

---

## 2. SUMMARY OF EQUATION SELECTION & VERIFICATION

| Equation Group | Candidate Evaluated | Selected for In-Depth Notes | Directly Applicable | Applicable with Assumptions | Analogy Only | Verification Status |
|---|---:|---:|---:|---:|---:|---|
| **Group B — Jamming & Friction Mechanics** | 22 | 9 | 0 | 8 | 1 | 100% VERIFIED_FULL_TEXT |
| **Group C — Wire Bundle & NiTi Mechanics** | 18 | 10 | 3 | 6 | 1 | 100% VERIFIED_FULL_TEXT |
| **Group D — SMA Friction & Actuation** | 12 | 9 | 4 | 5 | 0 | 100% VERIFIED_FULL_TEXT |
| **TOTAL** | **52** | **28** | **7** | **19** | **2** | **100% VERIFIED_FULL_TEXT** |

### Chi tiết các phương trình được chọn:
- **WP-B (9 ghi chú):**
  - Note B-01: M17 Eqs. (1)–(3) (Pre-slip shear limit $F_0$, deflection $w_0$, second moment of area $I_{\text{p-s}}$)
  - Note B-02: M17 Eqs. (5)–(7), (8)–(15) (Post-slip deflection $w_1$, partial-slip $I_{\text{pa-s}}$, full-slip $I_{\text{f-s}}$, general $n$-layer relations)
  - Note B-03: M18 Eqs. (1)–(2) (Continuum curved beam equilibrium for layer jamming beam)
  - Note B-04: M18 Eqs. (3), (5) (Parabolic shear stress $\tau(y, Q)$ and slip threshold shear force $Q_{\text{slip}}$)
  - Note B-05: M18 Eqs. (7)–(9) (Continuum shear stress $\tau(y, s)$, sliding boundary $y_s(Q)$ propagation, $Q_{\max}$)
  - Note B-06: M13 Eqs. (1), (5)–(10) (Positive-pressure fiber jamming work-energy balance and slipping-state inertia $I_S$)
  - Note B-07: M13 Eq. (11) (Phenomenological quadratic transition model $I_{\text{eq}}(Q)$)
  - Note B-08: M19 Eqs. (1)–(3) (Incremental Coulomb friction law $\tau = \operatorname{sign}(Q)\mu p$ and sliding layer normal stress $\sigma$)
  - Note B-09: M20 Eqs. (4), (8) (RVE stress tensor and average-field volume homogenization $\bar{\boldsymbol{\sigma}}$)
- **WP-C (10 ghi chú):**
  - Note C-01: M22 Eqs. (33)–(35) (Effective bending stiffness $EI_{\text{eff} 2}$ and deflection magnification $\delta_2$ under midspan load)
  - Note C-02: M22 Eq. (37) (Linear slip rigidity calibration $k = \xi \bar{\sigma} + k_0$)
  - Note C-03: M23 Eqs. (3)–(4) (2D Plane stress state space formulation and normal bending stress $\sigma_x$)
  - Note C-04: M23 Eq. (15) (Interfacial slip boundary condition in state space and global transfer matrix)
  - Note C-05: M23 Eq. (26) (Deflection magnification coefficient DMC $\delta$ and stiffness coefficient EBSC $\gamma$)
  - Note C-06: M23 Eq. (28) (Exponential interfacial slip ratio distribution $\Delta u_i / \Delta u_1$)
  - Note C-07: M24 Eqs. (11)–(12) (Eigenstrain kinematics for wire rope slip states: stick, partial stick, full slip)
  - Note C-08: M24 Eq. (18) (6x6 cross-section constitutive stiffness matrix under wire slip modes)
  - Note C-09: M29 Eqs. (8)–(9) (Total strain increment decomposition for superelastic SMA: $d\varepsilon = d\varepsilon^{\text{tr}} + d\varepsilon^{\text{th}} + d\varepsilon^{\text{e}}$)
  - Note C-10: M29 Eqs. (14)–(17) (Phase transformation flow rule and 3D incremental constitutive law for SMA)
- **WP-D (9 ghi chú):**
  - Note D-01: M31 Eqs. (1), (2.1)–(2.2) (Work-energy balance for flexible robot with SMA clamping friction: $\int F_{\text{ext}} dx = U + F_f s$)
  - Note D-02: M31 Eqs. (3)–(6) (Peripheral wire sliding kinematics and chord deflection geometry)
  - Note D-03: M31 Eqs. (7)–(9) (Modeled flexural rigidity $(EI)_a$ from SMA clamping friction dissipation)
  - Note D-04: M31 Eq. (10) (Experimental flexural rigidity calculation from cantilever tip deflection: $EI = F_{\text{ext}} L^3 / (3\delta)$)
  - Note D-05: M32 Eq. (1) (Multi-element cantilever beam stiffness in unjammed state: $P/\delta = 3 n E I / L^3$)
  - Note D-06: M33 Eqs. (24), (31) (Gaussian error function phase hysteresis $R_m(x)$ and thermomechanical actuator force rate $\dot{F}$)
  - Note D-07: M34 Eq. (1) (Brinson detwinned martensite fraction $\xi_{St}$ under shear stress)
  - Note D-08: M34 Eq. (2) (SMA helical spring force-deflection relation with pitch angle change and detwinning)
  - Note D-09: M34 Eq. (3) (Kinematic displacement compatibility between SMA spring and compliant container)

---

## 3. SCIENTIFIC DISTINCTION & INTEGRITY COMPLIANCE

Bộ ghi chú tuân thủ 100% các yêu cầu phân định cơ học nghiêm ngặt:
1. **$EI$ không đồng nhất với Young's modulus $E$:** Luôn tách bạch độ cứng uốn kết cấu (phụ thuộc vào hình học và trạng thái trượt tiếp xúc) với mô đun đàn hồi của vật liệu.
2. **Bending stiffness không mặc nhiên tương đương slope của force-displacement curve:** Phân định rõ độ dốc đo đạc $F/\delta$ chịu ảnh hưởng của công tiêu tán ma sát và phi tuyến hình học.
3. **Lực không đồng nhất với mô men:** Tách bạch rõ các công thức uốn chịu lực cắt ($V, Q$) với uốn thuần túy ($M$).
4. **Áp suất không đồng nhất với lực nén tiếp xúc:** Phân tích rõ sự suy giảm áp suất qua màng bọc và hiệu ứng vòm (arching effect) trong bó dây tròn.
5. **Tiếp xúc dây-dây khác tiếp xúc dây-ống bọc:** Ghi rõ sự khác biệt trong M31 (dây-ống cao su) so với M22/M23/M24 (dây-dây).
6. **Kẹt lớp khác kẹt bó dây:** Khác biệt giữa trượt phẳng 2D và trượt theo đường tiếp xúc 3D phân bố theo góc azimuthal.
7. **Lực lò xo SMA khác áp suất mẫu:** Lực nén của lò xo xoắn $F_M$ là lực tập trung, cần cơ cấu phân phối để chuyển đổi thành áp suất tiếp xúc giam $p$.
8. **Phân biệt 3 loại trễ (hysteresis):**
   - *Elastic hysteresis:* Tiêu tán nội ma sát nhớt đàn hồi rất nhỏ.
   - *Superelastic hysteresis:* Trễ chuyển pha tinh thể austenite $\leftrightarrow$ martensite do năng lượng tự do nhiệt động học (M29).
   - *Frictional hysteresis:* Trễ do ma sát Coulomb trượt giữa các mặt tiếp xúc (M17, M18, M31).
9. **Full slip không đồng nghĩa biến dạng dẻo:** Trượt hoàn toàn chỉ giải phóng liên kết cắt giữa các phần tử, bản thân từng sợi dây vẫn hoàn toàn đàn hồi.
10. **Calibration không phải independent validation:** Đánh dấu rõ các công thức hiệu chuẩn tham số (như M22 Eq. 37, M13 Eq. 11) để phân biệt với mô hình dẫn xuất vi mô cơ bản.

---

## 4. METRICS & COUNTS

- **WP_B_EQUATIONS_SELECTED:** 9 (từ 5 bài báo: M17, M18, M13, M19, M20)
- **WP_C_EQUATIONS_SELECTED:** 10 (từ 4 bài báo: M22, M23, M24, M29)
- **WP_D_EQUATIONS_SELECTED:** 9 (từ 4 bài báo: M31, M32, M33, M34)
- **EQUATIONS_VERIFIED:** 28/28 (100% verified against canonical PDFs)
- **EQUATIONS_UNVERIFIED:** 0
- **VARIABLES_EXPLAINED:** > 110 biến số và ký hiệu (đầy đủ định nghĩa, đơn vị và ngữ cảnh)
- **APPLICABILITY_ASSESSED:** 28 phương trình được phân loại chặt chẽ trong `EQUATION_APPLICABILITY_MATRIX.csv`
- **SOURCE_LOCATOR_VALIDATION:** 100% locators khớp chính xác số trang PDF và phần văn bản gốc
- **HUMAN_REVIEW_REQUIRED:** Không có mục nào bắt buộc human review; các lỗi in ấn của tác giả (như `sing Q` ở M18 Eq. 4) đã được ghi nhận đầy đủ tại `EQUATION_UNVERIFIED_ITEMS.md`.

---

## 5. DELIVERABLES CREATED

Thư mục đầu ra: `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/`

1. `EQUATION_SELECTION_MATRIX.csv` (52 dòng đánh giá đầy đủ tất cả các ứng viên phương trình)
2. `WP_B_EQUATION_NOTES.md` (Ghi chú chuyên sâu 9 phương trình nhóm kẹt lớp và ma sát)
3. `WP_C_EQUATION_NOTES.md` (Ghi chú chuyên sâu 10 phương trình nhóm bó dây và NiTi)
4. `WP_D_EQUATION_NOTES.md` (Ghi chú chuyên sâu 9 phương trình nhóm phát động và ma sát SMA)
5. `EQUATION_VARIABLE_GLOSSARY.md` (Từ điển biến số toàn diện, cảnh báo đồng hóa ký hiệu chéo)
6. `EQUATION_APPLICABILITY_MATRIX.csv` (Ma trận đánh giá khả năng áp dụng cho MP1 với 28 dòng)
7. `EQUATION_UNVERIFIED_ITEMS.md` (Nhật ký theo dõi các điểm dị biệt nguồn, lỗi in ấn của tác giả)
8. `EQUATION_READING_COMPLETION_REPORT.md` (Báo cáo hoàn thành này)

---

## 6. QUALITY GATE DECISION

**QUALITY GATE: PASS**

Bộ ghi chú chuyên sâu về phương trình cơ học (MP1-LR-P2-EQ-R1) đã hoàn thành xuất sắc, đầy đủ 8 tệp theo quy định, xác minh 100% trực tiếp từ các file PDF canonical, duy trì đầy đủ tính liêm chính khoa học và sẵn sàng bàn giao cho WP-E để tích hợp vào P3 handoff.

**READY_FOR_WP_E: YES**
