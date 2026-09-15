# RESEARCH_STATE.md

## 1. Research Goal

The project is trying to identify an MSc research direction in mechanical engineering / soft robotics that is:

- scientifically defensible
- mechanically rigorous
- experimentally falsifiable
- feasible at MSc level
- plausibly publishable in a WoS/Scopus journal

The workflow is intentionally adversarial:

```text
literature
→ evidence extraction
→ cross-paper reasoning
→ candidate direction
→ adversarial critique
→ adjudication
→ independent verification corpus
→ falsification attempt
→ KEEP / NARROW / PIVOT / REJECT
→ repeat
```

The goal is not to preserve an idea. The goal is to eliminate weak or already-solved ideas.

---

## 2. Discovery Corpus and Pipeline

The original discovery corpus contains:

```text
54 seed papers
```

The discovery pipeline completed:

```text
54 papers
→ evidence extraction
→ literature matrix
→ 9 reasoning batches
→ batch synthesis
→ GPT-5.6 Sol cross-batch reasoning
→ 5 candidate directions
→ Gemini adversarial critique
→ GPT-5.6 Sol final adjudication
```

Discovery outputs were frozen under:

```text
outputs/discovery_snapshot/
```

Key files:
- `literature_matrix_54papers.json`
- `candidate_directions.json`
- `direction_critique.json`
- `final_adjudication.json`

---

## 3. Original Selected Direction: D1

The original final-adjudication title was:

> **Modeling and Experimental Characterization of Interlayer Slip and Bending Stiffness in Vacuum Layer-Jamming Beams**

Vietnamese working title:

> Mô hình hóa và đặc trưng thực nghiệm sự trượt giữa các lớp và độ cứng uốn của dầm kẹt lớp chân không.

Original adjudication:

```text
selected_direction: D1
decision: select_with_revision
confidence: medium
astra_escalation_required: false
```

This result was provisional because novelty had not yet been independently verified.

---

## 4. Why D1 Was Put Under Adversarial Verification

D1 implicitly relied on the idea that meaningful novelty might remain in:

```text
vacuum layer jamming
+ interlayer slip
+ bending stiffness
+ predictive mechanics
+ experimental validation
```

Rather than accept that claim, a separate verification corpus was created.

Verification round:

```text
D1-V001
```

Purpose:

> Find the closest prior work capable of falsifying the central novelty claims of D1.

---

## 5. D1-V001 Verification Corpus

Three independent verification papers were included.

### V1 — Narang et al. (2018)

**Title:** Mechanically Versatile Soft Machines through Laminar Jamming  
**DOI:** `10.1002/adfm.201707136`  
**paper_id:** `5f7ccd7357`

Relevance:
- foundational laminar-jamming mechanics
- vacuum pressure
- friction
- interlayer slip
- pre-slip / transition / full-slip behavior
- modeling + experiment + frictional-contact FEA

### V2 — Caruso et al. (2023)

**Title:** Layer jamming: Modeling and experimental validation  
**DOI:** `10.1016/j.ijmecsci.2023.108325`  
**paper_id:** `652e62758f`

Relevance:
- multilayer vacuum layer jamming
- analytical modeling
- progressive slip
- critical transition loads
- bending stiffness degradation
- three-point bending
- FEA
- experimental validation
- number of layers
- vacuum pressure
- coefficient of friction
- hysteresis / frictional dissipation

This is the closest direct prior work to D1.

### V3 — Atakuru et al. (2024)

**Title:** Layer Jamming of Magnetorheological Elastomers for Variable Stiffness in Soft Robots  
**DOI:** `10.1007/s11340-024-01031-7`  
**paper_id:** `56d058a34a`

Relevance:
- pre-slip / partial-slip / full-slip behavior
- frictional-contact FEA
- three-point bending
- slip initiation
- layer-count effects
- shows transfer of slip mechanics to another jamming actuation regime

---

## 6. D1-V001 Result

`verify_direction.py` was run using GPT-5.6 Sol at high reasoning effort.

Result:

```text
verification_verdict: PIVOT
confidence: high
```

The system concluded that D1's central contribution is substantially closed.

### Claims judged already solved

The verification result judged the following central claims as already solved or substantially addressed:

1. A predictive framework for pressure/friction/interlayer-slip transitions in vacuum layer-jamming beams.
2. Experimental validation of slip onset and bending-stiffness behavior against mechanics models.
3. Characterization of quasi-static hysteresis associated with interlayer slip.

### Important negative conclusion

Do **not** claim novelty merely from:
- another sheet material
- another envelope
- another geometry
- another pressure range
- edge tracking
- held-out tests
- more FEA
- more experiments

unless they create a new mechanics question.

