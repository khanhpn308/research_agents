# D1/M1 Novelty Reconstruction — Master Execution Plan

**Scope:** D1/M1 novelty only  
**Status:** Plan only; no full audit executed by this artifact  
**Repository HEAD inspected:** 0ade68e73d93c38618b366a000ac7a01215a3936  
**Current selected direction:** D1_M1  
**Current decision:** LOCK_WITH_FEASIBILITY_GATE  
**Current model:** Zhang et al., *A continuum-based model for a layer jamming beam*  
**DOI:** 10.5194/ms-16-821-2025  
**Architecture:** M → R → E  
**Language:** schemas and keys in English; research explanation in Vietnamese.

> The worktree was dirty when this plan was prepared. Any execution must first create a provenance-locked snapshot and distinguish HEAD files from working-tree edits.

## A. Mục tiêu Stage 1

Tái dựng đầy đủ lịch sử hình thành, thu hẹp và phản chứng của D1/M1; xác định phần nào đã bị prior art bao phủ, phần nào còn có thể bảo vệ, và bằng chứng nào đủ để hỗ trợ kết luận.

Kết luận được phép là KEEP, NARROW, PIVOT, REJECT, hoặc UNRESOLVED. Không được mặc định rằng D1 là novel. Kết luận mạnh nhất thường phải được giới hạn bằng câu:

> not directly pre-empted within the audited evidence scope

## B. Phân rã bài toán novelty

| Tầng kiểm tra | Câu hỏi |
|---|---|
| Historical identity | D1 ban đầu là gì và thay đổi thế nào? |
| Claim lineage | Claim nào bị bác bỏ, thu hẹp, reformulate hoặc sống sót? |
| Prior-art coverage | Layer-jamming, continuum, homogenization, friction, slip, contact và validation đã được giải quyết đến đâu? |
| Exact overlap | Có công trình nào đã thực hiện tương đương specified reduced model → interface/full-layer reference → independent experiment chưa? |
| Validity contribution | Có ai đã lập validity/breakdown map bằng tolerance khai báo trước chưa? |
| Mechanism contribution | Có ai đã giải thích failure bằng pressure redistribution, contact, slip hoặc separation chưa? |
| Objection A | Layer-jamming modeling đã làm nhiều lần chưa? |
| Objection B | Layer-jamming models đã được validation nhiều lần chưa? |
| Objection C | Exact current D1/M1 contribution đã được làm chưa? |
| Novelty category | Novelty thuộc system, mechanism, model, method, validation, scientific question hay workflow? |
| Evidence strength | Claim dựa trên full text, metadata, inference hay hypothesis? |
| Scope | Kết luận đúng trong corpus và protocol nào? |

A hoặc B đúng không tự động chứng minh C đúng; nhưng C cũng không được mặc định là chưa có.

## C. Repository evidence map

### Canonical current state

- docs/project/PROJECT_HANDOFF_CURRENT.md
- docs/project/RESEARCH_STATE.md
- docs/project/research_state.json
- docs/project/RESEARCH_LOG.md
- outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json

### Research design

- docs/research_design/M1_RESEARCH_ARCHITECTURE.md
- docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md
- docs/research_design/EXACT_MODEL_SELECTION.md
- docs/research_design/LAYER_JAMMING_MODEL_COMPARISON.md

Các file này phải phân biệt điều Zhang et al. thực sự công bố, điều repository suy luận, điều chỉ là research-design proposal, và điều còn chưa khóa như reference formulation, tolerance, output và apparatus.

### Historical D1 rounds

Đọc nội dung thực tế, không suy luận từ filename:

- outputs/verification/D1-V001/
- outputs/verification/D1-V002/
- outputs/verification/D1-V003/
- outputs/verification/D1-V004/
- outputs/verification/D1-V005/
- outputs/verification/D1-V006/
- outputs/verification/D1-V007/
- outputs/verification/D1-V008/
- outputs/verification/D1-V009/

Mỗi round phải đọc canonical JSON/Markdown, verification matrix, prompt và provenance khi có.

