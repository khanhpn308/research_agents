# D1: Lịch sử quyết định và bằng chứng dẫn tới đề tài M1

Ngày dựng lại: 26-09-2026. Repository HEAD: `02ce5251df0a29247f3dba677a634f18ff754436`.

## 1. Mục đích và giới hạn của báo cáo

Báo cáo giải thích con đường từ tập 54 bài ban đầu, qua các lần bác bỏ và thu hẹp D1, đến tên đề tài hiện tại. Mục đích là giúp người nghiên cứu trình bày với người hướng dẫn: **ban đầu định làm gì, tài liệu nào khiến phải thay đổi, điều gì đã có người làm, và phần nào vẫn chỉ là ứng viên đóng góp cần kiểm chứng**.

Đây là tái dựng lịch sử từ hồ sơ hiện có, không phải một vòng tìm kiếm mới, một phán quyết novelty mới, hay báo cáo kết quả thực nghiệm của đề tài. Không thay đổi registry, scientific state hoặc các vòng kiểm chứng đã hoàn thành.

Quy ước bằng chứng:

- **[HỒ SƠ QUYẾT ĐỊNH]**: điều được ghi trong verdict, log hoặc tài liệu thiết kế. Chứng minh dự án đã ra quyết định đó; không tự chứng minh quyết định đúng về khoa học.
- **[VERIFIED FULL TEXT]**: nội dung được hỗ trợ bởi evidence JSON/full-text audit có truy nguyên tới bài gốc.
- **[METADATA ONLY]**: mới có thông tin thư mục/abstract; không đủ kết luận chi tiết cơ học.
- **[INFERENCE]**: diễn giải hoặc hệ quả do người phân tích rút ra, không phải kết luận nguyên văn của tác giả.
- **[HYPOTHESIS]**: câu hỏi hoặc đóng góp dự kiến chưa được chứng minh.

Ngày trong tên run là mốc thực thi có chứng cứ, không mặc nhiên là ngày người hướng dẫn chấp thuận. Những chỗ chưa tìm được ngày quyết định chính xác được ghi theo pha, không dựng thêm ngày.

## 2. Kết luận ngắn để định vị toàn bộ lịch sử

Không phải dự án tìm thấy 54 bài rồi suy ra ngay một đề tài mới. Tập 54 bài tạo ra **năm hướng ứng viên**. D1 được chọn có sửa đổi, sau đó literature verification làm mất cơ sở của claim rộng về xây dựng mô hình slip–stiffness mới. Các vòng tiếp theo tiếp tục loại bỏ claim “mô hình continuum”, “mô hình nhiều lớp”, “so sánh với FEM/thực nghiệm”, và cả claim rộng “dùng sai số để xác định miền áp dụng”.

Hướng hiện tại vì vậy chuyển từ **đề xuất một mô hình cơ học mới** sang **đánh giá có kiểm soát giới hạn dự đoán của một mô hình đã được chỉ định**. Nhưng chuyển cách đặt câu hỏi không tự tạo ra novelty. Chính các nghiên cứu continuum–contact–error trong cơ học lân cận vẫn có thể bác bỏ hoặc làm đóng góp trở thành một ứng dụng thường quy.

Tên hiện tại trong quyết định lựa chọn lịch sử:

> **Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams**
>
> **Đánh giá thực nghiệm giới hạn hiệu lực và sự mất hiệu lực của mô hình liên tục cho dầm kẹt lớp chân không.**

Trạng thái lựa chọn: `D1_M1`, `LOCK_WITH_FEASIBILITY_GATE`, confidence `medium`. Đây là **khóa có điều kiện**, không phải xác nhận novelty cuối cùng hay xác nhận đã làm được thí nghiệm. Nguồn: [quyết định lựa chọn](../../outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json).

## 3. Từ 54 bài: đã sinh ra những hướng nào?

[HỒ SƠ QUYẾT ĐỊNH] Snapshot discovery gồm ma trận 54 seed papers, các bước tổng hợp theo batch, candidate directions, critique và adjudication. Đây là corpus khám phá; không đại diện cho toàn bộ prior art.

| Hướng | Tên tiếng Anh trong candidate file | Câu hỏi trọng tâm lúc đề xuất | Xử lý ở discovery |
|---|---|---|---|
| D1 | Modeling and Experimental Characterization of Friction, Warping, and Cyclic Stiffness Degradation in Vacuum Layer-Jamming Structures | Ma sát, vênh và suy giảm độ cứng theo chu kỳ trong vacuum layer jamming | Critique yêu cầu sửa; adjudication chọn D1 sau khi thu hẹp |
| D2 | Predictive Mechanics and Experimental Validation of Positive-Pressure Layer Jamming Under Flexural Loading | Dự đoán đáp ứng uốn khi lực ép lớp đến từ áp suất dương | Critique yêu cầu sửa; không được chọn trong adjudication này |
| D3 | Coupled Thermomechanical Modeling and Experimental Investigation of Forced Cooling in a Phase-Change Variable-Stiffness Soft Finger | Liên hệ truyền nhiệt, làm nguội và đáp ứng cơ học | Critique loại trong đợt lựa chọn này |
| D4 | Investigation of Membrane–Granulate Interaction and Surface-Friction Scaling in Vacuum Jamming Grippers | Tương tác màng–hạt và ma sát khi kẹp | Critique loại trong đợt lựa chọn này |
| D5 | Higher-Order Shear-Deformation Modeling and Experimental Validation of Ribbed Fluidic Prestressed Composite Actuators | Mô hình biến dạng cắt bậc cao cho actuator composite có gân | Critique loại trong đợt lựa chọn này |

