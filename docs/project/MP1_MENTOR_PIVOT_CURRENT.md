# MP1 — Mentor Pivot: Trạng thái hiện tại

> **Trạng thái:** `MP1-V002 ACTIVE`. Matrix hiện có **10 full-text papers**. Audit mới nhất vẫn trả `SUBSTANTIALLY_NARROWED` với `confidence = high`. Citation coverage vẫn **OPEN**.  
> **Nguyên tắc:** hướng luận văn D1/M1 hiện tại vẫn được bảo toàn và **chưa bị thay thế**. MP1 chỉ có thể thay thế D1/M1 sau khi hoàn tất falsification và có final adjudication rõ ràng.

## 1. Ý tưởng ban đầu từ mentor

Kiến trúc được đề xuất ban đầu:

```text
superelastic NiTi / metallic wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven syringe/piston pressure source
```

Ý tưởng ban đầu có nhiều lớp đóng góp tiềm năng: vật liệu NiTi, wire/fiber jamming, positive-pressure jamming, nguồn áp suất compact/onboard và khả năng thay đổi độ cứng uốn (variable bending stiffness).

Điểm quan trọng của toàn bộ MP1 là **không mặc định xem tổ hợp linh kiện là novelty**. Mỗi lớp phải bị tấn công bằng prior art.

## 2. Vì sao phải chạy MP1-V001?

MP1-V001 được thiết kế như một **core prior-art architecture audit** để trả lời câu hỏi:

> Trong kiến trúc mentor đề xuất, phần nào thực sự còn là câu hỏi khoa học mới và phần nào chỉ là tổ hợp những cơ chế đã có?

Các claim được đánh số C1-C8.

### Kết quả MP1-V001

```text
STATUS      = PIVOT_TO_MECHANICS_CORE
CONFIDENCE  = high
```

Canonical outputs:

- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md`

### Các claim bị đóng hoặc bị pre-empt mạnh

- **C1 — wire/fiber jamming for variable stiffness:** closed.
- **C2 — positive-pressure jamming for variable stiffness:** closed.
- **C3 — SMA + jamming in one variable-stiffness device:** closed.
- **C4 — onboard/compact pressure source for jamming:** closed.
- **C8 — SMA-driven syringe/piston powering jamming pressure:** substantially pre-empted; rủi ro rất cao trở thành implementation substitution.

Điều này có nghĩa: nếu chỉ nói “dùng NiTi thay nylon”, “dùng SMA thay motor”, “dùng syringe/piston thay pump” hoặc “đưa các cơ cấu đã biết vào một robot khác”, thì chưa đủ để tạo scientific novelty.

### Các claim còn mở sau MP1-V001

- **C5:** NiTi wires tự thân là frictional contacting/slipping bundle.
- **C6:** positive-pressure confinement trực tiếp lên một superelastic NiTi wire bundle.
- **C7:** coupling giữa NiTi superelasticity, inter-wire contact/slip/friction, pressure và bending stiffness.

Do đó MP1 không còn là một “component-combination project”. Nó chuyển sang một câu hỏi **mechanics** có thể falsify.

## 3. Mechanics core hình thành như thế nào?

Sau MP1-V001, câu hỏi được thu hẹp thành:

> Positive confinement pressure, inter-wire slip/friction và superelastic NiTi response tương tác như thế nào để quyết định bending stiffness và hysteresis của một NiTi wire bundle?

Dạng kill-test nghiêm ngặt hơn:

> Một superelastic NiTi wire bundle có tạo ra pressure- và curvature-dependent stick/slip, bending stiffness và hysteresis mà **không thể** được mô tả đầy đủ bởi một existing elastic-fiber/contact model chỉ bằng cách thay material modulus, friction coefficient và các material parameters hay không?

Nếu existing mechanics chỉ cần parameter substitution là đủ, phần mechanics còn lại của MP1 phải bị kill hoặc narrow tiếp.

## 4. MP1-V002 — targeted citation chase

MP1-V002 không mở lại broad keyword search. Mục tiêu là tấn công ba target còn sống:

### T1 — NiTi wire bundle có contact/slip/friction

```text
NiTi / Nitinol wires
→ bundle / strand / cable
→ wire-wire contact
→ friction / micro-slip / stick-slip
→ structural response / stiffness / hysteresis
```

### T2 — actively controlled confinement pressure

```text
actively varied positive / radial / transverse pressure
→ compress metallic/NiTi wire bundle
→ change wire-wire normal force
→ change friction / stick-slip
→ change bending / flexural stiffness
```

### T3 — coupling giữa NiTi phase transformation và contact mechanics

```text
NiTi superelasticity / martensitic transformation
+ inter-wire contact / slip / friction
+ confinement pressure
+ hysteresis
+ structural / bending stiffness
```

## 5. Kết quả audit mới nhất trên 10 full-text papers

Matrix hiện tại:

- `outputs/verification/MP1-V002/verification_matrix.json`
- `paper_count = 10`

Hai paper được thêm sau citation screening để đánh trực tiếp vào parameter-substitution kill test:

1. Reedlunn, Daly & Shaw (2013) — *Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses* — DOI `10.1016/j.ijsolstr.2013.03.015`.
2. Fang et al. (2019) — *Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application* — DOI `10.1016/j.engstruct.2019.01.049`.

Audit 10-paper mới nhất:

```text
STATUS      = SUBSTANTIALLY_NARROWED
CONFIDENCE  = high
```

Canonical output:

- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.md`

