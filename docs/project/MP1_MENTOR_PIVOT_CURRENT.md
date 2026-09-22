# MP1 — Mentor-Pivot Current Handoff

> **Status:** MP1-V001 COMPLETE — next round is MP1-V002 targeted citation chasing.  
> **Important:** the existing D1/M1 thesis remains preserved and is NOT replaced unless MP1 survives falsification and a final adjudication explicitly selects it.

## Mentor-proposed architecture

```text
superelastic NiTi / metal wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven syringe/piston pressure source
```

## MP1-V001 formal result

```text
STATUS      = PIVOT_TO_MECHANICS_CORE
CONFIDENCE  = high
```

Canonical result:

- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md`

### Closed / substantially pre-empted claims

- C1 — wire/fiber jamming for variable stiffness: **closed**
- C2 — positive-pressure jamming for variable stiffness: **closed**
- C3 — SMA + jamming in one variable-stiffness device: **closed**
- C4 — onboard/compact pressure source for jamming: **closed**
- C8 — SMA-driven syringe/piston specifically powering jamming pressure: **substantially pre-empted** and high implementation-only novelty risk

### Surviving mechanics core in the supplied corpus

- C5 — superelastic NiTi wires themselves as the frictional jamming medium: **open in supplied corpus**
- C6 — positive-pressure confinement of a superelastic NiTi wire bundle: **open in supplied corpus**
- C7 — coupling among NiTi superelastic response, inter-wire slip/friction, pressure and bending stiffness: **open in supplied corpus**

The surviving contribution is therefore NOT a component-combination claim.

## Current scientific core

The strongest provisional research question is:

> How do positive confining pressure, inter-wire slip/friction, and superelastic NiTi response interact to determine the bending stiffness and hysteresis of a NiTi wire bundle?

A stricter falsification form is:

> Does a superelastic NiTi wire bundle exhibit pressure- and curvature-dependent stick/slip and bending behavior that cannot be explained by an existing elastic-fiber Coulomb-jamming model using only substituted elastic modulus and friction parameters?

If the answer is no, the MP1 mechanics pivot should be killed.

## Immediate next round — MP1-V002

Purpose:

> Attempt to kill C5-C7 through targeted backward/forward citation chasing without reopening broad keyword searching.

### T1 — NiTi as actual jamming medium

Find prior work where:

```text
superelastic / NiTi / Nitinol metallic wires
→ form the bundle itself
→ contact/slip against one another
→ friction is intentionally modulated
→ bundle stiffness changes
```

### T2 — positive-pressure confinement of metallic/NiTi wire bundle

Find prior work where:

```text
positive/internal/confining pressure
→ radially or transversely compresses a metallic wire bundle
→ increases inter-wire normal force/friction
→ changes bending/torsional/axial stiffness
```

### T3 — coupled NiTi superelasticity + inter-wire friction

Find models or experiments coupling:

- stress-induced martensitic transformation / superelastic plateau;
- hysteresis / recoverable strain;
- wire-wire contact;
- inter-wire slip/friction;
- confinement pressure;
- structural/bending stiffness.

## Citation anchors

Start from the exact papers named by MP1-V001:

1. Bai et al. 2022 — `10.3390/app12073582`
2. Liu et al. 2021 — `10.1109/LRA.2021.3097255`
3. Zhang & Yao 2026 — `10.5194/ms-17-481-2026`
4. Takashima et al. 2022 — `10.20965/jrm.2022.p0466`
5. Matsumoto et al. 2024 — `10.1299/mej.24-00130`
6. Wang et al. 2024 — `10.1108/IR-11-2023-0305`

Primary emphasis:

- T1: Bai 2022 + Zhang & Yao 2026
- T2: Liu 2021 + Zhang & Yao 2026
- T3: Zhang & Yao 2026 + Takashima 2022 + Matsumoto 2024 + Wang 2024

## MP1-V002 inclusion rule

Register a new paper under MP1-V002 only if title/abstract/full text provides a concrete mechanics threat to T1/T2/T3.

Do NOT ingest generic:

- SMA actuator papers;
- generic cable friction papers;
- generic jamming reviews;
- robot papers that merely contain NiTi wires.

## Search-stop rule

Stop MP1-V002 when:

1. backward references of the strongest T1/T2/T3 anchors have been screened;
2. forward citations of those anchors have been screened through the current search date;
3. no named high-threat source remains unresolved.

Possible V002 outcomes:

- `FALSIFIED`
- `SUBSTANTIALLY_NARROWED`
- `SURVIVES_TARGETED_CITATION_CHASE`
- `INCONCLUSIVE`

## Current guardrail

Do not treat:

- a different wire material;
- a different pump;
- a syringe;
- a different robot platform;
- a compact package

as scientific novelty by themselves.

The mechanics pivot survives only if NiTi superelasticity changes the pressure-dependent contact/slip/bending mechanics in a way not reducible to parameter substitution in existing elastic-fiber models.

## Canonical files

- `docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md`
- `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
- `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `outputs/verification/MP1-V002/README.md`

## Immediate action

Perform only the targeted backward/forward citation screening for T1-T3. Do not begin MP1-V003 and do not change the official D1/M1 thesis yet.
