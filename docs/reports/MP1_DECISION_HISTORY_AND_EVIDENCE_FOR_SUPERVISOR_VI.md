# MP1: Lịch sử nghiên cứu, quyết định và bằng chứng cho thảo luận với người hướng dẫn

Ngày dựng lại: **26-09-2026**. Repository HEAD: `02ce5251df0a29247f3dba677a634f18ff754436`.

## 1. Mục đích và cách đọc

Báo cáo dựng lại MP1 từ đề xuất của người hướng dẫn, qua phân rã claim, tìm prior art, hai vòng verification, phản biện và hiệu chỉnh, đến câu hỏi phân biệt mô hình và các bước WR1/S01/S02 đã có trong repository.

Mục đích là giải thích **vì sao cách đặt vấn đề thay đổi**, chứ không bảo vệ đề xuất ban đầu hoặc tuyên bố đề tài đã mới. Báo cáo chỉ xét MP1, không đánh giá hoặc so sánh các hướng khác. Không có tìm kiếm mới, ingestion, mô phỏng, thí nghiệm hoặc adjudication mới trong lần dựng lại này.

Quy ước:

- **[HỒ SƠ QUYẾT ĐỊNH]**: ghi nhận dự án đã quyết định gì; không tự là bằng chứng quyết định đúng về khoa học.
- **[VERIFIED FULL TEXT]**: nội dung có nguồn evidence JSON hoặc source-level audit truy về PDF.
- **[METADATA ONLY]**: thông tin thư mục/abstract phục vụ tìm và sàng lọc; không dùng chứng minh cơ chế.
- **[INFERENCE]**: diễn giải, hệ quả hoặc đánh giá khả năng từ các nguồn; không phải kết quả đã đo.
- **[HYPOTHESIS]**: giả thuyết còn cần kiểm tra.

Các verdict lịch sử được giữ đúng phạm vi tại thời điểm đó. Một file mang tên “current” hoặc ghi “complete” có thể đã có successor artifact; hoàn thành xử lý hồ sơ không đồng nghĩa hoàn thành kiểm chứng khoa học.

## 2. Bức tranh tổng thể: MP1 đã đi qua những bước nào?

```text
Đề xuất mentor: bó dây NiTi + ép bằng áp suất dương + jamming
              + độ cứng uốn thay đổi + tùy chọn bơm/piston SMA
    ↓
Tách thành C1–C8 để kiểm tra từng căn cứ novelty
    ↓
MP1-V001: PIVOT_TO_MECHANICS_CORE
Các claim thành phần/kiến trúc rộng bị prior art bao phủ
    ↓
MP1-V002: T1/T2/T3 và parameter-substitution kill test
T1 đóng; T3 bị bao phủ đáng kể; T2 còn mở trong tập nguồn
    ↓
Reedlunn + Fang; trace packets → Astra critique → remediation
Không được suy “mô-đun hằng sai” thành “cần luật cơ học mới”
    ↓
Tách H0a / H0b / H1; hoàn tất citation protocol 15/15
    ↓
Final V002: SURVIVES_TARGETED_CITATION_CHASE
Chỉ sống sót trong phạm vi protocol, không chứng minh novelty toàn cầu
    ↓
W02 reconstruction/red-team closeout: CONDITIONAL / BLOCKED
8 khoảng trống khoa học, không thể dùng protocol closure thay phép thử
    ↓
WR1: lập lại tuyến kiểm chứng có gate
    ↓
S01: existing formulation sufficient in principle
S02: preparation complete; physical pilot NOT_YET_TESTED
```

**Điểm đến hiện tại không phải “đã tìm được luật coupling mới”.** Đó là một câu hỏi model discrimination: mô hình mạnh nhất xây từ cơ học đã biết có dự đoán được hệ MP1 hay không; nếu không, đã loại trừ được lỗi tham số, truyền áp, hình học, nhiệt và phép đo trước khi viện dẫn cơ chế mới hay chưa?

## 3. Nguồn gốc MP1: đề xuất hệ thống, không phải kết quả từ 54 bài

[HỒ SƠ QUYẾT ĐỊNH] [Research log, Phase 10](../project/RESEARCH_LOG.md) và [roadmap MP1](../protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md) ghi MP1 là đề xuất của mentor được mở thành một nhánh kiểm chứng riêng. Không có cơ sở để kể MP1 là một trong năm candidate được sinh trực tiếp từ discovery snapshot 54 bài.

Kiến trúc được đề xuất:

> Superelastic NiTi/metallic wire bundle + positive-pressure confinement + inter-wire frictional jamming + variable bending stiffness + optional SMA-driven syringe/piston pressure source.

Giải thích vật lý ở mức ý tưởng:

1. Bó nhiều dây có thể đổi độ cứng biểu kiến khi các dây trượt tương đối dễ hoặc bị lực ma sát cản trượt.
2. Confinement bên ngoài được dự kiến dùng để thay đổi điều kiện contact giữa các dây.
3. NiTi siêu đàn hồi bổ sung đáp ứng vật liệu có chuyển pha do ứng suất và phụ thuộc lịch sử, không giống một dây đàn hồi tuyến tính có một mô-đun cố định.
4. SMA syringe/piston chỉ là một phương án tạo áp suất dự kiến, không mặc nhiên là nội dung khoa học trung tâm.

[HYPOTHESIS] Điều hấp dẫn lúc đầu là liệu superelasticity và frictional assembly dưới confinement có tạo ra response đáng nghiên cứu. Nhưng “ghép những thành phần này trong cùng thiết bị” và “cần một mô tả cơ học chưa có” là hai claim khác nhau.

## 4. Tại sao phải tách thành C1–C8?

Nếu chỉ tìm một thiết bị có tên hoặc hình thức giống hệt MP1, có thể bỏ sót prior art tương đương về cơ học. V001 tách kiến trúc thành các câu hỏi có thể bị từng nguồn bác bỏ.

| Claim | Nội dung kiểm tra ở V001 | Kết luận V001 | Diễn tiến sau đó |
|---|---|---|---|
| C1 | Wire/fiber jamming để đổi stiffness có mới không? | `closed` | Không dùng làm novelty riêng |
| C2 | Positive-pressure jamming có mới không? | `closed` | Không dùng pressure sign như discovery mới |
| C3 | SMA và jamming cùng một thiết bị có mới không? | `closed` | Phải phân biệt SMA backbone/tendon với chính môi trường tiếp xúc |
| C4 | Nguồn áp suất compact/onboard cho jamming có mới không? | `closed` | Compact không đồng nghĩa fully untethered; không nâng scope tùy tiện |
| C5 | NiTi wires tự làm medium tiếp xúc/trượt ma sát | `open_in_supplied_corpus` | T1 của V002 đóng claim tồn tại rộng này |
| C6 | Positive confinement của bó NiTi | `open_in_supplied_corpus` | Về sau thu hẹp thành boundary/control condition, không tự là luật mới |
| C7 | NiTi–friction–pressure–bending stiffness coupling | `open_in_supplied_corpus` | Chuyển thành phép phân biệt H0b với nhu cầu bổ sung H1 |
| C8 | SMA syringe/piston cấp áp suất cho jamming | `substantially_preempted` | Không giữ làm đóng góp chính; rủi ro actuator substitution |

