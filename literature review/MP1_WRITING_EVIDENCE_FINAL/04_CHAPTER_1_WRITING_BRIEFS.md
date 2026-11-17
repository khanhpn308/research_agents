# MP1 Writing Evidence Pack — Chapter 1 briefs

These are source-grounded writing briefs, not thesis prose. The section order follows the task priority while each section retains the authoritative PDF ID/title.

### 1.1.1. Robot mềm và robot continuum trong môi trường hạn chế
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `READY_TO_WRITE`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. **M04 — Lin, Song, and Wang (2024); Evidence M04-E02.** Mục 1.2 và Hình 2(a–d) hệ thống hóa bốn phương pháp xác định độ cứng hoạt động (operational stiffness): (1) độ cứng tuyến tính đầu công tác K = F/d [N/m] (ghi chú: bản in M04 in nghịch đảo d/F), (2) độ cứng xoắn K = \tau/\theta [N·m/rad] (bản in in \theta/\tau), (3) độ cứng chống uốn dầm tựa hai đầu uốn ba điểm K = EI = FL^3/(48\Delta w) [N·m²], và (4) độ cứng chống uốn dầm công-xôn ngàm một đầu K = EI = FL^3/(3\Delta w) [N·m²]. Ý nghĩa đo lường là mỗi công thức gắn liền với một sơ đồ gá đặt và điều kiện biên cụ thể dưới giả thiết dầm Euler-Bernoulli võng nhỏ, đàn hồi tuyến tính; các giá trị K hoặc EI này không thể hoán đổi trực tiếp và chưa bao gồm hiệu ứng trượt ma sát hay biến dạng màng bao. Bối cảnh: Force/displacement, torque/rotation, beam and cantilever cases. Giới hạn chuyển sang MP1: Giới hạn trong lý thuyết dầm đàn hồi tuyến tính Euler-Bernoulli biến dạng nhỏ; không tính đến trượt tiếp xúc ma sát phi tuyến, hiệu ứng cắt hay biến dạng màng bao.
     - DOI: `10.1016/j.birob.2024.100168`; nguồn chấp nhận: `data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf`; locator: PDF p.2; printed p.NOT_REPORTED; source section: Section 1.2; figure/table/equation: Fig. 2(a-d), Eqs. (1)-(4).
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: stiffness K can be calculated. Units/quantities: ['NOT_REPORTED'].
  2. **M03 — Russo et al. (2023); Evidence M03-E02.** Bảng 2 và Mục 3 của M03 hệ thống hóa phổ các phương pháp mô hình hóa cơ học cho robot liên tục: từ xấp xỉ hình học độ cong không đổi từng đoạn (PCC/PCS), đến cơ học thanh phi tuyến Cosserat/Kirchhoff (cân bằng lực và mômen vi phân), và mô hình phần tử hữu hạn phi tuyến (FEM). Phổ mô hình này cung cấp cơ sở phương pháp luận để MP1 lựa chọn mức độ chi tiết mô hình: mô hình dầm đồng nhất hóa (homogenized beam) chỉ phù hợp khi bỏ qua hoặc đơn giản hóa hiện tượng trượt, trong khi việc mô tả chính xác chuyển tiếp độ cứng đòi hỏi mô hình phân lớp có điều kiện biên tiếp xúc ma sát giao diện. Bối cảnh: Review synthesis. Giới hạn chuyển sang MP1: Khảo sát phổ mô hình dầm đơn thuần nhất; không tính đến hiện tượng trượt giữa các lớp vật liệu rời rạc trong kết cấu jamming.
     - DOI: `10.1002/aisy.202200367`; nguồn chấp nhận: `data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf`; locator: PDF p.3; printed p.NOT_REPORTED; source section: Section 1.2 Modeling and Control; figure/table/equation: Table 1.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: geometrical models ... finite-element methods. Units/quantities: ['NOT_REPORTED'].
  3. **M02 — Burgner-Kahrs, Rucker, and Choset (2015); Evidence M02-E01.** Burgner-Kahrs và cộng sự tổng kết đặc tính cơ học cốt lõi của robot liên tục: thân robot có khả năng uốn cong mềm dẻo liên tục theo các đường cong giải phẫu hẹp và phức tạp để tiếp cận vùng can thiệp sâu trong phẫu thuật xâm lấn tối thiểu. Khảo sát chỉ rõ mâu thuẫn cơ học cố hữu: độ mềm dẻo cao làm giảm khả năng chịu tải và độ chính xác truyền lực khi tương tác với mô sống, đặt ra yêu cầu phải tích hợp các cơ cấu biến đổi độ cứng (variable stiffness) trên thân robot. Đây là luận cứ định vị bối cảnh ứng dụng y sinh cho MP1 ở cấp độ tổng quan hệ thống; nguồn không chứa dữ liệu đo độ cứng thực nghiệm hay phân bố ứng suất của dầm nhiều lớp. Bối cảnh: Medical intervention context. Giới hạn chuyển sang MP1: Bài tổng quan phân loại vĩ mô các hệ thống robot y sinh; không cung cấp dữ liệu định lượng về lực cản uốn hay ứng suất tiếp xúc cục bộ của dầm nhiều lớp.
     - DOI: `10.1109/TRO.2015.2489500`; nguồn chấp nhận: `data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf`; locator: PDF p.1; printed p.NOT_REPORTED; source section: Abstract / Introduction; figure/table/equation: Fig. 1.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: continuum robot designs can traverse confined spaces. Units/quantities: ['NOT_REPORTED'].
  4. **M02 — Burgner-Kahrs, Rucker, and Choset (2015); Evidence M02-E02.** Định nghĩa 1 (Definition 1) xác lập ranh giới động học và cơ học chính quy: robot liên tục là cấu trúc truyền động có vật liệu cấu tạo tạo thành các đường cong có vectơ tiếp tuyến biến thiên liên tục dưới biến dạng đàn hồi, phân biệt với chuỗi khớp cứng rời rạc (discrete rigid links) hoặc cơ cấu giả liên tục (pseudocontinuum). Định nghĩa này cung cấp cơ sở hình học để MP1 xem xét bó dây như một dầm đàn hồi biến dạng liên tục; tuy nhiên, định nghĩa thuần túy ở cấp độ động học vĩ mô, không bao gồm các hiệu ứng phi tuyến tiếp xúc ma sát, trượt tương đối hay biến dạng tiết diện ngang giữa các sợi dây trong bó. Bối cảnh: Definition-level statement. Giới hạn chuyển sang MP1: Định nghĩa động học và hình học định tính; không bao gồm các hiệu ứng phi tuyến tiếp xúc ma sát hay trượt tương đối giữa các lớp vật liệu.
     - DOI: `10.1109/TRO.2015.2489500`; nguồn chấp nhận: `data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf`; locator: PDF p.2; printed p.NOT_REPORTED; source section: Section II-A Classification; figure/table/equation: Definition 1.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: constitutive material forms curves with continuous tangent vectors. Units/quantities: ['NOT_REPORTED'].
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.1.2. Độ cứng cần được định nghĩa theo đại lượng đo
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `READY_TO_WRITE`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. **M04 — Lin, Song, and Wang (2024); Evidence M04-E02.** Mục 1.2 và Hình 2(a–d) hệ thống hóa bốn phương pháp xác định độ cứng hoạt động (operational stiffness): (1) độ cứng tuyến tính đầu công tác K = F/d [N/m] (ghi chú: bản in M04 in nghịch đảo d/F), (2) độ cứng xoắn K = \tau/\theta [N·m/rad] (bản in in \theta/\tau), (3) độ cứng chống uốn dầm tựa hai đầu uốn ba điểm K = EI = FL^3/(48\Delta w) [N·m²], và (4) độ cứng chống uốn dầm công-xôn ngàm một đầu K = EI = FL^3/(3\Delta w) [N·m²]. Ý nghĩa đo lường là mỗi công thức gắn liền với một sơ đồ gá đặt và điều kiện biên cụ thể dưới giả thiết dầm Euler-Bernoulli võng nhỏ, đàn hồi tuyến tính; các giá trị K hoặc EI này không thể hoán đổi trực tiếp và chưa bao gồm hiệu ứng trượt ma sát hay biến dạng màng bao. Bối cảnh: Force/displacement, torque/rotation, beam and cantilever cases. Giới hạn chuyển sang MP1: Giới hạn trong lý thuyết dầm đàn hồi tuyến tính Euler-Bernoulli biến dạng nhỏ; không tính đến trượt tiếp xúc ma sát phi tuyến, hiệu ứng cắt hay biến dạng màng bao.
     - DOI: `10.1016/j.birob.2024.100168`; nguồn chấp nhận: `data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf`; locator: PDF p.2; printed p.NOT_REPORTED; source section: Section 1.2; figure/table/equation: Fig. 2(a-d), Eqs. (1)-(4).
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: stiffness K can be calculated. Units/quantities: ['NOT_REPORTED'].
  2. **M31 — Jeon et al. (2022); Evidence M31-E07.** Đo là stiffness kết cấu từ slope lực–chuyển vị; không nên đọc như constitutive modulus của TiNi. Bối cảnh: {'reported': 'end-disk displacement 5 mm; force sensor; 10 repetitions; diameter cases'}. Giới hạn chuyển sang MP1: Dynamic-friction noise noted; austenite state had more noise.
     - DOI: `10.1109/LRA.2022.3174363`; nguồn chấp nhận: `data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf`; locator: PDF p.6; printed p.6587; source section: Sec. 4.B; figure/table/equation: Eq. (10); Table II.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: The stiffness is the slope of the resistive force vs. displacement graph. Units/quantities: ['N/mm', 'mm'].
  3. **M04 — Lin, Song, and Wang (2024); Evidence M04-E03.** Tác giả cảnh báo rằng các giá trị độ cứng đo theo các định nghĩa hoạt động khác nhau không thể hoán đổi trực tiếp vì phụ thuộc vào thứ nguyên, điều kiện biên và sơ đồ chất tải. Tỉ số điều chỉnh độ cứng R = K_max/K_min là đại lượng không thứ nguyên biểu thị dải điều chỉnh, nhưng chỉ có ý nghĩa khoa học khi K_max và K_min được đo trên cùng một cấu hình thử nghiệm và cùng khoảng biến dạng. Đối với MP1, cảnh báo này đòi hỏi phải chuẩn hóa cố định sơ đồ gá đặt và đại lượng đo trước khi đánh giá hiệu quả tăng cứng theo áp suất; tỉ số R không phản ánh được độ trễ cơ học (hysteresis) hay độ cứng tuyệt đối của bó dây. Bối cảnh: Review comparison. Giới hạn chuyển sang MP1: Cảnh báo phương pháp luận về so sánh độ cứng; tỉ số R phụ thuộc điều kiện đo và không thể hiện độ trễ cơ học (hysteresis) hay độ cứng tuyệt đối.
     - DOI: `10.1016/j.birob.2024.100168`; nguồn chấp nhận: `data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf`; locator: PDF p.3; printed p.NOT_REPORTED; source section: Section 1.2; figure/table/equation: stiffness adjusting ratio.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: readers should be aware that stiffness values ... [differ]. Units/quantities: ['NOT_REPORTED'].
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.1.3. Nhu cầu thay đổi độ cứng bằng điều khiển tiếp xúc
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `READY_TO_WRITE`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. **M04 — Lin, Song, and Wang (2024); Evidence M04-E02.** Mục 1.2 và Hình 2(a–d) hệ thống hóa bốn phương pháp xác định độ cứng hoạt động (operational stiffness): (1) độ cứng tuyến tính đầu công tác K = F/d [N/m] (ghi chú: bản in M04 in nghịch đảo d/F), (2) độ cứng xoắn K = \tau/\theta [N·m/rad] (bản in in \theta/\tau), (3) độ cứng chống uốn dầm tựa hai đầu uốn ba điểm K = EI = FL^3/(48\Delta w) [N·m²], và (4) độ cứng chống uốn dầm công-xôn ngàm một đầu K = EI = FL^3/(3\Delta w) [N·m²]. Ý nghĩa đo lường là mỗi công thức gắn liền với một sơ đồ gá đặt và điều kiện biên cụ thể dưới giả thiết dầm Euler-Bernoulli võng nhỏ, đàn hồi tuyến tính; các giá trị K hoặc EI này không thể hoán đổi trực tiếp và chưa bao gồm hiệu ứng trượt ma sát hay biến dạng màng bao. Bối cảnh: Force/displacement, torque/rotation, beam and cantilever cases. Giới hạn chuyển sang MP1: Giới hạn trong lý thuyết dầm đàn hồi tuyến tính Euler-Bernoulli biến dạng nhỏ; không tính đến trượt tiếp xúc ma sát phi tuyến, hiệu ứng cắt hay biến dạng màng bao.
     - DOI: `10.1016/j.birob.2024.100168`; nguồn chấp nhận: `data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf`; locator: PDF p.2; printed p.NOT_REPORTED; source section: Section 1.2; figure/table/equation: Fig. 2(a-d), Eqs. (1)-(4).
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: stiffness K can be calculated. Units/quantities: ['NOT_REPORTED'].
  2. **M05 — Fan et al. (2024); Evidence M05-E02.** Mục 3.3.1, Hình 5(g) và Bảng 4 phân loại cơ chế jamming sợi/dây (fibre/filament jamming - FJ) dựa trên các phần tử sợi mảnh xếp dọc trục bên trong vỏ bọc kín khí đàn hồi; ma sát tương tác giữa các phần tử khi bị nén ép giúp cản trở biến dạng uốn. Đối với MP1, phân loại này cung cấp bối cảnh hình thái cho kết cấu bó dây, nhưng bản chất tiếp xúc thực tế của MP1 (tiếp xúc giữa các sợi dây với nhau, giữa dây với ống bọc/sleeve, hay tương tác kết hợp) vẫn là vấn đề chưa được giải quyết; không được tự ý khẳng định một mô hình tiếp xúc đường (line contact) hay Hertzian đã được xác nhận cho MP1 từ bài tổng quan này. Bối cảnh: Review classification. Giới hạn chuyển sang MP1: Phân loại cơ cấu ở cấp độ hình thái học; không cung cấp mô hình phân bố lực nén pháp tuyến hay lực ma sát tiếp xúc giữa các sợi.
     - DOI: `10.1016/j.rcim.2024.102811`; nguồn chấp nhận: `data/chap1-2_citations/M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf`; locator: PDF p.10; printed p.NOT_REPORTED; source section: Section 3.3.1 Fibre/filament jamming; figure/table/equation: Fig. 8.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: Fibre/filament jamming. Units/quantities: ['NOT_REPORTED'].
  3. **M04 — Lin, Song, and Wang (2024); Evidence M04-E01.** Lin và cộng sự phân tích mâu thuẫn chức năng cơ học trong phẫu thuật xâm lấn tối thiểu: robot phẫu thuật mềm cần độ cứng thấp và độ linh hoạt cao để đi xuyên an toàn qua các xoang hẹp giải phẫu, nhưng lại cần độ cứng cao để ổn định tư thế, chống phản lực mô và truyền lực cắt/kẹp chính xác ở đầu công tác. Động cơ lâm sàng này biện minh trực tiếp cho nhu cầu phát triển cơ cấu biến đổi độ cứng chủ động như cơ cấu bó dây điều khiển ma sát trong MP1; nguồn đóng vai trò phân tích yêu cầu thiết kế hệ thống, không cung cấp thông số lực hay mô hình cơ học tiếp xúc cho cơ cấu cụ thể. Bối cảnh: Minimally invasive surgery. Giới hạn chuyển sang MP1: Tổng quan định tính về nhu cầu lâm sàng; không cung cấp mô hình giải tích phân bố ứng suất hay số liệu kiểm chứng độc lập cho layer jamming.
     - DOI: `10.1016/j.birob.2024.100168`; nguồn chấp nhận: `data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf`; locator: PDF p.1; printed p.NOT_REPORTED; source section: Abstract / Introduction; figure/table/equation: Fig. 1.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: variable stiffness has became a desirable ability. Units/quantities: ['NOT_REPORTED'].
  4. **M05 — Fan et al. (2024); Evidence M05-E01.** Fan và cộng sự xác định độ cứng không đủ (insufficient stiffness) là thách thức trung tâm của robot liên tục khi cần tương tác lực với môi trường bên ngoài mà vẫn duy trì tính uốn dẻo khi chuyển động. Khảo sát khẳng định các phương pháp tăng cứng điều chỉnh được (tunable stiffening) là hướng tiếp cận cốt lõi để giải quyết sự đánh đổi này. Bằng chứng đóng vai trò định vị cơ cấu tăng cứng bó dây của MP1 vào bản đồ phân loại công nghệ robot mềm; nguồn không cung cấp phương trình cân bằng cơ học hay số liệu thực nghiệm đo độ cứng cho cấu hình cụ thể. Bối cảnh: Continuum robot review. Giới hạn chuyển sang MP1: Tổng quan phân loại diện rộng; không cung cấp mô hình giải tích chi tiết hay dữ liệu thực nghiệm gốc cho cơ chế khóa dầm layer jamming.
     - DOI: `10.1016/j.rcim.2024.102811`; nguồn chấp nhận: `data/chap1-2_citations/M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf`; locator: PDF p.1; printed p.NOT_REPORTED; source section: Abstract / Introduction; figure/table/equation: NOT_APPLICABLE.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: insufficient stiffness. Units/quantities: ['NOT_REPORTED'].
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.2.1. Những thành phần đã có tiền lệ
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `WRITE_WITH_LIMITATIONS`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. **M06 — Caro and Carmichael (2024); Evidence M06-E01.** Bài tổng quan định nghĩa topology lớp–màng và trạng thái khóa/trượt; độ cứng hệ thống không phải tự thân là tính chất vật liệu của từng lớp. Bối cảnh: {'geometry': 'thin-sheet beam stack', 'pressure': 'mechanism-dependent', 'loading': 'bending; lock/unlock'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.3390/act13020064`; nguồn chấp nhận: `data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf`; locator: PDF p.3; printed p.NOT_REPORTED; source section: Introduction / mechanism definition; figure/table/equation: Fig. 2.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: An LJS consists of a beam that is made of thin sheets. Units/quantities: NOT_REPORTED.
  2. **M08 — Brancadoro et al. (2019); Evidence M08-E01.** Hệ là fiber jamming trong module silicone; contact topology là fiber–fiber/interlocking comb, không phải wire–sleeve hay layer jamming. Bối cảnh: {'geometry': 'Module A 50 mm x 14.5 mm; Module B central lumen', 'material': 'silicone; fibers', 'interface': 'interlocking comb'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.3389/frobt.2019.00012`; nguồn chấp nhận: `data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf`; locator: PDF p.4; printed p.NOT_REPORTED; source section: Design / Fig. 2; figure/table/equation: Fig. 2.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: central channel hosts the fibers. Units/quantities: ['mm'].
  3. **M09 — Bai et al. (2022); Evidence M09-E01.** Đây là wire/rope jamming trong envelope HDPE; không nên gộp với laminar sheet jamming. Bối cảnh: {'material': 'kraft, hemp, nylon', 'envelope': 'HDPE', 'geometry': 'rectangular/circular layouts', 'interface': 'wire-wire and envelope'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.3390/app12073582`; nguồn chấp nhận: `data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`; locator: PDF p.4; printed p.NOT_REPORTED; source section: 2.2 Design; figure/table/equation: Fig. 2.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: choose inextensible materials. Units/quantities: ['mm'].
  4. **M10 — Liu et al. (2021); Evidence M10-E01.** Cơ chế là positive-pressure granular jamming, với pressure path qua bladder–granules–sleeve; khác vacuum layer-jamming. Bối cảnh: {'geometry': '26 mm diameter, 50 mm length prototype', 'material': 'rubber bladder; SMP granules; fabric sleeve', 'pressure': 'positive air'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.1109/LRA.2021.3097255`; nguồn chấp nhận: `data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`; locator: PDF p.2; printed p.NOT_REPORTED; source section: Design / Fig. 1; figure/table/equation: Fig. 1.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: squeeze air into a rubber bladder. Units/quantities: ['mm'].
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.2.2. Vấn đề truyền áp suất vào tiếp xúc
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `WRITE_WITH_LIMITATIONS`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. **M06 — Caro and Carmichael (2024); Evidence M06-E02.** Áp suất nguồn là chân không trong buồng; lực pháp tuyến tại tiếp xúc đến từ chênh áp qua màng và không đồng nhất với áp suất cục bộ tại mọi giao diện. Bối cảnh: {'pressure': 'vacuum; atmospheric compression', 'interface': 'layer-layer friction', 'boundary': 'airtight chamber'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.3390/act13020064`; nguồn chấp nhận: `data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf`; locator: PDF p.5; printed p.NOT_REPORTED; source section: 3.1.3 Vacuum Pressure Jamming; figure/table/equation: Fig. 3c.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: generated by vacuum pressure is the most developed technology. Units/quantities: ['mm'].
  2. **M09 — Bai et al. (2022); Evidence M09-E04.** Áp suất dương của actuator và chân không của wire-jamming là hai biến khác nhau; không được gọi chúng là cùng một áp suất tiếp xúc. Bối cảnh: {'positive_pressure': '145 vs 87 kPa at 90°', 'vacuum': '0 to −85 kPa', 'application': 'gripper; wearable glove'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.3390/app12073582`; nguồn chấp nhận: `data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`; locator: PDF p.10; printed p.NOT_REPORTED; source section: Application / Fig. 5; figure/table/equation: Fig. 5.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: remarkably enhanced. Units/quantities: ['kPa', 'mm'].
  3. **M12 — Huynh et al. (2022); Evidence M12-E01.** Hai đường áp suất có vai trò khác nhau: negative pressure điều biến frictional jamming, positive pressure tạo biến dạng actuator. Bối cảnh: {'material': 'PDMS; aluminium oxide particles; flexible ECF micropump', 'pressure': 'negative for jamming; positive for bending', 'geometry': '24 x 8 x 6 mm actuator'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.1016/j.sna.2022.113449`; nguồn chấp nhận: `data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf`; locator: PDF p.3; printed p.NOT_REPORTED; source section: Concept / Fig. 2–3; figure/table/equation: Fig. 2.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: granular jamming by negative pressure of ECF jet flow. Units/quantities: ['mm'].
  4. **M22 — Zhang, Wang, Ye, and Xu (2018); Evidence M22-E01.** Mô hình laminated-beam là cầu nối cơ học gần với bó dây, nhưng cấu hình cáp khác MP1. Bối cảnh: Parallel-wire cable; distributed or midspan load.. Giới hạn chuyển sang MP1: VERIFIED_FULL_TEXT
     - DOI: `10.1061/(ASCE)ST.1943-541X.0002171`; nguồn chấp nhận: `data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf`; locator: PDF p.1; printed p.NOT_REPORTED; source section: Abstract; figure/table/equation: Abstract.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: idealized as laminated beams including interlayer slips. Units/quantities: ['stiffness', 'force', 'length'].
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.2.3. Phát biểu bài toán nghiên cứu
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `WRITE_WITH_LIMITATIONS`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. **M15 — Yi, Fan, and Liu (2024); Evidence M15-E01.** Đây là prior art mô hình động control-oriented cho LJ continuum robot, trực tiếp làm suy yếu claim rằng chỉ có homogenized static model. Bối cảnh: {'model': 'port-Hamiltonian + LuGre', 'system': 'tendon-driven LJ continuum robot', 'validation': 'OctRobot-I experiments'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.1109/ICRA57147.2024.10610912`; nguồn chấp nhận: `data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf`; locator: PDF p.1; printed p.NOT_REPORTED; source section: Abstract / Fig. 1; figure/table/equation: Fig. 1.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: energy-based model that is integrated with the LuGre frictional model. Units/quantities: NOT_REPORTED.
  2. **M16 — Fan, Yi, and Liu (2026); Evidence M16-E01.** Đây là counterevidence mới nhất trong corpus đối với giả định rằng mô hình động/constitutive liên quan chưa có. Bối cảnh: {'model': 'dynamical port-Hamiltonian + LuGre', 'scope': 'LJ continuum robot', 'year': '2026'}. Giới hạn chuyển sang MP1: NOT_REPORTED
     - DOI: `10.1109/TCST.2026.3690756`; nguồn chấp nhận: `data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf`; locator: PDF p.1; printed p.NOT_REPORTED; source section: Abstract / introduction; figure/table/equation: Abstract.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: models rely on static or quasi-static. Units/quantities: NOT_REPORTED.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.3.1. Mục tiêu tổng quát
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `EVIDENCE_INSUFFICIENT`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.3.2. Mục tiêu cụ thể
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `HUMAN_DECISION_PENDING`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.4.1. Câu hỏi nghiên cứu
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `HUMAN_DECISION_PENDING`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.4.2. Giả thuyết và logic phản chứng
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `EVIDENCE_INSUFFICIENT`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.5.1. Đối tượng nghiên cứu
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `EVIDENCE_INSUFFICIENT`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.5.2. Phạm vi thực hiện
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `HUMAN_DECISION_PENDING`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.5.3. Ngoài phạm vi và giới hạn suy luận
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `EVIDENCE_INSUFFICIENT`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.6.1. Tổng quan tài liệu
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `WRITE_WITH_LIMITATIONS`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. **M01 — Christine B. Feak and John M. Swales (2009); Evidence M01-E01.** Feak và Swales định nghĩa tổng quan tài liệu (literature review) là một “câu chuyện nghiên cứu” (research story) có cấu trúc logic chặt chẽ, liên kết các công trình tiền đề để dẫn dắt tất yếu đến bài toán của người nghiên cứu, thay vì lập danh mục tóm tắt rời rạc từng bài. Về mặt phương pháp luận, nguyên tắc này định hình cấu trúc lập luận cho Chương 1 và Chương 2 của luận văn MP1 (từ bối cảnh robot liên tục, nhu cầu biến đổi độ cứng, đến cơ cấu bó dây chịu ma sát). Phạm vi áp dụng thuần túy là phương pháp tổ chức văn bản học thuật; nguồn không cung cấp phương trình cơ học, dữ liệu thực nghiệm hay cơ sở đánh giá độ cứng của bó dây. Bối cảnh: NOT_REPORTED. Giới hạn chuyển sang MP1: Tài liệu phương pháp luận viết học thuật, không cung cấp dữ liệu cơ học thực nghiệm hay phương trình vật lý; phạm vi áp dụng giới hạn trong cấu trúc văn bản khoa học.
     - DOI: `N/A — sách; PDF người dùng cung cấp`; nguồn chấp nhận: `data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf`; locator: PDF p.3; printed p.NOT_REPORTED; source section: Introduction / Contents; figure/table/equation: Figure 1 / Contents.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: tell a research story. Units/quantities: ['NOT_REPORTED'].
  2. **M01 — Christine B. Feak and John M. Swales (2009); Evidence M01-E02.** Nguồn khẳng định tiêu chí lựa chọn tài liệu (selection criteria) phải được công bố tường minh để ranh giới khảo sát của tổng quan có thể kiểm chứng độc lập (auditable). Về mặt phương pháp luận, việc quy định rõ tiêu chí bao hàm (dầm phân lớp, cáp song song, cơ chế ma sát Coulomb, chuẩn đo lường GUM) và tiêu chí loại trừ giúp bảo đảm tính liêm chính khoa học, ngăn ngừa thiên vị xác nhận (confirmation bias) khi xây dựng corpus tài liệu cho MP1. Nguồn chỉ đóng vai trò hướng dẫn quy trình tổng quan; bản thân tiêu chí lựa chọn không chứng minh tính đầy đủ tuyệt đối của văn liệu hay xác nhận tính đúng đắn của mô hình cơ học. Bối cảnh: NOT_REPORTED. Giới hạn chuyển sang MP1: Quy tắc kiểm soát phạm vi tổng quan văn bản; không thay thế được các tiêu chuẩn kiểm chứng mô hình cơ học độc lập.
     - DOI: `N/A — sách; PDF người dùng cung cấp`; nguồn chấp nhận: `data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf`; locator: PDF p.25; printed p.NOT_REPORTED; source section: Getting Started on the Literature Review; figure/table/equation: Selection criteria.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: Describing the selection criteria for literature in the review. Units/quantities: ['NOT_REPORTED'].
  3. **M01 — Christine B. Feak and John M. Swales (2009); Evidence M01-E03.** Chất lượng của một tổng quan tài liệu được đánh giá thông qua tính mạch lạc trong cấu trúc, độ bao phủ hợp lý của văn liệu và năng lực xây dựng cuộc thảo luận độc lập (“original discussion”) bằng ngôn ngữ học thuật của chính người viết (paraphrase và critical synthesis), phân biệt rõ với việc sao chép hoặc tóm lược cơ học. Đối với MP1, nguyên tắc này hỗ trợ phương pháp so sánh đối chiếu giữa các mô hình dầm liên tục, mô hình phân lớp và kết quả đo lường; “tính độc lập” ở đây thuộc về năng lực tổng hợp phương pháp luận, không đồng nghĩa với việc tự ý suy diễn tính mới cơ học khi chưa có bằng chứng thực nghiệm. Bối cảnh: NOT_REPORTED. Giới hạn chuyển sang MP1: Tiêu chuẩn đánh giá văn phong và cấu trúc lập luận; không đại diện cho chuẩn đánh giá dung sai sai số đo lường hay độ tin cậy thực nghiệm.
     - DOI: `N/A — sách; PDF người dùng cung cấp`; nguồn chấp nhận: `data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf`; locator: PDF p.93; printed p.NOT_REPORTED; source section: Criteria for Evaluating Literature Reviews; figure/table/equation: Evaluation criteria.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: Criteria for Evaluating Literature Reviews. Units/quantities: ['NOT_REPORTED'].
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.6.2. Bench A và Bench B
- **Mục đích viết:** Trình bày Bench A/B như các quyết định thiết kế của tác giả để cô lập pressure input, SMA–piston behavior và điều kiện so sánh.
- **Readiness:** `AUTHOR_DEFINED_DRAFTABLE`
- **Không có bằng chứng external trực tiếp:** M01 chỉ hướng dẫn tổ chức literature review; không hỗ trợ thiết kế Bench A/B, input isolation hoặc pressure-matched comparison.
- **Nội dung được phép viết ở dạng đề xuất:** Bench A dùng nguồn áp ngoài để tách pressure input khỏi động lực nhiệt của SMA; Bench B đặc trưng SMA–piston trước khi tích hợp; hai bench phải dùng pressure gần mẫu và quy ước bất định chung nếu được human approval.
- **Điều kiện chuyển tiếp:** Năm quyết định human boundary và mismatch PDF RQ1–RQ5 với P3 RQ groups vẫn pending; không gọi Bench A/B là validation đã được nguồn công bố.

### 1.6.3. Đối chiếu mô hình và bất định
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `READY_TO_WRITE`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. **M38 — Joint Committee for Guides in Metrology (JCGM/WG 1) (2008); Evidence M38-E02.** Mục 4.1 và Phương trình (1)–(5) quy định kết quả của phép đo gián tiếp phải được biểu diễn qua mô hình hàm đo lường giải tích Y = f(X_1, \dots, X_N), trong đó đại lượng đo Y (như độ cứng K hoặc flexural rigidity EI) được xác định từ các đại lượng đầu vào X_i (lực tải F, độ võng \Delta w, chiều dài nhịp L). Đối với các đại lượng thu được từ chuỗi quan sát lặp lại độc lập, phương sai thực nghiệm của giá trị trung bình s^2(q_bar) = s^2(q_k)/n xác định độ không đảm bảo chuẩn Loại A u(q_bar) = s(q_k)/\sqrt{n}. Điều kiện áp dụng là hệ thống đo phải đạt trạng thái kiểm soát thống kê và hàm f phải bao quát đầy đủ mọi đại lượng vật lý ảnh hưởng. Bối cảnh: Measurement model. Giới hạn chuyển sang MP1: Giả định hàm đo lường f chứa đầy đủ mọi đại lượng ảnh hưởng và hiệu chỉnh; không tự động bù trừ các sai số mô hình vật lý chưa được nhận diện.
     - DOI: `N/A — hướng dẫn đo lường`; nguồn chấp nhận: `data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf`; locator: PDF p.8; printed p.NOT_REPORTED; source section: 4.1 Modelling the measurement; figure/table/equation: Eq. (4).
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: measurand Y is represented as a function of input quantities. Units/quantities: ['NOT_REPORTED'].
  2. **M01 — Christine B. Feak and John M. Swales (2009); Evidence M01-E01.** Feak và Swales định nghĩa tổng quan tài liệu (literature review) là một “câu chuyện nghiên cứu” (research story) có cấu trúc logic chặt chẽ, liên kết các công trình tiền đề để dẫn dắt tất yếu đến bài toán của người nghiên cứu, thay vì lập danh mục tóm tắt rời rạc từng bài. Về mặt phương pháp luận, nguyên tắc này định hình cấu trúc lập luận cho Chương 1 và Chương 2 của luận văn MP1 (từ bối cảnh robot liên tục, nhu cầu biến đổi độ cứng, đến cơ cấu bó dây chịu ma sát). Phạm vi áp dụng thuần túy là phương pháp tổ chức văn bản học thuật; nguồn không cung cấp phương trình cơ học, dữ liệu thực nghiệm hay cơ sở đánh giá độ cứng của bó dây. Bối cảnh: NOT_REPORTED. Giới hạn chuyển sang MP1: Tài liệu phương pháp luận viết học thuật, không cung cấp dữ liệu cơ học thực nghiệm hay phương trình vật lý; phạm vi áp dụng giới hạn trong cấu trúc văn bản khoa học.
     - DOI: `N/A — sách; PDF người dùng cung cấp`; nguồn chấp nhận: `data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf`; locator: PDF p.3; printed p.NOT_REPORTED; source section: Introduction / Contents; figure/table/equation: Figure 1 / Contents.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: tell a research story. Units/quantities: ['NOT_REPORTED'].
  3. **M39 —  (1994); Evidence M39-E01.** NIST TN 1297 khẳng định nguyên lý đo lường nền tảng: kết quả của bất kỳ phép đo nào chỉ là một giá trị ước lượng (estimate) của đại lượng cần đo và hoàn toàn chưa đầy đủ nếu thiếu công bố định lượng về độ không đảm bảo đo. Trong nghiên cứu uốn dầm bó dây TiNi của MP1, các đường cong quan hệ lực - độ võng hay giá trị độ cứng uốn suy ra không thể được coi là kết quả thực nghiệm hoàn chỉnh nếu không đi kèm với các dải độ không đảm bảo đo được lượng hóa chặt chẽ theo quy tắc chuẩn mực; nguyên lý này áp dụng cho mọi phép đo vật lý trong đề tài. Bối cảnh: Research and engineering measurements. Giới hạn chuyển sang MP1: Nguyên lý triết lý đo lường của NIST; không cung cấp số liệu sai số định lượng cụ thể cho thiết bị thử nghiệm cơ học uốn dầm.
     - DOI: `N/A — technical note`; nguồn chấp nhận: `data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf`; locator: PDF p.1; printed p.NOT_REPORTED; source section: 1 Introduction; figure/table/equation: NOT_APPLICABLE.
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: result of a measurement is only an approximation or estimate. Units/quantities: ['NOT_REPORTED'].
  4. **M38 — Joint Committee for Guides in Metrology (JCGM/WG 1) (2008); Evidence M38-E03.** Mục 5 và Phương trình (10)–(14) thiết lập Luật lan truyền độ không đảm bảo đo (Law of Propagation of Uncertainty): đối với các biến đầu vào không tương quan, phương sai kết hợp là tổng các số hạng [c_i u(x_i)]^2 với hệ số độ nhạy c_i = \partial f/\partial x_i; đối với các biến tương quan, phải bổ sung số hạng hiệp phương sai 2\sum c_i c_j u(x_i, x_j). Công thức dựa trên xấp xỉ chuỗi Taylor bậc một quanh điểm ước lượng. Trong MP1, nếu cảm biến lực và cảm biến dịch chuyển cùng gắn trên một khung thử nghiệm chịu ảnh hưởng của biến dạng đàn hồi khung hoặc nhiệt độ, việc bỏ qua tương quan sẽ dẫn đến đánh giá sai lệch độ không đảm bảo của độ cứng uốn EI. Bối cảnh: Linearized propagation framework. Giới hạn chuyển sang MP1: Dựa trên xấp xỉ chuỗi Taylor bậc một; khi hàm đo lường phi tuyến mạnh hoặc độ không đảm bảo đầu vào lớn, cần bổ sung số hạng bậc hai hoặc mô phỏng Monte Carlo.
     - DOI: `N/A — hướng dẫn đo lường`; nguồn chấp nhận: `data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf`; locator: PDF p.18; printed p.NOT_REPORTED; source section: 5 Determining combined standard uncertainty; figure/table/equation: Eqs. (10)-(13).
     - Claim status: `VERIFIABLE_FULL_TEXT`; exact anchor: combined standard uncertainty. Units/quantities: ['NOT_REPORTED'].
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.7.1. Ý nghĩa khoa học
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `EVIDENCE_INSUFFICIENT`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.7.2. Ý nghĩa kỹ thuật
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `EVIDENCE_INSUFFICIENT`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

### 1.8.1. Vai trò của từng chương
- **Mục đích viết:** Đặt section trong chuỗi lập luận dẫn từ nhu cầu kỹ thuật đến câu hỏi cơ học có thể kiểm chứng, đồng thời giới hạn claim.
- **Readiness:** `HUMAN_DECISION_PENDING`
- **Chuỗi luận cứ để người viết triển khai (không phải văn bản luận văn):**
  1. Không có Evidence Record được chấp nhận nhắm trực tiếp section này. Chỉ ghi mục tiêu/phạm vi như đề xuất; không biến thành kết quả đã biết.
- **Đồng thuận / khác biệt / không so sánh được:**
  - Đồng thuận chỉ ghi ở mức cơ chế hoặc phương pháp mà các record nêu trực tiếp; không cộng các record trùng dữ liệu thành nghiên cứu độc lập.
  - Khác biệt cần giữ theo topology, vật liệu, pressure/load input, branch và observable; không chuyển định luật giữa wire/fiber, layer, granular, cable, wire–tube và TiNi bundle.
  - Nếu chưa có record cùng geometry/interface/observable, ghi `không so sánh trực tiếp được`.
- **Giả định và ranh giới áp dụng:** giữ nguyên giả định mô hình, điều kiện tải, packing, sleeve/ngàm, biến dạng nhỏ/lớn và trạng thái nhiệt trong từng record; EI/E/K và lực pháp tuyến cục bộ không được đồng nhất.
- **Hình/bảng/phương trình nên kiểm tra:** xem locator trong từng argument; mọi tái sử dụng hình ảnh phải qua rà soát bản quyền (`REVIEW_REQUIRED_BEFORE_REUSE`), không sao chép hình nguyên bản.
- **Claims cấm/không đủ cơ sở:** không gọi thay đổi hình học/vật liệu/platform/actuator là novelty; không tuyên bố H1 hoặc universal pressure law; không suy ra local normal traction từ M–κ/F–δ toàn cục.
- **Chuyển tiếp khái niệm:** chốt cơ chế/giới hạn của section rồi chuyển sang section kế tiếp theo outline PDF; không tự tạo section hoặc đổi thứ tự.

