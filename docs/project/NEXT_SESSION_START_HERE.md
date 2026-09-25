# NEXT SESSION — START HERE

> **Mục đích:** Điểm khởi đầu chính thức, súc tích và có thẩm quyền cao nhất để phiên làm việc tiếp theo bắt đầu ngay công việc khoa học mà không cần suy đoán trạng thái dự án.  
> **Quy tắc cốt lõi:** `DO NOT DEFEND A DIRECTION BY DEFAULT. TEST THE CURRENT FEASIBILITY GATE AND PIVOT IF THE EVIDENCE FAILS.`  
> **Thời điểm cập nhật:** 2026-09-25 (sau final cross-direction adjudication D1/M1 vs MP1).

---

## 1. Canonical State at HEAD

Trạng thái chuẩn hóa hiện tại tại commit HEAD được định hình bởi các quyết định kiểm định canonical (`outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json` và `docs/project/research_state.json`):

- **Hướng nghiên cứu được chọn (Selected Direction):** `D1_M1`
- **Quyết định đề tài (Decision):** `LOCK_WITH_FEASIBILITY_GATE`
- **Độ tin cậy (Confidence):** `medium`
- **Thang leo thang Astra (Astra Escalation):** `false` (không cần thiết vì các hướng đã rõ ràng về mặt rủi ro thực thi)
- **Vòng kiểm chứng MP1-V002:** `CLOSED`
  - `protocol_outcome`: `SURVIVES_TARGETED_CITATION_CHASE`
  - `confidence`: `high`
  - `direct_kill_found`: `false`
  - `citation_coverage`: `15/15 required directions screened` (`backward = 9/9`, `forward = 6/6`), `stop_condition.satisfied = true`, `search_cutoff_date = 2026-09-25`.
- **Định vị của MP1:** Được lưu trữ chính thức như một phương án thay thế có giá trị khoa học (`closed_archived_viable_alternative`), **không bị bác bỏ hoàn toàn**, nhưng **không được chọn** làm hướng luận văn hiện tại.
- **Tình trạng tìm kiếm văn hiến:** Dừng toàn bộ tìm kiếm diện rộng (broad search stopped).

---

## 2. What Has Been Completed

Dự án đã trải qua chuỗi kiểm định khoa học đối kháng toàn diện:

1. **Chuỗi kiểm định D1 (D1-V001 đến D1-V009):**
   - Loại bỏ tính mới ở cấp độ nguyên lý kẹt lớp (layer jamming), môi trường liên tục tổng quát (generalized/Cosserat continua), trượt ma sát giữa các lớp và mô phỏng tiếp xúc phần tử hữu hạn (FE contact).
   - Bảo toàn tính mới hẹp có điều kiện: Xây dựng bản đồ hiệu lực/mất hiệu lực (validity/breakdown map) có kiểm chứng thực nghiệm cho một mô hình liên tục cụ thể $M_1$.
2. **Quy trình kiểm chứng độc lập MP1 (Ý tưởng Mentor):**
   - **MP1-V001:** Bác bỏ tính mới cấp kiến trúc hệ thống (C1: kẹt dây, C2: áp suất dương, C3: kết hợp SMA+jamming, C4: nguồn áp suất mini, C8: piston jamming đều đã có tiền nhiệm trực tiếp); rút về cơ học tiếp xúc lõi (mechanics core).
   - **MP1-V002 (16 bài báo toàn văn):**
     - *Stage 1:* Gemini Flash trích xuất 11 evidence packets (`outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/`).
     - *Stage 2:* GPT-5.6 Astra thực hiện phản biện khoa học đối kháng 12 lỗ hổng G01–G12 (`docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md`).
     - *Stage 3:* Khắc phục toàn bộ 12 lỗ hổng, phân rã $H_0$ thành $H_{0a}$ (bác bỏ), $H_{0b}$ (chưa bị bác bỏ) và $H_1$ (chưa có bằng chứng), đính chính dữ liệu lịch sử Carboni 2015, ban hành báo cáo tổng hợp 24 chương (`docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md`).
     - *Stage 4:* Đóng phủ sóng trích dẫn (15/15 nhánh, bao gồm B11 Kang 2020 và B12 Barsi 2025).
     - *Stage 5:* Final adjudication xác nhận MP1 sống sót trong phạm vi giao thức (`outputs/verification/MP1-V002/FINAL_ADJUDICATION.json`).