Nguồn canonical: [CORE_PRIOR_ART_AUDIT](../../outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json). “Open in supplied corpus” chỉ nói tập nguồn tại thời điểm đó chưa đóng claim; không phải tuyên bố chưa ai làm trên thế giới.

## 5. MP1-V001: prior art nào làm thay đổi đề xuất?

Matrix hiện có của V001 gồm **11 full-text entries**. Run canonical `20260922T055150Z`, verdict `PIVOT_TO_MECHANICS_CORE`, confidence `high`. Một bản history worker ghi matrix 10 bài ở pha chuẩn bị; không dùng số đó thay paper count 11 của run và matrix hoàn thành.

| Bài then chốt | Nội dung đã có [VERIFIED FULL TEXT] | Claim bị tác động | Điều chưa được chứng minh bởi riêng bài này |
|---|---|---|---|
| Bai et al. (2022), *Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming*, DOI `10.3390/app12073582`, `240fbf6022` | Wire/fiber bundles, vacuum-controlled inter-wire friction và stiffness; evidence tr. 4–5, 7–9 | C1 | Không phải active positive confinement của superelastic NiTi |
| Liu et al. (2021), *A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots*, DOI `10.1109/LRA.2021.3097255`, `182d854610` | Positive-pressure jamming và stiffness control | C2 | Medium là granular, không phải bó NiTi |
| Zhang & Yao (2026), *A variable stiffness omnidirectional chain based on positive-pressure fiber jamming*, DOI `10.5194/ms-17-481-2026`, `3aa8790db0` | Fiber bundle chịu positive pressure; friction, các regime jam/transition/slip và bending model, evidence tr. 3–6 | C1, C2; đe dọa gần nhất với C6/C7 | Sợi nylon không trực tiếp chứng minh constitutive response của NiTi; nhưng thay vật liệu chưa đủ mới |
| Takashima, Imazawa & Cho (2022), *Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon*, DOI `10.20965/jrm.2022.p0466`, `2cd907e77a`; các follow-up | Shape-memory material kết hợp granular jamming | C3 | NiTi backbone trong hạt không đồng nghĩa các dây NiTi tự tạo frictional medium |
| Matsumoto et al. (2024), *Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon*, DOI `10.1299/mej.24-00130`, `7ce492505d` | Ti-Ni transformation/recovery trong một cơ cấu variable stiffness | C3; T3 về sau | Recovery behavior không tự bằng pressure-controlled inter-wire friction |
| Huynh et al. (2022), *Soft actuator with switchable stiffness using a micropump-activated jamming system*, DOI `10.1016/j.sna.2022.113449`, `bbe88a0c04` | Micropump tích hợp kích hoạt jamming | C4 | Không suy thành hệ hoàn toàn không nguồn điện/reservoir ngoài |
| Wang, Ding & Sun (2024), *Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm*, DOI `10.1108/IR-11-2023-0305`, `c6a31066f8` | Motor/ball-screw piston nén particle core; NiTi có vai trò tendon | C4, C8 và nguy cơ nhầm C5 | Không phải fluid pressure ép hướng kính một bó NiTi tự jam |
| Pierce & Mascaro (2013), *A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump*, DOI `10.1109/TMECH.2012.2211032`, `de64029540`; Kotb et al. (2021), *Shape Memory Alloy Capsule Micropump for Drug Delivery Applications*, DOI `10.3390/mi12050520`, `55457a97c6` | SMA-driven pumping đã có | C8 | Không chứng minh đúng mọi hookup SMA–syringe–jamming từng được công bố |

Hai follow-up Takashima 2024/2026 còn lại nằm trong [matrix V001](../../outputs/verification/MP1-V001/verification_matrix.json); bảng trên gom theo vai trò, không phải danh sách đầy đủ 11 entries.

**Quyết định:** bỏ căn cứ novelty kiểu kết hợp component; tiếp tục kiểm tra C5–C7 dưới dạng mechanics core. Điều này không chứng minh chính xác toàn bộ assembly MP1 đã có tiền nhiệm, và không phải kết luận về khả năng bảo hộ thiết kế.

## 6. Sau V001: mechanics core được đặt như thế nào?

[HỒ SƠ QUYẾT ĐỊNH] Câu hỏi chuyển sang:

> Áp suất confinement dương, inter-wire slip/friction và superelastic NiTi response tương tác thế nào để quyết định bending stiffness và hysteresis của bó dây?

Kill test lúc đầu:

> Nếu framework elastic-fiber/contact hiện có chỉ cần thay modulus, friction và material parameters là đủ, thì claim mechanics đặc thù phải bị bác bỏ hoặc thu hẹp.

Đây là tiến bộ về khả năng falsify, nhưng từ “thay tham số” chưa đủ rõ. Nó có thể chỉ thay một hằng số modulus, hoặc dùng đầy đủ một constitutive law NiTi đã biết với internal state và history. Sự nhập nhằng này trở thành lỗ hổng lớn ở giai đoạn phản biện sau.

## 7. V002 tìm tài liệu bác bỏ bằng cách nào?

Theo [targeted citation-chasing protocol](../protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md), không mở lại broad search. Dự án dùng các anchor Bai, Zhang–Yao, Liu, Takashima/Matsumoto, Wang và những dòng cable/rope/strand mechanics được chúng dẫn tới.

| Target | Nội dung muốn tìm để bác bỏ | Từ vựng có trong protocol, dùng cho screening | Lý do không chỉ tìm “jamming” |
|---|---|---|---|
| T1 | NiTi wires là assembly có contact/slip/friction | `NiTi`, `Nitinol`, `superelastic alloy`; `wire bundle`, `wire rope`, `strand`, `cable`, `metallic fiber`; `inter-wire friction`, `interfilament friction` | Cable mechanics có thể đã giải hiện tượng dưới tên khác |
| T2 | Confinement tác động lực pháp tuyến và stiffness | `confining pressure`, `radial compression`, `transverse pressure`; `bending stiffness`, `flexural rigidity` | Contact pressure có thể xuất hiện trong submarine cable hoặc rope thay vì robotics |
| T3 | Transformation đi cùng contact, friction, hysteresis | `slip`, `stick-slip`, `locking`, `frictional stiffening`; NiTi transformation/superelastic response | Ghép luật vật liệu và contact có thể nằm trong FE/structural mechanics |

Đây là **vocabulary được ghi trong protocol**, không phải khẳng định từng tổ hợp đã được gửi nguyên văn lên search engine. Search thực tế phải truy về export, database, ngày và screening record.

Ở pha screening đầu, log ghi **187 raw records → 178 unique candidates** từ tám CSV; phân loại 12 `GET_FULL_TEXT`, 85 `KEEP_METADATA`, 81 `EXCLUDE`, không có metadata candidate được xếp `POTENTIAL_KILL_PAPER`. Con số zero này chỉ là triage, không phải chứng minh không có killer paper.

Human review không tải hàng loạt cả 12 bài: ưu tiên Reedlunn Part II và Fang vì trực tiếp tấn công parameter-substitution test. Từ tám bài full text ban đầu, matrix tăng lên mười; tập evidence mở rộng tiếp, đến matrix V002 hiện tại có **16 entries**.

Nguồn số liệu lịch sử: [log, Phases 14–20](../project/RESEARCH_LOG.md). Raw export và nhánh hiện tại truy từ [citation_coverage.json](../../outputs/verification/MP1-V002/citation_coverage.json), không phải lấy một manifest cũ làm tổng corpus hiện tại.

