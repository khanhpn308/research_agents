# MP1 H0a / H0b / H1 Hypothesis Matrix

> **Task ID:** MP1-E1-W2-03  
> **Scope:** READ-ONLY Tripartite Hypothesis Reconstruction (Clarifications C-02, C-04)  

## 1. Executive Summary Table

| Hypothesis ID | Type | Role | Canonical Status (S16) | Evidence Status | Core Scientific Logic |
|---|---|---|---|---|---|
| **H0a** | `naive_parameter_substitution_null` | Primary null hypothesis (elementary model) | `REFUTED` | `VERIFIED` | The bending response of a vacuum/pressure-confined NiTi wire bundle can be predi... |
| **H0b** | `established_physics_null` | Secondary / Competitor null hypothesis (established continuum mechanics) | `NOT_FALSIFIED` | `VERIFIED` | The bending response, stiffness variation, and energy dissipation of a pressure-... |
| **H1** | `novel_mechanics_alternative` | Alternative hypothesis (research novelty candidate) | `INSUFFICIENT` | `VERIFIED` | A genuinely distinct coupled mechanics formulation is required, wherein local co... |

---

## 2. Detailed Hypothesis Dossiers

### H0a: The bending response of a vacuum/pressure-confined NiTi wire bundle can be predicted by substituting an equivalent constant elastic modulus E_eff into an existing elastic fiber/wire jamming model.

- **Hypothesis Type:** `naive_parameter_substitution_null`
- **Role in Logic Architecture:** Primary null hypothesis (elementary model)
- **Historical Origin:** Formulated explicitly by Astra critique G01 and Stage 3 remediation W07 to evaluate parameter substitution. (Commit: `3a216d680b6e5d4c263121afee0577ac86e530ac`)
- **Canonical Status:** `REFUTED` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Logical Relation to Other Hypotheses:** Rejection of H0a is necessary but NOT sufficient to prove H1; H0b sits between H0a and H1.

#### Evidence Analysis
- **Evidence Supporting:** Valid only in Regime II (small-strain elastic austenite deformation below transformation threshold eps_Ms ~ 0.75%, where NiTi behaves purely as linear elastic wire with E = E_A).
- **Evidence Challenging:** Fails completely in the presence of martensitic transformation: transformation plateau, pinched hysteresis, tension-compression asymmetry, and large stiffness divergence between loading (E_A ~ 60 GPa) and unloading/phase mixture (E_M ~ 25 GPa).
- **What Would Falsify It:** Demonstrating that cyclic bending drives wire strains beyond eps_Ms, causing severe pinched hysteresis and stiffness drops that no single constant E_eff can match.
- **What Would Support It:** Restricting bundle deformation strictly to small curvatures where strains remain below eps_Ms.
- **Remaining Uncertainty:** None regarding its insufficiency under phase transformation; well-bounded that H0a fails whenever strains exceed 0.75%.

#### Historical Evolution Across Stages
| Stage | Status at Stage |
|---|---|
| `S02` | `IMPLICIT` |
| `S06` | `REJECTED_AS_ELASTIC_MODEL` |
| `S10` | `FORMALIZED_AS_H0a` |
| `S12` | `REFUTED_WHEN_TRANSFORMATION_ACTIVE` |
| `S16` | `REFUTED` |

- **Provenance:** `{"source_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md", "commit": "3a216d680b6e5d4c263121afee0577ac86e530ac"}`

---

### H0b: The bending response, stiffness variation, and energy dissipation of a pressure-confined NiTi wire bundle can be predicted by combining existing transformation-aware NiTi constitutive models (e.g., Auricchio-Petrini or Graesser) with standard frictional contact mechanics (Coulomb stick-slip), treating confining pressure p(t) as an external boundary condition, using independently calibrated material and friction parameters.

- **Hypothesis Type:** `established_physics_null`
- **Role in Logic Architecture:** Secondary / Competitor null hypothesis (established continuum mechanics)
- **Historical Origin:** Formulated by Astra critique G01 and Stage 3 remediation W07 to prevent premature claims of novelty. (Commit: `3a216d680b6e5d4c263121afee0577ac86e530ac`)
- **Canonical Status:** `NOT_FALSIFIED` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Logical Relation to Other Hypotheses:** Direct alternative to H1. Unless H0b is falsified under locked calibration, H1 cannot be claimed.

