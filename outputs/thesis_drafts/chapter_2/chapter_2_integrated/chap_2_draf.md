# CHƯƠNG 2. TỔNG QUAN NGHIÊN CỨU VÀ CƠ SỞ CƠ HỌC

## 2.1. Phạm vi và định hướng tổng quan

Chương 2 xây dựng cơ sở lý thuyết và bằng chứng thực nghiệm để đánh giá bài toán MP1, tập trung vào bó dây nhiều phần tử bằng hợp kim nhớ hình TiNi chịu uốn và khả năng điều chỉnh độ cứng bằng tải ép hoặc áp suất[cite: 1]. Phạm vi tổng quan xem xét đồng thời tính chất vật liệu, hình học sắp xếp dây, cơ học tiếp xúc, ma sát, trạng thái pha của TiNi và điều kiện biên nhằm phục vụ trực tiếp năm câu hỏi nghiên cứu (RQ1–RQ5) đã đặt ra ở Mục 1.4.1[cite: 1]. Lịch sử phát triển chung của robot mềm chỉ được đề cập khi cần xác định bối cảnh cơ học[cite: 1].

Tài liệu trong chương được tổ chức theo bốn trụ cột cơ học gắn liền với các câu hỏi nghiên cứu[cite: 1, 4]:

1. **Truyền tải áp suất và cơ chế kẹt cơ học (phục vụ RQ1 và RQ2):** Các nghiên cứu về ma sát điều khiển bằng áp suất được xem xét để làm rõ áp suất tác động lên giao diện nào (dây–dây, dây–ống bao hoặc cả hai) và làm thay đổi ứng suất tiếp xúc tại đó theo chiều hướng nào[cite: 1]. Tài liệu về kẹt dây/sợi (wire/fiber jamming) được đặt cạnh các kiến trúc đối chiếu như kẹt lớp/tấm (layer/laminar jamming) và kẹt hạt (granular jamming) để xác định điều kiện kế thừa về đường truyền tải và chuyển động tương đối[cite: 1]. Chẳng hạn, Zhang và Yao đã mô hình hóa và thử uốn chuỗi kẹt bó sợi nylon bằng túi khí áp suất dương [1][cite: 1, 73]; tiền lệ này giúp định hình các giả thiết cần kiểm tra lại khi chuyển sang bó dây kim loại TiNi[cite: 1].
2. **Đáp ứng cơ–nhiệt của TiNi và cơ học cáp nhiều dây (phục vụ RQ1, RQ2 và RQ5):** Cơ học bó dây TiNi cần được xét cùng mô hình tiếp xúc để phân biệt đáp ứng nội tại của vật liệu với hiện tượng truyền lực và trượt tương đối giữa các phần tử[cite: 1]. Thí nghiệm kéo gần đẳng nhiệt của Reedlunn và cộng sự đã ghi nhận đáp ứng siêu đàn hồi và vòng trễ khác nhau ở hai cấu trúc cáp NiTi [2][cite: 1, 73]; kết quả này đòi hỏi phải tách biệt phần tiêu tán năng lượng do chuyển pha vật liệu khỏi phần tiêu tán do ma sát giao diện khi xét bài toán uốn có tải ép[cite: 1, 27].
3. **Nguồn chấp hành SMA tạo tải ép và áp suất (phục vụ RQ3 và RQ4):** Vai trò của bó dây TiNi chịu uốn cần được tách bạch với vai trò của phần tử SMA dẫn động nguồn áp suất[cite: 1]. Các công trình như bơm vi mô dùng lò xo SMA tác động lên vỏ silicone của Kotb và cộng sự [3] cung cấp cơ sở đối chiếu về khả năng tạo, duy trì và hồi áp suất theo lực, hành trình, nhiệt độ và thời gian[cite: 1, 73]. Đây là tiền đề để thiết lập phép so sánh giữa hệ tích hợp nguồn SMA–piston (Bench B) với hệ đối chứng chỉ dùng nguồn áp suất ngoài (Bench A) tại cùng áp suất gần mẫu[cite: 1].
4. **Mô hình hóa, phép đo, khả năng nhận dạng và độ không đảm bảo (phục vụ RQ5):** Nhóm tài liệu này giúp phân biệt đại lượng quan sát trực tiếp với đại lượng suy ra qua giả thiết, cũng như tách biệt bước hiệu chỉnh tham số (calibration) khỏi bước kiểm chứng dự báo độc lập (validation)[cite: 1, 4]. Trong khuôn khổ MP1, mô hình đối chứng $H_{0b}$ (kết hợp mô hình cấu thành TiNi có xét chuyển pha với tiếp xúc ma sát Coulomb thông thường dưới điều kiện biên áp suất $p(t)$) cần được kiểm tra khắt khe trên tập dữ liệu kiểm chứng độc lập trong phạm vi độ không đảm bảo đo trước khi xem xét sự cần thiết của bất kỳ giả thuyết luật ghép mới nào ($H_1$)[cite: 1, 61].

Mạch nội dung của chương đi từ việc chuẩn hóa thuật ngữ và khung đại lượng cơ học ở Mục 2.2, phân tích các kiến trúc điều chỉnh độ cứng và jamming đã công bố ở Mục 2.3, đi sâu vào vật liệu TiNi, ma sát bó dây và nguồn tạo áp bằng SMA ở Mục 2.4, đến các phương pháp mô hình hóa, đo lường và nhận dạng tham số ở Mục 2.5[cite: 2]. Cuối cùng, Mục 2.6 tổng hợp các khoảng trống có thể kiểm chứng và xác lập tiêu chí chuyển giao sang Chương 3 và Chương 4[cite: 2, 70].

---

## 2.2. Thuật ngữ và khung cơ học

### 2.2.1. Robot continuum và các cấp đại lượng độ cứng

Robot liên tục (continuum robot) là lớp cơ cấu có thân uốn liên tục dựa trên các đường cong có vectơ tiếp tuyến liên tục trong vật liệu cấu tạo, phân biệt với chuỗi các khâu cứng nối bằng khớp rời rạc [5], [6][cite: 7, 73]. Trong biểu diễn thanh Cosserat được Russo và cộng sự trình bày, hình dạng thân được mô tả bằng một đường trục đi qua trọng tâm tiết diện (tham số hóa theo chiều dài cung ở cấu hình ban đầu) cùng trường định hướng tiết diện dọc theo thân [6][cite: 7, 73]. Xấp xỉ độ cong hằng từng đoạn (piecewise constant curvature) chỉ là một lựa chọn biểu diễn hình học, chưa phải quan hệ tải – biến dạng; để dự đoán hình dạng dưới tải trọng còn cần phương trình cân bằng cơ học, quan hệ cấu thành và điều kiện biên cụ thể [5][cite: 7, 73].

Khi thay thế một cấu trúc nhiều dây bằng mô hình dầm một chiều tương đương, việc sử dụng chung một đường trục không hàm ý rằng mọi phần tử vật lý bên trong có cùng biến dạng dọc trục hoặc tạo thành một tiết diện liên hợp hoàn toàn [5], [6][cite: 7, 73]. Do đó, cần phân biệt rạch ròi ba cấp độ đại lượng độ cứng thường xuất hiện trong văn liệu[cite: 7, 8]:

* **Cấp vật liệu – Mô đun đàn hồi Young ($E$, đơn vị $\text{Pa}$ hoặc $\text{N/m}^2$):** Mô tả quan hệ ứng suất pháp – biến dạng dọc trong miền đàn hồi tuyến tính ở một trạng thái vật liệu xác định[cite: 7]. Đối với hợp kim TiNi, do quá trình chuyển pha làm thay đổi đáp ứng cơ học theo nhiệt độ, ứng suất và nhánh tải, không thể gán một hằng số $E$ duy nhất cho toàn bộ chu trình biến dạng [2][cite: 7, 73].
* **Cấp tiết diện – Độ cứng uốn ($B$ hoặc $EI$, đơn vị $\text{N}\cdot\text{m}^2$):** Phản ánh đồng thời đặc tính vật liệu và sự phân bố diện tích tiết diện thông qua mô men quán tính diện tích $I$ ($\text{m}^4$) đối với trục uốn đang xét[cite: 7]. Trong miền đàn hồi tuyến tính, mô men uốn $M$ ($\text{N}\cdot\text{m}$) liên hệ với độ biến thiên độ cong $\kappa$ ($\text{m}^{-1}$) [5][cite: 7, 8, 73]. Khi quan hệ $M-\kappa$ là phi tuyến, độ cứng uốn tiếp tuyến được xác định bằng độ dốc cục bộ $\text{d}M/\text{d}\kappa$ trên một nhánh tải, còn độ cứng uốn cát tuyến là tỷ số gia số $\Delta M/\Delta \kappa$ giữa hai trạng thái đã chọn[cite: 8, 50].
* **Cấp toàn cơ cấu – Độ cứng lực–chuyển vị ($K$, đơn vị $\text{N/m}$ hoặc $\text{N/mm}$):** Biểu diễn tỷ số hoặc độ dốc giữa lực tác dụng tại điểm đặt tải và chuyển vị tương ứng của điểm đó[cite: 8]. Chẳng hạn, Jeon và cộng sự xác định độ cứng robot từ độ dốc lực cản – chuyển vị ở đĩa đầu mút, sau đó mới suy ra độ cứng uốn tương đương thông qua xấp xỉ dầm công xôn [7][cite: 8, 73]. Giá trị $K$ phụ thuộc trực tiếp vào chiều dài mẫu, vị trí đặt tải, điều kiện gá đặt và biên dạng uốn[cite: 8].

Các mô hình quy giản dầm (như dầm Euler–Bernoulli bỏ qua biến dạng cắt hoặc dầm Timoshenko xét biến dạng cắt) khi áp dụng cho bó nhiều dây cần làm rõ các bậc tự do nội tại được giữ lại [5], [6][cite: 8, 73]. Ví dụ, mô hình cáp dây song song của Zhang và cộng sự giả thiết các lớp dây quy đổi có chung độ võng và độ cong nhưng vẫn cho phép trượt dọc trục tương đối tại giao diện thông qua một độ cứng trượt hiệu chuẩn [8][cite: 8, 73]. Điều này khẳng định rằng sự phù hợp của một đường cong lực – độ võng tổng thể chưa đủ để xác định duy nhất sự phân bố tiếp xúc và trượt bên trong nếu mô hình đã gộp chúng vào các tham số hiệu dụng [8][cite: 8, 9, 73].

### 2.2.2. Jamming, khóa ma sát (frictional locking) và các trạng thái trượt (slip)

Ở cấp độ kết cấu, kẹt cơ học (jamming) là sự gia tăng ràng buộc chuyển động tương đối giữa các phần tử (sợi, dây, lớp mỏng hoặc hạt) nhờ tương tác ma sát, giúp chúng truyền tải cùng nhau mạnh hơn [9][cite: 9, 73]. Khóa nhờ ma sát (frictional locking) chỉ khả năng hạn chế chuyển động tương đối trong một miền tải trọng nhất định chứ không đồng nghĩa với khóa cứng tuyệt đối[cite: 9]:

* **Trạng thái bám dính (Stick / Pre-slip):** Là điều kiện động học cục bộ trong đó không có chuyển vị tương đối theo phương tiếp tuyến tại vùng tiếp xúc[cite: 9]. Theo lý tưởng hóa ma sát tĩnh Coulomb, lực tiếp tuyến khi bám dính được quyết định bởi phương trình cân bằng và bị chặn trên bởi giới hạn ma sát tĩnh (phụ thuộc hệ số ma sát tĩnh và tải pháp tuyến cục bộ)[cite: 9, 42].
* **Trạng thái trượt một phần (Partial slip / Transition):** Xuất hiện khi ứng suất tiếp tuyến tại một số vùng giao diện hoặc một số cặp phần tử đạt tới ngưỡng ma sát và bắt đầu trượt, trong khi các vùng còn lại vẫn duy trì trạng thái bám dính [8], [9], [10][cite: 9, 42, 43, 73].
* **Trạng thái trượt toàn phần (Full slip):** Chỉ trạng thái mà hiện tượng trượt đã lan rộng ra toàn bộ phạm vi giao diện thuộc miền khảo sát của mô hình [9], [10][cite: 9, 43, 73]. Cần lưu ý rằng trượt toàn phần không đồng nghĩa với ma sát bằng không, độ cứng uốn $B$ triệt tiêu hay các dây hoàn toàn độc lập, bởi lực ma sát động tại giao diện vẫn tiếp tục truyền lực cản và gây tiêu tán năng lượng [9][cite: 10, 43, 73].

Các thuật ngữ bám dính và trượt mô tả động học tại giao diện tiếp xúc, cần được phân biệt rõ với biến dạng đàn hồi, biến dạng dẻo hoặc chuyển pha của bản thân vật liệu dây[cite: 9, 10]. Trong mô hình liên tục cho dầm kẹt lớp của Zhang và cộng sự, phép tương tự đàn–dẻo (elastoplastic analogy) được sử dụng để mô tả sự suy giảm độ cứng kết cấu khi các lớp trượt theo lịch sử gia tải – dỡ tải, chứ không hàm ý vật liệu của từng lớp bị chảy dẻo [11][cite: 10, 73]. Đặc biệt đối với bó dây TiNi, sự xuất hiện của vòng trễ (hysteresis loop) trên đồ thị tải – dỡ tải toàn cục có thể bắt nguồn đồng thời từ ma sát trượt giữa các dây, biến dạng của ống bao/đồ gá và quá trình chuyển pha siêu đàn hồi có trễ của chính vật liệu NiTi [2][cite: 10, 73].

