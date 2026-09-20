# Layer Jamming Model Comparison

> **Purpose.** This report reconstructs and teaches the mechanical models in Narang et al. (2018), Caruso et al. (2023), and Zhang et al. (2025), then tests what their combined evidence leaves unresolved. It is an educational comparison and a research-scope analysis, not a novelty adjudication. The provisional direction P1 must still be attacked with additional closest literature.

## Evidence status and scope

- **VERIFIED FULL TEXT** means the claim is supported by a locally held paper whose evidence JSON passed repository validation. The three primary papers all have this status.
- **INFERENCE** means a transparent deduction from verified equations, figures, or reported observations, rather than a conclusion explicitly stated by an author.
- **METADATA ONLY** means bibliographic/search metadata exists but no validated full-text mechanics claim is available. Metadata-only work is not used as scientific evidence here.
- **UNRESOLVED** means the inspected verified text does not establish the answer.

The primary records are:

| Paper | DOI | `paper_id` | Verification round | Full-text status |
|---|---|---|---|---|
| Narang et al. (2018), *Mechanically Versatile Soft Machines through Laminar Jamming* | `10.1002/adfm.201707136` | `5f7ccd7357` | `D1-V001` | **VERIFIED FULL TEXT** |
| Caruso et al. (2023), *Layer jamming: Modeling and experimental validation* | `10.1016/j.ijmecsci.2023.108325` | `652e62758f` | `D1-V001` | **VERIFIED FULL TEXT** |
| Zhang et al. (2025), *A continuum-based model for a layer jamming beam* | `10.5194/ms-16-821-2025` | `95646b2cfc` | `D1-V002` | **VERIFIED FULL TEXT** |

Page references to Narang use its nine-page article pagination/PDF pages. Caruso references use PDF pages, which coincide with the article page numbers shown in the local copy. Zhang references give the journal printed page followed by the PDF page. Exact equations from a source are identified by that source's equation number. Equations introduced only to teach a common idea are labeled **educational derivation**.

One repository-state inconsistency is preserved rather than resolved here: `docs/project/RESEARCH_STATE.md` and `docs/project/research_state.json` still describe Zhang (2025) as awaiting screening, whereas the registry and validated evidence record now identify it as a `D1-V002` verification paper. This report uses the newer validated full-text evidence because that is the explicit task premise; it does not modify either research-state file.

## 1. Physical intuition shared by all three models

### 1.1 The device

A layer- or laminar-jamming beam is a stack of thin flexible sheets inside an airtight membrane. With no vacuum, the sheets can bend and slide almost independently. Applying vacuum creates a pressure difference across the membrane. The membrane compresses the stack, producing normal contact between adjacent sheets. Friction then transfers longitudinal shear between layers.

The elementary Coulomb limit used in all three modeling lines is

\[
|\tau|\le \mu p.
\]

Here \(\tau\) is interfacial or continuum shear stress [Pa], \(\mu\) is the dimensionless coefficient of friction [–], and \(p\) is the imposed vacuum/confining pressure [Pa]. The product \(\mu p\) is a shear-traction capacity [Pa]. Below the limit, neighboring material can stick; at the limit, sliding can occur. **VERIFIED FULL TEXT — Narang 2018, Sect. 2.1, PDF pp. 2–3; Caruso 2023, Sects. 2–2.2, PDF pp. 3–4; Zhang 2025, Sect. 2, printed p. 823 / PDF p. 3.**

This is an idealization. Vacuum pressure creates the normal force that enables friction, but local contact pressure can also be changed by supports and deformation. Caruso and Zhang both identify errors caused by omitting such local pressure redistribution. **VERIFIED FULL TEXT — Caruso 2023, Sect. 5.1–5.2, PDF pp. 5–6; Zhang 2025, Sect. 5, printed p. 828 / PDF p. 8.**

### 1.2 Why sticking makes the beam stiff

Let \(n\) identical sheets each have thickness \(t\) [m] and width \(b\) [m], so total stack thickness is \(H=nt\) [m]. If the sheets slide freely, their bending inertias add:

\[
I_{\mathrm{free}}=n\frac{bt^3}{12}.
\]

Here \(I_{\mathrm{free}}\) is the summed second moment of area of independently bending sheets [m\(^4\)], \(n\) is layer count [–], \(b\) is sheet width [m], and \(t\) is one-sheet thickness [m].

If friction makes the stack act like one bonded rectangle,

\[
I_{\mathrm{jam}}=\frac{b(nt)^3}{12}.
\]

Here \(I_{\mathrm{jam}}\) is the second moment of area of the fully coupled stack [m\(^4\)]; \(b,n,t\) retain the definitions above.

Therefore,

\[
\frac{I_{\mathrm{jam}}}{I_{\mathrm{free}}}=n^2.
\]

Here the ratio is dimensionless and \(n\) is layer count [–]. These three expressions are an **educational geometric derivation** of the \(n^2\) jammed-to-unjammed stiffness scaling reported by Narang and Caruso; they assume identical layers, unchanged Young's modulus, rectangular sections, and ideal fully stuck versus freely sliding limits. **VERIFIED FULL TEXT for the \(n^2\) scaling — Narang 2018, Sect. 2.1, PDF p. 2; Caruso 2023, Sect. 5.5, PDF p. 8.**

### 1.3 What bending does to the interfaces

In bending, material above the neutral axis wants to shorten while material below it wants to lengthen, or vice versa depending on sign. If all sheets must share one curvature, longitudinal shear must be transferred across their interfaces. As the load rises, the required shear eventually reaches \(\mu p\). Sliding then starts where the demand is largest and spreads as load increases.

All three papers use three broad regimes:

1. **Pre-slip / full jamming:** every relevant interface or material region is below the friction limit; stiffness is maximum and the response is elastic in the models.
2. **Transition / partial or progressive slip:** only part of the interface length, only some interfaces, or only part of the cross-sectional continuum has yielded. Stiffness decreases and friction dissipates energy.
3. **Full slip:** all modeled interfaces or nearly all of Zhang's cross-sectional sliding region have reached their limiting state; stiffness is minimum and model error may increase.

The important difference is *what is allowed to progress*:

- Narang's two-layer analytical model tracks the **length of one slipping interface** from the cantilever root toward the free end.
- Caruso's many-layer model tracks **which discrete interfaces** have slipped, from the central interface outward through the thickness.
- Zhang tracks the **half-height of a continuous yielded band**, \(y_s(s)\), through the cross-section and along the beam.

That distinction is the conceptual backbone of the comparison.

## 2. Common beam-mechanics language

All three models use Euler–Bernoulli beam ideas somewhere in their analytical construction. The basic relation is

\[
M=EI\kappa,\qquad \kappa=\frac{d\theta}{dx}.
\]

Here \(M\) is bending moment [N·m], \(E\) is Young's modulus [Pa], \(I\) is second moment of area [m\(^4\)], \(\kappa\) is curvature [m\(^{-1}\)], \(\theta\) is cross-section rotation [rad], and \(x\) is an axial coordinate [m]. This is an **educational statement of Euler–Bernoulli theory**, consistent with the model class reported by all three sources. It assumes plane sections remain plane and transverse shear deformation is negligible.

For a rectangular section carrying shear force \(V\), the classical maximum shear stress is

\[
\tau_{\max}=\frac{3V}{2A}.
\]

Here \(\tau_{\max}\) is maximum transverse shear stress [Pa], \(V\) is section shear force [N], and \(A\) is cross-sectional area [m\(^2\)]. Caruso uses this Jourawski result to obtain discrete slip loads, and Zhang uses the complete parabolic field. **VERIFIED FULL TEXT — Caruso 2023, Eq. (1), PDF p. 3; Zhang 2025, Eq. (3), printed p. 824 / PDF p. 4.**

These beam equations do not determine slip by themselves. They must be combined with a friction rule, interface/continuum kinematics, force equilibrium, boundary conditions, and a decision about how many layer/interface states to retain.

## 3. Narang et al. (2018): two-layer analytical mechanics plus explicit many-layer FEA

### 3.1 Physical system and modeling objective

Narang models vacuum-jammed stacks of thin paper layers. The analytical system is a **two-layer cantilever under a uniform distributed transverse load**. The many-layer systems are represented with explicit 2D frictional-contact finite elements and tested in three-point bending. The paper also integrates jamming structures into a pneumatic bending actuator and a cable-driven segmented soft structure, but those demonstrations are applications of the mechanics rather than a new beam constitutive model. **VERIFIED FULL TEXT — Narang 2018, Sects. 2.1–2.3 and Experimental Section, PDF pp. 2–5 and 7.**

The model seeks to predict:

- beam shape or elastica;
- force–deflection behavior and bending stiffness;
- first and second transition loads;
- the length of the slipped part of the interface;
- dissipated energy and damping;
- how pressure, friction, dimensions, and load affect those quantities.

### 3.2 Inputs, outputs, geometry, and assumptions

| Category | Narang model |
|---|---|
| Analytical inputs | Two-layer geometry; elastic material properties; friction coefficient; vacuum pressure; uniform distributed load; clamped/free boundary conditions |
| Analytical outputs | Elastica, stiffness, transition loads, slipped length, energy dissipation, damping |
| Many-layer numerical inputs | Layer count, pressure, friction coefficient, layer geometry/material, three-point-bending boundary/loading data |
| Many-layer numerical outputs | Force–deflection curves, regime stiffness/damping, interface contact/slip response |
| Analytical geometry/loading | Two-layer cantilever, uniform distributed load |
| Numerical/experimental geometry/loading | Explicit many-layer rectangular stacks in quasi-static three-point bending |
| Material model | Analytical Euler–Bernoulli layers; FEA uses homogeneous 2D plane-strain linear elastic layers with large deformation enabled |
| Contact model | Coulomb friction; FEA uses penalty friction contact at every interface |

The analytical strain field in each layer is described as the superposition of a part varying linearly through thickness and a part constant through thickness, together with an interfacial displacement variable. Moment–stress relations and static equilibrium are written separately for cohesive and slipped sections; continuity joins those regions. **VERIFIED FULL TEXT — Narang 2018, Experimental Section, PDF p. 7.**

The verified local article says the exact governing system, dimensionless forms, and explicit solution are in Supporting Information, but that Supporting Information is not present in the locally validated nine-page PDF. Consequently, this report does **not** reconstruct unverified differential equations or boundary conditions from memory. This is an evidence limitation, not a criticism of the paper.

### 3.3 Governing mechanics that can be verified

The paper explicitly identifies Euler–Bernoulli beam theory, equilibrium, moment–stress relations, interface displacement, Coulomb friction, and region-coupling continuity as the analytical ingredients. The exact numbered field equations cannot be recovered from the verified local main article. One explicit result retained in the article is the full-slip damping force:

\[
F_{\mathrm{damp,full}}=\mu Pbh.
\]

Here \(F_{\mathrm{damp,full}}\) is the full-slip damping force [N], \(\mu\) is the dimensionless interlayer friction coefficient [–], \(P\) is vacuum pressure [Pa], \(b\) is layer width [m], and \(h\) is the layer height dimension used by Narang [m]. The dimensions are \([\mathrm{Pa}][\mathrm{m}^2]=[\mathrm{N}]\). **VERIFIED FULL TEXT — Narang 2018, Sect. 2.1, PDF p. 3.**

