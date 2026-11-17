# MP1 READING PACK — WP-C EQUATION READING NOTES
## Wire Bundle and NiTi Mechanics

- **Task ID:** MP1-LR-P2-EQ-R1
- **Package:** WP-C (Wire Bundle and NiTi Mechanics)
- **Status:** VERIFIED_FULL_TEXT
- **Target Thesis Sections:** C1.2.1, C2.4, C2.4.2, C2.5, C2.5.1, C2.5.2, C2.5.3, C2.5.5

---

## 1. TỔNG QUAN VÀ PHÂN ĐỊNH BẢN CHẤT CƠ HỌC NHÓM WP-C

Để tránh nhầm lẫn trong xây dựng mô hình cơ học MP1, các phương trình trong WP-C được phân định thành 3 lớp cơ học độc lập:
1. **Material Constitutive Equations (Phương trình cấu tạo vật liệu):** Mô tả quan hệ ứng suất - biến dạng vi mô của vật liệu NiTi siêu đàn hồi ($d\sigma_{ij} - d\varepsilon_{ij}$), sự tiến triển của phân số thể tích martensite $\xi$, và biến dạng chuyển pha $d\varepsilon_{ij}^{tr}$ (tiêu biểu: M29).
2. **Structural Bending Equations (Phương trình uốn kết cấu):** Mô tả quan hệ giữa mô men uốn vĩ mô $M$, độ cong $\kappa$, lực cắt $Q$, độ võng $w$, và ma trận độ cứng mặt cắt $6 \times 6$ (tiêu biểu: M22, M23, M24).
3. **Contact / Interfacial Slip Equations (Phương trình tiếp xúc và trượt giao diện):** Mô tả quan hệ lực tương tác ma sát hoặc độ cứng trượt $k_i$ với độ dịch chuyển trượt tương đối $\Delta u_i$ giữa các sợi hoặc các lớp (tiêu biểu: M22 Eq. 37, M23 Eqs. 15 & 28, M24 Eqs. 11–12).

Tuyệt đối không đồng nhất độ cứng uốn kết cấu $EI$ với mô đun đàn hồi vật liệu $E$, và không đồng nhất trượt ma sát với biến dạng dẻo hay chuyển pha martensite.

---

## 2. GHI CHÚ CHI TIẾT TỪNG PHƯƠNG TRÌNH ĐƯỢC CHỌN

---

### NOTE C-01: M22 Eqs. (33)–(35) — Độ võng uốn và độ cứng uốn hiệu dụng (EBS) của cáp bó dây song song

#### A. Source Identity
- **Paper ID:** M22
- **Title:** Bending Stiffness of Parallel Wire Cables
- **Authors:** Y. Zhang, Q. Feng, S. Xu, C. Liu
- **Year:** 2018
- **DOI:** 10.1061/(ASCE)ST.1943-541X.0002164
- **Evidence ID:** M22-E02
- **Equation Number:** Eqs. (33), (34), (35)
- **PDF Page:** 4, 5
- **Printed Page:** 04018164-4, 04018164-5 (J. Struct. Eng., 2018, 144(10): 04018164)
- **SHA-256:** `9c2773e4cd31c3fc5290b0e5138f3ea70e6371aa43f32f3fba0c7bb0b56b5736`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 4):

$$w_{\max 2} = \frac{P L}{4 F} + \frac{P [F/(EI_0) - \lambda_2^2]}{2 F \lambda_1 (\lambda_2^2 - \lambda_1^2)} \tanh\frac{\lambda_1 L}{2} - \frac{P [F/(EI_0) - \lambda_1^2]}{2 F \lambda_2 (\lambda_2^2 - \lambda_1^2)} \tanh\frac{\lambda_2 L}{2}$$

$$\delta_2 = \frac{w_{\max 2}}{\bar{w}_{\max 2}}$$

$$EI_{\text{eff} 2} = \frac{1}{\delta_2} EI_\infty$$

Trong đó $\bar{w}_{\max 2}$ là độ võng lớn nhất ở trạng thái dính hoàn toàn (fully bonded / no-slip), $EI_\infty$ là độ cứng uốn giới hạn trên khi không có trượt, $EI_0$ là độ cứng uốn giới hạn dưới khi trượt hoàn toàn.

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $w_{\max 2}$ | Độ võng lớn nhất tại giữa nhịp dưới lực tập trung $P$ | m (mm) | Nghiệm giải tích của phương trình vi phân uốn dầm phân lớp có trượt đàn hồi | Đặt trên 2 gối tựa đơn, có lực kéo dọc trục $F$ |
| $P$ | Lực tập trung đặt tại giữa nhịp | N (kN) | Tải trọng uốn thử nghiệm | Tải trọng tĩnh hoặc quasi-static |
| $F$ | Lực kéo căng dọc trục cáp | N (kN) | Lực căng trước đặt tại hai đầu cáp | Lực kéo $F > 0$ không đổi dọc trục |
| $L$ | Chiều dài nhịp cáp | m (mm) | Khoảng cách giữa hai đầu gối tựa đơn | Dầm thẳng nhịp $L$ |
| $EI_0$ | Độ cứng uốn ở trạng thái trượt hoàn toàn (full-slip) | N·m² | Tổng độ cứng uốn của các dây riêng lẻ: $\sum E_j I_j$ | Không có lực ma sát truyền qua giao diện |
| $EI_\infty$ | Độ cứng uốn ở trạng thái dính hoàn toàn (no-slip) | N·m² | Độ cứng uốn của tiết diện dầm liền khối theo định lý trục song song Steiner | Giao diện dính cứng tuyệt đối |
| $EI_{\text{eff} 2}$ | Độ cứng uốn hiệu dụng (Equivalent Bending Stiffness - EBS) | N·m² | $EI_{\text{eff} 2} = EI_\infty / \delta_2$ | Độ cứng uốn quy đổi về dầm Euler-Bernoulli tương đương |
| $\delta_2$ | Hệ số khuếch đại độ võng (Deflection Magnification Coefficient - DMC) | Không chiều | $\delta_2 = w_{\max 2} / \bar{w}_{\max 2} \ge 1$ | So sánh với độ võng dầm liền khối cùng tải |
| $\lambda_1, \lambda_2$ | Các nghiệm đặc trưng của phương trình vi phân uốn | 1/m | Phụ thuộc vào $F, EI_0, EI_\infty$, và độ cứng trượt giao diện $k$ | Nghiệm thực phân biệt |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô hình uốn kết cấu của bó dây song song có xét đến lực căng dọc trục $F$ và biến dạng trượt đàn hồi tại giao diện giữa các lớp dây.
2. **Liên hệ giữa các đại lượng:**
   - Sự trượt tại giao diện làm giảm khả năng truyền lực cắt tiếp xúc giữa các dây, dẫn tới độ võng $w_{\max 2}$ tăng lên so với dầm liền khối ($\bar{w}_{\max 2}$), được định lượng bằng hệ số $\delta_2 > 1$.
   - Độ cứng uốn hiệu dụng $EI_{\text{eff} 2}$ giảm tỷ lệ nghịch với $\delta_2$.
   - Khi độ cứng trượt $k \to \infty$: $\delta_2 \to 1$, $EI_{\text{eff}} \to EI_\infty$ (cận trên).
   - Khi độ cứng trượt $k \to 0$: $\delta_2 \to EI_\infty / EI_0$, $EI_{\text{eff}} \to EI_0$ (cận dưới).
