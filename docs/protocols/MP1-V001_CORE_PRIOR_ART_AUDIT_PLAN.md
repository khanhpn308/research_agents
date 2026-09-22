# MP1-V001 — Core Prior-Art Architecture Audit Plan

> **Status:** SETUP ONLY — papers are not yet registered under MP1-V001.
> **Role:** first formal falsification round for the mentor-proposed direction.

## Candidate under attack

```text
positive-pressure frictional jamming
of a superelastic NiTi wire bundle
with an optional compact SMA-driven syringe/piston pressure source
```

The current official D1/M1 thesis remains preserved while MP1 is audited.

## Core full-text corpus to register

Register the high-threat papers already collected locally. Recommended core set:

1. Liu et al. 2021 — positive-pressure jamming.
2. Bai et al. 2022 — wire jamming.
3. Huynh et al. 2022 — micropump-activated jamming.
4. Takashima et al. 2022 — SMA + granular jamming original mechanism.
5. Takashima et al. 2024 — motion evaluation of SMA + jamming link.
6. Zhang & Yao 2026 — positive-pressure fiber jamming.
7. Takashima et al. 2026 — later SMA + jamming application.
8. Pierce & Mascaro 2013 — SMA robotic pump.
9. Kotb et al. 2021 — NiTi SMA capsule micropump.
10. Wang et al. 2024 — piston-like particle jamming.

Optional but useful:
- Matsumoto et al. 2024 — R-phase / Ti-Ni recovery behavior in the Takashima lineage.

## Claim audit

The model must independently classify each claim:

### C1
Wire/fiber jamming for variable stiffness is novel.

### C2
Positive-pressure jamming for variable stiffness is novel.

### C3
SMA and jamming in the same variable-stiffness device is novel.

### C4
An onboard/compact pressure source for jamming is novel.

### C5
Superelastic NiTi wires themselves as the frictional jamming medium remain open.

### C6
Positive-pressure confinement of a superelastic NiTi wire bundle remains open.

### C7
Coupling among NiTi superelastic response, inter-wire slip/friction, pressure and bending stiffness remains open.

### C8
SMA-driven syringe/piston specifically powering the jamming pressure remains open.

For C1-C4, a closed result is expected from the currently known corpus, but the audit must decide from ingested evidence rather than this expectation.

## Mandatory distinction

The audit must distinguish:

```text
NiTi wires present in a jamming robot
!=
NiTi wires are the jamming medium
```

and:

```text
mechanical piston compression of particles
!=
fluid pressure radially confining a NiTi wire bundle
```

and:

```text
SMA pump exists
!=
SMA-powered jamming architecture is a strong scientific novelty
```

## Kill logic

`KILL_MP1` is justified if either:

1. supplied prior work directly/substantially establishes T1 + T2 + the relevant stiffness mechanics; or
2. after removing known components, the only remaining difference is an implementation substitution (for example pump technology/material choice) without a defensible new mechanics question.

`PIVOT_TO_MECHANICS_CORE` is appropriate when the broad architecture is heavily pre-empted but C5-C7 remain genuinely open and scientifically meaningful.

`SURVIVES_CORE_CORPUS` requires that no fatal direct prior art is established for the core C5-C7 claims, while still acknowledging that novelty is not proven until citation chasing is completed.

## Local ingestion setup

Create the inbox:

```bash
mkdir -p data/inbox/verification_pending/MP1-V001
```

Put the selected PDFs there, then remove Windows metadata:

```bash
find data/inbox/verification_pending/MP1-V001 \
  -name '*:Zone.Identifier' \
  -delete
```

Register each PDF:

```bash
for f in data/inbox/verification_pending/MP1-V001/*.pdf; do
  python -m app.ingestion.add_paper "$f" \
    --type verification \
    --verification-id MP1-V001 \
    --reason "Core prior-art full text for adversarial audit of mentor-proposed superelastic NiTi wire jamming / positive-pressure architecture."
done
```

Do not skip the screening gate. For every printed `paper_id`:

```bash
python -m app.ingestion.screen_paper \
  --id <PAPER_ID> \
  --decision include \
  --reason "High-relevance full-text prior art for MP1-V001 architecture and novelty falsification."
```

Then ingest and validate:

```bash
python -m app.ingestion.ingest_papers --limit 20
python -m app.ingestion.validate_evidence
python -m app.ingestion.build_verification_matrix \
  --verification-id MP1-V001
```

Prepare the formal audit:

```bash
set -a
source .env
set +a

python -m app.ingestion.mp1_v001_core_prior_art_audit \
  --prepare-only
```

If preparation passes:

```bash
python -m app.ingestion.mp1_v001_core_prior_art_audit
```

## Expected outputs

```text
outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json
outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md
outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT_raw.json
outputs/verification/MP1-V001/core_prior_art_runs/<timestamp>/
```

Do not manually create a verdict before the evidence matrix exists.
