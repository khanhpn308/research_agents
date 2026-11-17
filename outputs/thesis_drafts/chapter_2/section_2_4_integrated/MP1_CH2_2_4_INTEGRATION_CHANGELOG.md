# Nhật ký tích hợp mục 2.4

TASK_ID: MP1-CH2-2.4-INTEGRATION-AND-CONSISTENCY-REVIEW  
STATUS: PARTIAL_WITH_FINDINGS  
Ngày: 18/10/2026, Asia/Bangkok.

## Mục tiêu và phạm vi bằng chứng

Tích hợp bốn bản thảo hiện hữu cho luận văn Thạc sĩ Kỹ thuật Cơ khí, định hướng nghiên cứu chuyên sâu, Khoa Cơ khí, Trường Đại học Bách khoa, Đại học Quốc gia Thành phố Hồ Chí Minh. Chủ đề làm việc là "Đặc trưng độ cứng uốn của bó dây TiNi dưới ma sát điều khiển bằng áp suất dương từ piston dẫn động bằng lò xo SMA". Không viết lại toàn bộ tổng quan, tìm bài mới, tái trích xuất toàn bộ PDF, thiết kế thí nghiệm hay thay trạng thái nghiên cứu.

`VERIFIED FULL TEXT` trong hồ sơ nhận định là trạng thái kế thừa từ các CSV gốc. Lần này đối chiếu trực tiếp định danh DOI 13 nguồn trên PDF, metadata có xung đột và phương trình thực sự được giữ; không tái kiểm chứng toàn bộ kết quả của 13 nghiên cứu. `METADATA ONLY` không chứng minh cơ chế; `INFERENCE` là tổng hợp hoặc diễn giải. Mọi quyết định khoa học thuộc ROOT. Vai trò agent không tạo bằng chứng thực nghiệm độc lập.

## Kiểm kê và trạng thái chấp nhận đầu vào

Đủ 20/20 tệp, mỗi tiểu mục có DOCX, truy xuất, thuật ngữ, báo cáo bảy cổng và thực thi. Đã đọc cả bốn cặp báo cáo trước hợp nhất; không nâng trạng thái gốc.

| Tiểu mục | Chấp nhận ghi trong hồ sơ gốc | Giới hạn được giữ |
|---|---|---|
| 2.4.1 | PARTIAL_WITH_FINDINGS; cổng 1 và 7 PARTIAL; bản R2 | Cơ sở soạn thảo được chấp nhận có giới hạn nhiệt độ/tốc độ; kéo gần đẳng nhiệt không xác lập luật nhiệt/tốc độ hay trạng thái MP1. Render độc lập chưa xác minh. |
| 2.4.2 | PARTIAL_WITH_FINDINGS; cổng 1 và 7 PARTIAL | Bện/bao được phân biệt theo hình học, không có kiểm chứng chuyên biệt; M22/M23 cùng tuyến Chen; đơn vị k_i M23 chưa xác minh; cáp thép/cáp xoắn không là MP1. |
| 2.4.3 | PARTIAL_WITH_FINDINGS; cổng 1–6 PASS có giới hạn, cổng 7 PARTIAL | Hồ sơ ghi nhận rà soát DOCX độc lập; giao diện dây–cao su, lực kéo không tách tải pháp tuyến/hệ số ma sát; không suy pha R của MP1. |
| 2.4.4 | PARTIAL_WITH_FINDINGS; cổng 1–6 PASS trong phạm vi nêu, cổng 7 PARTIAL | Theo đúng hồ sơ thực tế, chấp nhận nội dung tổng quan có giới hạn; không giả định người dùng đã rà Word độc lập. (1)–(4) nguồn đã được hồ sơ kiểm tra có giới hạn, chỉ (1) trong DOCX. Nhóm phương trình nhiệt khác không được nâng trạng thái. |

| Tệp đầu vào chỉ đọc | SHA-256 trước và sau, không đổi |
|---|---|
| `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx` | `a58cf37dee216f2e193f9ee607fa15ba4987cf49b66c4a884dab895172ebf6d4` |
| `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv` | `dacb3c6ad632a1ec7e3aab167f614cddaa00c7a76850506616060c332eac7890` |
| `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv` | `d9bcd231bfb43ed223b8db6b270060196d5f485aa9f848cc5459d64ae857ba91` |
| `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md` | `1191dfd41f394d76ed933c3805c69ad4be1a47ac69e4494f19743a414696136a` |
| `outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md` | `9f60f4434b1699bc38ad23fbe7f5e7ae8c816957f4885caae3cd83dd6c0d5d7b` |
| `outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx` | `35a6842cd1513cb2ac91328ebadc1de0feacb2c6d421c5c4170d7ddce3c7e4e5` |
| `outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv` | `f3778953f446e71e61ae192a3021b02407b13c35b11df2d30ab5914da49181dc` |
| `outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv` | `ca606e7804945c1ac719f8088b4a9965525078033cced17e08364c45705a31b7` |
| `outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md` | `d87a902881e1d5d2161172d2db700c261a8ba653af2f7cff1722ea5213206e19` |
| `outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md` | `72a9556ed438ef126da2d186add01b053970cae41df9b3e151d1b6e443621128` |
| `outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx` | `2ecd6ccd690b0285e3414faa52135aaeb2db738e3b69df773548a597a4230da2` |
| `outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv` | `4eaae31d939e4fe3a64c2ae2afac173eafa843a22f86d9d88befc62d14bc98c5` |
| `outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv` | `aa372e9fa39f91b4bfb04c9342831cd90e9ecd530c537c2361c35d45de1548c5` |
| `outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md` | `cb02fffbe114df41dd6068c908f8e53d5de323c296b2b43a903f33519c027832` |
| `outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md` | `932a5705b875d978a2158d4b1a590d4c2170cae3a60d4385a0b5cbc3b03466f4` |
| `outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx` | `0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376` |
| `outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv` | `49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550` |
| `outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv` | `a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7` |
| `outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md` | `675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff` |
| `outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md` | `543a25380b524439bcb97253e4531aefff28a6a50912b16a23e9815f154e98e9` |