## 8. MP1-V002 đã đóng T1 và thu hẹp T2/T3 ra sao?

[HỒ SƠ QUYẾT ĐỊNH] Interim verdict `SUBSTANTIALLY_NARROWED`, confidence `high`. Bản `TARGETED_THREAT_AUDIT.json` tại HEAD là run `20260925T090319Z`, **16 papers**, không phải bản audit 10 bài mà trace-packet handoff cũ mô tả.

### T1 — NiTi contacting/slipping assembly đã có

[VERIFIED FULL TEXT] Carboni, Vahidi, Reedlunn cùng các nguồn NiTi rope/braid/micro-cable cho thấy NiTi đã được nghiên cứu trong assembly có contact/friction, structural stiffness và hysteretic response. Đây không chỉ là generic damping của một dây độc lập. T1 `closed_by_full_text` hợp lý ở **claim tồn tại rộng**.

Không suy thêm rằng từng interface đã được đo trượt, mọi cơ chế đã identifiable, hoặc mọi pressure-controlled bundle đã được validated. Việc đó không nằm trong closure của T1.

### T2 — active confinement chưa thấy trong tập nguồn, nhưng chưa là cơ học mới

Audit phân biệt:

| Nhãn áp suất | Nguồn áp lực | Ví dụ trong corpus | Giới hạn suy luận |
|---|---|---|---|
| P1 | Contact pressure thụ động do helix, tension hoặc deformation | Cable theory, Reedlunn/Xin Liu | Không tự là pressure điều khiển độc lập |
| P2 | Preload/confinement cố định | Tjahjanto có radial-pressure load case cố định | Không phải sweep active pressure; nhưng phương trình có thể nhận pressure khác |
| P3 | Positive confinement được thay đổi như control variable | Mục tiêu MP1 | Đổi từ fixed sang adjustable chưa chứng minh cần luật cơ học mới |

Các nhãn P1/P2/P3 ở đây là **vai trò áp suất trong MP1**, không phải mã hướng nghiên cứu.

Audit ghi `open_in_current_full_text_set`. Đó là kết luận về **bằng chứng ứng dụng/loading đã tìm được**, không chứng minh existing contact equations không mô tả được tải đó.

### T3 — transformation + friction + hysteresis không còn là claim mới chung

Vahidi ghép SMA constitutive response với interwire contact/friction; Carboni và các nguồn khác có NiTi assemblies, hysteresis và stiffness. Vì vậy `substantially_preempted` không chỉ dựa vào keyword overlap.

Phần còn hỏi về pressure-controlled bending phải chứng minh giá trị dự đoán hoặc explanatory value riêng. Không được nối logic: “các thành phần coupling đã biết; chỉ thiếu active pressure; vậy active pressure chính là novelty”.

Nguồn: [targeted audit V002](../../outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json), [matrix V002](../../outputs/verification/MP1-V002/verification_matrix.json).

## 9. Những bài cơ học làm thay đổi lập luận mạnh nhất

| Nguồn | Điều thực sự hỗ trợ | Tác động đến MP1 và điều không được suy quá |
|---|---|---|
| Reedlunn, Daly & Shaw (2013), *Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses*, DOI `10.1016/j.ijsolstr.2013.03.015`, `fac21c950e` | [VERIFIED FULL TEXT] Constitutive response và kinematics của subcomponents NiTi cable; giới hạn simplified cable model | Sai số khi bỏ local bending/twisting ở helix angle lớn không chứng minh cần luật mới cho pressure-controlled bundle |
| Fang et al. (2019), *Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application*, DOI `10.1016/j.engstruct.2019.01.049`, `2f7fcf2f8f` | [VERIFIED FULL TEXT] Hysteretic cable response và mô hình hiện tượng học/rút gọn | Fit tốt response vĩ mô có thể không cần resolve mọi contact; nhưng bằng chứng tensile/seismic không tự là validation pressure-controlled bending |
| Carboni, Lacarbonara & Auricchio, *Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification*, DOI `10.1061/(ASCE)EM.1943-7889.0000852`, `d9966f2f5e` | [VERIFIED FULL TEXT] NiTi/steel assemblies, tải và cấu hình khác nhau, hysteresis và identification | Phải phân biệt đúng vật liệu/cấu hình; không gán S2a steel cho NiTi pure bending. Corpus gọi 2014/2015; dùng DOI làm định danh ổn định |
| Carboni & Lacarbonara (2016), *Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments*, DOI `10.1061/(ASCE)EM.1943-7889.0001072`, `40760daa02` | [VERIFIED FULL TEXT theo V002] NiTi assembly, hysteresis, model/experiment | Coupled structural response đã được nghiên cứu; không mặc nhiên mọi microscopic cause đã được đo độc lập |
| Vahidi et al., *Mechanical response of single and double-helix SMA wire ropes*, DOI `10.1080/15376494.2021.1955313`, `53200aa0c6` | [VERIFIED FULL TEXT] 3D solid FE, Souza SMA UMAT và frictional interwire contact; nguồn mô hình constitutive đã tồn tại | Strong H0b precedent, không phải Auricchio–Petrini như một số summary ghi; tensile helical ropes không phải validation MP1 |
| Tjahjanto, Tyrberg & Mullins (2017), *Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable*, `ccdc1bb980` | [VERIFIED FULL TEXT] Geometrically nonlinear FE, frictional contact, bending/axial load/radial pressure | Pressure đã vào boundary-value problem; không đo được mapping áp suất→contact force của MP1 chỉ bằng bài này |
| Xin Liu (2004), *Cable Vibration Considering Internal Friction*, `aaad9c248c` | [VERIFIED FULL TEXT] Luận văn có reduced cable dynamics và quan hệ flexural rigidity–curvature với internal pressure information | Reduced comparator, không tự giải local contact hay transformation. Không gọi tài liệu này là journal paper |
| Barsi, Carboni & Lacarbonara (2025), *A new mechanical model of short wire ropes: Theory and experimental validation*, DOI `10.1016/j.engstruct.2024.119217`, `9f4295be23` | [VERIFIED FULL TEXT] Shear-deformable rope model và stiffness bounds theo slip-state assumptions | Bound/limit state không tương đương solved pressure-dependent evolving stick-slip path |
| Kang et al. (2020), *Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables*, DOI `10.3901/JME.2020.14.065`, `56793dea9b` | [VERIFIED FULL TEXT theo S01 PDF crosscheck] SMA UMAT, 3D solid FE, smooth/frictionless interwire contact trong tensile model | Không mô tả thành Coulomb beam-contact model có bending validation; frictional contact của H0b cần nguồn khác |

Các nguồn Reedlunn Part I, Salvatore 2021, Narjabadifam 2024, Liu 2023, Niu & Chen 2021, Liu 2026 và Silva 2022 cũng thuộc 16-entry matrix. Bảng chọn các bài làm thay đổi lập luận, không giả vờ toàn corpus chỉ có chín bài. Primary IDs và evidence paths nằm trong matrix; có cả luận văn và conference source, nên không gọi toàn bộ 16 entries là “16 peer-reviewed journal papers”.

## 10. Phản biện Astra: tại sao đã có nhiều evidence mà vẫn chưa đủ?

