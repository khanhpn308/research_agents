# RESEARCH_LOG.md

## Dòng thời gian quyết định nghiên cứu (Research Decision Timeline)

> File này ghi lại **vì sao hướng nghiên cứu thay đổi**, không chỉ ghi danh sách task đã thực hiện.
> Code, schema, filename, key và status token giữ English; phần giải thích/decision viết tiếng Việt.

## Phase 0 — Định hướng rộng

Research domain ban đầu được thu hẹp về:

- soft robotics;
- variable stiffness;
- soft grippers;
- continuum robots;
- jamming-based stiffening;
- mechanics + experimental validation.

## Phase 1 — Discovery corpus

Xây dựng seed corpus 54 papers.

Đã hoàn tất:

- paper registry;
- screening;
- evidence extraction;
- validation;
- literature matrix;
- 9 reasoning batches;
- batch synthesis.

## Phase 2 — Candidate generation

GPT-5.6 Sol tạo năm candidate research directions.

D1 được chọn provisional.

## Phase 3 — Adversarial critique

Gemini adversarial critic đánh giá các candidate directions.

Shortlist:

- D1;
- D2.

Recommended:

- D1.

## Phase 4 — Final adjudication cho D1

GPT-5.6 Sol so sánh D1 và D2.

Kết quả:

```text
selected: D1
decision: select_with_revision
confidence: medium
astra_required: false
```

Working title:

> *Modeling and Experimental Characterization of Interlayer Slip and Bending Stiffness in Vacuum Layer-Jamming Beams*

## Phase 5 — External verification bắt đầu

Project ngừng coi discovery corpus 54 papers là bằng chứng đủ cho novelty.

Một verification corpus riêng được tạo.

Round:

- `D1-V001`.

## Phase 6 — D1-V001

Added/screened:

- Narang et al. 2018;
- Caruso et al. 2023;
- Atakuru et al. 2024.

Built:

- verification matrix;
- direction verification output.

## Phase 7 — Broad D1 bị falsify

Verification result:

```text
verdict: PIVOT
confidence: high
```

Nguyên nhân:

- pressure–friction–slip mechanics đã được model;
- bending-stiffness evolution đã được model;
- slip transitions đã được characterize;
- experimental validation đã tồn tại;
- hysteresis / energy dissipation đã được nghiên cứu.

Strongest conflicts:

- Narang 2018;
- Caruso 2023.

## Phase 8 — P1 provisional pivot

Hướng provisional:

> *Validity Limits of a Homogenized Slip Model for High-Layer-Count Vacuum-Jammed Beams*

Trạng thái:

- provisional;
- chưa novelty-verified;
- phải bị attack, không được defend.

## Phase 9 — Các threat mới trong D1 lineage

Forward-citation / Scholar search phát hiện thêm:

1. Zhang et al. 2025 — *A continuum-based model for a layer jamming beam*.
2. Zhang et al. 2025 — *Toward a deeper understanding of layer jamming structures*.
3. Fan et al. 2026 — *Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots*.

D1 tiếp tục được audit qua các verification rounds sau đó. Hướng D1/M1 được bảo toàn làm thesis baseline trong khi một mentor-proposed alternative được mở riêng để falsify.

---

# Mentor Pivot lineage — MP1

## Phase 10 — Mentor đề xuất một architecture mới

Một alternative direction được mentor đề xuất:

```text
superelastic NiTi / metallic wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven syringe/piston pressure source
```

Quyết định quan trọng:

> Không thay D1/M1 ngay. Mở MP1 như một **alternative research direction under adversarial novelty audit**.

Lý do: architecture có vẻ mới ở cấp tổ hợp, nhưng từng component có thể đã có prior art.

Canonical entry points:

- `docs/project/MENTOR_PIVOT_STATUS.md`
- `docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md`

## Phase 11 — MP1-V001: attack broad architecture

MP1-V001 đặt C1-C8 để tách architecture thành các claim độc lập.

Kết quả:

```text
STATUS      = PIVOT_TO_MECHANICS_CORE
CONFIDENCE  = high
```

### Vì sao broad architecture không còn defensible?

Prior art đã đóng:

- C1 — wire/fiber jamming;
- C2 — positive-pressure jamming;
- C3 — SMA + jamming;
- C4 — compact/onboard pressure source.

C8 — SMA-driven syringe/piston powering jamming — substantially pre-empted và có nguy cơ chỉ là implementation substitution.

### Cái gì còn sống?

C5-C7 còn mở trong supplied corpus:

