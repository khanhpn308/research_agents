# MP1 — Claim-Level Evidence Report Tutor

> **Mục đích:** hướng dẫn agent tạo một báo cáo khoa học chi tiết, có thể kiểm chứng từng câu, trả lời các câu hỏi kiểu:  
> “C1 bị `closed` vì paper nào?”, “Paper đó thực sự làm gì?”, “Dùng model gì?”, “Thí nghiệm ra sao?”, “Kết quả nào đủ để bác bỏ claim?”, “Thông tin này nằm ở trang nào?”, “Điều gì paper đó KHÔNG chứng minh?”  
>
> **Nguyên tắc tối cao:** **không có nguồn kiểm chứng cụ thể thì không được trình bày như một fact khoa học.**

---

## 1. Chuẩn ngôn ngữ

Báo cáo viết bằng **tiếng Việt**.

Giữ English cho:

- code;
- schema;
- filename;
- JSON key;
- status token;
- CLI command;
- DOI;
- paper title;
- technical/mechanical terms khi cần độ chính xác.

Ví dụ:

- độ cứng uốn (**bending stiffness**);
- ma sát giữa các dây (**inter-wire friction**);
- trạng thái dính–trượt (**stick-slip**);
- áp suất giam giữ chủ động (**actively varied confinement pressure**);
- mô hình cấu thành (**constitutive model**);
- biến dạng do chuyển pha (**phase-transformation strain**).

Không dịch cưỡng ép `jamming`, `superelasticity`, `hysteresis`, `stick-slip`, `constitutive model` nếu bản dịch làm mất nghĩa cơ học.

---

# 2. Evidence rule bắt buộc

Mỗi statement khoa học trong báo cáo phải thuộc **một trong năm loại** dưới đây.

## 2.1 VERIFIED PAPER FACT

Thông tin trực tiếp từ full-text paper.

Phải ghi:

```text
Paper title
Authors / year
DOI
paper_id
page(s)
evidence_type
repo evidence path
repo PDF path
```

Ví dụ:

```text
[SOURCE — VERIFIED FULL TEXT]
Bai et al. (2022), "Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming"
DOI: 10.3390/app12073582
paper_id: 240fbf6022
Pages: 8
Evidence type: experimental
Evidence JSON:
data/evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json
PDF:
papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf
```

## 2.2 AUDIT VERDICT

Kết luận của verification round, ví dụ:

```text
C1 = closed
T1 = closed_by_full_text
```

Phải chỉ nguồn audit:

```text
outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json
outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json
```

**Audit verdict không thay thế paper evidence.**

Nếu viết:

> C1 bị closed.

thì ngay sau đó phải chỉ ra paper nào và evidence nào khiến audit đưa ra verdict đó.

## 2.3 METADATA-ONLY INFORMATION

Nguồn:

- citation CSV;
- title/abstract;
- `METADATA_SCREENING.json`;
- `FULL_TEXT_SHORTLIST.csv`.

Chỉ được dùng để nói:

- paper là candidate;
- paper được triage;
- cần full text;
- branch nào đã tìm thấy candidate.

Không dùng metadata-only để khẳng định mechanics đã được established.

## 2.4 COVERAGE FACT

Nguồn:

- `citation_coverage.json`;
- `CITATION_COVERAGE_STATUS.md`;
- search export / zero-result provenance.

Chỉ dùng để nói:

- đã screen bao nhiêu record;
- branch nào đã/ chưa screen;
- search cutoff;
- stop condition.

Không biến:

```text
0 result
```

thành:

```text
novelty proven
```

## 2.5 INFERENCE / DERIVATION

Nếu agent tự suy luận từ nhiều paper hoặc tự tính toán:

phải ghi rõ:

```text
[INFERENCE]
```

hoặc:

```text
[DERIVATION]
```

và liệt kê source đầu vào.

Ví dụ:

> [INFERENCE] Vì Bai 2022 đã có wire jamming và Zhang & Yao 2026 đã có positive-pressure fiber jamming, việc chỉ thay fiber bằng NiTi không tự động tạo novelty.