For many-layer FEA, the paper reports that full-slip damping scales linearly with layer count, vacuum pressure, and friction coefficient. The main article does not print a single closed-form many-layer equation for that scaling, so none is invented here. **VERIFIED FULL TEXT — Narang 2018, Sect. 2.2, PDF pp. 3–4.**

### 3.4 Derivation and solution logic

The verified derivation logic is:

1. Approximate each layer with Euler–Bernoulli kinematics.
2. Add an interfacial displacement variable so the layers need not remain perfectly bonded.
3. Derive separate equilibrium and moment–stress equations for cohesive and slipped portions.
4. Impose clamped and free boundary conditions.
5. Impose continuity where the interface changes from stuck to sliding.
6. Solve the resulting boundary-value problem explicitly for a two-layer cantilever under uniform distributed load.
7. Recover shape, stiffness, energy, damping, transition loads, and slip length; then nondimensionalize the results.

In the two-layer cantilever, shear demand is greatest near the clamped end, so slip starts there and propagates toward the free end. Figure 2 highlights the increasing slipped length and compares analytical and two-layer FEA results. **VERIFIED FULL TEXT — Narang 2018, Fig. 2 and Sect. 2.1, PDF p. 3.**

Extending the analytical construction to many layers is described as possible but algebraically taxing. Narang therefore uses explicit-interface FEA for practical many-layer predictions. Each layer is a plane-strain body, every interface is a contact surface with penalty friction, pressure equal to vacuum pressure is applied to the outer surfaces, large-deformation analysis is enabled, and each layer has two elements through its thickness. **VERIFIED FULL TEXT — Narang 2018, Sects. 2.1–2.2 and Experimental Section, PDF pp. 3 and 7.**

### 3.5 Treatment of the three slip regimes

- **Pre-slip:** the sheets are cohesive; stiffness is maximum, by a factor \(n^2\) over the freely sliding ideal; energy dissipation and damping are zero in the idealized quasi-static model.
- **Transition:** some interface length is at the friction limit; the slipping part grows, stiffness declines, and friction dissipates energy.
- **Full slip:** the complete available interface length has slipped; stiffness is minimum and damping is maximum.

This regime definition is spatial along the beam for the two-layer analytical example. In many-layer FEA, all interfaces exist explicitly and can slip simultaneously according to their contact state. **VERIFIED FULL TEXT — Narang 2018, Fig. 1 and Sect. 2.1, PDF pp. 2–3.**

### 3.6 Vacuum pressure and layer count

Pressure enters through the friction capacity, so more pressure postpones slip and raises the load that can be carried at high stiffness. Vacuum is bounded by ambient absolute pressure, which the authors identify as a cap on the sustainable load before stiffness declines. **VERIFIED FULL TEXT — Narang 2018, Sects. 2.1 and 3.3, PDF pp. 2–3 and 7.**

Layer count enters explicitly in the geometry and FEA. The ideal stiffness ratio grows as \(n^2\), and full-slip damping scales linearly with \(n\). The authors report that explicit FEA execution time scales linearly with layer count and may become prohibitive for exceptionally many layers. They also warn that achieving homogeneous vacuum pressure may become difficult as layer count grows. **VERIFIED FULL TEXT — Narang 2018, Sects. 2.2, 3.1, and 3.3, PDF pp. 3, 6–7.**

Narang proposes that at fixed total thickness and very high layer count, the stack might be approximated as a single crystal with a single slip system. This is a **VERIFIED FULL-TEXT future/limiting proposal**, not a developed or experimentally validated continuum model. **VERIFIED FULL TEXT — Narang 2018, Sect. 3.3, PDF p. 7.**

### 3.7 Experimental and numerical validation

The many-layer test matrix shown in Figure 3 includes 5, 10, 15, and 20 layers at 71 kPa; a 20-layer case at 0, 24, 47, and 71 kPa; and numerical friction coefficients 0.25, 0.50, and 0.75. The structures were loaded in three-point bending. The Experimental Section reports paper layers, TPU envelopes, and a crosshead rate of 25 mm min\(^{-1}\). **VERIFIED FULL TEXT — Narang 2018, Fig. 3, PDF p. 4; Experimental Section, PDF pp. 7–8.**

Figure 3 reports a maximum experimental deviation of 0.24 N and a minimum coefficient of determination of \(R^2=0.9879\) between many-layer FEA and experiment. No fitting parameters were used. Hysteresis/damping validation is referenced to Supporting Figure S6. **VERIFIED FULL TEXT — Narang 2018, Fig. 3 caption and Sect. 2.2, PDF p. 4.**

The two-layer analytical result is corroborated by two-layer FEA in Figure 2, but the locally verified main text does not supply a numerical analytical-versus-FEA error norm. Therefore “close corroboration” is supported; a specific percentage accuracy for the analytical model is **UNRESOLVED**.

### 3.8 Stated limitations and likely failure conditions

**Author-stated, VERIFIED FULL TEXT:**

- many-layer explicit FEA runtime grows linearly with \(n\);
- exceptionally large \(n\) may make simulation prohibitive;
- homogeneous vacuum distribution becomes physically harder at high \(n\);
- experimental friction could not be controlled precisely;
- vacuum pressure is capped by ambient pressure;
- a vacuum tether was still required in the shape-locking prototype.

**INFERENCE from the verified formulation:** the 2D plane-strain, linear-elastic, quasi-static contact model may lose fidelity under torsion, spatial bending, rate effects, wear, large three-dimensional edge deformation, or material nonlinearity. These conditions were not mapped as failure boundaries in the paper.

### 3.9 What Narang solves—and what it leaves

Narang establishes a mechanics vocabulary that later work must respect: three regimes, pressure/friction-controlled transition, spatial slip propagation, stiffness loss, and frictional damping. It also shows that explicit many-layer FEA can be highly predictive. Its main representational limitation is that the exact analytical solution demonstrated in the verified article is for **two layers**, while practical many-layer behavior is delegated to an interface-explicit numerical model whose cost grows with \(n\).

## 4. Caruso et al. (2023): an explicit-interface analytical model for many layers

### 4.1 Physical system and modeling objective

Caruso studies a rectangular stack with an even number \(n\) of paper layers under vacuum and three-point bending. The span between two supports is \(L\); the specimen also has overhanging portions outside the supports. A central transverse load is applied, so the reaction/shear magnitude in each half-span is half the total applied load. **VERIFIED FULL TEXT — Caruso 2023, Fig. 2 and Sects. 2–3, PDF pp. 3–4.**

The model is designed to predict, analytically and without interface-resolved FEA:

- the load and central deflection at successive slip events;
- the order in which interfaces slip;
- the piecewise reduction in bending stiffness;
- the force–deflection path through pre-slip, partial slip, and full slip;
- frictional hysteresis/energy loss;
- effects of \(n\), \(p\), \(\mu\), and the cohesive overhangs.

This is a **discrete multilayer analytical model**. It avoids a full contact simulation, but it does not erase interface identity: the index \(i\) identifies successive symmetric interfaces.

### 4.2 Inputs, outputs, geometry, and assumptions

| Category | Caruso model |
|---|---|
| Inputs | Even layer count \(n\); one-layer thickness \(h\); width \(b\); support span \(L\); Young's modulus \(E\); Poisson ratio \(\nu\); friction coefficient \(\mu\); pressure \(p\); imposed load or deflection |
| State description | Which central/symmetric interfaces have slipped; cumulative transition load and deflection |
| Outputs | Critical load increments \(F_i\), deflection increments \(w_i\), piecewise force–deflection curve, stiffness segments, hysteresis energy |
| Geometry/loading | Rectangular, even-layer stack in symmetric three-point bending, with overhangs beyond the supports |
| Kinematics | Euler–Bernoulli beam relations within each currently cohesive layer group |
| Material | Linear isotropic elastic paper; plane-strain correction because \(b\gg h\) |
| Friction | Uniform Coulomb threshold \(\tau_{\mathrm{slip}}=\mu p\) |
| Boundary approximation | After first slip, the interface between the loaded span and relatively cohesive overhang is idealized as clamped |

For comparison with the experiment, the paper uses a plane-strain modulus

\[
\bar E=\frac{E}{1-\nu^2}.
\]

Here \(\bar E\) is the effective plane-strain modulus used in the analytical curve [Pa], \(E\) is the measured Young's modulus [Pa], and \(\nu\) is Poisson's ratio [–]. The article subsequently writes \(E\) in its formulas; readers should check whether a calculation uses the material modulus or its plane-strain-adjusted value. **VERIFIED FULL TEXT — Caruso 2023, Sect. 5, PDF p. 5.**

### 4.3 Four-layer derivation: seeing the mechanics before the general formula

Caruso first uses four layers because the slip sequence is visible. In pre-slip all four layers act as one rectangle. At the first event, the central interface slips, leaving two coherent two-layer sub-beams. At the second symmetric event, the two remaining outer interfaces slip, leaving four independent layers. Figure 2 shows these stress redistributions. **VERIFIED FULL TEXT — Caruso 2023, Fig. 2 and Sect. 2.1, PDF p. 3.**

The first half-span shear/reaction increment is obtained with the rectangular-section Jourawski maximum:

\[
F_0=\frac{2\tau_{\mathrm{slip}}A}{3},
\tag{Caruso 1}
\]

where \(F_0\) is the reaction/shear magnitude in one half of the symmetric beam at first slip [N], \(\tau_{\mathrm{slip}}=\mu p\) is the interfacial limit [Pa], and \(A=4bh\) is total four-layer area [m\(^2\)]; \(b\) is width [m] and \(h\) is one-layer thickness [m]. Figure 2 plots the **total central load** as \(2F_0\). The prose directly below Eq. (2) calls \(F_0\) the external applied load, but the diagram and later Sect. 5 use \(2F_0\); this report follows the mechanically consistent figure convention and flags the notation inconsistency. **VERIFIED FULL TEXT — Eq. (1), Fig. 2, PDF p. 3.**

The central deflection at that first event is

\[
w_0=\frac{2F_0L^3}{48EI_{p-s}}.
\tag{Caruso 2}
\]

Here \(w_0\) is midspan deflection [m], \(2F_0\) is total central load [N], \(L\) is the support span [m], \(E\) is the modulus used by the beam model [Pa], and \(I_{p-s}\) is pre-slip second moment of area [m\(^4\)]. This is the simply supported Euler–Bernoulli central-load formula. **VERIFIED FULL TEXT — Eq. (2), PDF p. 3.**

For four fully cohesive layers,

\[
I_{p-s}=\frac{16bh^3}{3}.
\tag{Caruso 3}
\]

Here \(I_{p-s}\) is pre-slip inertia [m\(^4\)], \(b\) is width [m], and \(h\) is one-layer thickness [m]. This equals \(b(4h)^3/12\), the inertia of one four-layer-thick rectangle. **VERIFIED FULL TEXT — Eq. (3), PDF p. 3.**

The additional half-load needed to trigger the remaining symmetric interfaces is

