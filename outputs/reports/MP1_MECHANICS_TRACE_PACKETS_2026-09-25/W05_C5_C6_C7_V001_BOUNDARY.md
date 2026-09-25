# W05 — Ranh giới Thẩm tra C5, C6, C7 sau MP1-V001 và Sự Hình thành Mechanics Core

## 1. Mục tiêu (Mission)

Phân tích sâu sắc ranh giới khoa học giữa những gì đã bị bác bỏ và những gì còn mở lại (`open`) sau vòng thẩm tra kiến trúc MP1-V001 đối với ba phát biểu sống sót:
- **C5:** Bản thân các dây NiTi siêu đàn hồi đóng vai trò môi trường nghẽn ma sát trực tiếp (Superelastic NiTi wires themselves as the frictional jamming medium).
- **C6:** Áp suất giam giữ dương tác động trực tiếp lên bó dây NiTi siêu đàn hồi (Positive-pressure confinement of a superelastic NiTi wire bundle).
- **C7:** Sự ghép cặp đa trường giữa tính siêu đàn hồi NiTi, trượt ma sát giữa các dây, áp suất giam giữ và độ cứng uốn (Coupling among NiTi superelasticity, inter-wire slip/friction, pressure, and bending stiffness).

Nhiệm vụ làm rõ:
1. Từng bài báo đe dọa mạnh nhất đã thiết lập được những gì và thiếu yếu tố chính xác nào khiến claim không bị đóng hoàn toàn trong V001.
2. Vì sao trạng thái `open_in_supplied_corpus` tuyệt đối không đồng nghĩa với tính mới khoa học (novelty).
3. Quá trình suy luận logic chặt chẽ đưa phát biểu C7 trở thành bài toán cơ học cốt lõi (*mechanics core*) duy nhất của MP1.

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md`
- `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md`
- `outputs/verification/MP1-V001/verification_matrix.json`
- Các tệp bằng chứng và PDF gốc của: Bai et al. 2022 (`240fbf6022`), Liu et al. 2021 (`182d854610`), Takashima et al. 2022 (`2cd907e77a`), Wang et al. 2024 (`c6a31066f8`), Zhang & Yao 2026 (`3aa8790db0`).

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **C5:** `open_in_supplied_corpus` [AUDIT VERDICT]
- **C6:** `open_in_supplied_corpus` [AUDIT VERDICT]
- **C7:** `open_in_supplied_corpus` [AUDIT VERDICT]
- **Phán quyết tổng thể vòng V001:** `PIVOT_TO_MECHANICS_CORE` (nguồn: `CORE_PRIOR_ART_AUDIT.json`)

## 4. Bảng bằng chứng ranh giới (Boundary evidence table)

| Claim | Trạng thái V001 | Bài báo đe dọa chính | Những gì bài báo ĐÃ chứng minh | Yếu tố chính xác còn THIẾU |
|---|---|---|---|---|
| **C5** | `open_in_supplied_corpus` | Bai 2022 (`240fbf6022`); Zhang 2026 (`3aa8790db0`); Takashima 2022 (`2cd907e77a`); Wang 2024 (`c6a31066f8`) | Nghẽn dây/sợi (kraft, nylon); dây NiTi làm cốt dầm hoặc dây chằng kéo uốn. | Thiếu: Bó dây NiTi siêu đàn hồi tự nó là các phần tử tiếp xúc, trượt ma sát nghẽn trực tiếp lên nhau. |
| **C6** | `open_in_supplied_corpus` | Liu 2021 (`182d854610`); Zhang 2026 (`3aa8790db0`) | Áp suất dương nén nghẽn hạt (Liu) và nén bó sợi nylon (Zhang) lên tới 300 kPa. | Thiếu: Áp suất dương giam giữ trực tiếp một bó dây kim loại / NiTi siêu đàn hồi. |
| **C7** | `open_in_supplied_corpus` | Zhang 2026 (`3aa8790db0`); Takashima 2022 (`2cd907e77a`); Matsumoto 2024 (`7ce492505d`); Wang 2024 (`c6a31066f8`) | Zhang ghép cặp áp suất + ma sát sợi + độ cứng; Takashima ghép cặp nhiệt SMA + nghẽn hạt. | Thiếu: Ghép cặp đồng thời cả 4 yếu tố: chuyển pha NiTi $\times$ ma sát dính–trượt giữa các dây $\times$ áp suất giam giữ $\times$ độ cứng uốn. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W05-E01 — Ranh giới thẩm tra C5

**Phân loại (Classification):** [AUDIT VERDICT] kết hợp [VERIFIED PAPER FACT]

**Claim / Target:** C5 — Superelastic NiTi wires themselves as the frictional jamming medium remain open.

**Trạng thái thẩm tra:** `open_in_supplied_corpus`

**Audit source:** `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`, mục `claim_audit`, Claim C5.

### Phân tích chi tiết từng bài báo đe dọa:
1. **Bai et al. 2022 (`240fbf6022`):**
   - *Đã chứng minh:* Nghẽn dây bằng ma sát tiếp xúc giữa các sợi dây dưới áp suất chân không, làm tăng độ cứng uốn gần 7 lần (p. 8).
   - *Yếu tố còn thiếu:* Vật liệu là dây giấy kraft, dây gai dầu và dây cước nylon đàn hồi tuyến tính thông thường. Hoàn toàn không sử dụng dây hợp kim nhớ hình NiTi.
2. **Zhang & Yao 2026 (`3aa8790db0`):**
   - *Đã chứng minh:* Nghẽn bó 700 sợi nylon dưới áp suất dương, phân tách trạng thái dính–trượt (stick-slip) giải tích (pp. 1, 3–4).
   - *Yếu tố còn thiếu:* Vật liệu là sợi polymer tổng hợp (nylon monofilament), không có tính chất siêu đàn hồi.
3. **Takashima et al. 2022 (`2cd907e77a`):**
   - *Đã chứng minh:* Sử dụng 4 dây NiTi SMA tròn đường kính $1.0\text{ mm}$ kết hợp trong thiết bị biến đổi độ cứng bằng jamming (pp. 2, 3).
   - *Yếu tố còn thiếu:* Các dây NiTi được bố trí như các cốt dầm độc lập chôn trong môi trường hạt bã cà phê. **Bản thân các dây NiTi không tiếp xúc và không trượt ma sát lên nhau**; môi trường tạo nghẽn duy nhất là các hạt cà phê.
4. **Wang et al. 2024 (`c6a31066f8`):**
   - *Đã chứng minh:* Kết hợp các dây chằng siêu đàn hồi NiTi (superelastic NiTi tendons) chạy dọc thân robot mềm có lõi biến đổi độ cứng bằng particle jamming ép bởi piston (pp. 2, 5).
   - *Yếu tố còn thiếu:* Các dây chằng NiTi chỉ đóng vai trò truyền lực kéo uốn phân đoạn cánh tay từ bên ngoài, hoàn toàn tách biệt khỏi môi trường hạt bị nghẽn bên trong.

### Kết luận ranh giới C5:
Trong phạm vi 11 bài báo của MP1-V001, chưa có bài nào hiện thực hóa một cơ cấu mà ở đó các dây NiTi siêu đàn hồi tự đóng vai trò là các phần tử ma sát trượt lên nhau để tạo hiệu ứng nghẽn. Do đó C5 được ghi nhận là mở trong tập dữ liệu khảo sát (`open_in_supplied_corpus`).

---

### EVIDENCE W05-E02 — Ranh giới thẩm tra C6

**Phân loại (Classification):** [AUDIT VERDICT] kết hợp [VERIFIED PAPER FACT]

**Claim / Target:** C6 — Positive-pressure confinement of a superelastic NiTi wire bundle remains open.

**Trạng thái thẩm tra:** `open_in_supplied_corpus`

**Audit source:** `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`, mục `claim_audit`, Claim C6.

### Phân tích chi tiết từng bài báo đe dọa:
1. **Liu et al. 2021 (`182d854610`):**
   - *Đã chứng minh:* Áp suất nén dương bên trong làm giãn nở bóng khí, nén ép môi trường hạt trong khoang vành khuyên và tăng độ cứng uốn lên xấp xỉ 6 lần (pp. 1, 4).
   - *Yếu tố còn thiếu:* Môi trường bị giam giữ bởi áp suất dương là hạt rắn (granular beads), không phải bó dây kim loại.
2. **Zhang & Yao 2026 (`3aa8790db0`):**
   - *Đã chứng minh:* Áp suất nén dương từ bóng khí dẹt (lên tới $300\text{ kPa}$) giam giữ trực tiếp một bó sợi (pp. 1, 2, 5).
   - *Yếu tố còn thiếu:* Bó sợi được giam giữ là sợi nylon. Không có tài liệu nào trong tập V001 nén trực tiếp một bó dây kim loại hay NiTi bằng bóng khí nén dương.

### Cảnh báo nghiêm ngặt về suy luận (Strict Inference Rule):
[INFERENCE] Mặc dù C6 ở trạng thái mở trong tập dữ liệu, **không thể tuyên bố tính mới chỉ bằng việc "thay thế vật liệu" (material substitution)**:
$$\text{Sợi nylon} + \text{Áp suất dương} \quad \centernot\implies \quad \text{Dây NiTi} + \text{Áp suất dương là tính mới khoa học}$$
Nếu hành vi cơ học của bó dây NiTi dưới áp suất dương chỉ đơn giản tuân theo cùng các phương trình dầm đàn hồi của Zhang & Yao 2026 với việc thế mô-đun đàn hồi $E_{\text{NiTi}}$ và hệ số ma sát $\mu_{\text{NiTi}}$, thì C6 hoàn toàn không có đóng góp cơ học mới và sẽ bị tiêu diệt (killed) bởi bài toán thay thế thông số (parameter substitution).

---

### EVIDENCE W05-E03 — Ranh giới thẩm tra C7 và Sự hình thành Mechanics Core

**Phân loại (Classification):** [AUDIT VERDICT] kết hợp [INFERENCE]

**Claim / Target:** C7 — Coupling among NiTi superelastic response, inter-wire slip/friction, pressure, and bending stiffness remains open.

**Trạng thái thẩm tra:** `open_in_supplied_corpus`

**Audit source:** `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`, mục `claim_audit`, Claim C7 và mục `closest_prior_art`.

### Ma trận đối chiếu ghép cặp 4 thành phần trong các bài báo gần nhất:

| Bài báo | 1. Siêu đàn hồi / Chuyển pha NiTi | 2. Trượt / Ma sát giữa các dây | 3. Áp suất giam giữ chủ động | 4. Độ cứng uốn cấu trúc | Đánh giá ghép cặp |
|---|:---:|:---:|:---:|:---:|---|
| **Zhang & Yao 2026** (`3aa8790db0`) | **KHÔNG** (Nylon đàn hồi) | **CÓ** (Trượt ma sát giữa 700 sợi) | **CÓ** (Áp suất dương 0–300 kPa) | **CÓ** (Độ cứng uốn 3 điểm) | Ghép cặp được (2) + (3) + (4), thiếu (1). |
| **Takashima 2022** (`2cd907e77a`) | **CÓ** (Dây SMA biến đổi pha nhiệt) | **KHÔNG** (Dây không cọ xát nhau) | **CÓ** (Chân không nghẽn hạt) | **CÓ** (Độ cứng uốn công-xôn) | Ghép cặp được (1) + (3) + (4), thiếu (2). |
| **Matsumoto 2024** (`7ce492505d`) | **CÓ** (Pha R của dây Ti-Ni) | **KHÔNG** (Dây không cọ xát nhau) | **CÓ** (Chân không nghẽn hạt) | **CÓ** (Độ cứng phục hồi) | Ghép cặp được (1) + (3) + (4), thiếu (2). |
| **Wang et al. 2024** (`c6a31066f8`) | **CÓ** (Dây chằng kéo NiTi) | **KHÔNG** (Dây chằng ngoài) | **CÓ** (Piston ép hạt cơ khí) | **CÓ** (Độ cứng uốn cánh tay) | Ghép cặp tách rời: dây chằng uốn riêng, hạt chịu nén riêng. |

### Logic chuyển dịch sang Mechanics Core:
1. Nhìn vào bảng trên, **không một công trình nào tích hợp đồng thời cả 4 hiện tượng cơ học**.
2. Khi uốn một bó dây kim loại thông thường, các sợi chịu ứng suất kéo và nén dọc trục phụ thuộc vào khoảng cách tới trục trung hòa. Khi lực cắt vượt quá lực ma sát ma-xít ($Q > Q_J$), hiện tượng trượt (slip) xuất hiện.
3. Đối với hợp kim NiTi siêu đàn hồi, khi ứng suất vượt qua ngưỡng chuyển pha khởi đầu ($\sigma > \sigma_s^{AM}$), vật liệu xuất hiện **thềm chuyển pha (transformation plateau)** với biến dạng lớn ở ứng suất gần như không đổi, mô-đun tiếp tuyến giảm mạnh, và diện tích trễ rất lớn (flag-shaped hysteresis).
4. **Câu hỏi cơ học cốt lõi (Mechanics Core Question):**  
   > *Sự xuất hiện đồng thời của thềm ứng suất chuyển pha và biến dạng chuyển pha trong các sợi dây ngoài cùng (nơi chịu ứng suất lớn nhất khi uốn) sẽ làm thay đổi phân bố lực tiếp xúc pháp tuyến, ngưỡng trượt dính–trượt (stick-slip), và độ cứng uốn tương đương dưới tác dụng của áp suất giam giữ chủ động như thế nào? Liệu đáp ứng cơ học đó có vượt ra ngoài một mô hình dầm sợi đàn hồi tuyến tính chỉ với việc thay thế tham số hay không?*

Đây chính là câu hỏi khoa học duy nhất có thể bảo vệ được của MP1. Toàn bộ tính mới của đề tài được quy tụ về câu hỏi này, dẫn đến phán quyết chính thức: `PIVOT_TO_MECHANICS_CORE`.

## 6. Kết luận về claim/target (Claim/target conclusion)

- **Nguyên tắc "Open in supplied corpus" $\ne$ Novelty:**  
  [AUDIT VERDICT] Việc C5, C6, C7 ở trạng thái mở chỉ phản ánh rằng **11 bài báo được nạp vào vòng MP1-V001 chưa chứa đựng cơ chế ghép cặp này**. Đây là một kết quả bị chặn bởi giao thức (protocol-bounded finding), không phải bằng chứng chứng minh tính mới phổ quát (universal novelty).
- **Lý do sụp đổ của tính mới kết hợp linh kiện:**  
  [INFERENCE] Mọi nỗ lực xin cấp bằng sáng chế hay bảo vệ luận văn dựa trên "thiết bị gồm bó dây NiTi + bóng áp suất dương + bơm SMA" đều sẽ bị các hội đồng khoa học coi là kỹ thuật chắp vá linh kiện (mere aggregation of known elements).
- **Trục chuyển hướng sống còn:**  
  Dự án MP1 đã từ bỏ hoàn toàn việc tranh luận tính mới ở cấp độ robot/thiết bị, và chuyển toàn bộ nguồn lực sang việc kiểm chứng tính mới ở cấp độ cơ học tiếp xúc ghép cặp (coupled contact mechanics).

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Tập 11 bài báo của MP1-V001 chủ yếu đến từ cộng đồng Robot mềm (IEEE T-RO, Soft Robotics, RA-L, JRM).
- Các lĩnh vực kỹ thuật lân cận có lịch sử lâu đời về bó dây kim loại và cáp hợp kim nhớ hình — cụ thể là:
  - Cơ học cáp và dây vặn (Cable mechanics / Wire ropes);
  - Kết cấu giảm chấn công trình dân dụng (Civil structural dampers / Cable vibration isolators);
  - Cơ học vật rắn biến dạng (Solid mechanics / Multibody contact).
- Nếu các lĩnh vực này đã giải quyết bài toán ma sát tiếp xúc giữa các dây NiTi và ảnh hưởng của áp suất giam giữ, thì ngay cả Mechanics Core cũng sẽ bị tiêu diệt. Đây chính là lý do MP1-V002 phải được kích hoạt để kiểm chứng các mục tiêu đe dọa mục tiêu T1, T2, T3.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Liệu trong bài Wang et al. 2024 (`c6a31066f8`), khi cánh tay uốn cong ở biên độ lớn, các dây chằng NiTi có cọ xát với các lỗ dẫn hướng hoặc vỏ ngoài hay không, và ma sát đó có được mô hình hóa không?
2. Giả thuyết về "Mechanics Core" có thực sự đòi hỏi một mô hình cơ học vi mô hoàn toàn mới, hay chỉ cần một mô hình dầm composite phi tuyến nhiều lớp (multilayer beam model) với quan hệ cấu thành phi tuyến là đủ?

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
