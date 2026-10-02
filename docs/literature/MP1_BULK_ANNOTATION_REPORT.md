# Báo Cáo Tiến Trình Highlight Hàng Loạt Toàn Bộ Corpus MP1 (12 Workers)

**Dự án**: Nghiên cứu Soft Robotics & Variable Stiffness Mechanics (MP1 Corpus)  
**Thời gian thực thi**: 26-09-2026 16:16:07  
**Cấu hình phần cứng**: 12 Workers đa luồng (ProcessPoolExecutor trên 12 CPU cores)  
**Tổng số bài báo xử lý**: 27/27 papers (**Thành công 100%**)  
**Thời gian xử lý toàn bộ**: **3.53 giây**  
**Tổng số vị trí highlight đã tạo**: **1,851 annotations**  
**Thư mục lưu trữ kết quả**: [`data/final/MP1/annotated/`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/)  
**Chỉ mục dữ liệu JSON**: [`data/final/MP1/annotated/annotation_manifest.json`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/annotation_manifest.json)  
**Script thực thi**: [`scripts/batch_annotate_mp1.py`](file:///home/khanh/projects/mechanical-research-agents/scripts/batch_annotate_mp1.py)

---

## 1. Tóm Tắt Quy Trình và Phân Bổ 12 Workers

* **Nguyên tắc bảo toàn dữ liệu**: Toàn bộ 27 file PDF gốc trong các thư mục `08_current_reports/`, `03_trace_packets/`, v.v. được **giữ nguyên vẹn tuyệt đối**, không bị sửa đổi hay thay đổi mã băm SHA256 (tuân thủ nghiêm ngặt quy định lưu trữ nghiên cứu `data/final/MP1/README.md`).
* **Quy chuẩn trích xuất**:
  * **Bỏ qua nhóm "Thư mục"**: `title`, `authors`, `year`, `doi`.
  * **18 trường nội dung còn lại**: Mỗi trường được gán một **mã màu highlight riêng biệt** (xem bảng mã màu ở Mục 3).
  * **Ghép nối dòng (Line-merge)**: Tự động gom các hộp bao từ (word bounding boxes) trên cùng một dòng thành vệt highlight liền mạch, đẹp mắt như người đọc thao tác trong Adobe Acrobat.
  * **Tích hợp Tooltip Popup**: Mỗi vị trí highlight chứa thông tin chi tiết: `[Nhóm] Tên_trường` cùng đoạn trích xuất tương ứng từ file JSON.
  * **Cây thư mục Bookmark (PDF Outlines / TOC)**: Tự động tạo menu nhảy nhanh đến từng nhóm và từng trường trong thanh bên của PDF reader.

---

## 2. Bảng Thống Kê Chi Tiết 27 Bài Báo Đã Được Highlight

| STT | Paper ID | Tiêu đề bài báo | Worker | Số Highlight | Thời gian | File PDF đã Highlight |
|:---:|:---:|---|:---:|:---:|:---:|---|
| 01 | `00414aac4b` | Superelastic shape memory alloy cables: Part I – Isothermal tension experiments | #01 | 75 | 1.6s | [`2013-Superelastic shape memory alloy cables Part I..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2013-Superelastic%20shape%20memory%20alloy%20cables%20Part%20I%20%E2%80%93%20Isothermal%20tension%20experiments_annotated.pdf) |
| 02 | `182d854610` | A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots | #02 | 92 | 1.3s | [`2021-A Positive Pressure Jamming Based Variable..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2021-A%20Positive%20Pressure%20Jamming%20Based%20Variable%20Stiffness%20Structure%20and%20its%20Application%20on%20Wearable%20Robots_annotated.pdf) |
| 03 | `1c81b2d35c` | Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes | #03 | 72 | 1.6s | [`2024-Experimental-Numerical Assessment of Mechanical..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2024-Experimental-Numerical%20Assessment%20of%20Mechanical%20Behavior%20of%20Laboratory-Made%20Steel%20and%20NiTi%20Shape%20Memory%20Alloy%20Wire%20Ropes_annotated.pdf) |
| 04 | `240fbf6022` | Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming | #04 | 83 | 1.1s | [`2022-Detachable Soft Actuators with Tunable Stiffness..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2022-Detachable%20Soft%20Actuators%20with%20Tunable%20Stiffness%20Based%20on%20Wire%20Jamming_annotated.pdf) |
| 05 | `2cd907e77a` | Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon | #05 | 85 | 1.5s | [`2022-Variable-Stiffness and Deformable Link..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2022-Variable-Stiffness%20and%20Deformable%20Link%20Using%20Shape-Memory%20Material%20and%20Jamming%20Transition%20Phenomenon_annotated.pdf) |
| 06 | `2f7fcf2f8f` | Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application | #06 | 87 | 1.9s | [`2019-Superelastic NiTi SMA cables Thermal-mechanical..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2019-Superelastic%20NiTi%20SMA%20cables%20Thermal-mechanical%20behavior,%20hysteretic%20modelling%20and%20seismic%20application_annotated.pdf) |
| 07 | `3aa8790db0` | A variable stiffness omnidirectional chain based on positive-pressure fiber jamming | #07 | 88 | 1.1s | [`2026-A variable stiffness omnidirectional chain..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2026-A%20variable%20stiffness%20omnidirectional%20chain%20based%20on%20positive-pressure%20fiber%20jamming_annotated.pdf) |
| 08 | `40760daa02` | Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments | #08 | 66 | 1.5s | [`2016-Nonlinear Vibration Absorber with Pinched..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2016-Nonlinear%20Vibration%20Absorber%20with%20Pinched%20Hysteresis%20Theory%20and%20Experiments_annotated.pdf) |
| 09 | `53200aa0c6` | Mechanical response of single and double-helix SMA wire ropes | #09 | 67 | 0.9s | [`A3-2022-Mechanical response of single and double-helix_annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/A3-2022-Mechanical%20response%20of%20single%20and%20double-helix_annotated.pdf) |
| 10 | `55457a97c6` | Shape Memory Alloy Capsule Micropump for Drug Delivery Applications | #10 | 72 | 1.2s | [`2021-Shape Memory Alloy Capsule Micropump for Drug..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2021-Shape%20Memory%20Alloy%20Capsule%20Micropump%20for%20Drug%20Delivery%20Applications_annotated.pdf) |
| 11 | `56793dea9b` | Finite Element Method for Mechanical Behavior of Shape Memory Alloy | #11 | 25 | 0.5s | [`2025-Finite Element Method for Mechanical Behavior..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2025-Finite%20Element%20Method%20for%20Mechanical%20Behavior%20of%20Shape%20Memory%20Alloy%20_annotated.pdf) |
| 12 | `6dd1ca94d1` | NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings | #12 | 68 | 3.5s | [`A8-2022-NiTi SMA Superelastic Micro Cables..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/A8-2022-NiTi%20SMA%20Superelastic%20Micro%20Cables%20Thermomechanical%20Behavior%20and%20Fatigue%20Life%20under%20Dynamic%20Loadings_annotated.pdf) |
| 13 | `7ce492505d` | Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon | #01 | 72 | 1.1s | [`2024-Effect of R-phase on shape recovery speed..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2024-Effect%20of%20R-phase%20on%20shape%20recovery%20speed%20of%20Ti-Ni%20shape%20memory%20alloy%20wire%20for%20variable-stiffness%20mechanism%20using%20jamming%20transition%20phenomenon_annotated.pdf) |
| 14 | `7f3f45407f` | Nonlinear dynamic response of a wire rope isolator: Experiment, identification and validation | #02 | 58 | 1.3s | [`2021-Nonlinear dynamic response of a wire rope..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2021-Nonlinear%20dynamic%20response%20of%20a%20wire%20rope%20isolator%20Experiment,%20identification%20and%20validation_annotated.pdf) |
| 15 | `98fee47c04` | Nonlinear Vibration Isolation via a NiTiNOL Wire Rope | #03 | 67 | 1.0s | [`A4-2021-Nonlinear vibration isolation via a nitinol..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/A4-2021-Nonlinear%20vibration%20isolation%20via%20a%20nitinol%20wire%20rope_annotated.pdf) |
| 16 | `99fe24da8b` | Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon | #04 | 64 | 1.1s | [`2024-Motion Evaluation of Variable-Stiffness Link..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2024-Motion%20Evaluation%20of%20Variable-Stiffness%20Link%20Based%20on%20Shape-Memory%20Alloy%20and%20Jamming%20Transition%20Phenomenon_annotated.pdf) |
| 17 | `9e15094d68` | Superelasticity SMA cables and its simplified FE model | #05 | 57 | 0.8s | [`A2-2023-Superelasticity SMA cables and its simplified..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/A2-2023-Superelasticity%20SMA%20cables%20and%20its%20simplified%20FE%20model_annotated.pdf) |
| 18 | `9f4295be23` | A new mechanical model of short wire ropes: Theory and experimental | #06 | 71 | 1.3s | [`2025-A new mechanical model of short wire ropes..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2025-A%20new%20mechanical%20model%20of%20short%20wire%20ropes%20Theory%20and%20experimental_annotated.pdf) |
| 19 | `aaad9c248c` | Cable Vibration Considering Internal Friction | #07 | 78 | 1.4s | [`A5-Cable vibration considering internal friction_annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/A5-Cable%20vibration%20considering%20internal%20friction_annotated.pdf) |
| 20 | `bbe88a0c04` | Soft actuator with switchable stiffness using a micropump-activated jamming system | #08 | 53 | 0.9s | [`2022-Soft actuator with switchable stiffness using..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2022-Soft%20actuator%20with%20switchable%20stiffness%20using%20a%20micropump-activated%20jamming%20system_annotated.pdf) |
| 21 | `c6a31066f8` | Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm | #09 | 60 | 0.8s | [`2024-Piston-like particle jamming for enhanced..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2024-Piston-like%20particle%20jamming%20for%20enhanced%20stiffness%20adjustment%20of%20soft%20robotic%20arm_annotated.pdf) |
| 22 | `ccdc1bb980` | BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE | #10 | 54 | 1.6s | [`A6-2017-Bending Mechanics of Cable Cores and Fillers..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/A6-2017-Bending%20Mechanics%20of%20Cable%20Cores%20and%20Fillers%20in%20a%20Dynamic%20Submarine%20Cable_annotated.pdf) |
| 23 | `d3b3b6963f` | Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon | #11 | 70 | 1.0s | [`2026-Pick-and-Place Motion by Two-Robot-Arm..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2026-Pick-and-Place%20Motion%20by%20Two-Robot-Arm%20System%20Equipped%20with%20Variable-Stiffness%20and%20Deformable%20Link%20Using%20Shape-Memory%20Alloy%20and%20Jamming%20Transition%20Phenomenon_annotated.pdf) |
| 24 | `d9966f2f5e` | Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification | #12 | 66 | 1.3s | [`A1-2015-Hysteresis of Multiconfiguration Assemblies..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/A1-2015-Hysteresis%20of%20Multiconfiguration%20Assemblies%20of_annotated.pdf) |
| 25 | `de64029540` | A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump | #01 | 76 | 0.8s | [`2013-A Biologically Inspired Wet Shape Memory..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2013-A%20Biologically%20Inspired%20Wet%20Shape%20Memory%20Alloy%20Actuated%20Robotic%20Pump_annotated.pdf) |
| 26 | `e8462758c3` | High damping capacity with a wide temperature window in braided NiTi microfilaments | #02 | 49 | 0.5s | [`A7-2026-High damping capacity with a wide temperature..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/A7-2026-High%20damping%20capacity%20with%20a%20wide%20temperature%20window%20in%20braided%20NiTi%20microfilaments_annotated.pdf) |
| 27 | `fac21c950e` | Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses | #03 | 76 | 1.2s | [`2013-Superelastic shape memory alloy cables Part II..._annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2013-Superelastic%20shape%20memory%20alloy%20cables%20Part%20II%20%E2%80%93%20Subcomponent%20isothermal%20responses_annotated.pdf) |

---

## 3. Bảng Quy Chuẩn Mã Màu (18 Trường Nghiên Cứu)

Toàn bộ 27 tài liệu đều tuân thủ bảng mã màu chuẩn đồng nhất:

| Nhóm Trường | Tên Trường (Field) | Tên Màu | Mã Hex | Mã RGB |
|---|---|:---:|:---:|:---:|
| **Câu hỏi nghiên cứu** | `research_problem` | Đỏ san hô (Coral Red) | `#F25959` | `(0.95, 0.35, 0.35)` |
| | `research_objective` | Cam tươi (Bright Orange) | `#FF8C1A` | `(1.00, 0.55, 0.10)` |
| **Hệ thống / Cơ chế** | `robot_type` | Vàng nghệ (Gold Yellow) | `#FFE01A` | `(1.00, 0.88, 0.10)` |
| | `stiffness_mechanism` | Xanh ô liu (Olive) | `#999933` | `(0.60, 0.60, 0.20)` |
| | `actuation` | Vàng hổ phách (Amber) | `#E6B826` | `(0.90, 0.72, 0.15)` |
| **Mô hình** | `modeling_methods` | Tím hoa cà (Violet Purple) | `#A666E0` | `(0.65, 0.40, 0.88)` |
| | `constitutive_assumptions` | Tím phong lan (Plum/Magenta) | `#D152D1` | `(0.82, 0.32, 0.82)` |
| **Các biến** | `independent_variables` | Xanh lơ (Cyan) | `#26C7F2` | `(0.15, 0.78, 0.95)` |
| | `dependent_variables` | Xanh lam đậm (Dodger Blue) | `#2685F2` | `(0.15, 0.52, 0.95)` |
| | `control_variables` | Xanh mòng két (Teal) | `#1FB8A6` | `(0.12, 0.72, 0.65)` |
| **Thực nghiệm / Đánh giá** | `experimental_setup` | Xanh nõn chuối (Lime Green) | `#9ED92E` | `(0.62, 0.85, 0.18)` |
| | `performance_metrics` | Xanh bạc hà (Mint Green) | `#2ED17A` | `(0.18, 0.82, 0.48)` |
| | `main_results` | Xanh lá cây đậm (Emerald Green) | `#26BF40` | `(0.15, 0.75, 0.25)` |
| **Bằng chứng liên quan** | `evidence_relevant_to_topic` | Xanh hoàng gia (Royal Blue) | `#4D73E6` | `(0.30, 0.45, 0.90)` |
| **Giới hạn** | `limitations_stated_by_authors` | Cá hồi (Salmon Coral) | `#F27359` | `(0.95, 0.45, 0.35)` |
| | `limitations_inferred` | Hồng cánh sen (Rose Pink) | `#F27AAE` | `(0.95, 0.48, 0.68)` |
| **Hướng tiếp theo** | `future_work` | Tím hồng tươi (Fuchsia) | `#D938BF` | `(0.85, 0.22, 0.75)` |
| | `possible_gap_implications` | Nâu gạch (Rust Orange) | `#C7612E` | `(0.78, 0.38, 0.18)` |

---

## 4. Kiểm Tra Tính Toàn Vẹn & Khả Năng Sử Dụng

1. **Số lượng file**: Đủ 27 file `*_annotated.pdf` được tạo trong [`data/final/MP1/annotated/`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/).
2. **Kích thước file**: Tất cả các file đều không rỗng, dung lượng từ $1.1\text{ MB}$ đến $42\text{ MB}$ (tương ứng kích thước bản gốc + annotations).
3. **Tính năng tra cứu**:
   * Mở file bằng bất kỳ trình đọc PDF nào (Adobe Acrobat, Foxit Reader, trình duyệt web Chrome/Edge).
   * Dùng thanh Bookmark bên trái để nhảy nhanh theo từng mục.
   * Rê chuột hoặc bấm vào vệt màu để đọc popup nội dung trích xuất tương ứng.