Stage 1 tạo 11 trace packets trên danh mục mở rộng lúc đó; đây là **evidence-preparation artifacts**, không phải verdict. Stage 2 tập trung vào logic evidence→claim. Nguồn: [critique ngày 25-09](MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md), [packet manifest](../../outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/00_PACKET_MANIFEST.md).

| Vấn đề | Sai bước suy luận cần loại bỏ | Hệ quả đối với hướng nghiên cứu |
|---|---|---|
| H0 không rõ | Constant-modulus model không đủ → cần coupling law mới | Phải có baseline mạnh hơn, dùng NiTi constitutive law đã biết |
| P3 bị xem là mechanism mới | Chưa tìm thấy active-pressure experiment → existing mechanics không áp dụng | Phải kiểm tra equations và boundary conditions, không chỉ test cases đã công bố |
| Coexistence chưa chứng minh | NiTi có chuyển pha, bundle có slip → chúng chắc chắn cùng hoạt động trong specimen | Cần miền vận hành thực sự có cả hai cơ chế |
| Global response không identifiable | Moment–curvature khác → do contact–transformation coupling mới | Cần local observables và loại trừ fixture, membrane, hình học, nhiệt |
| Tham số bù trừ | Model fit tốt → cơ chế đã được xác nhận | Calibration độc lập và forward prediction chưa fit |
| Áp suất buồng bị dùng như contact force | Đo được pressure → đã biết lực pháp tuyến tại wires | Cần pressure-transfer/contact mapping và uncertainty |
| Threshold/stiffness chưa định nghĩa | Mọi stiffness hoặc hysteresis metric là cùng đại lượng | Phải khóa output, branch, rate, temperature, history |
| Citation chưa đóng | Không thấy exact match → chỉ còn thiếu một chi tiết mới | Hoàn tất named branches; giữ kết luận protocol-bounded |

### Đính chính Carboni có ý nghĩa gì?

[VERIFIED FULL TEXT qua PDF correction] Carboni Table 4, tr. 9–10 theo locator của correction: **S2a dùng ST49 steel; S1a dùng NiTi7 và chịu tension–bending**. Packet cũ đã dùng S2a như bằng chứng NiTi transformation trong pure bending; phép suy đó không hợp lệ.

Nguồn: [W04 Carboni correction](../../outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W04_T1_REAUDIT_CARBONI_CORRECTION.md). Chính file correction này vẫn chứa vài diễn giải mô hình Vahidi/Kang bị S01 sửa tiếp; vì vậy không coi nhãn “remediated” là bảo đảm tất cả nội dung đúng.

Sai cấu hình làm mất một bằng chứng cụ thể, nhưng không xóa các bằng chứng độc lập đóng T1 và thu hẹp T3.

## 11. Thay đổi cốt lõi: tách H0a, H0b và H1

Sau critique/remediation, “parameter substitution” không còn được dùng như một lựa chọn nhị phân mơ hồ.

| Giả thuyết | Nội dung | Trạng thái được giữ trong W02/WR1/S01/S02 | Ý nghĩa |
|---|---|---|---|
| H0a | Thay một modulus hằng và vài tham số trong elastic-wire model | `REFUTED_IN_TRANSFORMATION_REGIME` | Không đại diện được đầy đủ response chuyển pha; không nói mọi miền elastic-only đều sai |
| H0b | Luật NiTi transformation-aware đã biết + contact/friction/geometry/pressure mechanics đã biết | `NOT_FALSIFIED_LIVE_COMPETITOR` | Đối thủ khoa học thật sự; có thể đủ mà không cần luật mới |
| H1 | Cần mô tả constitutive–contact coupling bổ sung ngoài H0b đã được xác định | `INSUFFICIENT_EVIDENCE` | Chưa có bằng chứng xác lập tính cần thiết |

**Bác bỏ H0a không suy ra H1 đúng.** Ngay cả H0b dự đoán sai cũng chưa tự chứng minh H1: còn phải loại trừ calibration error, numerical error, sai boundary/pressure transmission, material law không phù hợp, geometry/history và uncertainty.

Fang đặc biệt quan trọng ở đây: [INFERENCE] một reduced/macroscopic model có thể đủ cho output vĩ mô dù không giải từng interface. Ngược lại, một detailed FE model có nhiều tham số chưa được identification cũng không tự có explanatory value cao hơn.

Nguồn: [remediation synthesis](MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md), [W02 final state](../../outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json), [S01 strongest H0b](../../outputs/execution/MP1-V002/WR1/S01/MP1_S01_H0B_MODEL_SPECIFICATION.md).

## 12. Citation closure và final MP1-V002: sống sót nghĩa là gì?

Lịch sử có nhiều snapshot: tám bài → mười bài; danh mục trace packet mở rộng 24 nguồn; matrix V002 về sau 16 entries. Các số này khác phạm vi và thời điểm. V001 hiện 11 entries, V002 hiện 16; không dùng “24 bài” của manifest cũ làm tổng hiện hành.

Coverage cũng thay đổi:

1. Pha đầu có 14 required directions, backward 8 và forward 6; stop condition chưa thỏa.
2. Các high-threat anchors được bổ sung/điều chỉnh. Cuối cùng canonical coverage là backward **9/9**, forward **6/6**, tổng **15/15**.
3. B11 Kang và B12 Barsi cuối đợt ghi 22 và 46 records; W02 reconciliation ghi 68 raw/67 unique cho hai nhánh này. Không nhầm với 187/178 của pha screening trước.
4. Cutoff là **25-09-2026**; `stop_condition.satisfied = true`; không còn unresolved named high-threat source trong protocol.

Nguồn: [citation coverage](../../outputs/verification/MP1-V002/citation_coverage.json), [W02 citation reconciliation](../../outputs/execution/MP1-V002/W2/MP1_W02_FINAL_SYNTHESIS.md).

[HỒ SƠ QUYẾT ĐỊNH] [Final V002 adjudication](../../outputs/verification/MP1-V002/FINAL_ADJUDICATION.json), run `20260925T093414Z`:

```text
protocol_outcome = SURVIVES_TARGETED_CITATION_CHASE
confidence = high
direct_kill_found = false
citation_coverage_closed = true
```

Đó là **kết luận cuối của vòng citation protocol**, không phải chứng minh global novelty hoặc H1. Confidence high gắn với kết luận trong phạm vi đó, không phải xác suất đề tài mới.

Title draft trong quyết định này:

> **Modeling and Experimental Characterization of Pressure-Controlled Bending Mechanics in Superelastic NiTi Wire Bundles**
>
> **Mô hình hóa và đặc trưng thực nghiệm cơ học uốn của bó dây NiTi siêu đàn hồi dưới áp suất giam giữ điều khiển.**

Tên trên là **bản nháp lịch sử**, không phải một tên đề tài mới được báo cáo này phê duyệt. Dự án về sau lưu MP1 như viable conditional alternative; đây là vị trí workflow, không phải phán quyết rằng MP1 scientifically invalid.

## 13. Vì sao sau “survives” còn cần W02 và red-team?

Vì ba loại kết luận khác nhau:

- **Search closure:** đã xử lý đủ các nhánh trong protocol.
- **Prior-art disposition:** trong tập đó chưa có direct kill của claim hẹp.
- **Scientific defensibility:** câu hỏi còn lại có đo được, phân biệt được, và vượt routine application hay không.