\[
F_1=\frac{F_0}{4}.
\tag{Caruso 4}
\]

Here \(F_1\) is the additional half-span reaction/load increment [N] and \(F_0\) is the first increment [N]. It follows from longitudinal equilibrium of the outer layers after superposing the axial stress caused by \(F_1\) on that caused by \(F_0\). The total central load at the second event is \(2(F_0+F_1)\). **VERIFIED FULL TEXT — Eq. (4) and Fig. 2, PDF p. 3.**

Caruso argues that the loaded internal span slips more than the zero-shear overhangs. It idealizes the transition at each support as clamped after first slip. The additional deflection is then

\[
w_1=\frac{2F_1L^3}{192EI_{pa-s}}.
\tag{Caruso 5}
\]

Here \(w_1\) is the added midspan deflection from the second load increment [m], \(2F_1\) is the added total central load [N], \(L\) is span [m], \(E\) is modulus [Pa], and \(I_{pa-s}\) is the partial-slip inertia [m\(^4\)]. The denominator 192 is the central-load stiffness of a clamped–clamped Euler–Bernoulli beam. **VERIFIED FULL TEXT — Eq. (5), PDF p. 4.**

After the central interface slips, two bonded two-layer groups remain:

\[
I_{pa-s}=\frac{4bh^3}{3}.
\tag{Caruso 6}
\]

Here \(I_{pa-s}\) is the summed inertia of the two two-layer groups [m\(^4\)], while \(b\) [m] and \(h\) [m] retain their definitions. **VERIFIED FULL TEXT — Eq. (6), PDF p. 4.**

With every interface sliding, four independent layers remain:

\[
I_{f-s}=\frac{bh^3}{3}.
\tag{Caruso 7}
\]

Here \(I_{f-s}\) is the summed full-slip inertia [m\(^4\)], \(b\) is width [m], and \(h\) is one-layer thickness [m]. It equals \(4(bh^3/12)\). **VERIFIED FULL TEXT — Eq. (7), PDF p. 4.**

The physical logic is therefore simple even though the general algebra becomes long: each new slip breaks a thick coherent group into thinner groups, reducing \(I\), hence reducing the slope of the force–deflection curve.

### 4.4 General even-\(n\) transition loads

For an arbitrary even number of layers, the first additional half-load is

\[
F_0=\frac{2\mu pbh n}{3}.
\tag{Caruso 8}
\]

Here \(F_0\) is the first half-span load/reaction increment [N], \(\mu\) is friction coefficient [–], \(p\) is pressure [Pa], \(b\) is width [m], \(h\) is one-layer thickness [m], and \(n\) is layer count [–]. The total central load at first slip is \(2F_0\). **VERIFIED FULL TEXT — Eq. (8), PDF p. 4.**

The next increment is

\[
F_1=\frac{\mu pbh n}{3(n-2)}.
\tag{Caruso 9}
\]

Here \(F_1\) is the next half-load increment [N]; \(\mu,p,b,h,n\) have the definitions and units above. **VERIFIED FULL TEXT — Eq. (9), PDF p. 4.**

The third listed increment is

\[
F_2=\frac{2\mu pbh\left(n^2-6n+12\right)}{3\left(n^2-6n+8\right)}.
\tag{Caruso 10}
\]

Here \(F_2\) is the next half-load increment [N]; \(\mu\) [–], \(p\) [Pa], \(b,h\) [m], and \(n\) [–] are as defined above. **VERIFIED FULL TEXT — Eq. (10), PDF p. 4.**

For later symmetric interface pairs,

\[
F_i=
\frac{2\mu pbh\left[n^3-6(i-1)n^2+12(i-1)^2n-8(i^3-3i^2+2i)\right]}
{3\left[n^3-6(i-1)n^2+\left(12(i-1)^2-4\right)n-8(i^3-3i^2+2i)\right]},
\quad i=3,\ldots,\frac n2-1.
\tag{Caruso 11}
\]

Here \(F_i\) is the half-load increment that produces the \(i\)-indexed symmetric slip event [N], \(i\) is a dimensionless event/interface index [–], and \(\mu,p,b,h,n\) retain their prior definitions and units. The cumulative total applied load at a transition is twice the sum of the relevant \(F_j\) increments. The increasing index is the mathematical bookkeeping that Zhang later removes. **VERIFIED FULL TEXT — Eq. (11), PDF p. 4.**

### 4.5 General even-\(n\) transition deflections

The first deflection is

\[
w_0=\frac{\mu pL^3}{3Eh^2n^2}.
\tag{Caruso 12}
\]

Here \(w_0\) is central deflection at first slip [m], \(\mu\) [–], \(p\) [Pa], \(L\) [m], \(E\) [Pa], \(h\) [m], and \(n\) [–] retain their meanings. The dimensions reduce to metres. It shows \(w_0\propto p/n^2\). **VERIFIED FULL TEXT — Eq. (12), PDF p. 4.**

The next added deflection is

\[
w_1=\frac{\mu pL^3}{6Eh^2n^2(n-2)}.
\tag{Caruso 13}
\]

Here \(w_1\) is a deflection increment [m], and \(\mu,p,L,E,h,n\) have the prior definitions and units. This and the following deflection expressions incorporate the clamped-boundary approximation for cohesive overhangs. **VERIFIED FULL TEXT — Eq. (13), PDF p. 4.**

The next increment is

\[
w_2=\frac{\mu pL^3}{6Eh^2n\left(n^2-6n+8\right)}.
\tag{Caruso 14}
\]

Here \(w_2\) is a deflection increment [m], while \(\mu\) [–], \(p\) [Pa], \(L,h\) [m], \(E\) [Pa], and \(n\) [–] retain their definitions. **VERIFIED FULL TEXT — Eq. (14), PDF p. 4.**

For later events,

\[
w_i=
\frac{\mu pL^3}
{3Eh^2\left[n^3-6(i-1)n^2+\left(12(i-1)^2-4\right)n-8(i^3-3i^2+2i)\right]},
\quad i=3,\ldots,\frac n2-1.
\tag{Caruso 15}
\]

Here \(w_i\) is the deflection increment associated with event \(i\) [m], \(i,n\) are dimensionless indices/counts [–], \(\mu\) is friction coefficient [–], \(p\) is pressure [Pa], \(L,h\) are lengths [m], and \(E\) is modulus [Pa]. **VERIFIED FULL TEXT — Eq. (15), PDF p. 4.**

### 4.6 Solution procedure and meaning of the piecewise curve

The analytical procedure is:

1. Use \(\tau_{\mathrm{slip}}=\mu p\) and the pre-slip shear distribution to compute the first transition.
2. Split the stack into coherent sub-beams after the central interface slips.
3. Superpose the additional axial stress caused by the next load increment.
4. Enforce longitudinal equilibrium on the remaining outer layer groups to obtain \(F_i\).
5. Compute the corresponding \(w_i\) with Euler–Bernoulli relations and the current grouped-section inertia.
6. Accumulate the load and deflection increments.
7. Connect consecutive transition points with straight segments, giving a piecewise-linear approximation to the nonlinear force–deflection curve.

The central interface slips first, followed by symmetric pairs moving toward the outer surfaces. Thus partial slip in Caruso is discrete through thickness: at a given stage, some interfaces are sliding and others remain cohesive. This differs from Narang's main two-layer example, in which the progressive coordinate is the slipped **length** of a single interface. **VERIFIED FULL TEXT — Caruso 2023, Figs. 1–2 and Sects. 2.1–2.2, PDF pp. 2–4.**

The overhang is not modeled with a continuously varying slip length in the closed-form equations. Instead, the internal/overhang boundary is treated as perfectly clamped after the first slip. FEA shows real slip does extend into the overhang, but less than in the loaded span. The new 2023 formulation therefore acts as an upper stiffness limit, while the authors' earlier simply supported formulation is the lower limit. **VERIFIED FULL TEXT — Caruso 2023, Sects. 2.1 and 5.4, Figs. 5–6, PDF pp. 3–4 and 7–8.**

### 4.7 Vacuum pressure and layer count

Every transition load/deflection in Eqs. (8)–(15) contains the product \(\mu p\). Raising pressure or friction delays the transitions. Pre-slip bending stiffness does not contain \(p\); pressure determines how long the high-stiffness state can be maintained, not the elastic slope while all layers are stuck. **VERIFIED FULL TEXT — Caruso 2023, Sect. 5.2–5.3, PDF pp. 6–7.**

Layer count remains explicit in every general transition formula. The pre-slip inertia is

\[
I_{p-s}=\frac{bn^3h^3}{12}.
\]

Here \(I_{p-s}\) is pre-slip inertia [m\(^4\)], \(b\) is width [m], \(n\) is layer count [–], and \(h\) is one-layer thickness [m]. **VERIFIED FULL TEXT — Caruso 2023, Sect. 5.1, PDF p. 5.**

The full-slip inertia is

\[
I_{f-s}=\frac{nbh^3}{12}.
\]

Here \(I_{f-s}\) is the summed inertia of independently bending layers [m\(^4\)], and \(n,b,h\) retain their definitions and units. This expression is stated through the paper's \(nh^3\) scaling and is consistent with its four-layer Eq. (7). **VERIFIED FULL TEXT for the scaling and four-layer case; algebraic general form is INFERENCE — Caruso 2023, Sects. 2.2 and 5.1, PDF pp. 4–5.**

The number of transition events is of order \(n/2\) for an even symmetric stack. The closed-form calculation is far cheaper than explicit contact FEA, but its state description still grows with the number of interfaces. The latter complexity statement is **INFERENCE from Eqs. (8)–(15)**; Caruso does not publish a runtime-scaling benchmark for the analytical formulas.

### 4.8 FEA and experiment

The validation specimens use 8, 12, 16, and 20 paper layers; each layer is 0.1 mm thick, 18 cm long, and 6 cm wide. The support span is 10 cm, the roller diameter is 1 cm, and the TPU envelope is 0.009 mm thick. Tests use 68 kPa for the layer-count sweep and 24, 48, and 68 kPa for the 20-layer pressure sweep. Loading and unloading proceed at 5 mm min\(^{-1}\) to 8 mm, data are sampled at 10 Hz, and each condition is repeated three times. The measured material/friction values are \(E=1.7\) GPa and \(\mu=0.55\); \(\nu=0.156\) is adopted from literature. **VERIFIED FULL TEXT — Caruso 2023, Sect. 3, PDF p. 4.**

FEA uses Abaqus/Standard 2017, half-symmetry, explicit rectangular layers, CPE4RH plane-strain elements with side length half a sheet thickness, linear isotropic elasticity, surface-to-surface penalty friction, maximum elastic slip \(5\times10^{-5}\), uniform pressure on outer edges, and geometric nonlinearity. **VERIFIED FULL TEXT — Caruso 2023, Sect. 4, PDF pp. 4–5.**

The comparisons show:

- accurate first-slip transitions and pre-slip stiffness;
- good agreement among analytical, numerical, and experimental force–deflection curves across tested \(n\) and \(p\);
- better post-slip agreement when overhang stiffness is included;
- hysteresis energy increasing with \(n\) and almost linearly with \(p\);
- numerical, but not experimental, confirmation of friction-coefficient trends for \(\mu=0.2,0.3,0.4,0.5\).