### T1 — CLOSED_BY_FULL_TEXT

Prior work đã chứng minh rõ:

- NiTi/Nitinol strands, ropes, cables và braided microfilaments có inter-wire/inter-filament contact;
- Coulomb friction, sliding/micro-slip và hysteresis tồn tại;
- phase transformation và friction cùng tham gia structural response;
- braid/cable architecture làm thay đổi effective stiffness, damping và transformation behavior.

Vì vậy:

```text
NiTi + inter-wire friction/slip + hysteresis
```

**không còn là novelty claim có thể bảo vệ.**

### T2 — OPEN_IN_CURRENT_FULL_TEXT_SET

Corpus đã có:

- passive contact pressure do helix geometry;
- axial-load-induced radial pressure;
- manufacturing/preforming pressure;
- fixed radial preload/confinement.

Nhưng chưa có full-text prior art trong matrix chứng minh chuỗi:

```text
actively varied confinement pressure
→ NiTi/metallic wire bundle
→ wire-wire normal force changes
→ friction / stick-slip changes
→ bending stiffness changes
```

T2 là phần quan trọng nhất còn mở.

### T3 — SUBSTANTIALLY_PREEMPTED

Prior work đã có nhiều phần của coupling:

- NiTi phase transformation;
- inter-wire friction;
- micro-slip;
- frictional heating;
- transformation-stress shift;
- hysteresis/damping;
- effective stiffness changes.

Phần còn thiếu không phải “NiTi + friction” mà là **active confinement pressure như independent control variable** và ảnh hưởng của nó lên bending mechanics.

## 6. Pressure classification bắt buộc

Mọi source liên quan đến pressure phải được phân loại:

```text
P1 = passive contact pressure
     sinh ra bởi helix geometry, axial load, bending hoặc deformation

P2 = fixed preload / fixed confinement
     áp đặt nhưng không thay đổi như một operational control variable

P3 = actively varied confinement pressure
     pressure là independent control variable trong vận hành
```

Chỉ **P3** là direct threat đối với mechanics core còn sống.

## 7. Parameter-substitution kill test hiện tại

Audit 10-paper trả:

```text
existing_elastic_fiber_model_appears_sufficient = false
niti_requires_distinct_constitutive_contact_coupling = false
evidence_status = insufficient
```

Diễn giải:

- Chưa có bằng chứng đủ mạnh để nói existing elastic-fiber/contact model chắc chắn là đủ.
- Cũng chưa có bằng chứng đủ mạnh để nói NiTi chắc chắn cần một new constitutive-contact coupling.
- Một số simplified/phenomenological NiTi cable models tái tạo được axial hysteresis mà không resolve full contact mechanics → đây là **substitution/reduced-order risk**.
- Ngược lại, braided/micro-cable studies cho thấy transformation, frictional heating và localized slip có các hiệu ứng không thể mô tả bằng một constant elastic modulus duy nhất.
- Nhưng các hiệu ứng đó chưa được chứng minh trong **quasi-static, pressure-controlled bending**.

