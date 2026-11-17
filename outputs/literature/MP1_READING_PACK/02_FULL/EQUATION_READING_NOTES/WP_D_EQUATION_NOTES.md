# MP1 READING PACK — WP-D EQUATION READING NOTES
## SMA Friction and Actuation

- **Task ID:** MP1-LR-P2-EQ-R1
- **Package:** WP-D (SMA Friction and Actuation)
- **Status:** VERIFIED_FULL_TEXT
- **Target Thesis Sections:** C1.2.1, C2.4, C2.4.2, C2.5, C2.5.4, C2.5.5

---

## 1. TỔNG QUAN VÀ PHÂN ĐỊNH BẢN CHẤT CƠ HỌC NHÓM WP-D

Nhóm phương trình WP-D tập trung vào nguyên lý sinh lực, sinh chuyển vị và điều khiển tiếp xúc ma sát thông qua cơ cấu chấp hành hợp kim nhớ hình (SMA Actuators & Springs):
- **M31 (Jeon et al., 2022):** Cơ cấu thay đổi độ cứng dạng dầm nhiều xương sống (multi-backbone) sử dụng lò xo SMA siết ngoài ống cao su, chuyển đổi công ngoại lực thành năng lượng đàn hồi và công tiêu tán ma sát trượt.
- **M32 (Nishida et al., 2022):** Cơ cấu khớp nối biến dạng và thay đổi độ cứng kết hợp vật liệu nhớ hình (SMP/SMA) và hiện tượng kẹt, thiết lập quan hệ độ cứng công xôn nhiều phần tử.
- **M33 (Pierce & Mascaro, 2012/2013):** Bơm robot dẫn động bằng dây SMA ướt, mô hình hóa phân số pha martensite theo hàm tích phân sai số Gaussian và phương trình vi phân tốc độ sinh lực nhiệt - cơ.
- **M34 (Shayganmanesh et al., 2021):** Bơm vi thể dùng lò xo xoắn SMA, thiết lập lực đàn hồi phi tuyến của lò xo SMA có xét đến góc nâng bước ốc và biến dạng chuyển pha khử song tinh (detwinning).

### Phân định khoa học then chốt:
1. **Lực lò xo SMA khác áp suất mẫu:** Lực kéo/nén của lò xo SMA ($F_M$ hoặc lực siết vòng) chỉ là nguồn sinh lực tập trung hoặc lực siết chu vi; để tạo thành áp suất giam phân bố đều ($p$) lên bó mẫu, cần qua một cơ cấu truyền lực (màng bọc đàn hồi, ống cao su hoặc buồng nén).
2. **Độ cứng uốn khác độ dốc đường cong lực - độ võng:** Trong M31, độ dốc đo được $F_{\text{ext}} / \delta$ chịu ảnh hưởng trực tiếp của công tiêu tán ma sát khô ($W_f = F_f s$). Việc quy đổi độ dốc này thành độ cứng uốn tương đương $EI = F_{\text{ext}} L^3 / (3\delta)$ là một **độ cứng vận hành biểu kiến (operational stiffness)**, không đồng nhất với mô đun đàn hồi thuần túy của vật liệu.

---

## 2. GHI CHÚ CHI TIẾT TỪNG PHƯƠNG TRÌNH ĐƯỢC CHỌN

---

### NOTE D-01: M31 Eqs. (1), (2.1)–(2.2) — Cân bằng công - năng lượng cho robot uốn mềm có ma sát kẹp SMA

#### A. Source Identity
- **Paper ID:** M31
- **Title:** Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism
- **Authors:** S. Jeon, A. W. Mahoney et al.
- **Year:** 2022
- **DOI:** 10.1109/LRA.2022.3178793
- **Evidence ID:** M31-E03
- **Equation Number:** Eqs. (1), (2.1), (2.2)
- **PDF Page:** 4
- **Printed Page:** 6585 (IEEE RA-L, 7(3): 6585–6592)
- **SHA-256:** `65d0979f31522c7eb16c52bb7fcda3a1e4a781f21508933b93f1cae5f5f403aa`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 4):

