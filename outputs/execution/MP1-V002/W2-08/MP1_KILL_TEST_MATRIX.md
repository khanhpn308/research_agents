# Ma trận Kiểm toán Cổng Giết K1–K9 (MP1 Kill-Test Matrix)

> **Tệp chính tắc:** `MP1_KILL_TEST_MATRIX.json`  
> **Tổng số bài kiểm tra:** 9 bài kiểm toán (K1 đến K9)  
> **Nguyên tắc cốt lõi:** KHÔNG BẢO VỆ Ý TƯỞNG; TÌM CÁCH BÁC BỎ BẰNG VĂN HIẾN VÀ CƠ HỌC TIỀN NHIỆM GẦN NHẤT.

## 1. Bảng Tổng hợp Kết quả 9 Bài Kiểm toán Cổng Giết

| Mã Bài kiểm (ID) | Phán quyết (Verdict) | Khóa Ứng viên? | Cần Người duyệt? | Trạng thái Bằng chứng | Độ tin cậy | Câu hỏi Kiểm toán Khoa học |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **K1** | `PARTIAL_OVERLAP` | **CÓ (BLOCKING)** | **CẦN DUYỆT** | `coexistence_domain_bounded` | `high` | Liệu có tồn tại một miền vận hành thực nghiệm khả thi mà ở đó hiện tượ... |
| **K2** | `UNRESOLVED` | **CÓ (BLOCKING)** | **CẦN DUYỆT** | `h0b_not_falsified_competitor_live` | `high` | Liệu một mô hình NiTi phi tuyến chuyển pha hiện hữu đã được hiệu chuẩn... |
| **K3** | `UNRESOLVED` | **CÓ (BLOCKING)** | **CẦN DUYỆT** | `macroscopic_killed_local_unresolved` | `high` | Liệu phương án thực nghiệm đề xuất có thể phân biệt độc lập và đơn nhấ... |
| **K4** | `PARTIAL_OVERLAP` | **CÓ (BLOCKING)** | **CẦN DUYỆT** | `architectural_contribution_collapsed_mechanics_narrowed` | `high` | Liệu đóng góp còn sống sót của đề tài có bị sụp đổ về khẳng định tầm t... |
| **K5** | `NO_KILL_FOUND` | KHÔNG | **CẦN DUYỆT** | `no_identical_paper_in_canonical_set` | `high` | Liệu cơ sở dữ liệu bằng chứng lưu trữ và văn hiến lân cận đã chứa đựng... |
| **K6** | `UNRESOLVED` | **CÓ (BLOCKING)** | **CẦN DUYỆT** | `pressure_mapping_uncertainty_identified` | `high` | Liệu áp suất chủ động có phải là một biến số cơ học độc lập thực sự, h... |
| **K7** | `UNRESOLVED` | **CÓ (BLOCKING)** | **CẦN DUYỆT** | `existing_formulation_plausibility_high` | `high` | Liệu các mô hình cáp dây, tao dây và cơ học tiếp xúc ma sát hiện hữu t... |
| **K8** | `PARTIAL_OVERLAP` | **CÓ (BLOCKING)** | **CẦN DUYỆT** | `locked_calibration_rule_mandated_pending_data` | `high` | Các tham số của mô hình có được đo lường độc lập và khóa chặt trước kh... |
| **K9** | `UNRESOLVED` | **CÓ (BLOCKING)** | **CẦN DUYỆT** | `hysteresis_definitions_formalized_observability_unresolved` | `high` | Liệu sự thay đổi độ cứng và trễ năng lượng có thể được quy kết một các... |

## 2. Chi tiết Toàn văn 9 Bài Kiểm toán Cổng Giết

