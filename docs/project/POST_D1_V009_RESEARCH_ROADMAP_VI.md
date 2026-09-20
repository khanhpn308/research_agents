# Lộ trình Review và Triển khai Nghiên cứu — Sau D1-V009

> **Trạng thái:** Lộ trình hiện hành sau D1-V009  
> **Mục đích:** cung cấp một thứ tự đọc theo chuỗi nhân quả để review toàn bộ project và một lộ trình triển khai nghiên cứu từ trạng thái hiện tại trở đi.  
> **Trạng thái repository hiện tại:** 123 paper records = 54 paper seed + 69 paper verification; 122 included, 1 excluded, 0 pending.  
> **Mô hình rút gọn hiện tại:** M1 — Zhang và cộng sự, *A continuum-based model for a layer jamming beam*, DOI 10.5194/ms-16-821-2025.  
> **Trạng thái novelty hiện tại:** provisional lock vẫn sống sót sau D1-V009; broad search tiếp tục dừng trừ khi xuất hiện một nguồn đe dọa cao cụ thể mới.

---

# 1. Tài liệu này dùng để làm gì?

Không nên review repository theo thứ tự tên file.

Phải đọc nó như một chuỗi nhân quả:

~~~text
bằng chứng gốc
→ evidence đã trích xuất
→ corpus có cấu trúc
→ suy luận cục bộ
→ tạo candidate trên toàn corpus
→ phản biện đối kháng
→ chọn tạm thời
→ corpus độc lập để bác bỏ
→ thu hẹp lặp lại
→ đóng các high-threat target
→ late-found post-lock audit
→ chọn exact model
→ kiến trúc nghiên cứu
→ triển khai
~~~

Ở mỗi mũi tên luôn hỏi:

> Kết luận phía sau có thực sự được bằng chứng phía trước hỗ trợ không?

Mục tiêu là để bạn tự hiểu và tự bảo vệ toàn bộ logic hình thành đề tài, không chỉ kế thừa kết luận của agent.

---

# 2. Toàn bộ trạng thái project hiện tại trong một sơ đồ

