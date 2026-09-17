# Zhang et al. (2025) — “Toward a Deeper Understanding of Layer Jamming Structures”

## Adversarial full-text technical audit for D1-V003

> **Paper:** Shuai Zhang, Jiantao Yao, Wumian Zhao, and Kunming Zhu, “Toward a deeper understanding of layer jamming structures,” *Frontiers of Mechanical Engineering* 20(4), article 27 (2025).  
> **DOI:** `10.1007/s11465-025-0843-5`  
> **Repository identity:** `paper_id: 7cb387b88d`  
> **Evidence origin:** previously ingested and validated under D1-V002; reused here for a new D1-V003 analysis. The paper was not re-added or re-ingested.  
> **Purpose:** attempt to falsify—not defend—the surviving mechanics-validity question. This report is not a novelty adjudication.

## Executive finding

**Final adversarial verdict: SUBSTANTIALLY NARROWS GAP. [INFERENCE]**

This is much closer to the surviving question than a general layer-jamming or control paper. It constructs a beam-level analytical representation in which the discrete advance of slipping interfaces is deliberately replaced by a continuous sliding-boundary variable, retains physical layer number and thickness, derives pressure-dependent transition criteria, adds an incremental history rule for unloading and cyclic response, handles initially curved beams and finite configuration updates, and compares load–deflection predictions with experiments across pressure, layer thickness, initial curvature, and cyclic loading. **[VERIFIED FULL TEXT — Zhang et al. 2025, Sects. 2–5, Figs. 3–7, Eqs. (1)–(26), PDF pp. 3–14]**

It therefore pre-empts a broad project framed as merely “develop a continuum/reduced slip model and test pressure, thickness/layer count, curvature, and hysteresis.” It also explicitly identifies one central approximation: the truly discrete activation of interfaces is smoothed by treating the sliding boundary \(y_s\) as continuous, with the authors stating that the approximation improves as layer thickness decreases. **[VERIFIED FULL TEXT — Sect. 2.2, PDF p. 7]**

It does **not**, however, define an allowable-error tolerance, calculate analytical-versus-explicit-interface error over a parameter grid, locate a boundary where such a tolerance is crossed, independently vary layer count from layer thickness/total height, or quantitatively decompose the first failure mechanism. Its reported disagreements are qualitative: critical load is overestimated especially at low pressure and with thin layers; theoretical cyclic dissipation is smaller than measured; and near-zero-load hysteresis differs because of compliant supports. **[VERIFIED FULL TEXT — Sects. 5.2 and 5.4, PDF pp. 12 and 14]**

The surviving question is consequently narrower: not whether a continuous-boundary model can cover those phenomena, but whether its error relative to explicit-interface mechanics and independent experiment can be quantified in advance and converted into a tolerance-defined validity/breakdown boundary. **[INFERENCE]**

## Evidence labels and source basis

- **[VERIFIED FULL TEXT]** means the claim is supported by the validated evidence record and the inspected repository PDF.
- **[METADATA ONLY]** means only bibliographic metadata is available. No technical conclusion in this report relies on such a source.
- **[INFERENCE]** means analysis derived from verified observations but not stated as a conclusion by the paper.

Primary evidence file: `data/evidence/2025-Toward a deeper understanding of layer jamming structures_7cb387b88d.json`. Source PDF SHA256: `7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a`; 16 PDF pages. **[VERIFIED FULL TEXT]**

## 1. Exact research objective of the paper

The paper's objective is to provide a closed-form deformation model for beam-stack layer-jamming structures (LJS), use layer-resolved finite-element analysis (FEA) to identify stress and stress-increment patterns, derive a governing angular-deformation equation for straight and initially curved beams, and use an incremental algorithm for large-deformation and complex loading histories. It then tests whether the model predicts effects of layer thickness, hydrostatic pressure, initial curvature, and cyclic loading. **[VERIFIED FULL TEXT — Abstract; Introduction; Sects. 2–5, PDF pp. 1–14]**

The authors are responding to prior models that are restricted mainly to straight beams, special loading conditions, two-layer solutions, summation forms, or computationally costly multilayer FEA. Their stated aspiration is a broadly applicable analytical model for planar bending of beam-stack LJS—not formal material homogenization and not robot control. **[VERIFIED FULL TEXT — Introduction, PDF pp. 2–3]**

Adversarially, that objective overlaps four axes of the surviving question—pressure, thickness/layer number, bending configuration/load, and slip history. It does not explicitly make “validity mapping” or “breakdown-boundary identification” an objective. **[INFERENCE]**

## 2. Mechanical model used

### 2.1 Model class

The model combines:

1. planar Euler–Bernoulli-type beam kinematics;
2. cross-sectional axial and shear stress patterns inferred from explicit layered FEA;
3. linear elasticity within the sheets;
4. Coulomb limiting shear traction at sliding interfaces;
5. a continuous through-thickness sliding boundary \(y_s\) that replaces discrete jumps as successive interfaces slip;
6. curved-beam internal-force equilibrium; and
7. an incremental stress-history algorithm for large configuration changes and reversed/cyclic loading.

**[VERIFIED FULL TEXT — Sects. 2–3, Figs. 2–5, Table 1, PDF pp. 3–10]**

The most accurate scientific description is a **beam-level continuous-slip-boundary reduction of discrete multilayer mechanics**. It is continuum beam modeling in the ordinary structural sense and a reduced/equivalent description of interface activation. It is not a formal homogenization derivation: no representative volume element, scale-separated asymptotic problem, or homogenized constitutive tensor is derived. Physical \(n\) and \(\delta\) remain explicit. **[INFERENCE grounded in the verified equations]**

### 2.2 Model architecture

The logic is:

1. Use 5-, 10-, and 25-layer explicit FEA to observe the forms of \(\sigma(y)\), \(\tau(y)\), \(\Delta\sigma(y)\), and \(\Delta\tau(y)\) in full-jamming, partial-slip, and full-slip states.
2. Encode those observations as piecewise linear axial stress and piecewise quadratic shear stress.
3. Replace the physically discrete number of slipped interfaces by a continuous boundary \(y_s\).
4. Enforce cross-sectional moment and shear resultants to obtain the stress coefficients \(k_\sigma\) and \(k_\tau\).
5. Use local stress equilibrium to relate \(y_s\) to shear force \(Q\).
6. Approximate the implicit relation by a quadratic closed form.
7. Use surface strain compatibility to obtain an incremental curvature/angle equation.
8. Step through the load history, selecting a stress-increment pattern based on load direction.

**[VERIFIED FULL TEXT — Sects. 2.1–3.3 and Algorithm 1, PDF pp. 3–10]**

## 3. Governing equations

The governing system is not one differential equation alone. It consists of curved-beam force/moment balance, piecewise stress fields, Coulomb slip constraints, a continuous slip-boundary relation, deformation compatibility, and a path-dependent incremental update. **[VERIFIED FULL TEXT]**

The paper's notation is occasionally internally inconsistent. The equations below reproduce the printed expressions where important; a dimensional or cross-reference concern is reported rather than silently repaired.

## 4. Important equations, symbols, meaning, units, and assumptions

### 4.1 Full-jamming stress field

**Printed Eq. (1) [VERIFIED FULL TEXT]:**

\[
\sigma=\frac{12M}{b h^3 E}\,y.
\]