Đây là inference của audit, không phải câu nguyên văn của một paper.

---

# 3. Quy tắc “không page = không fact”

Đây là rule bắt buộc đối với báo cáo chi tiết.

Nếu agent nêu:

- số liệu;
- pressure;
- stiffness;
- force;
- modulus;
- friction coefficient;
- số lần tăng stiffness;
- mô hình hoặc equation cụ thể;
- experimental setup;
- limitation quan trọng;

thì phải có **page hoặc section cụ thể**.

Ưu tiên lấy page từ:

```text
evidence_relevant_to_topic[*].page_numbers
```

trong evidence JSON.

Nếu thông tin chỉ nằm trong:

```text
main_results
modeling_methods
research_objective
```

nhưng không có page mapping, agent phải mở PDF và xác minh page/section trước khi đưa vào final report.

Nếu chưa xác minh được:

```text
[PAGE NOT YET VERIFIED]
```

và không được trình bày nó như một fact đã khóa.

**Không được tự đoán page.**

---

# 4. Retrieval order cho báo cáo claim-level

## Layer 1 — Claim definition

Đọc:

1. `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
2. `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`

Mục tiêu:

- biết C1-C8 được định nghĩa thế nào;
- biết status hiện tại;
- biết `evidence_paper_ids`.

## Layer 2 — Paper mapping

Đọc:

`outputs/verification/MP1-V001/verification_matrix.json`

Dùng `paper_id` để map:

```text
claim
→ paper_id
→ title
→ DOI
→ year
→ extracted evidence
```

## Layer 3 — Evidence JSON

Đọc đúng file trong:

`data/evidence/`

Đây là nơi có:

- `research_objective`;
- `research_problem`;
- `modeling_methods`;
- `main_results`;
- `evidence_relevant_to_topic`;
- `limitations_stated_by_authors`;
- page numbers.

## Layer 4 — Original PDF

Dùng:

`data/paper_registry.json`

để lấy `relative_path`.

PDF MP1-V001 nằm tại:

`papers/verification/MP1-V001/`

PDF MP1-V002 nằm tại:

`papers/verification/MP1-V002/`

Nếu cần xác minh:

- equation;
- figure;
- table;
- exact setup;
- page number;
- wording;
- limitation;

phải mở PDF gốc.

## Layer 5 — Audit consequence

Sau khi hiểu paper, quay lại:

`CORE_PRIOR_ART_AUDIT.json`

để giải thích:

> Evidence đó tác động lên C1/C2/... như thế nào?

Không được làm ngược:

> thấy verdict trước rồi tìm một câu bất kỳ để minh họa.

---

# 5. Source map — MP1-V001 C1-C8

Đây là map authoritative từ `CORE_PRIOR_ART_AUDIT.json`.

## C1 — Wire/fiber jamming for variable stiffness

```text
status = closed
```

Primary evidence:

- `240fbf6022` — Bai et al. 2022.
- `3aa8790db0` — Zhang & Yao 2026.

### Bai et al. 2022

Title:

*Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming*

DOI:

`10.3390/app12073582`

Evidence JSON:

`data/evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json`

PDF:

`papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`

High-value evidence:

- vacuum-controlled wire/fiber jamming;
- inter-wire friction;
- Euler–Bernoulli modelling of unjammed/jammed states;
- nearly 7× bending stiffness increase for an 8 mm kraft-rope structure when vacuum changes from 0 to -85 kPa;
- page-level evidence includes p. 8 for the ~7× result.

### Zhang & Yao 2026

Title:

*A variable stiffness omnidirectional chain based on positive-pressure fiber jamming*

DOI:

`10.5194/ms-17-481-2026`

Evidence JSON:

`data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json`

PDF:

`papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf`

High-value evidence:

- positive-pressure fiber jamming;
- jamming / transition / slipping states;
- Coulomb friction;
- pressure-dependent equivalent bending mechanics;
- three-point bending over 0–300 kPa;
- critical shear forces and slipping-state stiffness increase approximately linearly with pressure;
- relevant pages: 1, 3, 4, 6, 9, 10, 11 depending claim.

### Audit consequence

C1 bị `closed` vì wire/fiber jamming variable stiffness đã được:

- physically implemented;
- mechanically modelled;
- experimentally validated.

---

## C2 — Positive-pressure jamming for variable stiffness

```text
status = closed
```

Primary evidence:

- `182d854610` — Liu et al. 2021.
- `3aa8790db0` — Zhang & Yao 2026.

### Liu et al. 2021

Title:

*A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots*

DOI:

`10.1109/LRA.2021.3097255`

Evidence JSON:

`data/evidence/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json`

PDF:

`papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`

High-value evidence:

- internal pressurization of a granular chamber;
- pressure-controlled stiffness;
- bending stiffness approximately 0.69 → 4.02 N/mm over ~68/69 → 172 kPa;
- roughly six-fold stiffness increase;
- relevant pages include 1, 3, 4, 5.

### Zhang & Yao 2026

Dùng source card C1.

High-value evidence:

- positive pressure up to 300 kPa;
- pressure-dependent slip transitions;
- pressure-dependent bending stiffness.

### Audit consequence

Broad novelty claim “positive-pressure jamming for variable stiffness” không còn bảo vệ được.

---

## C3 — SMA + jamming trong cùng variable-stiffness device

```text
status = closed
```

Primary evidence:

- `2cd907e77a` — Takashima et al. 2022.
- `7ce492505d` — Matsumoto et al. 2024.
- `99fe24da8b` — Takashima et al. 2024.
- `d3b3b6963f` — Takashima et al. 2026.

### Takashima et al. 2022

Title:

*Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon*

DOI:

`10.20965/jrm.2022.p0466`

Evidence JSON:

`data/evidence/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json`

PDF:

`papers/verification/MP1-V001/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf`

High-value evidence:

- SMA wires + granular jamming trong cùng link;
- four stiffness states;
- bending-stiffness measurement;
- shape recovery;
- relevant pages include 1–10 depending claim.

### Matsumoto et al. 2024

paper_id:

`7ce492505d`

Evidence JSON:

`data/evidence/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json`

PDF:

`papers/verification/MP1-V001/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf`

### Takashima et al. 2024

paper_id:

`99fe24da8b`

Evidence JSON:

`data/evidence/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json`

PDF:

`papers/verification/MP1-V001/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf`

### Takashima et al. 2026

paper_id:

`d3b3b6963f`

Evidence JSON:

`data/evidence/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json`

PDF:

`papers/verification/MP1-V001/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf`

### Critical distinction

Các paper này chứng minh:

```text
SMA + jamming in one device
```

nhưng không chứng minh:

```text
NiTi wires themselves are the jammed frictional medium
```

Agent phải nói rõ điều này để tránh overclaim.

---

## C4 — Compact/onboard pressure source for jamming

```text
status = closed
```

Primary evidence:

- `bbe88a0c04` — Huynh et al. 2022.
- `c6a31066f8` — Wang et al. 2024.

### Huynh et al. 2022

Title:

*Soft actuator with switchable stiffness using a micropump-activated jamming system*

DOI:

`10.1016/j.sna.2022.113449`

Evidence JSON:

`data/evidence/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json`

PDF:

`papers/verification/MP1-V001/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf`

High-value evidence:

- embedded bidirectional flexible micropump;
- positive hydraulic actuation + negative-pressure granular jamming;
- ±55 kPa pump capability;
- -50 kPa jamming increases tip bending force from 0.134 N to 0.743 N at 3 mm displacement;
- ~5.5× stiffness enhancement;
- relevant pages include 1, 6, 7, 8, 9, 10.

### Wang et al. 2024

Title:

*Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm*

DOI:

`10.1108/IR-11-2023-0305`

Evidence JSON:

`data/evidence/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json`

PDF:

`papers/verification/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf`

High-value evidence:

- compact motor + ball screw + piston;
- up to 150 N jamming force;
- stiffening ratio ~6–25;
- relevant pages include 1–8 depending claim.

---

## C5 — NiTi wires themselves as frictional jamming medium

```text
status = open_in_supplied_corpus
```

Evidence papers used to establish the boundary:

- Bai 2022 — `240fbf6022`.
- Takashima 2022 — `2cd907e77a`.
- Wang 2024 — `c6a31066f8`.
- Zhang & Yao 2026 — `3aa8790db0`.

Correct interpretation:

- Bai uses kraft/hemp/nylon wire/fiber, not NiTi.
- Zhang & Yao use fiber bundle, not NiTi.
- Takashima uses NiTi as backbone/recovery element, not jamming medium.
- Wang uses NiTi tendons around particle-jamming core, not jammed bundle.

### Rule

Không được viết:

> C5 is novel.

Phải viết:

> C5 remained open **within the supplied MP1-V001 corpus**.

---

## C6 — Positive-pressure confinement of superelastic NiTi wire bundle

```text
status = open_in_supplied_corpus
```

Evidence:

- Liu 2021 — `182d854610`.
- Zhang & Yao 2026 — `3aa8790db0`.

Hai paper establish positive-pressure jamming, nhưng không dùng a superelastic NiTi wire bundle làm pressure-confined frictional medium.

### Rule

Không được suy luận:

```text
nylon fiber + pressure
therefore
NiTi + pressure is novel
```

Material substitution không đủ.

---

## C7 — Coupled NiTi superelasticity + inter-wire slip/friction + pressure + bending stiffness

```text
status = open_in_supplied_corpus
```

Evidence boundary:

- Zhang & Yao 2026 — pressure + fiber friction/slip + bending stiffness.
- Takashima 2022 — SMA + granular jamming.
- Matsumoto 2024 — Ti-Ni recovery/R-phase in jamming lineage.
- Wang 2024 — NiTi tendons + piston-compressed particles.

Không paper nào trong V001 trực tiếp couples toàn bộ bốn thành phần.

Đây là reason MP1 chuyển sang mechanics core.

---

## C8 — SMA-driven syringe/piston powering jamming

```text
status = substantially_preempted
```

Primary evidence:

- `de64029540` — Pierce & Mascaro 2013.
- `55457a97c6` — Kotb et al. 2021.
- `bbe88a0c04` — Huynh et al. 2022.
- `c6a31066f8` — Wang et al. 2024.

### Pierce & Mascaro 2013

Title:

*A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump*

DOI:

`10.1109/TMECH.2012.2211032`

Evidence JSON:

`data/evidence/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json`

PDF:

`papers/verification/MP1-V001/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf`

### Kotb et al. 2021

Title:

*Shape Memory Alloy Capsule Micropump for Drug Delivery Applications*

DOI:

`10.3390/mi12050520`

Evidence JSON:

`data/evidence/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json`

PDF:

`papers/verification/MP1-V001/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf`

### Why only “substantially_preempted”?

Exact:

```text
SMA → syringe/piston → jamming pressure
```

hookup chưa được trực tiếp thấy trong supplied corpus.

Nhưng component basis đã tồn tại:

- SMA pump exists;
- compact jamming pump exists;
- piston jamming exists.

Do đó exact topology có thể khác nhưng scientific contribution risk cao vì có thể chỉ là actuator substitution.

---

# 6. Source map — MP1-V002 current 10-paper mechanics evidence

Current authoritative matrix:

`outputs/verification/MP1-V002/verification_matrix.json`

## V002 paper table

### fac21c950e

Title:

*Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses*

DOI:

`10.1016/j.ijsolstr.2013.03.015`

Evidence JSON:

`data/evidence/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json`

PDF:

`papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf`

### 2f7fcf2f8f

Title:

*Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application*

DOI:

`10.1016/j.engstruct.2019.01.049`

Evidence JSON:

`data/evidence/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json`

PDF:

`papers/verification/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf`

### d9966f2f5e

Title:

*Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification*

DOI:

`10.1061/(ASCE)EM.1943-7889.0000852`

Evidence JSON:

`data/evidence/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json`

PDF:

`papers/verification/MP1-V002/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf`

### 9e15094d68

Title:

*Superelasticity SMA cables and its simplified FE model*

DOI:

`10.1007/s40430-022-03957-2`

Evidence JSON:

`data/evidence/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json`

PDF:

`papers/verification/MP1-V002/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf`

### 53200aa0c6

Title:

*Mechanical response of single and double-helix SMA wire ropes*

DOI:

`10.1080/15376494.2021.1955313`

Evidence JSON:

`data/evidence/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json`

PDF:

`papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf`

### 98fee47c04

Title:

*Nonlinear Vibration Isolation via a NiTiNOL Wire Rope*

DOI:

`10.3390/app112110032`

Evidence JSON:

`data/evidence/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json`

PDF:

`papers/verification/MP1-V002/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf`

### aaad9c248c

Title:

*Cable Vibration Considering Internal Friction*

Year:

2004

Type:

M.S. thesis

Evidence JSON:

`data/evidence/A5-Cable vibration considering internal friction_aaad9c248c.json`

PDF:

`papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf`

### ccdc1bb980

Title:

*BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE*

Year:

2017

Evidence JSON:

`data/evidence/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json`

PDF:

`papers/verification/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf`

### e8462758c3

Title:

*High damping capacity with a wide temperature window in braided NiTi microfilaments*

DOI:

`10.1016/j.matlet.2026.141544`

Evidence JSON:

`data/evidence/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json`

PDF:

`papers/verification/MP1-V002/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf`

### 6dd1ca94d1

Title:

*NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings*

DOI:

`10.3390/s22208045`

Evidence JSON:

`data/evidence/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json`

PDF:

`papers/verification/MP1-V002/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf`

---

# 7. Current V002 target mapping

Authoritative source:

`outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`

## T1 — closed_by_full_text

Evidence paper_ids:

- `d9966f2f5e`;
- `53200aa0c6`;
- `e8462758c3`;
- `6dd1ca94d1`;
- `98fee47c04`.

Agent phải giải thích:

- contact;
- friction;
- micro-slip;
- phase transformation;
- hysteresis/damping;
- stiffness effects.

Không chỉ list titles.

## T2 — open_in_current_full_text_set

Evidence paper_ids defining the boundary:

- `ccdc1bb980`;
- `aaad9c248c`;
- `53200aa0c6`;
- `fac21c950e`.

Agent phải phân loại pressure:

```text
P1 passive
P2 fixed
P3 actively varied
```

Và chỉ ra vì sao existing papers vẫn chưa đạt P3 NiTi bundle bending mechanics.

## T3 — substantially_preempted

Evidence paper_ids:

- `d9966f2f5e`;
- `53200aa0c6`;
- `e8462758c3`;
- `6dd1ca94d1`;
- `98fee47c04`.

Agent phải giải thích:

> phase transformation + inter-wire friction/hysteresis đã known, nhưng active confinement pressure coupling vẫn chưa established.

---

# 8. Mandatory report format cho từng claim

Mỗi C1-C8 hoặc T1-T3 phải dùng format này.

## 8.1 Claim

Ví dụ:

```text
C1 — Wire/fiber jamming for variable stiffness is novel.
```

## 8.2 Current verdict

```text
CLOSED
```

Nguồn verdict:

`outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`

## 8.3 Why this claim mattered

Giải thích claim ban đầu có ý nghĩa gì trong mentor architecture.

Không cần source paper vì đây là project-definition information; cite protocol file.

## 8.4 Paper 1 — Source card

Bắt buộc:

```text
Title:
Authors:
Year:
DOI:
paper_id:
Verification round:
Evidence JSON:
Original PDF:
```

## 8.5 What the paper physically/mechanically did

Phải mô tả:

- material;
- architecture;
- loading;
- pressure/vacuum;
- contact/friction role;
- actuation;
- measured output.

Mỗi paragraph phải có page citation.

## 8.6 Modeling / theory

Nếu có:

- beam theory;
- FE;
- constitutive law;
- Coulomb friction;
- energy method;
- empirical model.

Phải ghi page/section.

## 8.7 Experimental method

Phải nói rõ:

- specimen;
- pressure/loading range;
- bending/tension test;
- metric measured;
- comparison state.

Nếu evidence JSON chưa có page cho setup, mở PDF.

## 8.8 Quantitative result

Nêu số liệu quan trọng, không spam tất cả số liệu.

Mỗi số phải có source.

## 8.9 What it proves

Ví dụ:

> Paper này trực tiếp chứng minh wire jamming đã được dùng để điều chỉnh bending stiffness.

## 8.10 What it does NOT prove

Ví dụ:

> Paper này không dùng NiTi làm jamming medium và không chứng minh active positive confinement của NiTi wire bundle.

Phần này rất quan trọng để tránh overclaim.

## 8.11 Audit consequence

Ví dụ:

> Vì broad claim C1 chỉ yêu cầu “wire/fiber jamming for variable stiffness”, bằng chứng trên đủ để close C1. Nó không đủ để close C6/C7.

## 8.12 Verification box

Kết thúc mỗi claim bằng:

```text
VERIFICATION STATUS
Primary full-text evidence checked: YES
DOI checked: YES
paper_id checked: YES
Page-level evidence checked: YES
Audit source checked: YES
Inference explicitly labelled: YES/NO
Unresolved source issue: NONE / <describe>
```

---

# 9. Example — cách viết C1 đạt chuẩn

## C1 — Wire/fiber jamming for variable stiffness is novel

**Verdict:** `CLOSED`.

**Audit source:**  
`outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`

### Evidence 1 — Bai et al. 2022

Bai et al. thiết kế một soft actuator có stiffness-tunable layer dựa trên **wire/fiber jamming**. Họ thử kraft rope, hemp rope và nylon wire làm jamming medium. Khi vacuum được áp dụng, friction giữa các phần tử tăng và bundle chuyển từ trạng thái compliant sang jammed. Đối với cấu trúc kraft-rope dày 8 mm, bending stiffness tăng gần 7 lần khi vacuum thay đổi từ 0 kPa xuống -85 kPa, đạt khoảng 0.89 N/mm tại 15 mm deflection.  
**Source:** Bai et al. 2022, DOI `10.3390/app12073582`, paper_id `240fbf6022`, p. 8, experimental evidence.  
**Repo:** `data/evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json`.

Paper cũng dùng Euler–Bernoulli cantilever beam theory để mô tả giới hạn unjammed/jammed của wire structure. Khi trình bày chi tiết equation hoặc assumptions, agent phải mở PDF và cite đúng page/section thay vì chỉ dựa vào `modeling_methods`.  
**PDF:** `papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`.

**What this proves:** wire/fiber jamming để thay đổi bending stiffness đã tồn tại và đã được experimentally demonstrated.

**What this does not prove:** paper không dùng superelastic NiTi làm jamming medium và không đóng active positive-pressure NiTi mechanics.

### Evidence 2 — Zhang & Yao 2026

Zhang & Yao xây dựng positive-pressure fiber-jamming chain, dùng internal bladder để nén fiber bundle và làm three-point bending từ 0 đến 300 kPa. Họ phân chia response thành jamming, transition và slipping regimes, đồng thời cho thấy critical shear forces và slipping-state stiffness/equivalent inertia tăng xấp xỉ tuyến tính với jamming pressure.  
**Source:** Zhang & Yao 2026, DOI `10.5194/ms-17-481-2026`, paper_id `3aa8790db0`, pp. 1, 3–4, 9–11 depending subclaim.  
**Repo:** `data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json`.

**What this proves:** không chỉ wire/fiber jamming đã tồn tại; pressure-controlled fiber-jamming bending mechanics cũng đã được model và experimentally tested.

### Audit consequence

[INFERENCE — AUDIT] Vì C1 chỉ claim broad novelty của “wire/fiber jamming for variable stiffness”, hai full-text sources trên đủ để bác bỏ claim này. C1 bị `closed`. Tuy nhiên, conclusion này không đồng nghĩa với C6/C7 bị closed vì material và coupling mechanics khác.

### Verification box

```text
Primary full-text evidence checked: YES
DOI checked: YES
paper_id checked: YES
Page-level evidence checked: YES
Audit source checked: YES
Inference explicitly labelled: YES
Unresolved source issue: NONE
```

---

# 10. Numerical data rule

Mỗi số phải có source.

Không viết:

> stiffness tăng khoảng 6 lần.

Phải viết:

> Liu et al. báo cáo bending stiffness tăng từ khoảng 0.69 N/mm lên 4.02 N/mm khi input pressure tăng từ khoảng 68/69 kPa lên 172 kPa, tương đương xấp xỉ sáu lần.  
> **Source:** Liu et al. 2021, DOI ..., pp. 1, 4.

Nếu agent tự tính ratio:

```text
4.02 / 0.69 ≈ 5.83
```

phải ghi:

```text
[DERIVATION]
```

và chỉ ra hai input numbers đến từ paper.

---

# 11. Model/equation reporting rule

Nếu report nói:

> Tác giả dùng Euler–Bernoulli beam theory.

thì phải kiểm tra:

- paper page/section;
- equation context;
- assumption.

Nếu report viết một equation cụ thể, phải ghi:

```text
Equation source:
Paper:
Page:
Equation number:
Variables:
Assumptions:
```

Không copy equation từ memory hoặc từ secondary summary mà không kiểm chứng.

---

# 12. Figure/table reporting rule

Nếu figure hoặc table là bằng chứng mạnh:

báo cáo nên ghi:

```text
Figure/Table:
Paper:
Page:
What it shows:
Why it matters to the claim:
```

Không cần chèn hình nếu report không yêu cầu, nhưng phải đủ thông tin để người kiểm chứng mở paper và tìm đúng chỗ.

---

# 13. Contradiction rule

Nếu hai paper có kết quả khác nhau:

không được chọn một paper rồi bỏ paper kia.

Phải viết:

```text
Paper A reports ...
Paper B reports ...
Possible reason for difference ...
Current evidence does not resolve ...
```

Và label phần cuối là `[INFERENCE]` nếu không được authors xác nhận.

---

# 14. Missing-data rule

Nếu repo thiếu:

- page;
- DOI;
- author;
- experiment detail;
- exact equation;
- full text;

agent phải ghi:

```text
UNRESOLVED SOURCE DETAIL
```

và nêu chính xác thiếu gì.

Không được điền bằng đoán.

---

# 15. Recommended report structure

Tên file:

`docs/reports/MP1_DETAILED_CLAIM_EVIDENCE_REPORT_2026-09-25.md`

Structure:

```text
1. Executive summary

