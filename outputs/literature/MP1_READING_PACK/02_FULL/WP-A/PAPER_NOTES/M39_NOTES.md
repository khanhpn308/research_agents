# M39 — Paper Notes

**Title:** Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results (NIST Technical Note 1297, 1994 Edition)  
**Authors/year:** Barry N. Taylor and Chris E. Kuyatt; 1994  
**Canonical PDF:** `data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf`  
**SHA-256:** `24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a`  

---

## A. Research problem and objectives
Taylor & Kuyatt (1994) present the official policy and practical guidelines of the National Institute of Standards and Technology (NIST) for evaluating and expressing measurement uncertainty, operationalizing the international GUM standard for laboratory and engineering use. The central tenet is that the result of any physical measurement is only an approximation or estimate of the true value of the measurand; consequently, a measurement result is scientifically incomplete unless accompanied by a quantitative statement of its uncertainty ([M39-E01](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl), p. 1 [printed p. 1 / physical p. 5]). The objective is to provide unambiguous, uniform operational rules for assessing both statistical and non-statistical components of uncertainty in experimental investigations.

## B. Physical system, materials, geometry and topology
**NOT_APPLICABLE to a specific mechanical device.** NIST Technical Note 1297 is an institutional metrological guide. It applies universally across physical calibration laboratories and experimental research setups, including load cells, pressure transducers, displacement sensors, digital multimeters, and dimensional calipers.

## C. Physical mechanism and loading
**NOT_APPLICABLE.** The guide formalizes the statistical and probabilistic treatment of measurement data. Conditionally applied to mechanical testing in MP1, it governs the conversion of manufacturer datasheet tolerances, calibration certificates, and instrument resolutions (force cells, LVDTs, pressure sensors) into standard uncertainties for characterizing beam deformation, bending moments, and stiffness.

## D. Mechanical model, equations, assumptions and boundary conditions
The guidelines formulate the evaluation and classification of uncertainty components:
1. **Classification of Components (Section 2, [M39-E02](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl), printed p. 1 / physical p. 6):**
   Uncertainty components are grouped strictly according to the method used to evaluate their numerical values:
   - **Type A:** Evaluated by statistical methods applied to repeated observations.
   - **Type B:** Evaluated by other means (scientific judgment based on calibration reports, specifications, handbook data).
   *Crucial distinction:* Type A and Type B categories do not correspond to "random" and "systematic" error. Known systematic effects must be corrected; the uncertainty of the correction itself may be evaluated by Type A or Type B methods.
2. **Type B Operational Conversion Rules (Section 4, [M39-E03](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl), printed pp. 3–4 / physical pp. 7–8):**
   Unlike M38, M39 presents these as **unnumbered procedural rules**:
   - *Quoted standard deviation multiple (Sec. 4.2):* $u_j = U_{\text{quoted}} / m$.
   - *Quoted confidence interval (Sec. 4.3):* $u_j = \text{Interval} / 1.960$ (for 95%) or $\text{Interval} / 2.576$ (for 99%).
   - *Rectangular (uniform) distribution over bounding limits $[a_-, a_+]$ (Sec. 4.6):* When only lower and upper bounds are known, with half-width $a = (a_+ - a_-)/2$:
     $$u_j = \frac{a}{\sqrt{3}} \approx 0.577\, a$$
   - *Triangular distribution over $[-a, +a]$ (Sec. 4.6):* When values are more likely near the center:
     $$u_j = \frac{a}{\sqrt{6}} \approx 0.408\, a$$
3. **Combined Standard Uncertainty Distinction (Section 5.3, [M39-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl), printed p. 6 / physical p. 10):**
   Combined standard uncertainty $u_c$ is an estimated standard deviation. It must remain clearly distinguished from a confidence interval. In NIST reporting, $u_c$ is reserved for fundamental constant determinations; for engineering reports, expanded uncertainty $U = k \cdot u_c$ with $k=2$ is mandatory.

**Assumptions:**
- Bounding limits $a_-$ and $a_+$ are reliable and supported by technical evidence.
- Uniform distribution is the default maximum entropy assumption when no distribution shape is known within bounds.

