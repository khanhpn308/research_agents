# Báo cáo thực thi §2.4.4

TASK_ID: MP1-CH2-2.4.4-RESEARCH-THESIS-DRAFT  
STATUS: PARTIAL_WITH_FINDINGS  
TARGET_SECTION: 2.4.4 — SMA–piston và truyền áp suất  
ACADEMIC_CONTEXT: HCMUT–VNU-HCM; Khoa Cơ khí; Thạc sĩ Kỹ thuật Cơ khí, định hướng nghiên cứu chuyên sâu  
DRAFT_LANGUAGE: VIETNAMESE_ONLY; phụ lục song ngữ và tên tài liệu gốc theo yêu cầu  
ROOT_MODEL_REQUESTED: GPT-6.1 SOL HIGH  
ROOT_MODEL_ACTUAL: Không có định danh backend/telemetry để xác minh; phiên Codex hiện tại được mô tả là dựa trên GPT-6  
WORKERS_SPAWNED: 5 agent; 7 lượt phân công vai trò  
WORKER_TASKS: Kiểm tra M12; kiểm tra M33; kiểm tra M34; soạn tiếng Việt; thuật ngữ; tạo DOCX; QA độc lập  
WORKER_MODELS_REQUESTED: GPT-6.1 SOL MEDIUM; GPT-6 LUNA  
WORKER_MODELS_ACTUAL: Tham số gọi: gpt-6.1-sol/medium cho verify_m12, verify_m33, terminology; gpt-6-luna/medium cho verify_m34 và qa. Backend thực không được cung cấp để xác minh.  
PARALLEL_EXECUTION: Có: 3 worker nguồn ban đầu chạy song song; soạn/thuật ngữ và chuẩn bị DOCX chạy có giới hạn. Chỉ một người ghi DOCX tại từng thời điểm.  
OUTLINE_BULLETS_COVERED: 2.4.4-B01; 2.4.4-B02, đã đối chiếu nguyên văn CSV  
PAPERS_READ: M12; M33; M34; ba PDF gốc địa phương  
PDF_PAGES_VERIFIED: Locators dùng: M12 trang vật lý2–4,6–9; M33 trang1–4,8–11; M34 trang3–5,8–12; metadata trang1 mỗi bài. Trang ảnh/chi tiết kiểm tra ghi trong QA.  
EVIDENCE_IDS_USED: M12-E01; M33-E01; M33-E02; M34-E02; trang mở rộng ghi riêng, không tạo/sửa Evidence Record  
M12_PRESSURE_FUNCTIONS: Áp âm tạo kẹt hạt; áp dương tạo uốn; ECF, không phải SMA. Áp trong cơ cấu không đo trực tiếp.  
M33_WET_SMA_PUMP: SMA trong ống mềm có dòng nóng/lạnh, đòn bẩy và buồng bơm màng, bình tích/van một chiều; có cấp nhiệt và trợ điện.  
M33_EQUATIONS_VERIFIED: (1)–(4), trang vật lý3/trang in538; ROOT nhìn ảnh độc lập; chỉ(1) được đưa vào DOCX.  
M33_DIMENSIONAL_CHECK: (1) lưu lượng cùng đơn vị; (2),(3) m³/s; (4) không thứ nguyên. Điều kiện cần, không đủ.  
M33_PUBLICATION_METADATA: Online20/8/2012; currentversion10/1/2013; tập18,số2,tháng4/2013,tr.536–546. Không sửa registry2012.  
M34_COIL_ENCLOSURE_MECHANISM: Lò xo NiTi nén vỏ silicone khi nóng; vỏ hồi phục khi nguội. Cân bằng giao điểm khác chênh lực dẫn động; mô hình hai đầu pha.  
FORCE_STROKE_TEMPERATURE: Phân biệt hành trình tự do, lực khóa, hành trình chịu tải; cực đại không đồng thời; giữ pha/nhiệt/lịch sử và tải.  
VOLUME_PRESSURE_COUPLING: Biên chuyển động đổi thể tích; khung piston có điều kiện chỉ diễn giải bằng lời, không tạo luật MP1.  
SEAL_FRICTION_EVIDENCE: ENGINEERING_CONSIDERATION; ba nguồn không định lượng phớt piston MP1.  
COMPLIANCE_AND_LEAKAGE_EVIDENCE: Nguồn nêu độ mềm PDMS/silicone và van tiền ép hạn chế rò; không có hệ số rò/độ mềm hệ MP1.  
PRESSURE_TRANSIENT_EVIDENCE: Nguồn có đầu ra theo thời gian và giới hạn nhiệt; không có hàm truyền hoặc thời hằng áp suất MP1.  
COOLING_LIMITATIONS: Dòng lạnh/hồi lực của SMA ướt; đánh đổi tản nhiệt–gia nhiệt–hành trình của capsule; không chuyển thời hằng.  
SOURCE_TO_SPECIMEN_PRESSURE: Tách biến, vị trí và mốc tham chiếu; không giả sử bằng nhau.  
LOCAL_CONTACT_TRACTION: Không nhận dạng duy nhất từ áp suất hoặc đường uốn toàn cục; Pa khác lựcN và hệ số ma sát không thứ nguyên.  
MP1_MODEL_TRANSFER: Không được kiểm chứng; không có luật áp suất–ma sát–độ cứng hoặc thiết kế piston được chốt.  
SOURCE_GROUNDED_CLAIMS: 20  
INFERENCE_CLAIMS: 14  
AUTHOR_PROPOSAL_CLAIMS: 3  
DOCUMENT_COVERAGE_RECORDS: 2  
TOTAL_TRACEABILITY_RECORDS: 39  
CROSS_STUDY_SYNTHESIS: So sánh cơ cấu kích hoạt–biên chuyển động–đường lực/áp suất–đại lượng–miền kiểm chứng; không gộp cực đại/hiệu suất.  
TABLES: 2 bảng Word: 1 bảng so sánh3nghiên cứu và1phụ lục30thuật ngữ  
FIGURES: 0; không sao chép hình nguồn  
EQUATIONS: 1 OMML: Q_out ≥ Q_in từ M33(1); (2)–(4) bỏ khỏi DOCX, giữ kiểm toán trong QA/CSV  
CITATIONS: 3 danh tính/3DOI; [1]–[3] theo lần xuất hiện đầu; không kế thừa số từ baseline  
TERMINOLOGY_ENTRIES: 30  
TERMINOLOGY_REVIEW_REQUIRED: 0 mục chưa duyệt nội dung trong phạm vi này; vẫn cần rà bố cục và hợp nhất glossary ở bước biên tập toàn luận văn  
GATE_1: PASS (bounded)  
GATE_2: PASS (bounded)  
GATE_3: PASS (equations1–4 only)  
GATE_4: PASS  
GATE_5: PASS  
GATE_6: PASS (2012online/2013issue reconciled)  
GATE_7: PARTIAL (science/staticPASS; visual layout unverified)  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: NOT_VERIFIED  
DOCX_PATH: outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx  
TRACEABILITY_PATH: outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv  
TERMINOLOGY_PATH: outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv  
QA_REPORT_PATH: outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md  
EXECUTION_REPORT_PATH: outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md  
UNRESOLVED_LIMITATIONS: Thiếu kết xuất Word; mốc/vị trí áp suất nguồn chưa đầy đủ; số66 không có bất định đo riêng; không có dữ liệu phớt/rò/tiếp xúc MP1; mô hình M34 bỏ trạng thái trung gian.  
NEXT_ACTION: Rà từng trang DOCX trong Word/LibreOffice trước tích hợp; không tự tiếp tục §2.5/§2.6 hoặc thay đổi thiết kế/nghiên cứu.  

