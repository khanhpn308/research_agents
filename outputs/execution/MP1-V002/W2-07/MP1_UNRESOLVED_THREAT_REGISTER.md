# Sổ bộ Các Mối Đe dọa Chưa Giải quyết (MP1 Unresolved Threat Register)

> **Tệp chính tắc:** `MP1_UNRESOLVED_THREAT_REGISTER.json`  
> **Tổng số mối đe dọa:** 6 threats  
> **Mục tiêu:** Định lượng minh bạch toàn bộ các lỗ hổng lý thuyết, thực nghiệm và văn hiến đang đe dọa tính mới của ứng viên MP1-P1.

## 1. Bảng Tổng hợp Các Mối Đe dọa

| Mã Đe dọa (ID) | Mức độ | Khóa Phán quyết? | Phân loại Đe dọa | Trạng thái Hiện tại | Câu hỏi Khoa học Trọng tâm |
|:---:|:---:|:---:|---|:---:|---|
| **THREAT-01** | `CRITICAL` | **CÓ (BLOCKING)** | `MODEL_IDENTIFIABILITY_AND_PARAMETER_SUBSTITUTION` | `OPEN_BLOCKING_THREAT` | Liệu một mô hình phần tử hữu hạn tiêu chuẩn sẵn có kết hợp luật siêu đàn hồ... |
| **THREAT-02** | `CRITICAL` | **CÓ (BLOCKING)** | `EXPERIMENTAL_NON_IDENTIFIABILITY` | `OPEN_BLOCKING_THREAT` | Làm thế nào để chứng minh hiện tượng mềm hóa độ cứng uốn thực sự do chuyển ... |
| **THREAT-03** | `HIGH` | **CÓ (BLOCKING)** | `MECHANICAL_COEXISTENCE_DOMAIN_COLLAPSE` | `OPEN_BLOCKING_THREAT` | Liệu cơ cấu có thể hoạt động ổn định trong miền biến dạng lớn vượt ngưỡng c... |
| **THREAT-04** | `HIGH` | KHÔNG | `PRESSURE_TRANSMISSION_AND_ARCHING_UNCERTAINTY` | `OPEN_CALIBRATION_THREAT` | Mối quan hệ ánh xạ p -> f_n có thể được chuẩn hóa giải tích hay bắt buộc ph... |
| **THREAT-05** | `HIGH` | **CÓ (BLOCKING)** | `CITATION_CHASING_STOPPING_CONDITION_UNMET` | `OPEN_BLOCKING_THREAT` | Liệu trong văn hiến cơ học kết cấu cáp dây ngầm biển hoặc giảm chấn địa chấ... |
| **THREAT-06** | `MEDIUM` | KHÔNG | `THERMOMECHANICAL_LATENT_HEAT_COUPLING` | `OPEN_MONITORING_THREAT` | Ở tần số uốn cao của robot mềm, hiệu ứng tự gia nhiệt làm thay đổi đáp ứng ... |

## 2. Chi tiết Từng Mối Đe dọa

### Mối Đe dọa THREAT-01: MODEL_IDENTIFIABILITY_AND_PARAMETER_SUBSTITUTION (CRITICAL)
- **Khóa phán quyết tính mới (Blocks Adjudication):** `True`
- **Yêu cầu con người phê duyệt (Human Review):** `True`
- **Khẳng định & Mục tiêu ảnh hưởng:** Claims: C7 | Targets: T3 | Hypotheses: H0b, H1
- **Khoảng trống bằng chứng:** Chưa có phép thử phân biệt đối chứng chứng minh các mô hình NiTi phi tuyến ghép tiếp xúc Coulomb hiện hữu (H0b trong Abaqus/OpenSees) thất bại khi dự đoán dầm bó dây dưới áp suất biến thiên.
- **Câu hỏi khoa học:** Liệu một mô hình phần tử hữu hạn tiêu chuẩn sẵn có kết hợp luật siêu đàn hồi Auricchio và tiếp xúc mặt Coulomb có thể mô tả chính xác đáp ứng uốn mà không cần một phương trình vi mô mới hay không?
- **Yêu cầu giải quyết:** Thực hiện mô phỏng số đối chứng H0b với các tham số vật liệu bị khóa (Locked Calibration); so sánh sai số dự đoán ngoài tập dữ liệu hiệu chuẩn.
- **Điều kiện hóa giải:** Bác bỏ thực nghiệm hoặc số trị đối với H0b trước khi tuyên bố H1 hợp lệ.
- **Rủi ro còn lại:** Nếu H0b dự đoán tốt trong giới hạn sai số đo đạc, đóng góp lý thuyết H1 sẽ bị hạ xuống thành tinh chỉnh tham số.
- **Trạng thái hiện tại:** `OPEN_BLOCKING_THREAT`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#Section5, outputs/execution/MP1-V002/W2-03/MP1_PARAMETER_SUBSTITUTION_RECONSTRUCTION.json`