### 2.2.3. Áp suất cấp, lực pháp tuyến và trạng thái quan sát

Trong các hệ thống điều chỉnh độ cứng bằng áp suất, cần tách biệt ba đại lượng cùng mang thứ nguyên áp suất ($\text{Pa}$) nhưng ở các vị trí vật lý khác nhau: áp suất tại nguồn tạo áp ($p_{\text{source}}$), áp suất đo tại vị trí gần mẫu ($p_{\text{near\_sample}}$) và độ lớn ứng suất tiếp xúc pháp tuyến nén cục bộ ($\sigma_n(x)$ hoặc $p_n(x)$) tại điểm $x$ trên giao diện tiếp xúc[cite: 10, 42]. Hợp lực pháp tuyến $N_i$ (đơn vị $\text{N}$) tác dụng lên miền tiếp xúc thứ $i$ chỉ bằng tích phân vô hướng $\int_{A_{c,i}} \sigma_n(x)\,\text{d}A$ khi bề mặt tiếp xúc phẳng và có vectơ pháp tuyến không đổi; với bề mặt dây tròn cong, hợp lực phải được xác định qua tích phân vectơ hoặc phép chiếu theo phương xác định[cite: 10, 11].

Quy ước về dấu áp suất cũng gắn liền với đường truyền phản lực của từng kiến trúc[cite: 10, 11]. Trong cấu hình kẹt lớp chân không do Caro và Carmichael tổng hợp, việc rút khí làm giảm áp suất tuyệt đối trong bao kín, nhờ đó áp suất khí quyển bên ngoài nén màng bao và ép chặt chồng lớp (áp suất dư âm) [12][cite: 10, 19, 73]. Ngược lại, trong cấu hình kẹt sợi áp suất dương của Zhang và Yao, túi khí bên trong được bơm căng (áp suất dư dương) để ép bó sợi vào thành vỏ cứng bên ngoài [1][cite: 11, 43, 44, 73]. Do đường truyền lực, độ mềm của màng bao, sự sắp xếp hình học của các phần tử và tổn thất khí động trên đường ống khác nhau, không thể mặc nhiên đồng nhất $p_{\text{source}}$ với $p_{\text{near\_sample}}$, càng không thể nhân trực tiếp áp suất nguồn với diện tích danh định để suy ra lực pháp tuyến $N_i$ trên từng cặp dây nếu thiếu mô hình truyền tải đã được kiểm chứng [1], [3], [13][cite: 11, 12, 73].

Theo Hướng dẫn biểu diễn độ không đảm bảo trong đo lường (GUM) [14], việc phân loại một đại lượng là đo trực tiếp, đại lượng thay thế (proxy) hay đại lượng suy ra từ mô hình phải dựa trên kênh cảm biến thực tế và hàm đo lường[cite: 13, 74]. Bảng 2.1 tổng hợp điều kiện diễn giải và giới hạn suy luận của các nhóm đại lượng cơ học chính trong nghiên cứu[cite: 13].

**Bảng 2.1.** Phân loại trạng thái quan sát và giới hạn suy luận của các đại lượng cơ học[cite: 13]

| Đại lượng | Điều kiện được gọi là đo trực tiếp | Giới hạn suy luận cần kiểm soát |
| :--- | :--- | :--- |
| $p_{\text{source}}$; $p_{\text{near\_sample}}$ | Đo bằng cảm biến áp suất đã hiệu chuẩn đặt tại đúng vị trí cổng nguồn hoặc sát buồng mẫu[cite: 13]. | Đo tại một cổng chỉ xác lập áp suất tại vị trí đó; chưa phản ánh tổn thất đường truyền hoặc phân bố ứng suất tiếp xúc $\sigma_n(x)$[cite: 13]. |
| $\sigma_n(x)$; $N_i$ | Đo bằng cảm biến tiếp xúc hoặc cảm biến hợp lực có miền và hướng đo phù hợp đặt tại giao diện[cite: 13]. | Nếu suy ra từ cảm biến áp suất nguồn qua mô hình truyền tải, phải ghi nhận là đại lượng suy ra/thay thế, không coi là phép đo trực tiếp trên từng dây[cite: 13]. |
| $M$; $\kappa$ | $M$ đo bằng cảm biến mô men; $\kappa$ trích xuất trực tiếp từ trường hình dạng (như camera/DIC) theo định nghĩa hình học[cite: 13]. | Suy $M$ từ lực $F$ cần sơ đồ tải và cánh tay đòn; suy $\kappa$ từ độ võng $\delta$ cần giả thiết đường đàn hồi của dầm. Đường $F-\delta$ không tự động là $M-\kappa$[cite: 8, 13]. |
| $\mu$ và tham số giao diện | Là tham số nhận dạng trong mô hình tiếp xúc đã chọn từ phép thử ma sát độc lập có biết tải pháp tuyến[cite: 13, 34]. | Lực cản tổng hợp hoặc độ dốc đường cong uốn không thể nhận dạng duy nhất $\mu$ khi hợp lực pháp tuyến $N_i$ và đường truyền lực chưa xác định[cite: 13, 54]. |

---

## 2.3. Các cơ chế điều chỉnh độ cứng (Variable Stiffness) và kiến trúc Jamming

### 2.3.1. Phân loại các nguyên lý điều chỉnh độ cứng và kiến trúc kẹt cơ học

Trong lĩnh vực robot mềm và robot liên tục, các phương pháp điều chỉnh độ cứng được phân loại ở hai tầng: tầng nguyên lý vật lý cấp cao và tầng kiến trúc môi trường tiếp xúc [15][cite: 14, 74]. Ở tầng nguyên lý cấp cao, tổng quan của Fan và cộng sự phân biệt ba nhóm chính: (i) tạo lực đối kháng chủ động (như gân kéo hoặc truyền động chất lưu), (ii) thay đổi tính chất nội tại của vật liệu (như vật liệu đáp ứng nhiệt, từ trường), và (iii) thay đổi ràng buộc hoặc cấu hình cơ khí [15][cite: 14, 15, 74]. Khóa bằng ma sát (frictional locking) thuộc nhóm thay đổi ràng buộc cơ khí, trong đó lực ép pháp tuyến và ma sát tại giao diện tiếp xúc được dùng để hạn chế chuyển động trượt tương đối giữa các phần tử [12], [15][cite: 14, 73, 74].

Ở tầng kiến trúc kẹt cơ học (jamming), tùy thuộc vào hình thái của phần tử chịu tải, các hệ thống được chia thành ba họ chính: kẹt dây/sợi (wire/fiber jamming) [1], [15], [16], [18], kẹt lớp/tấm (layer/laminar jamming) [9], [10], [11], [12], [19] và kẹt hạt (granular jamming) [17], [20][cite: 14, 15, 19, 20, 73, 74]. Bảng 2.2 hệ thống hóa hai tầng phân loại này và làm rõ mối liên hệ với cấu hình bó dây TiNi của MP1[cite: 15, 16].

**Bảng 2.2.** Phân loại hai tầng các nguyên lý và kiến trúc điều chỉnh độ cứng trong robot liên tục[cite: 15, 16]

| Cấp phân loại | Nhóm hoặc kiến trúc | Mô tả cơ chế cơ học | Phương thức kích hoạt điển hình | Nguồn tiêu biểu |
| :--- | :--- | :--- | :--- | :--- |
| **Nguyên lý cấp cao** | Tạo lực đối kháng | Cơ cấu chấp hành tạo lực căng hoặc áp suất đối kháng lại tải trọng ngoài[cite: 15]. | Gân kéo (tendon), buồng chất lưu (fluidic)[cite: 15]. | [15][cite: 15] |
| **Nguyên lý cấp cao** | Vật liệu đáp ứng nhiệt | Thay đổi pha hoặc mô đun đàn hồi của vật liệu theo nhiệt độ để biến thiên độ cứng kết cấu[cite: 15]. | Gia nhiệt Joule, chất lưu nhiệt và làm nguội[cite: 15, 37, 38]. | [2], [15], [25][cite: 15, 27, 35] |
| **Nguyên lý cấp cao** | Thay đổi ràng buộc / khóa ma sát | Cơ cấu cơ khí hoặc lực ép ma sát hạn chế chuyển động tương đối giữa các phần tử[cite: 14, 15]. | Chân không, áp suất dương, lò xo SMA, tĩnh điện[cite: 15, 19, 34]. | [7], [12], [15][cite: 15, 34] |
| **Họ kiến trúc Jamming** | Kẹt sợi / Kẹt dây (Fiber / Wire jamming) | Các phần tử mảnh một chiều xếp dọc trục; tương tác sợi–sợi, dây–dây và dây–bao chi phối mức nén và trượt dọc[cite: 14, 15]. | Hút chân không trong bao kín hoặc túi khí áp suất dương[cite: 15, 17]. | [1], [15], [16], [18][cite: 15, 18, 19] |
| **Họ kiến trúc Jamming** | Kẹt lớp / tấm (Layer / Laminar jamming) | Các lá mỏng xếp chồng chuyển từ trạng thái trượt độc lập sang trạng thái ghép nối cùng chịu uốn[cite: 14, 15]. | Hút chân không hoặc túi áp suất dương trong khung định hình[cite: 15, 19]. | [9], [10], [11], [12], [19][cite: 15, 21, 25] |
| **Họ kiến trúc Jamming** | Kẹt hạt (Granular jamming) | Môi trường hạt rời rạc bị nén chặt trong bao không dãn, làm tăng sức kháng cắt của mạng tiếp xúc hạt–hạt[cite: 15, 16, 20]. | Hút chân không hoặc bóng cao su áp suất dương ở tâm[cite: 15, 16, 20]. | [17], [20], [25][cite: 16, 22, 35] |

### 2.3.2. Kiến trúc kẹt dây và kẹt sợi (Wire/Fiber Jamming)

Khác với chồng lớp phẳng, môi trường kẹt dây và sợi bao gồm nhiều phần tử mảnh có tiết diện cong hoặc đa giác xếp cạnh nhau; do đó, khả năng chống uốn phụ thuộc mạnh vào cách sắp xếp tiết diện (packing topology), độ rỗng, tương tác dây–dây và tương tác giữa dây với lớp bao ngoài (sleeve) [16], [18][cite: 16, 74].

Brancadoro và cộng sự khảo sát sự phụ thuộc của cơ chế kẹt sợi vào hình thái ghép nối trong một mô-đun thao tác phẫu thuật bằng silicone (chiều dài $50\text{ mm}$, đường kính ngoài $14,5\text{ mm}$) [18][cite: 16, 74]. Tác giả so sánh hai thiết kế dùng sợi cotton phủ sáp (waxed cotton) bố trí dạng răng lược đan xen nhau: Mô-đun A lấp đầy kênh trung tâm bằng sợi, trong khi Mô-đun B duy trì một lòng rỗng trung tâm đường kính $4,5\text{ mm}$ [18][cite: 16, 18]. Khi hút chân không (áp suất tuyệt đối giảm từ $1,01325\text{ bar}$ xuống $0,1\text{ bar}$), lực cản cực đại ở cấp mô-đun tăng từ $+43\%$ đến $+377,5\%$ tùy theo tổ hợp vật liệu sợi (nylon, PTFE, PVC, silicone, da, cotton phủ sáp) và kiểu xếp bó hay kiểu lược [18][cite: 16, 52]. Nghiên cứu này chứng minh vai trò quyết định của hình thái sắp xếp sợi và hoàn thiện bề mặt đối với khả năng truyền tải, dù đại lượng báo cáo chỉ là tỷ lệ lực cực đại toàn cục ($F_{\max,\text{jammed}}/F_{\max,\text{unjammed}}$) mà chưa đo độc lập lực tiếp xúc cục bộ [18][cite: 16, 52].

Ở một kiến trúc gần với bó dây hơn, Bai và cộng sự khảo sát các phần tử dây giấy kraft, dây gai dầu và dây nylon không dãn (đường kính khoảng $1\text{ mm}$, chiều dài $140–150\text{ mm}$, chiều dày kết cấu $6\text{ mm}$) đặt trong bao HDPE hàn kín khí với tiết diện chữ nhật hoặc tròn [16][cite: 16, 52, 74]. Dưới tác dụng của chân không (đến $-85\text{ kPa}$), đáp ứng lực – độ võng khi uốn ba điểm và mô men – góc xoay khi xoắn được chia thành ba miền: tiền trượt (pre-slip) với độ cứng cao và quan hệ gần tuyến tính; chuyển tiếp (transition) với độ dốc suy giảm phi tuyến khi các dây bắt đầu trượt và tái sắp xếp cục bộ; và hậu trượt (post-slip/full slip) khi độ dốc tiệm cận trạng thái chưa hút chân không [16][cite: 16, 43, 61]. Bài báo cũng tích hợp bộ phận kẹt dây với bộ chấp hành khí nén áp suất dương để tách bạch chức năng tạo chuyển động uốn và chức năng khóa độ cứng [16][cite: 61, 62].

