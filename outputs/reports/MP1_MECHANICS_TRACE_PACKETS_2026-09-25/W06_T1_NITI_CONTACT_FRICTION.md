# W06 — Kiểm chứng Chuyên sâu Mục tiêu T1: Cơ học Tiếp xúc và Ma sát Dây NiTi

## 1. Mục tiêu (Mission)

Thẩm tra chuyên sâu toàn văn (deep full-text audit) mục tiêu đe dọa **T1** trong vòng MP1-V002:
> "Bản thân các dây NiTi/Nitinol tạo thành các cụm bó/cáp tiếp xúc và trượt ma sát lên nhau, trong đó đáp ứng độ cứng và trễ kết cấu phụ thuộc trực tiếp vào tương tác ma sát tiếp xúc giữa các dây (inter-wire interaction)."

Nhiệm vụ trọng tâm:
1. Thẩm tra 5 bài báo ưu tiên cốt lõi: `d9966f2f5e`, `53200aa0c6`, `98fee47c04`, `e8462758c3`, `6dd1ca94d1`.
2. Bóc tách chi tiết: cấu trúc hình học cáp/bó dây (cable/rope architecture), cơ chế tiếp xúc pháp tuyến, ma sát Coulomb và vi trượt (microslip), hiện tượng tiêu tán năng lượng trễ (hysteresis), giảm chấn (damping), ghép cặp chuyển pha mactenxít (phase transformation), và biến thiên độ cứng tương đương.
3. Giải thích vì sao T1 bị đóng hoàn toàn bằng tài liệu toàn văn (`closed_by_full_text`), đồng thời chứng minh tại sao các bài báo này **hoàn toàn KHÔNG thiết lập được mục tiêu T2** (áp suất giam giữ chủ động).

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`
- `outputs/verification/MP1-V002/verification_matrix.json`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.md`
- Các tệp bằng chứng JSON và PDF tương ứng trong `data/evidence/` và `papers/verification/MP1-V002/`:
  - Carboni et al. 2014/2015 (`d9966f2f5e`)
  - Vahidi et al. 2021 (`53200aa0c6`)
  - Niu & Chen 2021 (`98fee47c04`)
  - Liu et al. 2026 (`e8462758c3`)
  - Silva et al. 2022 (`6dd1ca94d1`)

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **Target:** T1
- **Phán quyết thẩm tra:** `closed_by_full_text` [AUDIT VERDICT]
- **Độ tin cậy:** `high` [AUDIT VERDICT]
- **Tóm tắt đánh giá có thẩm quyền:** Tài liệu tiền nhiệm về cáp, tao cáp và bó sợi bện NiTi/Nitinol đã chứng minh đầy đủ rằng ma sát giữa các dây, sự trượt tương đối và biến dạng hình học vặn xoắn tác động sâu sắc lên độ cứng uốn/kéo, độ trễ thắt eo (pinched hysteresis), khả năng giảm chấn và động học chuyển pha.

## 4. Bảng bằng chứng (Evidence table)

