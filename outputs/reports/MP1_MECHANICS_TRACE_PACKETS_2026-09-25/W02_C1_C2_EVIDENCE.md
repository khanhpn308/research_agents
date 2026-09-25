# W02 — Bằng chứng Kiểm chứng Chuyên sâu C1 và C2

## 1. Mục tiêu (Mission)

Thẩm tra chuyên sâu toàn văn (deep full-text audit) hai phát biểu nền tảng:
- **C1:** Nghẽn sợi/dây để thay đổi độ cứng uốn (Wire/fiber jamming for variable stiffness) là mới.
- **C2:** Nghẽn bằng áp suất dương để thay đổi độ cứng uốn (Positive-pressure jamming for variable stiffness) là mới.

Nhiệm vụ trọng tâm là bóc tách cơ chế vật lý, môi trường nghẽn, phương pháp tạo áp suất/chân không, mô hình cơ học, thiết lập thí nghiệm, số liệu định lượng về độ cứng kèm số trang kiểm chứng; qua đó giải thích vì sao C1 và C2 bị đóng hoàn toàn (`closed`), đồng thời xác định ranh giới những gì các công trình này **chưa chứng minh** đối với dây hợp kim nhớ hình NiTi siêu đàn hồi.

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `data/evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json`
- `data/evidence/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json`
- `data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json`
- `papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`
- `papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`
- `papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf`

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **C1 (Wire/fiber jamming):** `closed` [AUDIT VERDICT] (nguồn: `CORE_PRIOR_ART_AUDIT.json`)
- **C2 (Positive-pressure jamming):** `closed` [AUDIT VERDICT] (nguồn: `CORE_PRIOR_ART_AUDIT.json`)

## 4. Bảng bằng chứng (Evidence table)

| Evidence ID | Claim/Target | Paper | DOI | paper_id | Page(s) | Evidence type | Finding |
|---|---|---|---|---|---|---|---|
| W02-E01 | C1 | Bai et al. 2022 | 10.3390/app12073582 | 240fbf6022 | 1, 4, 5, 8, 9 | Experimental / Analytical | Nghẽn dây kraft/nylon bằng chân không 0 đến -85 kPa; độ cứng uốn tăng gần 7 lần (0.89 N/mm); mô hình dầm Euler–Bernoulli. |
| W02-E02 | C1, C2 | Zhang & Yao 2026 | 10.5194/ms-17-481-2026 | 3aa8790db0 | 1, 3–4, 6, 9–11 | Experimental / Analytical | Nghẽn 700 sợi nylon bằng bóng khí áp suất dương 0–300 kPa; mô hình 3 trạng thái; độ cứng trượt tăng tuyến tính với áp suất. |
| W02-E03 | C2 | Liu et al. 2021 | 10.1109/LRA.2021.3097255 | 182d854610 | 1, 3, 4, 5 | Experimental / Analytical | Áp suất dương bên trong (68–172 kPa) nén hạt granular; độ cứng uốn tăng ~5.83 lần (0.69 → 4.02 N/mm); mô hình dầm vành khuyên. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W02-E01

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C1 — Wire/fiber jamming for variable stiffness.

**Paper title:** *Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming*

**Authors:** Long Bai, Hao Yan, Jiafeng Li, Jiefeng Shan, Penghao Hou

**Year:** 2022

**DOI:** `10.3390/app12073582`

