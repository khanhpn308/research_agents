# WP-C locator issues

## Non-blocking

1. P0 reports printed pages as `NOT_REPORTED` for all new WP-C PDFs.
2. The following 16 anchors are normalized phrases whose literal PDF text differs because of line wrapping, OCR/symbol encoding, or bilingual glyph extraction: `M25-E06`, `M25-E11`, `M27-E24`, `M27-E16`, `M28-E15`, `M28-E16`, `M29-E01`, `M29-E03`, `M29-E04`, `M29-E06`, `M30-E01`, `M30-E04`, `M30-E05`, `M35-E11`, `M35-E37`, `M35-E53`. Their physical PDF page, source section and figure/equation locator were checked; do not treat the short anchor as a verbatim quotation.
3. M29 equation glyphs are bilingual/visually dense; p3 was rendered and equations (8)–(18) were visually confirmed. Perform a final typography check before thesis quotation.
4. M35 is an encrypted thesis PDF with text extraction limitations; section/page anchors were checked, but figure-local numbering should be confirmed visually.
5. M25/M27/M28 plotted values are configuration-specific; no digitization was performed.
6. M23 locators (M23-E01 through M23-E10): all exact text anchors, source sections, equations (1)–(4), (10)–(19), (25), (26)–(28), and figures/tables were verified directly from the canonical 15-page PDF text and page layout.

## Blocking

- None. M23 identity mismatch is CLOSED under P0-R2 with verified hash `1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a`; full scientific extraction and locator verification are COMPLETED.
