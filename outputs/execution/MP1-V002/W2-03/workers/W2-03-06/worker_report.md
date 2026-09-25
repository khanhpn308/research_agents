# Worker W2-03-06: Hypothesis H0b Reconstruction Report

> **Worker:** W2-03-06  
> **Hypothesis:** H0b — Existing Transformation-Aware NiTi Model + Existing Contact/Friction Framework  
> **Trạng thái:** `COMPLETE` | **Phán quyết cuối cùng:** `NOT_FALSIFIED`  

## 1. Định nghĩa Toán học và Vật lý của H0b
H0b khẳng định rằng: Khung lý thuyết cơ học tiếp xúc Coulomb tiêu chuẩn kết hợp với các mô hình cấu thành vật liệu NiTi siêu đàn hồi hiện hữu (như mô hình 3D Auricchio-Petrini hoặc mô hình dầm sợi OpenSees), với áp suất giam giữ $p(t)$ đóng vai trò là điều kiện biên ứng suất mặt ngoài, là hoàn toàn đủ để mô tả và dự đoán định lượng đáp ứng uốn của bó dây NiTi.

## 2. Bằng chứng Thực nghiệm và Số học Ủng hộ H0b
- **Vahidi et al. (2022, `53200aa0c6`):** Abaqus 3D FEA kết hợp Auricchio UMAT và tiếp xúc phạt Coulomb ($\mu = 0.115$) tái tạo chính xác đáp ứng trễ kéo của cáp NiTi nhiều sợi.
- **Barsi et al. (2025, `9f4295be23`) & Tjahjanto et al. (2017, `ccdc1bb980`):** Cơ học uốn dầm có xét trượt tiếp xúc ma sát tiếp nhận hoàn toàn các điều kiện biên áp suất hướng kính mà không cần bổ sung bất kỳ số hạng ghép cặp vi mô nào.

## 3. Trạng thái Hiện tại và Điều kiện Falsify
- H0b **chưa từng bị bác bỏ** (`NOT FALSIFIED`) trong toàn bộ y văn hiện có của repository.
- H0b chỉ bị coi là thất bại nếu trong một phép thử dự đoán uốn với **bộ tham số được khóa tuyệt đối (locked calibration)**, mô hình sai lệch có hệ thống vượt quá dải không chắc chắn của thực nghiệm.