3. **Input:** Lực uốn $P$, lực căng $F$, nhịp $L$, độ cứng trượt giao diện $k$, mô đun $E$, kích thước dây.
4. **Output:** Độ võng giữa nhịp $w_{\max 2}$, hệ số khuếch đại $\delta_2$, và độ cứng uốn hiệu dụng $EI_{\text{eff} 2}$.
5. **Giả thiết:** Mô hình hóa bó dây tròn thành dầm phân lớp tương đương bảo toàn diện tích; quan hệ trượt - lực tương tác tuân theo độ cứng trượt tuyến tính $k$.
6. **Điều kiện đúng:** Cáp dây song song chịu kéo $F > 0$ và uốn tải trọng tập trung giữa nhịp.
7. **Phân biệt khoa học:** $EI_{\text{eff}}$ là độ cứng uốn **kết cấu** phụ thuộc vào trạng thái trượt và lực căng, không phải sự thay đổi mô đun đàn hồi $E$ của thép!

#### E. Relation to MP1
- **Khả năng áp dụng:** Áp dụng có giả thiết (Applicable with assumptions). Cung cấp công thức chuẩn tắc để định nghĩa độ cứng uốn hiệu dụng $EI_{\text{eff}}$ và hệ số suy giảm độ cứng cho bó dây song song MP1.

#### F. Validation Evidence
- **Phương pháp:** So sánh với phương pháp không gian trạng thái (State Space Method - SSM) và dữ liệu thí nghiệm cáp thép 37φ7, 55φ7, 61φ7 từ Chen et al. (2015).
- **Mức độ phù hợp:** Sai số tính toán độ võng dưới 2% ở hai trạng thái biên so với lý thuyết cổ điển; khớp tốt với thực nghiệm khi có lực căng $F$.

---

### NOTE C-02: M22 Eq. (37) — Hiệu chuẩn độ cứng trượt tuyến tính theo ứng suất nén/kéo ban đầu

#### A. Source Identity
- **Paper ID:** M22
- **Title:** Bending Stiffness of Parallel Wire Cables
- **Evidence ID:** M22-E04
- **Equation Number:** Eq. (37)
- **PDF Page:** 7
- **Printed Page:** 04018164-7
- **SHA-256:** `9c2773e4cd31c3fc5290b0e5138f3ea70e6371aa43f32f3fba0c7bb0b56b5736`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 7):

$$k = \xi \bar{\sigma} + k_0$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $k$ | Độ cứng trượt giao diện (slip rigidity) | Pa (N/m² hoặc MPa) | Hệ số tỉ lệ giữa lực cắt tương tác trên đơn vị diện tích và độ trượt tương đối: $\tau = k \Delta u$ | Giả thiết trượt đàn hồi tuyến tính (linear elastic slip) |
| $\bar{\sigma}$ | Ứng suất kéo căng trung bình dọc trục cáp | Pa (MPa) | $\bar{\sigma} = F / A_{\text{total}}$ | Ứng suất phân bố đều trên tất cả các dây |
| $\xi$ | Hệ số thực nghiệm không chiều | Không chiều | Hệ số góc thể hiện sự tăng trở lực trượt theo ứng suất dọc trục | Xác định từ khớp dữ liệu thực nghiệm (empirical fitting) |
| $k_0$ | Độ cứng trượt ban đầu khi không có ứng suất kéo | Pa (MPa) | Trở lực trượt tự thân do tiếp xúc ban đầu giữa các dây | Phụ thuộc độ khít và biến dạng dư ban đầu |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô hình tiếp xúc/ma sát bán thực nghiệm biểu diễn sự phụ thuộc của độ cứng chống trượt giao diện $k$ vào mức độ nén/kéo ban đầu $\bar{\sigma}$.
2. **Bản chất cơ học:** Khi cáp được kéo căng ($F$ tăng), hiệu ứng co thắt Poisson và sự nén ép hình học giữa các lớp dây làm tăng áp lực tiếp xúc pháp tuyến giữa các dây, từ đó làm tăng trở lực ma sát chống trượt.
3. **Phát biểu của tác giả:** *"The slip rigidity $k$ synthesizes all the factors that could provide the restriction to the interfacial slips... It is proposed that the approximately linear relations between the average tensile stress and the slip rigidity of the wires as $k = \xi\bar{\sigma} + k_0$."*
4. **Hạn chế khoa học (Scientific Distinction):**
   - Đây là công thức **hiệu chuẩn thực nghiệm** (calibration equation), **không phải định luật vật lý cơ bản**.
   - Giả định trượt tuyến tính $\tau = k \Delta u$ bỏ qua ngưỡng trượt Coulomb dẻo lý tưởng ($\tau \le \mu p$).
   - Nếu áp dụng vào hệ áp suất dương ngoài như MP1, $\bar{\sigma}$ cần được thay thế hoặc bổ sung bằng áp suất giam hướng kính $p$.

