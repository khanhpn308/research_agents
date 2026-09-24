# MP1-V002 — Current Handoff

> **Mục đích:** checkpoint ngắn gọn nhưng đủ chính xác để một chat/agent mới có thể tiếp tục MP1-V002 mà không phải dựng lại lịch sử.  
> **Checkpoint:** 2026-09-25.  
> **Trạng thái:** `MP1-V002 ACTIVE`; matrix = **10 full-text papers**; audit = `SUBSTANTIALLY_NARROWED`, `confidence = high`; citation coverage vẫn **OPEN**.  
> **Quan trọng:** D1/M1 vẫn là thesis direction được bảo toàn. MP1 chưa thay thế D1/M1.

## 1. Tóm tắt một câu

MP1 đã đi từ một kiến trúc “NiTi wire bundle + positive pressure + jamming + compact SMA pressure source” sang một câu hỏi mechanics rất hẹp:

> Dưới actively varied confinement pressure, pressure và curvature chi phối stick-slip và bending stiffness của một superelastic NiTi wire bundle như thế nào, và response đó có vượt ra ngoài existing elastic-fiber/contact model chỉ với parameter substitution hay không?

## 2. Vì sao không còn theo novelty kiểu component combination?

MP1-V001 đã trả:

```text
STATUS      = PIVOT_TO_MECHANICS_CORE
CONFIDENCE  = high
```

Các broad claims bị đóng/pre-empt:

- wire/fiber jamming;
- positive-pressure jamming;
- SMA + jamming trong cùng device;
- compact/onboard jamming pressure source;
- SMA-driven syringe/piston như stand-alone contribution;
- mechanical piston-driven jamming;
- NiTi chỉ đóng vai trò tendon/backbone trong variable-stiffness robot.

Do đó không được dùng “NiTi thay nylon”, “SMA thay motor”, “syringe thay pump” hoặc “robot khác” làm novelty.

## 3. Audit 10-paper mới nhất

Canonical matrix:

`outputs/verification/MP1-V002/verification_matrix.json`

```text
paper_count = 10
```

Kết quả:

```text
STATUS      = SUBSTANTIALLY_NARROWED
CONFIDENCE  = high
```

Canonical audit:

- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
- `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.md`

### T1 — CLOSED_BY_FULL_TEXT

NiTi/Nitinol cable/strand/rope literature đã có:

- wire-wire contact;
- Coulomb friction;
- micro-slip/sliding;
- hysteresis/damping;
- phase transformation;
- architecture-dependent effective stiffness.

Kết luận:

```text
NiTi + inter-wire friction/slip + hysteresis = prior art
```

Không claim novelty ở đây.

### T2 — OPEN_IN_CURRENT_FULL_TEXT_SET

Đã có:

- passive contact pressure;
- axial-load-induced radial pressure;
- manufacturing/preforming pressure;
- fixed radial preload.

Chưa có trong full-text matrix:

```text
actively varied external confinement pressure
→ NiTi/metallic wire bundle
→ change inter-wire normal force
→ change friction / stick-slip
→ change bending stiffness
```

T2 là phần còn mở quan trọng nhất.

### T3 — SUBSTANTIALLY_PREEMPTED

NiTi phase transformation + inter-wire friction/slip/hysteresis đã có prior art.

Phần còn mở là:

```text
P3 active confinement
× NiTi transformation
× inter-wire contact/slip
→ pressure-dependent bending stiffness / hysteresis
```

## 4. Hai paper mới đã giải quyết gì?

Sau metadata screening, hai full texts được thêm để đánh parameter-substitution kill test:

### Reedlunn, Daly & Shaw 2013

- paper_id: `fac21c950e`
- DOI: `10.1016/j.ijsolstr.2013.03.015`

Đóng góp đối với audit:

- hierarchical subcomponent response của 7×7 và 1×27 NiTi cables;
- phase transformation front propagation;
- cable architecture làm thay đổi compliance;
- analytical model đơn giản bắt đầu sai khi helix angle lớn vì bỏ qua local bending/twisting;
- paper thừa nhận localized radial contact pressure có thể bị bỏ sót trong response decomposition.

Không có P3 active confinement control.

### Fang et al. 2019

- paper_id: `2f7fcf2f8f`
- DOI: `10.1016/j.engstruct.2019.01.049`

Đóng góp đối với audit:

- 7×7 NiTi cable hysteresis;
- phenomenological multi-layer modelling;
- stiffness-reduction factors;
- non-synchronous wire engagement;
- cyclic degradation.

Paper cho thấy cable-level hysteresis có thể được fit bằng reduced-order model mà không resolve full contact mechanics, vì vậy tăng **parameter-substitution/reduced-order risk**.

Nhưng không có actively varied external confinement pressure.

## 5. Parameter-substitution kill test hiện tại

Audit trả:

```text
existing_elastic_fiber_model_appears_sufficient = false
niti_requires_distinct_constitutive_contact_coupling = false
evidence_status = insufficient
```

