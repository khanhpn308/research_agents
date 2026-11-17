# WP-A-R1 Changelog — Scientific Reading Notes Remediation

- **TASK_ID:** `MP1-LR-P2-WP-A-R1`
- **ACTION:** `DEEPEN_EXISTING_PAPER_NOTES`
- **TARGET:** `WP_A_CONTENT_QUALITY_PASS`
- **TIMESTAMP:** 2026-10-15
- **SCOPE:** 7 Canonical Papers (M01, M02, M03, M04, M05, M38, M39) in Work Package A.

---

## 1. Executive Summary of Changes

| Artifact | Before Remediation | After Remediation | Rationale & Quality Gain |
|---|---|---|---|
| **7 Paper Notes (M01–M05, M38, M39)** | Generic 32-line templates with identical boilerplate text across all sections A–L; zero paper-specific mechanics analysis. | Fully rewritten, self-contained, paper-specific scientific reading notes (80–120+ lines each) with detailed evidence mapping. | Provides substantive academic context, mechanical models, and methodology to support human drafting of Chapters 1 and 2. |
| **23 Evidence Records (`EVIDENCE_RECORDS.jsonl`)** | 23/23 records had the identical boilerplate: `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."` | 23/23 records have customized, deep 5-point Vietnamese technical explanations addressing: (1) finding, (2) scientific/mechanical meaning, (3) conditions, (4) argumentative utility, (5) non-warranted claims. | Eliminates generic placeholders; establishes auditable scientific rigor for every extracted finding. |
| **Validation & Limitations (`EVIDENCE_RECORDS.jsonl`)** | 23/23 records had: `"Source scope retained; no MP1-specific validation inferred."` | 23/23 records feature tailored, source-specific physical and methodological limitations. | Prevents over-claiming and delineates the exact valid domain of each source. |
| **Bibliographic Metadata (`EVIDENCE_RECORDS.jsonl` & Notes)** | M39 was missing authors (`""`). M38 had title conflated into author string (`"Guide to the expression..."`). | M39 updated to `"Barry N. Taylor and Chris E. Kuyatt"`. M38 updated to `"Joint Committee for Guides in Metrology (JCGM/WG 1)"`. | Ensures full bibliographic compliance and citation auditability. |
| **Equation Registry (`EQUATION_REGISTRY.md`)** | 9-line locator table with zero mathematical content or symbols. | Comprehensive mathematical registry with LaTeX formulas, symbol definitions, physical units, mechanical significance, assumptions, and locators. | Directly enables mechanics comprehension of operational stiffness and uncertainty propagation. |
| **Figure/Table Registry (`FIGURE_TABLE_REGISTRY.md`)** | Minimal 9-line table. | Expanded registry with detailed conceptual descriptions and legacy locator cross-referencing. | Clarifies continuum architectures and jamming taxonomies. |
| **Locator & Typography Audit (`LOCATOR_ISSUES.md`)** | Brief 4-line note. | Exhaustive dual-page audit (physical vs. printed pages for M01–M39), M05 figure numbering resolution, and M04 equation typography note. | Resolves all pagination and typographical ambiguities without breaking existing verified locators. |
| **Terminology Notes (`TERMINOLOGY_NOTES.md`)** | 7-line bullet list. | Detailed conceptual reference defining continuum robotics, stiffness vs. modulus, jamming mechanisms, and metrological terminology. | Prevents conceptual conflation in thesis writing. |

---

## 2. Before / After Comparison for All 23 Evidence Records

### M01 — Feak & Swales (2009)

#### M01-E01 (PDF p. 3, Introduction / Contents)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Feak & Swales (2009) định nghĩa một bài tổng quan tài liệu (literature review) không phải danh mục tóm tắt rời rạc mà là một 'câu chuyện nghiên cứu' (research story) có cấu trúc, kết nối mạch lạc các công trình tiền nhiệm với bài toán nghiên cứu mới của chính tác giả.\n2. Ý nghĩa khoa học: Về mặt phương pháp luận học thuật, điều này nhấn mạnh việc thiết lập lãnh thổ nghiên cứu (establishing a territory), xác định khoảng trống (niche), và kết nối bằng chứng có mục đích thay vì liệt kê máy móc.\n3. Điều kiện xác lập: Khung phương pháp luận viết học thuật sau đại học trong khối ngành khoa học - kỹ thuật.\n4. Sử dụng cho lập luận: Hỗ trợ xây dựng cấu trúc luận văn cho C1.6 và C2.1, giải thích tính liên kết giữa các công trình tiền nhiệm về robot liên tục và cơ cấu biến đổi độ cứng với bài toán dầm layer jamming của MP1.\n5. Không thể kết luận: Không thể dùng để suy diễn bất kỳ tính chất cơ học, mô hình vật lý hay khẳng định tính mới (novelty) nào cho kết cấu layer jamming trong MP1."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Tài liệu phương pháp luận viết học thuật, không cung cấp dữ liệu cơ học thực nghiệm hay phương trình vật lý; phạm vi áp dụng giới hạn trong cấu trúc văn bản khoa học."`

