# MP1 sau phản hồi của mentor: đề xuất thu hẹp phạm vi

**Ngày:** 29-09-2026 (Asia/Bangkok)  
**Trạng thái:** đề xuất để thảo luận; không thay đổi `research_state.json`, quyết định D1/M1, W02 hoặc các vòng verification.  
**Câu hỏi quyết định:** Có nên chuyển MP1 từ câu hỏi cần luật cơ học NiTi–tiếp xúc mới sang một bài toán thiết kế và đặc trưng cơ cấu điều biến độ cứng bằng áp suất dương, dùng lò xo SMA làm nguồn áp suất, trong bối cảnh MRI không?

## Kết luận đề xuất

**Có, nên gọt MP1; chưa nên tuyên bố đã đổi đề tài luận văn chính thức.** Phản hồi mentor cho thấy mục tiêu thực dụng hơn: một cơ cấu nhỏ, tránh các phần tử truyền động từ tính ở gần vùng MRI, đạt độ cứng uốn hữu ích và chuyển trạng thái đủ nhanh. Vì vậy, đề xuất mở **nhánh MP1-R (rescope proposal)** nhằm đánh giá hệ `lò xo SMA → piston → áp suất chất lỏng → lực pháp tuyến tại giao diện dây → ma sát → độ cứng uốn`. Đây là giả thuyết kiến trúc để kiểm tra, không phải novelty đã xác minh.

Đóng góp MSc khả dĩ là **bản đồ hiệu năng có đối chứng và giới hạn vật lý của cơ cấu**: áp suất có thực sự tăng ma sát/độ cứng trong cấu hình mentor muốn, nhanh đến đâu, gây tổn thất gì, có lặp lại sau chu kỳ không. Luật ghép cặp NiTi–contact `H1` chỉ là câu hỏi nâng cao nếu mô hình hiện hữu đã được kiểm định nghiêm túc và thất bại. Thành phần MRI phải được mô tả là **động cơ ứng dụng / yêu cầu thiết kế cần thử**, chưa phải năng lực đã được xác nhận.

## Bằng chứng từ bài mentor gửi

