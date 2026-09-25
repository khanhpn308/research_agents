# W09: Phân cấp Độ Tin cậy Mô hình và Hiện tượng Bù trừ Tham số (Model Validation Credibility & Parameter Confounding)

**Worker ID:** W09  
**Mục tiêu:** Thiết lập thang bậc phân cấp 5 tầng về độ tin cậy mô hình từ khớp đường cong đến chứng minh nhân quả; phân tích hiện tượng bù trừ tham số (parameter confounding / non-uniqueness) trong mô hình uốn bó dây có tiếp xúc ma sát (giải quyết phê bình G06 và G08 của Astra).  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Phân cấp 5 Tầng về Độ Tin cậy Mô hình (G06 Remediation)

Astra đã chỉ ra lỗ hổng nghiêm trọng G06: Các nghiên cứu và báo cáo trước đây thường đánh đồng sự tồn tại của mô hình giải tích, việc chạy thành công mô phỏng số, việc khớp số liệu thực nghiệm và việc kiểm chứng khoa học độc lập.

Worker W09 thiết lập thang bậc phân cấp chuẩn hóa gồm 5 tầng (5-Level Model Credibility Hierarchy):

```
┌────────────────────────────────────────────────────────────────────────┐
│ TẦNG 5: Chứng minh Nhân quả Cơ chế (Causal Identification)            │
│ Các biến trạng thái nội vi mô (độ trượt, phần thể tích pha ξ,         │
│ trường nhiệt) được đo độc lập và khớp với mô hình.                    │
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 4: Kiểm chứng Thực nghiệm Độc lập (Experimental Validation)       │
│ Mô hình với bộ tham số ĐƯỢC KHÓA (locked) dự đoán chính xác các       │
│ đường tải uốn MỚI chưa từng dùng trong cân chỉnh.                     │
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 3: Cân chỉnh Tham số / Khớp Đường cong (Parameter Calibration)   │
│ Tinh chỉnh các tham số tự do để làm vừa khít một đường cong đo đạc;   │
│ R² cao nhưng có nguy cơ bù trừ tham số rất lớn.                       │
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 2: Kiểm chứng Số học (Numerical Verification)                     │
│ Thuật toán hội tụ, bảo toàn năng lượng, giải đúng bài toán toán học.   │
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 1: Thiết lập Mô hình / Tồn tại Công thức (Model Formulation)      │
│ Hệ phương trình vi phân và điều kiện biên được viết ra trên giấy.      │
└────────────────────────────────────────────────────────────────────────┘
```

### 1.1. Định vị Trạng thái của các Nghiên cứu Tiền nhiệm trong Ma trận V002
- **Fang et al. (2019, `2f7fcf2f8f`):** Đạt **Tầng 3** (Calibration). Mô hình OpenSees phân chia các lớp sợi tương đương và gán vật liệu Steel02 kết hợp Self-centering để khớp đường cong kéo của cáp; chưa có kiểm chứng độc lập dưới tải uốn hay đo đạc trượt vi mô.
- **Vahidi et al. (2022, `53200aa0c6`):** Đạt **Tầng 3–4** cho tải kéo đơn trục. Mô hình Abaqus FEA 3D sử dụng tham số Auricchio từ mẫu thử kéo độc lập của Reedlunn và tái tạo được đường cong kéo cáp 1x27 và 7x7; nhưng chưa mở rộng sang tải uốn dưới áp suất thay đổi.
- **Barsi, Carboni, Lacarbonara (2025, `9f4295be23`):** Đạt **Tầng 4** cho dầm cáp thép chịu uốn thuần túy. Dự đoán chính xác hai cận trên và cận dưới của độ cứng uốn (stick/slip bounds) với các chiều dài dầm khác nhau mà không cần thay đổi bộ tham số đàn hồi của thép.
- **Zhang & Yao (2026):** Đạt **Tầng 3** cho kẹt sợi nylon dưới áp suất dương. Khớp tốt mô-men kháng uốn nhưng chưa đo trực tiếp lực tiếp xúc nội tại giữa các sợi.

---

## 2. Hiện tượng Bù trừ và Không Duy nhất của Tham số (G08 Remediation)

Astra nhấn mạnh trong G08: Có quá nhiều tham số tự do có thể bù trừ lẫn nhau trong phép khớp số liệu uốn, dẫn đến việc mô hình có thể đạt hệ số xác định $R^2 \approx 0.99$ nhưng hoàn toàn sai lệch về mặt cơ chế vật lý.

### 2.1. Phân tích Trường hợp Điển hình từ Fang 2019 (PDF Trang 11–12)
Trong tệp `data/papers/verification/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf`, chính nhóm tác giả Fang đã thừa nhận rằng:
- Việc chia tiết diện cáp thành các vùng sợi đồng tâm với tỷ lệ diện tích khác nhau và gán các ngưỡng ứng suất kích hoạt chuyển pha khác nhau cho phép **nhiều tổ hợp tham số hoàn toàn khác nhau cùng tạo ra một đường cong trễ kéo giống hệt nhau**.
- Tham số vật liệu "Steel02" chỉ là một công cụ hiện tượng học để mô phỏng biến dạng dư và suy thoái chu kỳ; nó không đại diện cho một lõi thép vật lý thực sự nào bên trong cáp NiTi.
- Do đó, việc mô hình khớp hoàn hảo số liệu thực nghiệm **không chứng minh tính duy nhất (uniqueness) hay tính xác thực vật lý của các tham số đó**.