#### M01-E02 (PDF p. 25, Getting Started on the Literature Review)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Tác giả nhấn mạnh tiêu chí lựa chọn tài liệu (selection criteria) phải được công bố rõ ràng và minh bạch để biên giới và phạm vi của tổng quan nghiên cứu có thể kiểm chứng được (auditable).\n2. Ý nghĩa khoa học: Đảm bảo tính lặp lại (reproducibility) và tính khách quan trong việc sàng lọc tài liệu, ngăn chặn việc lựa chọn thiên vị (cherry-picking) các bài báo chỉ ủng hộ giả thuyết ban đầu.\n3. Điều kiện xác lập: Hướng dẫn phương pháp luận chọn lọc và mô tả tài liệu nghiên cứu học thuật.\n4. Sử dụng cho lập luận: Củng cố cơ sở phương pháp luận cho C1.6.2 và C2.1 về quy trình sàng lọc corpus tài liệu trong đề tài (tiêu chí bao hàm và loại trừ minh bạch).\n5. Không thể kết luận: Tiêu chí lựa chọn tài liệu không chứng minh một cơ chế biến đổi độ cứng cụ thể là tối ưu hay một mô hình cơ học là hợp lệ."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Quy tắc kiểm soát phạm vi tổng quan văn bản; không thay thế được các tiêu chuẩn kiểm chứng mô hình cơ học độc lập."`

#### M01-E03 (PDF p. 93, Criteria for Evaluating Literature Reviews)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Chất lượng của một bài tổng quan được đánh giá thông qua tổ chức mạch lạc, độ bao phủ hợp lý của các hướng nghiên cứu liên quan, và sự liên kết rõ ràng với bài toán nghiên cứu đề xuất bằng ngôn ngữ của chính tác giả (paraphrasing và critical synthesizing).\n2. Ý nghĩa khoa học: Đặt ra chuẩn mực học thuật nhằm phân biệt giữa việc chỉ tóm tắt cơ học thuần túy (descriptive summary) với phân tích phản biện có luận điểm (critical synthesis).\n3. Điều kiện xác lập: Tiêu chuẩn đánh giá văn bản học thuật sau đại học.\n4. Sử dụng cho lập luận: Định hướng viết C1.6.3 và C2.6.3 trong việc tổng hợp phản biện các mô hình cơ học và thử nghiệm của các nghiên cứu trước.\n5. Không thể kết luận: Không cung cấp dữ liệu cơ học thực nghiệm hay phương trình giải tích nào cho robot hay cơ cấu làm cứng."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Tiêu chuẩn đánh giá văn phong và cấu trúc lập luận; không đại diện cho chuẩn đánh giá dung sai sai số đo lường hay độ tin cậy thực nghiệm."`

---

### M02 — Burgner-Kahrs, Rucker, and Choset (2015)

#### M02-E01 (PDF p. 1, Abstract / Introduction, Fig. 1)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Burgner-Kahrs, Rucker và Choset (2015) khảo sát robot liên tục y sinh có kết cấu uốn cong liên tục, độ mềm dẻo cấu trúc tự thân (inherent compliance), phù hợp di chuyển trong không gian hẹp và tương tác an toàn với mô sinh học.\n2. Ý nghĩa cơ học: Nhấn mạnh động cơ cơ học cốt lõi của robot liên tục: sự đánh đổi giữa khả năng biến dạng mềm uốn lượn để tiếp cận an toàn với khả năng chịu tải hoặc truyền lực khi thao tác phẫu thuật.\n3. Điều kiện xác lập: Bối cảnh tổng quan các thiết kế robot liên tục y tế (chủ yếu là concentric tubes, tendon-driven, fluidic).\n4. Sử dụng cho lập luận: Cung cấp bối cảnh ứng dụng và động cơ trực tiếp cho C1.1 và C2.2.1 về nhu cầu tích hợp cơ chế biến đổi độ cứng vào robot liên tục.\n5. Không thể kết luận: Không báo cáo số liệu độ cứng định lượng hay mô hình giải tích cụ thể cho cơ chế layer jamming (laminar jamming)."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Bài tổng quan phân loại vĩ mô các hệ thống robot y sinh; không cung cấp dữ liệu định lượng về lực cản uốn hay ứng suất tiếp xúc cục bộ của dầm nhiều lớp."`

#### M02-E02 (PDF p. 2, Section II-A Classification, Definition 1)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Định nghĩa 1 khẳng định robot liên tục là kết cấu có thể truyền động mà vật liệu cấu tạo tạo thành các đường cong liên tục thông qua biến dạng đàn hồi, tách biệt ranh giới với chuỗi khớp cứng rời rạc (discrete rigid links).\n2. Ý nghĩa cơ học: Xác lập nền tảng động học và cơ học: cấu hình thân robot là một đường cong khả vi liên tục trong không gian (vô hạn bậc tự do về mặt cơ học liên tục), khác biệt với không gian cấu hình hữu hạn của cánh tay robot khớp cứng.\n3. Điều kiện xác lập: Định nghĩa cơ sở (Definition 1) trong khung phân loại robot y sinh.\n4. Sử dụng cho lập luận: Hỗ trợ C1.1.1 và C2.2.1 khi định nghĩa phạm vi đối tượng kết cấu liên tục và lý do cần các mô hình cơ học môi trường liên tục (như dầm Euler-Bernoulli hoặc Cosserat rod).\n5. Không thể kết luận: Không chứng minh kết cấu liên tục không có biến dạng trượt (shear) hoặc trượt tiếp xúc giữa các lớp (interlayer slip); không mô hình hóa cơ chế khóa/trượt của jamming."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Định nghĩa động học và hình học định tính; không bao gồm các hiệu ứng phi tuyến tiếp xúc ma sát hay trượt tương đối giữa các lớp vật liệu."`

