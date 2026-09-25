# MP1 Astra Critique Matrix (Ma trận Phê bình Khoa học G01–G12)

> **Commit:** `8ccfa3c`  
> **Source Document:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md`  
> **Total Gaps:** 12  

## 1. Bảng Tổng hợp 12 Lỗ hổng Phê bình Astra (G01–G12)

| Critique ID | Mức độ Nghiêm trọng | Claims Ảnh hưởng | Targets Ảnh hưởng | Workers Khắc phục | Trạng thái Khắc phục | Tóm tắt Phê bình |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **G01** | `CRITICAL` | C7 | T3 | W07, W02, W03 | `REPAIRED_WITH_RESIDUAL_RISK` | H0 chưa được định nghĩa nhất quán: Bác bỏ mô-đun đàn hồi hằng số (naive sub... |
| **G02** | `CRITICAL` | C6 | T2 | W05, W02 | `REPAIRED` | P3 đang được xem gần như một cơ chế mới chỉ vì áp suất điều chỉnh được: Tha... |
| **G03** | `CRITICAL` | C7 | T3 | W06, W03 | `REPAIRED_WITH_RESIDUAL_RISK` | Chưa chứng minh chuyển pha và inter-wire slip cùng hoạt động trong miền vận... |
| **G04** | `CRITICAL` | C7 | T3 | W08 | `REPAIRED_WITH_RESIDUAL_RISK` | Đáp ứng uốn vĩ mô không nhận diện riêng được các cơ chế: Đường cong $M - \k... |
| **G05** | `HIGH` | C7 | T3 | W04, W03 | `REPAIRED` | Packet W08 gán sai chuyển pha NiTi dưới uốn thuần cho cấu hình S2a của Carb... |
| **G06** | `HIGH` | C7 | T1, T2, T3 | W09 | `REPAIRED` | Đánh đồng tồn tại mô hình, khớp số liệu và kiểm chứng độc lập: Việc khớp đư... |
| **G07** | `HIGH` | C7 | T3 | W10, W07 | `REPAIRED` | Dùng kết quả của Reedlunn 2013 vượt quá phạm vi: Sai số mô hình ở góc xoắn ... |
| **G08** | `HIGH` | C7 | T3 | W09, W08, W10 | `REPAIRED_WITH_RESIDUAL_RISK` | Quá nhiều tham số có thể bù trừ nhau trong phép khớp uốn: Tích số giữa hệ s... |
| **G09** | `HIGH` | C6 | T2 | W08, W05 | `REPAIRED_WITH_RESIDUAL_RISK` | Ánh xạ từ áp suất buồng sang lực pháp tuyến tiếp xúc chưa được kiểm chứng: ... |
| **G10** | `HIGH` | C6, C7 | T2 | W11, W01 | `REPAIRED` | Chưa thỏa mãn điều kiện dừng nhưng diễn đạt như thể 'chỉ còn thiếu active p... |
| **G11** | `HIGH` | C7 | T3 | W07, W01 | `REPAIRED` | Xung đột trạng thái giữa Audit JSON và Báo cáo: Tệp JSON ghi niti_requires_... |
| **G12** | `MEDIUM` | C5, C6, C7 | T1, T2, T3 | W08 | `REPAIRED` | Đại lượng 'độ cứng uốn' chưa được định nghĩa theo lịch sử tải: Độ cứng tiếp... |

## 2. Phân tích Chi tiết Từng Lỗ hổng Phê bình

### Phê bình G01 (CRITICAL)
- **Điểm yếu ban đầu:** H0 chưa được định nghĩa nhất quán: Bác bỏ mô-đun đàn hồi hằng số (naive substitution) không đồng nghĩa với việc các mô hình NiTi cấu thành - tiếp xúc hiện hữu bị thất bại hay cần coupling mới.
- **Lập luận của Astra:** Mô hình NiTi phi tuyến ghép tiếp xúc Coulomb đã tồn tại trong Abaqus UMAT (Vahidi 2022). Việc bác bỏ mô-đun hằng chỉ loại trừ mô hình đàn hồi sơ đẳng H0a, hoàn toàn chưa thử thách mô hình NiTi phi tuyến hiện có H0b.
- **Bằng chứng bị thách thức:** Audit JSON, W08-W10; Vahidi 2022 (53200aa0c6); Fang 2019 (2f7fcf2f8f)
- **Yêu cầu khắc phục:** Tách H0 thành 3 tầng rõ rệt: H0a (đàn hồi hằng số), H0b (mô hình NiTi phi tuyến + Coulomb hiện hữu), và H1 (lý thuyết ghép cặp vi mô mới); kiểm tra độc lập cả hai baseline.
- **Workers thực hiện khắc phục:** W07, W02, W03
- **Trạng thái khắc phục:** `REPAIRED_WITH_RESIDUAL_RISK`
- **Rủi ro còn lại (Residual Risk):** H0b chưa bị bác bỏ bởi thực nghiệm uốn; nguy cơ các mô hình phần tử hữu hạn thương mại hiện có vẫn mô tả đầy đủ mà không cần phát triển lý thuyết mới.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* H0 bị gộp chung; phán quyết bác bỏ H0a bị đánh đồng với việc xác lập H1.
  - *Hiện tại:* H0a bị bác bỏ dứt điểm (REFUTED); H0b chưa bị bác bỏ (NOT FALSIFIED); H1 chưa đủ bằng chứng (INSUFFICIENT).
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L30-L37`

