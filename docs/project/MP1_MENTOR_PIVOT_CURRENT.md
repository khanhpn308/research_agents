# MP1 — Mentor-Pivot Current Handoff

> **Status:** ACTIVE CANDIDATE AUDIT.  
> **Important:** the existing D1/M1 thesis is preserved and is NOT replaced unless MP1 survives falsification and a final adjudication explicitly selects it.

## Mentor-proposed architecture

```text
superelastic NiTi / metal wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven syringe/piston pressure source
```

## Broad claims already unsafe

The current full-text corpus shows that the following cannot be treated as novel by themselves:

- wire/fiber jamming;
- positive-pressure jamming;
- positive-pressure fiber jamming;
- SMA + jamming in one device;
- NiTi wires/tendons inside a jamming robot;
- compact/onboard pressure source for jamming;
- SMA-driven pumping / pressure generation;
- piston-driven mechanical jamming.

## Surviving hypotheses to falsify

### T1 — NiTi as actual jamming medium

Superelastic NiTi wires themselves form the frictional bundle and are intentionally jammed by wire-wire contact/slip.

### T2 — Positive-pressure confinement of NiTi bundle

Positive/internal/confining pressure radially or transversely compresses a metallic/NiTi bundle, increases inter-wire normal force/friction, and changes bending stiffness.

### T3 — Coupled mechanics

Superelastic NiTi material response interacts materially with:

- wire-wire contact;
- inter-wire slip/friction;
- pressure;
- hysteresis;
- bending stiffness.

### T4 — SMA pressure-source integration

An SMA-driven syringe/piston specifically powers the jamming pressure source.

T4 is secondary because SMA-driven pumping and compact jamming pumps already exist. It should not carry the thesis novelty by itself.

## MP1-V001 — current next round

Purpose:

> Formal full-text prior-art architecture audit using the already-collected high-threat corpus.

Core corpus:

1. Liu et al. 2021 — positive-pressure jamming.
2. Bai et al. 2022 — wire jamming.
3. Huynh et al. 2022 — micropump-activated jamming.
4. Takashima et al. 2022 — SMA + granular jamming original mechanism.
5. Takashima et al. 2024 — motion evaluation of SMA + jamming.
6. Zhang & Yao 2026 — positive-pressure fiber jamming.
7. Takashima et al. 2026 — later SMA + jamming application.
8. Pierce & Mascaro 2013 — SMA robotic pump.
9. Kotb et al. 2021 — NiTi SMA capsule micropump.
10. Wang et al. 2024 — piston-like particle jamming.
11. Matsumoto et al. 2024 — optional but recommended Ti-Ni/R-phase paper in the Takashima lineage.

Expected V001 outcomes:

- `KILL_MP1`
- `PIVOT_TO_MECHANICS_CORE`
- `SURVIVES_CORE_CORPUS`
- `INCONCLUSIVE`

## MP1-V002 — only after V001

If T1/T2/T3 survive, perform targeted backward/forward citation chasing around:

- Bai et al. 2022;
- Zhang & Yao 2026;
- Wang et al. 2024;
- Takashima 2022/2024/2026;
- any metallic-wire / cable / rope / strand sources explicitly named by those papers.

Do not reopen broad keyword searching.

## Current scientific guardrail

A different material, pump, syringe, geometry, or robot platform is not enough by itself.

A stronger surviving research question would look like:

> How do positive confining pressure, inter-wire slip/friction, and superelastic NiTi response interact to determine bending stiffness and hysteresis of a NiTi wire bundle?

This is a hypothesis for falsification, not a novelty claim.

## Canonical files

- `docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md`
- `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
- `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`
- `app/ingestion/mp1_v001_core_prior_art_audit.py`
- `outputs/verification/MP1-V001/README.md`

## Immediate next action

1. Register the collected PDFs under `MP1-V001`.
2. Screen them as included.
3. Ingest and validate evidence.
4. Build the MP1-V001 verification matrix.
5. Run `mp1_v001_core_prior_art_audit --prepare-only`.
6. If preparation passes, run the formal audit.
7. Only then decide whether MP1-V002 is necessary.
