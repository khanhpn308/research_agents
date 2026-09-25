# Báo cáo Toàn diện Tái cấu trúc Nguồn gốc Trích dẫn MP1-V002 (W2-05)

## Tóm tắt Điều hành (Executive Summary)

Báo cáo này hoàn thiện nhiệm vụ **MP1-E1-W2-05 — MP1-V002 Citation Provenance Reconstruction**, thực hiện tái cấu trúc hồi quy ở chế độ CHỈ ĐỌC (read-only) đối với toàn bộ mạng lưới trích dẫn xuôi và ngược của vòng kiểm chứng MP1-V002.

### Các Chỉ số Cốt lõi
- **Số lượng Worker:** 12 logical workers (`W2-05-01` đến `W2-05-12`).
- **Mẫu số Phủ Trích dẫn Chuẩn hóa (Canonical Denominator):** **15/15** hướng.
  - Phủ trích dẫn ngược: **9/9** nhánh (`B01`, `B02`, `B03`, `B04`, `B05`, `B06`, `B09`, `B11`, `B12`).
  - Phủ trích dẫn xuôi: **6/6** nhánh (`F01`, `F02`, `F03`, `F04`, `F05`, `F06`).
- **Ngày chốt tìm kiếm:** `2026-09-25`.
- **Điều kiện dừng (Stop Condition):** `satisfied = true` (không còn nguồn đe dọa cao nào chưa được giải quyết trong ranh giới giao thức).
- **Hòa giải Bản ghi:**
  - Toàn bộ 15 nhánh chuẩn: **312** bản ghi thô $ightarrow$ **258** ứng viên duy nhất (54 bản ghi trùng lặp).
  - Hai nhánh bổ sung cuối B11 + B12: **68** bản ghi thô $ightarrow$ **67** bản ghi duy nhất (khớp chính xác phát biểu lịch sử tại Handoff Stage 4).
- **Nhánh phụ lịch sử:** 8 nhánh (`B10`, `F07`–`F13`) với 338 bản ghi được bảo tồn độc lập làm bằng chứng truy vết, không làm phình mẫu số chuẩn 15/15.

---

## 1. Phương pháp luận & Ranh giới Giao thức

Giao thức truy quét trích dẫn có mục tiêu MP1-V002 (`docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`) được kích hoạt với mục đích: **cố gắng làm sụp đổ (falsify) giả thuyết cơ học MP1 bằng tài liệu sát nhất trước khi công nhận tính khả thi**.

### Quy tắc Diễn giải Bắt buộc (Interpretation Guardrail)
> [!IMPORTANT]
> **Phát biểu Chuẩn hóa:**
> *Quy trình truy quét trích dẫn có mục tiêu đã hoàn thành điều kiện dừng độ phủ được xác định trong giao thức, và không còn nguồn đe dọa cao có tên nào chưa được giải quyết bên trong ranh giới giao thức.*
> 
> Tuyệt đối KHÔNG diễn giải độ phủ 15/15 hoặc việc thiếu vắng tài liệu trùng khớp là bằng chứng chứng minh tính mới toàn cục (Universal Novelty).

---

## 2. Tái cấu trúc 9 Nhánh Trích dẫn Ngược Chuẩn (Backward Branches B01–B12)