### Original evidence

- data/evidence/
- data/papers/
- papers/
- data/search_exports/
- verification matrices và source manifests.

Evidence status bắt buộc:

~~~text
VERIFIED_FULL_TEXT
METADATA_ONLY
INFERENCE
HYPOTHESIS
UNAVAILABLE
~~~

Không dùng MP1 artifacts làm evidence cho D1.

## D. Execution stages

### S0 — Provenance and workspace lock

- **Objective:** khóa phiên bản evidence trước khi đọc lại lịch sử.
- **Question:** dữ liệu nào thuộc HEAD và dữ liệu nào chỉ có trong dirty worktree?
- **Inputs:** Git HEAD, git status, canonical D1 files, file hashes.
- **Sources:** repository only.
- **MODEL:** GPT-6 Sol.
- **REASONING:** Medium.
- **WHY:** kiểm tra nhất quán và provenance.
- **WHY NOT ASTRA:** chưa có tranh luận khoa học cần giải.
- **Workers:** 1 coordinator.
- **Responsibilities:** tạo manifest commit, status, hash và excluded paths.
- **Outputs:** repository_manifest.json, scope_lock.json.
- **Acceptance:** mọi input có commit/path/hash; không trộn working-tree edits.
- **Failure:** canonical file chỉ tồn tại ở dirty tree hoặc hash không xác định.
- **Dependency:** none.
- **Human review:** xác nhận corpus boundary.
- **Astra:** không cần.

### S1 — Repository inventory and historical index

- **Objective:** lập chỉ mục toàn bộ D1 evidence.
- **Question:** round, artifact, source và provenance nào đang tồn tại?
- **Inputs:** D1-V001…D1-V009, research-design files, evidence registry.
- **Sources:** repository files only.
- **MODEL:** Gemini 3.8 Flash.
- **REASONING:** High.
- **WHY:** bulk extraction, indexing và provenance capture.
- **WHY NOT ASTRA:** công việc lặp lại, không cần phán đoán đắt tiền.
- **Workers:** 2 — round/artifact inventory; paper/source inventory.
- **Outputs:** d1_evidence_inventory.json, d1_round_index.json.
- **Acceptance:** không bỏ sót round; mỗi artifact có type, path, status và hash.
- **Failure:** artifact không đọc được hoặc evidence status bị suy đoán.
- **Dependency:** S0.
- **Human review:** kiểm tra inventory completeness.
- **Astra:** không cần.

### S2 — D1 lineage reconstruction

- **Objective:** tái dựng claim → threat → evidence → decision → revised claim.
- **Question:** paper hoặc source nào thực sự làm D1 thay đổi?
- **Inputs:** S1 inventory, handoff, research log, all D1 verdicts.
- **Sources:** canonical verdict JSON/MD, matrices, prompts, source provenance.
- **MODEL:** Gemini 3.8 Flash.
- **REASONING:** High.
- **WHY:** chronology extraction và structured evidence binding.
- **WHY NOT ASTRA:** chưa cần adjudicate mâu thuẫn.
- **Workers:** 3 — chronology; decision extraction; source-trigger mapping.
- **Outputs:** d1_lineage.json, d1_lineage.md.
- **Acceptance:** mỗi transition có claim_before, threat, trigger_source, effect_on_D1, decision, claim_after.
- **Failure:** transition chỉ dựa trên filename hoặc summary không có source pointer.
- **Dependency:** S1.
- **Human review:** mọi transition thay đổi claim.
- **Astra:** không cần.

### S3 — Paper-level evidence packet extraction