Thay vì dùng chân không, Zhang và Yao đã phát triển một chuỗi khớp biến thiên độ cứng dựa trên bó $700\text{ sợi nylon}$ (đường kính $0,4\text{ mm}$) đặt trong mắt xích nhựa cứng và được ép bởi một bóng polyethylene dày $0,1\text{ mm}$ bơm áp suất dương từ $0$ đến $300\text{ kPa}$ [1][cite: 23, 43, 44, 73]. Trong phép thử uốn ba điểm (nhịp $100\text{ mm}$, $5\text{ lần lặp}$ cho mỗi mức áp suất ở cả hai phương uốn), tác giả giả thiết áp suất bóng truyền trực tiếp thành áp suất kẹt thủy tĩnh hiệu dụng $p$ và thiết lập ba miền trạng thái theo lực cắt ngang quy đổi $Q = F/2$ [1][cite: 23, 44]:

$$\tau_{\max}(Q) = \mu p \quad (2.1)$$

$$Q_J = k \mu p \quad (2.2)$$

$$Q_S = A \mu p \quad (2.3)$$

trong đó $\tau_{\max}(Q)$ là ứng suất cắt cực đại trên tiết diện ($\text{Pa}$), $\mu$ là hệ số ma sát tĩnh liên sợi, $k$ là hệ số hình học có thứ nguyên diện tích ($\text{m}^2$) và $A$ là tổng diện tích tiết diện các sợi ($\text{m}^2$) [1][cite: 23, 44]. Hệ ở trạng thái kẹt hoàn toàn khi $Q < Q_J$, ở miền chuyển tiếp trượt một phần khi $Q_J \le Q \le Q_S$, và trượt toàn phần khi $Q > Q_S$ [1][cite: 23]. Trong miền chuyển tiếp, mô men quán tính hiệu dụng được nội suy theo quy luật bậc hai mang tính hiện tượng luận [1][cite: 23, 59]. Từ dữ liệu uốn thực nghiệm, nhóm tác giả nhận dạng mô đun hiệu dụng $E = 4,85\text{ GPa}$ (tại $p = 0$) và hệ số ma sát hiệu dụng $\mu = 0,3665$ từ độ dốc hồi quy $Q_S - p$ (đạt $R^2 = 0,817$), trong khi hồi quy ngưỡng khởi phát trượt $Q_J - p$ chỉ đạt $R^2 = 0,4311$ và $0,4475$ theo hai phương uốn do hiện tượng truyền áp suất không đồng đều, nén cục bộ của túi khí và sự xê dịch cách xếp bó sợi [1][cite: 23, 44].

### 2.3.3. Nhóm đối chứng: Kẹt lớp/tấm (Layer Jamming) và Kẹt hạt (Granular Jamming)

Các nghiên cứu về kẹt lớp và kẹt hạt đóng vai trò nhóm đối chứng quan trọng để làm rõ sự khác biệt về hình thái mặt tiếp xúc, sự lan truyền vùng trượt và cơ chế truyền áp suất dương/âm[cite: 16, 19, 20]:

* **Cơ học trượt trong kẹt lớp chân không:** Narang, Vlassak và Howe kết hợp mô hình dầm giải tích hai lớp (Euler–Bernoulli), mô phỏng phần tử hữu hạn (FE) và thí nghiệm uốn ba điểm trên chồng lớp giấy ($5, 10, 15$ và $20\text{ lớp}$) dưới độ lớn chân không $0, 24, 47$ và $71\text{ kPa}$ [9][cite: 22, 43, 73]. Nghiên cứu chỉ ra rằng vùng trượt khởi phát tại vị trí ứng suất cắt dọc đạt giới hạn ma sát (gần ngàm trong dầm công xôn) rồi lan dần theo chiều dài và chiều dày khi tải tăng; kết quả FE khớp tốt với thực nghiệm ($R^2 \ge 0,9879$, độ lệch cực đại $0,24\text{ N}$) [9][cite: 22, 43, 50]. Phát triển chi tiết hơn cho cấu hình uốn ba điểm, Caruso và cộng sự thử nghiệm mẫu giấy chữ nhật ($b = 6\text{ cm}, L = 18\text{ cm}$, dày $0,1\text{ mm}$, từ $8$ đến $20\text{ lớp}$ ở $24, 48$ và $68\text{ kPa}$) và chứng minh rằng giao diện trung tâm đạt ngưỡng trượt trước tiên trước khi lan ra các lớp ngoài; tuy nhiên, mô hình giải tích bắt đầu lệch khỏi thực nghiệm ở độ võng lớn do bỏ qua ứng suất tiếp xúc cục bộ phát sinh tại gối tựa [10][cite: 9, 25, 48, 73].
* **Mô hình môi trường liên tục khi số lớp lớn:** Khi số lớp tăng cao và chiều dày mỗi lớp rất nhỏ so với tổng chiều cao dầm, Zhang và cộng sự đề xuất mô hình đồng nhất hóa liên tục (continuum-based model) cho dầm kẹt lớp, được kiểm tra qua FE ($10$ và $25\text{ lớp}$) và thí nghiệm công xôn $20\text{ tấm PVC}$ ở chân không $60\text{ kPa}$ [11][cite: 25, 62, 65, 73]. Dù đường lực – độ võng lý thuyết nằm trong dải $\pm 1\text{ độ lệch chuẩn}$ của thí nghiệm, chính nhóm tác giả chỉ ra rằng việc bỏ qua ứng suất pháp theo phương chiều dày làm mô hình dự báo vùng trượt rộng hơn thực tế và gây sai lệch ở vùng biên ngàm cũng như khi trượt lớn [11][cite: 25, 62, 65]. Ở cấp độ điều khiển robot liên tục sử dụng vỏ kẹt lớp ($3$ đến $5\text{ lớp}$ dưới chân không $0–80\text{ kPa}$), chuỗi công trình của Fan, Yi và Liu đã phát triển từ mô hình dầm tương đương định tính [28] sang mô hình xét ma trận độ cứng và khóa hình dạng với lực pháp tuyến gộp tỷ lệ tuyến tính với chân không [29], và gần nhất là mô hình cho phép hệ số đàn hồi phụ thuộc phi tuyến vào áp suất [30][cite: 48, 55, 62, 65, 75].
* **Kẹt lớp và kẹt hạt dưới áp suất dương và nguồn áp kép:** Crowley, Zeng và Su triển khai kẹt lớp áp suất dương bằng cách dùng túi khí TPU ép các lớp Mylar vào khung cứng PETG phân đoạn trong một ngón kẹp mềm [19][cite: 19, 43, 74]. Ở áp suất $10\text{ psi}$ ($69,0\text{ kPa}$), độ cứng suy giảm do trượt sau khoảng $2\text{ mm}$ chuyển vị, trong khi ở $45\text{ psi}$ ($310,3\text{ kPa}$) không quan sát thấy điểm gãy trượt rõ rệt trong hành trình $6\text{ mm}$; lực kéo giữ vật của bộ kẹp bão hòa ở khoảng $80\text{ N}$ tại $241,3\text{ kPa}$ [19][cite: 43, 62]. Đối với môi trường hạt dưới áp suất dương (PPJ), Liu và cộng sự đặt bóng cao su ở tâm lớp hạt SMP bao bởi ống vải không dãn (đường kính ngoài $D = 26–35\text{ mm}$, đường kính trong $d = 10–15\text{ mm}$, dài $50\text{ mm}$) [17][cite: 15, 20, 52, 54, 74]. Khi bơm áp suất dư $69, 103, 138$ và $172\text{ kPa}$, độ cứng công xôn tính trong $1\text{ mm}$ đầu hành trình tăng tương ứng từ $0,69$ lên $1,72; 2,75$ và $4,02\text{ N/mm}$ [17][cite: 23, 52]. Trong một thiết kế tích hợp khác, Huynh và cộng sự dùng vi bơm chất lưu điện liên hợp (ECF) hai chiều để vừa tạo áp suất âm danh định ($-10$ đến $-50\text{ kPa}$) làm kẹt hạt $\text{Al}_2\text{O}_3$ trong khoang PDMS (giúp lực cản ở độ võng $3\text{ mm}$ tăng từ $0,134\text{ N}$ lên $0,743\text{ N}$, tức gấp $5,5\text{ lần}$), vừa tạo áp suất dương làm uốn cấu trúc Pneu-Net [20][cite: 20, 37, 55, 74].

### 2.3.4. Tổng hợp so sánh các kiến trúc Jamming

Bảng 2.3 tổng hợp trực diện các thông số cấu hình, phương thức kích hoạt, đại lượng đo và giới hạn mô hình của các công trình jamming trọng tâm để định vị bài toán bó dây TiNi của MP1[cite: 18, 21, 24, 26].

**Bảng 2.3.** Tổng hợp so sánh các nghiên cứu thực nghiệm và mô hình hóa kiến trúc Jamming tiêu biểu[cite: 18, 21, 24]

| Nghiên cứu & Kiến trúc | Cấu hình mẫu & Môi trường tiếp xúc | Phương thức kích hoạt áp suất | Đại lượng quan sát & Mô hình hóa | Phạm vi kiểm chứng & Giới hạn chuyển giao sang MP1 |
| :--- | :--- | :--- | :--- | :--- |
| **Brancadoro và cs. (2019) [18]**<br>*(Fiber jamming)* | Mô-đun silicone ($L=50\text{ mm}, D=14,5\text{ mm}$); sợi cotton phủ sáp, nylon, PVC... xếp kiểu bó hoặc răng lược[cite: 16, 18, 52]. | Chân không ($0,1\text{ bar}$ tuyệt đối so với khí quyển $1,01325\text{ bar}$)[cite: 52]. | Lực cản cực đại ở tư thế thẳng và cong; tỷ số tăng lực $+43\%$ đến $+377,5\%$[cite: 16, 18, 52]. | Chỉ báo cáo tỷ số lực cực đại cấp mô-đun; không có mô hình truyền áp hoặc đo lực tiếp xúc cục bộ giữa các sợi[cite: 18, 52]. |
| **Bai và cs. (2022) [16]**<br>*(Wire jamming)* | Dây kraft, gai dầu, nylon ($d \approx 1\text{ mm}, L=140–150\text{ mm}$) trong bao HDPE chữ nhật/tròn[cite: 16, 18, 52]. | Chân không ($0$ đến $-85\text{ kPa}$) kết hợp buồng uốn áp suất dương[cite: 16, 61]. | Lực–độ võng (uốn 3 điểm) và mô men–góc xoay (xoắn); phân 3 miền pre-slip, transition, post-slip[cite: 16, 18, 43, 52]. | Phân miền dựa trên đồ thị toàn cục; chưa có mô hình định lượng nối áp suất với ứng suất tiếp xúc dây–dây và dây–bao[cite: 16, 43, 45]. |
| **Zhang và Yao (2026) [1]**<br>*(Positive-pressure fiber jamming)* | Bó $700\text{ sợi nylon}$ ($d=0,4\text{ mm}$) trong mắt xích cứng; bóng PE dày $0,1\text{ mm}$ ép từ đáy[cite: 23, 43, 44]. | Áp suất dương trong bóng khí ($0–300\text{ kPa}$)[cite: 19, 23, 44]. | Uốn 3 điểm (nhịp $100\text{ mm}$); mô hình ngưỡng $Q_J, Q_S$ và nội suy bậc hai mô men quán tính hiệu dụng[cite: 23, 44, 59]. | $E$ và $\mu$ là tham số hiệu dụng khớp trên 1 nguyên mẫu; $R^2(Q_J-p)$ thấp ($0,43–0,45$) do truyền áp không đều và xếp bó xê dịch[cite: 23, 24, 44]. |
| **Narang và cs. (2018) [9]**<br>*(Vacuum layer jamming)* | Chồng $5, 10, 15, 20\text{ lớp giấy}$ trong bao kín khí[cite: 18, 22, 43]. | Chân không ($0, 24, 47, 71\text{ kPa}$)[cite: 22, 43]. | Mô hình dầm elastica 2 lớp, FE nhiều lớp và uốn 3 điểm ($R^2 \ge 0,9879$)[cite: 22, 24, 43, 50]. | Tiếp xúc phẳng lớp–lớp dưới áp suất âm đồng nhất; hệ số ma sát trong FE là đầu vào giả định, không đo độc lập[cite: 24, 43, 45]. |
| **Caruso và cs. (2023) [10]**<br>*(Vacuum layer jamming)* | Mẫu giấy chữ nhật ($6\times 18\text{ cm}$, dày $0,1\text{ mm}$), $8–20\text{ lớp}$[cite: 25]. | Chân không ($24, 48, 68\text{ kPa}$)[cite: 25]. | Giải tích 4 lớp (trượt từ tâm ra ngoài), FE và uốn 3 điểm; đo năng lượng tiêu tán[cite: 25, 48]. | Sai lệch giải tích tăng ở độ võng lớn do bỏ qua tập trung ứng suất tiếp xúc tại các gối đỡ[cite: 25]. |
| **Zhang và cs. (2025) [11]**<br>*(Continuum layer jamming)* | Dầm công xôn $20\text{ lớp PVC}$ trong màng bọc PVC (và FE $10, 25\text{ lớp}$)[cite: 25, 62]. | Chân không ($60\text{ kPa}$)[cite: 25, 62]. | Mô hình đồng nhất hóa môi trường liên tục theo chiều dày (tương tự đàn–dẻo)[cite: 10, 25, 65]. | Yêu cầu tỷ số chiều dày lớp nhỏ và số lớp lớn ($\ge 10$); lệch ở gần biên ngàm và khi trượt lớn do bỏ qua ứng suất pháp theo chiều dày[cite: 25, 65]. |
| **Crowley và cs. (2022) [19]**<br>*(Positive-pressure layer jamming)* | Các lớp Mylar trong khung cứng PETG phân đoạn và túi khí TPU (ngón kẹp)[cite: 19, 21, 43]. | Áp suất dương ($10–45\text{ psi}$, tức $69–310,3\text{ kPa}$)[cite: 43]. | Lực–chuyển vị cấp ngón kẹp (biên độ $6\text{ mm}$) và lực kéo bật ống bìa (bão hòa ở $80\text{ N}$)[cite: 43, 62]. | Đáp ứng gắn chặt với hình học khung phân đoạn và bài toán giữ vật; không đo trượt cục bộ giữa các lớp[cite: 20, 21, 45, 62]. |
| **Liu và cs. (2021) [17]**<br>*(Positive-pressure granular jamming)* | Bóng cao su ở tâm, hạt SMP bao quanh, vỏ vải không dãn ($D=26–35\text{ mm}, L=50\text{ mm}$)[cite: 15, 20, 52, 54]. | Áp suất dương trong bóng cao su ($69–172\text{ kPa}$)[cite: 23, 24, 52]. | Uốn công xôn; độ cứng lấy ở $1\text{ mm}$ đầu ($0,69–4,02\text{ N/mm}$); mô hình tiết diện vành khăn với $E_{\text{eq}}$[cite: 23, 52, 54, 59]. | $E_{\text{eq}}$ là tham số hiệu dụng gộp cả mạng hạt, bóng cao su và vỏ vải; giả định kẹt hoàn toàn ngay từ đầu dù hạt đã trượt vi mô[cite: 23, 24, 54, 59]. |

