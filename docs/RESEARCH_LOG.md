# RESEARCH_LOG.md

## Research Decision Timeline

### Phase 0 — Broad orientation

Research domain narrowed toward:
- soft robotics
- variable stiffness
- soft grippers
- continuum robots
- jamming-based stiffening
- mechanics + experimental validation

### Phase 1 — Discovery corpus

Built a 54-paper seed corpus.

Completed:
- paper registry
- screening
- evidence extraction
- validation
- literature matrix
- 9 reasoning batches
- batch synthesis

### Phase 2 — Candidate generation

GPT-5.6 Sol produced five candidate research directions.

D1 was provisionally recommended.

### Phase 3 — Adversarial critique

Gemini adversarial critic reviewed all candidate directions.

Shortlist:
- D1
- D2

Recommended:
- D1

### Phase 4 — Final adjudication

GPT-5.6 Sol compared D1 vs D2.

Result:

```text
selected: D1
decision: select_with_revision
confidence: medium
astra_required: false
```

Working title:

> Modeling and Experimental Characterization of Interlayer Slip and Bending Stiffness in Vacuum Layer-Jamming Beams

### Phase 5 — External verification begins

The project explicitly stopped treating the 54-paper discovery corpus as sufficient proof of novelty.

A separate verification corpus was created.

Verification round:
- `D1-V001`

### Phase 6 — D1-V001

Added and screened:
- Narang et al. 2018
- Caruso et al. 2023
- Atakuru et al. 2024

Built:
- verification matrix
- direction verification output

### Phase 7 — D1 falsified as a broad novelty claim

GPT-5.6 Sol verification result:

```text
verdict: PIVOT
confidence: high
```

Main reason:
- core pressure–friction–slip mechanics already modeled
- bending-stiffness evolution already modeled
- slip transitions already characterized
- experimental validation already performed
- hysteresis / energy dissipation already studied

Strongest conflicts:
- Narang 2018
- Caruso 2023

### Phase 8 — Pivot candidate P1

New provisional direction:

> Validity Limits of a Homogenized Slip Model for High-Layer-Count Vacuum-Jammed Beams

Status:
- provisional
- not novelty-verified
- must be attacked, not defended

### Phase 9 — New threats discovered

Recent papers discovered during forward-citation / Scholar search:

1. Zhang et al. 2025 — *A continuum-based model for a layer jamming beam*
2. Zhang et al. 2025 — *Toward a deeper understanding of layer jamming structures*
3. Fan et al. 2026 — *Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots*

These papers have not yet been fully integrated into a new verification round.

### Phase 10 — Current next step

Create / populate `D1-V002` and attempt to falsify P1.

Do not overwrite `D1-V001`.
