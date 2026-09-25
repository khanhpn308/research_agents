# MP1-E1-W2-09 — Astra High Adversarial Red-Team Prompt

## ROLE

You are the independent Astra High adversarial red-team for MP1.

## MODEL

GPT-6 Astra

Reasoning effort: HIGH

This is one independent Astra call. Do not replace it with Gemini, Sol, or a parallel extraction worker.

## TASK

Audit the current MP1 candidate and the W2-08 K1–K9 kill-gate outputs adversarially.

The objective is to try to falsify, materially narrow, or expose a logical or provenance failure in the surviving MP1 mechanics candidate. Do not defend MP1 and do not treat the absence of a kill as evidence of global novelty.

## SCOPE LOCK

This is an adversarial red-team task only.

Do not:

- search the web or reopen literature search;
- add papers;
- modify canonical scientific files;
- modify W2-01 through W2-08 outputs;
- perform D1 analysis;
- compare D1 with MP1;
- write a mentor-persuasion report;
- issue the final MP1 adjudication;
- perform human sign-off;
- silently resolve contradictions;
- declare `SURVIVES_TARGETED_NOVELTY_AUDIT`.

Create outputs only under:

```text
outputs/execution/MP1-V002/W2-09/
```

## AUTHORITATIVE INPUTS

Read the completed W2 execution outputs:

```text
outputs/execution/MP1-V002/W2-01/
outputs/execution/MP1-V002/W2-02/
outputs/execution/MP1-V002/W2-03/
outputs/execution/MP1-V002/W2-04/
outputs/execution/MP1-V002/W2-05/
outputs/execution/MP1-V002/W2-06/
outputs/execution/MP1-V002/W2-07/
outputs/execution/MP1-V002/W2-08/
```

At minimum inspect:

```text
outputs/execution/MP1-V002/W2-07/MP1_NON_NOVELTY_REGISTER.json
outputs/execution/MP1-V002/W2-07/MP1_NOVELTY_CANDIDATE_REGISTER.json
outputs/execution/MP1-V002/W2-07/MP1_UNRESOLVED_THREAT_REGISTER.json
outputs/execution/MP1-V002/W2-07/MP1_CONTRADICTION_REGISTER.json
outputs/execution/MP1-V002/W2-07/MP1_PROVENANCE_QA.json
outputs/execution/MP1-V002/W2-08/MP1_KILL_TEST_MATRIX.json
outputs/execution/MP1-V002/W2-08/MP1_KILL_GATE_DECISION.json
outputs/execution/MP1-V002/W2-08/W2_08_BLOCKING_THREATS.json
```

Also inspect:

```text
outputs/verification/MP1-V002/verification_matrix.json
outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json
outputs/verification/MP1-V002/citation_coverage.json
outputs/verification/MP1-V002/FINAL_ADJUDICATION.json
outputs/verification/MP1-V002/FINAL_ADJUDICATION.md
docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md
docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md
docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md
```

Use original PDFs only when they are already present in the repository. Do not acquire new sources.

## ADVERSARIAL QUESTIONS

Try to falsify or narrow the candidate on every relevant axis:

1. H0 logic — Is rejection of H0a being improperly treated as support for H1? Is H0b still a viable competitor?
2. H0b sufficiency — Could an independently calibrated transformation-aware NiTi constitutive model plus ordinary contact/Coulomb friction explain the response?
3. Coexistence — Is there an accessible regime where inter-wire slip and stress-induced NiTi transformation occur simultaneously and materially?
4. Identifiability — Can the proposed measurements distinguish friction, transformation, contact redistribution, temperature, prestrain, geometry and cycle history?
5. Pressure interpretation — Is active pressure only an external boundary/control variable? Is chamber pressure independently mapped to internal normal force?
6. Parameter leakage — Were parameters measured or frozen before validation, or tuned post hoc? Does H1 only fit better because it has more free parameters?
7. Prior art — Does any existing source in the locked corpus already cover the claimed combination of NiTi bundle, contact/slip, confinement, bending and comparable outputs?
8. Citation overreach — Is `15/15` citation coverage being misused as proof of global novelty or H1?
9. Historical drift — Are historical states, superseded interpretations and current canonical state being confused?
10. Evidence integrity — Are Carboni S2a/S1a, Reedlunn, Fang, pressure-role and paper-count interpretations correct?
11. Kill-gate integrity — Did W2-08 correctly classify K1–K9, blocking threats and unresolved tests?
12. Candidate wording — Is the candidate still broader than the evidence supports? Rewrite it narrower when necessary.

