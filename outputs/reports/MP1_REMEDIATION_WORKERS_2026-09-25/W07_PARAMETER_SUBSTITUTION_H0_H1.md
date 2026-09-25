# W07: Đánh giá Phép thử Thay thế Tham số H0a, H0b, H1 và Giải quyết Xung đột Trạng thái Audit (Parameter Substitution H0a/H0b/H1 & Audit Discrepancy Resolution)

**Worker ID:** W07  
**Mục tiêu:** Định nghĩa lại hệ thống giả thuyết H0/H1 một cách chặt chẽ theo cấu trúc ba tầng H0a, H0b, H1; làm rõ bản chất của bài toán thay thế tham số; và giải quyết triệt để xung đột giữa phán quyết trong `TARGETED_THREAT_AUDIT.json` và kết luận của Astra (giải quyết phê bình G01 và G11).  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Bản chất Xung đột và Lỗ hổng G01/G11

Trong các tài liệu Stage 1 và tệp `TARGETED_THREAT_AUDIT.json`, mục `parameter_substitution_test` ghi nhận:
- `existing_elastic_fiber_model_appears_sufficient: false`
- `niti_requires_distinct_constitutive_contact_coupling: true`
- `evidence_status: "established"`

Astra đã chỉ ra hai vấn đề mang tính quyết định:
1. **Lỗ hổng G01:** Khái niệm "giả thuyết không" (H0) bị định nghĩa nhập nhằng. Việc bác bỏ một mô hình dầm đàn hồi có mô-đun không đổi ($E = \text{const}$) chỉ chứng minh rằng dây NiTi không phải là dây đàn hồi tuyến tính đơn giản; nó **hoàn toàn không chứng minh** rằng các mô hình cấu thành NiTi phi tuyến kết hợp tiếp xúc hiện hữu (H0b) bị thất bại hay cần một cơ chế ghép cặp mới (H1).
2. **Lỗ hổng G11:** Có sự xung đột giữa nhãn `established` trong audit JSON và thực tế bằng chứng. Audit JSON dùng nhãn `established` để chỉ việc bác bỏ thay thế mô-đun hằng, nhưng nếu dùng chữ này để tuyên bố "bắt buộc phải có lý thuyết ghép cặp mới" thì hoàn toàn không có bằng chứng khoa học hỗ trợ (`insufficient`).

---

## 2. Phân rã Ba Tầng Giả thuyết: H0a, H0b và H1

Để loại bỏ sự mập mờ, Worker W07 phân định rõ ràng 3 giả thuyết lồng nhau:

```
┌────────────────────────────────────────────────────────────────────────┐
│ H0a: Naive Elastic Substitution                                        │
│ Thay thế dây NiTi bằng dầm đàn hồi tuyến tính (E = E_eff = const)      │
│ vào mô hình kẹt sợi hiện hữu.                                          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ BỊ BÁC BỎ (REFUTED khi có chuyển pha)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ H0b: Existing NiTi Constitutive + Contact Theory                       │
│ Kết hợp luật cấu thành NiTi hiện hữu (Auricchio, Graesser, v.v.)       │
│ với cơ học tiếp xúc Coulomb và điều kiện biên áp suất biến thiên p(t). │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ CHƯA BỊ BÁC BỎ (PLAUSIBLE / UNTESTED)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ H1: Novel Genuinely Distinct Coupled Mechanics                         │
│ Cần một phương trình vi mô mới ghép cặp trực tiếp áp suất cục bộ       │
│ với động học chuyển pha vượt ra ngoài khuôn khổ của H0b.               │
└────────────────────────────────────────────────────────────────────────┘
  TRẠNG THÁI: KHÔNG CÓ BẰNG CHỨNG HỖ TRỢ (INSUFFICIENT EVIDENCE)
```

### 2.1. Giả thuyết H0a: Thay thế Đàn hồi Đơn giản (Naive Elastic Substitution)
- **Định nghĩa:** Giữ nguyên mô hình kẹt sợi/dây đàn hồi hiện có (ví dụ: mô hình của Zhang & Yao 2026 hoặc Bai 2022), chỉ thay thế tham số vật liệu bằng một giá trị mô-đun đàn hồi tương đương $E_{\text{eff}}$ và một hệ số ma sát $\mu$ cố định.
- **Đánh giá Bằng chứng:** `REFUTED` / `THẤT BẠI`.
  - Khi tải trọng uốn đi vào miền kích hoạt chuyển pha Martensite, hợp kim NiTi biểu hiện:
    1. Hiện tượng mềm hóa trên thềm chuyển pha (transformation plateau);
    2. Hiện tượng trễ thắt (pinched hysteresis) khi dỡ tải;
    3. Bất đối xứng kéo - nén (tension-compression asymmetry);
    4. Biến đổi mô-đun giữa Austenite ($E_A \approx 60\,\text{GPa}$) và Martensite ($E_M \approx 25\,\text{GPa}$).
  - Một giá trị $E_{\text{eff}}$ cố định không thể tái tạo được đồng thời độ cứng tại các nhánh tải, dỡ tải và chu kỳ trễ. Do đó, việc bác bỏ H0a là **hoàn toàn chính xác và đã được xác lập vững chắc** (`established`).