#### E. Relation to MP1
- **Khả năng áp dụng:** Tương tự (Analogy only). MP1 không dựa vào lực kéo cáp để tạo áp lực tiếp xúc mà dùng áp suất khí nén dương bên ngoài. Do đó quan hệ cần xây dựng là $k(p)$ thay vì $k(\bar{\sigma})$.

---

### NOTE C-03: M23 Eqs. (3)–(4) — Phương trình trạng thái dầm phân lớp 2D Plane Stress và ứng suất uốn

#### A. Source Identity
- **Paper ID:** M23
- **Title:** Analytical model for the bending of parallel wire cables considering interactions among wires
- **Authors:** Y. Zhang, Q. Feng, G. Wang, S. Xu
- **Year:** 2021
- **DOI:** 10.1016/j.ijmecsci.2020.106192
- **Evidence ID:** M23-E03
- **Equation Number:** Eqs. (3), (4)
- **PDF Page:** 3
- **Printed Page:** 3 (Int. J. Mech. Sci. 194, 106192)
- **SHA-256:** `1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 3):

$$\frac{\partial}{\partial y} \begin{Bmatrix} u^{(i)} \\ \sigma_y^{(i)} \\ v^{(i)} \\ \tau_{xy}^{(i)} \end{Bmatrix} = \begin{bmatrix} 0 & 0 & -\frac{\partial}{\partial x} & \frac{1}{G_i} \\ 0 & 0 & -\sigma_{x0}^{(i)} \frac{\partial^2}{\partial x^2} & -\frac{\partial}{\partial x} \\ -\mu_i \frac{\partial}{\partial x} & \frac{1 - \mu_i^2}{E_i} & 0 & 0 \\ -(E_i + \sigma_{x0}^{(i)}) \frac{\partial^2}{\partial x^2} & \mu_i \frac{\partial}{\partial x} & 0 & 0 \end{bmatrix} \begin{Bmatrix} u^{(i)} \\ \sigma_y^{(i)} \\ v^{(i)} \\ \tau_{xy}^{(i)} \end{Bmatrix}$$

$$\sigma_x^{(i)} = E_i \frac{\partial u^{(i)}}{\partial x} + \mu_i \sigma_y^{(i)}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $u^{(i)}, v^{(i)}$ | Chuyển vị dọc trục ($x$) và chuyển vị đứng ($y$) của lớp thứ $i$ | m | Trường chuyển vị 2D trong mặt phẳng | Biến dạng bé |
| $\sigma_y^{(i)}$ | Ứng suất pháp vuông góc giao diện (ứng suất nén tiếp xúc) | Pa | Biến trạng thái mô tả tương tác nén ép giữa các lớp | Ứng suất phẳng (plane stress) |
| $\tau_{xy}^{(i)}$ | Ứng suất cắt tiếp xúc trên mặt phẳng $y = \text{const}$ | Pa | Biến trạng thái truyền lực ma sát giữa các lớp | Cân bằng vi phân Cauchy |
| $\sigma_x^{(i)}$ | Ứng suất pháp uốn dọc trục của lớp thứ $i$ | Pa | Tính từ phương trình cấu tạo đàn hồi 2D có xét hiệu ứng Poisson | Quan hệ đàn hồi tuyến tính Hooke |
| $\sigma_{x0}^{(i)}$ | Ứng suất kéo căng trước ban đầu trong lớp $i$ | Pa | Lực căng ban đầu phân bố trên diện tích lớp | Đều trong từng lớp |
| $E_i, G_i$ | Mô đun Young và mô đun trượt của lớp $i$ | Pa | $G_i = E_i / [2(1 + \mu_i)]$ | Vật liệu đẳng hướng |
| $\mu_i$ | Hệ số Poisson của vật liệu lớp $i$ | Không chiều | Đặc tính vật liệu đàn hồi (lưu ý: $\mu_i$ ở M23 là Poisson ratio, không phải ma sát!) | Khác với hệ số ma sát |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô hình hóa cơ học uốn của từng lớp trong dầm phân lớp bằng lý thuyết đàn hồi 2D (plane stress) không dựa vào giả thiết tiết diện phẳng Euler-Bernoulli hay Timoshenko.
2. **Bản chất toán học:** Biểu diễn các phương trình cân bằng vi phân và phương trình tương thích biến dạng dưới dạng hệ phương trình trạng thái hiện đại cấp 1 theo biến không gian chiều dày $y$.
3. **Ưu điểm vượt trội:** Các biến trạng thái bao gồm trực tiếp cả 2 thành phần chuyển vị $\{u, v\}$ và 2 thành phần ứng suất mặt $\{ \sigma_y, \tau_{xy} \}$. Điều này cho phép áp dụng điều kiện biên tiếp xúc và trượt ma sát một cách tự nhiên và chính xác tuyệt đối mà các lý thuyết dầm cổ điển không thể thực hiện được.
4. **Phân biệt biến số:** Chú ý rằng trong M23, ký hiệu $\mu_i$ đại diện cho hệ số Poisson (Poisson's ratio), trong khi hệ số ma sát được phản ánh gián tiếp qua độ cứng trượt $k_i$.

#### E. Relation to MP1
- **Khả năng áp dụng:** Nền tảng phương pháp luận cao cấp (High-level benchmark framework). Có thể dùng để kiểm chứng sai số của các mô hình dầm 1D giản lược khi phân tích bó dây TiNi trong MP1.

---

### NOTE C-04: M23 Eq. (15) — Điều kiện trượt giao diện trong không gian trạng thái và ma trận truyền

#### A. Source Identity
- **Paper ID:** M23
- **Title:** Analytical model for the bending of parallel wire cables considering interactions among wires
- **Evidence ID:** M23-E04
- **Equation Number:** Eqs. (15), (18), (19)
- **PDF Page:** 5
- **Printed Page:** 5
- **SHA-256:** `1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 5, đã kiểm tra trực quan ảnh quét):

