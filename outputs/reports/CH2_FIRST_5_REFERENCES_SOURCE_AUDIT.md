# Audit truy vết Chương 2 — 5 tài liệu tham khảo đầu tiên

**Đối tượng:** `outputs/thesis_drafts/chapter_2/chapter_2_integrated/chap_2_draf.md`  
**Phạm vi:** các ý trong bản nháp gắn citation [1]–[5]. Đây là vòng 1/5 tài liệu, chưa rà các nguồn từ [6] trở đi.

## Lịch sử và nguồn truy vết đã tìm thấy

- Thư mục tích hợp có `MP1_CH2_INTEGRATION_CHANGELOG.md`, `MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv`, `MP1_CH2_7_GATE_REVIEW.md` và các PDF nguồn. Chúng là lịch sử biên soạn/kiểm soát và dấu vết claim→nguồn có sẵn.
- Changelog ghi hotfix tích hợp hoàn tất nhưng tự đánh giá; independent acceptance vẫn “REQUIRED_NOT_PERFORMED”. Do đó trạng thái traceability không đồng nghĩa đã có kiểm định độc lập.
- `literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json` không được dùng làm authority cho bản này: hash chương trong map là `3c94a19f…`, khác hash DOCX được ghi trong changelog hotfix (`72a9409f…`); đây là một snapshot khác.
- `git log --follow` không trả lịch sử cho đường dẫn bản Markdown hiện tại; lịch sử tái dựng bên dưới dựa trên changelog và CSV truy vết, không thể xác nhận commit lineage của file Markdown.

## Danh tính 5 tài liệu và số ý được truyّ

| Ref | Tài liệu | DOI | Số claim có neo trong CSV | Ghi chú nguồn |
|---:|---|---|---:|---|
| [1] | S. Zhang & J. Yao (2026), “A variable stiffness omnidirectional chain based on positive-pressure fiber jamming” | 10.5194/ms-17-481-2026 | 19 | PDF bản tích hợp 01; trong chapter draft dùng [1]. |
| [2] | B. Reedlunn, S. Daly & J. Shaw (2013), “Superelastic shape memory alloy cables: Part I – Isothermal tension experiments” | 10.1016/j.ijsolstr.2013.03.013 | 10 | PDF bản tích hợp 02; trong chapter draft dùng [2]. |
| [3] | Y. Kotb, I. Elgamal & M. Serry (2021), “Shape Memory Alloy Capsule Micropump for Drug Delivery Applications” | 10.3390/mi12050520 | 12 | PDF bản tích hợp 03; trong chapter draft dùng [3]. |
| [4] | IEEE Publication Operations (2025), IEEE Reference Guide, ver. 3.28.2025 | Không có DOI | 1 | Nguồn quy tắc trích dẫn, không phải tài liệu cơ học; trace ghi bản PDF tạm /tmp không còn trong thư mục nguồn tích hợp. |
| [5] | J. Burgner-Kahrs, D. C. Rucker & H. Choset (2015), “Continuum Robots for Medical Applications: A Survey” | 10.1109/TRO.2015.2489500 | 7 | PDF bản tích hợp 05; trong chapter draft dùng [5]. |

## Các ý trong bản thảo và vị trí trích đoạn trong traceability

### [1] S. Zhang & J. Yao (2026), “A variable stiffness omnidirectional chain based on positive-pressure fiber jamming”

**CH2-S1-R0006-A01 — mục 2.1.1.** Chẳng hạn, Zhang và Yao đã mô hình hóa và thử uốn một chuỗi kẹt bó sợi nylon bằng túi khí áp suất dương [1].

- **Vị trí PDF theo trace:** Abstract; §4.1 Prototype fabrication and test setup. **Trạng thái:** `DIRECTLY_VERIFIED_SELECTED_PDF_PASSAGE_AND_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “an internal inﬂatable bladder is used to compact a ﬁber bundle in a rigid chain link || This cavity housed a bundle of 700 nylon ﬁbers”
- **Ranh giới/ghi chú:** Chỉ trong điều kiện nguồn; chuyển giao sang MP1 phải được kiểm tra.

**CH2-S2-R0062-A01 — mục 2.2.2.** Các phần tử có thể là dây hoặc sợi, lớp mỏng hay hạt; mạng tiếp xúc của các kiến trúc này khác nhau nên không thể dùng chung một mô tả động học tiếp xúc chỉ vì cùng mang tên jamming [1].

- **Vị trí PDF theo trace:** §1 Introduction. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “conﬁned discrete elements (granules, layers, or ﬁbers)”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0066-A01 — mục 2.2.2.** Chẳng hạn, trong nguyên mẫu fiber jamming của Zhang và Yao, độ cứng ở trạng thái jamming được báo cáo là tương đối ít nhạy với áp suất trong miền khảo sát [1].

- **Vị trí PDF theo trace:** Abstract. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “jamming state stiffness is comparatively insensitive to pressure”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0123-A01 — mục 2.2.3.** Ở cấu hình kẹt sợi áp suất dương của Zhang và Yao, túi phồng bên trong ép bó sợi trong một mắt xích có vỏ cứng [1].

- **Vị trí PDF theo trace:** Abstract. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “an internal inflatable bladder”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0152-A01 — mục 2.2.3.** Trong mô hình của Zhang và Yao, p được định nghĩa là áp suất thủy tĩnh tạo kẹt và tham gia ngưỡng ứng suất ma sát μp [1].

- **Vị trí PDF theo trace:** §2.1, Eqs. (1)–(3). **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “the hydrostatic pres- sure applied to maintain the jamming state”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0177-A01 — mục 2.2.3.** Kết quả nhận dạng phải giữ riêng với đo trực tiếp: Zhang và Yao suy hệ số ma sát hiệu dụng từ quan hệ tải chuyển trạng thái–áp suất trong mô hình của họ [1].

- **Vị trí PDF theo trace:** §5.1, parameter identification. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “effective inter-fiber static friction co- efficient”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0178-A01 — mục 2.2.3.** Tác giả cũng nêu truyền áp suất không đều và nén cục bộ do túi phồng cùng trạng thái xếp bó là các nguyên nhân khả dĩ của biến thiên tải bắt đầu trượt [1].

- **Vị trí PDF theo trace:** §5.2, paragraph below Fig. 6. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “non-uniform jamming pressure transmission”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S3-R0017-A01 — mục Abstract / Introduction / mechanics model.** Zhang và Yao cung cấp một nguồn so sánh gần hơn ở cấp kiến trúc, nhưng vẫn không tương đương với bó dây TiNi [1]. Hệ của họ dùng bóng tạo áp suất dương để nén bó sợi trong một mắt xích cứng; thử uốn ba điểm trong khoảng 0–300 kPa và phân biệt các trạng thái kẹt, chuyển tiếp và trượt bằng tải tới hạn trên đường lực–độ võng. Mô hình dùng các tham số hiệu dụng và mô men quán tính diện tích phụ thuộc áp suất để mô tả đáp ứng của một nguyên mẫu. Bài báo cũng nêu các giới hạn như áp suất truyền không đồng nhất, tham số được hiệu chỉnh từ đáp ứng của một nguyên mẫu và quan hệ chuyển tiếp mang tính hiện tượng học. Vì vậy, nghiên cứu của Zhang và Yao cho thấy kiến trúc kẹt sợi dưới áp suất dương và mô hình độ cứng phụ thuộc áp suất đã được nghiên cứu, nhưng không cung cấp mô hình trực tiếp cho dầm kẹt lớp chân không hoặc bó dây TiNi.

- **Vị trí PDF theo trace:** Abstract; model sections. **Trạng thái:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Kiến trúc mắt xích, bladder và áp suất dương khác MP1; không chuyển pressure range.

**CH2-S3-R0017-A02 — mục Abstract / Introduction / mechanics model.** Zhang và Yao [1] — nguồn so sánhBó sợi trong bóng tạo áp suất dương và mắt xích cứng.Tiếp xúc sợi trong cấu trúc bị ràng buộc; thử uốn ba điểm.Áp suất dương; thử 0–300 kPa trong nguyên mẫu của bài báo.Tải tới hạn và độ cứng trên các nhánh kẹt/chuyển tiếp/trượt; mô hình tham số hiệu dụng.Không phải dây TiNi; bóng tạo áp suất, mắt xích cứng, áp suất dương và tham số hiệu chỉnh khác MP1.

- **Vị trí PDF theo trace:** Abstract; model sections. **Trạng thái:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Kiến trúc mắt xích, bladder và áp suất dương khác MP1; không chuyển pressure range.

**CH2-S3-R0018-A01 — mục Abstract; model limitations; §5.3.** Zhang và Yao cung cấp một nguồn so sánh gần hơn ở cấp kiến trúc, nhưng vẫn không tương đương với bó dây TiNi [1]. Hệ của họ dùng bóng tạo áp suất dương để nén bó sợi trong một mắt xích cứng; thử uốn ba điểm trong khoảng 0–300 kPa và phân biệt các trạng thái kẹt, chuyển tiếp và trượt bằng tải tới hạn trên đường lực–độ võng. Mô hình dùng các tham số hiệu dụng và mô men quán tính diện tích phụ thuộc áp suất để mô tả đáp ứng của một nguyên mẫu. Bài báo cũng nêu các giới hạn như áp suất truyền không đồng nhất, tham số được hiệu chỉnh từ đáp ứng của một nguyên mẫu và quan hệ chuyển tiếp mang tính hiện tượng học. Vì vậy, nghiên cứu của Zhang và Yao cho thấy kiến trúc kẹt sợi dưới áp suất dương và mô hình độ cứng phụ thuộc áp suất đã được nghiên cứu, nhưng không cung cấp mô hình trực tiếp cho dầm kẹt lớp chân không hoặc bó dây TiNi.

- **Vị trí PDF theo trace:** Abstract; model equations; limitations. **Trạng thái:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không phải định luật hiến định chung cho bó dây TiNi hoặc dầm layer.

**CH2-S3-R0020-A05 — mục Respective source sections.** Zhang và Yao cung cấp một nguồn so sánh gần hơn ở cấp kiến trúc, nhưng vẫn không tương đương với bó dây TiNi [1]. Hệ của họ dùng bóng tạo áp suất dương để nén bó sợi trong một mắt xích cứng; thử uốn ba điểm trong khoảng 0–300 kPa và phân biệt các trạng thái kẹt, chuyển tiếp và trượt bằng tải tới hạn trên đường lực–độ võng. Mô hình dùng các tham số hiệu dụng và mô men quán tính diện tích phụ thuộc áp suất để mô tả đáp ứng của một nguyên mẫu. Bài báo cũng nêu các giới hạn như áp suất truyền không đồng nhất, tham số được hiệu chỉnh từ đáp ứng của một nguyên mẫu và quan hệ chuyển tiếp mang tính hiện tượng học. Vì vậy, nghiên cứu của Zhang và Yao cho thấy kiến trúc kẹt sợi dưới áp suất dương và mô hình độ cứng phụ thuộc áp suất đã được nghiên cứu, nhưng không cung cấp mô hình trực tiếp cho dầm kẹt lớp chân không hoặc bó dây TiNi.

- **Vị trí PDF theo trace:** Respective figures/abstract. **Trạng thái:** `NOT_APPLICABLE`.
- **Ranh giới/ghi chú:** Đây là bản ghi nghiệm thu dàn ý, không phải phát biểu khoa học độc lập.

**CH2-S3-R0020-A10 — mục Respective source sections.** Zhang và Yao [1] — nguồn so sánhBó sợi trong bóng tạo áp suất dương và mắt xích cứng.Tiếp xúc sợi trong cấu trúc bị ràng buộc; thử uốn ba điểm.Áp suất dương; thử 0–300 kPa trong nguyên mẫu của bài báo.Tải tới hạn và độ cứng trên các nhánh kẹt/chuyển tiếp/trượt; mô hình tham số hiệu dụng.Không phải dây TiNi; bóng tạo áp suất, mắt xích cứng, áp suất dương và tham số hiệu chỉnh khác MP1.

- **Vị trí PDF theo trace:** Respective figures/abstract. **Trạng thái:** `NOT_APPLICABLE`.
- **Ranh giới/ghi chú:** Đây là bản ghi nghiệm thu dàn ý, không phải phát biểu khoa học độc lập.

**CH2-S3-R0036-A01 — mục Abstract;Design;Experimental methods.** Zhang và Yao đưa ra tiền lệ gần hơn cho kẹt sợi áp suất dương bằng một bó 700 sợi nylon đường kính 0,4 mm, đặt trong mắt xích nhựa cứng và được nén bởi bóng polyethylene [1]. Mẫu được thử uốn ba điểm trong khoảng 0–300 kPa, với nhịp 100 mm và năm lần lặp cho mỗi điều kiện. Mô hình của bài báo quy áp suất bóng về áp suất kẹt hiệu dụng p và mô tả ba miền trạng thái bằng các quan hệ:

- **Vị trí PDF theo trace:** Abstract;Fig.4. **Trạng thái:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Kiến trúc không tương đương bó dây TiNi MP1.

**CH2-S3-R0039-A01 — mục 5 Results and discussion;Limitations.** Dữ liệu kiểm chứng của cùng nghiên cứu cho thấy giới hạn của cách giảm bậc này. Trong cấu hình uốn ba điểm của Zhang và Yao, lực cắt quy đổi được lấy là Q = F/2, với F là lực tác dụng tại giữa nhịp. Mô đun E = 4,85 GPa là tham số hiệu dụng được nhận dạng từ đáp ứng uốn ở p = 0, khi đóng góp ma sát liên sợi được xem là triệt tiêu; E không được đo bằng thí nghiệm vật liệu độc lập. Hệ số ma sát liên sợi hiệu dụng μ = 0,3665 được nhận dạng từ độ dốc của ngưỡng trượt hoàn toàn Q_S theo p, không phải từ phép đo ma sát riêng. Hồi quy giữa Q_J và p có R² = 0,4311 ở chế độ uốn theo trục và R² = 0,4475 ở chế độ uốn ngang; quan hệ Q_S–p gộp cho R² = 0,817 [1]. Tác giả dùng các chỉ số này để đánh giá khả năng diễn giải của mô hình trong cấu hình đã thử, đồng thời thừa nhận quan hệ bậc hai của miền chuyển tiếp mang tính hiện tượng học. Độ phân tán tăng theo áp suất được liên hệ với trượt dính–trượt không đồng nhất, sự truyền áp suất không đều, độ nén cục bộ và trạng thái xếp bó.

- **Vị trí PDF theo trace:** Figs.5–6;Conclusion. **Trạng thái:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** E và μ là tham số hiệu dụng của mô hình; E lấy từ đáp ứng uốn p=0, μ từ hồi quy ngưỡng trượt hoàn toàn; validation một nguyên mẫu.

**CH2-S3-R0040-A05 — mục 3.1.3;Experiments;Design/Fig.1;Limitations.** Kẹt sợi áp suất dương [1]Bóng polyethylene nén bó 700 sợi nylon trong mắt xích cứng.Uốn ba điểm; Q_J, Q_S; độ cứng theo miền.Q < Q_J: kẹt; Q_J–Q_S: chuyển tiếp; Q > Q_S: trượt hoàn toàn.0–300 kPa; 5 lần lặp; μ = 0,3665; R²(Q_S–p) = 0,817.Một nguyên mẫu; p là áp suất hiệu dụng; quan hệ chuyển tiếp hiện tượng học; truyền áp suất không đều.

- **Vị trí PDF theo trace:** Fig.3c;Fig.3;Fig.1;Conclusion. **Trạng thái:** `INFERENCE`.
- **Ranh giới/ghi chú:** Tổng hợp của tác giả; không phải tuyên bố novelty.

**CH2-S6-R0087-A01 — mục 2.6.2.** Trong cơ cấu xích kẹt sợi nylon của Zhang và Yao, áp suất dương đã được dùng để thay đổi đáp ứng uốn của mẫu, nên bản thân khả năng tạo kẹt bằng áp suất dương đã có bằng chứng thực nghiệm [1].

- **Vị trí PDF theo trace:** {"M13-E01": ["Abstract; §4.1 Prototype fabrication and test setup"], "M13-E05": ["§5.2 Correlation between critical loads and jamming pressure; §5.3 Pressure dependence of bending stiffness; Figure 6"], "M13-E06": ["§5.3 final paragraph; §6 Conclusion"]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “The VSOC uses an inflatable bladder to compact a fiber bundle in a rigid chain link, extending operation beyond the approximately 1-atm vacuum limit.; Critical loads and slipping-state inertia increase approximately linearly with pressure, while jammed-state i”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0092-A01 — mục 2.6.2.** Mô đun dùng trong mô hình là giá trị hiệu dụng xác định từ đáp ứng uốn ở 0 kPa; tác giả yêu cầu đối chiếu thêm bằng thử vật liệu trực tiếp [1].

- **Vị trí PDF theo trace:** {"M13-E06": ["§5.3 final paragraph; §6 Conclusion"]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “The quadratic transition relation is phenomenological and validation is restricted to a single prototype with one fiber type, diameter and count; friction and pressure transmission variability remain.”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0164-A01 — mục 2.6.3.** Mắt xích đầu tiên cần được xem xét là từ áp suất tới tải tiếp xúc: nghiên cứu kẹt sợi của Zhang và Yao có đo áp suất túi khí, đồng thời nêu truyền áp không đều như một nguyên nhân khả dĩ của độ phân tán ngưỡng trượt [1].

- **Vị trí PDF theo trace:** {"M13-E04": ["4. Experimental methods; 4.1 Prototype fabrication and test setup; 4.2 Data processing and parameter extraction algorithm; 5.2, continued before 5.3 Pressure dependence of bending stiffness"], "M13-E06": ["6. Conclusion; 5.2, continued before 5.3 Pressure dependence of bending stiffness"]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0216-A01 — mục 2.6.4.** Zhang và Yao đã khảo sát uốn ba điểm của chuỗi có bó sợi nylon được giam giữ bằng túi khí áp suất dương, ghi lực, chuyển vị và áp suất túi khí [1].

- **Vị trí PDF theo trace:** {"M13-E01":[{"physical_pages":[1],"printed_pages":["481"],"exact_locator":"Abstract","anchor":"prototype-level experimental assessment"}],"M13-E04":[{"physical_pages":[7],"printed_pages":["487"],"exact_locator":"4 Experimental methods; 4.1 Prototype fabrication and test setup; 4.2 Data processing and parameter extraction algorithm","anchor":"700 nylon"},{"physical_pages":[8],"printed_pages":["488"],"exact_locator":"Figs.4 and5; Section4.2 continued","anchor":"Specimen geometry"},{"physical_pages":[9],"printed_pages":["489"],"exact_locator":"4.2 continued; 5.1 Identification of material parameters; 5.2 Validation of critical load models","anchor":"independent material test"}]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “The VSOC uses an inflatable bladder to compact a fiber bundle in a rigid chain link, extending operation beyond the approximately 1-atm vacuum limit.; Three-point bending tests cover shaft and lateral bending, pressures 0–300 kPa, five repeats per pressure/mod”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.

### [2] B. Reedlunn, S. Daly & J. Shaw (2013), “Superelastic shape memory alloy cables: Part I – Isothermal tension experiments”

**CH2-S1-R0011-A01 — mục 2.1.1.** Thí nghiệm kéo gần đẳng nhiệt của Reedlunn và cộng sự đã ghi nhận đáp ứng siêu đàn hồi khác nhau ở hai cấu trúc cáp NiTi [2];

- **Vị trí PDF theo trace:** Abstract, nearly isothermal responses of two cable designs. **Trạng thái:** `DIRECTLY_VERIFIED_SELECTED_PDF_PASSAGE_AND_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “the nearly isothermal, superelastic responses of the two cable designs are presented and compared”
- **Ranh giới/ghi chú:** Chỉ trong điều kiện nguồn; chuyển giao sang MP1 phải được kiểm tra.

**CH2-S2-R0013-A01 — mục 2.2.1.** Với TiNi, phải chỉ rõ trạng thái pha, nhiệt độ, nhánh tải và miền tuyến tính hóa khi dùng một giá trị E để mô tả đáp ứng, vì chuyển pha có thể làm quan hệ cơ học thay đổi theo trạng thái [2].

- **Vị trí PDF theo trace:** §1, cơ chế chuyển pha; đối chiếu §5.1 PDF8 Fig. 6. **Trạng thái:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “temperature-induced or stress-induced martensitic transformation”
- **Ranh giới/ghi chú:** Nguồn đo kéo cáp và dây lõi, không đo E theo mọi nhiệt độ và không lập luật uốn MP1.

**CH2-S2-R0014-A01 — mục 2.2.1.** Các đường kéo–dỡ tải của dây lõi trong [2] có những miền chuyển pha khác miền đàn hồi ban đầu; chúng không hỗ trợ việc gán một hằng số Young duy nhất cho toàn chu trình TiNi.

- **Vị trí PDF theo trace:** §5.1, Fig. 6(b), core wires. **Trạng thái:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “Both wires are superelastic at room temperature”
- **Ranh giới/ghi chú:** Suy luận giới hạn mô hình từ phép kéo; không chuyển giá trị mô đun cáp sang dây hoặc MP1.

**CH2-S2-R0083-A01 — mục 2.2.2.** Nó không nhận diện duy nhất ma sát: thí nghiệm kéo cáp TiNi của Reedlunn và cộng sự cho thấy vòng trễ gắn với đáp ứng siêu đàn hồi và đáp ứng còn thay đổi theo chu kỳ [2].

- **Vị trí PDF theo trace:** §5.4; Fig. 15. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “the evolution of the mechanical response”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0113-A01 — mục 2.2.2.** Riêng TiNi, chỉ quan sát vòng trễ chưa đủ để kết luận có biến dạng dẻo, vì chuyển pha siêu đàn hồi cũng tạo đáp ứng có trễ [2].

- **Vị trí PDF theo trace:** §5.1, đoạn mô tả Fig. 6(b); vòng trễ trong cùng đoạn. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “Both wires are superelastic at room temperature, but the mechanical responses are not identical. The 7  7 core wire has a larger loading plateau stress (526 MPa versus 481 MPa), a larger plateau strain (7.2% versus 5.0%, during loading), and a narrower stress”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S4-R0001-A01 — mục 2.4.1.** Ở trạng thái nhiệt độ cao hơn miền chuyển pha, TiNi có thể ở pha austenit; khi nhiệt độ hoặc ứng suất thay đổi theo điều kiện thích hợp, vật liệu có thể chuyển sang martensit. Chuyển pha martensit có thể được kích hoạt bởi nhiệt hoặc bởi ứng suất, và chiều ngược lại phụ thuộc vào nhiệt độ, ứng suất và lịch sử biến dạng. Reedlunn và cộng sự mô tả austenit và martensit như hai pha nền của đáp ứng NiTi, đồng thời nhấn mạnh rằng cùng một vật liệu có thể biểu hiện hiệu ứng nhớ hình hoặc siêu đàn hồi ở gần nhiệt độ phòng tùy vị trí của các nhiệt độ chuyển pha [2, tr. 2–4]. Do đó, cụm từ “dây TiNi” chưa đủ để xác định mô đun hay miền ứng xử; cần biết trạng thái nhiệt–cơ và điều kiện gia công của dây.

- **Vị trí PDF theo trace:** physical PDF p.2, Abstract/Introduction. **Trạng thái:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S6-R0037-A01 — mục 2.6.1.** Với TiNi, thí nghiệm kéo gần đẳng nhiệt của Reedlunn và cộng sự cung cấp bằng chứng về đáp ứng vật liệu và cấu trúc cáp [2].

- **Vị trí PDF theo trace:** {"M26-E01": "Abstract; §5.1; Fig. 6"}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “Here in Part I, the nearly isothermal, superelastic responses of the two cable designs are presented”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0119-A01 — mục 2.6.2.** Đối với cáp TiNi, Reedlunn và cộng sự đã kết hợp kéo chậm gần đẳng nhiệt, nhiệt lượng quét vi sai, đo trường biến dạng và nhiệt độ, cùng các phép thử chu trình [2].