$$\int_0^\delta F_{\text{ext}} dx = U + F_f s$$

$$\int_0^\delta F_{\text{ext}, m} dx = U + F_{f, m} s = U_m$$

$$\int_0^\delta F_{\text{ext}, a} dx = U + F_{f, a} s = U_a$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $F_{\text{ext}}$ | Lực ngoài tác dụng vào đĩa đầu cuối robot | N | Lực ngang kéo đầu tự do của robot uốn cong | Tải trọng quasi-static, vận tốc kéo không đổi |
| $\delta$ | Độ võng ngang tại đầu cuối robot | m (mm) | Chuyển vị thẳng của đĩa đầu cuối | Đo tại vị trí đặt lực |
| $U$ | Thế năng đàn hồi tích lũy trong các thanh xương sống | J (N·m) | Năng lượng biến dạng uốn thuần túy không có ma sát | Các thanh đàn hồi tuyến tính |
| $F_f$ | Lực ma sát tổng cộng giữa các dây ngoại vi và ống cao su | N | Lực ma sát sinh ra do lực siết kẹp của lò xo SMA | Ma sát Coulomb trượt khô |
| $s$ | Tổng chiều dài trượt tích lũy của toàn bộ các dây | m (mm) | Tổng dịch chuyển trượt tương đối của các dây: $s = \sum \Delta l_{b, i}$ | Dây trượt trơn tru trong rãnh |
| $F_{\text{ext}, m}, F_{\text{ext}, a}$ | Lực ngoài ở trạng thái martensite và austenite của SMA | N | Lực kéo đo được tương ứng khi lò xo SMA nguội và nóng | Nhiệt độ kiểm soát ổn định |
| $F_{f, m}, F_{f, a}$ | Lực ma sát ở trạng thái martensite và austenite | N | $F_{f, a} > F_{f, m}$ do lò xo SMA ở pha austenite siết chặt hơn | Pha austenite có lực hồi phục lớn hơn |
| $U_m, U_a$ | Tổng công ngoại lực thực hiện trong pha martensite và austenite | J | Diện tích dưới đường cong lực - biến dạng $\int F dx$ | Tích phân công cơ học |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Thiết lập định luật bảo toàn công - năng lượng cho hệ robot uốn dẻo nhiều thanh có cơ cấu thay đổi độ cứng bằng ma sát siết ép bởi lò xo SMA.
2. **Liên hệ cơ học:**
   - Công do ngoại lực thực hiện $\int F_{\text{ext}} dx$ được phân chia thành hai phần: thế năng đàn hồi tích trữ trong các thanh kim loại ($U$) và công tiêu tán không phục hồi do ma sát trượt ($W_f = F_f s$).
   - Khi gia nhiệt lò xo SMA lên nhiệt độ austenite ($50-60^\circ\text{C}$), lực siết của lò xo tăng vọt, ép ống cao su chặt vào 8 dây ngoại vi, làm lực ma sát tăng từ $F_{f, m}$ lên $F_{f, a}$.
   - Kết quả là công ngoại lực cần thiết để làm dầm biến dạng cùng một độ võng $\delta$ tăng từ $U_m$ lên $U_a$, tạo nên hiệu ứng dầm "cứng hơn" khi chịu tải.
3. **Phân biệt khoa học then chốt:** Sự tăng độ cứng ở đây là **độ cứng biểu kiến do tiêu tán ma sát** (apparent stiffness via frictional dissipation), hoàn toàn không phải do vật liệu các thanh xương sống tăng mô đun đàn hồi $E$.

#### E. Relation to MP1
- **Khả năng áp dụng:** Rất liên quan trực tiếp về mặt nguyên lý năng lượng (Directly applicable energy formulation). MP1 sử dụng áp suất dương để ép bó dây TiNi; phương pháp phân tích công biến dạng đàn hồi cộng công ma sát $W = U + W_f$ có thể áp dụng nguyên vẹn để giải thích sự tăng trở lực uốn của MP1.

---

### NOTE D-02: M31 Eqs. (3)–(6) — Động học trượt dây ngoại vi và quan hệ hình học uốn dầm

