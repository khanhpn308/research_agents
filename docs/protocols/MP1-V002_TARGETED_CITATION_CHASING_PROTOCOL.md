# MP1-V002 — Targeted Citation-Chasing Protocol

> **Run condition:** only after MP1-V001 formally shows that C5/C6/C7 remain open or unresolved.
> **Purpose:** attempt to kill the surviving mechanics claim without reopening broad searching.

## Targets

### T1 — NiTi as the actual jamming medium

Find prior work where:

```text
superelastic / NiTi / Nitinol metallic wires
→ form the bundle itself
→ contact/slip against one another
→ friction is intentionally modulated
→ bundle stiffness changes
```

Do not count a paper merely because NiTi tendons pass through a granular or layer-jamming structure.

### T2 — Positive-pressure confinement of metallic/NiTi wire bundle

Find prior work where:

```text
positive/internal/confining pressure
→ radially or transversely compresses a metallic wire bundle
→ increases inter-wire normal force/friction
→ changes bending/torsional/axial stiffness
```

### T3 — Coupled NiTi superelasticity + wire friction/jamming

Find work that treats or experimentally demonstrates material coupling involving:

- stress-induced martensitic transformation / superelastic plateau;
- hysteresis / recoverable strain;
- wire-wire contact;
- inter-wire slip/friction;
- confining pressure;
- structural stiffness.

## Citation anchors

Start citation chasing from:

- Bai et al. 2022 — wire jamming;
- Zhang & Yao 2026 — positive-pressure fiber jamming;
- Wang et al. 2024 — piston-like particle jamming;
- Takashima et al. 2022 and later follow-ups — SMA + jamming;
- any metallic-wire, cable, rope, strand or bundle mechanics sources named by those papers.

## Search vocabulary for citation-screening only

Use synonyms to avoid missing the same mechanics under different labels:

```text
NiTi / Nitinol / superelastic alloy
wire bundle / wire rope / strand / cable / metallic fiber
inter-wire friction / interfilament friction / contact friction
confining pressure / radial compression / transverse pressure
slip / stick-slip / locking / jamming / frictional stiffening
bending stiffness / flexural rigidity / torsional stiffness
```

## Inclusion rule

Include a paper in MP1-V002 only when title/abstract/full text provides a concrete mechanics threat to T1/T2/T3.

Generic SMA actuators, generic cable friction, or generic jamming reviews are not sufficient.

## Stop condition

Stop when both are true:

1. backward references of the strongest T1/T2/T3 papers have been screened; and
2. forward citations of the core anchors have been screened through the current search date;

and no new named high-threat source remains unresolved.

Possible final outcomes after V002:

- `FALSIFIED`
- `SUBSTANTIALLY_NARROWED`
- `SURVIVES_TARGETED_CITATION_CHASE`
- `INCONCLUSIVE`

Absence of a matching paper is not proof of universal novelty; it is a protocol-bounded result.


## Operational staging

### Phase A — targeted full-text threat audit

Use the currently ingested MP1-V002 full-text matrix to determine whether T1-T3 are already falsified, substantially narrowed, or still unresolved.

Run:

```bash
python -m app.ingestion.mp1_v002_targeted_threat_audit --prepare-only
python -m app.ingestion.mp1_v002_targeted_threat_audit
```

This phase is intentionally INTERIM.

Allowed outputs:

- `FALSIFIED`
- `SUBSTANTIALLY_NARROWED`
- `SURVIVES_CURRENT_FULL_TEXT_SET`
- `INCONCLUSIVE`

Except for a direct `FALSIFIED` result, this phase may not produce the final protocol outcome `SURVIVES_TARGETED_CITATION_CHASE`.

### Phase B — citation-coverage tracking

Initialize only after the interim audit:

```bash
python -m app.ingestion.mp1_v002_citation_coverage --init
```

The tracker records backward and forward citation screening separately.

A required direction is complete only when:

- it was actually screened in the stated database;
- a search date is recorded;
- the number of screened records is recorded;
- any high-threat candidates have either been resolved or remain explicitly listed.

Check progress with:

```bash
python -m app.ingestion.mp1_v002_citation_coverage --check
```

A true coverage stop condition is a protocol-bounded search stop, not proof of universal novelty.

### Pressure-role classification

For T2/T3, classify every use of pressure as one of:

1. passive contact pressure produced by geometry, helix angle, axial load, or deformation;
2. fixed preload/confinement;
3. actively varied positive/internal/transverse pressure used as an independent control variable.

Only category 3 directly supports the proposed pressure-controlled variable-stiffness mechanism.

### Parameter-substitution kill test

The surviving mechanics core should be rejected or narrowed further if the NiTi bundle response can be represented adequately by an existing elastic-fiber/contact framework using only substituted material modulus and friction parameters.

The mechanics core remains potentially distinct only if full-text evidence supports a material coupling in which NiTi transformation/hysteresis materially changes contact, slip, or pressure-dependent structural stiffness beyond simple parameter replacement.