Hai loại đầu không bảo đảm loại thứ ba. Workflow sau đó tái dựng lịch sử và thử bác bỏ mechanics core bằng K-tests.

[HỒ SƠ QUYẾT ĐỊNH] Các historical subruns W2-01…W2-09 lần lượt phục vụ: lịch sử trạng thái; C1–C8; T1–T3/H0; paper roles; citation provenance; critique/remediation crosswalk; evidence registers; K1–K9; Astra red-team.

Chuỗi từng bị tổ chức như 12 bước bắt buộc; sau đó được sửa thành **macro-stage W02 closeout**. W2-10/W2-11/W2-12 không chạy và bị supersede. Đây là sửa workflow, không phải ba thí nghiệm bị bỏ dở.

W02 kết thúc:

```text
analytical/evidence closeout = COMPLETE
candidate = CONDITIONAL
scientific gate = BLOCKED
blocking scientific gaps = 8
unresolved K tests = K2,K3,K6,K7,K9
final novelty adjudication in W02 = NOT PERFORMED
```

Nguồn: [W02 final state](../../outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json), [K reconciliation](../../outputs/execution/MP1-V002/W2/MP1_W02_K1_K9_RECONCILED_MATRIX.json), [red-team W2-09](../../outputs/execution/MP1-V002/W2-09/W2_09_ASTRA_RED_TEAM_REPORT.md).

Có **năm K-tests mang nhãn unresolved**, nhưng danh sách **blocking K-tests gồm tám** vì một số partial-overlap tests cũng còn chặn gate. Không kể hai con số này thành mâu thuẫn hoặc dùng “0 kill” để gọi là pass.

## 14. WR1/S01/S02: bước mới nhất đã làm đến đâu?

### 14.1 WR1 đã hoàn tất routing, không còn chỉ là next task

[WR1 final state](../../outputs/execution/MP1-V002/WR1/MP1_WR1_FINAL_STATE.json) ghi `COMPLETE_ROUTING_ONLY`. Nó phân tuyến tám gaps sang analytical, identifiability, calibration và feasibility gates. Không chạy literature search hay chứng minh H1; không hồi sinh W2-10…W2-12.

Snapshot/handoff cấp project vẫn ghi “next = WR1”; phải đọc successor này để không báo tiến độ cũ.

### 14.2 S01 đã trả lời câu hỏi formulation-level

[HỒ SƠ QUYẾT ĐỊNH] [S01 report](../../outputs/execution/MP1-V002/WR1/S01/MP1_S01_H0B_MODEL_SPECIFICATION.md) và [receipt](../../outputs/execution/MP1-V002/WR1/S01/MP1_S01_EXECUTION_RECEIPT.json) chọn:

> **EXISTING_FORMULATION_SUFFICIENT_IN_PRINCIPLE.**

[INFERENCE từ các formulations full text] Một explicit-wire 3D FE framework có thể kết hợp constitutive NiTi có transformation/history, frictional surface contact, deformable membrane, external pressure và bending/prestrain. Chưa chỉ ra được field equation hoặc coupling term nào chắc chắn thiếu về nguyên lý.

Đây là thay đổi quan trọng theo hướng **làm yếu căn cứ phải xây luật mới**, không phải bằng chứng H0b đã dự đoán đúng MP1. S01 chưa implement, calibrate hoặc validate hệ MP1.

Strongest H0b dự kiến gồm:

- Geometry/packing/prestrain thực của bó dây, không tự thay bằng helical cable khác.
- Established NiTi constitutive law phù hợp với specimen và thermal/history regime; Souza trong Vahidi là precedent đã kiểm tra.
- Contact có normal traction, separation và tangential friction/slip.
- Membrane chịu fluid pressure trên đúng fluid-wetted boundary; contact forces được tính qua equilibrium/packing hoặc bounded independently calibrated transfer model.
- Independent calibration và numerical verification trước khi khóa model cho untouched validation.

Chamber pressure có đơn vị áp suất; interwire force là lực tích phân từ contact traction. Không được đồng nhất chúng về giá trị hoặc ý nghĩa vật lý.

### 14.3 S02 mới hoàn tất chuẩn bị pilot

[S02 receipt](../../outputs/execution/MP1-V002/WR1/S02/MP1_S02_PREPARATION_RECEIPT.json) ghi:

```text
stage_status = PREPARATION_COMPLETE_PHYSICAL_PILOT_PENDING
physical_pilot_status = NOT_YET_TESTED
physical_experiment_performed = false
pressure_test_performed = false
H1_formulated = false
```

[HYPOTHESIS / engineering starting point] Pilot đề xuất bắt đầu từ ba dây NiTi bố trí tam giác trong positive-pressure cuff. Đây là một phép sàng lọc khả thi nhỏ, không phải specimen đã chế tạo, kích thước đã phê duyệt hoặc đại diện tự động cho mọi bó lớn.

Pilot phải kiểm tra sealed access, relative wire motion, tín hiệu transformation-sensitive đã được calibration, nhiệt, curvature, fixture/membrane motion và độ bền specimen. Tín hiệu biến dạng gián tiếp không được gọi là phép đo phase trực tiếp nếu chưa được xác nhận.

Trước physical execution cần người nghiên cứu chọn wire lot, cuff/fixture, giới hạn pressure/strain/fatigue và safety procedure được phê duyệt. Báo cáo này không ban hành thông số hoặc cho phép pressurization.

Nguồn: [S02 preparation handoff](../../outputs/execution/MP1-V002/WR1/S02/MP1_S02_PREPARATION_HANDOFF.md). Một negative result ở ba dây không tự bác bỏ toàn bộ bó mục tiêu nếu chưa có domain-coverage argument.

## 15. Ma trận lịch sử quyết định

Các ID `MH` là mục đọc của báo cáo này, không phải verdict mới hoặc ID thay canonical state.