$$\begin{Bmatrix} U_m^{(i+1)}(\zeta_i) \\ \sigma_m^{(i+1)}(\zeta_i) \\ V_m^{(i+1)}(\zeta_i) \\ \tau_m^{(i+1)}(\zeta_i) \end{Bmatrix} = \begin{bmatrix} 1 & 0 & 0 & E_0 / (k_i h_0) \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{Bmatrix} U_m^{(i)}(\zeta_i) \\ \sigma_m^{(i)}(\zeta_i) \\ V_m^{(i)}(\zeta_i) \\ \tau_m^{(i)}(\zeta_i) \end{Bmatrix}$$

$$\begin{Bmatrix} U_m^{(n)}(1) \\ \sigma_m^{(n)}(1) \\ V_m^{(n)}(1) \\ \tau_m^{(n)}(1) \end{Bmatrix} = [\mathbf{T}_n] [\mathbf{C}_{n-1}] [\mathbf{T}_{n-1}] \cdots [\mathbf{C}_1] [\mathbf{T}_1] \begin{Bmatrix} U_m^{(1)}(0) \\ \sigma_m^{(1)}(0) \\ V_m^{(1)}(0) \\ \tau_m^{(1)}(0) \end{Bmatrix}$$

Trong đó $[\mathbf{T}_i] = \exp([\mathbf{K}_i] \Delta\zeta_i)$ và $[\mathbf{C}_i]$ là ma trận ghép trượt giao diện ở trên.

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $U_m^{(i)}, V_m^{(i)}$ | Hệ số chuỗi Fourier của chuyển vị không thứ nguyên | Không chiều | Khai triển Fourier theo phương dọc trục $x$ của $u$ và $v$ | Khai triển chuỗi điều hòa Navier |
| $\sigma_m^{(i)}, \tau_m^{(i)}$ | Hệ số chuỗi Fourier của ứng suất pháp và ứng suất cắt | Không chiều | Khai triển Fourier của $\sigma_y$ và $\tau_{xy}$ | Chuỗi hội tụ (lấy $\ge 10$ số hạng) |
| $k_i$ | Độ cứng trượt tại giao diện thứ $i$ | Pa (MPa) | Đặc trưng cản trở trượt tại giao diện giữa lớp $i$ và $i+1$ | Trượt đàn hồi tuyến tính |
| $E_0, h_0$ | Mô đun đàn hồi và chiều dày chuẩn hóa | Pa, m | Các đại lượng cơ sở dùng để không thứ nguyên hóa | Hằng số chuẩn hóa |
| $[\mathbf{T}_i]$ | Ma trận truyền qua lớp thứ $i$ (Transfer matrix) | Không chiều | Tính bằng hàm số mũ ma trận: $\exp([\mathbf{K}_i]\Delta\zeta_i)$ | Tính chất vật liệu đồng nhất trong mỗi lớp |
| $[\mathbf{C}_i]$ | Ma trận ghép nối điều kiện trượt tại giao diện thứ $i$ | Không chiều | Ma trận $4 \times 4$ chứa phần tử trượt $E_0/(k_i h_0)$ | Ứng suất tiếp xúc và chuyển vị đứng liên tục |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Thiết lập điều kiện tiếp xúc cơ học thực tế tại mặt phân cách giữa hai lớp kế tiếp có xét đến độ trượt tương đối $\Delta u_i = u^{(i+1)} - u^{(i)}$.
2. **Liên hệ cơ học:**
   - Tại giao diện, ứng suất nén tiếp xúc $\sigma_y$ và ứng suất cắt $\tau_{xy}$ hoàn toàn liên tục (cân bằng lực vi mô).
   - Chuyển vị đứng $v$ liên tục (không có sự hở tách lớp - no separation).
   - Chuyển vị dọc trục nhảy một bước bằng độ trượt $\Delta u_i = \tau / k_i$. Trong phương trình trạng thái, bước nhảy này được thể hiện qua phần tử $(1, 4)$ của ma trận $[\mathbf{C}_i]$ là $E_0 / (k_i h_0)$.
   - Khi $k_i \to \infty$ (không trượt), phần tử này triệt tiêu, $[\mathbf{C}_i]$ trở thành ma trận đơn vị $[\mathbf{I}_4]$.
3. **Ý nghĩa thuật toán:** Cho phép nhân dồn ma trận truyền từ đáy dầm lên đỉnh dầm, quy bài toán dầm nhiều lớp về hệ phương trình đại số $2 \times 2$ đơn giản từ điều kiện biên ứng suất mặt ngoài.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cực kỳ hữu ích cho mô hình hóa giao diện. Cho phép thay thế tiếp xúc cứng ngắc bằng phần tử tiếp xúc đàn hồi trượt có thể điều chỉnh tham số $k_i$ theo áp suất buồng khí.

