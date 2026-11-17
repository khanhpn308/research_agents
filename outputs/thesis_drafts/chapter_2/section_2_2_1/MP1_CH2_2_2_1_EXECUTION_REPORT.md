# Báo cáo thực hiện bản thảo §2.2.1

TASK_ID: MP1-CH2-2.2.1-RESEARCH-THESIS-DRAFT
STATUS: SUCCESS_DRAFT_SELF_REVIEW_ONLY
OFFICIAL_HEADING: 2.2.1. Robot continuum và các đại lượng độ cứng
OUTLINE_SHA256: 18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e
OUTLINE_PHYSICAL_PAGE: 11
OUTLINE_BULLETS: 2
WORKSPACE: /home/khanh/projects/mechanical-research-agents
BRANCH: main
HEAD: e66bb2f2339006e763cd60687cfc24680b945d97
ROOT_MODEL_REQUESTED: GPT-6.1 Sol High
ROOT_MODEL_ACTUAL: NOT_VERIFIABLE_FROM_BACKEND_TELEMETRY
WORKER_MODELS_REQUESTED: Sol Medium / Luna
WORKER_MODELS_ACTUAL: NOT_VERIFIABLE_FROM_BACKEND_TELEMETRY
WORKERS_USED: 3
REVIEW_AUTHORITY: SELF_REVIEW_ONLY
AUTHOR_APPROVAL_STATUS: HUMAN_APPROVAL_PENDING
FINAL_INDEPENDENT_ACCEPTANCE: REQUIRED; NOT_PERFORMED

## Kết quả và giới hạn kết luận

Đã tạo bản thảo Word duy nhất §2.2.1, phân biệt đối tượng robot/cấu trúc vật lý với biểu diễn đường trục, phân cấp E–B/EI–K, quan hệ mô men–độ cong và điều kiện dùng dầm. Trượt tương đối đặt vấn đề kiểm tra ràng buộc tiết diện, không tự làm mọi dầm hiệu dụng vô giá trị. Không có kết quả MP1, giá trị tham số mới, quyết định cấu hình, literature-gap adjudication hoặc nghiệm thu độc lập.

B01: Định nghĩa vật thể, dầm tương đương, độ cứng vật liệu, độ cứng uốn và độ cứng đầu công tác.

B02: Giải thích điều kiện khi dùng mô hình dầm và khi chuyển động tương đối giữa các phần tử làm mô hình dầm đơn không còn đủ.

B01_COVERAGE: COMPLETE_WITHIN_DRAFT_SCOPE; P001–P009 và glossary.
B02_COVERAGE: COMPLETE_WITHIN_DRAFT_SCOPE; P004, P010–P014.

## WEP đúng §2.2.1

WEP_221_CROSSWALK_ROWS: 2, B01/B02.
WEP_221_SOURCE_MATRIX_ROWS: 4, A01–A04.
WEP_221_READINESS_STATUS: EVIDENCE_READY theo WEP09/11, riêng §2.2.1; không kế thừa readiness §2.6.
WEP_221_SOURCE_BINDINGS: M03-E02; M02-E01; M02-E02; M02-E03, cùng xuất hiện trong hai bullet; hai paper M02/M03.
WEP_221_EVIDENCE_GAPS: binding cho continuum/model framing không đủ chứng minh mọi định nghĩa stiffness hoặc cơ chế nhiều dây; bổ sung trực tiếp M26/M31/M22 theo claim và giới hạn. Không tạo binding WEP mới hoặc Evidence ID mới.
WEP_221_HUMAN_DEPENDENCIES: 5 nhóm ở phần quyết định mở dưới đây; không cần tự chốt để soạn định nghĩa có điều kiện.
WEP_221_UNRESOLVED: locator M03-E02 xung đột lịch sử còn trong input read-only; không dùng nó làm chứng cứ đúng trang3. Locator glossary/câu đang sử dụng được đọc trực tiếp trang1/9, ghi không có Evidence ID đã đăng ký cho đoạn mới.

Đã đọc các tệp WEP01/02/03/05/06/07/08/09/11. WEP03 có một số diễn giải mạnh hơn nguồn; không dùng mô tả của brief thay cho PDF nghiên cứu. WEP06 không bắt buộc quota hình/bảng/công thức nên không sao chép hình, không tạo bản vẽ prototype, không thêm phương trình chỉ để lấp nội dung.

### WEP rows nguyên gốc — 01_OUTLINE_BULLET_CROSSWALK.csv

