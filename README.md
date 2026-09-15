# Mechanical Research Agents — Context Pack

Copy these files into the root of your `mechanical-research-agents` repository.

Recommended layout:

```text
mechanical-research-agents/
├── AGENTS.md
└── docs/
    ├── RESEARCH_STATE.md
    ├── RESEARCH_LOG.md
    ├── LITERATURE_STRATEGY.md
    ├── KNOWN_ISSUES.md
    └── research_state.json
```

Recommended agent loading sequence:

1. Read `AGENTS.md`
2. Read `docs/RESEARCH_STATE.md`
3. Read `docs/research_state.json`
4. Read the remaining docs only when needed

For the first session after loading, ask the agent to reconstruct the current state and identify ambiguities before it makes any research decision.