- **Vị trí PDF theo trace:** {"M26-E01": ["Abstract / Introduction; Introduction; direct page/anchor controls"], "M26-E03": ["Sec. 3.2 calorimetry; Fig. 3; direct page/anchor controls"], "M26-E04": ["Experimental matrix; Table 1–2; Fig. 5; direct page/anchor controls"], "M26-E07": ["Sec. 5.4 / conclusions; Fig. 14–15; direct page/anchor controls", "Sec. 5.4 / conclusions; Fig. 14–15; direct page/anchor controls"]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “Part I reports nearly isothermal tension data for two NiTi cable constructions; structural/constitutive modeling is left for future work.; DSC reports two-step transformations and different transition temperatures; 7×7 is clearly superelastic at room temperatu”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0174-A01 — mục 2.6.3.** Thí nghiệm kéo gần đẳng nhiệt của Reedlunn và cộng sự còn cung cấp nhiệt lượng quét vi sai, trường biến dạng, trường nhiệt và đáp ứng chu trình của cáp TiNi [2].

- **Vị trí PDF theo trace:** {"M26-E01": ["Abstract; §5 opening"], "M26-E03": ["§3.2; Fig.3"], "M26-E04": ["§4 Experimental setup; Figs.4–5; Tables1–2"], "M26-E07": ["§5.4; Figs.13–15; §6"]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0227-A01 — mục 2.6.4.** Trong thí nghiệm kéo gần đẳng nhiệt trên cáp TiNi, Reedlunn và cộng sự đã dùng quan sát biến dạng và nhiệt độ, đồng thời ghi nhận sự thay đổi đáp ứng qua chu trình [2].

- **Vị trí PDF theo trace:** {"M26-E01":[{"physical_pages":[1],"printed_pages":["1 in proof"],"exact_locator":"Abstract","anchors":["nearly isothermal","stereo digital image correlation and infrared imaging"]}],"M26-E04":[{"physical_pages":[4,5,6,7],"printed_pages":["4","5","6","7"],"exact_locator":"§3.3–3.4 Figs.4–5 Table1","anchors":["Temperature was monitored simultaneously","laser extensometry and stereo DIC","spurious strains"]}],"M26-E07":[{"physical_pages":[14,15,16,17],"printed_pages":["14","15","16","17"],"exact_locator":"§5.4 Figs.13–15 and §6","anchors":["We do not have DIC data for this experiment","six","predicted asymptotic"]}]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “Part I reports nearly isothermal tension data for two NiTi cable constructions; structural/constitutive modeling is left for future work.; The study combines LE, DIC, thermocouples and IR; Table 2 records specimen dimensions, cycles and strain rates.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.

### [3] Y. Kotb, I. Elgamal & M. Serry (2021), “Shape Memory Alloy Capsule Micropump for Drug Delivery Applications”

**CH2-S1-R0016-A01 — mục 2.1.1.** Kotb và cộng sự đã công bố bơm dùng lò xo SMA tác động lên vỏ silicone, có khảo sát lực–chuyển vị và cột áp tĩnh [3].

- **Vị trí PDF theo trace:** §2.2 Pump Operation; §4.3 Characterization. **Trạng thái:** `DIRECTLY_VERIFIED_SELECTED_PDF_PASSAGE_AND_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “the spring is the silicone enclosure || The pump’s displacement, discharge, volume ﬂow rate, static pressure head”
- **Ranh giới/ghi chú:** Chỉ trong điều kiện nguồn; chuyển giao sang MP1 phải được kiểm tra.

**CH2-S2-R0156-A01 — mục 2.2.3.** Tương tự, áp suất cột áp tĩnh của bơm SMA do Kotb và cộng sự báo cáo là một đại lượng đầu ra của bơm [3]; nó không đo tải pháp tuyến tại mạng tiếp xúc MP1.

- **Vị trí PDF theo trace:** §5.5, text and Figs. 11–12. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “static head pressure response”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S4-R0099-A01 — mục 2.4.4.** Kotb, Elgamal và Serry dùng lò xo SMA bằng NiTi cuốn quanh vỏ silicone đàn hồi. Gia nhiệt Joule làm lò xo co, nén buồng và đẩy chất lưu ra; khi nguội, vỏ tạo lực hồi phục, kéo lò xo giãn và hút chất lưu cho chu kỳ tiếp theo. Vỏ vừa chứa chất lưu vừa là phần tử hồi phục. Đường truyền lực vì vậy khác một xi lanh cứng có piston trượt [3, tr. 3–4].

- **Vị trí PDF theo trace:** §§2.1–2.3; Figs1–2. **Trạng thái:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0100-A01 — mục 2.4.4.** Đồ thị lực–chuyển vị của tác giả mô tả vị trí cân bằng bằng giao điểm đường lực của lò xo và vỏ. Khi pha SMA thay đổi, đường lực và giao điểm dịch chuyển. Bài báo quy áp suất nén cực đại cho chênh lực giữa lò xo ở pha austenit và vỏ, nhưng không cung cấp phương trình chuyển đổi áp suất có quy ước dấu. Tại giao điểm, hai lực bằng nhau. Bởi vậy, chênh lực có khả năng dẫn động nén ở một cấu hình không được coi là một hằng số duy trì suốt chu kỳ, cũng không được gán thành lực dư tại chính điểm cân bằng [3, tr. 3].

- **Vị trí PDF theo trace:** §2.2; Fig1. **Trạng thái:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0101-A01 — mục 2.4.4.** Mô hình của công trình chỉ tìm hai đầu hành trình với giả định austenit hoàn toàn khi nóng và martensit hoàn toàn khi nguội. Tác dụng của chất lưu được bỏ qua tại hai đầu đứng yên; độ mềm của vỏ silicone được mô tả bằng đặc tính lực–chuyển vị đo thực nghiệm, xấp xỉ tuyến tính trong miền làm việc. Mô hình này không xác định toàn bộ diễn biến cơ–nhiệt trung gian. Đặc biệt, giả định bỏ tải chất lưu ở đầu hành trình không cho phép bỏ tải đó trong quá trình nén có dòng chảy [3, tr. 4–5].

- **Vị trí PDF theo trace:** §3; Fig3; phần lực–độ dịch silicone. **Trạng thái:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0102-A01 — mục 2.4.4.** Trong một chế độ điều khiển của bơm ba vòng, tác giả đặt thể tích đẩy mục tiêu 43 mm³ mỗi hành trình và dòng cực đại 790 mA, rồi báo cáo áp suất cột áp tĩnh 6,5 kPa theo chu kỳ. Đây là đầu ra của hệ bơm ở cấu hình thử. Phần trình bày chưa chỉ rõ đầy đủ vị trí lấy áp và mốc tham chiếu để quy giá trị ấy thành áp suất tại một mẫu cơ học khác [3, tr. 12].

- **Vị trí PDF theo trace:** §5.5; Fig12. **Trạng thái:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0103-A01 — mục 2.4.4.** Trong bơm của Kotb và cộng sự, van lá được tạo tiền ép để hạn chế rò theo mô tả thiết kế. Chi tiết này không phải phép đo độ kín của một piston khác. Xấp xỉ độ cứng tuyến tính của vỏ cũng chỉ có cơ sở trong khoảng khảo sát [3, tr. 4–5]. Tương tự, tăng khả năng tản nhiệt có thể rút ngắn làm nguội nhưng đồng thời làm giảm mức gia nhiệt, hành trình và lưu lượng trong điều kiện khảo sát. Bài toán chu kỳ vì vậy phải giữ cả hai nửa nóng và nguội [3, tr. 9–10].

- **Vị trí PDF theo trace:** §5.2; Figs7–8. **Trạng thái:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0105-A01 — mục 2.4.4.** Trong bơm của Kotb và cộng sự, van lá được tạo tiền ép để hạn chế rò theo mô tả thiết kế. Chi tiết này không phải phép đo độ kín của một piston khác. Xấp xỉ độ cứng tuyến tính của vỏ cũng chỉ có cơ sở trong khoảng khảo sát [3, tr. 4–5]. Tương tự, tăng khả năng tản nhiệt có thể rút ngắn làm nguội nhưng đồng thời làm giảm mức gia nhiệt, hành trình và lưu lượng trong điều kiện khảo sát. Bài toán chu kỳ vì vậy phải giữ cả hai nửa nóng và nguội [3, tr. 9–10].

- **Vị trí PDF theo trace:** §2.3; Fig2. **Trạng thái:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S6-R0052-A01 — mục 2.6.1.** Tiền lệ chuyển từ tác động SMA sang áp suất còn xuất hiện trong bơm vi mô dùng lò xo NiTi quấn quanh vỏ silicone [3].

- **Vị trí PDF theo trace:** {"M34-E02": "§2.1–2.2; Fig. 1"}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “The maximum fluid pressure pumped during compression is caused by the”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0127-A01 — mục 2.6.2.** Tương tự, bơm vi mô của Kotb và cộng sự đã đo áp suất tĩnh và đáp ứng bơm, nên khả năng chuyển tác động SMA thành áp suất đầu ra đã có tiền lệ [3].

- **Vị trí PDF theo trace:** {"M34-E02": ["§2.1 Pump Characteristics; §2.2 Pump Operation; Fig. 1"], "M34-E07": ["§4.3 Characterization; Fig. 4"], "M34-E09": ["§5.5 Controlled Volume Pumping; Fig. 12"]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “Heating moves SMA force–deflection curve to austenite and contracts the enclosure; cooling lets enclosure stiffness restore the coil; fluid pressure during compression is caused by force difference between austenite coil and silicone container.; Characterizati”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0188-A01 — mục 2.6.3.** Nguồn bơm còn có phép thử diễn biến chuyển vị và lưu lượng, nên không thể đặt câu hỏi trên giả định rằng tác động SMA hoặc đáp ứng theo thời gian hoàn toàn chưa được khảo sát [3].

- **Vị trí PDF theo trace:** {"M34-E08": ["§5.1–5.3 Figs.5–10"]}. **Trạng thái:** `INFERENCE_WITH_DIRECT_PDF_VERIFIED_INGREDIENTS`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0235-A01 — mục 2.6.4.** Kotb và cộng sự đã công bố bơm dùng lò xo SMA tương tác với vỏ silicone, với các đặc trưng lực–chuyển vị, cột áp tĩnh và đáp ứng theo thời gian được khảo sát thực nghiệm [3].

- **Vị trí PDF theo trace:** {"M34-E02":[{"physical_pages":[3],"printed_pages":["3"],"exact_locator":"§2.1–2.2 Fig.1","anchors":["instantaneous SMA material phase","difference in force"]}],"M34-E07":[{"physical_pages":[8],"printed_pages":["8"],"exact_locator":"§4.3 Characterization","anchors":["displacement, discharge, volume flow rate, static pressure head","force-displacement responses"]}],"M34-E08":[{"physical_pages":[8,9,10,11],"printed_pages":["8","9","10","11"],"exact_locator":"§5.1–5.3 Figs.5–10","anchors":["Pump displacement vs. time","Volume flow rate vs. frequency"]}],"M34-E09":[{"physical_pages":[11,12,13],"printed_pages":["11","12","13"],"exact_locator":"§5.4–5.5 Figs.11–12 Table3","anchors":["static head pressure","43 mm3","6.5 kPa"]}]}. **Trạng thái:** `DIRECT_PDF_VERIFIED`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “Heating moves SMA force–deflection curve to austenite and contracts the enclosure; cooling lets enclosure stiffness restore the coil; fluid pressure during compression is caused by force difference between austenite coil and silicone container.; Characterizati”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.

### [4] IEEE Publication Operations (2025), IEEE Reference Guide, ver. 3.28.2025

**CH2-S1-R0124-A01 — mục 2.1.4.** Theo hướng dẫn IEEE, số trích dẫn đặt trong ngoặc vuông, nguồn được dẫn lại giữ cùng số và có thể bổ sung vị trí cụ thể khi viện dẫn một phần của tài liệu [4]. 

- **Vị trí PDF theo trace:** physical/printed p.4, I.A–B; II.Style. **Trạng thái:** `SOURCE_SUPPORT_VERIFIED_FOR_STYLE`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “in square brackets; cite the earlier reference number”
- **Ranh giới/ghi chú:** Quy tắc tác giả hoặc governance; không phải kết quả cơ học/thực nghiệm MP1.

### [5] J. Burgner-Kahrs, D. C. Rucker & H. Choset (2015), “Continuum Robots for Medical Applications: A Survey”

**CH2-S2-R0001-A01 — mục 2.2.1.** Robot continuum là lớp cơ cấu có thể được chấp hành để thân uốn liên tục; định nghĩa của Burgner-Kahrs và cộng sự dựa trên các đường cong có vectơ tiếp tuyến liên tục trong vật liệu cấu tạo [5].

- **Vị trí PDF theo trace:** §II-A, Definition 1. **Trạng thái:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “constitutive material forms curves with continuous tangent vectors”
- **Ranh giới/ghi chú:** Định nghĩa phân loại, không xác lập tuyến tính vật liệu hoặc cấu trúc tiếp xúc.

**CH2-S2-R0005-A01 — mục 2.2.1.** Mô tả hình học như vậy chưa phải quan hệ tải–biến dạng: muốn dự đoán hình dạng dưới tải còn cần cân bằng cơ học, quan hệ cấu thành và điều kiện biên [5].

- **Vị trí PDF theo trace:** §II-D2, đoạn sau Eqs. (3)–(4). **Trạng thái:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “through some material constitutive law”
- **Ranh giới/ghi chú:** Khung thanh; không suy ra các tham số cho MP1.

**CH2-S2-R0006-A01 — mục 2.2.1.** Xấp xỉ độ cong hằng từng đoạn chỉ là một lựa chọn biểu diễn, trong đó độ cong không đổi theo chiều dài cung của mỗi đoạn, chứ không nhất thiết không đổi theo thời gian [5].

- **Vị trí PDF theo trace:** §II-D1, constant-curvature frameworks. **Trạng thái:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “invariance with respect to arc length, not time”
- **Ranh giới/ghi chú:** Không phải định nghĩa phổ quát của robot continuum.

**CH2-S2-R0007-A01 — mục 2.2.1.** Dạng hình học này có thể được giả thiết trước hoặc xuất hiện từ một số thiết kế và giả thiết cơ học cụ thể; các trường hợp không phù hợp cần biểu diễn độ cong biến thiên [5].

- **Vị trí PDF theo trace:** §II-D1, đoạn constant-curvature assumption. **Trạng thái:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “certain robot designs and assumptions”
- **Ranh giới/ghi chú:** Không gán điều kiện độ cong hằng cho MP1.

**CH2-S2-R0010-A01 — mục 2.2.1.** Các tương tác không được giữ tường minh phải được bỏ qua có lý do hoặc phản ánh qua quan hệ hiệu dụng; lựa chọn này xác định những gì mô hình có thể dự đoán [5].

- **Vị trí PDF theo trace:** §II-D2–D3, single-rod building block và modeling principles. **Trạng thái:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “extended or coupled to other models”
- **Ranh giới/ghi chú:** Quy tắc chọn mô hình; không có sai số hay miền hiệu lực MP1 đã xác lập.

**CH2-S2-R0017-A01 — mục 2.2.1.** Trong mô hình uốn đàn hồi tuyến tính thích hợp, mô men uốn tỷ lệ với thay đổi độ cong so với cấu hình tự nhiên, thay vì luôn tỷ lệ với độ cong tuyệt đối [5].

- **Vị trí PDF theo trace:** §II-D2, đoạn Bernoulli–Euler constitutive law. **Trạng thái:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “internal moment is proportional to change in curvature”
- **Ranh giới/ghi chú:** Quan hệ M=EIΔκ trong nguồn; bản thảo chỉ diễn giải, không coi là luật tổng quát cho chuyển pha/trượt/vòng trễ.

**CH2-S2-R0029-A01 — mục 2.2.1.** Bỏ qua biến dạng cắt và tuyến tính hóa hình học là hai lựa chọn khác nhau: lý thuyết elastica Bernoulli–Euler vẫn có thể mô tả độ võng lớn, nên chuyển vị lớn tự nó chưa đủ để bác bỏ mọi mô hình dầm [5].

- **Vị trí PDF theo trace:** §II-D2, đoạn large-deflection elastica. **Trạng thái:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Mẩu văn bản/anchor được CSV lưu (cần đối chiếu PDF gốc):** “planar, large-deflection, Bernoulli–Euler elastica theory”
- **Ranh giới/ghi chú:** Không dùng công thức độ võng nhỏ cho trường hợp quay lớn nếu chưa biện minh.

## Nhận xét audit vòng này

- **[1]** Nguồn về bó sợi nylon/áp suất dương hỗ trợ các mô tả của chính nguyên mẫu. Mọi chuyển giao sang bó dây TiNi hoặc kết luận về luật áp suất–tiếp xúc phải được xem là suy luận, trừ khi câu nêu rõ phạm vi kiến trúc gốc.
- **[2]** Nguồn là thí nghiệm kéo gần đẳng nhiệt trên cáp NiTi. Nó hỗ trợ tính phụ thuộc cấu trúc/chu trình và chuyển pha trong điều kiện của bài; không trực tiếp xác nhận đáp ứng uốn MP1.
- **[3]** Nguồn khảo sát micropump dùng lò xo SMA và vỏ silicone. Đây là tiền lệ cho nguồn áp suất; không phải phép đo lực pháp tuyến trong bó dây hay xác nhận thiết kế piston của MP1.
- **[4]** Chỉ hỗ trợ quy tắc trình bày tài liệu tham khảo. Bản PDF được trỏ tới đường dẫn `/tmp` trong trace không còn được định vị ở kho nguồn hiện tại; cần bổ sung bản lưu cố định nếu muốn audit độc lập.
- **[5]** Survey hỗ trợ định nghĩa/khung continuum và mô hình hóa. Các claim từ survey cần giới hạn theo đúng nội dung tổng quan; không xem đây là kết quả thực nghiệm hay mô hình vật liệu TiNi. Một số claim có excerpt quá ngắn hoặc thiếu page number trong CSV.
- Các `source_locator` trong CSV phần lớn là mục/tiểu mục, không phải số trang PDF vật lý. Tôi giữ nguyên locator và excerpt đã lưu, chưa tái trích xuất từng câu trực tiếp từ PDF trong vòng này; vì vậy các excerpt này là dấu vết dẫn đường, chưa được gắn nhãn VERIFIED FULL TEXT. Các mục thiếu số trang cần kiểm tiếp trên PDF.

## Provenance và tài liệu đầu vào

- Bản nháp: `outputs/thesis_drafts/chapter_2/chapter_2_integrated/chap_2_draf.md`
- Traceability: `outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv`
- Changelog: `outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_INTEGRATION_CHANGELOG.md`
- PDF đóng gói: `outputs/thesis_drafts/chapter_2/chapter_2_integrated/tai_lieu_tham_khao_pdf/01…05` (PDF [4] không thấy trong danh mục này).


---

# Tiếp nối audit: tài liệu tham khảo [6]–[10]

**Phạm vi:** tiếp tục từ bản audit [1]–[5], dùng cùng bản nháp và cùng master traceability. Các excerpt dưới đây được chép từ trường `source_fragment`/anchor hiện có; locator được giữ đúng như trace ghi. Đây là dấu dẫn để mở PDF, chưa phải xác nhận độc lập từng câu từ PDF.

| Ref | Nguồn | DOI | Claim/anchor duy nhất | PDF đóng gói |
|---:|---|---|---:|---|
| [6] | M. Russo, S. M. H. Sadati, X. Dong, A. Mohammad, I. D. Walker, C. Bergeles, K. Xu & D. A. Axinte (2023), “Continuum Robots: An Overview” | 10.1002/aisy.202200367 | 2 | `06_M03__2023-Russo-Continuum Robots An Overview.pdf` |
| [7] | H. Jeon, Q. N. Le, S. Jeong, S. Jang, H. Jung, H. Chang, H. J. Pandya & Y. Kim (2022), “Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism” | 10.1109/lra.2022.3174363 | 21 | `07_M31__2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf` |
| [8] | Y. Zhang, J. Wang, G. Ye & R. Xu (2018), “Bending Stiffness of Parallel Wire Cables Including Interfacial Slips among Wires” | 10.1061/(asce)st.1943-541x.0002171 | 12 | `08_M22__2018-Bending Stiffness of Parallel Wire Cables.pdf` |
| [9] | Y. S. Narang, J. J. Vlassak & R. D. Howe (2018), “Mechanically Versatile Soft Machines through Laminar Jamming” | 10.1002/adfm.201707136 | 13 | `09_2018-Mechanically Versatile Soft Machines through Laminar.pdf` |
| [10] | F. Caruso, G. Mantriota, V. Moramarco & G. Reina (2023), “Layer jamming: Modeling and experimental validation” | 10.1016/j.ijmecsci.2023.108325 | 5 | `10_2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf` |

## [6] M. Russo, S. M. H. Sadati, X. Dong, A. Mohammad, I. D. Walker, C. Bergeles, K. Xu & D. A. Axinte (2023), “Continuum Robots: An Overview”

**CH2-S2-R0003-A01 — mục 2.2.1.** Để mô tả hình dạng, có thể thay thân vật lý bằng một đường trục cùng trường định hướng tiết diện dọc thân; trong biểu diễn thanh Cosserat được Russo và cộng sự trình bày, đường trục đi qua trọng tâm tiết diện và được tham số hóa theo chiều dài cung ở cấu hình ban đầu [6].

- **Locator PDF trong trace:** §3.1.3, đoạn trước Eqs. (6)–(8). **Trạng thái trace:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Excerpt/anchor đã lưu:** “A Cosserat rod is defined by its centerline”
- **Ranh giới/ghi chú:** Đoạn PDF đã đọc trực tiếp; không dùng locator M03-E02 trang 3 bị sai.

**CH2-S2-R0028-A01 — mục 2.2.1.** Với giả thiết Euler–Bernoulli thông thường, tiết diện giữ vuông góc với đường trục nên bỏ qua biến dạng cắt; mô tả thanh cho phép tiết diện nghiêng so với tiếp tuyến có thể giữ biến dạng cắt [6].

- **Locator PDF trong trace:** §3.1.3, đoạn rigid cross section. **Trạng thái trace:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Excerpt/anchor đã lưu:** “not necessarily normal to the tangent”
- **Ranh giới/ghi chú:** Phân biệt động học tiết diện; không suy cùng một luật vật liệu cho các lý thuyết.


## [7] H. Jeon, Q. N. Le, S. Jeong, S. Jang, H. Jung, H. Chang, H. J. Pandya & Y. Kim (2022), “Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism”

**CH2-S2-R0022-A01 — mục 2.2.1.** Trong thí nghiệm của Jeon và cộng sự, độ cứng robot được lấy từ độ dốc lực cản–chuyển vị của đĩa đầu, còn độ cứng uốn được suy ra bằng xấp xỉ dầm công xôn [7].

- **Locator PDF trong trace:** §IV-B, đoạn stiffness slope và Eq. (10). **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Excerpt/anchor đã lưu:** “The stiffness is the slope of the resistive force vs. displacement graph”
- **Ranh giới/ghi chú:** Thí nghiệm riêng với đĩa đầu, góc uốn nhỏ; không chuyển công thức sang MP1.

**CH2-S4-R0055-A01 — mục 2.4.3.** Cơ cấu của Jeon và cộng sự [7] cung cấp một tiền lệ trực tiếp cho đường truyền lực này. Thân robot có lõi polyuretan nhiệt dẻo (TPU) ở giữa và tám dây siêu đàn hồi bố trí xung quanh, đi qua các đĩa dẫn hướng. Các dây chỉ cố định tại đế nên có thể trượt qua những đĩa còn lại khi thân uốn. Một ống cao su bao quanh đoạn trung tâm, còn lò xo SMA quấn bên ngoài ống. Khi nung nóng, lò xo có xu hướng phục hồi về đường kính trong đã ghi nhớ nhỏ hơn. Sự phục hồi bị ống và các dây cản lại tạo tác dụng siết hướng kính, ép cao su vào dây và hạn chế chuyển động trượt. Lõi TPU và ống cao su có vai trò riêng trong cấu trúc này. Bề mặt điều biến ma sát được khảo sát là tiếp xúc dây với cao su, chưa phải bằng chứng cho cơ chế kẹt giữa các dây trong một bó dây.

- **Locator PDF trong trace:** M31:2–3; Secs.II.A–II.B; Fig.1. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0056-A01 — mục 2.4.3.** Cơ cấu của Jeon và cộng sự [7] cung cấp một tiền lệ trực tiếp cho đường truyền lực này. Thân robot có lõi polyuretan nhiệt dẻo (TPU) ở giữa và tám dây siêu đàn hồi bố trí xung quanh, đi qua các đĩa dẫn hướng. Các dây chỉ cố định tại đế nên có thể trượt qua những đĩa còn lại khi thân uốn. Một ống cao su bao quanh đoạn trung tâm, còn lò xo SMA quấn bên ngoài ống. Khi nung nóng, lò xo có xu hướng phục hồi về đường kính trong đã ghi nhớ nhỏ hơn. Sự phục hồi bị ống và các dây cản lại tạo tác dụng siết hướng kính, ép cao su vào dây và hạn chế chuyển động trượt. Lõi TPU và ống cao su có vai trò riêng trong cấu trúc này. Bề mặt điều biến ma sát được khảo sát là tiếp xúc dây với cao su, chưa phải bằng chứng cho cơ chế kẹt giữa các dây trong một bó dây.

- **Locator PDF trong trace:** M31:2–3; Sec.II.A; Fig.1d–f. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0056-A02 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:2–3; Sec.II.A; Fig.1d–f. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0057-A01 — mục 2.4.3.** Giá trị của nghiên cứu [7] nằm ở việc đo lực trượt riêng bên cạnh đáp ứng uốn của toàn thân. Trong phép thử ma sát, một dây được kéo qua ống cao su, còn bảy dây được giữ cố định. Hành trình kéo là 5 mm với tốc độ 10 mm/phút; mỗi cấu hình đường kính và trạng thái pha được lặp lại mười lần. Phép thử này cho phép quan sát trực tiếp lực cản kéo dây khi thay đổi trạng thái của lò xo SMA. Tuy nhiên, lực kéo đo được là kết quả của tiếp xúc trong cấu hình thử cụ thể, không phải phép đo riêng lực kẹp của lò xo hoặc lực pháp tuyến cục bộ. Khi chưa xác định độc lập tải ép, cũng không thể dùng lực kéo để suy ra duy nhất hệ số ma sát. Giá trị đỉnh hoặc trung bình trên hành trình thử chỉ đặc trưng cho quy trình đó, chưa đủ để coi là giới hạn chống trượt chung của cơ cấu [7].

- **Locator PDF trong trace:** M31:5–6; Sec.IV.A; Fig.4;TableI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0058-A01 — mục 2.4.3.** Cơ cấu của Jeon và cộng sự [7] cung cấp một tiền lệ trực tiếp cho đường truyền lực này. Thân robot có lõi polyuretan nhiệt dẻo (TPU) ở giữa và tám dây siêu đàn hồi bố trí xung quanh, đi qua các đĩa dẫn hướng. Các dây chỉ cố định tại đế nên có thể trượt qua những đĩa còn lại khi thân uốn. Một ống cao su bao quanh đoạn trung tâm, còn lò xo SMA quấn bên ngoài ống. Khi nung nóng, lò xo có xu hướng phục hồi về đường kính trong đã ghi nhớ nhỏ hơn. Sự phục hồi bị ống và các dây cản lại tạo tác dụng siết hướng kính, ép cao su vào dây và hạn chế chuyển động trượt. Lõi TPU và ống cao su có vai trò riêng trong cấu trúc này. Bề mặt điều biến ma sát được khảo sát là tiếp xúc dây với cao su, chưa phải bằng chứng cho cơ chế kẹt giữa các dây trong một bó dây.

- **Locator PDF trong trace:** M31:5–6; Sec.IV.A; Fig.4c–e;TableI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0058-A02 — mục 2.4.3.** Giá trị của nghiên cứu [7] nằm ở việc đo lực trượt riêng bên cạnh đáp ứng uốn của toàn thân. Trong phép thử ma sát, một dây được kéo qua ống cao su, còn bảy dây được giữ cố định. Hành trình kéo là 5 mm với tốc độ 10 mm/phút; mỗi cấu hình đường kính và trạng thái pha được lặp lại mười lần. Phép thử này cho phép quan sát trực tiếp lực cản kéo dây khi thay đổi trạng thái của lò xo SMA. Tuy nhiên, lực kéo đo được là kết quả của tiếp xúc trong cấu hình thử cụ thể, không phải phép đo riêng lực kẹp của lò xo hoặc lực pháp tuyến cục bộ. Khi chưa xác định độc lập tải ép, cũng không thể dùng lực kéo để suy ra duy nhất hệ số ma sát. Giá trị đỉnh hoặc trung bình trên hành trình thử chỉ đặc trưng cho quy trình đó, chưa đủ để coi là giới hạn chống trượt chung của cơ cấu [7].

- **Locator PDF trong trace:** M31:5–6; Sec.IV.A; Fig.4c–e;TableI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0058-A03 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:5–6; Sec.IV.A; Fig.4c–e;TableI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0059-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:5–6; Sec.IV.B; Fig.5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0060-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:6; Sec.IV.B; Eq.10 (omitted). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0061-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:3–5,7; Sec.III;Sec.V; Fig.3;Eqs.1–9 (omitted). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0062-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:6–7; Secs.IV.B/V; TablesII–III. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0063-A01 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:3,5–7; Secs.II.B;IV introduction;IV.C/V; Fig.6. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0064-A01 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:6–7; Sec.IV.C/V; Fig.6b–c. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0065-A01 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:7; Sec.V Discussion/Conclusion; Limitations paragraph. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0076-A02 — mục 2.4.3.** Giá trị của nghiên cứu [7] nằm ở việc đo lực trượt riêng bên cạnh đáp ứng uốn của toàn thân. Trong phép thử ma sát, một dây được kéo qua ống cao su, còn bảy dây được giữ cố định. Hành trình kéo là 5 mm với tốc độ 10 mm/phút; mỗi cấu hình đường kính và trạng thái pha được lặp lại mười lần. Phép thử này cho phép quan sát trực tiếp lực cản kéo dây khi thay đổi trạng thái của lò xo SMA. Tuy nhiên, lực kéo đo được là kết quả của tiếp xúc trong cấu hình thử cụ thể, không phải phép đo riêng lực kẹp của lò xo hoặc lực pháp tuyến cục bộ. Khi chưa xác định độc lập tải ép, cũng không thể dùng lực kéo để suy ra duy nhất hệ số ma sát. Giá trị đỉnh hoặc trung bình trên hành trình thử chỉ đặc trưng cho quy trình đó, chưa đủ để coi là giới hạn chống trượt chung của cơ cấu [7].

- **Locator PDF trong trace:** M31:2–3,5–6; Mechanical pathway synthesis; No equation. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S4-R0077-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:5–7;M32:7–8;M37:4–6; Cross-study observable comparison; Original comparison table. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S6-R0047-A01 — mục 2.6.1.** Vai trò chấp hành của SMA đã được khai thác trong một cơ cấu khác, nơi lò xo SMA bao quanh ống cao su để điều chỉnh tương tác với các dây ngoại vi [7].

- **Locator PDF trong trace:** {"M31-E01": "§II.A; Fig. 1"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “The core of the proposed stiffness control mechanism is the frictional force”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0123-A01 — mục 2.6.2.** Một phản chứng đối với nhận định rằng các nghiên cứu chỉ đo đáp ứng toàn cục xuất hiện trong cơ cấu SMA của Jeon và cộng sự: tác giả kéo riêng một dây trong ống cao su để đo ma sát, tách khỏi thử uốn [7].

- **Locator PDF trong trace:** {"M31-E06": ["§IV.A Friction Force Characterization; Fig. 4; Table I"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “A single wire is attached; friction force tests were repeated ten times”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0165-A01 — mục 2.6.3.** Jeon và cộng sự đã đo riêng lực cản khi kéo một dây qua ống cao su trong cơ cấu siết bằng lò xo SMA [7].

- **Locator PDF trong trace:** {"M31-E01": ["§II-A; Fig.1"], "M31-E06": ["§IV-A; Fig.4; TableI"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “CSV chỉ có nội dung finding tóm tắt, không có quote anchor.”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0220-A01 — mục 2.6.4.** Jeon và cộng sự đã bổ sung phép kéo một dây tương đối với ống cao su để đo lực cản riêng, bên cạnh phép đánh giá độ cứng toàn cơ cấu [7].

- **Locator PDF trong trace:** {"M31-E06":[{"physical_pages":[5],"printed_pages":["6586"],"exact_locator":"IV. Experiment Setup and Result; A. Friction Force Characterization; Fig.4","anchor":"repeated ten times"},{"physical_pages":[6],"printed_pages":["6587"],"exact_locator":"IV.A continued; TableI; IV.B Stiffness Characterization of the Robot; TableII","anchor":"slope of the resistive force"}],"M31-E07":[{"physical_pages":[6],"printed_pages":["6587"],"exact_locator":"IV.A continued; TableI; IV.B Stiffness Characterization of the Robot; TableII","anchor":"slope of the resistive force"},{"physical_pages":[7],"printed_pages":["6588"],"exact_locator":"IV.B continued; TableIII","anchor":"modeled ﬂexural rigidity"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “CSV chỉ có nội dung finding tóm tắt, không có quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.


## [8] Y. Zhang, J. Wang, G. Ye & R. Xu (2018), “Bending Stiffness of Parallel Wire Cables Including Interfacial Slips among Wires”

**CH2-S2-R0031-A01 — mục 2.2.1.** Mô hình cáp dây song song của Zhang và cộng sự dùng các lớp tương đương có cùng độ võng và độ cong, không cho tách lớp, nhưng vẫn cho phép trượt dọc tương đối tại giao diện [8].

- **Locator PDF trong trace:** Modeling and Formulation, assumptions 1–3. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Excerpt/anchor đã lưu:** “Slip is allowed at each interface”
- **Ranh giới/ghi chú:** Cáp được thay bằng lớp chữ nhật bảo toàn chiều cao/diện tích; không phải hình học dây tròn MP1.

**CH2-S2-R0032-A01 — mục 2.2.1.** Nguồn còn đưa vào độ cứng trượt đã hiệu chuẩn và nêu rõ tương tác ma sát thực phức tạp hơn giả thiết giao diện tuyến tính [8].

- **Locator PDF trong trace:** Eq. (4) và đoạn giới hạn ngay sau. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Excerpt/anchor đã lưu:** “not elastic because of the friction among wires”
- **Ranh giới/ghi chú:** Độ cứng trượt của giao diện khác K lực–chuyển vị của toàn cơ cấu.

**CH2-S2-R0033-A01 — mục 2.2.1.** Ví dụ này cho thấy cùng độ võng ngang không đồng nghĩa cùng biến dạng dọc của mọi phần tử; giả thiết tiết diện liên hợp hoàn toàn cần được kiểm tra khi có chuyển vị tương đối [8].

- **Locator PDF trong trace:** Assumptions 2–3; PDF3 Eqs. (4)–(5). **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Excerpt/anchor đã lưu:** “Each rectangular layer has the same curvature and deflection”
- **Ranh giới/ghi chú:** Suy từ cấu trúc biến của mô hình, không khẳng định MP1 đã có trượt.

**CH2-S2-R0035-A01 — mục 2.2.1.** Tuy nhiên, mô hình dầm hiệu dụng vẫn có thể biểu diễn đáp ứng tổng thể trong một miền được kiểm chứng; mô hình cáp có xét trượt trong [8] là một ví dụ về khả năng giữ ảnh hưởng trượt trong phép quy giản dầm.

- **Locator PDF trong trace:** Abstract, equivalent bending stiffness. **Trạng thái trace:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Excerpt/anchor đã lưu:** “equivalent bending stiffness (EBS)”
- **Ranh giới/ghi chú:** Nguồn hiệu chuẩn với thử nghiệm trong tài liệu; không chứng minh tính phổ quát hoặc độ đúng MP1.

**CH2-S2-R0037-A01 — mục 2.2.1.** Một đường cong tổng thể phù hợp chưa đủ để xác định duy nhất sự phân bố tiếp xúc và trượt bên trong, vì mô hình có thể gộp chúng vào tham số hiệu dụng [8].

- **Locator PDF trong trace:** Đoạn giới hạn/hiệu chuẩn ngay sau Eq. (4). **Trạng thái trace:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Excerpt/anchor đã lưu:** “calibrated”
- **Ranh giới/ghi chú:** Suy luận về khả năng nhận dạng, không phải phép chứng minh tính không duy nhất do tác giả M22 thực hiện.

**CH2-S2-R0071-A01 — mục 2.2.2.** Slip được xác định bằng chuyển vị tương đối theo phương tiếp tuyến giữa hai phía giao diện đã chọn; trong mô hình cáp dây song song, Zhang và cộng sự biểu diễn độ trượt qua các chuyển vị dọc và góc xoay của lớp tương đương [8].

- **Locator PDF trong trace:** Eqs. (4)–(5) and explanatory text. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “The slip has a relation with the axial displacements and deflec-”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S4-R0021-A02 — mục 2.4.2.** Trong mô hình của Zhang và cộng sự năm 2018 [8], mỗi hàng dây được thay bằng một lớp chữ nhật, bảo toàn tổng chiều cao và diện tích dây của hàng. Các lớp có chung độ võng và độ cong, không tách nhau theo phương đứng hoặc phương ngang, nhưng có thể trượt tương đối dọc trục. Lực tương tác tại mặt phân cách được giả thiết tỷ lệ tuyến tính với độ trượt thông qua tham số k. Cách quy đổi này giữ lại khả năng truyền lực giữa các hàng dây trong một mô hình dầm, đồng thời lược bỏ mô tả riêng từng vùng tiếp xúc cong của dây tròn. Nghiên cứu xét tải phân bố ngang đều hoặc lực tập trung giữa nhịp cùng lực kéo dọc trục, với các ví dụ dầm tựa đơn.

- **Locator PDF trong trace:** Physical PDF M22:2–3; Modeling and Formulation; Fig.1; Eqs.4–8 (not reproduced). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0022-A01 — mục 2.4.2.** Tham số độ cứng chống trượt k trong [8] là sức cản tương đương được hiệu chỉnh từ quan hệ lực và chuyển vị uốn của các mẫu Chen dưới những mức lực kéo dọc trục. Tham số này bao hàm ảnh hưởng của vỏ bảo vệ, sự siết giữ và hiệu ứng Poisson. Do đó, k không phải hệ số ma sát, không phải áp suất pháp tại tiếp xúc và không tạo thành một quy luật liên hệ giữa áp suất với ma sát. Việc nghiệm của mô hình phù hợp với nghiệm không gian trạng thái hoặc các trường hợp giới hạn cổ điển kiểm tra tính nhất quán của lời giải toán học. Phần đối chiếu thực nghiệm lại dựa trên dữ liệu đã công bố; đó không phải một thí nghiệm mới do nhóm tác giả thực hiện.

- **Locator PDF trong trace:** Physical PDF M22:3,7; Governing Differential Equations; Calibration of Slip Rigidity; Eq.4; Eq.37 and accompanying prose. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0023-A01 — mục 2.4.2.** Trong mô hình của Zhang và cộng sự năm 2018 [8], mỗi hàng dây được thay bằng một lớp chữ nhật, bảo toàn tổng chiều cao và diện tích dây của hàng. Các lớp có chung độ võng và độ cong, không tách nhau theo phương đứng hoặc phương ngang, nhưng có thể trượt tương đối dọc trục. Lực tương tác tại mặt phân cách được giả thiết tỷ lệ tuyến tính với độ trượt thông qua tham số k. Cách quy đổi này giữ lại khả năng truyền lực giữa các hàng dây trong một mô hình dầm, đồng thời lược bỏ mô tả riêng từng vùng tiếp xúc cong của dây tròn. Nghiên cứu xét tải phân bố ngang đều hoặc lực tập trung giữa nhịp cùng lực kéo dọc trục, với các ví dụ dầm tựa đơn.

- **Locator PDF trong trace:** Physical PDF M22:1,4–5; Abstract; Numerical Examples; Fig.3; Table1; Figs.4–5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0023-A02 — mục 2.4.2.** Tham số độ cứng chống trượt k trong [8] là sức cản tương đương được hiệu chỉnh từ quan hệ lực và chuyển vị uốn của các mẫu Chen dưới những mức lực kéo dọc trục. Tham số này bao hàm ảnh hưởng của vỏ bảo vệ, sự siết giữ và hiệu ứng Poisson. Do đó, k không phải hệ số ma sát, không phải áp suất pháp tại tiếp xúc và không tạo thành một quy luật liên hệ giữa áp suất với ma sát. Việc nghiệm của mô hình phù hợp với nghiệm không gian trạng thái hoặc các trường hợp giới hạn cổ điển kiểm tra tính nhất quán của lời giải toán học. Phần đối chiếu thực nghiệm lại dựa trên dữ liệu đã công bố; đó không phải một thí nghiệm mới do nhóm tác giả thực hiện.

- **Locator PDF trong trace:** Physical PDF M22:1,4–5; Abstract; Numerical Examples; Fig.3; Table1; Figs.4–5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S6-R0027-A01 — mục 2.6.1.** Đối với cáp thép gồm các dây song song, mô hình dầm phân lớp đã đưa tương tác chống trượt vào mô tả độ cứng uốn tương đương [8].

- **Locator PDF trong trace:** {"M22-E01": "Abstract; Modeling and formulation", "M22-E02": "Model of laminated beam with interfacial slips; Eqs. (1)–(9)"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “idealized as laminated beams including interlayer slips; Slip is allowed at each interface”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0115-A01 — mục 2.6.2.** Trong nghiên cứu cáp thép gồm dây song song, tương tác và trượt giữa các thành phần đã được đưa vào mô hình dầm phân lớp, nên không thể xem mọi mô hình cáp là bỏ qua tương tác dây [8].

- **Locator PDF trong trace:** {"M22-E01": ["Abstract; Abstract; direct page/anchor controls"], "M22-E02": ["Modeling and formulation; Eqs. (1)–(9); direct page/anchor controls", "Modeling and formulation; Eqs. (1)–(9); direct page/anchor controls"], "M22-E04": ["Calibration; Eq. (37); direct page/anchor controls", "Calibration; Eq. (37); direct page/anchor controls"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “Each rectangular layer has the same curvature and deflection; Each rectangular layer has the same curvature and deflection; The initial slip”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.


## [9] Y. S. Narang, J. J. Vlassak & R. D. Howe (2018), “Mechanically Versatile Soft Machines through Laminar Jamming”

**CH2-S2-R0061-A01 — mục 2.2.2.** Jamming được hiểu ở cấp kết cấu là sự tăng ràng buộc chuyển động tương đối giữa các phần tử, nhờ đó tương tác ma sát có thể làm chúng truyền tải cùng nhau mạnh hơn [9].

- **Locator PDF trong trace:** Abstract. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “a structural phenomenon in which a laminate of compliant strips becomes strongly coupled through friction”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0064-A01 — mục 2.2.2.** Trong cấu trúc laminar của Narang và cộng sự, trạng thái đã hút chân không vẫn có thể chuyển từ miền tiền trượt sang miền có trượt khi tải tăng [9].

- **Locator PDF trong trace:** §2.1 and Fig. 1. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “all layers have slipped along the full length of their interfaces”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0077-A01 — mục 2.2.2.** Trượt vẫn có thể truyền lực ma sát; Narang và cộng sự còn thu được lực cản tiêu tán trong miền full slip [9].

- **Locator PDF trong trace:** §2.1; Fig. 2. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “full-slip damping force was given succinctly by”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S3-R0016-A01 — mục Introduction / Fig. 1.** Đối chiếu với kẹt lớp/tấm của Narang và cộng sự cho thấy điểm chung chủ yếu nằm ở sự chuyển tiếp giữa trạng thái dính và trượt [9]. Trong chồng lớp, khi lực cắt dọc vượt giới hạn ma sát, trượt khởi phát tại một số vùng và làm giảm độ cứng; nguồn mô tả các miền tiền-trượt, chuyển tiếp và trượt hoàn toàn. Kết quả này cung cấp một tương tự cơ học để đặt câu hỏi về ngưỡng trượt và điều kiện biên, nhưng không phải bằng chứng trực tiếp cho kẹt dây hoặc kẹt sợi. Các đại lượng độ cứng của chồng lớp giấy, dây/cáp và mô-đun sợi không tự động cùng nghĩa, vì chúng được đo trên hình học, cách xếp phần tử và điều kiện tải khác nhau.

- **Locator PDF trong trace:** Fig. 1. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** M07 là laminar-sheet comparator, không phải direct wire/fiber evidence và không chuyển ngưỡng sang MP1.

**CH2-S3-R0032-A01 — mục Experiments.** Nghiên cứu của Narang và cộng sự cung cấp đối chứng thực nghiệm–mô phỏng cho cấu hình kẹt lớp chân không. Các mẫu gồm 5, 10, 15 và 20 lớp, được khảo sát ở các độ lớn chân không 0, 24, 47 và 71 kPa bằng phép uốn ba điểm; đường lực–độ võng được dùng để đánh giá độ cứng [9]. Tác giả phân biệt miền trước trượt, miền chuyển tiếp và miền trượt hoàn toàn. Trong miền chuyển tiếp, trượt khởi phát tại những vùng mà ứng suất cắt giao diện đạt sức kháng ma sát cực đại rồi lan truyền theo tải. Mô hình phần tử hữu hạn và thí nghiệm đạt hệ số xác định nhỏ nhất R² = 0,9879 trong tập được báo cáo. Kết quả cho thấy mô hình có thể phù hợp tốt trong cấu hình đã kiểm tra, nhưng không chứng minh rằng cùng một biểu diễn trượt vẫn đúng khi số lớp tăng cao hơn hoặc khi trường áp suất không đồng đều; hơn nữa, đây là bằng chứng về áp suất âm, không phải áp suất dương.

- **Locator PDF trong trace:** Fig.3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Chỉ là bằng chứng kẹt lớp chân không, không phải positive pressure.

**CH2-S3-R0033-A01 — mục Experiments.** Nghiên cứu của Narang và cộng sự cung cấp đối chứng thực nghiệm–mô phỏng cho cấu hình kẹt lớp chân không. Các mẫu gồm 5, 10, 15 và 20 lớp, được khảo sát ở các độ lớn chân không 0, 24, 47 và 71 kPa bằng phép uốn ba điểm; đường lực–độ võng được dùng để đánh giá độ cứng [9]. Tác giả phân biệt miền trước trượt, miền chuyển tiếp và miền trượt hoàn toàn. Trong miền chuyển tiếp, trượt khởi phát tại những vùng mà ứng suất cắt giao diện đạt sức kháng ma sát cực đại rồi lan truyền theo tải. Mô hình phần tử hữu hạn và thí nghiệm đạt hệ số xác định nhỏ nhất R² = 0,9879 trong tập được báo cáo. Kết quả cho thấy mô hình có thể phù hợp tốt trong cấu hình đã kiểm tra, nhưng không chứng minh rằng cùng một biểu diễn trượt vẫn đúng khi số lớp tăng cao hơn hoặc khi trường áp suất không đồng đều; hơn nữa, đây là bằng chứng về áp suất âm, không phải áp suất dương.

- **Locator PDF trong trace:** Fig.3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Độ khớp không chứng minh ngoại suy số lớp cao hoặc áp suất không đều.

**CH2-S5-R0005-A01 — mục §2.5.1.** Narang, Vlassak và Howe nghiên cứu chồng lớp giấy trong bao hút chân không. Ở trạng thái không hút, các lớp uốn gần như độc lập; khi hút, ma sát ghép các lớp thành một phần tử chịu uốn. Hình 1 của nguồn mô tả miền pre-slip, miền chuyển tiếp và miền full-slip. Trong pre-slip, các lớp được mô tả là dính kết, độ cứng lớn và gần như không tiêu tán năng lượng. Khi tải tăng, ứng suất cắt dọc tại một số vùng giao diện đạt giới hạn do hệ số ma sát và gradient áp suất quyết định; các vùng đó trượt và độ cứng giảm. Trong full-slip, nguồn gọi là mọi lớp đã trượt dọc theo toàn bộ chiều dài giao diện, nên độ cứng kết cấu đạt mức thấp nhất trong mô hình. Đây là mô tả cơ học của chồng lớp giấy dưới tải uốn, không phải phép đo trực tiếp tt(x) hay pn(x) trên từng giao diện [9].

- **Locator PDF trong trace:** Introduction/Fig. 1. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không đo trực tiếp traction cục bộ hay p_n(x).

**CH2-S5-R0006-A01 — mục §2.5.1.** Mô hình hai lớp của cùng nghiên cứu dùng dầm Euler–Bernoulli, cấu hình công xôn ngàm–tự do và tải phân bố để theo dõi vùng trượt. Vùng này được dự đoán khởi phát gần đầu ngàm rồi phát triển về phía đầu tự do khi tải tăng; mô hình phần tử hữu hạn hai lớp tái hiện vùng trượt dự đoán. Các mô phỏng nhiều lớp cho phép tiếp xúc ma sát đồng thời ở các giao diện và có phân tích biến dạng lớn, trong khi thí nghiệm uốn ba điểm ghi lực–độ võng ở 5, 10, 15 và 20 lớp, với các mức chân không 0, 24, 47 và 71 kPa. Mức phù hợp cao giữa mô phỏng và lực–độ võng chỉ kiểm chứng đáp ứng kết cấu trong kiến trúc đã xét; hệ số ma sát không được đo trực tiếp với độ chính xác độc lập [9].

- **Locator PDF trong trace:** Analytical model/Fig. 2; Experiments/Fig. 3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Validation của đáp ứng kiến trúc, không phải luật tiếp xúc MP1.

**CH2-S5-R0023-A01 — mục §2.5.2.** Narang, Vlassak và Howe dùng mô hình hai lớp công xôn ngàm–tự do với tải phân bố đều. Vùng trượt được dự đoán khởi phát gần đầu ngàm rồi lan về phía tự do khi tải tăng; mô hình phần tử hữu hạn hai lớp tái hiện vùng này. Kết quả cho thấy một cấu trúc có thể đồng thời chứa vùng dính và vùng trượt, nên không thể dùng một trạng thái full-slip cục bộ để suy ra cận dây độc lập cho toàn tiết diện [9].

- **Locator PDF trong trace:** Analytical model/Fig.2/SI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không cung cấp cận MP1; topology là laminar paper.

**CH2-S5-R0040-A01 — mục §2.5.3.** Trong thí nghiệm của Narang và cộng sự, các mẫu chồng lớp giấy được uốn ba điểm và biểu diễn bằng lực ngang–độ võng. Hình 3 so sánh 5, 10, 15 và 20 lớp ở 71 kPa, các mức chân không 0, 24, 47 và 71 kPa với 20 lớp, cùng các giá trị hệ số ma sát chỉ trong phần tử hữu hạn. Đường thực nghiệm là trung bình với dải ±1 độ lệch chuẩn; độ lệch cực đại được báo cáo là 0,24 N và R² nhỏ nhất giữa phần tử hữu hạn với thực nghiệm là 0,9879. Đây là kiểm tra đáp ứng kết cấu trong cấu hình lớp giấy; không phải nhận dạng trực tiếp hệ số ma sát, lực pháp tuyến cục bộ hay vị trí trượt [9].

- **Locator PDF trong trace:** Experiments/Fig.3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không đo local slip/traction/μ thực nghiệm.

**CH2-S5-R0081-A01 — mục §2.5.5.** Nhóm mô hình dầm giải tích hoặc elastica giữ lại cân bằng lực–mô men và các điều kiện biên để tạo ra một mô tả cơ học có thể diễn giải. Narang, Vlassak và Howe phát triển mô hình elastica hai lớp công xôn, dùng ma sát Coulomb tại giao diện; vùng trượt bắt đầu gần ngàm và mở rộng về phía đầu tự do khi tải tăng. Mô hình dự đoán hình dạng elastica, độ cứng, năng lượng tiêu tán, lực chuyển tiếp và chiều dài vùng trượt. Hai lớp được đối chiếu bằng mô hình phần tử hữu hạn, còn các cấu hình nhiều lớp được mô phỏng và so sánh với thí nghiệm uốn ba điểm trong phạm vi 5–20 lớp và áp suất chân không 0–71 kPa [9]. Bài báo nêu rằng mô hình FE không dùng tham số khớp, nhưng hệ số ma sát trong khảo sát số là đầu vào được quy định; các đường thực nghiệm theo hệ số ma sát không được thu thập do khó điều chỉnh chính xác. Do đó, đây là bằng chứng mạnh cho tính diễn giải của cơ chế trượt trong kiến trúc lớp giấy đã xét, đồng thời là đối chiếu FE–thực nghiệm có phạm vi, chứ không phải kiểm chứng độc lập cho bó dây TiNi hoặc cho cấu hình dây–ống bao.

- **Locator PDF trong trace:** PDF physical p.3, Fig. 2 and Sec. 2.1 Analytical Modeling. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Not a TiNi wire/sleeve validation

**CH2-S5-R0082-A01 — mục §2.5.5.** Nhóm mô hình dầm giải tích hoặc elastica giữ lại cân bằng lực–mô men và các điều kiện biên để tạo ra một mô tả cơ học có thể diễn giải. Narang, Vlassak và Howe phát triển mô hình elastica hai lớp công xôn, dùng ma sát Coulomb tại giao diện; vùng trượt bắt đầu gần ngàm và mở rộng về phía đầu tự do khi tải tăng. Mô hình dự đoán hình dạng elastica, độ cứng, năng lượng tiêu tán, lực chuyển tiếp và chiều dài vùng trượt. Hai lớp được đối chiếu bằng mô hình phần tử hữu hạn, còn các cấu hình nhiều lớp được mô phỏng và so sánh với thí nghiệm uốn ba điểm trong phạm vi 5–20 lớp và áp suất chân không 0–71 kPa [9]. Bài báo nêu rằng mô hình FE không dùng tham số khớp, nhưng hệ số ma sát trong khảo sát số là đầu vào được quy định; các đường thực nghiệm theo hệ số ma sát không được thu thập do khó điều chỉnh chính xác. Do đó, đây là bằng chứng mạnh cho tính diễn giải của cơ chế trượt trong kiến trúc lớp giấy đã xét, đồng thời là đối chiếu FE–thực nghiệm có phạm vi, chứ không phải kiểm chứng độc lập cho bó dây TiNi hoặc cho cấu hình dây–ống bao.

- **Locator PDF trong trace:** PDF physical p.3, Sec. 2.1–2.2 and SI Governing Equations. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** High-layer extrapolation and homogeneous pressure limits

**CH2-S5-R0083-A01 — mục §2.5.5.** Nhóm mô hình dầm giải tích hoặc elastica giữ lại cân bằng lực–mô men và các điều kiện biên để tạo ra một mô tả cơ học có thể diễn giải. Narang, Vlassak và Howe phát triển mô hình elastica hai lớp công xôn, dùng ma sát Coulomb tại giao diện; vùng trượt bắt đầu gần ngàm và mở rộng về phía đầu tự do khi tải tăng. Mô hình dự đoán hình dạng elastica, độ cứng, năng lượng tiêu tán, lực chuyển tiếp và chiều dài vùng trượt. Hai lớp được đối chiếu bằng mô hình phần tử hữu hạn, còn các cấu hình nhiều lớp được mô phỏng và so sánh với thí nghiệm uốn ba điểm trong phạm vi 5–20 lớp và áp suất chân không 0–71 kPa [9]. Bài báo nêu rằng mô hình FE không dùng tham số khớp, nhưng hệ số ma sát trong khảo sát số là đầu vào được quy định; các đường thực nghiệm theo hệ số ma sát không được thu thập do khó điều chỉnh chính xác. Do đó, đây là bằng chứng mạnh cho tính diễn giải của cơ chế trượt trong kiến trúc lớp giấy đã xét, đồng thời là đối chiếu FE–thực nghiệm có phạm vi, chứ không phải kiểm chứng độc lập cho bó dây TiNi hoặc cho cấu hình dây–ống bao.

- **Locator PDF trong trace:** PDF physical p.4, Fig. 3 and Sec. 2.2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Values not transferable to TiNi bundle


## [10] F. Caruso, G. Mantriota, V. Moramarco & G. Reina (2023), “Layer jamming: Modeling and experimental validation”

**CH2-S2-R0074-A01 — mục 2.2.2.** Phải nêu rõ phạm vi ấy: mô hình Caruso và cộng sự vẫn giữ một miền ngoài gối tựa liên kết với nhau trong khi miền giữa các gối đã trượt [10].

- **Locator PDF trong trace:** §2.1, internal/external region approximation. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “the external region will remain cohesive”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0081-A01 — mục 2.2.2.** Các miền tiền trượt, trượt một phần và trượt toàn phần hữu ích để diễn giải một số mô hình layer jamming, nhưng không đặt ra ba ngưỡng tải tách bạch cho mọi kiến trúc [10].

- **Locator PDF trong trace:** Fig. 1 caption. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “the shear stress at each interface remains below the static friction limit”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S3-R0045-A01 — mục Secs.5.1–5.3.** Các kết quả của Caruso và cộng sự minh họa rõ quan hệ giữa điều kiện thử và mức độ kiểm chứng. Với mẫu chữ nhật, b = 6 cm, L = 18 cm và lớp giấy dày 0,1 mm, bốn cấu hình 8, 12, 16 và 20 lớp được thử ở 68 kPa; cấu hình 20 lớp được thử thêm ở 24 và 48 kPa, mỗi điều kiện lặp ba lần [10]. Phép uốn ba điểm ghi lực–độ võng và năng lượng tiêu tán; mô hình giải tích, phần tử hữu hạn và thí nghiệm được so sánh trong cùng miền hình học. Mô hình mô tả được sự lan truyền trượt và xu hướng thay đổi độ cứng, nhưng sai lệch tăng ở độ võng lớn do mô hình giải tích bỏ qua áp suất và ứng suất tiếp xúc phát sinh tại gối đỡ. Vì vậy, kết quả này xác lập một miền kiểm chứng cụ thể, không phải luật phổ quát theo số lớp.

- **Locator PDF trong trace:** Fig.4. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Mẫu chữ nhật, uốn ba điểm, giấy/TPU và biên đỡ cụ thể.

**CH2-S3-R0046-A01 — mục Secs.5.1–6.** Các kết quả của Caruso và cộng sự minh họa rõ quan hệ giữa điều kiện thử và mức độ kiểm chứng. Với mẫu chữ nhật, b = 6 cm, L = 18 cm và lớp giấy dày 0,1 mm, bốn cấu hình 8, 12, 16 và 20 lớp được thử ở 68 kPa; cấu hình 20 lớp được thử thêm ở 24 và 48 kPa, mỗi điều kiện lặp ba lần [10]. Phép uốn ba điểm ghi lực–độ võng và năng lượng tiêu tán; mô hình giải tích, phần tử hữu hạn và thí nghiệm được so sánh trong cùng miền hình học. Mô hình mô tả được sự lan truyền trượt và xu hướng thay đổi độ cứng, nhưng sai lệch tăng ở độ võng lớn do mô hình giải tích bỏ qua áp suất và ứng suất tiếp xúc phát sinh tại gối đỡ. Vì vậy, kết quả này xác lập một miền kiểm chứng cụ thể, không phải luật phổ quát theo số lớp.

- **Locator PDF trong trace:** Fig.4–5;Conclusion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không chứng minh luật số lớp phổ quát hoặc chuyển sang bó dây.

**CH2-S5-R0024-A01 — mục §2.5.2.** Caruso và cộng sự mở rộng mô tả cho bốn lớp trong uốn ba điểm. Với hình chữ nhật gồm bốn lớp, giao diện trung tâm đạt giới hạn ma sát trước, sau đó các giao diện ngoài lần lượt trượt. Các phương trình ngưỡng và mô men quán tính trong nguồn gắn với chiều dày lớp, áp suất chân không, hệ số ma sát, nhịp và điều kiện gối; thí nghiệm và phần tử hữu hạn kiểm tra đường lực–độ võng trong cấu hình đó. Trật tự trung tâm–ra ngoài vì thế là thông tin về một topology lớp cụ thể, không phải điều kiện tổng quát cho packing dây TiNi [10].

- **Locator PDF trong trace:** Figs.1–2; Sec.2.1 Eqs.(1–15). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Trật tự trung tâm–ngoài không phổ quát cho packing dây.

## Nhận xét audit [6]–[10]

- **[6] Russo et al.** Trace định vị hai ý ở §3.1.3: biểu diễn Cosserat và giả thiết tiết diện/biến dạng cắt. Đây là tổng quan/mô tả mô hình; không cung cấp thông số hoặc xác nhận trực tiếp cho MP1. Locator hiện thiếu số trang vật lý.
- **[7] Jeon et al.** Nguồn được dùng rộng ở §2.4.3 và đối chiếu §2.6: cấu trúc robot, biến đổi lực ma sát bởi SMA, phép kéo dây riêng và phép thử uốn. Đây là cơ cấu khác với bó dây TiNi MP1; cần giữ rõ khác biệt giữa lực kéo giao diện, độ dốc lực–độ võng và EI suy ra. Một số locator trong trace có số trang/figure/table, một số chỉ có mã “M31”.
- **[8] Zhang et al.** Hỗ trợ mô hình dầm cáp dây song song có trượt giao diện; tham số `k` là độ cứng trượt hiệu dụng được hiệu chuẩn theo nguồn, không đồng nhất với hệ số ma sát hoặc áp suất pháp. Các locator ghi mục/phương trình và một phần số PDF, chưa chuẩn hóa physical page cho từng claim.
- **[9] Narang et al.** Cung cấp tiền lệ laminar jamming, miền pre-slip/transition/full-slip và mô hình/đối chiếu thực nghiệm cho chồng lớp. Không chuyển ngưỡng hoặc tham số sang bó dây. Một số dòng có physical page (ví dụ p.3–4); các dòng khác chỉ ghi section/figure.
- **[10] Caruso et al.** Hỗ trợ mô hình và thực nghiệm layer-jamming trong topology lớp cụ thể; không biến thứ tự trượt của bốn lớp thành luật tổng quát. Trace có 5 claim narrative sau khi bỏ dòng `NOT_APPLICABLE`; một số locator chỉ ghi section/figure và chưa nêu physical page.
- Dù các PDF [6]–[10] có trong thư mục đóng gói, vòng này vẫn dựa trên traceability có sẵn để nối ý và locator; chưa trích xuất/đối chiếu trực tiếp mọi câu từ PDF. Chưa gắn nhãn `VERIFIED FULL TEXT` mới.


---

# Tiếp nối audit: tài liệu tham khảo [11]–[15]

**Phạm vi:** tiếp tục cùng bản nháp và master traceability. Locator và excerpt/anchor được chuyển từ CSV; đây là dấu vết sẵn có để đối chiếu, không phải xác nhận độc lập từng câu từ PDF.

| Ref | Nguồn | DOI/ID | Claim/anchor duy nhất | PDF đóng gói |
|---:|---|---|---:|---|
| [11] | S. Zhang, J. Yao, W. Zhao & C. Wei (2025), “A continuum-based model for a layer jamming beam” | 10.5194/ms-16-821-2025 | 7 | `11_2025-A continuum-based model for a layer jamming beam.pdf` |
| [12] | F. Caro & M. G. Carmichael (2024), “A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics” | 10.3390/act13020064 | 6 | `12_A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf` |
| [13] | Y. Zhang, Q. Feng, G. Wang & R. Xu (2021), “Analytical model for the bending of parallel wire cables considering interactions among wires” | 10.1016/j.ijmecsci.2020.106192 | 3 | `13_2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf` |
| [14] | Joint Committee for Guides in Metrology (2008), “Evaluation of measurement data — Guide to the expression of uncertainty in measurement” | JCGM 100:2008 | 11 | `14_M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf` |
| [15] | Y. Fan, B. Yi & D. Liu (2024), “An overview of stiffening approaches for continuum robots” | 10.1016/j.rcim.2024.102811 | 7 | `15_M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf` |

## [11] S. Zhang, J. Yao, W. Zhao & C. Wei (2025), “A continuum-based model for a layer jamming beam”

**CH2-S2-R0076-A01 — mục 2.2.2.** Zhang và cộng sự dùng tương tự đàn dẻo để mô tả môi trường layer jamming có trượt, nên chữ “dẻo” trong cách quy giản đó không chứng minh dây TiNi bị biến dạng dẻo [11].

- **Locator PDF trong trace:** §2, continuum stress-state discussion. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “there is no slipping between sheets”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0079-A01 — mục 2.2.2.** Trạng thái tiếp xúc còn phụ thuộc đường tải: mô hình liên tục của Zhang và cộng sự phân biệt tăng tải, trượt tại giới hạn và dỡ tải, rồi giải đáp ứng theo gia số [11].

- **Locator PDF trong trace:** §2, loading/yielding/unloading discussion. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “must be solved incrementally”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S3-R0047-A01 — mục Abstract;Sec.2;Secs.4–5.** Zhang và cộng sự đi xa hơn về mức mô hình hóa khi coi chồng lớp như một môi trường liên tục trong giới hạn lớp mỏng vô hạn, với δ/h nhỏ và số lớp đủ lớn; bài báo nêu miền thực hành xấp xỉ từ khoảng 10 lớp trở lên dựa trên đối chiếu phần tử hữu hạn [11]. Mô hình liên tục mô tả ứng suất pháp, ứng suất cắt và các trạng thái kẹt, trượt một phần, trượt hoàn toàn; kết quả được so sánh với phần tử hữu hạn cho các mẫu 10 và 25 lớp, rồi với thí nghiệm dầm PVC 20 lớp ở 60 kPa. Tuy nhiên, chính phần kiểm chứng cho thấy sai lệch gần biên, trong vùng trượt lớn và khi ảnh hưởng hình học cong hoặc ứng suất pháp không còn phù hợp với giả thiết liên tục. Độ phù hợp của biến dạng toàn cục trong một cấu hình không đồng nghĩa với việc mô hình đã nhận dạng đúng lực tiếp xúc cục bộ hoặc có thể chuyển sang bó dây TiNi.

- **Locator PDF trong trace:** Fig.1;Fig.6–7. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Giả thiết δ/h nhỏ, n lớn; vật liệu, hình học và tải riêng của LJS.

**CH2-S3-R0048-A01 — mục Secs.4–6.** Zhang và cộng sự đi xa hơn về mức mô hình hóa khi coi chồng lớp như một môi trường liên tục trong giới hạn lớp mỏng vô hạn, với δ/h nhỏ và số lớp đủ lớn; bài báo nêu miền thực hành xấp xỉ từ khoảng 10 lớp trở lên dựa trên đối chiếu phần tử hữu hạn [11]. Mô hình liên tục mô tả ứng suất pháp, ứng suất cắt và các trạng thái kẹt, trượt một phần, trượt hoàn toàn; kết quả được so sánh với phần tử hữu hạn cho các mẫu 10 và 25 lớp, rồi với thí nghiệm dầm PVC 20 lớp ở 60 kPa. Tuy nhiên, chính phần kiểm chứng cho thấy sai lệch gần biên, trong vùng trượt lớn và khi ảnh hưởng hình học cong hoặc ứng suất pháp không còn phù hợp với giả thiết liên tục. Độ phù hợp của biến dạng toàn cục trong một cấu hình không đồng nghĩa với việc mô hình đã nhận dạng đúng lực tiếp xúc cục bộ hoặc có thể chuyển sang bó dây TiNi.

- **Locator PDF trong trace:** Figs.6–7. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Độ phù hợp biến dạng toàn cục không nhận dạng local traction.

**CH2-S6-R0017-A01 — mục 2.6.1.** Một mức đối chiếu khác được báo cáo trong mô hình liên tục cho dầm kẹt lớp của Zhang và cộng sự [11].

- **Locator PDF trong trace:** {"M18-E01": "Abstract; Sections 1–2", "M18-E06": "Section 5; Fig. 7a–b"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “infinitely many thin layers; analytical curve lies entirely within the 1σ interval”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0107-A01 — mục 2.6.2.** Ở một cấp mô tả khác, mô hình liên tục của Zhang và cộng sự đã biểu diễn biến dạng và ứng suất trong dầm kẹt lớp có nhiều lớp mỏng [11].

- **Locator PDF trong trace:** {"M18-E01": ["Abstract; Abstract; direct page/anchor controls"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “while the total height h remains constant”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0111-A01 — mục 2.6.2.** Chính nguồn cũng chỉ ra sai khác gần đầu dầm và khi vùng trượt lớn; bỏ qua thành phần ứng suất pháp theo chiều dày làm mô hình dự đoán vùng trượt rộng hơn trong một số đối chiếu số [11].

- **Locator PDF trong trace:** {"M18-E07": ["Sec. 5–6 limitations; Fig. 6; Conclusions; direct page/anchor controls"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “CLJM’s neglect of normal stress along the y axis”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.


## [12] F. Caro & M. G. Carmichael (2024), “A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics”

**CH2-S2-R0122-A01 — mục 2.2.3.** Trong kẹt lớp bằng chân không mà Caro và Carmichael tổng hợp, bơm hạ áp suất trong buồng kín bao quanh các lớp, còn áp suất khí quyển nén buồng và chồng lớp [12].

- **Locator PDF trong trace:** §3.1.3 Vacuum Pressure. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “atmospheric pressure compresses the chamber”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S3-R0010-A06 — mục Classification context; Section 2; Section 2.2; Design.** Họ kiến trúc kẹt cơ họcKẹt lớp/tấmCác lá hoặc tấm mỏng chuyển giữa trạng thái cùng chịu uốn và trạng thái trượt tương đối.Cơ cấu khóa phụ thuộc kiến trúc, gồm chân không hoặc cơ cấu khác.Không chuyển trực tiếp đáp ứng của tấm sang bó dây.[12]

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S3-R0022-A01 — mục 3.1.3 Vacuum Pressure Jamming.** Trong phần tổng quan của Caro và Carmichael, cấu hình kẹt lớp/tấm dưới chân không (vacuum layer jamming) là một chồng lớp vật liệu mềm được đặt trong một khoang kín khí; khi không khí được hút ra, áp suất khí quyển ép chồng lớp lại và làm tăng sức kháng ma sát đối với trượt giữa các lớp [12]. Cơ chế này minh họa rõ vai trò của tiếp xúc phân bố trên toàn chồng lớp: độ cứng tăng lên nhờ hạn chế trượt tương đối giữa các lớp, chứ không phải vì áp suất chân không tự nó là một đại lượng cơ học cục bộ đã biết. Mô tả của nguồn cung cấp cơ sở cho một mô hình lớp tiếp xúc có biến dạng và ma sát, nhưng không đưa ra luật địa phương đầy đủ nối áp suất nguồn với lực pháp tuyến, sự khởi phát hư hỏng hay phân bố trượt trong từng vùng.

- **Locator PDF trong trace:** Fig. 3c. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** M06 là review-level synthesis tại locator này; không báo cáo local normal-pressure field, slip localization hoặc failure criterion.

**CH2-S3-R0022-A02 — mục 3.1.3 Vacuum Pressure Jamming.** Caro và Carmichael [12] — kẹt lớp/tấm chân khôngChồng lớp mềm trong khoang kín khí; tiếp xúc lớp–lớp.Hút khí tạo chênh áp; áp suất khí quyển ép khoang và chồng lớp.Sức kháng ma sát đối với trượt giữa lớp tăng, hạn chế chuyển vị tương đối và tăng độ cứng uốn.Nguồn xác nhận cơ chế khóa; không báo cáo phân bố lực pháp tuyến cục bộ hay tiêu chuẩn hư hỏng trong mô tả nguồn này.Không chuyển trực tiếp sang topology dây hoặc bó TiNi.

- **Locator PDF trong trace:** Fig. 3c. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** M06 là review-level synthesis tại locator này; không báo cáo local normal-pressure field, slip localization hoặc failure criterion.

**CH2-S3-R0031-A01 — mục 3.1.3 Vacuum Pressure Jamming.** Trong cơ cấu kẹt lớp chân không, tổng quan của Caro và Carmichael mô tả một chồng lớp mềm nằm trong khoang kín khí. Khi hút khí, áp suất khí quyển ép khoang và chồng lớp, làm tăng tương tác ma sát giữa các lớp [12]. Cách mô tả này xác định đúng chuỗi cơ học ở mức kiến trúc, nhưng không cung cấp trường áp suất cục bộ theo chiều dày hay phân bố lực pháp tuyến tại từng giao diện. Do đó, áp suất chân không được dùng như biến kích hoạt của cấu hình, không được đồng nhất với một áp suất tiếp xúc đồng đều.

- **Locator PDF trong trace:** Fig.3c. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Review-level synthesis; không báo cáo trường áp suất cục bộ.

**CH2-S6-R0157-A01 — mục 2.6.3.** Sự thay đổi truyền lực do giam giữ và trượt tiếp xúc đã có cơ sở trong các hệ được nghiên cứu trước; tổng quan về kẹt lớp của Caro và Carmichael mô tả sự chuyển tiếp giữa các miền trước trượt và trượt khi chịu tải [12].

- **Locator PDF trong trace:** {"M06-E04": ["6. Limitations of Lock/Unlock Mechanisms; 6. Limitations of Lock/Unlock Mechanisms, continued; 1. Introduction"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “limitations are inherent; transition from the pre-slip regime; excludes other forms of jamming”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.


## [13] Y. Zhang, Q. Feng, G. Wang & R. Xu (2021), “Analytical model for the bending of parallel wire cables considering interactions among wires”

**CH2-S2-R0154-A01 — mục 2.2.3.** Mô hình cáp của Zhang và cộng sự giả thiết lực tương tác tỷ lệ với trượt, đồng thời thừa nhận tương tác thực phức tạp hơn và cần hiệu chuẩn thực nghiệm [13].

- **Locator PDF trong trace:** §2.1 continuation, before §2.2. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “much more complicated than the linear assumption”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S4-R0025-A01 — mục 2.4.2.** Zhang và cộng sự năm 2021 [13] mở rộng mô tả sang bài toán hai chiều trong trạng thái ứng suất phẳng, giải đồng thời chuyển vị, ứng suất và trượt giữa các lớp bằng phương pháp không gian trạng thái. Các hàng dây vẫn được quy đổi theo chiều cao và diện tích. Khi chuyển sang lớp tương đương có bề rộng đơn vị, tác giả điều chỉnh mô đun theo bề rộng quy đổi. Mô đun của lớp tương đương trong bước này là tham số của phép quy đổi, không phải một giá trị mô đun Young mới đo trên vật liệu dây. Mô hình cho phép khảo sát trường cơ học bên trong sâu hơn quan hệ lực và chuyển vị tổng thể, nhưng phép giảm chiều vẫn không phân giải hình dạng thật của tiếp xúc dây tròn, sự thay đổi xếp chặt theo tiết diện hay trường ngoài mặt phẳng.

- **Locator PDF trong trace:** Physical PDF M23:2–3; Secs.2.1–2.2; Figs.1–2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0026-A01 — mục 2.4.2.** Zhang và cộng sự năm 2021 [13] mở rộng mô tả sang bài toán hai chiều trong trạng thái ứng suất phẳng, giải đồng thời chuyển vị, ứng suất và trượt giữa các lớp bằng phương pháp không gian trạng thái. Các hàng dây vẫn được quy đổi theo chiều cao và diện tích. Khi chuyển sang lớp tương đương có bề rộng đơn vị, tác giả điều chỉnh mô đun theo bề rộng quy đổi. Mô đun của lớp tương đương trong bước này là tham số của phép quy đổi, không phải một giá trị mô đun Young mới đo trên vật liệu dây. Mô hình cho phép khảo sát trường cơ học bên trong sâu hơn quan hệ lực và chuyển vị tổng thể, nhưng phép giảm chiều vẫn không phân giải hình dạng thật của tiếp xúc dây tròn, sự thay đổi xếp chặt theo tiết diện hay trường ngoài mặt phẳng.

- **Locator PDF trong trace:** Physical PDF M23:3–5; Secs.2.1–2.2; Figs.4–5; state and interface matrices (not reproduced). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.


## [14] Joint Committee for Guides in Metrology (2008), “Evaluation of measurement data — Guide to the expression of uncertainty in measurement”

**CH2-S2-R0158-A01 — mục 2.2.3.** GUM mô tả kết quả đo thông qua quan hệ giữa đại lượng cần đo và các đại lượng đầu vào [14].

- **Locator PDF trong trace:** §4.1.1, Eq. (1). **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “Modelling the measurement”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0180-A01 — mục 2.2.3.** Độ phân tán giữa các lần lặp chỉ phản ánh một phần thông tin về độ không đảm bảo; GUM còn xét hiệu chỉnh, độ phân giải, các đại lượng ảnh hưởng và giả thiết của phương pháp [14].

- **Locator PDF trong trace:** §3.3.2, sources of uncertainty. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “variations in repeated observations”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0181-A01 — mục 2.2.3.** Sai số không đồng nghĩa với độ không đảm bảo [14].

- **Locator PDF trong trace:** §3.2.2, Note 2. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “They are not”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0182-A01 — mục 2.2.3.** Độ không đảm bảo mở rộng U được lập từ độ không đảm bảo chuẩn kết hợp và hệ số phủ đã nêu [14].

- **Locator PDF trong trace:** §3.3.6–3.3.7. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “coverage factor”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0183-A01 — mục 2.2.3.** Các đại lượng dẫn xuất dùng chung kênh đầu vào không tự độc lập; hiệp phương sai có ý nghĩa phải được xét trong mô hình đo [14].

- **Locator PDF trong trace:** §5.2.1–5.2.2, Eq. (13). **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “Correlated input quantities”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S6-R0062-A01 — mục 2.6.1.** Hướng dẫn GUM cung cấp nền tảng phương pháp để tổ chức các phép suy ra đại lượng như vậy [14].

- **Locator PDF trong trace:** {"M38-E02": "§4.1.1–4.1.5; Eqs. (1)–(2)"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “a measurand Y is not measured directly”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0132-A01 — mục 2.6.2.** Theo hướng dẫn GUM, cần nhận diện mô hình phép đo, các đầu vào và ảnh hưởng đáng kể; khi đầu vào tương quan, phép lan truyền độ không đảm bảo phải tính đến hiệp phương sai [14].

- **Locator PDF trong trace:** {"M38-E02": ["§4.1.1–4.1.5; Eqs.(1)–(2)"], "M38-E03": ["§5.1.2 Eq.(10); §5.2.2 Eq.(13)"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “measurand Y is represented as a function of input quantities; combined standard uncertainty”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0192-A01 — mục 2.6.3.** GUM yêu cầu xác định mô hình phép đo, các đầu vào và ảnh hưởng đáng kể, đồng thời giữ đóng góp của hiệp phương sai khi đầu vào tương quan; khoảng bất định mở rộng còn cần hệ số phủ và cách diễn giải thích hợp [14].

- **Locator PDF trong trace:** {"M38-E02": ["§4.1.1–4.1.3; Eq.(1) is not reproduced"], "M38-E03": ["§5.1.2; §5.2.2; Eqs.(10)/(13) not reproduced"], "M38-E04": ["§6.2.1–6.3.3; Eq.(18) not reproduced"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “functional relationship; correlated; coverage factor”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0228-A01 — mục 2.6.4.** Theo GUM, độ lặp lại gắn với các phép đo liên tiếp của cùng đại lượng trong những điều kiện đo giống nhau; đánh giá dưới điều kiện thay đổi cần khai báo những điều kiện đã thay đổi [14].

- **Locator PDF trong trace:** {"M38-E01":[{"physical_pages":[13],"printed_pages":["1"],"exact_locator":"§1 Scope","anchor":"general rules"},{"physical_pages":[47],"printed_pages":["35"],"exact_locator":"Annex B.2.15–B.2.16","anchor":"same conditions of measurement","ADDITIONAL_FRAGMENT_NOT_IN_ORIGINAL_RECORD":true}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.

**CH2-S6-R0231-A01 — mục 2.6.4.** GUM yêu cầu mô hình phép đo thể hiện các đại lượng đầu vào có liên quan và xem xét tương quan khi truyền độ không đảm bảo đo [14].

- **Locator PDF trong trace:** {"M38-E02":[{"physical_pages":[20,21],"printed_pages":["8","9"],"exact_locator":"§4.1.1–4.1.3 model of measurement; Eq.(1)","anchor":"mathematical model"},{"physical_pages":[14],"printed_pages":["2"],"exact_locator":"§2.2.3 uncertainty definition","ADDITIONAL_FRAGMENT_NOT_IN_ORIGINAL_RECORD":true}],"M38-E03":[{"physical_pages":[31,33],"printed_pages":["19","21"],"exact_locator":"§5.1.2 and §5.2.2 covariance/correlated inputs","anchor":"correlated"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.

**CH2-S6-R0251-A01 — mục 2.6.4.** Mô hình phép đo cần cho biết áp suất, lực, chuyển vị và độ cong tham gia vào kết quả nào, đầu vào nào được đo hay suy ra, cùng các tương quan đáng kể nếu có [14].

- **Locator PDF trong trace:** {"M38-E02":[{"physical_pages":[20,21],"printed_pages":["8","9"],"exact_locator":"§4.1.1–4.1.3 model of measurement; Eq.(1)","anchor":"mathematical model"},{"physical_pages":[14],"printed_pages":["2"],"exact_locator":"§2.2.3 uncertainty definition","ADDITIONAL_FRAGMENT_NOT_IN_ORIGINAL_RECORD":true}],"M38-E03":[{"physical_pages":[31,33],"printed_pages":["19","21"],"exact_locator":"§5.1.2 and §5.2.2 covariance/correlated inputs","anchor":"correlated"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.


## [15] Y. Fan, B. Yi & D. Liu (2024), “An overview of stiffening approaches for continuum robots”

**CH2-S3-R0001-A01 — mục Abstract / Introduction; classification context.** Trong robot mềm và robot liên tục, điều chỉnh độ cứng là thay đổi khả năng chống lại biến dạng trong khi vẫn duy trì một mức độ mềm dẻo cần thiết cho chuyển động. Ở tầng nguyên lý cấp cao, các tổng quan phân biệt những cách tạo lực đối kháng, thay đổi tính chất vật liệu, và thay đổi ràng buộc hoặc cấu hình cơ khí [15]. Ở tầng kiến trúc, các cơ chế kẹt cơ học (jamming) được phân chia theo môi trường tiếp xúc như sợi, dây, lớp/tấm hoặc hạt. Vì vậy, khóa bằng ma sát là một cơ chế ràng buộc có thể xuất hiện trong nhiều kiến trúc, chứ không phải một nhóm đồng cấp loại trừ các kiến trúc kẹt cơ học. Đối với bó dây TiNi, vật liệu dây, hình thái tiếp xúc, đường truyền tải nén và trạng thái biến dạng của từng dây cần được xem xét riêng.

- **Locator PDF trong trace:** Fig. 1; Table 1 context. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** M05 cung cấp taxonomy cấp hệ thống; việc tách tầng nguyên lý khỏi kiến trúc jamming là tổng hợp biên tập.

**CH2-S3-R0010-A01 — mục Classification context; Section 2; Section 2.2; Design.** Trong robot mềm và robot liên tục, điều chỉnh độ cứng là thay đổi khả năng chống lại biến dạng trong khi vẫn duy trì một mức độ mềm dẻo cần thiết cho chuyển động. Ở tầng nguyên lý cấp cao, các tổng quan phân biệt những cách tạo lực đối kháng, thay đổi tính chất vật liệu, và thay đổi ràng buộc hoặc cấu hình cơ khí [15]. Ở tầng kiến trúc, các cơ chế kẹt cơ học (jamming) được phân chia theo môi trường tiếp xúc như sợi, dây, lớp/tấm hoặc hạt. Vì vậy, khóa bằng ma sát là một cơ chế ràng buộc có thể xuất hiện trong nhiều kiến trúc, chứ không phải một nhóm đồng cấp loại trừ các kiến trúc kẹt cơ học. Đối với bó dây TiNi, vật liệu dây, hình thái tiếp xúc, đường truyền tải nén và trạng thái biến dạng của từng dây cần được xem xét riêng.

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S3-R0010-A02 — mục Classification context; Section 2; Section 2.2; Design.** Nguyên lý cấp caoTạo lực đối khángCơ cấu hoặc cơ cấu chấp hành tạo lực chống lại tải ngoài.Gân kéo (tendon), truyền động chất lưu (fluidic) hoặc cơ cấu tương tự.Không xác định giao diện tiếp xúc của bó TiNi.[15]

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S3-R0010-A03 — mục Classification context; Section 2; Section 2.2; Design.** Nguyên lý cấp caoVật liệu đáp ứng nhiệtThay đổi trạng thái hoặc đặc tính vật liệu để thay đổi độ cứng của kết cấu.Gia nhiệt và làm nguội.Động học nhiệt và trạng thái TiNi của MP1 chưa được xác định ở đây.[15]

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S5-R0079-A01 — mục §2.5.5.** Nguồn tổng quan của Fan và cộng sự phân loại kẹt sợi (fibre/filament jamming) theo cơ chế hình thái: các sợi xếp dọc trục trong vỏ kín khí, độ cứng hiệu dụng thay đổi khi ma sát giữa các sợi thay đổi dưới tác dụng hút chân không. Bài báo đặt cơ chế này cạnh kẹt hạt, kẹt lớp và các dạng lai; Hình 5(g) và Bảng 4 mô tả vị trí của kẹt sợi trong hệ phân loại [15]. Giá trị của nguồn đối với MP1 là xác định không gian kiến trúc và cơ chế ở cấp độ khái quát. Đây không phải là mô hình dự đoán lực pháp tuyến cục bộ, cũng không cung cấp một quan hệ đã kiểm chứng giữa áp suất nguồn và lực tiếp xúc trong bó dây TiNi.

- **Locator PDF trong trace:** PDF physical p.10, Sec. 3.3.1, Fig. 5(g); Table 4 p.11. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** No local normal-force law or MP1 contact topology

**CH2-S5-R0080-A01 — mục §2.5.5.** Nguồn tổng quan của Fan và cộng sự phân loại kẹt sợi (fibre/filament jamming) theo cơ chế hình thái: các sợi xếp dọc trục trong vỏ kín khí, độ cứng hiệu dụng thay đổi khi ma sát giữa các sợi thay đổi dưới tác dụng hút chân không. Bài báo đặt cơ chế này cạnh kẹt hạt, kẹt lớp và các dạng lai; Hình 5(g) và Bảng 4 mô tả vị trí của kẹt sợi trong hệ phân loại [15]. Giá trị của nguồn đối với MP1 là xác định không gian kiến trúc và cơ chế ở cấp độ khái quát. Đây không phải là mô hình dự đoán lực pháp tuyến cục bộ, cũng không cung cấp một quan hệ đã kiểm chứng giữa áp suất nguồn và lực tiếp xúc trong bó dây TiNi.

- **Locator PDF trong trace:** PDF physical p.10–11, Sec. 3.3.1 and Table 4. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Cannot validate MP1 model accuracy

**CH2-S5-R0098-A01 — mục §2.5.5.** Nguồn tổng quan của Fan và cộng sự phân loại kẹt sợi (fibre/filament jamming) theo cơ chế hình thái: các sợi xếp dọc trục trong vỏ kín khí, độ cứng hiệu dụng thay đổi khi ma sát giữa các sợi thay đổi dưới tác dụng hút chân không. Bài báo đặt cơ chế này cạnh kẹt hạt, kẹt lớp và các dạng lai; Hình 5(g) và Bảng 4 mô tả vị trí của kẹt sợi trong hệ phân loại [15]. Giá trị của nguồn đối với MP1 là xác định không gian kiến trúc và cơ chế ở cấp độ khái quát. Đây không phải là mô hình dự đoán lực pháp tuyến cục bộ, cũng không cung cấp một quan hệ đã kiểm chứng giữa áp suất nguồn và lực tiếp xúc trong bó dây TiNi.

- **Locator PDF trong trace:** PDF physical p.10–11; locator issue record. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Legacy locator retained only in provenance, not manuscript

## Nhận xét audit [11]–[15]

- **[11] Zhang et al. (2025)** là nguồn gần nhất trong nhóm này với các claim về continuum layer-jamming; trace dẫn tới phần mô hình, trạng thái tăng tải/trượt/dỡ tải và các đối chiếu/giới hạn. Các ý về giả thiết lớp mỏng, số lớp, sai khác biên và vùng trượt cần được đối chiếu nguyên văn trước khi dùng để kết luận phạm vi hiệu lực.
- **[12] Caro & Carmichael** là bài tổng quan; các claim dùng nó cho cơ chế chân không và phân loại là evidence cấp review, không phải xác minh độc lập các kết quả nghiên cứu gốc.
- **[13] Zhang et al. (2021)** hỗ trợ mô hình cáp nhiều dây có tương tác/trượt, nhưng mô hình và hiệu chuẩn của bài cần được giữ đúng phạm vi; `k` không được đồng nhất với hệ số ma sát Coulomb hoặc áp suất tiếp xúc.
- **[14] GUM** là chuẩn hướng dẫn đo lường. Trace có cả trang vật lý và trang in ở một số dòng; phải phân biệt hai hệ số trang khi đối chiếu. Đây không phải bằng chứng cơ học cho cấu hình MP1.
- **[15] Fan et al.** là tổng quan phân loại phương pháp tăng cứng; hữu ích cho phân loại và thuật ngữ, không phải bằng chứng thực nghiệm cụ thể cho bó dây TiNi.
- Năm PDF có trong thư mục đóng gói. Trace cho [11], [12], [13], [15] thường chỉ rõ mục/hình; riêng một số claim [14] ghi physical page và printed page. Phần này vẫn chưa tái trích xuất nguyên văn từng claim từ PDF, nên excerpt giữ trạng thái “locator/anchor trong trace” như hai phần trước.


---

# Tiếp nối audit: tài liệu tham khảo [16]–[20]

**Phạm vi:** các claim trong bản nháp trỏ tới [16]–[20], theo master traceability. Locator và excerpt/anchor được chuyển từ CSV; đây là dấu vết sẵn có để mở PDF, chưa phải xác nhận độc lập từng câu từ PDF.

| Ref | Nguồn | DOI | Claim/anchor duy nhất | PDF đóng gói |
|---:|---|---|---:|---|
| [16] | L. Bai, H. Yan, J. Li, J. Shan & P. Hou (2022), “Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming” | 10.3390/app12073582 | 7 | `16_2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf` |
| [17] | T. Liu, H. Xia, D.-Y. Lee, A. Firouzeh, Y.-L. Park & K.-J. Cho (2021), “A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots” | 10.1109/lra.2021.3097255 | 14 | `17_2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf` |
| [18] | M. Brancadoro, M. Manti, F. Grani, S. Tognarelli, A. Menciassi & M. Cianchetti (2019), “Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition” | 10.3389/frobt.2019.00012 | 4 | `18_M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf` |
| [19] | G. B. Crowley, X. Zeng & H.-J. Su (2022), “A 3D Printed Soft Robotic Gripper With a Variable Stiffness Enabled by a Novel Positive Pressure Layer Jamming Technology” | 10.1109/lra.2022.3157448 | 5 | `19_M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf` |
| [20] | H. H. Huynh, D. Han, K. Yoshida, M. De Volder & J.-w. Kim (2022), “Soft actuator with switchable stiffness using a micropump-activated jamming system” | 10.1016/j.sna.2022.113449 | 8 | `20_2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf` |

## [16] L. Bai, H. Yan, J. Li, J. Shan & P. Hou (2022), “Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming”

**CH2-S3-R0014-A01 — mục §2.1 Design; §2.2 Modeling; §2.3 Fabrication.** Bai và cộng sự khảo sát một kiến trúc khác với các dây hoặc cáp kraft, gai dầu và nylon, trong đó dây nylon được chọn với đường kính khoảng 1 mm [16]. Các phần tử được bố trí theo tiết diện chữ nhật hoặc tròn trong một bao HDPE kín khí. Tương tác dây–dây và dây–bao, cùng với đường kính và cách xếp, ảnh hưởng đến mức nén, sự tái sắp xếp cục bộ và hiện tượng gradient ở đầu tự do. Chân không là phương thức kích hoạt, còn đáp ứng được đánh giá bằng lực–độ võng khi uốn và mô men–góc khi xoắn. Các miền tiền-trượt, chuyển tiếp và hậu-trượt được dùng để diễn giải đáp ứng toàn hệ; chúng không phải phép đo trực tiếp vị trí hoặc lực tiếp xúc tại từng giao diện. Vì vậy, ảnh hưởng của vật liệu, đường kính và cách xếp phần tử phải được tách khỏi ảnh hưởng của topology trước khi so sánh với bó dây TiNi.

- **Locator PDF trong trace:** Fig. 2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** WEP ghi §2.2 tại p.4 nhưng PDF gốc là §2.1; §2.2 bắt đầu p.5; HDPE xác nhận p.6.

**CH2-S3-R0014-A02 — mục §2.1 Design; §2.2 Modeling; §2.3 Fabrication.** Bai và cộng sự [16]Dây kraft, gai dầu hoặc nylon khoảng 1 mm trong bao HDPE kín khí; tiết diện chữ nhật hoặc tròn.Dây–dây và dây–bao; uốn và xoắn; cách xếp phần tử ảnh hưởng tái sắp xếp.Chân không; bao HDPE kín khí được hàn kín trong cấu trúc chữ nhật.Lực–độ võng khi uốn và mô men–góc khi xoắn; Nguồn dùng hai phép thử riêng cho uốn và xoắn; không so sánh trực tiếp trị số của hai đại lượng này.Vật liệu, đường kính, bao và mô hình không tương đương bó dây TiNi.

- **Locator PDF trong trace:** Fig. 2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** WEP ghi §2.2 tại p.4 nhưng PDF gốc là §2.1; §2.2 bắt đầu p.5; HDPE xác nhận p.6.

**CH2-S3-R0015-A01 — mục §2.2 Modeling; §3.1 Characterization.** Bai và cộng sự khảo sát một kiến trúc khác với các dây hoặc cáp kraft, gai dầu và nylon, trong đó dây nylon được chọn với đường kính khoảng 1 mm [16]. Các phần tử được bố trí theo tiết diện chữ nhật hoặc tròn trong một bao HDPE kín khí. Tương tác dây–dây và dây–bao, cùng với đường kính và cách xếp, ảnh hưởng đến mức nén, sự tái sắp xếp cục bộ và hiện tượng gradient ở đầu tự do. Chân không là phương thức kích hoạt, còn đáp ứng được đánh giá bằng lực–độ võng khi uốn và mô men–góc khi xoắn. Các miền tiền-trượt, chuyển tiếp và hậu-trượt được dùng để diễn giải đáp ứng toàn hệ; chúng không phải phép đo trực tiếp vị trí hoặc lực tiếp xúc tại từng giao diện. Vì vậy, ảnh hưởng của vật liệu, đường kính và cách xếp phần tử phải được tách khỏi ảnh hưởng của topology trước khi so sánh với bó dây TiNi.

- **Locator PDF trong trace:** Fig. 2; experimental plots. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không phải phép đo trực tiếp vị trí hoặc lực tiếp xúc cục bộ; các miền trượt phụ thuộc cách diễn giải đáp ứng.

**CH2-S5-R0007-A01 — mục §2.5.1.** Bai và cộng sự dùng dây kraft, dây gai dầu và dây nylon trong bao HDPE kín khí. Bố trí dây, đường kính và tương tác dây–dây/dây–bao làm thay đổi mức nén và sự tái sắp xếp cục bộ. Trong thử uốn và xoắn chậm, tác giả phân loại đường lực–độ võng thành ba miền: pre-slip với tăng lực gần tuyến tính và dây còn kết dính; transition với độ dốc giảm và đáp ứng phi tuyến khi dây bắt đầu trượt; post-slip với tăng lực chậm, gần miền khi tắt chân không, được gọi là full slip. Các nhãn này xuất phát từ đại lượng toàn cục force–deflection, không phải từ bản đồ trượt vi mô hoặc phép nhận dạng μ [16].

- **Locator PDF trong trace:** Sec. 3.1, Fig. 4g. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không có local slip mapping hoặc μ identification.

**CH2-S5-R0042-A01 — mục §2.5.3.** Bai và cộng sự dùng đường lực–độ võng để mô tả các miền pre-slip, transition và post-slip trong cơ cấu kẹt dây. Ở một số mức chân không, điểm trượt được biểu diễn bằng độ võng trên đường cong; độ cứng uốn trong Hình 4 được tính theo lực chia cho độ võng ở điểm quy định. Đây là một chỉ tiêu kết cấu phụ thuộc điểm lấy và áp suất, không phải mô đun vật liệu. Cùng nghiên cứu còn đo mô men–góc xoay trong thử xoắn; đại lượng này không thể so sánh số học trực tiếp với độ dốc lực–độ võng vì lực tổng quát và chuyển vị tổng quát khác nhau [16].

- **Locator PDF trong trace:** Sec.3.1/Fig.4. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không local slip map/μ.

**CH2-S5-R0043-A01 — mục §2.5.3.** Bai và cộng sự dùng đường lực–độ võng để mô tả các miền pre-slip, transition và post-slip trong cơ cấu kẹt dây. Ở một số mức chân không, điểm trượt được biểu diễn bằng độ võng trên đường cong; độ cứng uốn trong Hình 4 được tính theo lực chia cho độ võng ở điểm quy định. Đây là một chỉ tiêu kết cấu phụ thuộc điểm lấy và áp suất, không phải mô đun vật liệu. Cùng nghiên cứu còn đo mô men–góc xoay trong thử xoắn; đại lượng này không thể so sánh số học trực tiếp với độ dốc lực–độ võng vì lực tổng quát và chuyển vị tổng quát khác nhau [16].

- **Locator PDF trong trace:** Fig.4h–j. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không gộp số liệu xoắn với uốn.

**CH2-S6-R0002-A01 — mục 2.6.1.** Một phân biệt rõ về đường truyền áp suất xuất hiện trong cơ cấu mềm tích hợp bộ phận kẹt bó sợi của Bai và cộng sự [16].

- **Locator PDF trong trace:** {"M09-E04": [{"pdf_page": 9, "printed_page": "9 of 14", "section": "3.2. Applications"}, {"pdf_page": 10, "printed_page": "10 of 14", "section": "3.2. Applications", "figure": "Figure 5c–f"}, {"pdf_page": 11, "printed_page": "11 of 14", "section": "3.2. Applications", "figure": "Figure 5 caption continued"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “positive air pressure of 145 kPa; only about 87 kPa; adjust the positive air pressure”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.


## [17] T. Liu, H. Xia, D.-Y. Lee, A. Firouzeh, Y.-L. Park & K.-J. Cho (2021), “A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots”

**CH2-S3-R0010-A07 — mục Classification context; Section 2; Section 2.2; Design.** Họ kiến trúc kẹt cơ họcKẹt hạtBóng cao su nằm trong môi trường hạt bao quanh và được giữ bởi bao ngoài không dãn; khi bóng phồng, hạt bị nén và độ cứng tăng.Áp suất dương trong bóng cao su ở [17].Môi trường hạt và đường truyền lực khác kẹt dây/sợi; áp suất không phải lực pháp tuyến cục bộ.[17]

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S3-R0024-A01 — mục Design / Concept Design / experiments.** Trong cấu hình kẹt hạt (granular jamming) của Liu và cộng sự, một bóng cao su được bao quanh bởi các hạt SMP và toàn bộ cụm nằm trong một ống vải không co giãn [17]. Đường truyền áp suất đi từ bóng khí đến mạng tiếp xúc giữa các hạt rồi tới ống bao; trong phép thử công xôn, tải uốn bên ngoài tạo ra độ võng; mạng tiếp xúc hạt và biên giam giữ chi phối độ cứng và đáp ứng dưới tải. Đây là một ví dụ mà môi trường truyền lực không phải là các lớp liên tục mà là tập hợp hạt có tiếp xúc thay đổi, nên các đại lượng quan sát được và các dạng mất ổn định cũng khác với kẹt lớp/tấm. Sự khác biệt giữa mạng hạt và giao diện lớp–lớp phải được giữ riêng khi đối chiếu với MP1.

- **Locator PDF trong trace:** Fig. 1; Fig. 5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không mô tả tái tổ chức hạt như nguồn độc lập của tải uốn; không chuyển architecture sang MP1.

**CH2-S3-R0024-A02 — mục Design / Concept Design / experiments.** Liu và cộng sự [17] — kẹt hạt áp suất dươngBóng cao su, hạt SMP bao quanh bóng và ống vải không co giãn.Áp suất dương làm bóng phồng; lực truyền qua hạt đến ống bao.Mạng tiếp xúc hạt–hạt và hạt–biên bị nén, làm tăng sức kháng của cụm.Tải uốn bên ngoài tạo độ võng công xôn; mạng hạt và biên giam giữ chi phối độ cứng; đáp ứng phụ thuộc phân bố hạt, mức nạp và độ mềm bóng.Không chuyển mô hình hạt–bao hoặc kích thước mẫu sang MP1.

- **Locator PDF trong trace:** Fig. 1; Fig. 5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không mô tả tái tổ chức hạt như nguồn độc lập của tải uốn; không chuyển architecture sang MP1.

**CH2-S3-R0034-A01 — mục Design / Fig.1.** Một đường truyền khác được Liu và cộng sự sử dụng cho kẹt hạt áp suất dương: bóng cao su đặt trong môi trường hạt SMP, toàn bộ cụm nằm trong ống vải không giãn và các nắp biên [17]. Không khí dương làm bóng nở, nén môi trường hạt và truyền tải tới ống bao. Thí nghiệm công xôn ghi lực–chuyển vị ở các mức 69, 103, 138 và 172 kPa áp suất dư; độ cứng được tính từ khoảng 1 mm đầu hành trình. Nguồn này không đo trực tiếp lực tiếp xúc hạt–hạt hoặc hạt–bao, nên áp suất cấp cho bóng chỉ là biến điều khiển của hệ, không phải lực pháp tuyến cục bộ. Đáp ứng đo được cũng chịu ảnh hưởng đồng thời của mạng tiếp xúc hạt, độ mềm của bóng và hình học giam giữ.

- **Locator PDF trong trace:** Fig.1. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Áp suất nguồn không được đo như lực tiếp xúc cục bộ.

**CH2-S3-R0035-A01 — mục Pressure modulation / Fig.6.** Một đường truyền khác được Liu và cộng sự sử dụng cho kẹt hạt áp suất dương: bóng cao su đặt trong môi trường hạt SMP, toàn bộ cụm nằm trong ống vải không giãn và các nắp biên [17]. Không khí dương làm bóng nở, nén môi trường hạt và truyền tải tới ống bao. Thí nghiệm công xôn ghi lực–chuyển vị ở các mức 69, 103, 138 và 172 kPa áp suất dư; độ cứng được tính từ khoảng 1 mm đầu hành trình. Nguồn này không đo trực tiếp lực tiếp xúc hạt–hạt hoặc hạt–bao, nên áp suất cấp cho bóng chỉ là biến điều khiển của hệ, không phải lực pháp tuyến cục bộ. Đáp ứng đo được cũng chịu ảnh hưởng đồng thời của mạng tiếp xúc hạt, độ mềm của bóng và hình học giam giữ.

- **Locator PDF trong trace:** Fig.6. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Đáp ứng cấp hệ thống chịu ảnh hưởng của bóng, mạng hạt và hình học.

**CH2-S3-R0040-A04 — mục 3.1.3;Experiments;Design/Fig.1;Limitations.** Kẹt hạt áp suất dương [17]Bóng cao su → hạt SMP → ống vải không giãn.Công xôn; lực–chuyển vị; độ cứng trong 1 mm đầu.Đáp ứng cấp hệ thống; không có luật tiếp xúc cục bộ.69–172 kPa áp suất dư; đo lặp và khoảng tin cậy.Không đo lực tiếp xúc; ảnh hưởng đồng thời của bóng, mạng hạt và hình học.

- **Locator PDF trong trace:** Fig.3c;Fig.3;Fig.1;Conclusion. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Tổng hợp của tác giả; không phải tuyên bố novelty.

**CH2-S3-R0044-A04 — mục Design/experiments;Design/Modeling;Design/experiments;Abstract/Design/Methods.** Hạt [17]Mạng hạt–hạt và hạt–biên; bóng khí và ống bao; biên giam giữ truyền tải.Lực–chuyển vị và độ cứng hiệu dụng theo áp suất.Đáp ứng cấp hệ; lực tiếp xúc cục bộ thường không được đo.Áp suất nguồn không phải lực pháp tuyến; hình thái kết nối liên tục của bó dây không tương đương.

- **Locator PDF trong trace:** Fig.2;Fig.2;Fig.1/Fig.6;Abstract/Fig.4. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Tổng hợp từ các kiến trúc đã nghiệm thu; không xác định topology MP1.

**CH2-S3-R0051-A04 — mục Secs.5.1–5.3;Abstract;5 Performance comparison;Conclusion.** Hạt [17]Mạng hạt–hạt và hạt–biên; bóng khí và ống bao; biên giam giữ truyền tải.Lực–chuyển vị và độ cứng hiệu dụng theo áp suất.Đáp ứng cấp hệ; lực tiếp xúc cục bộ thường không được đo.Áp suất nguồn không phải lực pháp tuyến; hình thái kết nối liên tục của bó dây không tương đương.

- **Locator PDF trong trace:** Fig.4;Abstract;Table1;Conclusion. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Ranh giới so sánh do tác giả tổng hợp.

**CH2-S5-R0044-A01 — mục §2.5.3.** Ở nghiên cứu của Liu và cộng sự, cơ cấu hạt áp suất dương có bao vải, bóng cao su và hạt SMP; mẫu đơn có đường kính 26 mm và chiều dài 50 mm. Thử công xôn dùng áp suất tương đối 69, 103, 138 và 172 kPa; độ cứng được tính từ lực trong 1 mm đầu, vùng được xem là biến dạng nhỏ. Hình 6 dùng trung bình của tám lần lặp và dải khoảng tin cậy 95%; các độ dốc được báo cáo là 0,69; 1,72; 2,75 và 4,02 N/mm ở các mức áp suất tăng. Nghiên cứu này cũng dùng D = 26, 29, 32, 35 mm và d = 10 hoặc 15 mm để khảo sát hình học, đồng thời gọi E suy ra từ đáp ứng là mô đun Young tương đương. E này là tham số hiệu dụng cấp kết cấu, không phải phép đo độc lập của vật liệu hạt [17].

- **Locator PDF trong trace:** Figs.4–8/Table I. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** E effective; unloading K không tách riêng.

**CH2-S5-R0045-A01 — mục §2.5.3.** Ở nghiên cứu của Liu và cộng sự, cơ cấu hạt áp suất dương có bao vải, bóng cao su và hạt SMP; mẫu đơn có đường kính 26 mm và chiều dài 50 mm. Thử công xôn dùng áp suất tương đối 69, 103, 138 và 172 kPa; độ cứng được tính từ lực trong 1 mm đầu, vùng được xem là biến dạng nhỏ. Hình 6 dùng trung bình của tám lần lặp và dải khoảng tin cậy 95%; các độ dốc được báo cáo là 0,69; 1,72; 2,75 và 4,02 N/mm ở các mức áp suất tăng. Nghiên cứu này cũng dùng D = 26, 29, 32, 35 mm và d = 10 hoặc 15 mm để khảo sát hình học, đồng thời gọi E suy ra từ đáp ứng là mô đun Young tương đương. E này là tham số hiệu dụng cấp kết cấu, không phải phép đo độc lập của vật liệu hạt [17].

- **Locator PDF trong trace:** Pressure modulation/Eqs.(1–5). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không pressure–friction law MP1.

**CH2-S5-R0057-A01 — mục §2.5.4.** Liu và cộng sự nghiên cứu một kết cấu kẹt hạt bằng áp suất dương. Trong phép uốn công xôn, tác giả dùng tám cấu hình với đường kính ngoài D = 26, 29, 32 và 35 mm, đường kính trong d = 10 hoặc 15 mm, và báo cáo áp suất tương đối 103 kPa cho nghiên cứu hình học [17]. Độ cứng được tính từ lực tại 1 mm đầu tiên của đường cong, còn “mô đun Young tương đương” được định nghĩa như mô đun uốn hiệu dụng biểu thị khả năng các hạt đã kẹt chống biến dạng uốn. Do đó, đại lượng này là tham số của mô hình kết cấu trong điều kiện thử, không phải phép đo độc lập mô đun Young nội tại của vật liệu hạt, ống bao hoặc túi đàn hồi.

- **Locator PDF trong trace:** PDF p.4 (printed 8081), Sec. III-C, Fig. 7, Table I. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Not transferable to TiNi or local interface traction

**CH2-S5-R0059-A01 — mục §2.5.4.** Nguồn [17] cho thấy cách một đại lượng toàn cục có thể được dùng để suy ra một tham số hiệu dụng. Mô hình vòng của kết cấu PPJ giả định kẹt hoàn toàn, biến dạng nhỏ, phân bố hạt đều và bỏ qua một số ảnh hưởng của vật liệu ống bao, hệ số ma sát và biến dạng túi đàn hồi. Chính bài báo cũng ghi nhận rằng chuyển vị tương đối giữa các hạt xuất hiện ngay từ giai đoạn đầu và ma sát phụ thuộc áp suất góp phần vào độ cứng. Vì vậy, quan hệ hiệu dụng của [17] phải được hiểu trong phạm vi hình học, miền biến dạng và giả định của nguồn, không thể chuyển thành mô đun TiNi độc lập cho MP1.

- **Locator PDF trong trace:** PDF p.4 (printed 8081), Sec. III-C, Eqs. (1)–(4). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Not intrinsic material E; no TiNi transfer

**CH2-S5-R0084-A01 — mục §2.5.5.** Nhóm mô hình đồng nhất hóa hoặc tham số hiệu dụng nén nhiều chi tiết vi mô vào một đại lượng kết cấu. Liu và cộng sự mô tả cơ cấu kẹt hạt bằng áp suất dương như một tiết diện vành khăn, với mô đun Young tương đương và độ cứng công xôn được suy ra từ hình học D, d, chiều dài L và lực đo trong 1 mm đầu của đường cong. Tác giả báo cáo các độ cứng tăng theo áp suất 69, 103, 138 và 172 kPa, cùng các đường hồi quy có R² cao trong thí nghiệm của chính cơ cấu PPJ [17]. Tuy nhiên, mô đun tương đương được xây dựng từ đáp ứng kết cấu; hệ số C trong quan hệ hình học phụ thuộc các yếu tố như áp suất và vật liệu, có đơn vị của nguồn và không được đo như một mô đun vật liệu độc lập. Mô hình giả định tiết diện vành khăn, biến dạng nhỏ, các hạt phân bố đều và trạng thái kẹt lý tưởng trong phần suy luận. Vì vậy, nó hữu ích để diễn giải đáp ứng toàn cục trong miền hiệu chuẩn, nhưng không nhận dạng riêng lực tiếp xúc dây–dây hay dây–ống bao và không thể chuyển trực tiếp thành định luật cho bó dây TiNi.

- **Locator PDF trong trace:** PDF physical pp.3–4 (journal 8081–8082), Sec. III-B/C, Eqs. (1)–(5). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Positive-pressure granular PPJ, not TiNi wire bundle

**CH2-S5-R0085-A01 — mục §2.5.5.** Nhóm mô hình đồng nhất hóa hoặc tham số hiệu dụng nén nhiều chi tiết vi mô vào một đại lượng kết cấu. Liu và cộng sự mô tả cơ cấu kẹt hạt bằng áp suất dương như một tiết diện vành khăn, với mô đun Young tương đương và độ cứng công xôn được suy ra từ hình học D, d, chiều dài L và lực đo trong 1 mm đầu của đường cong. Tác giả báo cáo các độ cứng tăng theo áp suất 69, 103, 138 và 172 kPa, cùng các đường hồi quy có R² cao trong thí nghiệm của chính cơ cấu PPJ [17]. Tuy nhiên, mô đun tương đương được xây dựng từ đáp ứng kết cấu; hệ số C trong quan hệ hình học phụ thuộc các yếu tố như áp suất và vật liệu, có đơn vị của nguồn và không được đo như một mô đun vật liệu độc lập. Mô hình giả định tiết diện vành khăn, biến dạng nhỏ, các hạt phân bố đều và trạng thái kẹt lý tưởng trong phần suy luận. Vì vậy, nó hữu ích để diễn giải đáp ứng toàn cục trong miền hiệu chuẩn, nhưng không nhận dạng riêng lực tiếp xúc dây–dây hay dây–ống bao và không thể chuyển trực tiếp thành định luật cho bó dây TiNi.

- **Locator PDF trong trace:** PDF physical p.4, Eq. (3) discussion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Do not transfer C or E to MP1


## [18] M. Brancadoro, M. Manti, F. Grani, S. Tognarelli, A. Menciassi & M. Cianchetti (2019), “Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition”

**CH2-S3-R0012-A01 — mục Design.** Brancadoro và cộng sự minh họa sự phụ thuộc của cơ chế vào hình thái kết nối và ghép nối cơ học trong một mô-đun silicone [18]. Hai mô-đun có chiều dài 50 mm và đường kính ngoài 14,5 mm. Ở Mô-đun A, vùng kẹt sợi chiếm kênh trung tâm; ở Mô-đun B, một lòng rỗng trung tâm 4,5 mm được giữ lại và các sợi được bố trí theo dạng lược liên kết. Thân mô-đun dùng silicone, còn các sợi được xếp theo kiểu hai dãy răng lược ăn khớp, tạo tiếp xúc sợi–sợi. Các buồng sợi được hút chân không để tăng mức ghép nối; do đó, lòng rỗng, cách bố trí sợi và hướng uốn cùng quyết định đường truyền tải. Nghiên cứu đánh giá đáp ứng của mô-đun bằng các phép thử lực cản ở trạng thái thẳng và cong, nhưng không đo độc lập lực tiếp xúc tại từng vị trí sợi. Kết quả này hỗ trợ phân tích hình học và ghép nối của kiến trúc sợi, không xác nhận hình thái tiếp xúc của bó dây TiNi.

- **Locator PDF trong trace:** Fig. 2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Hình thái lược, silicone và lòng rỗng không tương đương bó dây TiNi.

**CH2-S3-R0012-A02 — mục Design.** Brancadoro và cộng sự [18]Mô-đun silicone; sợi bông phủ sáp (waxed cotton) dạng lược liên kết. Mô-đun A không giữ lòng rỗng; Mô-đun B giữ lòng rỗng 4,5 mm.Tiếp xúc sợi–sợi; mô-đun thẳng và cong.Buồng sợi hút chân không; nguồn không báo cáo lực tiếp xúc cục bộ.Lực cản ở trạng thái thẳng và cong; đánh giá khả năng thay đổi độ cứng của mô-đun.Không phải bó dây TiNi; hình thái lược, silicone và điều kiện biên khác.

- **Locator PDF trong trace:** Fig. 2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Hình thái lược, silicone và lòng rỗng không tương đương bó dây TiNi.

**CH2-S3-R0013-A01 — mục Design; experimental characterization context.** Brancadoro và cộng sự minh họa sự phụ thuộc của cơ chế vào hình thái kết nối và ghép nối cơ học trong một mô-đun silicone [18]. Hai mô-đun có chiều dài 50 mm và đường kính ngoài 14,5 mm. Ở Mô-đun A, vùng kẹt sợi chiếm kênh trung tâm; ở Mô-đun B, một lòng rỗng trung tâm 4,5 mm được giữ lại và các sợi được bố trí theo dạng lược liên kết. Thân mô-đun dùng silicone, còn các sợi được xếp theo kiểu hai dãy răng lược ăn khớp, tạo tiếp xúc sợi–sợi. Các buồng sợi được hút chân không để tăng mức ghép nối; do đó, lòng rỗng, cách bố trí sợi và hướng uốn cùng quyết định đường truyền tải. Nghiên cứu đánh giá đáp ứng của mô-đun bằng các phép thử lực cản ở trạng thái thẳng và cong, nhưng không đo độc lập lực tiếp xúc tại từng vị trí sợi. Kết quả này hỗ trợ phân tích hình học và ghép nối của kiến trúc sợi, không xác nhận hình thái tiếp xúc của bó dây TiNi.

- **Locator PDF trong trace:** Fig. 2; experimental figures. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Locator chính của E01 là p.4; các trang sau dùng để kiểm tra giới hạn/quan sát, không suy local traction.

**CH2-S5-R0041-A01 — mục §2.5.3.** Brancadoro và cộng sự [18]Sợi PTFE, PVC, nylon, silicone, cotton phủ sáp hoặc da; kiểu bó/lược; 1,01325 bar so với 0,1 bar.Lực cực đại cấp mô đun.Tỷ lệ Fmax,kẹt/Fmax,không kẹt; +43% đến +377,5% trong tổ hợp nguồn.Mẫu và giá trị được dẫn lại; tỷ lệ không phải E, EI hay một độ dốc chung.

- **Locator PDF trong trace:** Table 1; Methods. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không phải E/EI hoặc slope metric chung.


## [19] G. B. Crowley, X. Zeng & H.-J. Su (2022), “A 3D Printed Soft Robotic Gripper With a Variable Stiffness Enabled by a Novel Positive Pressure Layer Jamming Technology”

**CH2-S3-R0023-A01 — mục II-B Principle; II-C Design; IV-A results.** Nghiên cứu sử dụng cấu hình kẹt lớp/tấm dưới áp suất dương, trong đó các lớp Mylar nằm trong một khung PETG cứng phân đoạn và được bao bởi túi TPU [19]. Khung, túi và các lớp được bố trí sao cho các lớp làm việc trong điều kiện cong và chịu kéo phù hợp, từ đó giảm xu hướng oằn khi chịu tải. Tuy vậy, hiện tượng trượt vẫn được ghi nhận như một cơ chế giới hạn hoặc một chuyển tiếp trong đáp ứng, cho thấy áp suất dương không loại bỏ bài toán tiếp xúc mà chỉ thay đổi điều kiện giam giữ của nó. Các kết quả về độ cứng và chuyển trạng thái của nghiên cứu này vì thế gắn với kiến trúc cụ thể gồm khung phân đoạn, túi đàn hồi và lớp Mylar; vì vậy kết quả gắn với khung, túi, lớp và đường truyền lực của gripper.

- **Locator PDF trong trace:** Fig. 1; Fig. 2; experimental curves. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Kết quả phụ thuộc gripper 12 lớp, khung và tải cong; không phải luật dầm layer-jamming tổng quát.

**CH2-S3-R0023-A02 — mục II-B Principle; II-C Design; IV-A results.** Crowley và cộng sự [19] — kẹt lớp/tấm áp suất dươngLớp Mylar trong khung PETG phân đoạn, túi TPU và thân gripper.Túi bơm phồng ép lớp vào khung cứng; lớp nằm về phía trong vùng cong.Tăng lực nén và ma sát giữa lớp; bố trí lớp chịu kéo để giảm xu hướng oằn.Trượt giữa lớp vẫn là cơ chế giới hạn/chuyển tiếp; kết quả phụ thuộc cấu hình gripper.Không phải dầm layer-jamming tổng quát; không chuyển trực tiếp sang MP1.

- **Locator PDF trong trace:** Fig. 1; Fig. 2; experimental curves. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Kết quả phụ thuộc gripper 12 lớp, khung và tải cong; không phải luật dầm layer-jamming tổng quát.

**CH2-S5-R0009-A01 — mục §2.5.1.** Crowley, Zeng và Su khảo sát kẹt lớp dưới áp suất dương trong một ngón kẹp có túi khí, khung hạn chế cứng và các lớp Mylar chồng lấn. Ngón được cố định vào đế, đưa về cấu hình cong rồi tác dụng chuyển vị bằng cảm biến lực trên bàn trượt; mỗi mức áp suất được lặp năm lần với biên độ 6 mm. Trên đường lực–chuyển vị trung bình, ở 10 psi (69,0 kPa) độ cứng gần bão hòa trong khoảng 2 mm đầu và bắt đầu giảm do trượt khoảng 2 mm; ở 45 psi (310,3 kPa), không thấy chuyển tiếp trượt riêng biệt trong toàn bộ khoảng 6 mm. Đây là quan sát ở cấp ngón kẹp. Nguồn không đo trực tiếp ma sát cục bộ, pn(x) hay trạng thái trượt tại từng lớp, nên “không thấy trượt rõ rệt” không thể được diễn giải thành “không có trượt vi mô” [19].

- **Locator PDF trong trace:** Sec. IV-A; Fig. 6a–b caption. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không đo μ, p_n(x) hoặc microscopic slip.

**CH2-S5-R0010-A01 — mục §2.5.1.** Crowley, Zeng và Su khảo sát kẹt lớp dưới áp suất dương trong một ngón kẹp có túi khí, khung hạn chế cứng và các lớp Mylar chồng lấn. Ngón được cố định vào đế, đưa về cấu hình cong rồi tác dụng chuyển vị bằng cảm biến lực trên bàn trượt; mỗi mức áp suất được lặp năm lần với biên độ 6 mm. Trên đường lực–chuyển vị trung bình, ở 10 psi (69,0 kPa) độ cứng gần bão hòa trong khoảng 2 mm đầu và bắt đầu giảm do trượt khoảng 2 mm; ở 45 psi (310,3 kPa), không thấy chuyển tiếp trượt riêng biệt trong toàn bộ khoảng 6 mm. Đây là quan sát ở cấp ngón kẹp. Nguồn không đo trực tiếp ma sát cục bộ, pn(x) hay trạng thái trượt tại từng lớp, nên “không thấy trượt rõ rệt” không thể được diễn giải thành “không có trượt vi mô” [19].

- **Locator PDF trong trace:** Sec. IV-A; Fig. 6a–b. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không chứng minh vắng trượt vi mô hoặc ngưỡng phổ quát.

**CH2-S6-R0007-A01 — mục 2.6.1.** Kẹt lớp bằng áp suất dương được Crowley và cộng sự triển khai trong một ngón kẹp có túi tạo ép lên các lớp [19].

- **Locator PDF trong trace:** {"M11-E01": "§II.B–C; Fig.1, jamming bag and rigid reaction frame"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “compressed instead by an inflatable membrane or jamming bag”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.


## [20] H. H. Huynh, D. Han, K. Yoshida, M. De Volder & J.-w. Kim (2022), “Soft actuator with switchable stiffness using a micropump-activated jamming system”

**CH2-S3-R0025-A01 — mục Concept / Figs. 2–3; integrated tests/conclusions.** Huynh và cộng sự tách hai chức năng áp suất trong một cơ cấu kép: áp suất âm của chất lưu điện liên hợp (electro-conjugate fluid, ECF) được dùng để tạo kẹt hạt trong khoang PDMS chứa hạt Al₂O₃, còn áp suất dương của ECF làm cong một cấu trúc Pneu-Net [20]. Sự phân công này cho thấy cùng một môi chất có thể tạo ra hai tác động cơ học khác nhau khi đi qua hai hình thái tiếp xúc và hai đường biên khác nhau. Nếu suy ra một “áp suất tích hợp” từ đáp ứng toàn hệ, đó chỉ là đại lượng hiệu dụng dựa trên cấu hình và phép đo cụ thể, không phải bằng chứng rằng áp suất cấp ở hai nhánh có cùng ý nghĩa tại các giao diện. Vì vậy, hai đường áp suất cần được phân biệt khi diễn giải đáp ứng.

- **Locator PDF trong trace:** Figs. 2–3, 10–13. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Áp suất tích hợp được suy ra một phần từ hiệu chuẩn vi bơm; không chuyển sang piston SMA.

**CH2-S3-R0025-A02 — mục Concept / Figs. 2–3; integrated tests/conclusions.** Huynh và cộng sự [20] — cơ cấu kép kẹt hạt/uốnHạt Al₂O₃ trong khoang PDMS; vi bơm chất lưu điện liên hợp tạo hai nhánh áp suất.Áp suất âm tạo kẹt hạt; áp suất dương làm Pneu-Net cong.Hai đường áp suất có vai trò cơ học khác nhau trong cùng thân PDMS.Áp suất tích hợp và đáp ứng hệ phụ thuộc hiệu chuẩn vi bơm; không phải luật vật liệu chung.Không chuyển hành vi vi bơm hoặc áp suất hai nhánh sang piston SMA của MP1.

- **Locator PDF trong trace:** Figs. 2–3, 10–13. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Áp suất tích hợp được suy ra một phần từ hiệu chuẩn vi bơm; không chuyển sang piston SMA.

**CH2-S4-R0086-A01 — mục 2.4.4.** Huynh và cộng sự cho thấy cùng một nguồn áp suất có thể phục vụ hai chức năng khác nhau. Vi bơm dùng chất lưu điện liên hợp, ký hiệu ECF, được tích hợp dưới cơ cấu PDMS chứa hạt nhôm oxit. Áp suất âm gây kẹt hạt và tăng sức kháng uốn, còn áp suất dương làm phồng khoang để tạo uốn. Nguồn chấp hành ở đây là dòng chất lưu do điện trường, không phải SMA. Chức năng cơ học phụ thuộc cả chiều tạo áp lẫn cấu trúc nhận áp [20, tr. 2–4].

- **Locator PDF trong trace:** §2; Figs1–3. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0087-A01 — mục 2.4.4.** Tác giả khảo sát vi bơm riêng vì không đo trực tiếp được áp suất trong cơ cấu đã lắp. Trong phép thử công xôn, đầu tự do được đẩy 3 mm với tốc độ 0,5 mm/s; lực tại 3 mm tăng từ 0,134 N lên 0,743 N ở mức áp suất âm danh định −50 kPa. Hệ số khoảng 5,5 vì vậy là tỷ số lực tại cùng độ dịch trong điều kiện thử. Nó chưa xác định tỷ số mô đun vật liệu hoặc độ cứng chống uốn EI. Các nhãn áp suất của thử nghiệm được suy từ phép khảo sát vi bơm riêng [20, tr. 6–8].

- **Locator PDF trong trace:** §§4.1–4.2; Figs9–11. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0088-A01 — mục 2.4.4.** Tác giả khảo sát vi bơm riêng vì không đo trực tiếp được áp suất trong cơ cấu đã lắp. Trong phép thử công xôn, đầu tự do được đẩy 3 mm với tốc độ 0,5 mm/s; lực tại 3 mm tăng từ 0,134 N lên 0,743 N ở mức áp suất âm danh định −50 kPa. Hệ số khoảng 5,5 vì vậy là tỷ số lực tại cùng độ dịch trong điều kiện thử. Nó chưa xác định tỷ số mô đun vật liệu hoặc độ cứng chống uốn EI. Các nhãn áp suất của thử nghiệm được suy từ phép khảo sát vi bơm riêng [20, tr. 6–8].

- **Locator PDF trong trace:** §4.2; Fig11. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S5-R0061-A01 — mục §2.5.4.** Huynh và cs. (2022) [20]Hệ cấu trúc Pneu-Nets bằng PDMS chứa hạt alumina và bơm ECF hai chiều. Bơm riêng đạt 55 kPa và 140 mm³/s; phép thử kẹt dùng áp suất âm suy ra −10 đến −50 kPa.“Độ cứng” được biểu diễn bằng lực đầu mút theo chuyển vị; tại 3 mm, lực tăng từ 0,134 lên 0,743 N ở −50 kPa, tỷ số khoảng 5,5.Một đầu cố định, đầu kia chịu lực kế ở 0,5 mm/s trong hành trình 3 mm. Áp suất trong cơ cấu tích hợp không đo trực tiếp; không có lặp lại hoặc dải sai số cho đường lực.Tỷ số 5,5 là tỷ số lực tại 3 mm, không phải tỷ số mô đun hoặc độ dốc tiếp tuyến. Áp suất bơm tách rời không phải ứng suất tiếp xúc tại mẫu.

- **Locator PDF trong trace:** PDF pp.6–8, Sec. 4.1, Figs. 9–10. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Do not equate 55 kPa with pressure at integrated specimen

**CH2-S5-R0062-A01 — mục §2.5.4.** Huynh và cs. (2022) [20]Hệ cấu trúc Pneu-Nets bằng PDMS chứa hạt alumina và bơm ECF hai chiều. Bơm riêng đạt 55 kPa và 140 mm³/s; phép thử kẹt dùng áp suất âm suy ra −10 đến −50 kPa.“Độ cứng” được biểu diễn bằng lực đầu mút theo chuyển vị; tại 3 mm, lực tăng từ 0,134 lên 0,743 N ở −50 kPa, tỷ số khoảng 5,5.Một đầu cố định, đầu kia chịu lực kế ở 0,5 mm/s trong hành trình 3 mm. Áp suất trong cơ cấu tích hợp không đo trực tiếp; không có lặp lại hoặc dải sai số cho đường lực.Tỷ số 5,5 là tỷ số lực tại 3 mm, không phải tỷ số mô đun hoặc độ dốc tiếp tuyến. Áp suất bơm tách rời không phải ứng suất tiếp xúc tại mẫu.

- **Locator PDF trong trace:** PDF pp.2–3, Fig. 2; pp.8–10, Secs. 4.2–4.3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Do not relabel ECF pump as SMA pump

**CH2-S5-R0063-A01 — mục §2.5.4.** Huynh và cs. (2022) [20]Hệ cấu trúc Pneu-Nets bằng PDMS chứa hạt alumina và bơm ECF hai chiều. Bơm riêng đạt 55 kPa và 140 mm³/s; phép thử kẹt dùng áp suất âm suy ra −10 đến −50 kPa.“Độ cứng” được biểu diễn bằng lực đầu mút theo chuyển vị; tại 3 mm, lực tăng từ 0,134 lên 0,743 N ở −50 kPa, tỷ số khoảng 5,5.Một đầu cố định, đầu kia chịu lực kế ở 0,5 mm/s trong hành trình 3 mm. Áp suất trong cơ cấu tích hợp không đo trực tiếp; không có lặp lại hoặc dải sai số cho đường lực.Tỷ số 5,5 là tỷ số lực tại 3 mm, không phải tỷ số mô đun hoặc độ dốc tiếp tuyến. Áp suất bơm tách rời không phải ứng suất tiếp xúc tại mẫu.

- **Locator PDF trong trace:** PDF p.8, Sec. 4.2, Fig. 11. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Do not report 5.5 as a stiffness coefficient

## Nhận xét audit [16]–[20]

- **[16] Bai et al.** Nguồn về wire jamming dùng dây/cáp trong bao HDPE hút chân không; các claim về pre-slip/transition/post-slip và đáp ứng uốn/xoắn phải giữ đúng vật liệu, cách xếp và phép đo của nguồn. Không chuyển sang bó TiNi hay áp suất dương.
- **[17] Liu et al.** Là granular jamming áp suất dương với bóng khí, hạt SMP và ống vải. Dữ liệu lực–chuyển vị/độ cứng là đáp ứng cấp hệ; không được diễn giải thành phép đo trực tiếp lực tiếp xúc cục bộ.
- **[18] Brancadoro et al.** Là fiber-jamming manipulator với mô-đun và vật liệu riêng; một số bảng trong trace tổng hợp tỷ lệ lực cực đại từ các cấu hình. Cần giữ đó là tỷ số kết cấu trong phép thử được nêu, không phải E/EI.
- **[19] Crowley et al.** Là layer jamming áp suất dương trong ngón gripper, khác lớp chân không và khác bó dây; trace chủ yếu dẫn thiết kế và phép thử cấp ngón.
- **[20] Huynh et al.** Tích hợp vi bơm ECF cho cả áp suất âm tạo granular jamming và áp suất dương uốn Pneu-Net. Trong một số thử nghiệm, áp suất trong actuator tích hợp không đo trực tiếp; phải phân biệt áp suất danh định/hiệu chuẩn riêng với lực đầu mút đo được.
- Cả năm PDF có trong thư mục đóng gói. Locator của [17]–[19] phần lớn là section/figure; một số mục [20] có số trang vật lý. Excerpt và trang vẫn cần đối chiếu trực tiếp trên PDF trước khi đánh dấu VERIFIED FULL TEXT mới.


---

# Tiếp nối audit: tài liệu tham khảo [21]–[25]

**Phạm vi:** claim trong bản nháp gắn [21]–[25], theo master traceability. Locator và excerpt/anchor là dấu vết đã lưu để mở PDF; chưa xác nhận độc lập từng câu bằng cách đọc lại PDF trong lượt này.

| Ref | Nguồn | DOI | Claim/anchor duy nhất | PDF đóng gói |
|---:|---|---|---:|---|
| [21] | S. Vahidi, J. Arghavani, E. Choi & A. Ostadrahimi (2022), “Mechanical response of single and double-helix SMA wire ropes” | 10.1080/15376494.2021.1955313 | 9 | `21_A3-2022-Mechanical response of single and double-helix.pdf` |
| [22] | B. Reedlunn, S. Daly & J. Shaw (2013), “Superelastic shape memory alloy cables: Part II – Subcomponent isothermal responses” | 10.1016/j.ijsolstr.2013.03.015 | 4 | `22_2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf` |
| [23] | P. Narjabadifam et al. (2024), “Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes” | 10.3390/buildings14061567 | 2 | `23_2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf` |
| [24] | F. Barsi, B. Carboni & W. Lacarbonara (2025), “A new mechanical model of short wire ropes: Theory and experimental validation” | 10.1016/j.engstruct.2024.119217 | 15 | `24_2025-A new mechanical model of short wire ropes Theory and experimental.pdf` |
| [25] | K. Takashima, T. Imazawa & H. Cho (2022), “Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon” | 10.20965/jrm.2022.p0466 | 4 | `25_2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf` |

## [21] S. Vahidi, J. Arghavani, E. Choi & A. Ostadrahimi (2022), “Mechanical response of single and double-helix SMA wire ropes”

**CH2-S4-R0002-A01 — mục 2.4.1.** Siêu đàn hồi là khả năng thu hồi biến dạng lớn trong một chu trình tải–dỡ tải gần đẳng nhiệt nhờ chuyển pha do ứng suất, thường đi kèm vòng trễ cơ học. Hiệu ứng nhớ hình liên quan đến việc biến dạng được tạo ở trạng thái martensit và được phục hồi khi gia nhiệt qua miền chuyển pha. Hai hiện tượng có cùng nền tảng chuyển pha nhưng không thể dùng thay thế cho nhau. Trong nghiên cứu của Vahidi và cộng sự, trường hợp siêu đàn hồi được mô phỏng ở nhiệt độ trên nhiệt độ kết thúc austenit, còn trường hợp nhớ hình được mô phỏng bằng gia nhiệt sau khi tạo biến dạng ở nhiệt độ thấp hơn miền bắt đầu austenit [21, tr. 6–8]. Đây là điều kiện của mô hình nguồn, không phải bằng chứng rằng bó dây MP1 sẽ luôn làm việc trong một trong hai miền đó.

- **Locator PDF trong trace:** physical PDF pp.3–4, Introduction/model description. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0041-A01 — mục 2.4.2.** Vahidi và cộng sự [21] mô tả tường minh hình học xoắn và tiếp xúc giữa các bề mặt bằng mô hình FE. Mô hình có tương tác pháp tuyến và tiếp tuyến giữa các bề mặt, với hệ số ma sát được chỉ định. Với vật liệu SMA, tác giả dùng mô hình hiện tượng học Souza ba chiều trong Abaqus thông qua UMAT. Các hệ số ma sát và điều kiện tiếp xúc là đầu vào của bài toán nguồn; chúng chưa phải các tham số được nhận dạng cho bó TiNi của MP1.

- **Locator PDF trong trace:** Physical PDF M25:3,5; Sec.2; Sec.4.2; Souza model; UMAT implementation prose. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0042-A01 — mục 2.4.2.** Vahidi và cộng sự [21] mô tả tường minh hình học xoắn và tiếp xúc giữa các bề mặt bằng mô hình FE. Mô hình có tương tác pháp tuyến và tiếp tuyến giữa các bề mặt, với hệ số ma sát được chỉ định. Với vật liệu SMA, tác giả dùng mô hình hiện tượng học Souza ba chiều trong Abaqus thông qua UMAT. Các hệ số ma sát và điều kiện tiếp xúc là đầu vào của bài toán nguồn; chúng chưa phải các tham số được nhận dạng cho bó TiNi của MP1.

- **Locator PDF trong trace:** Physical PDF M25:4–5; Secs.4.1–4.2; Surface-to-surface contact prose. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0043-A01 — mục 2.4.2.** Phạm vi đối chiếu của [21] chủ yếu là kéo dọc trục. Một đầu mẫu bị ràng buộc, đầu còn lại nhận chuyển vị hoặc tải tham chiếu chỉ theo phương trục. Mẫu thép 1×37 được so sánh với kết quả FE đã công bố; các đường kéo của mẫu SMA 1×27 và 7×7 được đối chiếu với thí nghiệm Reedlunn đã công bố, với các tham số vật liệu được kế thừa. Công trình không thực hiện thí nghiệm mới và không cung cấp kiểm chứng uốn. Việc mô tả riêng hình học xoắn, tiếp xúc và ứng xử vật liệu giúp khảo sát một bài toán chi tiết hơn, nhưng mức độ chi tiết cùng chi phí tính toán không tự chứng minh khả năng dự báo tốt hơn cho bài toán khác. Khi biến đổi vật liệu và tương tác tiếp xúc cùng xuất hiện trong kết quả tổng thể, kết quả đó cũng chưa cho phép tách duy nhất phần trễ do vật liệu và phần trễ do ma sát.

- **Locator PDF trong trace:** Physical PDF M25:4–6; Secs.4.1–5.2; Table2; Figs.5,8–12. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0044-A01 — mục 2.4.2.** Phạm vi đối chiếu của [21] chủ yếu là kéo dọc trục. Một đầu mẫu bị ràng buộc, đầu còn lại nhận chuyển vị hoặc tải tham chiếu chỉ theo phương trục. Mẫu thép 1×37 được so sánh với kết quả FE đã công bố; các đường kéo của mẫu SMA 1×27 và 7×7 được đối chiếu với thí nghiệm Reedlunn đã công bố, với các tham số vật liệu được kế thừa. Công trình không thực hiện thí nghiệm mới và không cung cấp kiểm chứng uốn. Việc mô tả riêng hình học xoắn, tiếp xúc và ứng xử vật liệu giúp khảo sát một bài toán chi tiết hơn, nhưng mức độ chi tiết cùng chi phí tính toán không tự chứng minh khả năng dự báo tốt hơn cho bài toán khác. Khi biến đổi vật liệu và tương tác tiếp xúc cùng xuất hiện trong kết quả tổng thể, kết quả đó cũng chưa cho phép tách duy nhất phần trễ do vật liệu và phần trễ do ma sát.

- **Locator PDF trong trace:** Physical PDF M25:4–5; Sec.4;Sec.4.2; Implicit solver and contact/mesh discussion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0048-A01 — mục 2.4.2.** Phạm vi đối chiếu của [21] chủ yếu là kéo dọc trục. Một đầu mẫu bị ràng buộc, đầu còn lại nhận chuyển vị hoặc tải tham chiếu chỉ theo phương trục. Mẫu thép 1×37 được so sánh với kết quả FE đã công bố; các đường kéo của mẫu SMA 1×27 và 7×7 được đối chiếu với thí nghiệm Reedlunn đã công bố, với các tham số vật liệu được kế thừa. Công trình không thực hiện thí nghiệm mới và không cung cấp kiểm chứng uốn. Việc mô tả riêng hình học xoắn, tiếp xúc và ứng xử vật liệu giúp khảo sát một bài toán chi tiết hơn, nhưng mức độ chi tiết cùng chi phí tính toán không tự chứng minh khả năng dự báo tốt hơn cho bài toán khác. Khi biến đổi vật liệu và tương tác tiếp xúc cùng xuất hiện trong kết quả tổng thể, kết quả đó cũng chưa cho phép tách duy nhất phần trễ do vật liệu và phần trễ do ma sát.

- **Locator PDF trong trace:** Physical PDF M22:3; M23:3; M24:12; M25:5–6; Hysteresis synthesis; Model assumptions and limitations. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S4-R0050-A01 — mục 2.4.2.** Phạm vi đối chiếu của [21] chủ yếu là kéo dọc trục. Một đầu mẫu bị ràng buộc, đầu còn lại nhận chuyển vị hoặc tải tham chiếu chỉ theo phương trục. Mẫu thép 1×37 được so sánh với kết quả FE đã công bố; các đường kéo của mẫu SMA 1×27 và 7×7 được đối chiếu với thí nghiệm Reedlunn đã công bố, với các tham số vật liệu được kế thừa. Công trình không thực hiện thí nghiệm mới và không cung cấp kiểm chứng uốn. Việc mô tả riêng hình học xoắn, tiếp xúc và ứng xử vật liệu giúp khảo sát một bài toán chi tiết hơn, nhưng mức độ chi tiết cùng chi phí tính toán không tự chứng minh khả năng dự báo tốt hơn cho bài toán khác. Khi biến đổi vật liệu và tương tác tiếp xúc cùng xuất hiện trong kết quả tổng thể, kết quả đó cũng chưa cho phép tách duy nhất phần trễ do vật liệu và phần trễ do ma sát.

- **Locator PDF trong trace:** Physical PDF M23:3–6; M25:4–6; Model-dimensionality comparison; 2D elasticity vs3D FE. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S6-R0171-A01 — mục 2.6.3.** Về mô tả vật liệu và tiếp xúc, Vahidi và cộng sự đã kết hợp mô hình chuyển pha SMA với tiếp xúc ma sát giữa các dây trong mô phỏng phần tử hữu hạn cáp xoắn chịu kéo [21].

- **Locator PDF trong trace:** {"M25-E02": ["§2 Souza constitutive model; §4.1–4.2"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0172-A01 — mục 2.6.3.** Công trình đối chiếu với thí nghiệm đã công bố và sử dụng tham số vật liệu kế thừa [21].

- **Locator PDF trong trace:** {"M25-E06": ["§5.1–5.2; Figs.8,12; Table3"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.


## [22] B. Reedlunn, S. Daly & J. Shaw (2013), “Superelastic shape memory alloy cables: Part II – Subcomponent isothermal responses”

**CH2-S4-R0007-A01 — mục 2.4.1.** Bằng chứng phân cấp của nghiên cứu thành phần của Reedlunn và cộng sự làm rõ giới hạn này. Với 7×7, dây lõi, tao lõi 1×7 và cáp đầy đủ có đáp ứng kéo chuẩn hóa khá gần nhau do các góc xoắn nông; với 1×27, việc thêm các lớp góc xoắn sâu làm cáp mềm hơn và làm biến đổi cách chuyển pha phân bố trong cấu trúc [22, tr. 2, 7–14, 33–34]. Nghiên cứu thành phần của Reedlunn và cộng sự cũng cho thấy mô hình kéo một trục đơn giản có thể đánh giá quá cao ứng suất của đoạn nằm ngang (plateau) của một thành phần khi bỏ qua uốn và xoắn cục bộ [22, p. 18]. Vì thế, kết quả kéo của hai nghiên cứu của Reedlunn và cộng sự cung cấp bằng chứng về tương tác giữa vật liệu và kiến trúc cáp, nhưng không phải phép đo trực tiếp độ cứng uốn của bó dây thẳng MP1.

- **Locator PDF trong trace:** physical PDF pp.2–7, Abstract/Secs. 1–3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0008-A02 — mục 2.4.1.** Bằng chứng phân cấp của nghiên cứu thành phần của Reedlunn và cộng sự làm rõ giới hạn này. Với 7×7, dây lõi, tao lõi 1×7 và cáp đầy đủ có đáp ứng kéo chuẩn hóa khá gần nhau do các góc xoắn nông; với 1×27, việc thêm các lớp góc xoắn sâu làm cáp mềm hơn và làm biến đổi cách chuyển pha phân bố trong cấu trúc [22, tr. 2, 7–14, 33–34]. Nghiên cứu thành phần của Reedlunn và cộng sự cũng cho thấy mô hình kéo một trục đơn giản có thể đánh giá quá cao ứng suất của đoạn nằm ngang (plateau) của một thành phần khi bỏ qua uốn và xoắn cục bộ [22, p. 18]. Vì thế, kết quả kéo của hai nghiên cứu của Reedlunn và cộng sự cung cấp bằng chứng về tương tác giữa vật liệu và kiến trúc cáp, nhưng không phải phép đo trực tiếp độ cứng uốn của bó dây thẳng MP1.

- **Locator PDF trong trace:** physical PDF pp.12–14 and 34, Sec. 4/Conclusions. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0009-A01 — mục 2.4.1.** Bằng chứng phân cấp của nghiên cứu thành phần của Reedlunn và cộng sự làm rõ giới hạn này. Với 7×7, dây lõi, tao lõi 1×7 và cáp đầy đủ có đáp ứng kéo chuẩn hóa khá gần nhau do các góc xoắn nông; với 1×27, việc thêm các lớp góc xoắn sâu làm cáp mềm hơn và làm biến đổi cách chuyển pha phân bố trong cấu trúc [22, tr. 2, 7–14, 33–34]. Nghiên cứu thành phần của Reedlunn và cộng sự cũng cho thấy mô hình kéo một trục đơn giản có thể đánh giá quá cao ứng suất của đoạn nằm ngang (plateau) của một thành phần khi bỏ qua uốn và xoắn cục bộ [22, p. 18]. Vì thế, kết quả kéo của hai nghiên cứu của Reedlunn và cộng sự cung cấp bằng chứng về tương tác giữa vật liệu và kiến trúc cáp, nhưng không phải phép đo trực tiếp độ cứng uốn của bó dây thẳng MP1.

- **Locator PDF trong trace:** physical PDF p.18, analytical comparison. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0017-A01 — mục 2.4.1.** Bằng chứng phân cấp của nghiên cứu thành phần của Reedlunn và cộng sự làm rõ giới hạn này. Với 7×7, dây lõi, tao lõi 1×7 và cáp đầy đủ có đáp ứng kéo chuẩn hóa khá gần nhau do các góc xoắn nông; với 1×27, việc thêm các lớp góc xoắn sâu làm cáp mềm hơn và làm biến đổi cách chuyển pha phân bố trong cấu trúc [22, tr. 2, 7–14, 33–34]. Nghiên cứu thành phần của Reedlunn và cộng sự cũng cho thấy mô hình kéo một trục đơn giản có thể đánh giá quá cao ứng suất của đoạn nằm ngang (plateau) của một thành phần khi bỏ qua uốn và xoắn cục bộ [22, p. 18]. Vì thế, kết quả kéo của hai nghiên cứu của Reedlunn và cộng sự cung cấp bằng chứng về tương tác giữa vật liệu và kiến trúc cáp, nhưng không phải phép đo trực tiếp độ cứng uốn của bó dây thẳng MP1.

- **Locator PDF trong trace:** cross-study synthesis, physical PDFs cited above. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.


## [23] P. Narjabadifam et al. (2024), “Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes”

**CH2-S4-R0014-A01 — mục 2.4.1.** Nhiệt độ và tốc độ cần được tách khỏi nhau khi diễn giải. Nhiệt độ xác định pha ổn định và ứng suất chuyển pha; tốc độ tải quyết định mức độ trao đổi nhiệt trong quá trình biến dạng và có thể làm thay đổi nhiệt độ cục bộ. Hai nghiên cứu của Reedlunn và cộng sự theo dõi nhiệt độ và chọn tốc độ thấp để giữ điều kiện gần đẳng nhiệt, còn nghiên cứu của Vahidi và cộng sự dùng các đường cong vật liệu và nhiệt độ quy định trong mô phỏng. Nghiên cứu của Narjabadifam và cộng sự mô phỏng tải hình sin và kích động El Centro cho dây SMA nhưng không thực hiện phép thử NiTi độc lập, không quét nhiệt độ và không nhận dạng một định luật tốc độ [23, tr. 10–18]. Do đó, trong MP1, ảnh hưởng của nhiệt độ và tốc độ chỉ có thể được tách khi miền nhiệt–cơ và cách đo được quy định rõ; hiện tại chưa có cơ sở để gán một hệ số nhiệt hoặc hệ số tốc độ cho bó dây.

- **Locator PDF trong trace:** physical PDF pp.15–18, Secs. 3.1–3.3/Figs. 17–19. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0018-A01 — mục 2.4.1.** Nhiệt độ và tốc độ cần được tách khỏi nhau khi diễn giải. Nhiệt độ xác định pha ổn định và ứng suất chuyển pha; tốc độ tải quyết định mức độ trao đổi nhiệt trong quá trình biến dạng và có thể làm thay đổi nhiệt độ cục bộ. Hai nghiên cứu của Reedlunn và cộng sự theo dõi nhiệt độ và chọn tốc độ thấp để giữ điều kiện gần đẳng nhiệt, còn nghiên cứu của Vahidi và cộng sự dùng các đường cong vật liệu và nhiệt độ quy định trong mô phỏng. Nghiên cứu của Narjabadifam và cộng sự mô phỏng tải hình sin và kích động El Centro cho dây SMA nhưng không thực hiện phép thử NiTi độc lập, không quét nhiệt độ và không nhận dạng một định luật tốc độ [23, tr. 10–18]. Do đó, trong MP1, ảnh hưởng của nhiệt độ và tốc độ chỉ có thể được tách khi miền nhiệt–cơ và cách đo được quy định rõ; hiện tại chưa có cơ sở để gán một hệ số nhiệt hoặc hệ số tốc độ cho bó dây.

- **Locator PDF trong trace:** MP1 implication stated in prose. **Trạng thái trace:** `PROPOSAL`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.


## [24] F. Barsi, B. Carboni & W. Lacarbonara (2025), “A new mechanical model of short wire ropes: Theory and experimental validation”

**CH2-S4-R0031-A01 — mục 2.4.2.** Barsi và cộng sự [24] tiếp cận cáp xoắn ngắn bằng mô hình dầm Timoshenko tuyến tính có xét biến dạng cắt. Từng dây được mô tả như một dầm có trục cong; biến dạng riêng, hay eigenstrain, được đưa vào để giải phóng phần biến dạng của dây do độ cong gây ra theo giả thiết của từng trạng thái liên kết. Tác giả gán cùng một chế độ cho tất cả các dây trong một lần tính. Bởi vậy, các trạng thái dính hoàn toàn, dính một phần và trượt hoàn toàn là những giả thiết để đánh giá đáp ứng tương ứng. Mô hình không cập nhật diễn biến chuyển đổi giữa dính và trượt trên từng mặt tiếp xúc trong một chu kỳ tải.

- **Locator PDF trong trace:** Physical PDF M24:3–5; Secs.2–2.3; Eqs.6,11,12,18 (not reproduced). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0032-A01 — mục 2.4.2.** Khái niệm trượt phải gắn với cấp mô tả đang dùng. Trong mô hình lớp của bó dây song song, trượt được biểu diễn bằng chênh lệch chuyển vị dọc trục giữa các lớp tương đương. Với tiếp xúc giữa những dây cong trong cáp xoắn, trượt cục bộ là chuyển động tương đối theo phương tiếp tuyến tại mặt tiếp xúc. Chênh lệch chuyển vị giữa hai lớp quy đổi không cung cấp đầy đủ trường trượt trên bề mặt tiếp xúc của các dây tròn. Cũng cần phân biệt trạng thái dính, khi liên kết động học đang xét không cho phép trượt; trạng thái trượt một phần, khi chỉ một số mặt tiếp xúc hoặc một số vùng trượt; và trạng thái trượt hoàn toàn theo định nghĩa của từng mô hình. Trượt hoàn toàn không có nghĩa là mọi lực tương tác đều biến mất. Những trạng thái này mô tả quan hệ chuyển động giữa các thành phần, không đồng nghĩa với biến dạng dẻo của vật liệu dây. Đặc biệt, trạng thái dính một phần (partial stick) trong [24] là một giả thiết động học cụ thể, không phải tỷ lệ diện tích bám đo được và cũng không phải lời giải cho trượt vi mô cục bộ. Vì thế, không thể gán cùng một ngưỡng vật lý cho các trạng thái mang tên gần nhau trong các mô hình khác nhau.

- **Locator PDF trong trace:** Physical PDF M24:4–5; Sec.2.2; Eqs.11–12. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0032-A02 — mục 2.4.2.** Barsi và cộng sự [24] tiếp cận cáp xoắn ngắn bằng mô hình dầm Timoshenko tuyến tính có xét biến dạng cắt. Từng dây được mô tả như một dầm có trục cong; biến dạng riêng, hay eigenstrain, được đưa vào để giải phóng phần biến dạng của dây do độ cong gây ra theo giả thiết của từng trạng thái liên kết. Tác giả gán cùng một chế độ cho tất cả các dây trong một lần tính. Bởi vậy, các trạng thái dính hoàn toàn, dính một phần và trượt hoàn toàn là những giả thiết để đánh giá đáp ứng tương ứng. Mô hình không cập nhật diễn biến chuyển đổi giữa dính và trượt trên từng mặt tiếp xúc trong một chu kỳ tải.

- **Locator PDF trong trace:** Physical PDF M24:4–5; Sec.2.2; Eqs.11–12. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0033-A01 — mục 2.4.2.** Barsi và cộng sự [24] tiếp cận cáp xoắn ngắn bằng mô hình dầm Timoshenko tuyến tính có xét biến dạng cắt. Từng dây được mô tả như một dầm có trục cong; biến dạng riêng, hay eigenstrain, được đưa vào để giải phóng phần biến dạng của dây do độ cong gây ra theo giả thiết của từng trạng thái liên kết. Tác giả gán cùng một chế độ cho tất cả các dây trong một lần tính. Bởi vậy, các trạng thái dính hoàn toàn, dính một phần và trượt hoàn toàn là những giả thiết để đánh giá đáp ứng tương ứng. Mô hình không cập nhật diễn biến chuyển đổi giữa dính và trượt trên từng mặt tiếp xúc trong một chu kỳ tải.

- **Locator PDF trong trace:** Physical PDF M24:5; Sec.2.3; Eq.18 and following prose. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0034-A01 — mục 2.4.2.** Khác với hai mô hình lớp, [24] có thí nghiệm riêng trên các mẫu cáp thép. Tác giả thực hiện uốn gần tĩnh theo điều khiển chuyển vị ở 0,2 Hz, giữ không cho hai đầu quay và dùng cơ cấu trượt ngang để giảm sự kéo giãn mẫu. Điều kiện này không phải thí nghiệm uốn thuần túy cổ điển với mô men không đổi. Vòng trễ uốn được ghi nhận qua quan hệ lực và chuyển vị đầu mẫu. Độ dốc nhánh tăng tải thấp hơn độ dốc ở đoạn đầu nhánh dỡ tải, tạo ra hai mức độ cứng nhánh được khớp từ dữ liệu, có đơn vị kN/mm. Các độ dốc đó không phải EI của tiết diện và cũng không phải một độ cứng cát tuyến đại diện cho toàn bộ vòng trễ.

- **Locator PDF trong trace:** Physical PDF M24:5–7; Secs.3–3.1; Figs.3–5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0035-A01 — mục 2.4.2.** Khác với hai mô hình lớp, [24] có thí nghiệm riêng trên các mẫu cáp thép. Tác giả thực hiện uốn gần tĩnh theo điều khiển chuyển vị ở 0,2 Hz, giữ không cho hai đầu quay và dùng cơ cấu trượt ngang để giảm sự kéo giãn mẫu. Điều kiện này không phải thí nghiệm uốn thuần túy cổ điển với mô men không đổi. Vòng trễ uốn được ghi nhận qua quan hệ lực và chuyển vị đầu mẫu. Độ dốc nhánh tăng tải thấp hơn độ dốc ở đoạn đầu nhánh dỡ tải, tạo ra hai mức độ cứng nhánh được khớp từ dữ liệu, có đơn vị kN/mm. Các độ dốc đó không phải EI của tiết diện và cũng không phải một độ cứng cát tuyến đại diện cho toàn bộ vòng trễ.

- **Locator PDF trong trace:** Physical PDF M24:6–8; Sec.3.1; Sec.4; Fig.4b; Eq.21 (not reproduced). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0036-A01 — mục 2.4.2.** Trong đối chiếu của [24], giả thiết trượt hoàn toàn xấp xỉ mức độ cứng nhánh đo thấp hơn, còn giả thiết dính một phần gần mức độ cứng nhánh cao hơn; giả thiết dính hoàn toàn dự báo độ cứng cao quá mức rõ rệt. Cách so sánh này cho thấy tác dụng của giả thiết liên kết đối với độ cứng kết cấu. Tuy nhiên, các mức tính toán chỉ là những ước lượng theo mô hình, chưa phải các cận toán học bảo đảm cho mọi bó dây; một số ước lượng vẫn nằm ngoài khoảng đo. Ảnh hưởng của đầu mẫu và bước xoắn nổi rõ nhất đối với các đoạn cáp ngắn. Tác giả đo hình học và cho biết không hiệu chỉnh các tham số vật lý bằng cách khớp mô hình với thí nghiệm. Dữ liệu kéo và xoắn của Utting và Jones được dùng thêm cho một đối chiếu bên ngoài riêng. Dù mô hình đối chiếu được các mức độ cứng nhánh, nó chưa dự báo toàn bộ vòng trễ hoặc năng lượng tiêu tán trong chu kỳ; phần mở rộng này được tác giả để lại trong kết luận.

- **Locator PDF trong trace:** Physical PDF M24:8–11; Secs.4.1–4.3; Figs.9,11. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0037-A01 — mục 2.4.2.** Trong đối chiếu của [24], giả thiết trượt hoàn toàn xấp xỉ mức độ cứng nhánh đo thấp hơn, còn giả thiết dính một phần gần mức độ cứng nhánh cao hơn; giả thiết dính hoàn toàn dự báo độ cứng cao quá mức rõ rệt. Cách so sánh này cho thấy tác dụng của giả thiết liên kết đối với độ cứng kết cấu. Tuy nhiên, các mức tính toán chỉ là những ước lượng theo mô hình, chưa phải các cận toán học bảo đảm cho mọi bó dây; một số ước lượng vẫn nằm ngoài khoảng đo. Ảnh hưởng của đầu mẫu và bước xoắn nổi rõ nhất đối với các đoạn cáp ngắn. Tác giả đo hình học và cho biết không hiệu chỉnh các tham số vật lý bằng cách khớp mô hình với thí nghiệm. Dữ liệu kéo và xoắn của Utting và Jones được dùng thêm cho một đối chiếu bên ngoài riêng. Dù mô hình đối chiếu được các mức độ cứng nhánh, nó chưa dự báo toàn bộ vòng trễ hoặc năng lượng tiêu tán trong chu kỳ; phần mở rộng này được tác giả để lại trong kết luận.

- **Locator PDF trong trace:** Physical PDF M24:9,11; Secs.4.2–4.3; Fig.11; discussion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0038-A01 — mục 2.4.2.** Trong đối chiếu của [24], giả thiết trượt hoàn toàn xấp xỉ mức độ cứng nhánh đo thấp hơn, còn giả thiết dính một phần gần mức độ cứng nhánh cao hơn; giả thiết dính hoàn toàn dự báo độ cứng cao quá mức rõ rệt. Cách so sánh này cho thấy tác dụng của giả thiết liên kết đối với độ cứng kết cấu. Tuy nhiên, các mức tính toán chỉ là những ước lượng theo mô hình, chưa phải các cận toán học bảo đảm cho mọi bó dây; một số ước lượng vẫn nằm ngoài khoảng đo. Ảnh hưởng của đầu mẫu và bước xoắn nổi rõ nhất đối với các đoạn cáp ngắn. Tác giả đo hình học và cho biết không hiệu chỉnh các tham số vật lý bằng cách khớp mô hình với thí nghiệm. Dữ liệu kéo và xoắn của Utting và Jones được dùng thêm cho một đối chiếu bên ngoài riêng. Dù mô hình đối chiếu được các mức độ cứng nhánh, nó chưa dự báo toàn bộ vòng trễ hoặc năng lượng tiêu tán trong chu kỳ; phần mở rộng này được tác giả để lại trong kết luận.

- **Locator PDF trong trace:** Physical PDF M24:11–12; Sec.5; Sec.6 Conclusions; Table7; conclusions. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0039-A01 — mục 2.4.2.** Trong đối chiếu của [24], giả thiết trượt hoàn toàn xấp xỉ mức độ cứng nhánh đo thấp hơn, còn giả thiết dính một phần gần mức độ cứng nhánh cao hơn; giả thiết dính hoàn toàn dự báo độ cứng cao quá mức rõ rệt. Cách so sánh này cho thấy tác dụng của giả thiết liên kết đối với độ cứng kết cấu. Tuy nhiên, các mức tính toán chỉ là những ước lượng theo mô hình, chưa phải các cận toán học bảo đảm cho mọi bó dây; một số ước lượng vẫn nằm ngoài khoảng đo. Ảnh hưởng của đầu mẫu và bước xoắn nổi rõ nhất đối với các đoạn cáp ngắn. Tác giả đo hình học và cho biết không hiệu chỉnh các tham số vật lý bằng cách khớp mô hình với thí nghiệm. Dữ liệu kéo và xoắn của Utting và Jones được dùng thêm cho một đối chiếu bên ngoài riêng. Dù mô hình đối chiếu được các mức độ cứng nhánh, nó chưa dự báo toàn bộ vòng trễ hoặc năng lượng tiêu tán trong chu kỳ; phần mở rộng này được tác giả để lại trong kết luận.

- **Locator PDF trong trace:** Physical PDF M24:12; Sec.6 Conclusions; Final paragraph. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0046-A01 — mục 2.4.2.** Khái niệm trượt phải gắn với cấp mô tả đang dùng. Trong mô hình lớp của bó dây song song, trượt được biểu diễn bằng chênh lệch chuyển vị dọc trục giữa các lớp tương đương. Với tiếp xúc giữa những dây cong trong cáp xoắn, trượt cục bộ là chuyển động tương đối theo phương tiếp tuyến tại mặt tiếp xúc. Chênh lệch chuyển vị giữa hai lớp quy đổi không cung cấp đầy đủ trường trượt trên bề mặt tiếp xúc của các dây tròn. Cũng cần phân biệt trạng thái dính, khi liên kết động học đang xét không cho phép trượt; trạng thái trượt một phần, khi chỉ một số mặt tiếp xúc hoặc một số vùng trượt; và trạng thái trượt hoàn toàn theo định nghĩa của từng mô hình. Trượt hoàn toàn không có nghĩa là mọi lực tương tác đều biến mất. Những trạng thái này mô tả quan hệ chuyển động giữa các thành phần, không đồng nghĩa với biến dạng dẻo của vật liệu dây. Đặc biệt, trạng thái dính một phần (partial stick) trong [24] là một giả thiết động học cụ thể, không phải tỷ lệ diện tích bám đo được và cũng không phải lời giải cho trượt vi mô cục bộ. Vì thế, không thể gán cùng một ngưỡng vật lý cho các trạng thái mang tên gần nhau trong các mô hình khác nhau.

- **Locator PDF trong trace:** Physical PDF M22:2–3; M23:10–13; M24:4–5; Slip-definition comparison; Source definitions compared. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S5-R0020-A01 — mục §2.5.2.** Trong tài liệu về dây thép ngắn, Barsi, Carboni và Lacarbonara xây dựng mô hình dầm biến dạng cắt cho dây đơn và dây nhiều tao, với ba giả thuyết động học perfect-stick, partial-stick và full-slip. Nguồn đặt các trạng thái giới hạn vào hai phía của đáp ứng uốn và đối chiếu độ cứng cực đại, cực tiểu với thí nghiệm trên hai họ dây thép. Đây là tiền lệ gần nhất cho việc dùng trạng thái tiếp xúc để tạo giá trị tham chiếu, nhưng vật liệu, cấu trúc xoắn, chiều dài và đại lượng độ cứng của nguồn khác với bó dây TiNi MP1 [24].

- **Locator PDF trong trace:** Abstract; Secs.2–6; Figs.9–11; Table 6. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không chuyển số liệu sang TiNi; kN/mm khác B N·m².

**CH2-S5-R0021-A01 — mục §2.5.2.** Nghiên cứu của Barsi, Carboni và Lacarbonara cho thấy sự khác nhau này không chỉ là cách đặt tên. Trong mô hình của nguồn, full-slip làm các dây không còn đóng góp biến dạng cắt dây trong uốn, còn partial-stick vẫn tạo một trạng thái trung gian; ma trận quan hệ cấu thành chỉ giữ cùng dạng khi mọi dây được giả định ở cùng một trạng thái. Thí nghiệm uốn gần tĩnh trên dây R1 một tao và R2 bảy tao cho thấy full-slip dự đoán gần cận dưới, trong khi partial-stick phù hợp hơn với cận trên thực nghiệm; perfect-stick cho giá trị lớn hơn đáng kể. Vì độ cứng nguồn được biểu diễn bằng độ dốc lực–chuyển vị (kN/mm), không được đồng nhất trực tiếp với độ cứng uốn B có đơn vị N·m² [24].

- **Locator PDF trong trace:** Sec.2.2 Eq.(12), Eqs.(22–24), Discussion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Mixed-state local response không được mô tả bằng một matrix đồng nhất.

**CH2-S5-R0022-A01 — mục §2.5.2.** Nghiên cứu của Barsi, Carboni và Lacarbonara cho thấy sự khác nhau này không chỉ là cách đặt tên. Trong mô hình của nguồn, full-slip làm các dây không còn đóng góp biến dạng cắt dây trong uốn, còn partial-stick vẫn tạo một trạng thái trung gian; ma trận quan hệ cấu thành chỉ giữ cùng dạng khi mọi dây được giả định ở cùng một trạng thái. Thí nghiệm uốn gần tĩnh trên dây R1 một tao và R2 bảy tao cho thấy full-slip dự đoán gần cận dưới, trong khi partial-stick phù hợp hơn với cận trên thực nghiệm; perfect-stick cho giá trị lớn hơn đáng kể. Vì độ cứng nguồn được biểu diễn bằng độ dốc lực–chuyển vị (kN/mm), không được đồng nhất trực tiếp với độ cứng uốn B có đơn vị N·m² [24].

- **Locator PDF trong trace:** Figs.9–11; Table 6; Sec.6. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Sai số phụ thuộc chiều dài/kẹp; biến dạng hình học tăng ở biên độ lớn.

**CH2-S5-R0034-A01 — mục §2.5.2.** Nghiên cứu của Barsi, Carboni và Lacarbonara cho thấy sự khác nhau này không chỉ là cách đặt tên. Trong mô hình của nguồn, full-slip làm các dây không còn đóng góp biến dạng cắt dây trong uốn, còn partial-stick vẫn tạo một trạng thái trung gian; ma trận quan hệ cấu thành chỉ giữ cùng dạng khi mọi dây được giả định ở cùng một trạng thái. Thí nghiệm uốn gần tĩnh trên dây R1 một tao và R2 bảy tao cho thấy full-slip dự đoán gần cận dưới, trong khi partial-stick phù hợp hơn với cận trên thực nghiệm; perfect-stick cho giá trị lớn hơn đáng kể. Vì độ cứng nguồn được biểu diễn bằng độ dốc lực–chuyển vị (kN/mm), không được đồng nhất trực tiếp với độ cứng uốn B có đơn vị N·m² [24].

- **Locator PDF trong trace:** State definitions and limits. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** No local full-decoupling measurement.


## [25] K. Takashima, T. Imazawa & H. Cho (2022), “Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon”

**CH2-S4-R0067-A02 — mục 2.4.3.** Takashima và cộng sự [25] đánh giá đáp ứng công xôn bằng tải tập trung và độ dốc tuyến tính của quan hệ lực với độ võng, với chiều dài làm việc 50 mm. Độ cứng đo được tăng khi hút khí; bài báo nêu mức áp suất dưới −90 kPa nhưng không xác định rõ mốc tham chiếu của giá trị này. Áp suất trong túi không phải phép đo phân bố tải pháp tuyến tại các tiếp xúc giữa hạt. Ở trạng thái chưa kẹt, biến dạng cục bộ của màng ngoài cũng tham gia vào chuyển vị, nên độ dốc đo được không đại diện riêng cho mô đun của dây. Ước lượng dầm tuyến tính bằng cách cộng đóng góp của các phần tử trong bài báo là một đối chiếu cơ học sơ bộ, chưa phải định luật ma sát cục bộ. Các chu trình chuyển động lặp lại cho thấy ảnh hưởng của lịch sử và độ trễ, nhưng không tách riêng được đóng góp của vật liệu nhớ hình, trượt tiếp xúc, màng và sự sắp xếp hạt [25].

- **Locator PDF trong trace:** M32:3–4; Secs.2.2.1–2.2.2; Table1;construction text. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0068-A01 — mục 2.4.3.** Takashima và cộng sự [25] đánh giá đáp ứng công xôn bằng tải tập trung và độ dốc tuyến tính của quan hệ lực với độ võng, với chiều dài làm việc 50 mm. Độ cứng đo được tăng khi hút khí; bài báo nêu mức áp suất dưới −90 kPa nhưng không xác định rõ mốc tham chiếu của giá trị này. Áp suất trong túi không phải phép đo phân bố tải pháp tuyến tại các tiếp xúc giữa hạt. Ở trạng thái chưa kẹt, biến dạng cục bộ của màng ngoài cũng tham gia vào chuyển vị, nên độ dốc đo được không đại diện riêng cho mô đun của dây. Ước lượng dầm tuyến tính bằng cách cộng đóng góp của các phần tử trong bài báo là một đối chiếu cơ học sơ bộ, chưa phải định luật ma sát cục bộ. Các chu trình chuyển động lặp lại cho thấy ảnh hưởng của lịch sử và độ trễ, nhưng không tách riêng được đóng góp của vật liệu nhớ hình, trượt tiếp xúc, màng và sự sắp xếp hạt [25].

- **Locator PDF trong trace:** M32:4–5,8; Secs.2.3.2;3.1.2;3.2.2; Eq.1;Figs.16–17. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0069-A01 — mục 2.4.3.** Trong điều kiện của [25], nguyên mẫu SMA phục hồi nhanh hơn nguyên mẫu SMP nhưng chưa trở lại hoàn toàn hình dạng ban đầu. So sánh này gắn với hai kết cấu và hai loại vật liệu khác nhau nên chưa cho phép quy chênh lệch thời gian hoàn toàn cho bản chất SMA. Tác giả đề xuất phân bố cà phê không đồng đều là một nguyên nhân của phục hồi chưa hoàn toàn; đây là cách giải thích được đề xuất, chưa phải nguyên nhân duy nhất đã được đo và tách biệt. Kết quả này đặt ra một phân biệt cơ học cần giữ khi đánh giá cơ cấu điều biến ma sát: thời gian phục hồi ngắn và mức phục hồi lớn không phải cùng một tiêu chí.

- **Locator PDF trong trace:** M32:7–8; Secs.3.2.1–3.2.2; Figs.15–17. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0070-A01 — mục 2.4.3.** Takashima và cộng sự [25] đánh giá đáp ứng công xôn bằng tải tập trung và độ dốc tuyến tính của quan hệ lực với độ võng, với chiều dài làm việc 50 mm. Độ cứng đo được tăng khi hút khí; bài báo nêu mức áp suất dưới −90 kPa nhưng không xác định rõ mốc tham chiếu của giá trị này. Áp suất trong túi không phải phép đo phân bố tải pháp tuyến tại các tiếp xúc giữa hạt. Ở trạng thái chưa kẹt, biến dạng cục bộ của màng ngoài cũng tham gia vào chuyển vị, nên độ dốc đo được không đại diện riêng cho mô đun của dây. Ước lượng dầm tuyến tính bằng cách cộng đóng góp của các phần tử trong bài báo là một đối chiếu cơ học sơ bộ, chưa phải định luật ma sát cục bộ. Các chu trình chuyển động lặp lại cho thấy ảnh hưởng của lịch sử và độ trễ, nhưng không tách riêng được đóng góp của vật liệu nhớ hình, trượt tiếp xúc, màng và sự sắp xếp hạt [25].

- **Locator PDF trong trace:** M32:7–9; Secs.3.1.2;3.2.2–3.3.1; Figs.13,18–19. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

## Nhận xét audit [21]–[25]

- **[21] Vahidi et al.** Nguồn mô phỏng cáp xoắn SMA bằng mô hình vật liệu chuyển pha và tiếp xúc ma sát, nhưng đối chiếu chính chủ yếu là kéo dọc trục; không xem đó là kiểm chứng uốn bó dây MP1.
- **[22] Reedlunn et al., Part II.** Là nghiên cứu phản ứng đẳng nhiệt của các tiểu cấu phần cáp; kết quả phụ thuộc cấu trúc cáp và cấp cấu phần. Các diễn giải tổng hợp giữa Part I/II được trace phân loại inference, không phải một kết quả đơn nguồn.
- **[23] Narjabadifam et al.** Trace gắn một claim về tác động nhiệt/tốc độ và một implication đề xuất; cần giữ tách phần đo của nguồn khỏi suy luận ứng dụng cho MP1.
- **[24] Barsi et al.** Đây là nguồn gần về mô hình cơ học cáp ngắn và các giả thuyết perfect-stick/partial-stick/full-slip, kèm thử uốn riêng. Kết quả gắn với mẫu cáp thép, điều kiện biên và mô hình Timoshenko của bài; không tự động chuyển thành mô hình bó TiNi.
- **[25] Takashima et al.** Nguồn về link biến độ cứng có vật liệu nhớ hình và jamming transition; trace ghi chú áp suất dưới −90 kPa nhưng mốc tham chiếu không rõ, cần giữ bất định đó khi dùng số liệu.
- Cả năm PDF có trong thư mục tích hợp. Một số locator nêu physical PDF page, còn mã Mxx hoặc tên mục không phải số trang in; khi đối chiếu trực tiếp cần ghi đồng thời trang PDF và trang in nếu khác nhau. Excerpt trong phần này chưa được xác nhận mới trên PDF.


---

# Tiếp nối audit: tài liệu tham khảo [26]–[30]

**Phạm vi:** các claim trong bản nháp gắn [26]–[30], đối chiếu theo master traceability. Locator và excerpt/anchor dưới đây là dấu vết đã lưu để mở PDF; chưa xác nhận độc lập từng câu bằng cách đọc lại PDF trong lượt này.

| Ref | Nguồn | DOI | Claim/anchor duy nhất | PDF đóng gói |
|---:|---|---|---:|---|
| [26] | N. Matsumoto, H. Cho, K. Takashima & H. Suzuki (2024), “Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon” | 10.1299/mej.24-00130 | 8 | `26_2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf` |
| [27] | M. D. Pierce & S. A. Mascaro (2013), “A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump” | 10.1109/tmech.2012.2211032 | 11 | `27_2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf` |
| [28] | Y. Fan, D. Liu & L. Ye (2022), “A Novel Continuum Robot With Stiffness Variation Capability Using Layer Jamming: Design, Modeling, and Validation” | 10.1109/access.2022.3228775 | 2 | `28_A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf` |
| [29] | B. Yi, Y. Fan & D. Liu (2024), “A Novel Model for Layer Jamming-based Continuum Robots” | 10.1109/icra57147.2024.10610912 | 2 | `29_A Novel Model for Layer Jamming-based Continuum Robots.pdf` |
| [30] | Y. Fan, B. Yi & D. Liu (2026), “Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots” | 10.1109/tcst.2026.3690756 | 3 | `30_Modeling_Control_and_Stiffness_Regulation_of_Layer_Jamming-Based_Continuum_Robots.pdf` |

## [26] N. Matsumoto, H. Cho, K. Takashima & H. Suzuki (2024), “Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon”

**CH2-S4-R0071-A01 — mục 2.4.3.** Matsumoto và cộng sự [26] tiếp tục làm rõ sự phân biệt đó ở cấp vật liệu. Tác giả khảo sát bốn điều kiện dây Ti–Ni đường kính 0,9 mm của Furukawa và Nilaco, có lịch sử xử lý nhiệt và đặc trưng chuyển pha khác nhau. Phép đo nhiệt lượng quét vi sai (DSC) được dùng để phân loại sự xuất hiện của pha R. Nhiệt độ kết thúc chuyển sang austenit (Af) cũng khác giữa các điều kiện, vì vậy bộ mẫu chưa tạo thành một so sánh độc lập hoàn toàn giữa riêng ảnh hưởng pha R và ảnh hưởng nhiệt độ chuyển pha. Trong phép thử phục hồi tự do, đoạn dây dài 70 mm được uốn 90°, cấp điện áp 0,5 V và theo dõi đầu dây bằng camera. Đại lượng được gọi là vận tốc phục hồi là độ dốc tuyến tính khớp từ quan hệ chuyển vị phục hồi với thời gian cấp điện trong khoảng chuyển vị đến 50 mm. Đây là đại lượng suy ra từ quy trình xử lý dữ liệu, không phải vận tốc tức thời được cảm biến đo trực tiếp, tốc độ chuyển pha hay đại lượng tiếp xúc ma sát.

- **Locator PDF trong trace:** M37:2–3; Secs.1–2.1; Table1;Figs.1–2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0072-A01 — mục 2.4.3.** Matsumoto và cộng sự [26] tiếp tục làm rõ sự phân biệt đó ở cấp vật liệu. Tác giả khảo sát bốn điều kiện dây Ti–Ni đường kính 0,9 mm của Furukawa và Nilaco, có lịch sử xử lý nhiệt và đặc trưng chuyển pha khác nhau. Phép đo nhiệt lượng quét vi sai (DSC) được dùng để phân loại sự xuất hiện của pha R. Nhiệt độ kết thúc chuyển sang austenit (Af) cũng khác giữa các điều kiện, vì vậy bộ mẫu chưa tạo thành một so sánh độc lập hoàn toàn giữa riêng ảnh hưởng pha R và ảnh hưởng nhiệt độ chuyển pha. Trong phép thử phục hồi tự do, đoạn dây dài 70 mm được uốn 90°, cấp điện áp 0,5 V và theo dõi đầu dây bằng camera. Đại lượng được gọi là vận tốc phục hồi là độ dốc tuyến tính khớp từ quan hệ chuyển vị phục hồi với thời gian cấp điện trong khoảng chuyển vị đến 50 mm. Đây là đại lượng suy ra từ quy trình xử lý dữ liệu, không phải vận tốc tức thời được cảm biến đo trực tiếp, tốc độ chuyển pha hay đại lượng tiếp xúc ma sát.

- **Locator PDF trong trace:** M37:4–6; Sec.2.2;Sec.3.1; Figs.3–4,7–8. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0073-A01 — mục 2.4.3.** Các điều kiện Furukawa có pha R trong [26] có xu hướng phục hồi nhanh hơn trong bộ mẫu được xét. Tuy nhiên, nguồn dây, xử lý nhiệt và nhiệt độ chuyển pha cùng thay đổi nên kết quả chưa thiết lập một quan hệ nhân quả phổ quát rằng pha R luôn làm phục hồi nhanh hơn. Cấp điện áp không đổi cũng không duy trì nhiệt độ dây ở một giá trị đẳng nhiệt đã kiểm soát. Ở cấp cơ cấu, mẫu dùng dây có pha R phục hồi nhanh hơn nhưng dừng cách hình dạng ban đầu 10 mm, trong khi cơ cấu đối chiếu dùng dây Nilaco gần trở lại hình dạng ban đầu. Luyện chu kỳ cải thiện mức phục hồi mà không làm thay đổi rõ vận tốc phục hồi, song sự phục hồi vẫn chưa hoàn toàn [26]. Như vậy, đặc trưng pha và lịch sử vật liệu có liên quan đến đáp ứng phục hồi, nhưng chưa đủ để suy ra lực ép tiếp xúc hoặc khả năng chống trượt của một cơ cấu cụ thể.

- **Locator PDF trong trace:** M37:3,5–6; Secs.2.1;3.1; Table1;Figs.7–8. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0074-A01 — mục 2.4.3.** Các điều kiện Furukawa có pha R trong [26] có xu hướng phục hồi nhanh hơn trong bộ mẫu được xét. Tuy nhiên, nguồn dây, xử lý nhiệt và nhiệt độ chuyển pha cùng thay đổi nên kết quả chưa thiết lập một quan hệ nhân quả phổ quát rằng pha R luôn làm phục hồi nhanh hơn. Cấp điện áp không đổi cũng không duy trì nhiệt độ dây ở một giá trị đẳng nhiệt đã kiểm soát. Ở cấp cơ cấu, mẫu dùng dây có pha R phục hồi nhanh hơn nhưng dừng cách hình dạng ban đầu 10 mm, trong khi cơ cấu đối chiếu dùng dây Nilaco gần trở lại hình dạng ban đầu. Luyện chu kỳ cải thiện mức phục hồi mà không làm thay đổi rõ vận tốc phục hồi, song sự phục hồi vẫn chưa hoàn toàn [26]. Như vậy, đặc trưng pha và lịch sử vật liệu có liên quan đến đáp ứng phục hồi, nhưng chưa đủ để suy ra lực ép tiếp xúc hoặc khả năng chống trượt của một cơ cấu cụ thể.

- **Locator PDF trong trace:** M37:7; Sec.4.1; Figs.11–12. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0075-A01 — mục 2.4.3.** Các điều kiện Furukawa có pha R trong [26] có xu hướng phục hồi nhanh hơn trong bộ mẫu được xét. Tuy nhiên, nguồn dây, xử lý nhiệt và nhiệt độ chuyển pha cùng thay đổi nên kết quả chưa thiết lập một quan hệ nhân quả phổ quát rằng pha R luôn làm phục hồi nhanh hơn. Cấp điện áp không đổi cũng không duy trì nhiệt độ dây ở một giá trị đẳng nhiệt đã kiểm soát. Ở cấp cơ cấu, mẫu dùng dây có pha R phục hồi nhanh hơn nhưng dừng cách hình dạng ban đầu 10 mm, trong khi cơ cấu đối chiếu dùng dây Nilaco gần trở lại hình dạng ban đầu. Luyện chu kỳ cải thiện mức phục hồi mà không làm thay đổi rõ vận tốc phục hồi, song sự phục hồi vẫn chưa hoàn toàn [26]. Như vậy, đặc trưng pha và lịch sử vật liệu có liên quan đến đáp ứng phục hồi, nhưng chưa đủ để suy ra lực ép tiếp xúc hoặc khả năng chống trượt của một cơ cấu cụ thể.

- **Locator PDF trong trace:** M37:7–9; Sec.4.2; Figs.13–17. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0077-A02 — mục 2.4.3.** Matsumoto và cộng sự [26] tiếp tục làm rõ sự phân biệt đó ở cấp vật liệu. Tác giả khảo sát bốn điều kiện dây Ti–Ni đường kính 0,9 mm của Furukawa và Nilaco, có lịch sử xử lý nhiệt và đặc trưng chuyển pha khác nhau. Phép đo nhiệt lượng quét vi sai (DSC) được dùng để phân loại sự xuất hiện của pha R. Nhiệt độ kết thúc chuyển sang austenit (Af) cũng khác giữa các điều kiện, vì vậy bộ mẫu chưa tạo thành một so sánh độc lập hoàn toàn giữa riêng ảnh hưởng pha R và ảnh hưởng nhiệt độ chuyển pha. Trong phép thử phục hồi tự do, đoạn dây dài 70 mm được uốn 90°, cấp điện áp 0,5 V và theo dõi đầu dây bằng camera. Đại lượng được gọi là vận tốc phục hồi là độ dốc tuyến tính khớp từ quan hệ chuyển vị phục hồi với thời gian cấp điện trong khoảng chuyển vị đến 50 mm. Đây là đại lượng suy ra từ quy trình xử lý dữ liệu, không phải vận tốc tức thời được cảm biến đo trực tiếp, tốc độ chuyển pha hay đại lượng tiếp xúc ma sát.

- **Locator PDF trong trace:** M31:5–7;M32:7–8;M37:4–6; Cross-study observable comparison; Original comparison table. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S4-R0079-A01 — mục 2.4.3.** Matsumoto và cộng sự [26] tiếp tục làm rõ sự phân biệt đó ở cấp vật liệu. Tác giả khảo sát bốn điều kiện dây Ti–Ni đường kính 0,9 mm của Furukawa và Nilaco, có lịch sử xử lý nhiệt và đặc trưng chuyển pha khác nhau. Phép đo nhiệt lượng quét vi sai (DSC) được dùng để phân loại sự xuất hiện của pha R. Nhiệt độ kết thúc chuyển sang austenit (Af) cũng khác giữa các điều kiện, vì vậy bộ mẫu chưa tạo thành một so sánh độc lập hoàn toàn giữa riêng ảnh hưởng pha R và ảnh hưởng nhiệt độ chuyển pha. Trong phép thử phục hồi tự do, đoạn dây dài 70 mm được uốn 90°, cấp điện áp 0,5 V và theo dõi đầu dây bằng camera. Đại lượng được gọi là vận tốc phục hồi là độ dốc tuyến tính khớp từ quan hệ chuyển vị phục hồi với thời gian cấp điện trong khoảng chuyển vị đến 50 mm. Đây là đại lượng suy ra từ quy trình xử lý dữ liệu, không phải vận tốc tức thời được cảm biến đo trực tiếp, tốc độ chuyển pha hay đại lượng tiếp xúc ma sát.

- **Locator PDF trong trace:** M31:5–7;M37:3–4; Thermal comparability synthesis; No equation. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S4-R0079-A02 — mục 2.4.3.** Các điều kiện Furukawa có pha R trong [26] có xu hướng phục hồi nhanh hơn trong bộ mẫu được xét. Tuy nhiên, nguồn dây, xử lý nhiệt và nhiệt độ chuyển pha cùng thay đổi nên kết quả chưa thiết lập một quan hệ nhân quả phổ quát rằng pha R luôn làm phục hồi nhanh hơn. Cấp điện áp không đổi cũng không duy trì nhiệt độ dây ở một giá trị đẳng nhiệt đã kiểm soát. Ở cấp cơ cấu, mẫu dùng dây có pha R phục hồi nhanh hơn nhưng dừng cách hình dạng ban đầu 10 mm, trong khi cơ cấu đối chiếu dùng dây Nilaco gần trở lại hình dạng ban đầu. Luyện chu kỳ cải thiện mức phục hồi mà không làm thay đổi rõ vận tốc phục hồi, song sự phục hồi vẫn chưa hoàn toàn [26]. Như vậy, đặc trưng pha và lịch sử vật liệu có liên quan đến đáp ứng phục hồi, nhưng chưa đủ để suy ra lực ép tiếp xúc hoặc khả năng chống trượt của một cơ cấu cụ thể.

- **Locator PDF trong trace:** M31:5–7;M37:3–4; Thermal comparability synthesis; No equation. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.


## [27] M. D. Pierce & S. A. Mascaro (2013), “A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump”

**CH2-S4-R0089-A01 — mục 2.4.4.** Pierce và Mascaro bố trí dây SMA trong ống mềm có chất lưu nóng hoặc lạnh đi qua. Cấu hình này được gọi là cơ cấu SMA ướt vì dòng chất lưu trao đổi nhiệt trực tiếp với dây. Hai hệ bơm cho dòng nóng và lạnh gồm bình tích áp, bể chứa, buồng bơm và cơ cấu SMA; đòn bẩy chung dẫn động các buồng, còn van một chiều định hướng dòng. Nguồn gọi đây là bơm màng thể tích kiểu tịnh tiến. Chuyển kết quả sang piston cần xét lại quan hệ truyền động và tải, dù mô hình nguồn cũng sử dụng các biến chuyển động piston [27, tr. 536–538].

- **Locator PDF trong trace:** §§I–II; Figs1–3. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0090-A01 — mục 2.4.4.** Pierce và Mascaro bố trí dây SMA trong ống mềm có chất lưu nóng hoặc lạnh đi qua. Cấu hình này được gọi là cơ cấu SMA ướt vì dòng chất lưu trao đổi nhiệt trực tiếp với dây. Hai hệ bơm cho dòng nóng và lạnh gồm bình tích áp, bể chứa, buồng bơm và cơ cấu SMA; đòn bẩy chung dẫn động các buồng, còn van một chiều định hướng dòng. Nguồn gọi đây là bơm màng thể tích kiểu tịnh tiến. Chuyển kết quả sang piston cần xét lại quan hệ truyền động và tải, dù mô hình nguồn cũng sử dụng các biến chuyển động piston [27, tr. 536–538].

- **Locator PDF trong trace:** §§I–II; V.A–V.C; Figs12–13. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0090-A02 — mục 2.4.4.** Với cơ cấu dài 40 cm và thời gian cấp dòng 1,5 s, có trợ nhiệt điện và bổ sung nhiệt liên tục cho bình nóng, tác giả báo cáo tỷ số lưu lượng ra trên lưu lượng duy trì đạt 2,1, cùng khả năng cấp lưu lượng thuần 66 mL/phút. Bài báo chưa trình bày độ không đảm bảo đo riêng cho giá trị lưu lượng thuần này. Tỷ số 2,1 là tỷ số thể tích theo thời gian, không phải hiệu suất năng lượng. Ở các thử nghiệm trước bước bổ sung nhiệt liên tục, tỷ số cực đại là 0,88 khi chỉ dùng dòng nóng/lạnh và 1,54 khi có trợ điện. Vì vậy, không thể gộp các kết quả như thể cùng một điều kiện cấp năng lượng [27, tr. 544–545].

- **Locator PDF trong trace:** §§I–II; V.A–V.C; Figs12–13. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0090-A03 — mục 2.4.4.** Ở bơm SMA ướt, tăng đường kính dây giúp tăng lực nhưng làm chậm đáp ứng nhiệt; tăng chiều dài tăng khả năng tạo hành trình đồng thời tăng lượng chất lỏng cần cấp và tổn thất nhiệt. Cấp dòng quá ngắn có thể chưa đủ chuyển pha, còn quá dài làm tốn dòng sau khi co hữu ích kết thúc. Nhiệt độ chất lỏng nóng bị ràng buộc bởi điều kiện sôi, và vận hành còn cần duy trì phía lạnh. Các ảnh hưởng này được nguồn thảo luận theo cấu hình của họ, không phải hệ số hiệu chỉnh dùng chung cho piston. [27, tr. 538–545]

- **Locator PDF trong trace:** §§I–II; V.A–V.C; Figs12–13. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0091-A01 — mục 2.4.4.** Trong hệ này, một phần đầu ra được tuần hoàn để vận hành chính các cơ cấu SMA trước khi cấp cho hệ bên ngoài. Điều kiện khả thi về lưu lượng thể tích ban đầu được Pierce và Mascaro viết ở phương trình (1) của bài báo [27, tr. 538].

- **Locator PDF trong trace:** §III.A; Eq(1). **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0091-A02 — mục 2.4.4.** Trong đó, Qout là lưu lượng thể tích do bơm cung cấp trước khi trừ phần dùng nội bộ; Qin là lưu lượng thể tích cần để duy trì chấp hành của các cơ cấu SMA trong hệ. Cả hai có đơn vị m³/s và phải được xét trên cùng cơ sở thời gian. Dấu bằng là biên không còn phần dư để cấp ra ngoài; muốn có phần dư dương, lưu lượng ra phải lớn hơn lưu lượng duy trì. Đây là điều kiện cần về lưu lượng, chưa bảo đảm đầy đủ gia nhiệt, làm nguội và thắng tải. Nó không phải cân bằng năng lượng hay một định luật áp suất [27, tr. 537–538].

- **Locator PDF trong trace:** §III.A; Eq(1). **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0096-A01 — mục 2.4.4.** Với cơ cấu dài 40 cm và thời gian cấp dòng 1,5 s, có trợ nhiệt điện và bổ sung nhiệt liên tục cho bình nóng, tác giả báo cáo tỷ số lưu lượng ra trên lưu lượng duy trì đạt 2,1, cùng khả năng cấp lưu lượng thuần 66 mL/phút. Bài báo chưa trình bày độ không đảm bảo đo riêng cho giá trị lưu lượng thuần này. Tỷ số 2,1 là tỷ số thể tích theo thời gian, không phải hiệu suất năng lượng. Ở các thử nghiệm trước bước bổ sung nhiệt liên tục, tỷ số cực đại là 0,88 khi chỉ dùng dòng nóng/lạnh và 1,54 khi có trợ điện. Vì vậy, không thể gộp các kết quả như thể cùng một điều kiện cấp năng lượng [27, tr. 544–545].

- **Locator PDF trong trace:** §V.C; Figs12–13; p545. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0097-A01 — mục 2.4.4.** Với cơ cấu dài 40 cm và thời gian cấp dòng 1,5 s, có trợ nhiệt điện và bổ sung nhiệt liên tục cho bình nóng, tác giả báo cáo tỷ số lưu lượng ra trên lưu lượng duy trì đạt 2,1, cùng khả năng cấp lưu lượng thuần 66 mL/phút. Bài báo chưa trình bày độ không đảm bảo đo riêng cho giá trị lưu lượng thuần này. Tỷ số 2,1 là tỷ số thể tích theo thời gian, không phải hiệu suất năng lượng. Ở các thử nghiệm trước bước bổ sung nhiệt liên tục, tỷ số cực đại là 0,88 khi chỉ dùng dòng nóng/lạnh và 1,54 khi có trợ điện. Vì vậy, không thể gộp các kết quả như thể cùng một điều kiện cấp năng lượng [27, tr. 544–545].

- **Locator PDF trong trace:** §§V.B–V.C; Figs10–13. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0104-A02 — mục 2.4.4.** Ở bơm SMA ướt, tăng đường kính dây giúp tăng lực nhưng làm chậm đáp ứng nhiệt; tăng chiều dài tăng khả năng tạo hành trình đồng thời tăng lượng chất lỏng cần cấp và tổn thất nhiệt. Cấp dòng quá ngắn có thể chưa đủ chuyển pha, còn quá dài làm tốn dòng sau khi co hữu ích kết thúc. Nhiệt độ chất lỏng nóng bị ràng buộc bởi điều kiện sôi, và vận hành còn cần duy trì phía lạnh. Các ảnh hưởng này được nguồn thảo luận theo cấu hình của họ, không phải hệ số hiệu chỉnh dùng chung cho piston. [27, tr. 538–545]

- **Locator PDF trong trace:** §III; §IV.B; §V.B. **Trạng thái trace:** `VERIFIED FULL TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0123-A01 — mục 2.4.4.** Trong đó, Qout là lưu lượng thể tích do bơm cung cấp trước khi trừ phần dùng nội bộ; Qin là lưu lượng thể tích cần để duy trì chấp hành của các cơ cấu SMA trong hệ. Cả hai có đơn vị m³/s và phải được xét trên cùng cơ sở thời gian. Dấu bằng là biên không còn phần dư để cấp ra ngoài; muốn có phần dư dương, lưu lượng ra phải lớn hơn lưu lượng duy trì. Đây là điều kiện cần về lưu lượng, chưa bảo đảm đầy đủ gia nhiệt, làm nguội và thắng tải. Nó không phải cân bằng năng lượng hay một định luật áp suất [27, tr. 537–538].

- **Locator PDF trong trace:** §II; §III.A Eq1; §V.C. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S4-R0123-A02 — mục 2.4.4.** Với cơ cấu dài 40 cm và thời gian cấp dòng 1,5 s, có trợ nhiệt điện và bổ sung nhiệt liên tục cho bình nóng, tác giả báo cáo tỷ số lưu lượng ra trên lưu lượng duy trì đạt 2,1, cùng khả năng cấp lưu lượng thuần 66 mL/phút. Bài báo chưa trình bày độ không đảm bảo đo riêng cho giá trị lưu lượng thuần này. Tỷ số 2,1 là tỷ số thể tích theo thời gian, không phải hiệu suất năng lượng. Ở các thử nghiệm trước bước bổ sung nhiệt liên tục, tỷ số cực đại là 0,88 khi chỉ dùng dòng nóng/lạnh và 1,54 khi có trợ điện. Vì vậy, không thể gộp các kết quả như thể cùng một điều kiện cấp năng lượng [27, tr. 544–545].

- **Locator PDF trong trace:** §II; §III.A Eq1; §V.C. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.


## [28] Y. Fan, D. Liu & L. Ye (2022), “A Novel Continuum Robot With Stiffness Variation Capability Using Layer Jamming: Design, Modeling, and Validation”

**CH2-S5-R0026-A01 — mục §2.5.2.** Fan, Liu và Ye thay một robot layer-jamming bằng dầm trụ tương đương đồng nhất, dùng giả định Hooke, biến dạng nhỏ, uốn thuần và độ cứng uốn D. Các phương trình Maxwell–Mohr và độ cứng lực–chuyển vị mô tả xu hướng cấp cơ cấu; tác giả nêu D khó tính do cấu trúc phức tạp và để việc tính định lượng cho nghiên cứu sau. Nguồn không xác định trục trung hòa hoặc mô đun hiệu dụng của từng lớp, nên đây là ví dụ về phép giản lược dầm tương đương, không phải bằng chứng rằng tiết diện bó dây TiNi đã liên hợp hoàn toàn [28].

- **Locator PDF trong trace:** Sec.III Eqs.(5–19); Discussion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không chứng minh tiết diện dây TiNi liên hợp.

**CH2-S6-R0012-A01 — mục 2.6.1.** Ở cấp rôbốt liên tục, Fan và cộng sự kết hợp một trục đỡ với vỏ kẹt lớp để thay đổi đáp ứng theo phương ngang và phương dọc [28].

- **Locator PDF trong trace:** {"M14-E01": [{"pdf_page": 1, "printed_page": "130253", "section": "Abstract"}, {"pdf_page": 7, "printed_page": "130259", "section": "IV.A. Experiment Setup; IV.B. Force-Deflection Results", "figure": "Fig. 7; Fig. 8"}, {"pdf_page": 8, "printed_page": "130260", "section": "IV.B. Force-Deflection Results", "figure": "Fig. 9"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “overlap numbers n = 3, 5; external load at the transverse and axial directions are applied separately; Each experiment was repeatedly conducted five times”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.


## [29] B. Yi, Y. Fan & D. Liu (2024), “A Novel Model for Layer Jamming-based Continuum Robots”

**CH2-S5-R0068-A01 — mục §2.5.4.** Yi, Fan và Liu (2024) [29]OctRobot-I kẹt lớp; khóa hình dạng ở −30 kPa sau khi uốn 60°; Hình 3 biểu diễn độ cứng ngang trên dải áp suất âm 0–80 kPa.Mô hình điều khiển dự đoán ma trận độ cứng và quan hệ áp suất–độ cứng; thực nghiệm đọc độ cứng ngang tại cân bằng hở.Thử độ cứng lặp ba lần cùng điều kiện; Hình 3 hiển thị trung bình và ±1 độ lệch chuẩn. Ma trận độ cứng tổng thể không đo trực tiếp; giả định áp suất phân bố đều và liên hệ với lực pháp tuyến.Kiểm chứng khóa hình dạng và đáp ứng kết cấu không quan sát độc lập trạng thái tiếp xúc từng lớp, nên không chuyển trực tiếp sang cấu hình tiếp xúc MP1.

- **Locator PDF trong trace:** PDF p.5 (Fig. 3, printed 12731) and p.6 (Figs. 4–6, printed 12732); Sec. IV. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Fig. 3 range is 0–80 kPa; accepted matrix wording up to 40 kPa was not used as primary source range; no independent layer-contact observation

**CH2-S5-R0069-A01 — mục §2.5.4.** Yi, Fan và Liu (2024) [29]OctRobot-I kẹt lớp; khóa hình dạng ở −30 kPa sau khi uốn 60°; Hình 3 biểu diễn độ cứng ngang trên dải áp suất âm 0–80 kPa.Mô hình điều khiển dự đoán ma trận độ cứng và quan hệ áp suất–độ cứng; thực nghiệm đọc độ cứng ngang tại cân bằng hở.Thử độ cứng lặp ba lần cùng điều kiện; Hình 3 hiển thị trung bình và ±1 độ lệch chuẩn. Ma trận độ cứng tổng thể không đo trực tiếp; giả định áp suất phân bố đều và liên hệ với lực pháp tuyến.Kiểm chứng khóa hình dạng và đáp ứng kết cấu không quan sát độc lập trạng thái tiếp xúc từng lớp, nên không chuyển trực tiếp sang cấu hình tiếp xúc MP1.

- **Locator PDF trong trace:** PDF pp.3–5 and p.6, Assumption 3; Sec. IV. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Do not transfer contact-law calibration to MP1


## [30] Y. Fan, B. Yi & D. Liu (2026), “Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots”

**CH2-S6-R0103-A01 — mục 2.6.2.** Mô hình phát triển sau có nhận dạng tham số, đo độ cứng ngang đầu mút và thí nghiệm điều khiển cấu hình cùng độ cứng, nên giới hạn của nó không thể được mô tả là chỉ có lý thuyết [30].

- **Locator PDF trong trace:** {"M16-E04": ["SectionIV.D.5 sheath selection p9–10; V.A–C; Fig7 p11"], "M16-E05": ["SectionIV.D.1–3; Eqs47–49 p9; SectionV.D p11–12; Fig8 p12"], "M16-E06": ["SectionV.E; Figs9–10; TablesI–II"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “jamming sheath with two layers; maximum vacuum pressure of 40 kPa; with respect to the value (uP )1/2”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0180-A01 — mục 2.6.3.** Ở cấp mô hình giảm bậc, Fan và cộng sự đã cho phép tác động áp suất và hệ số đàn hồi phụ thuộc áp suất trong hệ kẹt lớp chân không, có nhận dạng tham số cùng thí nghiệm điều khiển cấu hình và độ cứng [30].

- **Locator PDF trong trace:** {"M16-E02": ["§II; Eqs.(1)–(15),§III Proposition2 Eq.(17)"], "M16-E04": ["§V-C Fig.7; §V-D identification"], "M16-E06": ["§V-E; Figs.9–10 TablesI–II"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0244-A01 — mục 2.6.4.** Việc đánh giá mô hình cũng phải phân biệt nhận dạng với kiểm chứng dự đoán: Fan và cộng sự đã dùng dữ liệu độ cứng để nhận dạng quan hệ phụ thuộc áp suất, sau đó thực hiện các thí nghiệm điều khiển cơ cấu kẹt lớp dưới chân không [30].

- **Locator PDF trong trace:** {"M16-E02":[{"physical_pages":[4],"printed_pages":["2222"],"exact_locator":"II.A continued; II.B Key Assumptions and Frictional Model With LJ","anchor":"additional input"},{"physical_pages":[5],"printed_pages":["2223"],"exact_locator":"II.B continued; Assumptions3 and4","anchor":"uniformly distributed"}],"M16-E04":[{"physical_pages":[10],"printed_pages":["2228"],"exact_locator":"V. Experiments and Results, A. Test Rig; Fig.5","anchor":"pressure gauge"},{"physical_pages":[11],"printed_pages":["2229"],"exact_locator":"V.C Open-Loop Stiffening; Fig.7; V.D Parameter Identification starts","anchor":"better ﬁtting performance"},{"physical_pages":[12],"printed_pages":["2230"],"exact_locator":"V.D continued; V.E Closed-Loop Control Experiments; Fig.8; TableI","anchor":"By ﬁtting the stiﬀness data"}],"M16-E06":[{"physical_pages":[12],"printed_pages":["2230"],"exact_locator":"V.D continued; V.E Closed-Loop Control Experiments; Fig.8; TableI","anchor":"By ﬁtting the stiﬀness data"},{"physical_pages":[13],"printed_pages":["2231"],"exact_locator":"V.E continued; Figs.9/10; TableII","anchor":"closed-loop stiﬀness"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.

## Nhận xét audit [26]–[30]

- **[26] Matsumoto et al.** So sánh các dây Ti–Ni có nguồn và xử lý nhiệt khác nhau; kết quả về tốc độ hồi phục/pha R chỉ áp dụng cho bộ mẫu và điều kiện thí nghiệm. Trace đánh dấu một số kết luận so sánh liên nghiên cứu là `INFERENCE`.
- **[27] Pierce & Mascaro.** Là bơm SMA ướt trao đổi nhiệt qua chất lưu, với tuần hoàn nội bộ và điều kiện thử cụ thể. Lưu lượng thuần/đầu ra không phải áp suất tại mẫu cơ học khác; phương trình cân bằng lưu lượng là quan hệ hệ thống theo nguồn.
- **[28] Fan et al. (2022).** Mô hình hóa layer-jamming continuum robot bằng dầm tương đương với giả thiết tuyến tính/biến dạng nhỏ; đây là mô hình hệ khác. Trace lưu một claim về mô hình/độ cứng và một claim về cấu trúc robot.
- **[29] Yi et al. (2024).** Mô hình/điều khiển robot layer-jamming với phép đo độ cứng ngang và lock-shape trong điều kiện nêu ở trace. Không suy thành kiểm chứng mô hình ứng suất/trượt của bó dây TiNi.
- **[30] Fan et al. (2026).** Nguồn gần về mô hình giảm bậc, tham số phụ thuộc áp suất, nhận dạng và kiểm chứng điều khiển cho layer jamming. Vì đây là đối chiếu gần, các claim về nhận dạng và thí nghiệm phải được đọc cùng nhau; không mô tả nguồn là “chỉ lý thuyết”. Cấu hình layer jamming vẫn khác đối tượng bó dây MP1.
- Cả năm PDF có trong thư mục tích hợp. Các mục [26]–[27] thường ghi mã trang nội bộ hoặc section; [28]–[30] có một số page locator. Excerpt và page chưa được xác minh trực tiếp mới trên PDF trong lượt này.
