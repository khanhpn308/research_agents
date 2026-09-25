# Sổ bộ Các Khẳng định Không có Tính mới (MP1 Non-Novelty Register)

> **Tệp chính tắc:** `MP1_NON_NOVELTY_REGISTER.json`  
> **Tổng số mục:** 8 khẳng định (C1–C8)  
> **Mục tiêu:** Khóa chặt các khẳng định đã bị văn hiến tiền nhiệm đóng hoặc đón đầu thực chất; phân loại chính xác bản chất tiền nhiệm.

## 1. Bảng Tổng hợp Sổ bộ Không Tính mới (C1–C8)

| Mã Sổ bộ (ID) | Khẳng định | Phân loại Tiền nhiệm | Nguồn Tiền nhiệm Chính | Paper ID | Trạng thái Bằng chứng | Độ tin cậy |
|:---:|:---:|---|---|:---:|:---:|:---:|
| **NN-01** | `C1` | `DEVICE_LEVEL_PRIOR_ART` | Bai et al. (2022) / Zhang & Yao (2026) | `240fbf6022` | `closed_by_full_text` | `high` |
| **NN-02** | `C2` | `DEVICE_LEVEL_PRIOR_ART` | Liu et al. (2021) / Zhang & Yao (2026) | `182d854610` | `closed_by_full_text` | `high` |
| **NN-03** | `C3` | `DEVICE_LEVEL_PRIOR_ART` | Takashima et al. (2022, 2024) / Matsumoto et al. (2024) | `2cd907e77a` | `substantially_preempted` | `high` |
| **NN-04** | `C4` | `IMPLEMENTATION_SUBSTITUTION` | Huynh et al. (2022) / Wang et al. (2024) | `bbe88a0c04` | `closed_by_full_text` | `high` |
| **NN-05** | `C5` | `EXISTENCE_LEVEL_PRIOR_ART` | Carboni et al. (2015) / Vahidi et al. (2022) / Silva et al. (2020) | `53200aa0c6` | `closed_by_full_text` | `high` |
| **NN-06** | `C6` | `BOUNDARY_CONDITION_NOVELTY` | Tjahjanto et al. (2017) / Xin Liu (2004) / Astra Critique G02 | `ccdc1bb980` | `downgraded_to_boundary_condition` | `high` |
| **NN-07** | `C7` | `MODEL_DISCRIMINATION_QUESTION` | Fang et al. (2019) / Carboni et al. (2016) / Niu et al. (2021) | `2f7fcf2f8f` | `substantially_preempted_and_narrowed` | `high` |
| **NN-08** | `C8` | `IMPLEMENTATION_SUBSTITUTION` | Kotb et al. (2021) / Pierce et al. (2013) | `55457a97c6` | `closed_by_full_text` | `high` |

## 2. Chi tiết Từng Khẳng định Không có Tính mới

### Khẳng định C1: NN-01 (DEVICE_LEVEL_PRIOR_ART)
- **Khẳng định ban đầu:** Cơ chế biến đổi độ cứng bằng kẹt dây (wire jamming) cho robot mềm dưới áp suất giam giữ.
- **Khẳng định hiện tại:** ĐÃ ĐÓNG (CLOSED). Hiện tượng kẹt ma sát giữa các sợi dây trong dầm dẻo là văn hiến đã xác lập trong robot mềm.
- **Nguồn tiền nhiệm:** Bai et al. (2022) / Zhang & Yao (2026) (`240fbf6022`)
- **Tiêu đề bài báo:** A Wire Jamming-Based Variable Stiffness Soft Gripper (Bai, Y. et al., 2022)
- **DOI:** `10.1109/LRA.2022.3188880`
- **Điều nguồn chứng minh:** Chứng minh biến thiên độ cứng lên tới 15 lần nhờ kẹt ma sát bó dây thép trong ngón tay robot mềm; Zhang & Yao 2026 mô hình hóa dầm sợi dẻo có trượt ma sát Coulomb.
- **Điều nguồn không chứng minh:** Không nghiên cứu vật liệu siêu đàn hồi NiTi có chuyển pha ứng suất (chỉ dùng thép đàn hồi tuyến tính và sợi nylon).
- **Tác động đối với đề tài MP1:** Khẳng định cấp thiết bị về wire jamming hoàn toàn không có tính mới; bị loại bỏ 100% khỏi phạm vi đóng góp của luận văn.
- **Trạng thái & Độ tin cậy:** `closed_by_full_text` | `high`
- **Xuất xứ (Provenance):** `outputs/execution/MP1-V002/W2-02/MP1_C1_C8_CLAIM_MATRIX.json#C1, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W02_C1_C2_EVIDENCE.md`

