# D1 V4→V5 REMEDIATION MATRIX

Source plan: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V4.md`  
Source re-audit: `D1_MASTER_PLAN_REAUDIT_V4.md`  
Target: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V5.md`

The A4 report contains exactly two distinct new HIGH findings and no new CRITICAL findings. Linked A3 residuals are preserved in A4 history and are not recounted.

| audit_revision_id | severity | audit_problem | audit_required_change | V1 location | V5 change | V5 location | resolved | residual risk |
|---|---|---|---|---|---|---|---|---|
| A4-HI-01 | HIGH | W01-W12 readiness was overclaimed because declared directories were absent and required control/final artifacts lacked an explicit owner. | Create physical directories, enforce existence/ownership checks, and assign every required output to a worker or named stage. | V4 §38 and `D1_WORKER_EXECUTION_READINESS_MATRIX.json` | Created physical W01-W12 directories, added structural readiness booleans, and assigned worker/stage outputs. | `D1_WORKER_EXECUTION_READINESS_MATRIX_V5.json`; `D1_ARTIFACT_OWNERSHIP_MATRIX.json`; V5 §V5-Workers | true | Runtime contents remain absent until separately authorized execution. |
| A4-HI-02 | HIGH | HG-01-HG-10 lacked return routes and HG-11-HG-15 were prose-only. | Create exactly fifteen complete hard-gate rows with route and re-entry fields, then validate routes. | V4 §41 and A4 §§K,S | Created fifteen gate rows, route-consistency QA and exact versioned re-entry routes. | `D1_HARD_GATE_MATRIX.json/.md`; `D1_HARD_GATE_ROUTING_QA.json`; `D1_REVISION_ROUTING_MATRIX_V5.json`; V5 §V5-Hard-Gates | true | Gate statuses are NOT_REACHED before execution. |

## Count reconciliation

- A4 CRITICAL findings: 0
- A4 HIGH findings: 2
- A4 MEDIUM findings: 4 (nonblocking; retained as residual risks in V5)
- A4 LOW findings: 0
- CRITICAL/HIGH unresolved: 0

Each A4 HIGH finding has exactly one remediation record in the JSON matrix and exactly one row above. No finding is silently dropped.
