# Fan et al. (2026) — Adversarial Full-Text Model Audit

> **Verification round:** D1-V003  
> **Primary falsification question:** Does Fan et al. (2026) already establish the quantitative validity domain or breakdown boundaries of a continuum/reduced representation of layer-jamming mechanics relative to discrete interlayer mechanics or experiments?  
> **Scope:** Technical evidence audit, not a novelty adjudication. No claim in this report establishes novelty.

## Executive verdict

**Fan et al. does not kill the surviving mechanics-validity question. It narrows it and is mainly a control-oriented contribution.** **[INFERENCE]**

The paper does establish a finite-dimensional, control-oriented dynamic model of a layer-jamming (LJ) continuum robot, cast in port-Hamiltonian form and coupled to a LuGre friction state. It experimentally demonstrates shape retention, pressure-dependent transverse stiffness, and closed-loop configuration/stiffness regulation on one planar prototype. **[VERIFIED FULL TEXT — Fan 2026, Abstract; Sects. II–V; printed pp. 2219–2231 / PDF pp. 1–13]**

However, “continuum” in this paper primarily names the robot morphology. The robot body is approximated by a planar piecewise-constant-curvature (PCC) rigid-link model with finitely many generalized angles. The physical layers and their interfaces are not resolved: their distributed friction is replaced by one lumped LuGre state and friction torque at each virtual robot joint, while pressure dependence is represented through identified scalar functions. **[VERIFIED FULL TEXT — Fan 2026, Sects. II-A–II-C, Figs. 1–2, printed pp. 2221–2224 / PDF pp. 3–6]**

The paper does **not** compare this reduced representation with an explicit layer/interface model, does **not** measure interface slip or contact traction, does **not** sweep layer count under matched conditions, and does **not** construct an error surface or a quantitative failure boundary over layer count, pressure, curvature/load, and slip regime. **[VERIFIED FULL TEXT for the reported study design; INFERENCE for the resulting gap assessment — Fan 2026, Sects. V–VI, printed pp. 2228–2232 / PDF pp. 10–14]**

### Six distinctions required by the falsification question

| Test | Finding | Evidence-based answer |
|---|---|---|
| A. Existence of a continuum/dynamic/control model | A control-oriented dynamic model exists. It uses PCC robot coordinates, a port-Hamiltonian energy balance, LuGre friction, and pressure-dependent fitted coefficients. | **YES — [VERIFIED FULL TEXT]** |
| B. Accuracy of that model | Some output-level agreement is quantified: the pressure–transverse-stiffness fit has coefficient of determination \(R_s^2=0.9216\); configuration-control MAE spans 0.0152°–0.7826° in Table I. There is no reported field-level mechanics error or general out-of-sample model-error bound. | **PARTIAL — [VERIFIED FULL TEXT]** |
| C. Validation against experiments | Shape locking, transverse stiffness trends, parameter identification, setpoint regulation, and stiffness regulation are tested on OctRobot-I. | **YES, within the tested prototype and ranges — [VERIFIED FULL TEXT]** |
| D. Validation against discrete interlayer mechanics | No explicit-interface analytical model, discrete-layer FEA, interface traction, or interface-slip field is used as a reference. | **NO — [VERIFIED FULL TEXT]** |
| E. Systematic validity-domain mapping | The experiments use fixed two-layer and five-layer sheaths for different tasks, not a factorial or convergence study. No accuracy-tolerance map is reported. | **NO — [VERIFIED FULL TEXT + INFERENCE]** |
| F. Quantitative breakdown-boundary identification | The authors state an identification interval and qualitative operational limitations, but do not identify a critical error boundary for the reduced LJ mechanics. | **NO — [VERIFIED FULL TEXT + INFERENCE]** |

## 1. Evidence basis and terminology

### Primary source

- Fan, Y.; Yi, B.; Liu, D. (2026), “Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots,” *IEEE Transactions on Control Systems Technology*, 34(5), DOI `10.1109/TCST.2026.3690756`. Repository `paper_id: 1f05cf83bc`, `verification_id: D1-V003`; validated evidence JSON and the corresponding 15-page PDF were inspected. **[VERIFIED FULL TEXT]**

### Comparative full texts

- Narang, Vlassak, and Howe (2018), `paper_id: 5f7ccd7357`, D1-V001. **[VERIFIED FULL TEXT]**
- Caruso et al. (2023), `paper_id: 652e62758f`, D1-V001. **[VERIFIED FULL TEXT]**
- Zhang et al., “A continuum-based model for a layer jamming beam” (2025), `paper_id: 95646b2cfc`, D1-V002. **[VERIFIED FULL TEXT]**
- Zhang et al., “Continuum modeling for layer jamming structures,” `paper_id: a792efc445`, D1-V002. The article was available online in November 2025 and appears in *Theoretical and Applied Mechanics Letters* 16 (2026), article 100633; the DOI contains 2025. This report therefore calls it “Zhang RVE/average-field model” to avoid silently choosing between online and issue year. **[VERIFIED FULL TEXT — article front matter / PDF p. 1]**

No detailed scientific conclusion below is based on a metadata-only record. **[VERIFIED FULL TEXT]**, **[METADATA ONLY]**, and **[INFERENCE]** mean, respectively: directly supported by an inspected validated full text; known only bibliographically; or reasoned from the verified record but not asserted by the cited authors.

## 2. What physical system Fan models

The experimental object is a one-section tendon-driven continuum robot surrounded by a sealed sheath containing flexible layers. Two antagonistic tendons bend the robot. Applying negative gauge pressure to the sheath increases normal contact between adjacent layers and therefore increases friction. The same robot can then resist deformation more strongly or retain a bent shape after tendon force is removed. **[VERIFIED FULL TEXT — Fan 2026, Figs. 1 and 5–7; Sects. I, II-B, V-A–V-C, printed pp. 2219–2223 and 2228–2229 / PDF pp. 1–5 and 10–11]**

Fan's objective is not to recover the stress and slip at every layer interface. It is to obtain a model simple enough for real-time controller design while reproducing two aggregate phenomena:

1. **shape locking** after vacuum is applied and tendon actuation is released; and
2. **adjustable stiffness** controlled mainly by vacuum pressure.

**[VERIFIED FULL TEXT — Fan 2026, stated problems P1–P2 and contributions, printed pp. 2220–2221 / PDF pp. 2–3]**

This distinction is decisive. Fan models the dynamics of a *continuum robot with an LJ mechanism*; the paper is not a continuum derivation of the layer stack's local stress, contact, or slip fields. **[INFERENCE grounded in Fan 2026, Sects. II–III]**

## 3. Model class and state variables

### 3.1 Geometric reduction

The continuum body is approximated as \(n\) planar rigid-link segments under PCC. Each segment has uniform mass and length, and axial deformation caused by tendon tension is assumed negligible relative to bending. The experimental platform uses \(n=6\) virtual segments and \(m=2\) tendon inputs. **[VERIFIED FULL TEXT — Fan 2026, Sect. II-A, Fig. 2, printed pp. 2221–2222 / PDF pp. 3–4]**

The principal variables are:

| Symbol | Meaning | Dimension / units |
|---|---|---|
| \(q\in\mathbb{R}^n\) | vector of virtual-segment bending angles | rad (reported experimentally in degrees) |
| \(p\in\mathbb{R}^n\) | generalized momentum conjugate to \(q\) | not stated; mechanically consistent with kg·m²/s for angular coordinates |
| \(z\in\mathbb{R}^n\) | virtual LuGre bristle deflection at each virtual joint | unit allocation not specified because it is coupled to lumped coefficients |
| \(v\in\mathbb{R}^n\) | generalized relative velocity used by the friction model | rad/s for angular coordinates |
| \(u\in\mathbb{R}^m\) | nonnegative tendon-tension inputs | force units are implied, but the paper's input map absorbs the moment arm |
| \(u_P\ge 0\) | magnitude of negative pressure in the sheath; applied gauge pressure is \(-u_P\) | Pa in mechanics; experiments report kPa |
| \(\chi=\operatorname{col}(q,p,z)\) | complete reduced state | \(3n\) components |
| \(k_n\) | number of physical jamming layers | dimensionless integer |

**[VERIFIED FULL TEXT — Fan 2026, Nomenclature and Eqs. (1), (6), (12), printed pp. 2219 and 2222–2224 / PDF pp. 1 and 4–6]** Units not explicitly printed are marked as mechanics-based interpretation rather than author-reported values.

Crucially, \(n\) and \(k_n\) are different. The experiment has six *robot model segments*, but uses a five-layer sheath for shape locking and a two-layer sheath for stiffness/control. Conflating \(n=6\) with physical layer count would be a category error. **[VERIFIED FULL TEXT — Fan 2026, Nomenclature, Sect. V-A, printed pp. 2219 and 2228 / PDF pp. 1 and 10]**

### 3.2 Is it a continuum model?

- **Continuum-robot model:** yes, in the robotics sense that the device has a continuously deformable body. **[VERIFIED FULL TEXT]**
- **Distributed-parameter continuum mechanics model:** no; the governing state has \(3n\) ordinary differential-equation states rather than fields over arc length and thickness. **[VERIFIED FULL TEXT + INFERENCE]**
- **Homogenized layer-stack model:** no homogenization map, representative volume element, scale-separation argument, or effective constitutive tensor is derived. **[VERIFIED FULL TEXT + INFERENCE]**
- **Reduced-order/control-oriented representation:** yes. The authors explicitly seek a simplified control model, and distributed layer friction is lumped at virtual joints. **[VERIFIED FULL TEXT]**
- **Phenomenological effective model of LJ at robot level:** this is the most precise mechanics description. Pressure-dependent elastic and friction effects are fitted to aggregate robot data. **[INFERENCE]**

## 4. Port-Hamiltonian formulation