Kiểm tra lại cả 20 hash sau dựng tài liệu và sau kiểm tra độc lập. Thêm 193 tệp hỗ trợ trong WEP, PDF chuẩn, reading pack và §2.3 được băm và kiểm tra không đổi. Không sửa registry, Paper Notes, Evidence Records, trạng thái khoa học hoặc các bản thảo khác. Kỹ năng biên tập áp dụng: academic-humanizer, unslop; ponytail giới hạn mã dựng ở script tạm.

## Quyết định khoa học và chuỗi lập luận

Giữ tiến trình vật liệu TiNi, kiến trúc bó dây/cáp, tải tiếp xúc được SMA điều biến, rồi tạo và truyền áp suất. Chuỗi nhiệt/chuyển pha SMA → lực và hành trình chịu tải → truyền cơ học/lưu chất → tải tại giao diện thực → ma sát và chuyển động tương đối → đáp ứng uốn là phân rã câu hỏi, không phải định luật MP1 đã kiểm chứng. Mỗi nghiên cứu chỉ hỗ trợ một số mắt xích và kiến trúc riêng.

Phân biệt E của vật liệu, EI cấp tiết diện và độ dốc lực–độ võng; lực pháp tuyến N và ứng suất tiếp xúc Pa; lực ma sát thực và giới hạn truyền lực; nhiệt của SMA chấp hành và dây chịu uốn; hiệu chuẩn phép đo, hiệu chỉnh tham số và kiểm chứng độc lập. Không chọn topology, pha, mô hình hoặc giả thuyết trội của MP1. Tiền lệ biến độ cứng bằng SMA, điều biến ma sát, mô hình dây/sợi, kẹt áp dương trong §2.3 và bơm SMA vẫn là kiến thức đã có, không là đóng góp mới do ghép tên gọi.

## Chồng lặp và mâu thuẫn được xử lý

| Nhóm | Vị trí gốc | Phân loại | Quyết định ROOT |
|---|---|---|---|
| O01 | 2.4.1 P8; 2.4.2 P5; 2.4.3 P4; 2.4.4 P22 | REDUNDANT_EXPLANATION | S01 rút định nghĩa E/EI ở P5, giữ liên kết về 2.4.1, K và giới hạn lực/ứng suất. |
| O02 | 2.4.1 P10; 2.4.2 P13 | REDUNDANT_EXPLANATION | S02 bỏ khai triển FE/UMAT lần hai, giữ Souza, hình học và tiếp xúc. |
| O03 | 2.4.1 P10/T12; 2.4.2 P13–14/T17 | NECESSARY_REINFORCEMENT, không phải DUPLICATED_SOURCE_SUMMARY thừa | Giữ hai vai trò vật liệu và cơ học tiếp xúc của cùng M25; chỉ một mục tham khảo, không nhân số kiểm chứng. |
| O04 | 2.4.3 P14, câu cuối và câu về nhận dạng | REDUNDANT_EXPLANATION | S03 bỏ câu chốt trùng ngay trong đoạn. |
| O05 | 2.4.1 P14; 2.4.2 P5/P18; 2.4.3 P14; 2.4.4 P30 | NECESSARY_REINFORCEMENT | Giữ giới hạn nhận dạng theo từng cấp vật liệu, giao diện, nguồn và mẫu. |
| O06 | 2.4.1 P4/P7; 2.4.3 P5/P13; 2.4.4 P28 | NECESSARY_REINFORCEMENT | Giữ trễ vật liệu, tiếp xúc và thời gian nhiệt/dòng riêng. |
| O07 | 2.4.2 P19; 2.4.3 P15; 2.4.4 P2/P30 | NECESSARY_REINFORCEMENT; không xóa như REPEATED_TRANSITION | Giữ các câu chuyển có chức năng; S05 định danh áp suất buồng phía piston. |
| O08 | 2.4.4 P2 so với P32 | INCONSISTENT_CLAIM về thuật ngữ, không phải mâu thuẫn kết quả thực nghiệm | S04 đổi "được thực nghiệm hiệu chuẩn" thành "được kiểm chứng thực nghiệm" cho chuỗi cơ chế. |

Không phát hiện mâu thuẫn vật lý mới chưa được rào giới hạn giữa bốn bản thảo. Có ba phần giải thích lặp được rút, một điều chỉnh thuật ngữ kiểm chứng, một làm rõ câu chuyển và một nhắc lại cần thiết thông tin bố trí xoắn. Không xóa đoạn khoa học hoặc hàng bảng nguồn. Không có bảng khoa học bị hợp nhất hay loại bỏ.

## Các chỉnh sửa được ROOT phê duyệt

P/T là chỉ số phần tử trực tiếp trong `word/document.xml` của từng DOCX đầu vào, đánh số từ 0. Mọi số trong sáu cặp trước/sau dưới đây còn là số trích dẫn cục bộ; bảng ánh xạ tiếp theo quyết định số cuối. Không đưa nhật ký sửa vào thân luận văn.

### S01, §2.4.2 P5

Phê duyệt: ROOT, chỉ áp dụng bản tích hợp. Lược định nghĩa E và EI đã có ở §2.4.1 P8; giữ định nghĩa K và phân biệt ứng suất bề mặt với lực phân bố trên chiều dài.

Trước:

