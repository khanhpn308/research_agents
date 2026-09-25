# MP1 — Mentor Pivot: Trạng thái hiện tại tại HEAD

> **Trạng thái MP1:** `MP1-V002 CLOSED`.
> **Final MP1-V002 outcome:** `SURVIVES_TARGETED_CITATION_CHASE`, `confidence = high`, `direct_kill_found = false`.
> **Citation coverage:** `15/15 required directions screened` (`backward = 9/9`, `forward = 6/6`), `search_cutoff_date = 2026-09-25`, `stop_condition.satisfied = true`.
> **Final cross-direction decision:** `selected_direction = D1_M1`, `decision = LOCK_WITH_FEASIBILITY_GATE`, `confidence = medium`.
> **Disposition của MP1:** không bị bác bỏ về mặt khoa học; được lưu như một **viable alternative**, nhưng **không được chọn** làm hướng luận văn hiện tại.
> **Current MSc direction:** D1/M1 — đánh giá miền hiệu lực/mất hiệu lực của mô hình continuum layer-jamming của Zhang et al. bằng full-layer frictional-contact reference và thí nghiệm.
> **Immediate next gate:** `D1/M1 boundary-resolvability pilot`.

---

## 1. Ý tưởng mentor và quyết định phương pháp luận ban đầu

Mentor đề xuất một hướng thay thế:

```text
superelastic NiTi / metallic wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven syringe/piston pressure source
```

Quyết định của workflow không phải là bác bỏ ý tưởng mentor theo trực giác. MP1 được mở như một **alternative research direction under adversarial novelty audit** và phải trải qua cùng nguyên tắc:

```text
DO NOT DEFEND THE IDEA
→ decompose claims
→ search direct prior art
→ ingest full text
→ test kill conditions
→ close citation coverage
→ final adjudication
```

D1/M1 được giữ nguyên làm baseline cho đến khi MP1 có đủ bằng chứng để thay thế.

---

## 2. MP1-V001 — Broad architecture bị loại khỏi novelty claim

MP1-V001 phân rã architecture thành C1–C8.

Kết quả:

```text
STATUS      = PIVOT_TO_MECHANICS_CORE
CONFIDENCE  = high
```

Các novelty claim ở cấp component/system đã bị đóng hoặc substantially pre-empted:

- **C1 — wire/fiber jamming:** prior art trực tiếp đã tồn tại.
- **C2 — positive-pressure jamming:** prior art trực tiếp đã tồn tại.
- **C3 — SMA + jamming coexistence:** prior art trực tiếp đã tồn tại.
- **C4 — compact/onboard pressure source:** prior art trực tiếp đã tồn tại.
- **C8 — SMA-driven syringe/piston powering jamming:** implementation substitution, không phải scientific core đủ mạnh.

Từ đây MP1 chỉ còn quyền tồn tại nếu mechanics core vượt qua kiểm chứng.

---

## 3. MP1-V002 — Mechanics core sau Stage 1–3

### Stage 1 — Evidence packets

Gemini tạo 11 evidence packets truy vết cơ học tại:

`outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/`

### Stage 2 — Astra adversarial critique

GPT-5.6 Astra thực hiện phản biện đối kháng và nêu 12 lỗ hổng G01–G12:

`docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md`

### Stage 3 — Scientific remediation & consensus

Gemini hoàn tất:

- 11 worker reports W01–W11;
- ma trận remediation G01–G12;
- báo cáo khoa học tổng hợp 24 chương;
- reconciliation ma trận **16 full-text papers**;
- đồng bộ Stage 3 handoff.

Canonical Stage 3 deliverables:

- `docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md`
- `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md`
- `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/`

---

## 4. Kết quả khoa học quan trọng đã được sửa sau Astra

### 4.1. H0a / H0b / H1

- **H0a — Naive Elastic Substitution:** `REFUTED` trong miền có chuyển pha. Không thể mô tả NiTi bằng một `E = const` đơn giản khi stress-induced transformation hoạt động.
- **H0b — Existing transformation-aware NiTi constitutive + Coulomb contact:** `NOT FALSIFIED`. Đây là đối thủ khoa học mạnh nhất của MP1.
- **H1 — Novel distinct coupling mechanics:** `INSUFFICIENT EVIDENCE`. Không được suy từ việc H0a thất bại sang kết luận cần một constitutive law mới.

### 4.2. P3 active pressure