#### A. Source Identity
- **Paper ID:** M31
- **Evidence ID:** M31-E04
- **Equation Number:** Eqs. (3), (4.1)–(4.5), (5), (6)
- **PDF Page:** 4
- **Printed Page:** 6585
- **SHA-256:** `65d0979f31522c7eb16c52bb7fcda3a1e4a781f21508933b93f1cae5f5f403aa`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 4):

$$s = \sum_{i=1}^8 \Delta l_{b, i}$$

$$\Delta l_{b, 1} = a_2 \theta, \quad \Delta l_{b, 2} = \Delta l_{b, 3} = a_1 \theta, \quad \Delta l_{b, 4} = \Delta l_{b, 5} = 0, \quad \Delta l_{b, 6} = \Delta l_{b, 7} = a_1 \theta, \quad \Delta l_{b, 8} = a_2 \theta$$

$$s = (4 a_1 + 2 a_2) \theta = (2 + 2\sqrt{2}) a_2 \theta$$

$$\delta = \frac{2 L}{\theta} \sin^2\left(\frac{\theta}{2}\right)$$

Trong đó $a_1 = a_2 / \sqrt{2}$.

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $s$ | Tổng chiều dài trượt tích lũy của 8 dây ngoại vi | m (mm) | Tổng khoảng cách trượt tương đối của các dây so với đĩa | Bó dây bố trí đối xứng tròn |
| $\Delta l_{b, i}$ | Độ trượt dọc trục của dây thứ $i$ | m (mm) | Biến thiên độ dài cung do dây nằm lệch trục trung hòa | Dây uốn theo cung tròn đồng tâm |
| $\theta$ | Góc uốn tổng thể tại đầu cuối robot | rad | Góc hợp bởi mặt phẳng đĩa gốc và đĩa ngọn | Uốn cong đều với bán kính cong $R = L/\theta$ |
| $a_1, a_2$ | Khoảng cách từ các dây ngoại vi tới trục trung hòa | m (mm) | Hình học bố trí dây trên mặt cắt đĩa tròn | $a_1 = a_2 \sin(45^\circ) = a_2 / \sqrt{2}$ |
| $L$ | Chiều dài tự nhiên của robot | m (mm) | Chiều dài dọc trục của thanh trung tâm | Thanh trung tâm không dãn dài trục |
| $\delta$ | Độ dịch chuyển ngang của điểm đầu cuối | m (mm) | Chuyển vị hình học của cung tròn uốn | Hình học tam giác hợp bởi dây cung |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Thiết lập mối quan hệ động học thuần túy giữa độ võng đầu cuối $\delta$, góc uốn cong $\theta$, và độ trượt dọc trục $s$ của các dây bố trí lệch tâm.
2. **Cơ chế:** Dây nằm trên trục trung hòa (dây 4 và 5) không trượt ($\Delta l = 0$). Các dây ở phía chịu kéo và chịu nén trượt một lượng tỷ lệ thuận với khoảng cách tới trục trung hòa ($a_1, a_2$) và góc uốn $\theta$.
3. **Ý nghĩa:** Cho phép liên kết trực tiếp biến dạng hình học vĩ mô ($\delta$) với biến dạng trượt vi mô ($s$) để đưa vào phương trình cân bằng công ma sát.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp mô hình động học chính xác cho bó dây tròn uốn cong cung tròn đều.

---

### NOTE D-03: M31 Eqs. (7)–(9) — Độ cứng uốn hiệu dụng $(EI)_a$ mô hình hóa từ ma sát kẹp SMA

#### A. Source Identity
- **Paper ID:** M31
- **Evidence ID:** M31-E05
- **Equation Number:** Eqs. (7), (8), (9)
- **PDF Page:** 4, 5
- **Printed Page:** 6585, 6586
- **SHA-256:** `65d0979f31522c7eb16c52bb7fcda3a1e4a781f21508933b93f1cae5f5f403aa`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (pp. 4–5):

$$U_a = U_m + (F_{f, a} - F_{f, m}) s$$

$$U = \int_0^L \frac{F_{\text{ext}}^2 l^2}{2 EI} dl = \frac{F_{\text{ext}}^2 L^3}{6 EI}$$