Không được diễn giải thành “NiTi chắc chắn cần model mới”.

Ý nghĩa đúng:

- existing models chưa được chứng minh là đủ cho pressure-controlled bending;
- cũng chưa chứng minh distinct NiTi constitutive-contact coupling là bắt buộc;
- direct baseline comparison vẫn cần thiết.

## 6. Pressure classification

```text
P1 = passive contact pressure
P2 = fixed preload / fixed confinement
P3 = actively varied confinement pressure
```

Chỉ P3 là direct threat cho mechanics core.

## 7. Citation metadata screening

Input:

```text
8 CSV exports
187 raw records
178 deduplicated candidates
```

Classification:

```text
POTENTIAL_KILL_PAPER = 0
GET_FULL_TEXT        = 12
KEEP_METADATA        = 85
UNCERTAIN            = 0
EXCLUDE              = 81
```

Canonical files:

- `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.json`
- `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.csv`
- `outputs/verification/MP1-V002/citation_screening/FULL_TEXT_SHORTLIST.csv`

Metadata-only labels không phải scientific evidence. Full-text audit mới được dùng để quyết định mechanics.

## 8. Citation coverage sau audit 10-paper

Tracker:

- `outputs/verification/MP1-V002/citation_coverage.json`
- `outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md`

Hiện tại:

```text
required directions = 14
backward required   = 8
forward required    = 6

all_required_directions_screened = false
no_unresolved_high_threat_source = true
stop_condition_satisfied         = false
search_cutoff_date               = NOT SET
```

Tracker vừa được re-init từ audit 10-paper, nên các branch đã thu thập trước đó chưa được ghi lại status screened trong JSON mới.

### Backward required

- B01 — Carboni et al.
- B02 — Vahidi et al.
- B03 — Xin Liu thesis.
- B04 — Tjahjanto et al.
- B05 — braided NiTi microfilaments.
- B06 — Silva et al. 2022.
- B07 — Niu & Chen 2021, DOI `10.3390/app112110032`.
- B08 — Reedlunn et al. 2013, DOI `10.1016/j.ijsolstr.2013.03.015`.

### Forward required

- F01 — Bai et al. 2022.
- F02 — Liu et al. 2021.
- F03 — Zhang & Yao 2026.
- F04 — Takashima et al. 2022.
- F05 — Matsumoto et al. 2024.
- F06 — Wang et al. 2024.

## 9. Citation provenance đã có

Đã preserve:

`data/search_exports/MP1-V002/raw/backward/`

và:

`data/search_exports/MP1-V002/raw/forward/`

B06/F03/F05/F06 có manual provenance files trong repo.

F03 và F06 là zero-result branches theo Scopus cutoff 2026-09-24.

F05 citing paper đã resolve thành Takashima et al. 2026, DOI `10.20965/jrm.2026.p0646`; human screen = `KEEP_METADATA`.

## 10. Stop condition

V002 chỉ đóng khi:

1. mọi required backward/forward branch đã được screen;
2. `search_date` và `records_screened` được ghi;
3. mọi high-threat candidate được resolve hoặc liệt kê unresolved;
4. `citation_coverage --check` trả stop condition satisfied.

Absence of a matching paper chỉ là **protocol-bounded result**, không phải proof of universal novelty.

## 11. Việc tiếp theo

Không broad search.

Ưu tiên:

```text
screen/resolve B07 + B08
→ populate screening status for B01-B08 and F01-F06
→ set search_cutoff_date
→ run citation_coverage --check
→ resolve any new high-threat source if exposed
→ final MP1-V002 adjudication
```

Nếu B07/B08 chỉ dẫn về passive/fixed cable pressure, generic wire-rope damping hoặc uniaxial SMA hysteresis thì không kill T2.

## 12. Kill conditions còn hiệu lực

Kill hoặc narrow MP1 nếu:

1. prior art cho thấy P3 actively pressure-controlled metallic/NiTi wire-bundle stiffness mechanics đã tồn tại; hoặc
2. parameter substitution trong existing elastic-fiber/contact framework đủ để reproduce pressure-dependent bending response.

## 13. Guardrails

Không được claim novelty từ:

- NiTi thay nylon;
- material substitution;
- generic NiTi cable friction;
- SMA + jamming trong cùng robot;
- compact pump/syringe;
- passive radial pressure;
- fixed preload.

Không đánh đồng:

```text
wire-rope friction != pressure-controlled wire jamming
P1/P2 pressure      != P3 active confinement
```

## 14. File cần đọc khi handoff

1. `docs/project/MP1_MENTOR_PIVOT_CURRENT.md`
2. `docs/project/MP1-V002_CURRENT_HANDOFF.md`
3. `docs/project/MP1_MENTOR_PIVOT_TUTOR.md`
4. `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
5. `outputs/verification/MP1-V002/verification_matrix.json`
6. `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
7. `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.json`
8. `outputs/verification/MP1-V002/citation_coverage.json`
9. `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`