These are **VERIFIED FULL TEXT — Caruso 2023, Figs. 4–6 and Sects. 5.1–5.4, PDF pp. 5–8.** The paper reports qualitative “good” or “very good” agreement and no fitting coefficients, but does not provide a global RMSE, \(R^2\), or maximum percentage error. A numerical accuracy percentage is therefore **UNRESOLVED**.

### 4.9 Stated limitations and likely failure conditions

**Author-stated or directly demonstrated, VERIFIED FULL TEXT:**

- high-deflection stiffness is underestimated, especially at larger \(n\) and \(p\), because support-induced contact-pressure increases are omitted;
- the perfectly clamped support boundary is idealized; real slip propagates partly into the overhang;
- \(\mu\) was varied only numerically because it was difficult to control experimentally;
- \(\nu\) was taken from literature rather than measured;
- the validation is for quasi-static 2D three-point bending of rectangular stacks.

**INFERENCE:** accuracy may degrade for nonuniform pressure, spatial bending, torsion, nonrectangular sections, dynamic/rate-dependent friction, wear, wrinkling, or loading paths unlike the tested cycle. These boundaries are not quantified.

### 4.10 What Caruso solves—and what it leaves

Caruso closes much of the gap between Narang's two-layer analytical solution and many-layer explicit FEA: it provides formulas for the sequential interface transitions of an arbitrary even-layer stack and validates them over several \(n\) and \(p\) values. It also corrects a boundary-condition omission by representing cohesive overhangs. What remains is a representation whose transition sequence is still explicitly indexed by interfaces and whose validation is tied to three-point bending, a particular material/geometry family, and idealized contact pressure.

## 5. Zhang et al. (2025): a continuum-limit yielded-band model

### 5.1 Physical system and modeling objective

Zhang considers a many-layer rectangular layer-jamming beam whose single-sheet thickness \(\delta\) is small compared with total height \(h\). The formal construction lets \(\delta\to0\) and \(n\to\infty\) while \(h=n\delta\) remains fixed. The paper states that the approximation is effective for multi-layer structures, typically around \(n\ge10\). **VERIFIED FULL TEXT — Zhang 2025, Sect. 2, printed pp. 822–823 / PDF pp. 2–3.**

The objective is to replace layer-by-layer/interface-by-interface mechanics with continuous fields capable of predicting:

- shear stress \(\tau(y,s)\);
- longitudinal normal stress \(\sigma(y,s)\);
- the boundary \(y_s(s)\) between sliding and jammed material;
- critical section shear forces \(Q_{\mathrm{slip}}\) and \(Q_{\max}\);
- section resultants and cantilever deformation;
- full-jamming, “half-slipping,” and full-slipping states.

Here \(s\) is distance along the beam middle surface [m], and \(y\) is the coordinate through its height [m].

### 5.2 Inputs, state variables, outputs, and assumptions

| Category | Zhang CLJM |
|---|---|
| Inputs | Geometry \(L,b,h,\delta\); modulus \(E\); friction \(\mu\); imposed pressure \(p\); distributed/applied load; reactions/boundary conditions |
| Continuous fields | \(\sigma(y,s)\), \(\tau(y,s)\), normal strain \(\varepsilon_s(y,s)\), shear strain \(\gamma_{sy}(y,s)\), rotation \(\theta(s)\) |
| Internal state | Sliding-zone half-height \(y_s(s)\), plus jammed-region resultants \(N_J,M_J\) and stress slope \(K_J\) |
| Outputs | Stress fields, slip-front location, regime thresholds, rotation and force–deflection response |
| Geometry/loading | Generic planar curved rectangular beam equilibrium; validation uses an end-loaded straight cantilever |
| Material/kinematics | Plane stress; elastic jammed region; ideal-plastic-like sliding; Euler–Bernoulli moment–curvature for jammed part; small deformation per increment |
| Contact/friction | Uniform Coulomb cap \(|\tau|=\mu p\); deformation-induced interlaminar normal pressure is neglected |

The discrete information discarded is the identity of each layer, each physical interface, and each individual relative interface displacement. The continuous information retained is the through-height and axial variation of stress plus a moving yield boundary. Single-layer thickness \(\delta\) does not disappear completely: it defines the full-slip saturation boundary and appears in \(Q_{\max}\).

### 5.3 Constitutive idea before the equations

Zhang treats the layered stack as an elastoplastic-like continuum:

- **elastic/jammed:** \(|\tau|<\mu p\); deformation is reversible in the idealization;
- **yielded/sliding:** \(|\tau|=\mu p\); shear strain can continue changing while shear stress remains capped;
- **unloading:** the sign of the stress increment indicates return from loading, but the paper does not provide a complete hardening, reverse-yield, or re-stick law.

This is not a conventional measured material law \(\tau=G\gamma\). It is a yield condition plus elastic bending of the surviving jammed region. Slip affects stiffness because the jammed portion's second moment of area shrinks as \(y_s\) grows. **VERIFIED FULL TEXT — Zhang 2025, Sects. 2 and 4, printed pp. 823 and 826 / PDF pp. 3 and 6.**

### 5.4 Curved-beam equilibrium: Zhang Eqs. (1)–(2)

The section resultants satisfy

\[
\frac{dN}{ds}=-Q\theta'-q_s=-\frac{Q}{r}-q_s,
\qquad
\frac{dQ}{ds}=N\theta'+q_y=\frac{N}{r}+q_y,
\qquad
\frac{dM}{ds}=Q.
\tag{Zhang 1}
\]

Here \(N\) and \(Q\) are axial and transverse section forces [N], \(M\) is bending moment [N·m], \(s\) is middle-surface arc coordinate [m], \(q_s,q_y\) are distributed load components [N/m], \(\theta\) is section rotation [rad], a prime denotes \(d/ds\), and \(r=ds/d\theta\) is curvature radius [m]. The equation balances an infinitesimal curved segment using first-order trigonometric increments. **VERIFIED FULL TEXT — Zhang 2025, Eq. (1), printed p. 823 / PDF p. 3.**

The first two balances are integrated as

\[
\begin{bmatrix}N\\Q\end{bmatrix}
=
\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}
\left[
\begin{bmatrix}N_0\\Q_0\end{bmatrix}
+\int_{s_0}^{s}
\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}
\begin{bmatrix}-q_s(\xi)\\q_y(\xi)\end{bmatrix}d\xi
\right].
\tag{Zhang 2}
\]

Here \(N,Q,N_0,Q_0\) are forces [N], \(s,s_0,\xi\) are axial/arc coordinates [m], \(q_s,q_y\) are distributed loads [N/m], \(\theta\) is rotation [rad], and \(\xi\) is the dummy integration coordinate. The matrices rotate between local and reference axes. Reactions define \(N_0,Q_0\); integration of \(dM/ds=Q\) then gives \(M\). The paper suppresses some explicit arguments of \(\theta\), so none are invented here. **VERIFIED FULL TEXT — Zhang 2025, Eq. (2), printed p. 823 / PDF p. 3.**

### 5.5 Shear field, regime thresholds, and moving yield boundary: Eqs. (3)–(9)

For a fully jammed rectangular section, Zhang adopts

\[
\tau(y,Q)=\frac{3}{2}\frac{Q}{A}\left(1-\frac{4y^2}{h^2}\right),
\qquad A=bh.
\tag{Zhang 3}
\]

Here \(\tau\) is shear stress [Pa], \(Q\) is section shear force [N], \(A\) is section area [m\(^2\)], \(b\) is width [m], \(h\) is total stack height [m], and \(y\) is through-height position [m]. It is the straight rectangular-beam parabola, used under the assumption \(r\gg h\). Its maximum at \(y=0\) makes yielding start at the cross-sectional center. **VERIFIED FULL TEXT — Zhang 2025, Eq. (3), printed p. 824 / PDF p. 4.**

In partial slip, the outer jammed bands retain a rescaled parabola. Its auxiliary resultant is

\[
Q_{\mathrm{eq}}=\operatorname{sign}(Q)\frac{2}{3}
\frac{\mu pA}{1-4y_s^2/h^2}.
\tag{Zhang 4}
\]

Here \(Q_{\mathrm{eq}}\) is an auxiliary shear force [N], \(Q\) is actual shear force [N], \(\operatorname{sign}(Q)\) is dimensionless, \(\mu\) is friction coefficient [–], \(p\) is pressure [Pa], \(A\) is area [m\(^2\)], and \(y_s,h\) are lengths [m]. Substitution into Eq. (3) makes \(\tau(y_s)=\operatorname{sign}(Q)\mu p\), joining the jammed parabola to the yielded core. **VERIFIED FULL TEXT — Zhang 2025, Eq. (4), printed p. 824 / PDF p. 4.**

Slip begins at

\[
Q_{\mathrm{slip}}=\frac{2}{3}\mu pbh.
\tag{Zhang 5}
\]

Here \(Q_{\mathrm{slip}}\) is section shear force at initial yielding [N], \(\mu\) is friction coefficient [–], \(p\) is pressure [Pa], and \(b,h\) are width and total height [m]. It follows by setting the peak of Eq. (3) equal to \(\mu p\). **VERIFIED FULL TEXT — Zhang 2025, Eq. (5), printed p. 824 / PDF p. 4.**

The paper's full-slip threshold is

\[
Q_{\max}=\mu pb\frac{3h^2-6\delta h+4\delta^2}{3(h-\delta)}.
\tag{Zhang 6}
\]

Here \(Q_{\max}\) is the section shear force marking saturation of the slip boundary [N], \(\mu\) is friction coefficient [–], \(p\) is pressure [Pa], \(b\) is width [m], \(h\) is total height [m], and \(\delta\) is one-layer thickness [m]. It is obtained at \(y_s=h/2-\delta\), demonstrating that \(\delta\) remains in the nominal continuum model. **VERIFIED FULL TEXT — Zhang 2025, Eq. (6), printed p. 824 / PDF p. 4.**

The piecewise shear field is printed as

\[
\tau(y,s)=
\begin{cases}
\dfrac{3}{2}\dfrac{Q}{A}\left(1-\dfrac{4y^2}{h^2}\right),
& |Q|\le Q_{\mathrm{slip}},\\[5pt]
\operatorname{sign}(Q)\mu p,
& |y|\le y_s,\ Q_{\mathrm{slip}}\le|Q|\le Q_{\max},\\[5pt]
\operatorname{sign}(Q)\mu p\dfrac{1-4y^2/h^2}{1-4y_s^2/h^2},
& |y|>y_s,\ Q_{\mathrm{slip}}\le|Q|\le Q_{\max},\\[5pt]
c_2y^2\pm c_1y+c_0,
& |y|>y_s,\ |Q|>Q_{\max}.
\end{cases}
\tag{Zhang 7}
\]

