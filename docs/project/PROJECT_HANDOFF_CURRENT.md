# PROJECT HANDOFF — CURRENT RESEARCH STATE

> **Purpose:** Fast handoff cho chat/agent mới.
> **Authority:** File này là current project entry point, nhưng thesis-critical claim phải drill down tới canonical JSON / evidence / PDF.
> **Updated:** 2026-09-25 sau final MP1-V002 adjudication và final D1/M1-vs-MP1 cross-direction adjudication.

---

# 1. Current selected thesis direction

```text
selected_direction = D1_M1
decision           = LOCK_WITH_FEASIBILITY_GATE
confidence         = medium
astra_required     = false
```

D1/M1 được chọn thay vì mentor-proposed MP1 sau khi **cả hai hướng** đã trải qua adversarial novelty/falsification workflows riêng.

Điều này là **conditional lock**, chưa phải irreversible commitment.

---

# 2. Current thesis title

## English

**Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams**

## Vietnamese

**Đánh giá thực nghiệm giới hạn hiệu lực và sự mất hiệu lực của mô hình liên tục cho dầm kẹt lớp chân không**

Đây là working title có authority cao nhất hiện tại vì xuất phát từ final cross-direction adjudication.

---

# 3. Research direction in one sentence

Luận văn hỏi:

> Trong miền layer count × vacuum pressure × quasi-static bending severity được khai báo trước, khi nào Zhang et al. continuum layer-jamming beam model đạt độ chính xác chấp nhận được so với một full-layer frictional-contact reference đã kiểm chứng và thí nghiệm độc lập, và contact/slip mechanism nào giải thích breakdown khi model thất bại?

Đây là **model-validity / model-form-error study**, không phải project phát minh một continuum model mới.

---

# 4. Core research architecture

Dùng shorthand:

```text
M → R → E
```

## M — Reduced / continuum model

**M1 — Zhang et al., _A continuum-based model for a layer jamming beam_**

DOI: `10.5194/ms-16-821-2025`

M1 là model cụ thể đang được đánh giá.

## R — Higher-fidelity numerical reference

Current scoped reference:

> **Full-layer explicit frictional-contact finite-element model**

R phải represent đủ các cơ chế cần để làm comparison có ý nghĩa:

- individual layers;
- normal contact;
- Coulomb friction;
- stick/slip;
- relevant separation/lift-off nếu xuất hiện;
- vacuum-pressure-related normal contact mechanics;
- verified numerical convergence.

R là higher-fidelity reference, không được gọi là “truth”.

## E — Experiment

Physical layer-jamming beam experiments dùng để test predicted-valid và predicted-invalid conditions.

Scientific logic:

```text
M1
→ compare against R
→ quantify output-specific model-form error
→ identify candidate validity boundary
→ test both sides experimentally
→ explain failure through contact/slip mechanics
```

---

# 5. Surviving contribution after D1 verification

Sau D1-V001 đến D1-V009, contribution còn defensible là:

> Một output-specific, uncertainty-aware validity/breakdown map của **một specified continuum model M1**, được đối chiếu với interface-resolving/full-layer reference và independent experiment, với tolerance được biện minh và fixed trước khi final validation/error results được dùng để kết luận.

Không được claim novelty cho:

- continuum modeling của layered media;
- Cosserat/generalized continuum mechanics;
- frictional interlayer slip;
- contact/opening mechanics;
- full-layer FE contact;
- pressure/friction/slip mechanics nói chung;
- một threshold/tolerance tự thân.

---

# 6. D1 novelty/falsification status

Historical sequence:

```text
D1 broad direction
→ D1-V001 PIVOT
→ validity-limit framing
→ D1-V002 ... D1-V007 narrowing
→ D1-V008 SURVIVES_FINAL_TARGET
→ D1-V009 SURVIVES_LATE_FOUND_TARGET
→ final novelty lock preserved
```

D1-V009 xác nhận các mechanics sau là old/prior-art và không được claim novel:

- equivalent/smeared layered continuum;
- Cosserat/generalized continuum;
- independent rotations/couple stresses;
- layer-bending stiffness in continuum;
- large-deformation layered continua;
- frictional/plastic interlayer slip;
- interface opening/delamination;
- FE implementation của các mechanics trên.