---
### Phê bình G02 (CRITICAL)
- **Điểm yếu ban đầu:** P3 đang được xem gần như một cơ chế mới chỉ vì áp suất điều chỉnh được: Thay đổi điều kiện biên từ hằng số sang biến thiên theo thời gian $p(t)$ có thể không cần phương trình cơ học mới.
- **Lập luận của Astra:** Các phương trình tiếp xúc dầm vi phân trong Tjahjanto 2017 và Xin Liu 2013 đều tự nhiên tiếp nhận áp suất pháp tuyến biến thiên $p(t)$ theo từng bước gia số tải mà không làm thay đổi định luật cấu thành vật lý.
- **Bằng chứng bị thách thức:** W07; Tjahjanto 2017 (ccdc1bb980); Xin Liu 2004/2013 (aaad9c248c); Barsi 2025 (9f4295be23)
- **Yêu cầu khắc phục:** Kiểm tra trực tiếp các phương trình vi phân tiếp xúc hiện hữu; hạ cấp P3 từ một cơ chế cơ học mới thành một giao thức điều khiển thực nghiệm (experimental protocol).
- **Workers thực hiện khắc phục:** W05, W02
- **Trạng thái khắc phục:** `REPAIRED`
- **Rủi ro còn lại (Residual Risk):** Áp suất biến thiên nhanh có thể gây trễ động học chất lưu trong màng bao, cần kiểm chứng thực nghiệm riêng.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* P3 được xem là trụ cột tính mới độc lập tạo ra cơ học mới.
  - *Hiện tại:* P3 chỉ là điều kiện biên thay đổi theo thời gian; không tạo ra định luật vật lý mới.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L38-L44`

---
### Phê bình G03 (CRITICAL)
- **Điểm yếu ban đầu:** Chưa chứng minh chuyển pha và inter-wire slip cùng hoạt động trong miền vận hành dự kiến: Nếu chỉ một cơ chế kích hoạt, lập luận ghép cặp sụp đổ về kẹt dây đàn hồi hoặc dầm siêu đàn hồi liền khối.
- **Lập luận của Astra:** Ngưỡng trượt $\kappa_{\text{slip}}$ và ngưỡng chuyển pha $\kappa_{\text{tr}}$ có thể phân tách rất xa. Ở biến dạng uốn nhỏ dưới 0.75%, NiTi hoàn toàn ở pha Austenite đàn hồi ($E_A$), không có chuyển pha xảy ra.
- **Bằng chứng bị thách thức:** Chưa có phép thử áp suất - uốn tương ứng trong bằng chứng đã kiểm tra; các mô hình uốn giả định sẵn chuyển pha.
- **Yêu cầu khắc phục:** Xác định độc lập ngưỡng chuyển pha và ngưỡng trượt ma sát; thiết lập điều kiện cần cho Miền Cùng Tồn Tại (Coexistence Domain) đòi hỏi uốn góc gập sâu hoặc kéo căng dọc trục.
- **Workers thực hiện khắc phục:** W06, W03
- **Trạng thái khắc phục:** `REPAIRED_WITH_RESIDUAL_RISK`
- **Rủi ro còn lại (Residual Risk):** Trong miền uốn nhỏ thường gặp của tay gắp mềm, cơ cấu bị thoái hóa về bài toán kẹt dây đàn hồi thông thường (H0a đủ dùng).
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Mặc định coi chuyển pha và trượt luôn luôn xảy ra đồng thời trong mọi chế độ uốn.
  - *Hiện tại:* Sự cùng tồn tại bị giới hạn nghiêm ngặt trong miền biến dạng lớn; ở biến dạng nhỏ bài toán thoái hóa về kẹt đàn hồi.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L45-L52`

