# MP1 READING PACK — WP-B EQUATION READING NOTES
## Jamming and Friction Mechanics

- **Task ID:** MP1-LR-P2-EQ-R1
- **Package:** WP-B (Jamming and Friction Mechanics)
- **Status:** VERIFIED_FULL_TEXT
- **Target Thesis Sections:** C1.2.1, C1.2.2, C2.1, C2.2, C2.3, C2.5

---

## 1. TỔNG QUAN NHÓM PHƯƠNG TRÌNH WP-B

Nhóm phương trình WP-B tập trung vào cơ học tiếp xúc, ma sát và biến thiên độ cứng uốn của các cấu trúc kẹt lớp (layer/laminar jamming) và kẹt sợi (fiber jamming). Các tài liệu cốt lõi bao gồm:
- **M17 (Caruso et al., 2023):** Mô hình giải tích rời rạc từng pha (pre-slip, partial-slip, full-slip) cho dầm kẹt lớp chịu uốn 3 điểm, tích hợp điều kiện biên kẹp ngoài gối (clamped overhang).
- **M18 (Zhang et al., 2025):** Mô hình môi trường liên tục (continuum-based) cho dầm kẹt lớp cong, giải tích chính xác sự lan truyền của ranh giới trượt $y_s$ qua chiều dày mặt cắt dưới lực cắt ngang $Q$.
- **M13 (Zhang & Yao, 2026):** Mô hình kẹt sợi dưới áp suất dương, cân bằng công - năng lượng trong pha trượt và mô hình suy giảm độ cứng bậc hai (phenomenological quadratic model).
- **M19 (Zhang et al., 2025):** Phân bố ứng suất pháp trong các lớp trượt và luật ma sát Coulomb gia số.
- **M20 (Zhang et al., 2025/2026):** Mô hình đồng hóa vi mô - vĩ mô (RVE homogenization) cho vật liệu kẹt lớp liên tục.

---

## 2. GHI CHÚ CHI TIẾT TỪNG PHƯƠNG TRÌNH ĐƯỢC CHỌN

---

### NOTE B-01: M17 Eqs. (1)–(3) — Tải trọng trượt ban đầu và độ cứng pha chưa trượt (Pre-slip)

#### A. Source Identity
- **Paper ID:** M17
- **Title:** Layer jamming: Modeling and experimental validation
- **Authors:** F. Caruso, S. Mintchev et al.
- **Year:** 2023
- **DOI:** 10.1016/j.ijmecsci.2023.108325
- **Evidence ID:** M17-E02
- **Equation Number:** Eqs. (1), (2), (3)
- **PDF Page:** 3
- **Printed Page:** 3 (Article 108325)
- **SHA-256:** `652e62758f1f7d2d3ce6b0333d45d8b2d7085c88b77054f48483f2dc98305c6a`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 3):

$$F_0 = \frac{2 \tau_{\text{slip}} A}{3}$$

$$w_0 = \frac{2 F_0 L^3}{48 E I_{\text{p-s}}}$$

$$I_{\text{p-s}} = \frac{16 b h^3}{3}$$

Trong đó $\tau_{\text{slip}} = \mu p$ và $A = 4 b h$.

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị gốc / SI | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $F_0$ | Lực cắt ngang danh định gây trượt tại giao diện giữa | N | Lực thành phần tại nửa nhịp ($V = F_0$); tổng tải trọng tác dụng tại giữa nhịp là $2F_0$ | Phân bố ứng suất cắt Jourawski bậc hai trên mặt cắt chữ nhật đặc |
| $\tau_{\text{slip}}$ | Giới hạn ứng suất tiếp xúc ma sát | Pa (N/m²) | $\tau_{\text{slip}} = \mu p$ | Định luật ma sát Coulomb trượt khô cục bộ |
| $\mu$ | Hệ số ma sát tĩnh giữa các lớp | Không chiều | Hệ số ma sát giữa bề mặt các lớp giấy (Fabriano Copy2) | Không đổi theo vận tốc trượt và áp suất |
| $p$ | Áp suất chân không giữ chặt các lớp | Pa (kPa) | Chênh lệch áp suất tạo bởi bơm chân không Piab | Phân bố đều hoàn toàn trên toàn bộ bề mặt |
| $A$ | Diện tích mặt cắt ngang tổng thể (4 lớp) | m² | $A = 4bh$ (chiều cao tổng $H = 4h$) | Mặt cắt chữ nhật đồng đều, không khe hở |
| $b$ | Chiều rộng của một lớp | m (mm) | Chiều rộng mặt cắt dầm ($b = 60$ mm trong thí nghiệm) | Chiều rộng đồng đều giữa các lớp |
| $h$ | Chiều dày của một lớp đơn lẻ | m (mm) | Chiều dày danh định của một tờ giấy ($h = 0.1$ mm) | Các lớp có chiều dày bằng nhau |
| $w_0$ | Độ võng tại điểm giữa dầm tại thời điểm chớm trượt | m (mm) | Độ võng uốn 3 điểm đàn hồi tuyến tính ứng với tải $2F_0$ | Dầm Euler-Bernoulli đặt trên 2 gối tựa đơn nhịp $L$ |
| $L$ | Khoảng cách giữa hai gối đỡ | m (mm) | Chiều dài nhịp tựa trong thí nghiệm 3 điểm ($L = 100$ mm) | Gối đỡ con lăn cứng, bỏ qua lún tiếp xúc |
| $E$ | Mô đun đàn hồi Young của vật liệu làm lớp | Pa (GPa) | Mô đun kéo của giấy ($E = 1.7$ GPa) | Vật liệu đẳng hướng, đàn hồi tuyến tính |
| $I_{\text{p-s}}$ | Mô men quán tính diện tích trong pha pre-slip | m⁴ | $I_{\text{p-s}} = b(4h)^3/12 = 16bh^3/3$ | Các lớp dính chặt hoàn toàn (no-slip), dầm hoạt động như thanh đặc nguyên khối |