- **Objective:** biến từng paper có ảnh hưởng thành evidence packet có thể audit.
- **Question:** paper làm gì, dùng model/reference nào, đo output gì, có tolerance và experiment gì?
- **Inputs:** paper PDFs, evidence JSON, verification matrices, metadata.
- **Sources:** ưu tiên PDF toàn văn; metadata chỉ dùng để định danh.
- **MODEL:** Gemini 3.8 Flash.
- **REASONING:** High.
- **WHY:** đọc số lượng lớn paper và chuẩn hóa fields.
- **WHY NOT ASTRA:** không dùng Astra cho extraction hàng loạt.
- **Workers:** 4 — layer-jamming; continuum/homogenization; contact/partial-interaction; validity/validation.
- **Outputs:** evidence_packets.jsonl, paper_overlap_map.json.
- **Acceptance:** claim quan trọng có page/section hoặc locator; tách what_it_proves và what_it_does_not_prove.
- **Failure:** metadata-only packet bị ghi như full-text evidence.
- **Dependency:** S1, S2.
- **Human review:** mọi high-threat packet và ít nhất một packet mỗi family.
- **Astra:** không cần.

### S4 — Targeted prior-art threat audit

- **Objective:** kiểm tra threat có khả năng giết exact D1/M1 contribution.
- **Question:** có prior work tương đương về conceptual structure dù khác thuật ngữ không?
- **Inputs:** S2 lineage, S3 packets, named unresolved targets, citation branches.
- **Sources:** primary full text, publisher pages, authoritative metadata, forward/backward citations.
- **MODEL:** Gemini 3.8 Flash cho screening; GPT-6 Sol cho consolidation.
- **REASONING:** Flash High; Sol High.
- **WHY:** Flash lọc rộng; Sol kiểm tra conceptual equivalence và contradiction.
- **WHY NOT ASTRA:** Astra chỉ dành cho unresolved fatal ambiguity.
- **Workers:** 3 Flash workers + 1 Sol synthesizer.
- **Outputs:** prior_art_threat_matrix.json, targeted_search_log.json, unresolved_targets.json.
- **Acceptance:** mỗi target có rationale, overlap dimensions, full-text status và kill assessment.
- **Failure:** exact-phrase search được dùng như evidence of absence.
- **Dependency:** S3.
- **Human review:** mọi high-threat source.
- **Astra:** chỉ mở nếu còn mâu thuẫn sau full-text expansion.

### S5 — Claim Evolution Matrix and novelty decomposition

- **Objective:** chuyển lịch sử thành claim-level audit.
- **Question:** claim cuối cùng còn đứng ở loại novelty nào?
- **Inputs:** S2 lineage, S3 evidence packets, S4 threat matrix.
- **Sources:** verified repository evidence.
- **MODEL:** GPT-6 Sol.
- **REASONING:** High.
- **WHY:** synthesis, contradiction reconciliation và novelty-scope reasoning.
- **WHY NOT ASTRA:** chưa cần final adversarial judgment.
- **Workers:** 2 — claim-evolution synthesis; novelty-category decomposition.
- **Outputs:** claim_evolution_matrix.json, novelty_decomposition.json, prior_art_family_map.json.
- **Acceptance:** generic claims bị loại rõ; surviving claim có scope, evidence và residual threat.
- **Failure:** novelty chuyển từ model sang method/validation mà không ghi nhận.
- **Dependency:** S4.
- **Human review:** supervisor/domain review.
- **Astra:** chưa cần.

### S6 — Adversarial kill analysis

- **Objective:** cố tình đánh bại surviving D1/M1 claim.
- **Question:** bằng chứng nào đủ để chuyển verdict thành REJECT, PIVOT hoặc NARROW?
- **Inputs:** Claim Evolution Matrix, Threat Matrix, source packets, current M1 architecture.
- **Sources:** evidence đã provenance-bind.
- **MODEL:** GPT-6 Astra.
- **REASONING:** High hoặc xHigh.
- **WHY:** phát hiện fatal logical gaps, false novelty transfer và conceptual equivalence.
- **WHY NOT MORE EXPENSIVE:** Astra là tier cao nhất cần thiết; không dùng cho extraction.
- **Workers:** 1 Astra adversarial judge + 1 GPT-6 Sol pre-audit.
- **Outputs:** d1_kill_analysis.json, d1_adversarial_review.md.
- **Acceptance:** nêu exact kill condition, supporting source, missing condition, revision nếu chỉ narrow và confidence.
- **Failure:** kết luận dựa trên absence, title similarity hoặc generic analogy.
- **Dependency:** S5.
- **Human review:** bắt buộc.
- **Astra:** justified ở stage này.