---
### Mối Đe dọa THREAT-02: EXPERIMENTAL_NON_IDENTIFIABILITY (CRITICAL)
- **Khóa phán quyết tính mới (Blocks Adjudication):** `True`
- **Yêu cầu con người phê duyệt (Human Review):** `True`
- **Khẳng định & Mục tiêu ảnh hưởng:** Claims: C7 | Targets: T3 | Hypotheses: H1
- **Khoảng trống bằng chứng:** Đường cong mô-men - độ cong uốn vĩ mô (M - kappa) là đại lượng tích phân không gian, không có tính nhận diện đơn nhất giữa chuyển pha, ma sát trượt và biến dạng màng bao.
- **Câu hỏi khoa học:** Làm thế nào để chứng minh hiện tượng mềm hóa độ cứng uốn thực sự do chuyển pha NiTi và trượt ma sát gây ra, thay vì do trượt tại ngàm kẹp hoặc biến dạng bẹp tiết diện dầm?
- **Yêu cầu giải quyết:** Thiết kế đồ gá thực nghiệm có đo biến trạng thái cục bộ: DIC bề mặt, cảm biến FBG trong lõi, ảnh nhiệt hồng ngoại ghi nhận nhiệt tiềm ẩn chuyển pha, và đo trượt đầu dây độc lập.
- **Điều kiện hóa giải:** Đề xuất và phê duyệt quy trình đo đạc cục bộ đa phương thức trước khi tiến hành thí nghiệm kiểm chứng.
- **Rủi ro còn lại:** Độ phức tạp cơ điện tử khi tích hợp cảm biến quang FBG vào bên trong bó dây bọc kín dưới áp suất cao.
- **Trạng thái hiện tại:** `OPEN_BLOCKING_THREAT`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#G04, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md`

---
### Mối Đe dọa THREAT-03: MECHANICAL_COEXISTENCE_DOMAIN_COLLAPSE (HIGH)
- **Khóa phán quyết tính mới (Blocks Adjudication):** `True`
- **Yêu cầu con người phê duyệt (Human Review):** `True`
- **Khẳng định & Mục tiêu ảnh hưởng:** Claims: C7 | Targets: T3 | Hypotheses: H0b, H1
- **Khoảng trống bằng chứng:** Ở miền biến dạng uốn nhỏ dưới 0.75% thường gặp trong tay gắp mềm, dây NiTi hoàn toàn ở pha đàn hồi Austenite, làm mất hiện tượng chuyển pha và thoái hóa về kẹt dây đàn hồi H0a.
- **Câu hỏi khoa học:** Liệu cơ cấu có thể hoạt động ổn định trong miền biến dạng lớn vượt ngưỡng chuyển pha mà không bị mỏi cơ học hoặc hỏng màng bao sau số chu kỳ thấp?
- **Yêu cầu giải quyết:** Xác định bản đồ chế độ tải uốn - kéo (bending-tension map); kiểm chứng độ bền mỏi chu kỳ thấp trong miền cùng tồn tại.
- **Điều kiện hóa giải:** Chứng minh sự tồn tại của miền vận hành thực tế mà ở đó cả hai cơ chế cùng kích hoạt và giữ được độ bền kết cấu.
- **Rủi ro còn lại:** Nếu phạm vi uốn thực tế bị giới hạn ở góc nhỏ, toàn bộ luận văn sẽ bị thoái hóa về bài toán kẹt dây đàn hồi đã được giải bởi Zhang & Yao 2026.
- **Trạng thái hiện tại:** `OPEN_BLOCKING_THREAT`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G03, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W06_T3_TRANSFORMATION_SLIP_COEXISTENCE.md`

---
### Mối Đe dọa THREAT-04: PRESSURE_TRANSMISSION_AND_ARCHING_UNCERTAINTY (HIGH)
- **Khóa phán quyết tính mới (Blocks Adjudication):** `False`
- **Yêu cầu con người phê duyệt (Human Review):** `False`
- **Khẳng định & Mục tiêu ảnh hưởng:** Claims: C6 | Targets: T2 | Hypotheses: H0b, H1
- **Khoảng trống bằng chứng:** Lực nén pháp tuyến thực tế giữa các sợi dây f_n bị suy giảm so với áp suất buồng khí p do độ cứng vòng của màng và hiệu ứng vòm (arching effect) trong bó dây.
- **Câu hỏi khoa học:** Mối quan hệ ánh xạ p -> f_n có thể được chuẩn hóa giải tích hay bắt buộc phải hiệu chuẩn thực nghiệm từng cấu hình bó dây?
- **Yêu cầu giải quyết:** Thực hiện thí nghiệm nén hướng kính độc lập và sử dụng cảm biến màng áp lực để đo hàm truyền áp suất p -> f_n.
- **Điều kiện hóa giải:** Xây dựng hàm truyền lực pháp tuyến được kiểm chứng trước khi lắp vào mô hình uốn.
- **Rủi ro còn lại:** Hiệu ứng vòm biến thiên phi tuyến theo độ cong uốn, tạo thêm sai số cho mô hình uốn.
- **Trạng thái hiện tại:** `OPEN_CALIBRATION_THREAT`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G09, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md`

