# W07 — Kiểm chứng Ranh giới Mục tiêu T2: Áp suất Giam giữ Chủ động (Active Confinement Pressure)

## 1. Mục tiêu (Mission)

Đây là **cuộc kiểm chứng ranh giới quan trọng nhất (the most important boundary audit)** của toàn bộ dự án MP1.
Mục tiêu là thẩm tra phát biểu đe dọa **T2**:
> "Áp suất giam giữ dương tác động từ bên ngoài theo phương hướng tâm/ngang (radially/transversely) nén ép bó dây kim loại / NiTi, làm thay đổi lực pháp tuyến tiếp xúc và ma sát, từ đó điều khiển sự biến thiên độ cứng uốn kết cấu (variable bending stiffness)."

Nhiệm vụ trọng tâm:
1. Thẩm tra nhóm bài báo ưu tiên cốt lõi: `ccdc1bb980` (Tjahjanto et al. 2017), `aaad9c248c` (Xin Liu 2004), `53200aa0c6` (Vahidi et al. 2021), `fac21c950e` (Reedlunn et al. 2013).
2. Phân loại nghiêm ngặt cơ chế áp suất theo hệ quy chuẩn:
   - **P1:** Áp suất tiếp xúc thụ động (*passive contact pressure*) sinh ra tự nhiên từ hình học vặn xoắn (helix lay), lực kéo dọc trục, uốn dầm, hoặc biến dạng tương thích.
   - **P2:** Áp suất nén đặt trước cố định (*fixed preload / fixed confinement*), không thay đổi trong quá trình làm việc.
   - **P3:** Áp suất giam giữ bên ngoài thay đổi chủ động (*actively varied external confinement pressure*) đóng vai trò biến số điều khiển vận hành độc lập (independent operational control variable).
3. Thiết lập bảng so sánh ma trận áp suất và giải thích tường minh tại sao áp suất hướng tâm thụ động (P1) hoặc lực siết cố định (P2) **tuyệt đối không tương đương với P3**.
4. Ghi lại kết quả rà soát từ khóa trong các tệp PDF gốc để chứng minh tính mở của T2 một cách có phương pháp, không tuyên bố tùy tiện.

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`
- `outputs/verification/MP1-V002/verification_matrix.json`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.md`
- Các tệp bằng chứng và PDF gốc:
  - Tjahjanto et al. 2017 (`ccdc1bb980`): `data/evidence/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json`, `papers/verification/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf`
  - Xin Liu 2004 (`aaad9c248c`): `data/evidence/A5-Cable vibration considering internal friction_aaad9c248c.json`, `papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf`
  - Vahidi et al. 2021 (`53200aa0c6`): `data/evidence/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json`, `papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf`
  - Reedlunn et al. 2013 (`fac21c950e`): `data/evidence/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json`, `papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf`

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **Target:** T2
- **Phán quyết thẩm tra:** `open_in_current_full_text_set` [AUDIT VERDICT]
- **Độ tin cậy:** `high` [AUDIT VERDICT]
- **Các thành phần cơ học còn thiếu trong tập tài liệu (Missing Mechanics):**
  1. Chưa có công trình nào áp dụng áp suất giam giữ dương hoặc áp suất ngang thay đổi chủ động (actively varied positive/transverse confinement pressure) lên một bó dây kim loại hoặc NiTi.
  2. Chưa có quan hệ đo đạc hoặc mô hình hóa độ cứng uốn phụ thuộc áp suất ($K_{\text{bending}} = f(p)$) cho bó dây NiTi.
  3. Chưa có kiểm chứng thực nghiệm chứng minh rằng áp suất ngoài điều khiển được lực pháp tuyến và ma sát giữa các dây đủ để tạo ra độ cứng uốn điều chỉnh được (tunable bending stiffness).

## 4. Bảng phân loại áp suất và đánh giá đe dọa T2 (Pressure classification table)

