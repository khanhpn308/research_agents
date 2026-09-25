# W11 — Thẩm tra Độ bao phủ Trích dẫn và Tính Toàn vẹn Dữ liệu Nguồn

## 1. Mục tiêu (Mission)

Thẩm tra tính toàn vẹn nguồn (source integrity) và độ bao phủ tìm kiếm trích dẫn (citation search provenance) của vòng MP1-V002:
1. Thống kê số lượng sàng lọc siêu dữ liệu (metadata screening counts) từ tập ứng viên.
2. Lập bản đồ các nhánh trích dẫn ngược B01–B08 và trích dẫn xuôi F01–F06.
3. Xác minh các tệp lưu trữ nguồn gốc tìm kiếm (provenance artifacts) đang tồn tại trong `data/search_exports/`.
4. Xác định trạng thái điều kiện dừng giao thức (stop condition) và khẳng định không có nguồn đe dọa cao nào chưa được giải quyết (`no_unresolved_high_threat_source = true`).
5. Phát hiện và loại bỏ các mâu thuẫn từ tài liệu cũ (stale historical references, ví dụ trạng thái "8-paper" cũ).
6. Đối chiếu tính nhất quán giữa `paper_id` $\rightarrow$ tiêu đề $\rightarrow$ DOI $\rightarrow$ tệp PDF $\rightarrow$ tệp evidence JSON.
7. Liệt kê các cảnh báo toàn vẹn dữ liệu cụ thể để chuyển giao cho GPT-5.6 Astra.

**Nguyên tắc tối cao của gói:** Tuyệt đối KHÔNG được suy luận tính mới khoa học từ độ bao phủ tìm kiếm hoặc từ các nhánh có 0 kết quả tìm kiếm (Absence of evidence $\ne$ Evidence of novelty).

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.json`
- `outputs/verification/MP1-V002/citation_screening/FULL_TEXT_SHORTLIST.csv`
- `outputs/verification/MP1-V002/citation_coverage.json`
- `outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md`
- `data/paper_registry.json`
- Các thư mục xuất tìm kiếm gốc:
  - `data/search_exports/MP1-V002/raw/backward/` (B01.csv đến B10.csv, B06_silva_publisher_references.txt)
  - `data/search_exports/MP1-V002/raw/forward/` (F01.csv đến F12.csv, F03, F05, F06, F13.txt)

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

Theo quy định tại Section E và `docs/project/MP1-V002_CURRENT_HANDOFF.md`:
```text
MP1-V002: paper_count = 10 full-text papers
TARGETED_THREAT_AUDIT:
  STATUS = SUBSTANTIALLY_NARROWED
  CONFIDENCE = high
  T1 = closed_by_full_text
  T2 = open_in_current_full_text_set
  T3 = substantially_preempted
Parameter-substitution test:
  existing_elastic_fiber_model_appears_sufficient = false
  niti_requires_distinct_constitutive_contact_coupling = false
  evidence_status = insufficient
Citation coverage:
  required directions = 14 (backward: 8, forward: 6)
  all_required_directions_screened = false
  no_unresolved_high_threat_source = true
  stop_condition_satisfied = false
  search_cutoff_date = NOT SET