#### D. Mechanical Interpretation (Giải thích cơ học)
1. **Quá trình vật lý:** Mô tả trạng thái đàn hồi ban đầu khi toàn bộ cấu trúc gồm 4 lớp hoạt động như một dầm đặc đồng nhất (solid beam). Dưới tải trọng uốn 3 điểm, ứng suất cắt dọc trục $\tau_{xy}$ xuất hiện do đạo hàm của mô men uốn. Ứng suất này lớn nhất tại trục trung hòa (giao diện giữa lớp 2 và lớp 3).
2. **Liên hệ giữa các đại lượng:** Theo công thức Jourawski cho mặt cắt chữ nhật, $\tau_{\max} = \frac{3V}{2A}$. Khi $\tau_{\max}$ đạt ngưỡng ma sát Coulomb $\tau_{\text{slip}} = \mu p$, lực cắt $V = F_0$ thỏa mãn $F_0 = \frac{2}{3} \tau_{\text{slip}} A = \frac{8}{3} \mu p b h$. Độ võng $w_0$ tỷ lệ thuận với tải trọng $2F_0 L^3$ và tỷ lệ nghịch với độ cứng uốn nguyên khối $E I_{\text{p-s}}$.
3. **Đại lượng đầu vào (Input):** Hình học dầm ($b, h, L$), số lớp ($n=4$), đặc tính vật liệu ($E, \mu$), và áp suất chân không ($p$).
4. **Đại lượng đầu ra (Output):** Ngưỡng lực gây trượt đầu tiên ($F_0$), mô men quán tính pha chưa trượt ($I_{\text{p-s}}$), và độ võng tại giới hạn đàn hồi ($w_0$).
5. **Giả thiết chi phối:**
   - (i) Áp suất giam $p$ truyền đều và trực tiếp thành lực pháp tuyến trên giao diện mà không có suy giảm qua màng bọc.
   - (ii) Trượt tuân theo ngưỡng Coulomb sắc nét; không có dão đàn nhớt (creep) hoặc vi trượt (micro-slip) trước khi đạt $\mu p$.
   - (iii) Dầm tuân theo động học Euler-Bernoulli (bỏ qua biến dạng cắt của dầm mỏng $H \ll L$).
6. **Điều kiện đúng:** Đúng khi tải trọng ngoài $F_{\text{ext}} \le 2F_0$, trong miền biến dạng bé và khi các lớp chưa hề trượt tương đối.
7. **Suy luận khi thay đổi tham số:**
   - Tăng áp suất $p$ hoặc hệ số ma sát $\mu$ làm tăng tuyến tính ngưỡng lực trượt $F_0$ và độ võng tới hạn $w_0$, nhưng **không** làm thay đổi độ cứng ban đầu ($E I_{\text{p-s}}$ không phụ thuộc $p$).
   - Tăng số lớp hoặc chiều dày $h$ làm tăng độ cứng theo bậc 3 của chiều cao tổng thể ($H^3$).
8. **Điều không cho phép kết luận:** Phương trình **không** cho phép kết luận rằng độ cứng uốn của dầm thay đổi theo áp suất trong pha pre-slip; trong pha này, độ cứng hoàn toàn cố định và bằng dầm đặc ($E I_{\text{solid}}$).

#### E. Relation to MP1
- **Khả năng áp dụng:** Áp dụng theo phép tương tự (Analogy only / Applicable with assumptions). Cấu trúc MP1 là bó dây (wire bundle) hoặc thanh TiNi, tiếp xúc hình học tròn-tròn hoặc tròn-ống, không phải mặt cắt chữ nhật phẳng.
- **Điều chỉnh cần thiết:** Công thức Jourawski $\tau_{\max} = 1.5 V/A$ chỉ đúng cho mặt cắt chữ nhật; đối với bó dây tròn hoặc mặt cắt phức tạp, hệ số phân bố ứng suất cắt khác 1.5. Lực pháp tuyến không đồng nhất với áp suất thủy tĩnh $p$ do hiệu ứng vòm (arching effect) và hình học cong của dây.
- **Sử dụng làm baseline:** Có thể dùng $F_0$ làm giới hạn trên lý tưởng (idealized upper bound) cho tải trọng kích hoạt trượt nếu quy đổi diện tích tiếp xúc tương đương.
- **Đại lượng cần đo độc lập:** Hệ số ma sát $\mu$ giữa các dây/lớp dưới áp suất thực tế; mô đun đàn hồi $E$ của vật liệu; hiệu suất truyền áp suất từ buồng khí vào bề mặt tiếp xúc.
- **Kiểm chứng thực nghiệm:** Kiểm chứng trực tiếp qua điểm gãy khúc (yield point) trên đường cong lực - độ võng ($F - \delta$) trong thí nghiệm uốn 3 điểm.
- **Thông tin chưa biết ở MP1:** Trở lực ma sát của vỏ bọc mềm và độ phân bố áp suất dọc chu vi bó dây.

#### F. Validation Evidence
- **Phương pháp:** Thí nghiệm uốn 3 điểm trên máy kéo nén MTS Alliance RT/30 (load cell 1 kN, độ phân giải 0.01 N, vận tốc 5 mm/min) kết hợp mô phỏng phần tử hữu hạn Abaqus 2D (phần tử CPE4RH, surface-to-surface contact penalty).
- **Đại lượng đo:** Lực uốn $F$ và độ võng giữa nhịp $w$.
- **Điều kiện thí nghiệm:** Mẫu giấy Fabriano 4, 8, 12, 16, 20 lớp; nhịp $L = 100$ mm; áp suất chân không 24, 48, 68 kPa.
- **Mức độ phù hợp:** Khớp rất tốt với mô phỏng FEA và thực nghiệm trong pha ban đầu (sai số dưới 5% cho độ dốc ban đầu).
- **Hạn chế:** Tác giả bỏ qua ma sát tại gối đỡ con lăn và giả định tiếp xúc hoàn hảo không có độ nhăn của màng TPU.

---

### NOTE B-02: M17 Eqs. (5)–(7) & (8)–(15) — Lan truyền trượt từng pha và suy giảm độ cứng dầm kẹt lớp

#### A. Source Identity
- **Paper ID:** M17
- **Title:** Layer jamming: Modeling and experimental validation
- **Evidence ID:** M17-E03
- **Equation Number:** Eqs. (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15)
- **PDF Page:** 4
- **Printed Page:** 4 (Article 108325)
- **SHA-256:** `652e62758f1f7d2d3ce6b0333d45d8b2d7085c88b77054f48483f2dc98305c6a`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 4):

Đối với cấu trúc 4 lớp có phần nhô ngoài gối đỡ (overhanging portion):

$$w_1 = \frac{2 F_1 L^3}{192 E I_{\text{pa-s}}}$$

$$I_{\text{pa-s}} = \frac{4 b h^3}{3}$$

$$I_{\text{f-s}} = \frac{b h^3}{3}$$

Công thức tổng quát cho cấu trúc $n$ lớp ($n$ chẵn):

$$F_0 = \frac{2 \mu p b h n}{3}$$

$$F_1 = \frac{\mu p b h n}{3(n - 2)}$$

$$F_2 = \frac{2 \mu p b h (n^2 - 6n + 12)}{3(n^2 - 6n + 8)}$$

$$F_i = \frac{2 \mu p b h (n^3 - 6(i-1)n^2 + 12(i-1)^2 n - 4n - 8(i^3 - 3i^2 + 2i))}{3(n^3 - 6(i-1)n^2 + (12(i-1)^2 - 4)n - 8(i^3 - 3i^2 + 2i))} \quad (i = 3, \dots, n/2 - 1)$$

$$w_0 = \frac{\mu p L^3}{3 E h^2 n^2}$$

