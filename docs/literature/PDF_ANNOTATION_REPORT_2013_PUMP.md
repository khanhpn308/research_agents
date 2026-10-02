# Báo Cáo Highlight và Đối Soát Bằng Chứng PDF theo Schema Trích Xuất

**Bài báo thử nghiệm**: *A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump* (IEEE/ASME TMech, 2013)  
**Mã tài liệu (Paper ID)**: `de64029540` | **DOI**: `10.1109/TMECH.2012.2211032`  
**File gốc PDF**: [`data/final/MP1/08_current_reports/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/08_current_reports/2013-A%20Biologically%20Inspired%20Wet%20Shape%20Memory%20Alloy%20Actuated%20Robotic%20Pump.pdf)  
**File JSON trích xuất**: [`data/final/MP1/08_current_reports/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/08_current_reports/2013-A%20Biologically%20Inspired%20Wet%20Shape%20Memory%20Alloy%20Actuated%20Robotic%20Pump_de64029540.json)  
**File PDF đã highlight (Annotated)**: [`data/final/MP1/annotated/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_annotated.pdf`](file:///home/khanh/projects/mechanical-research-agents/data/final/MP1/annotated/2013-A%20Biologically%20Inspired%20Wet%20Shape%20Memory%20Alloy%20Actuated%20Robotic%20Pump_annotated.pdf)  
**Script thực thi tái lập**: [`scripts/annotate_paper_pdf.py`](file:///home/khanh/projects/mechanical-research-agents/scripts/annotate_paper_pdf.py)

---

## 1. Nguyên Tắc Phân Loại và Bảng Mã Màu (Color Palette)

Theo yêu cầu, **nhóm "Thư mục"** (`title`, `authors`, `year`, `doi`) được **bỏ qua**.  
Trường `confidence` là chỉ số tin cậy trích xuất của mô hình ("high"), không phải văn bản trong bài báo nên được ghi chú trong phần metadata.

Tất cả các trường nội dung còn lại đều được gán một **mã màu highlight độc lập**, có độ tương phản cao, dễ đọc trên nền chữ in 2 cột của chuẩn IEEE:

| STT | Nhóm | Tên trường (Field) | Màu hiển thị | Mã RGB / Hex | Số vị trí highlight | Trang xuất hiện |
|:---:|---|---|:---:|:---:|:---:|:---:|
| 1 | Câu hỏi nghiên cứu | `research_problem` | Đỏ san hô (Coral Red) | `(0.95, 0.35, 0.35)` / `#F25959` | 5 | P.1, P.2 |
| 2 | Câu hỏi nghiên cứu | `research_objective` | Cam tươi (Bright Orange) | `(1.00, 0.55, 0.10)` / `#FF8C1A` | 3 | P.1, P.2 |
| 3 | Hệ thống/cơ chế | `robot_type` | Vàng nghệ (Gold Yellow) | `(1.00, 0.88, 0.10)` / `#FFE01A` | 1 | P.1 |
| 4 | Hệ thống/cơ chế | `stiffness_mechanism` | Xanh ô liu (Olive) | `(0.60, 0.60, 0.20)` / `#999933` | 0 *(Rỗng)* | — |
| 5 | Hệ thống/cơ chế | `actuation` | Vàng hổ phách (Amber) | `(0.90, 0.72, 0.15)` / `#E6B826` | 3 | P.3, P.5 |
| 6 | Mô hình | `modeling_methods` | Tím hoa cà (Violet Purple) | `(0.65, 0.40, 0.88)` / `#A666E0` | 5 | P.5, P.6 |
| 7 | Mô hình | `constitutive_assumptions` | Tím phong lan (Plum/Magenta) | `(0.82, 0.32, 0.82)` / `#D152D1` | 5 | P.4, P.6 |
| 8 | Các biến | `independent_variables` | Xanh lơ (Cyan) | `(0.15, 0.78, 0.95)` / `#26C7F2` | 5 | P.3, P.7, P.8, P.10 |
| 9 | Các biến | `dependent_variables` | Xanh lam đậm (Dodger Blue) | `(0.15, 0.52, 0.95)` / `#2685F2` | 6 | P.1, P.3, P.6, P.10 |
| 10 | Các biến | `control_variables` | Xanh mòng két (Teal) | `(0.12, 0.72, 0.65)` / `#1FB8A6` | 5 | P.7, P.8 |
| 11 | Thực nghiệm/đánh giá | `experimental_setup` | Xanh nõn chuối (Lime Green) | `(0.62, 0.85, 0.18)` / `#9ED92E` | 6 | P.8, P.9 |
| 12 | Thực nghiệm/đánh giá | `performance_metrics` | Xanh bạc hà (Mint Green) | `(0.18, 0.82, 0.48)` / `#2ED17A` | 7 | P.2, P.4, P.7, P.8, P.9 |
| 13 | Thực nghiệm/đánh giá | `main_results` | Xanh lá cây đậm (Emerald Green) | `(0.15, 0.75, 0.25)` / `#26BF40` | 7 | P.1, P.9, P.10 |
| 14 | Bằng chứng liên quan | `evidence_relevant_to_topic` | Xanh hoàng gia (Royal Blue) | `(0.30, 0.45, 0.90)` / `#4D73E6` | 4 | P.1, P.2, P.4, P.9 |
| 15 | Giới hạn | `limitations_stated_by_authors` | Cá hồi (Salmon Coral) | `(0.95, 0.45, 0.35)` / `#F27359` | 6 | P.4, P.7, P.8, P.9, P.10 |
| 16 | Giới hạn | `limitations_inferred` | Hồng cánh sen (Rose Pink) | `(0.95, 0.48, 0.68)` / `#F27AAE` | 3 | P.8, P.9 |
| 17 | Hướng tiếp theo | `future_work` | Tím hồng tươi (Fuchsia) | `(0.85, 0.22, 0.75)` / `#D938BF` | 3 | P.10 |
| 18 | Hướng tiếp theo | `possible_gap_implications` | Nâu gạch (Rust Orange) | `(0.78, 0.38, 0.18)` / `#C7612E` | 3 | P.5, P.10 |

**Tổng cộng**: **77 vị trí highlight chuẩn xác** trên toàn bộ 11 trang của tài liệu.

---

## 2. Chi Tiết Đối Soát Bằng Chứng Từng Trường Trong Bài Báo

### 2.1. Nhóm: Câu hỏi nghiên cứu
* **`research_problem`** *(Đỏ san hô)*:
  * **Trang 1, Cột 2**: Giới hạn băng thông và tốc độ làm nguội chậm của SMA truyền thống (*"SMAs are commonly used for applications that do not require high reciprocation rates due to their limited bandwidth..."*).
  * **Trang 2, Cột 1**: Hạn chế của thiết kế trước đây từ Ertel & Mascaro [11], [12] khi hiệu suất đầu ra không đủ để tự duy trì cơ cấu (*"output performance was not sufficient to sustain the actuation of its own wet SMA actuators"*).
  * **Trang 2, Cột 1**: Điều kiện cần để tự duy trì và cấp tải ngoài: tỷ số $Q_{out} / Q_{in} > 1.0$ (*"amount of fluid output of the pump must be greater than the amount of fluid input required..."*).
  * **Trang 2, Cột 1**: Các vi bơm (micropumps) hiện hành chỉ bơm được lưu lượng cỡ $\mu\text{L/min}$, không đủ để lái robot vĩ mô cỡ $\text{mL/min}$ (*"high net volume outputs on the order of mL/min are necessary"*).
* **`research_objective`** *(Cam tươi)*:
  * **Trang 1, Abstract**: Khái niệm, thiết kế, tối ưu hóa và phân tích thực nghiệm bơm robot dẫn động bằng hợp kim nhớ hình ướt (wet SMA) lấy cảm hứng sinh học (*"presents the concept, design, optimization, and experimental analysis of a biologically inspired wet shape memory alloy (SMA) actuated pump..."*).
  * **Trang 1, Abstract**: Cơ chế tương tự tim người: phân phối năng lượng nhiệt thủy lực cho các cơ bắp nhân tạo đồng thời trích một phần lưu lượng để tự nuôi chính nó.
  * **Trang 2, Cột 1-2**: Mục tiêu chứng minh bơm hoạt động tự nuôi với lưu lượng dương thực tế vượt trội nhiều bậc so với các bơm SMA trước đó.

### 2.2. Nhóm: Hệ thống / Cơ chế
* **`robot_type`** *(Vàng nghệ)*:
  * **Trang 1**: Định danh cơ cấu: *"biologically inspired wet shape memory alloy (SMA) actuated pump"*.
* **`actuation`** *(Vàng hổ phách)*:
  * **Trang 1 & 3**: Dẫn động nhiệt thủy lực đối lưu cưỡng bức qua ống mềm bọc dây SMA (*"forced convection by using both thermofluidic heating and cooling"*).
  * **Trang 3**: Gia nhiệt liên tục cho chất lỏng trong bình tích áp bằng cuộn điện trở hoặc phản ứng hóa học.
  * **Trang 3 & 6**: Gia nhiệt bổ trợ bằng hiệu ứng Joule trực tiếp trên dây SMA (*"Supplementary Joule heating may also be used in the wet SMA actuators themselves"*).

### 2.3. Nhóm: Mô hình
* **`modeling_methods`** *(Tím hoa cà)*:
  * **Trang 5**: Mô hình động lực học hệ thống dựa trên đồ thị liên kết năng lượng (energy bond graphs) và không gian trạng thái (state-space).
  * **Trang 5**: Phân đoạn cơ cấu chấp hành wet SMA thành 20 phân đoạn rời rạc (*"20 segments used in the actual model"*).
  * **Trang 5-6**: Mô hình vi phân từ trễ (differential hysteresis) dựa trên phân phối chuẩn tích lũy (cumulative normal distribution).
  * **Trang 6**: Quan hệ ứng suất - biến dạng tuyến tính từng đoạn (piecewise linear stress-strain) cho các pha mactenxit và austenit.
  * **Trang 6**: Các phương trình trạng thái thông số tập trung (lumped-parameter) mô tả áp suất buồng bơm pít-tông.
* **`constitutive_assumptions`** *(Tím phong lan)*:
  * **Trang 4**: Giả định co rút hoàn toàn và không có thất thoát thể tích trong buồng bơm (*"assuming full contraction and no volumetric loss within the pumping chambers"*).
  * **Trang 4-5**: Giả định không thất thoát nhiệt ra môi trường và không hòa trộn chất lỏng nóng-lạnh trong tính toán hiệu suất nhiệt động cực đại 3.4%.
  * **Trang 6**: Trở kháng thủy lực của van một chiều tiến tới vô cùng đối với dòng chảy ngược (*"values of these fluidic resistances approach infinity against check valves"*).
  * **Trang 6**: Lực cản nhớt tuyến tính $R$ trong phương trình tốc độ biến dạng dây SMA.

### 2.4. Nhóm: Các biến & Thực nghiệm
* **`independent_variables`** *(Xanh lơ)*:
  * Chiều dài cơ cấu (20 cm đến 45 cm, tối ưu 40 cm), cánh tay đòn cơ học (mechanical advantage $M = 0.84$), thời gian dòng chảy (1.0 s đến 5.0 s), thời gian trễ gia nhiệt Joule (lead time 0 đến 1.0 s), trạng thái cấp nhiệt bình tích áp (có/không cấp nhiệt liên tục), áp suất tích áp (15 kPa).
* **`dependent_variables`** *(Xanh lam đậm)*:
  * Tỷ số thể tích đầu ra/đầu vào ($Q_{out} / Q_{in}$), lưu lượng dòng chảy ròng ($\text{mL/min}$), áp suất buồng bơm, vị trí và vận tốc pít-tông, nhiệt độ các thành phần theo chiều dài dây.
* **`control_variables`** *(Xanh mòng két)*:
  * Đường kính dây SMA ($0.38\text{ mm}$), đường kính trong ống mềm ($2.4\text{ mm}$), chất lỏng làm việc (nước), nhiệt độ phòng ($22^\circ\text{C}$), dòng điện Joule ($4.5\text{ A}$), thời gian xung điện ($1.0\text{ s}$), thời gian dừng dòng chất lỏng ($2.0\text{ s}$).
* **`experimental_setup`** *(Xanh nõn chuối)*:
  * Hai cơ cấu wet SMA đối kháng nối qua đòn bẩy tới 2 buồng bơm màng chuyển vị dương.
  * Bình tích áp nóng và lạnh phân phối dòng áp suất $15\text{ kPa}$.
  * Thanh gia nhiệt nhúng điện trở trong bình tích áp nóng.
  * Hệ 4 van điện từ (2 van routing đầu vào, 2 van tách dòng đầu ra).
  * 2 nguồn cấp điện một chiều bên ngoài cấp xung Joule.
  * Thử nghiệm thực tế tại độ cao xấp xỉ $1400\text{ m}$ (nhiệt độ sôi của nước $\approx 88^\circ\text{C}$).

### 2.5. Nhóm: Kết quả chính & Đánh giá
* **`main_results`** *(Xanh lá cây đậm)*:
  * Đạt tỷ số $Q_{out}/Q_{in} = 0.88$ với chế độ thuần thủy lực cơ bản, tăng lên $1.35$ khi cấp nhiệt liên tục cho bình tích áp.
  * Đạt tỷ số $Q_{out}/Q_{in} = 2.1$ và lưu lượng dòng chảy ròng $66\text{ mL/min}$ khi kết hợp xung điện Joule $4.5\text{ A}$ trong $1\text{ s}$.
  * Lưu lượng thực nghiệm $66\text{ mL/min}$ lớn hơn 2 bậc độ lớn (gấp hơn 100 lần) so với các vi bơm SMA trước đó.
  * Mô phỏng động lực học khớp với thực nghiệm trong phạm vi sai số từ $5\%$ đến $10\%$.
* **`limitations_stated_by_authors`** *(Cá hồi)*:
  * Hiệu suất nhiệt động cực đại theo lý thuyết chỉ đạt $3.4\%$; hiệu suất thực tế thấp hơn nhiều do tổn thất môi trường và hòa trộn chất lỏng.
  * Thấp hơn đáng kể so với bơm dẫn động bằng động cơ điện thông thường.
  * Dòng điện Joule kéo dài gây biến dạng dẻo vĩnh viễn trên dây Nitinol nên phải giới hạn xung dưới $1\text{ s}$.
* **`limitations_inferred`** *(Hồng cánh sen)*:
  * Cơ cấu phụ thuộc nguồn điện ngoài để điều khiển 4 van solenoid và xung Joule, chưa thể vận hành độc lập (untethered).
  * Chu trình hở khiến nhiệt độ sôi thay đổi theo cao độ khí quyển ($1400\text{ m}$).
  * Hiện tượng mỏi cơ nhiệt (fatigue life) chưa được đánh giá qua chu kỳ dài hạn.
* **`future_work` & `possible_gap_implications`** *(Tím hồng & Nâu gạch)*:
  * Thu nhỏ thể tích bao gói bơm mà không cản trở hành trình co rút của SMA.
  * Loại bỏ điện phụ trợ bằng cách chuyển sang cơ cấu van định thời cơ khí và gia nhiệt thuần bằng phản ứng hóa học năng lượng cao (ví dụ: propane với mật độ năng lượng $46\text{ MJ/kg}$ so với pin Li-ion $0.46\text{ MJ/kg}$).

---

## 3. Các Tính Năng Tương Tác Được Tích Hợp Trên File PDF

1. **Hiển thị Popup Tooltip khi rê chuột hoặc nhấp vào vùng Highlight**:
   * Mỗi vùng highlight mang đầy đủ thông tin: Tên trường, Nhóm trường, và nội dung trích xuất tương ứng từ file JSON.
2. **Khung Mục Lục Bookmark (PDF Outlines / TOC)**:
   * Thanh sidebar bên trái của PDF viewer (Adobe Acrobat, Foxit Reader, Chrome, Firefox, v.v.) hiển thị cây thư mục được chia theo 8 nhóm và 17 trường.
   * Nhấp vào tên trường sẽ tự động nhảy (jump) trực tiếp đến đúng trang và vị trí của đoạn highlight đó.
3. **Bảo toàn số trang gốc (Page 1 đến Page 11)**:
   * Giữ nguyên số trang và bố cục gốc của bài báo để không làm sai lệch số trang trích dẫn học thuật.

---

## 4. Hướng Dẫn Chạy Cho Các Cặp File Khác Trong `data/final/MP1`

Script [`scripts/annotate_paper_pdf.py`](file:///home/khanh/projects/mechanical-research-agents/scripts/annotate_paper_pdf.py) có thể được chạy trực tiếp bằng dòng lệnh:

```bash
# Cú pháp chạy cho 1 cặp file bất kỳ:
.venv/bin/python scripts/annotate_paper_pdf.py \
  --pdf "data/final/MP1/08_current_reports/TEN_FILE.pdf" \
  --json "data/final/MP1/08_current_reports/TEN_FILE_hash.json" \
  --output "data/final/MP1/annotated/TEN_FILE_annotated.pdf"
```

Tất cả các bản sao gốc trong `data/final/MP1/` được giữ nguyên vẹn tuyệt đối (tuân thủ quy định bảo toàn hash SHA256 của kho lưu trữ nghiên cứu).