### 2.2. Sự Bù trừ giữa Áp suất, Hệ số Ma sát và Hình học Sắp xếp
Xét phương trình ma sát Coulomb giới hạn lực trượt:
$$F_{\text{cap}} = \mu \cdot f_n$$
Trong bài toán bó dây chịu áp suất buồng $p$:
$$f_n = \alpha_{\text{trans}} \cdot p \cdot d + f_{n,0}(\text{prestrain})$$
trong đó $\alpha_{\text{trans}}$ là hệ số truyền áp suất qua màng và bó dây.
Khi đưa vào bài toán uốn dầm, mô-men trượt tới hạn $M_{\text{slip}}$ tỷ lệ thuận với $F_{\text{cap}}$:
$$M_{\text{slip}} \propto \mu \cdot \alpha_{\text{trans}} \cdot p$$

**Hệ quả toán học:**
1. Trong một phép đo mô-men uốn vĩ mô $M(\kappa, p)$, dữ liệu thực nghiệm chỉ ràng buộc được **tích số $(\mu \cdot \alpha_{\text{trans}})$**, hoàn toàn không thể tách rời $\mu$ và $\alpha_{\text{trans}}$.
2. Một nghiên cứu có thể dùng hệ số ma sát quá thấp ($\mu = 0.1$) kết hợp với hệ số truyền áp suất quá cao ($\alpha_{\text{trans}} = 1.0$), hoặc ngược lại ($\mu = 0.5, \alpha_{\text{trans}} = 0.2$), cả hai đều cho ra đường cong $M(\kappa)$ giống hệt nhau!
3. Nếu người nghiên cứu lại đưa thêm mô-đun đàn hồi tương đương $E_{\text{eff}}$, độ cứng tiếp xúc phạt $k_{\text{pen}}$, và biến dạng dự ứng suất ban đầu $\varepsilon_0$ vào quá trình tối ưu hóa đa tham số, thì hiện tượng bù trừ (parameter confounding) sẽ trở nên vô cùng trầm trọng.

---

## 3. Nguy cơ "Tính Kép Độ Mềm" (Double-Counting Compliance)

Một cạm bẫy phương pháp luận nghiêm trọng được Astra cảnh báo:
- Nếu một nhà nghiên cứu đo độ cứng uốn của toàn bộ bó cáp, sau đó dùng đường cong này để suy ra một "mô-đun đàn hồi tương đương" $E_{\text{bundle}}$ (đã bao gồm độ mềm do trượt giữa các dây và độ rỗng hình học);
- Rồi sau đó lại đưa giá trị $E_{\text{bundle}}$ này vào một mô hình phần tử hữu hạn 3D đã mô phỏng chi tiết từng sợi dây và bề mặt tiếp xúc;
- Hệ quả là: **Độ mềm của kết cấu sẽ bị tính hai lần (double-counting compliance)**, dẫn đến việc mô phỏng dự đoán độ cứng uốn thấp hơn thực tế rất nhiều, và sau đó sai lệch này lại bị đổ lỗi cho "hiệu ứng chuyển pha NiTi chưa được mô hình hóa"!

---

## 4. Quy tắc Kiểm chứng Bắt buộc để Vượt qua G06 và G08

Để đảm bảo kết quả kiểm chứng đạt **Tầng 4 và Tầng 5**, nghiên cứu bắt buộc phải tuân thủ nghiêm ngặt 3 quy tắc sau:

1. **Quy tắc Phân tách Hiệu chuẩn (Decoupled Calibration):**
   - Mọi tham số vật liệu của NiTi ($E_A, E_M, \sigma_{\text{Ms}}, \sigma_{\text{Mf}}, \sigma_{\text{As}}, \sigma_{\text{Af}}$) phải được đo đạc và hiệu chuẩn từ thí nghiệm kéo dây đơn lẻ.
   - Hệ số ma sát $\mu$ phải được đo từ thí nghiệm trượt tiếp xúc phẳng hoặc hai sợi dây vắt chéo độc lập dưới dải tải trọng pháp tuyến tương ứng.
   - Hệ số truyền áp suất $\alpha_{\text{trans}}$ phải được đo bằng thí nghiệm nén hướng kính tĩnh không uốn.
2. **Quy tắc Khóa Tham số Tuyệt đối (Strict Locked Parameters):**
   - Khi chạy mô phỏng dự đoán đáp ứng uốn dưới các mức áp suất $p(t)$ khác nhau, **toàn bộ các tham số trên phải được khóa cố định**.
   - Tuyệt đối cấm việc cho phép mỗi mức áp suất hoặc mỗi chu kỳ tải có một bộ tham số hiệu chỉnh riêng.
3. **Phân tích Độ nhạy Toàn cục (Global Sensitivity & Identifiability Analysis):**
   - Thực hiện phân tích ma trận tương quan tham số (parameter correlation matrix) và phân tích Sobol để chứng minh rằng các cơ chế đề xuất không bị triệt tiêu bởi sai số của các biến hình học.

---

## 5. Kết luận của Worker W09

1. Việc chỉ đạt Tầng 3 (khớp đường cong) không có giá trị chứng minh sự tồn tại của cơ chế cơ học mới.
2. Sự bù trừ tham số giữa áp suất truyền, ma sát và độ cứng đàn hồi có thể tạo ra ảo tưởng về một mô hình hoàn hảo trong khi bản chất cơ học bị sai lệch.
3. Muốn chứng minh sự cần thiết của một lý thuyết mới (H1), mô hình hiện hữu (H0b) phải thất bại trong một phép thử dự đoán có **tham số bị khóa hoàn toàn** (Tầng 4).