### S7 — Final D1-only adjudication

- **Objective:** ban hành verdict có giới hạn phạm vi và provenance.
- **Question:** D1/M1 nên KEEP, NARROW, PIVOT, REJECT hay UNRESOLVED?
- **Inputs:** toàn bộ artifacts S0–S6.
- **Sources:** evidence có traceability.
- **MODEL:** GPT-6 Sol.
- **REASONING:** High.
- **WHY:** final synthesis phải bảo toàn uncertainty và scope.
- **WHY NOT ASTRA:** Astra đã làm adversarial kill pass; Sol tổng hợp verdict.
- **Workers:** 1 final adjudicator.
- **Outputs:** FINAL_D1_NOVELTY_ADJUDICATION.json, FINAL_D1_NOVELTY_ADJUDICATION.md, provenance_manifest.json.
- **Acceptance:** không claim universal novelty; thesis-critical statement đều trỏ tới source.
- **Failure:** còn high-threat source unresolved hoặc missing full text.
- **Dependency:** S6.
- **Human review:** final sign-off.
- **Astra:** chỉ rerun nếu còn bất đồng vật chất.

### S8 — Integrity and deliverable QA

- **Objective:** bảo đảm reviewer độc lập có thể tái lập kết quả.
- **Question:** có thể đi từ verdict về source locator và PDF không?
- **Inputs:** tất cả output S0–S7.
- **MODEL:** GPT-6 Sol.
- **REASONING:** Medium/High.
- **WHY:** schema validation, traceability và consistency checks.
- **WHY NOT ASTRA:** QA định thức.
- **Workers:** 1 QA worker.
- **Outputs:** qa_report.json, source_traceability_report.md.
- **Acceptance:** file tồn tại, non-empty, parse được, không orphan claim, không overwrite D1-V001…V009.
- **Failure:** thiếu provenance, duplicate IDs hoặc inconsistent verdict.
- **Dependency:** S7.
- **Human review:** xác nhận cuối.
- **Astra:** không cần.

## E. Model assignment and cost control

| Công việc | Model |
|---|---|
| Inventory, chronology, metadata, extraction | Gemini 3.8 Flash High |
| Cross-paper synthesis and contradiction resolution | GPT-6 Sol High |
| Adversarial novelty kill test | GPT-6 Astra High/xHigh |
| Final adjudication and QA | GPT-6 Sol High |

Cost controls:

- Không dùng Astra để đọc hàng loạt.
- Deduplicate bằng SHA256 + DOI + normalized title.
- Cache từng evidence packet.
- Chỉ gửi packet tối thiểu có source locator cho reasoning.
- Giữ raw output trước khi parse/validate.
- Chỉ mở thêm search khi có concrete_high_threat_target.
- Không tính citation count như evidence of overlap.

## F. Worker architecture

Các worker là vai trò logic; chưa dispatch worker trong nhiệm vụ lập kế hoạch này.

~~~text
Coordinator
├── Repository/Provenance Worker
├── Timeline Worker
├── Decision-Transition Worker
├── Paper Evidence Workers
│   ├── Layer-jamming
│   ├── Continuum/homogenization
│   ├── Contact/partial interaction
│   └── Validity/validation
├── Threat Screening Workers
├── GPT-6 Sol Synthesis
├── GPT-6 Astra Adversarial Judge
└── Human Review Gate
~~~

Mỗi worker ghi artifact riêng; synthesis không được xóa disagreement của worker khác.

## G. Evidence Packet schema