#### M02-E03 (PDF p. 3, Section II-B Structure, Fig. 2)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Phân loại kết cấu và phương thức truyền động của robot liên tục thành truyền động ngoại tại (extrinsic: dây kéo tendon, ống siêu đàn hồi NiTi lồng nhau) và truyền động nội tại (intrinsic: buồng áp suất khí nén/thủy lực).\n2. Ý nghĩa cơ học: Phân tích đường truyền lực và tải trọng tác dụng: truyền động ngoại tại tác dụng lực/mômen tập trung ở đầu mút hoặc các đốt; buồng khí tác dụng áp suất phân bố dọc thân; cả hai đều cần xương sống chịu nén hoặc cơ cấu chống xoắn.\n3. Điều kiện xác lập: Khảo sát phân loại cấu trúc hình thái của robot liên tục y sinh.\n4. Sử dụng cho lập luận: Cung cấp taxonomy cấu trúc cho C1.1.1 và C2.2.1, đối chiếu tải trọng đặt lên thân dầm khi tích hợp với cơ cấu jamming.\n5. Không thể kết luận: Không chứa đánh giá thực nghiệm hay định luật cấu lượng cho vật liệu có ma sát tiếp xúc hay dầm nhiều lớp (multi-layer beam)."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Phân loại phương thức truyền động ở cấp hệ thống; không mô hình hóa tương tác ma sát tiếp xúc cục bộ bên trong cấu trúc dầm nhiều lớp."`

---

### M03 — Russo et al. (2023)

#### M03-E01 (PDF p. 1, Abstract / Introduction, Fig. 1)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Russo et al. (2023) định nghĩa robot liên tục đặc trưng bởi một xương sống mềm dẻo có khả năng uốn cong liên tục, có tỷ số chiều dài trên đường kính lớn (L/D >> 1), hình dạng được điều khiển bằng tải truyền động nội tại hoặc ngoại tại.\n2. Ý nghĩa cơ học: Xác định đặc trưng hình học thanh mảnh dạng dầm/cột uốn của thân robot liên tục, biến dạng uốn là mode biến dạng chủ đạo.\n3. Điều kiện xác lập: Tổng quan toàn diện về thiết kế, mô hình hóa và điều khiển robot liên tục.\n4. Sử dụng cho lập luận: Cung cấp định nghĩa cơ học nền tảng cho C1.1.1 và C2.2.1 về hình học dạng thanh/dầm thanh mảnh chịu uốn.\n5. Không thể kết luận: Không giải quyết bài toán độ cứng thay đổi khi thân dầm được tạo thành từ nhiều lớp lá ép chân không."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Mô tả hình học và động học tổng quan của robot liên tục thanh mảnh; không mô hình hóa cơ chế khóa cứng hay ma sát tiếp xúc dầm nhiều lớp."`

#### M03-E02 (PDF p. 3 [printed pp. 2–3], Section 1.2 Modeling and Control, Table 1)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Khảo sát phân loại các mô hình cơ học theo phổ từ mô hình hình học giả định độ cong không đổi từng đoạn (PCC: piecewise constant curvature) đến mô hình cơ học thanh biến dạng phi tuyến hình học (Cosserat / Kirchhoff rod) và phần tử hữu hạn (FEM).\n2. Ý nghĩa cơ học: Làm rõ sự đánh đổi giữa chi phí tính toán (computational cost) và độ chính xác cơ học: PCC nhanh nhưng bỏ qua lực ngoại cảnh và biến thiên độ cong; Cosserat tính được tương tác lực-mômen nhưng phức tạp; FEM chính xác cục bộ nhưng quá nặng cho điều khiển thời gian thực.\n3. Điều kiện xác lập: Khảo sát lý thuyết mô hình hóa động học và cơ học robot liên tục.\n4. Sử dụng cho lập luận: Hỗ trợ C1.1.1 và C2.2.1 trong việc chọn cấp độ mô hình hóa phù hợp cho thân robot liên tục và đặt tiền đề cho các mô hình dầm tương đương trong C2.5.\n5. Không thể kết luận: Không mô hình hóa trạng thái tiếp xúc Coulomb hay hiện tượng trượt giữa các lá trong kết cấu layer jamming."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Khảo sát phổ mô hình dầm đơn thuần nhất; không tính đến hiện tượng trượt giữa các lớp vật liệu rời rạc trong kết cấu jamming."`

#### M03-E03 (PDF p. 4, Section 1.2 Modeling and Control)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Russo et al. chỉ ra các thách thức lớn còn tồn tại trong mô hình hóa và điều khiển: ma sát truyền động, biến dạng tiết diện, hiện tượng mất ổn định (bifurcation / buckling), tương tác tiếp xúc môi trường và sự phụ thuộc vào giả thiết hình học.\n2. Ý nghĩa cơ học: Thừa nhận giới hạn của các mô hình cơ học hiện tại: khi có phi tuyến vật liệu, ma sát và biến dạng cục bộ lớn, các mô hình giải tích đơn giản thường sai lệch đáng kể.\n3. Điều kiện xác lập: Đánh giá tổng quan về khoảng trống công nghệ và lý thuyết (open challenges).\n4. Sử dụng cho lập luận: Đóng vai trò phản biện (COUNTEREVIDENCE) trong C2.2.1 và C2.6.2, chứng minh rằng không thể áp dụng nguyên si các mô hình động học lý tưởng mà không xét đến ma sát và giới hạn miền kiểm chứng.\n5. Không thể kết luận: Không cung cấp dữ liệu định lượng cụ thể về sai số mô hình hay dữ liệu kiểm chứng cho layer jamming."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Báo cáo định tính về các thách thức mở; không lượng hóa biên độ sai số hoặc đề xuất định luật cấu lượng mới cho kết cấu dầm ghép lớp."`

