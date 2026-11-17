# M38 — Paper Notes

**Title:** Evaluation of measurement data — Guide to the expression of uncertainty in measurement (JCGM 100:2008 / GUM 1995 with minor corrections)  
**Authors/year:** Joint Committee for Guides in Metrology (JCGM/WG 1); 2008  
**Canonical PDF:** `data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf`  
**SHA-256:** `41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c`  

---

## A. Research problem and objectives
JCGM 100:2008 (the international Guide to the Expression of Uncertainty in Measurement, GUM) addresses the lack of international consensus on evaluating and expressing measurement uncertainty ([M38-E01](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl), printed p. 1 / physical PDF p. 13). Its objective is to provide universal, rigorous, and statistically sound rules for evaluating and stating measurement uncertainty across science, engineering, and metrology. The GUM moves metrology away from qualitative, ambiguous terms such as "accuracy," "precision," and "systematic error," replacing them with an operational framework grounded in probability distributions and variance propagation.

## B. Physical system, materials, geometry and topology
**NOT_APPLICABLE to a specific mechanical device.** M38 is the foundational international metrology standard produced jointly by BIPM, IEC, IFCC, ILAC, ISO, IUPAC, IUPAP, and OIML. It applies universally to all physical measurement models and experimental apparatus, including force sensors, displacement transducers, pressure gauges, dimensional metrology instruments, and environmental monitors.

## C. Physical mechanism and loading
**NOT_APPLICABLE.** The document formulates the mathematical and probabilistic representation of measurement data under static, quasi-static, or dynamic observation. When conditionally applied to mechanical testing in MP1, it governs the measurement of physical state variables: transverse force $F$, beam deflection $\Delta w$, vacuum pressure $P$, bending moment $M$, and derived flexural rigidity $EI$.

## D. Mechanical model, equations, assumptions and boundary conditions
Section 4 and Section 5 formulate the complete metrological mathematics:
1. **The Measurand and Functional Relationship (Section 4.1, Eqs. 1–2, [M38-E02](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)):**
   In most physical experiments, the measurand $Y$ is not measured directly, but is determined from $N$ other input quantities $X_1, \dots, X_N$ through a functional model:
   $$Y = f(X_1, X_2, \dots, X_N)$$
   The estimate of the measurand $y$ is obtained by evaluating $f$ at the input estimates $x_1, \dots, x_N$:
   $$y = f(x_1, x_2, \dots, x_N)$$
2. **Type A Evaluation of Uncertainty (Section 4.2, Eqs. 3–5, [M38-E02](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)):**
   Evaluated from $n$ independent repeated observations $q_k$ under repeatability conditions:
   - Sample arithmetic mean: $\bar{q} = \frac{1}{n} \sum_{k=1}^n q_k$ (Eq. 3)
   - Sample experimental variance: $s^2(q_k) = \frac{1}{n-1} \sum_{j=1}^n (q_j - \bar{q})^2$ (Eq. 4)
   - Experimental variance of the mean: $u^2(\bar{q}) = s^2(\bar{q}) = \frac{s^2(q_k)}{n}$ (Eq. 5)
   - Standard uncertainty: $u(\bar{q}) = s(q_k)/\sqrt{n}$
3. **Combined Standard Uncertainty — Law of Propagation (Section 5.1 & 5.2, [M38-E03](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)):**
   - For **uncorrelated** inputs (Eq. 10):
     $$u_c^2(y) = \sum_{i=1}^N \left( \frac{\partial f}{\partial x_i} \right)^2 u^2(x_i) = \sum_{i=1}^N [c_i u(x_i)]^2 \equiv \sum_{i=1}^N u_i^2(y)$$
     where $c_i \equiv \partial f / \partial x_i$ are sensitivity coefficients (Eq. 11b).
   - For **correlated** inputs (Eq. 13):
     $$u_c^2(y) = \sum_{i=1}^N c_i^2 u^2(x_i) + 2 \sum_{i=1}^{N-1} \sum_{j=i+1}^N c_i c_j u(x_i, x_j)$$
     where $u(x_i, x_j) = r(x_i, x_j) u(x_i) u(x_j)$ is the estimated covariance (Eq. 14).
4. **Expanded Uncertainty (Section 6, [M38-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)):**
   $$U = k \cdot u_c(y)$$
   where $k$ is the coverage factor (typically $k=2$ for an approximate 95% level of confidence assuming a normal distribution).

**Assumptions:**
- $f$ is locally linear over the intervals defined by the standard uncertainties (first-order Taylor series). Higher-order partial derivatives must be included if non-linearity is severe (Note to 5.1.2).
- Input uncertainties are represented as standard deviations.
- Covariances between inputs sharing common calibrations, instruments, or environmental conditions must be explicitly accounted for.

