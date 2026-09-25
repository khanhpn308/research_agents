import json

def get_novelty_candidate_register():
    return [
        {
            "candidate_id": "MP1-P1",
            "candidate_statement": "Mô hình cơ học ghép cặp cấu thành – tiếp xúc giữa chuyển pha Martensite cảm ứng ứng suất và ma sát trượt Coulomb nội tại trong bó dây NiTi siêu đàn hồi chịu áp suất giam giữ pháp tuyến chủ động.",
            "historical_origin": "Chuyển dịch từ đề xuất kiến trúc thiết bị ban đầu của mentor (C1–C8) sau khi tính mới linh kiện sụp đổ tại MP1-V001; định hình lại thành Mechanics Core (C5–C7, T1–T3) và được tái cấu trúc bảo thủ qua phản biện Astra Stage 2–3.",
            "scientific_category": "Cơ học vật rắn biến dạng / Cơ học tiếp xúc và cấu thành vật liệu thông minh (Solid & Contact Mechanics of Active Materials)",
            "novelty_category": "Coupled Constitutive-Contact Mechanics in Confined Active Bundles",
            "claim_ids": ["C5", "C6", "C7"],
            "target_ids": ["T2", "T3"],
            "hypothesis_ids": ["H0b", "H1"],
            "supporting_evidence": "Reedlunn et al. 2013 (fac21c950e) chứng minh ngưỡng chuyển pha dịch chuyển dưới áp lực tiếp xúc hướng tâm; Vahidi et al. 2022 (53200aa0c6) mô hình hóa ma sát tiếp xúc dây NiTi; Báo cáo khắc phục Stage 3 (W06) xác lập điều kiện cần cho Miền Cùng Tồn Tại ở góc uốn lớn.",
            "counter_evidence": "Fang et al. 2019 (2f7fcf2f8f) chứng minh mô hình hiện tượng học rút gọn không cần tiếp xúc vi mô vẫn khớp được trễ vĩ mô; Khung lý thuyết NiTi phi tuyến + tiếp xúc Coulomb trong Abaqus UMAT (H0b) chưa bị bác bỏ; Sai sót lịch sử về Carboni S2a bị lật tẩy là cáp thép.",
            "prior_art_overlap": "Bị đón đầu ở cấp thiết bị về wire jamming (Bai 2022), áp suất dương (Liu 2021), tích hợp SMA (Takashima 2022), cáp xoắn chịu kéo trục (Reedlunn 2013), và giảm chấn cáp vĩ mô (Fang 2019).",
            "unresolved_threat_ids": ["THREAT-01", "THREAT-02", "THREAT-03", "THREAT-04", "THREAT-05", "THREAT-06"],
            "kill_condition_ids": ["KILL-K01", "KILL-K02", "KILL-K03", "KILL-K04", "KILL-K05"],
            "H0_relationship": "H0a (mô-đun đàn hồi hằng số) đã bị BÁC BỎ (REFUTED); H0b (khung NiTi phi tuyến + tiếp xúc Coulomb hiện hữu) CHƯA BỊ BÁC BỎ (NOT FALSIFIED); H1 (nhu cầu về luật ghép cặp vi mô mới) CHƯA ĐỦ BẰNG CHỨNG (INSUFFICIENT).",
            "coexistence_requirement": "Bắt buộc phải vận hành ở độ cong uốn lớn kappa > kappa_tr ~ 0.75% hoặc có lực căng dọc trục đáng kể để đồng thời kích hoạt chuyển pha và trượt ma sát giữa các sợi dây.",
            "identifiability_requirement": "Bắt buộc phải đo biến trạng thái cục bộ (DIC đo biến dạng mặt ngoài sợi, FBG đo biến dạng lõi, ảnh nhiệt hồng ngoại, cảm biến trượt đầu dây); nghiêm cấm dùng đường cong uốn vĩ mô M - kappa để quy kết cơ chế.",
            "parameter_lock_requirement": "Toàn bộ tham số đàn hồi, chuyển pha (E_A, E_M, sigma_tr) và hệ số ma sát (mu) phải được hiệu chuẩn độc lập ngoài bài toán bó dây uốn (Locked Calibration Rule).",
            "candidate_status": "PENDING_GATE",
            "adjudication_status": "DEFERRED",
            "confidence": "medium",
            "provenance": "outputs/execution/MP1-V002/W2-03/MP1_T1_T2_T3_TARGET_MATRIX.json, docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md"
        }
    ]

