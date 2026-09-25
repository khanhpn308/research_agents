# D1 MASTER PLAN REMEDIATION CHECKLIST

## Provenance

- Source plan: outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN.md
- Audit source: outputs/plans/D1_MASTER_PLAN_AUDIT_V1.md
- Audit verdict: MAJOR_REVISION_REQUIRED
- Audit finding counts verified from the audit file:
  - CRITICAL = 4
  - HIGH = 8
  - MEDIUM = 5
  - LOW = 0
- Remediation task: D1-R1
- Scope: plan remediation only; no scientific execution.

## Remediation records

| audit_revision_id | severity | audit_problem | V1_location | V2_change | V2_location | resolved | residual_risk |
|---|---|---|---|---|---|---|---|
| CR-01 | CRITICAL | No state-at-time control or historical state register. | C, D/S2, H, L, M | Add Historical State Register and round coverage; preserve STATE_AT_TIME, CURRENT_CANONICAL_STATE, SUPERSEDED_INTERPRETATION and CORRECTED_INTERPRETATION. | V2 sections 4, 8, 13, 18 | true | Historical source ambiguity still requires human review. |
| CR-02 | CRITICAL | No formal non-novelty or novelty-candidate registers; incomplete categories. | B, H, J, M | Add separate D1_NON_NOVELTY_REGISTER and D1_NOVELTY_CANDIDATE_REGISTER; add eight novelty categories. | V2 sections 5, 6, 14 | true | Category assignment remains a scientific judgment. |
| CR-03 | CRITICAL | No source precedence, provenance chain or contradiction register. | C, G, K, M | Add provenance chain, source precedence, hash/locator validation and D1_CONTRADICTION_REGISTER with blocking rules. | V2 sections 7, 9, 15, 19 | true | Some source conflicts may remain UNRESOLVED and block final adjudication. |
| CR-04 | CRITICAL | No mandatory K1-K9 falsification gate or exact kill states. | J, S6, S7, L | Add D1_K1_K9_FALSIFICATION_MATRIX, direct/partial/unresolved rules and final blocking condition. | V2 sections 10, 16, 20 | true | K-test quality depends on full-text access. |
| HI-01 | HIGH | Claim transitions lack complete source metadata and evidence linkage. | H, S2, S5 | Expand transition schema and require evidence-packet linkage, supersession and confidence fields. | V2 sections 4, 13, 14 | true | Missing historical full text may leave a transition evidence-limited. |
| HI-02 | HIGH | Novelty categories and validation-versus-validity distinction are incomplete. | B, H, S5 | Add full category enum and explicit scientific-contribution versus workflow fields. | V2 sections 3, 6, 14 | true | Boundary between method and question still needs review. |
| HI-03 | HIGH | Prior-art family vocabulary and coverage proof are incomplete. | C, I, S3, S4 | Add family coverage matrix with inclusion, exclusion and unresolved-threat reasons. | V2 sections 3, 12, 15 | true | A new family may require a targeted search trigger. |
| HI-04 | HIGH | Paper packet omits method, experiment, error and mechanism fields. | G, S3 | Expand D1_PAPER_EVIDENCE_PACKETS with all required paper-level fields and locator rules. | V2 sections 11, 15 | true | Metadata-only sources remain limited. |
| HI-05 | HIGH | Search trigger, query logic, synonym expansion and closure are unspecified. | S4, L | Add targeted search protocol, search decision log, dedup/promotion/stop rules and bias controls. | V2 sections 3, 17, 20 | true | No protocol proves global literature absence. |
| HI-06 | HIGH | Worker groups lack DAG, exclusive responsibility and reconciliation contracts. | D, F | Add 12-role registry, dependency graph, allowed/forbidden inference and reconciliation owners. | V2 sections 18, 21 | true | Parallel workers can still disagree; contradiction layer handles this. |
| HI-07 | HIGH | S0 wastes Sol; final high-stakes gate lacks mandatory Astra challenge. | E, S0, S6, S7 | Make S0 deterministic; use Sol synthesis plus Astra High challenge; xHigh only for justified final conflict. | V2 sections 18, 21 | true | xHigh remains conditional on unresolved material disagreement. |
| HI-08 | HIGH | Missing output schemas, threshold freeze and causal-evidence classes. | G-I, L, M, S5-S8 | Add all required schemas, D1_THRESHOLD_FREEZE_RECORD and evidence class fields. | V2 sections 15, 16, 19, 20 | true | Mechanism attribution may remain hypothesis-level. |
| ME-01 | MEDIUM | Execution leakage into M1/R/FE/experiment work. | A, D, O | Add explicit non-execution scope fence. | V2 sections 2, 18 | true | Future users must still respect scope. |
| ME-02 | MEDIUM | No qualitative cost ledger. | E | Add LOW/MODERATE/HIGH/VERY_HIGH estimate per stage. | V2 section 18 | true | Actual vendor cost may vary. |
| ME-03 | MEDIUM | Human review gates lack a structured record. | K | Add D1_HUMAN_REVIEW_RECORD and escalation triggers. | V2 sections 19, 20 | true | Human availability is external. |
| ME-04 | MEDIUM | Stage definitions of done are incomplete. | D, L | Add stage-level acceptance and stop checklist. | V2 section 20 | true | Completeness still depends on evidence access. |
| ME-05 | MEDIUM | Red-team risks are prose-only. | N, S6 | Add D1_RED_TEAM_MATRIX and integrate it with K1-K9. | V2 sections 16, 20 | true | New bias modes may still be discovered during execution. |

## Completion check

- CRITICAL resolved: 4/4
- HIGH resolved: 8/8
- MEDIUM resolved or explicitly dispositioned: 5/5
- LOW findings: 0
- Unresolved CRITICAL/HIGH: 0
- READY_FOR_RE_AUDIT: true

This checklist was created before V2 and is a supporting remediation artifact. It does not execute the D1 scientific audit.