3. **Phán quyết So sánh Liên hướng (Cross-Direction Adjudication):**
   - Đưa D1/M1 và MP1 vào so sánh trực tiếp trên 18 tiêu chí độc lập (`outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json`).
   - Kết quả: Chọn D1/M1 với điều kiện vượt qua cổng khả thi (feasibility gate).

---

## 3. Why MP1 Was Not Selected

MP1 **không bị loại bỏ vì thiếu tính khoa học**; nó sống sót qua quy trình tra cứu trích dẫn và là một đề tài hợp lệ. Tuy nhiên, khi đặt lên bàn cân thực hiện luận văn Thạc sĩ (MSc thesis), D1/M1 vượt trội hơn MP1 dựa trên các lý do cốt lõi:

1. **Đối tượng mô hình hóa cụ thể (Concrete Baseline Model):** D1/M1 có một mô hình xác định tường minh ($M_1$ — Zhang et al. 2025); trong khi MP1 chưa khóa được cặp mô hình baseline và higher-fidelity cho cấu hình mẫu cụ thể.
2. **Câu hỏi khoa học ít phụ thuộc giả định chưa kiểm chứng:** Câu hỏi của D1/M1 là xác định giới hạn hiệu lực của một mô hình đã biết. MP1 phụ thuộc vào một giả định chưa được chứng minh: *Liệu trong miền vận hành thực nghiệm an toàn, hiện tượng trượt giữa các dây và chuyển pha siêu đàn hồi có cùng xảy ra đồng thời hay không (coexistence domain)?*
3. **Khả năng nhận diện tham số (Parameter Identifiability):** Ở MP1, sự thay đổi độ cứng uốn có thể bị bù trừ bởi ma sát, chuyển pha, lực nén vòm tiếp xúc, nhiệt độ tự gia nhiệt ma sát và biến dạng ban đầu. D1/M1 có ít tầng ghép cặp gây nhiễu hơn.
4. **Gánh nặng thiết bị và đo đạc (Experimental & Instrumentation Burden):** D1/M1 sử dụng dàn uốn dầm chân không đo chuyển vị/lực vĩ mô trực tiếp. MP1 đòi hỏi buồng áp suất chủ động, kiểm soát trạng thái nhiệt/pha của NiTi và bắt buộc phải có cảm biến vi mô (DIC, FBG, ảnh nhiệt hồng ngoại) để phân biệt cơ chế với mô hình $H_{0b}$.
5. **Giá trị của kết quả phủ định (Value of a Null Result):** Nếu thí nghiệm chỉ ra dầm layer-jamming không bị mất hiệu lực sớm, D1/M1 vẫn đóng góp một miền hiệu lực rộng có giới hạn bất định; nếu MP1 được giải thích hoàn toàn bởi mô hình $H_{0b}$ hiện hữu, khẳng định cơ học mới của MP1 bị triệt tiêu hoàn toàn.

---

## 4. Current Selected Direction D1/M1

### Tên Đề tài Chính thức (Official Working Title)
- **Tiếng Anh:** *Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams*
- **Tiếng Việt:** *Đánh giá thực nghiệm giới hạn hiệu lực và sự mất hiệu lực của mô hình liên tục cho dầm kẹt lớp chân không*

### Mô hình Rút gọn Được Đánh giá ($M_1$)
- **Bài báo gốc:** Zhang et al., *A continuum-based model for a layer jamming beam*, *Mechanisms and Machine Science*, 2025.
- **DOI:** `10.5194/ms-16-821-2025` | **paper_id:** `95646b2cfc`
- **Trạng thái:** `[VERIFIED FULL TEXT]` (Tệp PDF tại `data/papers/verification/D1-V002/2025-A continuum-based model for a layer jamming beam.pdf` và paper card tại `docs/literature/paper_cards/zhang_2025_continuum_beam/paper-card.md`).