> Việc diễn giải độ cứng cũng đòi hỏi phân biệt các đại lượng. Mô đun Young E mô tả tính chất vật liệu, còn độ cứng uốn EI của tiết diện có đơn vị N·m². Độ dốc K của quan hệ lực và chuyển vị có đơn vị lực trên chiều dài và phụ thuộc vào chiều dài mẫu, điều kiện biên, vị trí đặt tải cùng trạng thái tải ban đầu. Truyền lực cắt qua giao diện, ứng suất tiếp xúc, hệ số ma sát và sức kháng ma sát truyền được là các đại lượng khác nhau. Ứng suất tiếp xúc biểu thị lực trên đơn vị diện tích, gồm thành phần pháp tuyến và tiếp tuyến; không được đồng nhất với lực giao diện phân bố trên đơn vị chiều dài trong mô hình lớp. Một đường lực và chuyển vị tổng thể không tự xác định được phân bố trượt hay ứng suất tiếp tại từng mặt tiếp xúc. Nó cũng chưa tách được ảnh hưởng của tiếp xúc khỏi sự thay đổi trạng thái vật liệu đã nêu ở mục 2.4.1. Các so sánh độ cứng vì vậy chỉ có ý nghĩa khi hình học, tải ban đầu và điều kiện biên tương ứng đã được làm rõ.

Sau, trước khi đổi số trích dẫn:

> Theo phân biệt đại lượng ở mục 2.4.1, độ dốc K của quan hệ lực và chuyển vị có đơn vị lực trên chiều dài và phụ thuộc vào chiều dài mẫu, điều kiện biên, vị trí đặt tải cùng trạng thái tải ban đầu. Truyền lực cắt qua giao diện, ứng suất tiếp xúc, hệ số ma sát và sức kháng ma sát truyền được là các đại lượng khác nhau. Ứng suất tiếp xúc biểu thị lực trên đơn vị diện tích, gồm thành phần pháp tuyến và tiếp tuyến; không được đồng nhất với lực giao diện phân bố trên đơn vị chiều dài trong mô hình lớp. Một đường lực và chuyển vị tổng thể không tự xác định được phân bố trượt hay ứng suất tiếp tại từng mặt tiếp xúc. Nó cũng chưa tách được ảnh hưởng của tiếp xúc khỏi sự thay đổi trạng thái vật liệu đã nêu ở mục 2.4.1. Các so sánh độ cứng vì vậy chỉ có ý nghĩa khi hình học, tải ban đầu và điều kiện biên tương ứng đã được làm rõ.

### S02, §2.4.2 P13

Phê duyệt: ROOT, chỉ áp dụng bản tích hợp. FE và UMAT đã được giới thiệu ở §2.4.1 P10. Chỉ bỏ phần khai triển viết tắt; giữ Souza, hình học, pháp tuyến/tiếp tuyến và đầu vào ma sát.

Trước:

> Vahidi và cộng sự [4] mô tả tường minh hình học xoắn và tiếp xúc giữa các bề mặt bằng phương pháp phần tử hữu hạn, viết tắt là FE theo finite element. Mô hình có tương tác pháp tuyến và tiếp tuyến giữa các bề mặt, với hệ số ma sát được chỉ định. Với vật liệu SMA, tác giả dùng mô hình hiện tượng học Souza ba chiều trong Abaqus thông qua UMAT, tức chương trình con vật liệu do người dùng định nghĩa (user material subroutine). Các hệ số ma sát và điều kiện tiếp xúc là đầu vào của bài toán nguồn; chúng chưa phải các tham số được nhận dạng cho bó TiNi của MP1.

Sau, trước khi đổi số trích dẫn:

> Vahidi và cộng sự [4] mô tả tường minh hình học xoắn và tiếp xúc giữa các bề mặt bằng mô hình FE. Mô hình có tương tác pháp tuyến và tiếp tuyến giữa các bề mặt, với hệ số ma sát được chỉ định. Với vật liệu SMA, tác giả dùng mô hình hiện tượng học Souza ba chiều trong Abaqus thông qua UMAT. Các hệ số ma sát và điều kiện tiếp xúc là đầu vào của bài toán nguồn; chúng chưa phải các tham số được nhận dạng cho bó TiNi của MP1.

### S03, §2.4.3 P14

Phê duyệt: ROOT, chỉ áp dụng bản tích hợp. Câu cuối lặp ngay câu về giới hạn suy đồng thời trạng thái vật liệu, lực ép và hệ số ma sát trong cùng đoạn.

Trước:

> Đối với MP1, cơ sở cơ học cần làm rõ là tiếp xúc nào chịu tác động điều khiển, dây với dây hay dây với lớp bao, và lực hoặc chuyển vị thực của SMA được truyền đến tiếp xúc như thế nào. Đây là những yêu cầu nhận dạng cơ chế, chưa phải kết quả đã được chứng minh cho MP1. Đáp ứng uốn phải được liên hệ với tải tiếp xúc và cản trượt, đồng thời giữ riêng nhiệt độ, trạng thái pha và lịch sử của phần tử SMA. Nhiệt độ bộ chấp hành có thể khác nhiệt độ bó dây TiNi; khi đường truyền nhiệt chưa được đặc trưng, chênh lệch này là một biến có thể gây nhiễu trong diễn giải. Khả năng nhận dạng tham số bị giới hạn nếu chỉ dùng đáp ứng tổng thể để suy đồng thời trạng thái vật liệu, lực ép và hệ số ma sát. Việc hiệu chỉnh mô hình theo dữ liệu của cơ cấu cũng cần phân biệt với kiểm chứng trên dữ liệu độc lập. Những điều kiện đó giúp tránh dùng một đường cong độ cứng tổng để suy ra đồng thời lực ép, hệ số ma sát và trạng thái vật liệu.

Sau, trước khi đổi số trích dẫn:

> Đối với MP1, cơ sở cơ học cần làm rõ là tiếp xúc nào chịu tác động điều khiển, dây với dây hay dây với lớp bao, và lực hoặc chuyển vị thực của SMA được truyền đến tiếp xúc như thế nào. Đây là những yêu cầu nhận dạng cơ chế, chưa phải kết quả đã được chứng minh cho MP1. Đáp ứng uốn phải được liên hệ với tải tiếp xúc và cản trượt, đồng thời giữ riêng nhiệt độ, trạng thái pha và lịch sử của phần tử SMA. Nhiệt độ bộ chấp hành có thể khác nhiệt độ bó dây TiNi; khi đường truyền nhiệt chưa được đặc trưng, chênh lệch này là một biến có thể gây nhiễu trong diễn giải. Khả năng nhận dạng tham số bị giới hạn nếu chỉ dùng đáp ứng tổng thể để suy đồng thời trạng thái vật liệu, lực ép và hệ số ma sát. Việc hiệu chỉnh mô hình theo dữ liệu của cơ cấu cũng cần phân biệt với kiểm chứng trên dữ liệu độc lập.

### S04, §2.4.4 P2

Phê duyệt: ROOT, chỉ áp dụng bản tích hợp. Chuỗi cơ chế cần kiểm chứng, còn hiệu chuẩn được dùng cho phép đo. Bản thảo tự phân biệt hai khái niệm ở §2.4.4 P32.

Trước:

> Nguồn áp suất dẫn động bằng hợp kim nhớ hình, gọi tắt là SMA, cần được xét theo từng bước chuyển đổi năng lượng. Đầu vào điện hoặc nhiệt làm thay đổi nhiệt độ và trạng thái pha của SMA; cơ cấu chấp hành tạo lực và hành trình chịu tải; biên chuyển động làm đổi thể tích buồng; chất lưu tạo áp suất và truyền tới mẫu. Sau đó mới đặt câu hỏi về tải pháp tuyến tại tiếp xúc, sức kháng ma sát và đáp ứng uốn của bó dây. Chuỗi này là khung phân tích của luận văn. Sự hợp lý về cơ học của từng bước chưa đủ để coi toàn bộ chuỗi là quan hệ đã được thực nghiệm hiệu chuẩn.

Sau, trước khi đổi số trích dẫn:

> Nguồn áp suất dẫn động bằng hợp kim nhớ hình, gọi tắt là SMA, cần được xét theo từng bước chuyển đổi năng lượng. Đầu vào điện hoặc nhiệt làm thay đổi nhiệt độ và trạng thái pha của SMA; cơ cấu chấp hành tạo lực và hành trình chịu tải; biên chuyển động làm đổi thể tích buồng; chất lưu tạo áp suất và truyền tới mẫu. Sau đó mới đặt câu hỏi về tải pháp tuyến tại tiếp xúc, sức kháng ma sát và đáp ứng uốn của bó dây. Chuỗi này là khung phân tích của luận văn. Sự hợp lý về cơ học của từng bước chưa đủ để coi toàn bộ chuỗi là quan hệ đã được kiểm chứng thực nghiệm.

### S05, §2.4.3 P15

Phê duyệt: ROOT, chỉ áp dụng bản tích hợp. Làm rõ vị trí áp suất trong câu chuyển tiếp và tránh cách gọi áp suất tại một chi tiết rắn. Không chốt thiết kế piston hoặc môi chất.

Trước:

> Các công bố [1]–[3] xác lập rằng điều biến ma sát bằng tác dụng nhiệt của SMA và kết hợp SMA với cơ chế kẹt đã có tiền lệ. Thay loại bộ chấp hành hoặc vật liệu vì thế chưa đủ để xác lập đóng góp cơ học mới của MP1. Câu hỏi còn phải giải quyết là đường truyền từ đầu ra SMA đến tải tiếp xúc và đáp ứng chịu uốn của cấu trúc đang xét. Nếu đường truyền đó có khâu tạo áp suất, áp suất tại piston vẫn cần được phân biệt với tải pháp tuyến cục bộ. Cơ sở cho việc đánh giá khâu tạo và truyền áp suất được xem xét tiếp ở mục 2.4.4.

Sau, trước khi đổi số trích dẫn:

> Các công bố [1]–[3] xác lập rằng điều biến ma sát bằng tác dụng nhiệt của SMA và kết hợp SMA với cơ chế kẹt đã có tiền lệ. Thay loại bộ chấp hành hoặc vật liệu vì thế chưa đủ để xác lập đóng góp cơ học mới của MP1. Câu hỏi còn phải giải quyết là đường truyền từ đầu ra SMA đến tải tiếp xúc và đáp ứng chịu uốn của cấu trúc đang xét. Nếu đường truyền đó có khâu tạo áp suất, áp suất trong buồng phía piston vẫn cần được phân biệt với tải pháp tuyến cục bộ. Cơ sở cho việc đánh giá khâu tạo và truyền áp suất được xem xét tiếp ở mục 2.4.4.

### S06, §2.4.1 P5

Phê duyệt: ROOT, chỉ áp dụng bản tích hợp. Hiển thị thông tin bố trí xoắn đã có ở C03 và hồ sơ chấp nhận; đối chiếu PDF M26 trang vật lý1,3 và M27 trang vật lý2–3. Không đổi topology.

Trước:

> Các thí nghiệm của Reedlunn, Daly và Shaw được thiết kế để quan sát gần đẳng nhiệt: mẫu 7×7 được kéo ở các tốc độ biến dạng rất thấp, còn mẫu 1×27 được thử ở tốc độ cao hơn nhưng vẫn được chọn để hạn chế ghép nối nhiệt–cơ và được theo dõi bằng tương quan ảnh số (digital image correlation, DIC) và phép đo nhiệt bằng ảnh hồng ngoại (infrared thermography, IR) [1, pp. 5–11; 3, pp. 3–9]. Trong 7×7, các mặt chuyển pha có thể lan truyền dọc dây và cáp, trong khi 1×27 cho đáp ứng mềm hơn, ổn định hơn và không thể hiện mặt chuyển pha lan truyền trong các lớp xoắn sâu [1, pp. 1, 8–11; 3, pp. 2, 7–14]. Những quan sát này cho thấy tốc độ tải liên hệ với trường nhiệt cục bộ và động học mặt chuyển pha, nhưng chúng không phải là một phép quét tốc độ độc lập. Các nghiên cứu trên không thiết lập quan hệ tốc độ tổng quát hoặc chứng minh rằng đáp ứng không phụ thuộc nhiệt độ; phạm vi chính là kéo chậm, gần đẳng nhiệt, trong không khí ở nhiệt độ phòng.

Sau, trước khi đổi số trích dẫn:

> Hai cấu trúc được khảo sát là cáp 7×7 xoắn phải kiểu regular lay và cáp 1×27 có các lớp xoắn luân phiên [1, tr. 1–3; 3, tr. 2–3]. Các thí nghiệm của Reedlunn, Daly và Shaw được thiết kế để quan sát gần đẳng nhiệt: mẫu 7×7 được kéo ở các tốc độ biến dạng rất thấp, còn mẫu 1×27 được thử ở tốc độ cao hơn nhưng vẫn được chọn để hạn chế ghép nối nhiệt–cơ và được theo dõi bằng tương quan ảnh số (digital image correlation, DIC) và phép đo nhiệt bằng ảnh hồng ngoại (infrared thermography, IR) [1, pp. 5–11; 3, pp. 3–9]. Trong 7×7, các mặt chuyển pha có thể lan truyền dọc dây và cáp, trong khi 1×27 cho đáp ứng mềm hơn, ổn định hơn và không thể hiện mặt chuyển pha lan truyền trong các lớp xoắn sâu [1, pp. 1, 8–11; 3, pp. 2, 7–14]. Những quan sát này cho thấy tốc độ tải liên hệ với trường nhiệt cục bộ và động học mặt chuyển pha, nhưng chúng không phải là một phép quét tốc độ độc lập. Các nghiên cứu trên không thiết lập quan hệ tốc độ tổng quát hoặc chứng minh rằng đáp ứng không phụ thuộc nhiệt độ; phạm vi chính là kéo chậm, gần đẳng nhiệt, trong không khí ở nhiệt độ phòng.


## Tích hợp trích dẫn và hiệu chỉnh metadata

| Mục | Số cũ | Paper ID | DOI chuẩn | Số tích hợp |
|---|---:|---|---|---:|
| 2.4.1 | 1 | M26 | `10.1016/j.ijsolstr.2013.03.013` | 1 |
| 2.4.1 | 2 | M25 | `10.1080/15376494.2021.1955313` | 2 |
| 2.4.1 | 3 | M27 | `10.1016/j.ijsolstr.2013.03.015` | 3 |
| 2.4.1 | 4 | M28 | `10.3390/buildings14061567` | 4 |
| 2.4.2 | 1 | M22 | `10.1061/(ASCE)ST.1943-541X.0002171` | 5 |
| 2.4.2 | 2 | M23 | `10.1016/j.ijmecsci.2020.106192` | 6 |
| 2.4.2 | 3 | M24 | `10.1016/j.engstruct.2024.119217` | 7 |
| 2.4.2 | 4 | M25 | `10.1080/15376494.2021.1955313` | 2 |
| 2.4.3 | 1 | M31 | `10.1109/LRA.2022.3174363` | 8 |
| 2.4.3 | 2 | M32 | `10.20965/jrm.2022.p0466` | 9 |
| 2.4.3 | 3 | M37 | `10.1299/mej.24-00130` | 10 |
| 2.4.4 | 1 | M12 | `10.1016/j.sna.2022.113449` | 11 |
| 2.4.4 | 2 | M33 | `10.1109/TMECH.2012.2211032` | 12 |
| 2.4.4 | 3 | M34 | `10.3390/mi12050520` | 13 |


14 ánh xạ cục bộ, 13 DOI duy nhất. Chỉ một tài liệu bị lặp danh mục là M25, cũ 2.4.1[2] và 2.4.2[4], cùng tích hợp [2]. Không bỏ nguồn từng được dẫn. Thứ tự lần đầu trong thân/bảng là 1 đến 13; một bibliography đặt sau 2.4.4. Số tham khảo chỉ tạm cho §2.4, chưa phải số toàn Chương 2 hoặc luận văn; thông báo này không chèn vào bản thảo.

M25: 2.4.1 từng ghi số phát hành 2022 nhưng 2.4.2 giới hạn ở trực tuyến 03/08/2021. PDF chuẩn trang vật lý 1 xác nhận 2021 và đúng tạp chí Mechanics of Advanced Materials and Structures, không xác nhận 2022. Bản tích hợp dùng trực tuyến 2021. Paper Note lịch sử ghi nhầm Mechanics Based Design of Structures and Machines không được sửa; tên PDF có thẩm quyền cho đầu ra mới. M22: giữ DOI đầy đủ, không dùng chuỗi bị cắt `10.1061/(ASCE` trong hồ sơ cũ. M23: số báo 2021, online 11/11/2020; M24: số báo 2025, online 03/11/2024. M33: trang vật lý 1/trang in 536 xác nhận tập 18(2), tháng 4/2013 và online 20/08/2012; không tạo hai nguồn hoặc sửa registry 2012.