---
### Phê bình G04 (CRITICAL)
- **Điểm yếu ban đầu:** Đáp ứng uốn vĩ mô không nhận diện riêng được các cơ chế: Đường cong $M - \kappa$ không thể phân biệt giữa chuyển pha, ma sát trượt, biến dạng bẹp tiết diện và trượt tại ngàm.
- **Lập luận của Astra:** Dữ liệu lực - chuyển vị vĩ mô là đại lượng tích phân không gian. Nhiều hiện tượng vật lý khác nhau (chuyển pha, trượt ma sát, trượt ngàm) đều cùng dẫn đến hiện tượng mềm hóa độ cứng (softening).
- **Bằng chứng bị thách thức:** Carboni 2015 (d9966f2f5e); Fang 2019 (2f7fcf2f8f); Barsi 2025 (9f4295be23); Reedlunn 2013 (fac21c950e)
- **Yêu cầu khắc phục:** Nghiêm cấm quy kết hiện tượng mềm hóa vĩ mô cho coupling NiTi; bắt buộc phải bổ sung đo đạc trạng thái cục bộ (DIC, FBG, ảnh nhiệt hồng ngoại, đo trượt đầu dây).
- **Workers thực hiện khắc phục:** W08
- **Trạng thái khắc phục:** `REPAIRED_WITH_RESIDUAL_RISK`
- **Rủi ro còn lại (Residual Risk):** Thí nghiệm đo cục bộ trên từng sợi dây trong bó dây bọc kín dưới áp suất là cực kỳ phức tạp về mặt kỹ thuật.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Kỳ vọng chỉ cần đo đường cong uốn vĩ mô $M - \kappa$ là đủ chứng minh cơ chế ghép cặp mới.
  - *Hiện tại:* Đường cong vĩ mô không có tính nhận diện đơn nhất; phải có đối chứng cơ chế cục bộ.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L53-L60`

---
### Phê bình G05 (HIGH)
- **Điểm yếu ban đầu:** Packet W08 gán sai chuyển pha NiTi dưới uốn thuần cho cấu hình S2a của Carboni: S2a thực chất là cáp thép thuần ma sát; S1a mới là cáp NiTi chịu kéo - uốn kết hợp.
- **Lập luận của Astra:** Kiểm tra trực tiếp tệp PDF Carboni 2015 xác nhận cấu hình S2a là ST49 (cáp thép 49 sợi, mô hình trễ Bouc-Wen thuần ma sát). S1a mới là bó 7 sợi NiTi và chịu biến dạng kéo-uốn kết hợp do ngàm khóa dịch chuyển ngang.
- **Bằng chứng bị thách thức:** W08-E01; Carboni 2015 PDF tr. 9-10 và Bảng 4 (Table 4)
- **Yêu cầu khắc phục:** Loại bỏ hoàn toàn suy luận sai về S2a khỏi evidence chain; đính chính 100% dữ liệu thực tế; chỉ dùng S1a với đầy đủ giới hạn về lực kéo dọc trục đi kèm.
- **Workers thực hiện khắc phục:** W04, W03
- **Trạng thái khắc phục:** `REPAIRED`
- **Rủi ro còn lại (Residual Risk):** Không còn rủi ro dữ liệu sai; bằng chứng Carboni chỉ chứng minh kéo-uốn kết hợp, không chứng minh uốn thuần túy.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* S2a được dùng làm bằng chứng then chốt chứng minh chuyển pha uốn thuần.
  - *Hiện tại:* S2a là cáp thép; chỉ S1a là NiTi nhưng chịu tải kéo-uốn kết hợp có lực căng lớn.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L61-L68`

