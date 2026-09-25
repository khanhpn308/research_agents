# MP1 — Mentor Pivot: Trạng thái hiện tại (Current Status at HEAD)

> **Trạng thái:** `MP1-V002 ACTIVE` (Stage 3 Remediation Consensus at HEAD).
> **Quy mô Ma trận:** **16 full-text papers** trong `outputs/verification/MP1-V002/verification_matrix.json`.
> **Audit canonical mới nhất:** `TARGETED_THREAT_AUDIT.json` (16 papers) trả `final_v002_verdict = False`, `survives_current_full_text_set = True` (chỉ sống sót tạm thời dưới dạng câu hỏi cơ học hẹp về áp suất giam giữ), và `stop_condition_satisfied = False`.
> **Báo cáo Khoa học Tổng hợp:** Đã ban hành báo cáo chi tiết 24 chương tại `docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md` và ma trận khắc phục phê bình Astra tại `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md`.
> **Nguyên tắc:** Hướng luận văn D1/M1 hiện tại vẫn được bảo toàn và **chưa bị thay thế**. MP1 chỉ có thể thay thế D1/M1 sau khi hoàn tất falsification và có final adjudication rõ ràng.

---

## 1. Ý tưởng Ban đầu từ Mentor và Lý do Bác bỏ Kiến trúc Thiết bị

Kiến trúc ban đầu do Mentor đề xuất:
```text
superelastic NiTi / metallic wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven syringe/piston pressure source
```

MP1-V001 và V002 đã phân rã toàn diện và khẳng định: **Không tồn tại tính mới ở cấp độ lắp ghép linh kiện/thiết bị**. Các khẳng định cấp hệ thống C1–C4 đã bị tiền nhiệm đóng hoàn toàn:
- **C1 (Wire Jamming):** Đã có tiền nhiệm trực tiếp (Bai 2022, Liu 2021).
- **C2 (Positive-Pressure Jamming):** Đã có tiền nhiệm trực tiếp (Zhang & Yao 2026, Huynh 2022).
- **C3 (SMA + Jamming Coexistence):** Đã có tiền nhiệm trực tiếp (Takashima 2021, 2022).
- **C4 (Compact Pressure Source):** Đã có tiền nhiệm trực tiếp (Huynh 2022, Wang 2024).
- **C8 (Syringe/Piston Jamming):** Substantially preempted; chỉ là giải pháp kỹ thuật tích hợp.

---

## 2. Tiến hóa sang Mechanics Core và Thách thức Phản biện từ Astra

Sau MP1-V001, đề tài rút lui về bài toán cơ học tiếp xúc lõi (mechanics core). Tuy nhiên, phản biện độc lập của GPT-5.6 Astra (`docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md`) đã chỉ ra 12 lỗ hổng trọng yếu (G01–G12). Nhóm nghiên cứu Stage 3 đã tiếp thu 100% và thực hiện hiệu chỉnh dứt điểm:

### 2.1. Tái Cấu trúc Hệ Thống Giả Thuyết H0/H1 (G01 & G11 Remediation)
- **H0a (Naive Elastic Substitution):** Thay thế dây NiTi bằng dầm đàn hồi tuyến tính đơn giản ($E = \text{const}$). **Đã bị bác bỏ (`REFUTED` / `established`)** khi vượt ngưỡng chuyển pha do NiTi có thềm ứng suất, trễ thắt và biến thiên mô-đun.
- **H0b (Existing NiTi Constitutive + Contact Framework):** Khung lý thuyết kết hợp mô hình cấu thành NiTi hiện hữu (Auricchio, Graesser) với cơ học tiếp xúc Coulomb và điều kiện biên áp suất biến thiên $p(t)$. **Chưa bị bác bỏ (`NOT FALSIFIED` / `PLAUSIBLE`)**. Các công trình Vahidi 2022, Kang 2020, Carboni 2016, Barsi 2025 chứng minh khung lý thuyết này hoàn toàn khả thi và chưa từng thất bại.
- **H1 (Novel Distinct Coupling Mechanics):** Đòi hỏi một phương trình ghép cặp vi mô mới vượt ngoài H0b. **Chưa có bằng chứng khoa học (`INSUFFICIENT EVIDENCE`)**.
- **Hòa giải Audit JSON:** Nhãn `established` trong `TARGETED_THREAT_AUDIT.json` chỉ có giá trị cho việc bác bỏ H0a; đối với H1, trạng thái khoa học chính xác là `insufficient`.