---

### NOTE C-05: M23 Eq. (26) — Định nghĩa hệ số khuếch đại độ võng (DMC) và hệ số độ cứng uốn tương đương (EBSC)

#### A. Source Identity
- **Paper ID:** M23
- **Evidence ID:** M23-E05
- **Equation Number:** Eq. (26), Eq. (27)
- **PDF Page:** 7, 8
- **Printed Page:** 7, 8
- **SHA-256:** `1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (pp. 7–8):

$$\delta = \frac{w_{\max}(\text{with slip})}{w_{\max}(\text{no-slip})}$$

$$\gamma = \frac{1}{\delta} = \frac{EI_{\text{eff}}}{EI_{\max}}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $\delta$ | Hệ số khuếch đại độ võng (Deflection Magnification Coefficient - DMC) | Không chiều | Tỷ số giữa độ võng thực tế có trượt và độ võng lý thuyết dính cứng | $\delta \ge 1$ |
| $\gamma$ | Hệ số độ cứng uốn tương đương (Equivalent Bending Stiffness Coefficient - EBSC) | Không chiều | Tỷ số giữa độ cứng uốn hiệu dụng và độ cứng dính cứng lớn nhất: $\gamma = EI_{\text{eff}} / EI_{\max}$ | Nằm trong khoảng $[EI_{\min}/EI_{\max}, 1]$ |
| $w_{\max}(\text{with slip})$ | Độ võng lớn nhất có xét trượt giữa các dây | m | Tính từ nghiệm chuỗi Fourier hoặc đo thực nghiệm | Cùng một tải trọng uốn |
| $w_{\max}(\text{no-slip})$ | Độ võng lớn nhất ở trạng thái liên kết cứng | m | Độ võng khi $k \to \infty$ | Cùng cấu hình hình học |

#### D. Mechanical Interpretation
1. **Ý nghĩa:** Cung cấp chỉ số không thứ nguyên hóa chuẩn mực để lượng hóa sự suy giảm độ cứng uốn của kết cấu nhiều phần tử chịu trượt.
2. **Quan sát thực nghiệm của tác giả (Table 2, p. 9):**
   - Đối với cáp không kéo căng ($T_{x0} = 0$ kN), đường cong lực - độ võng có dạng hai đoạn thẳng gãy khúc (bilinear behavior).
   - Hệ số EBSC giai đoạn 1 ($\gamma_1$) chỉ đạt $0.237 - 0.459$ (tức nhỏ hơn 50% $EI_{\max}$).
   - Hệ số EBSC giai đoạn 2 ($\gamma_2$) đạt $0.022 - 0.037$ (lớn hơn $EI_{\min}$ nhưng rất nhỏ so với $EI_{\max}$).
   - Kết luận quan trọng của tác giả: Trong thực tế, các dây **không bao giờ ở trạng thái no-slip hoàn toàn hay full-slip hoàn toàn**, mà luôn ở trạng thái trượt cục bộ trung gian.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp trực tiếp định nghĩa metric đánh giá cho MP1: $EI_{\text{eff}} / EI_{\max}$. Cảnh báo người nghiên cứu MP1 không được mặc định hệ kẹt áp suất dương sẽ đạt 100% độ cứng nguyên khối $EI_{\max}$.

---

### NOTE C-06: M23 Eq. (28) — Tỷ lệ độ trượt giữa các giao diện theo mô men tĩnh

#### A. Source Identity
- **Paper ID:** M23
- **Evidence ID:** M23-E07
- **Equation Number:** Eq. (28)
- **PDF Page:** 10
- **Printed Page:** 10
- **SHA-256:** `1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 10):

$$\frac{\Delta u_i}{\Delta u_1} = \frac{S_i}{S_1} - \left(\frac{S_i}{S_1} - 1\right)\exp(-R_i) \quad (i = 1, 2, \dots, n-1)$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $\Delta u_i$ | Độ trượt tương đối tại giao diện thứ $i$ | m (mm) | $\Delta u_i = u^{(i+1)} - u^{(i)}$ | Đo tại tọa độ dọc trục bất kỳ |
| $\Delta u_1$ | Độ trượt tương đối tại giao diện ngoài cùng thứ nhất | m (mm) | Giao diện chuẩn để so sánh | Khác 0 khi có trượt |
| $S_i$ | Mô men tĩnh của phần mặt cắt phía trên giao diện thứ $i$ | m³ | Mô men tĩnh diện tích lấy đối với trục trung hòa mặt cắt | Hình học mặt cắt xác định |
| $R_i$ | Tham số không thứ nguyên đại diện cho độ cứng trượt | Không chiều | Tỷ lệ thuận với độ cứng trượt $k_i$ tại giao diện | $R_i \ge 0$ |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Thiết lập mối quan hệ giải tích dạng hàm mũ giữa độ trượt tương đối tại các giao diện khác nhau qua chiều sâu dầm.
2. **Hai trạng thái giới hạn (Asymptotic limits):**
   - Khi độ cứng trượt rất bé ($k \to 0 \implies R_i \to 0$): $\exp(0) = 1$, do đó $\frac{\Delta u_i}{\Delta u_1} \to 1$. Tất cả các giao diện trượt một lượng bằng nhau (mỗi dây uốn độc lập với độ cong như nhau).
   - Khi độ cứng trượt rất lớn ($k \to \infty \implies R_i \to \infty$): $\exp(-\infty) = 0$, do đó $\frac{\Delta u_i}{\Delta u_1} \to \frac{S_i}{S_1}$. Tỷ số trượt hội tụ về đúng tỷ số của các mô men tĩnh diện tích (phân bố lực cắt cổ điển Jourawski).
