# W06: Phân tích Miền Cùng Tồn tại của Chuyển pha Siêu đàn hồi và Trượt Ma sát (T3 Transformation & Slip Coexistence Domain Analysis)

**Worker ID:** W06  
**Mục tiêu:** Phân tích định lượng và đánh giá điều kiện vật lý cần thiết để hiện tượng chuyển pha Martensite cảm ứng ứng suất và trượt ma sát giữa các dây (inter-wire slip) có thể cùng kích hoạt và tương tác trong miền vận hành của bó dây NiTi chịu uốn (giải quyết phê bình G03 của Astra).  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Bản chất Lỗ hổng G03 do Astra chỉ ra

Trong toàn bộ đề xuất của MP1, giả thuyết cốt lõi khẳng định rằng: *"Dưới tác động của áp suất giam giữ chủ động, có sự cạnh tranh và ghép cặp phức tạp giữa chuyển pha siêu đàn hồi của NiTi và sự trượt giữa các dây, tạo nên biến thiên độ cứng uốn phi tuyến đặc thù"*.

Tuy nhiên, Astra đã phát hiện ra lỗ hổng chí mạng (Critical Gap G03):
- **Chưa có bất kỳ bằng chứng thực nghiệm hay giải tích nào chứng minh rằng chuyển pha Martensite và trượt giữa các dây cùng hoạt động đồng thời trong miền biến dạng uốn thực tế của thiết bị.**
- Nếu trong miền vận hành, hai cơ chế này phân tách hoàn toàn thành hai chế độ độc lập (disjoint regimes), thì toàn bộ lập luận về "cơ chế ghép cặp mới" (coupled mechanics core) sẽ sụp đổ hoàn toàn.

---

## 2. Phân tích Cơ học: Điều kiện Kích hoạt của Từng Cơ chế

Xét một bó gồm $N_w$ dây NiTi hình trụ tròn đường kính $d$, xếp trong ống bao bán kính $R_b$, chịu áp suất giam giữ $p$ và độ cong uốn vĩ mô $\kappa$.

```
         ┌──────────────────────────────────────┐
         │         MÀNG BAO ÁP SUẤT p           │
         │  ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○    │  <- Các dây NiTi đường kính d
         │  ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○    │  <- Tiếp xúc ma sát fn, ft
         └──────────────────────────────────────┘
                   UỐN VĨ MÔ: Độ cong κ
```

### 2.1. Ngưỡng Kích hoạt Trượt giữa các Dây (Slip Onset: $\kappa_{\text{slip}}$)
Khi bó dây bắt đầu bị uốn từ trạng thái dính hoàn toàn (stick state), biến dạng cắt dọc trục giữa các dây liền kề tăng tỷ lệ với độ cong $\kappa$. Lực cắt tiếp tuyến trên một đơn vị chiều dài $q_t(x)$ tỷ lệ với mô-men uốn và diện tích mặt cắt:
$$q_t = \frac{V(x) \cdot Q}{I_{\text{stick}}}$$
Theo định luật ma sát Coulomb, trượt tương đối xảy ra khi lực tiếp tuyến vượt quá giới hạn ma sát pháp tuyến:
$$q_t \ge \mu \cdot q_n(p)$$
trong đó $q_n(p) \propto p \cdot d$ là lực nén pháp tuyến phân bố do áp suất giam giữ $p$ tạo ra.
Do đó, độ cong tới hạn để bắt đầu xuất hiện trượt vĩ mô ($\kappa_{\text{slip}}$) tỷ lệ thuận với áp suất giam giữ $p$:
$$\kappa_{\text{slip}}(p) = \mathcal{C}_{\text{geom}} \cdot \frac{\mu \, p}{E_A \, d}$$
trong đó $E_A$ là mô-đun đàn hồi của pha Austenite ($E_A \approx 50 - 70\,\text{GPa}$), và $\mathcal{C}_{\text{geom}}$ là hằng số hình học.

