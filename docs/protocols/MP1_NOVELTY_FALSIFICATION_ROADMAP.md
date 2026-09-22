# MP1 — Mentor-Pivot Novelty Falsification Roadmap

> **Status:** active candidate audit; the existing D1/M1 thesis is NOT replaced yet.
> **Purpose:** test the mentor-proposed mechanism adversarially before changing the registered thesis direction.

## Candidate architecture

```text
superelastic NiTi / metal wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional compact SMA-driven syringe/piston pressure source
```

The scientific core must not be phrased as merely "SMA + jamming" or "positive-pressure jamming"; both have prior art.

## Current novelty map before formal repository audit

Broad claims already treated as unsafe from the collected full texts:

- wire/fiber jamming;
- positive-pressure jamming;
- positive-pressure fiber jamming;
- SMA + jamming in one device;
- compact/onboard pumping for jamming;
- SMA-driven pumping / fluid-pressure generation;
- piston-driven mechanical jamming;
- NiTi wires used as tendons or structural elements inside a jamming robot.

Candidate claims still requiring targeted falsification:

1. **T1 — NiTi-as-jamming-medium:** superelastic NiTi wires themselves form the frictional jamming bundle.
2. **T2 — positive-pressure NiTi bundle:** positive/internal pressure directly confines a metallic/NiTi wire bundle to tune inter-wire friction and bending stiffness.
3. **T3 — coupled mechanics:** superelastic phase transformation/hysteresis interacts materially with inter-wire slip/friction and pressure-controlled bundle stiffness.
4. **T4 — SMA pressure-source integration:** an SMA-driven syringe/piston specifically powers the jamming pressure source. This is secondary because broad SMA pumping already exists.

## Round structure

### MP1-V001 — Core prior-art architecture audit

Ingest the already-collected high-threat full texts and answer:

- which broad claims are closed;
- whether T1/T2/T3 are directly or substantially pre-empted;
- whether the remaining contribution is a scientific mechanics question or only an actuator/material substitution;
- which exact references/citations must be chased next.

Possible outcomes:

- `KILL_MP1`
- `PIVOT_TO_MECHANICS_CORE`
- `SURVIVES_CORE_CORPUS`
- `INCONCLUSIVE`

### MP1-V002 — Targeted citation chasing

Run only if T1/T2/T3 survive MP1-V001.

Search backward and forward citations around the strongest lineages, especially:

- Bai et al. 2022 — wire jamming;
- Zhang & Yao 2026 — positive-pressure fiber jamming;
- Wang et al. 2024 — piston-like particle jamming;
- Takashima et al. 2022/2024/2026 — SMA + jamming;
- any exact metallic-wire / wire-bundle contact source named by these papers.

The target questions are narrowly defined in:
`docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`.

### MP1-V003 — Pressure-source integration audit

Run only if the mentor intends the SMA-driven syringe/piston to be a thesis contribution rather than an implementation detail.

Question:

> Does the exact integrated architecture create a defensible scientific contribution beyond known SMA pumps and known onboard jamming pumps?

Do not run V003 merely to preserve novelty if the mechanics core has already been killed.

### MP1-V004 — Final direction adjudication

Compare:

- surviving MP1 mechanics contribution;
- feasibility, including achievable pressure, heating/cooling rate, NiTi fatigue/hysteresis, wire contact/friction, and experimental complexity;
- the already-defended D1/M1 validity-assessment direction.

This final round decides whether to:

- keep the existing D1/M1 thesis;
- pivot to MP1;
- narrow MP1;
- reject MP1.

## Search-stop rule

Do not return to broad keyword searching after MP1-V001.

Continue only when:

- a named high-threat source appears;
- a backward/forward citation is mechanically close to T1/T2/T3;
- the formal audit names a missing evidence class.

## Scientific guardrail

A different material, actuator, syringe, geometry, or robot platform is not enough by itself.

The preferred surviving contribution should be expressible as a falsifiable mechanics question, for example:

> How do positive confining pressure, inter-wire slip/friction, and superelastic NiTi response interact to determine the bending stiffness and hysteresis of a NiTi wire bundle?

This wording is a hypothesis for audit, not a novelty claim.
