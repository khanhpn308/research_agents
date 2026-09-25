# ASTRA SCIENTIFIC CRITIQUE — MP1

## 1. Overall assessment

Chuỗi bằng chứng đủ mạnh để bác bỏ các claim rộng về wire jamming, positive-pressure jamming, SMA kết hợp jamming và sự tồn tại của tiếp xúc–ma sát trong cáp NiTi. Tuy nhiên, việc loại bỏ các claim kiến trúc không tự động chứng minh rằng mechanics core còn lại có nội dung khoa học độc lập. Điểm yếu trung tâm là chưa phân biệt **thay mô-đun đàn hồi bằng một hằng số khác**, **dùng luật NiTi đã biết trong mô hình tiếp xúc đã biết**, và **thực sự cần thêm cơ chế ghép cặp**. T2 hiện còn mở theo tập nguồn, nhưng P3 không được dùng như một hàng rào để loại những lý thuyết đã chứa tải pháp tuyến và lịch sử stick–slip. T1 đóng là hợp lý ở cấp độ tồn tại; T3 bị đón đầu đáng kể cũng hợp lý, nhưng một số packet diễn giải quá mức bằng chứng cơ chế và validation. Đối chiếu PDF phát hiện lỗi đáng kể về cấu hình Carboni, còn Fang trực tiếp cảnh báo tính không duy nhất của phép khớp tham số. Chưa có bằng chứng phân biệt H0 với H1 trong chính điều kiện pressure-controlled bending đang xét. Tôi giữ nguyên input state bạn chỉ định; tuy nhiên, JSON audit trên đĩa ghi `13` paper và substitution `established/true`, trái với handoff `10` paper và `insufficient/false`. Vì vậy, độ chắc chắn của việc bác bỏ các claim rộng cao hơn rõ rệt độ chắc chắn của bước suy luận sang mechanics core hiện tại.

## 2. Critical gaps

| ID | Severity | Gap | Why it matters | Affected claim/target | Evidence/source | Required fix |
|---|---|---|---|---|---|---|
| G01 | CRITICAL | H0 chưa được định nghĩa nhất quán | Bác bỏ mô-đun hằng không chứng minh cần coupling ngoài lý thuyết hiện có | Parameter substitution; C7; T3 | Audit JSON, W08–W10; Vahidi; Fang | Tách baseline đàn hồi đơn giản khỏi baseline NiTi cấu thành–tiếp xúc đã biết; kiểm tra cả hai |
| G02 | CRITICAL | P3 đang được xem gần như một cơ chế mới chỉ vì áp suất điều chỉnh được | Thay điều kiện biên từ hằng sang biến thiên có thể không cần phương trình cơ học mới | C6; T2 | W07; Tjahjanto; Xin Liu; Zhang–Yao | Kiểm tra trực tiếp phương trình hiện có có nhận áp suất/lịch sử tải tùy ý hay không |
| G03 | CRITICAL | Chưa chứng minh chuyển pha và inter-wire slip cùng hoạt động trong miền vận hành dự kiến | Nếu chỉ một cơ chế hoạt động, lập luận “cạnh tranh/ghép cặp” có thể sụp đổ | C7; mechanics core | Chưa có phép thử áp suất–uốn tương ứng trong bằng chứng đã kiểm tra | Xác định độc lập ngưỡng chuyển pha và ngưỡng trượt; kiểm tra miền chồng lấn |
| G04 | CRITICAL | Đáp ứng uốn vĩ mô không nhận diện riêng được chuyển pha, ma sát và thay đổi hình học | Một đường cong khác dự đoán không đủ để quy nguyên nhân cho coupling NiTi | H1; experimental identifiability | Carboni; Fang; Silva; Reedlunn | Đo thêm slip, biến dạng cục bộ, nhiệt độ và lực biên; dùng đối chứng cơ chế |
| G05 | HIGH | W08 gán chuyển pha NiTi dưới uốn thuần cho cấu hình S2a của Carboni | Bằng chứng được dùng để nối trực tiếp NiTi–uốn–chuyển pha thực ra sai cấu hình/vật liệu | T3; W08-E01 | Carboni PDF tr. 9–10, Table 4: S2a = ST49 | Loại suy luận đó khỏi evidence chain; dùng đúng S1a và Carboni 2016, giữ giới hạn từng cấu hình |
| G06 | HIGH | Tồn tại mô hình, khớp dữ liệu và validation độc lập bị nhập làm một | Có thể đánh giá quá cao cả mức tiền nhiệm lẫn độ tin cậy baseline | T1–T3; kill test | Vahidi, Niu, Zhang–Yao, Fang | Tách numerical verification, calibration, experimental validation và causal identification |
| G07 | HIGH | Reedlunn bị dùng vượt phạm vi để suy ra coupling mới | Sai số do bỏ uốn/xoắn cục bộ không chứng minh thiếu một luật contact–transformation mới | H1; W09 | Reedlunn, `fac21c950e` | Thử khôi phục động học đã bỏ qua bằng mô hình hiện có trước khi viện dẫn cơ chế mới |
| G08 | HIGH | Quá nhiều tham số có thể bù trừ trong phép fit bending | Model tốt về đường cong nhưng không xác định được cơ chế | Model identifiability | Fang PDF tr. 11–12; Carboni identification | Calibration độc lập; kiểm tra độ nhạy, tương quan và tính duy nhất tham số |
| G09 | HIGH | Pressure → normal contact force chưa được xác định độc lập | Sai mapping áp suất có thể bị ngụy trang thành sai NiTi constitutive law | T2; H0/H1 | Zhang–Yao giả định truyền áp; Tjahjanto phân bố contact | Kiểm tra truyền áp, packing, membrane và lực dọc trục trước khi fit coupling |
| G10 | HIGH | Chưa thỏa stop condition nhưng có diễn đạt gần như “chỉ còn thiếu active pressure” | Không tìm thấy trong tập nguồn không bằng không tồn tại trong lý thuyết/liên ngành | C6–C7; T2 | W11; `citation_coverage.json` | Hoàn tất nhánh đe dọa nhắm đúng phương trình/cơ chế, đặc biệt B07/B08 |
| G11 | HIGH | Input state và audit JSON không cùng một trạng thái bằng chứng | Có nguy cơ dùng kết luận mạnh hơn mà không có phép thử tương ứng | Substitution verdict | `TARGETED_THREAT_AUDIT.json`, dòng 237–241 và provenance | Xác định phiên bản nào phục vụ adjudication; không dùng `established` để thay cho phép thử còn thiếu |
| G12 | MEDIUM | “Bending stiffness” chưa được định nghĩa theo lịch sử tải | Độ cứng tiếp tuyến, secant và động có thể cho kết luận khác nhau | Toàn bộ mechanics core | Các nguồn dùng loại tải và đại lượng khác nhau | Chỉ rõ observable, nhánh tải, nhiệt độ, trạng thái ban đầu và cách đo |