- NiTi wires tự thân làm frictional contacting/slipping medium;
- positive pressure trực tiếp confine NiTi wire bundle;
- coupling giữa NiTi superelasticity, inter-wire slip/friction, pressure và bending stiffness.

**Decision:** bỏ novelty kiểu “ghép component”; chuyển MP1 sang mechanics core.

Canonical result:

- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`.

## Phase 12 — Mechanics core được định nghĩa

Câu hỏi chuyển thành:

> Positive confining pressure, inter-wire slip/friction và superelastic NiTi response tương tác như thế nào để quyết định bending stiffness và hysteresis của NiTi wire bundle?

Kill test:

> Nếu existing elastic-fiber/contact mechanics chỉ cần thay modulus, friction và material parameters là đủ, MP1 mechanics core phải bị kill/narrow.

## Phase 13 — MP1-V002: targeted citation chasing

Không quay lại broad search.

Ba target:

- **T1:** NiTi contacting/slipping frictional bundle.
- **T2:** active pressure confinement của metallic/NiTi wire bundle.
- **T3:** coupling giữa NiTi transformation + wire contact/slip + pressure + stiffness.

Protocol:

- `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`.

## Phase 14 — MP1-V002 initial 8-paper full-text audit

8 full-text papers về NiTi/cable/wire-rope/contact mechanics được ingest.

Interim result:

```text
STATUS      = SUBSTANTIALLY_NARROWED
CONFIDENCE  = high
```

Kết luận ban đầu:

- T1 gần như đóng: NiTi + inter-wire friction/slip/hysteresis đã có prior art.
- T2 còn mở: chưa thấy actively varied confinement pressure điều khiển NiTi bundle stiffness.
- T3 bị narrow: NiTi transformation + friction đã biết; active pressure coupling chưa được chứng minh.

## Phase 15 — Citation coverage và metadata screening

Citation chase thu thập 8 CSV exports:

```text
raw records = 187
deduplicated candidates = 178
```

Metadata triage:

```text
POTENTIAL_KILL_PAPER = 0
GET_FULL_TEXT        = 12
KEEP_METADATA        = 85
UNCERTAIN            = 0
EXCLUDE              = 81
```

Human review quyết định không tải hàng loạt 12 papers.

Hai paper được promote vì đánh trực tiếp vào parameter-substitution kill test:

- Reedlunn, Daly & Shaw 2013.
- Fang et al. 2019.

## Phase 16 — Matrix tăng từ 8 lên 10 full-text papers

Hai paper mới được register, screen, ingest và build vào:

- `outputs/verification/MP1-V002/verification_matrix.json`.

```text
paper_count = 10
```

## Phase 17 — MP1-V002 audit lại trên 10-paper matrix

Latest result:

```text
STATUS      = SUBSTANTIALLY_NARROWED
CONFIDENCE  = high
```

### T1

```text
status = closed_by_full_text
```

NiTi/Nitinol frictional cable/strand mechanics là prior art.

### T2

```text
status = open_in_current_full_text_set
```

Chưa thấy:

```text
P3 actively varied confinement
→ NiTi wire bundle
→ variable normal force
→ stick-slip transition
→ pressure-dependent bending stiffness
```

### T3

```text
status = substantially_preempted
```

NiTi transformation + inter-wire friction/hysteresis đã biết. Phần còn lại phải xoay quanh active pressure-controlled bending mechanics.

## Phase 18 — Parameter-substitution test chưa có verdict

Latest audit:

```text
existing_elastic_fiber_model_appears_sufficient = false
niti_requires_distinct_constitutive_contact_coupling = false
evidence_status = insufficient
```

Điều này không có nghĩa cả hai giả thuyết đều sai.

Nó có nghĩa:

- chưa đủ bằng chứng để kill bằng parameter substitution;
- cũng chưa đủ bằng chứng để claim một distinct NiTi constitutive-contact model;
- direct baseline model comparison vẫn là bài kiểm tra bắt buộc.

## Phase 19 — Current mechanics core

Surviving question:

> Under actively varied positive radial/transverse confinement, pressure và curvature govern stick-slip transitions và bending stiffness của superelastic NiTi wire bundle như thế nào, và existing elastic-fiber/contact framework với substituted NiTi properties có predict được response đó hay không?

Đây là mechanics core hiện tại.

## Phase 20 — Citation coverage được re-init sau audit 10-paper

Latest tracker:

```text
required directions = 14
backward required    = 8
forward required     = 6

