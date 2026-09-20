# KNOWN_ISSUES.md

## 1. Linux `Argument list too long`

### Symptom

```text
OSError: [Errno 7] Argument list too long
```

### Cause

Large prompts were passed directly as command-line arguments.

### Resolution

The Codex provider was modified so large prompts are passed through a safer mechanism rather than as a huge argv payload.

Large-prompt smoke testing succeeded.

---

## 2. Strict JSON Schema rejection

### Symptom

Structured output schema rejected because:

```text
additionalProperties is required to be supplied and to be false
```

### Resolution

All object schemas must use:

```json
"additionalProperties": false
```

A recursive strict-schema helper was introduced for nested schemas.

---

## 3. `provisional_recommendation` mismatch

### Symptom

```text
provisional_recommendation does not match a valid direction_id
```

### Cause

The model returned a title / descriptive string rather than an exact ID such as `D1`.

### Resolution

Normalize against:
1. exact ID
2. embedded ID
3. exact title
4. explicit rank-1 candidate

Otherwise fail closed.

---

## 4. Preserve raw expensive-model output before validation

### Problem

A model call could succeed but post-processing validation could fail, forcing an unnecessary rerun.

### Resolution

Save raw output first, then parse/validate.

Current pattern:

```text
model output
→ save raw
→ parse JSON
→ validate
→ save normalized output
```

---

## 5. Antigravity empty-content transient failures

### Symptom

```text
Antigravity completed successfully but returned empty content
```

### Observed behavior

Some runs succeeded on retry.

### Current handling

Retry carefully for idempotent operations.

### Recommended future improvement

Provider-level retry + backoff + diagnostics.

---

## 6. Environment variable naming

Use:

```text
CODEX_RESEARCH_EFFORT
```

Avoid reintroducing:

```text
CODEX_RESEARCH_REASONING
```

unless the whole codebase is intentionally migrated.

---

## 7. `DRY_RUN=true`

`DRY_RUN=true` can remain enabled while direct research scripts call Codex / Antigravity explicitly.

Do not assume changing `DRY_RUN` is required for:
- candidate_directions
- critique_directions
- final_adjudication
- verification scripts

Check each script's actual call path.

---

## 8. Verification papers require a verification ID

For:

```bash
--type verification
```

the system requires:

```bash
--verification-id ...
```

Example:

```bash
python -m app.ingestion.add_paper   "paper.pdf"   --type verification   --verification-id D1-V002
```

---

## 9. Screening gate before ingestion

New verification papers may appear as:

```text
screening_status: pending
ingestion_status: not_eligible
```

This is expected.

They must be screened before ingestion.

---

## 10. Deduplication limitation

SHA256 detects identical files, but not necessarily the same paper downloaded in a different PDF version.

Recommended future deduplication:

```text
SHA256
+
DOI
+
normalized title
```

---

## 11. Discovery and verification corpora must remain separate

Do not blindly rebuild the main discovery matrix with new verification papers and overwrite the 54-paper discovery state.

Completed discovery state is frozen under:

```text
outputs/discovery_snapshot/
```

Verification rounds remain under:

```text
outputs/verification/
```

---

## 12. Never overwrite completed verification rounds

`D1-V001` is historical evidence.

New evidence belongs in a new round such as:

```text
D1-V002
```

---

## 13. Current scientific risk

The current pivot P1 may already be substantially addressed by 2025 continuum-model papers.

Do not spend time polishing P1 until those papers are screened and ingested.