## 3. Claims that appear robust

**Claim:** C1 và C2 — wire/fiber jamming và positive-pressure jamming không còn là claim mới ở mức nguyên lý.

**Reason:** Có tiền nhiệm trực tiếp cho từng nguyên lý, không chỉ tương đồng từ khóa.

**Strongest evidence:** Bai 2022; Liu 2021; Zhang–Yao 2026 trong V001.

**Residual caveat:** Điều này không đồng nghĩa mọi tổ hợp hình học/vật liệu đều đã được nghiên cứu; nhưng khác biệt tổ hợp không tự tạo mechanics novelty.

**Claim:** C3 — SMA và jamming đã cùng tồn tại trong một thiết bị.

**Reason:** Dòng Takashima cung cấp tiền nhiệm trực tiếp.

**Strongest evidence:** W03 và canonical V001 evidence.

**Residual caveat:** SMA backbone nằm trong môi trường hạt không tương đương NiTi wires tự tạo mạng tiếp xúc ma sát. Claim “cùng thiết bị” đóng; claim “cùng vai trò cơ học” phải xét riêng.

**Claim:** C4 — nguồn tạo áp suất gọn/tích hợp không phải nguyên lý chưa có.

**Reason:** Có tiền nhiệm bơm ECF và cơ cấu piston tạo confinement.

**Strongest evidence:** Huynh 2022; Wang 2024.

**Residual caveat:** “Compact/onboard” không đồng nghĩa hệ hoàn toàn tự chủ năng lượng, không dây hoặc không reservoir. Không được nâng phạm vi verdict tới mức đó.

**Claim:** T1 — NiTi wires đã được nghiên cứu như một tập hợp có tiếp xúc, ma sát và chuyển động tương đối.

**Reason:** Bằng chứng bao gồm mô hình contact–friction giữa wires, không chỉ một hệ số damping chung.

**Strongest evidence:** Vahidi (`53200aa0c6`); Carboni (`d9966f2f5e`); Reedlunn (`fac21c950e`).

**Residual caveat:** Đây là closure của claim tồn tại. Nó không chứng minh slip tại mọi interface đã được đo trực tiếp, hay mọi pressure-controlled bundle đều được dự đoán chính xác.

**Claim:** T3 — sự kết hợp NiTi transformation, contact/friction và hysteresis/stiffness đã bị tiền nhiệm chiếm lĩnh đáng kể.

**Reason:** Vahidi đã ghép luật SMA với contact; Carboni và các công trình tiếp theo có mô hình/đo đáp ứng hysteretic của assemblies chứa NiTi.

**Strongest evidence:** Vahidi; Carboni 2014/2015; Carboni–Lacarbonara 2016 (`40760daa02`).

**Residual caveat:** Không phải mọi giải thích vi mô đều đã được nhận diện độc lập. Sai sót W08 làm yếu claim cụ thể nhưng không đủ để mở lại T3 ở mức rộng.

**Claim:** Quyết định rời claim kiến trúc rộng là có cơ sở.

**Reason:** Nhiều thành phần C1–C4 đã có tiền nhiệm, C8 chủ yếu là tổ hợp các chức năng đã biết.

**Strongest evidence:** V001 decomposition và các nguồn tương ứng.

**Residual caveat:** Bước này chỉ loại một căn cứ novelty yếu; chưa xác nhận phần mechanics còn lại đủ mạnh.

## 4. Claims that remain vulnerable

**Claim/Target:** C5 — NiTi đóng vai trò môi trường ma sát.

**Current verdict:** Mở trong tập V001; nội dung rộng bị T1 đóng trong V002.