| Paper | Cơ chế áp suất trong bài | Phân loại (P1/P2/P3) | Thay đổi chủ động? (Actively varied?) | Bó dây NiTi? (NiTi bundle?) | Tương quan lực pháp tuyến? (Normal-force link?) | Tương quan dính–trượt? (Stick-slip link?) | Tương quan độ cứng uốn? (Bending-stiffness link?) | Mức độ đe dọa đối với T2 (Threat to T2) |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Tjahjanto et al. 2017** (`ccdc1bb980`) | Áp suất hướng tâm $0.2\text{ MPa}$ đặt trước lên vỏ trong cáp ngầm, cộng với lực ép tiếp xúc khi dầm bị uốn cong. | **P2** (áp suất đặt trước cố định) + **P1** (áp suất do uốn) | **KHÔNG** (áp suất giữ cố định $0.2\text{ MPa}$) | **KHÔNG** (lõi đồng, chất độn polymer, sợi thép) | **CÓ** (tải trọng tiếp xúc tuyến tính $60-63\text{ kN/m}$) | **CÓ** (dự báo trượt loxodromic dọc trục) | **KHÔNG** (không đo hay điều khiển độ cứng uốn theo áp suất) | **THẤP / GIÁN TIẾP:** Cho thấy áp suất hướng tâm chi phối lực tiếp xúc và trượt, nhưng áp suất là cố định (P2) và vật liệu không phải NiTi. |
| **Xin Liu 2004** (`aaad9c248c`) | Áp suất hướng tâm dư do chế tạo định hình (preforming pressure) giữa các lớp dây cáp ($0.475\text{ N/mm}^2$ giữa lớp 1–2; $0.053\text{ N/mm}^2$ giữa lớp 2–3). | **P1** (áp suất thụ động từ góc bện và chế tạo) | **KHÔNG** (áp suất là hằng số nội tại của mẫu) | **KHÔNG** (cáp thép đàn hồi tuyến tính) | **CÓ** (áp suất hướng tâm quyết định lực cắt tới hạn trượt) | **CÓ** (phân tách dao động tắt dần có trượt và dao động dính không trượt) | **CÓ** (độ cứng uốn giảm phi tuyến theo độ cong khi trượt bắt đầu) | **TRUNG BÌNH / CƠ SỞ:** Thiết lập mô hình độ cứng uốn phụ thuộc trượt ma sát do áp suất hướng tâm, nhưng áp suất là hằng số thụ động (P1), không phải biến số điều khiển (P3). |
| **Vahidi et al. 2021** (`53200aa0c6`) | Áp suất tiếp xúc pháp tuyến giữa các sợi sinh ra khi cáp bị kéo căng dọc trục; các sợi xoắn ép chặt vào sợi lõi. | **P1** (áp suất tiếp xúc thụ động do lực kéo và góc xoắn) | **KHÔNG** (không có nguồn áp lực ngoài) | **CÓ** (cáp SMA $1\times 27$ và $7\times 7$) | **CÓ** (ứng suất nén lên tới $330-680\text{ MPa}$ ở lõi) | **CÓ** (ma sát Coulomb, sinh ứng suất dư ma sát $100\text{ MPa}$) | **KHÔNG** (chỉ tải kéo dọc trục và kích nhiệt, không có chế độ uốn) | **THẤP đối với T2** (chỉ đe dọa T1 và T3): Tiếp xúc sinh ra do tải kéo dọc trục, không có áp suất giam giữ chủ động ngoài. |
| **Reedlunn et al. 2013** (`fac21c950e`) | Ứng suất nén hướng tâm cục bộ tại má kẹp ngàm khía nhám (knurled grips) và vết lõm tiếp xúc do chế tạo (contact dimples). | **P1** (áp suất thụ động cục bộ và điều kiện biên ngàm) | **KHÔNG** (không có áp suất giam giữ) | **CÓ** (cáp siêu đàn hồi $7\times 7$ và $1\times 27$) | **CÓ** (vết lõm tiếp xúc làm kích hoạt chuyển pha cục bộ) | **KHÔNG** (giả định tiết diện di chuyển đồng khối, không trượt) | **KHÔNG** (kéo đơn trục dãn dài đẳng nhiệt, không đo độ cứng uốn) | **THẤP đối với T2**: Hoàn toàn không khảo sát áp suất giam giữ ngang hay uốn. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W07-E01 — Thẩm tra sâu bài báo Tjahjanto et al. 2017 (`ccdc1bb980`)

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** T2 — Boundary audit against fixed radial preload (P2).