$$(EI)_a = \frac{F_{\text{ext}, a}^2 L^3}{6 [U_m + (F_{f, a} - F_{f, m}) s]}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $(EI)_a$ | Độ cứng uốn mô hình hóa ở trạng thái austenite | N·m² | Độ cứng uốn tương đương của dầm công xôn khi lò xo SMA nóng | Dầm công xôn uốn đàn hồi tương đương |
| $U$ | Năng lượng biến dạng đàn hồi tích lũy trong dầm công xôn | J | $U = \int_0^L \frac{M^2}{2EI} dl$ với $M(l) = F_{\text{ext}} l$ | Uốn Euler-Bernoulli dưới tải đầu mút |
| $F_{\text{ext}, a}$ | Lực tác dụng đầu mút đo được ở trạng thái austenite | N | Giá trị lực ngoài tại độ võng $\delta$ định trước | Trạng thái cân bằng tĩnh |
| $F_{f, a} - F_{f, m}$ | Chênh lệch lực ma sát giữa pha austenite và martensite | N | Độ tăng lực ma sát do lực siết nhiệt của SMA | Đo độc lập qua thử nghiệm kéo 1 dây |
| $L$ | Chiều dài dầm công xôn | m | Chiều dài làm việc của robot | Không đổi |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Tác giả quy đổi tổng công uốn (gồm cả công biến dạng và công ma sát gia tăng) về một độ cứng uốn hiệu dụng tương đương $(EI)_a$ của dầm công xôn Euler-Bernoulli.
2. **Cơ chế:** Năng lượng phân tán do ma sát siết $(F_{f, a} - F_{f, m})s$ được cộng gộp vào mẫu số năng lượng, từ đó định nghĩa một giá trị độ cứng uốn tăng cường cho trạng thái austenite.
3. **Phê phán khoa học (Scientific Critique):**
   - Đây là một **độ cứng vận hành xấp xỉ** (operational / apparent bending stiffness), không phải độ cứng đàn hồi bảo toàn (conservative elastic stiffness).
   - Khi đảo chiều tải trọng (dỡ tải), lực ma sát $F_f$ sẽ đảo dấu cản trở sự hồi phục, tạo ra một vòng trễ cơ học lớn (frictional hysteresis loop). Do đó $(EI)_a$ chỉ đúng cho quá trình gia tải một chiều (loading branch).

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp công thức so sánh cho cơ cấu thay đổi độ cứng uốn dựa trên ma sát kẹp ngoài.

---

### NOTE D-04: M31 Eq. (10) — Công thức uốn công xôn thực nghiệm chiết xuất độ cứng

#### A. Source Identity
- **Paper ID:** M31
- **Evidence ID:** M31-E07
- **Equation Number:** Eq. (10)
- **PDF Page:** 6
- **Printed Page:** 6587
- **SHA-256:** `65d0979f31522c7eb16c52bb7fcda3a1e4a781f21508933b93f1cae5f5f403aa`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 6):

$$EI = \frac{F_{\text{ext}} L^3}{3 \delta}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $EI$ | Độ cứng uốn thực nghiệm chiết xuất | N·m² | Độ cứng tính từ công thức độ võng dầm công xôn Euler-Bernoulli chịu lực đầu mút | Dầm công xôn thẳng, ngàm một đầu, biến dạng bé |
| $F_{\text{ext}}$ | Lực uốn đầu mút đo được | N | Lực ghi nhận từ cảm biến lực Model 333ALB | Vận tốc kéo 10 mm/min |
| $\delta$ | Độ võng đo được tại đầu mút | m (mm) | Chuyển vị đo được ($\delta = 5$ mm trong bài) | Chuyển vị tuyến tính |
| $L$ | Chiều dài dầm công xôn | m | Chiều dài dầm ($L = 60$ mm) | Ngàm cứng |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Sử dụng công thức cổ điển của dầm công xôn Euler-Bernoulli $\delta = \frac{F L^3}{3 EI}$ để quy đổi trực tiếp tỷ số đo đạc $F_{\text{ext}} / \delta$ thành độ cứng uốn $EI$.
2. **Cảnh báo khoa học bắt buộc (Mandatory Scientific Warning):**
   - Độ cứng uốn $EI$ không mặc nhiên tương đương với độ dốc của mọi đường cong lực - biến dạng!
   - Khi dầm có trượt ma sát hoặc biến dạng lớn, đường cong $F - \delta$ là phi tuyến. Việc lấy giá trị cát tuyến (secant stiffness) tại một điểm độ võng cố định ($\delta = 5$ mm) sẽ bỏ qua lịch sử trượt và sự tiêu tán ma sát.