---

### M04 — Lin, Song, and Wang (2024)

#### M04-E01 (PDF p. 1, Abstract / Introduction, Fig. 1)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Lin, Song, và Wang (2024) tổng quan các phương pháp biến đổi độ cứng cho robot mềm phẫu thuật xâm lấn tối thiểu (MIS), xuất phát từ mâu thuẫn cốt lõi: robot cần mềm để lách an toàn qua đường giải phẫu hẹp uốn lượn, nhưng cần cứng vững để truyền lực và giữ độ chính xác vị trí khi thao tác mô.\n2. Ý nghĩa cơ học: Đặt bài toán điều khiển độ cứng (tunable stiffness) vào trung tâm của thiết kế cơ khí robot mềm phẫu thuật.\n3. Điều kiện xác lập: Bối cảnh phẫu thuật nội soi qua lỗ tự nhiên (NOTES) và đa cổng (multi-port MIS).\n4. Sử dụng cho lập luận: Cung cấp bối cảnh ứng dụng và động cơ cơ học rõ rệt cho C1.1.1, C1.1.3, C2.3.1.\n5. Không thể kết luận: Không chứng minh cơ chế ma sát jamming là phương pháp tối ưu tuyệt đối so với các vật liệu biến pha (SMP, LMPA) hay thủy động lực học."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Tổng quan định tính về nhu cầu lâm sàng; không cung cấp mô hình giải tích phân bố ứng suất hay số liệu kiểm chứng độc lập cho layer jamming."`

#### M04-E02 (PDF p. 2, Section 1.2, Fig. 2(a–d), Eqs. 1–4)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Bài tổng quan hệ thống hóa 4 phương pháp tính toán độ cứng hoạt động của robot mềm: độ cứng thẳng tại đầu mút, độ cứng xoay quanh trục/gốc, độ cứng theo uốn dầm tựa 2 đầu (three-point bending: EI = F*L^3/(48*Delta_w)), và độ cứng theo uốn dầm ngàm cantilever (EI = F*L^3/(3*Delta_w)).\n2. Ý nghĩa cơ học: Xác lập rõ ràng rằng giá trị độ cứng đo được (K hoặc EI) phụ thuộc trực tiếp vào điều kiện biên (boundary conditions), cấu hình hình học (L), điểm đặt tải và định nghĩa vận hành; không thể so sánh số tuyệt đối giữa các sơ đồ tải khác nhau.\n3. Điều kiện xác lập: Giả thiết dầm đàn hồi tuyến tính Euler-Bernoulli, biến dạng nhỏ, tải tĩnh hoặc bán tĩnh.\n4. Sử dụng cho lập luận: Đóng vai trò bằng chứng cốt lõi (PRIMARY_EVIDENCE) cho C1.1.3, C2.3.1 và C2.5 để phân loại các phương pháp đo độ cứng và cảnh báo sự không đồng nhất thứ nguyên giữa các định nghĩa.\n5. Không thể kết luận: Không áp dụng trực tiếp được khi dầm có hiện tượng trượt liên lớp (interlayer slip) gây phi tuyến tải-chuyển vị hoặc khi vật liệu có tính nhớt đàn hồi."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Giới hạn trong lý thuyết dầm đàn hồi tuyến tính Euler-Bernoulli biến dạng nhỏ; không tính đến trượt tiếp xúc ma sát phi tuyến, hiệu ứng cắt hay biến dạng màng bao."`

#### M04-E03 (PDF p. 3, Section 1.2, Table 1)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Nhắc nhở người đọc rằng các giá trị độ cứng trong các nghiên cứu khác nhau có thể mang thứ nguyên khác nhau (N/m, N*m/rad, hoặc N*m^2), do đó không thể hoán đổi trực tiếp; đề xuất tỉ số điều chỉnh độ cứng R = K_max/K_min như một tham số không thứ nguyên để so sánh tương đối.\n2. Ý nghĩa phương pháp: Cảnh báo phương pháp luận sâu sắc: việc báo cáo 'độ cứng tăng X lần' hoặc giá trị độ cứng tuyệt đối dễ gây hiểu lầm nghiêm trọng nếu không chuẩn hóa điều kiện biên, sơ đồ tải và thứ nguyên.\n3. Điều kiện xác lập: Tổng hợp so sánh chéo giữa hàng chục nghiên cứu robot biến đổi độ cứng.\n4. Sử dụng cho lập luận: Bằng chứng phản biện (COUNTEREVIDENCE / METHODOLOGY) quan trọng cho C1.1.3 và C2.3.1 để kiểm soát tính hợp lệ khi so sánh độ cứng giữa các công trình trong Chương 1-2.\n5. Không thể kết luận: Tỉ số K_max/K_min không phản ánh giá trị độ cứng tuyệt đối và không phản ánh tổn hao năng lượng (hysteresis loop) trong chu trình chịu tải."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Cảnh báo phương pháp luận về so sánh độ cứng; tỉ số R phụ thuộc điều kiện đo và không thể hiện độ trễ cơ học (hysteresis) hay độ cứng tuyệt đối."`

