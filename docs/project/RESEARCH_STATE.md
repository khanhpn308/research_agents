# RESEARCH_STATE.md

> **Updated:** 2026-09-26  
> **Machine-readable companion:** `docs/project/research_state.json`  
> **Fast-start snapshot:** `docs/project/CURRENT_EXECUTION_SNAPSHOT.md`

## 1. Research goal

Identify and defend an MSc Mechanical Engineering research direction that is scientifically defensible, mechanically rigorous, experimentally falsifiable, feasible, and publishable. The workflow is adversarial: weak novelty claims are removed rather than protected.

## 2. Historical selected thesis direction

```text
selected_direction = D1_M1
decision           = LOCK_WITH_FEASIBILITY_GATE
confidence         = medium
```

Working title:

> *Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams*

Architecture:

```text
M = Zhang et al. continuum model
R = higher-fidelity full-layer frictional-contact reference
E = independent physical experiment
```

The prior cross-direction decision remains a historical canonical decision, not a substitute for the current mentor-defense audit.

## 3. Current workstream

Current objective:

```text
D1 novelty reconstruction/falsification
+
MP1 lineage reconstruction/falsification
→
fresh mentor-facing comparison after both branches reach their current checkpoints
```

The earlier instruction to immediately begin M1 reconstruction is deferred until this evidence/audit workstream is closed.

## 4. D1 current state

Plan:

`outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V6.md`

Path:

```text
control = outputs/execution/D1/
workers = outputs/d1_execution/V4/
```

Completed:

```text
W01-W08 COMPLETE
```

Latest W08:

```text
papers = 19/19
QA = PASS
direct threat candidates = 1
partial overlap = 8
reconciliation candidates = 3
retrospective threshold risks = 4
model-form ambiguities = 13
contradictions = 0
search reopened = false
```

Next:

```text
W09 / S4
GPT-6 Sol High
Cross-worker reconciliation
```

Expected W09 canonical outputs:

- `D1_PAPER_EVIDENCE_PACKETS.jsonl`
- `D1_CLAIM_EVOLUTION_MATRIX.json`
- `D1_NON_NOVELTY_REGISTER.json`
- `D1_NOVELTY_CANDIDATE_REGISTER.json`

## 5. MP1 current state

Historical MP1-V002 citation coverage:

```text
15/15 directions screened
stop condition = satisfied
```

Macro-stage W02 has now been consolidated:

```text
W02 status = COMPLETE
W2-01...W2-09 = historical subruns consumed
W2-10...W2-12 = not executed / superseded
```

Canonical package:

`outputs/execution/MP1-V002/W2/`

Current scientific state:

```text
H0a = REFUTED_IN_TRANSFORMATION_REGIME
H0b = NOT_FALSIFIED_LIVE_COMPETITOR
H1  = INSUFFICIENT_EVIDENCE

candidate = CONDITIONAL
scientific gate = BLOCKED
blocking gaps = 8
unresolved K tests = K2,K3,K6,K7,K9
```

Next:

```text
MP1-WR1
GPT-6 Sol High
Workflow Reconciliation & Next-Stage Routing
```

## 6. Search state

```text
D1 broad search = CLOSED
MP1 broad search = CLOSED
```

Only reopen through named evidence-first triggers in the active workflow.

## 7. Model allocation at the current checkpoint

```text
D1 W09 reconciliation      = GPT-6 Sol High
MP1 WR1 workflow reconcile = GPT-6 Sol High
D1 W12 adversarial gate    = GPT-6 Astra High later
Astra xHigh                = conditional only for unresolved high-stakes final conflict
```

## 8. Next-session rule

Read `CURRENT_EXECUTION_SNAPSHOT.md` first. Do not follow older "Immediate Next Action" sections in historical documents when they conflict with this current state.