---
### Khẳng định C2: NN-02 (DEVICE_LEVEL_PRIOR_ART)
- **Khẳng định ban đầu:** Cơ cấu kẹt dưới áp suất dương (positive-pressure jamming) dùng chất lưu hoặc khí nén.
- **Khẳng định hiện tại:** ĐÃ ĐÓNG (CLOSED). Cơ cấu kẹt ép bằng áp suất dương trong màng bao đàn hồi đã được công bố và ứng dụng rộng rãi.
- **Nguồn tiền nhiệm:** Liu et al. (2021) / Zhang & Yao (2026) (`182d854610`)
- **Tiêu đề bài báo:** A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots (Liu, X. et al., 2021)
- **DOI:** `10.1109/LRA.2021.3097255`
- **Điều nguồn chứng minh:** Chứng minh áp suất dương lên tới 250 kPa trong đồ gá đeo giúp tăng độ cứng vượt trội và tránh hiện tượng nhăn màng của chân không.
- **Điều nguồn không chứng minh:** Không nghiên cứu bó dây NiTi và không khảo sát phương trình vi phân tiếp xúc có áp suất biến thiên chủ động theo thời gian.
- **Tác động đối với đề tài MP1:** Áp suất dương không phải là nguyên lý mới; không thể dựa vào áp suất dương để biện minh tính mới cho đề tài.
- **Trạng thái & Độ tin cậy:** `closed_by_full_text` | `high`
- **Xuất xứ (Provenance):** `outputs/execution/MP1-V002/W2-02/MP1_C1_C8_CLAIM_MATRIX.json#C2, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W02_C1_C2_EVIDENCE.md`

---
### Khẳng định C3: NN-03 (DEVICE_LEVEL_PRIOR_ART)
- **Khẳng định ban đầu:** Sự kết hợp giữa hợp kim nhớ hình (SMA) và cơ cấu kẹt hạt/lớp (jamming) trong cùng một cơ cấu.
- **Khẳng định hiện tại:** ĐÓN ĐẦU THỰC CHẤT (SUBSTANTIALLY_PREEMPTED). Dòng nghiên cứu của Takashima và Matsumoto đã kết hợp sâu rộng SMA và jamming.
- **Nguồn tiền nhiệm:** Takashima et al. (2022, 2024) / Matsumoto et al. (2024) (`2cd907e77a`)
- **Tiêu đề bài báo:** Variable Stiffness Device Using Shape Memory Alloy and Granular Jamming (Takashima, K. et al., 2022)
- **DOI:** `10.1109/LRA.2022.3144502`
- **Điều nguồn chứng minh:** Tích hợp dây kích hoạt nhiệt SMA trong hạt jamming chân không để điều khiển độ cứng và khóa hình dạng.
- **Điều nguồn không chứng minh:** Dùng SMA làm actuator nhiệt hoặc cốt nâng đỡ, không khảo sát bó dây NiTi siêu đàn hồi tự trượt ma sát tiếp xúc với nhau.
- **Tác động đối với đề tài MP1:** Khẳng định phối hợp kiến trúc lai SMA + jamming bị đón đầu ở cấp hệ thống; chỉ bài toán cơ học trượt nội tại NiTi là có thể xem xét.
- **Trạng thái & Độ tin cậy:** `substantially_preempted` | `high`
- **Xuất xứ (Provenance):** `outputs/execution/MP1-V002/W2-02/MP1_C1_C8_CLAIM_MATRIX.json#C3, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W03_C3_SMA_JAMMING_LINEAGE.md`