---

### M05 — Fan et al. (2024)

#### M05-E01 (PDF p. 1, Abstract / Introduction)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Fan, Yi và Liu (2024) khảo sát toàn diện các phương pháp làm cứng cho robot liên tục, khẳng định thiếu độ cứng (insufficient stiffness) là nhược điểm chí mạng của robot liên tục vốn được thiết kế tối ưu cho tính mềm dẻo.\n2. Ý nghĩa cơ học: Làm rõ yêu cầu phải tích hợp các kỹ thuật làm cứng vào cả cấu trúc cơ khí lẫn phương thức truyền động của robot liên tục.\n3. Điều kiện xác lập: Tổng quan các cơ cấu làm cứng trong robot liên tục (antagonism, thermally responsive materials, jamming, mechanical structures).\n4. Sử dụng cho lập luận: Cung cấp bối cảnh và động cơ kỹ thuật cho C1.1, C1.1.3 và C2.3.1.\n5. Không thể kết luận: Không đề xuất phương trình cơ học giải tích mới cho từng cơ cấu cụ thể mà chỉ tổng hợp phân loại tài liệu."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Tổng quan phân loại diện rộng; không cung cấp mô hình giải tích chi tiết hay dữ liệu thực nghiệm gốc cho cơ chế khóa dầm layer jamming."`

#### M05-E02 (PDF p. 10, Section 3.3.1 Fibre/filament jamming, Fig. 5g, Table 4)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Fibre/filament jamming (FJ) được xếp vào phân nhóm cơ cấu jamming dựa trên ma sát giữa các sợi hoặc bó sợi xếp song song dọc trục bọc trong màng kín khí; độ cứng thay đổi khi hút chân không ép các sợi vào nhau.\n2. Ý nghĩa cơ học: Phân biệt rõ ràng hình thái hình học sợi 1D (fibres: chịu ma sát tiếp xúc mặt cong, tương tác dọc trục) với hạt 0D (grains) và tấm mỏng 2D (layers/sheets).\n3. Điều kiện xác lập: Bối cảnh phân loại cơ cấu jamming trong robot liên tục y tế và công nghiệp.\n4. Sử dụng cho lập luận: Hỗ trợ C1.1.3, C2.3.1 trong việc xây dựng taxonomy các cơ cấu jamming và phân tích ưu nhược điểm của hình thái sợi so với tấm.\n5. Không thể kết luận: Không cung cấp mô hình cơ học vi mô về phân bố lực ép và lực ma sát cục bộ giữa các sợi khi uốn cong."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Phân loại cơ cấu ở cấp độ hình thái học; không cung cấp mô hình phân bố lực nén pháp tuyến hay lực ma sát tiếp xúc giữa các sợi."`

#### M05-E03 (PDF p. 11, Section 3.3.3 Layer/laminar jamming, Fig. 5e, f, Table 4)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Layer/laminar jamming (LJ) được phân loại thành nhánh cơ cấu riêng biệt sử dụng các tấm/lá mỏng xếp chồng (flaps/sheets); nguồn khảo sát các ứng dụng nhưng không thiết lập mô hình chuyển đổi từ áp suất buồng hút sang phân bố ứng suất pháp tuyến tiếp xúc cục bộ (local normal traction).\n2. Ý nghĩa cơ học: Xác nhận rằng các bài tổng quan rộng chỉ phân loại LJ ở mức độ cấu trúc vĩ mô, để lại khoảng trống quan trọng về cơ học tiếp xúc cục bộ và mô hình giải tích chi tiết cho các nghiên cứu chuyên sâu.\n3. Điều kiện xác lập: Tổng hợp tài liệu trong bài báo review.\n4. Sử dụng cho lập luận: Đóng vai trò bằng chứng phản biện/khoảng trống (COUNTEREVIDENCE) cho C2.3.1 và C2.5.5, chứng minh các khảo sát tổng quan không cung cấp mô hình trường ứng suất tiếp xúc cục bộ.\n5. Không thể kết luận: Không phủ định sự tồn tại của các mô hình cơ học trong các bài báo nghiên cứu gốc riêng lẻ (như Narang et al., Caruso et al.)."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Thiếu mô hình liên hệ giữa áp suất buồng chân không và phân bố ứng suất tiếp xúc cục bộ; bài review chỉ tổng hợp các hình thái ứng dụng."`

---

### M38 — JCGM 100:2008 / GUM

#### M38-E01 (Printed p. 1 / Physical PDF p. 13, Section 1 Scope)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: JCGM 100:2008 (GUM) cung cấp các quy tắc chuẩn mực quốc tế chung để đánh giá và biểu diễn độ không đảm bảo đo (uncertainty of measurement) trên phạm vi rộng các cấp độ chính xác từ đo lường cơ bản đến kỹ thuật công nghiệp.\n2. Ý nghĩa phương pháp: Thiết lập nguyên tắc khoa học rằng mọi kết quả đo lường thực nghiệm đều không hoàn chỉnh nếu thiếu một công bố định lượng về độ không đảm bảo đo đi kèm.\n3. Điều kiện xác lập: Tiêu chuẩn hướng dẫn đo lường quốc tế được bảo trợ bởi BIPM, IEC, IFCC, ILAC, ISO, IUPAC, IUPAP, OIML.\n4. Sử dụng cho lập luận: Làm nền tảng phương pháp luận chuẩn tắc cho C1.6.3 và C2.5.4 khi thiết kế và báo cáo các phép đo thực nghiệm cơ học (lực, chuyển vị, áp suất, độ cứng).\n5. Không thể kết luận: GUM không ấn định cụ thể loại cảm biến hay giá trị độ không đảm bảo đo mục tiêu cho thiết bị thử nghiệm uốn dầm trong MP1."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Khung hướng dẫn đo lường tổng quát; không quy định cụ thể thông số kỹ thuật hay giới hạn dung sai cho cảm biến trong thí nghiệm cơ học robot mềm."`