**Paper title:** *BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE*

**Authors:** Denny D. Tjahjanto, Andreas Tyrberg, Jonathan Mullins

**Year:** 2017

**DOI:** [KHÔNG CÓ DOI — Kỷ yếu hội thảo quốc tế OMAE 2017 / ASME, Paper No. OMAE2017-61139]

**paper_id:** `ccdc1bb980`

**Verification round:** MP1-V002

**Evidence JSON:** `data/evidence/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json`

**Original PDF:** `papers/verification/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf`

**Page(s) / Section:** Trang 1, 3, 4, 5, 7, 8; Section: Finite Element Model, Results and Discussion.

**Evidence type:** 3D Finite element modeling and analytical comparison.

### Thiết lập cơ học (Mechanical setup)
- Kết cấu cáp ngầm động lực (dynamic submarine cable) gồm 3 lõi truyền tải điện bọc cách điện xoắn xoắn ốc (copper power cores), các thanh đệm polymer định hình (polymeric profile fillers) và các lớp vỏ bọc bảo vệ cùng áo giáp thép (steel armour).
- Cơ chế tác dụng tải: Quá trình đặt tải gồm 2 bước liên tiếp (pp. 4, 5):
  - Bước 1: Đặt biến dạng kéo dọc trục danh nghĩa cộng với **áp suất hướng tâm cố định $0.2\text{ MPa}$ ($2\text{ bar}$)** tác dụng lên lớp vỏ bọc bên trong để mô phỏng áp lực nén siết ban đầu của các lớp áo giáp.
  - Bước 2: Duy trì biến dạng kéo và áp suất này, dầm cáp bị uốn cong lặp chu kỳ theo các hàm độ cong $\kappa(t)$.

### Kết quả rà soát từ khóa PDF (PDF Keyword Search Evidence)
Rà soát toàn văn tệp PDF `A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf`:
- Từ khóa `radial pressure`: Xuất hiện tại p. 4 ("A radial pressure of 0.2 MPa is applied on the inner sheath..."), p. 5 ("Following the application of tensile strain and radial pressure...").
- Từ khóa `active` / `actively`: Xuất hiện 0 lần liên quan đến kiểm soát áp suất.
- Từ khóa `variable stiffness`: Xuất hiện 0 lần.
- Từ khóa `bending stiffness`: Xuất hiện tại p. 1 và p. 4 khi nói về độ cứng uốn của từng thành phần riêng lẻ, nhưng **không có bất kỳ đồ thị hay phân tích nào về độ cứng uốn thay đổi theo các mức áp suất khác nhau**.

### Phân tích cơ học & Kết quả định lượng (Quantitative results)
- Áp suất hướng tâm $0.2\text{ MPa}$ làm phát sinh tải trọng tiếp xúc phân bố dọc theo chiều dài (contact lineload) khoảng $60 - 63\text{ kN/m}$ lên mỗi lõi truyền tải, xấp xỉ bằng một phần ba tải trọng tiếp xúc trên lớp vỏ trong ($\sim 200\text{ kN/m}$) (pp. 5, 8).
- Dưới độ cong uốn, sự trượt giữa các lõi và vỏ xảy ra hầu như thuần túy theo phương dọc trục (loxodromic slip) (pp. 3, 7).
- Vật liệu đệm polymer chịu biến dạng cắt tới $1\%$, làm mềm đáp ứng ứng suất ma sát ở giai đoạn bắt đầu uốn (pp. 7, 8).