```csv
bullet_id,section_id,section_title,outline_pdf_page,bullet_type,guidance_bullet,evidence_status,paper_id,evidence_id,paper_authors,paper_year,doi,accepted_source_path,record_path,record_line,source_locator,source_section,figure_table_equation,exact_claim_supported,transfer_limit,rationale,support_role,coverage_class,provenance_note
2.2.1-B01,2.2.1,Robot continuum và các đại lượng độ cứng,11,WRITING_DIRECTION,"Định nghĩa vật thể, dầm tương đương, độ cứng vật liệu, độ cứng uốn và độ cứng đầu công tác.",SUPPORTED_WITH_LIMITATIONS,M03;M02;M02;M02,M03-E02;M02-E01;M02-E02;M02-E03,"Russo et al.; Burgner-Kahrs, Rucker, and Choset; Burgner-Kahrs, Rucker, and Choset; Burgner-Kahrs, Rucker, and Choset",2023;2015;2015;2015,10.1002/aisy.202200367;10.1109/TRO.2015.2489500;10.1109/TRO.2015.2489500;10.1109/TRO.2015.2489500,data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf;data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf;data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf;data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf,outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl;outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl;outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl;outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl,8;4;5;6,PDF p.3; printed p.NOT_REPORTED; PDF p.1; printed p.NOT_REPORTED; PDF p.2; printed p.NOT_REPORTED; PDF p.3; printed p.NOT_REPORTED,Section 1.2 Modeling and Control; Abstract / Introduction; Section II-A Classification; Section II-B Structure,Table 1; Fig. 1; Definition 1; Fig. 2,"The review places models on a spectrum from efficient geometric approximations to FEM. || The survey describes compliant curvilinear continuum robots for constrained access. || The operational definition separates continuum structures from discrete-joint approximations. || The survey lists structural and actuation categories, including NiTi concentric tubes; it is contextual prior art.",Khảo sát phổ mô hình dầm đơn thuần nhất; không tính đến hiện tượng trượt giữa các lớp vật liệu rời rạc trong kết cấu jamming. || Bài tổng quan phân loại vĩ mô các hệ thống robot y sinh; không cung cấp dữ liệu định lượng về lực cản uốn hay ứng suất tiếp xúc cục bộ của dầm nhiều lớp. || Định nghĩa động học và hình học định tính; không bao gồm các hiệu ứng phi tuyến tiếp xúc ma sát hay trượt tương đối giữa các lớp vật liệu. || Phân loại phương thức truyền động ở cấp hệ thống; không mô hình hóa tương tác ma sát tiếp xúc cục bộ bên trong cấu trúc dầm nhiều lớp. || Locator conflict is preserved; no additional M03 page/table claim is verified in this pack.,"Evidence Record hỗ trợ phần cơ chế/phương pháp được nêu; giới hạn topology, branch, transfer hoặc uncertainty phải giữ nguyên.",DIRECT_SUPPORT,SOURCE_GROUNDED_LIMITED,"M03-E02 locator conflict retained: accepted record says PDF p.3, Section 1.2 Modeling and Control, Table 1; Paper Notes describe pp.7–8, Section 3, Table 2. Treat accepted-record fields as verified and do not silently normalize."
2.2.1-B02,2.2.1,Robot continuum và các đại lượng độ cứng,11,METHODOLOGICAL_PROPOSAL,Giải thích điều kiện khi dùng mô hình dầm và khi chuyển động tương đối giữa các phần tử làm mô hình dầm đơn không còn đủ.,SUPPORTED_WITH_LIMITATIONS,M03;M02;M02;M02,M03-E02;M02-E01;M02-E02;M02-E03,"Russo et al.; Burgner-Kahrs, Rucker, and Choset; Burgner-Kahrs, Rucker, and Choset; Burgner-Kahrs, Rucker, and Choset",2023;2015;2015;2015,10.1002/aisy.202200367;10.1109/TRO.2015.2489500;10.1109/TRO.2015.2489500;10.1109/TRO.2015.2489500,data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf;data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf;data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf;data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf,outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl;outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl;outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl;outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl,8;4;5;6,PDF p.3; printed p.NOT_REPORTED; PDF p.1; printed p.NOT_REPORTED; PDF p.2; printed p.NOT_REPORTED; PDF p.3; printed p.NOT_REPORTED,Section 1.2 Modeling and Control; Abstract / Introduction; Section II-A Classification; Section II-B Structure,Table 1; Fig. 1; Definition 1; Fig. 2,"The review places models on a spectrum from efficient geometric approximations to FEM. || The survey describes compliant curvilinear continuum robots for constrained access. || The operational definition separates continuum structures from discrete-joint approximations. || The survey lists structural and actuation categories, including NiTi concentric tubes; it is contextual prior art.",Khảo sát phổ mô hình dầm đơn thuần nhất; không tính đến hiện tượng trượt giữa các lớp vật liệu rời rạc trong kết cấu jamming. || Bài tổng quan phân loại vĩ mô các hệ thống robot y sinh; không cung cấp dữ liệu định lượng về lực cản uốn hay ứng suất tiếp xúc cục bộ của dầm nhiều lớp. || Định nghĩa động học và hình học định tính; không bao gồm các hiệu ứng phi tuyến tiếp xúc ma sát hay trượt tương đối giữa các lớp vật liệu. || Phân loại phương thức truyền động ở cấp hệ thống; không mô hình hóa tương tác ma sát tiếp xúc cục bộ bên trong cấu trúc dầm nhiều lớp. || Locator conflict is preserved; no additional M03 page/table claim is verified in this pack.,"Evidence Record hỗ trợ phần cơ chế/phương pháp được nêu; giới hạn topology, branch, transfer hoặc uncertainty phải giữ nguyên.",DIRECT_SUPPORT,SOURCE_GROUNDED_LIMITED,"M03-E02 locator conflict retained: accepted record says PDF p.3, Section 1.2 Modeling and Control, Table 1; Paper Notes describe pp.7–8, Section 3, Table 2. Treat accepted-record fields as verified and do not silently normalize."
```

### WEP rows nguyên gốc — 02_SECTION_SOURCE_MATRIX.csv