### Kiến trúc Nghiên cứu Cốt lõi: M → R → E
- **M (Mô hình Rút gọn / Continuum Model):** Mô hình liên tục của Zhang et al. (2025) cho dầm layer jamming.
- **R (Mô hình Tham chiếu Độ chính xác Cao hơn / Numerical Reference):** Mô hình phần tử hữu hạn phân giải từng lớp riêng lẻ có tiếp xúc ma sát Coulomb tường minh (full-layer explicit frictional-contact FE model). *Lưu ý: R là chuẩn đối chứng số học đã được kiểm chứng hội tụ, không phải chân lý tuyệt đối.*
- **E (Thực nghiệm Độc lập / Physical Experiment):** Thử nghiệm uốn dầm kẹt lớp chân không thực tế trên các điều kiện dự đoán hợp lệ và mất hiệu lực.

### Câu hỏi Nghiên cứu (Research Question)
> Trong miền số lớp ($N$), áp suất chân không ($p_{\text{vac}}$) và mức độ uốn quasi-static ($\kappa$) được khai báo trước, mô hình liên tục Zhang et al. ($M_1$) đạt độ chính xác trong ngưỡng sai số biện minh trước đối với những đại lượng đo và điều kiện vận hành nào khi so với mô hình tham chiếu full-layer ($R$) và thực nghiệm ($E$), và cơ chế tiếp xúc/trượt nào giải thích sự mất hiệu lực khi mô hình thất bại?

### Giả thuyết Khoa học (Scientific Hypothesis)
> Sai số theo từng đại lượng đo của $M_1$ sẽ tăng lên có quy luật khi tính chất rời rạc của các lớp hữu hạn, sự trượt giữa các lớp và sự phân bố lại áp suất tiếp xúc trở nên áp đảo, tạo ra các vùng hiệu lực (validity) và mất hiệu lực (breakdown) có thể phân biệt được bằng thực nghiệm.

---

## 5. What Is Locked

Những nội dung sau đây đã được chốt và **không thay đổi** trong các phiên tới:
1. **Lĩnh vực nghiên cứu:** Đánh giá giới hạn hiệu lực của mô hình cơ học dầm kẹt lớp chân không (vacuum layer-jamming beam model validity/breakdown).
2. **Hướng đề tài được chọn:** `D1_M1`.
3. **Mô hình rút gọn đối tượng:** $M_1$ — Zhang et al. (2025), DOI: `10.5194/ms-16-821-2025`.
4. **Kiến trúc phương pháp luận:** $M \to R \to E$.
5. **Trạng thái quyết định:** `LOCK_WITH_FEASIBILITY_GATE`.
6. **Tìm kiếm văn hiến diện rộng:** Đóng hoàn toàn (broad search stopped).

---

## 6. What Is NOT Locked

Những nội dung sau **chưa được khóa** và là trọng tâm kỹ thuật cần giải quyết trong các phiên tới:
- Công thức toán học và triển khai cụ thể của mô hình tham chiếu $R$ (phần tử 2D hay 3D, thuật toán tiếp xúc penalty hay Lagrange multipliers).
- Định luật ma sát cụ thể và giao thức đo/hiệu chuẩn hệ số ma sát $\mu$ độc lập.
- Phương pháp biểu diễn áp suất chân không (tải trọng mặt ngoài đồng nhất vs mô hình buồng kín vs màng co).
- Lựa chọn đại lượng đo sơ cấp (primary output: độ võng đầu dầm, mô-men kháng uốn, độ cứng uốn tiếp tuyến, hay thời điểm bắt đầu trượt).
- Định nghĩa hàm sai số (error metric) và ngưỡng sai số chấp nhận được ($\varepsilon_{\text{tol}}$) có cơ sở toán học/vật lý.
- Bảng ngân sách bất định hoàn chỉnh (uncertainty budget: sai số số học $u_{\text{num}}$, sai số đo thực nghiệm $u_{\text{exp}}$).
- Các điều kiện tải dự kiến cho mẫu thử nghiệm accepted và rejected.
- Kích thước dầm, vật liệu các lớp (Mylar, thép, nhôm, giấy nhám) và cơ cấu gá đặt thực nghiệm.