---
### Phê bình G06 (HIGH)
- **Điểm yếu ban đầu:** Đánh đồng tồn tại mô hình, khớp số liệu và kiểm chứng độc lập: Việc khớp đường cong không chứng minh được tính đúng đắn của cơ chế vật lý.
- **Lập luận của Astra:** Nhiều mô hình điều chỉnh tham số tự do để ép khớp một đường cong thực nghiệm cụ thể (calibration), nhưng hoàn toàn thất bại khi dự đoán điều kiện biên mới (validation) hoặc không chứng minh được quan hệ nhân quả.
- **Bằng chứng bị thách thức:** Vahidi 2022; Niu 2023 (9e15094d68); Zhang & Yao 2026; Fang 2019
- **Yêu cầu khắc phục:** Thiết lập Thang bậc 5 tầng về độ tin cậy mô hình: Tầng 1 (Formulation), Tầng 2 (Numerical Verification), Tầng 3 (Calibration), Tầng 4 (Validation với tham số bị khóa), và Tầng 5 (Causal Identification).
- **Workers thực hiện khắc phục:** W09
- **Trạng thái khắc phục:** `REPAIRED`
- **Rủi ro còn lại (Residual Risk):** Mô hình mới đề xuất trong luận văn phải đạt tối thiểu Tầng 4 mới được xem là có giá trị khoa học vững chắc.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Đánh đồng việc một bài báo có đồ thị khớp số liệu với việc cơ chế đã được validate.
  - *Hiện tại:* Khớp số liệu chỉ là Calibration (Tầng 3); Validation bắt buộc phải khóa tham số trên tập dữ liệu độc lập.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L69-L76`

---
### Phê bình G07 (HIGH)
- **Điểm yếu ban đầu:** Dùng kết quả của Reedlunn 2013 vượt quá phạm vi: Sai số mô hình ở góc xoắn lớn là do bỏ qua uốn/xoắn cục bộ trong động học Costello, không phải chứng minh cần luật ghép cặp mới cho bó dây thẳng.
- **Lập luận của Astra:** Tác giả Reedlunn nêu rõ nguyên nhân sai số ở lớp ngoài cáp 1x27 là do giả thiết động học thanh xoắn Costello bỏ qua mô-men uốn và xoắn cục bộ của sợi. Ở cấu hình góc xoắn nông (7x7), cáp hành xử rất gần dây đơn.
- **Bằng chứng bị thách thức:** fac21c950e (Reedlunn et al. 2013 Part II); W09
- **Yêu cầu khắc phục:** Áp dụng nguyên tắc trích dẫn bảo thủ; không dùng sự thất bại của phép rút gọn động học cáp xoắn dốc để suy diễn về nhu cầu lý thuyết mới cho bó dây song song của robot mềm.
- **Workers thực hiện khắc phục:** W10, W07
- **Trạng thái khắc phục:** `REPAIRED`
- **Rủi ro còn lại (Residual Risk):** Không còn rủi ro suy diễn sai lệch từ Reedlunn 2013.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Dùng Reedlunn làm căn cứ lập luận rằng cơ học tiếp xúc cáp dây hiện hữu đã sụp đổ.
  - *Hiện tại:* Reedlunn chỉ chỉ ra giới hạn của giả thiết động học Costello đối với cáp xoắn dốc; không liên quan đến bó dây thẳng.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L77-L84`

