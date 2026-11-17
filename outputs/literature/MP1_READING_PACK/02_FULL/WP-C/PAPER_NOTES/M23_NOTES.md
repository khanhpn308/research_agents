# M23 — Zhang, Feng, Wang, Xu (2021)

**Analytical model for the bending of parallel wire cables considering interactions among wires**

- **Paper ID:** M23
- **DOI:** 10.1016/j.ijmecsci.2020.106192
- **Journal:** International Journal of Mechanical Sciences, Vol. 194, 106192
- **Canonical PDF:** `data/chap1-2_citations/M23__2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf`
- **SHA-256:** `1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a`
- **Pages:** 15
- **Status:** `VERIFIED_FULL_TEXT` (P0-R2 identity remediation CLOSED)

---

## A. Section objective

Trích xuất mô hình giải tích cho uốn bó dây song song, bao gồm cơ chế slip tại giao diện, lực tương tác giữa dây, và biểu diễn độ cứng uốn — phục vụ làm mô hình tham chiếu (reference model), xác định các giới hạn mô hình hóa (limitations), và cung cấp cơ sở phản biện (counterevidence) đối với các giả thiết đơn giản hóa khi nghiên cứu bó dây TiNi trong MP1.

## B. Concept and terminology notes

| Thuật ngữ | Định nghĩa trong M23 | Ghi chú MP1 |
|---|---|---|
| Parallel wire cable | Bó dây thẳng song song (không xoắn helix), hàn/kẹp hai đầu | Khác cáp xoắn helix; gần hơn với cấu hình bó TiNi thẳng trong MP1 |
| Laminated beam | Dầm phân lớp tương đương chuyển đổi từ mặt cắt tròn sang chữ nhật | Mỗi lớp giữ nguyên diện tích dây; chiều cao chia đều |
| Slip rigidity (k) | Hệ số tỉ lệ tuyến tính giữa lực tương tác và trượt tại giao diện [MPa] | Giả thiết linear ($F = k \cdot \Delta u$) — khác với ma sát khô Coulomb có ngưỡng kích hoạt |
| EBSC (γ) | Equivalent Bending Stiffness Coefficient — nghịch đảo của hệ số khuếch đại độ võng (DMC δ) | $\gamma = EI_{eff} / EI_{max}$; nằm trong khoảng $[EI_{min}/EI_{max}, 1]$ |
| State space method | Phương pháp không gian trạng thái: biến trạng thái gồm $u, \sigma_y, v, \tau_{xy}$ — giải đồng thời chuyển vị và ứng suất | Ưu điểm: xử lý giao diện trượt tự nhiên; hạn chế: giả thiết ứng suất phẳng 2-D |
| No-slip state (EI_max) | Toàn bộ mặt cắt liên kết dính chặt — dầm đồng nhất | Cận trên lý thuyết của độ cứng uốn |
| Full-slip state (EI_min) | Mỗi lớp uốn hoàn toàn độc lập không ma sát — tổng $EI$ các lớp riêng lẻ | Cận dưới lý thuyết của độ cứng uốn |

## C. Evidence with precise source locators

Xem Evidence Records: M23-E01 đến M23-E10 trong `EVIDENCE_RECORDS.jsonl`.

Tất cả locators đã được kiểm tra trực tiếp từ PDF gốc 15 trang.

