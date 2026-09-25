# D1 MASTER PLAN RE-AUDIT V4

## Task identity and scope

- Task ID: D1-A4.
- Audit target: outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V4.md.
- Audit type: independent plan re-audit only.
- No scientific workflow was executed.
- No worker was launched.
- No literature search or evidence extraction was performed.
- No D1 novelty verdict was issued.
- MP1 analysis and D1-vs-MP1 comparison were not started.
- V4, V3, A3 and all remediation inputs were left unchanged.

## A. Input artifacts verified

| Artifact | Path | Verification |
|---|---|---|
| Canonical V4 plan | outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V4.md | Read as the final plan file; 91,341 bytes; SHA256 D431901CB7203A15930759D7DA37C95DE170A2F988D7C6F6B151A2B353AF728 |
| D1-A3 re-audit | outputs/plans/D1_MASTER_PLAN_REAUDIT_V3.md | Read directly; SHA256 22A413A738EFD383B67A831B76EAB3A58AC3A862B850B1A29ABA600AA43EE728 |
| V3 finding register | outputs/plans/D1_V3_REAUDIT_FINDING_REGISTER.json | JSON parsed; 14 origin-qualified records |
| V3-to-V4 matrix | outputs/plans/D1_V3_TO_V4_REMEDIATION_MATRIX.json | JSON parsed; 14 records |
| V3-to-V4 matrix rendering | outputs/plans/D1_V3_TO_V4_REMEDIATION_MATRIX.md | Read and compared with JSON |
| Worker readiness matrix | outputs/plans/D1_WORKER_EXECUTION_READINESS_MATRIX.json | JSON parsed; 12 worker records |
| Revision routing matrix | outputs/plans/D1_REVISION_ROUTING_MATRIX.json | JSON parsed; 9 route records |
| Package manifest | outputs/plans/D1_PLAN_PACKAGE_MANIFEST.json | JSON parsed; 12 manifest records |

The temporary overlay and build helper are not present in outputs/plans. They
were not mistaken for the canonical V4 plan.

## B. Canonical V4 artifact identified

The canonical artifact is the single file
outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V4.md. It has V4 metadata,
an explicit V4 precedence statement, the inherited scientific plan, and a V4
control overlay in the same file. It is therefore readable without opening a
separate overlay file.

The integrity limitation is that the same file retains V2/V3 operational
sections, old worker contracts, old hard-gate rows and earlier V3 status
blocks. The V4 statement says the later overlay is authoritative, but the
earlier executable-looking material is not removed or rewritten. This matters
for an implementer who follows the first matching stage, schema or status
block.

## C. D1-A3 finding reconstruction

D1-A3 directly reported:

- remaining D1-A2 Critical: 1;
- remaining D1-A2 High: 2;
- remaining D1-A2 Medium: 3;
- new distinct High: 1;
- new defect rows NEW-MED-01, NEW-MED-02 and NEW-MED-03;
- A3 revision IDs A3-CR-01, A3-HI-01, A3-HI-02 and A3-ME-01.

A3-HI-01 and NEW-HIGH-01 describe the same worker-output-directory defect.
A3-HI-02 is linked to RA-03. The V4 register preserves these aliases and
origin-qualified records, so the audit does not double-count them as separate
scientific threats.

## D. A3 finding-by-finding verification

| finding | severity | V4 claim | actual verification | blocks execution |
|---|---|---|---|---|
| RA-01 / A3-CR-01 | CRITICAL | Post-freeze K changes carry bias and block unqualified survival. | RESOLVED. V4 defines the complete change record, sticky BIAS_RISK, human review and the blocked outcome rule in the V4 K-control section; HG-13 is named as the consumer. | false |
| RA-02 | HIGH | Worker inference and reconciliation contracts are complete. | PARTIALLY_RESOLVED. The required contract fields are present, but the readiness result overclaims runtime structural executability because paths do not exist and required control outputs are missing from worker ownership. | true |
| RA-03 / A3-HI-02 | HIGH | Evidence-first search log and package repair are present. | RESOLVED for the A3 defect: the V4 schema has evidence-first, necessity, OPEN, DO_NOT_OPEN and CLOSE logic, and the malformed literal entry was removed. A naming residual is recorded below. | false alone |
| ME-05 | MEDIUM | Red-team rows identify the attacked candidate. | RESOLVED. V4 adds claim_attacked and candidate linkage. | false |
| RA-04 / A3-NEW-MED-02 | MEDIUM | Review and contradiction statuses are machine-checkable with routes. | PARTIALLY_RESOLVED. The route matrix exists, but its human-review route is still reviewer-specified rather than a deterministic stage/artifact target. | false alone |
| D1-A2 NEW-MED-01 / A3 NEW-MED-01 | MEDIUM | Search decisions are durably recorded. | RESOLVED for evidence-first semantics. The JSON contract exists and is referenced by the V4 plan. | false |
| NEW-LOW-01 | LOW | Packet IDs remain linked to claim transitions. | RESOLVED. | false |
| NEW-HIGH-01 / A3-HI-01 | HIGH | Every worker has a concrete output directory and ownership. | NOT_RESOLVED. All twelve paths are explicit, but Test-Path is false for every path and the matrix still reports execution_ready=true. | true |
| A3-ME-01 / A3-NEW-MED-03 | MEDIUM | Packaging, claim identity and canonical precedence are repaired. | PARTIALLY_RESOLVED. claim_attacked and the manifest exist, but stale V3 controls remain executable-looking and package QA is not represented as complete per-gate rows. | false alone |

