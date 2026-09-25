# 00_PACKET_MANIFEST — Danh mục Hồ sơ Gói Bằng chứng MP1

## 1. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **Vòng thẩm tra hiện hành:** `MP1-V002 ACTIVE`
- **Số lượng bài báo toàn văn chính tắc:** `paper_count = 10` (10 full-text papers)
- **Phán quyết thẩm tra đe dọa (TARGETED_THREAT_AUDIT):**
  - **Trạng thái:** `STATUS = SUBSTANTIALLY_NARROWED` [AUDIT VERDICT]
  - **Độ tin cậy:** `CONFIDENCE = high` [AUDIT VERDICT]
  - **Mục tiêu T1 (Ma sát tiếp xúc dây NiTi):** `closed_by_full_text` [AUDIT VERDICT]
  - **Mục tiêu T2 (Áp suất giam giữ chủ động):** `open_in_current_full_text_set` [AUDIT VERDICT]
  - **Mục tiêu T3 (Ghép cặp chuyển pha và tiếp xúc):** `substantially_preempted` [AUDIT VERDICT]
- **Kiểm tra bài toán thay thế tham số (Parameter-substitution kill test):**
  - `existing_elastic_fiber_model_appears_sufficient = false` [AUDIT VERDICT]
  - `niti_requires_distinct_constitutive_contact_coupling = false` [AUDIT VERDICT]
  - `evidence_status = insufficient` [AUDIT VERDICT]
- **Độ bao phủ trích dẫn (Citation coverage):**
  - Số hướng bắt buộc: `required directions = 14` (trích dẫn ngược: 8, trích dẫn xuôi: 6)
  - `all_required_directions_screened = false`
  - `no_unresolved_high_threat_source = true`
  - `stop_condition_satisfied = false`
  - `search_cutoff_date = NOT SET`

---

## 2. Danh sách các gói bằng chứng (Packet list)