def get_unresolved_threat_register():
    return [
        {
            "threat_id": "THREAT-01",
            "claim_ids": ["C7"],
            "target_ids": ["T3"],
            "hypothesis_ids": ["H0b", "H1"],
            "threat_type": "MODEL_IDENTIFIABILITY_AND_PARAMETER_SUBSTITUTION",
            "source_files": [
                "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "evidence_gap": "Chưa có phép thử phân biệt đối chứng chứng minh các mô hình NiTi phi tuyến ghép tiếp xúc Coulomb hiện hữu (H0b trong Abaqus/OpenSees) thất bại khi dự đoán dầm bó dây dưới áp suất biến thiên.",
            "scientific_question": "Liệu một mô hình phần tử hữu hạn tiêu chuẩn sẵn có kết hợp luật siêu đàn hồi Auricchio và tiếp xúc mặt Coulomb có thể mô tả chính xác đáp ứng uốn mà không cần một phương trình vi mô mới hay không?",
            "required_search_or_model_or_experiment": "Thực hiện mô phỏng số đối chứng H0b với các tham số vật liệu bị khóa (Locked Calibration); so sánh sai số dự đoán ngoài tập dữ liệu hiệu chuẩn.",
            "severity": "CRITICAL",
            "blocks_adjudication": True,
            "current_status": "OPEN_BLOCKING_THREAT",
            "resolution_requirement": "Bác bỏ thực nghiệm hoặc số trị đối với H0b trước khi tuyên bố H1 hợp lệ.",
            "residual_risk": "Nếu H0b dự đoán tốt trong giới hạn sai số đo đạc, đóng góp lý thuyết H1 sẽ bị hạ xuống thành tinh chỉnh tham số.",
            "human_review_required": True,
            "provenance": "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#Section5, outputs/execution/MP1-V002/W2-03/MP1_PARAMETER_SUBSTITUTION_RECONSTRUCTION.json"
        },
        {
            "threat_id": "THREAT-02",
            "claim_ids": ["C7"],
            "target_ids": ["T3"],
            "hypothesis_ids": ["H1"],
            "threat_type": "EXPERIMENTAL_NON_IDENTIFIABILITY",
            "source_files": [
                "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "evidence_gap": "Đường cong mô-men - độ cong uốn vĩ mô (M - kappa) là đại lượng tích phân không gian, không có tính nhận diện đơn nhất giữa chuyển pha, ma sát trượt và biến dạng màng bao.",
            "scientific_question": "Làm thế nào để chứng minh hiện tượng mềm hóa độ cứng uốn thực sự do chuyển pha NiTi và trượt ma sát gây ra, thay vì do trượt tại ngàm kẹp hoặc biến dạng bẹp tiết diện dầm?",
            "required_search_or_model_or_experiment": "Thiết kế đồ gá thực nghiệm có đo biến trạng thái cục bộ: DIC bề mặt, cảm biến FBG trong lõi, ảnh nhiệt hồng ngoại ghi nhận nhiệt tiềm ẩn chuyển pha, và đo trượt đầu dây độc lập.",
            "severity": "CRITICAL",
            "blocks_adjudication": True,
            "current_status": "OPEN_BLOCKING_THREAT",
            "resolution_requirement": "Đề xuất và phê duyệt quy trình đo đạc cục bộ đa phương thức trước khi tiến hành thí nghiệm kiểm chứng.",
            "residual_risk": "Độ phức tạp cơ điện tử khi tích hợp cảm biến quang FBG vào bên trong bó dây bọc kín dưới áp suất cao.",
            "human_review_required": True,
            "provenance": "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#G04, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md"
        },
        {
            "threat_id": "THREAT-03",
            "claim_ids": ["C7"],
            "target_ids": ["T3"],
            "hypothesis_ids": ["H0b", "H1"],
            "threat_type": "MECHANICAL_COEXISTENCE_DOMAIN_COLLAPSE",
            "source_files": [
                "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W06_T3_TRANSFORMATION_SLIP_COEXISTENCE.md",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "evidence_gap": "Ở miền biến dạng uốn nhỏ dưới 0.75% thường gặp trong tay gắp mềm, dây NiTi hoàn toàn ở pha đàn hồi Austenite, làm mất hiện tượng chuyển pha và thoái hóa về kẹt dây đàn hồi H0a.",
            "scientific_question": "Liệu cơ cấu có thể hoạt động ổn định trong miền biến dạng lớn vượt ngưỡng chuyển pha mà không bị mỏi cơ học hoặc hỏng màng bao sau số chu kỳ thấp?",
            "required_search_or_model_or_experiment": "Xác định bản đồ chế độ tải uốn - kéo (bending-tension map); kiểm chứng độ bền mỏi chu kỳ thấp trong miền cùng tồn tại.",
            "severity": "HIGH",
            "blocks_adjudication": True,
            "current_status": "OPEN_BLOCKING_THREAT",
            "resolution_requirement": "Chứng minh sự tồn tại của miền vận hành thực tế mà ở đó cả hai cơ chế cùng kích hoạt và giữ được độ bền kết cấu.",
            "residual_risk": "Nếu phạm vi uốn thực tế bị giới hạn ở góc nhỏ, toàn bộ luận văn sẽ bị thoái hóa về bài toán kẹt dây đàn hồi đã được giải bởi Zhang & Yao 2026.",
            "human_review_required": True,
            "provenance": "docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G03, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W06_T3_TRANSFORMATION_SLIP_COEXISTENCE.md"
        },
        {
            "threat_id": "THREAT-04",
            "claim_ids": ["C6"],
            "target_ids": ["T2"],
            "hypothesis_ids": ["H0b", "H1"],
            "threat_type": "PRESSURE_TRANSMISSION_AND_ARCHING_UNCERTAINTY",
            "source_files": [
                "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md",
                "papers/verification/MP1-V002/2017-Submarine Cable Bending Mechanics_ccdc1bb980.pdf"
            ],
            "evidence_gap": "Lực nén pháp tuyến thực tế giữa các sợi dây f_n bị suy giảm so với áp suất buồng khí p do độ cứng vòng của màng và hiệu ứng vòm (arching effect) trong bó dây.",
            "scientific_question": "Mối quan hệ ánh xạ p -> f_n có thể được chuẩn hóa giải tích hay bắt buộc phải hiệu chuẩn thực nghiệm từng cấu hình bó dây?",
            "required_search_or_model_or_experiment": "Thực hiện thí nghiệm nén hướng kính độc lập và sử dụng cảm biến màng áp lực để đo hàm truyền áp suất p -> f_n.",
            "severity": "HIGH",
            "blocks_adjudication": False,
            "current_status": "OPEN_CALIBRATION_THREAT",
            "resolution_requirement": "Xây dựng hàm truyền lực pháp tuyến được kiểm chứng trước khi lắp vào mô hình uốn.",
            "residual_risk": "Hiệu ứng vòm biến thiên phi tuyến theo độ cong uốn, tạo thêm sai số cho mô hình uốn.",
            "human_review_required": False,
            "provenance": "docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G09, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md"
        },
        {
            "threat_id": "THREAT-05",
            "claim_ids": ["C6", "C7"],
            "target_ids": ["T2", "T3"],
            "hypothesis_ids": ["H0b", "H1"],
            "threat_type": "CITATION_CHASING_STOPPING_CONDITION_UNMET",
            "source_files": [
                "outputs/verification/MP1-V002/citation_coverage.json",
                "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W11_CITATION_COVERAGE_QA.md"
            ],
            "evidence_gap": "Điều kiện dừng trích dẫn chưa thỏa mãn (stop_condition_satisfied = false); các nhánh trích dẫn ngược B11 (Kang 2020) và B12 (Barsi 2025) chưa được rà soát triệt để.",
            "scientific_question": "Liệu trong văn hiến cơ học kết cấu cáp dây ngầm biển hoặc giảm chấn địa chấn đã có bài báo giải quyết trọn vẹn bài toán bó dây uốn dưới áp suất ngoài hay chưa?",
            "required_search_or_model_or_experiment": "Hoàn tất sàng lọc toàn văn các bài báo tiềm năng trong nhánh B11 và B12; thiết lập mốc ngày cắt tìm kiếm chính thức.",
            "severity": "HIGH",
            "blocks_adjudication": True,
            "current_status": "OPEN_BLOCKING_THREAT",
            "resolution_requirement": "Đóng điều kiện dừng trích dẫn trước khi đưa ra phán quyết tính mới cuối cùng.",
            "residual_risk": "Nguy cơ tìm thấy bài báo tiền nhiệm trực tiếp trong văn hiến cơ học kết cấu nặng.",
            "human_review_required": True,
            "provenance": "outputs/verification/MP1-V002/citation_coverage.json, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W11_CITATION_COVERAGE_QA.md"
        },
        {
            "threat_id": "THREAT-06",
            "claim_ids": ["C7"],
            "target_ids": ["T3"],
            "hypothesis_ids": ["H0b", "H1"],
            "threat_type": "THERMOMECHANICAL_LATENT_HEAT_COUPLING",
            "source_files": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W09_REEDLUNN_2013_DEEP_AUDIT.md",
                "papers/verification/MP1-V002/A1-2013-Part2.pdf"
            ],
            "evidence_gap": "Nhiệt tiềm ẩn tỏa ra và hấp thụ trong quá trình chuyển pha làm thay đổi nhiệt độ cục bộ của sợi dây, dẫn đến dịch chuyển ứng suất kích hoạt theo định luật Clausius-Clapeyron.",
            "scientific_question": "Ở tần số uốn cao của robot mềm, hiệu ứng tự gia nhiệt làm thay đổi đáp ứng độ cứng và ma sát trượt bao nhiêu phần trăm so với trạng thái tĩnh đẳng nhiệt?",
            "required_search_or_model_or_experiment": "Thử nghiệm uốn ở các tần số khác nhau (0.01 Hz đến 1 Hz) kết hợp đo nhiệt độ hồng ngoại.",
            "severity": "MEDIUM",
            "blocks_adjudication": False,
            "current_status": "OPEN_MONITORING_THREAT",
            "resolution_requirement": "Xác lập phạm vi tần số quasi-static mà ở đó hiệu ứng nhiệt tiềm ẩn có thể bỏ qua được.",
            "residual_risk": "Mô hình tĩnh có thể sai lệch khi áp dụng cho điều khiển robot chuyển động nhanh.",
            "human_review_required": False,
            "provenance": "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W09_REEDLUNN_2013_DEEP_AUDIT.md"
        }
    ]

print("Novelty Candidate Register defined: 1 candidate (MP1-P1)")
print("Unresolved Threat Register defined: 6 threats (THREAT-01 to THREAT-06)")
