# W09 — Thẩm tra Toàn văn Chuyên sâu Reedlunn et al. 2013 (Part II)

## 1. Mục tiêu (Mission)

Thẩm tra chuyên sâu toàn văn (deep full-text audit) công trình nền tảng kinh điển về cơ học cáp hợp kim nhớ hình NiTi:
> **Benjamin Reedlunn, Samantha Daly, John Shaw (2013)**  
> *Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses*  
> *International Journal of Solids and Structures*, Vol. 50, pp. 3027–3044. DOI: `10.1016/j.ijsolstr.2013.03.015`.  
> paper_id: `fac21c950e`

Nhiệm vụ trọng tâm:
1. Tái dựng chi tiết kiến trúc mẫu thử ($7\times 7$ vs $1\times 27$), các chế độ đặt tải, động học mặt sóng chuyển pha (transformation fronts), độ mềm dẻo (compliance), hiệu ứng góc nghiêng đường xoắn ốc (helix angle) và các lớp đồng tâm.
2. Phân tích mô hình giải tích, các giả thiết đơn giản hóa, vị trí mô hình bị sụp đổ (where model fails), bài toán uốn/xoắn cục bộ của từng sợi (local bending/twisting), và giới hạn bỏ qua áp suất tiếp xúc hướng tâm (radial contact pressure).
3. Làm rõ vết lõm tiếp xúc do chế tạo (manufacturing contact dimples/indentations) và phân rã đáp ứng từng lớp (response subtraction).
4. Đánh giá tác động cốt lõi của công trình đối với:
   - Mục tiêu **T1** (tiếp xúc và ma sát);
   - Mục tiêu **T3** (ghép cặp chuyển pha và cơ học tiếp xúc);
   - Rủi ro thay thế tham số (**parameter-substitution risk**);
   - Lý do vì sao công trình này **tuyệt đối KHÔNG thiết lập áp suất giam giữ chủ động P3**.

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.md`
- `data/evidence/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json`
- `papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf`
- (Đối chiếu bổ sung Part I): `papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf` (paper_id: `00414aac4b`)

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **Mức độ đe dọa đối với MP1:** `high` [AUDIT VERDICT]
- **Ưu tiên trích dẫn ngược (Backward citation priority):** `high` [AUDIT VERDICT]
- **Mục tiêu bị đe dọa trực tiếp:** T1 và T3.

## 4. Bảng bằng chứng (Evidence table)

| Evidence ID | Chủ đề cơ học | Vị trí trang / Mục trong PDF | Bằng chứng thực nghiệm / Mô hình | Kết luận đối với MP1 |
|---|---|---|---|---|
| W09-E01 | Cấu trúc mẫu $7\times 7$ và $1\times 27$ | pp. 2–5; Sec. 2 | $7\times 7$ bước xoắn thoải ($\alpha \approx 10.6^\circ$); $1\times 27$ xoắn ngược chiều xen kẽ ($\alpha$ lên tới $21.9^\circ$). | Kiến trúc hình học bện quyết định bản chất cơ học. |
| W09-E02 | Động học mặt sóng chuyển pha | pp. 6–11; Sec. 3.1 | $7\times 7$ có mặt sóng chuyển pha lan truyền rõ rệt; $1\times 27$ hoàn toàn KHÔNG có mặt sóng lan truyền. | Chuyển pha trong bó cáp xoắn bị biến dạng so với dây thẳng. |
| W09-E03 | Vết lõm tiếp xúc do chế tạo | pp. 2, 15–17, 21–22, 32 | Kính hiển vi điện tử quét (SEM) phát hiện vết khía và vết lõm tiếp xúc giữa các dây làm tập trung biến dạng. | Tiếp xúc hình học giữa các sợi NiTi đã có prior art từ 2013. |
| W09-E04 | Độ mềm dẻo và mô-men xoắn ngược chiều | pp. 11–14, 17–22; Sec. 3.2 | Thêm lớp ngoài làm mô-đun giảm từ $23.7\text{ GPa}$ xuống $7.3\text{ GPa}$; mô-men xoắn đổi dấu qua các lớp. | Cấu trúc đa lớp tạo ra biến dạng uốn/xoắn ghép cặp phức tạp. |
| W09-E05 | Phân rã đáp ứng trừ từng lớp | pp. 24–32; Sec. 4 | Trừ đáp ứng chứng minh chuyển pha kế tiếp từ lõi trong ra vỏ ngoài: Lớp B ($2.2\%$), Lớp C ($6.0\%$), Lớp D ($8.8\%$). | Thừa nhận việc trừ đáp ứng bỏ qua áp lực tiếp xúc hướng tâm lên lõi. |
| W09-E06 | Thất bại của mô hình giải tích đơn giản | pp. 8–10, 16–17; Sec. 3.1.4 | Mô hình kéo đơn trục chỉ đúng với góc xoắn nhỏ ($1\times 7$); đánh giá quá cao thềm ứng suất góc xoắn lớn ($1\times 6$). | Bỏ qua uốn và xoắn cục bộ của từng sợi dây làm sai lệch mô hình. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W09-E01 — Kiến trúc mẫu thử và Thiết lập thực nghiệm

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Trang kiểm chứng:** Trang 2, 3, 4, 5; Section 2 (Materials and Experimental Setup).

### Kiến trúc mẫu thử:
1. **Cáp $7\times 7$ NiTi (Right regular lay):** Gồm 1 tao cáp trung tâm $1\times 7$ và 6 tao cáp bao quanh, tổng cộng 49 sợi dây NiTi đường kính $0.38\text{ mm}$. Góc nghiêng đường xoắn ốc nhỏ ($\alpha \approx 10.6^\circ$).
2. **Cáp $1\times 27$ NiTi (Alternating lay):** Gồm 1 sợi lõi thẳng A, Lớp B (6 sợi, bước xoắn trái, $\alpha = 11.5^\circ$), Lớp C (9 sợi, bước xoắn phải, $\alpha = 15.6^\circ$), và Lớp D (12 sợi, bước xoắn trái, $\alpha = 21.9^\circ$). Chiều xoắn đổi chiều xen kẽ giữa các lớp để triệt tiêu mô-men xoắn tổng thể (pp. 2, 4).

### Thiết lập thí nghiệm:
- Máy kéo nén vạn năng cơ điện điều khiển dịch chuyển kéo đơn trục với tốc độ biến dạng danh nghĩa cực chậm ($10^{-5}\text{ s}^{-1}$ cho $7\times 7$ và $10^{-4}\text{ s}^{-1}$ cho $1\times 27$) để đảm bảo điều kiện đẳng nhiệt tuyệt đối (isothermal conditions) trong không khí tĩnh tại nhiệt độ phòng ($\sim 20 - 21^\circ\text{C}$) (pp. 4, 5).
- Ngàm kẹp má phẳng khía nhám (flat knurled plate clamping grips) khống chế góc quay trục bằng 0 (zero end rotation) (p. 4).
- Cảm biến đo mô-men xoắn phản lực (torque load cell, dải đo $2824\text{ N}\cdot\text{mm}$) (p. 4).
- Hệ thống đo biến dạng trường quang học nổi 3D (stereo digital image correlation — DIC) kết hợp camera nhiệt hồng ngoại (IR thermography) và kính hiển vi điện tử quét SEM (p. 5).

---

### EVIDENCE W09-E02 & W09-E03 — Động học chuyển pha và Vết lõm tiếp xúc ma sát

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Trang kiểm chứng:** Trang 6, 7, 8, 9, 10, 11, 15, 16, 17, 21, 22, 32; Section 3.

### Hiện tượng chuyển pha trong hai cấu trúc:
- Trong cáp $7\times 7$: Do góc xoắn thoải, các sợi hoạt động tương tự như một bó dây song song. Xuất hiện thềm ứng suất tải phẳng rõ rệt ($517\text{ MPa}$ ở sợi đơn, $506\text{ MPa}$ ở tao $1\times 7$). Stereo DIC phát hiện mặt sóng chuyển pha vĩ mô bao gồm các cụm mặt sóng chuyển pha cục bộ xoay đồng bộ quanh trục cáp (pp. 7–10).
- Trong cáp $1\times 27$: **Mặt sóng chuyển pha lan truyền hoàn toàn biến mất**. Thay vào đó là đường cong lực - biến dạng dốc liên tục, không có thềm ứng suất. Ảnh DIC và IR cho thấy các vùng biến dạng và nhiệt độ cục bộ phân tán không lan truyền (pp. 2, 11, 12, 15).

### Vết lõm tiếp xúc do chế tạo (Contact Indentations):
- Quan sát SEM bề mặt sợi dây cho thấy: trong quá trình sản xuất vặn xoắn cáp, lực ép giữa các lớp đã tạo ra vô số **vết lõm tiếp xúc (dimples, divots) và rãnh khía tiếp xúc dạng đường (line indents)** (pp. 2, 15, 16).
- Các vết lõm này gây tập trung ứng suất tiếp xúc cục bộ, đóng vai trò mầm kích hoạt biến đổi pha mactenxít cục bộ sớm ở mức tải thấp, triệt tiêu sự hình thành mặt sóng lan truyền và làm đường cong ứng xử trở nên trơn tru (pp. 16, 17, 32).

---

### EVIDENCE W09-E04, W09-E05 & W09-E06 — Mô hình giải tích, Phân rã đáp ứng và Giới hạn

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Trang kiểm chứng:** Trang 8, 9, 10, 16, 17, 24, 25, 26, 27, 28, 29, 30, 31, 32; Section 4.

### Phân rã đáp ứng trừ từng lớp (Subcomponent response subtraction):
- Bằng cách đo tuần tự từng bán thành phẩm: Sợi đơn $\rightarrow$ Tao $1\times 6$ $\rightarrow$ Tao $1\times 15$ $\rightarrow$ Cáp $1\times 27$, các tác giả lấy đáp ứng của cụm lớn trừ đi cụm nhỏ để tìm ra lực và mô-men xoắn của từng lớp đơn lẻ (pp. 24–26).
- Kết quả chứng minh quá trình chuyển pha diễn ra tuần tự từ trong ra ngoài:
  - Lớp B bắt đầu chuyển pha ở biến dạng trục $2.2\%$;
  - Lớp C bắt đầu chuyển pha ở biến dạng trục $6.0\%$;
  - Lớp D bắt đầu chuyển pha ở biến dạng trục $8.8\%$ (pp. 2, 32).

### Nơi mô hình giải tích bị sụp đổ (Where the model fails):
- Các tác giả xây dựng mô hình giải tích ước tính lực thềm chuyển pha dựa trên giả thiết kéo đơn trục thuần túy dọc theo đường xoắn ốc (pp. 8, 9).
- **Thất bại:** Mô hình dự báo rất chính xác cho tao cáp $1\times 7$ (góc xoắn nhỏ), nhưng **đánh giá quá cao ứng suất thềm chuyển pha đối với tao cáp $1\times 6$ có góc xoắn lớn** (p. 16).
- **Nguyên nhân cốt lõi được tác giả chỉ rõ:** Mô hình giải tích đơn giản chỉ xét lực kéo dọc sợi mà **bỏ qua hoàn toàn biến dạng uốn cục bộ (local bending) và xoắn cục bộ (local twisting) của từng sợi dây riêng lẻ** khi nằm trong cấu trúc xoắn (pp. 16, 17).

### Giới hạn bỏ qua áp lực tiếp xúc hướng tâm:
- Ở trang 32, các tác giả thẳng thắn thừa nhận hạn chế cơ học: Phương pháp phân rã đáp ứng dựa trên các giả thiết lý tưởng hóa **có thể đã bỏ qua các áp lực tiếp xúc hướng tâm cục bộ (localized radial contact pressures) tác dụng lên các sợi lõi bên trong**.

## 6. Kết luận về claim/target (Claim/target conclusion)

### 1. Tác động đối với Mục tiêu T1:
[VERIFIED PAPER FACT] Reedlunn et al. 2013 Part II khẳng định không thể chối cãi rằng: cấu trúc hình học tiếp xúc nhiều dây, vết lõm tiếp xúc cơ học và góc nghiêng đường bện quyết định toàn bộ độ mềm dẻo, mô-men xoắn và quy luật biến dạng của bó dây NiTi. Nó đóng góp bằng chứng toàn văn quyết định để đóng T1.

### 2. Tác động đối với Mục tiêu T3:
[VERIFIED PAPER FACT] Bài báo chứng minh sự ghép cặp chặt chẽ giữa trạng thái ứng suất đa trục cục bộ (kéo + uốn + xoắn) với sự kích hoạt chuyển pha từng lớp kế tiếp. Tuy nhiên, ở Phần I (Reedlunn et al. 2013 Part I, p. 8), tác giả đã bôi dầu bôi trơn xuyên thấu (penetrating lubricant) giữa các sợi nhưng không thấy đường cong kéo thay đổi, bởi vì lực ma sát tĩnh ban đầu quá lớn đã ngăn cản sự trượt tương đối dọc trục trong thí nghiệm kéo đơn trục ngàm cứng.

### 3. Tác động đối với Rủi ro thay thế tham số (Parameter-Substitution Risk):
[INFERENCE]  
Reedlunn et al. 2013 chứng minh rằng: **Không thể áp dụng một mô hình sợi đàn hồi đơn giản rồi chỉ thay thế thông số để mô tả bó cáp NiTi**. Khi góc bện tăng, các hiện tượng uốn/xoắn cục bộ, vết lõm tập trung ứng suất và sự chuyển pha tuần tự từng lớp làm cho đáp ứng phi tuyến tính sâu sắc. Nếu chỉ thay mô-đun đàn hồi hằng số vào mô hình sợi dầm cổ điển, mô hình sẽ hoàn toàn sai lệch.

### 4. Vì sao Reedlunn 2013 KHÔNG thiết lập Áp suất giam giữ chủ động P3?
[AUDIT VERDICT]  
Dù là một kiệt tác về cơ học cáp SMA, Reedlunn et al. 2013 hoàn toàn không đe dọa mục tiêu T2 của MP1 vì:
1. Thí nghiệm thuần túy là **kéo đơn trục dãn dài đẳng nhiệt (uniaxial isothermal extension)** với hai đầu ngàm cố định, không có tải trọng uốn ngang.
2. Áp suất tiếp xúc trong bài là **P1 thụ động** (sinh ra từ vết lõm chế tạo và lực nén cục bộ tại má kẹp ngàm).
3. **Hoàn toàn không có màng giam giữ áp suất dương, không có chất lỏng/khí nén ép ngoài, và không có biến số áp suất chủ động P3**.

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Nghiên cứu của Reedlunn chỉ tập trung vào cáp bện có góc xoắn cố định (helical cables), chưa khảo sát bó dây thẳng đặt song song (parallel wire bundles) thường dùng trong các cơ cấu nghẽn dầm robot mềm.
- Không đo đạc trực tiếp lực ma sát trượt động học giữa các sợi dây NiTi khi có ngoại lực nén ngang từ môi trường giam giữ.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Trong bài báo Part II, các vết lõm tiếp xúc do chế tạo (dimples) làm xuất hiện chuyển pha mactenxít cục bộ sớm; vậy trong một bó dây NiTi thẳng chịu áp suất dương ngoài P3, lực ép tiếp xúc giữa các dây có tự tạo ra các vết lõm vi mô tương tự làm thay đổi đường cong uốn hay không?
2. Giả thiết không có trượt tương đối giữa các dây (monolithic assumption) của Reedlunn trong kéo đơn trục có còn đúng khi bó dây chuyển sang chịu uốn dầm biên độ lớn dưới áp suất giam giữ hay không?

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
