# D1 V5→V6 REMEDIATION MATRIX

Source plan: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V5.md`  
Source re-audit: `D1_MASTER_PLAN_REAUDIT_V5.md`  
Target: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V6.md`

Exactly the two A5 blocking High findings are retained. No scientific logic is redesigned.

| audit_revision_id | severity | A5 problem | exact required change | V6 correction | V6 location | resolved | residual risk |
|---|---|---|---|---|---|---|---|
| A5-HI-01 | HIGH | V5 ownership disagreed with worker/stage contracts and omitted several worker outputs. | Establish canonical precedence, complete single-writer graph and ownership QA. | V6 derives ownership from worker/stage contracts, removes W12/S9 and W11/S16 conflicts, adds all output rows and passes zero-conflict QA. | `D1_ARTIFACT_OWNERSHIP_MATRIX_V6.json`; `D1_ARTIFACT_OWNERSHIP_QA_V6.json`; V6 §V6-Ownership | true | Future new artifacts must follow the same rule. |
| A5-HI-02 | HIGH | Worker QA failure returned generically to S16. | Add per-worker failure classes, repair targets, re-entry gates and hard-gate QA. | V6 provides routes for W01-W12 and all required failure classes; S16 is package-only. | `D1_WORKER_FAILURE_ROUTING_MATRIX.json`; `D1_WORKER_ROUTING_HARD_GATE_QA.json`; V6 §V6-Failure-Routing | true | Runtime must use the matrix rather than inventing routes. |

Counts: A5 Critical `0`; A5 High `2`; High resolved `2/2`; unresolved Critical/High `0`.