Từ Bảng 2.3 có thể rút ra kết luận tổng hợp cho nhóm nghiên cứu jamming: mặc dù nguyên lý tăng lực ép để mở rộng miền bám dính và trì hoãn trượt ma sát là điểm chung của mọi kiến trúc, nhưng ánh xạ định lượng từ áp suất nguồn đến lực pháp tuyến giao diện và ngưỡng trượt lại phụ thuộc tuyệt đối vào hình thái tiếp xúc (phẳng, hạt rời rạc hay bó trụ tròn) và biên giam giữ[cite: 20, 24, 25]. Chưa có công trình nào trong nhóm jamming kết hợp cấu trúc bó dây kim loại chịu chuyển pha (như TiNi) với nguồn tạo áp suất dương và kiểm chứng tách biệt giữa đáp ứng vật liệu với trượt ma sát giao diện[cite: 24, 25, 26].

---

## 2.4. Vật liệu TiNi, cơ học ma sát bó dây và nguồn tạo áp bằng SMA

### 2.4.1. Chuyển pha cơ–nhiệt và đáp ứng siêu đàn hồi của TiNi

Trong cấu hình bó dây của MP1, hợp kim TiNi vừa là phần tử kết cấu chịu uốn vừa là vật liệu có khả năng chuyển pha trạng thái rắn giữa pha austenit (ổn định ở nhiệt độ cao/ứng suất thấp) và pha martensit (ổn định ở nhiệt độ thấp/ứng suất cao) [2][cite: 26, 73]. Tuỳ thuộc vào vị trí của các nhiệt độ chuyển pha so với nhiệt độ làm việc, vật liệu có thể biểu hiện hiệu ứng nhớ hình (shape memory effect – biến dạng tạo ở trạng thái martensit được phục hồi khi gia nhiệt vượt qua miền kết thúc austenit $A_f$) hoặc tính siêu đàn hồi (superelasticity – thu hồi biến dạng lớn trong một chu trình tải – dỡ tải gần đẳng nhiệt ở nhiệt độ trên $A_f$ nhờ chuyển pha cảm ứng bởi ứng suất) [2], [21][cite: 26, 27, 73, 74].

Chuỗi công trình thực nghiệm kinh điển của Reedlunn, Daly và Shaw (Phần I và Phần II) đã làm sáng tỏ sự tương tác phức tạp giữa bản chất chuyển pha của NiTi và kiến trúc hình học của cáp thông qua phép thử kéo gần đẳng nhiệt ở nhiệt độ phòng kết hợp đo trường biến dạng bằng tương quan ảnh số (DIC) và ảnh nhiệt hồng ngoại (IR) [2], [22][cite: 27, 73, 74]:

* **Ảnh hưởng của kiến trúc xoắn đến sự lan truyền chuyển pha:** Cáp $7\times 7$ (xoắn phải kiểu regular lay, góc xoắn nông) có đáp ứng kéo chuẩn hóa khá gần với dây lõi đơn và tao lõi $1\times 7$, xuất hiện thềm ứng suất nằm ngang (stress plateau) rõ rệt đi kèm các mặt chuyển pha cục bộ lan truyền dọc cáp [2], [22][cite: 27, 28]. Ngược lại, cáp $1\times 27$ (có các lớp xoắn đảo chiều với góc xoắn sâu) cho đáp ứng tổng thể mềm hơn, độ dốc ổn định hơn và triệt tiêu hiện tượng mặt chuyển pha tập trung ở các lớp ngoài [2], [22][cite: 27, 28]. Nhóm tác giả cũng chỉ ra rằng mô hình kéo một trục đơn giản sẽ đánh giá quá cao ứng suất thềm nếu bỏ qua biến dạng uốn và xoắn cục bộ của từng sợi dây trong cáp [22][cite: 28].
* **Sự phụ thuộc vào lịch sử chu trình và ghép nối nhiệt–cơ:** Qua nhiều chu kỳ gia tải – dỡ tải, cáp NiTi xuất hiện sự suy giảm ứng suất thềm, thu hẹp diện tích vòng trễ và tích lũy biến dạng dư theo số chu kỳ [2][cite: 27, 63]. Đồng thời, tốc độ biến dạng quyết định mức độ giải phóng/hấp thụ ẩn nhiệt chuyển pha, làm thay đổi nhiệt độ cục bộ của dây và dịch chuyển ứng suất chuyển pha [2], [22][cite: 27].

Ở khía cạnh mô phỏng số, Vahidi và cộng sự đã xây dựng mô hình phần tử hữu hạn (FE) 3D trong Abaqus tích hợp mô hình vật liệu hiện tượng học Souza qua chương trình con UMAT cùng tiếp xúc mặt–mặt có ma sát cho cáp SMA $1\times 27$ và $7\times 7$ chịu kéo dọc trục [21][cite: 28, 32, 74]. Tương tự, Narjabadifam và cộng sự tiến hành thí nghiệm kéo/rung trên cáp thép và dùng Abaqus để mô phỏng đáp ứng chịu tải chu kỳ (hình sin và động đất El Centro) của cáp NiTi với tham số vật liệu lấy từ văn liệu [23][cite: 28, 74]. Bảng 2.4 tóm tắt phạm vi và giới hạn của nhóm nghiên cứu vật liệu và cáp TiNi[cite: 29].

**Bảng 2.4.** Tổng hợp các nghiên cứu về đáp ứng cơ–nhiệt và mô hình hóa cáp hợp kim nhớ hình NiTi[cite: 29]

| Nghiên cứu | Cấu trúc mẫu | Điều kiện cơ–nhiệt & Tải trọng | Đại lượng quan sát chính | Phương pháp & Giới hạn đối với bài toán MP1 |
| :--- | :--- | :--- | :--- | :--- |
| **Reedlunn và cs. (2013), Phần I [2]** | Cáp NiTi $7\times 7$ và $1\times 27$[cite: 27, 29]. | Kéo dọc trục tốc độ rất thấp (gần đẳng nhiệt) ở nhiệt độ phòng; lặp chu kỳ[cite: 27, 29]. | Lực – độ dãn dài, mô men xoắn phản lực, trường DIC/IR, diện tích vòng trễ[cite: 27, 29]. | Thực nghiệm kéo trực tiếp; chưa khảo sát tải uốn ngang hoặc lực ép giam giữ từ bên ngoài[cite: 28, 29]. |
| **Reedlunn và cs. (2013), Phần II [22]** | Dây lõi thẳng, tao lõi $1\times 7$ và các lớp của cáp $7\times 7, 1\times 27$[cite: 28, 29]. | Kéo gần tĩnh (quasi-static), hai đầu ngàm chống xoay[cite: 29]. | Đáp ứng phân cấp từng thành phần; suy ra đóng góp của các lớp ngoài bằng phép trừ[cite: 27, 28, 29]. | Làm rõ ảnh hưởng góc xoắn và uốn/xoắn cục bộ; phép trừ đại số có thể khuếch đại sai số thực nghiệm[cite: 27, 28, 29]. |
| **Vahidi và cs. (2022) [21]** | Cáp SMA $1\times 27$, $7\times 7$ (và cáp thép $1\times 37$ đối chứng)[cite: 29, 32]. | Mô phỏng kéo dọc trục ở cả miền siêu đàn hồi ($T > A_f$) và miền nhớ hình[cite: 27, 29, 32]. | Ứng suất pháp, ứng suất cắt, nhiệt độ và đường cong lực – chuyển vị kéo[cite: 29, 32]. | Mô phỏng Abaqus/UMAT 3D có tiếp xúc ma sát; không có thí nghiệm uốn và chưa tách riêng phần trễ vật liệu khỏi trễ ma sát[cite: 28, 29, 32, 33]. |
| **Narjabadifam và cs. (2024) [23]** | Cáp thép (thực nghiệm) và cáp NiTi (mô phỏng)[cite: 28, 29]. | Kéo/rung bàn lắc cho thép; tải chu kỳ hình sin và El Centro cho NiTi trong FE[cite: 28, 29]. | Vòng trễ lực – chuyển vị và ứng suất – biến dạng theo chu kỳ[cite: 28, 29]. | Kết quả NiTi hoàn toàn là mô phỏng số với tham số kế thừa; không kiểm chứng thực nghiệm uốn bó dây NiTi[cite: 28, 29]. |

### 2.4.2. Cơ học bó dây song song, cáp xoắn và sự trượt tương đối khi uốn

Để liên kết biến dạng của từng sợi dây với độ cứng uốn của cả bó, các mô hình cơ học cáp đã phát triển theo hai hướng chính: quy đổi thành các lớp phẳng tương đương cho bó dây song song và mô hình dầm trục cong cho cáp xoắn [8], [13], [24][cite: 29, 30, 31, 73, 74]:

* **Mô hình dầm phân lớp cho bó dây song song:** Zhang và cộng sự (2018) mô hình hóa cáp gồm các dây tròn xếp sát nhau theo tiết diện lục giác (37, 55 và 61 dây) bằng cách quy đổi mỗi hàng dây có cùng tọa độ chiều cao thành một lớp chữ nhật tương đương (bảo toàn diện tích và chiều cao hàng) [8][cite: 29, 31, 73]. Các lớp được giả thiết có chung độ võng và độ cong nhưng được phép trượt dọc trục tương đối với nhau; lực cắt tương tác tại mặt phân cách được giả định tỷ lệ tuyến tính với độ trượt qua tham số độ cứng chống trượt $k$ [8][cite: 8, 31]. Đến năm 2021, nhóm tác giả mở rộng bài toán sang trạng thái ứng suất phẳng hai chiều giải bằng phương pháp không gian trạng thái (state-space method), trong đó mô đun đàn hồi của từng lớp được điều chỉnh theo bề rộng quy đổi [13][cite: 29, 31, 73]. Cả hai công trình đều hiệu chỉnh tham số $k$ từ dữ liệu uốn cáp chịu lực kéo dọc trục đã công bố của Chen (2015) [8], [13][cite: 31, 33]. Do đó, tham số $k$ thực chất là một độ cứng giao diện hiệu dụng gộp chung ảnh hưởng của vỏ bọc bảo vệ, lực siết dọc trục và hiệu ứng Poisson, chứ không phải là một định luật ma sát Coulomb phụ thuộc áp suất ngang độc lập [8], [13][cite: 31, 33].
* **Mô hình dầm Timoshenko và các cận động học cho cáp xoắn ngắn:** Barsi, Carboni và Lacarbonara (2025) nghiên cứu uốn chu kỳ gần tĩnh ($0,2\text{ Hz}$) trên hai mẫu cáp thép ngắn: mẫu R1 một tao ($61\text{ dây}$, cấu trúc $1+6+12+18+24$) và mẫu R2 bảy tao ($133\text{ dây}$, mỗi tao $1+6+12$) [24][cite: 30, 32, 74]. Mỗi sợi dây được mô hình hóa như một dầm Timoshenko trục cong có đưa vào biến dạng riêng (eigenstrain) để biểu diễn ba giả thuyết liên kết động học trên toàn tiết diện: bám dính hoàn toàn (perfect-stick), bám dính một phần (partial-stick) và trượt hoàn toàn (full-slip) [24][cite: 31, 32, 46]. Đối chiếu với thí nghiệm uốn cho thấy độ dốc nhánh tăng tải (mềm hơn) xấp xỉ với dự báo của giả thuyết full-slip, độ dốc ở đầu nhánh dỡ tải (cứng hơn) gần với giả thuyết partial-stick, trong khi giả thuyết perfect-stick dự báo độ cứng vượt quá thực tế rất nhiều [24][cite: 32, 46]. Công trình này cung cấp minh chứng thực nghiệm rõ ràng về việc sử dụng các trạng thái động học giới hạn để chặn khoảng độ cứng nhánh, dù mô hình tuyến tính từng chế độ này chưa dự báo được toàn bộ đường cong vòng trễ liên tục [24][cite: 32, 33].

