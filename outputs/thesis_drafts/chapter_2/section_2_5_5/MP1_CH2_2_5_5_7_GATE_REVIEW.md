# MP1 CH2 §2.5.5 — Seven-Gate Review

**TASK_ID:** MP1-CH2-2.5.5-RESEARCH-THESIS-DRAFT  
**STATUS:** `PARTIAL_WITH_FINDINGS`
**TARGET_SECTION:** 2.5.5 — So sánh các nhóm phương pháp

## Gate 1 — Outline compliance: PASS_WITH_LIMITATIONS

B01 được đáp ứng bằng so sánh dầm giải tích/elastica, đồng nhất hóa, mô hình rút gọn hiện tượng luận, FE có tiếp xúc và thực nghiệm. Bảng nêu khả năng mô tả, tham số, chi phí, kiểm chứng và nguy cơ khớp quá mức. B02 phân biệt mô hình dự đoán, mô hình diễn giải và mô hình tham chiếu. B03 đặt H0b làm baseline cạnh tranh trước khi mở H1. Phần cuối chuyển sang §2.6, không viết §2.6.

**Finding:** không chọn mô hình MP1, topology, đại lượng uốn chính hay quy trình thí nghiệm cuối cùng.

## Gate 2 — Claim traceability: PASS_WITH_LIMITATIONS

Bốn Evidence IDs bắt buộc đã được đối chiếu: M05-E02, M07-E02, M10-E02 và M13-E03; M07-E03 được giữ như bằng chứng thực nghiệm bổ sung cho Hình 3 của M07. CSV có 20 record: `SOURCE_GROUNDED_CLAIM=11`, `INFERENCE=4`, `AUTHOR_PROPOSAL=2`, `AUTHOR_DERIVATION=0`, `PENDING_HUMAN_DECISION=1` và `DOCUMENT_COVERAGE=2`. M05 được dùng như taxonomy; M07 là comparator layer-jamming; M10 và M13 là các mô hình hiệu dụng/rút gọn theo kiến trúc riêng.

**Finding:** chín record source-grounded dựa trên bài báo; T015 và T016 là hai record source-grounded dựa trên định nghĩa giả thuyết P3 nội bộ đã được chấp nhận, không phải kết quả thực nghiệm được journal hỗ trợ. T011 đã được phân loại bảo thủ thành inference vì là tổng hợp phương pháp luận, không phải derivation.

## Gate 3 — Original PDF and model verification: PASS_WITH_FINDINGS

- M05: PDF p.10, Sec. 3.3.1, Fig. 5(g); Bảng 4 p.11. Nhãn Fig. 8 trong record cũ không được dùng trong bản thảo.
- M07: PDF p.3, Fig. 2/Sec. 2.1; p.4, Fig. 3/Sec. 2.2 (M07-E03); p.7, giới hạn. Hai lớp elastica, FE plane-strain nhiều lớp và kiểm chứng uốn ba điểm được giữ đúng phạm vi.
- M10: PDF pp.3–4, Eqs. (1)–(5), D/d/L và C. C có đơn vị phụ thuộc nguồn; E tương đương được suy ra từ đáp ứng kết cấu, không phải E vật liệu độc lập.
- M13: PDF p.5, Eq. (11), các miền I_J/I_S và nội suy bậc hai. Eq. (4) có sai thứ nguyên đã biết và không được tái bản.

Không đưa phương trình nguồn vào DOCX vì không cần thiết cho mục so sánh; do đó không có OMML phương trình hiển thị.

## Gate 4 — Cross-study synthesis: PASS

Bản thảo phân biệt taxonomy, mô hình diễn giải, mô hình hiệu dụng, mô hình hiện tượng luận, FE/contact và thực nghiệm. Không gộp R², độ cứng, tham số hoặc dữ liệu khác kiến trúc. Calibration fit được tách khỏi held-out validation; FE không được gán độ chính xác chỉ vì phức tạp hơn.

## Gate 5 — Mechanical and hypothesis limits: PASS_WITH_FINDINGS