**Why vulnerable:** Duy trì nhãn “open” mà không nhắc phạm vi lịch sử sẽ tạo gap giả.

**Missing evidence:** Nếu muốn giữ một phần C5, phải chỉ rõ đại lượng/cơ chế chưa được mô tả, không chỉ đổi từ cable sang bundle.

**Possible alternative explanation:** Cùng cơ học tiếp xúc dây, khác cách đóng gói và điều kiện biên.

**What would resolve it:** So sánh động học, contact network và phương trình — không so tên thiết bị.

**Claim/Target:** C6/T2 — confinement chủ động trên bó NiTi là một mechanics problem riêng.

**Current verdict:** `open_in_current_full_text_set`.

**Why vulnerable:** Verdict này hợp lệ như mô tả corpus, không đủ làm kết luận khoa học. P1/P2/P3 mô tả cách phát sinh hoặc điều khiển tải; chúng không tự xác định ba lớp lý thuyết khác nhau.

**Missing evidence:** Một hiệu ứng pressure-path mà mô hình contact–NiTi hiện có không dự đoán được.

**Possible alternative explanation:** Áp suất chỉ tăng tải pháp tuyến, qua đó dịch ngưỡng trượt theo luật hiện hữu.

**What would resolve it:** Đưa đúng pressure boundary vào một baseline đã biết, khóa calibration, rồi kiểm tra dự đoán. Không loại Tjahjanto chỉ vì bài dùng fixed preload.

**Claim/Target:** C7 — ghép NiTi–slip–pressure–stiffness tạo nội dung mechanics chưa giải quyết.

**Current verdict:** Cầu nối có điều kiện sang mechanics core.

**Why vulnerable:** Việc bốn yếu tố chưa xuất hiện trong cùng một bài không chứng minh tồn tại một tương tác mới giữa chúng.

**Missing evidence:** Dấu hiệu tương tác có thể quan sát, dự đoán và phân biệt với mô hình ghép tiêu chuẩn.

**Possible alternative explanation:** Luật NiTi đã biết + contact đã biết tự sinh ra phân bố lực và lịch sử trượt thông qua cân bằng.

**What would resolve it:** Phân biệt thiếu động học, sai contact boundary, sai calibration và thực sự thiếu constitutive coupling.

**Claim/Target:** C8 — SMA syringe/piston kết hợp jamming.

**Current verdict:** `substantially_preempted`.

**Why vulnerable:** Các thành phần chức năng đã biết hỗ trợ kết luận tổ hợp không đủ làm scientific novelty; không chứng minh chính xác mọi hookup đã xuất hiện.

**Missing evidence:** Tiền nhiệm trực tiếp nếu muốn claim exact architecture đã bị anticipation hoàn toàn.

**Possible alternative explanation:** Tích hợp kỹ thuật khác biệt nhưng không có mechanics mới.

**What would resolve it:** Giữ verdict ở mức component/function synthesis; không suy ra kết luận phổ quát về mọi thiết kế hoặc khả năng bảo hộ.

**Claim/Target:** T3 đã chứng minh gần như toàn diện causal coupling.

**Current verdict:** `substantially_preempted`.

**Why vulnerable:** W08 trộn kết quả đo, giải thích của tác giả và cơ chế được nhận diện độc lập.

**Missing evidence:** Đo riêng slip, phase evolution, contact loading và nhiệt trong cùng phép thử.

**Possible alternative explanation:** Thay đổi modulus vĩ mô do hình học; tăng nhiệt do transformation dissipation và truyền nhiệt khác nhau, không chỉ ma sát.

**What would resolve it:** Giữ closure của nguyên lý; thu hẹp những claim nhân quả cụ thể về đúng mức bằng chứng.

## 5. Parameter-substitution analysis

### Evidence supporting H0

Cần tách H0 thành hai baseline để tránh đánh bại một đối thủ quá yếu:

- **H0a:** Thay modulus và vài hệ số trong mô hình elastic-fiber.
- **H0b:** Giữ framework contact/geometry hiện có, dùng một luật NiTi history-dependent đã biết và được calibration độc lập.

H0b mạnh hơn nhiều nhưng vẫn **không phải một coupling mới**.

Bằng chứng thuận H0:

1. **Vahidi đã thực hiện NiTi constitutive law + contact/friction tiêu chuẩn.** Điều này chứng minh khả năng biểu diễn đồng thời không phải một trở ngại lý thuyết chưa giải quyết.
2. **Tjahjanto đã đặt radial pressure, tension và cyclic bending trong cùng mô hình contact.** Dùng một mức áp suất không chứng minh phương trình chỉ áp dụng được cho mức đó.
3. **Xin Liu và cơ học cable đã nối contact loading với slip và flexural response.** Phải kiểm tra khả năng chuyển giao trước khi gọi active pressure là mắt xích mới.
4. **Reedlunn cho thấy một số cấu hình góc xoắn nhỏ gần đáp ứng bó dây song song.** Chính paper thường được dùng để ủng hộ coupling cũng chứa miền mà mô tả đơn giản hoạt động khá tốt.
5. **Fang tái tạo đáp ứng hysteretic vĩ mô bằng mô hình tương đương.** Contact microscale có thể không cần thiết nếu đầu ra chỉ là lực/độ cứng toàn cục.

