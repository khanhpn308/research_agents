# Review dàn ý Chương 1–2 của `LR-FORMATED-rewrite.docx`

**Ngày review:** 2026-10-14

**Tệp được đọc:** `literature review/LR-FORMATED-rewrite.docx`

**Phạm vi:** chỉ Chương 1 và Chương 2.

## Kết luận

Khung dàn ý hiện tại **hợp lý ở cấp tuyến lập luận**, nhưng **chưa đủ nhất quán để gọi là bản chốt nội dung**. Có thể giữ kiến trúc hiện có và sửa có mục tiêu, không cần viết lại toàn bộ.

- **Chương 1:** tuyến `bối cảnh → vấn đề → mục tiêu → câu hỏi → phạm vi → phương pháp` là đúng. Các lỗi chính là tiêu đề 1.3 bị dùng sai, 1.5 trùng tiêu đề, câu hỏi nghiên cứu chưa bao phủ Bench B và logic phản chứng chưa được nêu rõ.
- **Chương 2:** phần 2.2–2.3 tạo được nền cơ học tốt, đặc biệt ở phân biệt áp suất cấp với lực pháp tuyến, các trạng thái stick–partial slip–full slip và giới hạn nhận dạng từ đường cong (M-kappa). Phần 2.4–2.6 còn là khung đề cương, chưa phải tổng quan hoàn chỉnh.
- **Ràng buộc khoa học lớn nhất:** bản thảo đôi lúc nói về ma sát dây–dây và dây–ống bao như hai thành phần đã xác định, trong khi trạng thái dự án vẫn yêu cầu xác nhận giao diện chi phối. Cần giữ cách viết trung tính cho đến khi mặt cắt và hướng lực được mentor xác nhận.

## Căn cứ và trạng thái bằng chứng

- Nội dung Word: **ĐỌC TOÀN VĂN TỆP DOCX**. Tệp có 242 đoạn văn, 1 bảng và các công thức Office Math.
- Trạng thái dự án: **VERIFIED REPOSITORY STATE**, đối chiếu với `docs/project/research_state.json`, `docs/project/MP1_MENTOR_PIVOT_CURRENT.md` và `docs/project/MP1_CHAPTERS_1_2_WORKING_DRAFT_2026-09-29_VI.md`.
- Nhận định về tính hợp lý của bố cục: **INFERENCE/REVIEW JUDGMENT**.
- Không dùng bản Word này để khẳng định novelty mới. Trạng thái hiện hành vẫn là MP1-R có điều kiện, H0b còn là đối thủ sống và H1 chưa được chứng minh.

## Điểm đang làm tốt

1. **Chương 1 thu hẹp được từ robot mềm/continuum robot vào bài toán cơ học cụ thể.** Đoạn chuyển từ độ mềm dẻo và khả năng chịu tải sang biến đổi độ cứng là phù hợp.
2. **Bài toán 1.2.3 được phát biểu thận trọng.** Câu “đặc trưng hóa ... đồng thời đánh giá khả năng giải thích ... bằng những mô hình đã có” không khẳng định đã có cơ chế mới.
3. **Mục tiêu dùng (M-κ) làm đại lượng trung tâm.** Điều này phù hợp với hướng model discrimination và tránh đồng nhất độ cứng đầu công tác với độ cứng uốn của mẫu.
4. **Phần 2.2.3 phân biệt áp suất cấp với áp suất tiếp xúc hữu hiệu.** Đây là một điểm cơ học quan trọng và phù hợp với rủi ro pressure-to-contact mapping trong trạng thái dự án.
5. **Phần 2.3 có các cảnh báo đúng về nhận dạng.** Bản thảo không suy ra toàn bộ vòng trễ là do ma sát và không xem full slip là các dây hoàn toàn độc lập không còn ma sát.
6. **Bản thảo đã loại bỏ một số cách tuyên bố novelty quá rộng.** Phần 2.2.4 nói rõ positive pressure và mô hình ba trạng thái không tự tạo thành nguyên lý mới.

## Các điểm cần sửa trước khi chốt

### Mức P0: cần sửa để không sai phạm vi khoa học

#### 1. Giữ giao diện ở trạng thái trung tính

Chương 1 hiện nêu cả “ma sát giữa các dây” và “tương tác giữa dây và ống bao”. Chương 2.3.3 cũng phân tích hai nhóm này như các thành phần của cấu hình. Cách trình bày này có thể được hiểu là cấu hình và đường truyền lực đã được xác nhận.