### 2.2. Ngưỡng Kích hoạt Chuyển pha Martensite (Transformation Onset: $\kappa_{\text{tr}}$)
Chuyển pha trực tiếp từ Austenite sang Martensite cảm ứng bởi ứng suất (stress-induced martensitic transformation) chỉ bắt đầu khi ứng suất kéo hoặc nén dọc trục tại thớ xa nhất của dây ngoài cùng vượt quá ứng suất tới hạn chuyển pha $\sigma_{\text{Ms}}$:
$$\sigma(y) \ge \sigma_{\text{Ms}}(T) = \sigma_0 + C_M (T - M_s)$$
Đối với hợp kim NiTi siêu đàn hồi ở nhiệt độ phòng ($T \approx 20 - 25^\circ\text{C}$):
- $\sigma_{\text{Ms}} \approx 400 - 500\,\text{MPa}$.
- Biến dạng đàn hồi giới hạn trước chuyển pha:
  $$\varepsilon_{\text{Ms}} = \frac{\sigma_{\text{Ms}}}{E_A} \approx \frac{450\,\text{MPa}}{60\,000\,\text{MPa}} \approx 0.75\% - 1.0\%$$
Độ cong uốn tới hạn để kích hoạt chuyển pha ở thớ ngoài cùng của bó dây ($\kappa_{\text{tr}}$) phụ thuộc vào bán kính bó dây $R_b$ (nếu ở trạng thái dính) hoặc bán kính từng sợi $d/2$ (nếu ở trạng thái trượt hoàn toàn):
- **Trường hợp dính hoàn toàn (Full Stick):** Biến dạng lớn nhất xảy ra ở thớ ngoài cùng của toàn bó:
  $$\varepsilon_{\text{max}} = \kappa \cdot R_b \implies \kappa_{\text{tr}}^{\text{stick}} = \frac{\varepsilon_{\text{Ms}}}{R_b}$$
- **Trường hợp trượt hoàn toàn (Full Slip):** Các dây tự do trượt qua nhau, biến dạng chỉ tích lũy cục bộ theo độ cong của từng dây:
  $$\varepsilon_{\text{max}} = \kappa \cdot \frac{d}{2} \implies \kappa_{\text{tr}}^{\text{slip}} = \frac{\varepsilon_{\text{Ms}}}{d/2} = \frac{2 \varepsilon_{\text{Ms}}}{d}$$

Vì $R_b \gg d/2$ (ví dụ: bó dây $R_b = 5\,\text{mm}$, dây sợi $d = 0.5\,\text{mm} \implies R_b / (d/2) = 20$), độ cong để kích hoạt chuyển pha trong trạng thái trượt lớn hơn gấp 20 lần so với trạng thái dính!

---

## 3. Ba Miền Cơ học và Nguy cơ Sụp đổ Giả thuyết Ghép cặp

Dựa trên mối tương quan giữa $\kappa_{\text{slip}}(p)$ và $\kappa_{\text{tr}}$, không gian trạng thái chia thành 3 miền rõ rệt:

```
Độ cong κ
   ▲
   │
   │  Miền III: TRƯỢT KẾT HỢP CHUYỂN PHA (Coexistence Domain)
   │  (Chỉ xảy ra khi tải uốn rất lớn HOẶC kéo căng hình học kết hợp)
───┼───────────────────────────────────────────── κ_tr(p)
   │  Miền II: TRƯỢT MA SÁT THUẦN TÚY (Pure Wire Jamming)
   │  - Vật liệu: Hoàn toàn Austenite đàn hồi (E = E_A = const)
   │  - Không có chuyển pha! (H0a ĐỦ KHẢ NĂNG DỰ ĐOÁN)
───┼───────────────────────────────────────────── κ_slip(p)
   │  Miền I: DÍNH HOÀN TOÀN (Full Stick / Elastic Beam)
   │  - Không trượt, không chuyển pha.
───┴─────────────────────────────────────────────► Áp suất p
```