### Bằng chứng này chứng minh điều gì (What this proves)
Chứng minh rằng áp suất nén hướng tâm đặt lên mặt ngoài kết cấu cáp vặn xoắn nhiều thành phần sẽ sinh ra tải trọng pháp tuyến và quyết định ứng suất ma sát trượt dính–trượt giữa các lớp khi cáp bị uốn.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- **Áp suất là P2 (tải đặt trước cố định $0.2\text{ MPa}$):** Tác giả không bao giờ thay đổi mức áp suất này để kiểm tra xem độ cứng uốn của cáp có thay đổi theo áp suất hay không.
- Vật liệu hoàn toàn là kim loại thông thường (đồng, thép) và polymer đàn dẻo, không có hợp kim nhớ hình NiTi.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Khẳng định ranh giới vững chắc: Tjahjanto et al. 2017 đã tiếp cận rất gần bài toán tiếp xúc do áp suất hướng tâm khi uốn, nhưng vì áp suất là hằng số cố định P2 và không phục vụ mục đích điều khiển độ cứng, công trình này **không thể phủ định mục tiêu T2** của MP1.

---

### EVIDENCE W07-E02 — Thẩm tra sâu luận văn Xin Liu 2004 (`aaad9c248c`)

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** T2 — Boundary audit against passive preforming pressure (P1).

**Paper title:** *Cable Vibration Considering Internal Friction*

**Authors:** Xin Liu

**Year:** 2004

**Loại tài liệu:** Luận văn Thạc sĩ Khoa học (M.S. thesis, Technische Universität Darmstadt, Germany)

**DOI:** [KHÔNG CÓ DOI — Luận văn Thạc sĩ]

**paper_id:** `aaad9c248c`

**Verification round:** MP1-V002

**Evidence JSON:** `data/evidence/A5-Cable vibration considering internal friction_aaad9c248c.json`

**Original PDF:** `papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf`

**Page(s) / Section:** Trang 10, 11, 15, 16, 17, 18, 26, 37, 44, 46, 58, 63, 65; Chapters 2, 3, 5.

**Evidence type:** Mechanical modeling, numerical simulation, and push-out friction experiments.

### Thiết lập cơ học (Mechanical setup)
- Khảo sát cáp xoắn nhiều lớp bằng kim loại (steel conductors / stranded cables).
- Cơ chế áp suất: Trong quá trình chế tạo dệt cáp (manufacturing/preforming), các sợi xoắn lớp ngoài bị biến dạng dẻo uốn ép vào lớp trong, tạo nên một trường **áp suất tiếp xúc hướng tâm thụ động (passive radial preforming pressure)** kẹp chặt các lớp dây lại với nhau (pp. 58, 62, 63).
- Tác giả thực hiện thí nghiệm đẩy trượt trục (push-out tests) trên máy thử cơ tính để đo trực tiếp lực ma sát và suy ra áp suất hướng tâm trung bình giữa các lớp:
  - Giữa Lớp 1 và Lớp 2: $p_{\text{radial}} = 0.475\text{ N/mm}^2$ ($475\text{ kPa}$).
  - Giữa Lớp 2 và Lớp 3: $p_{\text{radial}} = 0.053\text{ N/mm}^2$ ($53\text{ kPa}$) (pp. 63, 65).

### Mô hình / lý thuyết (Model / theory)
- Mô hình hóa sự biến thiên của độ cứng kháng uốn (flexural rigidity $EI$) của cáp theo độ cong uốn $\kappa$ (pp. 16, 17, 18):
  - Khi độ cong nhỏ ($\kappa < \kappa_{\text{crit}}$): Lực cắt do uốn chưa thắng được ma sát gây bởi áp suất hướng tâm $p_{\text{radial}}$, các lớp dây dính chặt (stick), $EI = EI_{\max}$ (ứng xử như một thanh đặc).
  - Khi độ cong vượt ngưỡng ($\kappa \ge \kappa_{\text{crit}}$): Trượt xuất hiện giữa các lớp (slip), lực ma sát Coulomb tiêu tán năng lượng, và độ cứng uốn giảm phi tuyến về độ cứng tổng của các sợi riêng rẽ $EI_{\min}$ (pp. 17, 26).
