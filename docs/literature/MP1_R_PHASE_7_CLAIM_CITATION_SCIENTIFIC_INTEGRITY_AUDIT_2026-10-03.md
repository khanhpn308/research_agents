# MP1-R Phase 7 — Claim–Citation and Scientific-Integrity Audit

## 1. Executive audit verdict

**READY_FOR_PHASE_8_FINALIZATION**

The actual Chapter 2 DOCX was independently audited against the Phase 3–5 authority and the approved original source PDFs. All substantive claim units are traceable and conservatively worded. No Critical or Major scientific-integrity finding remains. The audited DOCX is a byte-preserving copy because no scientific or citation-content rewrite was required; three bibliographic limitations are explicitly retained rather than guessed.

## 2. Audit scope

- DOCX substantive claims audited: **84**
- Phase 6 traceability claims audited: **84 / 84**
- Citation appearances audited: **121 / 121 expected**
- Unique references audited: **18 / 18**
- Tables audited: **4 / 4**
- Equations audited: **1 / 1**
- Subsections audited: **12 / 12**
- Original approved sources reopened: **18**
- Targeted external metadata verifications: **0**
- Broad literature searches: **0**

The 121 appearance count follows the declared rule: one single citation or one citation range counts as one appearance. The DOCX contains 126 raw bracket tokens because five ranges contain two bracketed endpoints; expanding ranges gives 131 reference-number mentions. This is a counting distinction, not a citation-order defect.

## 3. Artifact integrity

The input DOCX was read directly with editable paragraphs, tables, header field and OMML equation inspection. The audited output preserves the original file byte-for-byte:

- Phase 6 input SHA-256: `3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45`
- Phase 7 audited SHA-256: `3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45`
- DOCX opens/readable: **YES**
- A4, Times New Roman, 13 pt body, 1.5 spacing: **PASS**
- Margins top/bottom 3 cm, left 3.5 cm, right 2 cm: **PASS**
- Justification, 1 cm first-line indent, editable headings/tables/equation: **PASS**
- Automatic top-center PAGE field: **PASS**

## 4. Claim–citation results

The 84 traceability units were matched to DOCX text. CH2C018 is correctly represented as an editable OMML equation at P017 and was audited separately. Verdict totals are:

| Verdict | Count |
|---|---:|
| PASS_DIRECT | 13 |
| PASS_SYNTHESIS | 37 |
| PASS_ANALOGY | 3 |
| PASS_PROJECT_AUTHORITY | 31 |
| WEAK_SUPPORT / PARTIAL_SUPPORT | 0 |
| CITATION_MISMATCH / MISSING_CITATION | 0 |
| OVERCLAIM / CAUSAL_OVERREACH | 0 |
| ANALOGY_UPGRADED_TO_EVIDENCE | 0 |
| METRIC_MISMATCH | 0 |
| SOURCE_IDENTITY_ERROR | 0 |

Source claims are bounded to their material, geometry, loading, pressure direction and measurement domain. The prose repeatedly distinguishes evidence from analogy and project inference.

## 5. Scientific-boundary results

The chapter preserves the Phase 5 authority:

- scientific knowledge-gap claims introduced: **0**;
- primary contribution: quantitative pressure-conditioned bending characterization of the defined TiNi bundle with a locked conventional model-discrimination baseline;
- interface/local-slip identification and conventional-model prediction are secondary;
- actuator and integration checks are supporting;
- an additional pressure/contact/material term is conditional only.

No sentence converts a project-specific unresolved relation into a literature-wide absence claim.

## 6. Source-specific audit

S18 is cited only as the corrected 2025 vacuum-confined PVC layer-jamming continuum analogue. S15 and S17 are used as review/context sources within their restrictions. S07 is not used as independent friction calibration. S12 distinguishes physical steel tests from model-based SMA results. V-W02 is presented as numerical modeling precedent, not MP1-R experiment. S22 and S04 retain the limits on inferring normal load and separating μ from N. No S19, S20 or S21 citation appears.

The full targeted source log is in `outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json`.