Vì vậy mechanics core vẫn sống nhưng chưa được xác nhận novelty.

## 8. Câu hỏi khoa học còn sống ở checkpoint hiện tại

> Dưới actively varied positive radial/transverse confinement, pressure và curvature chi phối stick-slip transitions và bending stiffness của một superelastic NiTi wire bundle như thế nào, và các response này có thể được dự đoán đầy đủ bởi existing elastic-fiber/contact framework với substituted NiTi properties hay không?

Đây là câu hỏi phải tiếp tục bị falsify.

## 9. Citation coverage hiện tại

Tracker mới nhất:

- `outputs/verification/MP1-V002/citation_coverage.json`
- `outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md`

Trạng thái:

```text
required directions = 14
backward branches   = 8
forward branches    = 6

all_required_directions_screened = false
no_unresolved_high_threat_source = true
stop_condition_satisfied         = false
```

Sau khi re-init tracker trên audit 10-paper, các branch chưa được ghi lại trạng thái screening trong `citation_coverage.json`.

Backward anchors hiện gồm:

1. Carboni et al.
2. Vahidi et al.
3. Niu & Chen 2021.
4. Xin Liu thesis.
5. Tjahjanto et al.
6. braided NiTi microfilaments.
7. Silva et al. 2022.
8. Reedlunn et al. 2013.

Forward anchors vẫn là:

1. Bai et al. 2022.
2. Liu et al. 2021.
3. Zhang & Yao 2026.
4. Takashima et al. 2022.
5. Matsumoto et al. 2024.
6. Wang et al. 2024.

Các citation exports B01-B06/F01-F06 đã được thu thập và metadata screening đã chạy. Sau audit 10-paper, Niu 2021 và Reedlunn 2013 trở thành backward-priority anchors mới, tương ứng cần coverage bổ sung trước khi V002 có thể đóng.

## 10. Metadata screening đã thực hiện

Canonical screening:

- `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.json`
- `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.csv`
- `outputs/verification/MP1-V002/citation_screening/FULL_TEXT_SHORTLIST.csv`

Kết quả:

```text
input_csv_count              = 8
raw_record_count             = 187
deduplicated_candidate_count = 178

POTENTIAL_KILL_PAPER = 0
GET_FULL_TEXT        = 12
KEEP_METADATA        = 85
UNCERTAIN            = 0
EXCLUDE              = 81
```

Human review không yêu cầu tải cả 12 paper. Reedlunn 2013 và Fang 2019 được nâng lên full text để kiểm tra parameter-substitution risk và đã được ingest vào matrix 10-paper.

## 11. Guardrails hiện tại

Không được claim novelty chỉ vì:

- NiTi thay nylon/steel;
- wire thay fiber;
- SMA thay motor;
- syringe/piston thay pump;
- robot platform khác;
- generic NiTi cable hysteresis;
- passive radial contact pressure;
- fixed preload;
- compact integration.

Không được đánh đồng:

```text
NiTi wire-rope friction
==
pressure-controlled NiTi jamming
```

hoặc:

```text
passive/fixed radial pressure
==
actively varied confinement pressure
```

## 12. Hành động tiếp theo

Không mở lại broad search.

Workflow:

```text
resolve remaining required citation branches
→ write branch results into citation_coverage.json
→ run citation coverage --check
→ resolve any newly exposed high-threat source
→ satisfy protocol stop condition
→ final MP1-V002 adjudication
```

Nếu direct prior art cho P3 NiTi-bundle bending mechanics xuất hiện, hoặc existing elastic-fiber/contact model chỉ cần parameter substitution là đã giải thích đầy đủ response, MP1 phải bị kill hoặc narrow tiếp.

## 13. Canonical files cần đọc

Theo thứ tự:

1. `docs/project/MP1_MENTOR_PIVOT_CURRENT.md`
2. `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
3. `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`
4. `outputs/verification/MP1-V002/verification_matrix.json`
5. `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
6. `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.json`
7. `outputs/verification/MP1-V002/citation_coverage.json`
8. `docs/project/MP1-V002_CURRENT_HANDOFF.md`
9. `docs/project/MP1_MENTOR_PIVOT_TUTOR.md`

