# Danh mục bài báo cần đọc cho luận văn — bản hiện hành

> Cập nhật: 21-09-2026 (Asia/Bangkok)  
> Đề tài: **Đánh giá giới hạn hiệu lực của mô hình liên tục cho dầm kẹt lớp chân không bằng mô phỏng toàn lớp và kiểm chứng thực nghiệm**  
> Mô hình rút gọn: **M1 — Zhang et al. (2025), _A continuum-based model for a layer jamming beam_**

## 1. Cách hiểu chữ “tất cả”

Repository hiện có 123 bản ghi: 54 bài discovery và 69 bản ghi verification, trong đó 68 bài verification đã được include và một bản ghi bị loại vì gắn nhầm PDF. Đây là **corpus để audit**, không phải danh sách 123 bài mà người nghiên cứu phải đọc từng dòng.

Danh mục dưới đây là **toàn bộ reading set chủ động ở giai đoạn hiện tại**. Một bài được đưa vào đây khi nó cần cho ít nhất một trong năm nhiệm vụ:

1. tái dựng M1;
2. xây dựng mô hình tham chiếu full-layer R;
3. hiểu cơ chế ma sát, stick–slip và breakdown;
4. bảo vệ ranh giới đóng góp trước prior work gần nhất;
5. thiết kế verification, validation và thí nghiệm.

Danh mục này chưa thể bất biến đến cuối luận văn. Khi solver, formulation tiếp xúc và thiết kế thí nghiệm được khóa, sẽ cần bổ sung một nhóm tài liệu phương pháp chuyên biệt. Điều đó không đồng nghĩa phải mở lại tìm kiếm novelty diện rộng.

## 2. Quy ước mức đọc

| Mức | Yêu cầu |
|---|---|
| **A — đọc sâu** | Đọc đủ nhiều vòng; tự giải thích được giả thiết, phương trình, thuật toán, bằng chứng và giới hạn; có paper card hoặc reconstruction note. |
| **B — đọc có mục tiêu** | Đọc abstract, introduction, mô hình/phương pháp liên quan, các hình/bảng so sánh, limitations và conclusion; chỉ tái dựng các phương trình chuyển giao trực tiếp sang M1 hoặc R. |
| **C — đọc định vị** | Đọc abstract, hình chính và conclusion để biết công trình đã làm gì; quay lại toàn văn khi cần trích dẫn hoặc khi một quyết định thiết kế chạm đúng nội dung của bài. |
| **T — cần audit mới** | Nguồn mới xuất hiện sau D1-V009; phải lấy toàn văn và kiểm tra có thực sự đe dọa câu hỏi validity của M1 hay không trước khi thay đổi trạng thái đề tài. |

## 3. Mức A — tám bài phải đọc sâu