- **M23-E01 (p. 1, Abstract):** Mô hình giải tích uốn bó dây song song bằng phương pháp chuyển đổi dầm phân lớp và không gian trạng thái; độ cứng uốn nằm giữa hai cận $EI_{min}$ và $EI_{max}$ tùy thuộc khả năng chống trượt.
- **M23-E02 (p. 2, Sec. 2.1, Fig. 1):** Chuyển đổi mặt cắt tròn thành các lớp chữ nhật tương đương bảo toàn diện tích và chiều cao tổng thể $H$.
- **M23-E03 (p. 3, Sec. 2.2, Eqs. (1)–(4); Figs. 4–5):** Thiết lập phương trình trạng thái với 4 biến trạng thái $\{u, \sigma_y, v, \tau_{xy}\}$ trên từng lớp dưới trạng thái ứng suất phẳng có ứng suất ban đầu $\sigma_{x0}^{(i)}$.
- **M23-E04 (p. 5, Sec. 2.2, Eqs. (13)–(19), (25)):** Ma trận truyền $[T_i] = \exp([K_i]\Delta\zeta_i)$ và ma trận giao diện trượt $[C_i]$ giải bài toán biên 2x2 thông qua chuỗi Fourier.
- **M23-E05 (p. 7, Sec. 3.2–3.3, Figs. 9–11; Table 2):** Ứng xử lực–võng dạng bilinear đối với bó dây không có lực kéo đầu ($T_{x0} = 0$ kN); EBSC giai đoạn 1 nhỏ hơn $0.5 EI_{max}$, giai đoạn 2 lớn hơn $EI_{min}$.
- **M23-E06 (p. 2, Sec. 2.1):** Thừa nhận giả thiết trượt tuyến tính ($F \propto \Delta u$) là một sự đơn giản hóa, thực tế tương tác giữa các dây phức tạp hơn và cần calibrate bằng thực nghiệm.
- **M23-E07 (p. 9, Sec. 3.4, Eq. (28); Figs. 14–17; Table 3):** Tỷ lệ slip giữa các giao diện tiệm cận tỷ lệ mômen tĩnh $S_i/S_1$ khi $k$ lớn; quan hệ slip tuân theo quy luật hàm mũ Eq. (28).
- **M23-E08 (p. 12, Sec. 3.5, Figs. 19–20):** Khi $k$ nhỏ mỗi lớp biến dạng uốn độc lập với bước nhảy chuyển vị dọc trục; khi $k$ lớn chuyển vị biến thiên tuyến tính như dầm đồng nhất.
- **M23-E09 (p. 8, Sec. 3.3, Fig. 13):** Đồ thị EBSC $\gamma$ tăng đơn điệu từ $EI_{min}/EI_{max}$ tiệm cận 1 theo slip rigidity $k$; $k$ là tham số tự do, không liên hệ vật lý với áp suất ngoài.
- **M23-E10 (p. 13, Sec. 4 Conclusions):** Tổng kết 4 kết luận chính và xác định hạn chế cốt lõi là cơ chế tương tác thực tế giữa các dây chưa được giải quyết rõ ràng.

## D. Important equations and figures

### Phương trình chính

| Eq. | PDF page | Ý nghĩa vật lý |
|---|---|---|
| Eq. (1) | p. 3 | Phương trình cân bằng lớp thứ $i$ có ứng suất ban đầu $\sigma_{x0}^{(i)}$ — plane stress |
| Eq. (3) | p. 3 | State equation: $\partial/\partial y \{u, \sigma_y, v, \tau_{xy}\}^{(i)} = [K_i] \{u, \sigma_y, v, \tau_{xy}\}^{(i)}$ — dạng ma trận |
| Eq. (4) | p. 3 | Ứng suất uốn: $\sigma_x^{(i)} = E_i \partial u^{(i)}/\partial x + \mu_i \sigma_y^{(i)}$ |
| Eq. (10) | p. 4 | State equation sau khai triển Fourier — hệ ODE với biến $\zeta = y/H$ |
| Eq. (13)–(14) | p. 5 | Nghiệm transfer matrix: truyền biến trạng thái qua lớp $i$ bằng $[T_i] = \exp([K_i]\Delta\zeta_i)$ |
| Eq. (15) | p. 5 | Điều kiện giao diện với trượt tuyến tính: $U_m^{(i+1)} = U_m^{(i)} + \frac{E_0}{k_i h_0} \tau_m^{(i)}$ |
| Eq. (19) | p. 5 | Transfer toàn bộ mặt cắt: $[T_n][C_{n-1}]...[C_1][T_1]$ — tích ma trận lớp-giao diện |
| Eq. (25) | p. 5 | Hệ phương trình 2×2 từ điều kiện biên mặt trên/dưới $\rightarrow$ xác định $U_m^{(1)}(0)$ và $V_m^{(1)}(0)$ |
| Eq. (26) | p. 7 | Deflection Magnification Coefficient (DMC) $\delta = w_{max}(\text{with slip}) / w_{max}(\text{no slip})$ |
| Eq. (28) | p. 9 | Tỷ lệ trượt giữa các giao diện: $\Delta u_i / \Delta u_1 = S_i/S_1 - (S_i/S_1 - 1)\exp(-R_i)$ |