**paper_id:** `240fbf6022`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json`

**Original PDF:** `papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`

**Page(s) / Section:** Trang 1, 4, 5, 8, 9; Section 2 (Design and Modeling), Section 3 (Fabrication and Experiments).

**Evidence type:** Experimental and analytical modeling.

### Thiết lập cơ học (Mechanical setup)
- Môi trường nghẽn (jamming medium): Sợi dây giấy kraft (kraft rope), dây gai dầu (hemp rope), và dây cước nylon (nylon wire). Tác giả chọn dây kraft nhờ cân bằng giữa độ mềm ban đầu và độ cứng cao sau khi nghẽn mà không bị tái sắp xếp tiết diện (p. 8).
- Phương pháp giam giữ: Đặt bó dây trong vỏ màng kín khí, hút chân không để tạo chênh áp khí quyển nén các sợi lại với nhau.
- Bố trí hình học: Bố trí dây dạng tiết diện chữ nhật (rectangular wire arrangement) với các đầu dây cắt vát theo độ dốc ngược (reverse-gradient trimmed wire ends) nhằm triệt tiêu hiện tượng trượt chu vi và xoắn cục bộ khi uốn (pp. 4, 5).

### Mô hình / lý thuyết (Model / theory)
- Áp dụng lý thuyết dầm công-xôn Euler–Bernoulli cho hai trạng thái giới hạn (p. 5):
  1. Trạng thái tự do (unjammed state): Các sợi dây uốn độc lập xung quanh trục trung hòa riêng của từng sợi; độ cứng uốn tổng bằng tổng độ cứng của từng sợi riêng lẻ:
     $$EI_{\text{unjammed}} = \sum_{i=1}^{n} E_i I_i$$
  2. Trạng thái nghẽn (jammed state): Áp suất chân không tạo lực ma sát liên kết các sợi thành một dầm composite đặc thống nhất; mô-men quán tính tiết diện tính theo trục trung hòa chung của toàn khối:
     $$EI_{\text{jammed}} = E I_{\text{composite}}$$
  Mô hình dự báo độ cứng tăng tỷ lệ bậc ba với số lớp dây theo phương chiều dày (p. 5).

### Phương pháp thí nghiệm (Experimental method)
- Thí nghiệm uốn công-xôn trên máy kéo nén vạn năng; đầu ngọn dầm chịu tải trọng uốn ngang vuông góc với trục dầm (p. 8).
- Dải áp suất chân không kiểm tra: từ $0\text{ kPa}$ đến $-85\text{ kPa}$ (các bước trung gian $-20, -40, -60, -85\text{ kPa}$).
- Kiểm tra độ cứng xoắn (torsional impedance) ở các góc xoay từ $0^\circ$ đến $60^\circ$ để so sánh với công nghệ nghẽn lớp (layer jamming) (p. 9).

### Kết quả định lượng (Quantitative results)
- Với kết cấu dây kraft dày $8\text{ mm}$, khi áp suất chân không chuyển từ $0\text{ kPa}$ xuống $-85\text{ kPa}$, độ cứng uốn tăng gần 7 lần, đạt $0.89\text{ N/mm}$ tại độ võng $15\text{ mm}$ (p. 8).
- Độ cứng xoắn của cấu trúc wire jamming thấp hơn đáng kể so với layer jamming ($32.63\text{ N}\cdot\text{mm}$ ở chiều dày $6\text{ mm}$ và $47.5\text{ N}\cdot\text{mm}$ ở chiều dày $8\text{ mm}$), giúp tay gắp mềm linh hoạt đa hướng (p. 9).
- Bộ gắp mềm 3 ngón trang bị lớp nghẽn dây tăng gấp đôi tải trọng nâng vật thể khi hút chân không $-85\text{ kPa}$ (p. 10).

### Bằng chứng này chứng minh điều gì (What this proves)
Chứng minh trực tiếp và đầy đủ rằng: hiện tượng nghẽn ma sát giữa các sợi/dây (wire jamming) dưới tác dụng của chênh áp giam giữ đã được dùng để điều chỉnh độ cứng uốn (variable bending stiffness) trong robot mềm, có mô hình dầm giải tích và kiểm chứng thực nghiệm rõ ràng.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Bài báo không sử dụng dây kim loại hoặc hợp kim nhớ hình NiTi siêu đàn hồi (chỉ dùng kraft rope, hemp rope, nylon wire).
- Không sử dụng áp suất nén dương (chỉ dùng chân không với giới hạn trên $\sim 1\text{ atm} = 100\text{ kPa}$).
- Không tồn tại bài toán chuyển pha cơ học phụ thuộc ứng suất hay ma sát ghép cặp nhiệt - cơ.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Đóng hoàn toàn tính mới của C1 ở cấp độ nguyên lý "wire jamming for variable stiffness".

---

### EVIDENCE W02-E02

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C1 (Fiber jamming) và C2 (Positive-pressure jamming).

**Paper title:** *A variable stiffness omnidirectional chain based on positive-pressure fiber jamming*

**Authors:** Shuai Zhang, Jiantao Yao

**Year:** 2026

**DOI:** `10.5194/ms-17-481-2026`

**paper_id:** `3aa8790db0`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json`