Đây là bằng chứng H0 **plausible**, chưa phải xác nhận H0 cho bó NiTi chịu áp suất và uốn.

### Evidence supporting H1

Bằng chứng hiện tại chủ yếu hỗ trợ nhu cầu vượt khỏi H0a:

- Reedlunn: localization, ảnh hưởng helix, local bending/twisting và dấu tiếp xúc chế tạo.
- NiTi hysteresis/history không được xác định bởi một giá trị tangent modulus đơn lẻ.
- Vahidi: trạng thái ứng suất phụ thuộc tương tác wires.
- Silva: đáp ứng nhiệt–cơ thay đổi theo loading protocol.
- Các assemblies có thay đổi stiffness và pinching theo cấu hình.

Nhưng các hiện tượng này **có thể đã nằm trong H0b**. Một solver ghép tiêu chuẩn có thể tự tạo force redistribution khi một wire chuyển pha; redistribution tự nó không chứng minh cần thêm luật coupling.

Chưa có bằng chứng trực tiếp rằng active confinement tạo sai lệch có hệ thống mà H0b không giải thích được.

### What remains unproven

- NiTi transformation có thực sự xảy ra trong khoảng curvature mục tiêu?
- Transformation và slip có chồng lấn đủ để tạo đáp ứng khác biệt?
- Failure của H0a đến từ material law, kinematics hay pressure mapping?
- H0b có dự đoán được cả moment–curvature và slip, không chỉ fit một đường cong?
- Bằng chứng nào đòi hỏi **quan hệ vật lý bổ sung**, thay vì chỉ mô hình hóa đúng điều kiện đã biết?
- Có cần microscale resolution nếu mục tiêu chỉ là stiffness vĩ mô?

**Kết luận:** Chưa có cơ sở chọn H1. `insufficient` là trạng thái phù hợp cho phép phân biệt này.

### Minimum decisive test

1. **Chốt hai baseline lồng nhau:** elastic-fiber và existing NiTi constitutive–contact; cùng geometry, boundary conditions và định nghĩa stiffness.
2. **Calibration ngoài phép thử bundle:** single-wire response phù hợp trạng thái nhiệt/tải; friction theo dải normal load liên quan; kiểm tra pressure transmission và end loads.
3. **Khóa tham số trước phép thử phân biệt.** Không cho mỗi mức pressure một bộ tham số mới.
4. **Dùng các đường tải có khả năng phân biệt:** thay pressure tại curvature giữ cố định và thay curvature tại pressure giữ cố định; thêm đảo chiều để kiểm tra memory.
5. **Đo đồng thời:** moment/force, curvature cục bộ, relative slip khả dụng và temperature; cần bằng chứng phase transformation hoặc proxy được kiểm chứng độc lập.
6. **Chấm dự đoán bằng ngưỡng đặt trước và uncertainty.** H0b thất bại chỉ là lý do điều tra residual; chưa tự động xác nhận H1.
7. **Thử alternative explanations trước:** end effects, packing, truyền áp, tension–compression asymmetry, thermal drift và contact numerics.

Hai đường tải đi tới cùng pressure–curvature nhưng cho đáp ứng khác nhau chỉ chứng minh history dependence; một mô hình contact–NiTi hiện có cũng có thể dự đoán điều đó.

## 6. Mechanics-core attack

Current mechanics core:

> Under actively varied positive radial/transverse confinement, how do pressure and curvature govern stick-slip transitions and bending stiffness in a superelastic NiTi wire bundle, and can those responses be predicted by an existing elastic-fiber/contact framework with substituted NiTi properties?

### What is genuinely distinct?

Phân biệt quan sát được là **pressure được điều khiển độc lập với bending**, có thể thay đổi trong cùng một loading history, trên một assembly NiTi xác định.

Đó là khác biệt về protocol. Chưa có bằng chứng nó là khác biệt về cơ chế.

Một interaction chỉ có nội dung khoa học riêng khi xác định được điều gì mô hình hiện có bỏ sót, observable nào phát hiện nó và vì sao alternative explanations không đủ.

### What may only be parameter variation?

- Tăng friction capacity bằng tăng normal force.
- Dịch curvature bắt đầu trượt.
- Thay modulus đàn hồi bằng tangent response của NiTi.
- Thay số lượng/đường kính dây hoặc packing.
- Thêm nhiều mức pressure vào một quan hệ đã biết.

Pressure “active” không tự làm phương trình Coulomb khác đi. Ngược lại, thay pressure giữa chu kỳ có thể tạo history effects, nhưng phải kiểm tra xem existing state-dependent contact đã chứa chúng chưa.

### What may already be covered by existing theory?

- Cân bằng hình học phi tuyến.
- Contact opening/closing và thay đổi lực pháp tuyến.
- Stick–slip với loading history.
- NiTi phase-dependent constitutive response.
- Tái phân bố ứng suất khi độ cứng cục bộ thay đổi.
- Hysteresis vật liệu cộng hysteresis ma sát.
- Thermal coupling nếu sử dụng framework nhiệt–cơ tương ứng.

Không cần một paper có đúng tên kiến trúc MP1 để những phương trình này trở thành prior-art threat.

### What is not yet experimentally identifiable?

Từ force–displacement đơn độc, chưa tách được:

- transformation softening với slip softening;
- frictional hysteresis với material hysteresis;
- pressure-induced contact với pressure-induced axial tension;
- packing compaction với phase-dependent stiffness;
- tự gia nhiệt với biến đổi contact;
- slip trong gauge section với slip ở grips.

### What is not yet model-identifiable?

Một vấn đề tối thiểu là:

\[
F_{\mathrm{cap}}=\mu N.
\]

Ở đây \(F_{\mathrm{cap}}\) là lực tiếp tuyến giới hạn trước trượt, đơn vị N; \(\mu\) là hệ số ma sát, không thứ nguyên; \(N\) là lực pháp tuyến contact, đơn vị N. Đây là quan hệ Coulomb minh họa lập luận nhận diện, không phải phương trình mới đề xuất cho MP1.

Nếu chỉ đo ngưỡng trượt mà \(N\) được suy từ một pressure mapping chưa xác định, dữ liệu thường chỉ ràng buộc **tổ hợp ma sát–truyền áp**, không tách riêng từng thành phần.

Tương tự, modulus hiệu dụng, packing geometry, prestrain và contact stiffness có thể bù nhau trong đường cong uốn. Một modulus đã fit ở cấp assembly không được tùy tiện coi là modulus vật liệu rồi đưa vào mô hình đã resolve cùng hình học; như vậy có nguy cơ tính compliance hai lần.

## 7. Reedlunn 2013 — critique

Failure của mô hình đơn giản ở góc helix lớn không phải bằng chứng trực tiếp cho H1. Bài kiểm tra axial loading trên cấu trúc xoắn; nguyên nhân được nêu gồm bỏ local bending và twisting. Đây trước hết là failure của **kinematic reduction cụ thể**, không phải failure của mọi framework elastic-fiber/contact có thay luật NiTi.

Relevance với MP1 phụ thuộc geometry. Nếu bundle dự kiến gần thẳng/song song, dùng kết quả steep-helix để khẳng định bắt buộc có coupling mới là ngoại suy yếu. Nếu bundle xoắn, các cơ chế này vẫn có thể được mô tả bằng rod/beam/contact theory đã biết.

Radial contact pressure trong giới hạn của phép response subtraction là cảnh báo về độ tin cậy suy luận subcomponent. Nó không cung cấp một phép đo trực tiếp cho pressure-controlled redistribution, cũng không xác định một constitutive law mới.

Các indentations do chế tạo liên quan tới localization rất đáng chú ý. Nhưng phải phân biệt **imperfection có sẵn** với **contact damage phát sinh khi vận hành**. Chưa thể chuyển từ bằng chứng thứ nhất sang claim áp suất điều khiển tạo cơ chế thứ hai.

Quan trọng hơn, các cấu hình góc xoắn nhỏ trong cùng nguồn tương đối gần đáp ứng bó dây song song. Bỏ qua kết quả này sẽ cherry-pick paper theo hướng cứu H1.

Reedlunn hỗ trợ yêu cầu kiểm tra geometry, multiaxial loading và manufacturing history. Nó không hoàn tất parameter-substitution kill test.

## 8. Fang 2019 — critique

Fang tạo threat lớn nếu MP1 chỉ muốn dự đoán đáp ứng vĩ mô: một mô hình tương đương có thể tái tạo hysteresis mà không resolve từng contact.

Tuy nhiên, đó không phải bằng chứng mô hình ấy đã dự đoán pressure-controlled bending. Dữ liệu cáp và calibration được trình bày cho axial response; contact/slip không phải observable được xác nhận riêng.

Điểm mạnh nhất cho critique nằm ngay trong paper: tác giả cho phép nhiều tổ hợp diện tích và thuộc tính vật liệu khác nhau đạt agreement tương tự. Vì thế, fit tốt không xác nhận thành phần tương đương có ý nghĩa vật lý duy nhất.

“Steel02” trong mô hình là công cụ phenomenological để tái tạo permanent strain/degradation, không chứng minh có một lõi thép vật lý hay một vùng contact thật tương ứng. Cũng không được dùng nonlinear fiber element của **RC pier** trong phần bridge model như bằng chứng rằng paper đã resolve bending của NiTi cable.

Threat đối với MP1 phải diễn đạt chính xác:

- Nếu đầu ra chỉ là moment–curvature hoặc stiffness, phải chứng minh detailed contact model đem lại prediction hoặc transferability mà một baseline gọn không đạt được.
- Nếu đầu ra gồm vị trí và propagation của slip, một macromodel fit force chưa đủ giải quyết.
- Nếu phải refit theo pressure/path, baseline chưa thắng phép thử dự đoán.
- Nếu một bộ tham số cố định dự đoán tốt mọi đầu ra được quan tâm, lý do cần mô hình microscale phức tạp bị thu hẹp mạnh.

**More detailed mechanics không tự tạo explanatory value.** Ngược lại, một fit phenomenological thành công cũng không chứng minh đã hiểu cơ chế.

## 9. Experimental risks

