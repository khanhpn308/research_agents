# MP1 — MENTOR PIVOT CURRENT STATE

> **Updated:** 2026-09-26  
> **Canonical current MP1 execution package:** `outputs/execution/MP1-V002/W2/`  
> **Fast-start:** `docs/project/CURRENT_EXECUTION_SNAPSHOT.md`

## 1. Why MP1 exists

Mentor proposed a direction combining a superelastic NiTi/metallic wire bundle, positive confinement pressure, inter-wire frictional jamming, variable bending stiffness, and optional SMA/piston pressure actuation.

The project did not reject or accept the idea by intuition. It decomposed the architecture and repeatedly attacked it with prior art and mechanics tests.

## 2. Historical lineage

MP1-V001 removed broad architecture novelty from C1-C4/C8 and forced a pivot to mechanics core.

MP1-V002 then tested the narrowed mechanics core using full-text evidence, Astra critique/remediation, citation chasing and final adjudication.

Historical citation result remains:

```text
15/15 citation directions screened
stop condition satisfied
direct kill not found in protocol
```

The surviving question was narrowed to pressure-controlled NiTi-bundle bending mechanics and model discrimination against H0b.

## 3. Corrected hypothesis structure

```text
H0a = naive constant-modulus substitution
      REFUTED in transformation-active regime

H0b = existing transformation-aware NiTi constitutive model
      + Coulomb/contact mechanics
      NOT FALSIFIED / live competitor

H1  = genuinely new constitutive-contact coupling
      INSUFFICIENT EVIDENCE
```

Logical guardrail:

```text
H0a false != H1 true
```

## 4. W02 closeout — newest MP1 state

The later W02 workflow was incorrectly implemented as a mandatory W2-01→W2-12 chain. That architecture has been corrected.

```text
W2-01...W2-09 = preserved historical subruns
W2-10...W2-12 = not executed
old chain = SUPERSEDED_BY_W02_CLOSEOUT
W02 = COMPLETE
```

Canonical closeout is under:

`outputs/execution/MP1-V002/W2/`

Astra W2-09 findings were incorporated rather than rerun.

QA:

```text
claim reconciliation = PASS
target reconciliation = PASS
hypothesis reconciliation = PASS
K1-K9 reconciliation = PASS
provenance = PASS
```

## 5. Current MP1 candidate

The surviving candidate is not "SMA + jamming" novelty.

It is a conditional model-discrimination question:

> Under a declared experimentally accessible range where inter-wire slip and stress-induced NiTi transformation coexist, can an established transformation-aware NiTi constitutive + Coulomb-contact model H0b, calibrated independently and locked before held-out validation, predict pressure-dependent bending response and local observables, or is an additional coupling model H1 required?

Status:

```text
candidate = CONDITIONAL
scientific gate = BLOCKED
blocking gaps = 8
unresolved K-tests = K2,K3,K6,K7,K9
```

## 6. Why the gate is still blocked

The central unresolved risks are H0b sufficiency, mechanism identifiability, pressure-to-contact-force mapping, parameter compensation, coexistence feasibility, thermal/history confounding, adequacy of existing cable/contact formulations and local-observable feasibility.

Thus MP1 has not been scientifically killed, but it is not authorized to claim final novelty survival.

## 7. Exact next action

```text
MP1-WR1
Workflow Reconciliation & Next-Stage Routing

model = GPT-6 Sol
reasoning = High
```

WR1 must consume the W02 closeout and design the new execution graph. It must not revive the superseded W2-10/W2-12 chain.

No new broad search. No new Astra run at this step. No final novelty adjudication.

## 8. Mentor-facing use

When the mentor-facing report is eventually written, MP1 must be presented fairly:

- broad component-combination novelty was pre-empted;
- a narrow mechanics/model-discrimination question survived;
- that question remains conditional because decisive feasibility/identifiability tests are unresolved;
- the workflow treated mentor's idea as a serious scientific alternative rather than dismissing it.

The final D1-vs-MP1 comparison remains pending in the current workstream.