## E. Post-freeze K-criterion audit

PASS for the A3 requirement. V4 explicitly defines:

- criterion_before and criterion_after;
- criterion_version_before and criterion_version_after;
- evidence_seen_before_change and evidence description;
- reason_for_change and scientific_justification;
- bias_risk;
- human_review_required and human_review_id;
- approval_status;
- adjudication_consequence.

The plan requires non-NONE bias after evidence exposure, records
final_adjudication_bias_status, prohibits unqualified survival and blocks an
uncleared review. The K-control is consumed by the named HG-13 rule.

No K-test was executed during this audit, so no evidence exposure or actual
criterion-change row is being claimed.

## F. W01-W12 execution-readiness audit

All twelve worker records contain the listed contract fields, explicit paths,
models, reasoning, inference boundaries, owners and definitions of done.
However, two independent readiness failures remain:

1. The twelve directories outputs/d1_execution/V4/W01 through W12 do not
   exist. They are planned strings, not real output destinations.
2. The worker output list does not own or emit all required control artifacts.
   Missing from W01-W12 required_outputs are:

   - D1_HUMAN_REVIEW_CLEARANCE.json;
   - KILL_CRITERION_CHANGE_RECORD.jsonl;
   - D1_K_CRITERIA_REGISTER.json;
   - D1_PRIOR_ART_FAMILY_COVERAGE.json;
   - D1_FINAL_EVIDENCE_MAP.json;
   - FINAL_D1_NOVELTY_ADJUDICATION.json;
   - FINAL_D1_NOVELTY_ADJUDICATION.md;
   - the canonical merged D1_PAPER_EVIDENCE_PACKETS.jsonl.

The readiness matrix reports execution_ready=true for all workers even though
the directories are absent and the missing artifacts have no worker owner.
This fails the independent readiness test. No worker performs final novelty
adjudication by contract, which passes the inference-boundary test.

## G. Search Decision Log audit

The evidence-first logic is operational in prose and in the remediation
schema. A sufficient repository review can return DO_NOT_OPEN, and OPEN
requires a named evidence gap and bounded search fields.

A minor schema residual remains: the V4 row uses databases and
human_review_required, while the A4 audit interface names database/source and
human_review_requirement. The semantics are present, but a strict consumer
must normalize those aliases before machine validation.

## H. Revision Routing Matrix audit

The matrix contains source_gate, return_stage, required_artifact_update,
responsible_owner, reentry_condition and reentry_gate for the K, threshold,
provenance, contradiction, search, worker, threat, human-review and package
triggers.

The worker route returns to “originating worker contract stage” and the human
review route returns to “reviewer-specified stage from this matrix”. Those
phrases are not exact stage/artifact targets. They fail the stress test that
rejects generic return instructions. A human revision can therefore still
re-enter at an ambiguous location.

## I. Package Manifest audit

The seven plan-remediation artifacts exist, have unique names and IDs, and
the manifest reports zero missing required plan artifacts. Owners, consumers,
versions and schema_defined fields are present.

The manifest is not a complete execution package index: future outputs are
aggregated into wildcard and pipe-delimited entries, and the required pairing
rule is represented as a pseudo-artifact whose path is a plan section rather
than a file. This does not affect the seven plan files, but it prevents a
fully granular execution-time package audit.

## J. Canonical V4 integrity audit

Result: PARTIAL.

The V4 file is standalone in the sense that its overlay is inside the file.
The precedence statement is explicit. It nevertheless contains:

- old V2 and V3 stage descriptions;
- old worker contracts without output_directory;
- old V3 search and human-review schemas;
- an old V3 dependency graph;
- historical V3 and V4 final status blocks.

These are labelled as inherited or historical in places, but not every old
table is visibly marked at its point of use. A strict implementer can select
an obsolete schema before reaching the V4 overlay. Canonical integrity is
therefore not fully safe for execution.

## K. Hard Gate Matrix audit

The inherited table gives HG-01 through HG-10, but it lacks the V4
return_route field. HG-11 through HG-15 are named in V4 prose but are not
provided as complete machine rows with required_inputs, machine_check,
pass_condition, fail_condition, return_route, blocked_stage,
human_review_requirement and status.

The V4 plan therefore describes the desired hard gates without delivering one
complete operational hard-gate matrix. This is a blocking high-severity
defect because final readiness and revision routing depend on those rows.

## L. Dependency graph audit

The V4 overlay correctly describes:

criterion definition → freeze → evidence evaluation;
repository evidence → search decision → optional targeted search; and
REVISION_REQUIRED → route → corrected artifact → re-entry gate.