1. **B01 (Carboni et al. 2015, `d9966f2f5e`):** 57 bản ghi thô. Giải quyết cơ chế trượt ma sát tiếp xúc nội tại giữa các sợi Nitinol và thép dưới biến dạng uốn/kéo; dẫn chiếu tới Reedlunn et al. (2013).
2. **B02 (Vahidi et al. 2021, `53200aa0c6`):** 33 bản ghi thô. Mô hình hóa cáp xoắn kép SMA; lực ép tiếp xúc phát sinh thuần túy từ lực căng dọc trục và góc xoắn helix, không có áp suất buồng khí.
3. **B03 (Xin Liu 2004, `aaad9c248c`):** 4 bản ghi thô. Cơ học dao động cáp xét ma sát tiếp xúc nội tại; tiêu chuẩn trượt dầm uốn cổ điển.
4. **B04 (Tjahjanto et al. 2016, `ccdc1bb980`):** 9 bản ghi thô. Cơ học uốn lõi cáp ngầm dưới áp suất thủy tĩnh đại dương thụ động.
5. **B05 (Liu et al. 2026, `e8462758c3`):** 10 bản ghi thô. Bó sợi dệt vi mô NiTi tiêu hao năng lượng cao qua ma sát và chuyển pha thụ động.
6. **B06 (Silva et al. 2022, `6dd1ca94d1`):** 22 bản ghi tham khảo từ nhà xuất bản. Khám phá mỏi và ứng xử nhiệt cơ của vi cáp SMA; kết nối tới Fang et al. (2019) và Reedlunn et al. (2013).
7. **B09 (Carboni & Lacarbonara 2016, `40760daa02`):** 34 bản ghi thô. Giảm chấn uốn thắt nút dựa trên tiếp xúc cơ học hình học.
8. **B11 (Kang et al. 2020, `56793dea9b`):** 22 bản ghi thô. Mô hình phần tử hữu hạn tiếp xúc dầm cáp SMA; không có áp suất chất lưu.
9. **B12 (Barsi et al. 2025, `9f4295be23`):** 46 bản ghi thô. Lý thuyết cơ học cáp ngắn chịu uốn; chuyển tiếp trượt-dính nội tại điều khiển bởi lực căng và độ cong.

---

## 3. Tái cấu trúc 6 Nhánh Trích dẫn Xuôi Chuẩn (Forward Branches F01–F06)

1. **F01 (Bai et al. 2022, Wire Jamming):** 14 bản ghi xuôi đến 2026. Phát triển tay gắp mềm, chất lưu từ biến; không ứng dụng bó sợi kim loại siêu đàn hồi.
2. **F02 (Liu et al. 2021, Positive Pressure Jamming):** 51 bản ghi xuôi. Phát triển áo trợ lực, nẹp y tế dùng nghẽn áp suất dương với hạt/vải; không có bó dây NiTi.
3. **F03 (Zhang & Yao 2026, Positive-Pressure Fiber Jamming):** 0 bản ghi xuôi (bảo tồn nguyên văn tệp zero-result).
4. **F04 (Takashima et al. 2022, SMA + Jamming Link):** 9 bản ghi xuôi. Khớp mềm biến đổi độ cứng sử dụng SMA gia nhiệt kết hợp nghẽn chân không.
5. **F05 (Matsumoto et al. 2024, R-phase SMA Jamming):** 1 bản ghi xuôi (Takashima et al. 2026 trên JRM). Phân loại `KEEP_METADATA`; điều khiển cánh tay gắp-đặt, không áp suất buồng khí.
6. **F06 (Wang et al. 2024, Piston-like Particle Jamming):** 0 bản ghi xuôi (bảo tồn nguyên văn tệp zero-result).

---

## 4. Hòa giải Bản ghi Thô, Duy nhất và Khử trùng lặp

Báo cáo xác lập tính minh bạch toán học giữa các báo cáo:
- **Phát biểu 68 thô / 67 duy nhất:** Áp dụng cụ thể cho đợt rà soát bổ sung cuối cùng của Stage 4 gồm B11 (22) và B12 (46). Bài trùng duy nhất là Carboni et al. (2015) (`10.1061/(ASCE)EM.1943-7889.0000852`).
- **Toàn bộ 15 nhánh chuẩn:** Tổng cộng 312 bản ghi thô $ightarrow$ 258 ứng viên duy nhất qua khử trùng theo DOI và Tiêu đề chuẩn hóa.

---

## 5. Kết luận Kiểm toán

Worker W2-05-12 khẳng định:
1. Không thực hiện tìm kiếm tài liệu mới qua Internet.
2. Không thêm bớt bất kỳ bài báo nào vào kho ngữ liệu.
3. Không sửa đổi bất kỳ tệp chuẩn nào (`citation_coverage.json`, `paper_registry.json`).
4. Không thực hiện phán quyết tính mới chủ quan.
5. Tái cấu trúc thành công và bảo tồn toàn vẹn 100% bằng chứng trích dẫn của MP1-V002.