Here \(\sigma\) is called extensional stress [Pa]; \(M\) is bending moment [N·m]; \(b\) is beam width [m]; \(h\) is total stack height [m]; \(E\) is sheet Young's modulus [Pa]; and \(y\) is the through-thickness coordinate [m]. The equation is introduced as the linear Euler–Bernoulli full-jamming stress distribution, with axial-force effects omitted. **[VERIFIED FULL TEXT — Eq. (1), PDF p. 4]**

There is a dimensional defect in the printed equation: including \(E\) makes its right-hand side dimensionless, i.e. strain, not stress. Later Eq. (23) again divides \(\sigma\) by \(E\). The dimensionally conventional bending-stress expression would omit \(E\), but that correction is an **[INFERENCE]**, not a verified printed equation. This must be resolved before reproducing the model computationally.

**Printed Eq. (2) [VERIFIED FULL TEXT]:**

\[
\tau=\frac{3Q}{2bh}\left(1-4\frac{y^2}{h^2}\right).
\]

Here \(\tau\) is interlayer shear stress [Pa]; \(Q\) is section shear force [N]; and \(b,h,y\) are as defined above [m]. This is the parabolic rectangular-section shear field. It assumes a fully jammed, elastic section and reaches its largest magnitude at the mid-height, explaining why central interfaces reach the friction limit first. **[VERIFIED FULL TEXT — Eq. (2), PDF p. 4]**

The total height is:

\[
h=n\delta.
\]

Here \(n\) is physical layer count [dimensionless integer] and \(\delta\) is individual sheet thickness [m]. This relation is printed immediately after Eq. (2), although it is not assigned its own equation number. **[VERIFIED FULL TEXT — PDF p. 4]**

### 4.2 Coulomb threshold and slip states

The sliding traction is:

\[
\tau_{cr}=\operatorname{sign}(Q)\mu p.
\]

Here \(\tau_{cr}\) is signed limiting shear stress [Pa]; \(\operatorname{sign}(Q)\) gives the shear-force direction; \(\mu\) is the dimensionless Coulomb friction coefficient; and \(p\) is uniform hydrostatic/contact pressure [Pa]. This expression is printed in the prose of Sect. 2.2. It assumes spatially uniform pressure and constant \(\mu\). **[VERIFIED FULL TEXT — PDF p. 6]**

The three model states are:

- **full jamming:** \(|\tau|<\mu p\) at all interfaces;
- **half slipping/partial slip:** central interfaces have reached \(\tau_{cr}\), bounded by \(y=\pm y_s\), while outer regions remain jammed;
- **full slipping:** all friction pairs are treated as sliding, implemented by setting \(y_s=h/2-\delta\).

**[VERIFIED FULL TEXT — Sect. 2.2 and Fig. 4, PDF pp. 4–7]** “Half jamming” and “half slipping” are both used in the paper; this report treats them as the same intermediate state rather than inventing an additional regime.

### 4.3 Partial-slip axial and shear fields

For the central layer in the sliding region:

**Printed Eq. (3) [VERIFIED FULL TEXT]:**

\[
\sigma=k_\sigma y,
\qquad -\frac{\delta}{2}\le y\le\frac{\delta}{2}.
\]

Here \(k_\sigma\) is the axial-stress gradient [Pa/m], and \(\sigma,y,\delta\) are defined above. Other sliding layers use shifted copies of this linear field. The common slope follows the assumption that all layers share the same beam rotation. **[VERIFIED FULL TEXT — Eq. (3), PDF p. 6]**

For the upper jammed region:

**Printed Eq. (4) [VERIFIED FULL TEXT]:**

\[
\sigma=k_\sigma\left(y-y_s-\frac{\delta}{2}\right),
\qquad y_s\le y\le\frac{h}{2}.
\]

Here \(y_s\) is the upper sliding/jammed boundary [m]; all other symbols are defined immediately above. The expression uses the FEA-inspired boundary condition \(\sigma=-k_\sigma\delta/2\) at \(y=y_s\). A symmetric counterpart applies below the mid-plane. **[VERIFIED FULL TEXT — Eq. (4), PDF p. 6]**

For a central sliding layer, shear is:

**Printed Eq. (5) [VERIFIED FULL TEXT]:**

\[
\tau=k_\tau y^2-\frac{k_\tau}{4}\delta^2+\tau_{cr},
\qquad -\frac{\delta}{2}\le y\le\frac{\delta}{2}.
\]

Here \(k_\tau\) is a quadratic shear-stress coefficient [Pa/m²]; \(\tau\) and \(\tau_{cr}\) are shear stresses [Pa]; and \(y,\delta\) are lengths [m]. The expression enforces \(\tau=\tau_{cr}\) at the layer boundaries. Other sliding layers use translated copies. **[VERIFIED FULL TEXT — Eq. (5), PDF p. 6]**

For the upper jammed region, the printed quadratic is:

**Printed Eq. (6) [VERIFIED FULL TEXT]:**

\[
\tau=k_\tau y^2
-\frac{k_\tau h^2-4k_\tau y_s^2+4\tau_{cr}}{2(h-2y_s)}y
+\frac{k_\tau h y_s-2k_\tau y_s^2+2\tau_{cr}}{2(h-2y_s)}h,
\qquad y_s\le y\le\frac{h}{2}.
\]

Here \(\tau\) [Pa], \(k_\tau\) [Pa/m²], \(h,y,y_s\) [m], and \(\tau_{cr}\) [Pa] are defined above. It satisfies zero shear at the free surface and critical shear at the sliding boundary. The lower region is symmetric. **[VERIFIED FULL TEXT — Eq. (6), PDF p. 6]**

This architecture retains layer-scale offsets \(\delta\) but smooths the location of the last slipping interface into continuous \(y_s\). It is not an interface-by-interface complementarity/contact solution. **[INFERENCE]**

### 4.4 Loading-history rule

**Printed Eq. (7) [VERIFIED FULL TEXT]:**

\[
\begin{cases}
|Q|<Q_{cr}: & \text{full-jamming increment pattern},\\
|Q|\ge Q_{cr},\ \operatorname{sign}(\Delta Q)\operatorname{sign}(Q)<0:
& \text{full-jamming increment pattern},\\
|Q|\ge Q_{cr},\ \operatorname{sign}(\Delta Q)\operatorname{sign}(Q)\ge0:
& \text{half-jamming or full-sliding increment pattern}.
\end{cases}
\]

Here \(Q\) is current shear force [N]; \(Q_{cr}\) is the onset magnitude [N]; \(\Delta Q\) is the shear-force increment [N]; and \(\operatorname{sign}\) reports direction. On unloading/reversal, the increment is elastic/full-jamming-like; continued loading in the same direction preserves the partial/full-slip pattern. This rule introduces path dependence and enables hysteresis. It is an idealized stress-increment rule, not a measured re-stick law at each interface. **[VERIFIED FULL TEXT — Eq. (7), PDF p. 7; final distinction is INFERENCE]**

### 4.5 Curved-beam equilibrium

**Printed Eq. (8) [VERIFIED FULL TEXT]:**

\[
\frac{dN}{ds}=-Q\theta'-q_s,
\qquad
\frac{dQ}{ds}=N\theta'+q_y,
\qquad
\frac{dM}{ds}=Q.
\]