## 7. Metric/mechanics audit

The DOCX distinguishes F–δ slope, secant stiffness, M–κ tangent/secant rigidity, DMA loss and hysteresis-loop work. It defines the Coulomb relation as a capacity inequality, states the sliding boundary condition separately, and does not infer local N from pressure p. The equation `|Fₜ,ᵢ| ≤ μᵢ Nᵢ` is editable and its symbols are defined immediately after it. The expression ∮M dκ is correctly described as having units N and, for uniform curvature, as work per unit length rather than total specimen energy.

## 8. Causal-chain audit

The chapter preserves the canonical chain:

`fluid pressure → membrane/enclosure response → radial reaction → local wire–wire / wire–sleeve normal forces → friction capacity → slip regime → bending response`

The statuses are not silently upgraded: model-dependent, inferred, not established, model-dependent, model-dependent and partially supported, respectively. The critical weakest link remains the radial-reaction to local-contact-normal-force mapping.

## 9. Gap/contribution audit

Section 2.11 explicitly states that the validated corpus does not justify a general scientific-knowledge-gap claim. It correctly frames pressure/contact transmission, interface attribution and local slip as system-identification requirements; TiNi state activity and conventional-model adequacy as bounded empirical characterization questions; SMA source behavior as engineering validation; and bench comparison as integration validation. No unsupported G1 claim appears.

## 10. RQ/H0/H1 audit

The final section leads to exactly one primary and two secondary questions. No fourth major RQ is introduced. H0a-R and H0b-R remain plausible alternatives; H1-R remains not yet distinguishable and conditional. The chapter states that thesis success does not require H1 and does not require a new constitutive law.

## 11. IEEE citation audit

First appearance order is valid: references [1] through [18] appear in ascending first-use order. All 121 appearance groups use IEEE numeric syntax; all 18 bibliography entries are cited; no author–year citation occurs; no range contains an unsupported intermediate reference by the audited source-role check. The citation matrix is `outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json`.

## 12. Bibliography audit

Bibliographic identities match the cited source files. The following conservative omissions are retained:

1. S05a/S05b [12]–[13] have verified authors, titles, journal, year and DOI, but repository PDFs do not establish final volume/pages.
2. S11 [16] has verified article identifier 04016023 and DOI; volume/issue are not established in the inspected artifact.
3. V-W02 [7] is correctly cited as publisher-verified online-first, Aug. 3, 2021, with no guessed final issue metadata.

Therefore bibliography integrity is **PASS_WITH_CONSERVATIVE_OMISSIONS**, not a failure. Findings P7F001–P7F003 document these limitations.

## 13. Findings and remediation

| ID | Severity | Type | Status |
|---|---|---|---|
| P7F001 | MINOR | S05a/S05b incomplete final pagination metadata | ACCEPTED_LIMITATION |
| P7F002 | MINOR | S11 volume/issue not established locally | ACCEPTED_LIMITATION |
| P7F003 | INFO | V-W02 online-first version metadata | ACCEPTED_LIMITATION |

No claim-support correction was necessary, so the immutable Phase 6 DOCX was not altered. The separate audited DOCX was regenerated and rechecked.

The detailed register is `outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json`; audited traceability is `outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json`.

### Prohibited-claim scan

Literal occurrences of terms such as “duy nhất”, “mới” and “khoảng trống tri thức khoa học” are used only in explicit negations, limits or conditional statements. Substantive prohibited claims found: **0**. Prohibited claims remaining after remediation: **0**.

## 14. Residual limitations

The audit does not establish experimental results for MP1-R. It preserves the evidence boundary that local contact-force mapping, interface dominance, accessed-domain TiNi transformation and held-out model adequacy require future observations. It also preserves the conservative bibliographic omissions above.

## 15. Phase 8 readiness

The DOCX, audit register, finding register, source verification log and citation matrix are complete. No Critical or Major finding remains; IEEE citation integrity is **PASS**; bibliography integrity is **PASS_WITH_CONSERVATIVE_OMISSIONS**; scientific integrity is **PASS**.