| Evidence ID | Claim/Target | Paper | DOI | paper_id | Page(s) | Evidence type | Finding |
|---|---|---|---|---|---|---|---|
| W06-E01 | T1 | Carboni et al. 2014 | 10.1061/(ASCE)EM.1943-7889.0000852 | d9966f2f5e | 1, 7–11, 12–14 | Experimental / Analytical | Cụm tao cáp Nitinol chịu uốn thuần túy thể hiện trễ làm mềm giả tuyến tính do ma sát giữa các dây; mô hình Bouc-Wen thắt eo; T1 CLOSED. |
| W06-E02 | T1 | Vahidi et al. 2021 | 10.1080/15376494.2021.1955313 | 53200aa0c6 | 2–6, 8–12, 14 | FE Simulation / Contact | Mô hình 3D phần tử hữu hạn cáp SMA $1\times 27$ và $7\times 7$ ghép ma sát Coulomb và tiếp xúc pháp tuyến; ứng suất dư ma sát $100\text{ MPa}$; T1 CLOSED. |
| W06-E03 | T1 | Niu & Chen 2021 | 10.3390/app112110032 | 98fee47c04 | 1, 4, 10–16 | Modeling / Dynamics | Bộ cách chấn cáp vặn NiTiNOL; mô hình Bouc-Wen sửa đổi ghép ma sát và chuyển pha; độ cứng và giảm chấn phụ thuộc biên độ; T1 CLOSED. |
| W06-E04 | T1 | Liu et al. 2026 | 10.1016/j.matlet.2026.141544 | e8462758c3 | 1–4 | Experimental / DMA | Vi sợi bện NiTi (4B–88B); mạng vi lò xo chuyển biến dạng vĩ mô thành uốn/xoắn cục bộ và vi trượt ma sát tiếp xúc; mô-đun đàn hồi $3.6\text{ GPa}$; T1 CLOSED. |
| W06-E05 | T1 | Silva et al. 2022 | 10.3390/s22208045 | 6dd1ca94d1 | 1, 8–11, 13–15, 20 | Experimental / Thermomechanical | Vi cáp $1\times 7$ NiTi siêu đàn hồi; tự gia nhiệt ma sát giữa các sợi làm tăng nhiệt độ $80\%$, đẩy thềm ứng suất lên cao theo Clausius-Clapeyron, làm cứng kết cấu; T1 CLOSED. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W06-E01

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** T1 — NiTi wire assemblies exhibit inter-wire friction and stiffness modulation.

**Paper title:** *Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification*

**Authors:** Biagio Carboni, Walter Lacarbonara, Ferdinando Auricchio

**Year:** 2014 (Published online 2014, print 2015)

**DOI:** `10.1061/(ASCE)EM.1943-7889.0000852`

**paper_id:** `d9966f2f5e`

**Verification round:** MP1-V002

**Evidence JSON:** `data/evidence/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json`

**Original PDF:** `papers/verification/MP1-V002/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf`

**Page(s) / Section:** Trang 1, 7, 8, 9, 10, 11, 12, 13, 14; Sections: Experimental Campaign, Restoring Force Models.

**Evidence type:** Experimental mechanics and phenomenological identification.

### Thiết lập cơ học (Mechanical setup)
- Khảo sát các cấu hình lắp ráp đa dạng gồm các tao cáp Nitinol (tao $1\times 7$ sợi, đường kính danh nghĩa $0.5\text{ mm}$ mỗi sợi) và cáp thép.
- Ba cấu hình biên cơ học được phân tách rõ ràng:
  - Cấu hình S1: Chịu tải uốn - kéo kết hợp (bending-tension), dẫn đến hiện tượng cứng hóa hình học và thắt eo trễ cực mạnh.
  - Cấu hình S2: Chịu **uốn thuần túy (pure bending)**, loại bỏ ứng ứng suất kéo hình học màng.
  - Cấu hình S3: Cấu hình trung gian điều chỉnh tỷ số độ cứng giữa tao cáp thép và tao cáp Nitinol (pp. 1, 7, 9).

### Mô hình / lý thuyết (Model / theory)
- Mô hình Bouc-Wen mở rộng kết hợp hàm thắt eo hai tham số hình chuông (two-parameter bell-shaped pinching function), dự báo chính xác lực phục hồi phi tuyến với sai số toàn phương trung bình $\text{MSE} < 1\%$ (pp. 3–5).
- Ở cấp độ sợi đơn, áp dụng mô hình cấu thành nhiệt - đàn dẻo một chiều Ivshin–Pence mô tả đường cong trễ siêu đàn hồi (pp. 8, 12–14).