$$w_1 = \frac{\mu p L^3}{6 E h^2 n^2 (n - 2)}$$

$$w_2 = \frac{\mu p L^3}{6 E h^2 n (n^2 - 6n + 8)}$$

$$w_i = \frac{\mu p L^3}{3 E h^2 (n^3 - 6(i-1)n^2 + (12(i-1)^2 - 4)n - 8(i^3 - 3i^2 + 2i))} \quad (i = 3, \dots, n/2 - 1)$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $F_i$ | Tải trọng gia số kích hoạt trượt tại cặp giao diện thứ $i$ | N | Gia số lực ngoài làm ứng suất cắt tại giao diện $i$ đạt $\mu p$ | Các giao diện trượt đối xứng từ tâm ra ngoài |
| $w_i$ | Độ võng gia số trong pha trượt thứ $i$ | m | Biến dạng bổ sung khi dầm chuyển sang độ cứng giảm tiếp theo | Vùng ngoài gối đỡ hoạt động như ngàm đàn hồi |
| $I_{\text{pa-s}}$ | Mô men quán tính trong pha partial-slip (4 lớp) | m⁴ | Bằng tổng mô men quán tính của hai dầm 2 lớp riêng biệt: $2 \times [b(2h)^3/12] = 4bh^3/3$ | Giao diện trung tâm trượt tự do không ma sát dư |
| $I_{\text{f-s}}$ | Mô men quán tính trong pha full-slip (4 lớp) | m⁴ | Bằng tổng mô men quán tính của 4 lớp riêng rẽ: $4 \times [bh^3/12] = bh^3/3$ | Tất cả các giao diện trượt tự do hoàn toàn |
| $n$ | Tổng số lớp trong cấu trúc dầm kẹt | Không chiều | Số nguyên dương chẵn ($n = 4, 8, 12, 16, 20$) | Các lớp hoàn toàn đồng nhất về kích thước và vật liệu |
| 192 | Hệ số uốn cho dầm ngàm hai đầu (clamped-clamped) | Không chiều | Xuất phát từ công thức Euler-Bernoulli: $w = P L^3 / (192 E I)$ | Phần dầm ngoài gối chưa trượt cản trở xoay góc tự do |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô tả sự suy giảm độ cứng từng bước (piecewise linear degradation) của dầm kẹt lớp. Khi tải trọng tăng, trượt khởi phát từ giao diện trung tâm ($i=0$), sau đó lan dần sang các giao diện lân cận ($i=1, 2, \dots$) cho đến khi toàn bộ các lớp trượt lên nhau (full-slip).
2. **Liên hệ giữa các đại lượng:**
   - Trong pha 4 lớp: $I_{\text{p-s}} = \frac{16}{3}bh^3 \to I_{\text{pa-s}} = \frac{4}{3}bh^3 \to I_{\text{f-s}} = \frac{1}{3}bh^3$. Tỷ lệ độ cứng suy giảm chính xác là $16 : 4 : 1$ (tương ứng $n^2$ khi so sánh solid beam với $n$ lớp rời rạc).
   - Sự xuất hiện của hệ số 192 thay vì 48 phản ánh hiệu ứng "đảo chiều độ cong" (curvature reversal) do phần dầm nhô ra ngoài gối đỡ chưa trượt giữ chặt mép, tạo thành liên kết ngàm đàn hồi.
3. **Input:** Kích thước lớp ($b, h, L$), số lớp $n$, áp suất $p$, hệ số ma sát $\mu$, mô đun $E$.
4. **Output:** Dãy lực chuyển pha $F_i$, dãy độ võng gia số $w_i$, và các mức mô men quán tính $I_i$.
5. **Giả thiết chi phối:**
   - Khi một giao diện bắt đầu trượt, nó trượt hoàn toàn trên toàn bộ chiều dài giữa hai gối đỡ.
   - Ứng suất ma sát sau khi trượt được xem là hằng số hoặc bỏ qua trong tính toán gia số độ cứng bổ sung.
6. **Điều kiện đúng:** Thí nghiệm uốn 3 điểm có phần dầm nhô ra ngoài hai gối đỡ (overhanging beam), biến dạng uốn bé.
7. **Suy luận khi thay đổi tham số:**
   - Khi $n \to \infty$, khoảng cách giữa các mức lực trượt $F_i$ thu hẹp lại, đường cong lực - biến dạng chuyển từ đường gãy khúc rời rạc sang đường cong liên tục phi tuyến.
   - Độ cứng trạng thái khóa cứng tỷ lệ với $n^3$, trong khi độ cứng trạng thái trượt hoàn toàn tỷ lệ với $n$. Do đó dải điều chỉnh độ cứng (stiffness tuning ratio) tỷ lệ thuận với $n^2$.
8. **Điều không cho phép kết luận:** Không cho phép kết luận rằng độ cứng trong pha trượt hoàn toàn bằng 0; nó vẫn giữ độ cứng uốn dư bằng tổng độ cứng của $n$ lớp độc lập ($n \times E I_{\text{layer}}$).

#### E. Relation to MP1
- **Khả năng áp dụng:** Áp dụng có giả thiết (Applicable with assumptions). Cung cấp cơ chế giải thích sự chuyển tiếp giữa các trạng thái độ cứng cho hệ kẹt ma sát nhiều phần tử.
- **Điều chỉnh:** Trong bó dây TiNi của MP1, các dây tiếp xúc theo mạng lưới đường tiếp xúc 3D (contact lines), sự trượt không diễn ra đồng thời theo từng mặt phẳng ngang mà trượt cục bộ theo góc tiếp xúc azimuthal.
- **Sử dụng làm baseline:** Tỷ số điều chỉnh độ cứng lý thuyết $n^2$ là cận trên chuẩn mực (benchmark) để đánh giá hiệu quả của cơ cấu kẹt bó dây trong MP1.
- **Đại lượng cần đo độc lập:** Đo đường cong $F - \delta$ chu kỳ tải và dỡ tải để xác định các điểm chuyển tiếp độ dốc.

#### F. Validation Evidence
- **Phương pháp:** Đo đạc thực nghiệm trên 4 mẫu (8, 12, 16, 20 lớp giấy Fabriano) tại áp suất 68 kPa và mẫu 20 lớp tại 24, 48, 68 kPa.
- **Mức độ phù hợp:** Mô hình giải tích dự đoán chính xác sự tăng độ cứng do phần nhô ngoài gối đỡ và độ võng chuyển tiếp, sai số so với FEA và thực nghiệm dưới 8% trên toàn dải tải trọng.

---

### NOTE B-03: M18 Eqs. (1)–(2) — Phương trình vi phân cân bằng dầm kẹt lớp cong (Continuum Formulation)