---
### Phê bình G08 (HIGH)
- **Điểm yếu ban đầu:** Quá nhiều tham số có thể bù trừ nhau trong phép khớp uốn: Tích số giữa hệ số ma sát và tỷ lệ truyền áp $(\mu \cdot \alpha_{\text{trans}})$ không thể tách rời từ phép đo uốn vĩ mô.
- **Lập luận của Astra:** Trong phương trình lực cản trượt $F_{\text{cap}} = \mu f_n = \mu \alpha_{\text{trans}} p$, việc tăng $\mu$ và giảm $\alpha_{\text{trans}}$ tạo ra đáp ứng lực ma sát tương đương. Nếu thả nổi cả hai tham số, phép khớp uốn sẽ mất tính duy nhất.
- **Bằng chứng bị thách thức:** Fang 2019 PDF tr. 11-12; Carboni 2015 parameter identification
- **Yêu cầu khắc phục:** Thiết lập Quy tắc Khóa tham số tuyệt đối (Locked Calibration Rule): Mọi tham số vật liệu và ma sát phải đo độc lập ngoài bài toán bó dây; cấm thả nổi tham số để ép khớp đường cong uốn.
- **Workers thực hiện khắc phục:** W09, W08, W10
- **Trạng thái khắc phục:** `REPAIRED_WITH_RESIDUAL_RISK`
- **Rủi ro còn lại (Residual Risk):** Nếu thiết bị đo không đủ độ chính xác để đo độc lập mu và alpha_trans, hiện tượng bù trừ tham số vẫn có thể làm suy giảm tính thuyết phục của mô hình.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Chưa nhận thức được nguy cơ bù trừ tham số giữa ma sát tiếp xúc và truyền lực áp suất.
  - *Hiện tại:* Khóa tham số bắt buộc; kiểm tra độ nhạy và tính duy nhất tham số trước khi kết luận.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L85-L92`

---
### Phê bình G09 (HIGH)
- **Điểm yếu ban đầu:** Ánh xạ từ áp suất buồng sang lực pháp tuyến tiếp xúc chưa được kiểm chứng: Sai số truyền áp qua màng đàn hồi và cấu hình sắp xếp có thể bị ngụy trang thành sai số luật cấu thành.
- **Lập luận của Astra:** Màng bao có độ cứng vòng (hoop stiffness) và sự sắp xếp rỗng của bó dây tạo hiệu ứng vòm (arching effect), làm suy giảm lực pháp tuyến thực tế $f_n$ so với áp suất buồng $p$. Sai số hình học này dễ bị quy kết nhầm cho luật vật liệu NiTi.
- **Bằng chứng bị thách thức:** Zhang & Yao 2026; Tjahjanto 2017
- **Yêu cầu khắc phục:** Bổ sung phân tích chuỗi truyền áp lực; yêu cầu đo đạc hoặc hiệu chuẩn độc lập mối quan hệ $p 	o f_n$ bằng cảm biến áp lực màng hoặc thử nghiệm nén hướng kính độc lập.
- **Workers thực hiện khắc phục:** W08, W05
- **Trạng thái khắc phục:** `REPAIRED_WITH_RESIDUAL_RISK`
- **Rủi ro còn lại (Residual Risk):** Hiệu ứng vòm thay đổi động theo độ cong uốn của dầm, gây khó khăn cho việc lập mô hình giải tích chính xác tuyệt đối.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Mặc định giả định áp suất buồng chuyển hóa 100% thành lực pháp tuyến đồng đều giữa các sợi dây.
  - *Hiện tại:* Lực pháp tuyến thực tế bị suy giảm do hiệu ứng vòm; bắt buộc phải có mô hình truyền áp độc lập.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L93-L100`

