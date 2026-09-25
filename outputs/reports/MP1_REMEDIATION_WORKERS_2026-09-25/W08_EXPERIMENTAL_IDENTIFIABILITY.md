# W08: Khả năng Nhận diện Thực nghiệm của Cơ chế so với Đại lượng Đo (Experimental Identifiability of Mechanisms vs Observables)

**Worker ID:** W08  
**Mục tiêu:** Phân tích toàn diện thách thức về khả năng nhận diện thực nghiệm (experimental identifiability), phân tách các cơ chế vật lý bị chồng lấn trong dữ liệu uốn vĩ mô, kiểm chứng ánh xạ áp suất – lực pháp tuyến, và chuẩn hóa định nghĩa các đại lượng đo độ cứng uốn (giải quyết phê bình G04, G09 và G12 của Astra).  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Vấn đề Nhận diện Thực nghiệm trong Cơ học Uốn Bó dây (G04 Remediation)

Astra đã cảnh báo mạnh mẽ trong phê bình G04:
- Một đường cong lực – độ dịch chuyển ($F - \delta$) hoặc mô-men – độ cong ($M - \kappa$) vĩ mô là kết quả tích hợp của toàn bộ kết cấu.
- Từ dữ liệu vĩ mô đơn độc, **hoàn toàn không thể phân biệt được** sự sụt giảm độ cứng (softening) là do trượt giữa các dây (inter-wire slip), do chuyển pha siêu đàn hồi (martensitic transformation), do biến dạng hình học tiết diện (cross-sectional distortion/flattening), hay do sự lún/trượt tại ngàm kẹp (grip compliance).

### 1.1. Ma trận Chồng lấn Cơ chế (Mechanism Confounding Matrix)

| Biểu hiện Vĩ mô | Cơ chế Vật lý 1 (Ma sát / Hình học) | Cơ chế Vật lý 2 (Vật liệu NiTi) | Cơ chế Gây nhiễu Khác (Artifacts) |
|---|---|---|---|
| **Giảm độ cứng (Softening)** | Dây bắt đầu trượt qua nhau khi vượt ngưỡng ma sát ($f_t > \mu f_n$). | Ứng suất vượt ngưỡng chuyển pha $\sigma_{\text{Ms}}$, bắt đầu xuất hiện pha Martensite mềm hơn. | Tiết diện bó dây bị bẹp (ovalization), hoặc các dây ngoài bị xô lệch khỏi vị trí. |
| **Diện tích vòng trễ (Hysteresis Loop)** | Tiêu tán năng lượng do công ma sát trượt khô giữa các bề mặt dây ($W_{\text{fric}} = \oint \mathbf{f}_t \cdot d\mathbf{u}_t$). | Tiêu tán năng lượng vi mô do chuyển pha tinh thể không thuận nghịch nhiệt động (microscopic phase transformation dissipation). | Trễ do vật liệu màng bao đàn hồi (viscoelastic membrane) hoặc ma sát tại gối đỡ/ngàm. |
| **Độ cứng tăng trở lại (Hardening)** | Bó dây bị nén chặt (jammed packing lockup), các dây tựa cứng vào nhau hoặc chạm giới hạn hành trình. | Chuyển pha kết thúc, vật liệu chuyển hoàn toàn sang pha Martensite biến dạng đàn hồi ($E_M$). | Hiệu ứng kéo căng hình học lớn (geometric stretching) do ngàm cố định khoảng cách hai đầu. |

Nếu chỉ đo lực uốn ở đầu dầm, việc quan sát thấy một đường cong uốn phi tuyến không thể chứng minh sự tồn tại của cơ chế ghép cặp NiTi mới. Bất kỳ sự sai khác nào so với mô hình đơn giản đều có thể bị gán ghép sai thành "hiệu ứng NiTi đặc biệt".

---

## 2. Kiểm chứng Ánh xạ từ Áp suất Buồng sang Lực Pháp tuyến Tiếp xúc (G09 Remediation)

Astra chỉ ra trong G09: Áp suất đo được trong buồng $p$ không đồng nhất với lực nén pháp tuyến $f_n$ tại từng điểm tiếp xúc giữa các dây.

```
       ÁP SUẤT BUỒNG p
             │
             ▼
     ┌───────────────┐
     │ Màng bao đàn  │  <── Tổn thất do ứng suất kéo màng (membrane hoop tension)
     │ hồi (Sleeve)  │
     └───────┬───────┘
             │ Áp lực tiếp xúc ngoài: σ_r
             ▼
     ┌───────────────┐
     │ Cấu hình sắp  │  <── Độ rỗng ban đầu (initial void ratio), sự xô lệch ngẫu nhiên,
     │ xếp (Packing) │      tự khóa hình học (geometric arching)
     └───────┬───────┘
             │
             ▼
     LỰC PHÁP TUYẾN TIẾP XÚC NỘI TẠI: f_n
```

### 2.1. Các Yếu tố Che chắn và Biến dạng Lực Pháp tuyến
1. **Ứng suất vòng của màng bao (Membrane Hoop Stress):**
   Màng bao cao su/silicone có độ dày và độ cứng hữu hạn. Một phần đáng kể của áp suất $p$ bị tiêu hao để làm căng màng:
   $$\sigma_{r,\text{ext}} = p - \frac{t_{\text{mem}}}{R_{\text{mem}}} \sigma_{\theta,\text{mem}}$$
2. **Hiệu ứng Vòm và Độ rỗng Hình học (Geometric Arching & Packing Uncertainty):**
   Trong một bó gồm hàng chục dây song song, lực tiếp xúc không phân bố đều. Các dây ngoài cùng chịu tải lớn hơn, trong khi các dây bên trong có thể bị che chắn bởi hiệu ứng vòm (arching effect).