#### E. Relation to MP1
- **Khả năng áp dụng:** Dùng làm phương pháp chuẩn đo đạc thực nghiệm uốn công xôn trong MP1 để so sánh độ cứng biểu kiến giữa trạng thái kẹt và không kẹt.

---

### NOTE D-05: M32 Eq. (1) — Độ cứng uốn liên kết mềm nhiều phần tử trong trạng thái không kẹt

#### A. Source Identity
- **Paper ID:** M32
- **Title:** Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon
- **Authors:** A. Nishida, H. Morita, E. Fujieda, H. Sawada
- **Year:** 2022
- **DOI:** 10.20965/jrm.2022.p0466
- **Evidence ID:** M32-E04, M32-E06
- **Equation Number:** Eq. (1)
- **PDF Page:** 5, 8
- **Printed Page:** 470, 473 (J. Robot. Mechatron. 34(2): 466–477)
- **SHA-256:** `2cd907e77a29584dca2161f5c61304f5e7188f504e0e5a6c382023bb41249bdf`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 5, p. 8):

$$\frac{P}{\delta} = \frac{3 n EI}{L^3}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $P / \delta$ | Độ cứng kết cấu công xôn đo được | N/m (N/mm) | Tỷ số giữa lực đầu mút và chuyển vị | Biến dạng bé |
| $n$ | Số lượng phần tử uốn độc lập (dây hoặc tấm) | Không chiều | Prototype 1: $n=2$ tấm SMP; Prototype 2: $n=4$ dây SMA | Các phần tử uốn song song độc lập |
| $E$ | Mô đun Young của vật liệu phần tử | Pa (GPa) | SMA martensite $E = 28$ GPa; austenite $E = 67$ GPa | Vật liệu đồng nhất |
| $I$ | Mô men quán tính diện tích của một phần tử đơn lẻ | m⁴ (mm⁴) | Dây tròn đường kính 1 mm: $I = \pi d^4 / 64 = 0.049$ mm⁴ | Tiết diện tròn đều |
| $L$ | Chiều dài công xôn | m (mm) | $L = 50$ mm | Chiều dài dầm |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô tả độ cứng uốn ở trạng thái không kẹt (unjammed state) của liên kết mềm gồm $n$ phần tử uốn song song.
2. **Cơ chế:** Khi không có áp suất chân không giữ chặt (unjammed), màng bọc không truyền được lực cắt tiếp xúc giữa các dây/tấm. Toàn bộ các phần tử trượt tự do lên nhau và uốn độc lập quanh trục riêng của từng phần tử. Tổng độ cứng uốn bằng đúng tổng độ cứng của $n$ phần tử riêng rẽ ($n \times EI$).
3. **Kiểm chứng tác giả (p. 8):** Với 4 dây SMA martensite ($n=4, E=28$ GPa, $d=1$ mm, $L=50$ mm), tác giả tính ra $P/\delta = 0.13$ N/mm, hoàn toàn trùng khớp với giá trị đo đạc thực nghiệm ở trạng thái unjammed.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp cận dưới lý thuyết tuyệt đối ($EI_{\min}$) cho độ cứng uốn của bó dây TiNi trong MP1 khi áp suất kẹt bằng 0.

---

### NOTE D-06: M33 Eqs. (24), (31) — Hàm trễ pha martensite Gaussian và phương trình vi phân lực dây SMA