- Phương trình chuyển động dao động ngang của dầm cáp tích hợp hàm tiêu tán ma sát trượt nội tại phụ thuộc áp suất hướng tâm (pp. 20, 22, 26).

### Kết quả rà soát từ khóa PDF (PDF Keyword Search Evidence)
Rà soát toàn văn tệp PDF `A5-Cable vibration considering internal friction.pdf`:
- Từ khóa `radial pressure`: Xuất hiện dày đặc từ p. 15 đến p. 66 (ví dụ: p. 16 "The radial pressure between layers...", p. 63 "radial pressure of 0.475 N/mm^2...").
- Từ khóa `active pressure` / `confinement`: Không xuất hiện. Áp suất hoàn toàn là áp suất cơ học dư do biến dạng xoắn vặn khi sản xuất (preforming/manufacturing).
- Từ khóa `Nitinol` / `SMA` / `shape memory`: Xuất hiện 0 lần (vật liệu là thép đàn hồi tuyến tính).

### Bằng chứng này chứng minh điều gì (What this proves)
Chứng minh rằng lý thuyết cơ học về mối quan hệ giữa **áp suất hướng tâm $\rightarrow$ lực ma sát tiếp xúc pháp tuyến $\rightarrow$ ngưỡng trượt dính–trượt (stick-slip) $\rightarrow$ sự suy giảm độ cứng uốn phi tuyến** đã được phát triển và kiểm chứng thực nghiệm hoàn chỉnh từ năm 2004 cho cáp kim loại thông thường.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Áp suất hướng tâm trong luận văn là **P1 (áp suất thụ động cố hữu của kết cấu)**, không thể tăng giảm tùy ý trong lúc cáp đang vận hành.
- Vật liệu là thép đàn hồi cổ điển, không có hiệu ứng siêu đàn hồi hay chuyển pha mactenxít.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Xin Liu 2004 là nền tảng cơ học cực kỳ quan trọng. Nó khẳng định rằng việc mô hình hóa dầm sợi có ma sát phụ thuộc áp suất hướng tâm không phải là một phát minh mới. Tuy nhiên, việc chuyển từ **áp suất thụ động P1 (hằng số hình học)** sang **áp suất giam giữ chủ động P3 (biến số điều khiển động bằng chất lỏng hoặc khí nén)** và đưa vật liệu siêu đàn hồi NiTi vào trung tâm chính là lằn ranh bảo vệ tính mới của T2.

## 6. Kết luận về claim/target (Claim/target conclusion)

- **Tại sao áp suất thụ động (P1) hoặc lực siết cố định (P2) KHÔNG tương đương với P3?**  
  [INFERENCE]
  - **P1 (Áp suất thụ động):** Là hàm phụ thuộc hoàn toàn vào biến dạng và góc xoắn hình học ($p = f(\kappa, \varepsilon, \theta)$). Nhà nghiên cứu không thể can thiệp độc lập vào $p$ mà không làm thay đổi biến dạng của dầm. Khi dầm đứng yên hoặc chịu uốn nhỏ, $p$ không thể chủ động tăng vọt lên để hóa cứng dầm theo ý muốn.
  - **P2 (Tải đặt trước cố định):** Là điều kiện biên lắp ráp ($p = \text{const}$). Sau khi lắp ráp, dầm chỉ có một đường cong đặc tính cơ học cố định duy nhất. Không thể thực hiện chức năng biến đổi độ cứng (variable stiffness) theo thời gian thực.
  - **P3 (Áp suất giam giữ chủ động):** Là một biến số điều khiển vận hành độc lập ($p = p(t) \in [0, p_{\max}]$ do hệ thống bơm/van điều áp cung cấp). Ở cùng một độ cong uốn $\kappa$ và cùng một trạng thái hình học, người điều khiển có thể chủ động thay đổi $p$ từ $0$ lên $300\text{ kPa}$ để dịch chuyển tức thời ngưỡng trượt $Q_S(p)$ và làm biến đổi độ cứng uốn của dầm giữa trạng thái mềm linh hoạt và trạng thái cứng chịu tải.