Bảng 2.5 đối chiếu trực tiếp các phương pháp mô hình hóa tiếp xúc và trượt trong bó dây/cáp[cite: 33].

**Bảng 2.5.** So sánh các mô hình cơ học về tiếp xúc, trượt tương đối và đáp ứng uốn của bó dây và cáp[cite: 33]

| Nghiên cứu | Cấu trúc & Vật liệu | Giả thiết tiếp xúc & Mô hình hóa | Cơ sở kiểm chứng | Giới hạn khi áp dụng cho MP1 |
| :--- | :--- | :--- | :--- | :--- |
| **Zhang và cs. (2018) [8]** | Cáp dây thép song song ($37, 55, 61\text{ dây}$)[cite: 31, 33]. | Quy đổi hàng dây thành lớp phẳng; lực cản trượt tỷ lệ tuyến tính với độ trượt qua hệ số $k$[cite: 31, 33]. | Khớp tham số $k$ trên dữ liệu uốn có lực kéo dọc trục của Chen (2015)[cite: 31, 33]. | Hệ số $k$ tuyến tính gộp nhiều hiệu ứng; không phản ánh ngưỡng trượt Coulomb theo áp suất ngang[cite: 31, 33]. |
| **Zhang và cs. (2021) [13]** | Cáp dây song song quy đổi thành lớp phẳng[cite: 31, 33]. | Bài toán ứng suất phẳng 2D giải bằng không gian trạng thái; tương tác lớp tuyến tính[cite: 31, 33]. | Dùng lại dữ liệu Chen (2015) và kế thừa tham số hiệu chỉnh từ [8][cite: 31, 33]. | Không phân giải tiếp xúc điểm/đường của dây tròn; trường ứng suất cục bộ chưa được đo kiểm chứng trực tiếp[cite: 31, 33]. |
| **Barsi và cs. (2025) [24]** | Cáp thép xoắn ngắn: R1 ($61\text{ dây}$) và R2 ($133\text{ dây}$)[cite: 30, 33]. | Dầm Timoshenko trục cong; gán đồng loạt 3 chế độ động học: perfect-stick, partial-stick, full-slip[cite: 31, 32, 33, 46]. | Thí nghiệm uốn chu kỳ ở $0,2\text{ Hz}$ và đối chiếu ngoài với dữ liệu kéo/xoắn của Utting & Jones[cite: 32, 33]. | Chỉ ước lượng độ dốc hai nhánh cực trị (đơn vị $\text{kN/mm}$); chưa mô phỏng quá trình chuyển tiếp trượt liên tục trong chu kỳ[cite: 32, 33]. |

### 2.4.3. Điều biến ma sát và phục hồi hình dạng bằng cơ cấu chấp hành SMA

Việc sử dụng hợp kim nhớ hình (SMA) để chủ động điều chỉnh ma sát hoặc kết hợp với cơ chế jamming đã được khám phá qua một số cấu hình tiên phong [7], [25], [26][cite: 34, 35, 73, 74, 75]:

* **Lò xo SMA siết hướng kính điều biến ma sát dây:** Jeon và cộng sự thiết kế thân robot mềm gồm lõi TPU ở tâm, $8\text{ dây xương sống}$ siêu đàn hồi chạy dọc xung quanh qua các đĩa dẫn hướng, một ống cao su bao ngoài đoạn giữa và một lò xo SMA quấn quanh ống cao su [7][cite: 34, 73]. Khi gia nhiệt bằng dòng điện $0,5\text{ A}$ để duy trì nhiệt độ lò xo ở $50–60^\circ\text{C}$ (so với trạng thái nguội $23^\circ\text{C}$), lò xo co về đường kính nhớ nhỏ hơn, ép chặt ống cao su vào các dây xương sống và cản trở chúng trượt qua đĩa [7][cite: 34]. Điểm giá trị của công trình là tác giả thực hiện phép thử kéo rút riêng $1\text{ dây}$ qua ống cao su (hành trình $5\text{ mm}$, tốc độ $10\text{ mm/phút}$, lặp $10\text{ lần}$) để đo lực ma sát trung bình, sau đó đưa lực này vào mô hình năng lượng (giả thiết trượt theo cung tròn) để dự báo độ cứng uốn của toàn thân robot có $8\text{ dây}$ [7][cite: 34]. Tuy nhiên, giao diện làm việc ở đây là dây – cao su (không phải dây – dây), lực pháp tuyến cục bộ không được đo độc lập, và thời gian đáp ứng bị giới hạn bởi chu trình nhiệt (nung nóng mất khoảng $18\text{ s}$, làm nguội tự nhiên mất khoảng $60\text{ s}$) [7][cite: 34, 36].
* **Kết hợp phần tử nhớ hình với kẹt hạt và ảnh hưởng của pha R:** Takashima, Imazawa và Cho kết hợp túi kẹt hạt cà phê dưới chân không (dưới $-90\text{ kPa}$, chiều dài làm việc $50\text{ mm}$) với phần tử nhớ hình đặt bên trong (nguyên mẫu 1 dùng $2\text{ tấm SMP}$, nguyên mẫu 2 dùng $4\text{ dây NiTi}$ thẳng đường kính $1\text{ mm}$) [25][cite: 35, 74]. Trong hệ này, chân không đảm nhận việc tăng độ cứng công xôn, còn việc gia nhiệt dây NiTi đảm nhận chức năng phục hồi hình dạng; tuy nhiên, nguyên mẫu SMA không trở lại hoàn toàn hình dạng ban đầu do sự cản trở và phân bố không đều của các hạt cà phê xung quanh [25][cite: 35]. Tiếp nối hướng này, Matsumoto và cộng sự khảo sát $4\text{ loại dây Ti–Ni}$ (đường kính $0,9\text{ mm}$, dài $70\text{ mm}$ của hãng Furukawa và Nilaco) có lịch sử xử lý nhiệt khác nhau dưới điện áp kích hoạt $0,5\text{ V}$ [26][cite: 35, 75]. Kết quả phân tích DSC và quay camera cho thấy các mẫu dây xuất hiện pha trung gian R (R-phase) có vận tốc phục hồi góc uốn $90^\circ$ nhanh hơn nhưng lại dừng cách vị trí ban đầu $10\text{ mm}$, khẳng định rằng tốc độ đáp ứng nhanh và biên độ phục hồi hoàn toàn là hai tiêu chí đánh đổi nhau phụ thuộc chặt vào trạng thái pha và lịch sử luyện chu kỳ (training) của dây TiNi [26][cite: 35, 36].

### 2.4.4. Cơ cấu bơm/piston dẫn động bằng SMA và đường truyền áp suất

Khi sử dụng SMA làm nguồn tạo áp suất chất lưu (như cấu hình SMA–piston của Bench B trong MP1), quá trình truyền năng lượng đi qua chuỗi: kích thích điện/nhiệt $\rightarrow$ chuyển pha SMA sinh lực và hành trình $\rightarrow$ dịch chuyển biên làm thay đổi thể tích buồng $\rightarrow$ nén chất lưu tạo áp suất và truyền tới mẫu[cite: 37]. Hai công trình tiêu biểu dưới đây cung cấp cơ sở cơ học để đánh giá khâu tạo áp bằng SMA [3], [27][cite: 37, 38, 73, 75]:

* **Điều kiện khả thi lưu lượng của bơm SMA ướt:** Pierce và Mascaro phát triển hệ bơm màng thể tích kiểu tịnh tiến dẫn động bằng dây SMA dài $40\text{ cm}$ đặt trong ống mềm có dòng nước nóng/lạnh chảy qua trực tiếp kết hợp trợ nhiệt điện [27][cite: 37, 38, 75]. Do hệ phải trích một phần lưu lượng đầu ra để tuần hoàn nuôi chính quá trình trao đổi nhiệt của dây SMA, điều kiện cần để hệ có lưu lượng dư cấp ra ngoài là $Q_{\text{out}} \ge Q_{\text{in}}$ (trong đó $Q_{\text{out}}$ là tổng lưu lượng thể tích bơm sinh ra và $Q_{\text{in}}$ là lưu lượng cần để duy trì chu trình chấp hành SMA, đơn vị $\text{m}^3/\text{s}$) [27][cite: 37, 38]. Với thời gian cấp dòng $1,5\text{ s}$ và bổ sung nhiệt liên tục cho bình nóng, hệ đạt tỷ số $Q_{\text{out}}/Q_{\text{in}} = 2,1$ và lưu lượng thuần $66\text{ mL/phút}$ [27][cite: 38]. Công trình chỉ ra sự đánh đổi cốt lõi của chấp hành SMA: tăng đường kính dây giúp tăng lực nhưng làm chậm truyền nhiệt, trong khi tăng chiều dài dây giúp tăng hành trình nhưng làm tăng thể tích chất lưu tiêu thụ và tổn thất nhiệt [27][cite: 39].
* **Cân bằng lực – chuyển vị và cột áp tĩnh trong vi bơm lò xo SMA:** Kotb, Elgamal và Serry chế tạo bơm vi mô gồm lò xo NiTi quấn quanh vỏ ống silicone đàn hồi [3][cite: 38, 73]. Khi gia nhiệt Joule (dòng cực đại $790\text{ mA}$), lò xo chuyển sang pha austenit và co lại, thắng lực đàn hồi của vỏ silicone để nén buồng (thể tích đẩy mục tiêu $43\text{ mm}^3$ mỗi hành trình) và tạo ra cột áp tĩnh $6,5\text{ kPa}$; khi ngắt điện, lực đàn hồi của vỏ silicone kéo lò xo giãn ra ở pha martensit để hút chất lưu cho chu kỳ kế tiếp [3][cite: 38]. Mô hình thiết kế của tác giả xác định hai điểm mút hành trình dựa trên giao điểm giữa đường đặc tính lực – chuyển vị của lò xo SMA (ở hai pha thuần túy) và đường độ cứng tuyến tính của vỏ silicone [3][cite: 38]. Tuy nhiên, tại chính điểm giao cân bằng tĩnh ở cuối hành trình, lực lò xo bằng lực đàn hồi của vỏ nên chênh lệch lực dẫn động chất lưu bằng không; mặt khác, mô hình hai điểm mút này bỏ qua sức cản thủy lực trong suốt quá trình nén động [3][cite: 38].

Bảng 2.6 tổng hợp các nghiên cứu sử dụng SMA để điều biến ma sát và tạo áp suất chất lưu[cite: 36, 39].

**Bảng 2.6.** Tổng hợp các cơ cấu dùng SMA điều biến ma sát và dẫn động nguồn áp suất[cite: 36, 39]

| Nghiên cứu | Cấu trúc chấp hành SMA | Cơ chế truyền lực / Truyền áp suất | Đại lượng đo & Kết quả chính | Giới hạn khi đối chiếu với hệ SMA–piston (MP1) |
| :--- | :--- | :--- | :--- | :--- |
| **Jeon và cs. (2022) [7]** | Lò xo SMA quấn quanh ống cao su bao $8\text{ dây}$ xương sống[cite: 34, 36]. | Lò xo co hướng kính ($50–60^\circ\text{C}$) ép cao su vào dây, tăng lực ma sát cản trượt[cite: 34, 36]. | Đo lực rút $1\text{ dây}$ và độ cứng uốn công xôn; thời gian nung $18\text{ s}$, nguội $60\text{ s}$[cite: 34, 36]. | Tác động siết trực tiếp (không qua chất lưu/piston); giao diện là dây–cao su, không đo tải pháp tuyến độc lập[cite: 34, 36, 66]. |
| **Takashima và cs. (2022) [25]** | $4\text{ dây NiTi}$ ($d=1\text{ mm}$) đặt trong túi silicone chứa hạt cà phê[cite: 35, 36]. | Chân không ($<-90\text{ kPa}$) tạo kẹt hạt; gia nhiệt NiTi tạo mô men phục hồi hình dạng[cite: 35, 36]. | Độ cứng uốn công xôn ($L=50\text{ mm}$) và quỹ đạo phục hồi qua các chu kỳ[cite: 35, 36]. | Phục hồi hình dạng không hoàn toàn do hạt cản trở; không tách riêng trễ của dây NiTi, màng bao và hạt[cite: 35, 36]. |
| **Matsumoto và cs. (2024) [26]** | $4\text{ mẫu dây Ti–Ni}$ ($d=0,9\text{ mm}, L=70\text{ mm}$) có xử lý nhiệt khác nhau[cite: 35, 36]. | Kích hoạt điện áp $0,5\text{ V}$ cho dây uốn $90^\circ$ phục hồi tự do và trong cơ cấu[cite: 35, 36]. | Phân tích DSC (pha R) và đo vận tốc phục hồi đầu dây bằng camera[cite: 35, 36]. | Dây có pha R phục hồi nhanh hơn nhưng còn độ lệch dư $10\text{ mm}$; chưa khảo sát bài toán tạo áp suất nén[cite: 36]. |
| **Pierce & Mascaro (2013) [27]** | Dây SMA ướt dài $40\text{ cm}$ dẫn động đòn bẩy bơm màng[cite: 37, 38, 39]. | Dòng nước nóng/lạnh và điện làm co dây SMA, dẫn động buồng bơm qua van 1 chiều[cite: 37, 39]. | Điều kiện $Q_{\text{out}} \ge Q_{\text{in}}$; đạt tỷ số lưu lượng $2,1$ và lưu lượng thuần $66\text{ mL/phút}$[cite: 37, 38, 39]. | Hệ bơm màng tuần hoàn lưu chất hở; khác với cơ cấu piston nén buồng kín giữ áp tĩnh của MP1[cite: 37, 39]. |
| **Kotb và cs. (2021) [3]** | Lò xo NiTi quấn quanh vỏ buồng bằng silicone đàn hồi[cite: 38, 39]. | Gia nhiệt Joule ($790\text{ mA}$) làm lò xo nén vỏ đẩy lưu chất; vỏ đàn hồi tự hồi vị khi nguội[cite: 38, 39]. | Đồ thị cân bằng lực lò xo – vỏ; thể tích đẩy $43\text{ mm}^3$, cột áp tĩnh $6,5\text{ kPa}$[cite: 38, 39]. | Vỏ vừa là buồng chứa vừa là lò xo hồi vị; mô hình hai đầu mút bỏ qua quá trình quá độ và tải chất lưu động[cite: 38, 39, 66]. |