all_required_directions_screened = false
no_unresolved_high_threat_source = true
stop_condition_satisfied         = false
```

Hai backward-priority anchors mới so với coverage set cũ:

- Niu & Chen 2021 — DOI `10.3390/app112110032`.
- Reedlunn et al. 2013 — DOI `10.1016/j.ijsolstr.2013.03.015`.

Current action:

```text
screen/resolve remaining required citation branches
→ populate citation_coverage.json
→ citation_coverage --check
→ final MP1-V002 adjudication
```

## Phase 21 — Current checkpoint

As of 2026-09-25:

- D1/M1 vẫn được bảo toàn;
- MP1 chưa được chấp nhận làm thesis direction;
- broad architecture novelty đã bị loại bỏ;
- T1 đã đóng;
- T3 bị pre-empt phần lớn;
- T2/P3 pressure-controlled NiTi-bundle bending mechanics vẫn mở trong current full-text set;
- parameter-substitution kill test vẫn unresolved;
- citation coverage chưa đạt stop condition.

Không được bắt đầu MP1-V003 chỉ để cứu novelty. Chỉ tiếp tục nếu V002 coverage hoặc final adjudication yêu cầu.

## Phase 22 — Stage 3 Scientific Remediation & Consensus at HEAD (2026-09-25)

**Mô hình:** Gemini 3.8 Flash High (Stage 3 Remediation Engine)
**Tập tài liệu kiểm chứng:** 16 bài báo toàn văn PDF tại commit HEAD (`outputs/verification/MP1-V002/verification_matrix.json`)
**Audit canonical:** `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json` (16 papers)

### Các kết quả then chốt đạt được trong Stage 3:
1. **Reconciliation Hiện trạng Repository:** Xác nhận quy mô 16 bài báo tại HEAD; chấm dứt sự mập mờ giữa snapshot 10 bài cũ và trạng thái thực tế.
2. **Khắc phục 12 Lỗ hổng Trọng yếu của Astra (G01–G12):** Hoàn thành ma trận đối soát tại `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md` với 100% phê bình được kiểm chứng và hiệu chỉnh dứt điểm.
3. **Tái cấu trúc Ba Tầng Giả Thuyết H0/H1:** Bác bỏ mô hình thay thế đàn hồi đơn giản H0a (`REFUTED`); giữ nguyên giả thuyết khung lý thuyết NiTi cấu thành + tiếp xúc Coulomb hiện hữu H0b (`NOT FALSIFIED`); xác nhận chưa có bằng chứng cho lý thuyết ghép cặp vi mô mới H1 (`INSUFFICIENT`).
4. **Hạ cấp Phân loại Áp suất P3:** Xác định P3 (áp suất chủ động biến thiên) là giao thức điều khiển thực nghiệm, không phải nguyên lý cơ học mới; các phương trình tiếp xúc hiện hữu tự nhiên tiếp nhận $p(t)$.
5. **Đính chính Dữ liệu Lịch sử:** Sửa chữa triệt để sai sót Carboni 2015 (S2a là cáp thép thuần ma sát; S1a mới là NiTi chịu kéo-uốn kết hợp); hiệu chỉnh bảo thủ Reedlunn 2013 và Fang 2019.
6. **Ban hành Báo cáo Khoa học Tổng thể 24 Chương:** Hoàn thành `docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md` cùng 11 báo cáo worker chuyên sâu `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/` (W01–W11).

## File dùng để truy ngược toàn bộ mentor-pivot lineage

- `docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md`
- `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md`
- `docs/project/MP1_MENTOR_PIVOT_CURRENT.md`
- `docs/project/MP1-V002_CURRENT_HANDOFF.md`
- `docs/project/MP1_MENTOR_PIVOT_TUTOR.md`


## Phase 23 — Citation Coverage Closure (2026-09-25)

Sau Stage 3, hai backward branches cuối của MP1-V002 được xử lý:

- B11 — Kang et al. 2020: 22 references;
- B12 — Barsi, Carboni & Lacarbonara: 46 references.

Kết quả:

```text
backward = 9/9
forward  = 6/6
total    = 15/15