3. **Ý nghĩa:** Giải thích tại sao việc đo đạc trượt ở giao diện ngoài cùng có thể suy ra trường trượt bên trong lõi bó dây.

---

### NOTE C-07: M24 Eqs. (11)–(12) — Động học biến dạng riêng (Eigenstrain) cho các pha trượt bó dây

#### A. Source Identity
- **Paper ID:** M24
- **Title:** A new mechanical model of short wire ropes: Theory and experimental validation
- **Authors:** F. Barsi, A. Paolone, L. Placidi
- **Year:** 2025
- **DOI:** 10.1016/j.engstruct.2024.119217
- **Evidence ID:** M24-E04
- **Equation Number:** Eqs. (11), (12)
- **PDF Page:** 5
- **Printed Page:** 5 (Eng. Struct. 323, 119217)
- **SHA-256:** `9f4295be23df948762d1c68fce0db4122d10664be872b83440eec55cf73fa7bc`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 5):

$$\begin{aligned}
\text{perfect stick state:} \quad & \boldsymbol{\beta}_{S1}^{(i)} = \mathbf{0} \\
\text{partial stick state:} \quad & \boldsymbol{\beta}_{S2}^{(i)} = (\mathbf{d}_3^{(i)} \otimes \mathbf{d}_3^{(i)}) \cdot (\boldsymbol{\mu} \times \mathbf{z}^{(i)}) \\
\text{full slip state:} \quad & \boldsymbol{\beta}_{S3}^{(i)} = \boldsymbol{\mu} \times \mathbf{z}^{(i)} \\
\text{axial-torsional state:} \quad & \boldsymbol{\beta}_{S4}^{(i)} = (\mathbf{d}_1^{(i)} \otimes \mathbf{d}_1^{(i)} + \mathbf{d}_2^{(i)} \otimes \mathbf{d}_2^{(i)}) \cdot (\boldsymbol{\gamma} + \boldsymbol{\mu} \times \mathbf{z}^{(i)})
\end{aligned}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $\boldsymbol{\beta}_{S}^{(i)}$ | Tensor biến dạng riêng (eigenstrain) của sợi dây thứ $i$ | Không chiều | Biến dạng không tương thích biểu diễn sự trượt tương đối giữa các dây | Lý thuyết biến dạng riêng Eshelby |
| $\mathbf{d}_1^{(i)}, \mathbf{d}_2^{(i)}, \mathbf{d}_3^{(i)}$ | Hệ cơ sở trực chuẩn gắn với đường tâm sợi dây thứ $i$ | Không chiều | $\mathbf{d}_3^{(i)}$ là tiếp tuyến đường tâm; $\mathbf{d}_1, \mathbf{d}_2$ nằm trên mặt cắt ngang dây | Khung Frenet-Serret hoặc Bishop |
| $\boldsymbol{\mu}$ | Vector độ cong uốn và xoắn vĩ mô của cáp | rad/m | Độ cong của trục trung hòa kết cấu cáp tổng thể | Biến dạng uốn dầm cong |
| $\mathbf{z}^{(i)}$ | Vector vị trí của tâm sợi thứ $i$ so với trục trung hòa cáp | m | Tọa độ hình học của dây trên mặt cắt ngang | Vị trí bố trí dây xác định |
| $\boldsymbol{\gamma}$ | Vector biến dạng dọc trục và trượt vĩ mô của cáp | Không chiều | Biến dạng trung bình của dầm tương đương | Khung động học dầm |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Sử dụng khái niệm biến dạng riêng (eigenstrain) trong cơ học vật rắn (vốn dùng cho sai hỏng mạng tinh thể hoặc pha bao Eshelby) để mô hình hóa sự trượt ma sát giữa các sợi dây trong cáp chịu uốn.
2. **Cơ chế vật lý của từng pha:**
   - **Perfect stick:** $\boldsymbol{\beta}_{S1} = \mathbf{0}$. Các dây liên kết hoàn hảo; độ cong kết cấu gây ra biến dạng dãn dài trực tiếp của từng dây theo khoảng cách $\mathbf{z}^{(i)}$ tới trục trung hòa.
   - **Partial stick:** Dây trượt dọc theo phương tiếp tuyến $\mathbf{d}_3$ khi gradient lực dọc vượt quá ma sát ma sát tiếp xúc. Độ cong uốn không còn gây dãn dài dây.
   - **Full slip:** $\boldsymbol{\beta}_{S3} = \boldsymbol{\mu} \times \mathbf{z}^{(i)}$. Độ trượt bù trừ hoàn toàn biến dạng uốn vĩ mô; các dây uốn độc lập quanh trục riêng của chúng mà không làm dãn dài hay sinh ứng suất cắt liên kết.
3. **Ý nghĩa:** Tránh việc phải giải bài toán tiếp xúc phi tuyến cục bộ phức tạp tại từng điểm tiếp xúc bằng cách đưa trượt vào trường biến dạng riêng của dầm.

#### E. Relation to MP1
- **Khả năng áp dụng:** Khung lý thuyết hiện đại nhất (Cutting-edge 2025 approach). Có thể áp dụng trực tiếp để mô tả sự chuyển tiếp giữa các trạng thái dính-trượt của bó dây TiNi trong MP1.

---

### NOTE C-08: M24 Eq. (18) — Ma trận độ cứng mặt cắt $6 \times 6$ của bó cáp chịu trượt

