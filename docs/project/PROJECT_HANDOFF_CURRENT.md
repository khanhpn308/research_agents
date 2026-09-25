# PROJECT HANDOFF — CURRENT RESEARCH STATE

> **Updated:** 2026-09-26  
> **Fast-start:** `docs/project/CURRENT_EXECUTION_SNAPSHOT.md`  
> **Purpose:** handoff for a new chat/agent. Historical thesis decisions remain preserved, while the current workstream is the mentor-defense evidence reconstruction.

## 1. High-level thesis state

Historical repository decision:

```text
selected_direction = D1_M1
decision           = LOCK_WITH_FEASIBILITY_GATE
confidence         = medium
```

Working title:

> **Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams**

The selected direction remains conditional. The later thesis feasibility gate still requires M1 reconstruction, a credible full-layer reference, predeclared metrics/tolerances, uncertainty accounting and an experimentally resolvable accepted/rejected contrast.

However, the immediate workstream has changed from "start the pilot" to:

```text
reconstruct D1 novelty lineage
+
reconstruct MP1 scientific lineage
+
finish their current controlled audits
→
prepare a fresh mentor-facing comparison
```

## 2. D1 branch — live execution state

Authority:

- `outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V6.md`
- `outputs/plans/D1_WORKER_EXECUTION_READINESS_MATRIX_V6.json`

Path semantics:

```text
control root = outputs/execution/D1/
worker root  = outputs/d1_execution/V4/
plan         = V6
```

The `V4` worker path is intentional historical namespace under Plan V6.

Completed:

```text
W01-W08 = COMPLETE
```

Latest canonical extraction:

`outputs/d1_execution/V4/W08/D1_PAPER_EVIDENCE_SHARD_W08.jsonl`

Latest receipt:

`outputs/d1_execution/V4/W08/W08_EXECUTION_RECEIPT.json`

W08: 19/19 papers, QA PASS across packet/validity/model-form/threshold/uncertainty/provenance; 1 direct-threat candidate; 8 partial overlaps; 3 reconciliation candidates; 4 retrospective-threshold risks; 13 model-form ambiguities; no contradiction; no search reopen.

Immediate next action:

```text
W09 / S4 CROSS-WORKER RECONCILIATION
model = GPT-6 Sol
effort = High
```

W09 must merge W03-W08 into canonical evidence packets, claim evolution, non-novelty register and novelty-candidate register. It is not the final novelty adjudicator.

Downstream:

```text
W09 Sol
→ W10 conditional targeted search only on a valid trigger
→ W11 QA
→ W12 Astra High adversarial K1-K9
→ S14/S15 final D1-only synthesis/adjudication
```

## 3. MP1 branch — live execution state

Historical MP1-V002 citation protocol is still closed at 15/15 required directions and does not prove universal novelty.

A later MP1 execution workflow produced historical subruns W2-01 through W2-09. The architecture was then corrected because W02 had been incorrectly expanded as a mandatory W2-01→W2-12 chain.

Canonical consolidated closeout:

`outputs/execution/MP1-V002/W2/`

State:

```text
W02 = COMPLETE
W2-01...W2-09 = consumed historical subruns
W2-10 = not executed
W2-11 = not executed
W2-12 = not executed
old sequential architecture = SUPERSEDED
Astra W2-09 incorporated = true
```

Scientific reconciliation:

```text
H0a = REFUTED_IN_TRANSFORMATION_REGIME
H0b = NOT_FALSIFIED_LIVE_COMPETITOR
H1  = INSUFFICIENT_EVIDENCE
candidate status       = CONDITIONAL
scientific gate        = BLOCKED
blocking gaps          = 8
unresolved K-tests     = K2,K3,K6,K7,K9
```

Immediate next action:

```text
MP1-WR1
Workflow Reconciliation & Next-Stage Routing
model = GPT-6 Sol High
```

It must consume the W02 closeout, design the correct next execution graph, and must not continue W2-10/W2-12 by inertia.

## 4. Mentor-facing objective

The project must ultimately show the mentor:

- exactly how D1 changed under prior-art attacks and which residual novelty candidate survives;
- exactly how MP1 changed from the mentor's broad architecture to a narrow conditional mechanics/model-discrimination question;
- why any final preference between them follows from evidence, falsifiability, identifiability and execution risk rather than ownership of the idea.

The final mentor-facing comparison is **not started yet** in the current workflow.

## 5. Search rules

```text
D1 broad search  = CLOSED
MP1 broad search = CLOSED
```

Only reopen through explicit workflow triggers. A negative search result never proves global novelty.

## 6. Canonical read order

1. `docs/project/CURRENT_EXECUTION_SNAPSHOT.md`
2. `docs/project/research_state.json`
3. `outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V6.md`
4. `outputs/d1_execution/V4/W08/W08_EXECUTION_RECEIPT.json`
5. `outputs/execution/MP1-V002/W2/MP1_W02_HANDOFF.md`
6. `outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json`
7. `outputs/execution/MP1-V002/W2/MP1_W02_BLOCKING_GAP_REGISTER.json`
8. `docs/project/RESEARCH_LOG.md`
9. historical source-level reports/JSON/PDF when a claim must be defended.

## 7. Do not

Do not rename the D1 V4 worker namespace; do not rerun completed workers without a formal return route; do not run MP1 W2-10/W2-12; do not use Astra for routine merge/extraction; do not claim global novelty from citation closure; do not start the final D1-vs-MP1 mentor comparison before the live branches reach their designated checkpoints.
