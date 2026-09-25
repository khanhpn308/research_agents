import json

def get_crosswalk_entries():
    return [
        {
            "crosswalk_id": "CW-01",
            "packet_ids": ["W01", "W02", "W03", "W05"],
            "critique_id": "G01",
            "remediation_worker_ids": ["W07", "W02", "W03"],
            "initial_gap": "H0 bị định nghĩa mơ hồ và gộp chung; bác bỏ mô-đun hằng số bị đánh đồng với việc cần lý thuyết mới.",
            "remediation_action": "Tách H0 thành 3 tầng: H0a (đàn hồi hằng số - bị bác bỏ), H0b (khung NiTi + tiếp xúc Coulomb hiện hữu - chưa bị bác bỏ), và H1 (lý thuyết mới - chưa đủ bằng chứng).",
            "corrected_state": "H0a REFUTED; H0b NOT FALSIFIED; H1 INSUFFICIENT.",
            "residual_risk": "Các mô hình phần tử hữu hạn thương mại hiện hữu (Abaqus UMAT) vẫn có thể mô tả được bài toán uốn mà không cần công thức mới.",
            "status": "REPAIRED_WITH_RESIDUAL_RISK"
        },
        {
            "crosswalk_id": "CW-02",
            "packet_ids": ["W01", "W02", "W04", "W05", "W07"],
            "critique_id": "G02",
            "remediation_worker_ids": ["W05", "W02"],
            "initial_gap": "Áp suất chủ động P3 bị coi là một quy luật cơ học mới chỉ vì có khả năng điều khiển áp suất.",
            "remediation_action": "Chứng minh phương trình vi phân tiếp xúc hiện hữu tự nhiên tiếp nhận p(t); hạ cấp P3 thành giao thức điều khiển thực nghiệm (boundary condition).",
            "corrected_state": "P3 là điều kiện biên thay đổi theo thời gian; không tạo ra nguyên lý cơ học mới.",
            "residual_risk": "Trễ truyền áp động học chất lưu qua màng đàn hồi khi tần số biến thiên áp suất cao.",
            "status": "REPAIRED"
        },
        {
            "crosswalk_id": "CW-03",
            "packet_ids": ["W03", "W05", "W08"],
            "critique_id": "G03",
            "remediation_worker_ids": ["W06", "W03"],
            "initial_gap": "Chưa chứng minh chuyển pha siêu đàn hồi và trượt ma sát cùng hoạt động trong miền uốn dự kiến.",
            "remediation_action": "Phân tích định lượng ngưỡng trượt kappa_slip và ngưỡng chuyển pha kappa_tr; thiết lập điều kiện cần cho Miền Cùng Tồn Tại (uốn sâu góc gập lớn hoặc có lực kéo căng dọc trục).",
            "corrected_state": "Miền cùng tồn tại bị giới hạn nghiêm ngặt ở biến dạng lớn; ở biến dạng nhỏ cơ cấu thoái hóa về kẹt đàn hồi thông thường.",
            "residual_risk": "Khi vận hành ở biến dạng nhỏ, cơ cấu không tận dụng được hiệu ứng siêu đàn hồi và bị bao hàm bởi mô hình đàn hồi H0a.",
            "status": "REPAIRED_WITH_RESIDUAL_RISK"
        },
        {
            "crosswalk_id": "CW-04",
            "packet_ids": ["W08", "W10"],
            "critique_id": "G04",
            "remediation_worker_ids": ["W08"],
            "initial_gap": "Đường cong mô-men - độ cong uốn vĩ mô không thể nhận diện riêng rẽ các cơ chế vật lý vi mô bị chồng lấn.",
            "remediation_action": "Nghiêm cấm quy kết hiện tượng mềm hóa vĩ mô cho coupling NiTi; đưa vào yêu cầu bắt buộc đo biến trạng thái cục bộ (DIC, FBG, ảnh nhiệt, trượt đầu dây).",
            "corrected_state": "Đường cong vĩ mô không có tính nhận diện đơn nhất; bắt buộc phải có đối chứng cơ chế cục bộ.",
            "residual_risk": "Đo đạc cục bộ bên trong bó dây bọc kín dưới áp suất là thách thức kỹ thuật thực nghiệm cực kỳ lớn.",
            "status": "REPAIRED_WITH_RESIDUAL_RISK"
        },
        {
            "crosswalk_id": "CW-05",
            "packet_ids": ["W06", "W08"],
            "critique_id": "G05",
            "remediation_worker_ids": ["W04", "W03"],
            "initial_gap": "Gán nhầm chuyển pha NiTi uốn thuần cho cấu hình S2a trong bài báo của Carboni et al. 2015.",
            "remediation_action": "Kiểm tra trực tiếp tệp PDF Carboni 2015: S2a là cáp thép ST49 thuần trượt ma sát; S1a mới là cáp NiTi7 chịu kéo-uốn kết hợp. Sửa chữa dữ liệu 100%.",
            "corrected_state": "S2a là cáp thép; hiện tượng trễ thắt trên S1a gắn với kéo-uốn kết hợp có lực căng dọc trục, không phải uốn thuần.",
            "residual_risk": "Không còn rủi ro dữ liệu sai; văn hiến vẫn thiếu dữ liệu thực nghiệm về uốn thuần NiTi không lực căng.",
            "status": "REPAIRED"
        },
        {
            "crosswalk_id": "CW-06",
            "packet_ids": ["W06", "W10"],
            "critique_id": "G06",
            "remediation_worker_ids": ["W09"],
            "initial_gap": "Đánh đồng giữa việc tồn tại mô hình, khớp đường cong thực nghiệm và kiểm chứng độc lập (validation).",
            "remediation_action": "Xây dựng Thang bậc 5 tầng về độ tin cậy mô hình: Formulation -> Verification -> Calibration -> Locked Validation -> Causal Identification.",
            "corrected_state": "Khớp số liệu chỉ là Calibration (Tầng 3); Validation (Tầng 4) bắt buộc phải khóa tham số trên tập dữ liệu độc lập.",
            "residual_risk": "Mô hình mới đề xuất trong luận văn phải đạt tối thiểu Tầng 4 mới được xem là đóng góp khoa học đáng tin cậy.",
            "status": "REPAIRED"
        },
        {
            "crosswalk_id": "CW-07",
            "packet_ids": ["W09"],
            "critique_id": "G07",
            "remediation_worker_ids": ["W10", "W07"],
            "initial_gap": "Dùng sự sai lệch của mô hình động học cáp xoắn Costello trong Reedlunn 2013 để suy diễn nhu cầu luật cơ học mới cho bó dây thẳng.",
            "remediation_action": "Áp dụng nguyên tắc trích dẫn bảo thủ; làm rõ sai số trong Reedlunn do bỏ qua uốn/xoắn cục bộ của sợi cáp xoắn dốc ở lớp ngoài, không áp dụng cho bó dây thẳng.",
            "corrected_state": "Reedlunn 2013 chỉ phản ánh giới hạn động học thanh xoắn Costello; không chứng minh sự thiếu hụt lý thuyết trong bó dây thẳng.",
            "residual_risk": "Không còn rủi ro suy diễn vượt phạm vi.",
            "status": "REPAIRED"
        },
        {
            "crosswalk_id": "CW-08",
            "packet_ids": ["W10"],
            "critique_id": "G08",
            "remediation_worker_ids": ["W09", "W08", "W10"],
            "initial_gap": "Hiện tượng bù trừ tham số giữa hệ số ma sát và tỷ lệ truyền áp lực làm mất tính duy nhất của nghiệm khớp uốn.",
            "remediation_action": "Thiết lập Quy tắc Khóa tham số tuyệt đối (Locked Calibration Rule): Đo độc lập mu và tỷ lệ truyền áp ngoài bài toán uốn; cấm thả nổi tham số ép khớp đường cong.",
            "corrected_state": "Mọi tham số ma sát và cơ học tiếp xúc phải được khóa chặt từ các thử nghiệm độc lập trước khi chạy mô hình uốn.",
            "residual_risk": "Sai số trong các phép đo độc lập vẫn có thể lan truyền và ảnh hưởng đến độ chính xác của mô hình uốn.",
            "status": "REPAIRED_WITH_RESIDUAL_RISK"
        },
        {
            "crosswalk_id": "CW-09",
            "packet_ids": ["W04", "W07"],
            "critique_id": "G09",
            "remediation_worker_ids": ["W08", "W05"],
            "initial_gap": "Giả định đơn giản hóa rằng áp suất buồng khí chuyển hóa 100% thành lực nén pháp tuyến giữa các sợi dây.",
            "remediation_action": "Bổ sung chuỗi truyền áp lực: Áp suất buồng p bị suy giảm qua độ cứng vòng của màng bao và hiệu ứng vòm (arching) của bó dây trước khi thành f_n; yêu cầu đo đạc độc lập.",
            "corrected_state": "Lực pháp tuyến thực tế chịu suy giảm hình học; bắt buộc phải hiệu chuẩn chuỗi truyền áp lực độc lập.",
            "residual_risk": "Hiệu ứng vòm biến đổi phi tuyến theo độ cong uốn của dầm.",
            "status": "REPAIRED_WITH_RESIDUAL_RISK"
        },
        {
            "crosswalk_id": "CW-10",
            "packet_ids": ["W05", "W07", "W10", "W11"],
            "critique_id": "G10",
            "remediation_worker_ids": ["W11", "W01"],
            "initial_gap": "Tuyên bố khoảng trống nghiên cứu đã được xác lập chắc chắn dù chưa đạt điều kiện dừng tìm kiếm.",
            "remediation_action": "Minh bạch hóa việc stop_condition_satisfied = false; định danh khoảng trống đề xuất là một giả thuyết còn sống sót tạm thời (PROVISIONALLY SURVIVING HYPOTHESIS).",
            "corrected_state": "Khoảng trống chỉ có tính tạm thời trong phạm vi tập tài liệu đã duyệt; không khẳng định tính mới tuyệt đối.",
            "residual_risk": "Văn hiến cơ học kết cấu rộng lớn hơn có thể chứa đựng các mô hình tương tự làm sụp đổ giả thuyết.",
            "status": "REPAIRED"
        },
        {
            "crosswalk_id": "CW-11",
            "packet_ids": ["W08", "W11"],
            "critique_id": "G11",
            "remediation_worker_ids": ["W07", "W01"],
            "initial_gap": "Xung đột giữa việc Audit JSON ghi nhận 'established' và báo cáo phản biện ghi nhận 'insufficient'.",
            "remediation_action": "Bảo tồn provenance của tệp JSON; làm rõ trong báo cáo rằng nhãn 'established' áp dụng cho việc loại bỏ H0a; trạng thái khoa học giữa H0b và H1 là 'insufficient'.",
            "corrected_state": "Hòa giải ngữ nghĩa minh bạch; loại bỏ mâu thuẫn giữa dữ liệu máy và phân tích chuyên gia.",
            "residual_risk": "Không còn rủi ro xung đột ngữ nghĩa.",
            "status": "REPAIRED"
        },
        {
            "crosswalk_id": "CW-12",
            "packet_ids": ["W06", "W07", "W08"],
            "critique_id": "G12",
            "remediation_worker_ids": ["W08"],
            "initial_gap": "Sử dụng thuật ngữ 'độ cứng uốn' một cách mơ hồ mà không chỉ rõ lịch sử tải trọng và nhánh tải.",
            "remediation_action": "Chuẩn hóa 3 định nghĩa toán học: D_tan (độ cứng tiếp tuyến phụ thuộc đạo hàm chuyển vị và nhánh tải/dỡ tải), D_sec (độ cứng cát tuyến), và D_dyn (độ cứng động học).",
            "corrected_state": "Mọi kết luận về độ cứng uốn bắt buộc phải ghi rõ đại lượng toán học tương ứng.",
            "residual_risk": "Không còn rủi ro mơ hồ toán học.",
            "status": "REPAIRED"
        }
    ]

