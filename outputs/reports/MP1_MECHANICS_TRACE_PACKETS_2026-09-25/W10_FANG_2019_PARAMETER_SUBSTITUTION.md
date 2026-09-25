# W10 — Thẩm tra Chuyên sâu Fang et al. 2019 và Đánh giá Rủi ro Thay thế Tham số

## 1. Mục tiêu (Mission)

Thẩm tra chuyên sâu toàn văn (deep full-text audit) công trình then chốt về mô hình hóa hiện tượng học cáp hợp kim nhớ hình:
> **Cheng Fang, Yue Zheng, Junbai Chen, Michael C.H. Yam, Wei Wang (2019)**  
> *Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application*  
> *Engineering Structures*, Vol. 183, pp. 580–599. DOI: `10.1016/j.engstruct.2019.01.049`.  
> paper_id: `2f7fcf2f8f`

Nhiệm vụ trọng tâm:
1. Trích xuất đầy đủ: cấu trúc cáp $7\times 7$, chế độ nhiệt luyện định hình (annealing / form-setting), trễ dạng cờ (flag-shaped hysteresis), mô-đun đàn hồi cáp, hiện tượng các sợi dây vào tải không đồng bộ (non-synchronous wire engagement), suy giảm chu kỳ (cyclic degradation).
2. Phân tích mô hình hiện tượng học nhiều lớp sợi đồng tâm (multi-layer concentric fiber model) trong OpenSees và các hệ số suy giảm độ cứng (stiffness-reduction factors).
3. Đánh giá khách quan: *Mô hình tái hiện được những gì, và bỏ qua/không giải quyết những cơ chế vật lý nào?*
4. Trả lời câu hỏi thẩm định sống còn: *Bài báo này có chứng minh rằng "việc thay thế tham số (parameter substitution) trong mô hình sợi dầm hiện có là đủ" hay không?*  
   Tuân thủ nghiêm ngặt trạng thái thẩm tra có thẩm quyền: `evidence_status = insufficient`.