## REQUIRED CHALLENGE RECORD

For every challenge record, include:

```text
challenge_id
target_claim_or_register_row
affected_claim_ids
affected_target_ids
affected_hypothesis_ids
attack_statement
evidence_supporting_attack
counter_evidence
source_files
paper_ids
severity
disposition
required_remediation
blocking
human_review_required
residual_risk
evidence_status
confidence
provenance
```

Allowed `severity` values:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Allowed `disposition` values:

```text
CONFIRMED_GAP
MAJOR_CHALLENGE
MINOR_CHALLENGE
NO_CHALLENGE_FOUND
UNRESOLVED
```

## REQUIRED RED-TEAM OUTPUTS

Create exactly these files:

```text
outputs/execution/MP1-V002/W2-09/W2_09_ASTRA_RED_TEAM_REPORT.md
outputs/execution/MP1-V002/W2-09/MP1_ASTRA_RED_TEAM_CRITIQUE.json
outputs/execution/MP1-V002/W2-09/MP1_ASTRA_RED_TEAM_CRITIQUE.md
outputs/execution/MP1-V002/W2-09/MP1_RED_TEAM_CHALLENGE_REGISTER.json
outputs/execution/MP1-V002/W2-09/MP1_RED_TEAM_CHALLENGE_REGISTER.md
outputs/execution/MP1-V002/W2-09/W2_09_CONTRADICTION_CANDIDATES.json
outputs/execution/MP1-V002/W2-09/W2_09_SOURCE_MANIFEST.json
```

Do not create a final evidence map or final adjudication.

## SOURCE MANIFEST

For every inspected source record:

```text
source_path
source_type
repository_commit
date_accessed
role_in_red_team
claims_or_tests_supported
evidence_status
notes
```

Do not invent commit IDs, page numbers, DOIs, equations, figures or results.

## FINAL QA

Before completion verify:

- the red-team is based on W2-08 outputs;
- every K1–K9 result was challenged or explicitly marked not challengeable;
- critical and high challenges are clearly separated;
- unresolved contradictions remain visible;
- H0a rejection was not converted into H1 support;
- H0b was not declared false without direct evidence;
- citation closure was not treated as global novelty;
- no new literature search occurred;
- no paper was added;
- no D1 analysis occurred;
- no D1-vs-MP1 comparison occurred;
- no human sign-off occurred;
- no canonical file was modified;
- final adjudication was not performed.

## FINAL RESPONSE FORMAT

Return:

```text
A. Sources inspected
B. Candidate and K1–K9 challenged
C. Critical challenges
D. High challenges
E. Confirmed gaps
F. Unresolved issues
G. Required remediation
H. Residual risk
I. QA result
J. Output files created
K. Exact next dependency
```

End exactly with:

```text
WORKER
=
W2-09

TASK
=
ASTRA HIGH ADVERSARIAL RED-TEAM

MODEL
=
GPT-6-ASTRA

STATUS
=
COMPLETE / BLOCKED

NEW_LITERATURE_SEARCH
=
false

NEW_PAPERS_ADDED
=
false

FINAL_NOVELTY_ADJUDICATION
=
NOT PERFORMED

D1_ANALYSIS
=
NOT PERFORMED

D1-vs-MP1_COMPARISON
=
NOT PERFORMED

HUMAN_SIGN_OFF
=
NOT PERFORMED

CANONICAL_FILES_MODIFIED
=
false

NEXT_DEPENDENCY
=
W2-10 — FINAL SOL SYNTHESIS
```