| ID / pha | Claim hoặc câu hỏi trước | Nguồn kích hoạt thay đổi | Quyết định / thay đổi | Cái còn lại |
|---|---|---|---|---|
| MH01 — mentor proposal, Phase 10 | Tổ hợp NiTi–positive pressure–jamming–SMA pump có thể mới | Mentor proposal/roadmap | Mở MP1 để audit, chưa chấp nhận novelty | C1–C8 cần kiểm chứng |
| MH02 — V001, 22-09 run | Wire jamming, positive pressure, SMA+jamming, compact source | Bai, Liu, Zhang–Yao, Takashima, Huynh, Wang, SMA pumps | `PIVOT_TO_MECHANICS_CORE` | C5–C7 mở trong supplied corpus |
| MH03 — V002 protocol | NiTi làm frictional medium có thể khác | Citation chasing sang rope/strand/cable mechanics | Định nghĩa T1/T2/T3 và kill test | Kiểm tra equivalent mechanics thay exact architecture |
| MH04 — initial V002 | NiTi-contact/friction có thể chưa có | Carboni, Vahidi, Reedlunn và các nguồn NiTi rope/braid | T1 đóng; T3 substantially preempted | T2 active confinement chưa được đóng trong tập nguồn |
| MH05 — metadata expansion | Substitution chưa ngã ngũ | 187/178 triage; human selection Reedlunn II/Fang | 8 → 10 full-text matrix | Chưa đủ kết luận baseline hay luật mới thắng |
| MH06 — Stage 1–2, 25-09 | Trace packets tưởng đã nối được mechanism→gap | Astra G01–G12; Carboni configuration error | Yêu cầu remediation, không defend packets | Định nghĩa baseline, observability và evidence scope |
| MH07 — Stage 3 | Elastic substitution fail → distinct coupling | Remediation và 16-entry corpus | Tách H0a/H0b/H1; P3 là boundary/control input | H0b sống; H1 insufficient |
| MH08 — coverage closure, 25-09 | Search stop chưa thỏa | B11/B12 và các nhánh đã xử lý | 15/15 protocol closure | Không suy global absence |
| MH09 — final V002, 25-09 run | Có đủ cơ sở kết thúc citation chase không? | 16-entry matrix + coverage | `SURVIVES_TARGETED_CITATION_CHASE`, high | Model-discrimination candidate; chưa kiểm chứng thực nghiệm |
| MH10 — W02 closeout, 26-09 | Protocol survival đủ để bảo vệ mechanics core? | W2-01…09 và red-team/K-tests | `CONDITIONAL / BLOCKED`; 8 gaps | Cần forward baseline, local measurements và feasibility |
| MH11 — WR1 | Tiếp tục chuỗi worker hay xử lý scientific dependencies? | W02 gap register | `COMPLETE_ROUTING_ONLY` | S01/S02 entry gates; không chạy W2-10…12 |
| MH12 — S01, 26-09 | Existing theory có thiếu formulation cần thiết không? | PDF Barsi/Tjahjanto/Xin Liu/Kang/Vahidi | `EXISTING_FORMULATION_SUFFICIENT_IN_PRINCIPLE` | Quantitative adequacy của H0b chưa kiểm tra |
| MH13 — S02 preparation | Có đạt slip+transformation và đo được không? | Pilot protocol và channel/uncertainty design | `PREPARATION_COMPLETE_PHYSICAL_PILOT_PENDING` | Gate NOT_YET_TESTED; cần phê duyệt và bằng chứng vật lý |

Ngày run là mốc provenance có thể kiểm tra, không mặc nhiên là ngày mentor chấp thuận. History worker có một số timestamp không tăng theo thứ tự pha; báo cáo không dựng một chronology theo giờ từ chúng.

## 16. Tám khoảng trống khoa học chưa được việc viết protocol giải quyết

| Gap | Điều còn thiếu | Vì sao quyết định được MP1 có đứng vững không? |
|---|---|---|
| GAP-01 | Locked forward prediction của H0b | Chưa biết existing model có đủ; không được mặc định cần H1 |
| GAP-02 | Mechanism identifiability | Global bending curve không tách được transformation, slip, geometry, membrane hoặc fixture |
| GAP-03 | Pressure-to-contact mapping | Sai truyền áp có thể bị gọi nhầm là sai constitutive law |
| GAP-04 | Independent calibration, kiểm tra parameter compensation | Có thể fit cùng curve bằng nhiều bộ tham số khác nhau |
| GAP-05 | Miền coexistence slip–transformation khả thi và bền | Nếu không đạt cả hai, câu hỏi coupling hiện tại không được phép thử |
| GAP-06 | Kiểm soát/định lượng thermal, rate, training và history effects | Hysteresis hoặc stiffness đổi chưa chắc do contact mechanism được giả thuyết |
| GAP-07 | Quantitative sufficiency của existing formulations | S01 giải triage ở mức nguyên lý; không phải empirical pass |
| GAP-08 | Local observable channels dưới seal không làm thay đổi mechanics quá mức | Không đo được tín hiệu phân biệt thì kết quả dễ rơi vào non-identifying |

Nguồn: [W02 blocking gap register](../../outputs/execution/MP1-V002/W2/MP1_W02_BLOCKING_GAP_REGISTER.json), [WR1 gap routing](../../outputs/execution/MP1-V002/WR1/MP1_WR1_GAP_ROUTING_MATRIX.json), S01/S02 receipts. Việc các file analysis đã hoàn thành không đóng các gaps vật lý này.

## 17. Những sai khác hoặc overclaim cần tránh khi trình bày

| Vấn đề trong các bản tổng hợp | Cách dùng bằng chứng trong báo cáo này |
|---|---|
| Manifest cũ nói canonical V002 10 bài, danh mục mở rộng 24; hiện matrix 16 | Giữ state-at-time; dùng matrix/run provenance khi nói hiện tại |
| Handoff packet nói substitution `false/false/insufficient`; interim JSON HEAD ghi `requires_distinct... = true`, `established` | Công khai khác biệt. Final V002/W02 tách bác bỏ modulus hằng khỏi chứng minh luật mới; không tự sửa JSON cũ |
| W02 synthesis gọi cả 16 nguồn là peer-reviewed papers | Corpus có luận văn Xin Liu và conference source; không nâng source type |
| Packet/correction gán S2a Carboni cho NiTi pure bending | Dùng Table 4 correction: steel S2a; NiTi S1a tension–bending |
| Vahidi được gọi Auricchio–Petrini trong worker/correction cũ | Primary evidence và S01 kiểm tra PDF xác định Souza model |
| Kang được kể là Coulomb beam model đã validate bending | S01 PDF audit xác định solid FE, smooth contact, tensile loading |
| Barsi được kể như đã giải evolving slip transitions | S01 xác định stiffness bounds theo assumed states, không phải pressure-controlled transition solve |
| “Đã khắc phục 100% critique” trong log/remediation | Có thể là hoàn tất xử lý văn bản; không chứng minh calibration, local sensing hoặc coexistence đã được thực hiện |
| Snapshot “next WR1”, WR1 handoff “S01/S02 chưa chạy”, S01 handoff “S02 unexecuted” | Successors ghi WR1 routing complete, S01 analytical complete, S02 preparation complete. Physical pilot vẫn chưa chạy |
| Thiếu DOI Tjahjanto/Xin Liu | Ghi DOI chưa xác minh trong nguồn, không nói chắc chắn DOI không tồn tại; không loại full text chỉ vì thiếu DOI |
| H0b held-out failure được wording như chứng minh H1 cần thiết | Giữ như hypothesis cần kiểm tra; WR1 phân biệt failure có giải thích, uncertainty-dominated và nhu cầu nghiên cứu H1 về sau |
| W02/history summary có attribution/year hoặc timestamp khác nguồn gốc | Ưu tiên DOI/paper_id/PDF; không sao chép nguyên danh mục tác giả hoặc giờ quyết định từ worker |

Nguồn xử lý: [S01 formulation crosswalk](../../outputs/execution/MP1-V002/WR1/S01/MP1_S01_FORMULATION_CROSSWALK.json), [W02 contradiction reconciliation](../../outputs/execution/MP1-V002/W2/MP1_W02_CONTRADICTION_RECONCILIATION.json), canonical audits và successor receipts đã dẫn.

Một điểm giới hạn diễn đạt khác: pressure là boundary input **không đồng nghĩa pressure không thể gây response phức tạp hoặc coupling đáng nghiên cứu**. Kết luận đúng là sự thay đổi input không tự đòi hỏi một luật mới; độ đầy đủ của model vẫn phải được kiểm tra.

## 18. Câu hỏi hiện tại và cách nói với người hướng dẫn

### Một câu

MP1 hiện hỏi liệu mô hình NiTi–contact đã biết, với tham số được xác định độc lập, có dự đoán được uốn của bó dây dưới confinement điều khiển trong miền thực sự có cả slip và transformation hay không.