“Không chọn” ở discovery không đồng nghĩa mọi câu hỏi của hướng đó đã được literature falsify. Bảng chỉ ghi quá trình lựa chọn nội bộ, không so sánh giá trị đề tài hiện tại với các hướng khác.

Nguồn: [ma trận 54 bài](../../outputs/discovery_snapshot/literature_matrix_54papers.json), [năm ứng viên](../../outputs/discovery_snapshot/candidate_directions.json), [critique](../../outputs/discovery_snapshot/direction_critique.json), [adjudication discovery](../../outputs/discovery_snapshot/final_adjudication.json).

## 4. D1 ban đầu đã thay đổi ngay trước verification

### 4.1 Claim ban đầu

D1 ban đầu là một giả thuyết cơ học về ma sát–vênh–suy giảm độ cứng theo chu kỳ. Không nên kể lại nó chỉ là “làm một cấu trúc layer jamming mới”: như vậy sẽ làm mất nội dung của candidate gốc.

Critique nhận ra rủi ro phạm vi quá rộng và khả năng không tách được các nguyên nhân: thay đổi ma sát, biến dạng vênh, relaxation, leakage hoặc ảnh hưởng màng. Đây là **đánh giá của critic**, không phải bằng chứng thực nghiệm rằng một cơ chế chắc chắn không xảy ra.

### 4.2 D1 sau adjudication discovery

Tên được sửa thành:

> Modeling and Experimental Characterization of Interlayer Slip and Bending Stiffness in Vacuum Layer-Jamming Beams.

Claim chuyển sang mô hình hóa interlayer slip và bending stiffness, giảm gánh nặng phải giải đồng thời wear/fatigue/warping. Verdict: `select_with_revision`, confidence `medium`.

**Ý nghĩa:** đây mới là quyết định “đáng đem đi kiểm chứng”, không phải “đã mới”. Chính mô hình slip–stiffness này trở thành mục tiêu bị prior art tấn công ở D1-V001.

## 5. D1-V001: vì sao phải PIVOT?

[HỒ SƠ QUYẾT ĐỊNH] Matrix có ba bài. Verdict `PIVOT`, confidence `high`: [verdict V001](../../outputs/verification/D1-V001/direction_verification.json), [matrix V001](../../outputs/verification/D1-V001/verification_matrix.json).

| Bài | Bằng chứng cơ học liên quan | Điều làm suy yếu D1 | Không được suy thêm |
|---|---|---|---|
| Narang, Vlassak & Howe (2018), *Mechanically Versatile Soft Machines through Laminar Jamming*, DOI `10.1002/adfm.201707136`, `5f7ccd7357` | [VERIFIED FULL TEXT] Mô hình analytical hai lớp, FEA nhiều lớp có contact/friction, các chế độ pre-slip, transition và full-slip; đối chiếu force–deflection với thực nghiệm, tr. 2–5 theo evidence | Slip, ma sát, áp suất, stiffness và experimental validation không phải một tổ hợp chưa ai mô hình hóa | Future work của năm 2018 không chứng minh câu hỏi đó còn mở ở năm 2026 |
| Caruso et al. (2023), *Layer jamming: Modeling and experimental validation*, DOI `10.1016/j.ijmecsci.2023.108325`, `652e62758f` | [VERIFIED FULL TEXT] Mô hình analytical nhiều lớp, tiến triển slip qua các pha, ảnh hưởng đoạn overhang ngoài gối trong three-point bending, kiểm tra thực nghiệm | Đề xuất chung “mô hình interlayer slip và độ cứng uốn rồi kiểm chứng” bị prior art rất gần bao phủ | Không chứng minh mọi hình học, boundary condition và mô hình continuum đều đã được kiểm tra đầy đủ |
| Atakuru et al. (2024), *Layer Jamming of Magnetorheological Elastomers for Variable Stiffness in Soft Robots*, `56d058a34a` | Evidence đã có trong matrix; mở rộng bối cảnh điều khiển stiffness bằng layer jamming với vật liệu/kích hoạt khác | Củng cố việc không lấy biến thể vật liệu/actuation làm novelty tự thân | Không phải nguồn chính chứng minh miền validity của vacuum continuum beam |

Điều bị bác bỏ là **cơ sở novelty của claim rộng về mô hình slip–bending stiffness**. Không phải kết luận “mọi nghiên cứu layer jamming đã hết”, cũng không phải chứng minh thí nghiệm dự kiến vô giá trị.

Pivot đề xuất lúc đó:

> P1 — Validity Limits of a Homogenized Slip Model for High-Layer-Count Vacuum-Jammed Beams.

[HYPOTHESIS] P1 chuyển quan tâm sang giới hạn của biểu diễn liên tục khi số lớp lớn. Cách gọi “homogenized” và gợi ý “single-slip-system” ở giai đoạn sớm chưa phải lựa chọn mô hình đã được xác lập.

## 6. D1-V002: ba bài Zhang khiến claim continuum phải thay đổi

Matrix V002 có bốn bài; [synthesis V002](../../outputs/verification/D1-V002/adversarial_evidence_synthesis.md) dùng kết luận văn bản `SURVIVES BUT MUST BE NARROWED`. Không trình bày nó như một canonical JSON adjudication nếu không có file tương ứng.