Theo trạng thái dự án, chưa khóa wire–wire, wire–sleeve hay cả hai. Vì vậy, trước khi có mặt cắt và sơ đồ lực được xác nhận, nên dùng:

> “các giao diện tiếp xúc có thể chi phối, gồm dây–dây và/hoặc dây–ống bao”

Sau đó chỉ gọi một giao diện là “chi phối” nếu Bench A hoặc phép đo pull-out/shear riêng cung cấp bằng chứng. Không viết rằng áp suất dương chắc chắn làm tăng lực pháp tuyến giữa các dây.

#### 2. Tách H0a, H0b và H1 trong Chương 1

Tệp hiện nói rằng các giả thuyết sẽ đưa vào 2.6. Việc không đưa toàn bộ công thức vào Chương 1 là được, nhưng cần có một đoạn ngắn về logic phản chứng:

- H0a, mô hình mô đun hằng đơn giản, đã bị phản bác trong miền có chuyển pha NiTi;
- H0b, mô hình NiTi có xét chuyển pha kết hợp contact/Coulomb friction, vẫn là đối thủ sống;
- H1, luật ghép constitutive–contact mới, chưa có bằng chứng;
- H0a sai không suy ra H1 đúng.

Nên thêm một null kỹ thuật độc lập, H0P, để kiểm tra liệu thay đổi do áp suất có vượt bất định đo hay không. H0P/H1P không được trộn với H0b/H1 về mô hình vật liệu.

#### 3. Bổ sung câu hỏi cho Bench B hoặc hạ mục tiêu SMA–piston

Mục tiêu 1.3.2 đã có đánh giá nguồn SMA–piston, nhưng ba câu hỏi hiện tại chỉ bao phủ đáp ứng uốn, ma sát và vai trò vật liệu TiNi. Đây là lệch giữa mục tiêu, câu hỏi và bố cục Chương 4.

Có hai cách sửa, chọn một:

- **Khuyến nghị:** thêm câu hỏi về đặc tính nguồn áp và câu hỏi so sánh tích hợp ở cùng áp suất gần mẫu; hoặc
- xem SMA–piston chỉ là phần hỗ trợ/feasibility của Chương 4, bỏ nó khỏi mục tiêu chính của Chương 1.

Nếu giữ Bench B, nên nêu rõ Bench A pressure-only phải được thực hiện trước. Bench B chỉ được mở rộng khi Bench A chứng minh có tín hiệu cơ học do áp suất vượt bất định.

### Mức P1: cần sửa để bố cục và lập luận nhất quán

#### 4. Sửa cấu trúc tiêu đề Chương 1

Hiện có hai tiêu đề “Đối tượng và phạm vi nghiên cứu”. Phần 1.3 thực tế là **Mục tiêu nghiên cứu**, còn phần 1.5 mới là **Đối tượng và phạm vi nghiên cứu**.

Trình tự tối thiểu nên là:

1.1 Bối cảnh và tính cấp thiết  
1.2 Đặt vấn đề nghiên cứu  
1.3 Mục tiêu nghiên cứu  
1.4 Câu hỏi nghiên cứu  
1.5 Đối tượng và phạm vi nghiên cứu  
1.6 Phương pháp và cách tiếp cận  
1.7 Ý nghĩa dự kiến  
1.8 Bố cục luận văn

Các tiểu mục 1.2.1–1.2.3, 1.3.1–1.3.2 và 1.5.1–1.5.2 cần được đặt bằng style Heading tương ứng, không để dưới dạng đoạn Normal có đánh số thủ công.

#### 5. Sửa phần 1.8 để khớp tên các chương thật

Phần 1.8 hiện mô tả Chương 3 là “mô hình, thiết kế thực nghiệm và phương pháp nghiên cứu” và Chương 4 là “kết quả, phân tích và thảo luận”. Trong tệp, tên chương lại là:

- Chương 3: thí nghiệm với nguồn áp ngoài (Bench A);
- Chương 4: cơ cấu SMA–piston và thử nghiệm tích hợp (Bench B).

Phần bố cục phải dùng một phiên bản duy nhất. Theo trạng thái hiện hành, Chương 3–4 vẫn là các chương có điều kiện, nên có thể viết “dự kiến” và ghi rõ điều kiện mở chương.

#### 6. Làm rõ phép đo cần thiết cho (M-κ)