**Original PDF:** `papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf`

**Page(s) / Section:** Trang 1, 2, 3, 4, 6, 9, 10, 11; Section 2 (Design), Section 3 (Theoretical Modeling), Section 4 (Experiments).

**Evidence type:** Analytical derivation, parameter identification, and experimental validation.

### Thiết lập cơ học (Mechanical setup)
- Môi trường nghẽn: Bó gồm 700 sợi nylon (nylon fibers, đường kính $d = 0.4\text{ mm}$) đặt trong khoang của các mắt xích in 3D bằng nhựa resin ($R = 6\text{ mm}, h = 4\text{ mm}, a = 3\text{ mm}$) (p. 2).
- Phương pháp giam giữ: Sử dụng bóng khí nén polyethylene dẹt bên trong ($w = 10\text{ mm}$, độ dày $0.1\text{ mm}$) đặt dưới đáy khoang. Khi bơm khí nén, bóng khí nở ra ép chặt bó sợi lên thành khoang cứng phía trên (pp. 2, 5).
- Khớp nối: Các mắt xích liên kết qua trục thép không gỉ đặt trong lỗ côn kép (double-conical holes) với khoảng cách tâm $12\text{ mm}$, tạo chuỗi biến đổi độ cứng đẳng hướng (VSOC) với hai chế độ uốn trực giao: uốn quanh trục (shaft bending) và uốn ngang (lateral bending) (pp. 5, 6).

### Mô hình / lý thuyết (Model / theory)
- Khung lý thuyết 3 trạng thái cơ học uốn của dầm nghẽn sợi (pp. 1, 3, 4):
  1. Trạng thái nghẽn hoàn toàn (jamming state, $Q \le Q_J$): Không có trượt tương đối giữa các sợi, dầm ứng xử như một thanh đặc nguyên khối với mô-men quán tính tương đương $I_J$.
  2. Trạng thái chuyển tiếp (transition state, $Q_J < Q \le Q_S$): Trượt ma sát bắt đầu từ vùng có ứng suất cắt cực đại trên trục trung hòa và lan dần ra ngoài biên theo phân bố parabol.
  3. Trạng thái trượt hoàn toàn (slipping state, $Q > Q_S$): Toàn bộ các mặt tiếp xúc giữa các sợi trượt lên nhau; kháng uốn đến từ độ cứng uốn riêng của từng sợi cộng với công tiêu tán ma sát Coulomb, đặc trưng bởi mô-men quán tính tương đương phụ thuộc áp suất $I_S(p)$ (pp. 3, 4, 11).
- Công thức lực cắt chuyển tiếp (p. 6):
  Lực cắt bắt đầu trượt $Q_J$ phụ thuộc hình học tiết diện, hệ số ma sát tĩnh $\mu$, và áp suất giam giữ $p$. Lực cắt để trượt hoàn toàn $Q_S$ tỷ lệ trực tiếp với tổng diện tích tiết diện sợi $A$, hệ số ma sát $\mu$, và áp suất $p$:
  $$Q_S = A \cdot \mu \cdot p$$
- Cân bằng công - năng lượng trong uốn thuần túy: Công của ngoại lực cân bằng với thế năng đàn hồi và năng lượng tiêu tán do trượt ma sát Coulomb (p. 3).

### Phương pháp thí nghiệm (Experimental method)
- Thí nghiệm uốn 3 điểm (three-point bending) trên máy kéo nén vạn năng với nhịp $L = 100\text{ mm}$, tốc độ dịch chuyển đầu ấn $20\text{ mm/min}$ (p. 9).
- Dải áp suất khí nén chủ động: từ $0\text{ kPa}$ đến $300\text{ kPa}$ (các bước nhảy $50\text{ kPa}$) qua van điều áp chính xác (pp. 9, 10).
- Thuật toán hồi quy tuyến tính từng đoạn thích nghi (piecewise linear regression tối đa hóa $R^2$) để trích xuất tự động lực chuyển tiếp $(Q_J, Q_S)$ và độ cứng $(K_H, K_L)$ từ 60 đường cong thực nghiệm (p. 9).