| # | Bài báo | DOI / định danh | Vì sao bắt buộc |
|---:|---|---|---|
| A1 | Zhang et al. (2025), **A continuum-based model for a layer jamming beam** | [10.5194/ms-16-821-2025](https://doi.org/10.5194/ms-16-821-2025); `paper_id 95646b2cfc` | Chính là M1. Phải tái dựng được giả thiết continuum, trường ứng suất, điều kiện Coulomb, ba trạng thái, biên trượt, thuật toán gia tăng và tải–độ võng. **VERIFIED FULL TEXT** |
| A2 | Narang, Vlassak & Howe (2018), **Mechanically Versatile Soft Machines through Laminar Jamming** | [10.1002/adfm.201707136](https://doi.org/10.1002/adfm.201707136); `paper_id 5f7ccd7357` | Nền tảng cơ học laminar jamming: giới hạn stiffness, ma sát, mô hình hai lớp, full-layer/contact FEA và thí nghiệm. **VERIFIED FULL TEXT** |
| A3 | Caruso et al. (2022), **A theoretical model for multi-layer jamming systems** | [10.1016/j.mechmachtheory.2022.104788](https://doi.org/10.1016/j.mechmachtheory.2022.104788) | Tiền thân trực tiếp của Caruso 2023; mô hình số lớp bất kỳ, ba miền biến dạng, ảnh hưởng của số lớp, áp suất và hệ số ma sát. **PUBLISHER ABSTRACT VERIFIED; FULL TEXT CHƯA CÓ TRONG REPOSITORY** |
| A4 | Caruso et al. (2023), **Layer jamming: Modeling and experimental validation** | [10.1016/j.ijmecsci.2023.108325](https://doi.org/10.1016/j.ijmecsci.2023.108325); `paper_id 652e62758f` | Mô hình rời rạc/analytical benchmark gần nhất cho trượt tiến triển, stiffness degradation, FEA, thí nghiệm và hysteresis. Đây là reference phụ của luận văn. **VERIFIED FULL TEXT** |
| A5 | Zhang et al. (2025), **Toward a deeper understanding of layer jamming structures** | [10.1007/s11465-025-0843-5](https://doi.org/10.1007/s11465-025-0843-5); `paper_id 7cb387b88d` | Mở rộng sang biến dạng lớn, dầm thẳng/cong, tải chu kỳ, chiều dày lớp, áp suất và thuật toán gia tăng; chỉ ra nhiều cơ chế có thể làm M1 sai. **VERIFIED FULL TEXT** |
| A6 | Zhang et al. (online 2025; issue 2026), **Continuum modeling for layer jamming structures** | [10.1016/j.taml.2025.100633](https://doi.org/10.1016/j.taml.2025.100633); `paper_id a792efc445` | Mô hình continuum cấu thành/RVE M2; phải hiểu để phân biệt beam-level M1 với constitutive-level M2 và tránh claim continuum là mới. **VERIFIED FULL TEXT** |
| A7 | Wang et al. (2026), **The global-local mechanical behaviors of multilayered structure and applications to superconducting coils** | [10.1016/j.ijsolstr.2025.113689](https://doi.org/10.1016/j.ijsolstr.2025.113689); `paper_id ca46dc062d` | Prior work tổng quát đe dọa mạnh nhất: continuum multilayer, Coulomb contact, discrete-contact comparator, sweep số lớp/biến dạng, error mapping, ngưỡng applicability và thí nghiệm. **VERIFIED FULL TEXT** |
| A8 | Adhikary, Mühlhaus & Dyskin (1999), **Modelling the large deformations in stratified media—the Cosserat continuum approach** | `paper_id d75a3e82bc` | Chứng minh continuum/Cosserat, layer-bending, large deformation, frictional/plastic slip, opening/delamination và FE implementation đều không phải đóng góp mới. **VERIFIED FULL TEXT** |

### Đầu ra bắt buộc sau mức A

Sau tám bài này, người nghiên cứu phải tự vẽ được hai chuỗi:

```text
Narang → Caruso → Zhang M1 → câu hỏi validity của luận văn
```

và

```text
layered/partial-interaction mechanics → Cosserat/homogenization
→ Wang 2026 → phần novelty còn sống của luận văn
```

## 4. Mức B — mười ba bài đọc có mục tiêu

| # | Bài báo | Trọng tâm cần đọc | Trạng thái |
|---:|---|---|---|
| B1 | Caruso, Mantriota & Reina (2022), **An Analytical Model for Cantilever Layer-Jamming Structures** — [10.1007/978-3-031-10776-4_23](https://doi.org/10.1007/978-3-031-10776-4_23) | Công thức cho dầm công-xôn và cầu nối từ mô hình Caruso sang cấu hình M1. | **METADATA/REFERENCE VERIFIED; CẦN LẤY FULL TEXT** |
| B2 | Schnabl et al. (2007), **Analytical Solution of Two-Layer Beam Taking into Account Interlayer Slip and Shear Deformation** — [10.1061/(ASCE)0733-9445(2007)133:6(886)](https://doi.org/10.1061/(ASCE)0733-9445(2007)133:6(886)) | Nền beam theory có interlayer slip mà Zhang trích dẫn; đọc kinematics, assumptions và cách slip đi vào phương trình dầm. | **VERIFIED FULL TEXT**, `f5bba53ef2` |
| B3 | Steif & Trojnacki (1993), **Bending Stress Enhancement in Materials with Limited Shear Resistance—Part I: Slipping-Layers Model** | Discrete-to-continuum limit, sai số hữu hạn số lớp và phụ thuộc trạng thái tải. | **VERIFIED FULL TEXT**, `66fcf766cb` |
| B4 | Steif & Trojnacki (1993), **…Part II: Unlayered Shear-Weak Model** | Continuum thay các interface bằng miền shear-weak/plastic; so sánh với Part I. | **VERIFIED FULL TEXT**, `f00d886124` |
| B5 | Massabò & Campi (2014), **Assessment and correction of theories for multilayered plates with imperfect interfaces** — [10.1007/s11012-014-9994-x](https://doi.org/10.1007/s11012-014-9994-x) | Cách đánh giá và sửa reduced theory khi interface không hoàn hảo; boundary effects. | **VERIFIED FULL TEXT**, `33ea203427` |
| B6 | Darban & Massabò (2018), **A homogenized structural model for shear deformable composites with compliant interlayers** — [10.1007/s41939-018-0032-x](https://doi.org/10.1007/s41939-018-0032-x) | Homogenization của multilayer có compliant interfaces và giới hạn chuyển giao sang layer jamming. | **VERIFIED FULL TEXT**, `8113666e96` |
| B7 | Faella, Martinelli & Nigro (2002), **Steel and concrete composite beams with flexible shear connection: “exact” analytical expression of the stiffness matrix and applications** | Interaction parameter và applicability boundary; phân biệt model-validity rule với tolerance được định trước. | **VERIFIED FULL TEXT**, `d0699583ac` |
| B8 | Sonoda et al. (2013), **Analysis of Composite Beams with Incomplete Interaction I** | Sweep số connector hữu hạn, discrete reference và quy tắc xấp xỉ complete interaction. | **VERIFIED FULL TEXT**, `f8e8c7b1a4` |
| B9 | Ye et al. (2024), **Analytical Solution for Bending Deformation of Steel–Concrete Composite Beams Considering Nonlinear Interfacial Slip** — [10.1061/JSENDH.STENG-13096](https://doi.org/10.1061/JSENDH.STENG-13096) | Closed-form nonlinear slip, thí nghiệm, FE và applicability statement; dùng để học cấu trúc một study về giới hạn mô hình, không chuyển thẳng connector law sang ma sát chân không. | **VERIFIED FULL TEXT**, `53d328abaa` |
| B10 | Wang & Yue (2021), **A full layered numerical model for predicting hysteretic behavior of unbonded flexible pipes considering initial contact pressure** — [10.1016/j.apor.2021.102626](https://doi.org/10.1016/j.apor.2021.102626) | Kiến trúc full-layer contact, initial pressure, stick–transition–slip và hysteresis. | **VERIFIED FULL TEXT**, `afe2a3a310` |
| B11 | Wang, Ye & Yue (2022), **A novel helix contact model for predicting hysteretic behavior of unbonded flexible pipes** — [10.1016/j.oceaneng.2022.112407](https://doi.org/10.1016/j.oceaneng.2022.112407) | Reduced-versus-full-layer comparison và lỗi do giả định contact pressure không đổi. | **VERIFIED FULL TEXT**, `a300a3b714` |
| B12 | Messina & Miranda (2024), **A novel friction model for steel–polymer interfaces in sliding seismic isolation bearings** — [10.1002/eqe.4128](https://doi.org/10.1002/eqe.4128) | Friction law của interface steel–polymer, dependence on pressure/velocity; chỉ dùng nếu vật liệu và dữ liệu ma sát khiến Coulomb hằng số không đủ. | **VERIFIED FULL TEXT**, `13e407003a` |
| B13 | Caro & Carmichael (2024), **A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics** — [10.3390/act13020064](https://doi.org/10.3390/act13020064) | Từ vựng, taxonomy, lịch sử và bibliography; không dùng review để thay thế bằng chứng cơ học từ bài gốc. | **VERIFIED FULL TEXT**, `f5f31ef249` |

## 5. Mức C — năm bài đọc định vị

| # | Bài báo | Chỉ cần nắm điều gì? | Trạng thái |
|---:|---|---|---|
| C1 | Atakuru et al. (2024), **Layer Jamming of Magnetorheological Elastomers for Variable Stiffness in Soft Robots** — [10.1007/s11340-024-01031-7](https://doi.org/10.1007/s11340-024-01031-7) | Ba trạng thái slip và full-layer/contact FEA trong một cơ chế tạo lực ép khác; giúp phân biệt mechanics chung với vacuum-specific mechanics. | **VERIFIED FULL TEXT**, `56d058a34a` |
| C2 | Zhang et al. (2025), **Analysis and modeling of nonlinear saturated behavior of layer jamming soft pneumatic bending actuator** — [10.1088/1361-665X/adbf56](https://doi.org/10.1088/1361-665X/adbf56) | Nonlinearity, hysteresis và model error ở actuator tích hợp; không phải comparator trực tiếp cho dầm M1. | **VERIFIED FULL TEXT**, `1337634c62` |
| C3 | Fan, Yi & Liu (2026), **Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots** — [10.1109/TCST.2026.3690756](https://doi.org/10.1109/TCST.2026.3690756) | Robot-level dynamic/control abstraction và pressure–stiffness validation; không có discrete interlayer validity map. | **VERIFIED FULL TEXT**, `1f05cf83bc` |
| C4 | Newmark et al. (1951), **Test and analysis of composite beams with incomplete interaction** | Nguồn lịch sử của partial-interaction beam theory; đọc để định vị lineage, không cần tái dựng toàn bộ trước Gate R. | **REFERENCE VERIFIED; FULL TEXT CHƯA CÓ TRONG REPOSITORY** |
| C5 | Ibrahimi et al. (2021), **A Layer Jamming Actuator for Tunable Stiffness and Shape-Changing Devices** — [10.1089/soro.2019.0182](https://doi.org/10.1089/soro.2019.0182) | Cấu tạo, khả năng điều chỉnh stiffness/shape và thực nghiệm thiết bị; hữu ích cho Introduction và thiết kế mẫu, không phải core mechanics reference. | **REFERENCE VERIFIED; CẦN KIỂM TRA FULL TEXT KHI DÙNG** |

## 6. Mức T — hai nguồn mới phải audit trước khi coi novelty đã đóng hoàn toàn

Hai bài này được phát hiện ngày 21-09-2026, sau D1-V009. Chúng **không tự động bác bỏ đề tài**, nhưng là các nguồn cụ thể đủ gần để cần kiểm tra có mục tiêu.

| # | Bài báo | Vì sao phải kiểm tra | Trạng thái hiện tại |
|---:|---|---|---|
| T1 | Yang, Guo & Wang (2025), **Behavior of layer jamming plate with tunable stiffness and its near wake structure in cross flow** — [10.1038/s41598-025-22364-w](https://doi.org/10.1038/s41598-025-22364-w) | Thí nghiệm ba điểm quét `n = 2, 4, 8, 12` và `p = 0–80 kPa`, có ba trạng thái slip và simplified stiffness model. Cần kiểm tra liệu dữ liệu này có thể trở thành validation dataset độc lập hoặc đã chứa một phần validity boundary hay chưa. | **EXTERNAL FULL TEXT VERIFIED; CHƯA INGEST/AUDIT TRONG REPOSITORY** |
| T2 | Wang et al. (2026), **Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction** — [10.1016/j.matdes.2026.116573](https://doi.org/10.1016/j.matdes.2026.116573) | Quét vacuum pressure, layer configurations và loading; có cyclic tests, energy dissipation và simplified analytical model. Cần xác định có so sánh model-form error/giới hạn áp dụng của beam model hay chỉ giải thích thiết bị composite. | **PUBLISHER METADATA + ABSTRACT VERIFIED; FULL-TEXT AUDIT CHƯA THỰC HIỆN** |

## 7. Nguồn phương pháp bắt buộc nhưng không phải “paper cơ học layer jamming”

Các nguồn này nên đọc khi bắt đầu khóa R, error metrics và validation protocol:

| Nguồn | Vai trò |
|---|---|
| **ASME V&V 10-2019 (R2025), Standard for Verification and Validation in Computational Solid Mechanics** | Phân biệt code verification, solution verification, validation, uncertainty và credibility của mô hình solid mechanics. |
| **ASME V&V 10.1-2012, An Illustration of the Concepts of Verification and Validation in Computational Solid Mechanics** | Ví dụ áp dụng các khái niệm V&V; hữu ích khi viết protocol cho R. |
| Oberkampf & Roy (2010), **Verification and Validation in Scientific Computing** | Nền phương pháp cho model-form error, uncertainty, calibration/validation separation và cách không gọi mô phỏng là “truth”. |

Các nguồn cụ thể về mesh convergence, contact algorithm, DIC/optical measurement và uncertainty của load cell sẽ chỉ được chốt sau khi phần mềm FE và thiết kế thí nghiệm được chọn.

## 8. Thứ tự đọc thực tế

Không đọc hết A rồi mới bắt đầu nghiên cứu. Thứ tự hiệu quả là:

```text
Giai đoạn 1 — dựng backbone
A1 Zhang M1
→ A2 Narang 2018
→ A3 Caruso 2022
→ A4 Caruso 2023

Giai đoạn 2 — hiểu họ Zhang và các failure mode
A5 Zhang deeper understanding
→ A6 Zhang RVE/M2
→ C2 Zhang pneumatic actuator

Giai đoạn 3 — tấn công novelty và validity logic
A7 Wang 2026
→ A8 Adhikary 1999
→ B3–B9 theo đúng câu hỏi đang gặp

Giai đoạn 4 — khóa full-layer R
B10–B12
→ Narang/Caruso FEA sections quay lại lần hai
→ ASME V&V 10/10.1

Giai đoạn 5 — thiết kế experiment và viết Introduction
C1, C3, C5
→ T1, T2 sau khi audit
→ các bài mức C khác khi cần trích dẫn
```

## 9. Những bài không cần đọc toàn văn ngay

### 9.1 Phần còn lại của 68 bài verification đã include

Chúng đã phục vụ falsification audit nhưng phần lớn là adjacent mechanics hoặc ứng dụng robot. Không cần đọc lại từng bài từ đầu. Tra theo vòng audit khi một claim cụ thể xuất hiện:

| Nhánh | Nguồn điều hướng |
|---|---|
| Layer-jamming trực tiếp và continuum robots | `outputs/verification/D1-V001/` đến `D1-V003/` |
| Frictional multilayer/homogenization | `outputs/verification/D1-V004/` |
| Partial-interaction composite beams | `outputs/verification/D1-V005/` |
| Imperfect interface/contact/friction | `outputs/verification/D1-V006/` |
| Forward-citation closure | `outputs/verification/D1-V007/` |
| Ye 2024 final named target | `outputs/verification/D1-V008/` |
| Adhikary 1999 late-found audit | `outputs/verification/D1-V009/` |

### 9.2 54 bài discovery

54 bài discovery chủ yếu giúp chọn domain ban đầu và chứa nhiều công trình về soft grippers, SMA, particle jamming, sensors và ứng dụng không còn trực tiếp chi phối câu hỏi M1–R–E. Chỉ quay lại chúng để:

- viết bối cảnh rộng của soft robotics/variable stiffness;
- truy vết một claim đã sinh ra D1;
- lấy một thiết kế thí nghiệm hoặc cấu tạo vật lý cụ thể;
- trả lời một phản biện có tên bài/claim rõ ràng.

Không dùng việc “đã có trong 54-paper corpus” như bằng chứng rằng một bài là bắt buộc hoặc một novelty gap đã được kiểm chứng.

## 10. Danh sách hành động ngay lúc này

1. Hoàn thành paper card và reconstruction record cho A1.
2. Đọc A2–A4 để đối chiếu M1 với discrete/full-layer lineage.
3. Lấy toàn văn A3 và B1; hiện repository mới có metadata/reference cho hai bài này.
4. Ingest và audit T1; ưu tiên vì nó quét trực tiếp số lớp và áp suất trên mẫu vacuum layer-jamming.
5. Lấy toàn văn và screen T2; chỉ nâng thành mức A/B nếu nó thực sự chứa comparison hoặc validity result chuyển giao được sang M1.
6. Chỉ sau đó khóa formulation của R và bổ sung literature chuyên về phần mềm/contact/experimental uncertainty.

## 11. Provenance

Danh mục được tổng hợp từ:

- `docs/project/PROJECT_HANDOFF_CURRENT.md`;
- `docs/project/POST_D1_V009_RESEARCH_ROADMAP_VI.md`;
- `docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md`;
- `docs/learning/ZHANG_CONTINUUM_PAPERS_READING_GUIDE_VI.md`;
- `outputs/verification/D1-V001/` đến `D1-V009/`;
- các evidence JSON tương ứng trong `data/evidence/`;
- publisher pages cho Caruso 2022, Yang et al. 2025, Wang et al. 2026 và ASME V&V 10.

Mọi thay đổi mức đọc phải dựa trên một quyết định nghiên cứu cụ thể; không tăng mức chỉ vì bài mới hoặc có nhiều trích dẫn.