Ba nguồn Zhang phải được phân biệt:

| Nguồn | DOI / paper_id | Nội dung làm thay đổi cách đặt vấn đề |
|---|---|---|
| *A continuum-based model for a layer jamming beam* | `10.5194/ms-16-821-2025` / `95646b2cfc` | [VERIFIED FULL TEXT] Có sẵn continuum beam model với vùng jam/slip và biến dạng; đây là M1 được chỉ định về sau |
| *Toward a deeper understanding of layer jamming structures* | `10.1007/s11465-025-0843-5` / `7cb387b88d` | [VERIFIED FULL TEXT] Nghiên cứu cơ học, pressure, độ dày/số lớp, curvature, slip và đối chiếu thực nghiệm; không thể giữ claim chung “các yếu tố này chưa được nghiên cứu” |
| *Continuum modeling for layer jamming structures* | `10.1016/j.taml.2025.100633` / `a792efc445` | [VERIFIED FULL TEXT] Mô hình constitutive theo RVE và averaging; M2 trong tài liệu so sánh lựa chọn mô hình. Cần phân biệt online 2025 với issue 2026 |

Bài thứ tư trong matrix là nguồn Khaloujini, `1337634c62`, DOI `10.1088/1361-665X/adbf56`; phải giữ trong phạm vi corpus, không kể V002 chỉ có ba bài.

**Kết quả logic:** không thể xem “xây dựng continuum/homogenized model cho layer jamming” là phần còn mới. Câu hỏi phải chuyển sang **một mô hình cụ thể dự đoán được tới đâu**.

M1 là một mô hình continuum ở cấp beam với biểu diễn trường và vùng slip; không nên tự gán cho nó một formal homogenization như M2. Sự khác nhau này được ghi trong [EXACT_MODEL_SELECTION](../research_design/EXACT_MODEL_SELECTION.md). Tài liệu lựa chọn đó tự ghi là so sánh; việc M1 đã được khóa phải truy sang architecture, không gán ngược thời điểm khóa cho V002.

## 7. D1-V003: từ “có mô hình” sang “miền hiệu lực của mô hình nào?”

V003 có chín paper entries. [Cross-round synthesis](../../outputs/verification/D1-V003/cross_round_adversarial_synthesis.json) ghi `SURVIVES_WITH_REVISED_SCOPE`, confidence `medium`; phạm vi adjacent mechanics lúc đó chưa đủ để coi là kết luận cuối.

[VERIFIED FULL TEXT] Fan, Yi & Liu (2026), *Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots*, DOI `10.1109/TCST.2026.3690756`, `1f05cf83bc`, là một nguồn quan trọng về mô hình robot/control. Sự tồn tại mô hình động lực học và experimental agreement không tự tương đương với việc xác lập miền sai số của một mechanics-level continuum model đối với explicit interfaces.

[INFERENCE từ audit] Fan không đóng câu hỏi hẹp đó; tuy nhiên không được diễn giải thành “Fan không liên quan”. Mô hình reduced và đối chiếu thí nghiệm đã có, nên cần nói rõ **đầu ra, fidelity và mục tiêu kiểm tra**.

Bài *Toward a deeper understanding…* tiếp tục thu hẹp mạnh: pressure, số/độ dày lớp, curvature, progressive/full slip, cyclic response và discrepancy không thể liệt kê như các biến chưa được prior art chạm tới. Cái còn cần kiểm tra là **một boundary định lượng, đối với model và output xác định**, không phải chỉ thêm một parameter sweep.

## 8. D1-V004–V006: prior art ngoài layer jamming tấn công vào phần còn lại

### 8.1 V004 / C01 — continuum và interlayer mechanics không bắt đầu từ robotics

15 paper entries; verdict `SUBSTANTIALLY_NARROWED`, confidence `high`. Nguồn: [C01 audit](../../outputs/verification/D1-V004/C01_ADVERSARIAL_AUDIT.json).

[VERIFIED FULL TEXT] Steif & Trojnacki (1993), Part I *Slipping-Layers Model* (`66fcf766cb`) và Part II *Unlayered Shear-Weak Model* (`f00d886124`), cùng các nguồn relative-gradient/imperfect-interface sau đó, đặt trực tiếp vấn đề biểu diễn layer/slip và continuum/shear-weak response. Các nguồn Massabò & Campi (2014, `33ea203427`) và Darban & Massabò (2018, `8113666e96`) củng cố prior art về hiệu chỉnh/đánh giá mô hình layered structures.

**Claim phải bỏ:** “chuyển từ discrete layers sang continuum rồi so sánh là một ý tưởng khoa học mới tự thân”. Không được gạt cả corpus này đi bằng nhận xét “chỉ có bonded interfaces”: C01 có các nguồn friction/slip, cần xét từng bài.

### 8.2 V005 / C02 — partial interaction đã có tiêu chí định lượng

16 entries; `SUBSTANTIALLY_NARROWED`, confidence `high`. Nguồn: [C02 audit](../../outputs/verification/D1-V005/C02_ADVERSARIAL_AUDIT.json).

[VERIFIED FULL TEXT] Faella, Martinelli & Nigro (2002), *Steel and concrete composite beams with flexible shear connection: “exact” analytical expression of the stiffness matrix and applications* (`d0699583ac`), dùng tham số interaction và đánh giá ảnh hưởng của xấp xỉ đến đáp ứng. Các nguồn trong C02 còn có multilayer/N-layer theory và nghiên cứu mức rời rạc của connectors.