def get_contradiction_candidates():
    return [
        {
            "contradiction_candidate_id": "CONTRA-01",
            "source_A": "docs/project/MP1-V002_CURRENT_HANDOFF.md (commit bf0b79a) và W01-W11 packets (commit af9e7a5)",
            "source_B": "outputs/verification/MP1-V002/verification_matrix.json (commit 8ccfa3c) và W01 Remediation (commit 3a216d6)",
            "packet_ids_affected": ["W01", "W05", "W11"],
            "critique_ids_affected": ["G10", "G11"],
            "remediation_worker_ids_affected": ["W01", "W11"],
            "historical_context": "Trong giai đoạn đầu của Stage 1, số lượng bài báo toàn văn được viện dẫn không nhất quán (ghi 10 bài báo trong một số báo cáo, 13 bài trong ma trận đĩa, và 16 bài trong verification matrix chính tắc tại HEAD).",
            "difference": "10 bài báo toàn văn (Stage 1 ban đầu) so với 13 bài báo so với 16 bài báo toàn văn chính tắc.",
            "why_it_matters": "Ảnh hưởng trực tiếp đến tính đầy đủ của việc thẩm tra tính tiền nhiệm; nếu chỉ dựa trên 10 bài thì bỏ sót các bài báo đe dọa trọng yếu như Barsi 2025 và Kang 2020.",
            "resolution_status": "RECONCILED",
            "recommended_owner": "W2-06-12 / final synthesis auditor"
        },
        {
            "contradiction_candidate_id": "CONTRA-02",
            "source_A": "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json dòng 237-241 (commit 8ccfa3c)",
            "source_B": "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md (commit 8ccfa3c) và W07 Remediation (commit 3a216d6)",
            "packet_ids_affected": ["W08", "W10"],
            "critique_ids_affected": ["G01", "G11"],
            "remediation_worker_ids_affected": ["W07", "W01"],
            "historical_context": "Tệp Audit JSON ghi 'niti_requires_distinct_constitutive_contact_coupling = true' với evidence_status = 'established', trong khi báo cáo phản biện của Astra và W10 kết luận bằng chứng là 'insufficient'.",
            "difference": "Xung đột ngữ nghĩa giữa 'established' (đã xác lập) và 'insufficient' (chưa đủ bằng chứng).",
            "why_it_matters": "Nếu tuyên bố là 'established' thì ngộ nhận rằng H1 đã được chứng minh và không cần làm thí nghiệm đối chứng; nếu là 'insufficient' thì đây mới chỉ là một giả thuyết mở cần kiểm chứng.",
            "resolution_status": "RECONCILED",
            "recommended_owner": "W2-06-12 / final synthesis auditor"
        },
        {
            "contradiction_candidate_id": "CONTRA-03",
            "source_A": "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md (commit af9e7a5)",
            "source_B": "papers/verification/MP1-V002/A1-2015.pdf Table 4 (Carboni 2015) và W04 Remediation (commit 3a216d6)",
            "packet_ids_affected": ["W06", "W08"],
            "critique_ids_affected": ["G05"],
            "remediation_worker_ids_affected": ["W04", "W03"],
            "historical_context": "Packet W08 khẳng định cấu hình S2a trong bài báo của Carboni 2015 là bằng chứng thực nghiệm về chuyển pha siêu đàn hồi NiTi dưới uốn thuần.",
            "difference": "Sai sót dữ liệu thực tế: Cấu hình S2a là ST49 (cáp thép 49 sợi thuần ma sát); chỉ có S1a là cáp NiTi7 nhưng chịu tải kéo-uốn kết hợp.",
            "why_it_matters": "Lập luận về chuyển pha uốn thuần bị sụp đổ hoàn toàn về mặt bằng chứng thực nghiệm; không thể dùng S2a để biện minh cho cơ chế uốn NiTi.",
            "resolution_status": "REPAIRED",
            "recommended_owner": "W2-06-12 / final synthesis auditor"
        },
        {
            "contradiction_candidate_id": "CONTRA-04",
            "source_A": "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W11_CITATION_COVERAGE_AND_SOURCE_INTEGRITY.md (commit af9e7a5)",
            "source_B": "outputs/verification/MP1-V002/citation_coverage.json (commit 8ccfa3c) và W11 Remediation (commit 3a216d6)",
            "packet_ids_affected": ["W05", "W07", "W11"],
            "critique_ids_affected": ["G10"],
            "remediation_worker_ids_affected": ["W11", "W01"],
            "historical_context": "Lời văn tổng hợp trong một số báo cáo Stage 1 khẳng định khoảng trống cơ học đã được xác lập chắc chắn vì không tìm thấy bài báo nào trong tập rà soát, trong khi tệp canonical coverage JSON ghi rõ stop_condition_satisfied = false.",
            "difference": "Khẳng định khoảng trống chắc chắn vs thừa nhận điều kiện dừng chưa đạt.",
            "why_it_matters": "Vi phạm nguyên tắc phương pháp luận khoa học: Chưa thỏa mãn điều kiện dừng mà đã kết luận phủ định sự tồn tại của văn hiến tiền nhiệm.",
            "resolution_status": "REPAIRED",
            "recommended_owner": "W2-06-12 / final synthesis auditor"
        },
        {
            "contradiction_candidate_id": "CONTRA-05",
            "source_A": "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md (commit af9e7a5)",
            "source_B": "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md (commit 8ccfa3c) và W05 Remediation (commit 3a216d6)",
            "packet_ids_affected": ["W01", "W04", "W07"],
            "critique_ids_affected": ["G02", "G09"],
            "remediation_worker_ids_affected": ["W05", "W08"],
            "historical_context": "Packet W07 phân loại áp suất P3 là một nhánh cơ học mới có khả năng tạo ra tính mới khoa học độc lập.",
            "difference": "Áp suất chủ động là nguyên lý cơ học mới vs áp suất chủ động là điều kiện biên thay đổi theo thời gian.",
            "why_it_matters": "Nếu coi P3 là cơ học mới thì luận văn sẽ bị phản biện bác bỏ vì phương trình vi phân tiếp xúc hiện hữu đã tiếp nhận p(t) một cách tự nhiên.",
            "resolution_status": "REPAIRED",
            "recommended_owner": "W2-06-12 / final synthesis auditor"
        },
        {
            "contradiction_candidate_id": "CONTRA-06",
            "source_A": "docs/project/MP1-V002_CURRENT_HANDOFF.md (commit bf0b79a)",
            "source_B": "outputs/verification/D1-V001/direction_verification.json và Master Plan",
            "packet_ids_affected": ["W01"],
            "critique_ids_affected": [],
            "remediation_worker_ids_affected": ["W01", "W02"],
            "historical_context": "Trạng thái đề tài MP1 được ghi nhận là một hướng nghiên cứu khả thi đang kiểm chứng (viable alternative candidate), nhưng đôi khi bị hiểu nhầm là đã được phê duyệt làm đề tài luận văn chính thức thay thế D1.",
            "difference": "Hướng ứng viên dự phòng đang kiểm chứng đe dọa vs đề tài luận văn đã được phê duyệt chính thức.",
            "why_it_matters": "Quyết định lựa chọn đề tài thuộc thẩm quyền của final adjudication sau khi hoàn tất kiểm toán đe dọa; không được vượt quyền hạn trong giai đoạn tái dựng bằng chứng.",
            "resolution_status": "RECONCILED",
            "recommended_owner": "W2-06-12 / final synthesis auditor"
        }
    ]

print("Crosswalk entries defined: 12")
print("Contradictions defined: 6")