### Bài Kiểm toán K1: Liệu có tồn tại một miền vận hành thực nghiệm khả thi mà ở đ...
- **Phán quyết:** `PARTIAL_OVERLAP` | **Khóa ứng viên:** `True` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Liệu có tồn tại một miền vận hành thực nghiệm khả thi mà ở đó hiện tượng trượt ma sát giữa các dây (inter-wire slip) VÀ chuyển pha Martensite cảm ứng ứng suất của NiTi đồng thời xảy ra và ảnh hưởng trọng yếu đến đáp ứng cơ học?
- **Điều kiện loại bỏ (Kill Condition):** Không tồn tại miền cùng tồn tại khả thi trong thực nghiệm, hoặc sự cùng tồn tại quá yếu ớt/cục bộ không thể nhận diện được, dẫn đến cơ cấu bị thoái hóa về dầm kẹt dây đàn hồi thông thường hoặc dầm siêu đàn hồi liền khối.
- **Khẳng định & Mục tiêu liên quan:** Claims: C7 | Targets: T3 | Hypotheses: H0b, H1
- **Phương pháp & Bằng chứng thực tế:** Phân tích cơ học dầm nhiều sợi liên hợp: So sánh độ cong bắt đầu trượt kappa_slip = 2 mu p / (E A h) với độ cong bắt đầu chuyển pha kappa_tr = 2 sigma_tr / (E_A D_bundle); đối soát với biến dạng vận hành thực tế của robot mềm.
- **Kết quả quan sát:** Ở biến dạng uốn nhỏ epsilon < 0.75% (độ cong nhỏ thường gặp trong tay gắp mềm), NiTi hoàn toàn ở pha đàn hồi Austenite (E_A ~ 60 GPa); chuyển pha không kích hoạt, bài toán sụp đổ về kẹt dây đàn hồi H0a. Chuyển pha và trượt chỉ cùng kích hoạt khi dầm bị uốn cong sâu vượt quá kappa_tr hoặc khi có lực kéo căng dọc trục đáng kể.
- **Điều đã xác lập:** Xác lập rằng miền cùng tồn tại chỉ có thể tiếp cận được trong thực nghiệm ở chế độ biến dạng uốn góc lớn hoặc có tải kéo phụ trợ; không tồn tại sự cùng tồn tại phổ quát ở mọi dải uốn.
- **Điều chưa xác lập:** Chưa có thực nghiệm kiểm chứng độ bền mỏi chu kỳ thấp và độ bền màng bao của bó dây khi vận hành liên tục trong miền uốn sâu này.
- **Bất định còn lại:** Khả năng phân bố chuyển pha không đồng đều xuyên tâm: sợi ngoài cùng chuyển pha nhưng sợi bên trong vẫn thuần đàn hồi.
- **Trạng thái & Độ tin cậy:** `coexistence_domain_bounded` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G03, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W06_T3_TRANSFORMATION_SLIP_COEXISTENCE.md`

---
### Bài Kiểm toán K2: Liệu một mô hình NiTi phi tuyến chuyển pha hiện hữu đã được ...
- **Phán quyết:** `UNRESOLVED` | **Khóa ứng viên:** `True` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Liệu một mô hình NiTi phi tuyến chuyển pha hiện hữu đã được hiệu chuẩn độc lập kết hợp với cơ học tiếp xúc/ma sát Coulomb thông thường (H0b) có thể dự đoán đầy đủ đáp ứng cơ học của bó dây hay không?
- **Điều kiện loại bỏ (Kill Condition):** Khung lý thuyết H0b (mô hình phần tử hữu hạn thương mại hoặc mô hình sợi phi tuyến có sẵn) dự đoán được đáp ứng phụ thuộc áp suất trong phạm vi sai số đo đạc khai báo, khiến giả thuyết H1 (luật ghép cặp vi mô mới) không còn cơ sở tồn tại.
- **Khẳng định & Mục tiêu liên quan:** Claims: C7 | Targets: T3 | Hypotheses: H0b, H1
- **Phương pháp & Bằng chứng thực tế:** Đối soát năng lực mô hình hóa của UMAT Vahidi 2022 và mô hình vĩ mô Fang 2019; kiểm tra xem có hiện tượng vật lý nào trong uốn bó dây mà H0b về mặt toán học không thể biểu diễn được hay không.
- **Kết quả quan sát:** H0b chưa từng bị bác bỏ trong bất kỳ tài liệu nào của repository. Các mô hình phần tử hữu hạn hiện hữu có đầy đủ khả năng biểu diễn sự biến thiên độ cứng và trễ tiếp xúc. Bằng chứng hiện tại hoàn toàn chưa đủ (INSUFFICIENT) để chứng minh H0b thất bại hay H1 là cần thiết.
- **Điều đã xác lập:** H0a (mô-đun đàn hồi hằng số) đã bị bác bỏ hoàn toàn; H0b là đối thủ cạnh tranh trực tiếp còn sống sót và có độ tin cậy khoa học cao.
- **Điều chưa xác lập:** Chưa có kết quả chạy mô phỏng đối chứng số trị hoặc thực nghiệm đo lường trực tiếp để chứng minh giới hạn thất bại của H0b.
- **Bất định còn lại:** Rất cao: H0b có thể hoàn toàn đủ để giải quyết bài toán mà không cần phát minh lý thuyết mới.
- **Trạng thái & Độ tin cậy:** `h0b_not_falsified_competitor_live` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#Section5, outputs/execution/MP1-V002/W2-03/MP1_PARAMETER_SUBSTITUTION_RECONSTRUCTION.json`