### Phương pháp thí nghiệm (Experimental method)
- Thí nghiệm kéo tĩnh chu kỳ trên sợi đơn và tao cáp 7 sợi Nitinol bằng máy kéo nén thủy lực dưới kiểm soát dịch chuyển.
- Thí nghiệm uốn động chu kỳ với các mức biên độ dịch chuyển khác nhau để khảo sát biến thiên độ cứng và diện tích vòng trễ (pp. 7, 8).

### Kết quả định lượng (Quantitative results)
- Ở cấu hình uốn thuần túy S2, toàn bộ sự tiêu tán năng lượng và vòng lặp trễ làm mềm giả tuyến tính (quasi-linear softening hysteresis) được **chi phối hoàn toàn bởi ma sát khô giữa các dây (interwire friction)** (p. 10).
- Tao cáp 7 sợi Nitinol có ứng suất danh nghĩa trên đơn vị diện tích tại cùng mức biến dạng kéo luôn thấp hơn sợi thẳng đơn lẻ do bước xoắn dãn ra và hiện tượng trượt ma sát giữa các sợi dọc theo chiều dài tiếp xúc (pp. 8, 9, 10).

### Bằng chứng này chứng minh điều gì (What this proves)
Chứng minh trực tiếp rằng trong cụm dây/tao cáp NiTi, ma sát trượt giữa các dây là hiện tượng vật lý có thật, trực tiếp quyết định hình dạng vòng trễ năng lượng và độ cứng tương đương khi dầm chịu uốn.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Ma sát tiếp xúc giữa các dây trong bài báo thuần túy sinh ra do sự vặn xoắn hình học ban đầu của tao cáp (helix angle) và điều kiện biên ngàm gối.
- **Hoàn toàn không có nguồn áp suất giam giữ chủ động (active confinement pressure)** tác động vuông góc lên bề mặt ngoài của bó dây để điều chỉnh ma sát.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Đóng T1: Không thể tự nhận là người đầu tiên phát hiện ra hiện tượng ma sát giữa các dây NiTi làm thay đổi độ cứng uốn và độ trễ.

---

### EVIDENCE W06-E02

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** T1 — 3D contact FE modeling of SMA wire ropes.

**Paper title:** *Mechanical response of single and double-helix SMA wire ropes*

**Authors:** Saeed Vahidi, Jamal Arghavani, Eunsoo Choi, Alireza Ostadrahimi

**Year:** 2021 (Published online 2021, print 2022)

**DOI:** `10.1080/15376494.2021.1955313`

**paper_id:** `53200aa0c6`

**Verification round:** MP1-V002

**Evidence JSON:** `data/evidence/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json`

**Original PDF:** `papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf`

**Page(s) / Section:** Trang 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14; Sections: Constitutive Model, FE Modeling, Results.

**Evidence type:** 3D Finite element contact simulation and constitutive modeling.

### Thiết lập cơ học (Mechanical setup)
- Mô hình hóa chi tiết hình học không gian 3D của hai loại cáp hợp kim nhớ hình:
  - Cáp tao đơn xoắn ốc bậc một ($1\times 27$ single-helix SMA cable, gồm 4 lớp đồng tâm).
  - Cáp tao kép xoắn ốc bậc hai ($7\times 7$ double-helix SMA wire rope, gồm 7 tao cáp $1\times 7$ bện xoắn với nhau) (pp. 4, 5).
- Các mặt biên tiếp xúc giữa tất cả các sợi dây lân cận được định nghĩa tường minh với thuật toán tiếp xúc bề mặt - bề mặt (surface-to-surface penalty contact) kết hợp ma sát Coulomb ($\mu = 0.115$) (p. 4).

### Mô hình / lý thuyết (Model / theory)
- Tích hợp mô hình cấu thành biến đổi pha mactenxít 3D (mô hình Souza–Auricchio) vào phần mềm Abaqus qua chương trình con người dùng UMAT (pp. 2, 3).
- Lực ma sát và phản lực pháp tuyến tiếp xúc giữa các dây được giải trực tiếp đồng thời cùng phương trình cân bằng biến dạng phi tuyến lớn (p. 4).