#### M38-E02 (Printed p. 8 / Physical PDF p. 20, Section 4.1, Eqs. 1–5)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Đại lượng đo (measurand) Y trong hầu hết trường hợp không được đo trực tiếp mà được xác định từ N đại lượng đầu vào X_1, ..., X_N thông qua hàm chức năng Y = f(X_1, ..., X_N); kết quả đo y = f(x_1, ..., x_N) đòi hỏi phải nhận diện đầy đủ các đầu vào và độ không đảm bảo chuẩn u(x_i).\n2. Ý nghĩa cơ học: Cung cấp mô hình toán học đo lường (measurement model). Trong cơ học, độ cứng K không phải đại lượng đo trực tiếp mà là đại lượng suy ra từ hàm của lực, độ võng, chiều dài dầm (K = f(F, Delta_w, L)), do đó độ không đảm bảo của K phụ thuộc vào việc lan truyền sai số từ các đại lượng đo trực tiếp này.\n3. Điều kiện xác lập: Khung lý thuyết hàm đo lường tổng quát trong GUM.\n4. Sử dụng cho lập luận: Làm bằng chứng cơ sở (PRIMARY_EVIDENCE) cho C2.5.4 để xây dựng mô hình đo lường cho các phép đo độ cứng và kiểm định mô hình.\n5. Không thể kết luận: Hàm f không tự động tuyến tính; nếu hàm có phi tuyến mạnh thì phép xấp xỉ tuyến tính bậc một có thể không đủ."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Giả định hàm đo lường f chứa đầy đủ mọi đại lượng ảnh hưởng và hiệu chỉnh; không tự động bù trừ các sai số mô hình vật lý chưa được nhận diện."`
- **`bibliographic_identity`:**
  - *Before:* `{"title": "Evaluation of measurement data", "authors": "Guide to the expression of uncertainty in measurement* (JCGM 100:2008)", "year": 2008, "doi_or_identifier": "N/A — hướng dẫn đo lường"}`
  - *After:* `{"title": "Evaluation of measurement data", "authors": "Joint Committee for Guides in Metrology (JCGM/WG 1)", "year": 2008, "doi_or_identifier": "JCGM 100:2008 / GUM 1995 with minor corrections"}`

#### M38-E03 (Printed p. 18 / Physical PDF p. 30, Section 5, Eqs. 10–13)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Độ không đảm bảo chuẩn kết hợp u_c(y) được tính bằng cách khai căn tổng phương sai: nếu các đại lượng đầu vào độc lập, đóng góp qua hệ số độ nhạy c_i = partial f / partial x_i (Eq. 10); nếu các đầu vào có tương quan, bắt buộc phải cộng thêm các số hạng hiệp phương sai (covariance terms u(x_i, x_j)) (Eq. 13).\n2. Ý nghĩa cơ học: Quy luật lan truyền độ không đảm bảo đo (law of propagation of uncertainty): bỏ qua hiệp phương sai giữa các biến đo (ví dụ lực và chuyển vị đo từ cùng một hệ thống có chung độ dơ cơ khí hoặc phụ thuộc nhiệt độ) sẽ dẫn đến đánh giá sai lệch độ không đảm bảo của độ cứng.\n3. Điều kiện xác lập: Xấp xỉ chuỗi Taylor bậc một (first-order Taylor series approximation) của hàm Y = f(X_1, ..., X_N).\n4. Sử dụng cho lập luận: Bằng chứng cốt lõi (PRIMARY_EVIDENCE) cho C1.6.3 và C2.5.4 để giải thích cách lan truyền sai số từ cảm biến lực và cảm biến chuyển vị vào giá trị độ cứng.\n5. Không thể kết luận: Công thức xấp xỉ bậc một không xét đến số hạng bậc cao nếu các đạo hàm bậc hai partial^2 f / partial x_i partial x_j lớn hoặc khi sai số đầu vào lớn."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Dựa trên xấp xỉ chuỗi Taylor bậc một; khi hàm đo lường phi tuyến mạnh hoặc độ không đảm bảo đầu vào lớn, cần bổ sung số hạng bậc hai hoặc mô phỏng Monte Carlo."`
- **`bibliographic_identity`:**
  - *Before:* `{"title": "Evaluation of measurement data", "authors": "Guide to the expression of uncertainty in measurement* (JCGM 100:2008)", "year": 2008, "doi_or_identifier": "N/A — hướng dẫn đo lường"}`
  - *After:* `{"title": "Evaluation of measurement data", "authors": "Joint Committee for Guides in Metrology (JCGM/WG 1)", "year": 2008, "doi_or_identifier": "JCGM 100:2008 / GUM 1995 with minor corrections"}`