#### A. Source Identity
- **Paper ID:** M18
- **Title:** A continuum-based model for a layer jamming beam
- **Authors:** S. Zhang, J. Yao, Y. Ding, J. Hong, P. Fang
- **Year:** 2025
- **DOI:** 10.5194/ms-16-821-2025
- **Evidence ID:** M18-E04
- **Equation Number:** Eqs. (1), (2)
- **PDF Page:** 3
- **Printed Page:** 823 (Mech. Sci., 16, 821–830)
- **SHA-256:** `95646b2cfca7f40776997f74c7dbb949cfeb3c14c501e5648f58b68b75fcf3d1`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 3):

$$\begin{cases} \frac{dN}{ds} = -Q \frac{d\theta}{ds} - q_s \\ \frac{dQ}{ds} = N \frac{d\theta}{ds} - q_y \\ \frac{dM}{ds} = -Q \end{cases} \quad \Longleftrightarrow \quad \begin{cases} \frac{dN}{ds} = -\frac{Q}{r} - q_s \\ \frac{dQ}{ds} = \frac{N}{r} - q_y \\ \frac{dM}{ds} = -Q \end{cases}$$

$$\begin{bmatrix} N(s) \\ Q(s) \end{bmatrix} = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} \left( \begin{bmatrix} N_0 \\ Q_0 \end{bmatrix} + \int_0^s \begin{bmatrix} \cos\theta(\xi) & -\sin\theta(\xi) \\ \sin\theta(\xi) & \cos\theta(\xi) \end{bmatrix} \begin{bmatrix} -q_s(\xi) \\ -q_y(\xi) \end{bmatrix} d\xi \right)$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $s$ | Tọa độ độ dài cung dọc trục trung hòa | m | Tọa độ cong nội tại của dầm | Đường trục cong trơn, khả vi liên tục |
| $N(s)$ | Lực pháp tuyến (lực dọc trục) tại mặt cắt $s$ | N | Thành phần lực nội tại tiếp tuyến với trục dầm | Bỏ qua biến dạng dãn dài trục nếu giả thiết không dãn |
| $Q(s)$ | Lực cắt ngang tại mặt cắt $s$ | N | Thành phần lực nội tại vuông góc với trục dầm | Cân bằng lực vi phân trên phần tử cong $ds$ |
| $M(s)$ | Mô men uốn tại mặt cắt $s$ | N·m | Mô men nội tại quanh trục uốn | Cân bằng mô men vi phân bỏ qua đại lượng bậc 2 ($ds^2$) |
| $\theta(s)$ | Góc nghiêng tiếp tuyến của trục dầm | rad | Góc hợp bởi tiếp tuyến trục dầm với phương ngang | Biến dạng hình học phẳng trong mặt phẳng uốn |
| $r(s)$ | Bán kính cong tại vị trí $s$ | m | $1/r = d\theta/ds = \kappa$ (độ cong) | Độ cong biến thiên trơn |
| $q_s, q_y$ | Tải trọng phân bố ngoài dọc trục và vuông góc trục | N/m | Lực phân bố từ áp suất giam hoặc tải môi trường | Phân bố tải tác dụng liên tục |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Thiết lập hệ phương trình cân bằng tĩnh học vi phân cho phần tử dầm cong biến dạng lớn (curved beam element) dưới hệ tọa độ tự nhiên $(s, y)$.
2. **Liên hệ giữa các đại lượng:**
   - Phương trình thể hiện sự ghép cặp hình học chặt chẽ giữa lực dọc $N$ và lực cắt $Q$ thông qua độ cong $d\theta/ds = 1/r$.
   - Khi dầm cong, lực cắt sinh ra thành phần làm thay đổi lực dọc, và lực dọc đóng góp vào phương trình cân bằng lực cắt.
   - Phương trình đạo hàm mô men $dM/ds = -Q$ giữ nguyên dạng cổ điển nhưng được giải đồng thời với phân bố biến dạng hình học lớn.
3. **Input:** Tải trọng biên ($N_0, Q_0, M_0$), tải trọng phân bố ($q_s, q_y$), quy luật độ cong $\theta(s)$.
4. **Output:** Phân bố nội lực toàn diện $N(s), Q(s), M(s)$ dọc theo chiều dài dầm.
5. **Giả thiết:** Trục dầm không dãn dài đáng kể; biến dạng cắt không làm mất tính trực giao vi phân của mặt cắt ngang tại trục dầm.
6. **Điều kiện đúng:** Đúng cho dầm cong phẳng trong mặt phẳng 2D, áp dụng được cho chuyển vị lớn và góc xoay lớn.
7. **Suy luận:** Trong robot mềm liên tục biến dạng cong lớn, nội lực cắt $Q(s)$ thay đổi liên tục dọc theo thân robot. Vì ngưỡng trượt kẹt ma sát phụ thuộc trực tiếp vào $Q$, sự trượt sẽ bắt đầu cục bộ tại điểm có $|Q(s)|$ lớn nhất thay vì diễn ra đồng đều trên toàn thân dầm.
8. **Giới hạn:** Phương trình cân bằng tĩnh học thuần túy, chưa chứa phương trình cấu tạo (constitutive relation) của vật liệu hay điều kiện trượt tiếp xúc.

#### E. Relation to MP1
- **Khả năng áp dụng:** Áp dụng có giả thiết (Applicable with assumptions). Cung cấp khung cân bằng nội lực chính xác cho dầm mềm kẹt ma sát ở cấu hình uốn cong lớn (large deflection continuum beam).
- **Cần điều chỉnh:** MP1 cần tích hợp thêm lực nén pháp tuyến sinh ra bởi cơ cấu kẹp chủ động (áp suất dương hoặc lực kéo cáp/dây SMA).

---

### NOTE B-04: M18 Eqs. (3) & (5) — Phân bố ứng suất cắt và ngưỡng lực cắt khởi phát trượt $Q_{\text{slip}}$

#### A. Source Identity
- **Paper ID:** M18
- **Title:** A continuum-based model for a layer jamming beam
- **Evidence ID:** M18-E05
- **Equation Number:** Eqs. (3), (5)
- **PDF Page:** 4
- **Printed Page:** 824 (Mech. Sci., 16, 821–830)
- **SHA-256:** `95646b2cfca7f40776997f74c7dbb949cfeb3c14c501e5648f58b68b75fcf3d1`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 4):

$$\tau(y, Q) = \frac{3 Q}{2 A} \left(1 - \frac{4 y^2}{h^2}\right)$$

$$Q_{\text{slip}} = \frac{2}{3} \mu p b h$$