---
### Khẳng định C4: NN-04 (IMPLEMENTATION_SUBSTITUTION)
- **Khẳng định ban đầu:** Tích hợp nguồn áp suất thu nhỏ trên thân robot mềm để điều khiển cơ cấu kẹt độc lập.
- **Khẳng định hiện tại:** ĐÃ ĐÓNG / ĐÓN ĐẦU THỰC CHẤT. Các loại bơm vi mô tích hợp (ECF, nhiệt, điện môi, SMA) đã được công bố dày đặc.
- **Nguồn tiền nhiệm:** Huynh et al. (2022) / Wang et al. (2024) (`bbe88a0c04`)
- **Tiêu đề bài báo:** Electroconjugate Fluid Micropump for Soft Actuators (Huynh, T. et al., 2022)
- **DOI:** `10.1109/TMECH.2022.3168890`
- **Điều nguồn chứng minh:** Khả năng tích hợp trọn gói bơm vi mô áp suất cao trên thân cơ cấu chấp hành mềm quy mô milimét.
- **Điều nguồn không chứng minh:** Không đóng góp cơ học về tiếp xúc ma sát hay chuyển pha vật liệu.
- **Tác động đối với đề tài MP1:** Tích hợp bơm vi mô thuần túy là giải pháp kỹ thuật chế tạo, không có giá trị tính mới khoa học cơ học.
- **Trạng thái & Độ tin cậy:** `closed_by_full_text` | `high`
- **Xuất xứ (Provenance):** `outputs/execution/MP1-V002/W2-02/MP1_C1_C8_CLAIM_MATRIX.json#C4, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md`

---
### Khẳng định C5: NN-05 (EXISTENCE_LEVEL_PRIOR_ART)
- **Khẳng định ban đầu:** Cơ học tiếp xúc và ma sát trượt giữa các dây NiTi siêu đàn hồi.
- **Khẳng định hiện tại:** ĐÃ ĐÓNG (CLOSED). Cơ học tiếp xúc đường Hertz và ma sát trượt Coulomb giữa các sợi NiTi đã được mô hình hóa và đo đạc đầy đủ.
- **Nguồn tiền nhiệm:** Carboni et al. (2015) / Vahidi et al. (2022) / Silva et al. (2020) (`53200aa0c6`)
- **Tiêu đề bài báo:** Finite Element Modeling and Hysteresis Simulation of NiTi Wire Ropes (Vahidi, M. et al., 2022)
- **DOI:** `10.1007/s11071-022-07450-4`
- **Điều nguồn chứng minh:** Mô phỏng 3D phần tử hữu hạn Abaqus UMAT có ma sát Coulomb và tiếp xúc phạt (penalty) giữa các dây NiTi; đo hệ số ma sát mu = 0.18 - 0.22.
- **Điều nguồn không chứng minh:** Không khảo sát bó dây thẳng song song chịu trường áp suất phân bố biến thiên chủ động theo thời gian.
- **Tác động đối với đề tài MP1:** Mục tiêu T1 chính thức đóng bằng toàn văn; không thể tuyên bố tính mới về hiện tượng ma sát dây NiTi độc lập.
- **Trạng thái & Độ tin cậy:** `closed_by_full_text` | `high`
- **Xuất xứ (Provenance):** `outputs/execution/MP1-V002/W2-02/MP1_C1_C8_CLAIM_MATRIX.json#C5, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W06_T1_NITI_CONTACT_FRICTION.md`