## Phạm vi, trình tự và quyền ghi

Thực hiện độc lập với phiên §2.4.3. Không đọc hoặc sửa thư mục §2.4.3. Chỉ tạo đúng năm tệp cuối trong thư mục §2.4.4; dữ liệu tạm có tiền tố riêng `/tmp/mp1-244-eSeD0F/`. Không commit, push, checkout, đổi nhánh, reset hoặc thay đổi cấu hình chung. Không sửa mã nguồn, script dùng chung, WEP, PDF, registry, trạng thái khoa học hoặc baseline. Đã đọc baseline §2.3 tích hợp, §2.4.1 và §2.4.2 để giữ phân biệt vật liệu/kết cấu, áp nguồn/tiếp xúc và hiệu chỉnh/kiểm chứng. Hash của 30 tệp đầu vào được ghi trước khi soạn và kiểm tra lại không đổi.

Quy trình đã hoàn tất: kiểm tra đầu vào; đọc brief/crosswalk/source matrix; kiểm tra bốn Evidence ID; ba worker nguồn song song; ROOT kiểm tra phương trình độc lập; hòa giải cơ chế và phê duyệt lập luận; soạn tiếng Việt; ROOT sửa lập luận/thuật ngữ; tạo DOCX; QA độc lập có giới hạn; kiểm tra tĩnh và bảy cổng; ghi hai báo cáo cuối. Không có bộ kết xuất nên bước nhìn từng trang được giữ NOT_VERIFIED.