### 2.2. Hạ cấp Phân loại Áp suất P3 (G02 Remediation)
- Phân loại áp suất:
  - $P_1$: Áp suất chế tạo thụ động (Xin Liu 2013, Reedlunn 2013).
  - $P_2$: Áp suất biên ngoài cố định (Tjahjanto 2017, Zhang & Yao 2026).
  - $P_3$: Áp suất giam giữ chủ động biến thiên $p(t)$.
- **Kết luận:** $P_1, P_2, P_3$ là phân loại về **giao thức điều khiển thực nghiệm (protocol)**, không phải là ba lớp lý thuyết cơ học khác nhau. Các phương trình cơ học tiếp xúc hiện hữu tự nhiên tiếp nhận $p(t)$ mà không cần phương trình vật lý mới. Bỏ luận điểm "áp suất chủ động tự tạo cơ học mới".

### 2.3. Điều kiện Miền Cùng Tồn tại (Coexistence Domain: G03 Remediation)
- Ngưỡng trượt $\kappa_{\text{slip}}(p)$ và ngưỡng chuyển pha $\kappa_{\text{tr}}(p)$ có thể phân tách hoàn toàn.
- Nếu biến dạng uốn nhỏ dưới 0.75%, dây NiTi hoàn toàn ở pha Austenite đàn hồi ($E_A$). Khi đó hệ thống hành xử như **kẹt dây đàn hồi (elastic wire jamming)** truyền thống, mô hình H0a hoàn toàn đủ dùng.
- Sự cùng tồn tại chỉ xảy ra khi uốn góc gập rất sâu hoặc có lực kéo căng dọc trục đáng kể.

### 2.4. Đính chính Dữ liệu Thực tế Lịch sử (G05, G07, G08 Remediation)
- **Carboni et al. (2015):** Đính chính sai sót của packet W08. Cấu hình S2a hoàn toàn là cáp thép (ST49) nhận diện bằng mô hình Bouc-Wen thuần ma sát; chỉ có cấu hình S1a là cáp NiTi chịu kéo - uốn kết hợp do khóa chuyển vị ngang.
- **Reedlunn et al. (2013):** Sai số mô hình ở góc xoắn lớn là do bỏ qua uốn/xoắn cục bộ trong động học Costello, không phải chứng minh cần coupling mới cho bó dây thẳng.
- **Fang et al. (2019):** Cáp NiTi chỉ thử kéo; mô hình dầm sợi phi tuyến là dành cho trụ cầu bê tông cốt thép (RC pier) 1.4 m. Fang chưa từng giải uốn cáp NiTi.
- **Nhận diện Mô hình:** Cấm suy luận cơ chế từ đường cong $M-\kappa$ vĩ mô vì tích số $(\mu \cdot \alpha_{\text{trans}})$ và các tham số hình học có thể bù trừ nhau hoàn hảo; cảnh báo bẫy tính kép độ mềm (double-counting compliance).

---

## 3. Danh mục 16 Toàn văn Kiểm chứng MP1-V002 tại HEAD