Broad D1 search vẫn stopped trừ khi có concrete new high-threat source.

---

# 7. Mentor-proposed MP1 branch — final disposition

Mentor alternative:

```text
superelastic NiTi / metallic wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven pressure source
```

MP1 không bị bỏ bằng intuition. Nó trải qua:

```text
MP1-V001
→ broad architecture pre-empted
→ pivot to mechanics core

MP1-V002
→ 16 full-text papers
→ Astra critique G01–G12
→ Stage 3 remediation
→ citation chase 15/15 directions
→ final V002 adjudication
```

Final MP1 result:

```text
protocol_outcome =
SURVIVES_TARGETED_CITATION_CHASE

confidence =
high

direct_kill_found =
false

citation_coverage_closed =
true
```

MP1 vì vậy là **scientifically viable** nhưng chỉ ở scope hẹp:

```text
active radial/transverse confinement pressure
×
NiTi bundle bending
→ contact/slip regime
→ phase transformation
→ hysteresis/stiffness
→ model discrimination vs H0b
```

Không được claim novelty cho NiTi, jamming, SMA+jamming, inter-wire friction, hysteresis hoặc active pressure tự thân.

Canonical:

- `outputs/verification/MP1-V002/FINAL_ADJUDICATION.json`
- `outputs/verification/MP1-V002/citation_coverage.json`

---

# 8. Why D1/M1 was selected over MP1

Final cross-direction adjudication:

```text
selected_direction = D1_M1
decision           = LOCK_WITH_FEASIBILITY_GATE
confidence         = medium
```

D1/M1 được ưu tiên vì:

1. một named model M1 đã khóa;
2. scientific question rõ và falsifiable hơn;
3. measurable beam-level outputs trực tiếp hơn;
4. lower identifiability burden;
5. apparatus/diagnostic burden thấp hơn;
6. model-discrimination path ít phụ thuộc một coupled regime khó đạt;
7. null/negative result vẫn có scientific value;
8. MSc implementation risk tractable hơn.

MP1 có key fatal unknowns:

- slip + stress-induced transformation có coexist trong accessible domain hay không;
- local transformation/slip có đo đủ tốt hay không;
- pressure-to-contact-force calibration có credible hay không;
- existing transformation-aware NiTi + Coulomb contact model H0b có thể đã đủ.

Canonical:

- `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json`
- `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.md`

---

# 9. Final research question

> **Across a declared range of layer count, vacuum pressure, and quasi-static bending severity, for which measurable outputs and operating conditions does the Zhang et al. continuum layer-jamming beam model meet predeclared, justified error tolerances against a verified full-layer frictional-contact reference and independent experiments, and which contact or slip mechanisms explain failures?**

Đây là final working RQ từ cross-direction adjudication.

---

# 10. Scientific hypothesis

> **M1's output-specific error will generally grow as finite-layer discreteness and slip or contact-pressure redistribution become important, yielding experimentally resolvable validity and breakdown regions. The predicted trend and boundary are testable and may be rejected.**

Hypothesis được phép bị bác bỏ mà thesis vẫn có thể có giá trị nếu validity domain được xác định đáng tin cậy.

---

# 11. What is locked now

```text
RESEARCH DOMAIN
=
vacuum layer-jamming beam model validity/breakdown

SELECTED DIRECTION
=
D1_M1

REDUCED MODEL M
=
Zhang et al. continuum layer-jamming beam model
DOI 10.5194/ms-16-821-2025

SCIENTIFIC ARCHITECTURE
=
M → R → E

DECISION
=
LOCK_WITH_FEASIBILITY_GATE

BROAD SEARCH
=
stopped unless concrete high-threat evidence appears
```

---

# 12. What is not yet fully locked

Phải được freeze trong feasibility/research-design stage:

- exact full-layer reference R;
- FE solver / 2D-vs-3D scope;
- contact formulation;
- friction law/calibration;
- vacuum-pressure representation;
- separation/lift-off treatment;
- primary output;
- error metric;
- justified tolerance;
- uncertainty budget;
- accepted/rejected pilot conditions;
- experimental apparatus/boundary sampling.