## Phân công và provenance mô hình

| Agent | Tham số mô hình yêu cầu khi gọi | Công việc đã thực hiện |
|---|---|---|
| verify_m12 | gpt-6.1-sol, medium | Kiểm tra M12, sau đó soạn bản nháp theo lập luận ROOT đã duyệt. |
| verify_m33 | gpt-6.1-sol, medium | Kiểm tra SMA ướt, số đo và (1)–(4). |
| verify_m34 | gpt-6-luna, medium | Kiểm tra M34, sau đó tạo bộ dựng DOCX và sinh DOCX sau phê duyệt ROOT. |
| terminology | gpt-6.1-sol, medium | 30 ứng viên thuật ngữ; ROOT đối chiếu tất cả với văn bản cuối và duyệt. |
| qa | gpt-6-luna, medium | Vai trò QA độc lập, kiểm tra nguồn trọng yếu và ZIP/XML. |

Các tên mô hình trên là tham số đã gửi công cụ, không phải telemetry của backend. Agent chỉ tự nhận được định danh chung Codex dựa trên GPT-6. Không tuyên bố một backend cụ thể đã chạy khi runtime không cung cấp xác nhận. ROOT giữ trách nhiệm quyết định khoa học, sửa nội dung và chấp nhận cuối; không xem kết quả nhiều vai trò là bằng chứng thực nghiệm độc lập.

## Cơ sở khoa học đã chốt

B01 được kiểm tra nguyên văn: “Tổng hợp tiền lệ SMA tạo chuyển vị hoặc áp suất qua piston, pump hoặc chamber.” B02 được kiểm tra nguyên văn: “Phân tích force–stroke–temperature–volume, seal friction, compliance, leakage, pressure transient và cooling.” Brief nhận trạng thái BOUNDED_WRITING_READY. Ánh xạ kiểm tra đúng 2.4.4-A01→M12-E01, A02→M33-E01, A03→M34-E02, A04→M33-E02. B03 có trong CSV tổng thể nhưng không được dùng để đưa protocol Bench B vào mục này.

Lập luận ROOT chấp nhận gồm các bước điện/nhiệt→pha SMA→lực/hành trình chịu tải→biên chuyển động→thể tích→áp suất nguồn→truyền tới mẫu. Phần tiếp xúc, ma sát và uốn là các liên kết cần bằng chứng riêng. Phần tổng quan so sánh chức năng và miền kiểm chứng thay vì suy tất cả thiết bị thành cùng một piston. Các ảnh/đoạn nguồn và kiểm tra phương trình được tóm tắt đầy đủ trong báo cáo bảy cổng; không để kết luận quan trọng chỉ nằm ở báo cáo tạm của worker.

M12 là ví dụ ECF, không phải SMA. M33 là hệ SMA ướt cần dòng duy trì và cấp năng lượng; tỷ số2,1 không phải hiệu suất. M34 là lò xo–vỏ mềm với mô hình hai đầu pha, không nhận dạng toàn quỹ đạo nén. Không nguồn nào kiểm chứng trọn chuỗi MP1. Các yêu cầu đo lường ở cuối là đề xuất có giới hạn; không chọn piston, phớt, môi chất, duty cycle hoặc bộ cảm biến.