| Packet | Phạm vi công việc (Worker scope) | Yêu cầu / Mục tiêu chính | paper_ids cốt lõi | Trạng thái kiểm chứng | Vấn đề mở (Open issues) |
|---|---|---|---|:---:|---|
| **W01** | Tái dựng kiến trúc mentor ban đầu và logic MP1-V001 | Kiến trúc mentor; C1–C8; logic sụp đổ tính mới linh kiện | `240fbf6022`, `182d854610`, `3aa8790db0`, `2cd907e77a`, `bbe88a0c04`, `c6a31066f8`, `de64029540`, `55457a97c6` | Hoàn tất 100% | Cần làm rõ ranh giới giữa tính mới linh kiện và câu hỏi cơ học. |
| **W02** | Thẩm tra chuyên sâu C1 và C2 | Wire jamming; positive-pressure jamming | `240fbf6022` (Bai 2022), `182d854610` (Liu 2021), `3aa8790db0` (Zhang 2026) | Hoàn tất 100% | Mô hình sợi nylon của Zhang 2026 có thể mở rộng cho NiTi hay không. |
| **W03** | Thẩm tra dòng nghiên cứu SMA + Jamming (C3) | Dòng Takashima (2022–2026) và Matsumoto (2024) | `2cd907e77a`, `7ce492505d`, `99fe24da8b`, `d3b3b6963f` | Hoàn tất 100% | Dây SMA chỉ làm cốt nâng đỡ trong hạt, không tự trượt ma sát nghẽn. |
| **W04** | Thẩm tra nguồn áp suất và piston SMA (C4 & C8) | Bơm vi mô dẻo ECF; piston ép hạt; bơm SMA | `bbe88a0c04` (Huynh 2022), `c6a31066f8` (Wang 2024), `de64029540` (Pierce 2013), `55457a97c6` (Kotb 2021) | Hoàn tất 100% | C8 là actuator substitution, rủi ro cao nếu coi là đóng góp chính. |
| **W05** | Ranh giới C5, C6, C7 sau V001 và Mechanics Core | Phân tích các claim mở và sự hình thành Mechanics Core | `240fbf6022`, `182d854610`, `2cd907e77a`, `c6a31066f8`, `3aa8790db0` | Hoàn tất 100% | Open trong 11 bài V001 không đồng nghĩa với tính mới phổ quát. |
| **W06** | Thẩm tra mục tiêu T1 (Tiếp xúc & Ma sát NiTi) | Cáp/dây NiTi tiếp xúc và trượt ma sát thay đổi độ cứng | `d9966f2f5e`, `53200aa0c6`, `98fee47c04`, `e8462758c3`, `6dd1ca94d1` | Hoàn tất 100% | T1 đóng bằng full text; ma sát tiếp xúc giữa các dây NiTi đã có prior art. |
| **W07** | Thẩm tra mục tiêu T2 (Áp suất giam giữ chủ động) | Phân loại áp suất P1 (thụ động), P2 (cố định), P3 (chủ động) | `ccdc1bb980` (Tjahjanto 2017), `aaad9c248c` (Xin Liu 2004), `53200aa0c6`, `fac21c950e` | Hoàn tất 100% | T2 mở trong tập tài liệu; P1/P2 không tương đương với P3 chủ động. |
| **W08** | Thẩm tra mục tiêu T3 (Ghép cặp chuyển pha & tiếp xúc) | Ghép cặp chuyển pha NiTi $\times$ ma sát $\times$ độ cứng $\times$ áp suất | `d9966f2f5e`, `53200aa0c6`, `98fee47c04`, `e8462758c3`, `6dd1ca94d1` | Hoàn tất 100% | T3 bị đón đầu thực chất; chỉ còn thiếu mắt xích áp suất chủ động P3. |
| **W09** | Thẩm tra sâu Reedlunn et al. 2013 Part II | Cáp $7\times 7$ và $1\times 27$; vết lõm chế tạo; chuyển pha từng lớp | `fac21c950e` (Reedlunn, Daly & Shaw 2013 Part II) | Hoàn tất 100% | Thử nghiệm kéo đẳng nhiệt ngàm cứng, không có uốn và không có áp suất P3. |
| **W10** | Thẩm tra sâu Fang et al. 2019 & Rủi ro thay thế tham số | Mô hình sợi OpenSees; vào tải lệch pha; suy giảm chu kỳ | `2f7fcf2f8f` (Fang et al. 2019) | Hoàn tất 100% | Mô hình rút gọn OpenSees tăng rủi ro bị phản biện; bằng chứng vẫn là insufficient. |
| **W11** | Độ bao phủ trích dẫn và tính toàn vẹn nguồn | Sàng lọc 178 ứng viên; bản đồ B01–B08, F01–F06; kiểm tra registry | Toàn bộ 24 bài báo trong registry | Hoàn tất 100% | Điều kiện dừng chưa thỏa mãn; không suy luận tính mới từ nhánh 0 kết quả. |

---

## 3. Chỉ mục bài báo toàn cầu (Global paper index)

Toàn bộ 24 bài báo trong cơ sở dữ liệu kiểm chứng MP1 được liệt kê đầy đủ với siêu dữ liệu chính xác:

| paper_id | Tiêu đề bài báo (Title) | Năm | DOI | Vòng thẩm tra | Tệp Evidence JSON (trong `data/`) | Tệp PDF gốc (trong `papers/`) |
|---|---|:---:|---|:---:|---|---|
| `de64029540` | A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump | 2013 | `10.1109/TMECH.2012.2211032` | MP1-V001 | `evidence/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json` | `papers/verification/MP1-V001/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf` |
| `182d854610` | A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots | 2021 | `10.1109/LRA.2021.3097255` | MP1-V001 | `evidence/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json` | `papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf` |
| `55457a97c6` | Shape Memory Alloy Capsule Micropump for Drug Delivery Applications | 2021 | `10.3390/mi12050520` | MP1-V001 | `evidence/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json` | `papers/verification/MP1-V001/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf` |
| `240fbf6022` | Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming | 2022 | `10.3390/app12073582` | MP1-V001 | `evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json` | `papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf` |
| `bbe88a0c04` | Soft actuator with switchable stiffness using a micropump-activated jamming system | 2022 | `10.1016/j.sna.2022.113449` | MP1-V001 | `evidence/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json` | `papers/verification/MP1-V001/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf` |
| `2cd907e77a` | Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon | 2022 | `10.20965/jrm.2022.p0466` | MP1-V001 | `evidence/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json` | `papers/verification/MP1-V001/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf` |
| `7ce492505d` | Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon | 2024 | `10.1299/mej.24-00130` | MP1-V001 | `evidence/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json` | `papers/verification/MP1-V001/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf` |
| `99fe24da8b` | Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon | 2024 | `10.20965/jrm.2024.p0470` | MP1-V001 | `evidence/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json` | `papers/verification/MP1-V001/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf` |
| `c6a31066f8` | Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm | 2024 | `10.1108/IR-11-2023-0305` | MP1-V001 | `evidence/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json` | `papers/verification/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf` |
| `3aa8790db0` | A variable stiffness omnidirectional chain based on positive-pressure fiber jamming | 2026 | `10.5194/ms-17-481-2026` | MP1-V001 | `evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json` | `papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf` |
| `d3b3b6963f` | Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon | 2026 | `10.20965/jrm.2026.p0646` | MP1-V001 | `evidence/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json` | `papers/verification/MP1-V001/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf` |
| `00414aac4b` | Superelastic shape memory alloy cables: Part I – Isothermal tension experiments | 2013 | `10.1016/j.ijsolstr.2013.03.013` | MP1-V002 | `evidence/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json` | `papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf` |
| `fac21c950e` | Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses | 2013 | `10.1016/j.ijsolstr.2013.03.015` | MP1-V002 | `evidence/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json` | `papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf` |
| `d9966f2f5e` | Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification | 2014 | `10.1061/(ASCE)EM.1943-7889.0000852` | MP1-V002 | `evidence/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json` | `papers/verification/MP1-V002/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf` |
| `40760daa02` | Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments | 2016 | `10.1061/(ASCE)EM.1943-7889.0001072` | MP1-V002 | `evidence/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json` | `papers/verification/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf` |
| `ccdc1bb980` | BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE | 2017 | [KHÔNG CÓ DOI — OMAE 2017] | MP1-V002 | `evidence/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json` | `papers/verification/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf` |
| `2f7fcf2f8f` | Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application | 2019 | `10.1016/j.engstruct.2019.01.049` | MP1-V002 | `evidence/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json` | `papers/verification/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf` |
| `53200aa0c6` | Mechanical response of single and double-helix SMA wire ropes | 2021 | `10.1080/15376494.2021.1955313` | MP1-V002 | `evidence/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json` | `papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf` |
| `98fee47c04` | Nonlinear Vibration Isolation via a NiTiNOL Wire Rope | 2021 | `10.3390/app112110032` | MP1-V002 | `evidence/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json` | `papers/verification/MP1-V002/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf` |
| `7f3f45407f` | Nonlinear dynamic response of a wire rope isolator: Experiment, identification and validation | 2021 | `10.1016/j.engstruct.2021.112121` | MP1-V002 | `evidence/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json` | `papers/verification/MP1-V002/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf` |
| `aaad9c248c` | Cable Vibration Considering Internal Friction | 2004 | [KHÔNG CÓ DOI — Luận văn M.S.] | MP1-V002 | `evidence/A5-Cable vibration considering internal friction_aaad9c248c.json` | `papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf` |
| `6dd1ca94d1` | NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings | 2022 | `10.3390/s22208045` | MP1-V002 | `evidence/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json` | `papers/verification/MP1-V002/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf` |
| `9e15094d68` | Superelasticity SMA cables and its simplified FE model | 2023 | `10.1007/s40430-022-03957-2` | MP1-V002 | `evidence/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json` | `papers/verification/MP1-V002/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf` |
| `e8462758c3` | High damping capacity with a wide temperature window in braided NiTi microfilaments | 2026 | `10.1016/j.matlet.2026.141544` | MP1-V002 | `evidence/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json` | `papers/verification/MP1-V002/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf` |

---

## 4. Bản đồ phát biểu và mục tiêu (Claim map)