### Phương pháp thí nghiệm (Experimental method)
- Kiểm chứng mô hình tiếp xúc phần tử hữu hạn bằng dữ liệu chuẩn của cáp thép $1\times 37$ từ $10\text{ kN}$ đến $35\text{ kN}$ (sai số $< 2\%$) (pp. 4, 5).
- Mô phỏng kéo đơn trục và chu kỳ nhiệt dưới điều kiện ngàm không quay (zero end rotation) (pp. 5, 6).

### Kết quả định lượng (Quantitative results)
- Lực kéo dọc trục tự động sinh ra mô-men xoắn phản lực và ứng suất cắt nội tại rất lớn do góc nghiêng đường xoắn ốc (helix angle) (pp. 6, 8, 9).
- Phân bố tải trọng tiếp xúc không đồng đều: Sợi lõi trung tâm (core wire) chịu ứng suất pháp tuyến cực đại (lên tới $\sim 330\text{ MPa}$ trong cáp $7\times 7$ và $\sim 680\text{ MPa}$ trong cáp $1\times 27$), trong khi các sợi xoắn kép lớp ngoài mang phần lớn tổng lực kéo dọc trục ($\sim 260\text{ N}$) (pp. 6, 7, 12).
- Khi dỡ tải ở nhiệt độ dưới $A_s$, ma sát tiếp xúc và sự kẹt cơ học giữa các dây sinh ra **ứng suất dư ma sát nội tại rất lớn ($\sim 100\text{ MPa}$ ở sợi lõi cáp $7\times 7$)**, lượng ứng suất dư này chỉ được giải phóng khi nung nóng phục hồi pha austenite (pp. 7, 8, 14).

### Bằng chứng này chứng minh điều gì (What this proves)
Mô hình hóa cơ học tiếp xúc 3D kết hợp ma sát Coulomb giữa hàng chục sợi dây NiTi siêu đàn hồi chuyển pha đã được cộng đồng cơ học giải quyết hoàn chỉnh, chứng minh sự tương tác tiếp xúc nội tại chi phối phân bố ứng suất và biến dạng dư.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Thí nghiệm và mô phỏng chỉ thực hiện cho tải kéo dọc trục và kích nhiệt; không có tải uốn (bending).
- Áp lực tiếp xúc pháp tuyến sinh ra thụ động do góc xoắn sợi khi bị kéo căng; **không có trường áp suất nén giam giữ dương từ bên ngoài**.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Khẳng định chắc chắn T1 đã được giải quyết ở cấp độ mô hình hóa phần tử hữu hạn tiếp xúc 3D.

---

### EVIDENCE W06-E03

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** T1 — Dynamic friction and stiffness in NiTi wire ropes.

**Paper title:** *Nonlinear Vibration Isolation via a NiTiNOL Wire Rope*

**Authors:** Mu-Qing Niu, Li-Qun Chen

**Year:** 2021

**DOI:** `10.3390/app112110032`

**paper_id:** `98fee47c04`

**Verification round:** MP1-V002

**Evidence JSON:** `data/evidence/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json`

**Original PDF:** `papers/verification/MP1-V002/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf`

**Page(s) / Section:** Trang 1, 4, 5, 10, 11, 14, 15, 16; Sections: Mathematical Model, Dynamic Responses.

**Evidence type:** Analytical dynamics and experimental vibration validation.

### Thiết lập cơ học (Mechanical setup)
- Khảo sát bộ giảm chấn cách rung dạng vòng uốn cáp vặn NiTiNOL (wire rope isolator) chịu tải trọng rung động cưỡng bức đa chiều.
- Cáp vặn được uốn cong thành hình vòng cung, các sợi dây cọ xát tương đối lên nhau khi vòng cáp bị nén uốn và kéo dãn dao động (p. 2).