1. `00414aac4b`: Reedlunn et al. (2013 Part I) — Thí nghiệm kéo đẳng nhiệt cáp NiTi 7x7 và 1x27.
2. `fac21c950e`: Reedlunn et al. (2013 Part II) — Phân rã cấu phần cáp NiTi và tương tác tiếp xúc.
3. `40760daa02`: Carboni & Lacarbonara (2016) — Thiết bị tiêu tán dao động trễ thắt NiTi và thép.
4. `2f7fcf2f8f`: Fang et al. (2019) — Mô hình phần tử sợi OpenSees cho cáp NiTi và ứng dụng kháng chấn.
5. `7f3f45407f`: Ting-Long et al. (2021) — Đáp ứng động học và nhận diện tham số bộ cách ly cáp xoắn.
6. `1c81b2d35c`: Falcetelli et al. (2024) — Đánh giá thực nghiệm đối đầu cáp thép vs cáp NiTi.
7. `9f4295be23`: Barsi, Carboni, Lacarbonara (2025) — Mô hình dầm biến dạng cắt tính cận trên/dưới độ cứng uốn.
8. `56793dea9b`: Kang et al. (2020) — Abaqus UMAT cho cáp NiTi có ma sát tiếp xúc giữa các dây.
9. `d9966f2f5e`: Carboni et al. (2015) — Thí nghiệm trễ đa cấu hình của tao cáp Nitinol và thép.
10. `9e15094d68`: Niu et al. (2023) — Mô hình FE đơn giản hóa cho cáp SMA siêu đàn hồi.
11. `53200aa0c6`: Vahidi et al. (2022) — Mô hình FEA 3D chi tiết ghép luật Auricchio với tiếp xúc Coulomb.
12. `98fee47c04`: de Paula et al. (2021) — Cách ly dao động phi tuyến sử dụng cáp dây xoắn Nitinol.
13. `aaad9c248c`: Xin Liu (2013) — Luận án tiến sĩ về ma sát nội và áp suất hướng kính trong cáp.
14. `ccdc1bb980`: Tjahjanto et al. (2017) — Cơ học uốn cáp ngầm dưới áp suất hướng kính và tiếp xúc dính - trượt.
15. `e8462758c3`: Liu et al. (2026) — Vi sợi NiTi bện: micro-slip tiếp xúc và chuyển pha cục bộ.
16. `6dd1ca94d1`: Silva et al. (2022) — Vi cáp NiTi: tự gia nhiệt ma sát làm dịch ứng suất chuyển pha.

---

## 4. Trạng thái Phủ sóng Trích dẫn và Câu hỏi Khoa học Còn Sống

- **Trạng thái Citation Coverage:** `stop_condition_satisfied = false` (hai nhánh trích dẫn ngược B11 và B12 chưa đóng trong audit JSON).
- **Câu hỏi Cơ học Còn Sống Tạm thời:**
  > *"Dưới áp suất giam giữ biến thiên độc lập $p(t)$, liệu khung lý thuyết NiTi cấu thành – tiếp xúc Coulomb hiện hữu (H0b) với các tham số đo độc lập có đủ khả năng dự đoán các quá trình chuyển tiếp dính – trượt, sự phân bố chuyển pha và độ cứng uốn tiếp tuyến của bó dây NiTi hay không; và nếu thất bại thì cơ chế vi mô nào chịu trách nhiệm cho sự sai lệch đó?"*
- **Tiêu chí Bác bỏ:** Nếu mô hình H0b với tham số bị khóa dự đoán thành công đáp ứng uốn, hoặc nếu miền vận hành thực tế không kích hoạt chuyển pha (thoái hóa về H0a), đề tài MP1 sẽ bị bác bỏ hoàn toàn (`REJECT`).

---

## 5. Tài liệu Canonical Cần Đọc

1. `docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md` (Báo cáo tổng thể 24 chương)
2. `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md` (Ma trận khắc phục phê bình G01–G12)
3. `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/` (11 báo cáo worker chuyên sâu W01–W11)
4. `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json` (Audit canonical 16 bài báo)
5. `outputs/verification/MP1-V002/verification_matrix.json` (Ma trận 16 bài báo kiểm chứng)
