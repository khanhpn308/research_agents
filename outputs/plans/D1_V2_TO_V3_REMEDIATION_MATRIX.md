# D1 V2 TO V3 REMEDIATION MATRIX

Source plan: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V2.md`
Source re-audit: `D1_MASTER_PLAN_REAUDIT_V2.md`
Target: `D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V3.md`
Status: all remaining Critical, High and Medium findings resolved in V3; pending independent D1-A3 re-audit.

| finding_id | origin | severity | exact V3 correction | V3 location | blocking | resolved |
|---|---|---|---|---|---|---|
| RA-01 | ORIGINAL_AUDIT | CRITICAL | Add individually frozen K1-K9 criteria, change records and all-row hard gate. | V3 §§24, 29-30 | true | true |
| RA-02 | ORIGINAL_AUDIT | HIGH | Add full W01-W12 inference contract, reconciliation/QA owners and W04 extraction/reconciliation split. | V3 §25, §§30-31 | true | true |
| RA-03 | ORIGINAL_AUDIT | HIGH | Add concrete threat, red-team, search, threshold and clearance schemas with gate validation. | V3 §§26-30, §32 | true | true |
| ME-05 | ORIGINAL_AUDIT | MEDIUM | Add structured D1_RED_TEAM_MATRIX and require S14/S16 consumption. | V3 §27, §§30-32 | true | true |
| RA-04 | NEW_REAUDIT_FINDING | MEDIUM | Add human clearance, contradiction statuses and machine blocking. | V3 §29, §30 | true | true |
| NEW-MED-01 | NEW_REAUDIT_FINDING | MEDIUM | Add named D1_SEARCH_DECISION_LOG and package validation. | V3 §§25, 30, 32 | false | true |
| NEW-LOW-01 | NEW_REAUDIT_FINDING | LOW | Add evidence_packet_ids to claim transitions. | V3 §25, §32 | false | true |

## Counts

- Remaining Critical findings resolved: 1/1.
- Remaining High findings resolved: 2/2.
- Remaining Medium findings resolved or bounded: 3/3.
- Remaining Low findings resolved: 1/1.
- Unresolved blocking findings: 0.
- Ready for re-audit: true.
- Ready to launch Gemini workers: false by instruction; D1-A3 must decide.
