# Báo cáo Kiểm tra Chất lượng Xuất xứ (MP1 Provenance QA Report)

> **Mã đợt kiểm tra:** `QA-RUN-W2-07`  
> **Trạng thái tổng thể:** `PASS_WITH_WARNINGS`  
> **Phạm vi kiểm tra:** 8 Claims (C1–C8), 3 Targets (T1–T3), 3 Hypotheses (H0a, H0b, H1), 16 Canonical Papers, 15 Citation Branches.

## 1. Thống kê Định lượng Kiểm toán Xuất xứ
- **Số khẳng định kiểm tra:** 8 / 8 (100% bao phủ).
- **Số bài báo toàn văn kiểm tra:** 16 / 16 (100% tồn tại tệp PDF và JSON).
- **Số mục tiêu kiểm tra:** 3 / 3 (T1, T2, T3).
- **Số tầng giả thuyết kiểm tra:** 3 / 3 (H0a, H0b, H1).
- **Số nhánh trích dẫn kiểm tra:** 15 / 15 (B01–B08/B12, F01–F06).
- **Số khẳng định không có nguồn (Unsupported Claims):** 0.
- **Số con trỏ bằng chứng không hợp lệ (Invalid Pointers):** 0.
- **Số xung đột siêu dữ liệu (Metadata Conflicts):** 0.
- **Số tệp PDF bị thiếu:** 0.
- **Số khẳng định chỉ dựa vào tóm tắt:** 0.
- **Tỷ lệ bao phủ khẳng định sang nguồn:** `100%`.
- **Tỷ lệ bao phủ nguồn sang phán quyết:** `100%`.

## 2. Các Yếu tố Khóa Phán quyết (Blocking Items)
Các yếu tố sau đây bắt buộc phải được xử lý tại cổng kiểm toán K1–K9 (W2-08):
- **THREAT-01 (Model Non-Discrimination H0b vs H1)**
- **THREAT-02 (Experimental Non-Identifiability from Macroscopic M-kappa)**
- **THREAT-03 (Coexistence Domain Collapse at Small Strains)**
- **THREAT-05 (Citation Stopping Condition Unmet in B11/B12)**

## 3. Các Yếu tố Không Khóa (Non-blocking Items)
- THREAT-04 (Pressure Transmission Void Arching Uncertainty)
- THREAT-06 (Thermomechanical Latent Heat Dissipation Rate Dependence)
- CONTRA-EV-04 (Parameter Compensation Under Locked Calibration Pending Experimental Proof)