Đối với một cơ cấu SMA–piston dẫn động buồng kín (như định hướng Bench B của MP1), các tiền lệ trên cho thấy không thể ghép lực khóa cực đại (blocking force) với hành trình tự do cực đại (free stroke) thành một điểm làm việc duy nhất[cite: 39]. Ngoài ra, khi chuyển từ dịch chuyển hình học của piston sang áp suất thực tế tại mẫu ($p_{\text{near\_sample}}$), hệ thống thực nghiệm phải kiểm soát được ma sát phớt làm kín, độ mềm (compliance) của thành buồng và ống dẫn, tính nén được của môi chất, hiện tượng rò rỉ cũng như sự trễ nhiệt giữa chu trình gia nhiệt và làm nguội của phần tử SMA [3], [20], [27][cite: 39, 40].

---

## 2.5. Mô hình cơ học, phép đo và khả năng nhận dạng tham số

### 2.5.1. Ràng buộc ma sát Coulomb và hai cận độ cứng uốn tham chiếu

Để nối kết tải ép pháp tuyến với khả năng truyền lực cắt dọc trục giữa các dây trong bó mà không rơi vào việc khớp đường cong thuần túy hiện tượng luận, mô hình cơ học cần xuất phát từ điều kiện ma sát Coulomb ở hai cấp độ[cite: 42]:

* **Ở cấp độ hợp lực trên miền tiếp xúc:** Khi không có lực bám dính pháp tuyến, lực tiếp tuyến thực tế $F_t$ ($\text{N}$) tại một giao diện chịu lực pháp tuyến nén $N$ ($\text{N}$) chỉ duy trì trạng thái bám dính (stick) khi thỏa mãn bất đẳng thức[cite: 42]:

$$|F_t| \le \mu_s N \quad (2.4)$$

* **Ở cấp độ ứng suất cục bộ tại điểm $x$ trên giao diện:** Ứng suất tiếp tuyến $t_t(x)$ ($\text{Pa}$) và ứng suất pháp tuyến nén $p_n(x)$ ($\text{Pa}$) phải thỏa mãn[cite: 42]:

$$|t_t(x)| \le \mu_s p_n(x) \quad (2.5)$$

trong đó $\mu_s$ là hệ số ma sát tĩnh[cite: 42]. Ở trạng thái bám dính, $|F_t|$ (hoặc $|t_t(x)|$) được quyết định bởi điều kiện cân bằng cơ học và có thể nhỏ hơn giới hạn cực đại; chỉ tại thời điểm khởi phát trượt, lực tiếp tuyến mới chạm biên giới hạn[cite: 9, 42]. Khi giao diện đã chuyển sang trượt tương đối, ứng suất tiếp tuyến tuân theo luật ma sát động (với hệ số ma sát động $\mu_k$ không mặc nhiên bằng $\mu_s$ và có thể phụ thuộc vận tốc trượt cũng như lịch sử bề mặt)[cite: 42, 45].

Từ hai trạng thái động học giới hạn của giao diện (bỏ qua hoàn toàn truyền lực cắt dọc trục so với tương thích biến dạng dọc hoàn toàn trên toàn tiết diện), có thể thiết lập **hai cận độ cứng uốn tham chiếu có điều kiện** cho một bó gồm $n\text{ dây tròn đặc}$ thẳng, song song, biến dạng nhỏ theo lý thuyết dầm Euler–Bernoulli và làm việc trong miền đàn hồi tuyến tính với mô đun $E_i$ ($\text{Pa}$) ở trạng thái vật liệu xác định [24][cite: 46, 47]:

1. **Cận dưới tham chiếu – Các dây uốn độc lập ($B_{\text{ind}}$):** Khi bỏ qua hoàn toàn khả năng truyền lực cắt dọc trục tại mọi giao diện dây–dây và dây–ống bao, mỗi dây thứ $i$ (đường kính $d_i$, diện tích $A_i = \pi d_i^2/4$) tự uốn quanh trục trung hòa đi qua chính trọng tâm tiết diện riêng của nó[cite: 46, 47]:

$$I_{i,c} = \frac{\pi d_i^4}{64} \quad (2.6)$$

$$B_{\text{ind}} = \sum_{i=1}^{n} E_i I_{i,c} \quad (2.7)$$

2. **Cận trên tham chiếu – Tiết diện liên hợp lý tưởng ($B_{\text{bond}}$):** Khi lực cản ma sát tại các giao diện đủ lớn để khóa hoàn toàn trượt tương đối, buộc mọi sợi dây chia sẻ chung một độ cong và tuân theo quy luật biến dạng dọc tương thích phẳng trên toàn tiết diện, vị trí trục trung hòa chung $y_{\text{NA}}$ ($\text{m}$) và độ cứng uốn liên hợp được xác định theo định lý dời trục song song (Huygens–Steiner)[cite: 46, 47]:

$$y_{\text{NA}} = \frac{\sum_{i=1}^{n} E_i A_i y_i}{\sum_{i=1}^{n} E_i A_i} \quad (2.8)$$

$$B_{\text{bond}} = \sum_{i=1}^{n} E_i \left[ I_{i,c} + A_i (y_i - y_{\text{NA}})^2 \right] \quad (2.9)$$

trong đó $y_i$ là tọa độ trọng tâm của dây thứ $i$ theo phương vuông góc với trục uốn[cite: 47]. Thành phần chuyển trục $A_i(y_i - y_{\text{NA}})^2$ chính là nguồn gốc tạo nên sự gia tăng độ cứng uốn đột biến khi bó dây chuyển từ trạng thái rời rạc sang làm việc chung[cite: 47].

Bảng 2.7 tổng hợp các giả thiết và những điều kiện thực tế có thể làm dữ liệu thực nghiệm nằm ngoài khoảng kẹp $[B_{\text{ind}}, B_{\text{bond}}]$[cite: 48, 49].

**Bảng 2.7.** Giả thiết cơ học và điều kiện mất hiệu lực của các trạng thái độ cứng uốn tham chiếu[cite: 49]

| Trạng thái tham chiếu | Ràng buộc động học giao diện | Biểu thức độ cứng uốn ($\text{N}\cdot\text{m}^2$) | Các yếu tố thực tế làm mất hiệu lực của cận tham chiếu |
| :--- | :--- | :--- | :--- |
| **Dây độc lập ($B_{\text{ind}}$)** | Bỏ qua hoàn toàn truyền lực cắt dọc giữa các dây; mỗi dây uốn quanh trọng tâm riêng[cite: 46, 49]. | $B_{\text{ind}} = \sum_{i=1}^{n} E_i I_{i,c}$[cite: 47, 49] | Ma sát động còn dư vẫn truyền lực cản; ống bao (sleeve) hoặc đầu ngàm kẹp cưỡng bức biến dạng chung; dây bị xoắn/bện hoặc có lực căng trước[cite: 46, 48, 49]. |
| **Tiết diện liên hợp ($B_{\text{bond}}$)** | Không có trượt tương đối; biến dạng dọc trục tương thích phẳng trên toàn tiết diện[cite: 46, 49]. | $B_{\text{bond}} = \sum_{i=1}^{n} E_i \left[ I_{i,c} + A_i (y_i - y_{\text{NA}})^2 \right]$[cite: 47, 49] | Truyền lực cắt qua tiếp xúc đường của dây tròn không đủ lớn; áp suất phân bố không đều; chuyển pha TiNi làm $E_i$ giảm phi tuyến theo ứng suất/vị trí[cite: 48, 49]. |
| **Trượt một phần (Partial slip thực tế)** | Một số vùng hoặc một số cặp giao diện trượt trong khi phần còn lại vẫn bám dính[cite: 42, 49]. | Độ dốc tiếp tuyến $K_{t,M} = \text{d}M/\text{d}\kappa$ thay đổi theo nhánh tải và độ cong[cite: 49, 50]. | Phụ thuộc mạnh vào lịch sử đường tải, trễ chuyển pha TiNi và sự tái sắp xếp tiết diện bó dây khi uốn lớn[cite: 48, 49]. |

### 2.5.2. Quan hệ mô men – độ cong ($M-\kappa$), chỉ tiêu độ cứng và công tiêu tán vòng trễ

Trong thực nghiệm đánh giá kết cấu jamming và bó dây, cần chuẩn hóa các chỉ tiêu trích xuất từ đường cong đáp ứng để đảm bảo tính nhất quán về thứ nguyên[cite: 49, 50]:

* **Độ cứng tiếp tuyến và cát tuyến:** Trong mặt phẳng mô men – độ cong, độ cứng uốn tiếp tuyến cục bộ là $K_{t,M} = \text{d}M/\text{d}\kappa$ ($\text{N}\cdot\text{m}^2$), chỉ trùng với hằng số $B$ trong miền đàn hồi tuyến tính $M = B\kappa$[cite: 50]. Trong mặt phẳng lực – độ võng đầu mút, độ cứng tiếp tuyến là $K_{t,F} = \text{d}F/\text{d}\delta$ ($\text{N/m}$) và độ cứng cát tuyến giữa hai điểm trạng thái $(F_1, \delta_1)$ và $(F_2, \delta_2)$ trên cùng một nhánh tải là[cite: 50]:

$$K_{\text{sec}} = \frac{F_2 - F_1}{\delta_2 - \delta_1} \quad (2.10)$$

Khi mẫu tồn tại độ võng dư hoặc tải trọng đặt trước, điểm gốc $(F_1, \delta_1)$ phải được khai báo rõ theo trạng thái dỡ tải thay vì mặc định lấy tại $(0,0)$[cite: 50].

* **Công cơ học tiêu tán trên chu trình kín (Hysteresis loop area):** Với một chu trình gia tải – dỡ tải khép kín, năng lượng tiêu tán toàn cục được tính bằng tích phân đường có hướng trên cặp biến công liên hợp tương ứng (lực – độ võng $W_F$, mô men xoắn – góc xoay $W_T$, hoặc tích phân mô men – độ cong dọc theo chiều dài cung $s$ của dầm $W_{M\kappa}$)[cite: 51]:

$$W_F = \oint F\,\text{d}\delta; \quad W_T = \oint T\,\text{d}\theta; \quad W_{M\kappa} = \int_0^L \left( \oint M(s)\,\text{d}\kappa(s) \right) \text{d}s \quad (2.11)$$

Lưu ý rằng diện tích vòng trễ $\oint M\,\text{d}\kappa$ tại một tiết diện đơn lẻ có đơn vị là $\text{N}$ (tức năng lượng trên một đơn vị chiều dài $\text{J/m}$), chỉ sau khi tích phân dọc theo chiều dài chịu uốn $L$ mới cho tổng năng lượng tiêu tán tính bằng Joule ($\text{J}$)[cite: 51]. Trong bó dây TiNi bọc ống bao, $W_F$ hoặc $W_{M\kappa}$ là tổng hợp của tiêu tán ma sát trượt dây–dây, ma sát dây–ống bao, biến dạng trễ của vỏ bao và năng lượng tiêu tán nội tại do chuyển pha martensit thuận–nghịch của TiNi[cite: 51, 53].

### 2.5.3. Khả năng nhận dạng tham số (Identifiability), sự bù trừ tham số và độ không đảm bảo đo

Một thách thức phương pháp luận cốt lõi của bài toán MP1 là hiện tượng **bù trừ tham số (parameter compensation)** khi suy diễn cơ chế từ một đường cong đáp ứng toàn cục[cite: 54]. Cụ thể, trên đồ thị $F-\delta$ hoặc $M-\kappa$, sự gia tăng mô đun đàn hồi $E_i$ của dây TiNi có thể bị bù trừ bởi sự suy giảm diện tích truyền lực hoặc sự mềm đi của đồ gá/ống bao[cite: 54]. Tương tự, trong giới hạn trượt Coulomb $|F_t| = \mu N$, do đầu ra chỉ phụ thuộc vào tích số $\mu N$, một hệ số ma sát $\mu$ lớn đi kèm lực pháp tuyến $N$ nhỏ (do tổn thất truyền áp) sẽ tạo ra ngưỡng trượt giống hệt trường hợp $\mu$ nhỏ nhưng $N$ lớn nếu không có phép đo độc lập tách rời hai biến này[cite: 13, 54].

Do đó, cần phân biệt hai mức độ nhận dạng mô hình[cite: 55]:

1. **Nhận dạng cấu trúc (Structural identifiability):** Xét xem về mặt lý thuyết toán học, với tập biến đầu vào và đầu ra quan sát lý tưởng (không nhiễu), bộ tham số $\boldsymbol{\theta}$ của mô hình có được xác định duy nhất hay không[cite: 55].
2. **Nhận dạng thực dụng (Practical identifiability):** Xét xem với dữ liệu thực nghiệm hữu hạn, có nhiễu đo và tương quan, các tham số có thể ước lượng ổn định với khoảng tin cậy đủ hẹp hay không[cite: 55]. Công cụ đánh giá cục bộ là ma trận độ nhạy Jacobian $S_{ij} = \partial y_i / \partial \theta_j$ (biểu diễn đạo hàm của đại lượng quan sát $y_i$ theo tham số $\theta_j$)[cite: 56]. Nếu hai cột của ma trận $\mathbf{S}$ gần như phụ thuộc tuyến tính (song song), hai tham số tương ứng sẽ bù trừ lẫn nhau và không thể tách biệt nếu chỉ dùng tập quan sát đó[cite: 56].

Về mặt thống kê thực nghiệm, các công trình trước đây thường báo cáo độ phân tán dưới các dạng khác nhau: Liu và cộng sự dùng trung bình $8\text{ lần lặp}$ kèm dải khoảng tin cậy $95\%$ (nhưng không nêu rõ quy tắc phân bố) [17][cite: 52, 55, 56]; Narang và cộng sự [9], Zhang và cộng sự [11], Yi và cộng sự ($3\text{ lần lặp}$) [29] báo cáo dải $\pm 1\text{ độ lệch chuẩn (SD)}$[cite: 50, 55, 56, 62]; còn Zhang và Yao nội suy $5\text{ lần lặp}$ lên lưới $1000\text{ điểm}$ để hồi quy từng đoạn tìm ngưỡng trượt $F_J, F_S$ theo cực đại $R^2$ [1][cite: 55, 56]. Theo chuẩn đo lường GUM [14], độ lệch chuẩn của các lần lặp trên cùng một mẫu (repeatability) chỉ là một thành phần (Type A); độ không đảm bảo mở rộng $U = k u_c$ cần kết hợp cả độ phân giải thiết bị, bất định hiệu chuẩn cảm biến (Type B), độ tái lập giữa các mẫu khác nhau và xét đến hiệp phương sai khi các đại lượng dẫn xuất (như $M$ và $\kappa$) dùng chung kênh đo đầu vào[cite: 13, 56, 64].

### 2.5.4. So sánh các nhóm phương pháp mô hình hóa và chiến lược kiểm định $H_{0b}$

Bảng 2.8 tổng hợp ưu nhược điểm, yêu cầu tham số và phạm vi kiểm chứng của năm nhóm phương pháp tiếp cận để định hình chiến lược mô hình hóa cho MP1[cite: 60].

**Bảng 2.8.** So sánh năng lực mô tả, yêu cầu tham số và giới hạn kiểm chứng của các nhóm phương pháp[cite: 60]

| Nhóm phương pháp | Đại lượng và cơ chế mô tả được | Tham số đầu vào cần thiết | Chi phí thực hiện & Rủi ro mô hình | Vai trò và giới hạn đối với MP1 |
| :--- | :--- | :--- | :--- | :--- |
| **Dầm giải tích / Elastica rời rạc** ([9], [10], [24]) | Cân bằng lực–mô men, hình dạng uốn, ngưỡng khởi phát và sự lan truyền vùng trượt theo giao diện[cite: 58, 60]. | Hình học tiết diện, điều kiện biên, mô đun $E_i$, hệ số ma sát $\mu$ và tải pháp tuyến[cite: 58, 60]. | Chi phí tính toán thấp; dễ diễn giải vật lý nhưng phải lý tưởng hóa hình học tiếp xúc và phân bố áp suất[cite: 58, 60]. | Dùng để xây dựng hai cận tham chiếu ($B_{\text{ind}}, B_{\text{bond}}$) và mô hình đối chứng cơ sở[cite: 46, 60]. |
| **Đồng nhất hóa / Tham số hiệu dụng** ([8], [11], [17], [28]) | Đáp ứng toàn cục ($K, E_{\text{eq}}, B_{\text{eq}}$) hoặc trường ứng suất trung bình theo chiều dày khi số lớp lớn[cite: 59, 60]. | Tiết diện tương đương, giả thiết biến dạng nhỏ hoặc giới hạn lớp mỏng $\delta/h \ll 1$[cite: 25, 59, 60]. | Rất gọn nhẹ nhưng gộp chung nhiều cơ chế vi mô vào một tham số hiệu dụng; nguy cơ bù trừ tham số cao[cite: 54, 59, 60]. | Hữu ích để mô tả xu hướng cấp hệ thống; không tách riêng được tiếp xúc dây–dây và dây–ống bao[cite: 59, 60]. |
| **Mô hình rút gọn từng đoạn / Hiện tượng luận** ([1], [29], [30]) | Biến thiên độ cứng qua các miền trạng thái (stick, transition, slip) theo áp suất và lực cắt[cite: 59, 60]. | Các ngưỡng chuyển trạng thái ($Q_J, Q_S$) và hàm nội suy (như bậc hai hoặc phụ thuộc áp suất)[cite: 59, 60, 65]. | Khớp đường cong thực nghiệm tốt nhưng dễ bị quá khớp (overfitting) nếu không tách tập dữ liệu kiểm chứng[cite: 59, 60]. | Cung cấp khung tham chiếu để định nghĩa các ngưỡng chuyển miền trên đường cong $M-\kappa$ hoặc $F-\delta$[cite: 59, 60]. |
| **Phần tử hữu hạn (FE) 3D có tiếp xúc** ([9], [21], [23]) | Trường ứng suất–biến dạng 3D, tiếp xúc mặt–mặt của dây tròn/xoắn và chuyển pha vật liệu SMA[cite: 28, 59, 60]. | Hình học 3D chính xác, bộ tham số UMAT của TiNi, luật ma sát, lưới và điều kiện biên[cite: 28, 59, 60]. | Chi phí tính toán rất lớn, khó hội tụ khi số dây nhiều và trượt lớn; khó tách bạch nguồn gây trễ nếu thiếu đo đạc cục bộ[cite: 28, 59, 60]. | Công cụ tham chiếu chi tiết khi cần kiểm tra trường tiếp xúc cục bộ nhưng không thay thế kiểm chứng thực nghiệm[cite: 59, 60]. |
| **Thực nghiệm đặc trưng hóa tách lớp** ([2], [7], [14]) | Lực, chuyển vị, $M-\kappa$, áp suất gần mẫu, nhiệt độ, lực rút dây riêng lẻ và diện tích vòng trễ[cite: 34, 60]. | Hệ thống cảm biến đã hiệu chuẩn, quy trình lặp lại, kiểm soát lịch sử nhiệt và tải[cite: 60]. | Đòi hỏi thiết kế đồ gá chuẩn xác; phép đo toàn cục đơn lẻ không tự suy ra được ứng suất tiếp xúc cục bộ[cite: 56, 60]. | Cung cấp dữ liệu tách biệt cho bước hiệu chuẩn (calibration) và bước kiểm chứng độc lập (validation)[cite: 6, 60]. |

Từ sự phân tích trên, quy trình kiểm định mô hình trong MP1 (phục vụ RQ5) được thiết lập chặt chẽ theo nguyên tắc bác bỏ có điều kiện[cite: 1, 61]:

* **Mô hình đối chứng cạnh tranh ($H_{0b}$):** Kết hợp mô hình cấu thành TiNi có xét chuyển pha chuẩn với định luật ma sát tiếp xúc Coulomb thông thường, trong đó áp suất giam giữ $p(t)$ đóng vai trò điều kiện biên tác động từ bên ngoài và các tham số vật liệu, ma sát, truyền áp được khóa cố định thông qua các phép thử hiệu chuẩn độc lập[cite: 1, 61].
* **Điều kiện kiểm chứng và bác bỏ:** Sau khi khóa toàn bộ tham số trên tập dữ liệu hiệu chuẩn, mô hình $H_{0b}$ được dùng để dự báo tiến (forward prediction) trên các đường cong áp suất – độ cong thuộc tập dữ liệu giữ lại (hold-out validation set)[cite: 6, 61]. Chỉ khi phần dư sai lệch giữa dự báo của $H_{0b}$ và thực nghiệm có tính hệ thống, lặp lại và vượt ra ngoài dải độ không đảm bảo mở rộng $U$ (sau khi đã kiểm soát hiệu ứng biên, độ mềm ống bao, tổn thất truyền áp và nhiệt độ), nghiên cứu mới có cơ sở mở giả thuyết $H_1$ về sự tồn tại của một luật ghép nối cơ–nhiệt–ma sát mới giữa động học chuyển pha TiNi và trượt dính giao diện[cite: 61, 69]. Ngược lại, nếu $H_{0b}$ dự báo nằm trong dải bất định đo, kết quả khoa học xác lập chính là miền hiệu lực của cơ học tiếp xúc và vật liệu hiện hữu đối với cấu trúc bó dây TiNi[cite: 61, 69].

---

## 2.6. Tổng hợp khoảng trống nghiên cứu và tiêu chí chuyển giao sang Chương 3–4

### 2.6.1. Cơ sở kế thừa và khoảng trống nghiên cứu có thể kiểm chứng

Qua tổng quan 30 tài liệu tham khảo thuộc các nhánh cơ học liên quan, có thể khẳng định rằng từng mắt xích riêng lẻ của bài toán đã có tiền lệ nghiên cứu[cite: 61, 67, 73, 74, 75]:

* Nguyên lý điều chỉnh độ cứng bằng cách thay đổi lực ép pháp tuyến để kiểm soát quá trình chuyển tiếp từ bám dính (pre-slip/stick) sang trượt một phần (partial slip) và trượt toàn phần (full slip) đã được xác lập vững chắc trên chồng lớp phẳng [9], [10], [11], [12], [19], môi trường hạt [17], [20] và bó dây/sợi phi kim [1], [16], [18][cite: 61, 62, 67].
* Đáp ứng kéo gần đẳng nhiệt của cáp NiTi có xét chuyển pha [2], [22], mô hình phần tử hữu hạn cáp SMA chịu kéo [21] và các mô hình dầm phân lớp/dầm trục cong cho cáp thép chịu uốn [8], [13], [24] đã cung cấp nền tảng toán học để mô tả tương tác giữa các sợi dây[cite: 62, 63, 68].
* Khả năng sử dụng lò xo SMA để siết ma sát [7] hoặc nén buồng đàn hồi tạo áp suất bơm chất lưu [3], [27] cũng đã được chứng minh ở cấp độ nguyên mẫu[cite: 63, 69].

Tuy nhiên, khi đặt bài toán **bó dây nhiều phần tử bằng hợp kim TiNi chịu uốn dưới tác dụng của tải ép/áp suất dương và hướng tới tích hợp nguồn chấp hành SMA–piston (MP1)**, văn liệu hiện tại để lộ **bốn khoảng trống cơ học có thể kiểm chứng bằng thực nghiệm**[cite: 67, 68, 69]:

1. **Khoảng trống về giao diện chi phối và ánh xạ truyền tải áp suất trong bó dây kim loại tròn (gắn với RQ1 và RQ2):** Các mô hình kẹt lớp giả thiết tiếp xúc phẳng đồng nhất [9], [10], [11], trong khi mô hình bó sợi nylon áp suất dương của Zhang và Yao [1] gộp trực tiếp áp suất túi khí thành áp suất kẹt thủy tĩnh hiệu dụng và gặp độ phân tán lớn ở ngưỡng bắt đầu trượt ($R^2 \approx 0,43–0,45$)[cite: 23, 64, 65, 67]. Đối với bó dây tròn TiNi có độ cứng bản thân lớn hơn nhiều so với sợi polymer/nylon, chưa có nghiên cứu nào định lượng được đường truyền lực từ áp suất gần mẫu ($p_{\text{near\_sample}}$) qua lớp màng/ống bao đến tải pháp tuyến hữu hiệu tại các giao diện dây–dây và dây–ống bao, cũng như cách các ngưỡng trượt làm thay đổi đáp ứng mô men – độ cong $M-\kappa$[cite: 65, 67, 68].
2. **Khoảng trống về sự tương tác và tách bạch giữa trễ chuyển pha TiNi với trễ ma sát trượt dưới tải uốn (gắn với RQ2 và RQ5):** Các nghiên cứu về cáp NiTi của Reedlunn [2], [22] và Vahidi [21] chỉ dừng ở bài toán kéo dọc trục mà chưa xét tải uốn ngang kết hợp áp suất giam giữ mặt bên[cite: 28, 29, 66, 68]. Trong khi đó, các nghiên cứu uốn cáp thép của Zhang [8], [13] và Barsi [24] lại làm việc với vật liệu đàn hồi tuyến tính không có chuyển pha[cite: 31, 32, 66]. Chưa có bằng chứng thực nghiệm và mô hình kiểm chứng nào phân rã được đóng góp của quá trình chuyển pha TiNi (phụ thuộc nhiệt độ, tốc độ và lịch sử chu trình) với đóng góp của ma sát trượt giữa các dây trong vòng trễ uốn toàn cục[cite: 63, 68].
3. **Khoảng trống về đặc trưng nguồn áp suất SMA–piston làm việc với tải buồng kín và đối chiếu tương đương (gắn với RQ3 và RQ4):** Các công trình bơm SMA trước đây tập trung vào bài toán bơm lưu lượng tuần hoàn [27] hoặc nén vỏ ống silicone trong vi bơm truyền thuốc [3][cite: 37, 38, 66, 69]. Chưa có nghiên cứu nào đặc trưng hóa đầy đủ khả năng tạo, giữ và hồi áp suất theo thời gian của cơ cấu SMA–piston nén buồng giam giữ bó dây, cũng như thực hiện phép đối chiếu trực diện với nguồn áp suất ngoài tiêu chuẩn (Bench A so với Bench B) tại cùng lịch sử áp suất gần mẫu để cô lập ảnh hưởng của quá độ nhiệt, độ mềm nguồn và rò rỉ[cite: 1, 69, 71].
4. **Khoảng trống về kiểm chứng dự báo độc lập (Forward Validation) có kiểm soát độ không đảm bảo đo (gắn với RQ5):** Hầu hết các công trình kẹt dây/sợi và cáp hiện hữu đều nhận dạng tham số hiệu dụng ($E_{\text{eq}}, \mu_{\text{eq}}, k$) rồi đánh giá độ khớp ngay trên cùng một nguyên mẫu và cùng tập dữ liệu đó [1], [8], [13], [17][cite: 57, 65, 66]. Việc thiếu vắng quy trình khóa tham số độc lập và kiểm tra dự báo trên tập dữ liệu giữ lại kèm phân tích độ nhạy/bất định theo chuẩn GUM khiến ranh giới hiệu lực của mô hình cơ học cổ điển ($H_{0b}$) trên bó dây TiNi vẫn là một câu hỏi mở[cite: 57, 61, 69].