| Risk | Confounded variables | Consequence | How to discriminate |
|---|---|---|---|
| Không đạt transformation regime | Curvature, đường kính dây, mức độ stick, prestrain | Nghiên cứu mang tên NiTi coupling nhưng thực chất chỉ là elastic friction bundle | Characterize single-wire; đo strain cục bộ và kiểm tra phase activation |
| Không có miền transformation–slip chồng lấn | Pressure, friction, local strain | Không thể kiểm tra cạnh tranh cơ chế dự kiến | Xác định riêng các onset; kiểm tra overlap trước chiến dịch lớn |
| Pressure gây axial load | Endcaps, membrane, grips, preload | Geometric stiffening bị gán cho contact/phase change | Đo lực dọc trục; đối chứng enclosure và boundary conditions |
| Packing thay đổi | Pressure, wire count, helix, compaction | Apparent modulus và slip threshold không tái lập | Theo dõi hình học tiết diện, preconditioning và packing history |
| Thermal confounding | Loading rate, latent heat, friction, heat transfer | Plateau/stiffness shift bị gán sai cho pressure coupling | Đo nhiệt; kiểm tra rate/hold sensitivity thay vì chỉ gọi thử nghiệm “quasi-static” |
| Tổng hysteresis không tách nguồn | NiTi hysteresis, friction, grips, membrane | Không biết năng lượng tiêu tán đến từ đâu | Đối chứng single-wire, assembly, enclosure; đo slip và loop riêng |
| Training, fatigue và wear | Cycle count, thermal history, surface condition | Drift bị nhầm thành quy luật pressure | Protocol conditioning rõ; theo dõi drift và lặp thứ tự tải |
| Không quan sát được nội thất bó dây | Surface DIC, internal phase/slip | Suy cơ chế toàn bó từ bề mặt không đủ | Nêu giới hạn quan sát; dùng geometry kiểm chứng được hoặc phép đo bổ sung có khả năng phân biệt |

## 10. Modeling risks

| Risk | Why | Consequence | Required check |
|---|---|---|---|
| H0 strawman | Chỉ so với constant modulus | H1 thắng giả tạo | Thêm existing history-dependent NiTi/contact baseline |
| Tangent modulus thay thế state law | Cùng tangent có thể thuộc nhiều loading histories | Không dự đoán đúng reversal/hysteresis | Kiểm tra state variables và evolution laws |
| Quá nhiều tham số từ cùng bending curve | Ma sát, pressure transfer, stiffness và prestrain bù nhau | Non-unique fit | Calibration độc lập; sensitivity/profile analysis |
| Sai bending constitutive response | Luật fit kéo có thể bỏ tension–compression asymmetry | Residual bị quy cho contact coupling | Kiểm tra vật liệu trong trạng thái tải phù hợp |
| Contact numerics giả tạo stiffness | Penalty, regularization, mesh, stabilization | “Transition” là artefact số | Convergence và energy balance; tách numerical compliance |
| Macro stiffness không phải hàm duy nhất của pressure–curvature | Contact và NiTi có memory | Bản đồ phụ thuộc protocol nhưng bị trình bày như universal | Giữ history/state hoặc giới hạn rõ loading branch |
| Calibration bị gọi là validation | Modulus và friction fit từ chính structural data | Đánh giá accuracy quá lạc quan | Khóa tham số; dự đoán đầu ra/path không dùng để fit |
| Scope quá nhiều physics | Thermal, transformation, friction, packing, dynamics cùng mở | Không quy nguyên nhân được khi model sai | Trước hết cố định packing/material và thermal protocol; chỉ mở rộng khi residual đòi hỏi |

## 11. Evidence-chain weaknesses

1. **Carboni bị gán sai vật liệu/cấu hình trong W08.**  
   PDF tr. 9 mô tả S1a là tension–bending của NiTi; Table 4 tr. 10 ghi S2a dùng ST49. Claim “S2 chuyển pha NiTi từ ngoài vào trong” không được các trang đó hỗ trợ. Tuy nhiên, [evidence Carboni 2016](</home/khanh/projects/mechanical-research-agents/data/evidence/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json>) có cyclic bending của cáp lai NiTi–steel; phải dùng đúng nguồn và không biến nó thành all-NiTi pressure-controlled validation.

2. **Niu không phải một experimental replication độc lập mới.**  
   Canonical evidence ghi dùng dữ liệu thực nghiệm có trước. Agreement giữa HBM và Runge–Kutta là kiểm tra nghiệm của mô hình, không phải independent physical validation; nguồn cũng có discrepancy về softening ở excitation cao.

3. **Vahidi không “tích hợp hoàn hảo” theo nghĩa đã xác nhận định lượng toàn diện.**  
   PDF tr. 6, tương ứng printed p. 5, nêu sai khác tới khoảng 25% cho cấu hình 1×27 và các giả định bỏ qua về clamping/tension–compression. Benchmark sai số nhỏ với steel là so với numerical reference, không được chuyển thành experimental accuracy của NiTi.

4. **“Normal stress” không đồng nghĩa “normal contact pressure”.**  
   Vahidi trình bày normal/shear stress trong wire components; W07 không được dùng các giá trị đó như radial contact pressure đã xác nhận. Nhầm này tác động trực tiếp tới lập luận áp suất–chuyển pha.

5. **Silva và Liu 2026 không tự động cung cấp causal separation.**  
   Đo heating hoặc effective storage modulus không đủ chứng minh phần đóng góp riêng của friction, phase transformation và geometry. Các giải thích tác giả là bằng chứng cho hypothesis cơ chế, không thay thế phép đo phân biệt.

