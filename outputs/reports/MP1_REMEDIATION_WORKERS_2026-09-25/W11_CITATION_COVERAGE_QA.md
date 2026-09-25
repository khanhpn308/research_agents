# W11: Đánh giá Phủ sóng Trích dẫn và Bảo toàn Tính Toàn vẹn Nguồn (Citation Coverage Status & Source Integrity QA)

**Worker ID:** W11  
**Mục tiêu:** Rà soát thực tế trạng thái phủ sóng trích dẫn (citation coverage status), giải quyết lỗ hổng kết luận quá sớm khi chưa đạt điều kiện dừng (stop condition) theo phê bình G10 của Astra, và kiểm định chất lượng toàn vẹn dữ liệu nguồn (source integrity QA).  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Hiện trạng Phủ sóng Trích dẫn tại HEAD (G10 Remediation)

Astra đã cảnh báo nghiêm khắc trong phê bình G10:
- Việc một bài báo có đúng tổ hợp từ khóa chưa xuất hiện trong tập tài liệu đã kiểm tra **không đồng nghĩa với việc hiện tượng đó chưa từng tồn tại** trong lý thuyết cơ học hay các ngành kỹ thuật liên quan (như cơ học cáp ngầm, kỹ thuật đại dương, cơ học kết cấu hàng không).
- Báo cáo khoa học trước đây có xu hướng diễn đạt gần như "khoa học thế giới chỉ còn thiếu mỗi áp suất chủ động", trong khi quy trình tra cứu trích dẫn của chính repository vẫn chưa thỏa mãn điều kiện dừng (`stop_condition_satisfied = false`).

### 1.1. Bảng Đối soát Trạng thái Phủ sóng Trích dẫn (MP1-V002 Coverage Audit)
Dữ liệu trích xuất trực tiếp từ `outputs/verification/MP1-V002/citation_coverage.json` và `CITATION_COVERAGE_STATUS.md`:

- **Tổng số hướng trích dẫn bắt buộc (Total required directions):** 15
  - Hướng trích dẫn ngược (Backward directions): 9
  - Hướng trích dẫn xuôi (Forward directions): 6
- **Tất cả các hướng đã được sàng lọc (All required directions screened):** `False`
- **Điều kiện dừng được thỏa mãn (Stop condition satisfied):** `False`

| Nhóm Tài liệu Mỏ neo (Anchor) | Vai trò trong Giao thức | Trạng thái Trích dẫn Ngược (Backward) | Trạng thái Trích dẫn Xuôi (Forward) | Ghi chú & Nguồn Gốc (Provenance) |
|---|---|:---:|:---:|---|
| **6 Bài báo Cốt lõi Protocol** (Bai 2022, Liu 2021, Zhang 2026, Takashima 2021, 2022, Wang 2024) | `core_protocol_anchor` | Không bắt buộc | `screened` (đã sàng lọc, không phát hiện mối đe dọa trực tiếp) | Xác nhận C1–C4 đã bị đóng ở cấp độ thiết bị. |
| **Carboni & Lacarbonara 2016** (`40760daa02`) | `v002_high_threat_backward_anchor` | `screened_candidates_found` | Không bắt buộc | Trích dẫn ngược đã được sàng lọc. |
| **Carboni et al. 2015** (`d9966f2f5e`) | `v002_high_threat_backward_anchor` | `screened_candidates_found` | Không bắt buộc | Trích dẫn ngược đã được sàng lọc. |
| **Vahidi et al. 2022** (`53200aa0c6`) | `v002_high_threat_backward_anchor` | `screened_candidates_found` | Không bắt buộc | Trích dẫn ngược đã được sàng lọc. |
| **Kang et al. 2020** (`56793dea9b`) | `v002_high_threat_backward_anchor` | **`not_screened` (CHƯA SÀNG LỌC)** | Không bắt buộc | Nhánh B11 (`B11_kang2020.csv`) chưa được đóng chính thức trong audit JSON. |
| **Liu et al. 2026** (`e8462758c3`) | `v002_high_threat_backward_anchor` | `screened_no_high_threat` | Không bắt buộc | Đã hoàn tất sàng lọc nhánh B05. |
| **Silva et al. 2022** (`6dd1ca94d1`) | `v002_high_threat_backward_anchor` | `screened_candidates_found` | Không bắt buộc | Đã hoàn tất sàng lọc nhánh B06. |
| **Xin Liu Thesis 2013** (`aaad9c248c`) | `v002_high_threat_backward_anchor` | `screened_no_high_threat` | Không bắt buộc | Đã sàng lọc 4 tài liệu liên quan từ B03. |
| **Tjahjanto et al. 2017** (`ccdc1bb980`) | `v002_high_threat_backward_anchor` | `screened_no_high_threat` | Không bắt buộc | Đã sàng lọc 9 tài liệu liên quan từ B04. |
| **Barsi et al. 2025** (`9f4295be23`) | `v002_high_threat_backward_anchor` | **`not_screened` (CHƯA SÀNG LỌC)** | Không bắt buộc | Nhánh B12 (`B12_barsi.csv`) chưa được đóng chính thức trong audit JSON. |