Không expand parameter space sớm.

---

# 13. Immediate next scientific gate

```text
D1/M1 boundary-resolvability pilot
```

Objective:

> Xác định liệu verified M1-vs-full-layer comparison có tạo được ít nhất một accepted condition và một rejected condition trong miền thực nghiệm khả thi, với uncertainty đủ nhỏ để classification có ý nghĩa hay không.

Required outputs:

1. reconstructed M1 equations, assumptions và published-case reproduction;
2. specified full-layer contact formulation + convergence/verification;
3. independent parameter-calibration record;
4. predeclared primary output;
5. error metric;
6. justified tolerance;
7. uncertainty budget;
8. predicted accepted condition;
9. predicted rejected condition;
10. pilot measurement plan/data đủ để test boundary.

Pass chỉ khi accepted/rejected contrast được uncertainty-resolve và apparatus có thể test cả hai.

---

# 14. First task inside the gate

Bước đầu tiên vẫn là:

> **Reconstruct M1 completely.**

User phải hiểu/implement được:

```text
physical assumptions
→ kinematics
→ force/moment balance
→ shear/contact stress
→ Coulomb condition
→ jammed / partial-slip / full-slip state
→ slip-zone boundary
→ bending response
→ load-deflection prediction
→ incremental update
→ candidate breakdown mechanisms
```

Chỉ sau khi M1 được reconstruct/reproduce mới freeze R.

---

# 15. Evidence hierarchy

```text
L0 — markdown summary / handoff
↓
L1 — canonical JSON verdict
↓
L2 — verification matrix
↓
L3 — evidence JSON
↓
L4 — original PDF
↓
L5 — prompt / raw output / provenance
```

Thesis-critical claim phải trace xuống evidence level phù hợp.

---

# 16. Search-stop rules

Không mở broad search chỉ vì “còn paper”.

Reopen targeted search khi:

1. có concrete new high-threat paper;
2. forward/reference chase nêu direct predecessor;
3. implementation lộ ra model/theory family chưa audit;
4. mentor/reviewer đưa prior-art challenge cụ thể.

MP1 broad search cũng closed theo V002 protocol; chỉ reopen nếu có lý do cụ thể.

---

# 17. Canonical authority order for a new chat

1. `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json`
2. `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.md`
3. `docs/project/PROJECT_HANDOFF_CURRENT.md`
4. `docs/project/RESEARCH_LOG.md`
5. `docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md`
6. `docs/research_design/EXACT_MODEL_SELECTION.md`
7. `outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.json`
8. `outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json`
9. `outputs/verification/MP1-V002/FINAL_ADJUDICATION.json`
10. `outputs/verification/MP1-V002/citation_coverage.json`

Historical Stage 3 MP1 summaries không được dùng để override canonical final files.

---

# 18. Prompt for the next chat/agent

```text
Continue the mechanical MSc project from docs/project/PROJECT_HANDOFF_CURRENT.md.

Canonical current state:
- selected_direction = D1_M1
- decision = LOCK_WITH_FEASIBILITY_GATE
- confidence = medium
- mentor-proposed MP1 survived MP1-V002 but was not selected
- MP1 citation coverage is closed
- no broad literature search is currently required

Current thesis title:
Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams

Immediate gate:
D1/M1 boundary-resolvability pilot

Start by reconstructing M1 completely from the original Zhang et al. paper and repository evidence. Do not freeze the full-layer reference R until M1 has been reproduced. Distinguish verified evidence, inference, and hypothesis, and cite thesis-critical claims to concrete source files/papers.
```

---

# 19. Current bottom line

```text
MENTOR MP1:
scientifically viable
but not selected
→ archived alternative

CURRENT THESIS:
D1/M1 model-validity/breakdown study

DECISION:
LOCK_WITH_FEASIBILITY_GATE

NEXT:
reconstruct M1
→ verify/reproduce M1
→ freeze R
→ predeclare output/metric/tolerance/uncertainty
→ boundary-resolvability pilot
→ if PASS: commit thesis execution
→ if FAIL: narrow/pivot
```