---
### Mối Đe dọa THREAT-05: CITATION_CHASING_STOPPING_CONDITION_UNMET (HIGH)
- **Khóa phán quyết tính mới (Blocks Adjudication):** `True`
- **Yêu cầu con người phê duyệt (Human Review):** `True`
- **Khẳng định & Mục tiêu ảnh hưởng:** Claims: C6, C7 | Targets: T2, T3 | Hypotheses: H0b, H1
- **Khoảng trống bằng chứng:** Điều kiện dừng trích dẫn chưa thỏa mãn (stop_condition_satisfied = false); các nhánh trích dẫn ngược B11 (Kang 2020) và B12 (Barsi 2025) chưa được rà soát triệt để.
- **Câu hỏi khoa học:** Liệu trong văn hiến cơ học kết cấu cáp dây ngầm biển hoặc giảm chấn địa chấn đã có bài báo giải quyết trọn vẹn bài toán bó dây uốn dưới áp suất ngoài hay chưa?
- **Yêu cầu giải quyết:** Hoàn tất sàng lọc toàn văn các bài báo tiềm năng trong nhánh B11 và B12; thiết lập mốc ngày cắt tìm kiếm chính thức.
- **Điều kiện hóa giải:** Đóng điều kiện dừng trích dẫn trước khi đưa ra phán quyết tính mới cuối cùng.
- **Rủi ro còn lại:** Nguy cơ tìm thấy bài báo tiền nhiệm trực tiếp trong văn hiến cơ học kết cấu nặng.
- **Trạng thái hiện tại:** `OPEN_BLOCKING_THREAT`
- **Xuất xứ:** `outputs/verification/MP1-V002/citation_coverage.json, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W11_CITATION_COVERAGE_QA.md`

---
### Mối Đe dọa THREAT-06: THERMOMECHANICAL_LATENT_HEAT_COUPLING (MEDIUM)
- **Khóa phán quyết tính mới (Blocks Adjudication):** `False`
- **Yêu cầu con người phê duyệt (Human Review):** `False`
- **Khẳng định & Mục tiêu ảnh hưởng:** Claims: C7 | Targets: T3 | Hypotheses: H0b, H1
- **Khoảng trống bằng chứng:** Nhiệt tiềm ẩn tỏa ra và hấp thụ trong quá trình chuyển pha làm thay đổi nhiệt độ cục bộ của sợi dây, dẫn đến dịch chuyển ứng suất kích hoạt theo định luật Clausius-Clapeyron.
- **Câu hỏi khoa học:** Ở tần số uốn cao của robot mềm, hiệu ứng tự gia nhiệt làm thay đổi đáp ứng độ cứng và ma sát trượt bao nhiêu phần trăm so với trạng thái tĩnh đẳng nhiệt?
- **Yêu cầu giải quyết:** Thử nghiệm uốn ở các tần số khác nhau (0.01 Hz đến 1 Hz) kết hợp đo nhiệt độ hồng ngoại.
- **Điều kiện hóa giải:** Xác lập phạm vi tần số quasi-static mà ở đó hiệu ứng nhiệt tiềm ẩn có thể bỏ qua được.
- **Rủi ro còn lại:** Mô hình tĩnh có thể sai lệch khi áp dụng cho điều khiển robot chuyển động nhanh.
- **Trạng thái hiện tại:** `OPEN_MONITORING_THREAT`
- **Xuất xứ:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W09_REEDLUNN_2013_DEEP_AUDIT.md`

---