#### A. Source Identity
- **Paper ID:** M33
- **Title:** A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump
- **Authors:** R. J. Pierce, H. A. Mascaro
- **Year:** 2012 (Published 2013)
- **DOI:** 10.1109/TMECH.2012.2217150
- **Evidence ID:** M33-E04
- **Equation Number:** Eqs. (24), (31)
- **PDF Page:** 6
- **Printed Page:** 541 (IEEE/ASME Trans. Mechatron. 18(2): 536–545)
- **SHA-256:** `de64029540b6dc0bb76a1d48c0a87677fa9880175b5b4e054cfbebf48d616d2b`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 6):

$$R_m(x) = \frac{1}{2} \left[ 1 - \operatorname{erf}\left( \frac{T_w(x) - \bar{T}}{\sigma_T \sqrt{2}} \right) \right]$$

$$\dot{F} = \frac{\pi}{4} D_w^2 [E_a (1 - R_m)\dot{\varepsilon} - E_a \dot{R}_m \varepsilon + R_m \dot{\sigma} + \dot{R}_m \sigma]$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $R_m(x)$ | Phân số thể tích martensite tại vị trí $x$ | Không chiều | $R_m \in [0, 1]$, mô tả mức độ hoàn thành chuyển pha | Mô hình trễ hàm phân phối chuẩn tích lũy |
| $T_w(x)$ | Nhiệt độ cục bộ của dây SMA | K (°C) | Nhiệt độ phân bố dọc theo chiều dài dây | Truyền nhiệt đối lưu và gia nhiệt Joule |
| $\bar{T}$ | Nhiệt độ chuyển pha trung bình | K (°C) | Nhiệt độ trung bình giữa bắt đầu và kết thúc chuyển pha | Khác nhau giữa gia nhiệt và làm nguội |
| $\sigma_T$ | Độ lệch chuẩn phân bố nhiệt độ chuyển pha | K | Đặc trưng cho độ rộng của dải nhiệt độ chuyển pha | Thông số nhà sản xuất cung cấp |
| $\operatorname{erf}(\cdot)$ | Hàm tích phân sai số Gaussian | Không chiều | $\operatorname{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2} dt$ | Đường cong trễ trơn nhẵn liên tục |
| $\dot{F}$ | Tốc độ biến thiên lực kéo của dây SMA | N/s | Đạo hàm thời gian của lực dọc trục trong dây | Cân bằng động học |
| $D_w$ | Đường kính dây SMA | m (mm) | Đường kính mặt cắt tròn | Không đổi |
| $E_a$ | Mô đun Young của pha austenite | Pa (GPa) | Mô đun đàn hồi pha nhiệt độ cao | Hằng số vật liệu |
| $\varepsilon, \dot{\varepsilon}$ | Biến dạng dọc trục và tốc độ biến dạng của dây | Không chiều, 1/s | Biến dạng cơ học | Biến dạng kéo |
| $\sigma, \dot{\sigma}$ | Ứng suất và tốc độ ứng suất trong dây | Pa, Pa/s | Ứng suất cơ học cục bộ | Đơn trục |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô hình hóa hiện tượng trễ nhiệt - cơ (thermomechanical hysteresis) và tốc độ sinh lực động học của dây SMA khi được kích hoạt bằng nhiệt độ.
2. **Ý nghĩa:**
   - Sử dụng hàm tích phân sai số chuẩn $\operatorname{erf}$ để làm trơn đường cong chuyển pha $R_m(T)$, tránh các điểm gãy góc của mô hình Brinson hay Liang-Rogers, giúp các thuật toán giải phương trình vi phân hội tụ ổn định.
   - Phương trình tốc độ lực $\dot{F}$ phân tách tường minh đóng góp của tốc độ biến dạng cơ học $\dot{\varepsilon}$ và tốc độ chuyển pha do nhiệt $\dot{R}_m$.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp mô hình điều khiển lực động học nếu MP1 sử dụng dây SMA chủ động để siết hoặc điều khiển áp suất trong hệ thống.

---

### NOTE D-07: M34 Eq. (1) — Phân số Martensite khử song tinh theo ứng suất tiếp cắt (Brinson Model)