```csv
section_id,section_title,argument_id,paper_id,evidence_id,title,authors,year,doi,evidence_status,accepted_source_path,pdf_page,printed_page,source_section,figure_table_equation,exact_text_anchor,supportable_claim,experimental_or_modeling_context,model_assumptions,quantitative_units,validation_and_limitations,record_path,record_line,support_role,coverage_class,provenance_note
2.2.1,Robot continuum và các đại lượng độ cứng,2.2.1-A01,M03,M03-E02,Continuum Robots: An Overview,Russo et al.,2023,10.1002/aisy.202200367,VERIFIABLE_FULL_TEXT,data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf,3,NOT_REPORTED,Section 1.2 Modeling and Control,Table 1,geometrical models ... finite-element methods,The review places models on a spectrum from efficient geometric approximations to FEM.,Review synthesis,['piecewise constant curvature; FEM'],['NOT_REPORTED'],"{'status': 'VERIFIED_FULL_TEXT', 'limitations': 'Khảo sát phổ mô hình dầm đơn thuần nhất; không tính đến hiện tượng trượt giữa các lớp vật liệu rời rạc trong kết cấu jamming.'}; accepted-record locator conflicts with Paper Notes detailed locator (Table 2/Section 3); use accepted fields as the WEP locator and flag the conflict.",outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl,8,DIRECT_SUPPORT,SOURCE_GROUNDED_LIMITED,"ACCEPTED_RECORD_LOCATOR: PDF p.3; Section 1.2 Modeling and Control; Table 1. PAPER_NOTES_CONFLICT: M03 notes describe detailed taxonomy at PDF pp.7–8, Section 3, Table 2. Do not replace the accepted record locator without a focused source recheck."
2.2.1,Robot continuum và các đại lượng độ cứng,2.2.1-A02,M02,M02-E01,Continuum Robots for Medical Applications: A Survey,"Burgner-Kahrs, Rucker, and Choset",2015,10.1109/TRO.2015.2489500,VERIFIABLE_FULL_TEXT,data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf,1,NOT_REPORTED,Abstract / Introduction,Fig. 1,continuum robot designs can traverse confined spaces,The survey describes compliant curvilinear continuum robots for constrained access.,Medical intervention context,['infinite-DOF elastic member'],['NOT_REPORTED'],"{'status': 'VERIFIED_FULL_TEXT', 'limitations': 'Bài tổng quan phân loại vĩ mô các hệ thống robot y sinh; không cung cấp dữ liệu định lượng về lực cản uốn hay ứng suất tiếp xúc cục bộ của dầm nhiều lớp.'}",outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl,4,DIRECT_SUPPORT,SOURCE_GROUNDED_LIMITED,
2.2.1,Robot continuum và các đại lượng độ cứng,2.2.1-A03,M02,M02-E02,Continuum Robots for Medical Applications: A Survey,"Burgner-Kahrs, Rucker, and Choset",2015,10.1109/TRO.2015.2489500,VERIFIABLE_FULL_TEXT,data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf,2,NOT_REPORTED,Section II-A Classification,Definition 1,constitutive material forms curves with continuous tangent vectors,The operational definition separates continuum structures from discrete-joint approximations.,Definition-level statement,['continuous tangent vectors'],['NOT_REPORTED'],"{'status': 'VERIFIED_FULL_TEXT', 'limitations': 'Định nghĩa động học và hình học định tính; không bao gồm các hiệu ứng phi tuyến tiếp xúc ma sát hay trượt tương đối giữa các lớp vật liệu.'}",outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl,5,DIRECT_SUPPORT,SOURCE_GROUNDED_LIMITED,
2.2.1,Robot continuum và các đại lượng độ cứng,2.2.1-A04,M02,M02-E03,Continuum Robots for Medical Applications: A Survey,"Burgner-Kahrs, Rucker, and Choset",2015,10.1109/TRO.2015.2489500,VERIFIABLE_FULL_TEXT,data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf,3,NOT_REPORTED,Section II-B Structure,Fig. 2,"Concentric-tube robots are composed of multiple, precurved, elastic tubes","The survey lists structural and actuation categories, including NiTi concentric tubes; it is contextual prior art.",Medical continuum robot survey,['single/multibackbone; concentric tube'],['NOT_REPORTED'],"{'status': 'VERIFIED_FULL_TEXT', 'limitations': 'Phân loại phương thức truyền động ở cấp hệ thống; không mô hình hóa tương tác ma sát tiếp xúc cục bộ bên trong cấu trúc dầm nhiều lớp.'}",outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl,6,DIRECT_SUPPORT,SOURCE_GROUNDED_LIMITED,
```

## Nguồn thực sự được dùng

SOURCE_PAPERS: 5 — M02; M03; M26; M31; M22.
VERIFIED_PDFS: 5 — hash và các đoạn được sử dụng, không phải audit toàn bộ năm bài.
PDF_PAGES_DIRECTLY_VERIFIED: 12 trang vật lý duy nhất dùng cho claim, ROOT đọc trực tiếp; cộng kiểm xung đột M03 PDF3 và một số trang metadata không tính vào chỉ số12.
EVIDENCE_IDS: 3 — M02-E02; M22-E02; M31-E07. Đây là ID thực dùng trong CSV, khác bốn ID binding WEP gốc.

- M02 / [1]: J. Burgner-Kahrs, D. C. Rucker và H. Choset, “Continuum Robots for Medical Applications: A Survey,” IEEE Transactions on Robotics, tập 31, số 6, tr. 1261–1280, 2015. DOI 10.1109/TRO.2015.2489500. Trang claim: [2, 5, 6, 7]. Canonical `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf`. SHA256 `d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b`.
- M03 / [2]: M. Russo, S. M. H. Sadati, X. Dong, A. Mohammad, I. D. Walker, C. Bergeles, K. Xu và D. A. Axinte, “Continuum Robots: An Overview,” Advanced Intelligent Systems, tập 5, số 5, bài 2200367, 2023. DOI 10.1002/aisy.202200367. Trang claim: [1, 9]. Canonical `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf`. SHA256 `51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2`.
- M26 / [3]: B. Reedlunn, S. Daly và J. Shaw, “Superelastic shape memory alloy cables: Part I – Isothermal tension experiments,” International Journal of Solids and Structures, tập 50, số 20–21, tr. 3009–3026, 2013. DOI 10.1016/j.ijsolstr.2013.03.013. Trang claim: [2, 8]. Canonical `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf`. SHA256 `00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9`.
- M31 / [4]: H. Jeon, Q. N. Le, S. Jeong, S. Jang, H. Jung, H. Chang, H. J. Pandya và Y. Kim, “Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism,” IEEE Robotics and Automation Letters, tập 7, số 3, tr. 6582–6589, 2022. DOI 10.1109/LRA.2022.3174363. Trang claim: [6]. Canonical `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf`. SHA256 `65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03`.
- M22 / [5]: Y. Zhang, J. Wang, G. Ye và R. Xu, “Bending Stiffness of Parallel Wire Cables Including Interfacial Slips among Wires,” Journal of Structural Engineering, tập 144, số 10, bài 04018164, 2018. DOI 10.1061/(ASCE)ST.1943-541X.0002171. Trang claim: [1, 2, 3]. Canonical `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf`. SHA256 `9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe`.

Các fragment và locator chi tiết nằm trong CSV, gồm source_role/source_evidence_type. Những đoạn chưa có ID được ghi SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID. Không cấp Mxx-Exx mới, không sửa registry để làm khớp. M02/M03 là tổng quan cho định nghĩa/khung mô hình; M26 là kéo dây/cáp TiNi, không xác lập dầm MP1; M31 là phép thử đầu robot và suy EI công xôn trong cấu hình riêng; M22 là mô hình cáp dây song song với lớp tương đương và hiệu chuẩn bằng dữ liệu tài liệu, không phải kiểm chứng tiếp xúc dây tròn MP1.