search_cutoff_date               = 2026-09-25
all_required_directions_screened = true
no_unresolved_high_threat_source = true
stop_condition.satisfied         = true
```

Không phát hiện direct prior-art kill mới cho active-pressure NiTi-bundle bending chain.

Quyết định:

> Dừng MP1 citation chase. Không mở broad search thêm.

Canonical:

- `outputs/verification/MP1-V002/citation_coverage.json`
- `outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md`

## Phase 24 — Final MP1-V002 Adjudication (2026-09-25)

Final adjudication chạy bằng:

```text
model  = gpt-6-sol
effort = high
```

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

Decision meaning:

- MP1 không bị falsify trong V002 protocol;
- không được diễn giải thành universal novelty;
- surviving contribution chỉ còn là pressure-controlled NiTi-bundle bending **model discrimination**;
- H0b vẫn là competitor chưa bị bác bỏ;
- MP1 đủ điều kiện để so với D1/M1, chưa đủ để tự lock thesis.

Canonical:

- `outputs/verification/MP1-V002/FINAL_ADJUDICATION.json`
- `outputs/verification/MP1-V002/FINAL_ADJUDICATION.md`

## Phase 25 — Final Cross-Direction Adjudication: D1/M1 vs MP1 (2026-09-25)

Hai hướng đã sống sót các falsification workflow riêng được so trực tiếp.

Kết quả:

```text
selected_direction = D1_M1
decision           = LOCK_WITH_FEASIBILITY_GATE
confidence         = medium
astra_required     = false
```

Lý do D1/M1 được ưu tiên:

- scientific object/model cụ thể hơn;
- baseline M1 đã khóa;
- output dễ đo hơn;
- identifiability tốt hơn;
- apparatus/instrumentation burden thấp hơn;
- critical regime dễ tiếp cận hơn;
- negative/null result vẫn tạo validity-domain evidence;
- MSc execution risk thấp hơn MP1.

MP1 vẫn được lưu như một `viable alternative`, không bị gán nhãn scientifically invalid.

Canonical:

- `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json`
- `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.md`

## Phase 26 — D1/M1 Conditional Topic Lock (Current HEAD)

Current working title:

> *Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams*

Tiếng Việt:

> *Đánh giá thực nghiệm giới hạn hiệu lực và sự mất hiệu lực của mô hình liên tục cho dầm kẹt lớp chân không*

Current state:

```text
selected_direction = D1_M1
lock_state         = LOCK_WITH_FEASIBILITY_GATE
```

Immediate next gate:

```text
D1/M1 boundary-resolvability pilot
```

Gate phải tạo được:

1. M1 reconstruction + published-case reproduction;
2. verified full-layer frictional-contact reference;
3. predeclared primary output, error metric, justified tolerance và uncertainty budget;
4. ít nhất một accessible accepted condition;
5. ít nhất một accessible rejected condition;
6. measurement precision đủ để test classification.

Nếu không có accepted/rejected contrast được uncertainty-resolve trong apparatus domain, D1/M1 phải narrow hoặc pivot.

### Current principle

Không broad search thêm cho MP1 hoặc D1 chỉ để tăng số paper.

Từ đây workflow chuyển từ **novelty/falsification selection** sang **feasibility + mechanics execution**.


## Phase 27 — Mentor-defense dual-track planning and audit hardening (2026-09-25/26)

Mục tiêu công việc được tách thành hai nhánh độc lập trước khi làm mentor-facing comparison:

```text
D1 = reconstruct + falsify novelty lineage
MP1 = reconstruct + falsify mentor-direction lineage
comparison = defer until both branches reach controlled checkpoints
```

D1 Master Plan trải qua nhiều vòng audit/remediation và chốt ở Plan V6 với worker contracts, ownership, hard-gate routing, failure routing và canonical package hợp lệ.

Quy tắc path D1:

```text
Plan authority = V6
control root   = outputs/execution/D1/
worker root    = outputs/d1_execution/V4/
```

`V4` là historical execution namespace được V6 giữ lại; không migrate/rename.

## Phase 28 — D1 execution W01-W08 complete (2026-09-26)

D1 execution preflight PASS, sau đó W01-W08 được chạy có kiểm soát.

Đến W08:

```text
W01-W08 = COMPLETE
W08 assigned papers = 19
W08 processed       = 19
QA                   = PASS
direct threat candidates = 1
partial overlap          = 8
reconciliation candidates = 3
retrospective threshold risks = 4
model-form ambiguities = 13
contradictions = 0
search reopened = false
```

Canonical latest:

- `outputs/d1_execution/V4/W08/D1_PAPER_EVIDENCE_SHARD_W08.jsonl`
- `outputs/d1_execution/V4/W08/W08_EXECUTION_RECEIPT.json`

Next D1 dependency:

```text
W09 / S4 CROSS-WORKER RECONCILIATION
MODEL = GPT-6 Sol High
```

W09 phải hợp nhất W03-W08 nhưng không được tuyên bố final novelty.

## Phase 29 — MP1 W02 architecture correction and macro-stage closeout (2026-09-26)

MP1 execution từng bị phân rã sai thành chuỗi bắt buộc W2-01→W2-12.

Các run W2-01→W2-09 đã hoàn thành được giữ làm historical subruns. W2-10/W2-11/W2-12 không chạy và bị supersede bởi W02 closeout.

Canonical package:

`outputs/execution/MP1-V002/W2/`

State:

```text
W02 = COMPLETE
Astra W2-09 incorporated = true
claim/target/hypothesis/K1-K9/provenance QA = PASS
citation protocol closure = SATISFIED
final novelty adjudication = NOT PERFORMED
candidate = CONDITIONAL
scientific gate = BLOCKED
blocking gaps = 8
unresolved K tests = K2,K3,K6,K7,K9
```

Next MP1 dependency:

```text
AWAITING_WORKFLOW_RECONCILIATION
→ MP1-WR1 with GPT-6 Sol High
```

Không được tiếp tục W2-10/W2-12.

## Phase 30 — Dual Sol-High checkpoint (2026-09-26)

Cả hai hướng kết thúc phiên tại một reasoning checkpoint:

```text
D1 next  = W09/S4 GPT-6 Sol High
MP1 next = MP1-WR1 GPT-6 Sol High
```

Astra chưa cần chạy ở bước kế tiếp. D1 Astra được giữ cho adversarial K1-K9 stage (W12) hoặc formal escalation route. MP1 W2-09 Astra đã được incorporated trong W02 closeout.

Final mentor-facing D1-vs-MP1 comparison vẫn chưa bắt đầu trong workstream hiện tại.

## Phase 31 — End-of-session snapshot (2026-09-26)

User đã push toàn bộ worker outputs lên `main` tại source HEAD:

`fa4f5d2f823cbd67a055f5d6d2309adf91c5d755`

Tạo/đồng bộ current-context documents để chat/agent mới có thể tiếp tục không cần suy đoán:

- `docs/project/CURRENT_EXECUTION_SNAPSHOT.md`
- `docs/project/NEXT_SESSION_START_HERE.md`
- `docs/project/PROJECT_HANDOFF_CURRENT.md`
- `docs/project/RESEARCH_STATE.md`
- `docs/project/research_state.json`
- `docs/project/MP1-V002_CURRENT_HANDOFF.md`
- `docs/project/MP1_MENTOR_PIVOT_CURRENT.md`
- `docs/project/MENTOR_PIVOT_STATUS.md`

Current principle:

> Finish the active D1 reconciliation/adversarial chain and MP1 workflow reconciliation before using either branch as the final mentor-facing comparison.


## Phase 32 — D1 W09→W11 execution, named-threat reopening, and hard-gate stop (2026-09-26)

Phiên D1-only này tiếp tục trực tiếp từ `docs/project/CURRENT_EXECUTION_SNAPSHOT.md`.

### W09 — Cross-worker reconciliation

W03-W08 được preflight lại trước khi merge:

```text
W03-W08 receipts = COMPLETE
QA                 = PASS
source records      = 71
unique paper ids    = 68
duplicate identities = 2
```

W09 tạo bốn canonical artifacts:

- `outputs/d1_execution/V4/W09/D1_PAPER_EVIDENCE_PACKETS.jsonl`
- `outputs/d1_execution/V4/W09/D1_CLAIM_EVOLUTION_MATRIX.json`
- `outputs/d1_execution/V4/W09/D1_NON_NOVELTY_REGISTER.json`
- `outputs/d1_execution/V4/W09/D1_NOVELTY_CANDIDATE_REGISTER.json`

Kết quả reconciliation quan trọng:

1. layer-jamming architecture, vacuum stiffness tuning, Coulomb slip, continuum-model creation, full-contact FE, generic model validation và percentage threshold **không được** quay lại thành novelty claim;
2. broad C02 bị narrow: multi-layer / N-layer partial-interaction theory đã tồn tại trong prior art;
3. `ca46dc062d` được reconcile theo scope:
   - direct threat đối với M→R quantitative error-boundary core;
   - chỉ partial overlap đối với full vacuum-layer-jamming M→R→E scientific act;
4. residual novelty register còn bốn candidate components, tất cả vẫn pending falsification;
5. final novelty adjudication = `NOT_PERFORMED`.

Execution provenance correction:

```text
planned W09 model = GPT-6 Sol High
actual session model = GPT-5.6 Sol High
```

Metadata W09 đã được sửa để không claim sai model execution. Scientific fields không bị thay đổi bởi correction này.

### S9 — Freeze K1-K9 trước evaluation

Tạo:

- `outputs/d1_execution/V4/S09/D1_K_CRITERIA_REGISTER.json`

State:

```text
criterion rows    = 9
version           = K-CRITERIA-V3.1
post-evidence edit = false
K verdicts        = UNRESOLVED
```

Các tiêu chí được copy từ V6/V3 design freeze, không được viết lại theo evidence W09.

### W10 — Named targeted threat integration

Broad search vẫn CLOSED.

W10 tạo:

- `outputs/d1_execution/V4/W10/D1_PRIOR_ART_FAMILY_COVERAGE.json`
- `outputs/d1_execution/V4/W10/D1_PRIOR_ART_THREAT_MATRIX.json`
- `outputs/d1_execution/V4/W10/D1_UNRESOLVED_THREAT_REGISTER.json`
- `outputs/d1_execution/V4/W10/D1_SEARCH_DECISION_LOG.json`

Coverage:

```text
required prior-art families = 18/18
material threat rows        = 15
named searches              = 2
broad search                = false
```

Named target T1:

```text
Yang, Guo & Wang 2025
DOI = 10.1038/s41598-025-22364-w
full text = verified
disposition = PARTIAL_OVERLAP
```

T1 trực tiếp cover vacuum-LJ experiment, layer-count/vacuum-pressure sweep và physical slip regimes, nhưng không chứa Zhang-M1-vs-interface-resolved-reference model-form validity map hay experiment chủ động đi qua hai phía của predicted model-validity boundary.

Named target T2:

```text
Wang et al. 2026
DOI = 10.1016/j.matdes.2026.116573
publisher/repository metadata + abstract = verified
full text = NOT AUDITED
disposition = UNRESOLVED
blocking = true
```

Không được dùng abstract để kết luận K1-K9.

### W11 — Provenance / contradiction / threshold / human-review QA

W11 tạo:

- `outputs/d1_execution/V4/W11/D1_PROVENANCE_QA.json`
- `outputs/d1_execution/V4/W11/D1_CONTRADICTION_REGISTER.json`
- `outputs/d1_execution/V4/W11/D1_THRESHOLD_FREEZE_REGISTER.json`
- `outputs/d1_execution/V4/W11/D1_HUMAN_REVIEW_CLEARANCE.json`

Precheck:

```text
unsupported thesis-critical claims = 0
invalid locators                   = 0
critical open contradictions       = 0
HG-02 provenance                   = PASS_WITH_DOWNSTREAM_BLOCKERS
HG-03 contradiction                = PASS_PRECHECK
HG-06 threshold freeze             = BLOCKED
HG-09 human review                 = BLOCKED
```

Typed metadata contradiction:

```text
paper_id 53d328abaa