## E. Experimental setup and measured quantities
M39 provides practical guidance for laboratory experiments:
- Converting instrument manufacturer specifications (e.g. pressure sensor accuracy $\pm 0.25\%\text{ FS}$, load cell non-linearity $\pm 0.1\%$, digital scale resolution $0.1\text{ mg}$) into standard uncertainties using Type B rectangular evaluation ($u_j = a/\sqrt{3}$).
- Applying calibration corrections for environmental factors (ambient temperature, barometric pressure).
- Establishing combined uncertainty budgets for derived parameters.

## F. Quantitative findings
Contains mathematical conversion constants: $1/\sqrt{3} \approx 0.57735$, $1/\sqrt{6} \approx 0.40825$, normal distribution coverage factors $k = 1.960$ (95%), $k = 2.576$ (99%), and standard NIST engineering factor $k = 2$.

## G. Validation, uncertainty and verification domain
Official guideline of the National Institute of Standards and Technology (NIST), verified against the authoritative full text of NIST TN 1297 (September 1994 edition). Provides the operational metrological rules for validating experimental claims in MP1.

## H. Figures, tables and equations
- **Section 2 (printed pp. 1–2 / physical pp. 5–6):** Classification framework for Type A and Type B components ([M39-E02](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
- **Section 4 (printed pp. 3–4 / physical pp. 7–8):** Procedural transformation rules for Type B evaluation ([M39-E03](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
- **Section 5.3 (printed p. 6 / physical p. 10):** Policy and definition on combined standard uncertainty $u_c$ ([M39-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
- **Table B.1 (Appendix B):** Student $t$ critical values and effective degrees of freedom.
- **Appendix C:** Official NIST policy statement on expressing measurement uncertainty.

## I. Author limitations and counterevidence
Taylor & Kuyatt explicitly warn against critical reporting errors:
1. **Misrepresenting $u_c$ as a Confidence Interval ([M39-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)):** Reporting $Y = y \pm u_c$ and implying a 95% confidence interval is an egregious error; $u_c$ represents only a $1\sigma$ band (approx. 68% coverage under normality).
2. **Subjective Bias in Type B Estimates:** Type B evaluation relies on scientific judgment; assuming bounds without consulting certificates or manufacturer datasheets undermines the integrity of the uncertainty budget.
3. **Ignoring Known Systematic Biases:** Stating a large uncertainty cannot justify failing to correct for an identifiable, significant systematic error.

## J. Relevance to Chapter 1–2 and MP1 RQs
M39 is essential for structuring experimental integrity in Chapter 1 and Chapter 2:
- **Section C1.6 & C1.6.3 (Experimental Methodology):** Cites NIST guidelines ([M39-E01](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)) to establish that MP1 experimental testing must accompany every stiffness measurement with a quantitative uncertainty statement.
- **Section C2.5 & C2.5.4 (Sensor Uncertainty Modeling):** Employs Type B evaluation rules ([M39-E03](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)) to quantify standard uncertainties of load cells, displacement sensors, and pressure gauges, and adopts the NIST standard coverage factor $k=2$ for reporting experimental results.
- **Section C2.6.3 (Counterevidence on Error Reporting in Prior Art):** Uses [M39-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl) to critique prior soft robotics literature where raw standard deviations are routinely conflated with 95% confidence intervals or where measurement uncertainty is omitted entirely.

## K. Reading route
1. Read Section 1 Introduction (printed p. 1 / physical p. 5, [M39-E01](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)) for NIST's core policy stance.
2. Read Section 2 Classification of Components (printed pp. 1–2 / physical pp. 5–6, [M39-E02](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)) to understand the Type A / Type B distinction.
3. Study Section 4 Type B Evaluation (printed pp. 3–4 / physical pp. 7–8, [M39-E03](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)) for operational formulas.
4. Read Section 5 Combined Standard Uncertainty and Section 6 Expanded Uncertainty (printed pp. 5–7 / physical pp. 9–11, [M39-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).

## L. Unresolved evidence
Pagination offset: Printed pages 1–20 correspond to physical PDF pages 5–24 (pages 1–4 are covers, title, and preface). The existing verified records maintain `pdf_page: 1, 1, 7, 10` to preserve cross-package stability; this mapping is fully documented in `LOCATOR_ISSUES.md`. Bibliographic metadata corrected: authors Barry N. Taylor and Chris E. Kuyatt (previously omitted in old registry) are now fully recorded.