### 1.2. Ý nghĩa Phương pháp luận của việc Chưa đạt Điều kiện Dừng
1. Trạng thái `stop_condition_satisfied = false` là **BLOCKING đối với tuyên bố rằng "quá trình tìm kiếm tiền nhiệm đã hoàn tất toàn diện"**.
2. Không được phép tuyên bố tính mới tuyệt đối hay khẳng định đề tài là "khoảng trống duy nhất còn lại trên thế giới".
3. Trạng thái chưa hoàn tất này **không ngăn cản việc phân tích giả thuyết khoa học**, nhưng buộc kết luận khoa học phải duy trì ở mức thận trọng: Khoảng trống cơ học đề xuất chỉ là một giả thuyết sống sót tạm thời (`PROVISIONALLY SURVIVING HYPOTHESIS`) trong phạm vi tập dữ liệu đã kiểm tra.

---

## 2. Kiểm định Chất lượng và Toàn vẹn Dữ liệu Nguồn (Source Integrity QA)

Tuân thủ tuyệt đối quy tắc File-First và Integrity Policy của repository:
1. **Không bịa đặt DOI, số trang hoặc dữ liệu:**
   - Xin Liu (2013, `aaad9c248c`): Ghi rõ đây là Luận án Tiến sĩ tại University of Houston, **không có mã DOI**.
   - Tjahjanto et al. (2017, `ccdc1bb980`): Kỷ yếu hội nghị OMAE 2017 (ASME 36th International Conference on Ocean, Offshore and Arctic Engineering), **không có DOI thương mại trong tệp PDF**.
   - Mọi mã DOI của 14 bài báo còn lại đều được kiểm tra đối chiếu trực tiếp với trang bìa của PDF (Crossref verified).
2. **Minh bạch Phân loại Bằng chứng (Evidence Tagging):**
   Mọi khẳng định trong báo cáo phải được gắn thẻ nguồn gốc rõ ràng:
   - `[VERIFIED FULL TEXT]`: Trích dẫn trực tiếp từ toàn văn PDF có trong kho dữ liệu.
   - `[AUDIT VERDICT]`: Kết luận chính thức từ tệp `TARGETED_THREAT_AUDIT.json`.
   - `[ASTRA CRITIQUE]`: Phê bình khoa học phản biện độc lập từ GPT-5.6 Astra.
   - `[INFERENCE]`: Suy luận logic và đánh giá kỹ thuật của nhóm nghiên cứu.
   - `[COVERAGE FACT]`: Sự thật định lượng về độ phủ trích dẫn từ tệp coverage JSON.
   - `[UNRESOLVED]`: Khoảng trống hoặc câu hỏi chưa có đủ dữ liệu để chứng minh.

---

## 3. Kết luận của Worker W11

1. Xác nhận tình trạng phủ sóng trích dẫn chưa đóng (`stop_condition_satisfied = false`) do hai nhánh trích dẫn ngược B11 (Kang 2020) và B12 (Barsi 2025) chưa được kết luận dứt điểm trong ma trận.
2. Xóa bỏ hoàn toàn mọi luận điệu bao biện về việc "khoa học thế giới chưa giải quyết"; chuyển đổi ngôn ngữ báo cáo sang trạng thái kiểm chứng giả thuyết có điều kiện.
3. Đảm bảo toàn bộ 16 tài liệu nguồn đều có danh tính và bằng chứng nguyên văn xác thực.
