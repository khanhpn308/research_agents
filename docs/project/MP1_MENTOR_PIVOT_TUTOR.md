# MP1 — Mentor Pivot Tutor / Weekend Review Guide

> **Mục đích:** hướng dẫn một agent mới truy xuất đúng repository evidence và tạo báo cáo giải thích:  
> **“Tại sao từ ý tưởng mentor ban đầu lại đi đến mechanics core hiện tại?”**  
> File này không phải scientific evidence. Nó là retrieval + reporting guide.

## 1. Ngôn ngữ và thuật ngữ

Báo cáo phải viết bằng **tiếng Việt**.

Giữ English cho:

- code;
- schema;
- filename;
- JSON key;
- status token;
- CLI command;
- DOI;
- paper title;
- technical/mechanical term khi bản dịch có thể làm mất nghĩa.

Khi cần, dùng dạng:

```text
độ cứng uốn (bending stiffness)
ma sát giữa các dây (inter-wire friction)
trạng thái dính–trượt (stick-slip)
áp suất giam giữ chủ động (actively varied confinement pressure)
mô hình cấu thành (constitutive model)
```

Không dịch cưỡng ép các term như `jamming`, `superelasticity`, `hysteresis`, `stick-slip`, `constitutive model` nếu làm câu kém chính xác.

## 2. Câu hỏi trung tâm cần trả lời

Agent phải trả lời có bằng chứng:

> Tại sao kiến trúc mentor đề xuất ban đầu không còn được xem là novelty ở cấp component combination, và chuỗi falsification nào đã dẫn đến mechanics core hiện tại?

Không được trả lời bằng một câu kiểu “vì literature đã có”. Phải chỉ rõ:

1. ý tưởng mentor ban đầu gồm những claim nào;
2. MP1-V001 đã đóng claim nào và bằng evidence gì;
3. claim nào sống sót sau V001;
4. vì sao phải chuyển từ architecture novelty sang mechanics;
5. MP1-V002 đã tiếp tục đóng/narrow T1-T3 ra sao;
6. Reedlunn 2013 và Fang 2019 đã thay đổi parameter-substitution risk như thế nào;
7. mechanics core hiện tại chính xác là gì;
8. điều gì vẫn có thể kill mechanics core;
9. còn thiếu coverage/evidence nào trước final adjudication.

## 3. Retrieval order bắt buộc

Đọc theo thứ tự này. Không bắt đầu từ old chat history nếu repo đã có canonical artifact.

### Layer A — current state

1. `docs/project/MP1_MENTOR_PIVOT_CURRENT.md`
2. `docs/project/MP1-V002_CURRENT_HANDOFF.md`
3. `docs/project/RESEARCH_LOG.md`

Mục đích: biết current state và timeline.

### Layer B — original mentor proposal + falsification design

4. `docs/project/MENTOR_PIVOT_STATUS.md`
5. `docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md`
6. `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`

Mục đích: reconstruct original architecture, C1-C8 và kill logic.

### Layer C — MP1-V001 decision

7. `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
8. `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md`
9. `outputs/verification/MP1-V001/verification_matrix.json`

Mục đích: chứng minh vì sao result là `PIVOT_TO_MECHANICS_CORE`.

### Layer D — MP1-V002 protocol

10. `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`

Mục đích: hiểu T1/T2/T3, P1/P2/P3 pressure classification và parameter-substitution kill test.

### Layer E — current full-text scientific evidence

11. `outputs/verification/MP1-V002/verification_matrix.json`
12. `outputs/verification/MP1-V002/verification_matrix.md`
13. `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
14. `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.md`

Mục đích: dùng current 10-paper matrix, không dùng kết luận 8-paper cũ làm final current state.

### Layer F — citation search provenance

15. `outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.json`
16. `outputs/verification/MP1-V002/citation_screening/FULL_TEXT_SHORTLIST.csv`
17. `outputs/verification/MP1-V002/citation_coverage.json`
18. `outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md`
19. `data/search_exports/MP1-V002/raw/backward/`
20. `data/search_exports/MP1-V002/raw/forward/`

Mục đích: phân biệt “scientific evidence” với “search/coverage evidence”.

## 4. Evidence hierarchy

Agent phải dùng hierarchy sau:

### A. VERIFIED FULL TEXT

Nguồn:

- `verification_matrix.json`;
- extracted evidence JSON;
- canonical full-text audit outputs.

Đây là nguồn được phép dùng để nói một mechanics claim đã được established/pre-empted.

### B. METADATA ONLY

Nguồn:

- citation CSV;
- metadata screening output;
- title/abstract.

Chỉ dùng để:

- triage;
- identify threat;
- select GET_FULL_TEXT.

Không dùng metadata-only để claim một mechanics result chắc chắn.

### C. COVERAGE EVIDENCE

Nguồn:

- `citation_coverage.json`;
- zero-result provenance;
- branch record counts.

Chỉ dùng để nói protocol đã screen đến đâu.

Không được biến “0 citation found” thành “novelty proven”.

### D. INFERENCE

Mọi logical inference phải ghi rõ đó là inference, đặc biệt:

- liệu parameter substitution có đủ hay không;
- liệu NiTi cần distinct constitutive-contact coupling hay không;
- liệu một mechanics core có thật sự novel hay chỉ chưa bị tìm thấy.

## 5. Không được trộn historical state với current state

Current state authoritative:

```text
MP1-V002 matrix = 10 papers
TARGETED_THREAT_AUDIT = SUBSTANTIALLY_NARROWED
confidence = high

T1 = closed_by_full_text
T2 = open_in_current_full_text_set
T3 = substantially_preempted

parameter-substitution evidence = insufficient
citation coverage stop condition = false
```

