# Mechanical Research Agents

Repository for an iterative novelty-audit and research-design workflow in mechanical engineering, soft robotics, and vacuum layer jamming.

## Start here

1. Read [`AGENTS.md`](AGENTS.md) for operating rules.
2. Read [`docs/README.md`](docs/README.md) for the documentation map.
3. Use [`docs/project/PROJECT_HANDOFF_CURRENT.md`](docs/project/PROJECT_HANDOFF_CURRENT.md) as the current project entry point.

Do not infer the current research state from old output filenames. Generated verification evidence and historical run artifacts remain under `outputs/`.

## Documentation layout

```text
docs/
├── README.md
├── project/            # Current state, handoff, decision history, roadmaps
├── research_design/    # Model selection, M1 architecture, model comparisons
├── learning/           # Tutorials and paper-reading guides
├── literature/         # Search and literature strategy
├── protocols/          # Verification and audit protocols
└── operations/         # Technical issues and operational notes
```

## Main commands

```bash
python -m app.ingestion.corpus_status
python -m app.ingestion.validate_evidence
```