**Claim phải bỏ:** “chưa ai dùng tham số liên kết hoặc sai số để bàn khi nào beam approximation còn dùng được”. Không được mô tả toàn bộ partial-interaction literature chỉ là hai lớp; cũng không biến mesh-convergence error thành model-acceptance criterion.

### 8.3 V006 / C03 — mối đe dọa rất gần: Wang et al. 2026, IJSS

16 entries; `SUBSTANTIALLY_NARROWED`, confidence `high`. Nguồn: [C03 audit](../../outputs/verification/D1-V006/C03_ADVERSARIAL_AUDIT.json).

[VERIFIED FULL TEXT] Sijian Wang, Yuchen Han, Huadong Yong & Youhe Zhou, *The global-local mechanical behaviors of multilayered structure and applications to superconducting coils*, DOI `10.1016/j.ijsolstr.2025.113689`, `ca46dc062d`:

- Đưa contact/friction/slip vào continuum formulation và so sánh với discrete contact model.
- Xét sai số theo layer count và rotation; áp dụng ngưỡng sai số displacement 5% để xác định rotation cho phép (evidence tr. 9–10).
- Có đối chiếu dữ liệu thực nghiệm uốn ba điểm của các stack 35, 50 và 70 lớp (evidence tr. 10–11); dữ liệu này được lấy từ nghiên cứu được bài trích dẫn, không mặc nhiên là thí nghiệm mới của nhóm tác giả.

**Không được nói bài này “không có experimental validation”.** Điểm cần phân biệt là experimental comparison đã có, còn một chiến dịch thí nghiệm độc lập để kiểm tra trực tiếp boundary được dự đoán có được chứng minh hay không.

**Hệ quả lớn nhất:** ngay cả “continuum + explicit-contact reference + sai số theo tham số + một ngưỡng áp dụng” cũng không còn là claim chung an toàn. Muốn giữ D1, phải kiểm tra xem câu hỏi riêng của M1 có tạo ra kết quả cơ học thực chất hay chỉ tái áp dụng phương pháp đã biết.

## 9. D1-V007–V009: sửa nghĩa của threshold và xử lý các đe dọa còn sót

| Vòng | Nguồn/điểm kiểm tra | Verdict ghi trong hồ sơ | Ý nghĩa đúng phạm vi |
|---|---|---|---|
| V007 / C04 | Ba forward-citation entries và việc phân biệt adopted threshold với predeclared threshold | `INCONCLUSIVE_MISSING_TARGET` | Nhánh đã kiểm tra không đủ đóng một named target chưa có full text |
| V008 | Ye et al. (2024), *Analytical Solution for Bending Deformation of Steel–Concrete Composite Beams Considering Nonlinear Interfacial Slip*, DOI `10.1061/JSENDH.STENG-13096`, `53d328abaa` | `SURVIVES_FINAL_TARGET` | Full text của named target không đóng toàn bộ câu hỏi đã thu hẹp; không có nghĩa mọi prior art trên thế giới đã được loại trừ |
| V009 | Adhikary, Mühlhaus & Dyskin (1999), *Modelling the large deformations in stratified media—the Cosserat continuum approach*, `d75a3e82bc` | `SURVIVES_LATE_FOUND_TARGET` | Cosserat/slip/opening/large-deformation mechanics đã có; audit không tìm thấy toàn bộ phép kiểm tra boundary đang xét trong nguồn này |

Nguồn: [C04 audit](../../outputs/verification/D1-V007/C04_ADVERSARIAL_AUDIT.json), [semantic correction](../../outputs/verification/D1-V007/C04_SEMANTIC_CORRECTION.md), [V008](../../outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json), [V009](../../outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.json).

**Sửa nghĩa quan trọng:** bài dùng ngưỡng 5% không tự chứng minh ngưỡng được predeclare trước khi nhìn kết quả. Nhưng không xác minh được thời điểm predeclare cũng **không chứng minh tác giả chọn ngưỡng post hoc**. D1 không được dùng việc prior paper thiếu một chi tiết quy trình để phủ nhận toàn bộ phần cơ học đã có.

[VERIFIED FULL TEXT] Ye có analytical nonlinear interfacial slip, numerical/experimental comparison và giới hạn applicability gắn với giả thiết beam. Các tỷ lệ sai số quan sát được không tự là tiêu chí acceptance đã định trước. Adhikary có continuum tổng quát hóa và mô hình hóa slip/opening; numerical verification/mesh checks không tự tương đương với independent physical validation của một validity boundary.

Các run kiểm chứng cho thấy thứ tự: V003–V005 ngày 17-09 UTC, V006–V008 ngày 18-09 UTC, V009 ngày 20-09 UTC. Đây là mốc trong run provenance, không phải lịch phê duyệt của người hướng dẫn.

## 10. Vì sao chọn M1 và chuyển sang M → R → E?

[HỒ SƠ QUYẾT ĐỊNH] [Architecture tiếng Việt](../research_design/M1_RESEARCH_ARCHITECTURE_VI.md) và [architecture tiếng Anh](../research_design/M1_RESEARCH_ARCHITECTURE.md) xác định M1 là bài Zhang, DOI `10.5194/ms-16-821-2025`. Không phải mọi bài Zhang đều là M1.