6. **Fang xác nhận fit không duy nhất.**  
   PDF tr. 11–12, printed pp. 543–544, nói rõ các tổ hợp vật liệu/diện tích khác nhau có thể đạt agreement tương tự. Đây là giới hạn scientific inference, không phải tiểu tiết implementation.

7. **Zhang–Yao không phải baseline hoàn toàn first-principles và independently calibrated.**  
   Structural modulus và friction được nhận diện từ dữ liệu cấp kết cấu; quan hệ transition có thành phần giả định. Paper còn thừa nhận pressure transmission không đều và packing là nguồn variability. Không được dùng baseline này như “chân lý contact” để quy mọi residual cho NiTi.

8. **Coverage không hỗ trợ khẳng định “chỉ còn active pressure”.**  
   `no_unresolved_high_threat_source=true` chỉ nói về nguồn đã được nhận diện; không bao phủ nhánh chưa screened. Zero forward citations tại một ngày và database không chứng minh không có equivalent mechanics.

9. **Audit JSON tự chứa một bước nhảy.**  
   [Parameter-substitution assessment](/home/khanh/projects/mechanical-research-agents/outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json:237) đặt `established/true`, nhưng phần giải thích chỉ bác bỏ constant-modulus substitution và đồng thời thừa nhận existing NiTi/contact models đã xử lý nhiều complexity. Điều đó chưa hỗ trợ kết luận cần coupling riêng vượt các mô hình ấy.

Thiếu DOI **không tự động là scientific weakness** khi bản full text, tác giả, nội dung và provenance đủ xác định. Nó chỉ thành vấn đề khoa học nếu gây nhầm nguồn, phiên bản hoặc làm không kiểm tra được claim.

## 12. Remaining work ranked by scientific value

### P0 — must resolve before trusting mechanics core

1. Định nghĩa H0a/H0b và điều gì cụ thể được gọi là “distinct coupling”; không để H1 thay nghĩa sau khi thấy dữ liệu.
2. Kiểm tra liệu existing contact/cable equations đã nhận pressure history và dự đoán pressure-dependent slip hay chưa.
3. Xác định miền mà transformation và inter-wire slip thực sự cùng hoạt động.
4. Loại các suy luận bị lỗi nguồn về Carboni; đánh giá lại độ mạnh T3 với đúng cấu hình và validation level.
5. Hoàn tất citation branches có thể chứa baseline hoặc equivalent mechanism, đặc biệt B07/B08. `stop_condition=false` là **BLOCKING đối với kết luận đã hoàn tất falsification**, không chặn việc phân tích giả thuyết.
6. Kiểm tra H0b bằng dự đoán khóa tham số và quan sát có khả năng phân biệt, không chỉ fit bending curves.

### P1 — should resolve before experimental design

1. Xác định mapping từ pressure đo được tới confinement thực và end loads.
2. Kiểm tra practical identifiability của friction, constitutive parameters và packing/prestrain.
3. Chốt loại stiffness, loading history và error tolerance cần kiểm tra.
4. Giới hạn trước mắt vào một packing/material family; giữ wire count, diameter, prestrain và conditioning cố định; kiểm soát/đo nhiệt; chưa mở đồng thời dynamics và thermal actuation.
5. Xác định observable bổ sung tối thiểu để phân biệt slip, transformation và geometric effects.

B07/B08 là **IMPORTANT ngay cho việc chọn baseline**, và **BLOCKING nếu định dùng coverage hiện tại để bảo vệ gap đã sống sót**.

### P2 — useful but non-blocking

1. Khảo sát sâu hơn wear, fatigue và rate effects sau khi đã có phép phân biệt quasi-static.
2. Mở rộng geometry/layer count chỉ khi cần kiểm tra một giới hạn cơ học cụ thể.
3. Bổ sung DOI cho nguồn không có DOI: **NON-BLOCKING về khoa học**, trừ khi identity/version chưa chắc chắn.

Parameter-substitution còn `insufficient` là **BLOCKING cho claim cần coupling mới**, nhưng không phải bằng chứng H0 đúng.

## 13. Kill criteria

Những bằng chứng sau có thể giết hoặc thu hẹp mạnh mechanics core:

1. **Equivalent prior theory đã giải quyết đúng phụ thuộc pressure–curvature–history**, dù paper không dùng từ “active confinement” hoặc không chế tạo robot.
2. **H0b dự đoán trong tolerance đã định cả đáp ứng vĩ mô và slip observables**, trên đường tải không dùng calibration, với tham số đo độc lập. Điều này giết claim cần distinct coupling vượt framework hiện có.
3. **H0a đã đủ trong miền vận hành thực tế.** Khi ấy lợi ích khoa học của viện dẫn NiTi transformation/contact coupling bị thu hẹp rất mạnh.
4. **Transformation không xảy ra, hoặc không chồng lấn với slip trong miền khả dụng.** Cơ chế cạnh tranh làm nền cho câu hỏi không được kích hoạt.
5. **Residual biến mất khi sửa pressure transfer, boundary forces, packing hoặc temperature.** Khi ấy nguyên nhân không phải coupling NiTi mới.
6. **Một macromodel gọn, khóa tham số, dự đoán đủ mọi đầu ra thực sự cần thiết.** Điều này không giải quyết microslip chưa đo, nhưng giết lập luận “phải resolve microscale để dự đoán stiffness”.
7. **Không thể phân biệt các mechanism với uncertainty và observables khả dụng.** Không chứng minh vật lý không tồn tại; nhưng làm câu hỏi hiện tại không kiểm chứng được trong phạm vi thực nghiệm.
8. **Phần đóng góp cuối cùng chỉ còn đổi vật liệu, thêm điều khiển pressure hoặc tăng mật độ phép đo.** Khi đó chưa tới tầng D — mechanics/scientific contribution.