2. Evidence methodology
   - source hierarchy
   - full-text vs metadata
   - page verification rule

3. Original mentor architecture

4. C1 detailed audit
5. C2 detailed audit
6. C3 detailed audit
7. C4 detailed audit
8. C5 detailed boundary audit
9. C6 detailed boundary audit
10. C7 detailed boundary audit
11. C8 detailed audit

12. Why MP1-V001 produced PIVOT_TO_MECHANICS_CORE

13. MP1-V002 10-paper mechanics audit
    13.1 T1
    13.2 T2
    13.3 T3

14. Reedlunn 2013 detailed role
15. Fang 2019 detailed role

16. Parameter-substitution kill test

17. Current mechanics core

18. Remaining citation-coverage gaps

19. Kill conditions

20. Source index
    - paper_id
    - title
    - DOI
    - evidence JSON
    - PDF
    - claims/targets supported
```

---

# 16. Reader-comfort rule

Báo cáo phải dễ kiểm chứng, không biến thành “citation wall”.

Cho mỗi claim:

1. nói claim trước;
2. verdict ngay sau;
3. giải thích bằng prose ngắn;
4. sau mỗi evidence paragraph đặt source line;
5. cuối claim có “What it proves / What it does not prove”;
6. cuối claim có verification box.

Không gom 20 citations vào cuối một section khiến người đọc không biết citation nào support câu nào.

---

# 17. Source index format

Cuối report phải có table:

| paper_id | Paper | DOI | Verification round | Evidence JSON | PDF | Used for |
|---|---|---|---|---|---|---|

Ví dụ:

| `240fbf6022` | Bai et al. 2022, *Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming* | `10.3390/app12073582` | MP1-V001 | `data/evidence/...240fbf6022.json` | `papers/verification/MP1-V001/...pdf` | C1, C5 |

---

# 18. Mandatory final self-audit

Trước khi hoàn thành report, agent phải kiểm tra:

```text
[ ] Mọi quantitative claim có paper + page.
[ ] Mọi mechanical claim có full-text evidence.
[ ] Mọi audit verdict có canonical audit source.
[ ] Mọi inference được label.
[ ] Không dùng metadata-only như scientific proof.
[ ] Không nói “novel” từ absence of evidence.
[ ] Không nhầm NiTi tendon/backbone với NiTi jamming medium.
[ ] Không nhầm P1/P2 pressure với P3 active confinement.
[ ] Không nhầm generic hysteresis với variable bending stiffness.
[ ] Không nhầm exact architecture difference với scientific novelty.
[ ] Mỗi claim có “What it does NOT prove”.
[ ] Mọi DOI được kiểm tra từ evidence JSON/PDF.
[ ] Mọi paper_id map đúng title.
[ ] Source index hoàn chỉnh.
```

Nếu bất kỳ box nào chưa đạt, report phải ghi limitation thay vì che đi.

---

# 19. Prompt chuẩn cho reporting agent

Dùng prompt này:

```text
Đọc docs/project/MP1_CLAIM_EVIDENCE_REPORT_TUTOR.md và tuân thủ tuyệt đối.