Here \(s\) is arc coordinate [m]; \(N\) is axial force [N]; \(Q\) is shear force [N]; \(M\) is bending moment [N·m]; \(\theta\) is cross-section rotation [rad]; \(\theta'=d\theta/ds\) is curvature [m\(^{-1}\)]; and \(q_s,q_y\) are distributed-load components along the tangent and thickness axes [N/m]. The derivation neglects second-order differentials and uses \(\cos(d\theta)\approx1\), \(\sin(d\theta)\approx d\theta\). **[VERIFIED FULL TEXT — Eq. (8), PDF p. 7]**

Printed Eq. (9) is presented as an integrated force solution, but the displayed integral contains only a rotation matrix and \(d\xi\), with no visible distributed-load vector. Here \(\xi\) would be an integration coordinate [m], and \(N_0,Q_0\) are reaction-derived forces at \(s_0\). As printed, the equation is dimensionally incomplete, so this audit does not silently reconstruct the missing factor. **[VERIFIED FULL TEXT — Eq. (9), PDF p. 8; dimensional assessment is INFERENCE]** The surrounding sentence also says the first two equations of “Eq. (7)” give Eq. (9), although the balance equations are Eq. (8).

### 4.6 Stress coefficients from section resultants

**Printed Eq. (11) [VERIFIED FULL TEXT]:**

\[
k_\sigma=
\frac{12M}
{b\delta^3\left[2n-2\left(n-2y_s/\delta\right)
\left(1-n/2+y_s/\delta\right)
\left(1+2n+2y_s/\delta\right)\right]}.
\]

Here \(k_\sigma\) is axial-stress gradient [Pa/m]; \(M\) is moment [N·m]; \(b,\delta,y_s\) are lengths [m]; and \(n\) is layer count. It comes from requiring the moment of the piecewise axial-stress field to equal \(M\). **[VERIFIED FULL TEXT — Eqs. (10)–(11), PDF p. 8]**

For stress increments:

**Printed Eq. (12) [VERIFIED FULL TEXT]:**

\[
k'_\sigma=
\frac{12\Delta M}
{b\delta^3\left[2n-2\left(n-2y_s/\delta\right)
\left(1-n/2+y_s/\delta\right)
\left(1+2n+2y_s/\delta\right)\right]}.
\]

Here \(k'_\sigma\) is the incremental axial-stress gradient [Pa/m] and \(\Delta M\) is moment increment [N·m]; remaining symbols are defined above. It uses the same current sliding boundary. **[VERIFIED FULL TEXT — Eq. (12), PDF p. 8]**

The shear coefficient is:

**Printed Eq. (14) [VERIFIED FULL TEXT]:**

\[
k_\tau=
\frac{12b\tau_{cr}(n\delta+2y_s)-24Q}
{8b y_s\delta^2+b(n\delta-2y_s)^3}.
\]

Here \(k_\tau\) [Pa/m²] sets the quadratic shear field; \(\tau_{cr}\) [Pa] is the Coulomb limit; \(Q\) [N] is section shear; \(b,\delta,y_s\) [m] are geometric quantities; and \(n\) is layer count. It enforces that the integral of shear stress over the cross-section equals \(Q\). **[VERIFIED FULL TEXT — Eqs. (13)–(14), PDF p. 8]**

Printed Eq. (15) uses the same form with \(\Delta Q\) in place of \(Q\) to define \(k'_\tau\), while retaining the \(\tau_{cr}\) term. Here \(k'_\tau\) is the incremental quadratic coefficient [Pa/m²], and \(\Delta Q\) is shear-force increment [N]. **[VERIFIED FULL TEXT — Eq. (15), PDF p. 8]**

### 4.7 Local equilibrium and the sliding-boundary relation

**Printed Eqs. (16)–(17) [VERIFIED FULL TEXT]:**

\[
\frac{\partial\sigma}{\partial s}
+\frac{\partial\tau}{\partial y}=0,
\qquad
\left(\frac{\partial k_\sigma}{\partial s}+2k_\tau\right)y
=\frac{1}{bh}\frac{dN}{ds}.
\]

Here \(\partial/\partial s\) and \(\partial/\partial y\) are spatial derivatives [m\(^{-1}\)]; \(\sigma,\tau\) are stresses [Pa]; \(k_\sigma\) [Pa/m] and \(k_\tau\) [Pa/m²] are field coefficients; \(N\) is axial force [N]; and \(b,h,y,s\) are lengths [m]. The right-hand side is neglected when curvature is small and tangential distributed load is nonzero only at isolated points. This is one point where a nominally “large-deformation” algorithm still invokes a large-radius/small-curvature simplification in deriving \(y_s(Q)\). **[VERIFIED FULL TEXT — Eqs. (16)–(17), PDF p. 8; last implication is INFERENCE]**

The resulting dimensionless implicit relation is:

**Printed Eq. (18) [VERIFIED FULL TEXT]:**

\[
\frac{3Q}{2nb\delta\tau_{cr}}
=1+\frac{1}{2n}+\frac{y_s}{n\delta}
-\frac{1}{4-2n+4y_s/\delta}
+\frac{1}{4y_s/\delta-2}.
\]

Here \(3Q/(2nb\delta\tau_{cr})\) is a dimensionless normalized shear load; \(1/n\) is inverse layer count; and \(y_s/(n\delta)=y_s/h\) is the normalized sliding-boundary coordinate. All dimensional symbols are defined above. This equation is a central result: it connects load, pressure/friction through \(\tau_{cr}\), layer count/thickness, and slip-zone extent. **[VERIFIED FULL TEXT — Eq. (18), Fig. 5(a), PDF pp. 8–9]**

### 4.8 Closed-form approximation to the sliding boundary

The paper removes the final term of Eq. (18) and adjusts the result to pass through the full-jamming/partial-slip transition:

**Printed Eq. (19) [VERIFIED FULL TEXT]:**

\[
\frac{3Q}{2nb\delta\tau_{cr}}
\approx1+\frac{1}{2n}+\frac{y_s}{n\delta}
-\frac{1}{4-2n+4y_s/\delta}
-\frac{1}{2+2n}.
\]

Here all symbols and units are defined under Eq. (18). This is an algebraic approximation internal to the reduced model; it is not the comparison between the analytical model and explicit-interface FEA. **[VERIFIED FULL TEXT + INFERENCE]**

The closed form is:

**Printed Eq. (20) [VERIFIED FULL TEXT]:**

\[
y_s=-\frac{c_1+\sqrt{c_1^2-4c_2c_0}}{2c_2}\,n\delta,
\]

\[
c_0=-(4-2n)A-1,\qquad
c_1=4-2n-4A,\qquad
c_2=4n,
\]

\[
A=\frac{3Q}{2b\delta\tau_{cr}}-\frac12-n+\frac{n}{2+2n}.
\]

Here \(y_s\) [m] is sliding-boundary position; \(c_0,c_1,c_2,A\) are dimensionless auxiliary coefficients; and \(n,\delta,Q,b,\tau_{cr}\) retain their previous meanings and units. The equation is the quadratic solution generated by Eq. (19). **[VERIFIED FULL TEXT — Eq. (20), PDF p. 9]**

Figure 5(b) compares this approximate \(y_s(Q)\) with the “accurate” numerical solution of Eq. (18) for several \(\delta/h\) values from 0.05 to 0.4. The curves provide a graphical approximation check, but the paper reports no maximum, RMS, or relative error and no acceptance tolerance. Moreover, both curves belong to the same continuous-boundary analytical construction; neither is an explicit discrete-interface reference. **[VERIFIED FULL TEXT — Fig. 5, PDF p. 9; distinction is INFERENCE]**

### 4.9 Critical onset load

**Printed Eq. (21) [VERIFIED FULL TEXT]:**

\[
Q_{cr}=
\begin{cases}
\dfrac{2bn^3\delta\mu p}{3(n^2-1)}, & n\ \text{odd},\\[6pt]
\dfrac{nb\delta\mu p(3-2n)}{6-3n}, & n\ \text{even}.
\end{cases}
\]

Here \(Q_{cr}\) is critical shear-force magnitude [N]; \(b,\delta\) are widths/thicknesses [m]; \(n\) is layer count; \(\mu\) is friction coefficient; and \(p\) is pressure [Pa]. The onset boundary uses \(y_s=-\delta/2\) for odd \(n\) and \(y_s=0\) for even \(n\). Equation (21) predicts direct proportionality to pressure and friction. **[VERIFIED FULL TEXT — Eq. (21), PDF p. 9]**

The prose says \(Q_{cr}\) is computed from “Eq. (16),” but the relevant load–boundary relation is Eq. (18). This appears to be a cross-reference error. **[VERIFIED FULL TEXT for the printed cross-reference; INFERENCE for the diagnosis]**

### 4.10 Curvature/deformation update

The surface strain is written in two ways:

**Printed Eqs. (22)–(23) [VERIFIED FULL TEXT]:**

\[
\left.\varepsilon\right|_{y=h/2}
=\frac{l-l_0}{l}
=\frac{\Delta\theta'}{\theta'+2/h},
\]

\[
\left.\varepsilon\right|_{y=h/2}
=\frac{1}{E}\left.\sigma\right|_{y=h/2}
=\frac{k_\sigma}{E}\left(\frac{h}{2}-y_s-\frac{\delta}{2}\right).
\]

Here \(\varepsilon\) is dimensionless axial strain at the upper surface; \(l_0\) and \(l\) are undeformed and deformed top-fiber arc lengths [m]; \(\theta'\) is initial curvature [m\(^{-1}\)]; \(\Delta\theta'\) is curvature increment [m\(^{-1}\)]; \(h,y_s,\delta\) are lengths [m]; \(E\) is Young's modulus [Pa]; \(\sigma\) is stress [Pa]; and \(k_\sigma\) is stress gradient [Pa/m]. The derivation assumes linear elasticity and neglects axial-force influence on bending deformation. **[VERIFIED FULL TEXT — Eqs. (22)–(23), PDF pp. 9–10]**

Combining them gives:

**Printed Eq. (24) [VERIFIED FULL TEXT]:**

\[
\Delta\theta'
=\frac{k_\sigma}{E}
\left(\theta'+\frac{2}{n\delta}\right)
\left(\frac{n-1}{2}\delta-y_s\right).
\]

Here \(\Delta\theta'\) [m\(^{-1}\)] is curvature change; \(k_\sigma/E\) has units m\(^{-1}\); \(\theta'\) and \(2/(n\delta)\) have units m\(^{-1}\); and the final bracket is length [m]. Remaining symbols are defined above. This equation makes initial curvature affect incremental stiffness/deformation. **[VERIFIED FULL TEXT — Eq. (24), PDF p. 10]**

For history-dependent loading, the paper substitutes the incremental coefficient:

**Printed Eq. (25) [VERIFIED FULL TEXT]:**

\[
\Delta\theta'
=\frac{k'_\sigma}{E}
\left(\theta'+\frac{2}{n\delta}\right)
\left(\frac{n-1}{2}\delta-y_s\right).
\]

Here \(k'_\sigma\) [Pa/m] is based on \(\Delta M\); all other symbols and units are as under Eq. (24). Algorithm 1 divides the loading history into \(m\) steps, updates forces and \(y_s\), chooses the increment pattern using Eq. (7), computes \(k'_\sigma\), and adds \(\Delta\theta\) to the current configuration. **[VERIFIED FULL TEXT — Eq. (25), Table 1, PDF p. 10]**

Algorithm 1 itself contains cross-reference/notation concerns: line 8 directs computation of \(k'_\sigma\) using Eq. (11), although Eq. (12) is the incremental formula, and line 9 mentions \(k_\sigma\) while citing Eq. (25), which uses \(k'_\sigma\). **[VERIFIED FULL TEXT; interpretation as inconsistency is INFERENCE]**

### 4.11 Equivalent bending inertia

**Printed Eq. (26) [VERIFIED FULL TEXT]:**

\[
I^{eq}=
\frac{12\left(\theta'+2/(n\delta)\right)
\left[(n-1)\delta/2-y_s\right]}
{b\delta^3\left[2n-2(n-2y_s/\delta)
(1-n/2+y_s/\delta)(1+2n+2y_s/\delta)\right]}.
\]

In the denominator, juxtaposition between \((n-2y_s/\delta)\), \((1-n/2+y_s/\delta)\), and \((1+2n+2y_s/\delta)\) denotes multiplication, exactly as printed. Here \(I^{eq}\) is labeled the equivalent second moment of area [m\(^4\)]; \(\theta'\) is initial curvature [m\(^{-1}\)]; \(n\) is layer count; \(\delta,b,y_s\) are lengths [m]; and all bracketed ratios are dimensionless. The equation is said to follow by casting Eq. (24) into an Euler–Bernoulli-like moment–curvature form. **[VERIFIED FULL TEXT — Eq. (26), PDF p. 12]**

As printed, however, Eq. (26)'s numerator is dimensionless and its denominator has units m\(^4\), so the right side has units m\(^{-4}\), not m\(^4\). Its printed orientation is also difficult to reconcile with the immediately reported \(I^{eq}_{\max}=bh^3/12\) and \(I^{eq}_{\min}=b\delta^2h/12\). A numerator/denominator inversion is plausible, but that is an **[INFERENCE]** and is not silently applied here. This is a second equation-level issue that must be resolved before implementation.

The paper reports the straight-beam limits:

\[
I^{eq}_{\max}=\frac{bh^3}{12},
\qquad
I^{eq}_{\min}=\frac{b\delta^2h}{12}.
\]

Here \(I^{eq}_{\max}\) and \(I^{eq}_{\min}\) [m\(^4\)] are full-jamming and full-sliding equivalent inertias; \(b,h,\delta\) are lengths [m]. Their ratio is \((h/\delta)^2=n^2\), which is an **[INFERENCE]** obtained directly from the two verified printed limits. **[VERIFIED FULL TEXT — Sect. 5.1, PDF p. 12]**

## 5. Treatment of the required mechanical phenomena

| Topic | Treatment in the paper | Adversarial limitation |
|---|---|---|
| Physical layer count | \(n\) is explicit in \(h=n\delta\), \(k_\sigma\), \(k_\tau\), \(y_s(Q)\), \(Q_{cr}\), and \(I^{eq}\); FEA uses 5, 10, 25 layers. **[VERIFIED FULL TEXT]** | Experimental layer counts are not explicitly listed, and \(n\) is not varied independently of \(\delta\) and nominal \(h\). **[VERIFIED FULL TEXT + INFERENCE]** |
| Individual thickness | \(\delta\) is explicit; experiments compare 0.3, 0.5, 1.0 mm. **[VERIFIED FULL TEXT]** | Thickness changes physical layer count when total height is held approximately fixed, so their effects are confounded. **[INFERENCE]** |
| Total stack thickness | FEA uses 5 mm; experimental descriptions use 5 mm and 5.1 mm in different passages. **[VERIFIED FULL TEXT]** | The paper does not reconcile those nominal heights or give tolerance. |
| Vacuum/hydrostatic pressure | Uniform \(p\) sets Coulomb capacity \(\mu p\); FEA uses 0.1 MPa; experiments use 40, 70, 100 kPa. **[VERIFIED FULL TEXT]** | Actual contact pressure is not solved; fabrication nonuniformity is blamed for critical-load overprediction. |
| Interlayer friction | Constant Coulomb \(\mu\); experimental fit gives \(\mu=0.114\), whereas exploratory FEA assumes \(\mu=0.5\). **[VERIFIED FULL TEXT]** | No rate/state dependence, pressure-dependent \(\mu\), or direct tribology measurement. |
| Interlayer slip | Piecewise stress fields and \(y_s\) describe the sliding region. **[VERIFIED FULL TEXT]** | Individual interface displacement is not solved; discrete release is smoothed. |
| Pre-slip | Full-jamming elastic field; initial stiffness and \(Q_{cr}\). **[VERIFIED FULL TEXT]** | Microslip/contact compliance is not modeled. |
| Progressive/partial slip | Central sliding region expands as \(y_s(Q)\); stiffness decreases. **[VERIFIED FULL TEXT]** | The actual stepped interface sequence is replaced by a continuous boundary. |
| Full slip | Set \(y_s=h/2-\delta\); FEA at 8 N is described as all friction pairs sliding. **[VERIFIED FULL TEXT]** | No separately reported experimental full-slip threshold/error. |
| Bending curvature | Initial \(\theta'\) enters Eqs. (22)–(26); semicircular/quarter-circular beams are tested. **[VERIFIED FULL TEXT]** | Curvature is not swept continuously and the reported semicircular radius is inconsistent. |
| Large deformation | Incremental force/configuration updates in Algorithm 1. **[VERIFIED FULL TEXT]** | No step-size convergence study or error-versus-curvature map; derivation of Eq. (18) assumes small \(\theta'\). |
| Boundary/end effects | Curved-beam balance is general; a freely sliding frame reduces horizontal constraint. **[VERIFIED FULL TEXT]** | FEA stress is sampled at one interior section; no systematic end-effect study. Support compliance causes cyclic discrepancies. |
| Transverse normal stress/strain | Interlayer normal strain is explicitly disregarded and the state is reduced to \(\sigma,\tau\). **[VERIFIED FULL TEXT]** | No transverse-normal-stress field or validity test; this omission is not quantified. |
| Cyclic loading/hysteresis | Eq. (7), Eq. (25), and Algorithm 1 track increments; straight and curved beams undergo five cycles between ±3 mm at 100 kPa. **[VERIFIED FULL TEXT]** | Dissipation is underpredicted and long-cycle wear/rate effects are not tested. |

## 6. Experimental setup and parameter ranges

### Straight beams

- PVC sheets inside a polyethylene vacuum bag;
- nominal length 100 mm and width 20 mm;
- total height described as 5 mm in Sect. 4 and 5.1 mm in Sect. 5.2;
- \(\delta=0.3\) mm for pressure tests at 40, 70, and 100 kPa;
- \(\delta=0.3,0.5,1.0\) mm for thickness tests at 100 kPa;
- cantilever deflection stopped at 5 mm;
- five repetitions used to calculate mean and standard deviation.

**[VERIFIED FULL TEXT — Sect. 4 and Sect. 5.2, Figs. 6–7, PDF pp. 10–13]** The text says “four” 0.3-mm cantilevers but lists three pressure levels; the unreported fourth condition/specimen is an unresolved source ambiguity.

### Curved beams

PVC layers are thermoplastically formed at 70 °C for 1 h. Sect. 4 and Fig. 7(c) give a semicircular cantilever radius of 47.75 mm and a quarter-circle simply supported radius of 95.50 mm, both with 150 mm arc length, 20 mm width, approximately 5.1 mm height, and 0.3 mm layers. The semicircular cantilever is tested at 40, 70, and 100 kPa. **[VERIFIED FULL TEXT — Sect. 4, Fig. 7(c)–(d), PDF pp. 11–13]**

Sect. 5.3 instead reports a radius of 31.8 mm for the tested semicircular cantilever. The paper does not reconcile 31.8 mm with 47.75 mm. This report does not select one silently. **[VERIFIED FULL TEXT — PDF pp. 11–13]**

### Cyclic tests

Straight and quarter-circular beams with 0.3 mm sheets are simply supported and driven between +3 and −3 mm for five cycles at 100 kPa. Force–deflection loops are compared with the incremental analytical model. **[VERIFIED FULL TEXT — Sects. 4 and 5.4, Fig. 7(e)–(f), PDF pp. 11 and 14]**

## 7. FEM or numerical reference model

The exploratory FEA is a 2-D plane-stress Abaqus model of a 100 mm × 20 mm × 5 mm simply supported LJS beam. It represents 5, 10, and 25 physical layers with CPS4R reduced-integration quadrilaterals. Element side lengths are 0.1, 0.05, and 0.02 mm for the three layer counts; \(E=0.3\) GPa, \(\mu=0.5\), and \(p=0.1\) MPa are assumed. A nominal end load is distributed across layer ends for convergence; one bottom-layer node is vertically constrained, and symmetric conditions are applied at the right edges. Stress fields are examined 40 mm from the left endpoint at loads including 2, 4, and 8 N and during ±0.5 N increments. **[VERIFIED FULL TEXT — Sect. 2.1 and Fig. 3, PDF pp. 3–5]**

The FEA explicitly contains separate layers and friction pairs, so it is the closest in-paper reference to discrete interlayer mechanics. But it is used to *discover and justify the analytical stress-pattern ansatz*, not as an independent blind validation dataset. The paper does not report an analytical-versus-FEA error norm across \(n,p,Q\), and the inspected text does not fully specify contact enforcement, friction regularization, or convergence tolerances. **[VERIFIED FULL TEXT + INFERENCE]**

## 8. What quantities are actually validated

| Quantity | Reference and coverage | Validation strength |
|---|---|---|
| Forms of axial/shear stress through thickness | Layered FEA at 5, 10, 25 layers; loads 2, 4, 8 N and selected increments | Pattern-level support, not a reported error metric. **[VERIFIED FULL TEXT]** |
| Full/partial/full-slip state interpretation | FEA stress/contact behavior at selected loads | State demonstration, not mapped transition error. **[VERIFIED FULL TEXT]** |
| Load–deflection versus pressure | Straight 0.3-mm-layer cantilevers at 40, 70, 100 kPa | Experimental curve comparison with five-repeat mean/SD. **[VERIFIED FULL TEXT]** |
| Load–deflection versus layer thickness | Straight cantilevers at 0.3, 0.5, 1.0 mm and 100 kPa | Experimental curve comparison, but thickness and layer count co-vary. **[VERIFIED FULL TEXT + INFERENCE]** |
| Initially curved response | Semicircular cantilever at three pressures | Curve-level comparison; radius ambiguity remains. **[VERIFIED FULL TEXT]** |
| Hysteresis shape | Straight and quarter-circle simply supported beams, ±3 mm, five cycles, 100 kPa | Qualitative loop reproduction; dissipation magnitude is underpredicted. **[VERIFIED FULL TEXT]** |
| Critical sliding load trend | Transition inferred from minimum variance of incremental stiffness | Pressure proportionality demonstrated; model overpredicts, especially low pressure/thin layers. **[VERIFIED FULL TEXT]** |
| Continuous \(y_s\) approximation | Eq. (19)/(20) versus numerical solution of Eq. (18), \(\delta/h=0.05\)–0.4 | Internal analytical approximation check only, not discrete-interface validation. **[VERIFIED FULL TEXT + INFERENCE]** |

## 9. Quantitative prediction errors reported

The paper does **not** report RMSE, MAE, maximum relative error, confidence intervals for model parameters, transition-load percentage error, loop-area error, or a continuum-versus-discrete error norm. Figures show theoretical curves, experimental means, and experimental scatter, but no numerical accuracy table. **[VERIFIED FULL TEXT — Sects. 4–5 and Fig. 7, PDF pp. 10–14]**

The quantitative numbers that do appear are test parameters and model coefficients, not general prediction errors. The only explicit discrepancy descriptions are directional:

- critical loads are overestimated, particularly at low pressure and for thin layers;
- theoretical frictional energy loss is smaller than experimental loss;
- near-zero-load cyclic curves are distorted, attributed to low support stiffness.

**[VERIFIED FULL TEXT — Sects. 5.2 and 5.4, PDF pp. 12 and 14]**

Accordingly, phrases such as “highly accurate” and “robust correlation” in the abstract/conclusion cannot be converted into a numerical validity domain. **[INFERENCE]**

## 10. Dimensionless groups and scaling laws

The paper explicitly identifies that Eq. (18) depends on \(1/n\) and \(y_s/(n\delta)\), and Fig. 5 uses \(\delta/h\). The central dimensionless quantities are:

\[
\lambda=\frac{\delta}{h}=\frac{1}{n},
\qquad
\eta=\frac{y_s}{h}=\frac{y_s}{n\delta},
\qquad
\Pi_Q=\frac{3Q}{2nb\delta\tau_{cr}}.
\]

Here \(\lambda\) is relative layer thickness/inverse layer count; \(\eta\) is normalized sliding-boundary position; and \(\Pi_Q\) is normalized shear force. All are dimensionless; \(\delta,h,y_s,b\) are lengths, \(Q\) is force, and \(\tau_{cr}\) is stress. The symbols \(\lambda,\eta,\Pi_Q\) are introduced here for clarity and are **[INFERENCE]**; the ratios themselves are **[VERIFIED FULL TEXT — Eq. (18), Fig. 5, PDF pp. 8–9]**.

Verified scaling results include:

- \(Q_{cr}\propto\mu p\) at fixed geometry/layer count;
- full-jam to full-slip inertia ratio equals \(n^2\) by direct algebra from the printed limits;
- the authors state that continuous-\(y_s\) smoothing becomes more accurate as \(\delta\) decreases.

The first and third are **[VERIFIED FULL TEXT]**; the explicit \(n^2\) ratio is **[INFERENCE]** from verified formulas.

## 11. Transition criteria and critical thresholds

The paper supplies quantitative mechanics thresholds:

1. local slip capacity \(|\tau|=\mu p\);
2. full-jamming to partial-slip onset at \(|Q|=Q_{cr}\), with odd/even formulas in Eq. (21);
3. full-sliding saturation at \(y_s=h/2-\delta\);
4. unloading/reloading state selection through the sign criterion in Eq. (7);
5. experimental slip onset inferred from the minimum variance of the differential stiffness \(\Delta F/\Delta w\).

**[VERIFIED FULL TEXT — Sects. 2.2, 3.2, 4–5, PDF pp. 6–12]**

These are transition thresholds *inside the mechanical model or experiment*. They are not thresholds for model validity. Confusing “slip begins at \(Q_{cr}\)” with “the continuum approximation fails at \(Q_{cr}\)” would be incorrect. **[INFERENCE]**

## 12. Does the paper map validity as a function of parameters?

**Not in the tolerance/error sense required by the surviving question. [INFERENCE]**

The paper does vary or illustrate many relevant parameters:

- FEA layer counts 5, 10, 25;
- analytical approximation curves at \(\delta/h=0.05,0.1,0.2,0.3,0.4\);
- experimental layer thickness 0.3, 0.5, 1.0 mm;
- pressure 40, 70, 100 kPa;
- straight and curved geometries;
- monotonic and cyclic histories;
- multiple loads spanning modeled slip regimes.

**[VERIFIED FULL TEXT]**

But these are demonstrations and parameter comparisons, not a map from \((n,p,Q\text{ or }\kappa,\text{regime})\) to a defined model-error metric. Layer count is not independently controlled in the experiments; FEA is used to construct the model; and no accept/reject tolerance is applied. **[VERIFIED FULL TEXT + INFERENCE]**

## 13. Does it define a quantitative breakdown criterion?

**No. [INFERENCE]**

The paper defines physical slip transitions and describes discrepancies, but never states a criterion such as “the reduced model is valid while force error is below 5%” or “breakdown occurs when slip-boundary error exceeds one layer.” It does not locate a surface or interval at which an error tolerance is crossed. The tested range, an internal Eq. (19)-versus-Eq. (18) approximation, and qualitative mismatch observations must not be relabeled as a breakdown boundary. **[VERIFIED FULL TEXT + INFERENCE]**

## 14. Does it identify why the continuum/reduced model fails?

It identifies several plausible mechanisms, but at different evidence levels:

| Mechanism | Evidence status | What is established |
|---|---|---|
| Discrete interface activation replaced by continuous \(y_s\) | **[VERIFIED FULL TEXT]** | Authors explicitly describe the smoothing approximation and say it improves as layers become thinner. No error magnitude is given. |
| Nonuniform actual pressure from fabrication imperfections | **[VERIFIED FULL TEXT]** | Proposed explanation for critical-load overprediction, especially at low applied pressure. No pressure field is measured. |
| Low support stiffness | **[VERIFIED FULL TEXT]** | Proposed explanation for near-zero-load cyclic distortion and excess experimental dissipation. No fixture-compliance model is fitted. |
| Neglected axial force in bending stress/deformation | **[VERIFIED FULL TEXT]** | Stated assumption; no sensitivity or failure threshold. |
| Neglected interlayer normal strain/transverse stress | **[VERIFIED FULL TEXT]** | Stated reduction; not tested as a cause of error in this paper. |
| Large-curvature effect on the derivation of \(y_s(Q)\) | **[INFERENCE]** | Eq. (17)'s right side is neglected partly because \(\theta'\) is assumed small, yet the algorithm is promoted for large deformation/curved beams. No breakdown test isolates this approximation. |
| Coulomb coefficient variability, viscoelasticity, rate, wear | **[INFERENCE]** | Not modeled or isolated experimentally; five cycles do not establish long-term validity. |

The paper therefore qualitatively identifies limitations and plausible mismatch causes, including the central discrete-to-continuous smoothing. It does not quantify which mechanism becomes dominant first in parameter space. **[INFERENCE]**

## 15. Are calibration and independent validation separated?

**Partially, but not as a formal train/validation protocol. [VERIFIED FULL TEXT + INFERENCE]**

The authors fit \(E=0.99\) GPa and \(\mu=0.114\) from deformation data for a straight cantilever made of 1.0 mm sheets at 100 kPa. They then use those parameters for comparisons at other pressures, thinner sheets, curved geometries, and cyclic loading. Those other conditions provide a degree of condition-level external checking. **[VERIFIED FULL TEXT — Sect. 4, Fig. 6(b), PDF p. 11]**

However:

- the 1.0 mm, 100 kPa case also appears in the thickness comparison and is therefore calibration, not independent validation;
- no held-out protocol is declared;
- \(E\) and \(\mu\) are fitted jointly from structural response rather than measured independently;
- no parameter uncertainty or sensitivity is reported;
- the FEA that motivates the analytical stress pattern uses different assumed \(E\) and \(\mu\), and is not an independent final-model validation set.

**[VERIFIED FULL TEXT + INFERENCE]**

## 16. Direct comparison with the verified model lineage

| Dimension | Narang et al. 2018 | Caruso et al. 2023 | Zhang beam continuum 2025 | Zhang RVE/average-field model | Fan et al. 2026 | This paper |
|---|---|---|---|---|---|---|
| Primary aim | Foundational laminar mechanics/regimes | Explicit multilayer analytical bending/slip | Continuum-limit stress and slip-band beam model | Average-field elastoplastic continuum constitutive law | Dynamic/control model of LJ continuum robot | Closed-form straight/curved beam deformation with cyclic increments |
| Layer/interface representation | Two-layer analytical; explicit interfaces in multilayer FEA | Interface-indexed sequential slip | Interfaces replaced by continuous through-height fields and \(y_s\) | Two-layer RVE averaged to macro constitutive response | LJ friction lumped at virtual PCC joints | Physical \(n,\delta\) retained, but slipping-interface advance smoothed into continuous \(y_s\) |
| Pressure | Coulomb/contact mechanics | Explicit transition dependence | Uniform \(\mu p\) yield cap | Normal/shear stress enters RVE yield law | Fitted \(\alpha_2(u_P),\phi(u_P)\) | Uniform \(\mu p\), explicit \(Q_{cr}\propto p\) |
| Layer count | Explicit in FEA/experiments | Explicit analytical \(N\) and tested counts | Mostly continuum-limit; selected 10/25-layer FEA | Constitutive scale; no structural count map | Absent from dynamics; fixed sheaths | Explicit formulas; FEA 5/10/25; experiment changes thickness but does not list exact \(n\) |
| Curvature/large deformation | Mainly beam cases in foundational work | Three-point bending, explicit support effects | Slender cantilever, with known boundary/full-slip limitations | Material-point/RVE loading | PCC robot configuration | Initially curved beams and iterative configuration update |
| Cyclic/hysteresis | Regimes/damping demonstrated | Hysteresis represented and validated | No complete cyclic validation | Elastoplastic loading/unloading checked against RVE FEA | LuGre hysteresis potential; no cyclic mechanics test | Five-cycle straight/curved hysteresis experiment and incremental model |
| Validation reference | Experiment and contact FEA | Experiment and FEA | Discrete layered FEA plus one experiment | Periodic RVE FEA; no physical experiment | Robot-level experiments; no discrete mechanics | Layered FEA used to derive patterns; multi-condition experiments |
| Tolerance-defined validity map | No | No | No | No | No | No |

All factual entries are **[VERIFIED FULL TEXT]** from the repository evidence/PDFs; the representation labels are **[INFERENCE]** based on the published model architecture.

### What this paper adds relative to Narang and Caruso

Narang establishes the physical pre-slip/transition/full-slip framework and uses explicit contact FEA for many layers. Caruso retains individual interface order, predicts sequential slip and piecewise stiffness, and validates pressure/layer-count/hysteresis behavior under specific bending/support conditions. **[VERIFIED FULL TEXT — Narang 2018, Sects. 2–3; Caruso 2023, Sects. 2–5]**

This Zhang paper trades Caruso's discrete interface sequence for a smooth \(y_s\), derives a compact through-thickness field, and extends a beam-level analytical scheme to initially curved configurations and incremental cyclic loading. Its computational attractiveness comes precisely from averaging the discrete jumps that Caruso preserves. **[VERIFIED FULL TEXT + INFERENCE]**

### What this paper adds relative to “A continuum-based model for a layer jamming beam”

The other Zhang beam paper takes a thin-layer/high-layer-count continuum limit, derives continuous stress fields and a moving sliding band, and compares selected predictions with 10-/25-layer FEA and a 20-layer cantilever experiment. It reports boundary, transverse-normal-stress, and extreme/full-slip discrepancies. **[VERIFIED FULL TEXT — Zhang beam paper, Sects. 2–6, PDF pp. 2–9]**

The present paper is broader in loading and geometry: it retains explicit \(n\) and \(\delta\), uses a closed-form approximate \(y_s(Q)\), introduces stress-increment history, treats curved beams, and tests cyclic hysteresis. Yet it still does not calculate a systematic continuum-versus-discrete error surface. **[VERIFIED FULL TEXT + INFERENCE]**

### What this paper adds relative to “Continuum modeling for layer jamming structures”

The Zhang RVE/average-field paper develops a continuum elastoplastic constitutive law from a two-layer representative volume element and validates selected shear and coupled normal/shear paths against periodic discrete-cell FEA. That is closer to formal homogenization/effective-medium mechanics. **[VERIFIED FULL TEXT — Zhang RVE paper, Abstract and Sects. 2–4]**

The present paper instead works at beam structural scale. Its continuous \(y_s\) is a smoothed structural slip-front coordinate, not an RVE-derived internal variable or homogenized tensor. The two models address different levels and are not cross-validated against each other. **[INFERENCE]**

### What this paper adds relative to Fan 2026

Fan uses a finite-dimensional PCC rigid-link robot model with lumped LuGre friction and experimentally fitted pressure functions to support shape locking and feedback stiffness/configuration regulation. It does not resolve physical layers or compare against discrete-interface mechanics. **[VERIFIED FULL TEXT — Fan 2026, Sects. II–V]**

This Zhang paper is far closer to mechanics-level slip modeling: \(n,\delta,\mu,p,Q,M,y_s\) are explicit and the stress field is tied to beam equilibrium. Fan is primarily dynamic/control-oriented; this paper is quasi-static/path-incremental structural mechanics. **[INFERENCE]**

## 17. Seven distinctions required for falsification

| Distinction | Does this paper do it? | Evidence-based finding |
|---|---|---|
| A. Show that a continuum/reduced model exists | **Yes** | Continuous \(y_s\), piecewise fields, and beam equilibrium replace interface-by-interface events. **[VERIFIED FULL TEXT]** |
| B. Improve a continuum/reduced model | **Yes** | Closed-form approximation, curved-beam balance, large-configuration iteration, and cyclic increment rule broaden the representation. **[VERIFIED FULL TEXT]** |
| C. Demonstrate discrepancies | **Yes** | Critical-load overprediction, underpredicted dissipation, and near-zero-load cyclic mismatch are stated. **[VERIFIED FULL TEXT]** |
| D. Qualitatively identify limitations | **Yes** | Continuous-interface smoothing, nonuniform pressure, support compliance, planar/beam-stack restriction, and neglected normal strain/axial-force effects are disclosed or evident. **[VERIFIED FULL TEXT + INFERENCE]** |
| E. Quantitatively map model error | **No** | No error metric over \(n,p,Q/\kappa\), regime, or boundary condition. **[VERIFIED FULL TEXT + INFERENCE]** |
| F. Define a tolerance-based validity domain | **No** | No acceptance tolerance or valid/invalid classification. **[INFERENCE]** |
| G. Define a quantitative breakdown boundary | **No** | Physical slip thresholds are not model-error thresholds; no locus of tolerance crossing is calculated. **[INFERENCE]** |

## 18. Final adversarial verdict

# SUBSTANTIALLY NARROWS GAP

**[INFERENCE]**

### Strongest claim this paper pre-empts

> “No mechanics-level reduced/continuous-boundary model of beam-stack layer jamming has predicted pressure, layer-thickness/layer-count effects, curved-beam response, large configuration updates, progressive slip, and cyclic hysteresis with experimental comparison.”

That broad claim is pre-empted. **[INFERENCE grounded in VERIFIED FULL TEXT]** A project that merely adds more pressure values, sheet thicknesses, curved specimens, FEA cases, or hysteresis measurements would not establish a new mechanics question under the repository's novelty standard.

### Exact part of the current research question that survives

> **For one explicitly named mechanics-level continuum/reduced model and one fixed material/beam family, quantify its prediction error relative to an explicit-interface reference and independently calibrated experiments over independently controlled layer count, pressure, and nondimensional bending load/curvature; predeclare acceptable errors for transition load, force–deflection, slip-zone/interface state, and dissipated energy; and locate the parameter boundary at which each tolerance is first exceeded.** **[INFERENCE]**

The phrase “which omitted mechanism first causes failure” survives only if the study isolates competing causes—discrete interface jumps, nonuniform normal pressure, boundary compliance/end effects, transverse normal stress/strain, large-curvature kinematics, and friction/path dependence—rather than attributing mismatch after the fact. **[INFERENCE]**

### Most dangerous unresolved overlap

The most dangerous overlap is Fig. 5 plus the 5/10/25-layer FEA and multi-pressure/multi-thickness experiments. Together, they almost form the skeleton of a validity study: a normalized layer-thickness variable, an exact-versus-approximate \(y_s\) comparison, explicit layered simulations, and experimental response curves. **[VERIFIED FULL TEXT]**

What is missing is the decisive quantitative layer: the “accurate” Fig. 5 curve is only Eq. (18), not discrete mechanics; FEA helped formulate rather than independently test the model; errors are not calculated; and no tolerance turns the comparisons into a validity boundary. **[INFERENCE]** A future proposal that does not add those elements would be substantially duplicated by this paper.

### Next paper/search needed to falsify the surviving question

No not-yet-inspected title is promoted here as evidence. The next adversarial search should target papers that explicitly compare a continuous-slip, average-field, partial-interaction, or homogenized layered-beam model against discrete frictional interfaces **with numerical error or convergence versus \(n\) or \(\delta/h\)**. **[INFERENCE / FUTURE WORK]**

The highest-yield next search is a forward- and backward-citation check from both Zhang beam papers and the Zhang RVE paper using concept combinations such as:

- `layer jamming discrete continuum error layer count`
- `layer jamming sliding boundary validation δ/h`
- `frictional multilayer beam homogenization convergence`
- `partial interaction laminated beam discrete interface continuum validity`
- `layer jamming RVE structural beam validation experiment`

The falsifying target is a paper that supplies all four of: explicit-interface reference, independent experiment, declared error metric/tolerance, and a boundary over layer count/pressure/load or slip regime. If such a paper exists, the surviving question may be killed. **[INFERENCE / FUTURE WORK]**

## 19. Provenance and non-invention audit

### Primary paper claims

| Claim | Evidence label | Provenance |
|---|---|---|
| Continuous \(y_s\) intentionally smooths discrete interface releases | **[VERIFIED FULL TEXT]** | Sect. 2.2, PDF p. 7 |
| Explicit FEA uses 5, 10, 25 layers | **[VERIFIED FULL TEXT]** | Sect. 2.1, Fig. 3, PDF pp. 4–5 |
| Equations link \(n,\delta,p,\mu,Q,y_s\) | **[VERIFIED FULL TEXT]** | Eqs. (18)–(21), PDF pp. 8–9 |
| Curved/large-history model uses incremental curvature | **[VERIFIED FULL TEXT]** | Eqs. (22)–(25), Algorithm 1, PDF pp. 9–10 |
| Pressure tests cover 40/70/100 kPa | **[VERIFIED FULL TEXT]** | Sects. 4 and 5.2–5.3, PDF pp. 10–13 |
| Thickness tests cover 0.3/0.5/1.0 mm | **[VERIFIED FULL TEXT]** | Sects. 4 and 5.2, PDF pp. 10–12 |
| Cyclic tests use ±3 mm for five cycles at 100 kPa | **[VERIFIED FULL TEXT]** | Sects. 4 and 5.4, PDF pp. 11 and 14 |
| Critical load is overpredicted at low pressure/thin layers | **[VERIFIED FULL TEXT]** | Sect. 5.2, PDF p. 12 |
| Theory underpredicts experimental frictional loss | **[VERIFIED FULL TEXT]** | Sect. 5.4, PDF p. 14 |
| No numerical error/tolerance/breakdown map is reported | **[VERIFIED FULL TEXT + INFERENCE]** | Complete methods/results; absence assessed against the explicitly reported outputs |

### Source-level ambiguities preserved rather than repaired

1. Eq. (1) contains \(E\) while labeling the output stress; dimensions and Eq. (23) suggest a typographical problem.
2. Eq. (9) appears to omit the distributed-load vector from its integral and is dimensionally incomplete as printed.
3. Text points to Eq. (7) instead of Eq. (8) before Eq. (9), and to Eq. (16) instead of the apparent Eq. (18) before \(Q_{cr}\).
4. Algorithm 1 points to Eq. (11) for incremental \(k'_\sigma\), while Eq. (12) is the incremental expression, and then uses inconsistent priming in the next line.
5. Experimental total height is described as both 5.0 and 5.1 mm.
6. The semicircular radius is 47.75 mm in Sect. 4/Fig. 7(c) but 31.8 mm in Sect. 5.3.
7. The text says four 0.3-mm cantilevers were tested but lists only three pressure conditions.
8. Sect. 5.2 points to Fig. 7(b) for the pressure comparison and Fig. 7(c) for the thickness comparison, whereas the Fig. 7 caption identifies those panels as 7(a) and 7(b), respectively.

All eight are **[VERIFIED FULL TEXT]** as printed-source inconsistencies; the diagnosis of likely typographical or reporting error is **[INFERENCE]**. None was silently resolved.

### Comparative evidence provenance

- Narang evidence: `data/evidence/2018-Mechanically Versatile Soft Machines through Laminar_5f7ccd7357.json`; `paper_id: 5f7ccd7357`; D1-V001. **[VERIFIED FULL TEXT]**
- Caruso evidence: `data/evidence/2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation_652e62758f.json`; `paper_id: 652e62758f`; D1-V001. **[VERIFIED FULL TEXT]**
- Zhang beam evidence: `data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json`; `paper_id: 95646b2cfc`; D1-V002. **[VERIFIED FULL TEXT]**
- Zhang RVE evidence: `data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json`; `paper_id: a792efc445`; D1-V002. **[VERIFIED FULL TEXT]**
- Fan evidence: `data/evidence/2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming_1f05cf83bc.json`; `paper_id: 1f05cf83bc`; D1-V003. **[VERIFIED FULL TEXT]**

No registry, ingestion status, prior verification output, or scientific-state file was changed to produce this analysis.

## 20. Reference

Zhang, S.; Yao, J.; Zhao, W.; Zhu, K. (2025). “Toward a deeper understanding of layer jamming structures.” *Frontiers of Mechanical Engineering*, 20(4), article 27. DOI: `10.1007/s11465-025-0843-5`. **[VERIFIED FULL TEXT — article front matter, PDF p. 1]**

## Bottom line

This paper already does much of the *mechanics breadth* that a validity/breakdown project might otherwise claim: reduced continuous slip-front modeling, explicit pressure and layer-scale variables, straight and curved bending, progressive/full slip, incremental large-deformation treatment, cyclic hysteresis, FEA motivation, and multi-condition experiments. **[VERIFIED FULL TEXT]** It substantially narrows the surviving direction to a rigorous error-and-tolerance study against genuinely independent explicit-interface and experimental references. It does not itself supply that quantitative validity domain or breakdown boundary. **[INFERENCE]**