| Thành phần | Vai trò | Điều không được đánh đồng |
|---|---|---|
| M | Chính mô hình continuum beam M1 đã công bố, tái lập có version và kiểm tra source-to-code | Không âm thầm cải tiến M rồi gọi đó là đánh giá M1 gốc |
| R | Numerical reference phân giải từng lớp và contact/friction interfaces | Higher fidelity không có nghĩa ground truth; phải kiểm tra convergence, contact, loading và uncertainty |
| E | Thí nghiệm vật lý độc lập, geometry/material/pressure/loading đủ tương thích | Không dùng chính đường cong kiểm tra cuối để fit M hoặc R rồi coi là independent validation |

[INFERENCE] Chỉ định một model làm đối tượng cho phép hỏi chính xác “giả thiết nào của model này tạo ra sai số nào”. Nó tránh claim không kiểm chứng được “continuum models nói chung dùng đến đâu”. Caruso còn hữu ích như analytical benchmark, nhưng không phải primary R full-layer contact được chọn.

Không tìm được trong phần hồ sơ này một timestamp riêng chứng minh chính xác lúc người dùng chấp thuận M1. Vì vậy báo cáo chỉ khẳng định lựa chọn đã được ghi trong architecture, không gán nó ngược về V002.

## 11. Ma trận tiến hóa claim

Các mã `DH` dưới đây do báo cáo này dùng để đọc lịch sử; không phải ID hoặc verdict mới ghi vào canonical state.

| ID | Claim/câu hỏi trước | Bằng chứng hoặc vấn đề kích hoạt | Thay đổi có căn cứ trong hồ sơ | Claim/câu hỏi sau |
|---|---|---|---|---|
| DH01 | D1 friction–warping–cyclic degradation | Discovery critique: quá nhiều cơ chế, observability/confounding | Chọn có sửa đổi, medium | Interlayer slip và bending stiffness |
| DH02 | Phát triển mô hình slip–stiffness và kiểm tra thực nghiệm | Narang 2018, Caruso 2023; V001 | PIVOT, high | P1 validity limits/high-layer-count representation, còn giả thuyết |
| DH03 | Continuum/homogenized model có thể là phần chưa có | Ba nguồn Zhang và V002 | Thu hẹp | Không nhận creation of continuum model là novelty |
| DH04 | Các biến pressure/N/curvature/slip tạo gap | Deeper Understanding; Fan; V003 | SURVIVES_WITH_REVISED_SCOPE | Cần model cụ thể và kiểm tra quantitative validity |
| DH05 | Discrete-to-continuum/slip comparison là đóng góp mới | C01: slipping layers, shear-weak, imperfect interfaces | SUBSTANTIALLY_NARROWED | Phải tính cả prior art ngoài layer jamming |
| DH06 | Sai số/interaction parameter/applicability chưa có | C02: partial interaction, multilayer theory | SUBSTANTIALLY_NARROWED | Không lấy error metric hoặc parameter sweep làm novelty |
| DH07 | Continuum–contact error boundary là phần còn mới | C03: Wang IJSS 2026 | SUBSTANTIALLY_NARROWED | Cần chứng minh phần riêng vượt quá một ứng dụng thường quy |
| DH08 | Đã đủ đóng kiểm chứng | C04 còn thiếu named target; threshold timing chưa rõ | INCONCLUSIVE_MISSING_TARGET | Lấy full text, sửa nghĩa adopted/predeclared |
| DH09 | Ye có thể đã thực hiện phép kiểm tra tương đương | V008 full text | SURVIVES_FINAL_TARGET | Sống sót đối với target này, có điều kiện phạm vi |
| DH10 | Cosserat large-deformation/slip có thể pre-empt | V009 Adhikary | SURVIVES_LATE_FOUND_TARGET | Không claim continuum/slip/large deformation tự thân |
| DH11 | Validity của một lớp mô hình chung | So sánh M1/M2 và architecture | Chỉ định M1, M→R→E | Đánh giá giới hạn của đúng M1 trong một family |
| DH12 | Có thể chốt thành đề tài thực hiện | Final direction adjudication | LOCK_WITH_FEASIBILITY_GATE, medium | Tên hiện tại, nhưng cần gate khoa học/khả thi |
| DH13 | Có thể dùng các summary để khẳng định novelty | Plan V6, W01–W11; source contradictions và K-tests chưa đóng | Tái dựng và kiểm tra bằng chứng, chưa final adjudication | Candidate contribution tiếp tục bị thử bác bỏ |
| DH14 | T2 Wang M&D 2026 còn metadata-only | Full-text audit và append-only reconciliation ngày 26-09 | VERIFIED_FULL_TEXT / PARTIAL_OVERLAP ở source disposition | Đã gỡ thiếu full text; chưa có final K verdict, chưa mở W12 |

Các quyết định này không chứng minh “novelty xuất hiện dần” theo nghĩa logic tất yếu. Chúng chứng minh **claim đã bị cắt bỏ từng phần**; phần còn lại vẫn có thể không đủ đóng góp khoa học.

## 12. Tên đề tài hiện tại thực sự cam kết điều gì?