### 2.6.2. Yêu cầu thực nghiệm và tiêu chí chuyển giao sang Chương 3 và Chương 4

Để giải quyết trọn vẹn các khoảng trống trên mà không vượt quá phạm vi bằng chứng cho phép, Chương 3 và Chương 4 được thiết kế theo cấu trúc phân tầng thực nghiệm rõ ràng[cite: 70, 71, 72]:

* **Nhiệm vụ của Chương 3 – Thiết lập và khảo sát trên Hệ đối chứng nguồn áp suất ngoài (Bench A):**
  * *Mục tiêu cơ học:* Tách hoàn toàn các biến số động học của bộ chấp hành SMA–piston để tập trung trả lời RQ1, RQ2 và xây dựng cơ sở hiệu chuẩn/kiểm chứng cho RQ5[cite: 1, 70].
  * *Yêu cầu phép đo và thực nghiệm:* Sử dụng nguồn tạo áp suất ngoài có kiểm soát và lắp cảm biến đo trực tiếp áp suất gần mẫu ($p_{\text{near\_sample}}$)[cite: 13, 70]. Thực hiện các phép thử đặc trưng hóa riêng rẽ (vật liệu dây đơn, ảnh hưởng của ống bao, phép thử rút trượt tương đối và phép thử uốn bó dây theo chu trình gia tải – dỡ tải) trong miền nhiệt độ, tốc độ biến dạng và lịch sử chu trình xác định[cite: 57, 68, 70].
  * *Đầu ra bắt buộc:* Xác lập ánh xạ từ $p_{\text{near\_sample}}$ sang đáp ứng $M-\kappa$ (hoặc $F-\delta$ kèm mô hình quy đổi chính xác), nhận diện các miền bám dính – trượt một phần – trượt toàn phần, định lượng độ cứng nhánh cùng diện tích vòng trễ kèm dải độ không đảm bảo mở rộng $U$ theo chuẩn GUM [14], và kiểm định khả năng dự báo của mô hình đối chứng $H_{0b}$ trên tập dữ liệu giữ lại[cite: 70, 71].

* **Nhiệm vụ của Chương 4 – Đặc trưng hóa nguồn SMA–piston và tích hợp đối chiếu (Bench B):**
  * *Mục tiêu cơ học:* Trả lời RQ3 thông qua việc khảo sát độc lập bộ nguồn SMA–piston, sau đó trả lời RQ4 bằng phép so sánh chéo giữa Bench B và Bench A[cite: 1, 70, 71].
  * *Yêu cầu phép đo và thực nghiệm:* Ở bước thứ nhất, đo đạc quan hệ giữa kích thích điện/nhiệt độ phần tử SMA với lực, hành trình piston, khả năng tạo áp, duy trì áp suất và hồi áp theo thời gian khi làm việc với thể tích tải tương đương[cite: 71]. Ở bước thứ hai, kết nối nguồn SMA–piston với bó dây TiNi và thực hiện phép thử uốn tại cùng mức áp suất gần mẫu ($p_{\text{near\_sample}}$), cùng cấu hình hình học, điều kiện gá đặt và trạng thái nhiệt như ở Bench A[cite: 1, 71].
  * *Tiêu chí đánh giá tích hợp:* Phân biệt rõ sự tương thích tại một mức áp suất tĩnh với sự tương thích trên toàn bộ lịch sử áp suất theo thời gian[cite: 71]. Mọi sự sai khác về đáp ứng uốn giữa Bench B và Bench A chỉ được phép kết luận sau khi đã định lượng và loại trừ các yếu tố gây nhiễu từ quá độ nhiệt của nguồn SMA, độ mềm đường truyền và tổn thất rò rỉ[cite: 1, 71, 72].

---

## TÀI LIỆU THAM KHẢO

[1] S. Zhang và J. Yao, "A variable stiffness omnidirectional chain based on positive-pressure fiber jamming," *Mechanical Sciences*, tập 17, tr. 481–493, 2026. DOI: 10.5194/ms-17-481-2026[cite: 73].

[2] B. Reedlunn, S. Daly và J. Shaw, "Superelastic shape memory alloy cables: Part I - Isothermal tension experiments," *International Journal of Solids and Structures*, tập 50, số 20–21, tr. 3009–3026, 2013. DOI: 10.1016/j.ijsolstr.2013.03.013[cite: 73].

[3] Y. Kotb, I. Elgamal và M. Serry, "Shape Memory Alloy Capsule Micropump for Drug Delivery Applications," *Micromachines*, tập 12, bài 520, 2021. DOI: 10.3390/mi12050520[cite: 73].

[4] IEEE Publication Operations, *Reference Guide*, ver. 3.28.2025, Piscataway, NJ, USA, 2025[cite: 73].

[5] J. Burgner-Kahrs, D. C. Rucker và H. Choset, "Continuum Robots for Medical Applications: A Survey," *IEEE Transactions on Robotics*, tập 31, số 6, tr. 1261–1280, 2015. DOI: 10.1109/tro.2015.2489500[cite: 73].

[6] M. Russo, S. M. H. Sadati, X. Dong, A. Mohammad, I. D. Walker, C. Bergeles, K. Xu và D. A. Axinte, "Continuum Robots: An Overview," *Advanced Intelligent Systems*, tập 5, số 5, bài 2200367, 2023. DOI: 10.1002/aisy.202200367[cite: 73].

[7] H. Jeon, Q. N. Le, S. Jeong, S. Jang, H. Jung, H. Chang, H. J. Pandya và Y. Kim, "Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism," *IEEE Robotics and Automation Letters*, tập 7, số 3, tr. 6582–6589, 2022. DOI: 10.1109/lra.2022.3174363[cite: 73].

[8] Y. Zhang, J. Wang, G. Ye và R. Xu, "Bending Stiffness of Parallel Wire Cables Including Interfacial Slips among Wires," *Journal of Structural Engineering*, tập 144, số 10, bài 04018164, 2018. DOI: 10.1061/(asce)st.1943-541x.0002171[cite: 73].

[9] Y. S. Narang, J. J. Vlassak và R. D. Howe, "Mechanically Versatile Soft Machines through Laminar Jamming," *Advanced Functional Materials*, tập 28, số 17, bài 1707136, 2018. DOI: 10.1002/adfm.201707136[cite: 73].

[10] F. Caruso, G. Mantriota, V. Moramarco và G. Reina, "Layer jamming: Modeling and experimental validation," *International Journal of Mechanical Sciences*, tập 251, bài 108325, 2023. DOI: 10.1016/j.ijmecsci.2023.108325[cite: 73].

[11] S. Zhang, J. Yao, W. Zhao và C. Wei, "A continuum-based model for a layer jamming beam," *Mechanical Sciences*, tập 16, tr. 821–830, 2025. DOI: 10.5194/ms-16-821-2025[cite: 73].

[12] F. Caro và M. G. Carmichael, "A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics," *Actuators*, tập 13, số 2, bài 64, 2024. DOI: 10.3390/act13020064[cite: 73].

[13] Y. Zhang, Q. Feng, G. Wang và R. Xu, "Analytical model for the bending of parallel wire cables considering interactions among wires," *International Journal of Mechanical Sciences*, tập 194, bài 106192, 2021. DOI: 10.1016/j.ijmecsci.2020.106192[cite: 73].

[14] Joint Committee for Guides in Metrology, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, JCGM 100:2008, 2008[cite: 74].

[15] Y. Fan, B. Yi và D. Liu, "An overview of stiffening approaches for continuum robots," *Robotics and Computer-Integrated Manufacturing*, tập 90, bài 102811, 2024. DOI: 10.1016/j.rcim.2024.102811[cite: 74].

[16] L. Bai, H. Yan, J. Li, J. Shan và P. Hou, "Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming," *Applied Sciences*, tập 12, số 7, bài 3582, 2022. DOI: 10.3390/app12073582[cite: 74].

[17] T. Liu, H. Xia, D.-Y. Lee, A. Firouzeh, Y.-L. Park và K.-J. Cho, "A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots," *IEEE Robotics and Automation Letters*, tập 6, số 4, tr. 8078–8085, 2021. DOI: 10.1109/lra.2021.3097255[cite: 74].

[18] M. Brancadoro, M. Manti, F. Grani, S. Tognarelli, A. Menciassi và M. Cianchetti, "Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition," *Frontiers in Robotics and AI*, tập 6, bài 12, 2019. DOI: 10.3389/frobt.2019.00012[cite: 74].

[19] G. B. Crowley, X. Zeng và H.-J. Su, "A 3D Printed Soft Robotic Gripper With a Variable Stiffness Enabled by a Novel Positive Pressure Layer Jamming Technology," *IEEE Robotics and Automation Letters*, tập 7, số 2, tr. 5477–5482, 2022. DOI: 10.1109/lra.2022.3157448[cite: 74].

[20] H. H. Huynh, D. Han, K. Yoshida, M. De Volder và J.-w. Kim, "Soft actuator with switchable stiffness using a micropump-activated jamming system," *Sensors and Actuators A: Physical*, tập 338, bài 113449, 2022. DOI: 10.1016/j.sna.2022.113449[cite: 74].

[21] S. Vahidi, J. Arghavani, E. Choi và A. Ostadrahimi, "Mechanical response of single and double-helix SMA wire ropes," *Mechanics of Advanced Materials and Structures*, tập 29, tr. 5393–5406, 2022. DOI: 10.1080/15376494.2021.1955313[cite: 74].

[22] B. Reedlunn, S. Daly và J. Shaw, "Superelastic shape memory alloy cables: Part II - Subcomponent isothermal responses," *International Journal of Solids and Structures*, tập 50, tr. 3027–3044, 2013. DOI: 10.1016/j.ijsolstr.2013.03.015[cite: 74].

[23] P. Narjabadifam, N. Fazlalipour, S. Mollaei, M. Momeni, A. S. Watandoust, M. Chavoshi, A. Babaeian Amini và F. Karazmay, "Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes," *Buildings*, tập 14, bài 1567, 2024. DOI: 10.3390/buildings14061567[cite: 74].

[24] F. Barsi, B. Carboni và W. Lacarbonara, "A new mechanical model of short wire ropes: Theory and experimental validation," *Engineering Structures*, tập 323, bài 119217, 2025. DOI: 10.1016/j.engstruct.2024.119217[cite: 74].

[25] K. Takashima, T. Imazawa và H. Cho, "Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon," *Journal of Robotics and Mechatronics*, tập 34, số 2, tr. 466–477, 2022. DOI: 10.20965/jrm.2022.p0466[cite: 74].

[26] N. Matsumoto, H. Cho, K. Takashima và H. Suzuki, "Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon," *Mechanical Engineering Journal*, tập 11, số 6, bài 24-00130, 2024. DOI: 10.1299/mej.24-00130[cite: 75].

[27] M. D. Pierce và S. A. Mascaro, "A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump," *IEEE/ASME Transactions on Mechatronics*, tập 18, số 2, tr. 536–546, 2013. DOI: 10.1109/tmech.2012.2211032[cite: 75].

[28] Y. Fan, D. Liu và L. Ye, "A Novel Continuum Robot With Stiffness Variation Capability Using Layer Jamming: Design, Modeling, and Validation," *IEEE Access*, tập 10, tr. 130253–130263, 2022. DOI: 10.1109/access.2022.3228775[cite: 75].

[29] B. Yi, Y. Fan và D. Liu, "A Novel Model for Layer Jamming-based Continuum Robots," *2024 IEEE International Conference on Robotics and Automation (ICRA)*, tr. 12727–12733, 2024. DOI: 10.1109/icra57147.2024.10610912[cite: 75].

[30] Y. Fan, B. Yi và D. Liu, "Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots," *IEEE Transactions on Control Systems Technology*, tập 34, số 5, tr. 2219–2233, 2026. DOI: 10.1109/tcst.2026.3690756[cite: 75].