Trong 1.6.2, cụm “lực, chuyển vị và/hoặc hình dạng để xác định (M-κ)” còn quá rộng. Muốn báo cáo (M-κ), cần nêu rằng mômen và độ cong phải được suy ra bằng một ánh xạ đã xác định từ lực/chuyển vị/hình dạng, với điều kiện biên và giả thiết chuyển đổi được công bố.

Nếu chỉ đo lực–chuyển vị toàn cục mà không có độ cong hoặc hiệu chuẩn hình học, chỉ nên gọi kết quả là force–displacement stiffness, không gọi trực tiếp là (M-κ).

#### 7. Thu hẹp phần mở đầu của Chương 2

2.1.1–2.1.3 đang dành nhiều chỗ cho phân loại robot liên tục, phương thức dẫn động và độ cứng đầu công tác. Nội dung này nên giữ ở mức đủ để tạo bối cảnh rồi chuyển nhanh sang bó dây, contact/friction và (M-κ). Phần survey generic về robot và các vật liệu SMP/LMPA có thể rút thành một bảng ngắn.

## Đánh giá riêng Chương 2

### 2.1–2.2: đúng hướng nhưng cần kiểm soát độ rộng

Khung `bối cảnh ứng dụng → các cơ chế biến đổi độ cứng → cách tạo lực nén` là hợp lý. Phần positive-pressure jamming và Zhang–Yao 2026 nên giữ vì đây là mối đe dọa gần với lập luận pressure–slip–stiffness. Tuy nhiên, phần này phải kết luận rõ rằng positive pressure, fiber jamming và mô hình ba trạng thái đã có tiền lệ; phần còn lại chỉ có thể là câu hỏi interface-specific/model-discrimination có điều kiện.

Bảng 2.x nên được hoàn thiện với tối thiểu các cột: cơ chế, dạng tiếp xúc, đầu vào tạo lực nén, trạng thái mô hình, bằng chứng thực nghiệm và giới hạn chuyển giao sang MP1-R. Cần thay mọi placeholder như “Bảng 2.x” và “Hình 3” trước khi xem là bản hoàn tất.

### 2.3: là phần mạnh nhất, nên giữ làm lõi cơ sở khoa học

Các tiểu mục về Coulomb friction, cận lý tưởng, dây–dây/dây–ống bao và (M-κ) tạo được chuỗi cơ học tốt. Nên chỉnh ba điểm:

1. Đổi “Mô hình cận độ cứng uốn” thành “Các cận lý tưởng của độ cứng uốn” hoặc “Mô hình cận trên và cận dưới”, để người đọc biết đây là mốc tham chiếu có điều kiện.
2. Nói rõ independent-fiber và fully bonded là hai giới hạn động học, không phải hai trạng thái thực nghiệm luôn đạt được.
3. Giữ cảnh báo rằng một đường (M-κ) tổng thể không đủ để tách duy nhất ma sát dây–dây, ma sát dây–ống bao, độ cứng vỏ và trễ của TiNi. Cảnh báo này phải được liên kết trực tiếp với kế hoạch đo interface-specific ở Chương 3.

Phần tính diện tích vòng trễ và chuyển từ force–displacement sang (M-κ) có giá trị, nhưng các chi tiết tính toán quá sâu nên được rút ở Chương 2 và dành công thức thực thi cho chương phương pháp.

### 2.4: hiện mới là đề mục, chưa đủ cho bài toán TiNi

Cần bổ sung tối thiểu:

- trạng thái Austenite–Martensite, nhiệt độ và ứng suất chuyển pha;
- điều kiện để có siêu đàn hồi trong miền thử;
- khác biệt giữa uốn dây và kéo đơn trục;
- ảnh hưởng của nhiệt độ, tốc độ, lịch sử chu kỳ và training;
- cách phân biệt trễ do TiNi với trễ do ma sát và vỏ bao;
- thông số TiNi nào sẽ đo/độc lập hóa trước khi fit mô hình.

Không nên dùng một đường trễ (M-κ) để kết luận riêng về chuyển pha hay trượt.

### 2.5: là cầu nối bắt buộc nhưng đang còn trống

2.5 phải mô tả chuỗi:

`áp suất tại nguồn → áp suất gần mẫu → biến dạng màng/ống bao → lực hoặc traction pháp tuyến tại giao diện → trạng thái stick/slip → đáp ứng uốn`.

Mỗi mũi tên cần nêu biến đo được, biến suy ra, giả thiết và bất định. Đặc biệt, áp suất cấp không được đồng nhất với lực pháp tuyến cục bộ nếu chưa có hiệu chuẩn hoặc phép đo proxy được xác nhận.