Trong đó $A = b h$ là diện tích mặt cắt chữ nhật, $h$ là tổng chiều cao dầm, $b$ là chiều rộng dầm, và $y \in [-h/2, h/2]$.

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $\tau(y, Q)$ | Ứng suất cắt tại vị trí cách trục trung hòa khoảng cách $y$ | Pa | Phân bố ứng suất cắt Jourawski theo chiều cao dầm | Trạng thái dầm đặc đàn hồi chưa trượt (full-jamming state) |
| $Q$ | Lực cắt ngang tác dụng lên mặt cắt | N | Nội lực cắt ngang tại tọa độ $s$ | Lực cắt cân bằng tĩnh |
| $A$ | Diện tích mặt cắt ngang tổng thể | m² | $A = b h$ | Mặt cắt chữ nhật đặc |
| $h$ | Tổng chiều cao của toàn bộ dầm kẹt lớp | m | Khoảng cách từ mặt đáy đến mặt đỉnh dầm | Chiều dày danh định tổng các lớp |
| $b$ | Chiều rộng của dầm | m | Chiều rộng mặt cắt | Chiều rộng không đổi |
| $y$ | Tọa độ vuông góc với trục trung hòa | m | Gốc $y = 0$ tại trục trung hòa, $y \in [-h/2, h/2]$ | Trục đối xứng hình học |
| $Q_{\text{slip}}$ | Lực cắt tới hạn khởi phát trượt cục bộ | N | Giá trị $Q$ tại đó $\max_y \tau(y, Q) = \mu p$ | Đạt ngưỡng Coulomb tại trục trung hòa $y = 0$ |
| $p$ | Áp suất kẹt giam giữ các lớp | Pa | Áp suất thủy tĩnh duy trì trạng thái kẹt | Phân bố đều |
| $\mu$ | Hệ số ma sát tĩnh tiếp xúc giữa các lớp | Không chiều | Hệ số ma sát Coulomb | Đẳng hướng và không đổi |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Thiết lập mối liên hệ giữa nội lực cắt vĩ mô $Q$ và trường ứng suất cắt vi mô $\tau(y)$ trên mặt cắt dầm. Xác định thời điểm chính xác khi giao diện trung tâm bắt đầu trượt.
2. **Liên hệ giữa các đại lượng:**
   - Phân bố $\tau(y)$ có dạng parabol đối xứng, đạt cực đại tại tâm mặt cắt $y = 0$: $\tau_{\max} = \frac{3Q}{2A} = \frac{3Q}{2bh}$.
   - Tại mép biên tự do $y = \pm h/2$, ứng suất cắt bằng 0.
   - Đặt $\tau_{\max} = \mu p$, giải ra ngưỡng lực cắt gây trượt: $Q_{\text{slip}} = \frac{2}{3} \mu p b h = \frac{2}{3} \mu p A$.
3. **Input:** Lực cắt $Q$, áp suất $p$, hệ số ma sát $\mu$, kích thước mặt cắt ($b, h$).
4. **Output:** Trường ứng suất cắt $\tau(y)$ và giá trị tới hạn $Q_{\text{slip}}$.
5. **Giả thiết:** Mặt cắt tuân theo lý thuyết uốn kỹ thuật Saint-Venant / Jourawski; ứng suất nén pháp tuyến giữa các lớp bằng đúng áp suất chân không $p$.
6. **Điều kiện đúng:** Áp dụng khi dầm ở trạng thái khóa hoàn toàn (full-jamming state), tức $|Q| \le Q_{\text{slip}}$.
7. **Suy luận:** So sánh với M17 Eq. (1): Ở M17, $F_0 = \frac{2}{3}\tau_{\text{slip}}A$, và trong uốn 3 điểm lực cắt $V = F_0$, nên kết quả hoàn toàn trùng khớp về bản chất cơ học ($Q_{\text{slip}} = \frac{2}{3}\mu p b h$). M18 tổng quát hóa thành trường nội lực liên tục tại mọi mặt cắt $s$.
8. **Giới hạn:** Phương trình không mô tả được trạng thái sau khi trượt đã xảy ra (khi đó phân bố parabol bị bão hòa tại đỉnh).

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp điều kiện cục bộ khởi phát trượt (local slip onset criterion). Đối với bó dây song song của MP1, phân bố ứng suất cắt trên mặt cắt tròn không đồng đều như chữ nhật, nhưng nguyên lý trượt khởi phát tại tâm (nơi có độ dốc mô men uốn và ứng suất cắt lớn nhất) là tương đồng.

---

### NOTE B-05: M18 Eqs. (7)–(9) — Ranh giới trượt liên tục $y_s(Q)$ và phân bố ứng suất cắt pha nửa trượt

#### A. Source Identity
- **Paper ID:** M18
- **Title:** A continuum-based model for a layer jamming beam
- **Evidence ID:** M18-E05
- **Equation Number:** Eqs. (6), (7), (8), (9)
- **PDF Page:** 4
- **Printed Page:** 824
- **SHA-256:** `95646b2cfca7f40776997f74c7dbb949cfeb3c14c501e5648f58b68b75fcf3d1`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 4, đã kiểm tra trực quan ảnh quét):

$$\tau(y, s) = \begin{cases} \frac{3 Q}{2 A}\left(1 - \frac{4y^2}{h^2}\right), & |Q| \le Q_{\text{slip}} \\ \operatorname{sign}(Q)\mu p, & |y| \le y_s \text{ và } Q_{\text{slip}} \le |Q| \le Q_{\max} \\ \operatorname{sign}(Q)\mu p \frac{1 - 4y^2/h^2}{1 - 4y_s^2/h^2}, & |y| > y_s \text{ và } Q_{\text{slip}} \le |Q| \le Q_{\max} \\ c_2 y^2 \pm c_1 y + c_0, & |y| > y_s \text{ và } |Q| > Q_{\max} \end{cases}$$

$$Q_{\max} = \mu p b \frac{3h^2 - 6\delta h + 4\delta^2}{3(h - \delta)}$$

$$y_s = \begin{cases} 0, & |Q| < Q_{\text{slip}} \\ \frac{3Q - 2\mu p A + \sqrt{3(3Q - 2\mu p A)(Q + 2\mu p A)}}{8\mu p b}, & Q_{\text{slip}} \le Q < Q_{\max} \\ \frac{-3Q + 2\mu p A + \sqrt{3(3Q - 2\mu p A)(Q + 2\mu p A)}}{8\mu p b}, & -Q_{\max} < Q \le -Q_{\text{slip}} \\ h/2 - \delta, & |Q| \ge Q_{\max} \end{cases}$$