Hãy tạo báo cáo:
docs/reports/MP1_DETAILED_CLAIM_EVIDENCE_REPORT_2026-09-25.md

Mục tiêu:
giải thích chi tiết và có thể kiểm chứng từng bước vì sao mentor architecture bị thu hẹp từ C1-C8 sang mechanics core hiện tại.

Yêu cầu bắt buộc:
- mỗi scientific fact phải truy được về full-text paper cụ thể;
- ghi title, authors/year, DOI, paper_id, evidence JSON, PDF path;
- mọi quantitative/mechanical claim phải có page hoặc section cụ thể;
- nếu evidence JSON chưa có page, mở PDF để xác minh;
- không đoán page;
- tách VERIFIED PAPER FACT / AUDIT VERDICT / METADATA ONLY / COVERAGE FACT / INFERENCE / DERIVATION;
- với mỗi C1-C8: What it proves + What it does NOT prove + Audit consequence;
- giải thích T1/T2/T3 từ current 10-paper MP1-V002 matrix;
- trình bày riêng Reedlunn 2013 và Fang 2019;
- giải thích parameter-substitution kill test mà không biến “insufficient” thành yes/no;
- không claim universal novelty;
- cuối report phải có source index và mandatory self-audit checklist;
- nếu một statement không có nguồn kiểm chứng cụ thể, bỏ statement hoặc ghi UNRESOLVED SOURCE DETAIL.
```

---

# 20. Relationship với tutor tổng quan

Tutor này dùng cho **claim-level evidence report**.

Tutor tổng quan:

`docs/project/MP1_MENTOR_PIVOT_TUTOR.md`

dùng để truy ngược overall decision lineage.

Khi làm báo cáo cuối tuần chi tiết, agent phải đọc cả hai:

1. `MP1_MENTOR_PIVOT_TUTOR.md` — hiểu toàn bộ logic pivot.
2. `MP1_CLAIM_EVIDENCE_REPORT_TUTOR.md` — chứng minh từng claim bằng nguồn cụ thể.