| Claim / Target | Trạng thái có thẩm quyền | Gói bằng chứng chính | Các paper_id bằng chứng cốt lõi |
|---|:---:|:---:|---|
| **C1** (Wire/fiber jamming variable stiffness) | `closed` | W01, W02 | `240fbf6022` (Bai 2022), `3aa8790db0` (Zhang 2026) |
| **C2** (Positive-pressure jamming variable stiffness) | `closed` | W01, W02 | `182d854610` (Liu 2021), `3aa8790db0` (Zhang 2026) |
| **C3** (SMA + jamming in same device) | `closed` | W01, W03 | `2cd907e77a`, `7ce492505d`, `99fe24da8b`, `d3b3b6963f` (Takashima lineage) |
| **C4** (Onboard/compact pressure source) | `closed` | W01, W04 | `bbe88a0c04` (Huynh 2022), `c6a31066f8` (Wang 2024) |
| **C5** (NiTi wires themselves as jamming medium) | `open_in_supplied_corpus` | W01, W05 | `240fbf6022`, `2cd907e77a`, `c6a31066f8`, `3aa8790db0` |
| **C6** (Positive pressure on NiTi wire bundle) | `open_in_supplied_corpus` | W01, W05 | `182d854610`, `3aa8790db0` |
| **C7** (Coupled NiTi-friction-pressure-stiffness) | `open_in_supplied_corpus` | W01, W05 | `3aa8790db0`, `2cd907e77a`, `7ce492505d`, `c6a31066f8` |
| **C8** (SMA-driven syringe/piston powering jamming) | `substantially_preempted` | W01, W04 | `de64029540` (Pierce 2013), `55457a97c6` (Kotb 2021), `bbe88a0c04`, `c6a31066f8` |
| **T1** (NiTi wires contacting/slipping frictional bundle) | `closed_by_full_text` | W06, W09 | `d9966f2f5e`, `53200aa0c6`, `98fee47c04`, `e8462758c3`, `6dd1ca94d1`, `fac21c950e` |
| **T2** (Active positive/confinement pressure on bundle) | `open_in_current_full_text_set` | W07 | `ccdc1bb980` (Tjahjanto 2017), `aaad9c248c` (Xin Liu 2004), `53200aa0c6`, `fac21c950e` |
| **T3** (Coupled transformation, friction, hysteresis, pressure) | `substantially_preempted` | W08, W09 | `d9966f2f5e`, `53200aa0c6`, `98fee47c04`, `e8462758c3`, `6dd1ca94d1`, `fac21c950e` |
| **Parameter-substitution kill test** | `insufficient` | W10 | `2f7fcf2f8f` (Fang 2019), `fac21c950e` (Reedlunn 2013) |
| **Citation coverage stop condition** | `stop_condition_satisfied = false` | W11 | `citation_coverage.json`, `METADATA_SCREENING.json` |

---

## 5. Danh mục các vấn đề chưa giải quyết đã biết (Known unresolved issues)

1. **Điều kiện dừng tìm kiếm trích dẫn chưa đóng (Stop condition open):**  
   Nhánh trích dẫn ngược B07 (`98fee47c04`, Niu & Chen 2021) và B08 (`fac21c950e`, Reedlunn et al. 2013) vừa mới được xác lập làm ưu tiên bổ sung sau khi thẩm tra 10 bài toàn văn, hiện chưa hoàn tất việc rà soát và lưu trữ trạng thái sàng lọc.
2. **Thiếu mã định danh số (DOI missing):**  
   Hai tài liệu nền tảng rất quan trọng là Luận văn M.S. của Xin Liu 2004 (`aaad9c248c`) và bài báo kỷ yếu hội thảo OMAE 2017 của Tjahjanto et al. (`ccdc1bb980`) không có mã DOI số. Tuy nhiên, toàn văn PDF đã được kiểm chứng trực tiếp từng trang trong repository.
3. **Trường dữ liệu gốc trong Registry hiển thị null:**  
   Trong `data/paper_registry.json`, trường `title` và `year` của một số bài báo verification hiển thị `null` ở cấp độ danh mục, dù tệp evidence JSON tại `data/evidence/` lưu trữ đầy đủ 100% siêu dữ liệu.
4. **Trạng thái chưa xác minh đầy đủ về bài toán thay thế tham số:**  
   Hiện tại, repository chưa có một mô phỏng số hoặc thí nghiệm so sánh đối đầu (head-to-head baseline) trực tiếp giữa một mô hình dầm sợi đàn hồi thông thường (Zhang & Yao 2026) được gán mô-đun siêu đàn hồi NiTi với một mô hình tiếp xúc ma sát vi mô 3D đầy đủ dưới cùng một điều kiện uốn có áp suất P3. Do đó, trạng thái bắt buộc phải giữ nguyên là `insufficient`.