Here \(\tau\) [Pa] depends on \(y,s\) [m]; \(Q,Q_{\mathrm{slip}},Q_{\max}\) are forces [N]; \(A\) is area [m\(^2\)]; \(h,y_s\) are lengths [m]; \(\mu\) [–] and \(p\) [Pa] define the friction cap; and \(c_2,c_1,c_0\) have units Pa/m\(^2\), Pa/m, and Pa. The first branch is fully jammed, the middle pair is the yielded core plus outer jammed bands, and the last is the full-slip outer-band fit. The paper does not explicitly define the \(\pm\) choice in the last line and does not print a central-core branch for \(|Q|>Q_{\max}\). Retaining the Coulomb-capped core is physically implied by the prose but remains **INFERENCE**. **VERIFIED FULL TEXT with source ambiguity — Zhang 2025, Eq. (7), printed p. 824 / PDF p. 4.**

The full-slip outer-band coefficients are

\[
\begin{aligned}
c_2&=-\frac{12(\mu pbh+2\mu pby_s-2Q)}{b(h-2y_s)^3},\\
c_1&=\frac{4(3Qh+6Qy_s-2\mu pbh^2-4\mu pbhy_s-8\mu pby_s^2)}{b(h-2y_s)^3},\\
c_0&=\frac{h(\mu pbh^2+2\mu pbhy_s+16\mu pby_s^2-12Qy_s)}{b(h-2y_s)^3}.
\end{aligned}
\tag{Zhang 8}
\]

Here \(c_2\) [Pa/m\(^2\)], \(c_1\) [Pa/m], and \(c_0\) [Pa] are polynomial coefficients; \(\mu\) [–], \(p\) [Pa], \(b,h,y_s\) [m], and \(Q\) [N] retain their meanings. The coefficients impose zero shear at the free surface, the yield value at \(y_s\), and the section resultant \(Q\). **VERIFIED FULL TEXT — Zhang 2025, Eq. (8), printed p. 824 / PDF p. 4.**

The moving boundary follows

\[
y_s=
\begin{cases}
0, & |Q|<Q_{\mathrm{slip}},\\[3pt]
\dfrac{3Q-2\mu pA+\sqrt{3(3Q-2\mu pA)(Q+2\mu pA)}}{8\mu pb},
& Q_{\mathrm{slip}}\le Q<Q_{\max},\\[7pt]
\dfrac{-3Q+2\mu pA+\sqrt{3(3Q+2\mu pA)(Q-2\mu pA)}}{8\mu pb},
& -Q_{\max}<Q\le-Q_{\mathrm{slip}},\\[7pt]
h/2-\delta, & |Q|\ge Q_{\max}.
\end{cases}
\tag{Zhang 9}
\]

Here \(y_s\) is slip-zone half-height [m], \(Q,Q_{\mathrm{slip}},Q_{\max}\) are forces [N], \(\mu\) is friction coefficient [–], \(p\) is pressure [Pa], \(A=bh\) is area [m\(^2\)], and \(b,h,\delta\) are lengths [m]. Equation (9) converts section load into one of three continuous internal states: no yielded core, progressive growth of the core, or saturation. **VERIFIED FULL TEXT — Zhang 2025, Eq. (9), printed p. 824 / PDF p. 4.**

### 5.6 Longitudinal normal stress: Eqs. (10)–(18)

Zhang represents the normal stress with linear outer jammed branches and an inner sliding-region field:

\[
\sigma(y,s)=
\begin{cases}
N_J/A_J+K_J(y\mp y_s), & |y|>y_s,\\
\sigma_S(y), & |y|<y_s.
\end{cases}
\tag{Zhang 10}
\]

Here \(\sigma\) is longitudinal stress [Pa], \(N_J\) is axial force carried by jammed bands [N], \(A_J=b(h-2y_s)\) is jammed area [m\(^2\)], \(K_J\) is the outer stress gradient [Pa/m], \(y,y_s\) are lengths [m], and \(\sigma_S\) is sliding-region normal stress [Pa]. The minus sign is used above \(+y_s\) and the plus sign below \(-y_s\). **VERIFIED FULL TEXT — Zhang 2025, Eq. (10) and Fig. 4, printed p. 825 / PDF p. 5.**

The section force and moment are

\[
N=N_J+\int_{-y_s}^{y_s}\sigma_Sb\,dy,
\qquad
M=M_J+\int_{-y_s}^{y_s}\sigma_Syb\,dy.
\tag{Zhang 11}
\]

Here \(N,N_J\) are axial forces [N], \(M,M_J\) are bending moments [N·m], \(\sigma_S\) is stress [Pa], and \(b,y,y_s\) are lengths [m]. These equations partition the section resultants between jammed and sliding regions. **VERIFIED FULL TEXT — Zhang 2025, Eq. (11), printed p. 825 / PDF p. 5.**

Integration of the outer linear distribution gives

\[
M_J=\frac{b}{12}(h+y_s)(h-2y_s)^2K_J.
\tag{Zhang 12}
\]

Here \(M_J\) is jammed-region moment [N·m], \(b,h,y_s\) are lengths [m], and \(K_J\) is stress gradient [Pa/m]. It lets the jammed stress slope be recovered from moment. **VERIFIED FULL TEXT — Zhang 2025, Eq. (12), printed p. 825 / PDF p. 5.**

Local equilibrium inside the yielded region is

\[
\frac{\partial\sigma_S}{\partial s}+\frac{\partial\tau_S}{\partial y}=0.
\tag{Zhang 13}
\]

Here \(\sigma_S\) is longitudinal normal stress [Pa], \(\tau_S=\operatorname{sign}(Q)\mu p\) is the constant yielded-region shear stress [Pa], and \(s,y\) are coordinates [m]. Since \(\partial\tau_S/\partial y=0\), the mathematics gives \(\partial\sigma_S/\partial s=0\), so \(\sigma_S=f(y)\). One sentence in the paper says it “depends only on \(s\),” contradicting both Eq. (13) and the immediately following statement that equal \(y\) gives equal stress. This is a **VERIFIED FULL-TEXT internal inconsistency**; the equation is followed here. **Zhang 2025, Eq. (13), printed p. 825 / PDF p. 5.**

For the geometry in Figure 5b, the sliding-core integrals are transformed to path integrals:

\[
\int_{-y_s}^{y_s}\sigma_Sb\,dy
=\int_{s_0}^{s}[\sigma_S(y_s)+\sigma_S(-y_s)]b\,y_s'\,d\xi.
\tag{Zhang 14a}
\]