#### A. Source Identity
- **Paper ID:** M34
- **Title:** Shape Memory Alloy Capsule Micropump for Drug Delivery Applications
- **Authors:** A. Shayganmanesh et al.
- **Year:** 2021
- **DOI:** 10.3390/mi12050520
- **Evidence ID:** M34-E05
- **Equation Number:** Eq. (1)
- **PDF Page:** 5
- **Printed Page:** 5 (Micromachines 2021, 12, 520)
- **SHA-256:** `55457a97c6d64d1f2b48a4369a19c9689408994bb0498db2579df8996fe11802`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 5, đã kiểm tra trực quan ảnh quét):

$$\xi_{St} = 0.5 \cos\left( \pi \frac{\tau - \tau_f^{cr}}{\tau_s^{cr} - \tau_f^{cr}} \right) + 0.5$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $\xi_{St}$ | Phân số thể tích martensite khử song tinh (detwinned martensite fraction) | Không chiều | Tỷ lệ thể tích pha martensite định hướng dưới ứng suất | Nằm trong khoảng $[0, 1]$ |
| $\tau$ | Ứng suất tiếp cắt tác dụng lên dây lò xo | Pa (MPa) | Ứng suất xoắn cực đại trên mặt cắt dây lò xo | Trạng thái xoắn thuần túy |
| $\tau_s^{cr}$ | Ứng suất cắt tới hạn bắt đầu khử song tinh | Pa (MPa) | $\tau_s^{cr} = 105$ MPa trong Table 1 | Ngưỡng bắt đầu chuyển đổi vi cấu trúc |
| $\tau_f^{cr}$ | Ứng suất cắt tới hạn kết thúc khử song tinh | Pa (MPa) | $\tau_f^{cr} = 215$ MPa trong Table 1 | Hoàn thành định hướng vi cấu trúc |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô hình hóa quá trình khử song tinh (detwinning) của pha martensite dưới ứng suất cắt xoắn trong dây lò xo SMA theo mô hình kinh điển Brinson.
2. **Cơ chế:** Khi ứng suất cắt $\tau$ tăng từ 105 MPa lên 215 MPa, các phiến song tinh martensite ngẫu nhiên tự tái định hướng theo phương ứng suất tác dụng, làm $\xi_{St}$ tăng từ 0 lên 1. Quá trình này sinh ra biến dạng trượt dư lớn có khả năng phục hồi khi gia nhiệt (hiệu ứng nhớ hình).

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp thông số trạng thái vi cấu trúc bên trong dây lò xo nén SMA dùng trong cơ cấu phát lực MP1.

---

### NOTE D-08: M34 Eq. (2) — Lực đàn hồi của lò xo xoắn SMA có xét biến dạng chuyển pha và góc nâng bước

#### A. Source Identity
- **Paper ID:** M34
- **Evidence ID:** M34-E05
- **Equation Number:** Eq. (2)
- **PDF Page:** 5
- **Printed Page:** 5
- **SHA-256:** `55457a97c6d64d1f2b48a4369a19c9689408994bb0498db2579df8996fe11802`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 5, đã kiểm tra trực quan ảnh quét):

