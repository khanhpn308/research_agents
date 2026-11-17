# Equation Registry — WP-A

## 1. Registry Summary Table

| Paper | Locator | PDF page (physical / printed) | Status | Scope / Description |
|---|---|---:|---|---|
| M04 | Eqs. (1)–(4), Fig. 2 | 1–2 / 1–2 | VERIFIED_FULL_TEXT | Operational stiffness definitions under different loading/support cases (linear, torsional, 3-point bending, cantilever). |
| M38 | Eq. (4) [and Eqs. (1)–(2), (5)] | 20–22 / 8–10 | VERIFIED_FULL_TEXT | Measurement model $Y=f(X_1,\dots,X_N)$ and Type A experimental variance evaluation. |
| M38 | Eqs. (10)–(13) [and Eq. (14)] | 30–33 / 18–21 | VERIFIED_FULL_TEXT | Combined standard uncertainty and covariance treatment (Law of propagation of uncertainty). |
| M39 | Section 4 (Sec. 4.1–4.6) | 7–8 / 3–4 | VERIFIED_FULL_TEXT | Type B uncertainty procedural evaluation rules and distribution conversions (unnumbered formulas). |

---

## 2. Detailed Equation Notes

### 2.1. M04 — Variable Stiffness Operational Definitions (Lin, Song, and Wang, 2024)

- **Source Paper:** M04 (`data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf`)
- **Locators:** Physical PDF pp. 1–2 (printed pp. 1–2), Section 1.2, Fig. 2(a–d), Eqs. (1)–(4).
- **Linked Evidence IDs:** `M04-E02`, `M04-E03`

#### Mathematical Expressions

1. **Linear End-Deflection Stiffness (Eq. 1 as printed in M04):**
   $$K = \frac{d}{F} \quad (1)$$
   *(Note on printed formula: As printed in the text of Lin et al., the ratio is given as $d/F$, which is conventionally compliance/flexibility. Standard linear stiffness is defined as $K = F/d$. The authors explicitly highlight in the text that stiffness definitions across literature differ in form and dimensions).*

2. **Torsional Stiffness (Eq. 2 as printed in M04):**
   $$K = \frac{\theta}{\tau} \quad (2)$$
   *(Note on printed formula: As printed, the ratio is $\theta/\tau$. Standard torsional stiffness is conventionally defined as $K = \tau/\theta$)*.

3. **Three-Point Bending Flexural Rigidity (Eq. 3):**
   $$K = EI = \frac{F L^3}{48 \Delta w} \quad (3)$$

4. **Cantilever Bending Flexural Rigidity (Eq. 4):**
   $$K = EI = \frac{F L^3}{3 \Delta w} \quad (4)$$

5. **Stiffness Adjusting Ratio (Dimensionless, p. 2):**
   $$R = \frac{K_{\max}}{K_{\min}}$$

