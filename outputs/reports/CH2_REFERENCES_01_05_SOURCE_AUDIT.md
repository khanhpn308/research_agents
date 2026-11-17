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

