# Sổ bộ Ứng viên Tính mới Đề tài MP1 (MP1 Novelty Candidate Register)

> **Tệp chính tắc:** `MP1_NOVELTY_CANDIDATE_REGISTER.json`  
> **Ứng viên:** `MP1-P1`  
> **Trạng thái ứng viên:** `PENDING_GATE` (Tạm thời; chưa chạy cổng K1–K9)  
> **Trạng thái phán quyết:** `DEFERRED` (Được hoãn lại cho công đoạn thẩm tra cuối)  

## 1. Phát biểu Ứng viên Tính mới Khoa học
**Mô hình cơ học ghép cặp cấu thành – tiếp xúc giữa chuyển pha Martensite cảm ứng ứng suất và ma sát trượt Coulomb nội tại trong bó dây NiTi siêu đàn hồi chịu áp suất giam giữ pháp tuyến chủ động.**

- **Xuất xứ lịch sử:** Chuyển dịch từ đề xuất kiến trúc thiết bị ban đầu của mentor (C1–C8) sau khi tính mới linh kiện sụp đổ tại MP1-V001; định hình lại thành Mechanics Core (C5–C7, T1–T3) và được tái cấu trúc bảo thủ qua phản biện Astra Stage 2–3.
- **Phân loại khoa học:** Cơ học vật rắn biến dạng / Cơ học tiếp xúc và cấu thành vật liệu thông minh (Solid & Contact Mechanics of Active Materials)
- **Nhóm tính mới:** `Coupled Constitutive-Contact Mechanics in Confined Active Bundles`
- **Khẳng định liên quan:** C5, C6, C7 | **Mục tiêu:** T2, T3 | **Giả thuyết:** H0b, H1

## 2. Bằng chứng Ủng hộ và Bằng chứng Phản biện
- **Bằng chứng ủng hộ:** Reedlunn et al. 2013 (fac21c950e) chứng minh ngưỡng chuyển pha dịch chuyển dưới áp lực tiếp xúc hướng tâm; Vahidi et al. 2022 (53200aa0c6) mô hình hóa ma sát tiếp xúc dây NiTi; Báo cáo khắc phục Stage 3 (W06) xác lập điều kiện cần cho Miền Cùng Tồn Tại ở góc uốn lớn.
- **Bằng chứng phản biện / Đe dọa:** Fang et al. 2019 (2f7fcf2f8f) chứng minh mô hình hiện tượng học rút gọn không cần tiếp xúc vi mô vẫn khớp được trễ vĩ mô; Khung lý thuyết NiTi phi tuyến + tiếp xúc Coulomb trong Abaqus UMAT (H0b) chưa bị bác bỏ; Sai sót lịch sử về Carboni S2a bị lật tẩy là cáp thép.
- **Chồng lấn văn hiến tiền nhiệm:** Bị đón đầu ở cấp thiết bị về wire jamming (Bai 2022), áp suất dương (Liu 2021), tích hợp SMA (Takashima 2022), cáp xoắn chịu kéo trục (Reedlunn 2013), và giảm chấn cáp vĩ mô (Fang 2019).

## 3. Các Ràng buộc và Điều kiện Bắt buộc
- **Quan hệ với giả thuyết $H_0$:** H0a (mô-đun đàn hồi hằng số) đã bị BÁC BỎ (REFUTED); H0b (khung NiTi phi tuyến + tiếp xúc Coulomb hiện hữu) CHƯA BỊ BÁC BỎ (NOT FALSIFIED); H1 (nhu cầu về luật ghép cặp vi mô mới) CHƯA ĐỦ BẰNG CHỨNG (INSUFFICIENT).
- **Yêu cầu về Miền Cùng Tồn Tại (Coexistence Requirement):** Bắt buộc phải vận hành ở độ cong uốn lớn kappa > kappa_tr ~ 0.75% hoặc có lực căng dọc trục đáng kể để đồng thời kích hoạt chuyển pha và trượt ma sát giữa các sợi dây.
- **Yêu cầu về Khả năng Nhận diện Thực nghiệm (Identifiability Requirement):** Bắt buộc phải đo biến trạng thái cục bộ (DIC đo biến dạng mặt ngoài sợi, FBG đo biến dạng lõi, ảnh nhiệt hồng ngoại, cảm biến trượt đầu dây); nghiêm cấm dùng đường cong uốn vĩ mô M - kappa để quy kết cơ chế.
- **Yêu cầu về Khóa Tham số (Locked Calibration Requirement):** Toàn bộ tham số đàn hồi, chuyển pha (E_A, E_M, sigma_tr) và hệ số ma sát (mu) phải được hiệu chuẩn độc lập ngoài bài toán bó dây uốn (Locked Calibration Rule).
- **Các đe dọa chưa giải quyết:** THREAT-01, THREAT-02, THREAT-03, THREAT-04, THREAT-05, THREAT-06
- **Điều kiện loại bỏ liên quan:** KILL-K01, KILL-K02, KILL-K03, KILL-K04, KILL-K05
- **Độ tin cậy & Xuất xứ:** `medium` | `outputs/execution/MP1-V002/W2-03/MP1_T1_T2_T3_TARGET_MATRIX.json, docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md`