Xác nhận H0 vẫn có thể là một kết quả khoa học hữu ích. Nhưng nó không tự tạo novelty, và không được đổi tên thành H1 để giữ đề tài.

## 14. Questions the researcher must be able to answer

1. Vì sao pressure điều khiển được tạo vấn đề mechanics mới, thay vì chỉ là normal-load parameter thay đổi trong contact theory hiện có?
2. Bạn gọi “parameter substitution” là thay một hằng số, hay dùng toàn bộ luật NiTi có state/history? Tại sao baseline yếu hơn lại đủ để bác bỏ lý thuyết hiện hữu?
3. Observable nào chỉ ra transformation thay đổi slip, thay vì cả hai cùng thay đổi do curvature hoặc packing?
4. Làm sao biết pressure làm tăng ma sát, không phải tạo axial tension hoặc thay đổi hình học tiết diện?
5. Nếu hai bộ friction–pressure-transfer–prestrain parameters cùng khớp bending, bằng chứng nào chọn được bộ có ý nghĩa vật lý?
6. Cụ thể phương trình hoặc assumption nào của existing NiTi/contact theory thất bại? Vì sao sửa điều kiện biên chưa đủ?
7. Nếu Fang-style macromodel dự đoán stiffness tốt hơn với ít tham số hơn, lợi ích kiểm chứng được của microscale model là gì?
8. Bạn có bằng chứng transformation và slip cùng hoạt động trong miền vận hành, hay đang ghép hai hiện tượng xuất hiện ở hai chế độ khác nhau?
9. Khi pressure–curvature giống nhau nhưng stiffness khác do history, “pressure–stiffness map” của bạn được định nghĩa thế nào?
10. Điều gì sẽ khiến bạn chấp nhận mechanics core đã bị giết, thay vì mở thêm nhiệt, wear hoặc geometry để giữ nó sống?

## 15. Final uncertainty register

Confidence dưới đây là độ tin cậy của **đánh giá bằng chứng**, không phải xác suất novelty.

| Question | Current evidence state | Confidence | What evidence is missing |
|---|---|---|---|
| C1–C4 còn bảo vệ được novelty ở mức nguyên lý không? | Tiền nhiệm trực tiếp đủ bác bỏ claim rộng | HIGH | Chỉ cần thêm nếu xét claim chức năng hẹp khác |
| T1 có thực sự chỉ là generic damping không? | Không; có NiTi wire contact/friction models và assembly evidence | HIGH | Interface-resolved experimental validation cho cấu hình MP1 |
| T3 có bị tiền nhiệm chiếm lĩnh đáng kể không? | Có; nhưng một số causal claim trong packet bị nói quá | HIGH | Separation của transformation, friction và thermal/geometry effects |
| P3 có tự tạo mechanics mới so với P1/P2 không? | Chưa chứng minh; khác protocol chưa đủ | HIGH | Hiệu ứng không được existing pressure/contact history models dự đoán |
| H0a có đủ trong miền vận hành thực tế không? | Chưa kiểm tra đúng miền | LOW | Calibrated prediction và kiểm tra phase activation |
| H0b có đủ không? | Plausible, chưa được falsify bằng phép thử tương ứng | MEDIUM | Locked-parameter prediction trên pressure–bending paths |
| Có bằng chứng cần coupling vượt H0b không? | Chưa có bằng chứng phân biệt trực tiếp | HIGH | Residual lặp lại, vượt uncertainty, loại được alternatives |
| Transformation và slip có miền chồng lấn hữu ích không? | Chưa xác định | LOW | Local strain/phase và slip onset trong cùng assembly |
| Macroscopic bending data có nhận diện riêng cơ chế không? | Một mình nó không đủ | HIGH | Local observables và independent calibration |
| Reedlunn chứng minh pressure-specific coupling mới không? | Không; chủ yếu chỉ ra giới hạn geometry/kinematic reduction | HIGH | Kiểm tra đúng pressure-controlled bending geometry |
| Fang đã giải quyết pressure-dependent bending chưa? | Chưa; nhưng đe dọa nhu cầu mô hình chi tiết cho đầu ra vĩ mô | HIGH | Transferability của macromodel với một calibration cố định |
| Search đã đủ để nói “chỉ active pressure còn thiếu” chưa? | Chưa; stop condition chưa đạt | HIGH | Hoàn tất nhánh còn mở và kiểm tra equivalent mechanics |
| Input substitution verdict có thống nhất với JSON audit không? | Không; `insufficient` và `established` đang cùng tồn tại | HIGH | Xác định evidence basis của verdict mạnh hơn; không có phép thử thì không nâng kết luận |

**Tình trạng thực hiện:** Chép lại toàn bộ nhận xét phản biện trong response trước vào tài liệu Markdown này. Không có thay đổi nào đối với scientific state, registry, verification outputs hay evidence.