The inherited V3 graph remains in the same canonical file, and the worker
readiness matrix contains a W10 input referring to a W11 criterion-freeze
record while W11 depends on W10. The overlay narrative attempts to split W10
and W11 into passes, but the JSON contract does not fully encode those pass
dependencies. This is a medium dependency-clarity risk.

## M. Threshold-freeze regression test

PASS. The V3 threshold controls remain present, and the V4 overlay preserves
acceptance threshold, validity boundary, breakdown criterion, timing,
uncertainty and data-visibility controls. Retrospective threshold changes are
required to carry bias and human review.

## N. Prior-Art Threat Matrix regression test

PASS at schema level. The V3 threat schema remains concrete, includes overlap
and evidence fields, and states that each row feeds the candidate register
and linked K1-K9 rows. The future worker artifact is not yet populated.

## O. Red-Team Matrix regression test

PASS at schema level. The matrix remains consumed before synthesis, and V4
adds claim_attacked. An open high or critical row is stated to block package
QA. The missing W12 change-record output is a separate readiness defect.

## P. Human-review regression test

PARTIAL. The V4 clearance schema and blocking rule are machine-checkable in
the plan. The required clearance artifact is not among W11 required_outputs,
so the future worker contract cannot actually emit the register consumed by
HG-09 without an unstated extension.

## Q. Model-allocation audit

PASS. Gemini 3.8 Flash High is assigned to bulk extraction, GPT-6 Sol High
to reconciliation and synthesis, GPT-6 Astra High to adversarial critique,
and Astra xHigh only conditionally to unresolved final conflict. No
unnecessary Astra extraction or formatting call is authorized.

## R. Negative-outcome test

PASS. V4 retains FALSIFIED, SUBSTANTIALLY_NARROWED,
SURVIVES_TARGETED_NOVELTY_AUDIT and INCONCLUSIVE. The bias rule can block or
remove survival; the workflow does not force a positive result.

## S. New-defect scan

| defect_id | severity | finding | blocks execution |
|---|---|---|---|
| A4-HI-01 | HIGH | W01-W12 readiness is overstated: output directories do not exist and required control/final artifacts are missing from worker ownership. | true |
| A4-HI-02 | HIGH | HG-01..HG-15 is not delivered as one complete machine-checkable matrix: inherited rows lack return routes and HG-11..HG-15 are prose-only. | true |
| A4-ME-01 | MEDIUM | Human-review and worker revision routes contain generic reviewer/originating-stage destinations instead of exact stage/artifact routes. | false alone |
| A4-ME-02 | MEDIUM | V4 retains obsolete V2/V3 operational tables and duplicate status blocks; precedence is explicit but implementation ambiguity remains. | false alone |
| A4-ME-03 | MEDIUM | Package manifest aggregates future outputs and uses a section-reference pseudo-artifact, limiting granular execution QA. | false alone |
| A4-ME-04 | MEDIUM | Search field aliases databases/human_review_required do not exactly match the A4 interface names database/source/human_review_requirement. | false alone |

No new Critical finding was identified separately from the resolved A3
criterion-bias control.

## T. Final verdict

MAJOR_REVISION_REQUIRED

V4 resolves the A3 post-freeze bias requirement, evidence-first search
logic, named routing artifact and red-team claim identity. It is not safe to
enter execution because the worker readiness claim is false in the current
repository state and the hard-gate matrix is not a complete executable
matrix. The canonical file also retains obsolete executable-looking V3
material.

## U. Remaining nonblocking revisions

After the two blocking High findings are repaired, the plan should:

1. replace generic human and worker return routes with exact stage/artifact
   records;
2. mark inherited V3 sections as historical at their point of use or
   consolidate one canonical schema/stage table;
3. make future package entries granular and file-backed;
4. normalize search field aliases for deterministic consumers.

## V. Exact next action

Do not launch Gemini workers. Return V4 to the remediation architect to repair
A4-HI-01 and A4-HI-02, then independently re-audit the resulting plan. This
audit does not create V5, execute science or modify V4.

# D1 MASTER PLAN RE-AUDIT

MAJOR_REVISION_REQUIRED

# PLAN VERSION AUDITED

V4

# A3 REMAINING CRITICAL FINDINGS RESOLVED

1/1

# A3 REMAINING HIGH FINDINGS RESOLVED

2/2

# A3 REMAINING MEDIUM FINDINGS RESOLVED/ACCEPTABLY_DEFERRED

3/3

# NEW CRITICAL FINDINGS

0

# NEW HIGH FINDINGS

2

# NEW BLOCKING FINDINGS

2

# CANONICAL V4 PACKAGE VALID

false

# W01-W12 STRUCTURALLY EXECUTION-READY

false

# RE-AUDIT REQUIRED AGAIN

true

# READY TO LAUNCH GEMINI WORKERS

false

# NEXT ACTION

REMEDIATE A4-HI-01 AND A4-HI-02, THEN PERFORM INDEPENDENT D1-A5 RE-AUDIT

# MP1 ANALYSIS

NOT PART OF THIS RE-AUDIT

# D1-vs-MP1 COMPARISON

NOT STARTED