#### A. Source Identity
- **Paper ID:** M24
- **Evidence ID:** M24-E04
- **Equation Number:** Eq. (18)
- **PDF Page:** 5
- **Printed Page:** 5
- **SHA-256:** `9f4295be23df948762d1c68fce0db4122d10664be872b83440eec55cf73fa7bc`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 5):

$$\begin{bmatrix} N \\ Q_2 \\ Q_3 \\ T \\ M_2 \\ M_3 \end{bmatrix} = \begin{bmatrix} k_{11} & 0 & 0 & k_{14} & 0 & 0 \\ 0 & k_{22} & 0 & 0 & k_{25} & 0 \\ 0 & 0 & k_{33} & 0 & 0 & k_{36} \\ k_{41} & 0 & 0 & k_{44} & 0 & 0 \\ 0 & k_{52} & 0 & 0 & k_{55} & 0 \\ 0 & 0 & k_{63} & 0 & 0 & k_{66} \end{bmatrix} \begin{bmatrix} \varepsilon \\ \gamma_2 \\ \gamma_3 \\ \mu_T \\ \mu_2 \\ \mu_3 \end{bmatrix}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $N, Q_2, Q_3$ | Lực dọc trục và hai lực cắt ngang | N | Các lực nội tại tích hợp trên mặt cắt ngang | Cân bằng lực |
| $T, M_2, M_3$ | Mô men xoắn và hai mô men uốn | N·m | Các mô men nội tại tích hợp trên mặt cắt ngang | Cân bằng mô men |
| $\varepsilon, \gamma_2, \gamma_3$ | Biến dạng dọc trục và biến dạng trượt cắt | Không chiều | Các độ đo biến dạng trung bình của tiết diện cáp | Biến dạng dầm |
| $\mu_T, \mu_2, \mu_3$ | Độ xoắn và hai độ cong uốn | rad/m | Các thành phần vector độ cong của trục cáp | Biến dạng góc |
| $k_{ij}$ | Các hệ số độ cứng của mặt cắt ngang | Biến thiên | Hệ số độ cứng phụ thuộc vào trạng thái trượt (stick/slip state) | Ma trận xác định dương, có thể không đối xứng nếu có trượt |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Biểu diễn luật cấu tạo kết cấu mặt cắt ngang tích hợp đầy đủ hiệu ứng ghép cặp giữa kéo - xoắn ($k_{14}, k_{41}$) và uốn - cắt ($k_{25}, k_{36}, k_{52}, k_{63}$).
2. **Ảnh hưởng của trượt:** Khi chuyển từ stick sang partial-stick và full-slip, các hệ số độ cứng uốn $k_{55}$ và $k_{66}$ giảm mạnh do biến dạng riêng $\boldsymbol{\beta}_S$ triệt tiêu thành phần đóng góp của khoảng cách Steiner $\sum A_i z_i^2$.
3. **Phân biệt khoa học:** Đây là ma trận độ cứng **kết cấu của mặt cắt dầm** (cross-sectional structural stiffness matrix), không phải ma trận độ cứng vật liệu vi mô $C_{ijkl}$.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cho phép phân tích chính xác ứng xử uốn không gian và hiện tượng xoắn ngoài ý muốn của bó dây TiNi khi chịu uốn.

---

### NOTE C-09: M29 Eqs. (8)–(9) — Phân rã biến dạng gia số cho vật liệu hợp kim nhớ hình (SMA)

#### A. Source Identity
- **Paper ID:** M29
- **Title:** Finite Element Method for Mechanical Behavior of Shape Memory Alloy Cables (形状记忆合金超弹性缆索力学行为的有限单元法)
- **Authors:** Z. Kang et al. (康泽天 等)
- **Year:** 2020 (Journal publication 2020/2025)
- **Evidence ID:** M29-E03
- **Equation Number:** Eqs. (8), (9)
- **PDF Page:** 3
- **Printed Page:** 67 (Engineering Mechanics / 工程力学)
- **SHA-256:** `56793dea9be449e79b9b5fef7645f8f8f26df80c98f8045e7f7b3b05423f7902`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 3):

$$\varepsilon_{ij} = \varepsilon_{ij}^{\text{tr}} + \varepsilon_{ij}^{\text{th}} + \varepsilon_{ij}^{\text{e}}$$

$$d\varepsilon_{ij} = d\varepsilon_{ij}^{\text{tr}} + d\varepsilon_{ij}^{\text{th}} + d\varepsilon_{ij}^{\text{e}}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $d\varepsilon_{ij}$ | Tensor biến dạng toàn phần gia số | Không chiều | Biến dạng vi mô tổng cộng tại một điểm trong vật liệu SMA | Giả thiết biến dạng bé, biến dạng dẻo thuần túy bị bỏ qua |
| $d\varepsilon_{ij}^{\text{tr}}$ | Tensor biến dạng chuyển pha gia số (transformation strain) | Không chiều | Biến dạng sinh ra do sự chuyển pha austenite $\leftrightarrow$ martensite | Điều khiển bởi ứng suất và nhiệt độ theo mặt năng lượng tự do |
| $d\varepsilon_{ij}^{\text{th}}$ | Tensor biến dạng nhiệt gia số (thermal expansion strain) | Không chiều | $d\varepsilon_{ij}^{\text{th}} = \Theta_{ij} dT$ | Giãn nở nhiệt tuyến tính |
| $d\varepsilon_{ij}^{\text{e}}$ | Tensor biến dạng đàn hồi gia số (elastic strain) | Không chiều | $d\varepsilon_{ij}^{\text{e}} = S_{ijkl} d\sigma_{kl}$ | Đàn hồi phụ thuộc vào phân số thể tích pha $\xi$ |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Thiết lập nguyên lý phân rã biến dạng cho vật liệu NiTi siêu đàn hồi (superelastic NiTi) trong cơ học môi trường liên tục gia số.
2. **Phân biệt khoa học cốt lõi (Scientific Distinction):**
   - Biến dạng chuyển pha $\varepsilon_{ij}^{\text{tr}}$ là biến dạng vi cấu trúc tinh thể mạng nghịch đảo được (reversible phase transformation), **hoàn toàn khác với biến dạng dẻo trượt không nghịch đảo (plastic slip)** của kim loại thông thường.
   - Trượt cơ học giữa các dây (interfacial slip $\Delta u$) xảy ra ở **ranh giới tiếp xúc bên ngoài**, trong khi biến dạng chuyển pha $\varepsilon^{\text{tr}}$ xảy ra **bên trong thể tích vật liệu tinh thể**. Không bao giờ được đồng nhất hai hiện tượng này.

