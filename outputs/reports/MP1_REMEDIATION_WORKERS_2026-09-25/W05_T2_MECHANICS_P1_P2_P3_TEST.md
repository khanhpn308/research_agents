# W05: Kiểm chứng Cơ học T2 – Phân loại P1/P2/P3 và Khả năng Nhận Áp suất Biến thiên của Phương trình Hiện hữu (T2 Mechanics Test: P1/P2/P3 Classification & Existing Equations)

**Worker ID:** W05  
**Mục tiêu:** Kiểm tra nghiêm ngặt mối đe dọa T2, phân tích phân loại ba mức áp suất P1/P2/P3, và kiểm chứng trực tiếp xem các phương trình cơ học tiếp xúc và cấu thành hiện hữu có thể tự nhiên tiếp nhận lịch sử áp suất biến thiên $p(t)$ mà không cần phương trình mới hay không (giải quyết phê bình G02 của Astra).  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Phân loại Ba Mức Áp suất Giam giữ: P1, P2 và P3

Trong các tài liệu nghiên cứu cơ học bó dây và cáp, áp suất giam giữ tác động lên các dây xuất hiện dưới ba hình thức:

1. **Mức P1 — Áp suất chế tạo thụ động (Passive Manufacturing / Preforming Preload):**
   - Áp suất hướng kính sinh ra do quá trình xoắn/bện các lớp dây xung quanh lõi trong quá trình chế tạo.
   - Bằng chứng tiêu biểu:
     - Reedlunn et al. (2013 Part II, `fac21c950e`): Áp suất nén hướng kính giữa các lớp dây xoắn tạo ra các vết lõm vi mô (indentations) cố định trên bề mặt dây.
     - Xin Liu (2013, `aaad9c248c`): Luận án phân tích áp suất hướng kính giữa các lớp dây ($P_i$) sinh ra do quá trình "preforming" cáp. Áp suất này quyết định lực ma sát nội tại và khả năng dập tắt dao động của cáp mà không cần áp dụng lực căng ngoài.
2. **Mức P2 — Áp suất biên ngoài cố định (Fixed External Pressure / Preload):**
   - Áp suất hướng kính được áp đặt từ môi trường bên ngoài hoặc màng bao nhưng được giữ cố định ở một giá trị xác định trong suốt một chu trình uốn.
   - Bằng chứng tiêu biểu:
     - Tjahjanto et al. (2017, `ccdc1bb980`): Cáp ngầm chịu đồng thời lực căng dọc trục, áp suất hướng kính ngoài không đổi ($p = \text{const}$) và uốn chu kỳ; phân tích trạng thái dính - trượt (stick-slip) của các lõi dẫn điện.
     - Zhang & Yao et al. (2026, DOI: 10.5194/ms-17-481-2026): Thử nghiệm uốn các bó sợi dưới các mức áp suất dương cố định khác nhau ($p = 0.1, 0.2, 0.3\,\text{MPa}$).
3. **Mức P3 — Áp suất giam giữ chủ động biến thiên (Actively Varied Confinement Pressure):**
   - Áp suất giam giữ được điều khiển thay đổi liên tục theo thời gian $p(t)$ độc lập với lịch sử biến dạng uốn, hoặc thay đổi trong chính quá trình uốn.
   - Đây chính là cấu hình mà đề xuất MP1 nhắm tới.

---

## 2. Kiểm chứng Cơ học: Phương trình Hiện hữu có Tự nhiên Nhận $p(t)$ Không?

Astra đặt ra câu hỏi then chốt (G02): *Việc chuyển điều kiện biên áp suất từ hằng số (P2) sang biến thiên theo thời gian (P3) có đòi hỏi một phương trình cơ học mới, hay chỉ là giải cùng một hệ phương trình với điều kiện biên thay đổi?*

### 2.1. Phương trình Tiếp xúc Ma sát Cục bộ
Tại bất kỳ điểm tiếp xúc giữa hai dây trụ lân cận, định luật ma sát Coulomb cổ điển được biểu diễn ở dạng vi phân/gia số (incremental formulation):
$$\Phi = \|\mathbf{f}_t\| - \mu f_n \le 0$$
trong đó:
- $\mathbf{f}_t$ là véc-tơ lực tiếp tuyến (tangential friction force).
- $f_n$ là lực pháp tuyến (normal contact force).
- $\mu$ là hệ số ma sát tĩnh/động.

Quy tắc trượt (slip rule) theo lý thuyết đàn dẻo ma sát (frictional elastoplasticity):
$$\dot{\mathbf{u}}_t = \dot{\mathbf{u}}_t^e + \dot{\mathbf{u}}_t^p, \quad \dot{\mathbf{u}}_t^p = \dot{\lambda} \frac{\mathbf{f}_t}{\|\mathbf{f}_t\|}$$
với các điều kiện bổ sung Kuhn-Tucker:
$$\dot{\lambda} \ge 0, \quad \Phi \le 0, \quad \dot{\lambda} \Phi = 0$$