### Hình/bảng quan trọng

| Item | PDF page | Nội dung |
|---|---|---|
| Fig. 1 | p. 2 | Mặt cắt bó dây song song $\rightarrow$ chuyển đổi thành laminated beam |
| Fig. 4 | p. 3 | Mô hình plane stress: các lớp, giao diện trượt, ứng suất biên và tải trọng |
| Fig. 5 | p. 3 | Chi tiết giao diện trượt: lực tương tác tiếp tuyến và bước nhảy chuyển vị $\Delta u_i$ |
| Fig. 6 | p. 6 | Sơ đồ thí nghiệm: gối tựa đơn giản, lực tập trung $P$ tại giữa nhịp, lực kéo đầu $T_{x0}$ |
| Figs. 9–11 | pp. 7–8 | Đường cong lực–độ võng: cáp 37φ7, 55φ7, 61φ7 — đặc tính bilinear rõ rệt khi $T_{x0} = 0$ |
| Fig. 13 | p. 8 | EBSC $\gamma$ theo slip rigidity $k$ — biểu đồ chuyển tiếp độ cứng từ full-slip đến no-slip |
| Table 2 | p. 9 | Giá trị EBSC trong hai giai đoạn bilinear của cáp không kéo ($T_{x0} = 0$ kN) |
| Table 3 | p. 9 | Lực tương tác tại các giao diện 1–3 ứng với các mức slip rigidity $k = 10^2$ đến $10^5$ MPa |
| Fig. 14 | p. 9 | Phân bố slip dọc trục cáp: triệt tiêu ở giữa nhịp, cực đại ở hai đầu gối tựa |
| Figs. 19–20 | p. 12 | Phân bố chuyển vị dọc trục và ứng suất uốn pháp tuyến qua chiều cao mặt cắt |

## E. Experimental and quantitative findings

**Dữ liệu thực nghiệm đối chiếu** (lấy từ Chen et al. [57], Construction and Building Materials 2015; M23 không thực hiện thí nghiệm vật lý mới):

- Bó dây thép song song 37φ7 ($D = 49$ mm), 55φ7 ($D = 59.5$ mm), 61φ7 ($D = 63$ mm) [M23-E03].
- Nhịp uốn $L = 820$ mm, liên kết gối tựa đơn giản (simply supported).
- Lực kéo dọc trục $T_{x0} = 0, 50, 80, 100$ kN; tải trọng uốn $P$ tăng dần tại giữa nhịp.
- Thông số vật liệu: thép $E = 2 \times 10^5$ MPa, hệ số Poisson $\mu = 0.3$.

**Kết quả định lượng then chốt:**

- Khi không có lực kéo đầu ($T_{x0} = 0$ kN): quan hệ $P–w$ gãy khúc bilinear rõ rệt. EBSC giai đoạn 1 lần lượt là 0.459 (37φ7), 0.361 (55φ7), 0.237 (61φ7); giai đoạn 2 giảm xuống 0.037, 0.022, 0.025 nhưng vẫn lớn hơn $EI_{min}$ hoàn toàn không ma sát [M23-E05].
- Khi có lực kéo dọc ($T_{x0} \ge 50$ kN): quan hệ $P–w$ gần tuyến tính, độ cứng tăng mạnh nhờ lực căng dọc chi phối [M23-E04].
- Tỷ lệ slip $\Delta u_2/\Delta u_1$ tiệm cận 2.33 và $\Delta u_3/\Delta u_1$ tiệm cận 1.83 khi $k \ge 10^4$ MPa, hoàn toàn khớp với tỷ lệ mômen tĩnh $S_2/S_1$ và $S_3/S_1$ [M23-E07].
- Lực tương tác giao diện tại mặt tiếp xúc 3 tăng từ 25.22 kN/m ($k = 10^2$ MPa) lên 147.43 kN/m ($k = 10^5$ MPa) [M23-E07].
- Khi $k$ thấp, chuyển vị dọc trục bị gãy bậc tại mỗi mặt tiếp xúc; khi $k$ cao, mặt cắt biến dạng phẳng tuyến tính như dầm đồng nhất [M23-E08].