“Port-Hamiltonian” means that the dynamics are organized around stored energy, power-conserving interconnection, dissipative terms, and external input ports. This structure is valuable for passivity-based control because stability can be reasoned about from the energy balance. It does not, by itself, make the material mechanics spatially continuous or homogenized. **[VERIFIED FULL TEXT for Fan's formulation; INFERENCE for the terminology distinction]**

### 4.1 Robot without jamming

**Printed Fan Eq. (1):**

\[
\begin{bmatrix}\dot q\\ \dot p\end{bmatrix}
=
\begin{bmatrix}0&I_n\\-I_n&-D(q)\end{bmatrix}
\begin{bmatrix}\nabla_q H\\\nabla_p H\end{bmatrix}
+
\begin{bmatrix}0\\G(q)\end{bmatrix}u .
\]

Here \(\dot q\) [rad/s] and \(\dot p\) [generalized torque] are time derivatives; \(I_n\) is the dimensionless \(n\times n\) identity; \(D(q)\) is a positive-semidefinite damping matrix; \(G(q)\) maps the tendon input \(u\) into generalized torque; \(H\) is energy [J]; \(\nabla_q H\) is the energy gradient with respect to angle and has generalized-torque units; and \(\nabla_p H\) is generalized velocity [rad/s]. The zero blocks have the sizes required by the partition. **[VERIFIED FULL TEXT — Fan 2026, Eq. (1), printed pp. 2221–2222 / PDF pp. 3–4]**

The stored energy is:

**Printed Fan Eq. (2):**

\[
H(q,p)=\frac{1}{2}p^{\mathsf T}M^{-1}(q)p+U(q).
\]

Here \(M(q)\) is the positive-definite generalized inertia matrix [kg·m² for purely angular coordinates], \(p\) is generalized momentum, \(U(q)\) is potential energy [J], and superscript \({\mathsf T}\) denotes transpose. The first term is kinetic energy [J]; the second is stored gravitational and elastic energy. **[VERIFIED FULL TEXT — Fan 2026, Eq. (2), printed p. 2222 / PDF p. 4]**

The potential-energy approximation is:

**Printed Fan Eqs. (3)–(4):**

\[
U(q)=U_G(q)+U_E(q),\qquad
U_G=\alpha_1[1-\cos(q_\Sigma)],\qquad
U_E=\frac{1}{2}q^{\mathsf T}\Lambda q+U_0,
\]

\[
q_\Sigma=\sum_{i=1}^{n}q_i,qquad
\Lambda=\operatorname{diag}(\alpha_2,\ldots,\alpha_2).
\]

Here \(U_G\), \(U_E\), and \(U_0\) are energies [J]; \(q_i\) is segment angle [rad]; \(q_\Sigma\) is total bending angle [rad]; \(\alpha_1\) is a gravitational-energy coefficient [J under the radians-as-dimensionless convention]; \(\alpha_2\) is an elastic angular-stiffness coefficient [J/rad², conventionally N·m/rad]; \(\Lambda\) is the diagonal stiffness matrix; and \(\operatorname{diag}\) constructs a diagonal matrix. Uniform geometry makes every diagonal entry the same. **[VERIFIED FULL TEXT — Fan 2026, Eqs. (3)–(4), printed p. 2222 / PDF p. 4]**

Fan assumes air mass is negligible, so \(\alpha_1\) is pressure-independent, while \(\alpha_2=\alpha_2(u_P)\). All structural dissipation is then assigned to the LJ friction torque by setting \(D(q)=0\). **[VERIFIED FULL TEXT — Assumptions 1–2, printed p. 2222 / PDF p. 4]**

### 4.2 Robot–friction interconnection

Fan exposes friction as a passive port:

**Printed Fan Eqs. (5)–(6):**

\[
\dot x=J\nabla H(x)+G_r(x)u-G_f\tau_f,
\qquad
v=G_f^{\mathsf T}\nabla H(x)=M^{-1}(q)p,
\]

where \(x=\operatorname{col}(q,p)\) is the \(2n\)-state robot vector; \(J\) is the canonical skew-symmetric interconnection matrix; \(G_r\) maps tendon forces into the robot state equation; \(G_f\) maps friction torque into the momentum equation; \(\tau_f\in\mathbb{R}^n\) is the lumped friction torque [N·m]; and \(v\) is generalized velocity [rad/s]. **[VERIFIED FULL TEXT — Fan 2026, Eqs. (5)–(6), printed p. 2222 / PDF p. 4]**

### 4.3 LuGre friction as the LJ surrogate

LuGre friction represents rough contact as deformable microscopic bristles. Its internal state can reproduce pre-sliding displacement, stiction, Stribeck behavior, and gross sliding at a lumped contact. In Fan, each \(z_i\) belongs to a *virtual robot joint*, not to a named physical layer interface. **[VERIFIED FULL TEXT — Fan 2026, Sect. II-B and Eq. (7), printed p. 2223 / PDF p. 5]**

**Printed Fan Eq. (7):**

\[
\dot z=-R_z(v)\nabla H_z(z)+[N(v)-P(v)]v,
\qquad
\tau_f=[N(v)+P(v)]^{\mathsf T}\nabla H_z(z)+Sv.
\]

Here \(z\) is the vector of virtual bristle deflections; \(\dot z\) is its rate; \(H_z\) is stored virtual-bristle energy [J]; \(R_z\) is a nonnegative diagonal relaxation matrix; \(N(v)\) and \(P(v)\) are state-modulation matrices; \(v\) is generalized velocity [rad/s]; \(S\) is a viscous-friction matrix; and \(\tau_f\) is generalized friction torque [N·m]. The paper does not provide enough dimensional normalization to assign independent SI units to \(z\), \(R_z\), \(N\), \(P\), \(S\), and \(\phi\); only their products in energy and torque equations are dimensionally identifiable. **[VERIFIED FULL TEXT — Eq. (7) and Nomenclature; dimensional caveat is INFERENCE]**

The bristle energy and speed-dependent relaxation are:

**Printed Fan Eqs. (8)–(10):**

\[
H_z(z)=\frac{1}{2}\sigma_0\phi(u_P)\lVert z\rVert^2,
\qquad
R_z(v)=\operatorname{diag}(\beta_1,\ldots,\beta_n),
\qquad
\beta_i=\frac{|v_i|}{\phi(u_P)}\rho(v_i),
\]

\[
\rho(v_i)=\mu_C+(\mu_S-\mu_C)
\exp\!\left[-\left|\frac{v_i}{v_s}\right|^{\sigma_3}\right],
\]

\[
N(v)=I_n-\frac{1}{2}\sigma_1\phi(u_P)R_z(v),\quad
P(v)=-\frac{1}{2}\sigma_1\phi(u_P)R_z(v),\quad
S=(\sigma_1+\sigma_2)\phi(u_P)I_n.
\]

Here \(\lVert z\rVert\) is Euclidean magnitude; \(\sigma_0\) is bristle-stiffness coefficient; \(\phi(u_P)\) is a positive pressure-scaling function; \(v_i\) is joint velocity; \(\beta_i\) is the \(i\)th relaxation coefficient; \(\rho(v_i)\) is the Stribeck friction curve; \(\mu_S\) and \(\mu_C\) are dimensionless static and Coulomb friction coefficients; \(v_s\) is Stribeck velocity [rad/s in this generalized model]; \(\sigma_1\) is bristle damping; \(\sigma_2\) is viscous-friction coefficient; \(\sigma_3\) is a dimensionless curve-shape exponent; and \(\exp\) is the exponential function. The separate SI units of \(\sigma_0,\sigma_1,\sigma_2,\phi\), and \(z\) are not stated. **[VERIFIED FULL TEXT — Fan 2026, Eqs. (8)–(10), printed p. 2223 / PDF p. 5]**

At zero speed, \(\rho(0)=\mu_S\); at sufficiently high speed, \(\rho\) approaches \(\mu_C\). That is the lumped model's transition from static-friction capacity toward Coulomb friction. It is not a computed propagation of slip fronts through the physical stack. **[VERIFIED FULL TEXT for the equation; INFERENCE for its mechanics interpretation]**

The passivity condition is:

**Printed Fan Eq. (11):**

\[
\sigma_2>\sigma_1\frac{\mu_S-\mu_C}{\mu_C},
\qquad \mu_S\ge\mu_C>0.
\]

Here \(\sigma_1\) and \(\sigma_2\) are the LuGre damping and viscous coefficients, and \(\mu_S,\mu_C\) are the static and Coulomb friction coefficients. This inequality makes the interconnected friction description passive under the cited LuGre result; it is a mathematical admissibility condition, not an experimentally located layer-slip boundary. **[VERIFIED FULL TEXT — Fan 2026, Eq. (11) and Remarks 2–3, printed p. 2223 / PDF p. 5]**

### 4.4 Overall energy and dissipation

**Printed Fan Eqs. (12)–(14), abbreviated to the essential result:**

\[
\chi=\operatorname{col}(q,p,z),
\qquad
\dot\chi=[\mathcal J-\mathcal R]\nabla\mathcal H+\mathcal G(\chi)u_\chi,
\]

\[
\mathcal H(\chi,u_P)=
\frac{1}{2}p^{\mathsf T}M^{-1}(q)p
+\frac{1}{2}\sigma_0\phi(u_P)\lVert z\rVert^2
+U(q).
\]

Here \(\chi\in\mathbb{R}^{3n}\) is the total state; \(\mathcal J\) is the skew-symmetric power-conserving interconnection matrix; \(\mathcal R\) is the positive-semidefinite dissipation matrix; \(\mathcal G\) is the input map; \(u_\chi=\operatorname{col}(u,u_P)\) combines tendon inputs and the pressure input; \(\mathcal H\) is total modeled energy [J]; and all remaining symbols are defined above. **[VERIFIED FULL TEXT — Fan 2026, Eqs. (12)–(14), printed pp. 2223–2224 / PDF pp. 5–6]**

The energy architecture says: inertia stores kinetic energy, gravity and robot elasticity store configuration energy, the virtual bristles store friction-associated energy, and the \(\mathcal R\) terms dissipate energy. It does not calculate elastic energy or frictional work for each sheet and interface. **[VERIFIED FULL TEXT + INFERENCE]**

## 5. How pressure, friction, slip, and layer count enter

### 5.1 Vacuum pressure

Fan assumes uniform pressure \(-u_P\) along the jamming layer and says the lumped normal force is proportional to an unknown positive function \(\phi(u_P)\). The function is required to be nonnegative and monotonically increasing, then identified from data/mechanism-inspired scaling. **[VERIFIED FULL TEXT — Assumptions 3–4, printed p. 2223 / PDF p. 5]**

The paper's causal chain is therefore:

\[
u_P\ \longrightarrow\ \phi(u_P)\ \longrightarrow\
\text{LuGre bristle energy and friction torque}\ \longrightarrow\
\text{shape retention and generalized stiffness}.
\]

Here \(u_P\) is vacuum-pressure magnitude [kPa experimentally], \(\phi(u_P)\) is the fitted pressure scale, the bristle energy is \(H_z\) [J], friction torque is \(\tau_f\) [N·m], and generalized stiffness is \(K\) [N·m/rad in angular coordinates]. This arrow diagram is an **[INFERENCE]** summarizing printed Eqs. (7)–(17); it is not a numbered equation in Fan.

What is absent is equally important: the model does not solve a contact-pressure field, membrane loading, deformation-induced normal stress, or interface-specific normal force. **[VERIFIED FULL TEXT + INFERENCE]**

### 5.2 Interlayer slip

Fan explicitly motivates LuGre by its ability to capture zero-slip displacement, micromotion, stick–slip motion, state boundedness, and passivity. **[VERIFIED FULL TEXT — Sect. II-B, printed p. 2223 / PDF p. 5]**

But the state \(z_i\) is defined at virtual joint \(i\), and the relative velocity input is the generalized joint velocity \(v_i\). The paper does not give a mapping from \(z_i\) to the relative displacement of interface \(j\), nor from \(\tau_{f,i}\) to a through-thickness shear-traction distribution. It therefore represents the *aggregate dynamic effect* of interlayer friction/slip, not individual or distributed physical slip. **[VERIFIED FULL TEXT + INFERENCE]**

| Mechanical regime | What Fan represents | What it does not establish |
|---|---|---|
| Pre-slip | LuGre virtual-bristle deflection can store energy during zero-slip micromotion. **[VERIFIED FULL TEXT]** | No interface-level pre-slip displacement or traction validation. **[VERIFIED FULL TEXT]** |
| Stick–slip / transition | The speed-dependent LuGre law supports lumped stick–slip behavior. **[VERIFIED FULL TEXT]** | No sequential interface release, yielded-band position, or measured slip-front progression. **[VERIFIED FULL TEXT]** |
| Full slip | The Coulomb asymptote \(\mu_C\) exists in the lumped law. **[VERIFIED FULL TEXT]** | No structural full-slip threshold or experiment organized by a full-slip state. **[VERIFIED FULL TEXT]** |

Thus the existence of a LuGre state must not be reported as validation of discrete interlayer mechanics. **[INFERENCE]**

### 5.3 Physical layer count

Fan introduces \(k_n\) as the number of layers and cites a prior stiffness contrast scaling by \(k_n^2\), but \(k_n\) does not appear as an independent variable in the proposed dynamics, friction equations, controller, or stiffness formula. Its effects are absorbed into the fitted functions \(\alpha_2(u_P)\) and \(\phi(u_P)\) for the installed sheath. **[VERIFIED FULL TEXT — Nomenclature, Remark 1, Eqs. (1)–(17), printed pp. 2219 and 2222–2225 / PDF pp. 1 and 4–7; absorption statement is INFERENCE]**

The five-layer sheath is used for a high-pressure shape-locking demonstration; the two-layer sheath is used for model identification and closed-loop stiffness/configuration work to avoid unintentional locking. Because layer count and task/pressure range change together, these experiments cannot identify an independent layer-count effect. **[VERIFIED FULL TEXT — Sect. V-A, printed p. 2228 / PDF p. 10; causal identifiability assessment is INFERENCE]**

## 6. Shape locking and tunable stiffness

### 6.1 Shape-locking mechanism

Fan defines shape locking as forward invariance of a fixed configuration with zero momentum after vacuum is applied and actuation is removed. Proposition 1 gives the equilibrium manifold:

**Printed Fan Proposition 1:**

\[
\mathcal M=left\{(q,p,z)\in\mathbb R^{3n}:
p=0,\ \nabla U(q)=\sigma_0\phi(u_P)z\right\},
\qquad
z_a=\frac{\nabla U(q_a)}{\sigma_0\phi(u_P)}.
\]

Here \(\mathcal M\) is the equilibrium manifold; \(q_a\) is an arbitrary candidate locked configuration [rad]; \(p=0\) is zero generalized momentum; \(z_a\) is the virtual bristle state required at that equilibrium; \(\nabla U(q_a)\) is the elastic-plus-gravitational generalized torque [N·m]; \(\sigma_0\phi(u_P)z_a\) is the balancing lumped friction torque [N·m]; and \(u_P>0\) is pressure magnitude. **[VERIFIED FULL TEXT — Proposition 1 and Remark 4, printed p. 2224 / PDF p. 6]**

The proposition states local asymptotic stability of \(\mathcal M\). Larger \(u_P\) reduces the required \(z_a\) and can place the released state nearer the manifold's local domain of attraction. It does **not** calculate a critical locking pressure for a physical stack, guarantee global locking from every initial condition, or relate locking to a discrete slip-front state. **[VERIFIED FULL TEXT + INFERENCE]**

### 6.2 Open-loop stiffness

For a small generalized displacement around the open-loop equilibrium, Fan obtains:

**Printed Fan Eq. (17):**

\[
K=\alpha_1\mathbf 1_{n\times n}
+[\alpha_2+\sigma_0\phi(u_P)]I_n.
\]

Here \(K\) is the generalized angular-stiffness matrix [N·m/rad]; \(\alpha_1\) is the gravitational-potential coefficient; \(\mathbf 1_{n\times n}\) is the all-ones matrix; \(\alpha_2=\alpha_2(u_P)\) is the pressure-dependent elastic coefficient; \(\sigma_0\phi(u_P)\) is the pressure-scaled bristle-stiffness contribution; and \(I_n\) is the identity matrix. **[VERIFIED FULL TEXT — Fan 2026, Proposition 2, Eq. (17), printed pp. 2224–2225 / PDF pp. 6–7]**

This is a *local tangent stiffness of the reduced generalized-coordinate model*. It is not a bending constitutive law through the laminate thickness and does not locate slip transitions. **[INFERENCE]**

The pressure functions are parameterized as:

**Printed Fan Eqs. (47)–(48):**

\[
\alpha_2(u_P)=c_1u_P^2+c_2u_P+c_3,
\qquad
\phi(u_P)=c_4+c_5\sqrt{u_P}.
\]

Here \(u_P\) is pressure magnitude, experimentally entered in kPa; \(\alpha_2\) is elastic angular stiffness; \(\phi\) is the pressure/friction scale; and \(c_1,\ldots,c_5\) are fitted coefficients whose units depend on the pressure convention and the lumped model normalization. The paper identifies \(c_1=-0.0015\), \(c_2=0.0890\), \(c_3=1.7056\), and \(\alpha_1=1.0227\); the stiffness fit gives \(c_4=110.9847\), \(c_5=29.1067\), with \(c_4,c_5\) stated to include \(\sigma_0\). **[VERIFIED FULL TEXT — Fan 2026, Eqs. (47)–(49), Sect. V-D, printed pp. 2227 and 2230 / PDF pp. 9 and 12]**

There is a source-level consistency issue. The text introducing Eq. (47) calls the coefficients positive and the function monotone, but the reported fit has \(c_1<0\); Eq. (49) constrains \(\alpha_1,c_2,c_3>0\), not \(c_1\). With the printed fitted values, the derivative of the quadratic changes sign near 29.7 kPa. This arithmetic observation is **[INFERENCE]** from verified printed coefficients; it is not identified as a breakdown boundary by the authors. It weakens any attempt to extrapolate the fitted function or interpret it as a globally monotone physical law.

## 7. Controller formulation

### 7.1 Assignable configurations and input transformation

For controller design, Fan assumes two tendons, PCC, negligible actuator dynamics, uniform tendon tension, and an input map of the form:

**Printed Fan Eq. (18):**

\[
G(q)=\begin{bmatrix}g(q)\mathbf 1_n&-g(q)\mathbf 1_n\end{bmatrix},
\qquad |g(q)|>0\ \text{uniformly}.
\]

Here \(G(q)\) is the \(n\times2\) input matrix; \(g(q)\) is a continuously differentiable scalar transmission function; \(\mathbf 1_n\) is the \(n\)-vector of ones; and the two columns represent antagonistic tendons. **[VERIFIED FULL TEXT — Assumptions 5–6 and Eq. (18), printed p. 2225 / PDF p. 7]**

Only homogeneous target shapes \(q_\star=\operatorname{col}(\theta_\star,\ldots,\theta_\star)\) are treated as assignable equilibria. Here \(q_\star\) is the desired configuration [rad] and \(\theta_\star\) is the common desired segment angle [rad]. **[VERIFIED FULL TEXT — Eq. (19), printed p. 2225 / PDF p. 7]**

### 7.2 Energy shaping and damping injection

The controller is:

**Printed Fan Eqs. (24)–(25):**

\[
\tau=\tau_{es}(q)+\tau_{da}(q),\qquad u_P=u_P^\star,
\]

\[
\tau_{es}(q)=\frac{1}{g(q)}
\begin{bmatrix}
\alpha_1\sin q_\Sigma-\gamma\sin(q_\Sigma-q_\Sigma^\star)+\alpha_2\theta_\star\\
0
\end{bmatrix},
\qquad
\tau_{da}(q)=-
\begin{bmatrix}
K_DG_\tau^{\mathsf T}(q)\nabla_pH\\0
\end{bmatrix}.
\]

Here \(\tau\in\mathbb R^2\) is the transformed tendon-input vector; \(\tau_{es}\) is the energy-shaping term; \(\tau_{da}\) is damping injection; \(u_P^\star\) is constant commanded pressure [Pa or kPa by implementation]; \(q_\Sigma\) and \(q_\Sigma^\star\) are actual and desired total angles [rad]; \(\theta_\star\) is desired segment angle [rad]; \(\gamma>0\) is the shaped coupling-stiffness gain; \(K_D>0\) is damping gain; \(G_\tau=G(q)T_u^{-1}\) is the transformed input map; \(T_u=\left[\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\right]\) is Fan's dimensionless input transformation; and \(\nabla_pH=M^{-1}p\) is generalized velocity. **[VERIFIED FULL TEXT — Fan 2026, Eqs. (20)–(25), printed p. 2225 / PDF p. 7]**

The desired potential is:

**Printed Fan Eq. (30):**

\[
U_d(q)=-\gamma\cos(q_\Sigma-q_\Sigma^\star)
+\frac{1}{2}\alpha_2\lVert q-q_\star\rVert^2.
\]

Here \(U_d\) is desired potential energy [J]; \(\gamma\) is the energy/stiffness-shaping gain [J under the angular convention]; \(q\) and \(q_\star\) are actual and desired angle vectors [rad]; and \(q_\Sigma,q_\Sigma^\star\) are their summed angles [rad]. This shapes a minimum at the desired homogeneous configuration. **[VERIFIED FULL TEXT — Fan 2026, Eq. (30), printed p. 2226 / PDF p. 8]**

The stated closed-loop stiffness is:

**Printed Fan Eq. (27):**

\[
K=\gamma\mathbf 1_{n\times n}
+[\alpha_2+\sigma_0\phi(u_P^\star)]I_n.
\]

Here \(K\) is closed-loop generalized stiffness [N·m/rad]; \(\gamma\mathbf 1_{n\times n}\) is the controller-shaped coupling term; \(\alpha_2\) is elastic stiffness; \(\sigma_0\phi(u_P^\star)\) is the pressure-controlled LuGre stiffness contribution; and \(I_n\) is identity. **[VERIFIED FULL TEXT — Fan 2026, Eq. (27), printed p. 2225 / PDF p. 7]**

Fan proves global asymptotic stability for the assignable equilibrium under the printed model assumptions and passivity condition. That is a theorem about the model, not proof that the physical robot satisfies the model globally. **[VERIFIED FULL TEXT + INFERENCE]**

There is another printed inconsistency relevant to technical reuse: Eq. (27) uses \(\gamma\) in the all-ones stiffness term, while the final line of printed Eq. (45) shows \(\alpha_1\), even though the preceding Hessian \(\nabla^2U_d(q_\star)\) implied by Eq. (30) yields \(\gamma\). This report does not silently repair the paper; users should check author code or errata before implementing the stiffness proof. **[VERIFIED FULL TEXT — Eqs. (27), (30), (45), printed pp. 2225–2226 / PDF pp. 7–8; inconsistency diagnosis is INFERENCE]**

## 8. Experimental audit

### 8.1 Platform and instrumentation

The OctRobot-I test article is a single-section robot with six model segments, total length 252 mm, and diameter approximately 50 mm. Two DYNAMIXEL XM430-W350 servomotors with custom spools drive antagonistic tendons in current-regulation mode. Vacuum hardware comprises an H40-85 micro-piston pump, SMC IRV10-C08 regulator, nonreturn valve, and Panasonic DP-100 pressure gauge. A distal AprilTag is observed by an MJEG-640×400 camera at 210 frames/s; four detections are averaged per control update. Transverse stiffness is measured using a linear actuator and a JLBS-M2-10 kg force sensor at the end effector. **[VERIFIED FULL TEXT — Fan 2026, Sect. V-A and Fig. 5, printed p. 2228 / PDF p. 10]**

The single distal marker requires the experimental estimate \(q_i=\theta(t)\) for all segments, even though the theoretical controller does not impose equality of all measured segment angles during its derivation. Thus configuration validation observes one uniform-curvature scalar estimate, not six independently measured segment angles. **[VERIFIED FULL TEXT — Sect. V-A, footnote 8, printed p. 2229 / PDF p. 11; implication is INFERENCE]**

### 8.2 Shape-locking experiment

With a five-layer sheath, the robot is bent to a total 60°, vacuum is applied, and tendon tension is released. Residual position changes between the vacuum-held/tendon-driven and vacuum-held/tendon-released states are 9.2 mm at 30 kPa, 6.7 mm at 60 kPa, and 3.8 mm at 80 kPa. **[VERIFIED FULL TEXT — Fan 2026, Sect. V-B and Fig. 6, printed p. 2229 / PDF p. 11]**

This verifies the existence and pressure trend of aggregate shape retention on that setup. It does not validate \(z\), \(\tau_f\), interface slip, the domain of attraction, or a critical pressure. No predicted displacement curve or error metric is compared against those three displacements. **[VERIFIED FULL TEXT + INFERENCE]**

### 8.3 Open-loop stiffness and parameter identification

With a two-layer sheath and pressures in 0–40 kPa, a small end-effector displacement \(\delta_x\) is imposed and force \(f_{ext}\) is measured. The reported transverse stiffness is:

**Printed experimental definition:**

\[
K_T=\frac{f_{ext}}{\delta_x}.
\]

Here \(K_T\) is transverse end-effector stiffness [N/m], \(f_{ext}\) is measured transverse force [N], and \(\delta_x\) is the imposed small displacement [m]. The numerical magnitude of “sufficiently small” \(\delta_x\) is not reported in the inspected text. **[VERIFIED FULL TEXT — Fan 2026, Sect. V-C, Fig. 7, printed p. 2229 / PDF p. 11]**

Three repetitions are performed per pressure. The square-root pressure fit reports \(R_s^2=0.9216\), with fitted relation implied by the identified coefficients:

\[
K_T=110.9847+29.1067\sqrt{u_P}.
\]

Here \(K_T\) is in N/m and \(u_P\) is numerically entered in kPa; consequently the intercept is N/m and the square-root coefficient has units N·m\(^{-1}\)·kPa\(^{-1/2}\). The paper reports the coefficient values through \(c_4,c_5\) and notes that they include \(\sigma_0\); writing them as the displayed \(K_T\) fit is an **[INFERENCE]** from the printed identification and Fig. 7, not a separately numbered Fan equation. **[VERIFIED FULL TEXT — Sect. V-C–V-D, printed pp. 2229–2230 / PDF pp. 11–12]**

The same experimental data are used to select the function and identify its coefficients. Therefore \(R_s^2\) is an in-sample goodness-of-fit measure, not independent predictive validation. The paper gives no held-out error, residual distribution, confidence interval, or pressure extrapolation test. **[VERIFIED FULL TEXT + INFERENCE]**

For \(\alpha_1\) and \(\alpha_2\), Fan uses 15 configurations at each of five pressure values, repeats each three times, and reports 225 operating modes. The parameters are identified from static equilibrium data. Again, this calibrates aggregate robot-level coefficients; it does not identify physical interface parameters. **[VERIFIED FULL TEXT — Sect. V-D, Fig. 8, printed p. 2230 / PDF p. 12; last distinction is INFERENCE]**

### 8.4 Closed-loop configuration and stiffness

The control tests use a two-layer sheath, target segment angles 5°, 10°, and 15°, pressure values 0, 10, 20, 30, and 40 kPa, and gains \(\gamma=0.1\), \(K_D=1\). Table I reports steady-state MAE values from 0.0152° to 0.7826°, and transients last less than 15 s. **[VERIFIED FULL TEXT — Fan 2026, Sect. V-E, Table I, printed pp. 2230–2231 / PDF pp. 12–13]**

The column headed RMS contains values close to the requested angle itself rather than an RMS error about zero, although the surrounding wording calls the table's quantities errors. This report therefore does not reinterpret that column as a prediction-error statistic. **[VERIFIED FULL TEXT for Table I; INFERENCE for the caution]**

For stiffness regulation, the paper varies \(\gamma\) and pressure at desired angles 8° and 10°. It reports that \(\gamma\)'s maximum relative stiffness contribution is 8.73% and \(\alpha_2\)'s is 3.55%, with both contributions decreasing relative to the pressure term as pressure increases. **[VERIFIED FULL TEXT — Fig. 10 and Table II, printed p. 2231 / PDF p. 13]**

No numerical error between Eq. (27)'s full matrix prediction and measured stiffness is reported, and the full generalized stiffness matrix is not directly measured. The experiment measures one transverse end-effector stiffness. **[VERIFIED FULL TEXT — Sects. V-C and V-E; INFERENCE for the validation scope]**

## 9. What is validated—and what is not

| Quantity or claim | Validation status | Adversarial reading |
|---|---|---|
| Pressure helps retain a bent shape after tendon release | **[VERIFIED FULL TEXT]** | Demonstrated at 30, 60, 80 kPa with five layers; no predicted-vs-measured drift error. |
| Pressure increases transverse stiffness | **[VERIFIED FULL TEXT]** | Demonstrated with two layers over 0–40 kPa; fit is in-sample. |
| Square-root pressure parameterization | **[VERIFIED FULL TEXT]** | \(R_s^2=0.9216\) on the calibration data; not a universal law or held-out validation. |
| Static force–angle relation used for \(\alpha_2\) | **[VERIFIED FULL TEXT]** | Identified over 0–40 kPa; coefficients are setup-specific and internally challenge the monotonicity wording. |
| Homogeneous setpoint regulation | **[VERIFIED FULL TEXT]** | MAE reported on one planar single-section robot; not trajectory tracking or arbitrary shape control. |
| Closed-loop stability proof | **[VERIFIED FULL TEXT]** | Correctness is conditional on the model, PCC/input-map assumptions, coefficient constraints, and constant pressure. |
| LuGre internal state \(z\) as physical interface slip | **Not validated — [VERIFIED FULL TEXT]** | No interface-resolved measurement or mapping. |
| Lumped friction torque versus discrete-interface model | **Not tested — [VERIFIED FULL TEXT]** | No Caruso-type analytical comparison or discrete-contact FEA. |
| Layer-count scaling | **Not tested systematically — [VERIFIED FULL TEXT]** | Two and five layers serve different experiments; authors reserve configuration/scalability study for future work. |
| PCC validity | **Not mapped — [VERIFIED FULL TEXT]** | Cosserat extension is proposed for length/multisection behavior beyond PCC validity. |
| Breakdown boundary of reduced LJ mechanics | **Not identified — [INFERENCE]** | No predeclared error tolerance, parameter grid, or failure surface. |

## 10. Validity-domain and breakdown-boundary audit

A quantitative validity-domain map would require, at minimum, a declared reference model or experiment, independently varied parameters, selected outputs, an error metric, a tolerance defining acceptability, and interpolation or bracketing of the boundary where the tolerance is exceeded. A quantitative breakdown boundary is the locus of those failures, not merely a limitation sentence or a device ceasing to perform a control task. **[INFERENCE — audit criterion]**

Fan supplies several *range statements* but not that map:

| Candidate axis or failure mode | What Fan covers | Classification |
|---|---|---|
| Physical layer count \(k_n\) | Two layers for stiffness/control; five for shape locking; no matched sweep | **UNMAPPED — [VERIFIED FULL TEXT]** |
| Vacuum pressure | 0–40 kPa for identification/control; 30–80 kPa for five-layer shape retention | **PARTIALLY SAMPLED, not a validity boundary — [VERIFIED FULL TEXT]** |
| Curvature/configuration | Homogeneous segment targets and a 60° total-bend shape-lock test; no mechanics error versus curvature | **UNMAPPED — [VERIFIED FULL TEXT]** |
| External load | Small transverse deflection for stiffness; magnitude not reported; no load sweep through slip regimes | **UNMAPPED — [VERIFIED FULL TEXT]** |
| Pre-slip / progressive / full slip | LuGre can represent lumped friction regimes, but experiments are not classified or measured by interface-slip regime | **UNMAPPED — [VERIFIED FULL TEXT + INFERENCE]** |
| Dynamic frequency/rate | Setpoint transients are shown; no frequency response or rate-domain model-error map | **UNMAPPED — [VERIFIED FULL TEXT]** |
| Hysteresis/cyclic loading | LuGre is hysteretic in principle; no cyclic mechanics validation is reported | **UNMAPPED — [VERIFIED FULL TEXT + INFERENCE]** |
| PCC failure | Authors identify very long/multisection structures as motivation for a Cosserat extension, but give no numerical threshold | **QUALITATIVE LIMIT — [VERIFIED FULL TEXT]** |
| Shape-lock/control trade-off | High pressure or more layers may unintentionally lock the shape; two layers and at most 40 kPa are chosen for control | **QUALITATIVE OPERATIONAL LIMIT — [VERIFIED FULL TEXT]** |
| \(\alpha_2\) calibration | Authors explicitly limit identification to 0–40 kPa | **CALIBRATION RANGE, not a mechanics-validity domain — [VERIFIED FULL TEXT]** |

The paper therefore identifies *where its experiments and fit were conducted* and *some reasons its controller/model may cease to be convenient*. It does not quantify where the reduced LJ representation becomes inaccurate relative to discrete mechanics or independent experimental mechanics. **[INFERENCE]**

## 11. Direct comparison with the closest verified models

### 11.1 Model-level comparison

| Dimension | Narang et al. 2018 | Caruso et al. 2023 | Zhang beam model | Zhang RVE/average-field model | Fan et al. 2026 |
|---|---|---|---|---|---|
| Primary purpose | Explain laminar-jamming mechanics and regimes; design scaling | Predict multilayer bending and sequential slip analytically | Replace many thin layers by a through-height continuum-limit beam model | Derive a continuum elastoplastic constitutive law using average-field/RVE reasoning | Dynamic model and feedback control of an LJ continuum robot |
| Mechanical representation | Two-layer analytical mechanics; explicit multilayer frictional-contact FEA | Explicit layer/interface-indexed analytical model | Continuous axial/shear stress fields with moving jammed/sliding boundary | Micro-to-macro average-field constitutive response from a two-layer RVE | Finite-dimensional PCC rigid-link robot plus lumped LuGre friction |
| Interface treatment | Physical Coulomb contacts; individual contacts in FEA | Named interfaces and sequential symmetric slip events | Interfaces disappear in continuum limit; slip becomes a yielded band | Discrete RVE interactions are averaged into an effective elastoplastic material law | No physical interface index; one virtual bristle state per robot coordinate |
| Slip regimes | Pre-slip, transition, full slip | Pre-slip, progressive interface release, full slip and hysteresis | Full jamming, partial (“half-slipping”), full slipping | Jamming/yield/slipping at constitutive material-point scale | Zero-slip micromotion, stick–slip and Coulomb behavior phenomenologically through LuGre |
| Pressure | Sets contact/friction capacity in mechanics/FEA | Explicit in transition forces; pre-slip stiffness pressure-independent | Uniform Coulomb cap \(\mu p\); pressure changes slip thresholds | Normal/shear loading enters RVE/yield law | Uniform imposed pressure enters fitted \(\alpha_2(u_P)\) and \(\phi(u_P)\) |
| Layer count | Explicit in multilayer FEA/experiments | Explicit \(N\) in critical transitions/stiffness | Mostly replaced by total height in thin-layer limit; sheet thickness remains at full-slip limit | Intended scalable continuum law; no structural layer-count validation map | Absent from dynamics/stiffness equations; fixed sheaths used |
| Validation reference | Analytical/FEA/beam experiments | Three-point-bending experiments at multiple \(N,p\) | Discrete layered FEA and one beam experiment | Periodic discrete RVE FEA; no physical experiment | Aggregate robot experiments; no discrete layer model |
| Control/dynamics | Not Fan-style closed-loop control | Quasi-static mechanics | Quasi-static beam mechanics | Constitutive mechanics | Central contribution: dynamic model, passivity proof, controller |

Every factual comparison cell is **[VERIFIED FULL TEXT]** from the five repository PDFs. The categorization of Fan as phenomenological/reduced is **[INFERENCE]** from its state architecture.

### 11.2 Narang 2018 versus Fan 2026

Narang identifies pre-slip, progressive transition, and full-slip behavior from physical interlayer friction. Its two-layer analytical solution and explicit multilayer FEA preserve contact mechanics; experiments examine stiffness and damping changes. It also reports that explicit FEA cost grows with layer count. **[VERIFIED FULL TEXT — Narang 2018, Sects. 2–3, PDF pp. 3–7]**

Fan does not replace or validate that interface mechanics. It imports their aggregate consequence into a dynamic robot model through \(\alpha_2(u_P)\), \(\phi(u_P)\), and LuGre torque. What Fan adds is dynamic energy structure, shape-lock equilibrium analysis, and feedback control—not a more resolved laminar mechanics solution. **[VERIFIED FULL TEXT + INFERENCE]**

### 11.3 Caruso 2023 versus Fan 2026

Caruso's analytical model retains layer count and interface order. Under three-point bending, the central interface slips first and further interface pairs release progressively; the model predicts piecewise stiffness, transition loads, hysteresis, and support-overhang effects and is tested at 8, 12, 16, and 20 layers and 24, 48, and 68 kPa. **[VERIFIED FULL TEXT — Caruso 2023, Sects. 2–5, PDF pp. 3–8]**

Fan retains none of the interface-indexed state. Its \(z_i\) corresponds to robot segment \(i\), not Caruso interface \(i\). Consequently, Fan cannot directly predict which interface slips, how a slip front crosses the thickness, or how its lumped parameters should change when \(N\) changes. It also does not compare its torque/stiffness predictions with Caruso's. **[VERIFIED FULL TEXT + INFERENCE]**

### 11.4 Zhang 2025 beam continuum model versus Fan 2026

Zhang's beam model takes a thin-layer/high-layer-count limit, replaces discrete interfaces with continuous through-height normal and shear stress fields, and represents progressive slip by a moving boundary between a central yielded region and outer jammed regions. It compares stress profiles with explicit 10- and 25-layer FEA and compares cantilever force–deflection with one 20-layer, 60 kPa experiment. The reported discrepancies are concentrated near boundaries, under transverse-normal-stress effects, and in extreme/full-slip loading. **[VERIFIED FULL TEXT — Zhang beam 2025, Sects. 2–6, Figs. 3, 6–7, printed pp. 822–829 / PDF pp. 2–9]**

Fan's coordinates describe robot centerline configuration and lumped friction, not through-height fields. It neither uses Zhang's slip-boundary variable nor checks whether its fitted stiffness/friction terms reproduce Zhang's mechanics. Fan therefore does not validate, supersede, or map the validity of Zhang's beam continuum approximation. **[INFERENCE grounded in both full texts]**

### 11.5 Zhang average-field/RVE continuum model versus Fan 2026

The second Zhang paper explicitly constructs an elastoplastic continuum constitutive model using an average-field technique and a two-layer representative volume element. It derives a Coulomb-type yield surface and dissipated-energy density and validates selected uniaxial shear, multidirectional shear, and coupled shear-normal cases against periodic RVE finite-element calculations. The paper reports, among its selected checks, theoretical shear stiffness 1.0714 GPa versus FEA 0.888 GPa, yield radius 0.060 MPa versus 0.0612 MPa, and residual shear strain 0.144‰ versus 0.132‰. It does not report physical experiments or a structural layer-count/beam-boundary validity map. **[VERIFIED FULL TEXT — Zhang RVE/average-field paper, Abstract; Sect. 4.1–4.3, Figs. 6–8, PDF pp. 1 and 6–8]**

That Zhang model is scientifically much closer to *homogenization/effective constitutive modeling* than Fan's: it defines a microstructural averaging step and compares the macro law with a discrete periodic cell. Fan instead postulates robot-level energy and friction forms and identifies their aggregate coefficients experimentally. Fan should therefore not be cited as though it independently homogenizes discrete layers. **[INFERENCE]**

## 12. Does Fan identify model failure?

### Author-stated limitations **[VERIFIED FULL TEXT]**

- single-section planar bending and two-tendon specialization;
- rigid-link and PCC approximations;
- actuator dynamics and transmission friction neglected, with observed transient plateaus;
- single-marker uniform-curvature estimation and motion-blur artifacts;
- \(\alpha_2\) identification limited to 0–40 kPa;
- more layers or excessive pressure can cause unwanted shape locking and impede dynamic configuration control;
- setpoint regulation rather than trajectory tracking;
- different layer configurations, scalability, and distributed Cosserat extension left for future work.

**[VERIFIED FULL TEXT — Fan 2026, Sects. V-A, V-E, VI, printed pp. 2228, 2230–2232 / PDF pp. 10 and 12–14]**

### What these limitations do not amount to **[INFERENCE]**

They do not define an accuracy boundary of the LJ mechanics model. For example, “above some pressure the robot locks and control fails” is an operational observation. A mechanics breakdown boundary would require a defined error—such as stiffness, moment–curvature, dissipation, interface-slip, or transition-load error—measured against explicit-interface mechanics or independent experiments and bracketed as pressure/layer count/load varies. Fan does not perform that exercise.

## 13. Adversarial falsification verdict

### 13.1 Does Fan 2026 kill the surviving D1-V003 research gap?

**No. [INFERENCE]** Fan does not establish the quantitative validity domain or breakdown boundaries of a continuum/reduced LJ mechanics representation relative to discrete interlayer mechanics or experiments. Its experiment validates task-level behavior of one reduced control model on one robot, not discrete-to-reduced equivalence.

### 13.2 Does it narrow the gap?

**Yes. [INFERENCE]** Fan removes or sharply weakens any proposed claim that:

- no dynamic reduced model of an LJ continuum robot exists;
- pressure has not been incorporated as a control input in an energy-based model;
- LJ shape locking has not been formulated as an equilibrium/stability property;
- a pressure-dependent lumped stiffness/friction representation has not been fitted experimentally;
- simultaneous configuration and stiffness regulation has not been demonstrated with a stability argument.

Any future project must avoid rebranding those contributions as new. It must operate at the mechanics-validity level or another demonstrably distinct level.

### 13.3 Is Fan orthogonal or mainly control-oriented?

**Mainly control-oriented, with partial overlap. [INFERENCE]** It overlaps the surviving question because it is another reduced representation of LJ behavior and exposes qualitative limitations of PCC and pressure/layer operating range. It is orthogonal to the central discrete-to-continuum validation task because it does not resolve interfaces, derive a micro-to-macro law, or compare reduced predictions to discrete mechanics.

### 13.4 Narrowest defensible question after Fan

> **For a fixed planar vacuum-jammed beam geometry and material system, over what combinations of physical layer count (or layer-thickness ratio), vacuum pressure, and nondimensional bending load/curvature does a specified mechanics-level continuum representation remain within a predeclared error tolerance relative to explicit-interface mechanics and independent experiment, and which omitted mechanism first causes that tolerance to be exceeded as the system passes from pre-slip through progressive slip toward full slip?** **[INFERENCE]**

To be genuinely narrower than Fan, this question must:

1. use physical layer count, not PCC segment count;
2. select a mechanics-level continuum reference explicitly—such as the Zhang beam model or a structural reduction of the Zhang RVE constitutive law;
3. compare against an explicit-interface reference and independent experiment;
4. predeclare outputs and tolerances, for example transition load, force–deflection, dissipated energy, and slip-front/interface-state error;
5. separate calibration cases from validation cases; and
6. report failure mechanisms, not merely a global fit score.

This remains a defensible *verification question in the currently inspected full-text corpus*, not a confirmed novel research gap. Further closest-literature checking can still kill or narrow it. **[INFERENCE]**

## 14. What is already answered versus still unresolved

### Already answered in the verified corpus

- Physical laminar jamming has pre-slip, progressive-slip, and full-slip regimes and can be modeled with explicit frictional contacts. **[VERIFIED FULL TEXT — Narang 2018]**
- Sequential interface slip and pressure/layer-count-dependent piecewise stiffness can be modeled analytically and checked experimentally for a particular three-point-bending system. **[VERIFIED FULL TEXT — Caruso 2023]**
- A high-layer-count beam can be represented by continuous through-height stress fields and a moving slip boundary, with selected FEA and experimental comparisons. **[VERIFIED FULL TEXT — Zhang beam 2025]**
- An average-field/RVE elastoplastic continuum constitutive model can be derived and compared with periodic discrete-cell FEA under selected load paths. **[VERIFIED FULL TEXT — Zhang RVE/average-field paper]**
- A reduced dynamic LJ continuum-robot model can combine PCC rigid-link dynamics, LuGre friction, pressure-dependent stiffness, and passivity-based position/stiffness control. **[VERIFIED FULL TEXT — Fan 2026]**

### Still unresolved in these verified papers

- a common, quantitative discrete-to-continuum error measure across physical layer count;
- a factorial or nondimensional validity map over layer count, pressure, load/curvature, and slip regime;
- a tolerance-defined boundary where a specified continuum mechanics representation ceases to be acceptable;
- a measured correspondence among Caruso's released interfaces, Zhang beam's yielded-band boundary, Zhang RVE's constitutive yielding, and Fan's LuGre state;
- independent cyclic/hysteresis validation of the continuum representations;
- separation of boundary/contact, transverse-normal-stress, large-curvature, and rate/hysteresis mechanisms as causes of model failure.

Each item is **[INFERENCE bounded to the five inspected verified full texts]**, not a global novelty claim.

## 15. Evidence and provenance audit

| Major audit claim | Status | Primary provenance |
|---|---|---|
| Fan uses a planar PCC rigid-link dynamic model | **[VERIFIED FULL TEXT]** | Fan 2026, Sect. II-A, Fig. 2, Eqs. (1)–(4), printed pp. 2221–2222 / PDF pp. 3–4 |
| LJ friction is a lumped LuGre model at virtual joints | **[VERIFIED FULL TEXT]** | Fan 2026, Sect. II-B, Eqs. (5)–(11), printed pp. 2222–2223 / PDF pp. 4–5 |
| Pressure enters through \(\alpha_2(u_P)\) and \(\phi(u_P)\) | **[VERIFIED FULL TEXT]** | Fan 2026, Assumptions 1–4; Eqs. (8)–(17), (47)–(48), printed pp. 2222–2227 / PDF pp. 4–9 |
| Fan proves equilibrium/stiffness/control properties under assumptions | **[VERIFIED FULL TEXT]** | Fan 2026, Propositions 1–3, Eqs. (17), (24)–(45), printed pp. 2224–2226 / PDF pp. 6–8 |
| Shape-lock displacements are 9.2, 6.7, 3.8 mm at 30, 60, 80 kPa | **[VERIFIED FULL TEXT]** | Fan 2026, Sect. V-B, Fig. 6, printed p. 2229 / PDF p. 11 |
| Open-loop stiffness fit has \(R_s^2=0.9216\) over the tested two-layer data | **[VERIFIED FULL TEXT]** | Fan 2026, Sect. V-C, Fig. 7, printed p. 2229 / PDF p. 11 |
| Control MAE range is 0.0152°–0.7826° | **[VERIFIED FULL TEXT]** | Fan 2026, Table I, printed p. 2230 / PDF p. 12 |
| Fan contains no discrete-interface validation or systematic validity map | **[VERIFIED FULL TEXT + INFERENCE]** | Fan 2026, complete model and experiment sections; absence assessed against explicitly reported methods/results |
| Fan is a reduced phenomenological LJ representation, not layer homogenization | **[INFERENCE]** | Fan's finite state \(\chi=(q,p,z)\), lumped torque, empirical coefficients, and absence of a micro-to-macro averaging derivation |
| The surviving narrow question is not killed but is narrowed | **[INFERENCE]** | Cross-paper comparison of the five verified full texts |

No **[METADATA ONLY]** source supports any technical claim in this report.

### Repository source provenance

- Fan evidence: `data/evidence/2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming_1f05cf83bc.json`; source PDF SHA256 `1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a`; D1-V003.
- Narang evidence: `data/evidence/2018-Mechanically Versatile Soft Machines through Laminar_5f7ccd7357.json`; source PDF SHA256 `5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5`; D1-V001.
- Caruso evidence: `data/evidence/2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation_652e62758f.json`; source PDF SHA256 `652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee`; D1-V001.
- Zhang beam evidence: `data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json`; source PDF SHA256 `95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd`; D1-V002.
- Zhang RVE/average-field evidence: `data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json`; source PDF SHA256 `a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a`; D1-V002.

## 16. References

1. Fan, Y.; Yi, B.; Liu, D. (2026). “Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots.” *IEEE Transactions on Control Systems Technology*, 34(5). DOI: `10.1109/TCST.2026.3690756`. **[VERIFIED FULL TEXT]**
2. Narang, Y. S.; Vlassak, J. J.; Howe, R. D. (2018). “Mechanically Versatile Soft Machines through Laminar Jamming.” *Advanced Functional Materials*, 28, 1707136. DOI: `10.1002/adfm.201707136`. **[VERIFIED FULL TEXT]**
3. Caruso, F.; Mantriota, G.; Moramarco, V.; Reina, G. (2023). “Layer jamming: Modeling and experimental validation.” *International Journal of Mechanical Sciences*, 251, 108325. DOI: `10.1016/j.ijmecsci.2023.108325`. **[VERIFIED FULL TEXT]**
4. Zhang, S.; Yao, J.; Zhao, W.; Wei, C. (2025). “A continuum-based model for a layer jamming beam.” *Mechanical Sciences*, 16, 821–830. DOI: `10.5194/ms-16-821-2025`. **[VERIFIED FULL TEXT]**
5. Zhang, S.; Yao, J.; Li, S.; Chen, X. (available online 2025; issue 2026). “Continuum modeling for layer jamming structures.” *Theoretical and Applied Mechanics Letters*, 16, 100633. DOI: `10.1016/j.taml.2025.100633`. **[VERIFIED FULL TEXT]**

## Bottom line

Fan 2026 validates a useful robot-level dynamic/control abstraction of layer jamming. It does not validate that abstraction against discrete interlayer mechanics and does not quantify its validity or breakdown boundary. Its strongest adversarial effect is to force the surviving direction away from broad claims about “a continuum model,” pressure-dependent stiffness, shape locking, or stiffness control, and toward a narrowly specified mechanics-level, tolerance-defined discrete-to-continuum validity study. **[INFERENCE]**