Thay trích dẫn theo phạm vi từng mục và tập token được kiểm kê, không thay tất cả chữ số. Các nhóm nhiều nguồn được sắp tăng nhưng giữ nguồn đi với locator gốc; cụm liền nhau 2.4.2 [1],[2],[3],[4] thành [2,5,6,7]. Các khoảng [1]–[3] đổi theo đúng ba danh tính. Giữ số trang, số phương trình nguồn và thông số kỹ thuật. `pp.` chuyển thành `tr.` trong phần tiếng Việt. Mọi trường textual của glossary đều quét, gồm định nghĩa, ngữ cảnh, quy nguồn, giới hạn và provenance đã chuẩn hóa, không chỉ cột Nguồn.

## Truy xuất nhận định và bảo toàn nội dung

TOTAL_TRACEABILITY_RECORDS: 123 = 20 + 34 + 30 + 39. Phân loại gốc: SOURCE_GROUNDED_CLAIM 79, INFERENCE 28, AUTHOR_PROPOSAL 9, DOCUMENT_COVERAGE 7. `SOURCE_GROUNDED` của 2.4.1 chỉ chuẩn hóa tên nhóm, giữ nhãn gốc trong `original_claim_type` và toàn bộ dữ liệu trong `original_record_json`.

TECHNICAL_CLAIMS_BY_CATEGORY: nguồn 78, suy luận 27, đề xuất 9, bao phủ 0. Khác biệt với nhóm gốc là 244-C14 thuộc metadata và 244-C35 thuộc giải thích glossary, đều giữ nguyên loại gốc nhưng không đếm như kết quả kỹ thuật. Các số này là số hồ sơ, không phải số kiểm chứng thực nghiệm độc lập.

Mỗi ID gốc có đúng một dòng tích hợp, dạng `24-<tiểu mục>-C<chỉ số>`; 123 khóa (source_section, original_claim_id) duy nhất. Có 107 dòng gắn nội dung chính, 2 dòng gắn nội dung chính kèm chi tiết còn trong hồ sơ, 5 hồ sơ hỗ trợ riêng, 7 dòng bao phủ, 1 metadata bibliography và 1 glossary. Nhiều dòng cùng gắn một đoạn vẫn giữ mọi ID và không được đếm là thí nghiệm riêng. ROOT thay ánh xạ suy từ cùng citation của worker bằng đối chiếu nội dung chính xác theo từng claim.

Năm hồ sơ hỗ trợ riêng đã có trước tích hợp: 2.4.1 C13 về C3D8R/thuật toán tiếp xúc M28 và 2.4.4 244-C08/C09/C10/C11 về phương trình (2)–(4)/kiểm tra thứ nguyên. Không chèn lại vào DOCX và không làm mất khỏi CSV. 2.4.2 C17 và 2.4.3 C04 giữ chi tiết bổ sung trong nguyên văn hồ sơ; đoạn tương ứng chỉ bao phủ phần lập luận cốt lõi. Mỗi dòng có bản sao JSON nguyên vẹn để tránh mất trường giữa bốn schema khác nhau; bổ sung lookup Evidence ID với tệp/dòng canonical cho các trường đầu vào thiếu, không gán lookup này như kiểm chứng PDF mới. Nguồn trực tiếp cho kiến trúc bài báo vẫn chỉ là đối chiếu khi suy sang MP1.

Kiểm tra độc lập ở ROOT đối chiếu 82 phần tử thân được giữ, gồm 186 kiểm tra đoạn/ô: ngoài sáu đoạn đã duyệt và thay trích dẫn, văn bản khoa học và mọi ô bảng so sánh giữ nguyên nội dung. Không có thay số liệu hay bỏ giả định. Địa chỉ Word trong master CSV là chỉ số phần tử trực tiếp từ 0 kèm đoạn mở đầu, không là số trang chưa kết xuất.

## Thuật ngữ và phụ lục biên tập

93 bản ghi gốc (15/26/22/30) thành 88 mục, đủ 93 ánh xạ gốc duy nhất. Năm cặp gộp: Shape memory alloy, Interwire contact, Friction coefficient, Frictional shear capacity, Normal contact traction. Giữ riêng E/EI/K; lực/ứng suất pháp tuyến; sức cản/khả năng truyền ma sát; hành trình tự do/chịu tải/lực khóa; tốc độ/mức phục hồi; hiệu chuẩn/hiệu chỉnh/kiểm chứng. Các khác biệt hợp lệ không bị sửa cho giống nhau.

Thêm câu nêu giới hạn k_i trong ngữ cảnh Slip rigidity theo giới hạn đã chấp nhận; không thêm đơn vị. Chuẩn hóa prototype thành nguyên mẫu, dấu thập phân 0,5, mm/phút, pp. thành tr., diễn đạt kiểm chứng trong cột Việt. Trạng thái biên tập, quy nguồn riêng, mọi nguyên gốc/giới hạn vẫn nằm trong CSV; Word chỉ hiển thị ngữ nghĩa và số nguồn thật, thêm nhãn Tổng hợp biên soạn khi thích hợp. Phụ lục này phục vụ biên tập, chưa quyết định cấu trúc nộp chính thức HCMUT.

## Bảng, phương trình và định dạng