~~~json
{
  "claim_id": "D1-C-001",
  "paper_id": "string",
  "paper_title": "string",
  "authors": ["string"],
  "year": 2025,
  "doi": "string|null",
  "source_type": "PDF|JSON|MATRIX|REPORT|METADATA",
  "source_file": "absolute-or-repository-path",
  "evidence_status": "VERIFIED_FULL_TEXT|METADATA_ONLY|INFERENCE|HYPOTHESIS|UNAVAILABLE",
  "page_or_section": "string|null",
  "evidence_pointer": "string",
  "why_investigated": "string",
  "d1_claim_threatened": "string",
  "model_used": "string",
  "reference_used": "string",
  "variables": ["string"],
  "outputs": ["string"],
  "acceptance_criterion": "string|null",
  "validity_domain": "string|null",
  "breakdown_mechanism": "string|null",
  "what_it_proves": "string",
  "what_it_does_not_prove": "string",
  "overlap_with_d1": "string",
  "non_overlap_with_d1": "string",
  "confidence": "low|medium|high"
}
~~~

## H. Claim Evolution Matrix schema

~~~json
{
  "claim_id": "D1-C-001",
  "claim_family": "MODEL|MECHANISM|METHOD|VALIDATION|QUESTION|WORKFLOW",
  "original_claim": "string",
  "prior_art_threat": "string",
  "evidence_packet_ids": ["D1-E-001"],
  "prior_art_covers": "string",
  "prior_art_does_not_cover": "string",
  "historical_verdict": "KEEP|NARROW|REJECT|REFORMULATE|UNRESOLVED",
  "revised_claim": "string",
  "next_threat": "string",
  "final_disposition": "SURVIVES|NARROWED|KILLED|UNRESOLVED",
  "evidence_status": "VERIFIED|INFERENCE|HYPOTHESIS",
  "provenance": ["repository/path#locator"]
}
~~~

Transition schema:

~~~json
{
  "transition_id": "D1-T-001",
  "date_or_phase": "D1-V003",
  "claim_before": "string",
  "scientific_question_before": "string",
  "threat_or_problem": "string",
  "trigger_source": "D1-E-001",
  "effect_on_d1": "string",
  "decision": "KEEP|NARROW|REJECT|REFORMULATE|UNRESOLVED",
  "claim_after": "string",
  "reason_for_transition": "string"
}
~~~

## I. Prior-Art Threat Matrix schema

~~~json
{
  "threat_id": "D1-TH-001",
  "literature_family": "layer-jamming|homogenization|contact|partial-interaction|validation",
  "source_ids": ["D1-E-001"],
  "threat_level": "low|medium|high|fatal",
  "conceptual_overlap": "string",
  "requires_exact_model_match": false,
  "covers_named_reduced_model": false,
  "covers_interface_resolved_reference": false,
  "covers_output_specific_error": false,
  "uses_predeclared_tolerance": false,
  "maps_tolerance_boundary": false,
  "tests_both_sides_experimentally": false,
  "explains_failure_mechanism": false,
  "vacuum_pressure_contact_coupling": false,
  "kill_status": "KILL|NARROW_ONLY|NO_KILL|UNRESOLVED",
  "missing_evidence": ["string"],
  "recommended_action": "string"
}
~~~

## J. D1 novelty kill criteria

Một paper hoặc paper-chain có thể kill toàn bộ surviving claim nếu chứng minh được phần lớn hoặc toàn bộ chuỗi:

~~~text
specified reduced/continuum layer-jamming beam model
→ interface/full-layer or discrete frictional-contact reference
→ controlled layer-count / pressure / bending domain
→ output-specific model-form error
→ tolerance fixed before final error inspection
→ validity/breakdown boundary
→ deliberate tests on both accepted and rejected sides
→ independent experiment
→ physical explanation of failure
~~~

Các kết quả sau chỉ kill generic claims, không tự động kill exact D1/M1:

- layer jamming, continuum, homogenization, friction, slip hoặc contact đã tồn tại;
- full-layer FE hoặc physical experiment đã tồn tại;
- model-versus-experiment comparison đã tồn tại;
- percentage error hoặc tolerance từng được báo cáo;
- applicability rule không phải predeclared model-form boundary;
- framework khác có threshold nhưng không có vacuum-specific transfer và boundary-crossing experiment.