---
### Bài Kiểm toán K3: Liệu phương án thực nghiệm đề xuất có thể phân biệt độc lập ...
- **Phán quyết:** `UNRESOLVED` | **Khóa ứng viên:** `True` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Liệu phương án thực nghiệm đề xuất có thể phân biệt độc lập và đơn nhất giữa ma sát trượt, chuyển pha, tái phân bố tiếp xúc, biến dạng nhiệt, biến dạng dư ban đầu, hình học và lịch sử chu kỳ hay không?
- **Điều kiện loại bỏ (Kill Condition):** Nhiều cơ chế vật lý khác nhau vẫn đồng dạng quan sát (observationally equivalent) trong phạm vi độ không đảm bảo đo; đường cong mô-men - độ cong vĩ mô M - kappa không thể phân tách cơ chế.
- **Khẳng định & Mục tiêu liên quan:** Claims: C7 | Targets: T3 | Hypotheses: H1
- **Phương pháp & Bằng chứng thực tế:** Phân tích khả năng nhận diện thực nghiệm (Identifiability Analysis): Kiểm tra tính duy nhất của việc giải bài toán ngược (inverse problem) từ dữ liệu thực nghiệm để truy nguyên các thông số cấu thành.
- **Kết quả quan sát:** Đo đạc vĩ mô thuần túy (M - kappa hoặc F - delta) bị KILL hoàn toàn vì hiện tượng mềm hóa vĩ mô bị gây ra bởi nhiều cơ chế tích hợp. Khả năng nhận diện chỉ có thể cứu vãn được nếu triển khai thành công hệ thống cảm biến cục bộ đa kênh (DIC + FBG + IR).
- **Điều đã xác lập:** Xác lập giới hạn toán học: Dữ liệu tích phân vĩ mô không có tính nhận diện đơn nhất; cấm dùng dữ liệu vĩ mô để kết luận cơ chế.
- **Điều chưa xác lập:** Chưa chế tạo và thử nghiệm thành công đồ gá đo cục bộ tích hợp cảm biến quang FBG trong bó dây bọc kín dưới áp suất.
- **Bất định còn lại:** Thách thức kỹ thuật thực nghiệm cực lớn trong việc đo đạc bên trong vỏ màng kín chứa khí áp suất cao.
- **Trạng thái & Độ tin cậy:** `macroscopic_killed_local_unresolved` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G04, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md`

---
### Bài Kiểm toán K4: Liệu đóng góp còn sống sót của đề tài có bị sụp đổ về khẳng ...
- **Phán quyết:** `PARTIAL_OVERLAP` | **Khóa ứng viên:** `True` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Liệu đóng góp còn sống sót của đề tài có bị sụp đổ về khẳng định tầm thường 'áp suất chủ động làm thay đổi ma sát và độ cứng' mà không tạo ra một câu hỏi cơ học dự đoán mới nào hay không?
- **Điều kiện loại bỏ (Kill Condition):** Đề tài chỉ còn lại hiện tượng biến đổi độ cứng phụ thuộc áp suất chung chung (vốn đã được giải quyết bởi các bài báo wire jamming đàn hồi), thiếu vắng một bài toán cơ học dự đoán hoặc bài toán phân biệt mô hình thực sự.
- **Khẳng định & Mục tiêu liên quan:** Claims: C1, C2, C4, C6 | Targets: T2 | Hypotheses: H0a, H0b
- **Phương pháp & Bằng chứng thực tế:** Phân tích sụp đổ đóng góp (Contribution Collapse Audit): Đối soát các tuyên bố tính mới với các bài báo tiền nhiệm Bai 2022, Liu 2021 và Zhang & Yao 2026.
- **Kết quả quan sát:** Đóng góp ở cấp độ linh kiện và thiết bị đã sụp đổ 100%. Nếu chỉ tuyên bố 'áp suất tăng làm ma sát tăng và dầm cứng hơn', đề tài bị KILL ngay lập tức bởi Bai 2022. Đề tài chỉ còn tồn tại nếu định vị hẹp vào câu hỏi cơ học: 'Liệu khung lý thuyết H0b có dự đoán đúng hành vi uốn phi tuyến hay cần một luật ghép cặp H1 mới dưới áp suất phân bố biến thiên?'.
- **Điều đã xác lập:** Toàn bộ các đóng góp cấp thiết bị và nguyên lý áp suất mới đã bị loại bỏ; đóng góp duy nhất có thể bảo vệ là bài toán cơ học phân biệt mô hình.
- **Điều chưa xác lập:** Chưa chứng minh được rằng câu hỏi cơ học phân biệt mô hình này đem lại giá trị kỹ thuật thực chất vượt trội hơn mô hình H0b.
- **Bất định còn lại:** Nguy cơ supervisor hoặc hội đồng đánh giá rằng sự khác biệt cơ học vi mô là quá nhỏ đối với một đề tài thạc sĩ ứng dụng robot mềm.
- **Trạng thái & Độ tin cậy:** `architectural_contribution_collapsed_mechanics_narrowed` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W02_C1_C4_ROBUST_CLOSURES.md, W05_T2_MECHANICS_P1_P2_P3_TEST.md`