**VERIFIED FULL TEXT, PDF do người dùng cung cấp:** Jeon et al. (2022), *Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism*, *IEEE Robotics and Automation Letters*, 7(3), 6582–6589, DOI [10.1109/LRA.2022.3174363](https://doi.org/10.1109/LRA.2022.3174363). PDF tại `C:/Users/khanh/Downloads/Towards_a_Snake-Like_Flexible_Robot_With_Variable_Stiffness_Using_an_SMA_Spring-Based_Friction_Change_Mechanism.pdf`; SHA-256 `65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03`. Đã đọc text và kiểm tra trực quan sơ đồ Fig. 1 trong PDF. Preflight cấu trúc trả `UNAVAILABLE` do thiếu `pypdf`; do đó note này viện dẫn *section* và các số liệu trong text, không dùng số trang PDF làm locator chắc chắn.

- Cơ cấu của Jeon có backbone trung tâm, tám dây siêu đàn hồi ngoại vi, ống cao su và lò xo SMA **quấn bên ngoài**. Gia nhiệt bằng dòng điện làm đường kính lò xo co, bóp ống cao su; ma sát chủ yếu tại **dây–ống cao su**, hạn chế trượt của dây qua các đĩa khi uốn (Section II, Fig. 1). Không được kể bài này là đã chứng minh riêng ma sát *giữa các dây NiTi*.
- Bài báo đo lực kéo một dây qua ống cao su và đáp ứng uốn; tỉ số độ cứng hai trạng thái khoảng 1,41–1,50 cho ba cấu hình. Nó có một mô hình năng lượng uốn/ma sát và so sánh với thực nghiệm (Sections III–IV).
- Thời gian gia nhiệt từ khoảng 25 đến 60 °C là khoảng 18 s ở 0,5 A, 21 s ở 0,4 A, 115 s ở 0,3 A; làm nguội tự nhiên khoảng 60 s trong thí nghiệm đó. Các giá trị này **không phải** response time của hệ piston–thủy lực mới, nhưng cho thấy nhánh nguội có thể là nút thắt (Section IV.C).
- Bài nêu MRI là bối cảnh ứng dụng và thừa nhận các giới hạn về làm nguội, tỉ số độ cứng, điều khiển nhiệt và xấp xỉ hình học. Việc bài nói đến MRI không có nghĩa cụm thủy lực/SMA mới đã được thử an toàn/chất lượng ảnh.
- Cần tránh câu “đề xuất thủy lực là điều bài báo chưa hề nghĩ tới”: phần future work của Jeon đã nêu *fluidics* để tăng phạm vi ma sát và làm nguội SMA nhanh hơn. Cách triển khai áp suất dương bằng piston khác với đề xuất đó, nhưng khác phần cứng không tự thành novelty.

## Điểm khác nhau quyết định: mặt tiếp xúc và chiều lực

**MENTOR INPUT sau khi người dùng đính chính:** mentor nói áp suất dương đẩy dây *ra ngoài* để tăng ma sát, nhưng **chưa xác định bề mặt ma sát là dây–dây hay dây–ống/vỏ ngoài**. Lò xo SMA co khi gia nhiệt kéo piston tạo áp suất. Câu “đẩy ra ngoài” tự nó không cho biết lực pháp tuyến ở giao diện nào; thậm chí có thể làm tăng ma sát dây–vỏ trong khi lực dây–dây giảm hoặc không đổi. Vì vậy không được khóa MP1 vào *inter-wire friction* trước khi có mặt cắt hoặc xác nhận trực tiếp từ mentor. Có ít nhất hai cấu hình không thể đánh đồng:

| Cấu hình | Dòng lực áp suất dự kiến | Giao diện ma sát được kích hoạt | Rủi ro kiểm tra đầu tiên |
|---|---|---|---|
| A — lõi/ống nở bên trong đẩy dây ra ngoài vào ống ràng buộc | lõi có áp → dây → ống ngoài/khung phản lực | có thể là dây–vỏ; mạng dây–dây có thể đổi theo packing | lực dây–dây tăng, giảm hoặc gần như không đổi; phải đo |
| B — cuff áp suất ở ngoài đẩy vào bó dây (thiết kế S02 cũ) | cuff ngoài → màng trong → dây | có thể là dây–dây và dây–màng | **không được coi là cấu hình mentor** nếu mentor thực sự muốn đẩy ra ngoài |

Trong bài Jeon, lò xo bóp **từ ngoài vào** và tăng ma sát dây–cao su. Câu mô tả của mentor chỉ cho biết áp suất tác động theo hướng ra ngoài; trước khi chế tạo cần hỏi rõ khoang chất lỏng, từng dây, ống/vỏ phản lực, seal và cặp tiếp xúc mà mentor muốn điều khiển. Pilot phải đo cả pull-out dây–dây **và** dây–vỏ để không gán nhầm cơ chế. Khi chốt hình học, cần kiểm tra lại H0b và prior art theo giao diện thực. **Không sửa ngầm** artifact cũ; dùng nhánh rescope riêng.

## Phân biệt hai SMA và môi trường MRI

Lò xo SMA **actuator** được gia nhiệt để co/kéo piston là một bộ phận. Các dây NiTi siêu đàn hồi **backbone/friction medium** là bộ phận khác. Nhiệt từ actuator có thể thay đổi tính chất dây backbone nếu dẫn nhiệt tới chúng; đo nhiệt tại cả hai vị trí. Câu “lò xo nguội là tự giãn ra” cần nói chính xác hơn: nguội giảm lực hồi phục và **cần lực bias / lò xo đối kháng, áp suất phản hồi hoặc tải ngoài** để đẩy piston về, tùy thiết kế. Kiểm tra hành trình co, lực theo hành trình, áp suất trên hai nhánh, hiện tượng trễ và tốc độ làm nguội.

Với đường truyền thủy lực, áp suất lý tưởng có thể ước lượng bởi \(p \simeq (F_{\mathrm{SMA}}-F_{\mathrm{bias}}-F_{\mathrm{seal}})/A_p\), và thể tích bơm \(\Delta V \simeq A_p\Delta x\); \(A_p\) là tiết diện piston, \(\Delta x\) là hành trình. Đây là **INFERENCE / cân bằng lực và thể tích lý tưởng**, chưa phải dữ liệu. Áp suất đo tại xilanh không tự bằng áp suất tại cuff khi có khí lẫn, độ giãn ống, rò, tổn thất hoặc đáp ứng quá độ. Áp suất tại cuff lại càng không tự bằng lực pháp tuyến dây–ống/dây–dây. Cần tối thiểu cảm biến áp suất tại nguồn và gần cấu trúc, phép đo pull-out/ma sát, hình học và biến dạng vỏ.

**Về MRI:** lập luận “động cơ không thể quay trong từ trường mạnh” là quá tuyệt đối. Động cơ điện từ thông thường có rủi ro lớn, nhưng các actuator khác và thậm chí prototype electromagnetic được thiết kế riêng đã được thử trong MRI; điều kiện phụ thuộc thiết kế, vị trí, trường và dây cấp. SMA cũng không tự được chứng nhận `MR Safe`/`MR Conditional`; dây điện gia nhiệt, connector, piston, sensor, ống dẫn, heating và ảnh hưởng tới ảnh đều thuộc **toàn cụm**. FDA có hướng dẫn đánh giá/ghi nhãn thiết bị trong MR environment, và literature đã có robot dùng SMA được kiểm tra MRI. Do vậy:

- Nếu chưa có quyền tiếp cận scanner và người phụ trách MR safety: ghi **“thiết kế hướng tới môi trường MRI / tránh thành phần truyền động sắt từ tại đầu robot”**, không ghi “MRI-compatible” trong tên đề tài hoặc kết quả.
- Nếu có scanner và quy trình được phê duyệt: xác định trường, vị trí actuator và electronics, vật liệu từng bộ phận, nhiệt, induced current, force/torque, artifact/SNR và tiêu chí chấp nhận trước khi thử. Đây là nhánh validation riêng; không đưa prototype chưa đánh giá vào scanner.

Nguồn ngoài cho luận điểm MRI: [FDA guidance 2023](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/testing-and-labeling-medical-devices-safety-magnetic-resonance-mr-environment); [Kim et al. 2018 SMA MRI robot, PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/29434530/); [Chauvière et al. 2024 electromagnetic actuator MRI prototype](https://www.mdpi.com/1996-1073/17/13/3254). Hai nguồn sau là **bằng chứng sự tồn tại/ngoại lệ**, không chứng minh tính tương thích của thiết kế đang đề xuất.

## Câu hỏi nghiên cứu và phạm vi MSc đề xuất

**Tên làm việc, chưa khóa:** *Đặc trưng độ cứng uốn của bó dây TiNi dưới cơ cấu ma sát điều khiển bằng áp suất dương từ piston dẫn động lò xo SMA.* Tên này giữ giao diện ma sát ở dạng trung tính cho tới khi mentor xác nhận và pilot đo được nó. Chỉ dùng “ma sát liên dây” hoặc “ma sát dây–vỏ” sau khi cơ chế đã được xác định.

**RQ chính, đề xuất tạm thời:** *Trong một bó dây TiNi có hình học và bề mặt phản lực được xác định, áp suất dương do piston–lò xo SMA tạo ra làm thay đổi lực ma sát tại giao diện chịu tải và độ cứng uốn như thế nào, so với cùng cấu trúc được cấp áp bằng nguồn điều áp ngoài?* Sau khi mentor xác nhận giao diện, thay “giao diện chịu tải” bằng “dây–dây” hoặc “dây–vỏ”.

So sánh nguồn điều áp ngoài là then chốt: nó tách **cơ chế tăng ma sát do áp suất** khỏi **động học nguồn SMA–piston**. Hai “điểm sáng” có thể đủ cho báo cáo MSc nếu đo cẩn thận:

1. **Độ cứng:** đo độ cứng uốn tại cùng độ cong/tải, tỉ số cứng/mềm, lực trượt tại cả giao diện dây–dây và dây–vỏ để xác định giao diện chi phối, công suất/năng lượng tạo áp, độ trễ, drift sau chu kỳ và giới hạn p→contact. Không dùng tỉ số 1,4× của Jeon làm ngưỡng pass tự động; đặt tiêu chí theo chức năng và uncertainty của thiết bị.
2. **Đáp ứng:** tách thời gian `Joule heat → lực SMA`, `lực → p tại cuff`, `p → thay đổi độ cứng`, và chiều hồi phục khi tắt nhiệt. Báo cáo t10–t90, t90–t10, overshoot, repeatability cùng định nghĩa phép đo. Nếu chỉ đổi piston/cuff mà làm nguội vẫn khoảng phút, không tuyên bố “nhanh hơn” khi chưa có đối chứng.

**Bộ thí nghiệm tối thiểu:** (i) bench piston–SMA với tải, hành trình, nhiệt, áp suất hai đầu; (ii) cụm dây được cấp áp ngoài theo vài mức p để cô lập response ma sát–độ cứng; (iii) tích hợp piston–SMA theo cùng specimen/hình học và cùng protocol uốn; (iv) lặp chu kỳ heating/cooling và đối chứng áp bằng không. Quy định trước output, dwell, tốc độ uốn, nhiệt, trạng thái dây và sai số cảm biến. Nếu muốn kết luận NiTi chuyển pha trong dây backbone góp phần, cần một phép đo phase-sensitive hoặc calibration cùng lot; global stiffness/hysteresis không đủ.

**Các quyết định thiết kế cần chốt trước pilot:** giao diện ma sát là **chưa rõ**; cần chốt vị trí khoang áp, đường truyền lực, packing, vỏ phản lực và cách đo tách biệt ma sát dây–dây với dây–vỏ; fluid là chất lỏng thủy lực hay khí nén (không gọi khí nén là thủy lực); nguồn SMA–piston ở trong bore, ngoài bore hay ngoài phòng; lực hồi piston và seal. Người dùng **chưa rõ** có quyền tiếp cận MRI; vì thế MRI hiện chỉ là yêu cầu ứng dụng cần xác minh sau.

## Liên hệ với trạng thái MP1 đã có

**VERIFIED REPOSITORY STATE:** MP1-W02 là candidate `CONDITIONAL`, gate `BLOCKED`; H0b còn sống, H1 chưa có đủ bằng chứng. WR1-S01 đã cho kết luận `EXISTING_FORMULATION_SUFFICIENT_IN_PRINCIPLE` **đối với hình học cuff ép vào bó dây**. WR1-S02 mới chuẩn bị pilot, chưa có thí nghiệm. Vì lời mentor mô tả **áp suất đẩy ra ngoài**, các bản S01/S02 ấy là nền tham khảo về kỷ luật đo lường và model-lock, **không phải bằng chứng cơ cấu A hoạt động hay bài test sẵn để chạy nguyên trạng**.

**Prior art theo repo:** C8 (SMA-driven syringe/piston) đã bị đánh giá `PREEMPTED/REJECT` như claim novelty riêng; positive-pressure jamming và SMA actuation cũng đã có tiền lệ. Đề tài ứng dụng MSc vẫn có thể có đóng góp hữu ích nếu thể hiện cải thiện định lượng có đối chứng cho yêu cầu cụ thể, nhưng không nên quảng bá việc ghép SMA+piston+áp suất là một nguyên lý khoa học chưa từng có. Một quick check ngoài repo cho thấy các phương án truyền động MR khác đã được công bố; đây không phải systematic re-audit của toàn bộ nhánh MRI.

## Cổng quyết định và kết quả có thể xảy ra

1. **Chốt sơ đồ mặt cắt và ứng dụng:** xác nhận với mentor hình học đẩy ra ngoài A và bề mặt cần tăng ma sát; vẽ đường lực tới vỏ phản lực và vị trí dự kiến của nguồn SMA so với MRI. Nếu chưa có đường lực tăng normal traction tại giao diện đã chọn, sửa thiết kế trước khi phát biểu giả thuyết tăng ma sát.
2. **Bench áp suất ngoài:** nếu tăng p không tăng lực ma sát/độ cứng đáng kể ở cùng hình học, dừng hướng stiffness này hoặc đổi giao diện; chưa cần piston SMA.
3. **Bench SMA–piston:** nếu hành trình/lực/nhiệt không đạt áp–thể tích yêu cầu hoặc hồi quá chậm cho chức năng, giảm tham vọng tốc độ, dùng nguồn ngoài làm luận văn đặc trưng cấu trúc, hoặc đổi actuator; không đổi threshold sau khi nhìn kết quả.
4. **Tích hợp và so sánh:** nếu cùng p thì độ cứng của hai nguồn tương đương, nguồn SMA chỉ là giải pháp cấp áp; đóng góp có thể là packaging/operating envelope và phải mô tả đúng. Nếu khác, truy nguyên do đường ống, nhiệt, biến dạng, rò hoặc lặp chu kỳ trước khi gọi cơ học mới.
5. **MRI gate riêng:** chỉ khi có phép thử được phê duyệt và đạt tiêu chí mới dùng claim MR-compatible/MR-conditional theo phạm vi xác nhận.

## Việc nên làm ngay theo thứ tự

### 1. Xác nhận cơ chế với mentor trước khi chế tạo

Gửi câu hỏi ngắn sau:

> *Thầy cho em xác nhận: áp suất dương làm bó dây TiNi ép vào nhau, hay ép vào ống/vỏ ngoài? Bề mặt ma sát chính mà thầy muốn điều khiển là dây–dây hay dây–vỏ? Thầy có thể phác mặt cắt và hướng lực áp suất giúp em để em xây dựng đúng mô hình và thí nghiệm không ạ?*

Yêu cầu tối thiểu là một sơ đồ có: bó dây, khoang áp, piston, màng/ống, vỏ phản lực, đường seal và mũi tên lực. Cho tới khi có sơ đồ này, không chốt tên đề tài, không dùng `inter-wire jamming` làm giả định và không chạy S02 cũ.

### 2. Tách bài toán cơ cấu thành hai bench test

**Bench A — cấu trúc và áp suất:** dùng nguồn áp suất ngoài có đo được để kiểm tra trước quan hệ áp suất–biến dạng vỏ–lực trượt–độ cứng. Mục tiêu là xem áp suất có tạo ra thay đổi ma sát có ý nghĩa hay chỉ làm tăng tiếp xúc với vỏ.

**Bench B — nguồn SMA–piston:** chỉ sau khi Bench A có tín hiệu cơ học, đo riêng lực–hành trình–nhiệt độ của lò xo SMA, thể tích/áp suất piston, thời gian tăng áp và thời gian hồi áp. Nguồn áp ngoài được giữ làm đối chứng để tách cơ học ma sát khỏi tốc độ của actuator.

### 3. Đo cả hai giao diện ma sát

Ở mọi cấu hình cần đo riêng pull-out hoặc lực trượt của dây–dây và dây–vỏ. Nếu chỉ có độ cứng uốn tổng thể, không thể biết giao diện nào tạo ra thay đổi. Kết quả âm tính ở một bó ba dây chỉ được dùng để loại hướng khi miền áp suất, packing và biên tải đã bao phủ cấu hình dự kiến.

### 4. Chỉ sau ba kết quả này mới thu hẹp RQ

- Nếu áp suất làm tăng **ma sát dây–dây**: giữ hướng `pressure-controlled inter-wire friction`.
- Nếu áp suất chủ yếu làm tăng **ma sát dây–vỏ**: đổi hướng sang `pressure-controlled wire–sleeve friction`.
- Nếu áp suất không tạo thay đổi lặp lại: dừng claim điều biến độ cứng bằng cơ chế này và xem xét loại bỏ MP1.

MRI hiện chỉ là bối cảnh ứng dụng. Chỉ mở một nhánh kiểm tra MR safety sau khi cơ cấu cơ học đã có hiệu quả đo được và đã xác định được quyền tiếp cận scanner, điều kiện trường, vị trí đặt actuator, nhiệt và tiêu chí ảnh.

## Provenance và giới hạn

- **VERIFIED FULL TEXT:** PDF Jeon et al. 2022 do người dùng cung cấp, DOI `10.1109/LRA.2022.3174363`; kiểm tra trực quan Fig. 1 và Sections II–V. File PDF không được sao chép vào repo; kiểm tra cấu trúc preflight ở `outputs/reports/MP1_MENTOR_RESCOPE_2026-09-29/mentor_paper_pdf_preflight.json` là `UNAVAILABLE` do thiếu `pypdf`, không phải `PASS`.
- **VERIFIED REPOSITORY STATE:** `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`; `outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json`; `outputs/execution/MP1-V002/WR1/S01/MP1_S01_EXECUTION_RECEIPT.json`; `outputs/execution/MP1-V002/WR1/S02/MP1_S02_PREPARATION_RECEIPT.json` và `MP1_S02_SPECIMEN_AND_APPARATUS_SPEC.json`.
- **MENTOR INPUT:** lời nhận xét được người dùng chép trong chat ngày 29-09-2026; người dùng sau đó đính chính rằng **chưa chắc** giao diện là giữa các dây và quyền thử MRI cũng **chưa rõ**. Chưa có bản vẽ khẳng định đường truyền lực của cấu hình A. Không coi lời nhận xét là kết quả thí nghiệm hoặc chỉ dẫn nằm trong PDF.
- **INFERENCE/PROPOSAL:** công thức piston lý tưởng, tên/RQ mới, cấu trúc đối chứng và cổng quyết định. Chưa thiết kế, chế tạo, đo hoặc chứng nhận phần cứng mới.
- **Unresolved:** giao diện ma sát mentor muốn điều khiển; lực tiếp xúc ở giao diện đó khi đẩy ra ngoài; loại fluid, vị trí actuator, quyền tiếp cận MRI, tiêu chí chức năng, vật liệu/giới hạn áp suất, hiệu năng SMA–piston. Chưa có final D1-vs-MP1 adjudication.

**AI assistance:** note được AI hỗ trợ tổng hợp từ nguồn ghi trên; các quyết định cơ khí và thử nghiệm cần người nghiên cứu/mentor kiểm tra trên bản vẽ và dữ liệu thật.

## Các nhánh phát triển sau khi mentor xác nhận cơ chế

### Nhánh 1 — Áp suất làm tăng ma sát giữa các dây

**Câu hỏi:** Áp suất dương thay đổi mạng tiếp xúc, lực trượt và độ cứng uốn của bó dây TiNi như thế nào?

**Đóng góp có thể bảo vệ:** bản đồ định lượng `p → contact/slip → bending stiffness`, kèm mô hình cơ học đơn giản và kiểm tra lặp chu kỳ. Không dùng việc ghép lò xo SMA với piston làm novelty chính.

**Phép đo bắt buộc:** pull-out dây–dây, hình học packing, áp suất ở nguồn và gần bó dây, mô men–độ cong, nhiệt độ và lịch sử chu kỳ.

**Rủi ro:** lực ép ra ngoài có thể làm tăng tiếp xúc dây–vỏ thay vì dây–dây; nếu không tách được hai giao diện thì nhánh này không đạt.

**Tên làm việc:** *Pressure-Controlled Inter-Wire Friction and Bending Stiffness of Superelastic TiNi Wire Bundles.*

### Nhánh 2 — Áp suất chủ yếu làm tăng ma sát dây–ống/vỏ

**Câu hỏi:** Áp suất dương và độ biến dạng của ống/vỏ thay đổi ma sát dây–vỏ, độ cứng uốn và thời gian chuyển trạng thái như thế nào?

**Đóng góp có thể bảo vệ:** đặc trưng áp suất–ma sát–độ cứng và response time của một cơ cấu pressure-controlled wire–sleeve. Nhánh này gần bài Jeon hơn, nên novelty cần đặt ở hiệu năng, mô hình áp suất truyền qua màng và độ trễ, không đặt ở nguyên lý “SMA làm tăng ma sát”.

**Phép đo bắt buộc:** ma sát dây–vỏ, biến dạng vỏ, áp suất, độ cứng, thời gian tăng/giảm áp, làm nguội và độ bền chu kỳ.

**Tên làm việc:** *Pressure-Controlled Wire–Sleeve Friction for Variable Bending Stiffness of a TiNi-Based Flexible Structure.*

### Nhánh 3 — Cả ma sát dây–dây và dây–vỏ cùng thay đổi

**Câu hỏi:** Hai giao diện ma sát đóng góp như thế nào vào độ cứng uốn và hiện tượng trượt của bó dây?

**Đóng góp có thể bảo vệ:** mô hình phân rã các đóng góp contact và xác định vùng áp suất mà giao diện nào chi phối.

**Đánh giá:** có giá trị cơ học cao hơn nhưng rủi ro và khối lượng đo lớn. Chỉ chọn khi có phương pháp đo riêng hai giao diện; nếu không, thu hẹp về Nhánh 1 hoặc 2.

### Nhánh 4 — Đóng góp chính là piston–lò xo SMA và tốc độ đáp ứng

**Câu hỏi:** Piston được dẫn động bằng lò xo SMA tạo và hồi áp suất với lực, hành trình, năng lượng và thời gian đáp ứng nào?

**Đóng góp có thể bảo vệ:** đặc trưng actuator–fluidic và trade-off giữa lực, áp suất, tốc độ, nhiệt độ, năng lượng và độ lặp lại.

**Giới hạn:** đây là hướng actuator/packaging; prior art về SMA pump, piston và MRI actuator đã tồn tại. Không nên tuyên bố novelty chỉ từ việc thay motor bằng lò xo SMA.

**Tên làm việc:** *Characterization of an SMA-Spring-Driven Piston for Pressure-Controlled Stiffness Modulation.*

### Nhánh 5 — MRI là mục tiêu kiểm chứng chính

Nếu mentor yêu cầu chứng minh hoạt động trong MRI thật, đề tài sẽ thêm một work package riêng: lực/torque do trường, heating, induced current, ảnh hưởng dây điện và artifact/SNR. Nếu chưa có scanner, người phụ trách MR safety và tiêu chí thử, chỉ được ghi “MRI-oriented design constraint”. Không gắn `MRI-compatible` vào tên đề tài khi chưa có kiểm chứng.

### Nhánh 6 — Cơ cấu không tạo được thay đổi ma sát lặp lại

Nếu áp suất không tạo ra thay đổi độ cứng hoặc ma sát có ý nghĩa, phải dừng claim MP1 về cơ chế này. Khi đó có hai lựa chọn: quay lại D1/M1 là hướng luận văn chính, hoặc đổi MP1 thành một bài toán actuator/feasibility nhỏ hơn nếu mentor vẫn cần cơ cấu.

## Quy tắc chọn nhánh

1. Chọn **Nhánh 1** nếu lực dây–dây tăng được đo trực tiếp và lặp lại.
2. Chọn **Nhánh 2** nếu lực dây–vỏ là cơ chế chi phối và gần như không có bằng chứng dây–dây.
3. Chọn **Nhánh 3** chỉ khi hai giao diện được nhận dạng riêng.
4. Chọn **Nhánh 4** nếu mentor ưu tiên nguồn tạo áp hơn cơ học bó dây.
5. Chỉ thêm **Nhánh 5** khi có điều kiện MRI thực tế.
6. Chọn **Nhánh 6** nếu cơ cấu không vượt qua bench test áp suất ngoài.

Cho tới khi bước xác nhận với mentor hoàn tất, tên và RQ trung tính ở đầu note vẫn là lựa chọn an toàn nhất.