### 2.2. Sự Phụ thuộc của Lực Pháp tuyến vào Áp suất Biên $p(t)$
Trong một bó dây đặt trong màng bao chịu áp suất buồng $p(t)$, lực pháp tuyến $f_n$ tại các mặt tiếp xúc là nghiệm của bài toán cân bằng ứng suất trong tiết diện ngang:
$$\nabla \cdot \boldsymbol{\sigma} = \mathbf{0}, \quad \boldsymbol{\sigma} \cdot \mathbf{n}\big|_{\Gamma_{\text{ext}}} = -p(t) \mathbf{n}$$
Khi áp suất $p(t)$ thay đổi:
$$f_n(t) = \mathcal{K}_{\text{geom}} \cdot p(t) + f_{n,0}(\text{prestrain})$$
trong đó $\mathcal{K}_{\text{geom}}$ là toán tử hình học phụ thuộc vào cấu hình sắp xếp (packing geometry: lục giác đều, vòng tròn đồng tâm, hoặc bó ngẫu nhiên).

### 2.3. Đánh giá Khả năng Tiếp nhận của Lý thuyết Hiện hữu
Khi thay $p(t)$ vào hệ phương trình gia số:
1. Toán tử ma sát gia số (incremental contact operator) được tích hợp theo thời gian hoàn toàn tự nhiên:
   $$f_n(t_{k+1}) = f_n(t_k) + \Delta f_n(t)$$
   Nếu $p(t)$ tăng lên trong khi độ cong uốn $\kappa$ không đổi, giới hạn trượt $\mu f_n(t)$ tăng lên, lập tức biến một tiếp xúc đang ở trạng thái trượt ($\dot{\lambda} > 0$) trở lại trạng thái dính (re-sticking: $\dot{\lambda} = 0$).
2. Các phần mềm FEA phi tuyến hiện đại (như Abaqus, ANSYS, OpenSees) sử dụng thuật toán chiếu phản lực tiếp xúc (return mapping algorithm / penalty / Lagrange multipliers) **tự động xử lý lịch sử tải $p(t)$ biến thiên** mà không cần bất kỳ sự sửa đổi nào trong mã nguồn giải thuật.
3. Trong mô hình giải tích dầm uốn của Barsi et al. (2025, `9f4295be23`) hay Tjahjanto et al. (2017, `ccdc1bb980`), áp suất hướng kính đi vào phương trình thông qua việc dịch chuyển mặt giới hạn trượt (slip onset surface). Việc cho $p$ phụ thuộc thời gian $p(t)$ chỉ là việc cập nhật biến trạng thái theo từng bước tải.

---

## 3. Điều kiện để P3 Cấu thành Cơ học Mới Thực sự

Từ phân tích trên, Worker W05 khẳng định:
- **P3 không tự động là một cơ chế mới.** Nếu áp suất $p(t)$ chỉ đơn thuần làm thay đổi độ lớn của $f_n$ theo quy luật tĩnh và dịch ngưỡng trượt theo định luật Coulomb chuẩn, thì đây **hoàn toàn là lý thuyết cơ học tiếp xúc hiện hữu** được giải dưới một điều kiện biên tải trọng khác.
- **P3 chỉ cấu thành cơ học mới nếu và chỉ nếu:** Tồn tại một hiệu ứng phi tuyến phụ thuộc đường dẫn (path-dependent coupling) giữa tốc độ thay đổi áp suất $\dot{p}$ và động học chuyển pha NiTi hoặc sự tái cấu trúc mạng tiếp xúc mà mô hình tiếp xúc - cấu thành chuẩn **bỏ sót hoàn toàn**. Ví dụ:
  1. Sự biến thiên áp suất $p(t)$ làm thay đổi trường ứng suất thủy tĩnh đa trục $\sigma_m = \text{tr}(\boldsymbol{\sigma})/3$, qua đó làm thay đổi nhiệt độ chuyển pha cân bằng $T_0(p)$ của NiTi theo phương trình Clausius-Clapeyron mở rộng.
  2. Sự thay đổi $p(t)$ trong trạng thái đang trượt gây ra sự trượt giật (stick-slip instability / chatter) do biến thiên ma sát động học phụ thuộc tốc độ trượt.

Hiện tại, chưa có bất kỳ bằng chứng nào trong kho dữ liệu chứng minh các hiệu ứng trên là đáng kể trong miền vận hành chuẩn của robot mềm.

---

## 4. Kết luận của Worker W05

1. Phân loại P1/P2/P3 là sự phân loại về **giao thức điều khiển thực nghiệm**, không phải là ba lớp lý thuyết cơ học độc lập.
2. Các phương trình cơ học tiếp xúc ma sát và cấu thành vật liệu hiện hữu **hoàn toàn có khả năng tiếp nhận áp suất biến thiên $p(t)$**.
3. Do đó, việc chuyển từ P2 sang P3 không đủ để tuyên bố tính mới khoa học; mọi khẳng định tính mới cho MP1 dựa trên "active pressure" đơn độc đều bị bác bỏ.
