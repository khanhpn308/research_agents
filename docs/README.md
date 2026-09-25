# Documentation Map

The `docs/` tree is organized by function. This file is the navigation entry point; it does not replace the scientific source files.

## Reading order for a new session

1. [`project/PROJECT_HANDOFF_CURRENT.md`](project/PROJECT_HANDOFF_CURRENT.md) — latest concise project handoff and current working direction.
2. [`project/RESEARCH_STATE.md`](project/RESEARCH_STATE.md) — durable research-state narrative.
3. [`project/research_state.json`](project/research_state.json) — machine-readable state.
4. [`project/RESEARCH_LOG.md`](project/RESEARCH_LOG.md) — decision chronology.
5. [`literature/LITERATURE_STRATEGY.md`](literature/LITERATURE_STRATEGY.md) — literature-search and falsification strategy.
6. [`operations/KNOWN_ISSUES.md`](operations/KNOWN_ISSUES.md) — implementation and pipeline cautions.

For the current thesis execution phase, continue with the Vietnamese M1 architecture and reading guide:

- [`research_design/M1_RESEARCH_ARCHITECTURE_VI.md`](research_design/M1_RESEARCH_ARCHITECTURE_VI.md)
- [`learning/ZHANG_CONTINUUM_PAPERS_READING_GUIDE_VI.md`](learning/ZHANG_CONTINUUM_PAPERS_READING_GUIDE_VI.md)

## Functional areas

### `project/` — state, handoff, and roadmap

- `NEXT_SESSION_START_HERE.md`: immediate entry checkpoint for the next session.
- `PROJECT_HANDOFF_CURRENT.md`: current project entry point.
- `MP1_MENTOR_PIVOT_CURRENT.md`: final disposition of mentor-proposed MP1 alternative (viable alternative, not selected).
- `MENTOR_PIVOT_STATUS.md`: historical pre-V001 note.
- `RESEARCH_STATE.md` and `research_state.json`: human- and machine-readable state.
- `RESEARCH_LOG.md`: research decision timeline.
- `POST_D1_V009_RESEARCH_ROADMAP.md`: post-verification roadmap in English.
- `POST_D1_V009_RESEARCH_ROADMAP_VI.md`: post-verification roadmap in Vietnamese.

### `research_design/` — model and thesis architecture

- `EXACT_MODEL_SELECTION.md`: comparison and selection of the reduced model.
- `M1_RESEARCH_ARCHITECTURE.md`: M1–R–E research architecture in English.
- `M1_RESEARCH_ARCHITECTURE_VI.md`: M1–R–E research architecture in Vietnamese.
- `LAYER_JAMMING_MODEL_COMPARISON.md`: cross-model comparison.

### `learning/` — learning and reading material

- `CURRENT_RESEARCH_DIRECTION_TUTORIAL.md`: tutorial on the current direction.
- `ZHANG_CONTINUUM_PAPERS_READING_GUIDE_VI.md`: staged guide for reading the three Zhang continuum papers.

### `vocabularies/` — vocabulary notes by date

- `README.md`: entry format, Cambridge IPA requirement, and daily-file convention.
- `DD-MM-YYYY.md`: all English words asked on the same date, using the `Asia/Bangkok` calendar date.

### `literature/` — literature strategy

- `LITERATURE_STRATEGY.md`: search terms, screening criteria, forward-citation strategy, and search-stop rules.
- `THESIS_READING_LIST_CURRENT_VI.md`: current complete thesis reading set, prioritized by required reading depth and separated from the broader audit corpus.
- `paper_cards/zhang_2025_continuum_beam/paper-card.md`: source-grounded deep-reading card for Zhang et al. (2025), including equations, validation evidence, stated limitations, and project-relevant critique.
- `paper_assessments/`: concise, source-grounded decisions about how individual papers should or should not be used in the current project.

### `protocols/` — audit plans and verification protocols

- `D1-V003_LITERATURE_AUDIT_PLAN.md`
- `D1-V003_VALIDITY_GAP_SEARCH_PROTOCOL.md`
- `D1-V009_LATE_FOUND_ADJACENT_AUDIT_PLAN.md`\n- `MP1_NOVELTY_FALSIFICATION_ROADMAP.md`\n- `MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`\n- `MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`

These files describe how specific verification rounds were designed. Completed results remain under `outputs/verification/` and must not be overwritten.

### `operations/` — technical operations

- `KNOWN_ISSUES.md`: ingestion, schema, provider, deduplication, and environment-variable cautions.

## Authority and preservation rules

- `PROJECT_HANDOFF_CURRENT.md` is the latest concise entry point, but thesis-critical claims must be traced to structured verification evidence and original PDFs.
- `outputs/discovery_snapshot/` and completed `outputs/verification/` rounds are historical evidence, not general documentation folders.
- Historical output manifests and prompts intentionally retain the document paths recorded when those runs were created. They are not rewritten after this reorganization because doing so would alter provenance.
- Moving a document does not change its evidence status, scientific conclusions, or verification verdict.