Trong đó $\delta$ là chiều dày của một lớp đơn lẻ.

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $y_s$ | Tọa độ ranh giới trượt (sliding boundary) | m | Vị trí phân tách giữa miền trượt ma sát ($|y| \le y_s$) và miền đàn hồi dính ($|y| > y_s$) | Ranh giới trượt đối xứng qua trục dầm |
| $Q_{\max}$ | Lực cắt giới hạn trên của pha nửa trượt (half-slipping) | N | Giá trị $Q$ khi miền dính chỉ còn lại đúng 1 lớp ngoài cùng có bề dày $\delta$ | Lớp ngoài cùng biên tự do không bao giờ trượt hoàn toàn |
| $\delta$ | Chiều dày của một lớp mỏng đơn lẻ | m | Kích thước một lớp vật liệu ($h = n\delta$) | Tất cả các lớp có chiều dày $\delta$ bằng nhau |
| $c_0, c_1, c_2$ | Các hệ số đa thức bậc hai của ứng suất cắt khi $|Q| > Q_{\max}$ | Pa/m², Pa/m, Pa | Xác định từ điều kiện biên $\tau(h/2) = 0$, $\tau(y_s) = \mu p$, và tích phân $\int_{-h/2}^{h/2} \tau dy = Q$ | Cân bằng lực cắt tổng thể trên mặt cắt |
| $\operatorname{sign}(Q)$ | Hàm dấu của lực cắt | Không chiều | Xác định chiều của lực ma sát ngược chiều chuyển động | Ma sát Coulomb trượt động |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Mô hình hóa sự lan truyền liên tục của vùng trượt qua chiều dày dầm kẹt lớp. Thay vì trượt rời rạc từng giao diện như M17, M18 xem dầm kẹt lớp như một môi trường liên tục tương đương có ranh giới chảy dẻo/trượt $y_s(Q)$ mở rộng từ tâm $y=0$ ra hai biên khi lực cắt $Q$ tăng.
2. **Liên hệ giữa các đại lượng:**
   - Khi $|Q| \le Q_{\text{slip}}$: $y_s = 0$, dầm hoàn toàn đàn hồi.
   - Khi $Q_{\text{slip}} < |Q| < Q_{\max}$: Vùng trung tâm $|y| \le y_s$ chịu ứng suất cắt bão hòa không đổi bằng $\mu p$. Vùng ngoài $|y| > y_s$ tiếp tục chịu ứng suất dạng parabol suy giảm về 0 tại mép ngoài.
   - Biểu thức của $y_s(Q)$ là hàm phi tuyến giải tích chứa căn thức bậc hai $\sqrt{3(3Q - 2\mu p A)(Q + 2\mu p A)}$, dẫn xuất từ điều kiện tích phân cân bằng lực cắt $\int_{-h/2}^{h/2} \tau dy = Q$.
3. **Input:** Lực cắt $Q$, áp suất $p$, hệ số ma sát $\mu$, hình học dầm ($b, h, \delta$).
4. **Output:** Tọa độ ranh giới trượt $y_s(Q)$ và trường ứng suất cắt chi tiết $\tau(y, s)$.
5. **Giả thiết:** Lớp ngoài cùng luôn có bề mặt tự do ($\tau = 0$ tại $y = \pm h/2$), do đó không thể trượt hoàn toàn; trượt đạt cực đại tại $y_s = h/2 - \delta$.
6. **Điều kiện đúng:** Áp dụng cho dầm có số lượng lớp lớn ($n \ge 8$), xem cấu trúc phân lớp xấp xỉ liên tục.
7. **Suy luận:** Cho phép tính toán chính xác tổn hao ma sát và độ cứng uốn biến thiên liên tục theo $Q$, giải quyết hạn chế của mô hình bước nhảy rời rạc trong các nghiên cứu trước năm 2024.
8. **Điều không cho phép kết luận:** Không áp dụng được cho cấu trúc kẹt hạt (granular jamming) hoặc bó sợi xoắn helix (do không thỏa mãn phân bố phẳng 2D).

#### E. Relation to MP1
- **Khả năng áp dụng:** Đây là mô hình tham chiếu cạnh tranh trực tiếp (core competitor/baseline) mạnh nhất của P1/MP1.
- **Vai trò:** Cung cấp công thức giải tích kiểm chứng giới hạn hợp lệ của mô hình liên tục (continuum validity limits) khi số lớp $n$ tăng cao.

---

### NOTE B-06: M13 Eqs. (1), (5)–(10) — Khởi phát trượt và độ cứng trạng thái trượt của kẹt sợi áp suất dương

#### A. Source Identity
- **Paper ID:** M13
- **Title:** A variable stiffness omnidirectional chain based on positive-pressure fiber jamming
- **Authors:** S. Zhang, J. Yao
- **Year:** 2026
- **DOI:** 10.5194/ms-17-481-2026
- **Evidence ID:** M13-E02
- **Equation Number:** Eqs. (1), (5), (6), (8), (9), (10)
- **PDF Page:** 3, 4
- **Printed Page:** 483, 484 (Mech. Sci., 17, 481–493)
- **SHA-256:** `3aa8790db0be1b0586e379d7ec4fe9be2a6d7139174f74d081ec352e0085a676`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (pp. 3–4):

$$\tau_{\max}(Q) = \mu p$$

$$W = \frac{1}{2} M \theta = \frac{M^2 l}{2 E I_S}$$

$$w_i^e = \frac{1}{2} m \theta = \frac{m^2 l}{2 E I_{\text{fib}}}$$

$$w_i^f = |s_i| \mu p c l$$

$$W = \sum_{i=1}^N \left( w_i^e + \frac{1}{2} w_i^f \right)$$

$$\frac{M^2 l}{2 E I_S} = \sum_{i=1}^N \left( \frac{m^2 l}{2 E I_{\text{fib}}} + \frac{1}{2} \frac{M l}{E I_S} y_i \mu p c l \right)$$

Định nghĩa mô men diện tích thứ nhất tương đương $y_C = \frac{1}{N} \sum_{i=1}^N |y_i|$, ta thu được mô men quán tính trạng thái trượt $I_S$:

$$I_S = N I_{\text{fib}} + \frac{1}{2} \mu p c l y_C \quad (\text{dạng tương đương sau giản ước})$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $M$ | Mô men uốn tác dụng lên bó sợi | N·m | Tải trọng uốn thuần túy tác dụng lên bó $N$ sợi | Uốn thuần túy, độ cong tròn đều $\rho = E I_S / M$ |
| $l$ | Chiều dài của bó sợi kẹt | m (mm) | Chiều dài làm việc của đoạn xích kẹt sợi | Bó sợi không dãn dài trục |
| $I_S$ | Mô men quán tính tương đương trong trạng thái trượt (slipping state) | m⁴ | Độ cứng uốn hiệu dụng trong pha trượt quy về Euler-Bernoulli: $E I_S$ | Chứa cả đóng góp đàn hồi riêng lẻ và tiêu tán ma sát |
| $N$ | Số lượng sợi trong bó | Không chiều | Tổng số sợi trong khoang kẹp | Các sợi sắp xếp song song, nén chặt |
| $I_{\text{fib}}$ | Mô men quán tính diện tích của một sợi đơn lẻ quanh trục riêng | m⁴ | $I_{\text{fib}} = \pi d^4 / 64$ cho sợi tròn đường kính $d$ | Tiết diện sợi tròn đều |
| $w_i^e$ | Năng lượng biến dạng đàn hồi uốn của sợi thứ $i$ | J (N·m) | $w_i^e = m^2 l / (2 E I_{\text{fib}})$ | Sợi uốn đàn hồi tuyến tính |
| $w_i^f$ | Công tiêu tán do ma sát trượt của sợi thứ $i$ | J (N·m) | $w_i^f = |s_i| \mu p c l$ | Ma sát Coulomb đều trên diện tích tiếp xúc $c \cdot l$ |
| $s_i$ | Độ dịch chuyển trượt tương đối của sợi thứ $i$ | m | $s_i = y_i \theta = y_i M l / (E I_S)$ | Mặt cắt phẳng tuân theo Bernoulli |
| $c$ | Chu vi tiếp xúc ma sát hiệu dụng của một sợi | m (mm) | Phần chu vi tiết diện sợi tham gia truyền lực tiếp xúc | Chu vi tiếp xúc không đổi khi sợi bị nén |
| $p$ | Áp suất kẹt dương (positive pressure) | Pa (kPa) | Áp suất khí nén trong bóng khí (bladder) nén bó sợi | Áp suất thủy tĩnh truyền đều qua màng mỏng |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Sử dụng phương pháp cân bằng công - năng lượng (work-energy balance) để xác định độ cứng uốn hiệu dụng $E I_S$ của bó sợi khi tất cả các sợi đã trượt lên nhau dưới áp suất dương.
2. **Liên hệ giữa các đại lượng:**
   - Công ngoại lực $W = \frac{1}{2} M \theta$ không chỉ chuyển thành thế năng đàn hồi của các sợi riêng lẻ ($\sum w_i^e$) mà còn bị tiêu tán qua công ma sát trượt ($\frac{1}{2}\sum w_i^f$).
   - Nhờ có công ma sát này, mô men quán tính tương đương trong trạng thái trượt $I_S$ lớn hơn tổng mô men quán tính riêng rẽ của $N$ sợi tự do ($N I_{\text{fib}}$).
3. **Input:** Mô men uốn $M$, áp suất dương $p$, hệ số ma sát $\mu$, hình học sợi ($d, l, c$), số sợi $N$, mô đun $E$.
4. **Output:** Mô men quán tính tương đương $I_S$ và góc xoay uốn $\theta$.
5. **Giả thiết:** Bóng khí làm bằng polyethylene siêu mỏng (0.1 mm) truyền áp suất thủy tĩnh hoàn hảo; phân bố trượt giữa các sợi tỷ lệ bậc nhất với khoảng cách $y_i$ tới trục trung hòa.
6. **Điều kiện đúng:** Trạng thái trượt hoàn toàn dưới uốn thuần túy.
7. **Suy luận:** Phương trình chứng minh rằng áp suất dương $p$ có thể vượt xa giới hạn 100 kPa của chân không, tạo ra lực ma sát và độ cứng uốn ở trạng thái trượt lớn hơn nhiều so với hệ chân không truyền thống.
8. **Phân biệt khoa học:** Độ cứng tăng thêm trong $I_S$ là do **tiêu tán ma sát** cản trở biến dạng, không phải do tăng mô đun vật liệu $E$.

#### E. Relation to MP1
- **Khả năng áp dụng:** Rất liên quan trực tiếp (Directly relevant to positive pressure mechanics). MP1 sử dụng áp suất dương để điều khiển ma sát trong bó dây TiNi; phương pháp cân bằng năng lượng Eq. (9) là công cụ toán học lý tưởng để mô hình hóa trạng thái trượt của MP1.

---

### NOTE B-07: M13 Eq. (11) — Mô hình suy giảm độ cứng bậc hai hiện tượng luận (Phenomenological Transition)

#### A. Source Identity
- **Paper ID:** M13
- **Evidence ID:** M13-E03
- **Equation Number:** Eq. (11)
- **PDF Page:** 5
- **Printed Page:** 485
- **SHA-256:** `3aa8790db0be1b0586e379d7ec4fe9be2a6d7139174f74d081ec352e0085a676`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 5):

$$I_{\text{eq}} = \begin{cases} I_J, & Q < Q_J \\ (I_J - I_S) \frac{(Q - Q_S)^2}{(Q_J - Q_S)^2} + I_S, & Q_J \le Q \le Q_S \\ I_S, & Q > Q_S \end{cases}$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $I_{\text{eq}}$ | Mô men quán tính tương đương hiệu dụng | m⁴ | Đại lượng đặc trưng cho độ cứng uốn tức thời tại lực cắt $Q$ | Hàm liên tục $C^0$ và $C^1$ tại các điểm biên |
| $I_J$ | Mô men quán tính ở trạng thái khóa kẹt hoàn toàn (jammed state) | m⁴ | Độ cứng uốn cao nhất khi bó sợi hoạt động như một khối đặc | No-slip |
| $I_S$ | Mô men quán tính ở trạng thái trượt hoàn toàn (slipped state) | m⁴ | Độ cứng uốn thấp nhất tính từ Eq. (10) | Full-slip |
| $Q_J$ | Lực cắt tới hạn bắt đầu xuất hiện trượt | N | Ngưỡng lực cắt tương ứng với $Q_{\text{slip}}$ | Bắt đầu chuyển pha |
| $Q_S$ | Lực cắt tới hạn khi trượt đã lan tỏa hoàn toàn | N | Ngưỡng lực cắt kết thúc quá trình chuyển tiếp | Bó sợi trượt toàn phần |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Biểu diễn sự suy giảm trơn tru của độ cứng uốn từ trạng thái kẹt cứng $I_J$ xuống trạng thái trượt $I_S$ dưới tác dụng của lực cắt ngang $Q$.
2. **Bản chất toán học:** Đây là hàm nội suy bậc hai (quadratic interpolation) được lựa chọn để đảm bảo tính liên tục của giá trị độ cứng và đạo hàm tại hai đầu mút $Q = Q_J$ và $Q = Q_S$.
3. **Phát biểu của tác giả (Author statement):** Tác giả khẳng định rõ ràng (p. 5): *"This phenomenological model compactly represents the smooth degradation of bending stiffness... It provides an engineering approximation for the transition regime without claiming a rigorous derivation of the slipped area evolution law. The quadratic interpolation is therefore adopted for model completeness, not as a result strictly derived from fiber-bundle micromechanics."*
4. **Điều không cho phép kết luận:** Tuyệt đối không được xem quy luật bậc hai này là một quy luật vật lý cơ bản bắt nguồn từ cơ học tiếp xúc vi mô của sợi; đây thuần túy là đường cong xấp xỉ kỹ thuật.

#### E. Relation to MP1
- **Khả năng áp dụng:** Chỉ dùng làm mô hình kỹ thuật xấp xỉ nhanh (Analogy / Engineering approximation). Không được dùng làm nền tảng khoa học để tuyên bố về cơ chế tiếp xúc vi mô trong MP1.