### Kết quả định lượng (Quantitative results)
- Lực cắt chuyển tiếp $(Q_J, Q_S)$ và độ cứng trạng thái trượt ($I_S$) tăng tuyến tính với áp suất dương từ 0 đến $300\text{ kPa}$ cho cả hai chế độ uốn (pp. 1, 9, 10).
- Mô-men quán tính trạng thái nghẽn $I_J$ hầu như không đổi theo áp suất (trung bình $I_J = 47.02\text{ mm}^4$ cho uốn quanh trục và $43.22\text{ mm}^4$ cho uốn ngang), xác nhận $I_J$ thuần túy do hình học tiết diện bị nén chặt quyết định (p. 10).
- Nhận dạng được tham số thực nghiệm: mô-đun đàn hồi sợi hữu hiệu $E = 4.85\text{ GPa}$ ($95\%\text{ CI: } [4.765, 4.925]\text{ GPa}$ từ thí nghiệm uốn ở $0\text{ kPa}$); hệ số ma sát tĩnh giữa các sợi $\mu = 0.3665$ ($95\%\text{ CI: } [0.3433, 0.3897], R^2 = 0.817$) từ tương quan lực trượt hoàn toàn theo áp suất (p. 10).
- Độ dốc dự báo lý thuyết của lực cắt theo áp suất khớp với thực nghiệm trong phạm vi sai số tương đối $8.5\%$ cho uốn quanh trục ($9.9763\text{ N/kPa}$ lý thuyết vs $9.0591\text{ N/kPa}$ thực nghiệm) và $7.6\%$ cho uốn ngang ($11.3065\text{ N/kPa}$ vs $10.4563\text{ N/kPa}$) (p. 10).
- Độ tán xạ dữ liệu tăng khi áp suất tăng (độ lệch chuẩn tải trọng cực đại tăng từ $0.0354\text{ N}$ ở $0\text{ kPa}$ lên $5.4215\text{ N}$ ở $300\text{ kPa}$ trong uốn ngang), do tính ngẫu nhiên của hiện tượng dính–trượt (stick-slip) giữa các sợi (p. 10).

### Bằng chứng này chứng minh điều gì (What this proves)
1. Đóng hoàn toàn C1: Nghẽn sợi dưới uốn đã có mô hình chuyển tiếp dính–trượt (stick-slip) giải tích chính xác.
2. Đóng hoàn toàn C2: Áp suất giam giữ dương (positive pressure lên tới 300 kPa) đã được dùng trực tiếp để nén sợi, điều khiển tuyến tính lực chuyển tiếp và độ cứng uốn trạng thái trượt.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Vật liệu sợi là nylon đàn hồi tuyến tính ($E = 4.85\text{ GPa}$ cố định), hoàn toàn không có hiệu ứng chuyển pha nhiệt - đàn hồi (martensitic transformation), không có thềm ứng suất (transformation plateau), và không có trễ siêu đàn hồi (superelastic hysteresis).
- Không khảo sát bó dây kim loại với biến dạng lớn hoặc tiếp xúc Hertzian đàn dẻo giữa các dây kim loại.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Zhang & Yao 2026 là mối đe dọa trực tiếp mạnh nhất đối với kiến trúc của MP1. Nó chứng minh rằng nếu chỉ thay sợi nylon bằng dây kim loại/NiTi mà không chỉ ra được sự ghép cặp cơ học chuyển pha làm thay đổi quy luật stick-slip, thì toàn bộ ý tưởng chỉ là thay thế vật liệu (material substitution).

---

### EVIDENCE W02-E03

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C2 — Positive-pressure jamming for variable stiffness.

**Paper title:** *A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots*

**Authors:** Zhenhua Liu, Shiwu Zhang, Minjie Dong, Hongying Xiao, Jingwen Zhao

**Year:** 2021

**DOI:** `10.1109/LRA.2021.3097255`

