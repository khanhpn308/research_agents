# P2 Pilot R1 locator verification report

## Method

All 26 Evidence Records were re-read against the P0 canonical paths and SHA-256 values. The 16 records whose prior anchors did not match literal extracted text were checked on their cited PDF pages; high-risk equation/figure pages were rendered and visually inspected. No P0/P1 or PDF file was modified.

## Results

- Evidence records checked: 26/26.
- Prior unmatched anchors checked: 16/16.
- Locator verified by text: 9 of the 16 remediated records.
- Locator verified by rendered visual/text inspection: 7 of the 16 remediated records.
- Locator corrections: 2 page corrections and 14 anchor normalizations; see `LOCATOR_CORRECTIONS.csv`.
- Claim–source mismatches: 0.
- All records now carry `locator_verification_status`; no record remains `LOCATOR_NOT_VERIFIED`.
- All canonical SHA-256 values match `SOURCE_REGISTRY.json`.

## Important corrections

- **M18-E06:** physical PDF page corrected from 7 to 8; Fig. 7 and its ±1σ comparison are on p8.
- **M22-E06:** physical PDF page corrected from 9 to 8; p9 is the references page, while the Conclusions section is on p8.
- Other changes shorten anchors to exact phrases that survive PDF line wrapping/symbol extraction; scientific findings were not changed.

## Equation/Figure/Table check

The 8 equation entries and 11 figure/table entries were reconciled against the cited page/caption ranges. M17 Fig. 2, M18 Fig. 7, M22 Figs. 4–5 and M26 Figs. 2–3/6–7/14–15 received rendered-page checks.

Printed-page labels are retained as `NOT_REPORTED` where the article’s PDF does not provide a stable integer convention; this is a locator-format issue for later human citation, not a source mismatch.