| Cụm trong tên | Nghĩa cần trình bày | Không nên hiểu thành |
|---|---|---|
| Experimental Assessment | Dùng phép đo để kiểm tra giá trị dự đoán và các giới hạn của mô hình | Dự án đã hoàn thành thí nghiệm |
| Validity | Mô hình đủ chính xác đối với output, domain và mục đích đã định | Mô hình đúng tuyệt đối |
| Breakdown | Dự đoán vượt mức chấp nhận hoặc giả thiết không còn phù hợp | Nhất thiết vật mẫu bị gãy/hỏng |
| A Continuum Model | Đúng M1 được chỉ định | Tất cả continuum/homogenization models |
| Vacuum Layer-Jamming Beams | Family cơ học giới hạn để bảo đảm so sánh kiểm soát được | Đổi application/material là đủ mới |

[HYPOTHESIS] Câu hỏi làm việc: đối với M1 và một beam/material family được khóa, sai số dự đoán nào thay đổi theo số lớp, áp suất và mức uốn; ở đâu sai số vượt tiêu chí đã biện minh; sự vượt ngưỡng có liên hệ nhân quả đủ mạnh với contact/slip hoặc giả thiết cơ học bị bỏ qua hay không?

Nêu câu hỏi này không đồng nghĩa đã chứng minh nó còn mới. Đặc biệt, “thêm uncertainty và predeclared tolerance” có thể chỉ nâng chất lượng nghiên cứu, chưa chắc tạo scientific-question novelty.

## 13. Những gì chắc chắn không nên nhận làm đóng góp mới

Từ bằng chứng nêu ở các mục 5–9, không nhận novelty tự thân cho: layer jamming; vacuum-controlled stiffness; friction; interlayer slip; các regime pre/partial/full slip; continuum hoặc reduced modeling; layered beam theory; Coulomb contact; full-layer FEM; experimental characterization; model-versus-experiment comparison; error metric; threshold; parameter sweep.

Phần còn đang **được kiểm tra**, không phải được xác nhận:

1. Một kết quả model-specific: xác định được miền dự đoán dùng được/không dùng được của M1 với outputs có nghĩa cơ học và uncertainty đủ nhỏ để phân biệt.
2. Một kết quả explanatory: chỉ ra mechanism chịu trách nhiệm cho failure, thay vì chỉ vẽ contour sai số.
3. Một kiểm tra độc lập có sức phân biệt: R đã verification và E không bị calibration leakage xác nhận hoặc bác bỏ boundary dự đoán.

**Phép thử chống tự bảo vệ đề tài:** nếu prior art đã làm một phép kiểm tra tương đương về mechanics, khác model name hoặc hệ chân không không đủ cứu novelty. Nếu framework đã biết áp dụng trực tiếp và không tạo hiểu biết cơ học mới, contribution có thể chỉ còn validation/application work.

## 14. Tiến độ mới nhất: phải đọc cả các bản bổ sung, không chỉ snapshot

### 14.1 Tái dựng W01–W11 đã được thực hiện

[HỒ SƠ QUYẾT ĐỊNH] [Current snapshot](../project/CURRENT_EXECUTION_SNAPSHOT.md) ghi các bước inventory, lịch sử claim, extraction theo literature families, reconciliation, K1–K9 freeze, targeted threats và provenance QA. W09 tổng hợp 68 unique papers từ 71 source records. Không cộng số này với 54 rồi gọi là tổng số primary papers duy nhất: hai phép đếm thuộc corpus/workflow khác nhau.

Các matrices V001–V009 lần lượt có 3, 4, 9, 15, 16, 16, 3, 1, 1 entries. Chúng là counts của vòng, không phải phép chứng minh independence hoặc coverage toàn cầu.

W12 và final D1-only adjudication chưa được cho phép chỉ vì W11 đã hoàn thành. QA PASS là trạng thái của một lần kiểm tra, không bảo đảm mọi narrative statement đều đúng.

### 14.2 Bổ sung quan trọng: T2 đã có full-text audit

Snapshot và threat matrix lịch sử còn ghi Wang et al. (2026), DOI `10.1016/j.matdes.2026.116573`, là metadata/abstract-only. Tuy nhiên có nguồn successor riêng:

- [Full-text audit](../../outputs/d1_execution/V4/W10/D1_T2_WANG2026_FULLTEXT_AUDIT.json).
- [Append-only reconciliation](../../outputs/d1_execution/V4/W10/D1_T2_WANG2026_THREAT_RECONCILIATION.json).
- [W11 provenance review](../../outputs/d1_execution/V4/W11/D1_T2_WANG2026_PROVENANCE_REVIEW.json).

[VERIFIED FULL TEXT] Đây là *Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction*, Qinyu Wang, Peng Feng, Bo Wu, Mingrui Teng, Kaspar Jansen & Charun Bao; full text 17 trang có hash được kiểm tra trong audit. Bài có simplified models, thực nghiệm và thảo luận discrepancies/structural causes.

[INFERENCE của audit] Disposition kế tiếp là `PARTIAL_OVERLAP`; audit không xác lập bài này có toàn bộ interface-resolved R/error-map/predeclared-boundary experiment đang xét. Đây chỉ là source disposition. `final_K_verdict_assigned = false`, `W12_authorized = false`.

**Không còn đúng nếu nói hiện nay T2 vẫn chưa được đọc full text.** Lịch sử metadata-only vẫn được giữ để audit, nhưng không được dùng nó thay trạng thái evidence mới. Còn thiếu raw measurements/uncertainty và một số chi tiết specimen nêu trong audit; không tự điền thêm.