## Phương trình, số liệu và trích dẫn

ROOT đã nhìn ảnh trang vật lý3 của M33 và kiểm tra dạng phân số, dấu, chỉ số của(1)–(4). Biến và đơn vị cùng giả định, vai trò cần/chưa đủ và hạn chế thực nghiệm đều có trong QA. Chỉ(1) vào DOCX vì làm rõ chênh lệch dòng bơm ra với dòng duy trì. (2)–(4) không cần cho lập luận và quá đặc thù hệ SMA ướt; không chuyển ràng buộc lưu lượng sang luật áp suất–ma sát. Không thêm phương trình piston hay luật MP1. Các nhóm phương trình khác không được đánh dấu đã kiểm chứng.

Giá trị dùng: M12 0,134→0,743N tại3mm và0,5mm/s, áp danh định−50kPa từ phép bơm riêng; M33 tỷ số0,88/1,54 ở thử trước bổ sung nhiệt và2,1/capability thuần66mL/phút ở chế độ được nêu; M34 bơm3vòng,43mm³,790mA,6,5kPa. Mỗi số có locator và giới hạn riêng trong CSV/QA. Không đưa cực đại14kPa của M34 hoặc cực đại áp/lưu lượng bơm riêng M12 vào phép tính MP1.

Ba mục tham khảo dùng đúng ba DOI gốc và thứ tự tác giả trên PDF. M33 được hòa giải online2012/số báo2013 thay vì sửa registry. Tên nguồn giữ ngôn ngữ gốc; văn bản khoa học và định nghĩa tiếng Việt. Tất cả30 nhãn thuật ngữ xuất hiện trong phần văn bản đã duyệt, gồm5 mục mô tả có nguồn trực tiếp và25 định nghĩa biên tập. Định nghĩa biên tập không giả gán cho tác giả nguồn. CSV giữ nghĩa, ngữ cảnh, locator, giới hạn và trạng thái duyệt; phần Word bỏ mã nội bộ.

## Diễn giải số lượng traceability

20 SOURCE_GROUNDED_CLAIM;14 INFERENCE;3 AUTHOR_PROPOSAL;2 DOCUMENT_COVERAGE, tổng39. Đây là số hồ sơ truy xuất, không phải39 kết quả độc lập. Bao gồm ba dòng phương trình không đưa vào DOCX, một dòng kiểm tra thứ nguyên, một dòng metadata và một dòng giải thích glossary. Bản đồ neo dưới đây giúp đọc CSV mà không cần tệp JSON tạm. Nội dung exact_scientific_claim và locator vẫn là căn cứ chính.