Đối chiếu metadata: title/authors/year/venue/DOI được đọc tại canonical PDF. M02 có số đầu1261/cuối1280; M03 ghi tập5/bài2200367, issue5 đối chiếu [publisher Wiley](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202200367). M22 PDF1 ghi144(10)/04018164 và DOI đầy đủ, trong khi registry rút gọn DOI; giữ cả sự khác biệt trong traceability. M26 PDF article-in-press ghi xxx cho pagination tạp chí, vì vậy bibliography dùng pagination3009–3026, tập50 số20–21 được đối chiếu [publisher Elsevier](https://www.sciencedirect.com/science/article/pii/S0020768313001145); trang in trong CSV vẫn theo PDF, không quy đổi máy móc. M31 PDF1/cuối8 ghi6582–6589, tập7 số3, DOI, tác giả; [trang công bố của nhóm tác giả](https://labs.dese.iisc.ac.in/beeslab/journal-articles/) bổ trợ DOI. Một số trang DOI IEEE/ASCE không truy cập được bằng web tool; không dùng lỗi truy cập đó để phủ nhận PDF. Web chỉ kiểm metadata của nguồn đã có, không mở broad novelty search. Nguồn2013/2015/2018 dùng cho cơ sở khái niệm/cơ học, không chứng minh novelty hiện tại.

## Đếm trực tiếp từ DOCX/CSV cuối

BODY_PARAGRAPHS: 14
CLAIM_RECORDS: 60
BODY_CLAIM_RECORDS: 46
BODY_UNIQUE_CLAIM_SPANS: 42
GLOSSARY_CLAIM_RECORDS: 14
UNRESOLVED_ANCHORS: 0
SOURCE_FRAGMENT_CHECKS: 34
UNRESOLVED_SOURCE_FRAGMENTS: 0
TERMINOLOGY_ENTRIES: 14
GLOSSARY_ENTRIES: 14
SCIENTIFIC_TABLES: 0
GLOSSARY_TABLES: 1
FIGURES: 0
OMML_EQUATIONS: 0
REFERENCES: 5
UNIQUE_DOIS: 5
CITATION_OCCURRENCES: 35
CITATION_OCCURRENCES_BODY: 27
CITATION_OCCURRENCES_GLOSSARY: 8
ORPHAN_CITATIONS: 0
ORPHAN_REFERENCES: 0

Phân loại claim records: {"SOURCE_GROUNDED_CLAIM": 12, "CROSS_STUDY_INFERENCE": 12, "AUTHOR_SYNTHESIS": 14, "DEFINITION_OR_CONVENTION": 21, "PENDING_HUMAN_DECISION": 1}. Một câu có thể có hai binding nguồn nên60 dòng không phải60 kết quả độc lập. Đã đếm phủ 5608/5608 ký tự không trắng trong nội dung; đây là kiểm phủ span, không phải chứng chỉ khoa học tự động. Glossary định nghĩa/quy ước được tách khỏi empirical claim. Không đếm5 nhãn reference vào citation occurrences.

## P3, RQ và quyết định con người

P3_STATUS_PRESERVATION: PRESERVED_READ_ONLY.
H0a: REFUTED_IN_TRANSFORMATION_REGIME, chỉ trong miền chuyển pha tương ứng; không phủ nhận mọi nhánh đàn hồi nhỏ.
H0b: NOT_FALSIFIED_LIVE_COMPETITOR.
H1: INSUFFICIENT_EVIDENCE.
RQ_MAPPING_STATUS: PROVISIONAL_MANY_TO_MANY; HUMAN_DECISION_PENDING.
PENDING_HUMAN_DECISIONS: 5/5 vẫn mở.

Đã đọc P3_RESEARCH_GAP_MATRIX.csv, P3_GAP_ADJUDICATION.md, P3_HYPOTHESIS_ASSESSMENT.md, P3_RESEARCH_QUESTIONS.md, P3_DECISION_REPORT.md và DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md tại canonical root bên dưới. Đối chiếu thêm WP_E_THEMATIC_SYNTHESIS.md và WP_E_ASSUMPTIONS_LIMITATIONS.md. Không dùng giới hạn dầm để tạo gap mới. Giữ riêng5 câu hỏi trong dàn ý PDF và4 nhóm RQ của P3; không phê duyệt mapping hoặc hợp nhất chúng. Các nhãn R-suffixed lịch sử không thay thế trạng thái canonical.

1. Hình học, tiết diện và giao diện tiếp xúc thực tế.
2. Đại diện/quan sát độc lập của tải pháp tuyến cục bộ.
3. Miền nhiệt độ, pha, tốc độ và lịch sử TiNi.
4. Đại lượng độ cứng chính, nhánh và bất định đo.
5. Phạm vi đóng góp/kiểm chứng của SMA–piston và Bench B.

Trạng thái G00–G11 đọc trực tiếp từ matrix canonical:

| gap_id | classification | status |
|---|---|---|
| G00 | SUPPORTED_WITHIN_REVIEWED_CORPUS | CLOSED_AS_GENERAL_MECHANISM; MP1 transfer remains open |
| G01 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-IDENTIFICATION QUESTION |
| G02 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-IDENTIFICATION QUESTION |
| G03 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN BOUNDED EMPIRICAL CHARACTERIZATION |
| G04 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN ENGINEERING/SYSTEM-IDENTIFICATION QUESTION |
| G05 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN ATTRIBUTION/REPEATABILITY QUESTION |
| G06 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN BOUNDED MODEL-DISCRIMINATION QUESTION |
| G07 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN IDENTIFIABILITY GATE |
| G08 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-CALIBRATION QUESTION |
| G09 | OUT_OF_SCOPE | PROJECT PREREQUISITE, NOT A LITERATURE GAP |
| G10 | NOT_ESTABLISHED | CONDITIONAL STRETCH ONLY |
| G11 | NOT_ESTABLISHED | PROHIBITED CLAIM |

G00 đóng cơ chế chung; G01–G08 là câu hỏi có điều kiện; G09 là prerequisite của dự án; G10 chưa xác lập; G11 là cách tuyên bố novelty bị cấm. Không thay đổi kết luận này.

## Liên tục với các phần đã nghiệm thu

CROSS_SECTION_TERMINOLOGY_FINDINGS: 2 phát hiện về mức khái quát, không sửa baseline.

1. §2.3 dùng “độ cứng uốn” rộng cho bending stiffness/rigidity; bản mới khai báo B/EI và đơn vị theo phân biệt chặt ở §2.6, đồng thời dùng K riêng cho lực–chuyển vị.
2. “Mô đun hiệu dụng” của §2.5–§2.6 là tham số nhận dạng qua mô hình, không tự bằng E vật liệu. §2.2.1 không tạo thêm định nghĩa E_eff; nêu ranh giới E/B/K và điều kiện tuyến tính hóa TiNi.

Đã đọc master terminology/source traceability và ngữ cảnh DOCX §§2.3–2.6. Không dùng bản thảo đã nghiệm thu làm nguồn gốc thay PDF. Không sửa minor errata §2.5, 58 đoạn khoa học/267 master claim/35 thuật ngữ/16 references của baseline §2.6; các số đó là đặc điểm baseline theo nhiệm vụ, không phải số của bản mới và không được dùng thay kiểm hash.

## Kết quả gate và Word

GATE_1: PASS
GATE_2: PASS_WITH_DOCUMENTED_LIMITATIONS
GATE_3: PASS
GATE_4: PASS
GATE_5: PASS_WITH_DOCUMENTED_LIMITATIONS
GATE_6: PASS_WITH_DOCUMENTED_LIMITATIONS
GATE_7: PASS

DOCX_SHA256: 9a332dd845352f5afcc0d821e2e0e2f28d805b92265ad8547c28b2a800a2dbba
DOCX_ZIP_XML_STATUS: PASS; ZIP CRC không lỗi,13 phần XML parse được.
WORD_RENDER_VALIDATION: PASS_LIBREOFFICE_SELECTED_ENVIRONMENT; bản DOCX cuối render PDF và PNG trong scratch, ROOT xem tất cả trang.
RENDERED_PAGES: 4
PAGES_VISUALLY_REVIEWED: 4/4
MICROSOFT_WORD_VALIDATION: NOT_VERIFIED
RENDER_PDF_SHA256: e868cd4b06073f7043bc640e34bf4594461046eea028b293041a4513ae5c63ae
BASELINES_UNCHANGED: TRUE;12/12 tệp DOCX/master CSV đối chiếu checksum.
INPUT_CHECKSUMS_UNCHANGED: TRUE;196/196 tệp theo dõi.
GIT_CHANGE_SCOPE: đúng5 tệp mới tại outputs/thesis_drafts/chapter_2/section_2_2_1/;2 modified và358 untracked có sẵn không bị thay/dọn.
P1_P2_UNRESOLVED: 0 trong phạm vi tự kiểm.

Runtime LibreOffice24.2.7.2 được giải nén cục bộ cùng dependencies trong scratch, không cài hệ thống và không thêm dependency vào repo. Quá trình chuẩn bị runtime từng lỗi bootstrap, đã xử lý trước khi xuất; tiến trình render cuối trả0. Cảnh báo Java/liblangtag vẫn có nhưng bản PDF cuối hiển thị đủ nội dung, chỉ dùng Times New Roman regular/bold, không thiếu glyph hoặc ô bảng. Microsoft Word chưa mở trực tiếp. Không đưa PDF/PNG/runtime vào final. Một lần kiểm font đầu cho thấy theme Heading dùng phông khác, đã sửa và kiểm/render lại toàn bộ. Lần sửa nội dung cuối làm rõ thân dài/mảnh; parser và render cuối đã chạy lại sau sửa đó.

DOCUMENTED_LIMITATIONS: chỉ xác minh các đoạn PDF dùng, không tuyên bố audit toàn bộ bài; một số đoạn không có Evidence ID đăng ký; M03 locator và M22 DOI trong registry lịch sử giữ nguyên với note; mapping RQ/five human decisions chưa phê duyệt; Word chưa kiểm; tự kiểm không thay nghiệm thu độc lập. Không kiểm lại toàn bộ khoa học của baseline được nghiệm thu, không sửa registry, không tìm novelty mới, không viết phần khác.

## Phân công và khả năng xác minh model

Worker A đối chiếu WEP/dàn ý, continuum/giả thiết dầm; B đối chiếu đại lượng/cơ học/source limits; C đối chiếu P3/thuật ngữ/văn phong. ROOT trực tiếp viết, đọc các đoạn nguồn được dùng, tạo Word, giải anchor, kiểm bố cục và phân xử. Worker không sửa baseline hoặc final files.

Cấu hình gửi qua công cụ spawn: A/B `gpt-6.1-sol`, reasoning medium; C `gpt-6-luna`, reasoning medium. Đây là tham số yêu cầu dispatch quan sát được, không phải telemetry backend xác minh model thực thi. Không khai ROOT/worker actual là verified chỉ từ tên cấu hình. Có3 worker thực tế được gọi; không giả lập các vai trò khác của kỹ năng. Quy trình tiểu mục này tuân theo cấu trúc và quyền hạn cụ thể của người dùng, không chạy pipeline toàn bài, không thêm abstract/disclosures/workflow metadata vào manuscript.

## Pre-flight và bảo toàn

Repo root/pwd đã đối chiếu `/home/khanh/projects/mechanical-research-agents`, branch main, HEAD `e66bb2f2339006e763cd60687cfc24680b945d97`. Đã đọc AGENTS.md và bảy context files theo thứ tự yêu cầu trước tổng hợp. Dàn ý được mở trực tiếp, checksum đúng. Target directory không chứa output khi bắt đầu, nên không có tệp tác vụ khác bị ghi đè. Snapshot lưu hash196 đầu vào, bản sao2 tệp tracked đang modified và diff/staged/status; scratch ở ngoài final. Phạm vi tạo mới chỉ5 deliverables. Tệp script tạm và render không nằm trong repo final và không được stage.

Git pre-status đầy đủ (porcelain v1 -uall):2 modified,358 untracked; danh sách này được giữ trong report để không phụ thuộc scratch. Các untracked là có sẵn trước tác vụ, không phải đều do phiên này tạo.

```text
 M outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py
 M outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md
?? .agents/skills.json
?? data/LR-FORMATED-rewrite.docx
?? data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md
?? data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md
?? data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md
?? data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md
?? "data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt"
?? "data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt"
?? "data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt"
?? "data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt"
?? data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt
?? "data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt"
?? data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt
?? data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt
?? "data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt"
?? data/chap1-2_citations/MANIFEST.json
?? data/chap1-2_citations/README.md
?? docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md
?? docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md
?? docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md
?? docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md
?? docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx
?? docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx
?? "docs/project/almost done/LR-FORMATED.docx"
?? docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md
?? docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md
?? "literature review/LR-FORMATED-rewrite-outline-de-xuat.docx"
?? "literature review/LR-FORMATED-rewrite.docx"
?? "literature review/LR-FORMATED.docx"
?? "literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL.zip"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md"
?? "literature review/ma-tran-tong-quan-tai-lieu.docx"
?? "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json"
?? "literature review/~$-FORMATED-rewrite.docx"
?? "literature review/~$-FORMATED.docx"
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/CLAIM_SOURCE_MAP.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/HIGHLIGHT_REGISTER.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/README.md
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S01_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S02_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S03_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S04_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05a_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05b_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S06_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S07_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S09_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S10_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S11_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S12_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S13_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S15_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S17_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S18_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S22_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/V-W02_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/VALIDATION.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curated_passages.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/inputs.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/package_highlights.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf_text_geometry.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/prepare_inputs.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S01_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S03_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S04_P5.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S07_P6.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S09_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S22_P71.png
?? outputs/literature/LR_CITATION_MATRIX_2026-10-14.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv
?? outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv
?? outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv
?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md
?? outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_8_CHAPTER_2_RELEASE_MANIFEST_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINALIZATION_CHANGELOG_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINAL_CITATION_REGISTER_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINAL_CLAIM_TRACEABILITY_2026-10-04.json
?? outputs/reports/MP1_GLOSSARY_C2_3_1_REPORT_2026-10-16.md
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/actual_docx_inventory.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/artifact_integrity_original.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/citation_appearances_original.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/inspect_artifact.py
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05a_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05b_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S11_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/V-W02_crossref.json
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_TERMINOLOGY.csv
```

## Manifest checksum đầu vào trước/sau

196 tệp dưới đây đều có hash sau bằng hash trước; đường dẫn tuyệt đối. Nhóm snapshot ban đầu166 tệp gồm docs/project, thesis_drafts có sẵn, WEP và AGENTS;30 tệp bổ sung gồm context, P3/WP-E, canonical outline, Evidence Records và5 PDF được hash khi mở rộng danh mục bảo toàn, sau một số lượt đọc chỉ đọc và trước tạo deliverables. Không có khác biệt.

| Tệp | SHA256 trước = sau |
|---|---|
| `/home/khanh/projects/mechanical-research-agents/AGENTS.md` | `bf6bd863326f85f1f77eeccaec10928439555b939a6701fd5134aec0a7abcd00` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv` | `75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv` | `5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md` | `6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md` | `2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md` | `adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv` | `f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv` | `1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md` | `999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md` | `0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md` | `65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md` | `8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md` | `bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd` |
| `/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf` | `d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b` |
| `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf` | `51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2` |
| `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf` | `9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe` |
| `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf` | `00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9` |
| `/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf` | `65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03` |
| `/home/khanh/projects/mechanical-research-agents/docs/README.md` | `ee87dd76eaf983521550499cc5662f64f331347cf0fab89af4cbe5cc285a5fc2` |
| `/home/khanh/projects/mechanical-research-agents/docs/literature/LITERATURE_STRATEGY.md` | `2a4853e7228c66273916db8e129ff2a42d76b76bae418e7f6e368ff644cd32f6` |
| `/home/khanh/projects/mechanical-research-agents/docs/operations/KNOWN_ISSUES.md` | `ae4db17709c0d7f5af82746c5a51aee6be03cb7d1513335e68d91212e3f1bfcb` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/CURRENT_EXECUTION_SNAPSHOT.md` | `f2a673fe397f879ba1c5fc1dcc55649855c2c876c430490e28e4a4519f813fa9` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MENTOR_PIVOT_STATUS.md` | `b73c248cef5214fcae49261ae2506830d298922eeed10299976d407317bc9f7f` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1-V002_CURRENT_HANDOFF.md` | `fe48c78ff4e7d4437c17dcc044caf98e8df963349b01853968c3235ec7a2d025` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_CHAPTERS_1_2_WORKING_DRAFT_2026-09-29_VI.md` | `8ff36e2327b4a6de2f43a051a805646b648c91a7ff1d2e75e46ec552709bdeaa` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_CHAPTER_1_2_WRITING_PLAN_VI.md` | `682554cc75d871bc050cc37bf478b2107356be67d0729c1771b05273a60355cd` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_CLAIM_EVIDENCE_REPORT_TUTOR.md` | `6136c4d4433675d471953f5683d9a82beff4b2a11749bec037f7318c9bec3587` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_MENTOR_FEEDBACK_RESCOPE_2026-09-29_VI.md` | `8eadfc48b2d1b64443543f11c9993b538ecad3b9b90afdda80c07ea41f4c4a9c` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_MENTOR_PIVOT_CURRENT.md` | `9eb6cd362729d7aa1ea6b0094c21f753b3c0f011d69b7c112aa4deedfd1df3f8` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_MENTOR_PIVOT_TUTOR.md` | `df5a7edb7c71ebb8b20f9144164eed515c1f8811472bd9e61c396399fecc32be` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx` | `3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx` | `833344a5d64632ff9336832dbfccb2a8ae98dec45df046278e26d229b189ca9b` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx` | `3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_PHASE_6_NEXT_SESSION_CHECKPOINT_2026-10-02.md` | `5b3ee8e1032de8909b0146ad3a1f826ad31a3f10fc9308107117d4424325d136` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_STATUS_AND_NEXT_STEPS_VI.md` | `1a9b89f55d2ead283631215e300833928eb8c9bf97b85599fa594028ac043341` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/MP1_THESIS_OUTLINE_AND_RESEARCH_MASTER_PROMPT_VI.md` | `21ab597f5875bb2683913a9645bcbdca668186040789aa6a3e797173d8e94352` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/NEXT_SESSION_START_HERE.md` | `f2ec58cbffef9b90c8d3c8640309f30ae1d42014cc1bd5b75b5a14f5ad635ace` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/POST_D1_V009_RESEARCH_ROADMAP.md` | `d0aa08b8c7a42aa196d71ba65c63b619808452aa84922d19cf4a11e5717c2554` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/POST_D1_V009_RESEARCH_ROADMAP_VI.md` | `43f43d17db00ac68917cccd23ebf1e4cfc4e9b61b569b85e711a1d5d7c9eaf2b` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/PROJECT_HANDOFF_CURRENT.md` | `b84cde745e54b6b7ab83fe7da67d8e31f4ca7c38533a2f2bd81dd16673658423` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/RESEARCH_LOG.md` | `7cd88db0b06ee2a8ef01896412a469b0447dd83b7fbc8e8b21a8e3ce692cd575` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/RESEARCH_STATE.md` | `f302c37003601a20de6c148b5c84a6824618df4bcc9c34e5d09797ab3b1f3296` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/almost done/LR-FORMATED.docx` | `a63016590d98ff10636895166307603e2b3095ee5b632a30891b71c21190986c` |
| `/home/khanh/projects/mechanical-research-agents/docs/project/research_state.json` | `70b17fda40524a9e1c81231d6d969048cff5bcf0fc33052dffd85f75eaf58c67` |
| `/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl` | `a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba` |
| `/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl` | `9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033` |
| `/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl` | `a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2` |
| `/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl` | `ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd` |
| `/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl` | `e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md` | `402f6fc7c9d279b6b0c1fb6af3d72c5d42d131eeb0d8994a61c71c21cbc902cb` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx` | `6ded97f12de61cde7be319c865c3ea40cc6cbdc8d04e00cc648530ec718311a0` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md` | `91947d11eea09cac56f882936218d690458b1cbbbe431bd7f854be6a172ac9b7` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv` | `08202df03396abf83a4d320b56bd91abface6535c0379c1b75ec0c4ff89f3649` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv` | `f917c23d7dc2a404dbbbfa38874ede6dd10a50fac598cf7e3cfd880fdce83a2f` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md` | `4ca60c29585ed5a364ae526397fe7120976a3912ea9342996ba105f05e56e9ba` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx` | `7f614d06edca11ae573f27aeb5d277e5e7d74f3dc1d6ec9978dbe43f1795c8fb` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md` | `b6e59281460fcf9a88df683bebcebef1007c232ce9497da1ce3952b46402f622` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv` | `ec210ec6bf5bd02798db60db8a9366b3981efc23a9ddff0303051d7220f2523f` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv` | `287da4a23314f4a98d0ce9a9bbd84946ec235af7fd6a147e95f02b85e81f4984` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md` | `557429b44c0a0dfb8036e3aa734c8bcffc04bafbfd0be6f47bda207148ff3531` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx` | `1727dd0eeb32da84135d094f34c443605060cfd3fa39d269d85f855ce731b563` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md` | `757ba0ea8e15d71d2a9bbe2ba1bc2add412122ef610753b898871038a109bfc4` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv` | `c075ca7049f5cb81ea7fe997a9f29a0d0cc07971af52594f4560d2e659991826` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv` | `d79fa7a1611883a9ad6dfb5d4f02a58622c48e7533d0efc20ea4e3bd04b3bb76` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md` | `bfedc08e96e0163ce64b75a967f6327e42e49bee87dad55fcf522f9747ea22db` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx` | `38be496eb71922f7165b916ac552f9b9bcb54dbfd94dc0f635acd55372ce793d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md` | `7d3b803e0d690dacd49997861769e218186b6719f11c2337b5ebff813864bfb3` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv` | `7b3105acf012369a2c3a7ee4426ef66d457c874da38d2dd2d6fc8f518daed630` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv` | `735c2ad438e0a2ae0c05e83483ed51b6aeba2e49e372d59dc89bf6c6d9f1c223` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md` | `15537e97652af58e55a85bf001a604205953111db06dafb17243f481f266eec1` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx` | `a7a46894a3384cc519cdea0ab6b957cbb5e8fb130dd9b2073678a6d5513546e4` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md` | `c0aed9db3f084398feda73059135071c66d453e204afe08ed7fb6eef78cc4c10` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv` | `4c97bff4f998a10c465abde26731e236759599a17a32923a6459e6fc6bff73fa` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv` | `a86e1e9c781a788bea9de40bdb4a0186abf5a5f4c4382a74edeff02ad8ea6463` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md` | `84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv` | `eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md` | `e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx` | `bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md` | `25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv` | `54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv` | `65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md` | `1191dfd41f394d76ed933c3805c69ad4be1a47ac69e4494f19743a414696136a` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx` | `a58cf37dee216f2e193f9ee607fa15ba4987cf49b66c4a884dab895172ebf6d4` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md` | `9f60f4434b1699bc38ad23fbe7f5e7ae8c816957f4885caae3cd83dd6c0d5d7b` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv` | `dacb3c6ad632a1ec7e3aab167f614cddaa00c7a76850506616060c332eac7890` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv` | `d9bcd231bfb43ed223b8db6b270060196d5f485aa9f848cc5459d64ae857ba91` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md` | `d87a902881e1d5d2161172d2db700c261a8ba653af2f7cff1722ea5213206e19` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx` | `35a6842cd1513cb2ac91328ebadc1de0feacb2c6d421c5c4170d7ddce3c7e4e5` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md` | `72a9556ed438ef126da2d186add01b053970cae41df9b3e151d1b6e443621128` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv` | `f3778953f446e71e61ae192a3021b02407b13c35b11df2d30ab5914da49181dc` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv` | `ca606e7804945c1ac719f8088b4a9965525078033cced17e08364c45705a31b7` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md` | `cb02fffbe114df41dd6068c908f8e53d5de323c296b2b43a903f33519c027832` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx` | `2ecd6ccd690b0285e3414faa52135aaeb2db738e3b69df773548a597a4230da2` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md` | `932a5705b875d978a2158d4b1a590d4c2170cae3a60d4385a0b5cbc3b03466f4` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv` | `4eaae31d939e4fe3a64c2ae2afac173eafa843a22f86d9d88befc62d14bc98c5` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv` | `aa372e9fa39f91b4bfb04c9342831cd90e9ecd530c537c2361c35d45de1548c5` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md` | `675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx` | `0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md` | `543a25380b524439bcb97253e4531aefff28a6a50912b16a23e9815f154e98e9` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv` | `49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv` | `a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md` | `751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv` | `3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md` | `09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx` | `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md` | `0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv` | `d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv` | `eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md` | `78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx` | `a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md` | `31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv` | `e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv` | `3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md` | `c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx` | `8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md` | `d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv` | `c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv` | `5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md` | `ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx` | `024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md` | `256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv` | `8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv` | `baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md` | `a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx` | `8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md` | `945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv` | `6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv` | `336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md` | `86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx` | `9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md` | `eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv` | `0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv` | `de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md` | `b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv` | `a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md` | `3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx` | `cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md` | `d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv` | `229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv` | `70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md` | `03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx` | `983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md` | `0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv` | `b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv` | `bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md` | `c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx` | `fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md` | `e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv` | `ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv` | `c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md` | `5a9b1e21647777cb2855490d42e553a92f56906dad609522cc92841c4c59a9c9` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx` | `5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md` | `1d12b07ae29792e7ae547576468134926e6acefde9ccc740dd670cea084f70cd` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv` | `badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv` | `3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md` | `efc42a239b43168aa4f24fe938892cc7969bf062827e92103e3587dc0379bf2d` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx` | `607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md` | `93abadee17152b5e6eef625915ea7b828ee54f69124335a2de215e11b62ae65a` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv` | `636a5acb7514ccd8309a6e786280252847bdbd5c6674264069866a772429275b` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv` | `346ffdf77c8e5b60680d7fb57ee9992765a7112de12673a4328ce3c8149a64f5` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_7_GATE_REVIEW.md` | `b066121b47c37197b10d2bed2fa9709d5688d4973b5d13e23121c7bbf6ed275a` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv` | `019d4780f896a73b3b85400675d394dcfdda1c13e8404d7a0ff9723db4887944` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_EXECUTION_REPORT.md` | `de894a4c00089ca73f15076e06fdba9870b86231e236f7a7add802e9f701a2d6` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx` | `d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATION_CHANGELOG.md` | `15fc8d6380b20bff447626adff74034251ab633c548dea0893a836d7f0f28fc0` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv` | `987fb13dda00f2d62abb4da346f2c6da7e3cbd3857749edc3f72725b59049a13` |
| `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_TERMINOLOGY.csv` | `ec725c4206ac2854febc16f7ddb882802c1d71e53037792dd6ad6383869bca09` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md` | `cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_EXECUTION_REPORT.md` | `631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_P3_HANDOFF.md` | `bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md` | `5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_DECISION_MATRIX.md` | `4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md` | `5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_PROTOCOL_FREEZE_CHECKLIST.md` | `cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_R2_REPORT.md` | `a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md` | `e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_EXPERIMENTAL_VALIDATION_PLAN.md` | `f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md` | `f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md` | `2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_MODEL_STRATEGY.md` | `61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv` | `9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md` | `09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_SYSTEM_IDENTIFICATION_MATRIX.csv` | `894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf` | `18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e` |

## Manifest checksum đầu ra

- `MP1_CH2_2_2_1_7_GATE_REVIEW.md`: `3c5a8a85b77c3dd685c6c50b0b757603910710f4dc7b5bd52c367961f7d7ffcf`
- `MP1_CH2_2_2_1_DRAFT.docx`: `9a332dd845352f5afcc0d821e2e0e2f28d805b92265ad8547c28b2a800a2dbba`
- `MP1_CH2_2_2_1_SOURCE_TRACEABILITY.csv`: `c57f02dd60264c9c7689211783a5ca51171abe6e479ca93d519c0a0464b0e0f4`
- `MP1_CH2_2_2_1_TERMINOLOGY.csv`: `25bc782f7adb4b14f0531ab77be4d29642e18ba1b574f258491b51174c26113e`

Báo cáo thực hiện không nhúng hash tự thân để tránh tự tham chiếu. Khi nghiệm thu, tính SHA-256 đủ5 tệp bằng đoạn code dưới; không tạo tệp thứ sáu trong thư mục final.

```python
from pathlib import Path
import hashlib
p = Path('/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1')
for f in sorted(p.iterdir()):
    assert f.is_file()
    print(hashlib.sha256(f.read_bytes()).hexdigest(), f.name)
```

## Tệp, tái lập và điểm dừng

FILES_CREATED:
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_DRAFT.docx`
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_SOURCE_TRACEABILITY.csv`
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_TERMINOLOGY.csv`
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_7_GATE_REVIEW.md`
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_EXECUTION_REPORT.md`

Để tái lập kiểm tự động, dùng mã tự chứa trong 7_GATE_REVIEW.md; không cần script ở scratch. Để kiểm ý nghĩa, dùng CSV truy từng claim tới trang PDF canonical và giới hạn. Để lặp kiểm render trên máy có LibreOffice: `libreoffice --headless --convert-to pdf --outdir /thu-muc-scratch /duong-dan/MP1_CH2_2_2_1_DRAFT.docx`, render từng trang PDF bằng PyMuPDF/pdftoppm và xem trực tiếp. Sai khác engine hoặc font trên máy khác cần người nghiệm thu kiểm, không được giả định từ parser.

COMMIT_STATUS: NOT_PERFORMED
PUSH_STATUS: NOT_PERFORMED
STAGE_STATUS: NOT_PERFORMED
FINAL_SELF_REVIEW_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; bản thảo đủ điều kiện chuyển nghiệm thu độc lập trong phạm vi §2.2.1, chưa được tác giả phê duyệt hoặc nghiệm thu độc lập.
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE

Dừng tại §2.2.1. Không viết §2.2.2/§2.2.3/§2.1, không tích hợp §2.2 hoặc toàn Chương2.