| Thành phần gốc | Tích hợp | Quyết định |
|---|---|---|
| 2.4.1 Bảng 2.4.1, 5 hàng × 6 cột | Bảng 2.4.1, 5 × 6 | Giữ mọi ô, đổi citation theo danh tính. |
| 2.4.2 Bảng 2.4.2, 5 × 6 | Bảng 2.4.2, 5 × 6 | Giữ cả bốn nguồn và các giới hạn. |
| 2.4.3 Bảng 2.4.3, 4 × 6 | Bảng 2.4.3, 4 × 6 | Giữ ba kiến trúc riêng. |
| 2.4.4 Bảng 2.4.4, 4 × 6 | Bảng 2.4.4, 4 × 6 | Giữ ECF, SMA ướt, cuộn–vỏ. |
| Bốn glossary 16/27/23/31 hàng, gồm tiêu đề | Một Bảng A.2, 89 × 5 | Hợp nhất 88 mục; A.2 tiếp quy ước A.1 của 2.3, không mặc định số phụ lục toàn luận văn. |
| 2.4.4, phương trình nguồn (1), cũ [2] | Một OMML không đánh số phương trình luận văn, nguồn [12] | Giữ nguyên XML, dấu ≥, hai chỉ số dưới, lời định nghĩa và điều kiện. Không có đổi số phương trình; (1) trong lời là số nguồn. |

ROOT xem ảnh trang vật lý 3/trang in 538 của M33 và đối chiếu nguồn M33-E02, WP-D/EVIDENCE_RECORDS.jsonl dòng 18. Biểu thức giữ là Q_out ≥ Q_in. Hai Q là lưu lượng thể tích, đơn vị m³/s trên cùng cơ sở thời gian; dấu bằng cho phần dư bằng không, phần dư dương cần lớn hơn. Đây là điều kiện cần cho dòng duy trì SMA ướt, không phải cân bằng năng lượng hay quan hệ áp suất. Không chép (2)–(4), không suy tất cả nhóm phương trình nguồn được xác minh. Hash OMML nguồn/đích: `98fb9a6775e1874ece4728d56f6d084e9e4ce8e4925e12f493bc0faf0549ca0f`. Chỉ số dưới trong lời định nghĩa và glossary giữ bằng run Word gốc/chỉnh sửa được.

Tài liệu A4 dọc, Times New Roman, thân 12 pt, tài liệu tham khảo/chú thích 10 pt, bảng 9,5 pt; lề trên/dưới 2,5 cm, trái 3 cm, phải 2 cm theo quy ước §2.3. Bốn tiêu đề tiểu mục giữ trình tự; các tiêu đề nội bộ 2.4.4 không thêm số mục. Tất cả năm bảng có tblGrid/tblW/tcW trong vùng chữ thực 9071 twip, đầu lặp và 107 hàng không tách. Đã sửa sai số làm tròn 1 twip. Một bibliography, một glossary; mỗi reference có keepLines, chân trang có trường PAGE; không ép số trang. Sửa parser để đổi riêng span trích dẫn, giữ run chỉ số dưới và OMML; kiểm tra lại sau sửa.

## Phát hiện QA độc lập và sửa trước đóng gói

F01: cột trang chuẩn hóa ở master traceability ban đầu bắt nhầm chữ trong Abstract, analytical hoặc từ mô tả khi không có locator. ROOT sửa parser để chỉ nhận p./pp. ở ranh giới từ, theo sau bằng chữ số/range. C01 mục 2.4.1 giữ trang 2, C09 giữ trang 18; các dòng suy luận/đề xuất/bao phủ không có trang riêng mang NOT_APPLICABLE có giải thích. Locator gốc và toàn bộ JSON chưa từng bị đổi. Năm assert hồi quy kiểm tra cả khoảng trang và văn bản không phải trang; QA mở lại CSV xác nhận khắc phục. Thêm cột giải thích phạm vi vai trò nguồn khi chuyển kiến trúc sang MP1, không thay source_role gốc.

F02: bảng khoa học sao chép có bốn tblHeader và 18 cantSplit thừa khi builder thêm thuộc tính đã có. ROOT duyệt chuẩn hóa mỗi thuộc tính đúng một lần; mọi hàng và nội dung giữ nguyên. N01: hai k_i trong ô ngữ cảnh Slip rigidity chuyển thành k với i dạng chỉ số dưới Word, không thêm OMML hoặc gán đơn vị. F03: hai ô Nguồn của Volumetric flow rate và Chamber pressure ban đầu kèm citation của ví dụ ngữ cảnh dù source_paper_ids trống. ROOT giữ các citation ở ngữ cảnh, đổi hai ô Nguồn thành Tổng hợp biên soạn; không gán định nghĩa biên tập cho bài ví dụ. Các sửa này không thay sáu chỉnh sửa khoa học đã duyệt hoặc các bản gốc.

QA kiểm tra lại tệp thực sau từng lượt sửa. Trạng thái cuối được dẫn đầy đủ trong báo cáo bảy cổng; không dùng hash/manifest của bản tạm làm nghiệm thu bản cuối.

## Provenance thực thi và kiểm tra độc lập

ROOT requested GPT-6.1 SOL HIGH; runtime không công bố định danh/effort chính xác. Sáu worker được gọi theo cấu hình A/B/C/F gpt-6.1-sol medium, D/E gpt-6-luna medium. Đây là tham số yêu cầu gửi công cụ, không phải chứng thực backend. Giới hạn bốn slot gồm ROOT: A/B/C song song; D sau A; E sau phê duyệt khoa học/citation/terms; F sau DOCX. Không có hai worker ghi cùng tệp cuối. ROOT tạo ba CSV và ba báo cáo, E chỉ ghi DOCX; QA chỉ đọc.

QA độc lập: PASS_STATIC_BOUNDED. Kết quả đầy đủ được đưa vào báo cáo bảy cổng; không dùng tư cách độc lập để tuyên bố tái kiểm chứng toàn bộ PDF. Script dựng và validator có assert được lưu tạm tại `/tmp/MP1-CH2-2.4-INTEGRATION/`; đầu ra bền vững cuối chỉ đúng bảy tệp. Sáu chỉnh sửa, ánh xạ nguồn/claim và các quyết định đầy đủ ở tệp này cùng ba CSV, không chỉ nằm trong terminal.

## Giới hạn và hành động tiếp theo