5. Giải thích vì sao Fang et al. 2019 làm gia tăng rủi ro mô hình bậc rút gọn / thay thế tham số (*reduced-order / parameter-substitution risk*) đối với MP1 nhưng vẫn **hoàn toàn chưa giải quyết được bài toán uốn chịu áp suất giam giữ chủ động**.

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `docs/project/MP1-V002_CURRENT_HANDOFF.md`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.md`
- `data/evidence/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json`
- `papers/verification/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf`

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

Theo quy định tại Section E và `MP1-V002_CURRENT_HANDOFF.md`:
- `existing_elastic_fiber_model_appears_sufficient = false` [AUDIT VERDICT]
- `niti_requires_distinct_constitutive_contact_coupling = false` [AUDIT VERDICT]
- `evidence_status = insufficient` [AUDIT VERDICT]
- **Mức độ đe dọa:** `medium` [AUDIT VERDICT]

## 4. Bảng bằng chứng (Evidence table)

| Evidence ID | Chủ đề | Vị trí trang / Mục trong PDF | Bằng chứng thực nghiệm / Mô hình hóa | Ý nghĩa đối với MP1 |
|---|---|---|---|---|
| W10-E01 | Cấu trúc cáp $7\times 7$ & Nhiệt luyện định hình | pp. 2–4, 7–8; Sec. 2.1–2.2 | Cáp $7\times 7$ (49 sợi); ủ $350 - 450^\circ\text{C}$ trong $15\text{ phút}$ tôi nước đạt định hình hoàn hảo, chống bung khi cắt; ủ $\ge 500^\circ\text{C}$ làm hỏng siêu đàn hồi. | Quy trình chế tạo cáp NiTi thực tế đã được chuẩn hóa. |
| W10-E02 | Mô-đun đàn hồi & Vào tải không đồng bộ | pp. 1, 2, 7, 11; Sec. 3.2 | Mô-đun cáp ban đầu $30 - 45\text{ GPa}$ (thấp hơn sợi thẳng $\sim 60\text{ GPa}$); đường cong trễ trơn tru do trạng thái ứng suất đa trục và các sợi vào tải lệch pha. | Đáp ứng vĩ mô của cáp không đồng nhất với sợi đơn. |
| W10-E03 | Suy giảm chu kỳ & Huấn luyện cơ học | pp. 10, 16; Sec. 3.4 | Giới hạn chảy giảm $> 20\%$ sau 20 chu kỳ; huấn luyện cơ học 5 chu kỳ hấp thụ $> 80\%$ biến dạng dẻo tích lũy, ổn định trễ. | Đặc tính trễ phụ thuộc vào lịch sử tải chu kỳ. |
| W10-E04 | Mô hình sợi OpenSees bậc rút gọn | pp. 11–13; Sec. 4.1–4.2 | Mô hình phần tử dầm-cột dẻo phi tuyến nhiều lớp sợi đồng tâm, dùng các hệ số giảm độ cứng mô phỏng sợi vào tải lệch pha mà KHÔNG cần giải tiếp xúc 3D. | **Tăng rủi ro:** Phản biện có thể chất vấn sự cần thiết của mô hình tiếp xúc phức tạp. |
| W10-E05 | Giới hạn không giải quyết áp suất uốn | Toàn văn; Sec. 4.3 | Mô hình chỉ áp dụng cho kéo đơn trục dọc trục; hoàn toàn không có tiếp xúc ma sát ngang, không có uốn và không có biến số áp suất ngoài. | Không giết chết T2; trạng thái bằng chứng vẫn là `insufficient`. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W10-E01 — Kiến trúc cáp $7\times 7$ và Nhiệt luyện định hình (Form-setting)

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Trang kiểm chứng:** Trang 2, 3, 4, 7, 8, 16; Section 2 (Material and Specimen Preparation).

### Thiết lập cơ học & Luyện kim:
- Cáp siêu đàn hồi $7\times 7$ NiTi gồm 49 sợi (đường kính ngoài danh nghĩa $6.0\text{ mm}$ và $8.0\text{ mm}$, đường kính mỗi sợi $0.68\text{ mm}$ và $0.90\text{ mm}$).
- Xử lý nhiệt luyện định hình trong lò điện từ $350^\circ\text{C}$ đến $550^\circ\text{C}$ trong $15\text{ phút}$, sau đó tôi nước (pp. 3, 4).
- **Kết quả thực nghiệm:**
  - Nhiệt luyện ở nhiệt độ vừa phải ($350 - 450^\circ\text{C}$): Giữ nhiệt độ kết thúc pha austenite $A_f$ xấp xỉ nhiệt độ phòng, tạo khả năng phục hồi siêu đàn hồi $> 80 - 85\%$ (biến dạng dư $< 1.5\%$ sau biến dạng kéo $10\%$) (pp. 4, 10).
  - Nhiệt luyện ở $400^\circ\text{C}$ trở lên giúp cáp đạt trạng thái định hình hoàn chỉnh (full form-setting): Khi dùng kéo cắt ngang giữa nhịp cáp, các sợi dây không bị bung xòe (unravelling) (pp. 7, 8, 16).
  - Nhiệt luyện quá cao ($\ge 500^\circ\text{C}$): Gây quá già hóa (over-aging), nhiệt độ $A_f$ tụt xuống $-20^\circ\text{C}$, phá hủy khả năng tiêu tán năng lượng siêu đàn hồi (p. 4).

---

### EVIDENCE W10-E02 & W10-E03 — Hiện tượng vào tải không đồng bộ và Suy giảm chu kỳ

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Trang kiểm chứng:** Trang 1, 2, 7, 10, 11, 16; Section 3 (Experimental Results and Discussion).

### Hiện tượng cơ học bóc tách:
1. **Mô-đun đàn hồi cáp thấp hơn sợi đơn:** Mô-đun đàn hồi ban đầu của cáp $7\times 7$ chỉ đạt từ $30\text{ GPa}$ đến $45\text{ GPa}$, thấp hơn nhiều so với mô-đun đàn hồi của sợi NiTi đơn thẳng ($\sim 60\text{ GPa}$) (p. 10).
2. **Vào tải không đồng bộ (Non-synchronous wire engagement):** Do góc nghiêng đường xoắn ốc khác nhau giữa sợi lõi trung tâm và các sợi xoắn lớp ngoài, khi cáp bị kéo dãn, các sợi không đạt trạng thái chịu tải cùng lúc. Sợi lõi chịu ứng suất kéo cao hơn và chuyển pha trước, trong khi các sợi xoắn ngoài chịu trạng thái ứng suất phức hợp (kéo + uốn + xoắn) và vào tải muộn hơn. Hiện tượng này làm cho đường cong lực - biến dạng dạng cờ của cáp trở nên **trơn tru, mềm mại hơn, không có thềm ứng suất sắc nhọn như sợi đơn** (pp. 1, 2, 7, 11).
3. **Suy giảm chu kỳ (Cyclic degradation):** Dưới tải trọng chu kỳ 20 lần, giới hạn ứng suất chuyển pha giảm hơn $20\%$ (từ $> 500\text{ MPa}$ xuống dưới $400\text{ MPa}$). Tuy nhiên, hơn $80\%$ biến dạng dẻo tích lũy diễn ra ngay trong 5 chu kỳ đầu tiên, chứng minh rằng quy trình huấn luyện cơ học tiền trạm (mechanical pre-training 5 chu kỳ) có thể ổn định hóa hoàn toàn đường trễ của cáp (pp. 10, 16).

---

### EVIDENCE W10-E04 — Mô hình sợi OpenSees bậc rút gọn (Reduced-Order Fiber Model)

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Trang kiểm chứng:** Trang 11, 12, 13; Section 4 (Numerical Modelling of NiTi SMA Cables).

### Cấu trúc mô hình hiện tượng học:
- Tác giả không mô hình hóa tiếp xúc 3D chi tiết giữa 49 sợi dây (như Vahidi et al. 2021) vì chi phí tính toán quá lớn.
- Thay vào đó, tác giả sử dụng phần tử dầm-cột dẻo phi tuyến dựa trên chuyển vị (displacement-based nonlinear fiber beam-column elements) trong phần mềm mã nguồn mở OpenSees (p. 11).
- Tiết diện cáp được chia thành các lớp sợi đồng tâm (concentric fiber layers):
  - Lõi trung tâm: Gồm vật liệu thép tăng cứng đẳng hướng Steel02.
  - Các lớp bao quanh: Sử dụng mô hình vật liệu tự định tâm Self-centering SMA material.
- **Hệ số suy giảm độ cứng (Stiffness-reduction factors):** Để mô phỏng hiện tượng các sợi vào tải không đồng bộ, tác giả áp dụng các hệ số chiết giảm độ cứng tăng dần từ lõi trong ra lớp ngoài cho các lớp sợi SMA (pp. 11, 12).
- **Kết quả:** Mô hình bậc rút gọn này tái hiện xuất sắc đường cong trễ dạng cờ, sự trơn nhẵn của thềm chuyển pha, và suy giảm chu kỳ của cáp $7\times 7$ trong kéo đơn trục với thời gian tính toán chỉ trong vài giây (pp. 12, 13).

---

### EVIDENCE W10-E05 — Những gì mô hình Fang et al. KHÔNG giải quyết

**Phân loại (Classification):** [VERIFIED PAPER FACT] kết hợp [INFERENCE]

**Trang kiểm chứng:** Trang 11, 12, 13, 14, 18, 19.

### Giới hạn cơ học cốt lõi:
1. **Không giải quyết tiếp xúc và ma sát 3D:** Mô hình hiện tượng học OpenSees là mô hình 1D quy ước dọc trục; nó không giải phương trình ma sát Coulomb hay phản lực pháp tuyến giữa các sợi dây.
2. **Không mô hình hóa uốn dầm và trượt ngang:** Nghiên cứu chỉ áp dụng cho cáp kéo dọc trục dùng làm dây giằng động đất (seismic restrainers). Mô hình hoàn toàn không có khả năng dự báo sự trượt tương đối giữa các lớp sợi khi dầm bị uốn cong (bending slip / stick-slip transitions).
3. **Hoàn toàn không có áp suất giam giữ ngoài:** Không có biến số áp suất thủy tĩnh hoặc áp suất ngang nào xuất hiện trong mô hình của Fang et al.

## 6. Kết luận về claim/target (Claim/target conclusion)

### Phân tích trọng tâm: Bài báo này có chứng minh việc thay thế tham số là đủ hay không?
- **Câu trả lời khoa học chính xác:** **KHÔNG THỂ KHẲNG ĐỊNH.**  
  [AUDIT VERDICT] Trạng thái thẩm tra bắt buộc phải duy trì:
  ```text
  existing_elastic_fiber_model_appears_sufficient = false
  niti_requires_distinct_constitutive_contact_coupling = false
  evidence_status = insufficient
  ```
- **Ý nghĩa đúng đắn của trạng thái `insufficient`:**
  1. Mô hình của Fang et al. 2019 chứng minh rằng: Đối với **kéo dọc trục đơn thuần**, một mô hình hiện tượng học bậc rút gọn kết hợp các hệ số chiết giảm độ cứng là đủ để khớp dữ liệu thực nghiệm mà không cần giải bài toán ma sát tiếp xúc vi mô chi tiết.
  2. Tuy nhiên, bài báo **chưa bao giờ kiểm tra cơ chế uốn dầm dưới áp suất giam giữ chủ động P3**.
  3. Do đó, tài liệu hiện có chưa đủ bằng chứng (*insufficient evidence*) để khẳng định mô hình dầm sợi thông thường có thể áp dụng cho uốn có áp suất; đồng thời cũng chưa đủ bằng chứng để chứng minh rằng bắt buộc phải có một mô hình tiếp xúc ghép cặp NiTi hoàn toàn mới. Cần phải có thí nghiệm đối đầu trực tiếp (direct baseline comparison).

### Tại sao Fang et al. 2019 làm gia tăng rủi ro cho MP1?
[INFERENCE]  
Fang et al. 2019 là một lời cảnh báo nghiêm khắc đối với nghiên cứu sinh:
- Các chuyên gia bình duyệt (peer reviewers) sẽ đặt câu hỏi: *"Tại sao anh/chị phải phát triển một mô hình cơ học tiếp xúc ma sát vi mô phức tạp cho bó dây NiTi, trong khi một mô hình sợi OpenSees đơn giản với các hệ số chiết giảm độ cứng (như Fang 2019) đã có thể dự báo được phản lực vĩ mô?"*
- Nếu MP1 không chứng minh được rằng **dưới áp suất giam giữ chủ động P3, sự chuyển pha mactenxít làm thay đổi căn bản quy luật dính–trượt (stick-slip) và độ cứng uốn theo cách mà mô hình bậc rút gọn không thể nắm bắt được**, thì đóng góp của MP1 sẽ bị quy giảm về bài toán thừa thãi (over-engineering a solved macro-response).

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Fang et al. chỉ thử nghiệm kéo cáp ở trạng thái khô và nhiệt độ phòng, chưa khảo sát ứng xử cơ học khi cáp đặt trong môi trường chất lỏng nén hoặc màng khí nén.
- Chưa có dữ liệu về độ cứng kháng uốn thực tế của cáp $7\times 7$ khi chịu tải trọng ngang vuông góc với trục cáp.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Mô hình sợi đa lớp của Fang et al. 2019 có thể mở rộng để mô phỏng uốn dầm hay không, và nếu thêm lực nén ngang thì phần tử sợi của OpenSees có cơ chế nào để truyền tải lực ép tiếp xúc giữa các sợi hay không?
2. Trong các công trình trích dẫn tiếp theo của nhóm tác giả Fang (như Liang et al. 2020 về gối trượt cáp SMA), họ có sử dụng mô hình tiếp xúc vi mô nào để bổ cứu cho mô hình hiện tượng học năm 2019 hay không?

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