Here the left side and right side are axial force contributions [N], \(\sigma_S\) is stress [Pa], \(b,y_s,s,s_0,\xi\) are lengths [m], and \(y_s'=dy_s/ds\) is dimensionless [–].

The corresponding moment transformation is

\[
\int_{-y_s}^{y_s}\sigma_Syb\,dy
=\int_{s_0}^{s}[\sigma_S(y_s)-\sigma_S(-y_s)]y_sb\,y_s'\,d\xi.
\tag{Zhang 14b}
\]

Here both sides are moment contributions [N·m]; \(\sigma_S\) [Pa], \(y_s,b,s,s_0,\xi\) [m], and \(y_s'\) [–] retain the definitions above. The stress **sum** enters axial force, whereas the stress **difference** enters moment because the lower boundary is at \(-y_s\). These compact expressions preserve the final equalities of the paper's Eq. (14). **VERIFIED FULL TEXT — Zhang 2025, Eq. (14) and Fig. 5, printed p. 825 / PDF p. 5.**

Continuity at \(y=\pm y_s\) then gives

\[
N=N_J+\int_{s_0}^{s}\frac{2N_J}{A_J}b\,y_s'\,d\xi,
\qquad M=M_J.
\tag{Zhang 15}
\]

Here \(N,N_J\) are forces [N], \(M,M_J\) are moments [N·m], \(A_J\) is area [m\(^2\)], \(b,s,s_0,\xi\) are lengths [m], and \(y_s'\) is dimensionless [–]. Symmetry makes the yielded-core moment contribution vanish in this construction. **VERIFIED FULL TEXT — Zhang 2025, Eq. (15), printed p. 825 / PDF p. 5.**

Differentiation produces

\[
N'=N_J'+N_J\frac{y_s'}{h/2-y_s}=-Q\theta'.
\tag{Zhang 16}
\]

Here \(N,N_J,Q\) are forces [N], primes denote differentiation with respect to \(s\) [m], \(y_s,h\) are lengths [m], \(y_s'\) is dimensionless [–], and \(\theta'\) is curvature [m\(^{-1}\)]. The last equality uses Eq. (1) with no distributed axial load. **VERIFIED FULL TEXT — Zhang 2025, Eq. (16), printed p. 825 / PDF p. 5.**

The solution is printed in the form

\[
N_J=\left(\frac{2y_s}{h}-1\right)
\left[
\int_{s_0}^{s}\frac{-Q\theta'}{2y_s/h-1}\,d\xi
+\frac{N(s_0)}{2y_s(s_0)/h-1}
\right].
\tag{Zhang 17}
\]

Here \(N_J,Q,N(s_0)\) are forces [N], \(y_s,h,s,s_0,\xi\) are lengths [m], and \(\theta'\) is curvature [m\(^{-1}\)]. The lower-limit glyph in the PDF is unclear; \(s_0\) is used because the preceding prose identifies it as the boundary where \(N_J=N\). This is a transcription note, not a hidden correction. **VERIFIED FULL TEXT — Zhang 2025, Eq. (17), printed p. 826 / PDF p. 6.**

For the second Figure 5 geometry, the boundary distribution is

\[
\begin{aligned}
\sigma_J(s_0)&=\frac{N(s_0)}{A}+K_J(s_0)(y\mp y_s)\\
&=\frac{N(s_0)}{A}+\frac{12M(s_0)}{b(h+y_s)(h-2y_s)^2}(y\mp y_s),\\
\sigma_S(s_0)&=\frac{N(s_0)}{A}.
\end{aligned}
\tag{Zhang 18}
\]

Here \(\sigma_J,\sigma_S\) are stresses [Pa], \(N(s_0)\) is axial force [N], \(A\) is area [m\(^2\)], \(K_J\) is stress gradient [Pa/m], \(M(s_0)\) is moment [N·m], and \(b,h,y,y_s\) are lengths [m]. The equation assumes uniform axial stress at \(s_0\) and adds the outer bending gradient. The following prose states \(N_J(s_0)=N(s_0)2y_s(s_0)/h\), which conflicts with the jammed area \(b(h-2y_s)\): uniform axial stress would instead imply a jammed-force fraction \((h-2y_s)/h\). The printed follow-on expression is therefore **UNRESOLVED / apparent source inconsistency**, not silently repaired here. **VERIFIED FULL TEXT — Zhang 2025, Eq. (18) and following sentence, printed p. 826 / PDF p. 6.**

### 5.7 Deformation and incremental solution: Eqs. (19)–(20)

Rotation is recovered from jammed-region bending:

\[
\Delta\theta(s)=\int_0^s\frac{M}{EI_J}\,d\xi.
\tag{Zhang 19}
\]

Here \(\Delta\theta\) is rotation increment [rad], \(s,\xi\) are coordinates [m], \(M\) is bending moment [N·m], \(E\) is Young's modulus [Pa], and \(I_J\) is jammed-region second moment of area [m\(^4\)]. It is the Euler–Bernoulli moment–curvature relation applied to the surviving jammed bands. **VERIFIED FULL TEXT — Zhang 2025, Eq. (19), printed p. 826 / PDF p. 6.**

The paper prints

\[
I_J=
\begin{cases}
bh^3/12, & y_s=0,\\[3pt]
\dfrac{2}{3}\left[(h/2)^3-y_s^3\right], & y_s\ne0.
\end{cases}
\tag{Zhang 20}
\]

Here \(I_J\) should be second moment of area [m\(^4\)], \(b\) is width [m], and \(h,y_s\) are lengths [m]. The first branch has correct dimensions; the second has units m\(^3\) as printed. Direct integration of the two jammed outer bands would give \(2b[(h/2)^3-y_s^3]/3\), but adding \(b\) is an **INFERENCE**, not the published equation. Author code or clarification is needed before independent implementation. **VERIFIED FULL TEXT with dimensional inconsistency — Zhang 2025, Eq. (20), printed p. 826 / PDF p. 6.**

The unnumbered algorithm applies the target load incrementally. At load step \(k\), it scales the load, calculates \(N^k,Q^k,M^k\) with Eq. (2), obtains \(y_s^k\) with Eq. (9), reduces the load increment until the maximum change in \(y_s\) satisfies a sheet-thickness-based tolerance, computes the moment/rotation increment with Eqs. (19)–(20), and updates \(\theta\). Here \(k\) is a dimensionless step index, \(\alpha^k\) is a dimensionless load factor, and \(\beta_\alpha,\beta_\delta\) are dimensionless step/tolerance factors. Numerical values and admissible ranges for those factors, and parts of the update ordering, are not sufficiently specified for unambiguous reproduction. **VERIFIED FULL TEXT for the printed algorithm; implementation details UNRESOLVED — Zhang 2025, Algorithm, printed p. 826 / PDF p. 6.**

### 5.8 How Zhang treats slip, pressure, and layer count

Zhang does **not** calculate individual interface displacement. Instead:

- the sliding zone \(|y|\le y_s(s)\) is a distributed region at the Coulomb cap;
- the outer regions \(|y|>y_s(s)\) remain jammed;
- the movement of \(y_s\) represents progressive slip;
- the changing \(I_J(y_s)\) converts slip progression into changing bending compliance.

This is more informative than a single equivalent stiffness because it predicts stress fields and a slip boundary. It is less detailed than a discrete-interface model because it cannot say that a particular numbered interface has slipped by a particular displacement.

Pressure enters through \(\mu p\), then through \(Q_{\mathrm{slip}}\), \(Q_{\max}\), and \(y_s(Q)\), then through \(I_J\), rotation, and deflection. At fixed \(Q\), increasing \(p\) reduces or delays the yielded zone; this directional statement is **INFERENCE directly from Eqs. (5)–(9)**. The model assumes the cap is spatially uniform and does not solve a local normal-contact field.

Layer count \(n\) is eliminated from most equations by using total height \(h\). At fixed \(h\), it survives implicitly through \(\delta=h/n\), especially in \(Q_{\max}\) and \(y_s=h/2-\delta\). The number of governing equations does not grow by adding one state per interface; that complexity advantage is **INFERENCE from the architecture**, because no runtime benchmark is reported.

### 5.9 Numerical validation

Zhang compares the CLJM with explicitly layered-looking Abaqus models of straight cantilevers 40 mm long, 20 mm out-of-plane width, and 5 mm total height. Discrete cases use 10 and 25 layers; Figure 6 labels the continuum-based curve “50 layers.” Parameters are \(E=0.3\) GPa, \(\mu=0.5\), and \(p=0.1\) MPa. CPS4R plane-stress elements have 0.1 mm side length. A transverse end force is distributed among layer ends, with 3, 4, and 5.5 N cases representing full jamming, half slipping, and full slipping. **VERIFIED FULL TEXT — Zhang 2025, Sect. 5 and Fig. 6, printed pp. 827–828 / PDF pp. 7–8.**

The comparisons show:

- good interior stress agreement in full jamming;
- layer-scale FEA oscillations decreasing from 10 to 25 layers;
- reasonable interior agreement in partial slip, but a CLJM sliding region that is too wide because transverse normal stress is neglected;
- substantial full-slip shear error in jammed outer bands because the actual segments are curved while Eq. (3) uses a straight-beam profile;
- boundary error near the cantilever end/constraint region.

These are **VERIFIED FULL TEXT — Zhang 2025, Sect. 5, Fig. 6, printed pp. 827–828 / PDF pp. 7–8.** The main text does not report the FEA contact formulation, a stress-error norm, mesh convergence, or runtime scaling. Exact constitutive equivalence between FEA and CLJM is therefore **UNRESOLVED**.

### 5.10 Experimental validation

The experiment uses 20 PVC sheets in a flexible PVC membrane, forming a 100 mm long, 20 mm wide, and 5 mm high cantilever. The root fixture is mounted on a free-sliding rail to release horizontal restraint. A tensile testing machine applies transverse load. Vacuum pressure is 60 kPa, and the analytical comparison uses \(E=755\) MPa and \(\mu=0.55\). **VERIFIED FULL TEXT — Zhang 2025, Sect. 5 and Fig. 7, printed p. 828 / PDF p. 8.**

Figure 7 compares load against deflection over axes extending approximately to 10 N and 50 mm. The red CLJM curve lies entirely within the experimental mean ±1 standard-deviation band. That supports one global force–deflection case; it is not a pressure sweep, a layer-count sweep, or a quantified universal error bound. **VERIFIED FULL TEXT — Zhang 2025, Fig. 7 and accompanying text, printed p. 828 / PDF p. 8.**

The main text does not state the repeat/specimen count, loading rate, parameter-identification method for \(E\) and \(\mu\), or RMSE/maximum percentage error. Those details are **UNRESOLVED**.

### 5.11 Stated limitations and likely failure conditions

**Author-stated or demonstrated, VERIFIED FULL TEXT:**

- end/constraint effects are not explicit and cause near-boundary stress errors;
- omitting transverse interlaminar normal stress overpredicts sliding-zone width;
- the straight-beam shear profile is inaccurate in strongly curved/full-slip outer regions;
- the authors recommend FEA near free boundaries and under extreme loads causing full slip;
- the best reported performance is away from boundaries and under partial or small-to-moderate slip.

**UNRESOLVED:** quantitative error versus \(n\), pressure, curvature, load-step size, reverse loading, cycle count, rate, wear, pressure nonuniformity, or material nonlinearity.

**INFERENCE:** low \(n\), short/thick beams, nonrectangular cross-sections, torsion, spatial bending, wrinkling, and non-Coulomb friction are plausible failure regimes because they violate the model architecture, but Zhang does not map those boundaries.

### 5.12 What Zhang solves—and what it leaves

Zhang demonstrates that a many-layer layer-jamming beam can be represented by a continuous yielded-band model that predicts internal stresses and global deformation without interface indexing. That means “construct any continuum model” is already solved as a broad research claim. The paper does **not** provide a systematic, tolerance-based domain of validity over layer count, pressure, curvature/load, and regime; it gives selected FEA cases and one experiment. This absence within the three-paper verified set is evidence of an unresolved question, not proof of novelty across all literature.

## 6. Direct comparison: Narang 2018 → Caruso 2023 → Zhang 2025

### 6.1 One-page mechanical comparison

| Dimension | Narang et al. (2018) | Caruso et al. (2023) | Zhang et al. (2025) |
|---|---|---|---|
| Primary analytical representation | Two explicit layers joined by one frictional interface, with cohesive and slipped segments along the beam | Arbitrary even \(n\), retaining discrete interface identity and sequential symmetric slip events | Continuous fields over \(y,s\), with a moving boundary between yielded and jammed regions |
| What progresses | Slipped **length** along the two-layer interface | Number/location of slipped **interfaces** through thickness | Half-height \(y_s(s)\) of a **distributed sliding band** |
| Main analytical loading | Uniformly distributed load on a cantilever | Symmetric three-point bending with overhangs | General planar curved-beam resultants; validated as an end-loaded cantilever |
| Beam theory | Euler–Bernoulli with an interfacial displacement variable | Euler–Bernoulli for current coherent layer groups | Curved-beam equilibrium plus Euler–Bernoulli bending of jammed bands |
| Friction | Coulomb; penalty friction in FEA | \(\tau_{\mathrm{slip}}=\mu p\); penalty friction in FEA | \(|\tau|\le\mu p\), used as an ideal-plastic yield cap |
| Individual interface slip | Explicit in two-layer analytical solution and many-layer FEA | Explicitly indexed, central to outer | Not retained |
| Slip displacement | Interfacial displacement variable in two-layer derivation | Slip events inferred from equilibrium/thresholds; closed-form formulas focus on transitions | No individual relative-displacement field; distributed yielded-zone state |
| Pre-slip | Fully cohesive; maximum stiffness; zero damping | One composite beam; \(I\propto n^3\); pressure-independent elastic slope | Full-height elastic/jammed section; parabolic shear field |
| Partial/progressive slip | Slipped length grows from root to free end | Central interface then symmetric pairs slip outward; piecewise stiffness | Central cross-sectional yielded band grows outward continuously |
| Full slip | Whole available interface length slips | All discrete interfaces slip; sum of individual layer inertias | \(y_s=h/2-\delta\); capped core plus thin outer bands |
| Pressure | Sets friction capacity and transition behavior; experimental pressure sweep | Linear in transition loads/deflections; experimental sweep at 24/48/68 kPa | Sets yield cap and thresholds; one experimental pressure and one FEA pressure |
| Layer count | Analytical demonstration: 2; many-layer FEA/experiment explicit; ideal stiffness ratio \(n^2\) | Explicit in transition formulas; experiments at 8/12/16/20 | Removed from most equations; implicit through \(\delta=h/n\); FEA at 10/25, experiment at 20 |
| Outputs | Elastica, stiffness, slip length, transition loads, energy, damping | Critical loads/deflections, piecewise force–deflection, stiffness, hysteresis | \(\sigma\), \(\tau\), \(y_s\), thresholds, rotation/deflection |
| Analytical complexity versus \(n\) | General extension said possible but algebraically taxing | Roughly \(n/2\) indexed events | No per-interface equation enumeration (**INFERENCE**) |
| Numerical reference | Explicit 2D plane-strain contact FEA, large deformation | Explicit 2D plane-strain contact FEA, large deformation | Explicit-looking 2D plane-stress layered FEA; contact details not reported |
| Experimental validation | Multiple \(n,p\); minimum FEA–experiment \(R^2=0.9879\) | Multiple \(n,p\), three repeats; good agreement, no global numerical error metric | One \(n,p\) global curve within ±1 SD; no numerical error metric |
| Hysteresis | Predicted and experimentally evaluated | Predicted/validated over loading–unloading cycles | Constitutive analogy is path dependent, but hysteresis is not experimentally validated |
| Key verified limitation | Many-layer FEA runtime grows with \(n\); high-\(n\) pressure uniformity | Support contact pressure and ideal clamping cause high-deflection error | Boundary effects, omitted transverse normal stress, full-slip curvature error |

Unless marked **INFERENCE**, the table is **VERIFIED FULL TEXT** from Narang Sects. 2–3 and Experimental Section, Caruso Sects. 2–6, and Zhang Sects. 2–6.

### 6.2 Exactly what each later work attempts to overcome

#### Narang → Caruso

Narang solves the full three-regime analytical problem for two layers and shows that explicit many-layer FEA can accurately reproduce experiments. But a many-layer analytical extension is described as algebraically taxing, while explicit FEA execution time grows with layer count. **VERIFIED FULL TEXT — Narang 2018, Sects. 2.1 and 3.3, PDF pp. 3 and 7.**

Caruso's response is not to make the stack continuous. It retains the discrete interfaces but exploits their orderly symmetric slip sequence. Closed-form increments \(F_i,w_i\) replace repeated contact simulation, and the nonlinear curve becomes a succession of linear stiffness segments. The 2023 extension also addresses a specific loading/boundary limitation: cohesive overhangs outside the supports create curvature reversal and additional post-slip stiffness, so Caruso replaces the earlier simply supported post-slip assumption with an ideal clamped boundary. **VERIFIED FULL TEXT — Caruso 2023, Introduction, Sect. 2, and Sects. 5.4–6, PDF pp. 2–4 and 7–8.**

Thus Caruso overcomes:

- the absence of a practical arbitrary-even-\(n\) analytical transition model;
- reliance on expensive FEA for every many-layer design calculation;
- omission of overhang-induced post-slip stiffness in the authors' preceding formulation.

Caruso does **not** overcome the conceptual growth in discrete state count: it still needs an interface/event index through approximately \(n/2\).

#### Caruso → Zhang

Zhang explicitly identifies discrete layer-by-layer analytical models as inconvenient for many layers. Its response is to replace the interface sequence with a continuous field and one moving yield boundary. **VERIFIED FULL TEXT — Zhang 2025, Introduction and Sect. 2, printed pp. 821–823 / PDF pp. 1–3.**

Thus Zhang attempts to overcome:

- per-layer/per-interface bookkeeping;
- saw-tooth, layer-scale stress descriptions that become dense as \(\delta/h\to0\);
- difficulty obtaining smooth internal stress fields in a high-layer-count beam;
- computational/analytical complexity that grows with interface count.

In exchange, Zhang loses exact interface identity and inherits continuum assumptions. Its main errors arise precisely where erased details or simplified kinematics matter: end contacts, transverse normal stress, and strongly curved full-slip bands.

### 6.3 The three models are complementary, not a simple winner sequence

- Narang is strongest for understanding **spatial slip-length propagation, damping, and a fully coupled two-layer boundary-value solution**, plus high-fidelity many-layer FEA.
- Caruso is strongest for **explicit multilayer transition sequencing, parametric \(n,p,\mu\) formulas, three-point-bending overhang effects, and hysteresis**.
- Zhang is strongest for **compact high-layer-count stress fields and a continuous slip-front representation**.

Which model is “better” depends on the desired output. A controller needing a fast global stiffness estimate may prefer a reduced description; a failure analyst needing individual interface displacement may require a discrete model; a design study near full slip or supports may need explicit contact FEA.

## 7. Is Zhang scientifically “homogenization”?

### 7.1 Terms that should not be conflated

| Term | Scientific meaning | Does Zhang clearly satisfy it? |
|---|---|---|
| **Continuum modeling** | Treats stress, strain, and state quantities as fields varying continuously in space | **Yes — VERIFIED FULL TEXT.** This is the authors' own description and mathematical construction. |
| **Homogenization** | Derives macroscopic equations/properties from microscale structure through an explicit averaging, representative-cell, asymptotic, or scale-separation procedure | **Not demonstrated.** The paper takes a thin-layer continuum limit but does not derive an effective tensor or cell problem. |
| **Effective-medium modeling** | Replaces a heterogeneous/discrete material with a continuum response reproducing selected aggregate behavior | **Partly, as interpretation.** The Coulomb interface stack becomes an elastoplastic-like medium, but the authors do not perform a formal effective-property identification. |
| **Equivalent-property model** | Replaces the structure mainly with equivalent scalar/tensor properties, such as one effective modulus or stiffness | **No, not primarily.** Zhang predicts spatial \(\sigma,\tau,y_s\), not only a scalar stiffness. |
| **Reduced-order model** | Uses fewer state variables/degrees of freedom to reproduce selected outputs than a higher-fidelity reference | **Yes, relative to explicit interfaces, as INFERENCE.** One field boundary replaces many interface states, although no formal projection/basis reduction is used. |

### 7.2 Best description

The most defensible name is:

> **a continuum-limit, elastoplastic-like beam surrogate with a distributed Coulomb-yielded slip zone.**

“Continuum-based model” is directly supported by the paper. “Reduced representation” is scientifically reasonable when explicitly relative to Caruso or discrete FEA. “Effective-medium-like” is acceptable as a cautious interpretation. “Homogenized model” should be used only informally and with qualification; **formal homogenization is not established by the verified derivation**.

This wording matters for P1. If P1 promises “a homogenized model” but only reproduces Zhang's continuum limit with a new label, it is not a new mechanics contribution. A defensible project would need either a genuine micro-to-macro derivation or a new falsifiable question about the existing continuum approximation's validity.

## 8. Model validity and breakdown: what the verified evidence actually spans

### 8.1 Validation-domain comparison

| Axis | Narang 2018 | Caruso 2023 | Zhang 2025 |
|---|---|---|---|
| Layer count | Analytical 2; many-layer tests/FEA 5,10,15,20 in Fig. 3 | Tests 8,12,16,20 | FEA 10,25; experiment 20; continuum plot labeled 50 |
| Pressure | Figure 3: 0,24,47,71 kPa for 20 layers | Experiment 24,48,68 kPa for 20 layers; 68 kPa \(n\)-sweep; 70 kPa friction FEA | Experiment 60 kPa; FEA 0.1 MPa |
| Friction | FEA 0.25,0.50,0.75; not varied experimentally | FEA 0.2–0.5; measured \(\mu=0.55\) for specimens | \(\mu=0.5\) FEA; \(\mu=0.55\) experiment/model; identification method unstated |
| Loading | Two-layer distributed-load cantilever; many-layer 3-point bending | 3-point bending, load/unload to 8 mm | End-loaded cantilever; selected 3,4,5.5 N FEA; experimental curve to roughly 10 N/50 mm axes |
| Regimes | All three; two-layer slip length and many-layer FEA | All three; discrete interface progression and hysteresis | All three; continuous yield zone; largest error in full slip |
| Accuracy evidence | Many-layer FEA: minimum \(R^2=0.9879\); max experimental deviation 0.24 N | Qualitative good agreement; no global error norm | Experiment within ±1 SD; no error norm; selected stress profiles |
| Boundary/contact validity | General two-layer clamped/free conditions; explicit contact FEA | Cohesive overhang idealized as clamp; support pressure omitted | End effects omitted; transverse normal contact stress omitted |

All numeric entries are **VERIFIED FULL TEXT** from the cited papers. Cross-study comparison must remain cautious because geometry, materials, plane-stress/plane-strain choices, fixtures, and outputs differ.

### 8.2 Breakdown evidence by mechanism

| Candidate breakdown mechanism | Verified status |
|---|---|
| Low layer count for Zhang | **UNRESOLVED boundary.** The derivation requires \(\delta/h\ll1\), and the authors state roughly \(n\ge10\), but no dense convergence study is given. |
| Very high layer count | **UNRESOLVED for model accuracy.** Narang warns about physical pressure uniformity; Zhang expects smoother continuum fields but provides no upper-range experiment. |
| Low/high vacuum pressure | **UNRESOLVED for Zhang.** Its equations give trends, but no pressure sweep validates them. Narang and Caruso sweep pressure for their different discrete models. |
| Increasing load/curvature | **Partly VERIFIED.** Zhang shows interior partial-slip agreement but substantial full-slip curved-beam shear error. |
| End/support effects | **VERIFIED limitation.** Caruso and Zhang independently show that boundaries/contact pressure matter. |
| Transverse normal stress | **VERIFIED limitation for Zhang.** Its omission makes the predicted sliding region too wide. |
| Hysteresis/reverse loading | **Solved for discrete models; UNRESOLVED for Zhang.** Narang and Caruso validate damping/hysteresis; Zhang does not validate a reverse-loading law. |
| Cyclic fatigue, wear, rate | **UNRESOLVED** in these model validations. |
| Three-dimensional bending/torsion | **UNRESOLVED** for all three analytical formulations. |
| Nonuniform pressure | **UNRESOLVED quantitatively.** Narang flags high-\(n\) uniformity; Caruso/Zhang use uniform imposed pressure. |

## 9. Questions already solved by verified evidence

The following broad questions should not be presented as open:

1. **Do layer-jamming beams have pre-slip, progressive/partial-slip, and full-slip regimes?** Yes. All three papers model them, and Narang/Caruso validate the regime behavior experimentally.
2. **Can pressure and Coulomb friction predict slip thresholds?** Yes, within the stated uniform-pressure, constant-friction assumptions.
3. **Can a two-layer beam be modeled analytically through all regimes, including slip length and damping?** Yes, by Narang.
4. **Can many-layer explicit-contact FEA predict force–deflection behavior accurately?** Yes. Narang reports minimum \(R^2=0.9879\) in its tested matrix.
5. **Can progressive discrete interface slips in an arbitrary even-layer stack be predicted analytically?** Yes, by Caruso within its geometry and assumptions.
6. **Can layer count and vacuum pressure effects on transition loads/stiffness be modeled and experimentally checked?** Yes, for the discrete formulations and tested ranges in Narang and Caruso.
7. **Can three-point-bending overhangs change post-slip stiffness and be represented analytically?** Yes, approximately, by Caruso's clamped-boundary extension.
8. **Can a continuum-based model of a many-layer layer-jamming beam be constructed and compared with FEA/experiment?** Yes, by Zhang.
9. **Are boundary effects, transverse contact stress, and large-curvature/full-slip behavior important limitations of Zhang's CLJM?** Yes, qualitatively and through selected FEA comparisons.

These conclusions are **VERIFIED FULL TEXT** within the sources' stated domains. “Solved” does not mean universally valid for every geometry or loading path.

## 10. Questions genuinely unresolved in the three verified papers

The following remain unresolved **within this verified three-paper corpus**:

1. What is the quantitative discrete-to-continuum convergence rate as \(\delta/h=1/n\to0\)?
2. At what \(n\) does Zhang's CLJM first meet a predeclared error tolerance for global response and slip-zone prediction?
3. How does CLJM error change when pressure is varied independently rather than held at one experimental value?
4. How do load and curvature separately affect error, especially during the transition into full slip?
5. Can \(y_s(s)\) be mapped quantitatively to the number and displacement of slipped discrete interfaces?
6. Can transverse normal-contact stress and end effects be incorporated without returning to full interface FEA?
7. Can the continuum model reproduce load–unload hysteresis, reverse slip, re-sticking, and cycle-to-cycle evolution?
8. How sensitive are predictions to the apparent inconsistencies around Zhang Eqs. (13), (18), and (20), and to its under-specified incremental algorithm?
9. What dimensionless parameters transfer a validity boundary between specimen sizes, materials, and fixtures?
10. Do adjacent 2025–2026 or laminated-beam/partial-interaction literatures already answer these questions under different terminology?

Items 1–9 are **UNRESOLVED based on the three verified full texts**. Item 10 explicitly **requires further literature verification**. None is automatically a novel research gap.

## 11. Is validity/breakdown mapping still scientifically defensible?

### 11.1 Answer

**Yes—as a falsifiable verification question, not yet as a confirmed novelty claim.**

The verified evidence supports this careful conclusion:

- Zhang has already built and partly validated the continuum representation.
- Zhang has already identified several failure mechanisms qualitatively.
- Zhang has **not** reported a systematic, tolerance-based validity surface across layer count, pressure, load/curvature, and slip regime.
- Narang and Caruso provide discrete baselines and broader \(n,p\) experiments, but they do not map the error of Zhang's later continuum model.

The direction would cease to be defensible if closer verified literature already supplies that validity surface, if the CLJM cannot be reproduced reliably from its published equations, or if its error remains negligible over every relevant design condition and no meaningful boundary is found. Those are productive falsification outcomes, not failures of the research process.

### 11.2 Useful nondimensional coordinates

A compact validity study could use layer-scale ratio

\[
\lambda=\frac{\delta}{h}=\frac{1}{n}.
\]

Here \(\lambda\) is dimensionless layer slenderness [–], \(\delta\) is one-layer thickness [m], \(h\) is total stack height [m], and \(n\) is layer count [–].

A normalized section shear demand is

\[
\chi=\frac{|Q|}{\mu pbh}.
\]

Here \(\chi\) is a dimensionless demand-to-friction-cap ratio [–], \(Q\) is section shear force [N], \(\mu\) is friction coefficient [–], \(p\) is pressure [Pa], and \(b,h\) are width and total height [m]. Zhang's first threshold corresponds to \(\chi=2/3\). This coordinate combines load and pressure in the way the governing equations do.

A dimensionless curvature is

\[
\eta=\frac{h}{r}=h\kappa.
\]

Here \(\eta\) is dimensionless curvature [–], \(h\) is total height [m], \(r\) is curvature radius [m], and \(\kappa=1/r\) is curvature [m\(^{-1}\)]. Zhang assumes \(\eta\ll1\) for the straight-beam shear approximation.

These coordinates are **INFERENCE / proposed analysis variables**, not a validated scaling law from the papers. They reduce a four-variable sweep to physically interpretable ratios but do not eliminate the need to vary \(n\) and \(p\) independently when checking assumptions such as vacuum uniformity or pressure-dependent contact.

### 11.3 Narrowest defensible research question

> **For slender rectangular vacuum layer-jamming cantilevers of fixed material and friction pair under monotonic quasi-static planar bending, how does the prediction error of Zhang's CLJM relative to an explicit-interface reference and independent experiments vary with \(\lambda=\delta/h\), applied pressure \(p\), normalized shear demand \(\chi\), and normalized curvature \(\eta\) as the beam moves from pre-slip through partial slip into full slip, and where does that error first exceed a pre-registered engineering tolerance?**

This is narrower than “develop a homogenized model.” It fixes geometry class, material pair, loading dimensionality, and loading history; treats the published CLJM as the object being tested; and requires a declared error metric and tolerance. The two primary outputs should be limited to:

1. global force–deflection error; and
2. slip-front or discrete-to-continuum slip-state error.

A broader claim about cyclic behavior, torsion, arbitrary soft robots, or universal homogenization should be excluded unless later evidence and feasibility justify it.

### 11.4 What would constitute a meaningful answer

A validity map is scientific only if it includes:

- an independently implemented CLJM with source ambiguities documented;
- an explicit-interface reference whose contact assumptions are stated;
- calibration data separated from validation data;
- predeclared error measures and acceptance threshold;
- parameter points in pre-slip, partial-slip, and full-slip states;
- a boundary or scaling explanation tied to mechanics, not just a colored error plot;
- experiments at enough independent \(n,p\) combinations to test rather than merely fit the boundary.

Merely running more FEA or collecting more curves would not satisfy the repository's novelty standard unless the results expose a reproducible mechanics-based breakdown criterion.

## 12. Fit under the registered variable-stiffness topic

Registered topic:

> **Design and Development of Variable-Stiffness Mechanisms for Soft Manipulators and Continuum Robots.**

The narrow question fits as the **model-based design and validation component** of a layer-jamming variable-stiffness mechanism:

1. A soft manipulator or continuum robot needs a jamming insert sized for required compliant and stiff states.
2. Narang and Caruso show that stiffness is load- and slip-regime-dependent, not a single on/off property.
3. Zhang offers a compact model potentially suitable for rapid sizing or control, but its design domain is not systematically bounded.
4. A verified validity map would tell a designer when the compact model is trustworthy and when explicit contact analysis or experiments are required.
5. A prototype mechanism could then be designed *using* those limits and tested at representative safe and breakdown points.

The mechanical research contribution would therefore be “validated design limits for a reduced layer-jamming beam representation,” while the registered application context is “design and development of a variable-stiffness mechanism for a soft manipulator/continuum robot.” The robot embodiment should not be used to manufacture novelty: the mechanics question must stand even before integration.

## 13. Practical learning synthesis

If you need to explain the progression to a supervisor in one minute:

> Vacuum does not directly make the sheets stiff; it raises normal contact, allowing friction to transmit longitudinal shear. Narang solved how slip grows along one interface in a two-layer cantilever and used explicit contact FEA for many layers. Caruso retained every interface but converted the many-layer slip sequence into analytical transition loads and piecewise stiffness, including support-overhang effects. Zhang then removed the interface index and treated the stack as a continuous elastoplastic-like medium with a central yielded band whose boundary moves outward. Zhang is therefore a continuum-limit reduced representation, not demonstrated formal homogenization. The remaining defensible question is not whether a continuum model exists, but where its approximation error becomes unacceptable relative to discrete mechanics and experiment.

The most important mental picture is:

```text
load rises
   ↓
required interlayer shear rises
   ↓
shear reaches μp
   ↓
slip progresses
   ├─ along interface length (Narang two-layer)
   ├─ across numbered interfaces (Caruso many-layer)
   └─ across a continuous yielded height y_s (Zhang continuum)
   ↓
effective coherent bending section shrinks
   ↓
bending stiffness falls and friction dissipates energy
```

## 14. Evidence and provenance audit

### 14.1 Major claim traceability

| Major claim | Status | Primary provenance |
|---|---|---|
| Narang analytically solves a two-layer distributed-load cantilever through all regimes | **VERIFIED FULL TEXT** | Narang 2018, Sect. 2.1 and Experimental Section, PDF pp. 3 and 7 |
| Narang many-layer FEA matches experiments with minimum \(R^2=0.9879\) | **VERIFIED FULL TEXT** | Narang 2018, Fig. 3, PDF p. 4 |
| Narang high-\(n\) single-crystal/single-slip-system idea is a future proposal | **VERIFIED FULL TEXT** | Narang 2018, Sect. 3.3, PDF p. 7 |
| Caruso predicts sequential central-to-outer interface slips for arbitrary even \(n\) | **VERIFIED FULL TEXT** | Caruso 2023, Eqs. (8)–(15), Fig. 2, PDF pp. 3–4 |
| Caruso validates \(n,p\) effects and overhang-induced post-slip stiffness | **VERIFIED FULL TEXT** | Caruso 2023, Figs. 4–6, Sects. 5.1–5.4, PDF pp. 5–8 |
| Zhang replaces interface indexing by continuous fields and \(y_s(s)\) | **VERIFIED FULL TEXT** | Zhang 2025, Sects. 2–4, Eqs. (1)–(20), printed pp. 822–826 / PDF pp. 2–6 |
| Zhang's interior stress fields improve with layer count | **VERIFIED FULL TEXT** | Zhang 2025, Fig. 6, Sect. 5, printed pp. 827–828 / PDF pp. 7–8 |
| Zhang's 20-layer/60 kPa curve lies within ±1 SD | **VERIFIED FULL TEXT** | Zhang 2025, Fig. 7, printed p. 828 / PDF p. 8 |
| Zhang is not demonstrated formal homogenization | **INFERENCE** | Absence of cell/averaging/asymptotic effective-property derivation in inspected Sects. 2–4 |
| A systematic CLJM validity map is absent from these three papers | **INFERENCE bounded to this corpus** | Comparison of Narang, Caruso, and Zhang validation matrices |
| No other literature has already produced that map | **UNRESOLVED; requires verification** | Cannot be established from these three papers |

### 14.2 Source ambiguities preserved

1. Narang's exact two-layer governing equations and dimensionless solution are delegated to Supporting Information not present in the locally validated article PDF.
2. Caruso's text directly below Eq. (2) calls \(F_0\) the external load, whereas Figure 2 and Sect. 5 identify total applied load as \(2F_0\).
3. Zhang Eq. (7) does not explicitly print a full-slip central-core branch and does not define the \(\pm\) choice for its outer polynomial.
4. Zhang's post-Eq. (13) prose conflicts with \(\sigma_S=f(y)\) and Eq. (13).
5. Zhang's post-Eq. (18) expression for \(N_J(s_0)\) conflicts with its own jammed-area definition under uniform stress.
6. Zhang Eq. (20) appears dimensionally incomplete because width \(b\) is absent from the sliding-state inertia branch.
7. Zhang's incremental algorithm does not fully specify step-control parameter values or update details.
8. Zhang's FEA contact law and experimental repeat/rate/error metrics are not reported in the inspected main text.

### 14.3 Repository provenance

- `data/evidence/2018-Mechanically Versatile Soft Machines through Laminar_5f7ccd7357.json`; PDF SHA256 `5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5`.
- `data/evidence/2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation_652e62758f.json`; PDF SHA256 `652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee`.
- `data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json`; PDF SHA256 `95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd`.

No metadata-only paper supports a detailed mechanical statement in this report.

## 15. References

Only references supported by verified repository evidence are listed.

1. Narang, Y. S., Vlassak, J. J., and Howe, R. D. (2018). “Mechanically Versatile Soft Machines through Laminar Jamming.” *Advanced Functional Materials*, 28, 1707136. DOI: `10.1002/adfm.201707136`.
2. Caruso, F., Mantriota, G., Moramarco, V., and Reina, G. (2023). “Layer jamming: Modeling and experimental validation.” *International Journal of Mechanical Sciences*, 251, 108325. DOI: `10.1016/j.ijmecsci.2023.108325`.
3. Zhang, S., Yao, J., Zhao, W., and Wei, C. (2025). “A continuum-based model for a layer jamming beam.” *Mechanical Sciences*, 16, 821–830. DOI: `10.5194/ms-16-821-2025`.

---

**Research conclusion:** The existence of analytical slip models, discrete multilayer transition models, and a continuum-based layer-jamming model is already verified. A narrow validity/breakdown study remains scientifically defensible only as an adversarial, tolerance-based comparison of Zhang's CLJM against discrete-interface evidence across controlled \(n\), \(p\), and load/curvature regimes—and only until broader literature verification shows whether that comparison has already been done.