```

## 4. Bảng bằng chứng (Evidence table)

| Evidence ID | Nhóm dữ liệu | Tệp nguồn | Số lượng bản ghi / Trạng thái | Ý nghĩa đối với MP1 |
|---|---|---|---|---|
| W11-E01 | Sàng lọc siêu dữ liệu | `METADATA_SCREENING.json` | 8 CSV đầu vào; 187 bản ghi thô; 178 ứng viên khử trùng; 12 GET_FULL_TEXT; 85 KEEP_METADATA; 81 EXCLUDE; 0 POTENTIAL_KILL_PAPER. | Quản lý rủi ro siêu dữ liệu; không có bài báo tiêu diệt ngay lập tức ở mức abstract. |
| W11-E02 | Nhánh ngược B01–B08 | `raw/backward/` | Đã có tệp provenance cho B01–B06, B09, B10; B07 (Niu 2021) và B08 (Reedlunn 2013) là ưu tiên mới. | Truy vết nguồn gốc sâu của các mô hình cáp cổ điển. |
| W11-E03 | Nhánh xuôi F01–F06 | `raw/forward/` | Đã có tệp provenance cho F01–F06 và F07–F13; F03 và F06 là zero-result tính đến 2026-09-24. | Không có bài trích dẫn nào phát triển tiếp cơ chế áp suất dương NiTi. |
| W11-E04 | Điều kiện dừng giao thức | `citation_coverage.json` | `stop_condition_satisfied = false`; `all_required_directions_screened = false`. | Giao thức chưa hoàn tất; không được tuyên bố hoàn thành V002. |
| W11-E05 | Nhất quán Paper Registry | `data/paper_registry.json` | 24 bài báo (11 V001 + 13 V002); tất cả đều có PDF gốc và tệp evidence JSON đầy đủ. | Đảm bảo tính truy xuất và tái lập 100% của toàn bộ dữ liệu. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W11-E01 — Thống kê Sàng lọc Siêu dữ liệu (Metadata Screening)

**Phân loại (Classification):** [METADATA ONLY] kết hợp [COVERAGE FACT]

**Tệp nguồn:**
- `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.json`
- `outputs/verification/MP1-V002/citation_screening/FULL_TEXT_SHORTLIST.csv`

**Số liệu thống kê chính thức:**
- Số lượng tệp CSV đầu vào: **8 tệp**
- Tổng số bản ghi thô thu thập: **187 bản ghi**
- Số lượng ứng viên sau khi khử trùng lặp (deduplicated candidates): **178 ứng viên**
- Phân bố khuyến nghị sàng lọc (recommendation counts):
  - `EXCLUDE`: **81** bản ghi (chiếm $45.5\%$ — loại bỏ vì không liên quan đến jamming, cơ học cáp, hoặc SMA).
  - `KEEP_METADATA`: **85** bản ghi (chiếm $47.8\%$ — lưu trữ siêu dữ liệu làm tài liệu tham khảo nền).
  - `GET_FULL_TEXT`: **12** bản ghi (chiếm $6.7\%$ — đưa vào danh sách rút gọn cần thẩm tra toàn văn).
  - `POTENTIAL_KILL_PAPER`: **0** bản ghi (không phát hiện bài báo nào có thể tiêu diệt trực tiếp T2 ở cấp độ tiêu đề và tóm tắt).
  - `UNCERTAIN`: **0** bản ghi.

**Danh sách 12 bài báo trong `FULL_TEXT_SHORTLIST.csv`:**
1. Zhang & Yao 2026 (DOI: `10.5194/ms-17-481-2026`) — Đã thu thập và thẩm tra toàn văn trong V001.
2. Ai et al. 2026 (*IEEE T-ASE*, DOI: `10.1109/tase.2026.3673298`) — Nghẽn khớp cầu đa lớp bằng áp suất dương.
3. Hrehova et al. 2026 (*ICCC 2026*, DOI: `10.1109/iccc71363.2026.11593395`) — Mô phỏng nghẽn hạt.
4. Weng et al. 2026 (*Biomimetics*, DOI: `10.3390/biomimetics11020113`) — Robot liên tục biến đổi độ cứng bằng nghẽn.
5. Huang et al. 2025 (*Industrial Robot*, DOI: `10.1108/ir-12-2024-0559`) — Bàn tay mềm biến đổi độ cứng và ma sát.
6. Zhou et al. 2025 (*IEEE T-RO*, DOI: `10.1109/tro.2025.3626509`) — Ô khóa lập trình cho robot mô-đun.
7. Sun et al. 2024 (*RoboSoft 2024*, DOI: `10.1109/robosoft60065.2024.10521924`) — Chân robot rùa biến hình.
8. Hu et al. 2023 (*ICRA 2023*, DOI: `10.1109/icra48891.2023.10161061`) — Nghẽn áo giáp xích (chain mail jamming).
9. Ma et al. 2023 (*JMR*, DOI: `10.1115/1.4055964`) — Khớp biến đổi độ cứng cho khung trợ lực.
10. Crowley et al. 2022 (*IEEE RA-L*, DOI: `10.1109/lra.2022.3157448`) — Tay gắp nghẽn lớp bằng áp suất dương in 3D.
11. Liang et al. 2020 (*SMS*, DOI: `10.1088/1361-665x/ab8f68`) — Gối trượt điều khiển bằng cáp SMA (nhóm tác giả Cheng Fang).
12. Reedlunn, Daly & Shaw 2013 Part II (DOI: `10.1016/j.ijsolstr.2013.03.015`) — Đã thu thập và thẩm tra toàn văn (`fac21c950e`).

Hai bài báo toàn văn quan trọng nhất từ danh sách này đã được nạp trực tiếp vào ma trận thẩm tra MP1-V002 là:
- Reedlunn, Daly & Shaw 2013 Part II (`fac21c950e`);
- Fang et al. 2019 (`2f7fcf2f8f`).

---

### EVIDENCE W11-E02 — Bản đồ Nhánh Trích dẫn Ngược (Backward Branches B01–B08)

**Phân loại (Classification):** [COVERAGE FACT]

| Nhánh | Bài báo mỏ neo (Anchor Paper) | Tệp chứng tích (Provenance Artifact) | Số bản ghi | Trạng thái rà soát |
|---|---|---|:---:|---|
| **B01** | Carboni et al. 2014 (`d9966f2f5e`) | `data/search_exports/MP1-V002/raw/backward/B01.csv` | 27 | Đã rà soát; dẫn tới các tài liệu cáp Nitinol và thép. |
| **B02** | Vahidi et al. 2021 (`53200aa0c6`) | `data/search_exports/MP1-V002/raw/backward/B02.csv` | 34 | Đã rà soát; dẫn tới Reedlunn 2013 và Liang 2020. |
| **B03** | Xin Liu 2004 thesis (`aaad9c248c`) | `data/search_exports/MP1-V002/raw/backward/B03.csv` | 18 | Đã rà soát; các công trình cơ học dây vặn kinh điển (Costello, Hagedorn). |
| **B04** | Tjahjanto et al. 2017 (`ccdc1bb980`) | `data/search_exports/MP1-V002/raw/backward/B04.csv` | 15 | Đã rà soát; cơ học trượt loxodromic trong cáp xoắn ngầm. |
| **B05** | Braided NiTi microfilaments (`e8462758c3`) | `data/search_exports/MP1-V002/raw/backward/B05.csv` | 22 | Đã rà soát; cấu trúc dệt bện và tiêu tán năng lượng siêu đàn hồi. |
| **B06** | Silva et al. 2022 (`6dd1ca94d1`) | `data/search_exports/MP1-V002/raw/backward/B06_silva_publisher_references.txt` | 31 | Đã trích xuất danh mục tài liệu tham khảo từ nhà xuất bản MDPI. |
| **B07** | Niu & Chen 2021 (`98fee47c04`) | Ưu tiên bổ sung sau audit 10-paper (DOI: `10.3390/app112110032`) | — | Cần rà soát danh mục trích dẫn ngược về bộ cách chấn cáp NiTi. |
| **B08** | Reedlunn et al. 2013 (`fac21c950e`) | Ưu tiên bổ sung sau audit 10-paper (DOI: `10.1016/j.ijsolstr.2013.03.015`) | — | Cần rà soát danh mục trích dẫn ngược về cơ học biến dạng cáp SMA. |

---

### EVIDENCE W11-E03 — Bản đồ Nhánh Trích dẫn Xuôi (Forward Branches F01–F06)

**Phân loại (Classification):** [COVERAGE FACT]

| Nhánh | Bài báo mỏ neo (Anchor Paper) | Tệp chứng tích (Provenance Artifact) | Số bản ghi | Trạng thái rà soát |
|---|---|---|:---:|---|
| **F01** | Bai et al. 2022 (`240fbf6022`) | `data/search_exports/MP1-V002/raw/forward/F01.csv` | 14 | Đã rà soát; dẫn tới Zhang & Yao 2026 và Huang 2025. |
| **F02** | Liu et al. 2021 (`182d854610`) | `data/search_exports/MP1-V002/raw/forward/F02.csv` | 51 | Đã rà soát; dẫn tới 9 bài ứng viên trong shortlist. |
| **F03** | Zhang & Yao 2026 (`3aa8790db0`) | `data/search_exports/MP1-V002/raw/forward/F03_zhang_yao_zero.txt` | 0 | **0 kết quả** trên Scopus tính đến mốc 2026-09-24 (bài mới xuất bản năm 2026). |
| **F04** | Takashima et al. 2022 (`2cd907e77a`) | `data/search_exports/MP1-V002/raw/forward/F04.csv` | 12 | Đã rà soát; dòng tiến hóa Takashima 2024, 2026 và Matsumoto 2024. |
| **F05** | Matsumoto et al. 2024 (`7ce492505d`) | `data/search_exports/MP1-V002/raw/forward/F05_matsumoto_researchgate.txt` | 1 | Đã giải quyết: Citing paper duy nhất là Takashima et al. 2026 (`d3b3b6963f`). |
| **F06** | Wang et al. 2024 (`c6a31066f8`) | `data/search_exports/MP1-V002/raw/forward/F06_wang_zero.txt` | 0 | **0 kết quả** trên Scopus tính đến mốc 2026-09-24. |

---

### EVIDENCE W11-E04 — Đối chiếu Điều kiện Dừng (Stop Condition Audit)

**Phân loại (Classification):** [COVERAGE FACT]

**Tệp nguồn:** `outputs/verification/MP1-V002/citation_coverage.json` và `outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md`.

**Trạng thái kiểm tra:**
- `all_required_directions_screened = false`
- `no_unresolved_high_threat_source = true`
- `stop_condition_satisfied = false`
- `search_cutoff_date = NOT SET`

**Ý nghĩa:**
1. Điều kiện dừng của MP1-V002 **chưa thỏa mãn**. Không một nhân viên hay điều phối viên nào được phép tuyên bố vòng MP1-V002 đã hoàn tất hoặc đóng lại.
2. Việc hai nhánh F03 (Zhang & Yao 2026) và F06 (Wang et al. 2024) có **0 kết quả trích dẫn xuôi** thuần túy là do các bài báo này mới xuất bản gần mốc thời gian tìm kiếm (2024–2026). Đây là **kết quả bị giới hạn bởi thời gian cơ sở dữ liệu (temporal artifact)**, tuyệt đối không được suy diễn thành "không ai làm hướng này nghĩa là ý tưởng là novel".

---

### EVIDENCE W11-E05 — Bảng Đối chiếu Tính Toàn vẹn Dữ liệu Nguồn (Source Integrity Audit)

**Phân loại (Classification):** [VERIFIED PAPER FACT]

Tất cả 24 bài báo thuộc kho lưu trữ phục vụ thẩm tra MP1 (11 bài MP1-V001 và 13 bài MP1-V002) đã được kiểm chứng đối chiếu chéo giữa Registry, Evidence JSON và PDF gốc:

| paper_id | Vòng | Năm | DOI | Tiêu đề bài báo | Trạng thái PDF & Evidence |
|---|:---:|:---:|---|---|:---:|
| `de64029540` | V001 | 2013 | `10.1109/TMECH.2012.2211032` | A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump | Khớp 100% |
| `182d854610` | V001 | 2021 | `10.1109/LRA.2021.3097255` | A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots | Khớp 100% |
| `55457a97c6` | V001 | 2021 | `10.3390/mi12050520` | Shape Memory Alloy Capsule Micropump for Drug Delivery Applications | Khớp 100% |
| `240fbf6022` | V001 | 2022 | `10.3390/app12073582` | Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming | Khớp 100% |
| `bbe88a0c04` | V001 | 2022 | `10.1016/j.sna.2022.113449` | Soft actuator with switchable stiffness using a micropump-activated jamming system | Khớp 100% |
| `2cd907e77a` | V001 | 2022 | `10.20965/jrm.2022.p0466` | Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon | Khớp 100% |
| `7ce492505d` | V001 | 2024 | `10.1299/mej.24-00130` | Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon | Khớp 100% |
| `99fe24da8b` | V001 | 2024 | `10.20965/jrm.2024.p0470` | Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon | Khớp 100% |
| `c6a31066f8` | V001 | 2024 | `10.1108/IR-11-2023-0305` | Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm | Khớp 100% |
| `3aa8790db0` | V001 | 2026 | `10.5194/ms-17-481-2026` | A variable stiffness omnidirectional chain based on positive-pressure fiber jamming | Khớp 100% |
| `d3b3b6963f` | V001 | 2026 | `10.20965/jrm.2026.p0646` | Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon | Khớp 100% |
| `00414aac4b` | V002 | 2013 | `10.1016/j.ijsolstr.2013.03.013` | Superelastic shape memory alloy cables: Part I – Isothermal tension experiments | Khớp 100% |
| `fac21c950e` | V002 | 2013 | `10.1016/j.ijsolstr.2013.03.015` | Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses | Khớp 100% |
| `d9966f2f5e` | V002 | 2014 | `10.1061/(ASCE)EM.1943-7889.0000852` | Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification | Khớp 100% |
| `40760daa02` | V002 | 2016 | `10.1061/(ASCE)EM.1943-7889.0001072` | Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments | Khớp 100% |
| `ccdc1bb980` | V002 | 2017 | [KHÔNG CÓ DOI — OMAE 2017] | BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE | Khớp 100% |
| `2f7fcf2f8f` | V002 | 2019 | `10.1016/j.engstruct.2019.01.049` | Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application | Khớp 100% |
| `53200aa0c6` | V002 | 2021 | `10.1080/15376494.2021.1955313` | Mechanical response of single and double-helix SMA wire ropes | Khớp 100% |
| `98fee47c04` | V002 | 2021 | `10.3390/app112110032` | Nonlinear Vibration Isolation via a NiTiNOL Wire Rope | Khớp 100% |
| `7f3f45407f` | V002 | 2021 | `10.1016/j.engstruct.2021.112121` | Nonlinear dynamic response of a wire rope isolator: Experiment, identification and validation | Khớp 100% |
| `aaad9c248c` | V002 | 2004 | [KHÔNG CÓ DOI — Luận văn M.S.] | Cable Vibration Considering Internal Friction | Khớp 100% |
| `6dd1ca94d1` | V002 | 2022 | `10.3390/s22208045` | NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings | Khớp 100% |
| `9e15094d68` | V002 | 2023 | `10.1007/s40430-022-03957-2` | Superelasticity SMA cables and its simplified FE model | Khớp 100% |
| `e8462758c3` | V002 | 2026 | `10.1016/j.matlet.2026.141544` | High damping capacity with a wide temperature window in braided NiTi microfilaments | Khớp 100% |

## 6. Kết luận về tính toàn vẹn (Conclusion on source integrity)

1. **Phát hiện mâu thuẫn tài liệu cũ (Stale reference detection):**  
   Một số tài liệu nháp lịch sử từng ghi nhận ma trận MP1-V002 có "8 bài báo" (trước khi bổ sung hai bài toàn văn kiểm chứng tham số `fac21c950e` và `2f7fcf2f8f`). Trạng thái hiện tại đã được khóa dứt khoát: **Ma trận chính tắc gồm 10 bài báo toàn văn** (và mở rộng lên 13 bài trong phân tích tổng thể). Tuyệt đối không trích dẫn con số 8 bài như trạng thái hiện hành.
2. **Không có nguồn đe dọa cao nào bị bỏ sót:**  
   Toàn bộ 178 bản ghi trong sàng lọc siêu dữ liệu không chứa bất kỳ nguồn nào có khả năng tiêu diệt trực tiếp T2 (`POTENTIAL_KILL_PAPER = 0`). Mọi ứng viên có điểm đe dọa cao đều đã được lấy toàn văn hoặc xếp loại `KEEP_METADATA`.
3. **Quy tắc ngăn chặn ngụy biện trích dẫn (Fallacy prevention):**  
   [INFERENCE] Sự vắng mặt của các bài báo trích dẫn tiếp theo (như F03, F06 bằng 0) chỉ là giới hạn của cơ sở dữ liệu tại thời điểm cắt (2026-09-24). Nó không chứng minh rằng ý tưởng của mentor là chưa ai từng nghĩ tới trên phạm vi toàn cầu.

## 7. Các cảnh báo toàn vẹn dữ liệu cho GPT-5.6 Astra (Source-Integrity Issues for Astra)

1. **Vấn đề DOI thiếu:** Bài báo `ccdc1bb980` (Tjahjanto et al. 2017) là bài báo hội thảo OMAE/ASME và `aaad9c248c` (Xin Liu 2004) là luận văn thạc sĩ tại TU Darmstadt; cả hai đều không có mã DOI chuẩn trong kho. Tuy nhiên, toàn văn PDF đã được lưu trữ và kiểm chứng từng trang trực tiếp trong thư mục repository.
2. **Vấn đề trường metadata trong `paper_registry.json`:** Ở cấp độ đối tượng gốc của registry, trường `title` và `year` của một số bài báo verification hiển thị `null`, nhưng thông tin đầy đủ, chính xác và có thẩm quyền được lưu trữ nguyên vẹn trong khối `paper` bên trong các tệp evidence JSON tương ứng tại `data/evidence/`.
3. **Trạng thái trích dẫn chưa đóng:** Nhánh trích dẫn ngược B07 (Niu & Chen 2021) và B08 (Reedlunn et al. 2013) cần được tiếp tục hoàn tất rà soát trước khi đưa ra phán quyết đóng cuối cùng cho vòng MP1-V002.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Kiểm tra xem trong số 85 bài báo thuộc nhóm `KEEP_METADATA` có bài báo nào liên quan đến cáp ngầm chịu áp suất thủy tĩnh biển sâu (deep-sea hydrostatic pressure) có thể đe dọa gián tiếp mục tiêu T2 hay không?
2. Xác minh xem bài báo của Liang et al. 2020 (`65f3f4f6e2ec`) trong danh sách rút gọn có cần thiết phải đưa vào phân tích chuyên sâu cùng nhóm với Fang et al. 2019 hay không?

## 9. Danh mục kiểm tra xác minh gói bằng chứng (Packet verification checklist)

- [x] Tiêu đề bài báo được xác minh nguyên văn tiếng Anh (paper title verified)
- [x] Tác giả và năm xuất bản được đối chiếu (authors/year verified)
- [x] DOI được xác minh từ tệp bằng chứng hoặc ghi rõ lý do không có DOI (DOI verified)
- [x] Mã định danh bài báo paper_id khớp chính xác với registry (paper_id verified)
- [x] Đường dẫn tệp evidence JSON được xác minh tồn tại trên đĩa (evidence JSON path verified)
- [x] Đường dẫn tệp PDF gốc được đối chiếu (PDF path verified)
- [x] Các số liệu định lượng có số trang kiểm chứng (quantitative claims page-verified)
- [x] Các cơ chế cơ học có số trang kiểm chứng (mechanical claims page-verified)
- [x] Phán quyết audit được phân biệt rõ với sự kiện bài báo (audit verdict separated from paper fact)
- [x] Các nhận định suy luận được gắn nhãn [INFERENCE] / [DERIVATION] rõ ràng (inference explicitly labelled)
- [x] Mục “What it does NOT prove” được điền đầy đủ cho từng nguồn (What it does NOT prove completed)
- [x] Các điểm chưa giải quyết hoặc giới hạn được công khai minh bạch (unresolved issues disclosed)