---
### Bài Kiểm toán K5: Liệu cơ sở dữ liệu bằng chứng lưu trữ và văn hiến lân cận đã...
- **Phán quyết:** `NO_KILL_FOUND` | **Khóa ứng viên:** `False` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Liệu cơ sở dữ liệu bằng chứng lưu trữ và văn hiến lân cận đã chứa đựng một công trình tương đương gần gũi: Bó dây kim loại/NiTi chịu nén hướng tâm chủ động + uốn dầm + cơ học trượt/tiếp xúc phụ thuộc áp suất?
- **Điều kiện loại bỏ (Kill Condition):** Tồn tại một bài báo tiền nhiệm đã giải quyết trực tiếp và bao hàm toàn bộ cấu hình cơ học và bài toán tiếp xúc dầm NiTi chịu áp suất ngoài.
- **Khẳng định & Mục tiêu liên quan:** Claims: C5, C6, C7 | Targets: T1, T2, T3 | Hypotheses: H0b, H1
- **Phương pháp & Bằng chứng thực tế:** Kiểm tra sự trùng khớp cấu hình cơ học (Mechanical Configuration Matching): Đối chiếu chi tiết điều kiện biên, vật liệu và phương trình vi phân tiếp xúc giữa MP1 và 16 bài báo canonical.
- **Kết quả quan sát:** Trong tập 16 bài báo canonical, KHÔNG có bài báo nào hoàn toàn trùng khớp 100% cấu hình: Tjahjanto 2017 xét cáp thép ngầm biển dưới áp suất thủy tĩnh tĩnh (P2); Barsi 2025 xét cáp thép ngắn uốn thuần; Kang 2020 mô phỏng cáp xoắn SMA chịu kéo; Vahidi 2022 xét cáp xoắn không áp suất buồng. Tuy nhiên, các nhánh trích dẫn B11 và B12 chưa đóng hoàn toàn (stop_condition_satisfied = false).
- **Điều đã xác lập:** Không có bài báo nào trong tập 16 bài canonical triệt tiêu hoàn toàn tính mới của ứng viên mechanics core.
- **Điều chưa xác lập:** Chưa hoàn tất rà soát các bài báo tiềm năng sâu hơn trong nhánh B11 và B12 thuộc văn hiến cơ học kết cấu hàng hải và địa chấn.
- **Bất định còn lại:** Khả năng tồn tại bài báo tiền nhiệm trực tiếp trong các tạp chí chuyên ngành kết cấu cáp dây nặng (heavy cable mechanics).
- **Trạng thái & Độ tin cậy:** `no_identical_paper_in_canonical_set` | `high`
- **Xuất xứ:** `outputs/execution/MP1-V002/W2-04/MP1_16_PAPER_ROLE_MATRIX.json, outputs/verification/MP1-V002/citation_coverage.json`

