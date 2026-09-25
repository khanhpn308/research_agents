# Worker W2-02-10: Mechanics-Core Pivot Reconstruction Report

> **Worker:** W2-02-10  
> **Nhiệm vụ:** Tái dựng bước chuyển hướng chiến lược sang Cơ học Tiếp xúc Lõi (Mechanics-Core Pivot)  
> **Mã chuyển hướng:** `PIVOT-MP1-V001-TO-MECHANICS-CORE`  
> **Commit nguồn:** `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` $\to$ **Commit đích:** `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7`  

## 1. Bối cảnh và Nguyên nhân Kích hoạt
Tại thời điểm hoàn thành kiểm chứng MP1-V001 (S04), kết quả phân tích 10 bài báo toàn văn đã chứng minh rằng toàn bộ các thành phần kiến trúc của ý tưởng Mentor (C1: kẹt dây, C2: áp suất dương, C3: SMA+jamming, C4: bơm nhỏ gọn, C8: piston SMA) đều đã có tiền nhiệm trực tiếp trong giai đoạn 2021–2026. Nếu tiếp tục theo đuổi tính mới ở cấp độ chế tạo thiết bị tích hợp, đề tài chắc chắn sẽ bị bác bỏ hoàn toàn.

Tuy nhiên, trong tập 10 bài báo được cung cấp, không có công trình nào sử dụng chính các sợi dây NiTi siêu đàn hồi làm môi trường tự trượt ma sát chịu áp suất dương và phân tích sự ghép cặp cơ học uốn sinh ra (C5, C6, C7). Do đó, workflow đã thực hiện một bước chuyển hướng chiến lược: **PIVOT_TO_MECHANICS_CORE**.

## 2. Bảng Phân loại Sự thay đổi của các Claims tại Thời điểm Pivot

| Claim ID | Nhãn Khẳng định | Trạng thái sau Pivot | Nguồn Tiền nhiệm Kích hoạt |
|:---:|:---|:---:|:---|
| **C1** | Kẹt dây/sợi tạo biến thiên độ cứng | `CLOSED` | Bai et al. (2022), Zhang & Yao (2026) |
| **C2** | Kẹt bằng áp suất dương | `CLOSED` | Liu et al. (2021), Zhang & Yao (2026) |
| **C3** | SMA và Jamming cùng thiết bị | `CLOSED` | Dòng Takashima (2022–2026), Matsumoto et al. (2024) |
| **C4** | Nguồn áp suất tích hợp/nhỏ gọn | `CLOSED` | Huynh et al. (2022), Wang et al. (2024) |
| **C8** | Piston/xi lanh dẫn động bằng SMA | `SUBSTANTIALLY_PREEMPTED` | Pierce & Mascaro (2013), Kotb et al. (2021), Wang et al. (2024) |
| **C5** | Dây NiTi tự thân làm môi trường ma sát | `OPEN_IN_SUPPLIED_CORPUS` | Mở trong kho V001 (chưa thấy trong 10 bài này) |
| **C6** | Áp suất dương giam giữ bó dây NiTi | `OPEN_IN_SUPPLIED_CORPUS` | Mở trong kho V001 |
| **C7** | Ghép cặp NiTi, ma sát, áp suất và độ cứng | `OPEN_IN_SUPPLIED_CORPUS` | Mở trong kho V001 |

## 3. Những gì Bước Pivot Thiết lập và KHÔNG Thiết lập

### Những gì Bước Pivot Thiết lập:
1. Từ bỏ vĩnh viễn và dứt điểm mọi tuyên bố tính mới ở cấp độ lắp ghép hệ thống/thiết bị.
2. Định hình lại bài toán nghiên cứu thành câu hỏi cơ học tiếp xúc: *Áp suất giam giữ, hiện tượng trượt ma sát giữa các dây, và phản ứng siêu đàn hồi của NiTi tương tác như thế nào để quyết định độ cứng uốn và trễ của bó dây?*
3. Bảo toàn D1/M1 làm hướng baseline trong khi MP1 rút về kiểm chứng cơ học sâu hơn.

### Những gì Bước Pivot KHÔNG Thiết lập:
1. **KHÔNG** chứng minh mechanics core là có tính mới toàn cầu.
2. **KHÔNG** chứng minh dây NiTi chưa từng được nghiên cứu tiếp xúc ma sát ở ngoài tập 10 bài báo này (các vòng V002 sau đó chứng minh y văn cáp xoắn NiTi đã giải quyết phần lớn vấn đề này).
3. **KHÔNG** chứng minh rằng cần phải có một định luật cấu thành - tiếp xúc hoàn toàn mới.
4. **KHÔNG** chọn MP1 làm đề tài luận văn Thạc sĩ.

## 4. Các Hiệu chỉnh Sau này đối với Diễn giải Pivot
- Nhận thức ban đầu cho rằng C5–C7 là "miền cơ học chưa được khai phá" đã bị hiệu chỉnh sâu sắc trong V002 và Stage 3 Remediation:
  - C5 thực chất đã bị y văn cáp xoắn NiTi (Vahidi 2022, Carboni 2015/2016) đóng ở cấp độ tồn tại cơ học.
  - C6 (áp suất chủ động P3) được hạ cấp thành điều kiện biên tải trọng ngoài, không phải nguyên lý vật lý mới.
  - C7 chuyển thành câu hỏi phân biệt mô hình (model discrimination) đối kháng với khung lý thuyết NiTi cấu thành + tiếp xúc Coulomb hiện hữu ($H_{0b}$).