E, EI/B, K, lực pháp tuyến cục bộ và đáp ứng toàn cục được giữ riêng. Áp suất nguồn không được đồng nhất với traction cục bộ. H0b được ghi là `NOT_FALSIFIED_LIVE_COMPETITOR`; H1 là `INSUFFICIENT_EVIDENCE`. H1 chỉ mở sau dự đoán H0b với tham số khóa thất bại có hệ thống trên dữ liệu giữ lại và sau khi kiểm soát confounders.

**Finding:** chưa có forward benchmark MP1, topology và trạng thái TiNi còn bỏ ngỏ; không có mệnh đề cận phổ quát hoặc luật cấu thành mới.

## Gate 6 — Citation and source integrity: PASS

Bốn DOI được xác minh và đánh số lần xuất hiện [1]–[4]. Mọi nguồn trong bảng và glossary quy về cùng bốn tài liệu; không có Paper ID/Evidence ID trong văn bản luận văn. Locator M05 được hiệu chỉnh theo PDF gốc. Không dùng nguồn FE bổ sung.

## Gate 7 — Vietnamese MSc and DOCX quality: PASS_WITH_FINDINGS

Văn bản tiếng Việt, một bảng so sánh năm cột và một glossary ba cột Word-native được tạo. DOCX dùng A4, Times New Roman, dòng tiêu đề bảng lặp lại, hàng không tách và không có footer workflow. ZIP/XML và cấu trúc bảng được kiểm tra tĩnh.

`WORD_RENDER_VALIDATION: NOT_VERIFIED` vì môi trường không có renderer DOCX khả dụng.  
`MICROSOFT_WORD_VALIDATION: NOT_VERIFIED` vì Microsoft Word chưa được chạy.

## H0b/H1 canonical boundary

H0b: mô hình cấu thành TiNi có xét chuyển pha + tiếp xúc Coulomb dưới áp suất như điều kiện biên ngoài, tham số được hiệu chuẩn độc lập và khóa trước dự đoán. Trạng thái: chưa bị bác bỏ. H1: luật ghép cấu thành–tiếp xúc mới mà H0b không thể dự đoán; trạng thái: chưa đủ bằng chứng. Bác bỏ H0a không suy ra H1 đúng.

## Remaining MP1 decisions

Topology dây–dây/dây–ống bao; đường truyền áp suất đến lực pháp tuyến; miền nhiệt/chuyển pha TiNi; đại lượng uốn chính và quy tắc bất định; phạm vi Bench B.

## Seven-gate result

`PARTIAL_WITH_FINDINGS` là trạng thái phù hợp: nội dung khoa học và truy xuất nguồn sẵn sàng cho rà soát học thuật, còn kiểm chứng render Word và các quyết định MP1 chưa khóa.


## Final targeted hotfix R1

- Reference [2] corrected to Y. S. Narang, J. J. Vlassak and R. D. Howe.
- Reference [3] corrected to pp. 8078–8085.
- Reference [4] corrected to *Mechanical Sciences*, vol. 17, no. 1, pp. 481–493.
- Four DOI identities and citation order [1]–[4] are unchanged; M07-E03 remains supplementary traceability.
- DOCX terminology was edited locally; English glossary headwords were preserved.
- “P3 canonical” was removed from the thesis glossary; P3 provenance remains in supporting records.
- T011 was reclassified from `AUTHOR_DERIVATION` to `INFERENCE`; total remains 20.
- DOCX retains one five-column scientific table, one three-column glossary and zero displayed equations.
- Prior independent LibreOffice review reported five readable A4 pages; current Microsoft Word validation remains `NOT_VERIFIED`.

**Updated seven-gate result:** `PARTIAL_WITH_FINDINGS`.


## Integration Changelog — mandatory pre-integration corrections

1. Reference [3] corrected from “S. Liu et al.” to “T. Liu et al.”; DOI 10.1109/LRA.2021.3097255 and pp. 8078–8085 preserved.
2. T001 terminology definition synchronized between DOCX and TERMINOLOGY.csv: “kinematic” → “động học”, with the mechanical definition unchanged.
3. Glossary sources T008 and T010 in the DOCX shortened to “Tổng hợp biên tập”; P3 provenance remains in TERMINOLOGY.csv and SOURCE_TRACEABILITY.csv.

Citation and terminology were checked by identity and content. Gate 6 remains `PASS` only after confirming the corrected [3] metadata.