#### E. Relation to MP1
- **Khả năng áp dụng:** Bắt buộc áp dụng cho vật liệu TiNi. Cung cấp nền tảng vật liệu chính xác khi dây TiNi trong MP1 đạt ngưỡng ứng suất chuyển pha $\sigma_{\text{MS}}$ trong quá trình uốn.

---

### NOTE C-10: M29 Eqs. (14)–(17) — Quy luật chảy chuyển pha và phương trình cấu tạo 3D gia số của SMA

#### A. Source Identity
- **Paper ID:** M29
- **Evidence ID:** M29-E03
- **Equation Number:** Eqs. (14), (15), (16), (17)
- **PDF Page:** 3
- **Printed Page:** 67
- **SHA-256:** `56793dea9be449e79b9b5fef7645f8f8f26df80c98f8045e7f7b3b05423f7902`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 3):

$$d\varepsilon_{ij}^{\text{tr}} = H \Lambda_{ij} d\xi = H \Lambda_{ij} (1 - \xi_0) d\eta$$

$$\Lambda_{ij} = \begin{cases} \frac{3 \sigma_{ij}'}{2 \bar{\sigma}}, & \text{chuyển pha thuận (forward transformation)} \\ \frac{\varepsilon_{ij}^{\text{tr}}}{\bar{\varepsilon}^{\text{tr}}}, & \text{chuyển pha nghịch (reverse transformation)} \end{cases}$$

$$d\sigma_{kl} = C_{ijkl} [d\varepsilon_{ij} - H \Lambda_{ij} (1 - \xi_0) d\eta - \Theta_{ij} dT]$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $H$ | Biến dạng chuyển pha cực đại trong thí nghiệm kéo đơn trục | Không chiều | Thông số vật liệu đặc trưng của NiTi ($H \approx 0.04 - 0.06$) | Xác định từ thí nghiệm kéo đơn trục ở nhiệt độ $T > A_f$ |
| $\Lambda_{ij}$ | Tensor định hướng dòng chuyển pha | Không chiều | Tương tự vector pháp tuyến thế dẻo Drucker-Prager / von Mises | Dòng chuyển pha đồng trục với tensor ứng suất lệch |
| $\sigma_{ij}'$ | Tensor ứng suất lệch (deviatoric stress tensor) | Pa | $\sigma_{ij}' = \sigma_{ij} - \frac{1}{3}\sigma_{kk}\delta_{ij}$ | Thể tích không đổi trong biến dạng chuyển pha |
| $\bar{\sigma}$ | Ứng suất tương đương von Mises | Pa | $\bar{\sigma} = \sqrt{\frac{3}{2} \sigma_{ij}' \sigma_{ij}'}$ | Đẳng hướng |
| $\xi, \eta$ | Phân số thể tích martensite và hệ số nhớ hình | Không chiều | $\xi \in [0, 1]$, biến nội tại mô tả trạng thái pha | Hàm phụ thuộc vào $(\bar{\sigma}, T)$ |
| $C_{ijkl}$ | Tensor độ cứng đàn hồi tức thời của SMA | Pa | $C_{ijkl} = S_{ijkl}^{-1}$, phụ thuộc pha: $S = (1-\xi)S^A + \xi S^M$ | Austenite và Martensite có mô đun khác nhau ($E_A \approx 60-80$ GPa, $E_M \approx 20-40$ GPa) |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô hình hóa toán học hoàn chỉnh cho ứng xử cơ học phi tuyến siêu đàn hồi và hiện tượng trễ (hysteresis) của SMA trong không gian ứng suất 3D.
2. **Cơ chế vật lý:**
   - Trong quá trình gia tải uốn, khi ứng suất von Mises $\bar{\sigma}$ vượt qua ứng suất bắt đầu chuyển pha $\sigma_{\text{MS}}(T)$, austenite chuyển thành detwinned martensite, sinh ra biến dạng chuyển pha $d\varepsilon^{\text{tr}}$ dọc theo hướng ứng suất lệch $\sigma'$.
   - Quá trình này tạo nên đoạn cao nguyên ứng suất (stress plateau) trên đường cong $\sigma - \varepsilon$.
   - Khi dỡ tải, martensite không bền nhiệt động sẽ tự động chuyển ngược lại austenite tại ngưỡng $\sigma_{\text{AS}}(T)$, khép kín vòng trễ siêu đàn hồi (pseudoelastic loop).
3. **Phân biệt khoa học:** Vòng trễ siêu đàn hồi này bắt nguồn từ **năng lượng tự do hóa học và ma sát dịch chuyển pha tinh thể**, hoàn toàn độc lập với **vòng trễ ma sát Coulomb** sinh ra do trượt tiếp xúc giữa các dây.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp mô hình vật liệu chuẩn xác nhất để mô tả bó dây TiNi trong MP1 khi biến dạng uốn đủ lớn để kích hoạt chuyển pha siêu đàn hồi.
