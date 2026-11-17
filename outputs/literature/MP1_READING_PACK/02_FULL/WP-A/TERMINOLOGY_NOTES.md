# Terminology Notes — WP-A

This document establishes canonical definitions and usage boundaries for key scientific terms across the seven papers of Work Package A (M01, M02, M03, M04, M05, M38, M39), preventing conceptual conflation during the drafting of Chapters 1 and 2.

---

## 1. Continuum Robotics Terminology (M02, M03)

- **Continuum Robot (Robot liên tục):**
  - *Definition (M02 Definition 1, p. 2):* An actuatable structure whose constitutive material forms continuous curves with elastic deformation.
  - *Distinction from Hyper-Redundant / Rigid-Link Robots:* Conventional articulated robots consist of discrete rigid links joined at discrete kinematic hinges or ball joints. A continuum robot bends continuously along its structure, possessing theoretically infinite degrees of freedom in continuous mechanics.
  - *Pseudocontinuum / Hybrid Systems (M02, p. 2):* Systems composed of many short rigid links coupled with elastic elements. They only approximate curves with continuous tangent vectors.
- **Actuation Classification (M02, M03):**
  - *Intrinsic Actuation (Truyền động nội tại):* Actuators are distributed along the backbone body itself (e.g. pneumatic or hydraulic fluidic elastomer chambers).
  - *Extrinsic Actuation (Truyền động ngoại tại):* Actuators are located externally (typically at the proximal base), and forces/moments are transmitted to the backbone via tendons, push-pull rods, or concentric pre-curved tubes.
- **Backbone (Xương sống đàn hồi):**
  - The primary continuous load-bearing elastic structure (often central NiTi rod, tube bundle, or compliant polymer spine) that provides structural integrity and restores initial shape upon unloading.

---

## 2. Variable Stiffness & Jamming Terminology (M04, M05)

- **Operational Stiffness vs. Material Modulus (Độ cứng hoạt động vs. Môđun vật liệu):**
  - *Stiffness ($K$):* A structural/system property depending on geometry ($L, I$), boundary conditions (cantilever vs. 3-point support), and loading location. Dimensions vary: $\text{N/m}$ (linear), $\text{N}\cdot\text{m/rad}$ (torsional), or $\text{N}\cdot\text{m}^2$ (flexural rigidity $EI$).
  - *Modulus ($E$):* An intrinsic material property ($[\text{Pa}]$ or $[\text{N/m}^2]$). Structural stiffening in jamming is achieved by friction-induced shear resistance coupling multiple layers, **not** by changing the intrinsic Young's modulus of the constituent sheet material.
- **Stiffness Adjusting Ratio ($R$, Tỉ số điều chỉnh độ cứng):**
  - Defined as $R = K_{\max} / K_{\min}$ (M04, p. 2). A dimensionless metric representing the dynamic tuning range under identical boundary conditions.
- **Jamming Mechanism Taxonomy (M05):**
  - *Granular / Particle Jamming (GJ, Jamming hạt):* 0D discrete particles jammed via volumetric confinement and inter-particle contact forces. High omnidirectional stiffness variation but bulky volume.
  - *Fibre / Filament Jamming (FJ, Jamming sợi):* 1D axial fibres packed in a flexible sheath. Resists axial bending through frictional shear along longitudinal contact lines.
  - *Layer / Laminar Jamming (LJ, Jamming lớp/lá):* 2D stacked planar thin sheets. Under vacuum compression, atmospheric pressure increases normal contact traction between sheets; friction prevents interlayer sliding, shifting the bending behavior from decoupled independent bending ($\sum I_i$) to cohesive composite beam bending ($I_{\text{total}}$).

---

## 3. Metrological & Uncertainty Terminology (M38, M39)

- **Measurand (Đại lượng đo, $Y$):**
  - Particular quantity subject to measurement (GUM/M38 Sec. 2.2). In MP1, stiffness $K$ is the measurand, typically derived indirectly from primary input quantities ($F, \Delta w, L$).
- **Measurement Model (Mô hình đo lường, $Y = f(X_1, \dots, X_N)$):**
  - Mathematical functional relationship relating output measurand $Y$ to input quantities $X_i$.
- **Type A Evaluation (Đánh giá Loại A):**
  - Method of evaluation of uncertainty by the statistical analysis of a series of repeated observations (sample mean $\bar{q}$, sample variance $s^2(q_k)$, variance of the mean $s^2(\bar{q}) = s^2/n$).
- **Type B Evaluation (Đánh giá Loại B):**
  - Method of evaluation of uncertainty by means other than statistical analysis of repeated observations, using scientific judgment based on manufacturer specifications, calibration certificates, handbook data, and assumed probability distributions (rectangular $u = a/\sqrt{3}$, triangular $u = a/\sqrt{6}$).
  - *Critical distinction:* Type A and Type B designate the method of evaluation, **not** the nature of the error (i.e. neither corresponds strictly to "random" or "systematic").
- **Standard Uncertainty ($u(x_i)$, Độ không đảm bảo chuẩn):**
  - Uncertainty of the result of a measurement expressed as an estimated standard deviation.
- **Combined Standard Uncertainty ($u_c(y)$, Độ không đảm bảo chuẩn kết hợp):**
  - Standard uncertainty of the result of a measurement when that result is obtained from the values of a number of other quantities, calculated using the Law of Propagation of Uncertainty (taking into account partial derivative sensitivity coefficients $c_i$ and covariance terms for correlated inputs).
  - *Critical warning (M39 Sec. 5.3):* $u_c(y)$ represents a standard deviation ($\pm 1\sigma$), **not** a 95% confidence interval.
- **Expanded Uncertainty ($U$, Độ không đảm bảo mở rộng):**
  - Quantity defining an interval about the measurement result that may be expected to encompass a large fraction of the distribution of values ($U = k \cdot u_c(y)$). Must always be reported with an explicit coverage factor $k$ (typically $k=2$ for approximately 95% level of confidence under a normal distribution).