$$F_M = \frac{G_M d^4}{8 D^3 n} \left( \frac{\cos^3 \alpha_i}{\cos^2 \alpha_f + \frac{\sin^2 \alpha_f}{1+\nu}} \right) \delta - \frac{\pi d^3}{8 D} G_M \gamma_L \xi_{St}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $F_M$ | Lực dọc trục do lò xo SMA sinh ra trong pha martensite | N | Lực tác động lên pít-tông hoặc buồng nén | Lực dọc trục lò xo |
| $G_M$ | Mô đun trượt cắt của pha martensite | Pa (GPa) | $G_M = 5.65$ GPa trong Table 1 | Vật liệu đàn hồi tuyến tính |
| $d$ | Đường kính dây lò xo | m (mm) | Đường kính sợi dây kim loại làm lò xo | Dây tròn đều |
| $D$ | Đường kính trung bình của vòng xoắn lò xo | m (mm) | Đường kính vòng xoắn ($C = D/d$ là chỉ số lò xo) | Giả thiết biến dạng đối xứng trục |
| $n$ | Số vòng xoắn làm việc tích cực của lò xo | Không chiều | Số vòng tự do biến dạng | Vòng xoắn đều |
| $\alpha_i, \alpha_f$ | Góc nâng bước xoắn ban đầu và kết thúc | rad (độ) | Góc nghiêng của dây lò xo so với mặt phẳng ngang | Có xét biến đổi góc bước lớn |
| $\nu$ | Hệ số Poisson của vật liệu | Không chiều | $\nu \approx 0.33$ | Đẳng hướng |
| $\delta$ | Độ nén hoặc kéo dọc trục của lò xo | m (mm) | Biến dạng chiều dài lò xo | Biến dạng cơ học |
| $\gamma_L$ | Biến dạng trượt dư cực đại (maximum residual strain) | Không chiều | $\gamma_L = 0.056$ trong Table 1 | Giới hạn chuyển pha cực đại |
| $\xi_{St}$ | Phân số martensite khử song tinh | Không chiều | Xác định từ Eq. (1) | Khử song tinh cơ học |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Thiết lập phương trình lực - biến dạng phi tuyến chính xác cho lò xo xoắn SMA trong pha martensite.
2. **Cấu trúc phương trình:**
   - Số hạng thứ nhất: Lực đàn hồi cơ học tuyến tính sửa đổi, có xét hiệu ứng phi tuyến hình học của góc nâng bước ốc $\alpha_f$ khi lò xo bị nén/dãn lớn.
   - Số hạng thứ hai: Thành phần lực giảm đi do biến dạng chuyển pha khử song tinh $\gamma_L \xi_{St}$ làm mềm lò xo.
3. **Phân biệt khoa học:** Đây là lực do **lò xo xoắn** sinh ra, chịu chi phối bởi ứng suất xoắn cắt trong tiết diện dây tròn và góc nâng bước ốc; không được đồng nhất với lực kéo dãn dọc trục đơn thuần của dây thẳng!

#### E. Relation to MP1
- **Khả năng áp dụng:** Cho phép thiết kế và tính toán chính xác lực siết hoặc lực ép buồng nếu MP1 sử dụng lò xo SMA làm nguồn phát động tạo áp lực kẹp.

---

### NOTE D-09: M34 Eq. (3) — Điều kiện tương thích chuyển vị giữa lò xo SMA và vỏ bọc đàn hồi

#### A. Source Identity
- **Paper ID:** M34
- **Evidence ID:** M34-E05
- **Equation Number:** Eq. (3)
- **PDF Page:** 5
- **Printed Page:** 5
- **SHA-256:** `55457a97c6d64d1f2b48a4369a19c9689408994bb0498db2579df8996fe11802`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 5):

$$\delta_{\text{silicone}} = d_i - \delta_{\text{spring}}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $\delta_{\text{silicone}}$ | Độ dịch chuyển biến dạng của vỏ bọc silicone | m (mm) | Chuyển vị nén ép của khoang chứa | Ứng xử đàn hồi tuyến tính |
| $d_i$ | Khoảng cách dịch chuyển ban đầu khả dụng | m (mm) | Khoảng không gian hình học định sẵn | Kích thước khoang kín |
| $\delta_{\text{spring}}$ | Độ dịch chuyển biến dạng của lò xo SMA | m (mm) | Hành trình dịch chuyển của đầu lò xo | Tương thích hình học |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Phương trình tương thích động học (kinematic compatibility equation) giữa cơ cấu sinh lực (lò xo SMA) và cấu trúc chịu lực mềm (vỏ silicone / buồng nén).
2. **Ý nghĩa:** Điểm làm việc thực tế của cơ cấu chấp hành là giao điểm của đường cong lực - biến dạng của lò xo SMA và đường cong độ cứng của vỏ bọc đàn hồi. Không thể xác định hành trình hay lực phát động nếu không giải đồng thời hệ ghép cặp này.

#### E. Relation to MP1
- **Khả năng áp dụng:** Bắt buộc áp dụng khi ghép nối cơ cấu chấp hành SMA với màng bọc mềm hoặc buồng khí của MP1.