---

## 7. Immediate Scientific Gate

### Tên Cổng: `D1/M1 boundary-resolvability pilot`
- **Mục tiêu:** Xác định xem phép so sánh giữa mô hình $M_1$ và mô hình tham chiếu $R$ (đã được kiểm chứng hội tụ) có tạo ra đồng thời ít nhất một điều kiện chấp nhận được (accepted condition) và một điều kiện bị bác bỏ (rejected condition) trong miền thực nghiệm khả thi, với độ không đảm bảo đo đủ nhỏ để phân loại có ý nghĩa hay không.
- **Tiêu chí ĐẠT (Pass Condition):** Sử dụng các tham số hiệu chuẩn độc lập và ngưỡng sai số đã cố định trước; chỉ ra ít nhất một trạng thái hợp lệ và một trạng thái mất hiệu lực có khoảng cách sai số lớn hơn độ không đảm bảo đo; thực hiện được phép đo thực nghiệm phân biệt được hai trạng thái đó.
- **Tiêu chí KHÔNG ĐẠT (Fail Condition):** Không tìm thấy sự tương phản accepted/rejected trong miền vận hành khả thi của thiết bị, hoặc mô hình tham chiếu $R$ không thể hội tụ/kiểm chứng được. Khi đó đề tài bắt buộc phải thu hẹp (narrow) hoặc chuyển hướng (pivot).

---

## 8. First Task: Reconstruct M1

> [!IMPORTANT]
> **NHIỆM VỤ ĐẦU TIÊN BẮT BUỘC TRONG PHIÊN TIẾP THEO:**  
> **Tái cấu trúc hoàn chỉnh mô hình $M_1$ (Reconstruct M1 Completely) từ bài báo gốc của Zhang et al. (2025) trước khi đóng băng mô hình tham chiếu $R$.**

Trình tự khoa học bắt buộc:
```text
Tái cấu trúc phương trình M1
→ Hiểu rõ các giả thiết và chuỗi biến đổi
→ Kiểm tra việc tái tạo lại (reproduce) trường hợp mẫu trong bài báo Zhang et al.
→ Xác định rõ các cơ chế mất hiệu lực tiềm năng
→ SAU ĐÓ MỚI khóa công thức mô hình tham chiếu R
```

Nội dung cụ thể cần thực hiện đối với $M_1$:
1. Xác định rõ hệ vật lý và các giả thiết cơ học (Euler-Bernoulli vs Timoshenko, chiều dày hữu hạn, giả thiết trượt Coulomb).
2. Lập từ điển ký hiệu, biến số và thứ nguyên toán học.
3. Lần theo chuỗi phương trình cân bằng vi phân, phân bố ứng suất tiếp tuyến $\tau(x, z)$ và ứng suất pháp $\sigma(z)$.
4. Phân tích 3 trạng thái cơ học: Kẹt hoàn toàn (fully jammed / stick) $\to$ Trượt một phần (partial slip) $\to$ Trượt hoàn toàn (full slip).
5. Lần theo phương trình đường ranh giới vùng trượt (slip-zone boundary) và nghiệm giải tích quan hệ mô-men – độ cong – độ võng.
6. Ghi nhận các điểm mập mờ toán học (mathematical gaps) và các trường hợp mẫu (published benchmark cases) để chuẩn bị chạy kiểm tra tái lập (reproduction check).

---

## 9. Files to Read Before Working

Trước khi bắt tay vào công việc khoa học trong phiên tới, đọc theo thứ tự ưu tiên:

1. [`docs/project/NEXT_SESSION_START_HERE.md`](file:///home/khanh/projects/mechanical-research-agents/docs/project/NEXT_SESSION_START_HERE.md) *(Tài liệu này)*
2. [`outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json`](file:///home/khanh/projects/mechanical-research-agents/outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json) *(Quyết định khóa đề tài chính thức)*
3. [`docs/project/PROJECT_HANDOFF_CURRENT.md`](file:///home/khanh/projects/mechanical-research-agents/docs/project/PROJECT_HANDOFF_CURRENT.md) *(Bản handoff tổng thể)*
4. [`docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md`](file:///home/khanh/projects/mechanical-research-agents/docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md) *(Kiến trúc chi tiết của M1)*
5. [`docs/literature/paper_cards/zhang_2025_continuum_beam/paper-card.md`](file:///home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/paper-card.md) *(Hồ sơ trích xuất chuyên sâu về bài báo Zhang et al. 2025)*
6. Bài báo toàn văn gốc: `data/papers/verification/D1-V002/2025-A continuum-based model for a layer jamming beam.pdf`

---

## 10. Explicit DO NOT List

Tuyệt đối tuân thủ các điều cấm sau:
- **KHÔNG** tìm kiếm thêm tài liệu diện rộng (no broad literature search).
- **KHÔNG** mở lại quy trình kiểm chứng MP1-V003 hoặc mở lại các nhánh trích dẫn B11/B12 đã đóng.
- **KHÔNG** tuyên bố MP1 bị "bác bỏ hoàn toàn" hay "không có giá trị" (MP1 là viable alternative đã được đóng và lưu trữ).
- **KHÔNG** vội vàng đóng băng mô hình tham chiếu $R$ trước khi hoàn thành việc tái cấu trúc và hiểu sâu sắc mô hình $M_1$.
- **KHÔNG** tuyên bố tính mới ở việc phát minh mô hình continuum hay cơ học kẹt dầm (đây là prior art).
- **KHÔNG** gọi mô hình tham chiếu $R$ là "chân lý" (ground truth); $R$ chỉ là đối chứng số học độ chính xác cao hơn.
- **KHÔNG** sử dụng mô hình Astra khi không có mâu thuẫn khoa học nghiêm trọng chưa thể hòa giải.
- **KHÔNG** sửa đổi các tệp báo cáo lịch sử hay tệp canonical JSON cũ.

---

## 11. Definition of Done for the Next Session

Phiên tiếp theo được coi là **HOÀN THÀNH (`DONE`)** khi và chỉ khi:
1. **Hệ vật lý và giả thiết của $M_1$ được tài liệu hóa đầy đủ:** Nêu rõ các điều kiện biên, cách mô hình hóa màng bọc chân không, và các giả thiết rút gọn động học.
2. **Từ điển biến số và ký hiệu hoàn tất:** Toàn bộ các đại lượng toán học trong bài báo Zhang et al. (2025) được định nghĩa rõ ràng kèm đơn vị đo SI.
3. **Chuỗi dẫn xuất phương trình được truy vết rành mạch:** Tường minh hóa các bước thiết lập phương trình cân bằng, điều kiện trượt Coulomb vi mô, sự hình thành và lan truyền của vùng trượt, và công thức tính mô-men uốn / độ võng dầm.
4. **Cơ học dính – trượt của $M_1$ được phân tích thấu đáo:** Làm rõ cách mô hình chuyển tiếp từ trạng thái dính hoàn toàn, qua trượt từng phần, đến trượt hoàn toàn.
5. **Trường hợp mẫu đối chứng (Published Benchmark Case) được xác lập:** Xác định cụ thể các thông số đầu vào (hình học dầm, áp suất chân không, hệ số ma sát, mô-đun đàn hồi) và các đường cong chuẩn trong bài báo Zhang et al. để chuẩn bị cho bước chạy tái lập (reproduction check).
6. **Ghi nhận các điểm còn mập mờ:** Lập danh mục các bước nhảy công thức, giả thiết ngầm, hoặc các giới hạn vật lý có thể dẫn đến sự mất hiệu lực của $M_1$.