---
### Bài Kiểm toán K6: Liệu áp suất chủ động có phải là một biến số cơ học độc lập ...
- **Phán quyết:** `UNRESOLVED` | **Khóa ứng viên:** `True` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Liệu áp suất chủ động có phải là một biến số cơ học độc lập thực sự, hay chỉ là một điều kiện biên ngoài không được xác định rõ ràng do sai số truyền áp?
- **Điều kiện loại bỏ (Kill Condition):** Áp suất buồng khí p không thể ánh xạ một cách đơn nhất và tin cậy sang lực tiếp xúc pháp tuyến f_n giữa các sợi dây do hiệu ứng vòm (arching) và độ cứng màng bao, dẫn đến việc sai số hình học bị quy kết nhầm thành sai số của luật cơ học cấu thành.
- **Khẳng định & Mục tiêu liên quan:** Claims: C6 | Targets: T2 | Hypotheses: H0b, H1
- **Phương pháp & Bằng chứng thực tế:** Phân tích cơ học màng và xếp chặt hình học: Đánh giá độ cứng vòng của màng đàn hồi và hiệu ứng vòm phân tán lực nén trong cấu hình xếp ngẫu nhiên so với xếp lục giác đều.
- **Kết quả quan sát:** Áp suất buồng p không chuyển hóa 100% thành lực pháp tuyến f_n giữa các sợi dây. Lực pháp tuyến thực tế bị suy giảm đáng kể bởi lực căng vòng của màng và các điểm tì vòm. Nếu không đo đạc hoặc hiệu chuẩn độc lập quan hệ p -> f_n, mọi kết luận về việc mô hình uốn bị sai lệch sẽ bị ngụy trang bởi sai số truyền lực.
- **Điều đã xác lập:** Nhận diện rõ ràng lỗ hổng truyền áp suất; bắt buộc phải có bước hiệu chuẩn nén hướng kính độc lập trước khi uốn.
- **Điều chưa xác lập:** Chưa có phương trình giải tích hoặc hàm truyền thực nghiệm xác định chính xác f_n(p, kappa) cho cấu hình bó dây của MP1.
- **Bất định còn lại:** Hiệu ứng vòm biến đổi phi tuyến theo độ cong uốn, khiến việc ánh xạ lực tiếp xúc pháp tuyến gặp sai số động học.
- **Trạng thái & Độ tin cậy:** `pressure_mapping_uncertainty_identified` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G09, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md`

---
### Bài Kiểm toán K7: Liệu các mô hình cáp dây, tao dây và cơ học tiếp xúc ma sát ...
- **Phán quyết:** `UNRESOLVED` | **Khóa ứng viên:** `True` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Liệu các mô hình cáp dây, tao dây và cơ học tiếp xúc ma sát hiện hữu trong văn hiến có thể giải thích đầy đủ đáp ứng cơ học đề xuất khi kết hợp với luật cấu thành NiTi chuyển pha hay không?
- **Điều kiện loại bỏ (Kill Condition):** Các công thức giải tích hoặc phần tử hữu hạn hiện hữu (Costello, Love curved rod, Abaqus contact formulation, Tjahjanto cable ODE) đã cung cấp đầy đủ công cụ dự đoán chính xác mà không cần bất kỳ sự phát triển lý thuyết ghép cặp mới nào.
- **Khẳng định & Mục tiêu liên quan:** Claims: C7 | Targets: T3 | Hypotheses: H0b
- **Phương pháp & Bằng chứng thực tế:** Phân tích phương trình vi phân tiếp xúc dầm liên hợp: Đánh giá xem việc thay thế luật vật liệu đàn hồi E bằng ma trận Jacobian cấu thành tiếp tuyến C_tan(sigma, epsilon, xi) của NiTi vào hệ phương trình vi phân tiếp xúc của Tjahjanto có giải quyết trọn vẹn bài toán hay không.
- **Kết quả quan sát:** Về mặt toán học cơ học môi trường liên tục, việc tích hợp luật cấu thành siêu đàn hồi vào phương trình cân bằng tiếp xúc dầm là một bài toán tiêu chuẩn (standard forward formulation). Không xuất hiện số hạng kỳ dị hay nghịch lý vật lý nào đòi hỏi phải phát minh ra một quy luật tự nhiên mới. Do đó, khả năng rất cao là các mô hình hiện hữu kết hợp lại là hoàn toàn đủ.
- **Điều đã xác lập:** Hệ phương trình vi phân dầm cáp tiếp xúc hiện hữu có khả năng dung nạp luật vật liệu phi tuyến theo từng bước gia số.
- **Điều chưa xác lập:** Chưa triển khai tích hợp giải số hệ phương trình này cho bài toán bó dây NiTi dưới áp suất biến thiên để so sánh với thực nghiệm.
- **Bất định còn lại:** Khả năng cao là việc giải thành công hệ phương trình kết hợp này chỉ là một bài toán tính toán kỹ thuật (engineering implementation), không phải phát minh khoa học nền tảng.
- **Trạng thái & Độ tin cậy:** `existing_formulation_plausibility_high` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#Section6, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W10_REEDLUNN_FANG_CONSERVATIVE_REMEDIATION.md`

