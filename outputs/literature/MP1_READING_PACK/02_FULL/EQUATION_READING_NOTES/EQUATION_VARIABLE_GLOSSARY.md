# MP1 READING PACK — EQUATION VARIABLE GLOSSARY
## Bảng Tra Cứu và Đồng Hóa Ký Hiệu Cơ Học Toàn Diện

- **Task ID:** MP1-LR-P2-EQ-R1
- **Scope:** WP-B, WP-C, WP-D Selected Equations
- **Status:** VERIFIED_FULL_TEXT
- **Target Thesis Sections:** C1.2.1, C1.2.2, C2.1–C2.5

---

## 1. MỤC ĐÍCH VÀ CẢNH BÁO ĐỒNG HÓA KÝ HIỆU (CROSS-PAPER NOTATION WARNING)

Trong các bài báo từ WP-B, WP-C và WP-D, nhiều tác giả sử dụng cùng một ký hiệu cho các đại lượng vật lý hoàn toàn khác nhau, hoặc sử dụng các ký hiệu khác nhau cho cùng một khái niệm cơ học. Người nghiên cứu MP1 **phải tuyệt đối lưu ý các điểm dị biệt sau**:

1. **Ký hiệu chiều dày ($h$ vs $\delta$):**
   - Trong **M17 (Caruso et al.)**: $h$ là chiều dày của **một lớp đơn lẻ**; tổng chiều cao dầm 4 lớp là $4h$ (hoặc $nh$).
   - Trong **M18 (Zhang et al. 2025)**: $h$ là **tổng chiều cao dầm**; chiều dày của một lớp đơn lẻ ký hiệu là $\delta$!
   - Trong **M23 (Zhang et al. 2021)**: $h_i$ là chiều dày của lớp thứ $i$, và $H = \sum h_i$ là tổng chiều cao dầm!