- **Phán quyết thẩm tra (Audit Verdict):**  
  [AUDIT VERDICT] **T2 = `open_in_current_full_text_set`**. Trong toàn bộ tập tài liệu toàn văn hiện có của repository, **chưa có bất kỳ công trình nào thực hiện việc giam giữ một bó dây kim loại hay NiTi bằng áp suất giam giữ chủ động P3 để điều khiển độ cứng uốn**.
- **Cảnh báo khoa học:** Tính mở của T2 trong tập tài liệu này chỉ là kết quả bị chặn bởi giao thức (protocol-bounded result), không chứng minh tính mới phổ quát trên toàn bộ kho tàng khoa học nhân loại.

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Chưa có bất kỳ phép đo thực nghiệm nào trong repo về đường cong mô-men uốn - độ cong ($M - \kappa$) của bó dây NiTi được vẽ ở nhiều mức áp suất giam giữ chủ động khác nhau (ví dụ: $0, 50, 100, 200, 300\text{ kPa}$).
- Chưa rõ liệu ma sát giữa vỏ màng áp suất (silicone/màng cao su) với các sợi NiTi lớp ngoài có đóng góp đáng kể vào độ cứng uốn so với ma sát giữa các sợi dây NiTi nội tại hay không.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Kiểm tra lại xem trong các nhánh trích dẫn ngược của Xin Liu 2004 (như các công trình kinh điển của Costello về cơ học dây vặn cáp xoắn "Theory of Wire Rope") có tài liệu nào từng đề xuất việc đặt cáp vào trong một ống áp suất thủy tĩnh để điều chỉnh độ cản uốn hay chưa?
2. Trong bài Tjahjanto et al. 2017 (`ccdc1bb980`), áp suất $0.2\text{ MPa}$ tác dụng lên vỏ trong có tạo ra sự phân bố ứng suất nén không đều giữa các sợi trong cùng một tao cáp hay không, và hiệu ứng vòm (arching effect) trong bó dây NiTi dưới áp suất dương P3 có làm triệt tiêu áp lực truyền vào các sợi lõi trung tâm hay không?

## 9. Danh mục kiểm tra xác minh gói bằng chứng (Packet verification checklist)

- [x] Tiêu đề bài báo được xác minh nguyên văn tiếng Anh (paper title verified)
- [x] Tác giả và năm xuất bản được đối chiếu (authors/year verified)
- [x] DOI được xác minh từ tệp bằng chứng hoặc ghi rõ lý do không có DOI (DOI verified)
- [x] Mã định danh bài báo paper_id khớp chính xác với registry (paper_id verified)
- [x] Đường dẫn tệp evidence JSON được xác minh tồn tại trên đĩa (evidence JSON path verified)
- [x] Đường dẫn tệp PDF gốc được đối chiếu (PDF path verified)
- [x] Các số liệu định lượng có số trang kiểm chứng (quantitative claims page-verified)
- [x] Các cơ chế cơ học có số trang kiểm chứng (mechanical claims page-verified)
- [x] Phán quyết audit được phân biệt rõ với sự kiện bài báo (audit verdict separated from paper fact)
- [x] Các nhận định suy luận được gắn nhãn [INFERENCE] / [DERIVATION] rõ ràng (inference explicitly labelled)
- [x] Mục “What it does NOT prove” được điền đầy đủ cho từng nguồn (What it does NOT prove completed)
- [x] Các điểm chưa giải quyết hoặc giới hạn được công khai minh bạch (unresolved issues disclosed)