---
### Phê bình G10 (HIGH)
- **Điểm yếu ban đầu:** Chưa thỏa mãn điều kiện dừng nhưng diễn đạt như thể 'chỉ còn thiếu active pressure': Không tìm thấy trong tập tài liệu đã duyệt không tương đương với việc không tồn tại trong toàn bộ nền khoa học.
- **Lập luận của Astra:** citation_coverage.json ghi nhận stop_condition_satisfied = false, các nhánh trích dẫn ngược B11 và B12 chưa đóng. Do đó, việc tuyên bố 'đã xác lập khoảng trống khoa học' là vội vàng và chưa có cơ sở phương pháp luận.
- **Bằng chứng bị thách thức:** W11; outputs/verification/MP1-V002/citation_coverage.json
- **Yêu cầu khắc phục:** Minh bạch hóa trạng thái bao phủ trích dẫn; khẳng định dứt khoát điều kiện dừng chưa đạt; định danh khoảng trống đề xuất chỉ là một giả thuyết còn sống sót tạm thời (PROVISIONALLY SURVIVING HYPOTHESIS).
- **Workers thực hiện khắc phục:** W11, W01
- **Trạng thái khắc phục:** `REPAIRED`
- **Rủi ro còn lại (Residual Risk):** Các nhánh trích dẫn sâu hơn trong văn hiến cơ học kết cấu có thể tìm thấy mô hình tương tự, đòi hỏi quy trình rà soát liên tục.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Tuyên bố khoảng trống nghiên cứu đã được xác lập vững chắc.
  - *Hiện tại:* Khoảng trống chỉ là giả thuyết sống sót tạm thời trong phạm vi tập tài liệu đã rà soát.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L101-L108`

---
### Phê bình G11 (HIGH)
- **Điểm yếu ban đầu:** Xung đột trạng thái giữa Audit JSON và Báo cáo: Tệp JSON ghi niti_requires_distinct_constitutive_contact_coupling = true với evidence_status = 'established' trong khi Astra kết luận là 'insufficient'.
- **Lập luận của Astra:** Phán quyết 'established' trong JSON xuất phát từ việc bác bỏ mô hình thay thế đàn hồi đơn giản H0a; nhưng đối với H1 (nhu cầu về một luật ghép cặp mới) thì bằng chứng hoàn toàn chưa đủ ('insufficient'). Việc dùng nhãn 'established' dễ gây hiểu lầm nghiêm trọng.
- **Bằng chứng bị thách thức:** outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json dòng 237-241; provenance
- **Yêu cầu khắc phục:** Giữ nguyên tệp canonical JSON để bảo toàn provenance lịch sử; làm rõ trong báo cáo rằng nhãn 'established' chỉ áp dụng cho việc bác bỏ H0a; trạng thái khoa học giữa H0b và H1 là 'insufficient'.
- **Workers thực hiện khắc phục:** W07, W01
- **Trạng thái khắc phục:** `REPAIRED`
- **Rủi ro còn lại (Residual Risk):** Không còn rủi ro hiểu lầm khi đọc song song JSON và báo cáo tổng hợp.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Xung đột ngầm giữa JSON kết luận 'established' và báo cáo phản biện kết luận 'insufficient'.
  - *Hiện tại:* Hòa giải minh bạch: 'established' áp dụng cho việc loại bỏ H0a; 'insufficient' áp dụng cho tính cần thiết của H1.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L109-L116`

---
### Phê bình G12 (MEDIUM)
- **Điểm yếu ban đầu:** Đại lượng 'độ cứng uốn' chưa được định nghĩa theo lịch sử tải: Độ cứng tiếp tuyến, cát tuyến và động học có thể dẫn đến các kết luận trái ngược nhau.
- **Lập luận của Astra:** Trong vật liệu có trễ lớn và trượt ma sát, độ cứng tiếp tuyến $D_{\text{tan}} = \partial M / \partial \kappa$ biến thiên liên tục theo nhánh tải/dỡ tải và có thể âm; độ cứng cát tuyến $D_{\text{sec}} = M / \kappa$ phản ánh năng lượng biến dạng toàn phần; độ cứng động học $D_{\text{dyn}}$ phụ thuộc tần số và biên độ dao động.
- **Bằng chứng bị thách thức:** Các nguồn tài liệu trong V002 dùng các khái niệm tải trọng và định nghĩa độ cứng không đồng nhất.
- **Yêu cầu khắc phục:** Chuẩn hóa 3 định nghĩa toán học riêng biệt: $D_{\text{tan}}(\kappa, p)$ kèm theo điều kiện dấu $\text{sgn}(\dot{\kappa})$, $D_{\text{sec}}(\kappa, p)$, và $D_{\text{dyn}}(\kappa_0, p, \omega)$; quy định rõ đại lượng đo trong mọi phát biểu khoa học.
- **Workers thực hiện khắc phục:** W08
- **Trạng thái khắc phục:** `REPAIRED`
- **Rủi ro còn lại (Residual Risk):** Cần đảm bảo tính nhất quán tuyệt đối trong các công thức toán học của các báo cáo tiếp theo.
- **Diễn giải lịch sử vs Hiện tại:**
  - *Lịch sử:* Dùng chung một thuật ngữ 'bending stiffness' mơ hồ cho nhiều chế độ tải khác nhau.
  - *Hiện tại:* Phân định nghiêm ngặt giữa độ cứng tiếp tuyến, cát tuyến và động học theo công thức toán học cụ thể.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md#L117-L125`

---
