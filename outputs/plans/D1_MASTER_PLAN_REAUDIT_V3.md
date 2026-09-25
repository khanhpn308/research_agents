# D1 MASTER PLAN RE-AUDIT V3

## Task identity and scope

- Task ID: D1-A3.
- Audit target: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V3.md` only.
- No scientific workflow was executed.
- No Gemini, Sol or Astra worker was launched for evidence work.
- No literature search or evidence extraction was performed.
- MP1 analysis, D1-vs-MP1 comparison and mentor reporting were not performed.
- V1, Audit V1, V2, Re-Audit V2, V3 and all remediation matrices were left unchanged.

## A. Input artifacts verified

The following were read before issuing this verdict:

| Artifact | Path | Verification |
|---|---|---|
| D1 Master Plan V2 | `outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V2.md` | Read in full; SHA256 `A4797F765A5BD7C5561707238B9A9BF1420DF8F2BA0A1438D66D93D8F114BD34` |
| D1 Independent Re-Audit V2 | `outputs/plans/D1_MASTER_PLAN_REAUDIT_V2.md` | Read in full; authoritative D1-A2 findings recovered |
| D1 Master Plan V3 | `outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V3.md` | Read in full; SHA256 `947B41571AFDCA55BF2EC5F3E908EE940AB536D560586796AB611160B921964D` |
| V2 re-audit finding register | `outputs/plans/D1_V2_REAUDIT_FINDING_REGISTER.json` | JSON parsed; 7 records |
| V2 to V3 matrix JSON | `outputs/plans/D1_V2_TO_V3_REMEDIATION_MATRIX.json` | JSON parsed; 7 records |
| V2 to V3 matrix Markdown | `outputs/plans/D1_V2_TO_V3_REMEDIATION_MATRIX.md` | Read in full |
| D1 Master Plan V1 / Audit V1 | Earlier plan artifacts | Inspected to check that inherited controls were not lost |

The V2 hash is unchanged. The repository still contains D1-V001 through D1-V009 and the existing dirty-worktree state. No V3 modification was made by this audit.

## B. D1-A2 finding reconstruction

D1-A2 reported one remaining Critical finding, two remaining High findings, and three remaining Medium findings. The counts below agree with the authoritative D1-A2 final block. The independent verification is:

| finding_id | severity | D1-A2 problem | required change | claimed V3 resolution | actual V3 location | verification result | residual risk | blocks execution |
|---|---|---|---|---|---|---|---|---|---|
| RA-01 | CRITICAL | K1-K9 criteria were generic and could be changed after evidence; high-significance was undefined. | Freeze per-test criteria before evaluation, preserve changes, record bias and block unsafe adjudication. | Nine per-test YAML criteria, freeze fields, change record and HG-04/HG-05. | V3 §§24, 29-30 | PARTIALLY_RESOLVED | A post-freeze change with human approval is recorded, but V3 does not explicitly force the final adjudication to recognize criterion leakage or prohibit survival after such a change. | true |
| RA-02 | HIGH | Worker contracts lacked inference boundaries and reconciliation ownership; W04 Flash/Sol boundary was ambiguous. | Add complete W01-W12 contracts and reconciliation/QA owners. | Expanded contract table and W04 split. | V3 §25, §§30-31 | RESOLVED | A named output-directory field is still absent; this is a new execution-readiness finding below. | false for RA-02; new defect remains |
| RA-03 | HIGH | Threat/red-team schemas and temporal threshold controls were incomplete; search log was not a persistent artifact. | Add concrete schemas, timing fields and gate consumers. | Threat/red-team/threshold/search/clearance schemas and S10-S16 graph. | V3 §§26-30, §32 | PARTIALLY_RESOLVED | Search log schema does not record evidence-first checking, reason search is necessary, or the requested DO_NOT_OPEN/CLOSE decision vocabulary; the deliverables list contains a malformed literal `\n` sequence. | true |
| ME-05 | MEDIUM | Red-team artifact was prose-capable. | Add a concrete row schema and machine acceptance. | JSON schema, W12 output, S14/S16 consumption. | V3 §27, §§30-32 | RESOLVED | `candidate_claim_id` functions as claim identity, but an explicit `claim_attacked` alias would improve clarity. | false |
| RA-04 | MEDIUM | Human review and contradiction status were not machine-checkable. | Add sign-off states, contradiction status vocabulary and blocking logic. | Clearance schema and contradiction control. | V3 §29-30 | RESOLVED | `REVISION_REQUIRED` has no explicit route-to-stage rule. | false for RA-04; new defect remains |
| NEW-MED-01 | MEDIUM | Search decisions were not a named durable artifact. | Add a named search decision log and package validation. | `D1_SEARCH_DECISION_LOG` is named and emitted by W10/S10. | V3 §§25, 29-32 | PARTIALLY_RESOLVED | The artifact exists, but its fields do not capture all required decision provenance. | false by itself; contributes to RA-03 |
| NEW-LOW-01 | LOW | Claim transition lacked a dedicated packet ID. | Add `evidence_packet_ids`. | V3 transition override. | V3 §§25, 32 | RESOLVED | Unavailable packets still require explicit status. | false |

The remediation register is complete as an inventory, but its `resolved_in_V3=true` values overstate the three partial resolutions above.

## C. Remaining Critical finding verification

**RA-01: PARTIALLY_RESOLVED and blocking.** V3 does define each K1-K9 with the requested criterion fields, `criterion_frozen_at`, `criterion_frozen_before_evidence_evaluation=true`, version and a `KILL_CRITERION_CHANGE_RECORD` containing old/new criterion, evidence already seen, bias risk and human approval. This passes the basic freeze test.

The stress test exposes a missing hard rule. If K4 has been inspected and a worker tries to loosen the criterion, V3 requires a change record and human approval. If approval is absent, the test becomes `UNRESOLVED` and blocks. If approval is present, however, V3 does not require the final evidence map/adjudication to carry a `BIAS_RISK` classification or prohibit a survival verdict. The final gate can therefore treat the approved change as ordinary criteria evolution. Criterion leakage remains possible.

## D. Remaining High findings verification

**RA-02: RESOLVED as a D1-A2 finding.** Every V3 worker row supplies role, scientific question, exclusive scope, inputs, outputs/schema, dependencies, parallelization, allowed and forbidden inference, must-not-conclude, reconciliation owner, QA owner, human trigger, model and reasoning. Extraction roles cannot issue a final novelty verdict. W04 extraction is separated from W09/Sol reconciliation, and W05-W08 disagreements flow to W09 and W11.

**RA-03: PARTIALLY_RESOLVED and blocking.** V3 adds concrete threat, red-team, threshold and human-clearance schemas, and the graph consumes them. The search log is still incomplete for a defensible audit: there is no `existing_evidence_checked_first`, no `reason_search_is_necessary`, no explicit `decision = OPEN | DO_NOT_OPEN | CLOSE`, and no field that records a no-search decision. The artifact list also contains a literal `\\n-` sequence at the deliverable insertion, which can produce an invalid package entry.

## E. Remaining Medium finding verification

- **ME-05: RESOLVED.** The red-team matrix has a concrete schema, attack-type vocabulary, W12 ownership and S14/S16 consumption.
- **RA-04: RESOLVED for the original requirement.** Human clearance has PENDING/CLEARED/BLOCKED sign-off and required reviews block downstream stages. Contradiction statuses are enumerated and critical open/blocked rows fail HG-03.
- **NEW-MED-01: PARTIALLY_RESOLVED.** The search log is durable and named, but the decision provenance fields required by the D1-A3 stress test are absent.

## F. K1-K9 operational audit

Each K1-K9 block contains `kill_test_id`, question, candidate claim, scope, conceptual equivalence, direct-kill, partial-overlap, no-kill and unresolved criteria, required evidence, evidence quality, source precedence, repository sources, search trigger, human trigger, definition/freeze fields, version, verdict space and confidence. The nine tests are individually present.

The answer to the freeze stress test is only conditionally safe:

- Before evidence: criteria are frozen at S9 and S10 is the first classification stage.
- After evidence, a change record is mandatory and the old criterion/evidence/bias risk/human approval are retained.
- Without approval: the test is unresolved and blocked.
- With approval: V3 lacks an explicit rule that the final adjudication must mark criterion leakage as `BIAS_RISK` and disallow an unqualified survival verdict.

Therefore K1-K9 are structurally operational but not fully safe under post-freeze modification. This keeps RA-01 blocking.

## G. Worker-contract audit

The contract schema and W01-W12 table contain the requested inference controls. The following forbidden inferences are explicit: absence of a discovered paper to global novelty, abstract-only evidence to full mechanics, correlation to causation, better fit to new mechanics, rejected null to accepted alternative, and citation coverage to scientific closure.

Extraction workers are forbidden from issuing the final novelty verdict. W09 reconciles packets and W12 performs adversarial tests; S14/S15 own synthesis/adjudication.

A separate execution-readiness defect remains: no worker contract contains `output_directory`, and no worker row defines a concrete per-worker output directory. The package lists filenames but does not bind each W01-W12 output to a directory. Under the D1-A3 launch test, this means no worker is fully launch-ready even though the scientific contract fields are present.

## H. Reconciliation ownership audit

The normal conflict path is operational:

```text
W05/W06/W07/W08 disagreement
→ W09 Sol reconciliation
→ D1_CONTRADICTION_REGISTER / W11 QA
→ human clearance when thesis-critical
→ W12 adversarial integration
→ S14 synthesis
```

The paper-level evidence packet, source precedence and worker disagreement types are available. A direct-threat versus partial-overlap conflict therefore has a named owner, evidence inputs and a contradiction artifact. The missing `REVISION_REQUIRED` route means a human can block the stage without a defined return target; this is a Medium process defect, not a failure of ordinary disagreement ownership.

## I. Prior-Art Threat Matrix audit

**PASS.** V3 §26 defines all required fields: identity, metadata, family, reason, conceptual/system/mechanism/model/method/validation/question/domain overlap, high-fidelity reference, experiment, validity map, breakdown test, model-form error, mechanism, proves/does-not-prove, direct/partial flags, K links, evidence locator/status/confidence, review and disposition.

The matrix is not standalone: W10 emits it, S7/S10 consume it, and V3 states that each threat row feeds both the candidate register and linked K1-K9 rows. This satisfies the direct-consumer requirement.

## J. Red-Team Matrix audit

**PASS WITH A CLARITY PATCH.** V3 §27 defines `D1_RED_TEAM_MATRIX`, all required attack types, evidence/counter-evidence, logical failure, dependencies, outcome, Astra assessment, Sol reconciliation, human review, resolution, residual risk and status. S14 must consume every High/Critical row and S16 rejects an open blocking row.

`candidate_claim_id` identifies the claim attacked, but the schema does not carry a separate `claim_attacked` field. This is not a blocking scientific gap because the candidate ID is stable, but it is a minor schema clarity issue.

## K. Threshold Freeze audit

**PASS.** V3 §28 records metric, physical meaning, use, justification, uncertainty, acceptance and breakdown thresholds, validity boundary, breakdown criterion, defined/frozen stages, pre-validation timing, data visibility, version and change record. The hard rule sets `BIAS_RISK`, blocks survival classification and requires human review when validation data were seen before freeze.

This is machine-checkable through HG-06 and S16. The inherited V2 threshold section remains visible, but V3 §28 is the binding temporal register under the explicit V3 precedence note.

## L. Human Review Clearance audit

**PASS WITH A ROUTING GAP.** V3 §29 defines `D1_HUMAN_REVIEW_CLEARANCE` with all requested fields and the hard rule that required review with sign-off other than CLEARED blocks the dependent stage. A K7 KILL with no sign-off cannot reach S14 or S15.

For `decision = REVISION_REQUIRED`, V3 stops the dependent stage but does not specify the return stage, artifact revision owner or re-entry condition. The plan cannot silently continue, but the execution route is incomplete.

## M. Hard Gate Matrix audit

**PASS.** HG-01 through HG-10 cover historical completeness, provenance, contradiction clearance, K criterion freeze, K resolution, threshold freeze, prior-art threat completion, red-team completion, human review and final readiness. Each lists inputs, pass/fail condition, blocked stage, machine-checkable flag and human-clearance requirement. Initial status is OPEN and S16 computes status; gates cannot be bypassed by prose.

## N. Dependency graph S0-S16 audit

**Result: PARTIAL.** The graph is acyclic and orders provenance/contradiction controls before K criteria freeze, targeted evaluation, threshold freeze, red-team, human clearance and final adjudication. No bypass around the named gates is present in the graph.

Every scientific artifact has a downstream consumer. The plan-level worker contract artifact itself is listed for packaging, but its concrete output directory is absent. The old inherited S0-S13 graph and new S0-S16 graph coexist; the V3 precedence statement resolves their authority, but duplicating two execution graphs creates avoidable implementation ambiguity.

## O. Source-precedence audit

**PASS.** V3 preserves PDF > evidence JSON > AI summary for paper facts, latest valid canonical JSON > stale narrative for current state, and historical state rows after later correction. Contradictions remain explicit and critical unresolved contradictions block final adjudication.

## P. Search Decision Log audit

**PARTIAL; contributes to RA-03.** V3 adds a named `D1_SEARCH_DECISION_LOG` and makes S10 conditional on a trigger. It records search ID, trigger, question, query family, terms, synonyms, database/source, date, screening, deduplication, promotion, stop, human trigger, closure and status.

It does not record: existing repository evidence checked first, reason the search is necessary, an explicit `DO_NOT_OPEN` decision, or the fact that no search was opened. Search-bias protection is therefore stated but incompletely auditable.

## Q. Model/reasoning audit

**PASS.** Gemini Flash High is reserved for inventory/history/packet work; Sol High performs reconciliation and synthesis; Astra High performs K-test/red-team attacks; Astra xHigh is conditional only for a final material conflict. No unnecessary Astra extraction or schema population was introduced.

## R. Execution-readiness audit W01-W12

| worker group | contract fields | output schema | inference controls | reconciliation/QA owner | dependencies | output directory | launch-ready |
|---|---|---|---|---|---|---|---|
| W01-W12 | present | present by artifact name | present | present | present | absent | NO |

The same missing `output_directory` field affects every worker. The package has filenames but not per-worker output locations or ownership paths. Because the D1-A3 rule requires every worker's output directory to be defined, W01-W12 cannot be marked launch-ready.

## S. Negative-outcome test

A direct prior-art kill can reach `KILL` in a K-test, trigger human review, enter the threat/candidate registers and produce `FALSIFIED` or `SUBSTANTIALLY_NARROWED` in the allowed outcome space. Insufficient evidence can remain `UNRESOLVED` and be classified `INCONCLUSIVE` after the hard gate. V3 does not structurally force survival.

The caveat is criterion leakage: a post-freeze change approved without an explicit final bias flag could weaken the integrity of a survival result. This is why the plan is not approved for execution.

## T. New defect scan

| defect_id | severity | defect | result | blocks execution |
|---|---|---|---|---|
| NEW-HIGH-01 | HIGH | Worker readiness requires an output directory, but V3 defines no `output_directory` field or per-worker output path. | NOT_RESOLVED | true |
| NEW-MED-01 | MEDIUM | `D1_SEARCH_DECISION_LOG` lacks evidence-first, reason-necessary and explicit OPEN/DO_NOT_OPEN/CLOSE decision fields. | NOT_RESOLVED | false alone; contributes to RA-03 |
| NEW-MED-02 | MEDIUM | `REVISION_REQUIRED` blocks but has no route-back stage, owner or re-entry condition. | NOT_RESOLVED | false alone |
| NEW-MED-03 | MEDIUM | Red-team schema has candidate claim identity but no explicit `claim_attacked`; the artifact list contains a literal `\n-` insertion and inherited/new execution sections are duplicated. | INTRODUCED_NEW_RISK | false alone |
| RA-01-RESIDUAL | CRITICAL | A human-approved post-freeze K-criterion change is recorded but final adjudication is not explicitly forced to carry criterion-leakage bias risk or block unqualified survival. | Counted under RA-01; not a new finding. | true |

No new Critical finding was identified separately from RA-01. NEW-HIGH-01 is the only distinct new High-level execution-control defect. The search-log defect remains counted under RA-03, and criterion leakage remains counted under RA-01.

## U. Final verdict

**MAJOR_REVISION_REQUIRED**

V3 is materially stronger than V2 and passes the core schema, provenance, threat, red-team, threshold, source-precedence and negative-outcome checks. It is not safe to enter execution because:

1. post-freeze K-criterion changes are not guaranteed to appear as bias-risk in final adjudication;
2. W01-W12 have no defined output directories, so the launch-readiness contract fails for every worker;
3. the search log, revision routing and deliverable packaging have remaining auditability gaps.

## V. Remaining revisions

| revision_id | severity | exact required change | affected area | re-audit |
|---|---|---|---|---|
| A3-CR-01 | CRITICAL | For any post-freeze criterion change, set `BIAS_RISK`, preserve the old criterion and evidence set, require human approval, and prohibit an unqualified `SURVIVES_TARGETED_NOVELTY_AUDIT`; route the candidate to `INCONCLUSIVE` or a fresh pre-evaluation version. | K1-K9, KILL_CRITERION_CHANGE_RECORD, HG-04/HG-05, S14-S15 | true |
| A3-HI-01 | HIGH | Add `output_directory` and `artifact_owner` to every W01-W12 contract, bind each output to a concrete path under the execution package, and make S16 validate path existence and ownership. | Worker contract, §32, S16 | true |
| A3-HI-02 | HIGH | Complete `D1_SEARCH_DECISION_LOG` with `existing_evidence_checked_first`, `reason_search_is_necessary`, `decision = OPEN|DO_NOT_OPEN|CLOSE`, and no-search records; repair the malformed deliverable entry and make S16 reject it. | Search schema, §32, S10/S16; residual RA-03 | true |
| A3-ME-01 | MEDIUM | Add return-stage/owner/re-entry fields for `REVISION_REQUIRED`; add explicit `claim_attacked`, remove duplicate ambiguity or mark one graph/schema authoritative, and correct the literal `\n` package entry. | Human clearance, red-team, package QA | recommended before launch |

## W. Exact next action

Do not launch Gemini workers. Remediate A3-CR-01 through A3-ME-01 in a new plan version without modifying V1, Audit V1, V2, Re-Audit V2, V3 or the existing remediation matrices. Then perform a new independent re-audit. Scientific execution remains blocked until the new re-audit confirms worker launch readiness.

## Final status block

D1 MASTER PLAN RE-AUDIT
=
MAJOR_REVISION_REQUIRED

PLAN VERSION AUDITED
=
V3

D1-A2 REMAINING CRITICAL FINDINGS RESOLVED
=
0/1

D1-A2 REMAINING HIGH FINDINGS RESOLVED
=
1/2

D1-A2 REMAINING MEDIUM FINDINGS RESOLVED/ACCEPTABLY_DEFERRED
=
2/3

NEW CRITICAL FINDINGS
=
0

NEW HIGH FINDINGS
=
1

NEW BLOCKING FINDINGS
=
1

RE-AUDIT REQUIRED AGAIN
=
true

READY TO LAUNCH GEMINI WORKERS
=
false

NEXT ACTION
=
Remediate A3-CR-01 through A3-ME-01 in a new plan version, then perform an independent re-audit

MP1 ANALYSIS
=
NOT PART OF THIS RE-AUDIT

D1-vs-MP1 COMPARISON
=
NOT STARTED