## F. Cross-paper comparisons

| Paper | Đối tượng so sánh | Bản chất cơ học & Điểm khác biệt |
|---|---|---|
| M22 (Zhang et al. 2018) | Beam-theory parallel cable model | M22 thiết lập mô hình giải tích dựa trên lý thuyết dầm Euler–Bernoulli kết hợp quan hệ trượt giao diện. M23 là bước phát triển mở rộng sang mô hình ứng suất phẳng 2-D (không áp đặt giả thiết biến dạng phẳng lên toàn tiết diện), cho phép tính toán chi tiết trường ứng suất cục bộ và phân bố trượt. Kết quả độ cứng tổng thể của hai mô hình hoàn toàn nhất quán. |
| M24 (Barsi et al. 2025) | Short wire rope pure bending bounds | Cả hai cùng khảo sát cận độ cứng uốn nhưng dùng công cụ cơ học khác nhau: M24 áp dụng lý thuyết dầm Timoshenko có biến dạng trượt và đưa vào khái niệm biến dạng riêng (eigenstrain) để định nghĩa 3 trạng thái động học (perfect stick, partial stick, full slip). M23 chuyển đổi mặt cắt thành dầm phân lớp giải bằng phương pháp không gian trạng thái với độ cứng trượt $k$. M24 chứng minh perfect-stick đánh giá quá cao độ cứng thực tế, trong khi M23 cho thấy cáp không kéo ở trạng thái chuyển tiếp bilinear. |
| M35 (Xin Liu 2004) | Cable vibration with internal friction | **Phân biệt bản chất tiếp xúc:** M35 sử dụng luật ma sát khô Coulomb với **ngưỡng kích hoạt trượt** phụ thuộc áp suất pháp tuyến hướng tâm giữa các lớp dây xoắn ($\mu_s p_{rad}$), tạo nên quan hệ độ cứng uốn phi tuyến phụ thuộc độ cong ($EI(\kappa)$) và làm xuất hiện hai pha dao động (pha tắt dần khi $\kappa > \kappa_{cr}$ và pha không tắt dần khi $\kappa < \kappa_{cr}$). Ngược lại, M23 áp dụng cho uốn tĩnh của bó dây song song với **luật trượt giao diện tuyến tính** ($F = k \cdot \Delta u$) **không có ngưỡng kích hoạt** (không có Coulomb threshold); trượt xuất hiện liên tục tỉ lệ với lực cắt, và độ cứng chuyển tiếp liên tục theo thông số $k$. |
| M26/M27 (Reedlunn et al. 2013) | Superelastic SMA wire cables | M26/M27 tập trung vào ứng xử kéo của cáp hợp kim nhớ hình NiTi có chuyển pha siêu đàn hồi và tương tác phân cấp giữa các tao dây. M23 sử dụng vật liệu đàn hồi tuyến tính đơn thuần (thép), không có chuyển pha nhiệt–cơ hay hysteresis siêu đàn hồi. |

## G. Limitations and counterevidence