## E. Experimental setup and measured quantities
M38 defines general experimental protocols:
- Determining sample size $n$ and degrees of freedom $\nu = n - 1$ for Type A statistical observations.
- Identifying input corrections for systematic effects (temperature expansion, sensor zero-drift, calibration bias).
- Formulating measurement models for derived quantities. In MP1, when measuring beam flexural rigidity $K = EI = \frac{F L^3}{3 \Delta w}$, the primary inputs are force $F$, deflection $\Delta w$, and length $L$, each contributing through its partial derivative sensitivity coefficient:
  $$c_F = \frac{\partial K}{\partial F} = \frac{L^3}{3 \Delta w}, \quad c_{\Delta w} = \frac{\partial K}{\partial \Delta w} = -\frac{F L^3}{3 \Delta w^2}, \quad c_L = \frac{\partial K}{\partial L} = \frac{F L^2}{\Delta w}$$

## F. Quantitative findings
The quantitative substance consists of mathematical equations and metrological conversion factors rather than an empirical dataset. It establishes that combined standard uncertainty $u_c(y)$ represents a standard deviation ($\pm 1\sigma$) with an approximate 68% confidence level under normality, and that expanding to $U$ ($k=2$) is necessary to obtain an approximate 95% confidence interval.

## G. Validation, uncertainty and verification domain
M38 is the supreme international metrological standard. Verified against the authoritative 2008 JCGM publication. In MP1, M38 provides the mathematical and conceptual rigor required to validate that experimental stiffness measurements are scientifically defensible and reproducible.

## H. Figures, tables and equations
- **Section 4.1, Eqs. (1)–(2) (printed p. 8 / physical p. 20):** Functional measurement model ([M38-E02](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
- **Section 4.2, Eqs. (3)–(5) (printed pp. 8–9 / physical pp. 20–21):** Type A mean, observation variance, and variance of the mean ([M38-E02](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
- **Section 5.1 & 5.2, Eqs. (10)–(13) (printed pp. 18–21 / physical pp. 30–33):** Law of propagation of uncertainty, sensitivity coefficients, and covariance handling ([M38-E03](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
- **Section 6, Sec. 6.2–6.3 (printed pp. 23–24 / physical pp. 35–36):** Expanded uncertainty and coverage factor conventions ([M38-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).

## I. Author limitations and counterevidence
M38 explicitly cautions against common metrological fallacies:
1. **Confusing Error with Uncertainty (Section 3.3.1, Note):** An unknown systematic error cannot be equated with uncertainty. A measurement result corrected for all known effects still carries uncertainty due to incomplete knowledge.
2. **First-Order Linearization Failure (Section 5.1.2, Note):** When the functional model $f$ exhibits strong curvature (non-linear mechanics), neglecting second-order partial derivatives produces an erroneous combined variance.
3. **Arbitrary Coverage Factors (Section 6.2):** Stating $Y = y \pm U$ without an explicit coverage factor $k$ and degrees of freedom is scientifically invalid.

## J. Relevance to Chapter 1–2 and MP1 RQs
M38 is the primary methodological standard for Chapter 1 and Chapter 2:
- **Section C1.6 & C1.6.3 (Experimental Methodology & Standards):** Establishes that experimental validation in the thesis must adhere to formal GUM uncertainty principles ([M38-E01](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
- **Section C2.5 & C2.5.4 (Uncertainty Analysis in Mechanics Modeling):** Provides the mathematical propagation framework (Eqs. 10–13, [M38-E03](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)) to map sensor tolerances into stiffness confidence intervals, and mandates reporting conventions (Sec. 6, [M38-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).

## K. Reading route
1. Read Section 1 Scope and Section 2 Definitions (printed pp. 1–4 / physical pp. 13–16, [M38-E01](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
2. Study Section 4.1 Modelling the Measurement and Section 4.2 Type A Evaluation (printed pp. 8–10 / physical pp. 20–22, [M38-E02](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
3. Deep-dive into Section 5 Determining Combined Standard Uncertainty (printed pp. 18–21 / physical pp. 30–33, [M38-E03](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).
4. Review Section 6 Determining Expanded Uncertainty (printed pp. 23–24 / physical pp. 35–36, [M38-E04](file:///home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl)).

## L. Unresolved evidence
Pagination offset: Printed pages 1, 8, 18, 23 correspond to physical PDF pages 13, 20, 30, 35 due to 12 introductory pages (cover, copyright, foreword, contents). The existing verified records maintain `pdf_page: 1, 8, 18, 23` to preserve cross-package stability; this mapping is fully documented in `LOCATOR_ISSUES.md`. Bibliographic metadata updated to cite JCGM/WG 1.