---
### Khẳng định C6: NN-06 (BOUNDARY_CONDITION_NOVELTY)
- **Khẳng định ban đầu:** Áp suất giam giữ chủ động biến thiên p(t) tạo ra một nhánh quy luật cơ học tiếp xúc mới (P3).
- **Khẳng định hiện tại:** HẠ CẤP THÀNH ĐIỀU KIỆN BIÊN (DOWNGRADED). p(t) chỉ là điều kiện biên thay đổi theo thời gian; phương trình tiếp xúc hiện hữu tiếp nhận tự nhiên.
- **Nguồn tiền nhiệm:** Tjahjanto et al. (2017) / Xin Liu (2004) / Astra Critique G02 (`ccdc1bb980`)
- **Tiêu đề bài báo:** Submarine Cable Bending Mechanics Under External Hydrostatic Pressure (Tjahjanto, P. et al., 2017)
- **DOI:** `10.1016/j.oceaneng.2017.06.012`
- **Điều nguồn chứng minh:** Phương trình vi phân tiếp xúc dầm cáp dq/dx = -mu * fn(p) giải tích và số tự nhiên tiếp nhận lịch sử tải và áp suất bất kỳ mà không cần đổi công thức cơ học.
- **Điều nguồn không chứng minh:** Các nghiên cứu trước tập trung vào áp suất thủy tĩnh tĩnh (P2) hoặc lực căng tự thân (P1), chưa áp dụng cho tay gắp mềm.
- **Tác động đối với đề tài MP1:** P3 bị tước bỏ tư cách nguyên lý cơ học mới; chỉ được xem như giao thức điều khiển thực nghiệm (control protocol).
- **Trạng thái & Độ tin cậy:** `downgraded_to_boundary_condition` | `high`
- **Xuất xứ (Provenance):** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G02, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W05_T2_MECHANICS_P1_P2_P3_TEST.md`

---
### Khẳng định C7: NN-07 (MODEL_DISCRIMINATION_QUESTION)
- **Khẳng định ban đầu:** Ghép cặp chuyển pha siêu đàn hồi và ma sát trượt là một khoảng trống cơ học hoàn toàn chưa từng được mô hình hóa.
- **Khẳng định hiện tại:** ĐÓN ĐẦU THỰC CHẤT TRONG CÁP DÂY / THU HẸP NGHIÊM NGẶT. Các mô hình vĩ mô (Fang 2019, Carboni 2016) đã mô tả trễ thắt và ma sát.
- **Nguồn tiền nhiệm:** Fang et al. (2019) / Carboni et al. (2016) / Niu et al. (2021) (`2f7fcf2f8f`)
- **Tiêu đề bài báo:** A Phenomenological Constitutive Model for Superelastic SMA Cables Under Cyclic Tension (Fang, C. et al., 2019)
- **DOI:** `10.1016/j.engstruct.2019.109356`
- **Điều nguồn chứng minh:** Mô hình sợi OpenSees tái hiện xuất sắc trễ dạng cờ và suy giảm chu kỳ bằng hàm hiện tượng học mà không cần giải phương trình tiếp xúc vi mô.
- **Điều nguồn không chứng minh:** Không chứng minh cơ chế vi mô nhân quả trong bó dây chịu nén ngang; bỏ qua ma sát tiếp xúc cục bộ từng điểm.
- **Tác động đối với đề tài MP1:** Khẳng định C7 bị thu hẹp thành bài toán phân biệt mô hình (H0b vs H1) trong Miền Cùng Tồn Tại; không tồn tại tính mới phổ quát.
- **Trạng thái & Độ tin cậy:** `substantially_preempted_and_narrowed` | `high`
- **Xuất xứ (Provenance):** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md, docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G01`

---
### Khẳng định C8: NN-08 (IMPLEMENTATION_SUBSTITUTION)
- **Khẳng định ban đầu:** Cơ cấu piston/bơm vi mô kích hoạt bằng dây SMA là một phát minh cơ cấu mới cho robot biến đổi độ cứng.
- **Khẳng định hiện tại:** ĐÃ ĐÓNG (CLOSED). Cơ cấu bơm piston/màng bằng dây SMA đã có tiền nhiệm đầy đủ trong y sinh và vi cơ điện tử.
- **Nguồn tiền nhiệm:** Kotb et al. (2021) / Pierce et al. (2013) (`55457a97c6`)
- **Tiêu đề bài báo:** Shape Memory Alloy Capsule Micropump for Drug Delivery Applications (Kotb, M. et al., 2021)
- **DOI:** `10.3390/mi12050520`
- **Điều nguồn chứng minh:** Bơm vi mô viên nang dẫn động bằng lò xo và dây SMA đạt áp suất và lưu lượng ổn định.
- **Điều nguồn không chứng minh:** Không liên quan đến cơ học dầm biến đổi độ cứng.
- **Tác động đối với đề tài MP1:** C8 chỉ là thay thế cơ cấu chấp hành (actuator substitution); bị loại bỏ hoàn toàn để bảo vệ độ tin cậy của luận văn.
- **Trạng thái & Độ tin cậy:** `closed_by_full_text` | `high`
- **Xuất xứ (Provenance):** `outputs/execution/MP1-V002/W2-02/MP1_C1_C8_CLAIM_MATRIX.json#C8, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md`

---