### 14.3 U1/U2 đã làm rõ protocol, nhưng chưa tạo kết quả cơ học

[HỒ SƠ QUYẾT ĐỊNH] [U1 state](../../outputs/d1_execution/V4/W11/D1_HG06_U1_STATE.json) và [U2 state](../../outputs/d1_execution/V4/W11/D1_HG06_U2_STATE.json) là các bổ sung cần đọc cùng architecture cũ:

- M1 implementation contract đã mô tả đủ để khóa bằng văn bản, nhưng chưa có executable implementation/hash/published-case reproduction hoàn tất.
- R đã thu hẹp thành primary 2D plane-stress, từng physical layer riêng, unilateral frictional contact, finite rotation, có targeted 3D/fixture/membrane challenge; vẫn `PARTIALLY_LOCKED` và cần pilot.
- Sweep số lớp dự kiến giữ tổng thickness và thay individual thickness; đây là lựa chọn protocol, không phải một kết quả convergence đã đo.
- Deflection output đã có định nghĩa; stiffness dùng service-window chord nhưng numerical service interval còn thiếu.
- Mô hình onset, local interface onset trong R và onset đo trong E chưa được coi mặc nhiên là cùng sự kiện. Global force–deflection kink không tự chứng minh first slip.
- Các tolerance vẫn `null`; HG-06/HG-09 vẫn blocked. U2 không phải bằng chứng đã chạy M, R hoặc E.

T2 successor audit đã giải quyết phần thiếu full text được nhắc lại trong một số U2 routing text. Các yêu cầu human review và threshold/pilot khác không vì vậy tự được giải quyết.

## 15. Sai khác trong hồ sơ cần công khai khi trình bày

| Sai khác | Cách xử lý trong báo cáo này |
|---|---|
| AGENTS/current-state đoạn cũ dừng ở V001/P1, handoff và snapshot cũng có mốc khác nhau | Giữ operating rules; dùng verdict theo vòng và successor artifacts để kể lịch sử. Không sửa file cũ |
| W09 Claim Evolution Matrix trộn tên *Toward a deeper understanding…* với DOI M1 | Phân biệt theo DOI/paper_id ở mục 6; không dùng transition đó làm citation identity |
| W09 gán Fan với DOI của Zhang M2 | Fan dùng DOI `10.1109/TCST.2026.3690756`; M2 dùng `10.1016/j.taml.2025.100633` |
| Một số summary/register nói Wang IJSS không có thực nghiệm | Evidence `ca46dc062d`, tr. 10–11, có experimental comparison; thiếu boundary-crossing experiment là câu hỏi khác |
| Một report gọi ngưỡng Wang là post hoc | Chỉ xác minh được adopted threshold; không suy thời điểm lựa chọn nếu không có chứng cứ |
| W09 Ye DOI sai | W11 contradiction register và V008 xác định `10.1061/JSENDH.STENG-13096` |
| V002 synthesis có specimen M1 khác evidence sau | Không dùng số 12 lớp/80 kPa trong summary cũ; source-grounded U2/evidence M1 dùng published example 20 lớp/60 kPa |
| Snapshot nói T2 thiếu full text, nhưng successor audit/provenance đã có | Báo cáo cả trạng thái cũ và transition mới; không giả vờ các file cũ đã được cập nhật |
| Chưa xác minh một ngày quyết định riêng cho việc khóa M1 | Ghi theo pha và nguồn architecture, không tạo ngày chính xác |

Nguồn đối chiếu: [W09 claim matrix](../../outputs/d1_execution/V4/W09/D1_CLAIM_EVOLUTION_MATRIX.json), [W09 candidate register](../../outputs/d1_execution/V4/W09/D1_NOVELTY_CANDIDATE_REGISTER.json), [W11 contradiction register](../../outputs/d1_execution/V4/W11/D1_CONTRADICTION_REGISTER.json), cùng evidence nguyên thủy ở mục 18.

Những sai khác này không tự đổi historical verdict; nhưng chúng làm một số cách giải thích verdict không còn đáng tin. Không nên trình bày supervisor bằng một summary đã PASS citation-check mà bỏ qua mâu thuẫn nội dung gốc.

## 16. Cách trình bày đầy đủ với người hướng dẫn

Một trình tự giải thích có thể kiểm tra được:

1. **Xuất phát:** 54 seed papers được dùng để sinh năm hướng, không dùng để chứng minh novelty.
2. **Lựa chọn ban đầu:** D1 đã là một câu hỏi cơ học; sau critique, bỏ bớt cyclic-degradation/warping để tập trung slip–stiffness.
3. **Bác bỏ trực tiếp:** Narang và Caruso khiến claim mô hình slip–stiffness chung không đứng được; V001 yêu cầu pivot.
4. **Bác bỏ formulation rộng:** Zhang đã có continuum model và khảo sát các yếu tố quan trọng; không thể chỉ “làm continuum cho nhiều lớp”.
5. **Bác bỏ bằng cơ học lân cận:** partial-interaction, slipping-layer, Cosserat và đặc biệt Wang IJSS đã có nhiều phần của quantitative validity analysis.
6. **Định nghĩa lại đối tượng:** chọn đúng M1; phân biệt M, R và E; tìm một câu hỏi model-specific có thể bị dữ liệu bác bỏ.
7. **Trạng thái trung thực:** tên đề tài đã được khóa có điều kiện, nhưng scientific novelty và feasibility chưa được kết luận cuối; hồ sơ mới vẫn cần giải quyết gate và mâu thuẫn evidence.