**paper_id:** `182d854610`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json`

**Original PDF:** `papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`

**Page(s) / Section:** Trang 1, 3, 4, 5; Section II (Working Principle and Modeling), Section III (Experimental Validation).

**Evidence type:** Experimental characterization and empirical beam modeling.

### Thiết lập cơ học (Mechanical setup)
- Môi trường nghẽn: Hạt rắn (glass beads / granular particles) chứa trong khoang vành khuyên hình trụ giữa lớp bóng khí cao su bên trong (đường kính trong $d$) và lớp vỏ vải bọc không giãn bên ngoài (đường kính ngoài $D$) (pp. 1, 2).
- Phương pháp giam giữ: Bơm khí nén áp suất dương vào bóng khí bên trong; bóng khí giãn nở ép các hạt cát/thủy tinh nén chặt vào nhau và tựa vào lớp vỏ ngoài.

### Mô hình / lý thuyết (Model / theory)
- Áp dụng công thức dầm công-xôn Euler–Bernoulli:
  $$K = \frac{3EI}{L^3}$$
- Mô-men quán tính diện tích tiết diện vành khuyên (p. 4):
  $$I = \frac{\pi (D^4 - d^4)}{64}$$
- Mô hình tỷ lệ mô-đun Young tương đương $E$ theo lực tiếp xúc trung bình giữa các hạt, tỷ lệ thuận với áp suất khí nén $P$:
  $$E = \frac{C \cdot P}{D^2 - d^2}$$
  Từ đó dẫn xuất độ cứng uốn tổng hợp tỷ lệ thuận trực tiếp với áp suất tương đối $P$ (p. 4).

### Phương pháp thí nghiệm (Experimental method)
- Thí nghiệm uốn công-xôn trên mẫu trụ với áp suất tương đối từ $68/69\text{ kPa}$ đến $172\text{ kPa}$ (các mức $69, 103, 138, 172\text{ kPa}$) (p. 4).
- So sánh trực tiếp giữa nghẽn áp suất dương (+62 kPa) và nghẽn chân không (-62 kPa) (p. 3).
- So sánh giữa cấu trúc hạt nghẽn với bóng khí thuần túy cùng kích thước ở $103\text{ kPa}$ (p. 4).

### Kết quả định lượng (Quantitative results)
- Độ cứng uốn công-xôn tăng xấp xỉ 6 lần (từ $0.69\text{ N/mm}$ lên $4.02\text{ N/mm}$, tương đương tỷ số [DERIVATION] $4.02 / 0.69 \approx 5.826$) khi áp suất tăng từ $68/69\text{ kPa}$ lên $172\text{ kPa}$, lực kháng uốn đạt từ $4\text{ N}$ đến $23\text{ N}$ (pp. 1, 4).
- Tương quan giữa độ cứng uốn và áp suất là tuyến tính cao ($R^2$ lần lượt là $0.992, 0.995, 0.994, 0.993$ tại các dải đo) (p. 4).
- Ở cùng mức áp suất $103\text{ kPa}$, cấu trúc hạt nghẽn áp suất dương có độ cứng uốn cao hơn $40\%$ so với bóng khí nén không chứa hạt (p. 4).
- Nghẽn áp suất dương (+62 kPa) có độ cứng ban đầu tương đương hút chân không (-62 kPa), nhưng ít biến dạng dẻo hơn và độ trễ khi dỡ tải (unloading hysteresis) nhỏ hơn đáng kể nhờ độ đàn hồi hồi phục của bóng khí (p. 3).

### Bằng chứng này chứng minh điều gì (What this proves)
Áp suất giam giữ dương bên trong (positive pressure jamming) đã được nghiên cứu bài bản, chứng minh khả năng thay đổi độ cứng uốn tuyến tính theo áp suất và vượt trội hơn hút chân không về độ ổn định dỡ tải. Claim C2 hoàn toàn không còn tính mới.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Đây là nghẽn hạt (granular jamming), không phải nghẽn sợi/dây (fiber/wire jamming).
- Không có bất kỳ vật liệu kim loại hay vật liệu thông minh nhớ hình nào tham gia vào cơ chế uốn.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Khẳng định nguyên lý tạo áp suất dương nén môi trường jamming là kỹ thuật đã biết trong ngành soft robotics.

## 6. Kết luận về claim/target (Claim/target conclusion)

- **Sự kiện bài báo xác minh (Verified Paper Facts):**
  1. Bai et al. 2022 đã hiện thực hóa wire jamming bằng chân không, uốn công-xôn đạt độ cứng tăng $\sim 7$ lần ở $-85\text{ kPa}$.
  2. Liu et al. 2021 đã hiện thực hóa positive-pressure granular jamming, độ cứng uốn tăng $\sim 5.83$ lần ở $172\text{ kPa}$.
  3. Zhang & Yao 2026 đã tích hợp cả hai: positive-pressure fiber jamming lên tới $300\text{ kPa}$, mô hình hóa giải tích 3 trạng thái dính–trượt (stick-slip) ăn khớp thực nghiệm trong sai số $7.6\% - 8.5\%$.
- **Phán quyết thẩm tra (Audit Verdicts):**
  - **C1 = `closed`:** Không thể tuyên bố tính mới cho nguyên lý wire/fiber jamming.
  - **C2 = `closed`:** Không thể tuyên bố tính mới cho nguyên lý positive-pressure jamming.
- **Suy luận khoa học (Worker Inference):**  
  [INFERENCE] Nếu MP1 chỉ đề xuất "dùng áp suất dương để nén bó dây nhằm thay đổi độ cứng", toàn bộ cơ cấu đã bị Zhang & Yao 2026 và Liu et al. 2021 đón đầu (pre-empted). Điểm sống sót duy nhất của MP1 không nằm ở áp suất dương hay bó dây, mà phụ thuộc vào việc liệu **đặc tính chuyển pha phi tuyến của hợp kim NiTi siêu đàn hồi** có tương tác với áp suất dương và ma sát tiếp xúc để tạo ra một quy luật cơ học uốn mà mô hình sợi đàn hồi của Zhang & Yao không thể dự báo bằng cách thay thế thông số đàn hồi hay không.

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Cả 3 bài báo trên đều dùng vật liệu đàn hồi cổ điển (nylon, kraft, thủy tinh) với mô-đun đàn hồi hằng số.
- Chưa có mô hình nào trong số các bài này giải quyết biến dạng uốn kết hợp chuyển pha mactenxít cảm ứng ứng suất (stress-induced martensitic transformation) trong từng sợi dây cáp.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Mô hình giải tích 3 trạng thái của Zhang & Yao 2026 có thể mở rộng trực tiếp cho vật liệu dầm có quan hệ ứng suất - biến dạng dạng song tuyến (bilinear) hoặc dạng cờ (flag-shaped superelastic) bằng cách thay thế hàm ứng suất cắt hay không?
2. Trong bài Zhang & Yao 2026, hiện tượng phân tán dữ liệu thực nghiệm ở áp suất cao ($300\text{ kPa}$) có bắt nguồn từ cơ chế vi trượt ngẫu nhiên tương tự như hiện tượng trượt ma sát giữa các sợi kim loại hay không?

## 9. Danh mục kiểm tra xác minh gói bằng chứng (Packet verification checklist)

- [x] Tiêu đề bài báo được xác minh nguyên văn tiếng Anh (paper title verified)
- [x] Tác giả và năm xuất bản được đối chiếu (authors/year verified)
- [x] DOI được xác minh từ tệp bằng chứng (DOI verified)
- [x] Mã định danh bài báo paper_id khớp chính xác với registry (paper_id verified)
- [x] Đường dẫn tệp evidence JSON được xác minh tồn tại trên đĩa (evidence JSON path verified)
- [x] Đường dẫn tệp PDF gốc được đối chiếu (PDF path verified)
- [x] Các số liệu định lượng có số trang kiểm chứng (quantitative claims page-verified)
- [x] Các cơ chế cơ học có số trang kiểm chứng (mechanical claims page-verified)
- [x] Phán quyết audit được phân biệt rõ với sự kiện bài báo (audit verdict separated from paper fact)
- [x] Các nhận định suy luận được gắn nhãn [INFERENCE] / [DERIVATION] rõ ràng (inference explicitly labelled)
- [x] Mục “What it does NOT prove” được điền đầy đủ cho từng nguồn (What it does NOT prove completed)
- [x] Các điểm chưa giải quyết hoặc giới hạn được công khai minh bạch (unresolved issues disclosed)