### 2.2. Giả thuyết H0b: Khung lý thuyết NiTi Cấu thành – Tiếp xúc Hiện hữu
- **Định nghĩa:** Áp dụng các mô hình cấu thành siêu đàn hồi NiTi phụ thuộc lịch sử đã được kiểm chứng (như mô hình 3D Auricchio-Petrini hoặc mô hình 1D vi sợi OpenSees) kết hợp với các định luật cơ học tiếp xúc ma sát tiêu chuẩn (Standard Coulomb contact with penalty or Lagrange multipliers) và đưa áp suất giam giữ $p(t)$ vào như một điều kiện biên tải trọng ngoài.
- **Đánh giá Bằng chứng:** `NOT FALSIFIED` / `HOÀN TOÀN KHẢ THI`.
  - Vahidi et al. (2022, `53200aa0c6`) đã chứng minh rằng mô hình Auricchio UMAT kết hợp tiếp xúc bề mặt - bề mặt có ma sát Coulomb trong Abaqus tái tạo chính xác đáp ứng phi tuyến và tiêu tán năng lượng của cáp NiTi.
  - Barsi, Carboni, Lacarbonara (2025, `9f4295be23`) và Tjahjanto et al. (2017, `ccdc1bb980`) chứng minh cơ học dầm uốn có xét trượt ma sát tiếp nhận hoàn toàn các điều kiện biên áp suất hướng kính và phi tuyến vật liệu.
  - **Chưa có bất kỳ thí nghiệm hay nghiên cứu nào chứng minh H0b thất bại trong việc dự đoán đáp ứng uốn của bó dây NiTi dưới áp suất giam giữ.**

### 2.3. Giả thuyết H1: Cơ chế Ghép cặp Mới Vượt ngoài Lý thuyết Hiện hữu
- **Định nghĩa:** Tồn tại một quy luật ghép cặp nội tại mới (intrinsic coupling law) giữa ứng suất tiếp xúc cục bộ do áp suất $p$ gây ra và động học chuyển pha Martensite mà H0b không thể mô tả được dù đã hiệu chuẩn độc lập các tham số vật liệu và ma sát.
- **Đánh giá Bằng chứng:** `INSUFFICIENT` / `KHÔNG CÓ BẰNG CHỨNG`.
  - Chưa có một bằng chứng thực nghiệm nào chỉ ra sự sai lệch có tính lặp lại (systematic residual) giữa dự đoán của H0b và thực nghiệm để buộc phải viện dẫn đến H1.

---

## 3. Hòa giải Xung đột Audit JSON (Reconciliation of JSON Discrepancy)

Để bảo đảm tính trung thực khoa học tuyệt đối và tuân thủ các quy tắc bảo toàn của repository:
1. **Không can thiệp sửa đổi tệp canonical JSON:** Tệp `TARGETED_THREAT_AUDIT.json` được bảo toàn nguyên trạng làm bằng chứng lịch sử (provenance preservation).
2. **Làm rõ nghĩa trong Báo cáo Khoa học Tổng hợp:**
   - Trong báo cáo, cần trình bày rõ ràng: Khẳng định `niti_requires_distinct_constitutive_contact_coupling: true` với `evidence_status: "established"` trong tệp JSON chỉ có giá trị đối với việc **bác bỏ mô hình thay thế đàn hồi đơn giản H0a**.
   - Khi xét trên bài toán cạnh tranh giữa **H0b và H1**, trạng thái thực tế của bằng chứng khoa học là **`insufficient`**.
   - Việc chuyển từ việc "bác bỏ H0a" sang "tự động khẳng định H1 là mới" là một lỗi ngụy biện nhảy cóc logic. Đề tài hiện tại chỉ dừng ở việc đề xuất kiểm chứng H0b, hoàn toàn chưa có cơ sở khẳng định H1.

---

## 4. Phép thử Tối thiểu để Bác bỏ H0b (Minimum Decisive Test for H0b)

Để kiểm chứng xem H0b có bị bác bỏ hay không, quy trình thực nghiệm bắt buộc phải:
1. **Khóa tham số (Locked Calibration):** Đo đạc độc lập các tham số siêu đàn hồi của dây NiTi đơn lẻ ($E_A, E_M, \sigma_{\text{Ms}}, \sigma_{\text{Mf}}, \sigma_{\text{As}}, \sigma_{\text{Af}}$) và hệ số ma sát $\mu$ ngoài bài toán bó dây;
2. **Dự đoán không hiệu chỉnh (Forward Prediction):** Chạy mô hình H0b để dự đoán mô-men uốn và độ cứng uốn dưới các đường tải áp suất biến thiên $p(t)$ mà không được tùy tiện điều chỉnh lại tham số để ép khớp đường cong;
3. **Tiêu chuẩn bác bỏ:** H0b chỉ bị coi là thất bại nếu sai số dự đoán vượt quá ngưỡng không chắc chắn (uncertainty band) của thực nghiệm và không thể giải thích được bằng các hiệu ứng biên, nhiệt độ hoặc hình học sắp xếp (packing).

---

## 5. Kết luận của Worker W07

1. Đã phân định minh bạch ba tầng H0a, H0b và H1, chấm dứt sự mập mờ trong định nghĩa H0.
2. Xác nhận H0a bị bác bỏ (`REFUTED`), nhưng H0b vẫn hoàn toàn đứng vững (`NOT FALSIFIED`).
3. Hòa giải triệt để xung đột audit JSON: Phán quyết `established` áp dụng cho việc bác bỏ H0a; trong khi việc đòi hỏi H1 hiện tại là `insufficient`.