### Mô hình / lý thuyết (Model / theory)
- Mô hình Bouc-Wen sửa đổi ghép nối hình học dầm cong với hiện tượng trễ ma sát nội tại và trễ chuyển pha của Nitinol (pp. 3–5).
- Áp dụng phương pháp cân bằng điều hòa (Harmonic Balance Method — HBM) kết hợp tích phân Runge–Kutta để giải đáp ứng tần số phi tuyến (pp. 5, 11).

### Kết quả định lượng (Quantitative results)
- Tương tác ma sát và chuyển pha tạo ra độ cứng tương đương (equivalent stiffness) và tỷ số giảm chấn phụ thuộc phi tuyến vào biên độ kích động: xuất hiện hiện tượng làm mềm ở biên độ vừa và cứng hóa ở biên độ lớn (pp. 10–14).
- Kiểm chứng thực nghiệm quét tần số gia tốc xác nhận sự dịch chuyển tần số cộng hưởng do biến thiên độ cứng nội tại của cáp NiTi (pp. 14, 15).

### Bằng chứng này chứng minh điều gì (What this proves)
Xác nhận rằng độ cứng tương đương và khả năng tiêu tán năng lượng của kết cấu cáp NiTi chịu uốn dao động phụ thuộc mật thiết vào ma sát trượt nội tại giữa các sợi dây.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Không có biến số điều khiển áp suất giam giữ độc lập; ma sát là đặc tính cố định của cấu trúc hình học cáp uốn sẵn.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Củng cố lý do đóng T1: Hiện tượng biến thiên độ cứng do ma sát cáp NiTi uốn đã được ứng dụng trong công nghiệp giảm chấn.

---

### EVIDENCE W06-E04

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** T1 — Braided NiTi microfilament contact density and micro-slip.

**Paper title:** *High damping capacity with a wide temperature window in braided NiTi microfilaments*

**Authors:** Yiwen Liu, Yi Zeng, Yang Liu, Yizhou Xiao, Tingjun Zhou, Junhua Du, Xuejun Jin, Fei Xiao

**Year:** 2026

**DOI:** `10.1016/j.matlet.2026.141544`

**paper_id:** `e8462758c3`

**Verification round:** MP1-V002

**Evidence JSON:** `data/evidence/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json`

**Original PDF:** `papers/verification/MP1-V002/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf`

**Page(s) / Section:** Trang 1, 2, 3, 4; Full text.

**Evidence type:** Experimental dynamic mechanical analysis (DMA).

### Thiết lập cơ học (Mechanical setup)
- Bó vi sợi hợp kim nhớ hình NiTi đường kính siêu nhỏ bện dạng ống (braided microfilaments) với số lượng sợi thay đổi từ 4 sợi (4B), 8 sợi (8B), 12 sợi (12B) dạng bện đơn và $8\times 8$ sợi (88B) dạng bện kép (p. 2).
- Mật độ bện được kiểm soát chính xác từ 25 đến 80 bước bện trên inch (picks per inch — ppi) (p. 3).

### Mô hình / lý thuyết (Model / theory)
- Các sợi dây đan chéo theo đường xoắn ốc tạo thành mạng lưới các vi lò xo không gian (interwoven micro-springs). Biến dạng vĩ mô bị mạng lưới này phân rã thành các ứng suất uốn, xoắn và trượt cục bộ không đồng nhất, kích hoạt chuyển pha mactenxít cục bộ kế tiếp kết hợp với **vi trượt ma sát tiếp xúc (contact micro-sliding friction)** (pp. 1, 4).