#### M38-E04 (Printed p. 23 / Physical PDF p. 35, Section 6, Sec. 6.2–6.3)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Độ không đảm bảo mở rộng U = k * u_c(y) cung cấp một khoảng chứa phần lớn các giá trị có thể có của đại lượng đo; việc công bố U bắt buộc phải ghi rõ hệ số phủ k (thường chọn k=2 cho mức độ tin cậy xấp xỉ 95% khi phân bố chuẩn) và quy ước báo cáo đầy đủ.\n2. Ý nghĩa phương pháp: Đảm bảo tính minh bạch và khả năng tái lập: một công bố Y = y +- U là vô nghĩa nếu không nói rõ k hoặc mức độ tin cậy tương ứng.\n3. Điều kiện xác lập: Quy tắc biểu diễn độ không đảm bảo mở rộng dựa trên phân bố xấp xỉ chuẩn (định lý giới hạn trung tâm) hoặc phân bố Student t.\n4. Sử dụng cho lập luận: Hướng dẫn phương pháp luận (METHODOLOGY_SOURCE) cho C1.6.3 và C2.5.4 về chuẩn mực trình bày sai số thực nghiệm trong luận văn.\n5. Không thể kết luận: Hệ số k=2 chỉ tương ứng với khoảng tin cậy 95% khi phân bố đầu ra là chuẩn và bậc tự do hữu hiệu đủ lớn (theo công thức Welch-Satterthwaite); không tự tiện coi U là giới hạn dung sai tuyệt đối."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Hệ số k=2 chỉ đảm bảo mức tin cậy 95% khi phân bố xác suất đầu ra tiệm cận chuẩn và bậc tự do hiệu dụng đủ lớn; không áp dụng cho phân bố có đuôi nặng hoặc bị chặn lệch."`
- **`bibliographic_identity`:**
  - *Before:* `{"title": "Evaluation of measurement data", "authors": "Guide to the expression of uncertainty in measurement* (JCGM 100:2008)", "year": 2008, "doi_or_identifier": "N/A — hướng dẫn đo lường"}`
  - *After:* `{"title": "Evaluation of measurement data", "authors": "Joint Committee for Guides in Metrology (JCGM/WG 1)", "year": 2008, "doi_or_identifier": "JCGM 100:2008 / GUM 1995 with minor corrections"}`

---

### M39 — Taylor & Kuyatt (1994 / NIST TN 1297)

#### M39-E01 (Printed p. 1 / Physical PDF p. 5, Section 1 Introduction)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Hướng dẫn của NIST (TN 1297, Taylor & Kuyatt 1994) khẳng định kết quả của một phép đo chỉ là một xấp xỉ hoặc ước lượng về giá trị thực của đại lượng đo; nó chỉ hoàn chỉnh khi đi kèm một công bố định lượng về độ không đảm bảo đo.\n2. Ý nghĩa phương pháp: Phản ánh lập trường khoa học nghiêm ngặt: không có phép đo nào 'hoàn hảo' hoặc 'chính xác tuyệt đối'; tính tin cậy của dữ liệu thực nghiệm phụ thuộc vào việc định lượng độ không đảm bảo.\n3. Điều kiện xác lập: Hướng dẫn chính thức của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST).\n4. Sử dụng cho lập luận: Nguồn phương pháp luận chuẩn tắc (METHODOLOGY_SOURCE) cho C1.6.3 và C2.5.4.\n5. Không thể kết luận: Không cung cấp quy trình hiệu chuẩn riêng cho cảm biến áp suất hay lực của một giàn thí nghiệm cụ thể trong MP1."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Nguyên lý triết lý đo lường của NIST; không cung cấp số liệu sai số định lượng cụ thể cho thiết bị thử nghiệm cơ học uốn dầm."`
- **`bibliographic_identity`:**
  - *Before:* `{"title": "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results* (NIST Technical Note 1297)", "authors": "", "year": 1994, "doi_or_identifier": "N/A — technical note"}`
  - *After:* `{"title": "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results", "authors": "Barry N. Taylor and Chris E. Kuyatt", "year": 1994, "doi_or_identifier": "NIST Technical Note 1297 (NIST TN 1297)"}`

#### M39-E02 (Printed p. 1 / Physical PDF p. 6, Section 2 Classification of components)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Các thành phần độ không đảm bảo đo được phân loại thành Type A (đánh giá bằng các phương pháp thống kê trên chuỗi quan sát lặp lại) và Type B (đánh giá bằng các phương pháp phi thống kê dựa trên thông tin sẵn có); hai loại này dựa trên phương pháp đánh giá chứ không đồng nhất với khái niệm lỗi ngẫu nhiên (random) và lỗi hệ thống (systematic).\n2. Ý nghĩa phương pháp: Tránh nhầm lẫn cơ bản trong thực nghiệm kỹ thuật: một sai số hệ thống đã biết (như độ lệch zero) phải được hiệu chỉnh; còn độ không đảm bảo về giá trị hiệu chỉnh đó có thể được đánh giá theo Type A hoặc Type B.\n3. Điều kiện xác lập: Phân loại chuẩn hóa của NIST/GUM.\n4. Sử dụng cho lập luận: Cung cấp khung phân loại phương pháp luận (METHODOLOGY_SOURCE) cho C1.6.3 và C2.5.4 để tách bạch rõ các nguồn sai số khi đo biến dạng, áp suất và lực.\n5. Không thể kết luận: Phân loại Type A hay Type B không chỉ ra loại nào 'chính xác hơn' hay 'đáng tin hơn'; cả hai đều được quy về độ lệch chuẩn ước lượng u_i."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Phân loại phương pháp đánh giá (thống kê vs phi thống kê); không giải quyết bản chất cơ học của các nguồn nhiễu vật lý trong thí nghiệm."`
- **`bibliographic_identity`:**
  - *Before:* `{"title": "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results* (NIST Technical Note 1297)", "authors": "", "year": 1994, "doi_or_identifier": "N/A — technical note"}`
  - *After:* `{"title": "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results", "authors": "Barry N. Taylor and Chris E. Kuyatt", "year": 1994, "doi_or_identifier": "NIST Technical Note 1297 (NIST TN 1297)"}`

