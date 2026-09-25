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
