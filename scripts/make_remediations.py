import json

def get_remediation_workers():
    return [
        {
            "worker_id": "W01",
            "worker_question": "Làm thế nào để đồng bộ và đối soát hiện trạng bằng chứng tại commit HEAD so với các packet Stage 1, khắc phục độ trễ trạng thái (stale state) và định lượng chính xác tập bài báo kiểm chứng MP1-V002?",
            "input_sources": [
                "outputs/verification/MP1-V002/verification_matrix.json (commit 8ccfa3c)",
                "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json (commit 8ccfa3c)",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/00_PACKET_MANIFEST.md (commit af9e7a5)"
            ],
            "papers_reviewed": [
                "00414aac4b", "fac21c950e", "40760daa02", "2f7fcf2f8f", "7f3f45407f",
                "1c81b2d35c", "9f4295be23", "56793dea9b", "d9966f2f5e", "9e15094d68",
                "53200aa0c6", "98fee47c04", "aaad9c248c", "ccdc1bb980", "e8462758c3", "6dd1ca94d1"
            ],
            "claims_repaired": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
            "targets_repaired": ["T1", "T2", "T3"],
            "hypotheses_repaired": ["H0a", "H0b", "H1"],
            "related_critique_ids": ["G10", "G11"],
            "evidence_produced": "Đối soát thành công 16 bài báo toàn văn chính tắc trên đĩa tại HEAD, lập bảng ánh xạ sự phát triển từ 10 bài ban đầu lên 13 bài và hoàn thiện 16 bài.",
            "result": "Khắc phục triệt để độ trễ trạng thái; xác lập con số 16 bài báo toàn văn chính tắc là cơ sở đối soát của Stage 3; làm rõ trạng thái dừng trích dẫn chưa đạt.",
            "remaining_uncertainty": "Nhánh trích dẫn ngược B11 và B12 cần được hoàn tất đầy đủ ở các bước kiểm toán tiếp theo.",
            "corrected_interpretation": "Hòa giải rõ ràng sự khác biệt giữa các tài liệu lịch sử; loại bỏ mọi giả định vội vàng về việc đóng tập bằng chứng.",
            "evidence_status": "reconciled_at_head",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W01_STATE_RECONCILIATION.md#L1-L180"
        },
        {
            "worker_id": "W02",
            "worker_question": "Làm thế nào để xác lập tính vững chắc của các phán quyết đóng đối với C1–C4 và ngăn chặn việc diễn giải quá phạm vi (overclaim)?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W01_ORIGINAL_ARCHITECTURE_AND_V001_DECISION.md",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W02_C1_C2_EVIDENCE.md",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W03_C3_SMA_JAMMING_LINEAGE.md",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md"
            ],
            "papers_reviewed": ["240fbf6022", "182d854610", "3aa8790db0", "2cd907e77a", "bbe88a0c04", "c6a31066f8", "de64029540", "55457a97c6"],
            "claims_repaired": ["C1", "C2", "C3", "C4"],
            "targets_repaired": ["T1", "T2"],
            "hypotheses_repaired": ["H0a"],
            "related_critique_ids": ["G01", "G02"],
            "evidence_produced": "Bảng tổng hợp đối soát khẳng định tính vững chắc của các phán quyết: C1 (wire jamming) đóng bởi Bai 2022; C2 (áp suất dương) đóng bởi Liu 2021; C3 (SMA jamming) đón đầu bởi Takashima; C4 (nguồn áp suất) đóng bởi Huynh 2022 và Wang 2024.",
            "result": "Xác nhận 100% phán quyết đóng các khẳng định kiến trúc cấp thiết bị; khóa chặt không cho phép mở lại hay tuyên bố tính mới trên C1–C4.",
            "remaining_uncertainty": "Không có tính bất định về việc đóng C1–C4; câu hỏi mở duy nhất là hành vi cơ học vi mô của vật liệu trong cơ cấu.",
            "corrected_interpretation": "C1–C4 hoàn toàn không có tính mới khoa học; mọi nỗ lực bảo vệ tính mới cấp thiết bị đều bị bác bỏ.",
            "evidence_status": "firmly_closed_with_strict_bounds",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W02_C1_C4_ROBUST_CLOSURES.md#L1-L150"
        },
        {
            "worker_id": "W03",
            "worker_question": "Làm thế nào để sửa chữa ranh giới cơ học C5–C8, loại bỏ các lập luận tạo khoảng trống giả (false gap rhetoric), và phân biệt giữa giới hạn kho dữ liệu và tính mới bản chất?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W05_C5_C6_C7_V001_BOUNDARY.md",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "papers_reviewed": ["240fbf6022", "182d854610", "2cd907e77a", "c6a31066f8", "3aa8790db0", "55457a97c6"],
            "claims_repaired": ["C5", "C6", "C7", "C8"],
            "targets_repaired": ["T1", "T2", "T3"],
            "hypotheses_repaired": ["H0a", "H0b", "H1"],
            "related_critique_ids": ["G01", "G03", "G05"],
            "evidence_produced": "Tái định nghĩa ranh giới cơ học: C5 (ma sát trượt NiTi) đã bị đón đầu một phần; C6 (áp suất giam giữ) chuyển thành điều kiện biên; C7 (ghép cặp) chỉ có ý nghĩa nếu chứng minh được vùng cùng tồn tại; C8 loại bỏ hoàn toàn.",
            "result": "Xóa bỏ thuật ngữ tạo khoảng trống giả; chuyển từ 'đã tìm thấy khoảng trống' sang 'thiết lập giả thuyết kiểm chứng có điều kiện'.",
            "remaining_uncertainty": "Khả năng tồn tại các công trình tương tự trong cơ học kết cấu hàng hải hoặc địa kỹ thuật chưa được sàng lọc.",
            "corrected_interpretation": "Sự vắng mặt trong tập V001 là giới hạn của tập tài liệu ban đầu, không phải bằng chứng về tính mới phổ quát.",
            "evidence_status": "boundary_repaired_and_debiased",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W03_C5_C8_BOUNDARY_REPAIR.md#L1-L145"
        },
        {
            "worker_id": "W04",
            "worker_question": "Làm thế nào để tái kiểm chứng Mục tiêu T1 và đính chính triệt để sai sót thực tế về cấu hình S2a của Carboni et al. (2015) theo phê bình G05?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W06_T1_NITI_CONTACT_FRICTION.md",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md",
                "papers/verification/MP1-V002/A1-2015.pdf (Carboni et al. 2015, d9966f2f5e)"
            ],
            "papers_reviewed": ["d9966f2f5e", "53200aa0c6", "98fee47c04", "fac21c950e"],
            "claims_repaired": ["C5", "C7"],
            "targets_repaired": ["T1", "T3"],
            "hypotheses_repaired": ["H0b", "H1"],
            "related_critique_ids": ["G05"],
            "evidence_produced": "Trích xuất trực tiếp Bảng 4 và các trang 9–10 trong Carboni 2015 PDF: S2a = ST49 (cáp thép 49 sợi, thuần trượt ma sát); S1a = NiTi7 (7 sợi NiTi chịu kéo-uốn kết hợp).",
            "result": "Sửa chữa 100% sai sót dữ liệu thực tế; xóa bỏ nhận định sai rằng Carboni đã chứng minh chuyển pha dưới uốn thuần; xác định S1a chỉ chứng minh kéo-uốn kết hợp.",
            "remaining_uncertainty": "Hành vi uốn thuần túy của bó dây NiTi không có lực kéo căng dọc trục vẫn chưa có dữ liệu thực nghiệm trực tiếp trong văn hiến.",
            "corrected_interpretation": "S2a là cáp thép; hiện tượng trễ thắt trên S1a gắn liền với lực kéo hình học lớn; không thể suy diễn cho uốn thuần tự do.",
            "evidence_status": "factual_error_repaired",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W04_T1_REAUDIT_CARBONI_CORRECTION.md#L1-L160"
        },
        {
            "worker_id": "W05",
            "worker_question": "Làm thế nào để kiểm chứng xem các phương trình vi phân tiếp xúc dầm hiện hữu có thể tự nhiên tiếp nhận lịch sử áp suất biến thiên p(t) mà không cần phương trình mới hay không?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md",
                "papers/verification/MP1-V002/2017-Submarine Cable Bending Mechanics_ccdc1bb980.pdf (Tjahjanto 2017)",
                "papers/verification/MP1-V002/2004-Internal Friction of Cables_aaad9c248c.pdf (Xin Liu 2004)"
            ],
            "papers_reviewed": ["ccdc1bb980", "aaad9c248c", "9f4295be23", "53200aa0c6"],
            "claims_repaired": ["C6"],
            "targets_repaired": ["T2"],
            "hypotheses_repaired": ["H0b", "H1"],
            "related_critique_ids": ["G02", "G09"],
            "evidence_produced": "Chứng minh toán học rằng phương trình cân bằng tiếp xúc vi phân dq/dx = -mu * fn(p) tiếp nhận p = p(t) một cách tự nhiên trong công thức gia số tải; không xuất hiện số hạng vi phân mới đối với thời gian nếu bỏ qua quán tính chất lưu.",
            "result": "Hạ cấp dứt điểm P3: P1/P2/P3 là phân loại giao thức điều khiển thực nghiệm (boundary conditions), không phải ba lớp lý thuyết cơ học riêng biệt.",
            "remaining_uncertainty": "Ảnh hưởng động học trễ của áp suất qua màng nhớt đàn hồi khi tần số biến thiên áp suất cao.",
            "corrected_interpretation": "Áp suất chủ động p(t) là một điều kiện biên ngoại vi; không tạo ra một định luật cơ học mới.",
            "evidence_status": "p3_reclassified_as_boundary_condition",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W05_T2_MECHANICS_P1_P2_P3_TEST.md#L1-L155"
        },
        {
            "worker_id": "W06",
            "worker_question": "Làm thế nào để phân tích định lượng điều kiện vật lý cần thiết để hiện tượng chuyển pha siêu đàn hồi và trượt ma sát giữa các dây cùng kích hoạt trong bó dây NiTi chịu uốn?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W06_T1_NITI_CONTACT_FRICTION.md"
            ],
            "papers_reviewed": ["fac21c950e", "d9966f2f5e", "53200aa0c6", "3aa8790db0"],
            "claims_repaired": ["C7"],
            "targets_repaired": ["T3"],
            "hypotheses_repaired": ["H0b", "H1"],
            "related_critique_ids": ["G03"],
            "evidence_produced": r"Phân tích cơ học dầm nhiều sợi: Ngưỡng trượt ma sát kappa_slip = 2 mu p / (E A h); ngưỡng bắt đầu chuyển pha kappa_tr = 2 sigma_tr / (E_A D_bundle). Tính toán cho thấy ở biến dạng nhỏ epsilon < 0.75%, NiTi thuần đàn hồi Austenite và chỉ có trượt ma sát thông thường.",
            "result": "Thiết lập điều kiện cần cho Miền Cùng Tồn Tại (Coexistence Domain): Chỉ khi dầm bị uốn cong sâu vượt quá kappa_tr hoặc có kéo căng dọc trục thì chuyển pha và trượt mới tương tác; ở biến dạng nhỏ bài toán thoái hóa về dầm đàn hồi thông thường.",
            "remaining_uncertainty": "Sự phân bố ứng suất tiếp xúc không đều giữa các sợi bên trong và bên ngoài làm chuyển pha xảy ra cục bộ từng sợi.",
            "corrected_interpretation": "Cơ chế ghép cặp không tồn tại phổ quát mà phụ thuộc chặt chẽ vào biên độ tải trọng uốn.",
            "evidence_status": "coexistence_domain_bounded",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W06_T3_TRANSFORMATION_SLIP_COEXISTENCE.md#L1-L170"
        },
        {
            "worker_id": "W07",
            "worker_question": "Làm thế nào để tái cấu trúc hệ thống giả thuyết H0/H1 thành 3 tầng chặt chẽ và hòa giải xung đột trạng thái giữa Audit JSON và báo cáo tổng hợp?",
            "input_sources": [
                "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json (commit 8ccfa3c)",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "papers_reviewed": ["2f7fcf2f8f", "53200aa0c6", "fac21c950e"],
            "claims_repaired": ["C7"],
            "targets_repaired": ["T3"],
            "hypotheses_repaired": ["H0a", "H0b", "H1"],
            "related_critique_ids": ["G01", "G07", "G11"],
            "evidence_produced": "Tách H0 thành: H0a (thay thế mô-đun đàn hồi hằng số), H0b (khung lý thuyết NiTi cấu thành phi tuyến + tiếp xúc Coulomb hiện hữu), và H1 (lý thuyết ghép cặp vi mô mới). Phân tích nguồn gốc nhãn 'established' trong JSON.",
            "result": "Hòa giải thành công: Bác bỏ H0a là 'established'; nhưng H0b chưa bị bác bỏ ('not falsified') và H1 là 'insufficient'. Loại bỏ hoàn toàn sự mâu thuẫn giữa JSON và narrative.",
            "remaining_uncertainty": "Cần thiết kế thí nghiệm đối chứng có khả năng phân biệt dứt điểm giữa dự đoán của H0b và H1.",
            "corrected_interpretation": "Bác bỏ mô hình đàn hồi sơ đẳng H0a không phải là bằng chứng ủng hộ H1.",
            "evidence_status": "hypotheses_restructured_and_reconciled",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md#L1-L175"
        },
        {
            "worker_id": "W08",
            "worker_question": "Làm thế nào để xác định giới hạn nhận diện thực nghiệm (identifiability limits), phân tách cơ chế bị chồng lấn trong dữ liệu uốn vĩ mô, và chuẩn hóa định nghĩa độ cứng uốn?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "papers_reviewed": ["d9966f2f5e", "9f4295be23", "3aa8790db0", "ccdc1bb980"],
            "claims_repaired": ["C6", "C7"],
            "targets_repaired": ["T2", "T3"],
            "hypotheses_repaired": ["H1"],
            "related_critique_ids": ["G04", "G09", "G12"],
            "evidence_produced": r"Phân tích chuỗi nhận diện thực nghiệm: (1) Đường cong M-kappa vĩ mô không có tính nhận diện đơn nhất; (2) Chuỗi truyền áp suất p -> f_n chịu hiệu ứng vòm (arching); (3) Chuẩn hóa 3 công thức toán học cho D_tan, D_sec, D_dyn.",
            "result": "Thiết lập yêu cầu bắt buộc: Phải dùng cảm biến cục bộ (DIC, FBG, ảnh nhiệt) để đo trực tiếp trượt và biến dạng sợi; cấm dùng dữ liệu uốn vĩ mô để tuyên bố cơ chế mới.",
            "remaining_uncertainty": "Khó khăn trong việc tích hợp cảm biến đo quang FBG vào bên trong bó dây bọc kín dưới áp suất cao.",
            "corrected_interpretation": "Hiện tượng mềm hóa uốn vĩ mô có thể do nhiều nguyên nhân cơ học gây ra; không thể gán đơn nhất cho cơ chế NiTi.",
            "evidence_status": "identifiability_bounds_formalized",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md#L1-L165"
        },
        {
            "worker_id": "W09",
            "worker_question": "Làm thế nào để xây dựng thang bậc độ tin cậy mô hình và giải quyết hiện tượng bù trừ tham số (parameter confounding) trong bài toán khớp uốn?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "papers_reviewed": ["2f7fcf2f8f", "9e15094d68", "53200aa0c6"],
            "claims_repaired": ["C7"],
            "targets_repaired": ["T1", "T2", "T3"],
            "hypotheses_repaired": ["H0b", "H1"],
            "related_critique_ids": ["G06", "G08"],
            "evidence_produced": r"Xây dựng Thang bậc 5 tầng: T1 (Formulation) -> T2 (Verification số) -> T3 (Calibration khớp đường cong) -> T4 (Validation với tham số bị khóa) -> T5 (Nhận diện nhân quả). Phân tích tích số mu * alpha_trans.",
            "result": "Ban hành Quy tắc Khóa tham số tuyệt đối (Locked Calibration Rule): Cấm thả nổi tham số ma sát và truyền lực để ép khớp đường cong uốn; yêu cầu kiểm tra tính duy nhất của nghiệm.",
            "remaining_uncertainty": "Mức độ nhạy của mô hình đối với sai số đo đạc thực nghiệm các tham số vật liệu độc lập.",
            "corrected_interpretation": "Khớp đường cong thực nghiệm chỉ đạt Tầng 3; một mô hình chỉ có giá trị khoa học kiểm chứng khi đạt Tầng 4 và Tầng 5.",
            "evidence_status": "model_credibility_hierarchy_established",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W09_MODEL_VALIDATION_CREDIBILITY.md#L1-L185"
        },
        {
            "worker_id": "W10",
            "worker_question": "Làm thế nào để diễn giải bảo thủ các kết quả của Reedlunn et al. (2013) và Fang et al. (2019), ngăn chặn việc suy diễn sai lệch phạm vi cơ học?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W09_REEDLUNN_2013_DEEP_AUDIT.md",
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "papers_reviewed": ["fac21c950e", "2f7fcf2f8f"],
            "claims_repaired": ["C7"],
            "targets_repaired": ["T3"],
            "hypotheses_repaired": ["H0b", "H1"],
            "related_critique_ids": ["G07", "G08"],
            "evidence_produced": "Phân tích giới hạn động học trong Reedlunn: Thất bại của mô hình Costello xuất phát từ góc xoắn dốc ở lớp ngoài cáp 1x27 bỏ qua uốn/xoắn cục bộ. Phân tích mô hình sợi Fang: OpenSees bỏ qua ma sát tiếp xúc vi mô cục bộ.",
            "result": "Khắc phục triệt để các suy diễn quá đà: Không dùng lỗi động học của cáp xoắn để biện hộ cho nhu cầu lý thuyết bó dây thẳng; thừa nhận khả năng mô phỏng vĩ mô tốt của mô hình sợi OpenSees.",
            "remaining_uncertainty": "Khả năng mở rộng mô hình sợi OpenSees sang bài toán có áp suất pháp tuyến biến thiên lớn.",
            "corrected_interpretation": "Cả hai công trình đều có phạm vi hiệu lực riêng biệt; không được bóp méo kết quả của tác giả tiền nhiệm để tạo khoảng trống nghiên cứu giả.",
            "evidence_status": "conservative_interpretation_enforced",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W10_REEDLUNN_FANG_CONSERVATIVE_REMEDIATION.md#L1-L150"
        },
        {
            "worker_id": "W11",
            "worker_question": "Làm thế nào để đánh giá khách quan trạng thái bao phủ trích dẫn, xử lý việc chưa đạt điều kiện dừng tìm kiếm, và bảo toàn tính toàn vẹn dữ liệu nguồn?",
            "input_sources": [
                "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W11_CITATION_COVERAGE_AND_SOURCE_INTEGRITY.md",
                "outputs/verification/MP1-V002/citation_coverage.json (commit 8ccfa3c)",
                "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md"
            ],
            "papers_reviewed": ["00414aac4b", "fac21c950e", "40760daa02", "2f7fcf2f8f", "7f3f45407f", "1c81b2d35c", "9f4295be23", "56793dea9b", "d9966f2f5e", "9e15094d68", "53200aa0c6", "98fee47c04", "aaad9c248c", "ccdc1bb980", "e8462758c3", "6dd1ca94d1"],
            "claims_repaired": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
            "targets_repaired": ["T1", "T2", "T3"],
            "hypotheses_repaired": ["H0a", "H0b", "H1"],
            "related_critique_ids": ["G10", "G11"],
            "evidence_produced": "Đối soát 15 hướng trích dẫn bắt buộc; xác nhận điều kiện dừng chưa thỏa mãn (stop_condition_satisfied = false); thiết lập cơ chế ghi nhận tính mới thận trọng.",
            "result": "Chuyển toàn bộ các phát biểu về 'khoảng trống nghiên cứu' thành 'giả thuyết còn sống sót tạm thời' (PROVISIONALLY SURVIVING HYPOTHESIS); nghiêm cấm kết luận tính mới tuyệt đối.",
            "remaining_uncertainty": "Các nhánh trích dẫn sâu hơn có thể tiếp tục thu hẹp hoặc bác bỏ giả thuyết còn lại.",
            "corrected_interpretation": "Tính mới chỉ có giá trị tương đối trong phạm vi tập bằng chứng đã khảo sát; quy trình kiểm chứng phải mở và sẵn sàng bị phản biện.",
            "evidence_status": "stop_condition_transparently_acknowledged",
            "confidence": "high",
            "provenance": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W11_CITATION_COVERAGE_QA.md#L1-L140"
        }
    ]

print("Remediation workers defined: 11")