### Kết quả định lượng (Quantitative results)
- Tăng số lượng dây (từ 4B lên 8B và 12B) làm tăng mật độ điểm tiếp xúc ma sát, nâng hệ số tiêu tán năng lượng $\tan\delta$ từ $0.008-0.02$ (4B) lên $0.03-0.06$ (12B) (pp. 3, 4).
- Cấu trúc bện kép 88B đạt $\tan\delta \sim 0.06 - 0.11$ và làm suy giảm mô-đun tích trữ (storage modulus) xuống mức siêu thấp: **$\sim 3.6\text{ GPa}$ khi làm lạnh và $\sim 4.3\text{ GPa}$ khi gia nhiệt** trên một dải nhiệt độ cực rộng vượt quá $145^\circ\text{C}$ (từ $-70^\circ\text{C}$ đến $+75^\circ\text{C}$) (pp. 1, 4).
- Mật độ bện chi phối hành vi trượt: Mật độ thấp (25 ppi) dây lỏng lẻo trượt tự do; mật độ quá cao (80 ppi) kẹp chặt hình học làm hạn chế hành trình vi trượt, khiến $\tan\delta$ giảm xuống $0.02 - 0.04$ (pp. 3, 4).

### Bằng chứng này chứng minh điều gì (What this proves)
Chứng minh rằng mật độ tiếp xúc và sự hạn chế dịch chuyển vi trượt giữa các sợi NiTi trực tiếp điều biến mô-đun đàn hồi tương đương (storage modulus giảm từ $60\text{ GPa}$ xuống $3.6\text{ GPa}$) và độ tiêu tán năng lượng.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Thí nghiệm kéo DMA biên độ nhỏ; lực ép giam giữ là liên kết hình học thụ động của cấu trúc bện cố định, **không có áp suất giam giữ dương điều khiển chủ động**.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Cho thấy ràng buộc tiếp xúc cơ học có khả năng thay đổi sâu sắc độ cứng của cấu trúc NiTi đa sợi.

---

### EVIDENCE W06-E05

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** T1 — Inter-filament frictional heating and stiffening.

**Paper title:** *NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings*

**Authors:** Paulo C. S. Silva, Estephanie N. D. Grassi, Carlos J. Araújo, João M. P. Q. Delgado, Antonio G. B. Lima

**Year:** 2022

**DOI:** `10.3390/s22208045`

**paper_id:** `6dd1ca94d1`

**Verification round:** MP1-V002

**Evidence JSON:** `data/evidence/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json`

**Original PDF:** `papers/verification/MP1-V002/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf`

**Page(s) / Section:** Trang 1, 8, 9, 10, 11, 13, 14, 15, 20; Section 3 (Results and Discussion).

**Evidence type:** Experimental thermomechanical fatigue testing.

### Thiết lập cơ học (Mechanical setup)
- So sánh trực tiếp giữa vi cáp $1\times 7$ NiTi siêu đàn hồi (gồm 7 sợi xoắn đường kính ngoài tổng $0.48\text{ mm}$) và dây NiTi đơn đặc có cùng diện tích tiết diện chịu lực (p. 8).
- Tải trọng kéo chu kỳ động ở các tần số từ $0.25\text{ Hz}$ đến $10\text{ Hz}$.

### Kết quả định lượng (Quantitative results)
- Vi cáp đạt năng lượng tiêu tán chu kỳ cao hơn $15\% - 30\%$ và hệ số giảm chấn tương đương cao hơn $20\% - 47\%$ so với dây đơn đặc nhờ sự cọ xát ma sát giữa 7 sợi xoắn (pp. 1, 8, 13, 20).
- Sự cọ xát ma sát giữa các sợi cộng với ẩn nhiệt chuyển pha làm phát sinh **hiện tượng tự gia nhiệt do ma sát (frictional self-heating)** vượt bậc: ở tần số $10\text{ Hz}$, nhiệt độ vi cáp tăng vọt lên **$49.25^\circ\text{C}$ sau 128 chu kỳ (tăng $80\%$ so với tần số $0.25\text{ Hz}$)**, trong khi dây đơn đặc chỉ tăng $52\%$ (pp. 9, 10, 20).
- Theo hệ thức Clausius–Clapeyron:
  $$\frac{d\sigma}{dT} = -\frac{\Delta H}{T_0 \cdot \varepsilon_0}$$
  Sự gia tăng nhiệt độ nội tại này đẩy thềm ứng suất chuyển pha $\sigma^{AM}$ lên cao hơn, dẫn tới **sự cứng hóa nhiệt - cơ (thermomechanical stiffening)** của vi cáp khi chịu tải động (pp. 9, 10, 20).