### 2.6: cần đổi từ “khoảng trống” chung sang kết luận có điều kiện

Phần 2.6 nên trả lời bốn câu hỏi:

1. Cơ chế nào đã được chứng minh trong prior art?
2. Mô hình nào đã có thể dùng làm H0b?
3. Phần nào chưa được xác định cho đúng hình học/interface của MP1-R?
4. Phép đo nào ở Bench A/B có thể phân biệt các khả năng?

Cách kết luận phù hợp là:

> “Trong phạm vi corpus và cấu hình hiện chưa khóa, chưa xác định được ánh xạ có kiểm chứng từ áp suất áp dụng đến trạng thái tiếp xúc cụ thể của bó TiNi và đáp ứng uốn tương ứng. Đây là bài toán kiểm tra có điều kiện, không phải tuyên bố universal novelty.”

Phần này phải ghi rõ H0b còn sống, H1 chưa được chứng minh và kết quả null vẫn là kết quả hợp lệ để thu hẹp hướng nghiên cứu.

## Dàn ý tối thiểu nên chốt

### Chương 1

1.1 Bối cảnh và tính cấp thiết  
1.2 Vấn đề kỹ thuật và ranh giới prior art  
1.3 Bài toán MP1-R: áp suất là đầu vào biên, không phải lực pháp tuyến đã biết  
1.4 Mục tiêu tổng quát và mục tiêu cụ thể  
1.5 Câu hỏi nghiên cứu, gồm câu hỏi về Bench A, Bench B và model discrimination  
1.6 Logic phản chứng: H0a, H0b, H1 và null kỹ thuật H0P  
1.7 Đối tượng, phạm vi và điều không tuyên bố  
1.8 Phương pháp tiếp cận ở mức khái quát  
1.9 Ý nghĩa dự kiến  
1.10 Bố cục luận văn

### Chương 2

2.1 Phạm vi, cách tìm kiếm và phân loại bằng chứng  
2.2 Robot mềm, continuum robot và yêu cầu biến đổi độ cứng  
2.3 Các cơ chế jamming và điều biến ma sát  
2.4 Positive-pressure jamming và các prior art gần nhất  
2.5 Cơ học bó dây TiNi: chuyển pha, contact, slip và hysteresis  
2.6 Mô hình cận lý tưởng và đặc trưng hóa (M-κ)  
2.7 Chuỗi truyền áp suất đến lực tiếp xúc và đáp ứng uốn  
2.8 Nguồn SMA–piston, độ trễ và khả năng tái tạo điều kiện áp suất  
2.9 Tổng hợp bằng chứng, H0b/H1 và câu hỏi có điều kiện cho Bench A/B

Nếu muốn giữ số mục hiện tại để giảm sửa chữa, có thể gộp 2.1–2.2 như bản Word đang có, nhưng vẫn phải bổ sung phần phương pháp bằng chứng, prior-art boundary, TiNi mechanics, pressure-transfer chain và synthesis có điều kiện.

## Checklist trước khi gọi là bản chốt

- [ ] Sửa tiêu đề 1.3 và tiêu đề trùng 1.5.
- [ ] Đồng bộ mục lục, Heading styles và số mục.
- [ ] Chọn rõ vai trò của Bench B: mục tiêu chính hay feasibility có điều kiện.
- [ ] Thêm logic H0a/H0b/H1 và H0P ở mức ngắn trong Chương 1.
- [ ] Giữ giao diện dây–dây/dây–ống bao ở trạng thái trung tính cho đến khi được xác nhận.
- [ ] Bổ sung RQ cho nguồn SMA–piston và integrated comparison nếu vẫn giữ Chương 4.
- [ ] Hoàn thiện 2.4–2.6, đặc biệt TiNi, pressure-transfer map và synthesis.
- [ ] Hoàn thiện Bảng 2.x, Hình 1–3 và mọi công thức/định nghĩa ký hiệu.
- [ ] Đối chiếu từng trích dẫn [1]–[8] với một mục tài liệu tham khảo duy nhất; hiện phần `TÀI LIỆU THAM KHẢO` trong tệp đọc được chưa có nội dung.
- [ ] Kiểm tra lại phần bố cục Chương 3–4 trong 1.8 để khớp tên chương thực tế.
- [ ] Chỉ mở Chương 3 sau khi geometry/interface, pressure sensing, metrics, uncertainty và stop criteria đã được khóa.

