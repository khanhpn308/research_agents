# MP1-CH2-2.3.3 — Báo cáo thực thi

## Định danh

- **TASK_ID:** MP1-CH2-2.3.3-RESEARCH-THESIS-DRAFT
- **Target:** Chương 2, Mục 2.3.3 — Kẹt lớp/tấm và kẹt hạt như nhóm so sánh
- **Bối cảnh:** HCMUT / VNU-HCM / Khoa Cơ khí / Thạc sĩ Kỹ thuật Cơ khí định hướng nghiên cứu
- **Ngôn ngữ:** Tiếng Việt

## Orchestration

- `ROOT_MODEL_REQUESTED: GPT-6.1 SOL HIGH`
- `ROOT_MODEL_ACTUAL: NOT_VERIFIED`
- `WORKERS_SPAWNED: 6 bounded tasks`
- `WORKER_TASKS: M06 verification; M10 verification; M11/M12 verification; drafting; terminology; DOCX construction`
- `WORKER_MODELS_REQUESTED: GPT-6.1 Sol Medium for M06/M10/drafting/terminology; GPT-6 Luna for M11/M12 and DOCX`
- `WORKER_MODELS_ACTUAL: NOT_VERIFIED`
- `PARALLEL_EXECUTION: YES for independent source verification; sequential synthesis → drafting → terminology/DOCX`
- `WORKER_FAILURES: NONE`
- `WORKER_RETRIES: NONE`

M11 và M12 được giao chung một worker vì giới hạn bốn slot đồng thời gồm ROOT; hai PDF được kiểm tra và báo cáo riêng.

## Sources and verification

- **Papers read:** 4.
- **Evidence IDs:** M06-E02, M10-E01, M11-E01, M12-E01.
- **PDF locators:** M06 p.5/§3.1.3/Fig.3c; M10 p.2/Fig.1; M11 p.2/Fig.1 with result pages checked; M12 p.3/Figs.2–3 with result pages checked.
- **Direct source-grounded claims:** 4.
- **Inference claims:** 3.
- **Document coverage records:** 2, excluded from technical-claim count.

## Scientific synthesis

- Layer vacuum jamming: atmospheric compression of an airtight envelope increases interlayer friction.
- Layer positive-pressure jamming: a bag and rigid frame create a different confinement path; slip remains architecture-specific.
- Granular positive-pressure jamming: bladder expansion compresses surrounding particles against a non-extensible sleeve.
- Dual-pressure actuator: negative pressure jams particles, positive pressure bends the actuator.
- Transfer limits: medium, topology, confinement, pressure path, observable and failure/transition behavior differ from MP1.

## Document and QA results

- **Tables:** 1 comparative table with caption; 1 six-column glossary table.
- **Figures:** 0.
- **Equations:** 0.
- **Citations:** 4 provisional citations [1]–[4].
- **Terminology entries:** 13.
- **Terminology review required:** 0.
- DOCX opens, ZIP integrity passes, A4 portrait, Unicode Vietnamese preserved.
- Table headers repeat; rows are non-splitting; table runs use explicit Times New Roman 8.5 pt.
- Citation/reference closure and DOI metadata pass static checks.
- `SOURCE_VERIFICATION_COMPLETED: YES`.
- `SCIENTIFIC_SYNTHESIS_APPROVED: YES`.
- `DOCX_GENERATION: COMPLETE`.
- `WORD_RENDER_VALIDATION: NOT_VERIFIED`.
- `SEVEN_GATE_RESULT: PASS_ALL_7_GATES`.
- `FINAL_STATUS: PARTIAL_WITH_FINDINGS`.


## Targeted hotfix R1

- Bỏ B01/B02 khỏi thesis prose.
- Sửa attribution M06 thành review synthesis của Caro và Carmichael.
- Sửa friction wording thành sức kháng ma sát truyền được.
- Sửa M10: tải uốn bên ngoài tạo độ võng; mạng hạt/biên giam giữ chi phối độ cứng và đáp ứng.
- Giảm các câu transfer-limit lặp.
- Glossary DOCX rút gọn 6 cột và giảm padding; vẫn giữ 13 dòng, còn CSV đầy đủ.
- C01/C02/C04 trong traceability được cập nhật; technical claims vẫn 7, coverage records 2.

## Unresolved limitations

Không có nguồn nào trong bốn bài xác lập topology tiếp xúc, luật vật liệu hoặc pressure-to-traction law cho bó dây TiNi. M06 không cung cấp local pressure field; M10/M11/M12 là architecture-specific. Cần render DOCX trong môi trường có Word/LibreOffice trước khi đưa vào luận văn chính thức.