#### Symbol Definitions and Physical Units
- $d$: Magnitude of end-effector linear deviation [m or mm].
- $F$: Magnitude of applied external transverse force [N].
- $\theta$: Magnitude of angular rotation of the robot body [rad].
- $\tau$: Magnitude of applied external torque [$\text{N}\cdot\text{m}$].
- $E$: Flexural modulus (Young's modulus of equivalent beam material) [$\text{N/m}^2$ or Pa].
- $I$: Second moment of area of the cross-section [$\text{m}^4$].
- $EI$: Flexural rigidity [$\text{N}\cdot\text{m}^2$].
- $L$: Beam length between supports (Eq. 3) or overhang cantilever length (Eq. 4) [m].
- $\Delta w$: Transverse deflection at beam center (Eq. 3) or at distal cantilever tip (Eq. 4) [m].
- $K$: Operational stiffness (units depend on definition: $\text{N/m}$ or $\text{m/N}$ for Eq. 1; $\text{rad}/(\text{N}\cdot\text{m})$ or $(\text{N}\cdot\text{m})/\text{rad}$ for Eq. 2; $\text{N}\cdot\text{m}^2$ for Eqs. 3 and 4).
- $R$: Stiffness adjusting ratio [dimensionless].

#### Mechanical Significance
Equations (1)–(4) systematically classify the operational metrics used by soft and continuum robotics researchers. Equations (3) and (4) convert system-level force-deflection measurements into an equivalent continuum structural parameter ($EI$), enabling comparison across different specimen lengths. As Lin et al. caution in Section 1.2, stiffness values across studies cannot be directly compared without normalizing for boundary conditions, loading configuration, and physical dimensions.

#### Underlying Mechanical Assumptions
- Euler-Bernoulli beam theory applies (slender beam: length-to-thickness ratio $L/h \gg 10$).
- Pure bending deformation; shear deformation and axial extension are neglected.
- Small deflections and linear elastic constitutive behavior.
- Idealized boundary conditions: simple knife-edge supports (Eq. 3) or perfectly rigid clamped base (Eq. 4).
- Interlayer slip, Coulomb contact friction, and vacuum pressure are **not** explicitly modeled inside these classical formulas; they only provide the homogenized equivalence framework.

---

### 2.2. M38 — Measurement Model and Type A Variance Evaluation (JCGM 100:2008 / GUM)

- **Source Paper:** M38 (`data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf`)
- **Locators:** Physical PDF pp. 20–22 (printed pp. 8–10), Section 4.1 & Section 4.2, Eqs. (1), (2), (4), (5).
- **Linked Evidence IDs:** `M38-E02`

#### Mathematical Expressions

1. **General Measurement Model (Eq. 1):**
   $$Y = f(X_1, X_2, \dots, X_N) \quad (1)$$

2. **Output Estimate from Input Estimates (Eq. 2):**
   $$y = f(x_1, x_2, \dots, x_N) \quad (2)$$

3. **Sample Arithmetic Mean of Repeated Observations (Eq. 3):**
   $$\bar{q} = \frac{1}{n} \sum_{k=1}^n q_k \quad (3)$$

4. **Experimental Variance of the Observations (Eq. 4):**
   $$s^2(q_k) = \frac{1}{n - 1} \sum_{j=1}^n (q_j - \bar{q})^2 \quad (4)$$

5. **Experimental Variance of the Mean / Type A Standard Uncertainty (Eq. 5):**
   $$s^2(\bar{q}) = \frac{s^2(q_k)}{n} = \frac{1}{n(n - 1)} \sum_{j=1}^n (q_j - \bar{q})^2 \quad (5)$$
   $$u(\bar{q}) = s(\bar{q}) = \frac{s(q_k)}{\sqrt{n}}$$

#### Symbol Definitions and Physical Units
- $Y$: The measurand (output physical quantity to be determined, e.g. stiffness $K$ or flexural rigidity $EI$).
- $X_i$: Input quantities ($i = 1, \dots, N$) affecting the measurement result (e.g. force $F$, deflection $\Delta w$, length $L$).
- $f$: Functional relationship relating input quantities to the measurand.
- $y$: Result of the measurement / estimate of the measurand $Y$.
- $x_i$: Estimate of input quantity $X_i$.
- $q_k$: The $k$-th independent repeated observation of a randomly varying quantity $q$ ($k = 1, \dots, n$).
- $\bar{q}$: Arithmetic mean of $n$ observations.
- $s^2(q_k)$: Sample experimental variance characterizing the dispersion of individual readings [unit of $q^2$].
- $s^2(\bar{q})$: Experimental variance of the mean [unit of $q^2$].
- $u(\bar{q})$: Type A standard uncertainty of the estimate $\bar{q}$ [unit of $q$].
- $n$: Number of statistically independent repeated observations.

#### Metrological Significance
In mechanical experimentation, target properties such as stiffness $K$ cannot be directly sensed by a single physical transducer. Instead, $K$ is inferred from primary sensor signals (force cell $F$, displacement gauge $\Delta w$, micrometer dimensions $b, h, L$) via a mathematical model $K = f(F, \Delta w, L)$. Equation (4) and Equation (5) provide the statistical foundation for assessing the repeatability and random scatter of these primary readings under identical measurement conditions.

#### Underlying Assumptions
- Observations $q_1, \dots, q_n$ are statistically independent and identically distributed.
- Measurement system is under statistical control with stable environmental and operating conditions.
- Degree of freedom for the Type A evaluation is $\nu = n - 1$.

---

### 2.3. M38 — Law of Propagation of Uncertainty and Combined Variance (JCGM 100:2008 / GUM)

- **Source Paper:** M38 (`data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf`)
- **Locators:** Physical PDF pp. 30–33 (printed pp. 18–21), Section 5.1 & Section 5.2, Eqs. (10), (11a, b), (12), (13), (14).
- **Linked Evidence IDs:** `M38-E03`

#### Mathematical Expressions

1. **Combined Variance for Uncorrelated Input Quantities (Eq. 10):**
   $$u_c^2(y) = \sum_{i=1}^N \left( \frac{\partial f}{\partial x_i} \right)^2 u^2(x_i) \quad (10)$$

2. **Sensitivity Coefficients and Individual Variance Contributions (Eq. 11a, b):**
   $$u_c^2(y) = \sum_{i=1}^N [c_i u(x_i)]^2 \equiv \sum_{i=1}^N u_i^2(y) \quad (11a)$$
   $$c_i \equiv \frac{\partial f}{\partial x_i}, \quad u_i(y) \equiv |c_i| u(x_i) \quad (11b)$$

3. **Relative Combined Standard Uncertainty for Multiplicative Models (Eq. 12):**
   $$\left[ \frac{u_c(y)}{y} \right]^2 = \sum_{i=1}^N \left[ p_i \frac{u(x_i)}{x_i} \right]^2 \quad (12)$$
   *(Applies when $Y = c X_1^{p_1} X_2^{p_2} \dots X_N^{p_N}$ where exponents $p_i$ are known constants)*.

4. **Combined Variance for Correlated Input Quantities (Eq. 13):**
   $$u_c^2(y) = \sum_{i=1}^N \left( \frac{\partial f}{\partial x_i} \right)^2 u^2(x_i) + 2 \sum_{i=1}^{N-1} \sum_{j=i+1}^N \frac{\partial f}{\partial x_i} \frac{\partial f}{\partial x_j} u(x_i, x_j) \quad (13)$$

5. **Covariance and Correlation Coefficient (Eq. 14):**
   $$u(x_i, x_j) = r(x_i, x_j) u(x_i) u(x_j) \quad (14)$$
   where $-1 \le r(x_i, x_j) \le +1$.

#### Symbol Definitions and Physical Units
- $u_c(y)$: Combined standard uncertainty of the output estimate $y$ [unit of $y$].
- $u_c^2(y)$: Combined variance [$\text{unit of } y^2$].
- $c_i = \partial f / \partial x_i$: Partial derivative / sensitivity coefficient with respect to input $x_i$ evaluated at input estimates [$\text{unit of } y / \text{unit of } x_i$].
- $u(x_i)$: Standard uncertainty of input estimate $x_i$ (from Type A or Type B evaluation) [unit of $x_i$].
- $u_i(y) = |c_i| u(x_i)$: Component of standard uncertainty in $y$ generated by uncertainty in $x_i$ [unit of $y$].
- $u(x_i, x_j)$: Estimated covariance associated with input estimates $x_i$ and $x_j$ [$\text{unit of } x_i \cdot \text{unit of } x_j$].
- $r(x_i, x_j)$: Estimated correlation coefficient [dimensionless].

#### Metrological Significance
This is the foundational Law of Propagation of Uncertainty. When determining beam stiffness $K = f(F, \Delta w, L)$, uncertainties from the force transducer $u(F)$, displacement sensor $u(\Delta w)$, and length measurement $u(L)$ propagate into $u_c(K)$ weighted by the sensitivity coefficients ($\partial K / \partial F$, $\partial K / \partial \Delta w$, $\partial K / \partial L$). If force and displacement are measured on a single testing rig sharing common thermal expansion, structural compliance, or data acquisition channels, they may be mutually correlated ($r \ne 0$); neglecting the covariance term in Eq. (13) leads to an underestimation or overestimation of $u_c(K)$.

#### Underlying Assumptions
- $Y = f(X_1, \dots, X_N)$ is adequately approximated by a first-order Taylor series around $(x_1, \dots, x_N)$ over the range of their uncertainties.
- Higher-order partial derivatives are negligible. If strong non-linearity exists, second-order terms must be included (M38, Note to 5.1.2).
- Standard uncertainties $u(x_i)$ and covariances $u(x_i, x_j)$ are valid, positive-semidefinite representations of input dispersion.

---

### 2.4. M39 — Type B Uncertainty Procedural Evaluation Rules (Taylor and Kuyatt, 1994 / NIST TN 1297)

- **Source Paper:** M39 (`data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf`)
- **Locators:** Physical PDF pp. 7–8 (printed pp. 3–4), Section 4 (Sec. 4.1–4.6).
- **Linked Evidence IDs:** `M39-E03`

#### Distinction: Procedural Formulas vs. Numbered Equations
Unlike M04 and M38, NIST Technical Note 1297 presents its Type B evaluation rules as **unnumbered procedural conversion guidelines** in Section 4. These are mathematical transformation rules that convert manufacturer tolerances, calibration certificate intervals, or bounding limits into standard uncertainties ($u_j$).

#### Mathematical Formulations

1. **Quoted Multiple of Standard Deviation (Sec. 4.2):**
   $$u_j = \frac{U_{\text{quoted}}}{m}$$
   *(where $m$ is the explicitly stated multiplier, e.g. dividing by 2 or 3)*.

2. **Quoted Expanded Uncertainty with Stated Confidence Level (Sec. 4.3):**
   $$u_j = \frac{U_{\text{quoted}}}{k}$$
   - For a 95% confidence level under normal distribution: $k = 1.960$.
   - For a 99% confidence level under normal distribution: $k = 2.576$.

3. **Rectangular (Uniform) Probability Distribution over Bounding Interval (Sec. 4.6):**
   Given symmetric lower and upper limits $a_-$ and $a_+$ with half-width $a = \frac{a_+ - a_-}{2}$:
   $$x_j = \frac{a_+ + a_-}{2}$$
   $$u_j = \frac{a}{\sqrt{3}} \approx 0.577\, a$$

4. **Triangular Probability Distribution (Sec. 4.6):**
   When values are expected to lie within $[-a, +a]$ but are more likely to occur near the center:
   $$u_j = \frac{a}{\sqrt{6}} \approx 0.408\, a$$

#### Symbol Definitions and Physical Units
- $u_j$: Standard uncertainty evaluated by Type B method [unit of the input quantity $X_j$].
- $U_{\text{quoted}}$: Quoted expanded uncertainty or manufacturer tolerance limit [unit of $X_j$].
- $k$: Coverage factor [dimensionless].
- $a$: Semi-range or half-width of the bounding interval [unit of $X_j$].
- $a_-, a_+$: Lower and upper bounding limits of the quantity [unit of $X_j$].

#### Metrological Significance
In experimental soft robotics, many measurement uncertainties cannot be obtained through thousands of repeated trials (e.g., pressure sensor accuracy class $\pm 0.5\%$ of full scale, digital caliper resolution $0.01\text{ mm}$, load cell non-linearity). M39 provides the rigorous, standardized mathematical protocol to convert datasheet bounds into standard uncertainties ($u_j = a/\sqrt{3}$), enabling their direct combination with Type A uncertainties via the GUM propagation law.

#### Underlying Assumptions
- Scientific judgment and technical evidence supporting the bounding limits $a_-$ and $a_+$ are reliable.
- In the absence of specific knowledge about the distribution of values within $[-a, +a]$, the uniform/rectangular distribution represents the maximum entropy (least biased) assumption.
- The standard uncertainty $u_j$ obtained from Type B evaluation is treated on an equal mathematical footing as a sample standard deviation $s(\bar{q})$ from Type A evaluation.