Áp suất giam giữ chủ động biến thiên `p(t)` là **experimental control protocol / boundary condition**, không tự động là một nguyên lý cơ học mới.

### 4.3. Coexistence-domain risk

MP1 chỉ có giá trị cơ học đặc thù nếu thí nghiệm đi vào miền mà:

```text
inter-wire slip
AND
stress-induced NiTi transformation
```

cùng tồn tại và có thể đo/phân biệt.

Nếu NiTi vẫn ở Austenite đàn hồi trong miền uốn thực tế, bài toán thoái hóa về elastic-wire jamming. Nếu chỉ có transformation mà không có meaningful slip, bài toán quay về NiTi cable mechanics đã biết.

### 4.4. Identifiability risk

Global `M-κ` loops không đủ để phân biệt chắc chắn:

```text
friction
vs
phase transformation
vs
contact-force change
vs
temperature/history
```

Do đó MP1 cần local diagnostics (ví dụ DIC/FBG, phase-sensitive/thermal evidence, slip evidence), locked parameters và calibration độc lập.

---

## 5. Stage 4 — Citation-chase closure sau Stage 3

Stage 3 từng dừng với:

```text
stop_condition_satisfied = false
B11/B12 unresolved
search_cutoff_date = NOT SET
```

Trạng thái đó đã được supersede.

Hai nhánh cuối đã được đóng:

- **B11 — Kang et al. 2020:** 22 backward references screened.
- **B12 — Barsi, Carboni & Lacarbonara 2024/2025 lineage:** 46 backward references screened.

Tổng B11+B12:

```text
raw records = 68
unique records = 67
```

Không phát hiện direct kill mới cho chuỗi:

```text
actively varied confinement pressure
→ NiTi wire bundle
→ inter-wire normal force
→ stick/partial-slip/full-slip
→ bending stiffness / hysteresis
```

Canonical coverage hiện tại:

```text
backward = 9/9
forward  = 6/6
total    = 15/15

all_required_directions_screened = true
no_unresolved_high_threat_source = true
stop_condition.satisfied         = true
search_cutoff_date               = 2026-09-25
```

Nguồn:

- `outputs/verification/MP1-V002/citation_coverage.json`
- `outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md`

---

## 6. Stage 5 — Final MP1-V002 adjudication

Final adjudication được chạy bằng:

```text
model  = gpt-6-sol
effort = high
```

Canonical:

- `outputs/verification/MP1-V002/FINAL_ADJUDICATION.json`
- `outputs/verification/MP1-V002/FINAL_ADJUDICATION.md`

Kết quả:

```text
protocol_outcome =
SURVIVES_TARGETED_CITATION_CHASE

confidence =
high

citation_coverage_closed =
true

direct_kill_found =
false

msc_topic_readiness =
READY_FOR_CROSS_DIRECTION_COMPARISON

astra_escalation_required =
false
```

Điều này **không chứng minh universal novelty**. Nó chỉ chứng minh rằng trong protocol V002 đã đóng, không tìm thấy direct kill và một câu hỏi cơ học hẹp còn defensible.

Surviving MP1 contribution:

```text
independently varied radial/transverse confinement pressure
×
superelastic NiTi wire bundle under bending
→ pressure-dependent contact
→ stick / partial slip / full slip
→ transformation distribution
→ hysteresis + tangent/effective bending stiffness
→ model discrimination against H0b
```

Working title của MP1 ở thời điểm final V002:

> **Modeling and Experimental Characterization of Pressure-Controlled Bending Mechanics in Superelastic NiTi Wire Bundles**

MP1 đã đủ điều kiện để được đem so với D1/M1, nhưng chưa tự động trở thành thesis direction.

---

## 7. Stage 6 — Final cross-direction adjudication: D1/M1 vs MP1

Canonical:

- `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json`
- `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.md`

Kết quả:

```text
selected_direction = D1_M1
decision           = LOCK_WITH_FEASIBILITY_GATE
confidence         = medium
astra_required     = false
```

### Vì sao D1/M1 được chọn?

Final comparison không đánh giá theo “cái nào nghe mới hơn”, mà theo scientific defensibility + falsifiability + execution feasibility + negative-result value + publication logic.

Các lợi thế chính của D1/M1 tại trạng thái hiện tại:

1. **Scientific question rõ hơn:** một model cụ thể M1 đã được khóa; câu hỏi là model đúng ở đâu và breakdown ở đâu.
2. **Baseline rõ hơn:** Zhang et al. continuum model là object cụ thể; MP1 vẫn phải freeze model pair cho specimen/loading protocol.
3. **Identifiability tốt hơn:** D1/M1 vẫn có friction/contact confounders nhưng ít tầng coupling hơn MP1.
4. **Experimental measurability tốt hơn:** beam-level load/deflection/stiffness dễ đo hơn local NiTi transformation + inter-wire slip.
5. **Apparatus burden thấp hơn:** vacuum beam bending rig + contact FE dễ kiểm soát hơn pressure-controlled NiTi bundle + material-state control + local diagnostics.
6. **Critical regime dễ tiếp cận hơn:** M1 đã chứa slip transitions; MP1 còn chưa chứng minh được overlap của slip và stress-induced transformation.
7. **Negative/null result vẫn có giá trị:** nếu M1 valid trên miền rộng, đó vẫn là validity-domain result; nếu H0b dự đoán tốt MP1, distinct MP1 mechanics claim bị mất.
8. **MSc execution risk thấp hơn:** D1/M1 vẫn khó nhưng tractable hơn trong thời gian luận văn.

MP1 vì vậy được giữ như một **scientifically viable alternative**, không phải một ý tưởng “bị bác bỏ vì của mentor”.

---

## 8. Hướng luận văn hiện được chọn có điều kiện

Current selected direction:

> **Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams**

Tiếng Việt:

> **Đánh giá thực nghiệm giới hạn hiệu lực và sự mất hiệu lực của mô hình liên tục cho dầm kẹt lớp chân không**

Final research question:

> Across a declared range of layer count, vacuum pressure, and quasi-static bending severity, for which measurable outputs and operating conditions does the Zhang et al. continuum layer-jamming beam model meet predeclared, justified error tolerances against a verified full-layer frictional-contact reference and independent experiments, and which contact or slip mechanisms explain failures?

Scientific hypothesis:

> M1's output-specific error will generally grow as finite-layer discreteness and slip or contact-pressure redistribution become important, yielding experimentally resolvable validity and breakdown regions. The predicted trend and boundary are testable and may be rejected.

---

## 9. D1/M1 chưa được lock vô điều kiện

Final decision là:

```text
LOCK_WITH_FEASIBILITY_GATE
```

Gate tiếp theo:

```text
D1/M1 boundary-resolvability pilot
```

Phải chứng minh:

- reconstruct M1 và reproduce được published case;
- full-layer reference R đủ credible;
- primary output, error metric, tolerance và uncertainty budget được predeclare;
- có ít nhất một experimentally accessible accepted condition;
- có ít nhất một experimentally accessible rejected condition;
- numerical/measurement uncertainty nhỏ hơn classification margin.

Nếu gate thất bại, D1/M1 phải narrow hoặc pivot; không được bảo vệ bằng mọi giá.

---

## 10. Thông điệp dùng khi trao đổi với mentor

Lập luận cần trình bày là:

> Mentor-proposed MP1 đã được kiểm chứng nghiêm túc, không bị “loại bằng cảm giác”. Nó đã sống sót qua 16 full-text papers, targeted citation chase 15/15 directions, Astra critique/remediation và final MP1 adjudication. Tuy nhiên, khi so trực tiếp với D1/M1, MP1 có execution/identifiability risk cao hơn vì cần chứng minh một miền cùng tồn tại slip + NiTi transformation và cần local diagnostics để phân biệt cơ chế khỏi H0b. D1/M1 có object/model cụ thể hơn, measurement burden thấp hơn và negative result vẫn có giá trị khoa học. Vì vậy D1/M1 được chọn **có điều kiện**, không phải tuyệt đối; nó còn phải vượt boundary-resolvability pilot.

Đây là lý do khoa học và quản trị rủi ro nghiên cứu, không phải lựa chọn theo sở thích cá nhân.

---

## 11. Canonical authority order

Đối với trạng thái hiện tại, ưu tiên đọc:

1. `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json`
2. `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.md`
3. `outputs/verification/MP1-V002/FINAL_ADJUDICATION.json`
4. `outputs/verification/MP1-V002/citation_coverage.json`
5. `outputs/verification/MP1-V002/verification_matrix.json`
6. `docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md`
7. `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md`
8. `docs/project/PROJECT_HANDOFF_CURRENT.md`
9. `docs/project/RESEARCH_LOG.md`

Stage 3 reports vẫn có giá trị lịch sử và evidence synthesis, nhưng các status token cũ như `stop_condition_satisfied = false` đã bị canonical files mới hơn supersede.