1. **Giả thiết liên kết trượt tuyến tính (Linear slip rigidity) [M23-E06, M23-E10]:** Mô hình coi lực tiếp xúc tiếp tuyến tỉ lệ thuận với độ trượt ($F = k \cdot \Delta u$). Tác giả nêu rõ tại trang 2: "The actual interactions among wires would be much more complicated than the linear assumption and should be experimentally calibrated". Đây là hạn chế lớn nhất; mô hình không có ngưỡng ma sát tĩnh Coulomb và không mô tả được hiện tượng stick–slip cục bộ theo lực pháp tuyến.
2. **Lý thuyết biến dạng phẳng 2-D (Plane stress formulation) [M23-E02, M23-E03]:** Việc chuyển đổi tiết diện tròn sang các lớp chữ nhật tương đương giữ nguyên diện tích nhưng loại bỏ hoàn toàn hình học tiếp xúc điểm/đường giữa các sợi dây tròn và bỏ qua ứng xử theo phương ngang $z$.
3. **Vật liệu đàn hồi tuyến tính hằng số [M23-E01]:** $E$ và $\mu$ là hằng số của thép, không thể tự động mở rộng sang vật liệu có quan hệ ứng suất–biến dạng phi tuyến hoặc chuyển pha martensite/austenite như TiNi.
4. **Tham số độ cứng trượt $k$ không liên hệ với nguồn áp suất ngoài [M23-E09]:** Hệ số $k$ trong M23 là một biến tự do mang tính hiệu chỉnh (fitting parameter), không có công thức dẫn xuất từ áp suất pháp tuyến $p$ hay hệ số ma sát $\mu$.
5. **Thiếu năng lượng tiêu tán / hysteresis [M23-E05]:** Mô hình giải đàn hồi thuần túy với trượt tuyến tính nên không tạo ra diện tích vòng lặp hysteresis tiêu tán năng lượng khi tải–dỡ chu kỳ.

## H. Relevance to MP1

**Phân loại vai trò nguồn (Source Role Clarification):**

- **REFERENCE_MODEL:** M23 cung cấp khung giải tích tham chiếu chuẩn mực cho độ cứng uốn và hai cận độ cứng ($EI_{min}$ full-slip đến $EI_{max}$ no-slip) của bó dây song song thông qua chuyển đổi dầm phân lớp và phương pháp không gian trạng thái (state space method). Cấu trúc bó dây song song trong M23 có sự tương đồng hình học cao nhất với bó dây TiNi thẳng trong MP1 (khác với các loại cáp xoắn helix).
- **SUPPORTING_EVIDENCE:** Bằng chứng giải tích và thực nghiệm cho thấy sự tồn tại của quy luật phân bố slip dạng hàm mũ (Eq. 28) và sự chuyển tiếp độ cứng uốn tương đương (EBSC $\gamma$) theo khả năng chống trượt giữa các dây. Đồ thị EBSC vs $k$ (Fig. 13) là cơ sở tham khảo tốt cho đáp ứng điều khiển độ cứng.
- **COUNTEREVIDENCE (phản biện các giả thiết đơn giản hóa):**
  1. Phản bác giả thiết dầm đồng nhất: M23 chứng minh trực tiếp rằng giả thiết tiết diện phẳng của lý thuyết dầm cổ điển chỉ đúng trên từng lớp dây riêng lẻ chứ không đúng trên toàn bộ tiết diện bó dây [M23-E08, M23-E10].
  2. Phản bác giả thiết độ cứng không đổi: M23 chứng minh bó dây không chịu kéo dọc có quan hệ lực–độ võng dạng bilinear rõ rệt [M23-E05], trong đó độ cứng không cố định ở $EI_{max}$ hay $EI_{min}$.
- **LIMITATION (ranh giới chuyển giao sang MP1):**
  - M23 dùng dây thép đàn hồi tuyến tính, trong khi MP1 dùng dây hợp kim nhớ hình TiNi siêu đàn hồi có chuyển pha austenite $\leftrightarrow$ martensite.
  - M23 dùng luật trượt tuyến tính với $k$ là tham số tự do, trong khi MP1 điều khiển ma sát tiếp xúc thông qua áp suất dương thực tế sinh ra từ piston dẫn động bằng lò xo SMA.