### Bằng chứng này chứng minh điều gì (What this proves)
Chứng minh sự ghép cặp nội tại không thể tách rời giữa ma sát cơ học giữa các sợi NiTi và phản ứng nhiệt - cơ chuyển pha: ma sát sinh nhiệt $\rightarrow$ tăng nhiệt độ $\rightarrow$ tăng ứng suất chuyển pha $\rightarrow$ tăng độ cứng làm việc.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Thí nghiệm kéo thuần túy, không có trường áp suất nén giam giữ ngoài và không có thí nghiệm uốn dầm.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Cung cấp bằng chứng thực nghiệm quan trọng cho thấy ma sát giữa các dây NiTi không chỉ là ma sát cơ học thuần túy mà có phản hồi ngược lên trạng thái chuyển pha của vật liệu.

## 6. Kết luận về claim/target (Claim/target conclusion)

- **Sự kiện bài báo xác minh (Verified Paper Facts):**
  1. Cáp và tao cáp Nitinol chịu uốn thể hiện vòng trễ và độ cứng ma sát tiếp xúc rõ rệt (Carboni 2014, Niu 2021).
  2. Mô hình phần tử hữu hạn 3D đã giải bài toán tiếp xúc tiếp tuyến Coulomb và ứng suất dư ma sát giữa các sợi NiTi (Vahidi 2021).
  3. Mật độ vi trượt trong bó sợi bện NiTi làm biến đổi mô-đun đàn hồi từ $60\text{ GPa}$ xuống $3.6\text{ GPa}$ (Liu 2026).
  4. Ma sát giữa các sợi dây NiTi sinh nhiệt làm tăng ứng suất chuyển pha và độ cứng kết cấu (Silva 2022).
- **Phán quyết thẩm tra (Audit Verdict):**  
  [AUDIT VERDICT] **T1 = `closed_by_full_text`**. Tuyên bố rằng "dây NiTi tự cọ xát ma sát lên nhau để làm thay đổi độ cứng kết cấu là mới" hoàn toàn bị tài liệu tiền nhiệm phủ định.
- **Ranh giới bảo vệ (Defense Boundary):**  
  [INFERENCE] Mặc dù T1 bị đóng, **không có bất kỳ bài báo nào trong số 5 bài trên áp dụng một áp suất giam giữ dương chủ động (P3 active confinement pressure)** như một biến số điều khiển độc lập từ bên ngoài. Tất cả lực nén pháp tuyến trong các bài trên đều là lực nén thụ động sinh ra do bước xoắn hình học (helix lay angle) hoặc liên kết ngàm. Do đó, việc T1 bị đóng không giết chết T2.

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Chưa có bài nào khảo sát hành vi uốn công-xôn hoặc uốn 3 điểm của bó dây NiTi đặt trong một màng áp suất biến thiên chủ động.
- Chưa có số liệu thực nghiệm đo đạc lực ma sát trượt giữa các dây NiTi như một hàm số trực tiếp của áp suất giam giữ thủy tĩnh ngoài.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Trong bài Vahidi et al. 2021 (`53200aa0c6`), hệ số ma sát giữa các dây NiTi được chọn là $\mu = 0.115$ dựa trên nguồn tham khảo nào, và liệu giá trị này có thay đổi khi dây chuyển pha từ austenite sang martensite hay không?
2. Hiện tượng tự gia nhiệt ma sát trong bài Silva et al. 2022 (`6dd1ca94d1`) có thể trở thành một yếu tố gây nhiễu bất lợi (confounding factor) làm sai lệch phép đo biến thiên độ cứng theo áp suất trong các thí nghiệm tải chu kỳ của MP1 hay không?

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
