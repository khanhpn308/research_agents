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

1. `docs/README.md`
2. `docs/project/PROJECT_HANDOFF_CURRENT.md`
3. `docs/project/RESEARCH_STATE.md`
4. `docs/project/research_state.json`
5. `docs/project/RESEARCH_LOG.md`
6. `docs/literature/LITERATURE_STRATEGY.md`
7. `docs/operations/KNOWN_ISSUES.md`

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

## File-First Research Output Policy

**Terminal output is an execution interface, not the primary archive of research results.**

For substantial research tasks, long analyses, literature reviews, scientific comparisons, model deconstruction, novelty audits, verification reports, research planning, or other durable research work:

1. The complete deliverable MUST be written to a persistent file.
2. Preferred destinations:
   - `docs/` for durable human-readable research notes, explanations, learning documents, methodological guides, and thesis-oriented material.
   - `outputs/` for generated pipeline results, machine-generated analyses, verification outputs, matrices, adjudications, and run-specific artifacts.
3. The terminal/chat response MUST NOT be the only copy of a substantial research result.
4. For long research tasks, terminal output should normally contain only:
   - `SUCCESS` / `PARTIAL` / `FAILED`
   - output file path(s)
   - short execution summary
   - important warnings
   - unresolved evidence gaps
5. Do not dump the complete research report into the terminal when a persistent Markdown or structured output file is appropriate.
6. Markdown (`.md`) is the default human-readable format unless another format is explicitly required.
7. Scientific reports should be self-contained and, where applicable, contain:
   - research question or objective
   - evidence status
   - analysis
   - equations with symbol definitions
   - assumptions and limitations
   - citations
   - references
   - provenance
   - unresolved questions or evidence gaps
8. Every important scientific claim must remain traceable to its evidence. Clearly distinguish:
   - `VERIFIED FULL TEXT`
   - `METADATA ONLY`
   - `INFERENCE`
9. Never invent:
   - citations
   - DOI values
   - page numbers
   - equation numbers
   - figure numbers
   - section names
   - experimental results
   - bibliographic metadata
10. When exact source provenance is available in repository evidence, preserve it in the generated research file.
11. A durable research file should be suitable for:
    - later agent sessions
    - supervisor discussion
    - thesis literature review
    - research proposal development
    - Git history / diff inspection
    - reconstruction of project context
12. Before reporting `SUCCESS` for a file-first research task:
    - confirm the output file exists
    - confirm it is non-empty
    - reopen/read it
    - verify required sections exist
    - verify no important content exists only in terminal output
13. Do not modify scientific state, registry state, verification state, or historical outputs merely to satisfy the file-first rule.
14. If the user explicitly requests terminal-only output, follow that request unless doing so would conflict with a higher-priority repository safety or preservation rule.

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

## Vocabulary Logging Policy

When the user asks for the meaning of an English word during paper reading:

1. Answer in Vietnamese with the meaning, contextual nuance, an English example with Vietnamese translation, and related word forms.
2. Include American-English IPA verified against Cambridge Dictionary for both the headword and every listed related word form; link each term's own Cambridge entry. Do not infer or guess an unverified IPA.
3. Append the entry to `docs/vocabularies/DD-MM-YYYY.md`, using the `Asia/Bangkok` calendar date. Reuse the same file for every word asked on that date and preserve existing entries.
4. Follow `docs/vocabularies/README.md`. Present each word with headings, compact tables, and prose rather than a bullet-list definition.

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