#### M39-E03 (Printed pp. 3–4 / Physical PDF p. 7, Section 4.1–4.6 Type B evaluation)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Đánh giá Type B dựa trên suy đoán khoa học sử dụng mọi thông tin liên quan (chứng chỉ hiệu chuẩn, catalog nhà sản xuất, dữ liệu quá khứ, sổ tay kỹ thuật); khi chỉ biết cận trên và cận dưới (+- a), phải giả định một hàm phân bố xác suất (như phân bố đều rectangular: u = a/sqrt(3), hoặc phân bố tam giác triangular: u = a/sqrt(6)) để quy đổi về độ không đảm bảo chuẩn.\n2. Ý nghĩa cơ học: Cung cấp cơ sở toán học tường minh để lượng hóa các sai số từ tài liệu thiết bị (datasheet resolution, sensor accuracy class) mà không cần lặp lại hàng trăm phép đo thống kê.\n3. Điều kiện xác lập: Đánh giá thành phần độ không đảm bảo đo khi không có chuỗi quan sát lặp lại đầy đủ.\n4. Sử dụng cho lập luận: Nguồn phương pháp luận quan trọng (METHODOLOGY_SOURCE) cho C1.6.3 và C2.5.4 để tính độ không đảm bảo của cảm biến áp suất, loadcell, và thước đo chuyển vị từ thông số nhà sản xuất.\n5. Không thể kết luận: Việc chọn phân bố đều hay tam giác phải có cơ sở vật lý; không được tùy tiện áp đặt phân bố đều nếu có thông tin cho thấy giá trị tập trung ở tâm."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Phụ thuộc vào nhận định khoa học và độ tin cậy của tài liệu nhà sản xuất; giả định phân bố chữ nhật có thể đánh giá quá cao hoặc quá thấp độ phân tán thực tế."`
- **`bibliographic_identity`:**
  - *Before:* `{"title": "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results* (NIST Technical Note 1297)", "authors": "", "year": 1994, "doi_or_identifier": "N/A — technical note"}`
  - *After:* `{"title": "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results", "authors": "Barry N. Taylor and Chris E. Kuyatt", "year": 1994, "doi_or_identifier": "NIST Technical Note 1297 (NIST TN 1297)"}`

#### M39-E04 (Printed p. 6 / Physical PDF p. 10, Section 5.3 Combined standard uncertainty)
- **`vietnamese_technical_explanation`:**
  - *Before:* `"Bằng chứng được đối chiếu toàn văn tại trang PDF nêu trên; không mở rộng ngoài điều kiện nguồn."`
  - *After:* `"1. Kết quả: Độ không đảm bảo chuẩn kết hợp u_c chỉ đơn thuần là độ lệch chuẩn ước lượng của kết quả đo; nó không được tự động xem là một khoảng tin cậy (confidence interval) nếu không có các giả thiết thống kê cụ thể về phân bố xác suất của đại lượng đầu ra.\n2. Ý nghĩa phương pháp: Cảnh báo phản biện quan trọng: việc nhầm lẫn u_c (độ rộng +- 1 sigma) với khoảng tin cậy 95% sẽ dẫn đến đánh giá quá lạc quan về độ chính xác của kết quả đo; muốn có khoảng tin cậy phải xác lập phân bố và dùng độ không đảm bảo mở rộng U.\n3. Điều kiện xác lập: Nguyên tắc báo cáo độ không đảm bảo đo chuẩn của NIST/CIPM.\n4. Sử dụng cho lập luận: Đóng vai trò bằng chứng phản biện (COUNTEREVIDENCE) trong C1.6.3 và C2.5.4 để ngăn ngừa việc ngộ nhận hoặc báo cáo sai lệch khoảng tin cậy khi trình bày sai số thực nghiệm độ cứng.\n5. Không thể kết luận: Không phủ định giá trị của u_c trong các báo cáo so sánh cơ sở chuẩn hoặc nghiên cứu đo lường gốc."`
- **`validation_and_limitations.limitations`:**
  - *Before:* `"Source scope retained; no MP1-specific validation inferred."`
  - *After:* `"Quy tắc báo cáo kết quả; u_c không đại diện cho mức tin cậy 95% nếu không nhân với hệ số phủ k phù hợp với phân bố thực tế."`
- **`bibliographic_identity`:**
  - *Before:* `{"title": "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results* (NIST Technical Note 1297)", "authors": "", "year": 1994, "doi_or_identifier": "N/A — technical note"}`
  - *After:* `{"title": "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results", "authors": "Barry N. Taylor and Chris E. Kuyatt", "year": 1994, "doi_or_identifier": "NIST Technical Note 1297 (NIST TN 1297)"}`