~~~text
54 PAPER SEED
│
├─ evidence extraction
▼
data/evidence/*.json
│
├─ chuẩn hóa corpus
▼
outputs/discovery_snapshot/literature_matrix_54papers.json
│
├─ 54 papers → 9 batch × 6
▼
outputs/reasoning_batches/
│
├─ synthesis trong từng batch
▼
outputs/batch_syntheses/
│
├─ reasoning xuyên batch
▼
5 candidate directions
│
├─ adversarial critique
▼
direction critique
│
├─ final discovery adjudication
▼
D1 được chọn với revision
│
├─ independent verification
▼
D1-V001 → broad D1 bị PIVOT
│
▼
P1 = validity limits của continuum / homogenized layer-jamming mechanics
│
├─ kiểm tra các threat trực tiếp mới
▼
D1-V002
│
├─ direct LJ + forward-citation + target audits
▼
D1-V003
│
├─ adjacent mechanics: frictional multilayers
▼
D1-V004 / C01
│
├─ adjacent mechanics: partial interaction
▼
D1-V005 / C02
│
├─ adjacent mechanics: imperfect interface / friction-contact
▼
D1-V006 / C03
│
├─ forward citations của strongest threat
▼
D1-V007 / C04
│
├─ final named target
▼
D1-V008
│
├─ đạt stop condition của broad search
▼
PROVISIONAL NOVELTY LOCK
│
├─ so sánh exact reduced model
▼
M1 vs M2
│
├─ người dùng chọn M1
▼
M1 RESEARCH ARCHITECTURE
│
├─ phát hiện late-found adjacent mechanics paper
▼
D1-V009 — Adhikary et al. 1999
│
└─ kết quả:
   SURVIVES_LATE_FOUND_TARGET
   confidence: high
   kill condition: false
   novelty lock survives: true
   reopen broad search: false
   targeted follow-up: false
│
▼
GIAI ĐOẠN HIỆN TẠI:
RECONSTRUCT M1 → LOCK R → LOCK RQ/HYPOTHESIS/TOLERANCES → IMPLEMENT → VALIDATE → EXPERIMENT
~~~

---

# 3. Lộ trình review ngược — từ 54 paper nền đến đề tài hiện tại

## Giai đoạn A — Hiểu logic nghiên cứu của repository

Đọc trước:

1. `docs/project/RESEARCH_STATE.md`
2. `docs/project/RESEARCH_LOG.md`

Chỉ dùng hai file này để hiểu lịch sử. Không dùng chúng làm current source of truth.

Câu hỏi cần trả lời:

> Pipeline ban đầu được thiết kế để làm gì và vì sao lại dùng cách adversarial thay vì chỉ xác nhận ý tưởng?

---

## Giai đoạn B — Audit nền tảng 54 paper discovery

Bắt đầu từ:

1. `data/paper_registry.json`
2. 54 seed evidence JSON trong `data/evidence/`
3. `outputs/discovery_snapshot/literature_matrix_54papers.json`

Với từng paper, review:

~~~text
metadata
→ research objective
→ model/method
→ variables
→ evidence claims
→ assumptions
→ author-stated limitations
→ inferred limitations
→ future work
→ gap implications
~~~

Câu hỏi audit:

> Extraction có giữ đúng nội dung paper không, hay inference đã bị nâng thành fact?

Khi một claim quan trọng, quay lại PDF gốc đang lưu ở máy.

---

## Giai đoạn C — Audit 9 reasoning batches

Đọc:

1. `outputs/reasoning_batches/manifest.json`
2. `outputs/reasoning_batches/batch_001.json` đến `batch_009.json`
3. `outputs/batch_syntheses/manifest.json`
4. `outputs/batch_syntheses/B001.json` đến `B009.json`

Reasoning batches là input; batch syntheses là lớp inference lớn đầu tiên.

Với từng proposed gap:

~~~text
gap claim của agent
→ supporting paper_ids
→ evidence JSON
→ original paper nếu cần
~~~

Câu hỏi audit:

> Gap này có thật sự suy ra từ evidence, hay chỉ là "không thấy trong một batch nhỏ"?

---

## Giai đoạn D — Audit quá trình sinh 5 candidate directions

Đọc theo thứ tự:

1. `outputs/discovery_snapshot/candidate_directions.json`
2. `outputs/candidate_directions.md`
3. `outputs/discovery_snapshot/direction_critique.json`
4. `outputs/direction_critique.md`
5. `outputs/discovery_snapshot/final_adjudication.json`
6. `outputs/final_adjudication.md`

Năm candidate thực tế:

- D1 — vacuum layer-jamming: friction / warping / cyclic stiffness degradation, sau đó revision về interlayer slip + bending stiffness.
- D2 — positive-pressure layer jamming dưới tải uốn.
- D3 — phase-change soft finger / thermal mechanics.
- D4 — membrane–granulate interaction trong vacuum jamming grippers.
- D5 — higher-order shear model cho fluidic prestressed composite actuators.

Câu hỏi audit:

> Vì sao D1 sinh ra từ evidence?

> Vì sao critic giữ D1/D2 và đánh yếu các hướng còn lại?

> Vì sao final adjudication chọn D1?

Kết luận quan trọng:

~~~text
Ở đây D1 chỉ là candidate tốt nhất trong 54 paper.
Chưa có nghĩa D1 là novel.
~~~

---

# 4. Lịch sử verification — D1 biến thành P1 hiện tại như thế nào?

## D1-V001 — Broad D1 bị bác bỏ

Đọc:

1. `outputs/verification/D1-V001/verification_matrix.md`
2. `outputs/verification/D1-V001/direction_verification.md`

Paper chính:

- Narang et al. 2018
- Caruso et al. 2023
- Atakuru et al. 2024

Kết quả:

~~~text
VERDICT = PIVOT
CONFIDENCE = high
~~~

Ý nghĩa:

- pressure/friction/slip mechanics đã có;
- bending-stiffness evolution đã được model;
- transition load đã được đặc trưng;
- modeling + FEA + experiment đã tồn tại.

Novelty của D1 ban đầu bị đóng phần lớn.

---

## D1-V002 — Continuum models đã tồn tại

Đọc:

1. `outputs/verification/D1-V002/verification_matrix.md`
2. `outputs/verification/D1-V002/adversarial_evidence_synthesis.md`

Round này xác nhận contribution không thể là:

> tạo một continuum/homogenized model mới cho layer jamming.

Các continuum beam và constitutive formulation đã có.

Câu hỏi còn sống chuyển thành:

> Khi nào một reduced/continuum model cụ thể đủ chính xác, và khi nào nó breakdown?

Đây là nguồn gốc conceptual trực tiếp của thesis hiện tại.

---

## D1-V003 — Tấn công trực tiếp validity gap

Đọc protocol trước:

1. `docs/protocols/D1-V003_LITERATURE_AUDIT_PLAN.md`
2. `docs/protocols/D1-V003_VALIDITY_GAP_SEARCH_PROTOCOL.md`

Sau đó:

3. `outputs/verification/D1-V003/FAN_2026_MODEL_AUDIT.md`
4. `outputs/verification/D1-V003/ZHANG_2025_DEEPER_UNDERSTANDING_AUDIT.md`
5. `outputs/verification/D1-V003/D1-V003_EVIDENCE_MATRIX.md`
6. `outputs/verification/D1-V003/D1-V003_SEARCH_LOG.md`
7. `outputs/verification/D1-V003/cross_round_adversarial_synthesis.md`

Kết quả:

~~~text
SURVIVES_WITH_REVISED_SCOPE
~~~

Bài học chính:

Có continuum model không đồng nghĩa đã có quantitative validity-domain study.

---

## D1-V004 / C01 — Frictional multilayer mechanics

Đọc:

1. `outputs/verification/D1-V004/verification_matrix.md`
2. `outputs/verification/D1-V004/C01_ADVERSARIAL_AUDIT.md`

Kết quả:

~~~text
SUBSTANTIALLY_NARROWED
~~~

Round này loại bỏ các broad novelty claim dựa trên:

- discrete-to-continuum transition;
- asymptotic continuum limit;
- finite-layer error comparison;
- generic homogenization của layered structures.

---

## D1-V005 / C02 — Partial-interaction composite beams

Đọc:

1. `outputs/verification/D1-V005/verification_matrix.md`
2. `outputs/verification/D1-V005/C02_ADVERSARIAL_AUDIT.md`

Literature này đã có:

- interaction parameters;
- effective EI;
- exact-vs-approximate benchmarking;
- partial-interaction criteria;
- connector-discreteness studies.

Vì vậy các ý tưởng này không thể tự mình mang novelty.

---

## D1-V006 / C03 — Imperfect interface, friction và contact

Đọc:

1. `outputs/verification/D1-V006/verification_matrix.md`
2. `outputs/verification/D1-V006/C03_ADVERSARIAL_AUDIT.md`

Strongest generic threat xuất hiện:

> Wang et al. 2026, paper_id `ca46dc062d`

Paper này đã có nhiều phần của generic validity framework:

- continuum multilayer model;
- Coulomb friction/contact;
- discrete-contact comparison;
- quantitative error;
- finite layer/deformation sweeps;
- adopted 5% applicability threshold;
- experiments.

Surviving contribution bị thu hẹp thêm.

---

## D1-V007 / C04 — Đóng nhánh forward citation

Đọc:

1. `outputs/verification/D1-V007/verification_matrix.md`
2. `outputs/verification/D1-V007/C04_ADVERSARIAL_AUDIT.md`
3. `outputs/verification/D1-V007/C04_SEMANTIC_CORRECTION.md`

Semantic correction là file bắt buộc phải đọc.

Phân biệt cốt lõi:

~~~text
observed/adopted/post-hoc threshold
≠
predeclared acceptance tolerance
~~~

Trong project này, PREDECLARED nghĩa là:

> threshold được cố định trước khi xem relevant validation/model-error results.

Đây là một methodological guardrail chính thức của project.

---

## D1-V008 — Đóng final named target

Đọc:

1. `outputs/verification/D1-V008/verification_matrix.md`
2. `outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.md`
3. `outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json`

Kết quả:

~~~text
SURVIVES_FINAL_TARGET
kill_condition_met = false
broad_search_should_stop = true
final_novelty_lock_allowed = true
~~~

Ý nghĩa:

Search protocol đã đạt điều kiện dừng.

Đây không phải bằng chứng tuyệt đối rằng trên thế giới không có overlap. Nó là căn cứ để dừng broad search vô hạn và chuyển sang thesis execution.

---

# 5. Exact model selection

Sau khi novelty search dừng, đọc:

1. `docs/research_design/LAYER_JAMMING_MODEL_COMPARISON.md`
2. `docs/learning/CURRENT_RESEARCH_DIRECTION_TUTORIAL.md`
3. `docs/research_design/EXACT_MODEL_SELECTION.md`

Hai candidate cuối:

~~~text
M1 = Zhang 2025 continuum beam model
M2 = Zhang 2025/2026 RVE-derived constitutive continuum model
~~~

Bạn đã chọn:

~~~text
M1
~~~

vì thesis hiện tại là beam-scale validity study, không phải RVE-to-continuum constitutive-validation study.

---

# 6. D1-V009 — late-found post-lock audit

Đọc:

1. `docs/protocols/D1-V009_LATE_FOUND_ADJACENT_AUDIT_PLAN.md`
2. `outputs/verification/D1-V009/verification_matrix.md`
3. `data/evidence/Mech Cohesive Frict Material - 1999 - Adhikary - Modelling the large deformation_d75a3e82bc.json`
4. `outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.md`
5. `outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.json`

Target:

> Adhikary, Mühlhaus, and Dyskin (1999), *Modelling the large deformations in stratified media—the Cosserat continuum approach*.

Kết quả:

~~~text
STATUS = SURVIVES_LATE_FOUND_TARGET
CONFIDENCE = high
KILL CONDITION = false
FINAL NOVELTY LOCK SURVIVES = true
REOPEN BROAD SEARCH = false
TARGETED FOLLOW-UP = false
~~~

D1-V009 làm mất quyền claim novelty ở:

- equivalent/smeared continuum cho frictional layered media;
- Cosserat/generalized continuum;
- couple stresses + independent rotations để biểu diễn layer bending stiffness;
- large-deformation layered continuum;
- frictional/plastic interlayer slip;
- interface opening/delamination;
- FE implementation cho các mechanics đó.

Phần vẫn defensible:

- một reduced vacuum-layer-jamming model cụ thể;
- output-specific tolerance được định trước final error inspection;
- quantitative reduced-vs-full-layer model-form error mapping;
- layer-count/discreteness và vacuum pressure như validity variables;
- tolerance-defined valid/invalid regions;
- experiment chủ động test cả hai phía boundary;
- vacuum-specific normal-contact / friction / pressure-redistribution / separation mechanics khi cần.

---

# 7. Theoretical lineage mới nhất sau D1-V009

Nên hiểu literature thành hai nhánh hội tụ.

## Nhánh A — General layered-media mechanics

~~~text
classical layered / partial-interaction mechanics
        ↓
Cosserat / generalized continuum approaches
        ↓
Adhikary et al. 1999
equivalent continuum
+ independent rotations
+ couple stresses
+ large deformation
+ frictional/plastic interfaces
+ opening / delamination
        ↓
modern multilayer homogenization / imperfect-interface / contact mechanics
~~~

## Nhánh B — Layer-jamming-specific mechanics

~~~text
Narang 2018
two-layer analytical mechanics
+ explicit frictional-contact FEA
+ experiments
        ↓
Caruso 2023
arbitrary multilayer discrete-interface progressive slip
+ pressure
+ friction
+ stiffness degradation
+ FEA
+ experiments
        ↓
Zhang 2025
continuum beam representation
+ continuous slip-zone description
+ stress fields
+ load-deflection prediction
        ↓
CÂU HỎI HIỆN TẠI
Zhang M1 valid khi nào, xét định lượng?
~~~

Contribution không phải là phát minh continuum mechanics cho layered media. Contribution là kiến trúc validity định lượng, có experiment, cho một vacuum layer-jamming reduced model cụ thể.

---

# 8. Kiến trúc nghiên cứu hiện tại

Đọc canonical architecture:

1. `docs/research_design/M1_RESEARCH_ARCHITECTURE.md`
2. `docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md`

## Đã khóa

~~~text
RESEARCH DIRECTION =
quantitative validity / breakdown của vacuum layer-jamming beam model

REDUCED MODEL M =
Zhang et al. 2025 continuum beam model
DOI 10.5194/ms-16-821-2025

GENERAL CONTRIBUTION =
xác định khi nào M1 đủ chính xác và khi nào không
~~~

## Vẫn provisional

~~~text
PRIMARY REFERENCE R
PRIMARY OUTPUTS
PRIMARY BREAKDOWN VARIABLES
FINAL RESEARCH QUESTION
FINAL HYPOTHESIS
ERROR METRICS
ERROR TOLERANCES
PARAMETER-SPACE BOUNDS
CALIBRATION / VALIDATION SPLIT
EXPERIMENTAL BOUNDARY-SAMPLING PLAN
~~~

Working title hiện tại:

> **Quantitative Validity Limits of a Continuum Model for Vacuum Layer-Jamming Beams under Quasi-Static Bending**

Coi đây là working title đến khi exact RQ và reference architecture được khóa.

---

# 9. Lộ trình triển khai từ bây giờ

Sau D1-V009, không quay lại broad topic discovery trừ khi có concrete high-threat source.

Từ đây research đi qua các gate thực thi.

---

## Gate 1 — Tái dựng M1 hoàn chỉnh

Mục tiêu:

> hiểu M1 đến mức có thể tự derive, giải thích, implement và challenge mà không cần nhìn paper từng dòng.

Tạo một M1 reconstruction record gồm:

- physical system;
- notation;
- state variables;
- governing equations;
- assumptions;
- jammed / partial-slip / full-slip logic;
- load regimes;
- incremental algorithm;
- published numerical cases;
- published experiments;
- reported discrepancies;
- mọi assumption có thể gây breakdown.

Chuỗi tư duy bắt buộc:

~~~text
physical mechanism
→ assumption
→ governing equation
→ state transition
→ predicted output
→ validation evidence
→ possible failure mode
~~~

**Điều kiện qua Gate:** từ một tờ giấy trắng bạn tự dựng lại được computational flow của M1.

---

## Gate 2 — Khóa Primary Reference R

Lựa chọn provisional hiện tại:

> full-layer explicit-contact finite-element model.

Phải khóa formulation chính xác:

- FE software/solver;
- 2D hay 3D;
- layer representation;
- element type;
- interface/contact formulation;
- friction law;
- cách áp pressure;
- membrane representation hoặc lý do bỏ;
- separation/lift-off;
- boundary conditions;
- nonlinear geometry;
- convergence criteria;
- mesh-convergence protocol;
- numerical uncertainty.

Không gọi R là "truth". R chỉ là higher-fidelity reference và cũng có assumptions.

**Điều kiện qua Gate:** có một reference-model specification đủ để người khác tái tạo.

---

## Gate 3 — Khóa Primary Outputs

Candidate hiện tại:

~~~text
O1 = beam deflection w
O2 = effective bending stiffness K hoặc EI_eff
O3 = slip-transition load Q_slip hoặc external load tương đương
~~~

Với từng output phải định nghĩa:

- công thức chính xác;
- vị trí đo;
- cách M1 tính;
- cách R trích xuất;
- cách experiment đo;
- đơn vị;
- uncertainty;
- xử lý trường hợp denominator gần 0.

**Điều kiện qua Gate:** cùng một output được lấy nhất quán từ M1, R và experiment.

---

## Gate 4 — Khóa Breakdown Variables

Candidate hiện tại:

~~~text
B1 = finite layer count n
B2 = vacuum pressure p
B3 = bending severity P, kappa, hoặc normalized equivalent
~~~

Secondary variables để sau:

- friction coefficient;
- layer thickness;
- aspect ratio;
- boundary condition;
- initial curvature;
- membrane/sheath effects;
- pressure redistribution;
- separation/lift-off.

Không tăng số chiều parameter space trước khi primary three-variable study khả thi.

**Điều kiện qua Gate:** mỗi variable có physical rationale, range khả thi và cách điều khiển/đo được.

---

## Gate 5 — Khóa Research Question và Hypothesis

Working RQ:

> Under what combinations of finite layer count, vacuum pressure, and bending severity does the Zhang et al. continuum layer-jamming beam model remain within predeclared output-specific model-form error tolerances relative to an explicit full-layer frictional-contact reference and physical experiments?

Working hypothesis:

> Khi số lớp tăng, M1 có xu hướng tiến gần finite-layer reference hơn; model-form error có thể tăng ở số lớp nhỏ, trạng thái bending/slip mạnh, hoặc khi contact-pressure redistribution hay separation trở nên quan trọng.

Hai nội dung này vẫn provisional đến khi Gate 1–4 hoàn tất.

**Điều kiện qua Gate:** RQ và hypothesis falsifiable và map trực tiếp tới measurable variables + outputs.

---

## Gate 6 — Định nghĩa Error Metrics và PREDECLARE Tolerances

Candidate relative errors:

~~~math
e_w = |w_M-w_R|/|w_R|
~~~

~~~math
e_K = |K_M-K_R|/|K_R|
~~~

~~~math
e_Q = |Q_{slip,M}-Q_{slip,R}|/|Q_{slip,R}|
~~~

Có thể cần absolute/normalized metrics khác khi denominator gần 0.

Workflow:

~~~text
define output
→ define error metric
→ justify acceptable error
→ freeze tolerance
→ sau đó mới xem final validation map
~~~

Không chọn 5% chỉ vì paper khác dùng 5%.

Tolerance có thể được justify từ:

- engineering use-case;
- experimental uncertainty;
- reference-model uncertainty;
- numerical uncertainty;
- sensitivity của engineering decision với prediction error.

**Điều kiện qua Gate:** tolerance + justification được timestamp/freeze trước final validation.

---

## Gate 7 — Khóa Parameter Space và Study Design

Xác định:

- range/levels của (n);
- range/levels của (p);
- load/curvature domain;
- geometry/material constants;
- friction calibration plan;
- calibration subset;
- validation subset;
- experimental subset.

Ưu tiên nondimensional groups khi có ý nghĩa vật lý, nhưng không ép nondimensionalization trước khi hiểu M1.

**Điều kiện qua Gate:** có run matrix hữu hạn, khả thi trong thời gian/tài nguyên MSc.

---

## Gate 8 — Implement và Verify M1

Thứ tự khuyên dùng:

~~~text
reproduce 1 published M1 case
→ reproduce stress/slip-state quantities
→ reproduce load-deflection case
→ test incremental convergence
→ freeze implementation
~~~

Không tune M1 bằng final validation cases.

**Điều kiện qua Gate:** implementation tái tạo được published M1 benchmark trong numerical error đã ghi nhận.

---

## Gate 9 — Xây dựng và Verify R

Thứ tự:

~~~text
single-layer sanity check
→ two-layer contact benchmark
→ frictionless / fully bonded limits
→ mesh convergence
→ contact convergence
→ finite-layer reference cases
→ freeze R
~~~

Dùng Narang/Caruso hoặc analytical limits khác đã verify làm debugging benchmark khi phù hợp.

**Điều kiện qua Gate:** R qua independent verification và numerical uncertainty đã được quantify.

---

## Gate 10 — Tạo Model-Form Error Surfaces

Với mỗi parameter point:

~~~text
run M1
run R
extract cùng output
compute error
compare với predeclared tolerance
classify VALID / INVALID theo từng output
~~~

Validity có thể output-specific:

~~~text
VALID cho deflection
INVALID cho slip-transition load
~~~

Không ép một universal boundary nếu evidence không hỗ trợ.

**Điều kiện qua Gate:** có preliminary validity/breakdown surfaces mà không thay tolerance post-hoc.

---

## Gate 11 — Giải thích VÌ SAO Breakdown

Dùng secondary quantities sau khi primary validity map đã có:

- slip-zone position;
- discrete interface slip;
- contact-pressure redistribution;
- local opening/separation;
- shear stress distributions;
- energy dissipation;
- boundary effects.

Mục tiêu:

> giải thích cơ chế vật lý gây validity loss, không chỉ báo error.

**Điều kiện qua Gate:** mỗi invalid region chính có mechanics explanation defensible.

---

## Gate 12 — Thiết kế Experiment để Test Boundary

Experiment phải chủ động gồm:

~~~text
predicted-valid points
VÀ
predicted-invalid points
VÀ nếu khả thi
near-boundary points
~~~

Không chỉ test case mà M1 đã đồng ý với R.

Experimental plan phải khóa:

- specimen geometry;
- number of layers;
- material;
- membrane/envelope;
- vacuum regulation;
- pressure measurement;
- loading fixture;
- force measurement;
- displacement/curvature measurement;
- slip observation nếu làm được;
- uncertainty;
- repeats;
- calibration vs validation specimens.

**Điều kiện qua Gate:** experiment có khả năng falsify predicted boundary.

---

## Gate 13 — Final Adjudication của Hypothesis

Sau experiment, quyết định:

- output nào còn valid;
- numerical boundary có survive experiment không;
- boundary có dịch chuyển không;
- M1 có fail vì đúng mechanism dự đoán không;
- có cần physics mới không;
- cần một hay nhiều output-specific validity maps.

Các kết quả khoa học hợp lệ:

~~~text
hypothesis supported
hypothesis partly supported
hypothesis rejected
boundary tồn tại nhưng khác dự đoán
không có simple monotonic boundary
~~~

Hypothesis bị bác bỏ không có nghĩa thesis thất bại nếu research design đúng.

---

# 10. Lộ trình học 80/20 sau khi đã lock M1

Chỉ học thứ implementation cần.

Priority chain:

~~~text
Euler-Bernoulli beam mechanics
→ shear force / bending moment / curvature
→ cross-sectional shear-stress distribution
→ Coulomb friction
→ stick / partial slip / full slip
→ layered-beam / partial-interaction mechanics
→ continuum approximation
→ incremental nonlinear solution
→ finite-element contact mechanics
→ model verification and validation
→ uncertainty and error metrics
~~~

Cosserat/generalized continuum mechanics nên học như theoretical lineage và comparison framework khi cần, nhưng không mặc định bắt buộc để implement M1.

---

# 11. Evidence-Audit Ladder cho mọi kết luận quan trọng

Dùng hierarchy:

| Level | Nguồn | Câu hỏi |
|---|---|---|
| L0 | summary / markdown verdict | Agent kết luận gì? |
| L1 | structured JSON | Field nào tạo verdict? |
| L2 | verification matrix | Paper nào hỗ trợ? |
| L3 | evidence JSON | Paper đã bị extract thành claim gì? |
| L4 | original PDF | Primary source có thật sự hỗ trợ extraction không? |
| L5 | prompt/raw/provenance | Model đã thấy input gì, prompt có bias không? |

Không dừng ở L0 với thesis-critical claim.

---

# 12. Quy tắc Stop/Search hiện tại

Broad search tiếp tục dừng sau D1-V009.

Chỉ reopen search nếu:

1. xuất hiện một paper cụ thể có vẻ thỏa missing kill-chain link;
2. forward citation/reference trực tiếp nêu một high-threat predecessor;
3. implementation phát hiện governing theory/model family mà các audit trước chưa cover;
4. mentor/reviewer đưa ra một prior-art challenge cụ thể có thể chuyển thành targeted search.

Không reopen broad search chỉ vì ngoài kia còn nhiều paper.

---

# 13. Current Source-of-Truth Files

Để biết trạng thái hiện tại, ưu tiên:

1. `outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.md`
2. `outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.md`
3. `docs/research_design/EXACT_MODEL_SELECTION.md`
4. `docs/research_design/M1_RESEARCH_ARCHITECTURE.md`
5. `docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md`
6. tài liệu roadmap này.

Các file như `docs/project/RESEARCH_STATE.md`, `docs/project/RESEARCH_LOG.md`, `docs/literature/LITERATURE_STRATEGY.md` vẫn hữu ích để đọc lịch sử nhưng không phải authority mới nhất.

---

# 14. Việc phải làm ngay tiếp theo

Nhiệm vụ khoa học kế tiếp là:

> **Tái dựng M1 hoàn chỉnh trước khi khóa R.**

Chưa nên khóa ngay:

- tolerance values;
- exact parameter ranges;
- experimental points;
- final hypothesis wording.

Trước tiên phải hiểu selected reduced model đủ sâu để biết:

- nó giữ physics nào;
- nó bỏ physics nào;
- assumption nào làm reduction khả thi;
- assumption nào có thể là breakdown mechanism;
- output nào thật sự tồn tại và đo được bằng experiment.

Sau đó mới khóa reference model và final research design.
