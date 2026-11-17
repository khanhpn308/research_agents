# Locator readiness

Convention: `pdf_page` is physical PDF page index starting at 1. `printed_page` was not inferred where the PDF did not expose a reliable first-page printed number.

| ID | PDF pages | Printed page | Sections | Figures | Tables | Equations | Exact text | Visual render | P2 locator status |
|---|---:|---|---|---|---|---|---|---|---|
| M01 | 116 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M02 | 20 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M03 | 25 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M04 | 12 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M05 | 19 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | False | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M06 | 28 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | False | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M07 | 9 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M08 | 12 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | False | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M09 | 14 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M10 | 8 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M11 | 6 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | False | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M12 | 11 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | False | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M13 | 13 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M14 | 11 | NOT_DETERMINED_AUTOMATICALLY | False | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M15 | 7 | NOT_DETERMINED_AUTOMATICALLY | False | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M16 | 15 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M17 | 10 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M18 | 10 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M19 | 16 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M20 | 9 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M21 | 13 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M22 | 9 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M23 | 10 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | False | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M24 | 13 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M25 | 15 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M26 | 18 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M27 | 37 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M28 | 19 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M29 | 8 | NOT_DETERMINED_AUTOMATICALLY | True | False | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M30 | 5 | NOT_DETERMINED_AUTOMATICALLY | False | True | False | False | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M31 | 8 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M32 | 12 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M33 | 11 | NOT_DETERMINED_AUTOMATICALLY | True | True | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M34 | 15 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M35 | 80 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M36 | 21 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M37 | 10 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | False | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M38 | 134 | NOT_DETERMINED_AUTOMATICALLY | True | True | True | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |
| M39 | 25 | NOT_DETERMINED_AUTOMATICALLY | True | False | False | True | True | True | READY_WITH_MANUAL_FIGURE_CHECK |

P2 should cite `pdf_page` and record `printed_page` only when visibly confirmed. Figures, tables and equations require visual confirmation in the PDF; P0 only checks that representative rendering is possible.

M23 identity is now verified; printed-page and figure/table/equation locators still require the normal P2 visual check.