Metadata, abstract hoặc citation relationship không đủ để kill thesis-critical claim.

## K. Human-review checkpoints

1. Xác nhận chỉ D1/M1 được audit.
2. Xác nhận lineage không bị dựng lại sau khi biết kết quả.
3. Kiểm tra page/section và câu “what it proves / does not prove”.
4. Kiểm tra conceptual equivalence, không chỉ exact wording.
5. Kiểm tra tolerance được cố định trước validation.
6. Kiểm tra không dùng absence-of-evidence như evidence-of-absence.
7. Xác nhận reviewer độc lập có thể truy ngược claim về source.

## L. Stop conditions

Dừng broad search khi:

- toàn bộ named high-threat targets đã được xử lý;
- không còn unresolved high-threat source;
- không có target cụ thể mới;
- mọi claim sống sót đã được thu hẹp rõ.

Không final-lock khi:

- còn paper high-threat chưa có full text;
- M1 chưa được reconstruct;
- reference R chưa chứng minh credibility;
- tolerance được chọn sau khi xem error;
- không có output chung giữa M1, R và experiment;
- không phân biệt được model-form error với calibration error;
- không có accepted/rejected condition có uncertainty-resolved.

Nếu target không thể giải quyết, verdict phải là UNRESOLVED hoặc EVIDENCE-LIMITED.

## M. Expected D1-only deliverables

- repository_manifest.json
- d1_round_index.json
- d1_lineage.json
- d1_lineage.md
- evidence_packets.jsonl
- paper_overlap_map.json
- prior_art_threat_matrix.json
- prior_art_family_map.json
- claim_evolution_matrix.json
- novelty_decomposition.json
- d1_kill_analysis.json
- FINAL_D1_NOVELTY_ADJUDICATION.json
- FINAL_D1_NOVELTY_ADJUDICATION.md
- provenance_manifest.json
- qa_report.json
- source_traceability_report.md

Nếu cần tạo verification round mới, dùng thư mục mới như outputs/verification/D1-V010/; không ghi đè D1-V001…D1-V009.

## N. Risks that could invalidate the proof

- dirty worktree bị trộn với HEAD;
- dùng handoff summary thay cho canonical evidence;
- dùng metadata như full-text evidence;
- suy diễn novelty từ việc không tìm exact phrase;
- trộn discovery corpus với verification corpus;
- generic continuum/contact/error-threshold methodology bị trình bày như novelty;
- quên prior art về layered Cosserat/frictional continuum;
- tolerance hậu nghiệm;
- full-layer FE không thật sự resolve contact/slip;
- pressure, friction và contact pressure không được calibrate độc lập;
- experiment chỉ kiểm tra các điểm model đã dự đoán đúng;
- gọi là validated breakdown nhưng không có thử nghiệm hai phía;
- model-form error bị nhầm với parameter-fitting error;
- thiếu evidence status, confidence hoặc source locator.

## O. Current repository interpretation

Repository hiện hỗ trợ một protocol-bounded D1/M1 lock, không phải universal novelty proof. Các điểm còn phải chứng minh bằng thực thi là:

- M1 reconstruction và published-case reproduction;
- credibility của full-layer frictional-contact reference;
- shared measurable output;
- predeclared metric/tolerance;
- uncertainty budget;
- ít nhất một accepted condition và một rejected condition có thể phân biệt thực nghiệm;
- cơ chế contact/slip giải thích discrepancy.

## P. Exact recommended next action

Tạo một clean, provenance-locked execution snapshot của HEAD; sau đó chạy S0–S2 để lập inventory và tái dựng D1 lineage trước khi thu thập thêm paper nào.

Không bắt đầu bằng broad literature search. Không viết final novelty report trước khi Claim Evolution Matrix và paper-level evidence packets hoàn tất.

---

STAGE 1 SCOPE = D1 NOVELTY ONLY

MP1 ANALYSIS = NOT STARTED

D1-vs-MP1 COMPARISON = NOT STARTED