| Neo biên tập | Loại | Phần đầu nội dung trong DOCX |
|---|---|---|
| b01 | heading | Từ kích thích nhiệt đến tải cơ học |
| b02 | paragraph | Nguồn áp suất dẫn động bằng hợp kim nhớ hình, gọi tắt là SMA, cần được xét theo từng bước chuyển đổi năng lượng. Đầ |
| b03 | paragraph | Huynh và cộng sự cho thấy cùng một nguồn áp suất có thể phục vụ hai chức năng khác nhau. Vi bơm dùng chất lưu điện  |
| b04 | paragraph | Tác giả khảo sát vi bơm riêng vì không đo trực tiếp được áp suất trong cơ cấu đã lắp. Trong phép thử công xôn, đầu  |
| b05 | heading | Điều kiện thể tích của bơm dùng SMA |
| b06 | paragraph | Pierce và Mascaro bố trí dây SMA trong ống mềm có chất lưu nóng hoặc lạnh đi qua. Cấu hình này được gọi là cơ cấu S |
| b07 | paragraph | Trong hệ này, một phần đầu ra được tuần hoàn để vận hành chính các cơ cấu SMA trước khi cấp cho hệ bên ngoài. Điều  |
| b08 | equation | Q_out ≥ Q_in |
| b09 | paragraph | Trong đó, Q_out là lưu lượng thể tích do bơm cung cấp trước khi trừ phần dùng nội bộ; Q_in là lưu lượng thể tích cầ |
| b10 | paragraph | Với cơ cấu dài 40 cm và thời gian cấp dòng 1,5 s, có trợ nhiệt điện và bổ sung nhiệt liên tục cho bình nóng, tác gi |
| b11 | heading | Lực hồi phục và biến thiên thể tích buồng |
| b12 | paragraph | Kotb, Elgamal và Serry dùng lò xo SMA bằng NiTi cuốn quanh vỏ silicone đàn hồi. Gia nhiệt Joule làm lò xo co, nén b |
| b13 | paragraph | Đồ thị lực–chuyển vị của tác giả mô tả vị trí cân bằng bằng giao điểm đường lực của lò xo và vỏ. Khi pha SMA thay đ |
| b14 | paragraph | Mô hình của công trình chỉ tìm hai đầu hành trình với giả định austenit hoàn toàn khi nóng và martensit hoàn toàn k |
| b15 | paragraph | Trong một chế độ điều khiển của bơm ba vòng, tác giả đặt thể tích đẩy mục tiêu 43 mm³ mỗi hành trình và dòng cực đạ |
| b16 | paragraph | So sánh trên cùng đường truyền cơ học cho thấy ECF tạo dòng bằng điện trường, SMA ướt kéo cơ cấu truyền động tới bu |
| comparison | comparison | Bảng so sánh ba nghiên cứu |
| b18 | heading | Điều kiện để xét cơ cấu piston |
| b19 | paragraph | Hành trình tự do, lực khóa khi chặn chuyển vị và hành trình chịu tải là các đặc trưng ở những điều kiện biên khác n |
| b20 | paragraph | Với một piston giả định có biên cứng, diện tích piston hữu hiệu đã biết, không rò và chuyển động gần tĩnh, có thể d |
| b21 | paragraph | Đó là khung cơ học có điều kiện, chưa phải quan hệ đã được nhận dạng cho MP1. Lực có đơn vị N, hành trình có đơn vị |
| b22 | heading | Các tổn thất và sự phụ thuộc lịch sử |
| b23 | paragraph | Các giới hạn có bằng chứng trong nguồn phải được phân biệt với yếu tố cần xét cho cơ cấu mới. Huynh và cộng sự ghi  |
| thermal_limits | paragraph | Ở bơm SMA ướt, tăng đường kính dây giúp tăng lực nhưng làm chậm đáp ứng nhiệt; tăng chiều dài tăng khả năng tạo hàn |
| b24 | paragraph | Đối với piston dự kiến, ma sát phớt, độ rơ truyền động và hành trình mất là các yếu tố kỹ thuật cần xét nếu cấu hìn |
| b25 | paragraph | Trong bơm của Kotb và cộng sự, van lá được tạo tiền ép để hạn chế rò theo mô tả thiết kế. Chi tiết này không phải p |
| b26 | paragraph | Lịch sử nhiệt và tải cần đi cùng trạng thái làm việc khi diễn giải đáp ứng. Thời gian chuyển pha SMA, thời gian làm |
| b27 | heading | Từ đầu ra nguồn tới đáp ứng của mẫu |
| b28 | paragraph | Cần phân biệt áp suất nguồn hoặc áp suất buồng tạo áp, áp suất tại mẫu và ứng suất tiếp xúc pháp tuyến tại giao diệ |
| pressure_reference | paragraph | Dấu âm hoặc dương cần được hiểu so với một mốc áp suất được chỉ rõ. Ở công trình Huynh, các nhãn âm/dương phân biệt |
| b29 | paragraph | Để đánh giá một nguồn SMA–piston trong tương lai, luận văn đề xuất xem xét riêng đầu vào điện hoặc nhiệt và nhiệt đ |
| b30 | paragraph | Các tiền lệ đã cho thấy khả năng ghép lực, hành trình và lưu chất bằng SMA trong những thiết bị cụ thể; vi bơm ECF  |


## Kiểm tra đầu ra và giới hạn trình bày