---

### NOTE B-08: M19 Eqs. (1)–(3) — Phân bố ứng suất pháp và ma sát Coulomb gia số trong dầm kẹt

#### A. Source Identity
- **Paper ID:** M19
- **Title:** Toward a deeper understanding of layer jamming structures: A continuous-interface model
- **Authors:** S. Zhang, J. Yao, P. Fang, J. Hong
- **Year:** 2025
- **DOI:** 10.1007/s11465-025-0857-4
- **Evidence ID:** M19-E02
- **Equation Number:** Eqs. (1), (2), (3)
- **PDF Page:** 6
- **Printed Page:** 6 (Front. Mech. Eng. 2025, 20(4): 27)
- **SHA-256:** `7cb387b88d2eb975390e1f74dd7e3b99912066fa23be98f793b8098c8c64bb93`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 6):

$$\sigma = k_\sigma y, \quad -\frac{\delta}{2} \le y \le \frac{\delta}{2}$$

$$\tau = \operatorname{sign}(Q) \mu p$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $\sigma$ | Ứng suất pháp uốn dọc trục dầm | Pa | Phân bố ứng suất pháp trên mặt cắt ngang của một lớp đơn lẻ | Phân bố tuyến tính theo chiều cao lớp |
| $k_\sigma$ | Độ dốc ứng suất pháp trong lớp trượt | Pa/m | Hệ số xác định từ mô men uốn nội tại của lớp | Phụ thuộc độ cong cục bộ |
| $\delta$ | Chiều dày của một lớp đơn lẻ | m | Chiều dày danh định | Các lớp có bề dày bằng nhau |
| $\tau$ | Ứng suất tiếp xúc ma sát trên giao diện trượt | Pa | Giới hạn Coulomb bão hòa | Trượt hoàn toàn tại giao diện |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Khi các lớp bắt đầu trượt lên nhau, liên kết dính bị phá vỡ. Mỗi lớp trong vùng trượt uốn quanh trục trung hòa riêng của nó, tạo nên phân bố ứng suất pháp tuyến hình răng cưa (sawtooth distribution) trên toàn bộ mặt cắt dầm.
2. **Ý nghĩa:** Trục trung hòa chung của toàn dầm bị phân rã thành các trục trung hòa cục bộ của từng lớp đơn lẻ. Lực cắt dọc trục được truyền hoàn toàn qua ma sát Coulomb bão hòa $\tau = \operatorname{sign}(Q)\mu p$.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp cơ chế phân bố ứng suất pháp khi bó dây TiNi chuyển từ trạng thái uốn chung sang trạng thái từng dây uốn độc lập.

---

### NOTE B-09: M20 Eqs. (4), (8) — Đồng hóa môi trường liên tục dầm kẹt lớp bằng RVE

#### A. Source Identity
- **Paper ID:** M20
- **Title:** Continuum modeling for layer jamming structures based on an elastoplastic constitutive model
- **Authors:** S. Zhang, J. Yao, S. Li et al.
- **Year:** 2026 (Online 2025)
- **DOI:** 10.1016/j.taml.2025.100633
- **Evidence ID:** M20-E02
- **Equation Number:** Eqs. (4), (8)
- **PDF Page:** 3
- **Printed Page:** 3 (Theor. Appl. Mech. Lett. 16, 100633)
- **SHA-256:** `a792efc44569c73e04cf4c93ee5cfcbe202164a2f8b5a03d157a918a99478f69`

#### B. Original Equation
Trích xuất nguyên văn từ PDF (p. 3):

$$\boldsymbol{\sigma} = \begin{bmatrix} (\lambda + 2G)\epsilon_1 + \lambda\epsilon_2 + \lambda\epsilon_3 \\ \lambda\epsilon_1 + (\lambda + 2G)\epsilon_2 + \lambda\epsilon_3 \\ \lambda\epsilon_1 + \lambda\epsilon_2 + (\lambda + 2G)\epsilon_3 \\ G\gamma_2 / 2 \\ G\gamma_1 / 2 \\ G(\partial v_1^i/\partial\xi_2 + \partial v_2^i/\partial\xi_1)/2 \end{bmatrix}$$

$$\bar{\boldsymbol{\sigma}} = \frac{1}{V_{\text{RVE}}} \int_{V_{\text{RVE}}} \boldsymbol{\sigma} dV$$

#### C. Variable Dictionary

| Ký hiệu | Ý nghĩa vật lý | Đơn vị | Định nghĩa trong nguồn | Giả thiết bắt buộc |
|---|---|---|---|---|
| $\bar{\boldsymbol{\sigma}}$ | Tensor ứng suất liên tục tương đương vĩ mô | Pa | Ứng suất trung bình thể tích trên phần tử thể tích đại diện (RVE) | Lý thuyết trường trung bình (average-field theory) |
| $\boldsymbol{\sigma}$ | Tensor ứng suất vi mô tại một điểm trong RVE | Pa | Ứng suất đàn hồi cục bộ tính từ hằng số Lamé | Biến dạng bé bên trong mỗi lớp |
| $V_{\text{RVE}}$ | Thể tích của phần tử đại diện RVE | m³ | Thể tích đơn vị gồm 2 nửa lớp và 1 giao diện tiếp xúc | Tính tuần hoàn cục bộ của cấu trúc phân lớp |
| $\lambda, G$ | Các hằng số Lamé của vật liệu làm lớp | Pa | Đặc tính đàn hồi đẳng hướng của vật liệu cơ sở | Đàn hồi tuyến tính đẳng hướng |
| $\epsilon_i, \gamma_i$ | Các thành phần biến dạng pháp và biến dạng cắt | Không chiều | Biến dạng vi mô trong hệ tọa độ cục bộ $\xi_1, \xi_2, \xi_3$ | Khai triển chuyển vị bậc nhất |

#### D. Mechanical Interpretation
1. **Quá trình vật lý:** Chuyển đổi bài toán tiếp xúc tiếp giáp rời rạc giữa vô số lớp mỏng thành một bài toán cơ học môi trường liên tục đàn - dẻo tương đương (elastoplastic continuum). Trượt ma sát Coulomb tại giao diện được đồng hóa thành biến dạng dẻo trượt vĩ mô.
2. **Ý nghĩa:** Cho phép áp dụng các phương pháp phần tử hữu hạn tiêu chuẩn hoặc cơ học giải tích liên tục để giải kết cấu dầm kẹt lớp có số lớp cực lớn ($n \gg 1$) mà không phải mô hình hóa từng mặt tiếp xúc riêng lẻ.

#### E. Relation to MP1
- **Khả năng áp dụng:** Cung cấp phương pháp luận toán học cho việc xây dựng mô hình đồng hóa môi trường liên tục (homogenized model) cho bó dây hoặc dầm kẹt lớp trong MP1.