- Không có bộ kết xuất Word/LibreOffice/soffice/pandoc/OnlyOffice khả dụng. Chưa nhìn từng trang, nên chưa xác minh cắt bảng, trang trắng, trang tham khảo hoặc hàng thuật ngữ mồ côi. Kiểm tra XML không thay thế bước này.
- Đơn vị k_i ở phương trình (15) của M23 giữ `UNVERIFIED_UNITS_EQUATION_TEXT_VERIFIED`; không gán đơn vị, không sử dụng phương trình hay đồng nhất với k của M22.
- Giới hạn nhiệt độ/tốc độ của M26/M27; kéo khác uốn; thí nghiệm thép khác mô phỏng NiTi; hiệu chỉnh và dữ liệu Chen được dùng lại không thành kiểm chứng độc lập.
- M31 đo tiếp xúc dây–cao su; M32 tách nguyên mẫu SMP/SMA; M37 chưa tách độc lập pha R, nguồn dây, xử lý nhiệt và Af. Bất nhất nhãn xử lý nhiệt M37 và tiêu chí tỷ số phục hồi M32 không được tự giải quyết.
- M12 là ECF, áp âm tạo kẹt hạt còn áp dương tạo uốn; nhãn áp từ bơm riêng không thành áp khoang đo trực tiếp. M33 là bơm SMA ướt; M34 là cuộn SMA–vỏ mềm, không tự thành piston MP1.
- M33 chỉ có (1) được giữ và kiểm tra lại trong lần tích hợp. Giới hạn và dấu hiệu sai khác hệ số ở nhóm (8)/(9) đã ghi trong hồ sơ gốc vẫn ngoài phạm vi sử dụng; không tuyên bố toàn bộ phương trình M33 đã xác minh.
- Năm số báo 2022 của M25 chưa được PDF cung cấp xác nhận; bản tích hợp dùng trực tuyến 03/08/2021, không suy năm từ tên tệp.
- Topology dây–dây/dây–bao, môi chất, miền pha/nhiệt của dây chịu tải và SMA chấp hành, đường truyền áp suất, thông số phớt/rò/độ mềm, tải pháp tuyến cục bộ, hệ số ma sát, đại lượng uốn và khả năng nhận dạng MP1 vẫn mở. Không có luật áp suất–tiếp xúc–độ cứng hoặc kết luận tính mới/H1 mới.

Hành động tiếp theo duy nhất để đóng phần trình bày là mở/kết xuất Word bằng công cụ tương thích và rà từng trang. Không tiếp tục viết §2.5 hoặc thay quyết định thực nghiệm/nghiên cứu. Việc đó không làm mất hiệu lực các kiểm tra tĩnh đã có.


## Layout remediation R1 — authorized final replacement

TASK_ID: MP1-CH2-2.4-INTEGRATION-LAYOUT-REMEDIATION-R1  
Date: 18/10/2026, Asia/Bangkok.

The integrated DOCX was remediated after an independent LibreOffice render identified three presentation defects: mid-word wrapping in all four six-column comparison tables, an overly narrow five-column glossary, and a malformed right-hand equation subscript. No source files, CSV registers, original section drafts, §2.3, WEP, Paper Notes, Evidence Records, PDFs or registry files were modified.

### Approved presentation changes

1. The four scientific tables remain native six-column tables with identical cell text and row order. Each uses fixed 9071-twip width, non-equal widths `[1400, 1600, 1600, 1400, 1500, 1571]`, 8.5 pt Times New Roman, left alignment, zero first-line/paragraph spacing, space-based wrapping, modest cell padding, one repeated header marker and one `cantSplit` marker per row. LibreOffice visual review of rendered pages 3, 7, 10 and 13 found no clipping or mid-word breaks.
2. The master glossary remains 88 entries but changes from five columns to three: English/Vietnamese, full definition/context, and source. All original definition, context and source text remains available in the CSV and displayed in the DOCX. The rendered glossary is seven pages rather than the previous 13; first, continuation and last pages were inspected, with readable text, repeated headers and no visible clipping.
3. The selected equation candidate is the `candidate_nor.docx` variant. It preserves one editable OMML equation with `Q_out ≥ Q_in` and adds `<m:nor/>` only to the `out` and `in` subscript-label math runs. This is a minimal renderer-compatibility correction. The equation is not converted to an image and no new equation is introduced.

### Renderer evidence

The isolated LibreOffice 24.2.7 renderer produced A4 PDFs for the baseline (29 pages), layout-only candidate (23), selected candidate (23) and Cambria candidate (23). Baseline and layout-only/Cambria output retained the malformed right-hand subscript; the selected candidate displayed `Q_out ≥ Q_in` correctly. Candidate table/glossary pages were inspected visually. Microsoft Word was not run. Therefore `WORD_RENDER_VALIDATION: PARTIAL_LIBREOFFICE_VERIFIED_MS_WORD_NOT_VERIFIED`; no full cross-renderer PASS is claimed. The isolated renderer setup, commands and PDFs remain outside the seven final deliverables under `/tmp/MP1-CH2-2.4-LAYOUT-R1/renderer/`.

### Preservation and final hash

The layout QA reopened the selected candidate and confirmed 101 body paragraphs, four scientific tables cell-for-cell, 88 glossary records, 13 DOI references, 14 citation mappings, 123 traceability records, one editable OMML object and unchanged 20 input plus 193 support hashes. The original seven output files were backed up before remediation; only the authorized integrated DOCX was replaced.

FINAL_INTEGRATED_DOCX: `MP1_CH2_2_4_INTEGRATED.docx`  
FINAL_DOCX_BYTES: 74271  
FINAL_DOCX_SHA256: `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea`

Unresolved: Microsoft Word rendering remains unverified; scientific limits recorded in the original integration reports remain unchanged.