DOCX mở lại được bằng python-docx và ZIP/XML hợp lệ. Có2 bảng gốc,4 hàng so sánh/31 hàng glossary,35 cantSplit,2 tiêu đề bảng lặp,1OMML với2 chỉ số dưới,3 đoạn tham khảo giữ nguyên đoạn, trường số trang và1ngắt trang trước phụ lục. Các tiêu đề phụ đã được sửa thành Heading2,12pt; Heading1 chỉ dùng cho tiêu đề mục14pt. Chỉ số Qout/Qin cũng dùng Word subscript trong phần định nghĩa và glossary, không để dấu gạch dưới hiển thị.

Không thể kết luận PASS về số trang, bảng tràn hoặc mục glossary đơn lẻ bằng XML. Không có Word/LibreOffice/soffice để kết xuất; việc có pdftoppm không giải quyết chuyển DOCX sang PDF. Vì thế GATE7=PARTIAL, WORD_RENDER_VALIDATION=NOT_VERIFIED và STATUS=PARTIAL_WITH_FINDINGS. Không tuyên bố chuẩn định dạng chính thức HCMUT.

Các kỹ năng được áp dụng theo hợp đồng mục luận văn do người dùng chỉ định: academic-paper để giữ cấu trúc luận cứ/chứng cứ và liêm chính trích dẫn; academic-humanizer và unslop để sửa giọng văn cơ khí, bỏ đệm và hạ khẳng định về đúng mức bằng chứng. Bản thảo được ROOT sửa trước khi sinh DOCX, gồm bỏ glossary nháp trùng, thay giả định chất lỏng bằng chất lưu trong MP1, tách giao điểm cân bằng/chênh lực, sửa nghĩa hiệu chuẩn và tách kiểm chứng độc lập. Không thêm tuyên bố/abstract của một bài báo toàn văn vào mục luận văn.

## Dấu vết tệp cuối

DOCX SHA-256: `0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376`  
DOCX size: 49106 bytes.

| Tệp | Trạng thái | SHA-256 |
|---|---|---|
| [MP1_CH2_2_4_4_DRAFT.docx](MP1_CH2_2_4_4_DRAFT.docx) | Đã ghi, không rỗng, mở lại | `0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376` |
| [MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv](MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv) | Đã ghi, không rỗng, mở lại | `49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550` |
| [MP1_CH2_2_4_4_TERMINOLOGY.csv](MP1_CH2_2_4_4_TERMINOLOGY.csv) | Đã ghi, không rỗng, mở lại | `a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7` |
| [MP1_CH2_2_4_4_7_GATE_REVIEW.md](MP1_CH2_2_4_4_7_GATE_REVIEW.md) | Đã ghi, không rỗng, mở lại | `675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff` |

Báo cáo thực thi là tệp thứ năm; không ghi hash tự tham chiếu. Các PDF gốc giữ SHA-256 đã có trong từng dòng nguồn CSV. Dữ liệu nguồn, trạng thái khoa học và các baseline không bị cập nhật.


## Đóng QA và giới hạn còn lại

QA độc lập xác nhận khoa học và cấu trúc tĩnh; ROOT giữ GATE7 PARTIAL vì chưa nhìn trang kết xuất. Đề xuất đảo M33-E01/E02 của QA đã được rút sau khi đối chiếu JSONL canonical dòng17–18 và source matrixA02/A04. Lỗi nằm ở tiêu đề báo cáo tạm worker; ánh xạ trong deliverable từ đầu tuân đúng nguồn có thẩm quyền. Locator accepted-record đã được làm riêng theo record và loại trùng; source locator phần Word không chứa ghi chú PDF nội bộ. Các cập nhật này không thay đổi lập luận khoa học hoặc Evidence Record.

Đã mở lại cả năm tệp, xác nhận không rỗng và có phần bắt buộc. ROOT kiểm tra lại DOCX sau lần sửa nhãn trang glossary cuối, cùng hash dữ liệu đầu vào. Giới hạn chưa giải quyết là bố cục kết xuất, mốc/vị trí lấy áp chưa đủ trong nguồn và dữ liệu phớt/rò/tiếp xúc MP1 chưa có. Không có bước tiếp theo được thực thi ngoài đúng năm deliverable.