---
### Bài Kiểm toán K8: Các tham số của mô hình có được đo lường độc lập và khóa chặ...
- **Phán quyết:** `PARTIAL_OVERLAP` | **Khóa ứng viên:** `True` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Các tham số của mô hình có được đo lường độc lập và khóa chặt trước khi kiểm chứng hay không, hay mô hình chỉ khớp được số liệu nhờ vào việc thả nổi và bù trừ tham số tự do?
- **Điều kiện loại bỏ (Kill Condition):** Ứng viên chỉ vượt trội hơn H0b nhờ vào việc hiệu chỉnh tự do các tham số (over-fitting), bù trừ giữa hệ số ma sát mu và tỷ lệ truyền áp alpha_trans, hoặc rò rỉ dữ liệu kiểm chứng vào quá trình cân chỉnh tham số.
- **Khẳng định & Mục tiêu liên quan:** Claims: C7 | Targets: T3 | Hypotheses: H0b, H1
- **Phương pháp & Bằng chứng thực tế:** Phân tích bù trừ tham số (Parameter Confounding Analysis): Khảo sát tích số mu * alpha_trans trong phương trình lực cản trượt F_cap = mu * alpha_trans * p; kiểm tra tính duy nhất của nghiệm.
- **Kết quả quan sát:** Stage 3 W09 đã ban hành Quy tắc Khóa tham số tuyệt đối (Locked Calibration Rule): Cấm thả nổi tham số ma sát và truyền áp để ép khớp đường cong uốn; toàn bộ tham số phải đo độc lập ngoài bài toán bó dây. Tuy nhiên, đây mới là quy tắc phương pháp luận trên văn bản, chưa có dữ liệu thực nghiệm thực tế để chứng minh quy tắc này được thực thi thành công.
- **Điều đã xác lập:** Đã thiết lập khung kiểm soát phương pháp luận nghiêm ngặt ngăn chặn hiện tượng bù trừ tham số và rò rỉ dữ liệu.
- **Điều chưa xác lập:** Chưa thực hiện chiến dịch đo lường thực nghiệm độc lập các tham số vật liệu và ma sát.
- **Bất định còn lại:** Độ nhạy và lan truyền sai số đo đạc từ các thử nghiệm độc lập vào mô hình uốn tổng thể.
- **Trạng thái & Độ tin cậy:** `locked_calibration_rule_mandated_pending_data` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G08, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W09_MODEL_VALIDATION_CREDIBILITY.md`

---
### Bài Kiểm toán K9: Liệu sự thay đổi độ cứng và trễ năng lượng có thể được quy k...
- **Phán quyết:** `UNRESOLVED` | **Khóa ứng viên:** `True` | **Cần người duyệt:** `True`
- **Câu hỏi khoa học:** Liệu sự thay đổi độ cứng và trễ năng lượng có thể được quy kết một cách đơn nhất cho cơ chế đề xuất hay bị gây nhiễu bởi các hiệu ứng phụ (nhiệt độ, ma sát thuần, hình học, lịch sử tải)?
- **Điều kiện loại bỏ (Kill Condition):** Cơ chế ghép cặp đề xuất không thể phân biệt được với trễ ma sát thông thường, trễ nhiệt độ do nhiệt tiềm ẩn chuyển pha, hoặc biến dạng hình học trong phạm vi độ không đảm bảo đo.
- **Khẳng định & Mục tiêu liên quan:** Claims: C5, C6, C7 | Targets: T1, T2, T3 | Hypotheses: H0a, H0b, H1
- **Phương pháp & Bằng chứng thực tế:** Phân tích trễ cơ-nhiệt (Thermomechanical Hysteresis Analysis): So sánh công tiêu tán do ma sát Coulomb W_fric với năng lượng tiêu tán do trễ chuyển pha W_phase và trao đổi nhiệt môi trường.
- **Kết quả quan sát:** Đã chuẩn hóa 3 định nghĩa toán học riêng biệt cho độ cứng uốn để tránh mơ hồ. Tuy nhiên, việc phân tách trễ chuyển pha siêu đàn hồi khỏi trễ ma sát Coulomb trong chu kỳ uốn là rất khó khăn nếu không kiểm soát chặt chẽ nhiệt độ và tốc độ gia tải (phải tải chậm quasi-static < 0.05 Hz hoặc dùng ảnh nhiệt hồng ngoại đồng bộ).
- **Điều đã xác lập:** Đã chuẩn hóa các đại lượng đo độ cứng uốn và xác định các nguồn gây nhiễu năng lượng trễ.
- **Điều chưa xác lập:** Chưa có thiết kế thí nghiệm kiểm soát nhiệt độ đồng bộ trong quá trình đo trễ uốn.
- **Bất định còn lại:** Hiệu ứng tự gia nhiệt làm biến đổi cơ tính trong quá trình robot uốn lặp lại ở tần số cao.
- **Trạng thái & Độ tin cậy:** `hysteresis_definitions_formalized_observability_unresolved` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G12, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md`

---
