# MP1-WR1 canonical handoff

**WR1:** `COMPLETE_ROUTING_ONLY` (2026-09-26, Asia/Bangkok). **Scientific gate:** `BLOCKED`. All eight W02 gaps remain open; WR1 routes them and resolves none experimentally. No new literature search, Astra run, H1/novelty adjudication or D1 comparison occurred.

## Read order

1. [Current execution snapshot](../../../../docs/project/CURRENT_EXECUTION_SNAPSHOT.md) and [machine state](../../../../docs/project/research_state.json).
2. W02 [final state](../W2/MP1_W02_FINAL_STATE.json), [synthesis](../W2/MP1_W02_FINAL_SYNTHESIS.md), [gap register](../W2/MP1_W02_BLOCKING_GAP_REGISTER.json), [K-test matrix](../W2/MP1_W02_K1_K9_RECONCILED_MATRIX.json) and [source manifest](../W2/MP1_W02_SOURCE_MANIFEST.json).
3. WR1 [workflow reasoning](MP1_WR1_WORKFLOW_RECONCILIATION.md), [gap routing matrix](MP1_WR1_GAP_ROUTING_MATRIX.json), [execution graph](MP1_WR1_EXECUTION_GRAPH.json), [stage gates](MP1_WR1_STAGE_GATE_REGISTER.json) and [final state](MP1_WR1_FINAL_STATE.json).

## Exact next execution

`WR1-S01` and `WR1-S02` are independent entry stages and may proceed in parallel. If serial, start S01's inexpensive existing-formulation/H0b audit while preparing the S02 sealed feasibility pilot. Both are **proposed, not executed**. Do not resume W2-10 through W2-12.

S01: examine the named existing cable/contact and NiTi model formulations already in the repository; specify the strongest applicable H0b, observable signatures, calibration/validation partition and any exact missing-equation retrieval trigger. S02: test an instrumented sealed specimen for repeatable simultaneous slip and transformation, local-channel feasibility, thermal/rate effects and integrity. Stop or narrow the current coupling-core question if coexistence or discriminating measurements fail.

After both pass, S03 tests mechanism identifiability and S04 independently calibrates pressure transmission, NiTi, friction, membrane, geometry/prestrain and contact parameters. S05 verifies and locks H0b, parameter files, uncertainty method, held-out paths and tolerances. S06 acquires untouched controlled data. S07 evaluates locked forward predictions and records A (H0b adequate), B (systematic H0b failure correlated with independent local mechanisms, motivating later H1 work), or C (non-identifying/uncertainty dominated). H1 is not established by B.

## Guardrails

H0a = `REFUTED_IN_TRANSFORMATION_REGIME`; H0b = `NOT_FALSIFIED / LIVE COMPETITOR`; H1 = `INSUFFICIENT_EVIDENCE`. H0a false does not imply H1 true. All `GAP-01` through `GAP-08` remain blocking until their specific future pass criteria are met. Chamber pressure is a boundary input, not measured inter-wire normal force. Global moment-curvature loops cannot establish mechanism. Freeze independent calibration before held-out acquisition; any validation refit fails that model version and requires new untouched validation data.

The MP1-V002 citation protocol remains **CLOSED** at 15/15 (9/9 backward, 6/6 forward; 2026-09-25 cutoff), which is not universal novelty proof. No broad search is authorized. A named missing governing equation, material limit or sensing-method feasibility specification may justify bounded targeted retrieval under the [stage register](MP1_WR1_STAGE_GATE_REGISTER.json). Astra is not needed for these stages.