### Một đoạn giải thích lịch sử

“Ban đầu em xuất phát từ tổ hợp bó dây NiTi, áp suất dương và jamming. Kiểm chứng đầu tiên cho thấy các nguyên lý wire jamming, positive-pressure jamming, SMA kết hợp jamming và nguồn áp suất nhỏ gọn đã có. Khi chuyển sang mechanics, tài liệu cáp NiTi lại cho thấy contact, friction và transformation cũng đã được nghiên cứu. Vì vậy câu hỏi còn lại không thể là thay vật liệu hay thêm áp suất. Phản biện yêu cầu dùng một đối chứng mạnh: constitutive law NiTi đã biết ghép với contact, membrane và tải thực. Phân tích mới nhất thấy formulation đó đủ về nguyên lý, nhưng chưa biết khả năng dự đoán định lượng cho specimen MP1. Hiện em mới có thiết kế phép thử để kiểm tra coexistence, khả năng đo và sau đó model discrimination; chưa có kết quả để nói cần một luật mới.”

### Điều được phép và không được phép kết luận

Được phép nói: **claim ban đầu đã được thu hẹp có truy nguyên; literature protocol đã đóng trong phạm vi quy định; existing theory là một đối thủ chưa bị bác bỏ; việc kiểm chứng vật lý còn thiếu.**

Không được nói: **MP1 đã novel, H1 đã được chứng minh, active pressure tự tạo mechanics mới, hoặc pilot/forward validation đã thành công.**

## 19. Từ đây còn những bước nào — theo workflow đã có?

Đây là tóm tắt tuyến WR1, không phải một proposal mới hoặc lệnh thực thi:

1. Human review S01 và lựa chọn actual specimen/cuff/measurement/safety inputs cho S02.
2. Thực hiện S02 pilot khi được cho phép: kiểm tra sealed coexistence, local channels, nhiệt/rate/history và specimen integrity. Negative/uncertain phải được xử lý đúng domain, không ép pass.
3. Khi entry gates cho phép, S03 kiểm tra identifiability; S04 independent calibration, gồm pressure transmission, NiTi, friction, membrane và fixture.
4. S05 implement/verify/lock H0b, parameters, uncertainty và tiêu chí đánh giá trước dữ liệu validation chưa dùng.
5. S06 thu dữ liệu untouched; S07 đánh giá forward predictions. Nếu H0b adequate, claim “cần luật mới” bị thu hẹp/bác bỏ trong domain. Nếu systematic failure có local evidence, mới có cơ sở cho điều tra bổ sung; nếu uncertainty/non-identifiability chi phối, chưa phân xử được.

Không có broad search tự động, không chạy thêm expensive critique chỉ để kéo dài workflow. Named retrieval chỉ mở theo trigger thực sự thiếu phương trình, specimen limit hoặc sensing specification.

Nguồn: [WR1 execution graph](../../outputs/execution/MP1-V002/WR1/MP1_WR1_EXECUTION_GRAPH.json), [stage gates](../../outputs/execution/MP1-V002/WR1/MP1_WR1_STAGE_GATE_REGISTER.json), [S02 preparation handoff](../../outputs/execution/MP1-V002/WR1/S02/MP1_S02_PREPARATION_HANDOFF.md).

## 20. Chỉ mục bằng chứng để mở khi thảo luận

### Hồ sơ quyết định và lịch sử

- [Research log, MP1 Phases 10–24 và W02 closeout](../project/RESEARCH_LOG.md).
- [MP1 current narrative](../project/MP1_MENTOR_PIVOT_CURRENT.md): cần đọc kèm WR1/S01/S02 successors.
- [V001 canonical verdict](../../outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json), [V001 matrix](../../outputs/verification/MP1-V001/verification_matrix.json).
- [V002 interim audit](../../outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json), [V002 final adjudication](../../outputs/verification/MP1-V002/FINAL_ADJUDICATION.json), [V002 matrix](../../outputs/verification/MP1-V002/verification_matrix.json).
- [Stage 2 critique](MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md), [Stage 3 remediation](MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md).
- [W02 final state](../../outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json), [WR1 state](../../outputs/execution/MP1-V002/WR1/MP1_WR1_FINAL_STATE.json), [S01 handoff](../../outputs/execution/MP1-V002/WR1/S01/MP1_S01_HANDOFF.md), [S02 receipt](../../outputs/execution/MP1-V002/WR1/S02/MP1_S02_PREPARATION_RECEIPT.json).

### Evidence JSON của các bài then chốt

Các JSON dưới đây có bibliographic fields, source provenance và page locators. Nếu JSON/worker trái với PDF correction mới hơn, dùng correction được dẫn ở mục 17 và PDF gốc, không lặng lẽ đổi lịch sử.

- [Bai 2022 — 240fbf6022](<../../data/evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json>).
- [Zhang & Yao 2026 — 3aa8790db0](<../../data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json>).
- [Takashima 2022 — 2cd907e77a](<../../data/evidence/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json>).
- [Wang 2024 — c6a31066f8](<../../data/evidence/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json>).
- [Reedlunn Part II — fac21c950e](<../../data/evidence/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json>).
- [Fang 2019 — 2f7fcf2f8f](<../../data/evidence/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json>).
- [Carboni assemblies — d9966f2f5e](<../../data/evidence/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json>).
- [Vahidi — 53200aa0c6](<../../data/evidence/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json>).
- [Tjahjanto 2017 — ccdc1bb980](<../../data/evidence/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json>).
- [Xin Liu thesis — aaad9c248c](<../../data/evidence/A5-Cable vibration considering internal friction_aaad9c248c.json>).
- [Barsi 2025 — 9f4295be23](<../../data/evidence/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json>).
- [Kang 2020 — 56793dea9b](<../../data/evidence/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json>): filename 2025 không phải publication year.

Các nguồn khác truy từ matrices theo `paper_id` đã nêu, không điền DOI hoặc page number bằng suy đoán. Locator ở nội dung báo cáo là locator của evidence/audit; khi đưa vào thesis reference chính thức cần phân biệt PDF page và printed page. Carboni có year 2014 trong evidence/file label 2015; Vahidi online 2021/file label 2022: ghi rõ thay vì âm thầm đổi năm.

### Phạm vi hoàn thành

Đã dựng lại các chuyển đổi claim và bằng chứng quan trọng từ mentor architecture đến S01/S02 hiện có. **Chưa có physical pilot, independently calibrated MP1 forward-validation result hoặc evidence xác lập H1.** Báo cáo phục vụ thảo luận về lịch sử và mức chắc chắn thực tế; không thay scientific state, không sửa prior outputs và không ban hành final novelty verdict.

## 21. Framework trích xuất nghiên cứu từ Evidence JSON (Phần 4 — Phần 11)

Dưới đây là đặc tả chi tiết khung trích xuất nghiên cứu (Research Extraction Framework) từ tài liệu hướng dẫn evidence JSON (`docs/learning/EVIDENCE_JSON_FRAMEWORK_GUIDE_VI.md`), bao gồm các nhóm trường từ Phần 4 đến Phần 11 phục vụ trích xuất có cấu trúc, kiểm tra đối chứng và xây dựng ma trận bằng chứng khoa học cho dự án:

### 4. Thông tin trích xuất — `model` và `usage`