Ba phát biểu phải tách biệt: (A) layer-jamming modeling đã làm nhiều; (B) experimental validation đã làm nhiều; (C) đóng góp cụ thể của D1 đã được prior art tương đương bao phủ hay chưa. A và B đúng không tự chứng minh C; ngược lại, chưa tìm đủ bằng chứng cho C không chứng minh C sai.

## 17. Những việc còn thiếu trước khi có thể bảo vệ kết luận cuối

1. Dùng các successor artifacts và nguồn gốc để đóng những mâu thuẫn ảnh hưởng scientific claim; đặc biệt không dựa vào luận điểm sai “Wang không có thí nghiệm”. Đây là evidence reconciliation, không nhất thiết là broad search mới.
2. Hoàn tất human review theo gate đang ghi; đưa T2 full-text disposition vào review đúng phạm vi, không dùng source-level `PARTIAL_OVERLAP` thay final K adjudication.
3. Chốt specimen/fixture và engineering use case để output, pressure transfer, interval stiffness và slip observability có nghĩa vật lý.
4. Làm các feasibility/uncertainty pilots được cho phép theo protocol để biết R đáng tin tới đâu, E phân biệt được gì; không tự điền tolerance 5% hoặc lựa tolerance sau khi nhìn final map.
5. Sau khi đủ điều kiện mới thực hiện adversarial K-tests và D1-only final synthesis/adjudication. Nếu không có đóng góp cơ học vượt routine application, phải thu hẹp hoặc bác bỏ claim novelty.

**Cách nói đúng lúc này:** “Đây là ứng viên nghiên cứu được hình thành qua nhiều lần bác bỏ và thu hẹp, đã có tên làm việc cùng kiến trúc kiểm tra có điều kiện; chưa có đủ cơ sở từ báo cáo lịch sử này để tuyên bố novelty toàn cục.”

## 18. Chỉ mục nguồn để mở trong buổi thảo luận

### Hồ sơ quyết định và trạng thái

- [Discovery candidate và original D1](../../outputs/discovery_snapshot/candidate_directions.json).
- [Discovery final adjudication](../../outputs/discovery_snapshot/final_adjudication.json).
- [Research log](../project/RESEARCH_LOG.md), [machine-readable state](../project/research_state.json), [current snapshot](../project/CURRENT_EXECUTION_SNAPSHOT.md). Đọc kèm successor artifacts, không coi một snapshot là toàn bộ lịch sử.
- [Plan V6](../../outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V6.md), [K criteria register](../../outputs/d1_execution/V4/S09/D1_K_CRITERIA_REGISTER.json).
- [Historical final direction lock](../../outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json), [HG-06 threshold register](../../outputs/d1_execution/V4/W11/D1_THRESHOLD_FREEZE_REGISTER.json), [human review clearance](../../outputs/d1_execution/V4/W11/D1_HUMAN_REVIEW_CLEARANCE.json).

### Evidence JSON của các nguồn trực tiếp và đe dọa quan trọng

Các đường dẫn dưới đây là nguồn trích xuất full text; trường `source` và các evidence claims chứa provenance/page locators. Không điền thêm journal volume, DOI còn thiếu hoặc page number ngoài những gì đã xác minh. Page ở nội dung báo cáo là locator do evidence ghi; khi trích dẫn chính thức phải kiểm tra hệ đánh số PDF/printed page.

- [Narang 2018 — 5f7ccd7357](<../../data/evidence/2018-Mechanically Versatile Soft Machines through Laminar_5f7ccd7357.json>).
- [Caruso 2023 — 652e62758f](../../data/evidence/2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation_652e62758f.json).
- [Zhang M1 — 95646b2cfc](<../../data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json>).
- [Zhang Deeper Understanding — 7cb387b88d](<../../data/evidence/2025-Toward a deeper understanding of layer jamming structures_7cb387b88d.json>).
- [Zhang M2 — a792efc445](<../../data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json>).
- [Fan 2026 — 1f05cf83bc](../../data/evidence/2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming_1f05cf83bc.json).
- [Wang IJSS 2026 — ca46dc062d](<../../data/evidence/2026-The global-local mechanical behaviors of multilayered structure and_ca46dc062d.json>).
- [Wang M&D 2026 — full-text audit độc lập](../../outputs/d1_execution/V4/W10/D1_T2_WANG2026_FULLTEXT_AUDIT.json). Không nhầm với Wang IJSS; hai bài có DOI và vai trò khác nhau.

Đối với các nguồn adjacent khác, các canonical audits V004–V009 đã liên kết trong mục 8–9 và verification matrices cùng thư mục cung cấp `paper_id`, evidence file và source provenance. Chúng được dùng để truy vấn chính xác, không thay một DOI chưa xác minh bằng DOI suy đoán.

### Phạm vi hoàn thành của báo cáo

Đã tái dựng các bước quyết định quan trọng từ discovery đến current M1 và các bổ sung W10/W11; đã phân biệt lịch sử verdict, bằng chứng full text và đóng góp còn giả thuyết. Chưa thực hiện final novelty adjudication, chưa thực hiện pilot M/R/E, chưa đóng gate hoặc sửa các hồ sơ có sai khác. Báo cáo này phục vụ thảo luận có kiểm chứng, không phải tài liệu chứng nhận đề tài mới.
