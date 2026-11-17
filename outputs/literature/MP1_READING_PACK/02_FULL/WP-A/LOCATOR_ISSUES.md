# Locator Issues & Provenance Audit — WP-A

## 1. Page Mapping: Physical PDF Pages vs. Printed Pages

In the initial extraction of WP-A, physical PDF page numbers and printed page numbers were sometimes conflated or left unexamined. This remediation audit independently verified the exact dual-page mapping for all 7 canonical PDFs:

| Paper ID | Short Title | Canonical PDF File | Verified PDF Locators in Records | Physical PDF Page | Printed Page | Notes |
|---|---|---|---|---|---|---|
| **M01** | Feak & Swales (2009) | `M01__Telling-a-Research Story...pdf` | p. 3 (E01), p. 25 (E02), p. 93 (E03) | 3, 25, 93 | 1 (half-title), 9 (Orientations), 77 (Chap 4) | Record `pdf_page` reflects physical PDF page numbers. |
| **M02** | Burgner-Kahrs et al. (2015) | `M02__2015-Burgner-Kahrs...pdf` | p. 1 (E01), p. 2 (E02), p. 3 (E03) | 1, 2, 3 | 1261, 1262, 1263 | IEEE Transactions on Robotics journal pagination. Record `pdf_page` matches physical PDF pages. |
| **M03** | Russo et al. (2023) | `M03__2023-Russo-Continuum Robots...pdf` | p. 1 (E01), p. 3 (E02), p. 4 (E03) | 1, 3, 4 | 1, 3, 4 | Article open access pagination starts at page 1. Record `pdf_page` matches physical PDF pages. |
| **M04** | Lin et al. (2024) | `M04__1.2024-Lin-Variable stiffness...pdf` | p. 1 (E01), p. 2 (E02), p. 3 (E03) | 1, 2, 3 | 1, 2, 3 | ScienceDirect pagination starts at page 1. Record `pdf_page` matches physical PDF pages. |
| **M05** | Fan et al. (2024) | `M05__2.2024-Fan-An overview...pdf` | p. 1 (E01), p. 10 (E02), p. 11 (E03) | 1, 10, 11 | 1, 10, 11 | RCIM journal pagination starts at page 1. Record `pdf_page` matches physical PDF pages. |
| **M38** | JCGM 100:2008 (GUM) | `M38_2008-Evaluation of measurement...pdf` | p. 1 (E01), p. 8 (E02), p. 18 (E03), p. 23 (E04) | 13, 20, 30, 35 | 1, 8, 18, 23 | **Critical provenance note:** The existing verified records set `pdf_page: 1, 8, 18, 23`. In the GUM PDF, pages 1–12 are preliminary matter (title, copyright, foreword, contents). Printed pages 1, 8, 18, 23 correspond precisely to physical PDF pages 13 (Sec 1 Scope), 20 (Sec 4.1 Modelling), 30 (Sec 5 Combined uncertainty), and 35 (Sec 6 Expanded uncertainty). To preserve existing verified locators and cross-package references, `pdf_page` remains unchanged, with this dual mapping explicitly recorded. |
| **M39** | Taylor & Kuyatt (1994) | `M39_1994-Guidelines for Evaluating...pdf` | p. 1 (E01), p. 1 (E02), p. 7 (E03), p. 10 (E04) | 5, 6, 7, 10 | 1, 2, 3, 6 | In NIST TN 1297, physical pages 1–4 are covers, title, and preface. Section 1 begins on physical p. 5 (printed p. 1); Section 2 is on physical p. 6 (printed p. 2); Section 4 starts on physical p. 7 (printed p. 3); Section 5.3 is on physical p. 10 (printed p. 6). Record locators are maintained as verified. |

---

## 2. Figure / Table Numbering Provenance in M05

In `EVIDENCE_RECORDS.jsonl` and `FIGURE_TABLE_REGISTRY.md`, records M05-E02 and M05-E03 originally carried figure locators `"Fig. 8"` and `"Fig. 10"`:
- **Audit finding:** In the canonical PDF of M05 (Fan et al., 2024, *Robotics and Computer-Integrated Manufacturing*, 90, 102811), figures are numbered from Fig. 1 to Fig. 7.
- **Physical location:**
  - Fibre/filament jamming (FJ) is detailed in **Section 3.3.1 (p. 10)**, illustrated in **Fig. 5(g) (p. 10)**, and tabulated in **Table 4 (p. 11)**.
  - Layer/laminar jamming (LJ) is detailed in **Section 3.3.3 (p. 11)**, illustrated in **Fig. 5(e, f) (p. 10)**, and tabulated in **Table 4 (pp. 11–12)**.
- **Resolution:** The original labels "Fig. 8" and "Fig. 10" are legacy placeholders from an earlier draft numbering. The physical text and subfigures on pages 10 and 11 are verified with 100% full-text fidelity. Both the legacy locator and the exact primary figures/tables are cross-referenced in the registries and paper notes.

---

## 3. Typographical Audit for M04 Equations (1)–(2)

In M04 (Lin et al., 2024, p. 1–2):
- Eq. (1) is printed as $K = d/F$ where text describes it as the proportion of deviation from external force. Standard linear stiffness is defined as $K = F/d$.
- Eq. (2) is printed as $K = \theta/\tau$. Standard torsional stiffness is defined as $K = \tau/\theta$.
- Both formulas are faithfully recorded in `EQUATION_REGISTRY.md` with explicit notes explaining the typographical inversion relative to classical mechanics conventions, and highlighting the authors' own discussion that stiffness values in the literature carry different dimensions and definitions.