#### Evidence Analysis
- **Evidence Supporting:** Vahidi et al. (2022) successfully combined Auricchio UMAT with Coulomb contact in Abaqus to predict NiTi cable hysteresis. Barsi et al. (2025) and Tjahjanto et al. (2017) demonstrated friction beam formulation under radial pressure. Standard contact mechanics readily admits time-varying normal tractions p(t).
- **Evidence Challenging:** No repository study has yet performed a full forward prediction under actively varying dynamic pressure p(t) on NiTi bundles.
- **What Would Falsify It:** A statistically significant and systematic discrepancy between H0b forward predictions (with locked, independently measured parameters) and experimental moment-curvature data under diverse pressure paths p(t) that exceeds experimental and geometric uncertainty.
- **What Would Support It:** Demonstrating that an Abaqus Auricchio+Coulomb FEA model or an OpenSees fiber model with locked single-wire parameters predicts the measured moment-curvature curves within experimental error bands.
- **Remaining Uncertainty:** Untested on actively pressure-confined soft robotic bundles; remains a live, scientifically plausible hypothesis.

#### Historical Evolution Across Stages
| Stage | Status at Stage |
|---|---|
| `S02` | `UNFORMULATED` |
| `S06` | `OVERLOOKED_IN_AUDIT` |
| `S10` | `INTRODUCED_BY_ASTRA` |
| `S12` | `ESTABLISHED_AS_COMPETITOR_NULL` |
| `S16` | `NOT_FALSIFIED` |

- **Provenance:** `{"source_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md", "commit": "3a216d680b6e5d4c263121afee0577ac86e530ac"}`

---

### H1: A genuinely distinct coupled mechanics formulation is required, wherein local contact stress generated by confinement pressure directly alters martensitic transformation kinetics or vice-versa, producing emergent flexural behavior that cannot be predicted by H0b even with independently calibrated parameters.

- **Hypothesis Type:** `novel_mechanics_alternative`
- **Role in Logic Architecture:** Alternative hypothesis (research novelty candidate)
- **Historical Origin:** Initially presumed as the implicit justification for MP1-V001 pivot; formalized and bounded by Astra critique G01 and Stage 3 remediation W07. (Commit: `3a216d680b6e5d4c263121afee0577ac86e530ac`)
- **Canonical Status:** `INSUFFICIENT` | **Evidence Status:** `VERIFIED` | **Confidence:** `high`
- **Logical Relation to Other Hypotheses:** Cannot be inferred from rejection of H0a. Can only be supported if H0b is directly falsified.

#### Evidence Analysis
- **Evidence Supporting:** None in the repository full-text evidence base that mandates a new governing equation beyond H0b.
- **Evidence Challenging:** Existing models (Carboni 2016, Vahidi 2022) predict coupled behavior using standard continuum mechanics and separate friction + transformation equations without a micro-coupling term.
- **What Would Falsify It:** Experimental confirmation that H0b predictions match physical bundle response within measurement uncertainty across all pressure levels.
- **What Would Support It:** Empirical demonstration that under locked single-wire and flat-friction calibration, measured bundle bending exhibits residual stiffness or hysteresis anomalies that require an explicit cross-coupling term (e.g., normal pressure shifting transformation stress or phase fraction altering local friction coefficient).
- **Remaining Uncertainty:** Currently supported by zero direct evidence in repository literature; highly speculative pending definitive experimental tests.

#### Historical Evolution Across Stages
| Stage | Status at Stage |
|---|---|
| `S02` | `IMPLICIT_PRESUMPTION` |
| `S06` | `UNCRITICALLY_ASSERED` |
| `S10` | `DEMOTED_TO_UNPROVEN_ALTERNATIVE` |
| `S12` | `CLASSIFIED_AS_INSUFFICIENT_EVIDENCE` |
| `S16` | `INSUFFICIENT` |

- **Provenance:** `{"source_file": "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md", "commit": "3a216d680b6e5d4c263121afee0577ac86e530ac"}`

---