3. **Lực căng dọc trục phụ phụ thuộc áp suất:**
   Khi buồng áp suất kín khí được bơm căng, hiệu ứng nắp đáy (end-cap effect) có thể tạo ra lực kéo dọc trục bổ sung lên bó dây, làm tăng ứng suất kéo và kích hoạt chuyển pha sớm mà không phải do uốn.

**Kết luận G09:** Nếu không hiệu chuẩn độc lập mối quan hệ $p \to f_n$ bằng các cảm biến màng áp lực mỏng hoặc đo độ biến dạng hướng kính, mọi sai số trong việc ước lượng $f_n$ sẽ bị che đậy và ngụy trang thành sai số của luật cấu thành NiTi hoặc sai số của hệ số ma sát $\mu$.

---

## 3. Chuẩn hóa Định nghĩa Đại lượng Đo Độ cứng Uốn (G12 Remediation)

Astra nhấn mạnh trong G12: Khái niệm "độ cứng uốn" (bending stiffness) trong các tài liệu kiểm chứng thường bị dùng chung mà không chỉ rõ định nghĩa toán học và lịch sử tải, dẫn đến các kết luận mâu thuẫn.

Báo cáo khoa học chuẩn hóa 3 định nghĩa toán học riêng biệt:

```
Mô-men uốn M
   ▲                       / (Nhánh tải: loading branch)
   │                      / 
   │        B           /  
   │       /│         /   
   │      / │       /     
   │     /  │     /  
   │    /   │   /   
   │   /    │ / (Nhánh dỡ tải: unloading branch)
   │  A─────C
   │  │◄─Δκ─►│
   └────────────────────────► Độ cong uốn κ
```

1. **Độ cứng Tiếp tuyến (Tangent Bending Stiffness: $D_{\text{tan}}$):**
   $$D_{\text{tan}}(\kappa, p, \text{history}) = \left.\frac{\partial M}{\partial \kappa}\right|_{p = \text{const}}$$
   - Phụ thuộc mạnh vào nhánh tải (loading vs unloading).
   - Tại điểm bắt đầu trượt hoặc bắt đầu chuyển pha, $D_{\text{tan}}$ có thể giảm đột ngột (thậm chí tiệm cận 0 trên thềm chuyển pha).
2. **Độ cứng Cát tuyến (Secant Bending Stiffness: $D_{\text{sec}}$):**
   $$D_{\text{sec}}(\kappa, p) = \frac{M(\kappa, p) - M_0}{\kappa - \kappa_0}$$
   - Thường được dùng trong các báo cáo robot mềm để đo khả năng kháng uốn tổng thể tại một góc uốn cực đại xác định.
   - Luôn làm mịn (smooth out) các bước nhảy cục bộ của trạng thái dính - trượt và chuyển pha.
3. **Độ cứng Động học Chu kỳ Nhỏ (Dynamic / Storage Bending Stiffness: $D_{\text{dyn}}$):**
   $$D_{\text{dyn}}(\kappa_0, p, \omega) = \frac{\Delta M}{\Delta \kappa} \cos(\delta)$$
   - Đo bằng dao động biên độ nhỏ ($\Delta \kappa \ll \kappa_0$) xung quanh một trạng thái uốn tĩnh có sẵn $\kappa_0$.
   - Vì biên độ dao động rất nhỏ, các dây có thể ở trạng thái dính cục bộ (micro-stick), khiến $D_{\text{dyn}}$ xấp xỉ cận trên của độ cứng (stick bound) ngay cả khi $D_{\text{tan}}$ vĩ mô đang ở trạng thái trượt.

---

## 4. Yêu cầu Thực nghiệm Tối thiểu để Tách bạch Cơ chế

Để vượt qua thử thách về khả năng nhận diện, hệ thống đo đạc thực nghiệm bắt buộc phải có:
1. **Đo biến dạng quang học bề mặt (DIC / Fiber Bragg Gratings):** Gắn sợi FBG hoặc dùng camera DIC để đo trực tiếp độ cong cục bộ $\kappa(x)$ và phát hiện biến dạng dọc trục của từng sợi riêng lẻ, tách biệt hoàn toàn độ trượt của ngàm.
2. **Đo nhiệt độ bề mặt đồng thời (Thermal Imaging):** Chuyển pha Martensite là một quá trình tỏa nhiệt khi tải và thu nhiệt khi dỡ tải ($\Delta H_{\text{tr}} \approx 10 - 20\,\text{J/g}$), trong khi ma sát trượt chỉ sinh nhiệt đơn chiều. Ảnh nhiệt hồng ngoại là công cụ phân biệt tuyệt đối giữa chuyển pha và trượt ma sát.
3. **Cảm biến dịch chuyển tương đối tại đầu dây (LVDT / Macro-photography):** Đo trực tiếp chuyển vị trượt tương đối $\Delta u_{\text{slip}}$ giữa các đầu dây tại vị trí tự do. Nếu các đầu dây không trượt tương đối, kết luận dứt khoát không có hiện tượng inter-wire slip.

---

## 5. Kết luận của Worker W08

1. Dữ liệu mô-men – góc uốn vĩ mô đơn độc là **hoàn toàn không đủ** để nhận diện cơ chế ghép cặp NiTi.
2. Áp suất buồng $p$ bắt buộc phải được hiệu chuẩn sang lực nén tiếp xúc $f_n$ thông qua việc xét đến độ cứng màng bao và hình học bó dây.
3. Mọi công bố về độ cứng uốn phải ghi rõ là độ cứng tiếp tuyến, cát tuyến hay động học, cùng với lịch sử tải và nhiệt độ đo.