### 3.1. Miền II: Biến dạng Nhỏ và Trung bình ($\kappa_{\text{slip}} \le \kappa < \kappa_{\text{tr}}$)
- **Đặc điểm:** Độ cong đủ để thắng lực ma sát gây trượt giữa các dây, nhưng biến dạng cực đại tại các dây vẫn nhỏ hơn ngưỡng $\varepsilon_{\text{Ms}} \approx 0.75\%$.
- **Hệ quả khoa học nghiêm trọng:**
  - Trong miền này, hợp kim NiTi **hoàn toàn ở pha Austenite đàn hồi tuyến tính**.
  - Không có bất kỳ mầm Martensite nào được hình thành, không có thềm ứng suất (plateau), không có trễ vật liệu siêu đàn hồi.
  - Toàn bộ cơ chế biến đổi độ cứng uốn ở miền này **chính là hiện tượng kẹt dây đàn hồi (elastic wire jamming)** truyền thống!
  - **Mô hình thay thế tham số đơn giản H0a (xem dây NiTi là thanh đàn hồi có mô-đun $E = E_A$) hoàn toàn dự đoán chính xác miền này.** Đề tài hoàn toàn mất tính mới ở miền này.

### 3.2. Miền I: Áp suất Giam giữ Rất Lớn ($p \to p_{\text{max}}$)
- **Đặc điểm:** Áp suất giam giữ quá lớn khiến $\kappa_{\text{slip}}(p) > \kappa_{\text{tr}}^{\text{stick}}$.
- **Hệ quả:** Bó dây bị khóa cứng không thể trượt (full stick). Biến dạng tăng nhanh và kích hoạt chuyển pha Martensite ở các thớ ngoài trước khi xảy ra trượt. Tuy nhiên, vì các dây không trượt qua nhau, hệ thống hành xử như một dầm vật liệu siêu đàn hồi liền khối (monolithic superelastic beam). Không có tương tác giữa chuyển pha và trượt ma sát!

### 3.3. Miền III: Miền Cùng Tồn tại Thực sự (Coexistence Domain)
- Để chuyển pha và trượt ma sát cùng hoạt động, hệ thống bắt buộc phải chịu:
  1. Độ cong uốn cực lớn (uốn góc gập sâu với bán kính uốn nhỏ hơn vài centimet); HOẶC
  2. Phải có lực kéo dọc trục đáng kể (axial tension) áp đặt trước để đưa ứng suất tiệm cận thềm $\sigma_{\text{Ms}}$ như trong cấu hình S1a của Carboni et al. (2015).
- Trong ứng dụng tay gắp hoặc robot mềm thông thường (uốn mềm dẻo với góc uốn vừa phải, biến dạng dưới 1%), **rất có thể toàn bộ chu trình hoạt động chỉ nằm trong Miền II**.

---

## 4. Kết luận của Worker W06

1. Astra hoàn toàn đúng khi chỉ ra rằng **chưa có bằng chứng xác nhận chuyển pha và trượt cùng hoạt động trong miền biến dạng thiết kế**.
2. Nếu không có thực nghiệm đo đạc độc lập chứng minh sự hình thành của pha Martensite trong dải áp suất và góc uốn vận hành, đề tài có nguy cơ bị quy giản hoàn toàn về bài toán kẹt dây đàn hồi (elastic wire jamming) đã bị tiền nhiệm đóng từ lâu.
3. Kế hoạch kiểm chứng tối thiểu bắt buộc phải bao gồm việc xác định ranh giới $\kappa_{\text{slip}}(p)$ và $\kappa_{\text{tr}}(p)$ bằng các phép đo biến dạng cục bộ hoặc nhiệt độ trước khi đưa ra bất kỳ kết luận nào về tính mới của cơ chế ghép cặp.