| Trường | Ý nghĩa |
|---|---|
| `model` | Model AI được ghi nhận đã thực hiện trích xuất |
| `usage.prompt_tokens` | Số token đầu vào được báo cáo |
| `usage.completion_tokens` | Số token đầu ra được provider báo cáo |
| `usage.total_tokens` | Tổng token được báo cáo |
| `usage.thinking_tokens` | Token reasoning nếu provider có cung cấp |
| `usage.cache_read_tokens` | Token đầu vào được đọc từ cache |

*Lưu ý phương pháp:* Đây là thông tin vận hành, không phải bằng chứng bài đúng hoặc đề tài mới. Các bộ đếm có thể phụ thuộc provider; không tự cộng lại các trường như thể tất cả đều là các phần độc lập.

### 5. Thông tin thư mục trong `paper`

| Trường | Ý nghĩa | Kiểu dữ liệu quan sát được |
|---|---|---|
| `title` | Tên bài | Chuỗi |
| `authors` | Danh sách tác giả | Danh sách chuỗi |
| `year` | Năm công bố được trích xuất | Chuỗi, ví dụ `"2026"` |
| `doi` | Định danh DOI | Chuỗi |

*Lưu ý phương pháp:* Cần phân biệt online-first và năm issue nếu khác nhau. DOI để trống không đồng nghĩa chắc chắn bài không có DOI. Không dùng năm trong filename thay metadata đã xác minh.

### 6. Bài nghiên cứu vấn đề gì?

| Trường | Ý nghĩa | Câu hỏi giúp trả lời |
|---|---|---|
| `research_problem` | Vấn đề hoặc hạn chế bài muốn xử lý | Vì sao cần nghiên cứu? |
| `research_objective` | Mục tiêu cụ thể của bài | Tác giả định làm gì? |
| `robot_type` | Loại robot hoặc cấu trúc ứng dụng | Hệ được nghiên cứu hoặc ứng dụng vào đâu? |
| `stiffness_mechanism` | Cơ chế tạo hoặc thay đổi độ cứng | Vì sao độ cứng thay đổi? |
| `actuation` | Cách tác động/điều khiển hệ | Hệ được kích hoạt bằng gì? |

*Lưu ý phương pháp:* Ba trường đầu là chuỗi; `stiffness_mechanism` và `actuation` là danh sách trong dữ liệu đã kiểm tra. Cơ chế độ cứng khác cơ cấu tác động. Ví dụ minh họa: khí nén có thể là cách tác động, còn contact–friction là cơ chế khiến độ cứng thay đổi. Không coi hai trường này là từ đồng nghĩa.

### 7. Mô hình và giả thiết

| Trường | Ý nghĩa |
|---|---|
| `modeling_methods` | Danh sách phương pháp mô hình hóa: analytical beam model, FEM, mô hình hiện tượng học… |
| `constitutive_assumptions` | Danh sách giả thiết về ứng xử vật liệu/cơ học được ghi nhận: đàn hồi tuyến tính, luật NiTi, Coulomb friction… |

*Lưu ý phương pháp:* Dữ liệu hiện có đôi khi đưa cả giả thiết hình học hoặc beam theory vào `constitutive_assumptions`. Tên trường không bảo đảm mọi mục đều là giả thiết cấu thành vật liệu theo nghĩa hẹp. Khi phân tích chuyên sâu, phải tách material law, kinematics, contact law và boundary conditions theo nội dung nguồn thực tế.

### 8. Ba nhóm biến cần phân biệt

| Trường | Ý nghĩa | Ví dụ minh họa cho phép thử bó dây |
|---|---|---|
| `independent_variables` | Các biến chủ động thay đổi | Áp suất, mức uốn |
| `dependent_variables` | Các đại lượng đáp ứng được đo/tính | Lực, độ cứng, trượt tương đối |
| `control_variables` | Các yếu tố giữ cố định hoặc kiểm soát để so sánh công bằng | Vật liệu dây, chiều dài mẫu, nhiệt độ, tốc độ tải |

*Lưu ý phương pháp:* Cả ba trường là danh sách. Ví dụ trên chỉ minh họa phân loại, không phải protocol đã được thực hiện. Cùng một đại lượng có thể là independent variable trong nghiên cứu này nhưng là control variable trong nghiên cứu khác.

### 9. Thí nghiệm và kết quả

| Trường | Ý nghĩa |
|---|---|
| `experimental_setup` | Mẫu, apparatus, cảm biến, cách gá và cách tạo tải |
| `performance_metrics` | Tiêu chí dùng đánh giá: độ cứng, sai số dự đoán, năng lượng tiêu tán… |
| `main_results` | Những kết quả chính được trích xuất từ bài |

*Lưu ý phương pháp:* Cả ba trường là danh sách. Phân biệt đo đại lượng gì (`dependent_variables`) với dùng đại lượng nào để đánh giá (`performance_metrics`). Không suy từ một kết quả nằm trong `main_results` rằng nó đã được independent experimental validation: cần kiểm tra kết quả là analytical, numerical, fitted hay measured, và dữ liệu nào đã được dùng để calibration.

### 10. Bằng chứng liên quan — `evidence_relevant_to_topic`

Đây là danh sách các phát biểu được chọn vì liên quan đến câu hỏi nghiên cứu của dự án. Mỗi mục có ba trường con:

| Trường con | Ý nghĩa |
|---|---|
| `claim` | Phát biểu cụ thể được rút từ nguồn |
| `evidence_type` | Loại hỗ trợ cho phát biểu: analytical, numerical, experimental, background hoặc mô tả kết hợp |
| `page_numbers` | Danh sách trang được ghi để truy ngược PDF |

*Lưu ý phương pháp:* Một mục nằm trong trường này chưa chắc là kết quả thực nghiệm trực tiếp. Nó có thể là background mà bài đang dẫn từ nguồn khác. Cần kiểm tra loại bằng chứng và trang nguồn trước khi coi đó là primary evidence. `page_numbers` không mặc nhiên phân biệt printed page và số trang PDF. Nếu chuẩn bị citation chính thức, phải đối chiếu hệ đánh số. Không tự tạo equation/figure/section number khi JSON không lưu.

### 11. Giới hạn, suy luận và hướng tiếp theo

| Trường | Ý nghĩa | Cảnh báo |
|---|---|---|
| `limitations_stated_by_authors` | Giới hạn được ghi là do tác giả trực tiếp nêu | Cần kiểm tra đúng wording và scope trong bài |
| `limitations_inferred` | Giới hạn do người/model phân tích suy ra | Không gán thành kết luận của tác giả |
| `future_work` | Hướng nghiên cứu tiếp theo được trích xuất | Future work năm trước không chứng minh vấn đề vẫn mở hiện nay |
| `possible_gap_implications` | Suy luận về ảnh hưởng của bài đối với gap dự án | Không phải bằng chứng xác nhận novelty |
| `confidence` | Mức tự đánh giá độ tin cậy của bản trích xuất | Không phải confidence đề tài mới; không bảo đảm trích xuất không sai |

*Lưu ý phương pháp:* Bốn trường đầu là danh sách, `confidence` là chuỗi trong dữ liệu đã kiểm tra. Không phải mọi mục trong chúng đều có page locator riêng. Không biến `limitations_inferred` hoặc `possible_gap_implications` thành "khoảng trống đã được chứng minh" khi chưa qua đối chiếu nguồn và adversarial audit.