2. **Ký hiệu hệ số Poisson vs Hệ số ma sát ($\mu$):**
   - Trong **M17, M18, M13, M19, M31**: $\mu$ là **hệ số ma sát tĩnh/động Coulomb** giữa các lớp hoặc giữa dây với vỏ bọc.
   - Trong **M23 (Zhang et al. 2021)**: $\mu_i$ là **hệ số Poisson** (Poisson's ratio) của vật liệu lớp thứ $i$! Hệ số ma sát trong M23 không xuất hiện trực tiếp mà được phản ánh gián tiếp qua độ cứng trượt $k_i$.

3. **Ký hiệu áp suất giam ($p$ vs $P$ vs $u_P$):**
   - Trong **M17, M18, M13, M19**: $p$ là áp suất giam (chân không âm hoặc khí nén dương) [Pa hoặc kPa].
   - Trong **M07, M32**: $P$ là áp suất chân không hoặc lực tập trung [N].
   - Trong **M15, M16**: $u_P$ là áp suất chân không đóng vai trò tín hiệu điều khiển đầu vào [kPa].

4. **Ký hiệu độ cứng uốn ($EI$ vs $E$ vs $K$):**
   - $E$: Mô đun đàn hồi Young của vật liệu cơ sở [Pa, GPa].
   - $I$: Mô men quán tính diện tích của mặt cắt [m⁴].
   - $EI$: Độ cứng uốn kết cấu thuần túy [N·m²].
   - $EI_{\text{eff}}$ hoặc $(EI)_a$: Độ cứng uốn hiệu dụng biểu kiến (operational / apparent flexural rigidity) có tính đến trượt ma sát hoặc tiêu tán công [N·m²].
   - $K = P/\delta$: Độ cứng kết cấu công xôn đo được [N/m hoặc N/mm], phụ thuộc vào chiều dài nhịp $L^3$ và điều kiện biên.

---

## 2. BẢNG TRA CỨU KÝ HIỆU CHỮ LA-TINH (LATIN SYMBOLS)

| Ký hiệu | Tên gọi & Ý nghĩa vật lý | Đơn vị SI | Xuất hiện trong | Lưu ý ngữ cảnh |
|---|---|---|---|---|
| $A$ | Diện tích mặt cắt ngang tổng thể | m² | M17, M18, M22, M23 | $A = 4bh$ (M17), $A = bh$ (M18), $A_{\text{total}} = \sum A_i$ (M22) |
| $a_1, a_2$ | Khoảng cách từ dây ngoại vi đến trục trung hòa | m (mm) | M31 | $a_1 = a_2 / \sqrt{2}$ trong đĩa bố trí 8 dây đối xứng |
| $b$ | Chiều rộng mặt cắt ngang dầm | m (mm) | M17, M18, M19, M23 | Chiều rộng dầm chữ nhật |
| $c$ | Chu vi tiếp xúc ma sát hiệu dụng của sợi | m (mm) | M13 | Phần chu vi tiết diện sợi tham gia truyền lực ma sát |
| $c_0, c_1, c_2$ | Các hệ số đa thức bậc 2 của ứng suất cắt | Pa, Pa/m, Pa/m² | M18 | Hệ số xác định trường ứng suất cắt khi $|Q| > Q_{\max}$ |
| $C_{ijkl}$ | Tensor độ cứng đàn hồi của vật liệu | Pa (GPa) | M20, M29 | Tensor cấp 4 mô tả đàn hồi Hooke tổng quát |
| $d$ | Đường kính dây đơn lẻ | m (mm) | M22, M31, M32, M34 | Đường kính sợi kim loại tròn |
| $D$ | Đường kính trung bình vòng xoắn lò xo | m (mm) | M34 | $C = D/d$ là chỉ số lò xo (spring index) |
| $E, E_i$ | Mô đun đàn hồi Young của vật liệu | Pa (GPa) | M17, M22, M23, M32 | Đặc tính đàn hồi thuần túy của vật liệu |
| $E_A, E_M$ | Mô đun đàn hồi pha austenite và martensite của SMA | Pa (GPa) | M29, M32, M33 | $E_A \approx 60-80$ GPa; $E_M \approx 20-40$ GPa |
| $EI_0$ | Độ cứng uốn ở trạng thái trượt hoàn toàn (full-slip) | N·m² | M22 | Bằng tổng độ cứng các dây uốn độc lập: $\sum E_j I_j$ |
| $EI_\infty, EI_{\max}$ | Độ cứng uốn ở trạng thái dính hoàn toàn (no-slip) | N·m² | M22, M23 | Cận trên khi dầm hoạt động như thanh đặc nguyên khối |
| $EI_{\text{eff}}$ | Độ cứng uốn tương đương hiệu dụng (EBS) | N·m² | M22, M23 | $EI_{\text{eff}} = EI_\infty / \delta$ |
| $(EI)_a$ | Độ cứng uốn mô hình hóa ở trạng thái austenite | N·m² | M31 | Độ cứng biểu kiến có xét tiêu tán công ma sát |
| $f, f_{\text{friction}}$ | Lực ma sát tiếp xúc | N | M31 | Lực cản trượt giữa dây và ống cao su |
| $F, F_{\text{ext}}$ | Lực ngoài tác dụng uốn | N | M17, M22, M31, M32 | Lực tập trung uốn 3 điểm hoặc uốn công xôn |
| $F_0, F_1, F_i$ | Tải trọng trượt danh định các pha trong dầm kẹt lớp | N | M17 | Tải kích hoạt trượt tại giao diện trung tâm và các giao diện kế tiếp |
| $F_f, F_{f, m}, F_{f, a}$ | Lực ma sát tổng cộng ở trạng thái martensite / austenite | N | M31 | Lực siết cản trở trượt của 8 dây |
| $F_M$ | Lực phát động dọc trục của lò xo SMA martensite | N | M34 | Lực dọc trục của lò xo xoắn |
| $G, G_i$ | Mô đun trượt cắt đàn hồi của vật liệu | Pa (GPa) | M20, M23, M34 | $G = E / [2(1+\nu)]$ |
| $G_M, G_A$ | Mô đun trượt của pha martensite và austenite trong SMA | Pa (GPa) | M34 | $G_M = 5.65$ GPa, $G_A = 18.3$ GPa |
| $h$ | Chiều cao / chiều dày dầm hoặc lớp | m (mm) | M17, M18, M23 | **Xem cảnh báo mục 1** ($h$ lớp ở M17, $h$ tổng ở M18) |
| $H$ | Tổng chiều cao dầm phân lớp hoặc biến dạng chuyển pha cực đại | m hoặc không chiều | M23, M29 | $H = \sum h_i$ (M23); $H \approx 0.04-0.06$ (M29) |
| $I, I_i$ | Mô men quán tính diện tích của mặt cắt ngang | m⁴ | M17, M22, M31, M32 | Đại lượng hình học mặt cắt |
| $I_{\text{p-s}}$ | Mô men quán tính pha pre-slip (no-slip) | m⁴ | M17 | $I_{\text{p-s}} = 16bh^3/3$ (dầm 4 lớp) |
| $I_{\text{pa-s}}$ | Mô men quán tính pha partial-slip | m⁴ | M17 | $I_{\text{pa-s}} = 4bh^3/3$ (hai dầm 2 lớp) |
| $I_{\text{f-s}}$ | Mô men quán tính pha full-slip | m⁴ | M17 | $I_{\text{f-s}} = bh^3/3$ (bốn lớp độc lập) |
| $I_J, I_S$ | Mô men quán tính pha kẹt (jammed) và pha trượt (slipped) | m⁴ | M13 | Cận trên và cận dưới trong kẹt sợi |
| $k, k_i$ | Độ cứng trượt giao diện (slip rigidity) | Pa hoặc Pa/m | M22, M23 | Hệ số tỉ lệ giữa lực tiếp xúc và độ trượt: $\tau = k \Delta u$ |
| $k_\sigma$ | Độ dốc ứng suất pháp trong lớp trượt | Pa/m | M19 | $\sigma = k_\sigma y$ |
| $k_{ij}$ | Hệ số ma trận độ cứng mặt cắt cáp $6 \times 6$ | Biến thiên | M24 | Ghép cặp kéo-xoắn và uốn-cắt |
| $l, L$ | Chiều dài nhịp hoặc dầm | m (mm) | M17, M22, M23, M31, M32 | Khoảng cách gối tựa hoặc chiều dài công xôn |
| $m, M$ | Mô men uốn tác dụng lên sợi hoặc bó sợi | N·m | M13, M18, M24 | Nội lực mô men uốn |
| $n$ | Số lượng lớp hoặc số sợi hoặc số vòng lò xo | Không chiều | M17, M23, M32, M34 | Số nguyên dương |
| $N$ | Lực dọc trục của dầm | N | M18, M24 | Nội lực kéo/nén tiếp tuyến trục dầm |
| $p$ | Áp suất kẹt giam giữ (áp suất chân không hoặc khí nén) | Pa (kPa) | M13, M17, M18, M19 | Nguồn áp suất duy trì ma sát tiếp xúc |
| $P$ | Lực tập trung uốn hoặc áp suất | N hoặc Pa | M22, M32 | Tải trọng uốn thử nghiệm |
| $q_s, q_y$ | Tải trọng phân bố dọc trục và vuông góc trục dầm | N/m | M18 | Tải trọng ngoài phân bố trên dầm cong |
| $Q$ | Lực cắt ngang tác dụng lên mặt cắt | N | M18, M24 | Nội lực cắt ngang |
| $Q_{\text{slip}}, Q_J$ | Lực cắt tới hạn bắt đầu xuất hiện trượt | N | M13, M18 | $Q_{\text{slip}} = \frac{2}{3}\mu p b h$ |
| $Q_{\max}, Q_S$ | Lực cắt giới hạn trên của pha trượt | N | M13, M18 | Ngưỡng kết thúc chuyển pha |
| $r$ | Bán kính cong của trục dầm | m | M18 | $1/r = \kappa = d\theta/ds$ |
| $R_i$ | Tham số không thứ nguyên độ cứng trượt giao diện | Không chiều | M23 | Tỷ lệ thuận với $k_i$ |
| $R_m(x)$ | Phân số thể tích martensite theo hàm tích phân sai số | Không chiều | M33 | $R_m \in [0, 1]$ |
| $s$ | Tọa độ độ dài cung hoặc tổng chiều dài trượt tích lũy | m (mm) | M18, M31 | Tọa độ cong dầm (M18) hoặc tổng dịch chuyển trượt (M31) |
| $S_i$ | Mô men tĩnh diện tích đối với trục trung hòa | m³ | M22, M23 | Hình học mặt cắt dầm |
| $T$ | Nhiệt độ hoặc mô men xoắn | K (°C) hoặc N·m | M24, M29, M33 | Biến nhiệt động học hoặc nội lực xoắn |
| $u, v$ | Chuyển vị dọc trục và chuyển vị đứng 2D | m (mm) | M23 | Trường chuyển vị trong mặt phẳng uốn |
| $U$ | Thế năng đàn hồi tích lũy | J (N·m) | M31 | Năng lượng biến dạng bảo toàn |
| $U_m, V_m$ | Hệ số chuỗi Fourier của chuyển vị không thứ nguyên | Không chiều | M23 | Biến trạng thái trong không gian Fourier |
| $V$ | Lực cắt ngang tại gối tựa hoặc thể tích RVE | N hoặc m³ | M17, M20 | $V = F_0$ (M17); $V_{\text{RVE}}$ (M20) |
| $w$ | Độ võng uốn của dầm tại điểm giữa | m (mm) | M17, M22, M23 | Chuyển vị thẳng đứng dưới tải uốn |
| $W$ | Tổng công do ngoại lực thực hiện | J (N·m) | M13, M31 | $W = U + W_f$ |
| $x, y, z$ | Hệ tọa độ Descartes không gian | m | Tất cả | $x$: dọc trục, $y$: chiều dày, $z$: chiều rộng |
| $y_s$ | Tọa độ ranh giới trượt qua chiều dày dầm | m | M18 | Vị trí chuyển tiếp giữa dính và trượt |

---

## 3. BẢNG TRA CỨU KÝ HIỆU CHỮ HY LẠP (GREEK SYMBOLS)

| Ký hiệu | Tên gọi & Ý nghĩa vật lý | Đơn vị SI | Xuất hiện trong | Lưu ý ngữ cảnh |
|---|---|---|---|---|
| $\alpha_i, \alpha_f$ | Góc nâng bước ban đầu và kết thúc của lò xo xoắn | rad (độ) | M34 | Góc nghiêng đường xoắn ốc |
| $\beta, \boldsymbol{\beta}_S$ | Tensor biến dạng riêng (eigenstrain) | Không chiều | M24 | Biến dạng không tương thích mô tả trượt dây |
| $\gamma, \gamma_i$ | Biến dạng trượt cắt hoặc hệ số độ cứng EBSC | Không chiều | M20, M23, M24 | Biến dạng cắt (M20, M24) hoặc $\gamma = 1/\delta$ (M23) |
| $\gamma_L$ | Biến dạng trượt dư chuyển pha cực đại của SMA | Không chiều | M34 | Giới hạn chuyển pha trong lò xo xoắn ($\approx 0.056$) |
| $\delta$ | Độ võng uốn, chiều dày lớp đơn, hoặc hệ số DMC | m hoặc không chiều | M18, M22, M23, M31, M32 | **Xem ngữ cảnh:** bề dày lớp (M18), độ võng (M31, M32), DMC (M22, M23) |
| $\Delta u_i$ | Độ dịch chuyển trượt tương đối tại giao diện thứ $i$ | m (mm) | M23 | $\Delta u_i = u^{(i+1)} - u^{(i)}$ |
| $\varepsilon, \varepsilon_{ij}$ | Tensor biến dạng toàn phần | Không chiều | M24, M29, M33 | Biến dạng cơ học |
| $\varepsilon^{\text{tr}}, \varepsilon^{\text{th}}, \varepsilon^{\text{e}}$ | Các thành phần biến dạng chuyển pha, nhiệt và đàn hồi | Không chiều | M29 | Phân rã biến dạng gia số SMA |
| $\zeta$ | Tọa độ không thứ nguyên hóa theo chiều dày dầm | Không chiều | M23 | $\zeta = y / H \in [0, 1]$ |
| $\eta$ | Hệ số nhớ hình nội tại | Không chiều | M29 | Biến trạng thái nhiệt động học SMA |
| $\theta$ | Góc xoay uốn hoặc góc tiếp tuyến trục dầm cong | rad | M13, M18, M31 | $d\theta/ds = \kappa$ (độ cong) |
| $\kappa$ | Độ cong uốn của trục dầm | 1/m | M18, M22, M35 | $\kappa = 1/r = M / (EI)$ |
| $\lambda, \lambda_i$ | Hằng số Lamé hoặc nghiệm đặc trưng phương trình vi phân | Pa hoặc 1/m | M20, M22 | Đặc tính đàn hồi (M20) hoặc số sóng uốn (M22) |
| $\Lambda_{ij}$ | Tensor định hướng dòng chuyển pha SMA | Không chiều | M29 | Đồng trục với tensor ứng suất lệch |
| $\mu$ | Hệ số ma sát Coulomb hoặc hệ số Poisson | Không chiều | M13, M17, M18, M19, M23, M31 | **Xem cảnh báo mục 1** (Ma sát ở M17/M18; Poisson ở M23!) |
| $\boldsymbol{\mu}$ | Vector độ cong uốn và xoắn kết cấu | rad/m | M24 | Biến dạng góc tổng thể dầm cáp |
| $\nu$ | Hệ số Poisson của vật liệu | Không chiều | M17, M34 | $\nu \approx 0.156$ (giấy), $\nu \approx 0.33$ (kim loại) |
| $\xi$ | Phân số thể tích martensite hoặc hệ số góc hiệu chuẩn | Không chiều | M22, M29, M34 | $\xi \in [0, 1]$ (M29, M34) hoặc hệ số $k(\bar{\sigma})$ (M22) |
| $\rho$ | Bán kính cong uốn | m | M13 | $\rho = 1/\kappa = EI / M$ |
| $\sigma, \sigma_{ij}$ | Tensor ứng suất pháp hoặc ứng suất cơ học | Pa (MPa) | M18, M19, M20, M23, M29 | Trường ứng suất nội tại |
| $\bar{\sigma}$ | Ứng suất kéo căng trung bình hoặc ứng suất von Mises | Pa (MPa) | M20, M22, M29 | $\bar{\sigma} = F/A$ (M22) hoặc von Mises (M29) |
| $\sigma_y$ | Ứng suất nén vuông góc mặt tiếp xúc giữa các lớp | Pa | M23 | Biến trạng thái tiếp xúc 2D |
| $\sigma_{\text{MS}}, \sigma_{\text{MF}}$ | Ứng suất bắt đầu và kết thúc chuyển pha thuận SMA | Pa (MPa) | M29 | Phụ thuộc nhiệt độ theo quan hệ Clausius-Clapeyron |
| $\sigma_{\text{AS}}, \sigma_{\text{AF}}$ | Ứng suất bắt đầu và kết thúc chuyển pha nghịch SMA | Pa (MPa) | M29 | Xác định giới hạn dỡ tải |
| $\tau, \tau_{xy}$ | Ứng suất tiếp xúc cắt hoặc ứng suất xoắn | Pa (MPa) | M17, M18, M19, M23, M34 | Ứng suất truyền lực ma sát |
| $\tau_{\text{slip}}$ | Giới hạn ứng suất ma sát Coulomb | Pa | M17 | $\tau_{\text{slip}} = \mu p$ |
| $\Theta_{ij}$ | Tensor hệ số giãn nở nhiệt của SMA | 1/K | M29 | Biến dạng nhiệt |

---

## 4. BẢNG TRA CỨU MA TRẬN VÀ KÝ HIỆU CHỈ SỐ DƯỚI (MATRICES & SUBSCRIPTS)

| Ký hiệu | Ý nghĩa cơ học | Xuất hiện trong |
|---|---|---|
| $[\mathbf{K}_i]$ | Ma trận hệ số phương trình trạng thái của lớp thứ $i$ ($4 \times 4$) | M23 |
| $[\mathbf{T}_i]$ | Ma trận truyền biến trạng thái qua chiều dày lớp thứ $i$ ($[\mathbf{T}_i] = e^{[\mathbf{K}_i]\Delta\zeta_i}$) | M23 |
| $[\mathbf{C}_i]$ | Ma trận ghép nối điều kiện trượt tại giao diện thứ $i$ có phần tử $E_0/(k_i h_0)$ | M23 |
| $[\mathbf{T}]$ | Ma trận truyền tổng thể toàn bộ mặt cắt: $[\mathbf{T}] = [\mathbf{T}_n][\mathbf{C}_{n-1}]\cdots[\mathbf{C}_1][\mathbf{T}_1]$ | M23 |
| $\text{p-s}$ | Pre-slip (pha chưa trượt, liên kết dính hoàn toàn) | M17 |
| $\text{pa-s}$ | Partial-slip (pha trượt một phần, trượt tại các giao diện trung tâm) | M17 |
| $\text{f-s}$ | Full-slip (pha trượt toàn phần, tất cả các giao diện đều trượt) | M17 |
| $J, S$ | Jammed state (trạng thái kẹt) và Slipped state (trạng thái trượt) | M13 |
| $m, a$ | Martensite state (nhiệt độ thấp) và Austenite state (nhiệt độ cao) của SMA | M31, M34 |
