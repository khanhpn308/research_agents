# D1 V3→V4 REMEDIATION MATRIX

Source plan: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V3.md`
Source re-audit: `D1_MASTER_PLAN_REAUDIT_V3.md`
Target: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V4.md`

Every origin-qualified finding is retained exactly once; A3 aliases are explicit and not silently dropped.

| audit_revision_id | origin | severity | V4 change | V4 location | resolved | residual risk |
|---|---|---|---|---|---|---|
| D1_A2:RA-01 | D1_A2 | CRITICAL | Added KILL_CRITERION_CHANGE_RECORD_V4, final_adjudication_bias_status, prohibited outcome rule, and blocked state for unresolved review. | V4 §§36.2-36.4, §40 | True | A bias-qualified outcome can still be scientifically weaker than a fresh pre-evaluation rerun; the plan therefore preserves INCONCLUSIVE and SUBSTANTIALLY_NARROWED routes. |
| D1_A2:RA-02 | D1_A2 | HIGH | Reissued the full W01-W12 contract and readiness matrix with unique output directories and ownership. | V4 §37.1-37.4 | True | Structural readiness does not mean a worker has been launched; launch remains explicitly false until re-audit. |
| D1_A2:RA-03 | D1_A2 | HIGH | Added the full evidence-first search log, state machine, no-search rows, and package validation rules. | V4 §38, §42 | True | A targeted search remains bounded and cannot establish global absence; unresolved source access still blocks a survival claim. |
| D1_A2:ME-05 | D1_A2 | MEDIUM | Added claim_attacked and a candidate-ID referential-integrity check. | V4 §40.3, §42 | True | Attack rows may still use OTHER attack_type when a new failure mode is discovered. |
| D1_A2:RA-04 | D1_A2 | MEDIUM | Added deterministic revision routing with owner and re-entry predicates. | V4 §39, §41 | True | A human reviewer may still reject a revision, which correctly keeps the dependent stage blocked. |
| D1_A2:NEW-MED-01 | D1_A2 | MEDIUM | Completed the durable log schema and package QA rule. | V4 §38, §42 | True | No search result is generated in plan remediation; the log remains a future execution artifact. |
| D1_A2:NEW-LOW-01 | D1_A2 | LOW | Preserved and machine-validated evidence_packet_ids in the V4 worker and package contracts. | V4 §37.2, §42 | True | An unavailable packet remains explicitly unavailable and cannot support survival. |
| D1_A3_NEW:A3-CR-01 | D1_A3_NEW | CRITICAL | Resolved through the same control family as RA-01; this linked residual remains separately auditable. | V4 §§36.2-36.4, §40 | True | Deduplicated with RA-01 for primary severity counts; no unqualified survival is permitted. |
| D1_A3_NEW:NEW-HIGH-01 | D1_A3_NEW | HIGH | Assigned unique V4/W01-W12 output directories and machine readiness checks. | V4 §37.2-37.4, §42 | True | The directories are planned locations; no worker is launched in this task. |
| D1_A3_NEW:A3-HI-02 | D1_A3_NEW | HIGH | Completed the log, added no-search records, and replaced the artifact list with a manifest-backed canonical list. | V4 §38, §42 | True | The search gate remains conditional and cannot be used for open-ended discovery. |
| D1_A3_NEW:A3-ME-01 | D1_A3_NEW | MEDIUM | Added routing and package manifest controls; V4 §§36 onward are the sole authoritative execution overlay. | V4 §§39-42 | True | V3 historical duplication remains visible for provenance but cannot be used as an execution control. |
| D1_A3_NEW:NEW-MED-01 | D1_A3_NEW | MEDIUM | Resolved under A3-HI-02 and RA-03. | V4 §38 | True | Execution must populate the row before any search opens. |
| D1_A3_NEW:NEW-MED-02 | D1_A3_NEW | MEDIUM | Resolved under A3-ME-01 and RA-04. | V4 §39, §41 | True | Reviewer rejection remains blocking by design. |
| D1_A3_NEW:NEW-MED-03 | D1_A3_NEW | MEDIUM | Resolved under A3-ME-01 with manifest and canonical-overlay rules. | V4 §40.3, §42 | True | Historical V3 text remains visible but is explicitly non-authoritative for execution. |

## Required record fields

`audit_revision_id`, `severity`, `audit_problem`, `audit_required_change`, `V1_location`, `V2_change`, `V2_location`, `V3_location`, `V4_change`, `V4_location`, `resolved`, `residual_risk`, `re_audit_required`.

## Count reconciliation

- D1-A2 remaining Critical: 1/1 resolved.
- D1-A2 remaining High: 2/2 resolved.
- D1-A2 remaining Medium: 3/3 resolved or acceptably deferred.
- D1-A2 remaining Low: 1/1 resolved.
- Distinct A3 new High: 1/1 resolved; the search-log High is linked to RA-03.
- New blocking findings unresolved: 0.

No worker, search or scientific evidence workflow was executed.