- **AGENT_INFERENCE:** Để áp dụng cho MP1, cần kết hợp khung không gian trạng thái của M23 với quan hệ tiếp xúc ma sát phụ thuộc áp suất piston $k(p)$ hoặc ngưỡng Coulomb $\tau_{crit}(p) = \mu \cdot \sigma_n(p)$, đồng thời tích hợp mô đun đàn hồi hiệu dụng phụ thuộc biến dạng của TiNi.

*Lưu ý bảo vệ tính liêm chính:* Tuyệt đối không coi mô hình M23 là đã được kiểm chứng trên cấu hình bó dây TiNi hay cơ chế áp suất dương của MP1.

## I. Reading route

1. **Abstract (p. 1):** Nắm phạm vi bài toán, phương pháp dầm phân lớp và không gian trạng thái.
2. **Sec. 2.1 (p. 2):** Khảo sát Fig. 1 và các giả thiết chuyển đổi tiết diện bó dây tròn thành dầm phân lớp chữ nhật.
3. **Sec. 2.2 (pp. 3–5):** Nắm phương trình trạng thái Eq. (3), ma trận truyền $[T_i]$ Eq. (14), điều kiện trượt giao diện Eq. (15), và cách giải hệ 2x2 Eq. (25).
4. **Sec. 3.2–3.3 (pp. 6–9):** Xem sơ đồ thí nghiệm Fig. 6 và phân tích đường cong lực–độ võng bilinear Figs. 9–11 cùng biểu đồ EBSC Fig. 13 để hiểu cơ chế chuyển tiếp độ cứng.
5. **Sec. 3.4 (pp. 9–11):** Đọc phân tích phân bố trượt dọc trục Fig. 14, quy luật hàm mũ Eq. (28) và bảng lực tương tác Table 3.
6. **Sec. 3.5 & Sec. 4 (pp. 11–13):** Khảo sát phân bố chuyển vị/ứng suất Figs. 19–20 và phần thảo luận kết luận để nắm rõ ranh giới giả thiết tiết diện phẳng.

## J. Questions for human writing

1. **Cơ sở xác định độ cứng uốn (C2.4.2, C2.5.1):** Khi xây dựng mô hình dầm phân lớp tương đương cho bó dây TiNi trong MP1, quan hệ tiếp xúc nên giữ dạng liên kết trượt tuyến tính $k(p)$ hay cần chuyển hẳn sang mô hình ma sát Coulomb có ngưỡng trượt theo áp suất buồng piston?
2. **Hiện tượng gãy khúc bilinear (C2.5.2, C2.5.3):** Trong thí nghiệm uốn tĩnh của MP1 với bó dây TiNi không có lực căng dọc trục ban đầu, liệu đáp ứng lực–biến dạng có thể hiện pha bilinear như M23 quan sát hay sẽ bị chi phối bởi hysteresis chuyển pha của TiNi?
3. **Giới hạn giả thiết tiết diện phẳng (C2.5.5):** M23 chứng minh giả thiết tiết diện phẳng không đúng cho toàn bộ bó dây khi có trượt; điều này ảnh hưởng thế nào đến việc lựa chọn mô hình dầm liên tục (continuum beam) trong Chương 2 của luận văn?

## K. Unresolved evidence

1. Mối liên hệ định lượng giữa áp suất pháp tuyến thực tế $p$ và hệ số slip rigidity $k$ trong M23 chưa tồn tại trong bài báo; cần dữ liệu thực nghiệm riêng của MP1 để thiết lập quan hệ $k = f(p)$.
2. Ảnh hưởng của nhiệt độ (quá trình gia nhiệt kích hoạt lò xo SMA) lên đặc tính ma sát và độ dính bám giữa các sợi TiNi chưa được xem xét trong mô hình đàn hồi thuần túy của M23.
3. Số trang in (`printed_page`) trong P0 là `NOT_REPORTED`; các định vị trang sử dụng số trang vật lý của file PDF 15 trang.