### Fatal novelty conflicts

The strongest conflicts were:
- Narang et al. (2018)
- Caruso et al. (2023)

---

## 7. Current Provisional Pivot: P1

GPT-5.6 Sol proposed:

> **Validity Limits of a Homogenized Slip Model for High-Layer-Count Vacuum-Jammed Beams**

This is a **provisional pivot candidate**, not a verified topic.

### What P1 is trying to study

Instead of representing every discrete layer and every frictional interface individually, P1 asks whether a high-layer-count layer-jamming stack can be represented by a reduced / continuum / homogenized mechanics model that still captures the important effects of slip.

The scientific question is not merely:

> Can a homogenized model be built?

It is:

> Under what conditions is the simplified model valid, and where does it fail?

Potential variables:
- layer count
- vacuum pressure
- friction coefficient
- layer thickness
- curvature
- bending load
- slip regime

Potential outputs:
- global bending stiffness
- force-deflection response
- slip evolution
- hysteresis
- model prediction error
- validity / breakdown map

---

## 8. P1 Is NOT Yet Safe

The verification result itself said that the three-paper corpus was insufficient to establish that high-layer-count homogenization remains novel.

Recent literature has already revealed serious threats.

### Critical threat — Zhang et al. (2025)

**Title:** A continuum-based model for a layer jamming beam  
**Journal:** Mechanical Sciences  
**DOI:** `10.5194/ms-16-821-2025`

Why this matters:
- directly uses a continuum-based model
- directly studies a layer-jamming beam
- targets large layer counts / continuous-medium representation
- includes FEA and experimental validation

This paper may substantially close or force a further narrowing of P1.

### Important threat — Zhang et al. (2025)

**Title:** Toward a deeper understanding of layer jamming structures  
**DOI:** `10.1007/s11465-025-0843-5`

Relevant themes:
- large deformation
- complex loading
- layer thickness
- hydrostatic pressure
- cyclic loading
- FEA
- experimental validation

### Important 2026 paper

**Title:** Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots  
**Authors:** Yeman Fan, Bowen Yi, Dikai Liu  
**Journal:** IEEE Transactions on Control Systems Technology  
**Year:** 2026  
**DOI:** `10.1109/TCST.2026.3690756`

This paper must be screened because it is recent and directly related to layer-jamming modeling and stiffness regulation, although it may be more control-focused than homogenization-focused.

---

## 9. Other Important Prior Work to Screen

### Caruso et al. (2022)

**Title:** A theoretical model for multi-layer jamming systems  
**Journal:** Mechanism and Machine Theory  
**DOI:** `10.1016/j.mechmachtheory.2022.104788`

### Caruso et al. (2022)

**Title:** An Analytical Model for Cantilever Layer-Jamming Structures

Also seen during search:
- Comprehensive model of laminar jamming variable stiffness driven by electrostatic adhesion
- Behavior of layer jamming plate with tunable stiffness and its near wake structure in cross flow
- An enhanced soft growing robot with mixed-layer jamming for superior load capacity and improved mobility

These are search candidates until screened and verified.

---

## 10. Current Corpus Status

Latest clean state before the next verification round:

```text
Total papers: 57

seed: 54
verification: 3

D1-V001: 3 papers

screening:
included: 57
pending: 0

ingestion:
complete: 57
pending: 0
failed: 0

evidence:
present: 57
missing: 0

consistency: PASS
```

---

## 11. Next Verification Round

Do not overwrite `D1-V001`.

Recommended next round:

```text
D1-V002
```

Purpose:

> Attack P1 using the newest 2025–2026 closest prior work.

Core verification question:

> Has recent literature already developed and experimentally validated a continuum / homogenized / equivalent model for high-layer-count layer-jamming beams, including interlayer slip mechanics and the model's limits of validity?

Possible verdicts remain:

```text
KEEP
NARROW
PIVOT
REJECT
```

---

## 12. Current Stop / Rejection Logic

Reject or pivot P1 if later literature already provides:

```text
high / large layer count
+
continuum / homogenized / equivalent representation
+
interlayer slip mechanics
+
experimental validation
+
validity / breakdown limits
```

Also reject P1 if the only benefit of the proposed model is computational speed and no new mechanics question or breakdown criterion emerges.

---

## 13. Immediate Next Action

The next task is **not** to defend P1.

The next task is:

1. systematically collect 2025–2026 closest prior work;
2. perform forward-citation tracking of Narang 2018 and Caruso 2023;
3. export / deduplicate citation metadata;
4. screen the strongest threats;
5. ingest selected full-text papers into `D1-V002`;
6. build a new verification matrix;
7. run adversarial verification again.

Current working principle:

> **If the literature kills P1, pivot again.**
