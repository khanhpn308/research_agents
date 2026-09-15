# AGENTS.md

## Project Purpose

This repository implements an iterative scientific novelty-audit pipeline for MSc research in mechanical engineering / soft robotics.

Primary research domain:
- soft robotics
- variable stiffness
- layer / laminar jamming
- continuum robots
- soft grippers
- mechanics modeling
- experimental validation

## Core Research Principle

**DO NOT DEFEND THE CURRENT IDEA. TRY TO FALSIFY IT USING THE CLOSEST PRIOR WORK.**

A research direction must survive independent literature verification before it is treated as a defensible candidate.

Do not treat any of the following as scientific novelty by themselves:
- different geometry
- different material
- different robot platform
- different experimental apparatus
- more pressure levels
- more FEA
- more measurements
- held-out testing alone

These only matter if they expose a new, testable mechanics question or a clearly unresolved scientific limitation.

## Required Context Before Any Research Decision

Read these files in this order:

1. `docs/RESEARCH_STATE.md`
2. `docs/research_state.json`
3. `docs/RESEARCH_LOG.md`
4. `docs/LITERATURE_STRATEGY.md`
5. `docs/KNOWN_ISSUES.md`

Do not infer the current project state from old output filenames alone.

## Current Research State

- Original selected direction: `D1`
- Completed verification round: `D1-V001`
- Latest verified verdict: `PIVOT`
- Confidence: `high`
- Current provisional pivot candidate: `P1`
- P1 has **not** been validated as novel.
- Immediate objective: attack P1 using the newest 2025–2026 closest prior work and forward citations.

## Current Provisional Pivot Candidate

**P1**

> Validity Limits of a Homogenized Slip Model for High-Layer-Count Vacuum-Jammed Beams

Treat P1 as a hypothesis, not a conclusion.

## Source-of-Truth Outputs

Discovery snapshot:
- `outputs/discovery_snapshot/literature_matrix_54papers.json`
- `outputs/discovery_snapshot/candidate_directions.json`
- `outputs/discovery_snapshot/direction_critique.json`
- `outputs/discovery_snapshot/final_adjudication.json`

Completed verification:
- `outputs/verification/D1-V001/verification_matrix.json`
- `outputs/verification/D1-V001/direction_verification.json`
- `outputs/verification/D1-V001/direction_verification.md`

Do not overwrite completed verification rounds.

## Model Roles

Recommended model allocation:
- bulk extraction / screening: Gemini Flash-class model
- adversarial critic: Gemini critic model
- cross-paper scientific reasoning: GPT-5.6 Sol
- final adjudication: GPT-5.6 Sol
- Astra: only if there is unresolved conflict after evidence expansion

Current Codex research config:
- `CODEX_RESEARCH_MODEL=gpt-5.6-sol`
- `CODEX_RESEARCH_EFFORT=high`

Use `CODEX_RESEARCH_EFFORT`; do not introduce a second env name unless the codebase is intentionally migrated.

## Operating Rules

1. Never claim novelty from the discovery corpus alone.
2. Keep discovery and verification corpora separate.
3. Verification papers must be linked to a verification round.
4. New evidence must be able to cause `KEEP`, `NARROW`, `PIVOT`, or `REJECT`.
5. If a claim is already solved, say so explicitly.
6. If evidence is insufficient, mark it as uncertain instead of inventing a gap.
7. Prefer primary papers and full text for novelty judgments.
8. Preserve DOI, title, year, paper_id, and provenance.
9. Do not overwrite `D1-V001`.
10. Before changing P1, inspect the newest closest prior work first.

## Main Commands

```bash
python -m app.ingestion.corpus_status
python -m app.ingestion.validate_evidence

python -m app.ingestion.add_paper   "PATH_TO_PDF"   --type verification   --verification-id D1-V002

python -m app.ingestion.screen_paper   --id PAPER_ID   --decision include   --reason "..."

python -m app.ingestion.ingest_papers

python -m app.ingestion.build_verification_matrix   --verification-id D1-V002

python -m app.ingestion.verify_direction   --verification-id D1-V002
```

## Immediate Next Task

Build the next verification round around the strongest 2025–2026 threats to P1, especially continuum / homogenized / constitutive / reduced-order models for layer-jamming beams.

Do not continue by defending P1.