Nếu file lịch sử nói “8 papers”, phải ghi rõ đó là historical checkpoint, không dùng làm current state.

## 6. Cấu trúc báo cáo cuối tuần

Agent phải tạo báo cáo theo cấu trúc:

### 1. Executive summary

Tối đa 1 trang:

- mentor đề xuất gì;
- cái gì đã bị prior art đóng;
- vì sao project chuyển sang mechanics;
- mechanics core hiện tại;
- current blockers.

### 2. Original mentor architecture

Trình bày sơ đồ:

```text
NiTi wire bundle
+ positive pressure
+ frictional jamming
+ variable bending stiffness
+ SMA pressure source
```

Tách thành C1-C8.

### 3. MP1-V001: architecture falsification

Bảng:

| Claim | Original idea | V001 result | Evidence class | Consequence |
|---|---|---|---|---|

Phải có C1-C8.

### 4. Why PIVOT_TO_MECHANICS_CORE?

Giải thích causal chain, không chỉ lặp verdict.

Ví dụ:

```text
wire jamming known
+ positive-pressure jamming known
+ SMA+jamming known
+ compact pressure source known
↓
component-combination novelty collapses
↓
only unresolved scientific question is coupled mechanics
```

### 5. MP1-V002 threat audit

Bảng:

| Target | Current status | What prior art establishes | What remains missing |
|---|---|---|---|

T1/T2/T3.

### 6. Role of the 10 full-text papers

Không cần tóm tắt đều 10 paper.

Nhóm theo mechanics function:

- NiTi cable friction/contact;
- wire-rope bending/internal friction;
- phase transformation + hysteresis;
- braided/micro-cable effects;
- reduced-order/phenomenological modelling.

Nêu riêng Reedlunn 2013 và Fang 2019.

### 7. Parameter-substitution kill test

Phải giải thích:

```text
Can existing elastic-fiber/contact mechanics
+ substituted NiTi properties
reproduce pressure-dependent bending?
```

Current answer:

```text
insufficient evidence
```

Không được biến thành yes/no.

### 8. Current mechanics core

Phải quote/paraphrase đúng current question:

> Under actively varied positive radial/transverse confinement, pressure và curvature govern stick-slip transitions và bending stiffness của superelastic NiTi wire bundle như thế nào, và existing elastic-fiber/contact framework với substituted NiTi properties có predict được response đó hay không?

### 9. Current citation coverage

Ghi:

```text
14 required directions
8 backward
6 forward
stop_condition_satisfied = false
no_unresolved_high_threat_source = true
```

Giải thích B07/B08 là backward priorities mới sau audit 10-paper.

### 10. What could still kill MP1?

Ít nhất hai kill conditions:

1. direct prior art cho P3 pressure-controlled NiTi/metallic wire-bundle bending mechanics;
2. parameter substitution đủ để reproduce response, không cần distinct coupling.

### 11. What should happen next?

Không broad search.

Chỉ:

- close required citation branches;
- resolve new high-threat source nếu xuất hiện;
- run coverage check;
- final V002 adjudication;
- sau đó mới quyết định có đi MP1-V003/MP1-V004 hay giữ D1/M1.

## 7. Report quality rules

Báo cáo phải:

- phân biệt **fact / audit result / inference**;
- không claim “novel” chỉ vì chưa thấy paper;
- không coi material substitution là novelty;
- không dùng metadata-only để kết luận mechanics;
- không bỏ qua negative result;
- không cherry-pick paper ủng hộ MP1;
- ghi rõ D1/M1 vẫn được bảo toàn;
- ghi rõ V002 chưa đạt stop condition.

## 8. Suggested agent prompt

Có thể dùng nguyên prompt này:

```text
Đọc docs/project/MP1_MENTOR_PIVOT_TUTOR.md và làm đúng retrieval order trong file.

Mục tiêu: tạo báo cáo cuối tuần bằng tiếng Việt trả lời câu hỏi:
“Tại sao từ ý tưởng mentor ban đầu lại đi đến mechanics core hiện tại?”

Yêu cầu:
- chỉ dùng repository evidence;
- phân biệt VERIFIED FULL TEXT / METADATA ONLY / COVERAGE EVIDENCE / INFERENCE;
- current state phải lấy từ matrix 10-paper và TARGETED_THREAT_AUDIT mới nhất;
- không dùng historical 8-paper state làm current state;
- giải thích causal chain từ C1-C8 → PIVOT_TO_MECHANICS_CORE → T1/T2/T3 → current mechanics core;
- giải thích parameter-substitution kill test;
- nêu current citation-coverage gap và kill conditions;
- không claim universal novelty;
- giữ code/schema/filename/key bằng English;
- thuật ngữ cơ khí quan trọng giữ English trong ngoặc khi cần;
- báo cáo phải đủ rõ để một người chưa theo dõi project từ đầu hiểu được logic quyết định.
```

## 9. Output recommendation

Tên báo cáo gợi ý:

`docs/reports/MP1_WEEKEND_MECHANICS_CORE_TRACE_2026-09-25.md`

Nếu cần bản trình bày cho mentor, có thể tạo một bản ngắn hơn sau khi báo cáo kỹ thuật đã hoàn thành.



## 10. Tutor chi tiết cho claim-level evidence report

Khi cần báo cáo theo kiểu kiểm chứng từng claim C1-C8/T1-T3, bắt buộc đọc thêm:

`docs/project/MP1_CLAIM_EVIDENCE_REPORT_TUTOR.md`

Tutor đó quy định traceability chain:

```text
claim
→ audit verdict
→ paper_id
→ paper title / DOI
→ evidence JSON
→ original PDF
→ page / section
→ evidence type
→ what it proves
→ what it does NOT prove
→ audit consequence
```

Không được dùng tutor tổng quan này thay thế cho claim-level source verification.