wrong W09 DOI
= 10.3390/app14073041

authoritative D1-V008/full-text DOI
= 10.1061/JSENDH.STENG-13096
```

W11 adjudicates downstream identity using the verified D1-V008 source precedence and preserves the W09 error as historical provenance rather than silently rewriting it.

### Threshold stop

Canonical M1 architecture explicitly states:

```text
ERROR TOLERANCES = not yet defined
```

Vì chưa có đủ:

- experimental uncertainty;
- reference/numerical uncertainty;
- engineering-use tolerance;
- event-detection uncertainty;

nên W11 **không tự chọn** `epsilon_w`, `epsilon_K`, `epsilon_Q`.

Đặc biệt:

> Không dùng 5% của `ca46dc062d` làm D1 tolerance chỉ vì paper đó dùng/adopt 5%.

Current state:

```text
threshold freeze = BLOCKED_NOT_FROZEN
final project validation data inspected = false
post-hoc leakage = false
```

### Hard-gate consequence

W12 chưa được phép chạy.

Required re-entry:

1. full-text audit Wang et al. 2026 hoặc giữ các K-test liên quan ở UNRESOLVED;
2. justify + freeze `epsilon_w`, `epsilon_K`, `epsilon_Q` trước final validation/error-map inspection;
3. clear required human-review rows;
4. chỉ sau HG-06 và HG-09 mới chạy W12 Astra adversarial K1-K9.

Canonical fast-start state đã được đồng bộ tại:

- `docs/project/CURRENT_EXECUTION_SNAPSHOT.md`;
- `docs/project/research_state.json`.
