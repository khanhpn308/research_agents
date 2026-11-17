# MP1 §2.5 — Integration Changelog

TASK_ID: MP1-CH2-2.5-INTEGRATION-AND-CONSISTENCY-REVIEW

## Baseline inputs and immutability

Tất cả 25 tệp nguồn được xác nhận tồn tại và chỉ đọc. SHA-256 trước/sau giống nhau; không tệp baseline nào bị sửa.

| Tệp | SHA-256 trước | SHA-256 sau |
|---|---|---|
| `outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md` | `78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec` | `78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec` |
| `outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx` | `a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d` | `a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d` |
| `outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md` | `31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97` | `31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97` |
| `outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv` | `e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61` | `e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61` |
| `outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv` | `3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b` | `3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b` |
| `outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md` | `c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d` | `c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d` |
| `outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx` | `8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da` | `8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da` |
| `outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md` | `d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52` | `d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52` |
| `outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv` | `c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169` | `c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169` |
| `outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv` | `5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b` | `5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b` |
| `outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md` | `ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2` | `ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2` |
| `outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx` | `024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1` | `024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1` |
| `outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md` | `256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0` | `256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0` |
| `outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv` | `8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec` | `8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec` |
| `outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv` | `baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b` | `baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b` |
| `outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md` | `a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817` | `a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817` |
| `outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx` | `8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7` | `8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7` |
| `outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md` | `945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea` | `945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea` |
| `outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv` | `6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c` | `6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c` |
| `outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv` | `336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84` | `336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84` |
| `outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md` | `86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7` | `86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7` |
| `outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx` | `9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead` | `9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead` |
| `outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md` | `eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648` | `eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648` |
| `outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv` | `0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc` | `0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc` |
| `outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv` | `de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3` | `de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3` |

## Baseline acceptance states

Năm baseline đều ở trạng thái `PARTIAL_WITH_FINDINGS` hoặc tương đương; các giới hạn đã chấp nhận (M13 Eq. (4) sai thứ nguyên bị loại khỏi bản thảo; M10 không mô tả cách dựng CI; M12 5,5 lần là tỷ số lực tại 3 mm; M13 hồi quy từng đoạn không nhận dạng traction cục bộ; M15 dải Fig. 3 là 0–80 kPa; render trực quan chưa xác minh) được giữ nguyên.

## Inventory

| Tiểu mục | Đoạn | Heading | Bảng | Hàng bảng |
|---|---:|---:|---:|---|
| §2.5.1 | 43 | 9 | 2 | [5, 13] |
| §2.5.2 | 40 | 8 | 2 | [5, 13] |
| §2.5.3 | 44 | 8 | 2 | [5, 14] |
| §2.5.4 | 32 | 8 | 2 | [5, 21] |
| §2.5.5 | 26 | 0 | 2 | [6, 16] |
| **Tích hợp** | 165 paragraph objects (499 XML paragraphs) | 28 | 6 (6 XML) | [5, 5, 5, 5, 6, 68] |

## Claims and traceability

- Bản ghi truy vết gốc: **98** (18 + 20 + 18 + 22 + 20).
- Bản ghi master: **98**; mọi dòng có integrated claim ID, locator và integration action.
- Phân loại master: `{'DOCUMENT_COVERAGE': 8, 'AUTHOR_PROPOSAL': 17, 'SOURCE_GROUNDED_CLAIM': 29, 'INFERENCE': 16, 'AUTHOR_DERIVATION': 12, 'SOURCE_GROUNDED': 12, 'PENDING_HUMAN_DECISION': 2, 'P3_INTERNAL_DEFINITION': 2}`.
- T015/T016 của §2.5.5 được phân loại biên tập thành `P3_INTERNAL_DEFINITION`, giữ `P3_CANONICAL`, không gọi là bằng chứng thực nghiệm hay kết quả tạp chí.
- AUTHOR_DERIVATION, AUTHOR_PROPOSAL và PENDING_HUMAN_DECISION được giữ riêng; không biến thành SOURCE_GROUNDED_CLAIM.

## Citation integration

- 21 ánh xạ citation cục bộ → **12 DOI duy nhất**; loại 9 mục lặp danh tính.
- Ánh xạ theo `source_section + old_citation_number + canonical_doi`; citation trong đoạn, bảng và glossary dùng số tích hợp.
- Thứ tự xuất hiện lần đầu: [1] Narang, [2] Bai, [3] Crowley, [4] Zhang–Yao, [5] Barsi, [6] Caruso, [7] Fan–Liu–Ye, [8] Brancadoro, [9] Liu, [10] Huynh, [11] Yi–Fan–Liu, [12] Fan et al. tổng quan.
- Metadata đã chuẩn hóa: T. Liu et al., IEEE RA-L, tr. 8078–8085, DOI 10.1109/LRA.2021.3097255; Zhang–Yao ở Mechanical Sciences, tập 17, số 1, tr. 481–493.

## Terminology normalization

- 72 dòng terminology gốc được khử trùng theo danh tính/nghĩa thành **67 thuật ngữ**.
- Năm nhóm trùng được hợp nhất có provenance: Full slip; Bending rigidity; Parameter compensation; Model calibration; Independent validation.
- Không gộp các cặp khác cấp như E với B/EI, lực với traction/pressure, full slip với independent-wire bending, hay structural với practical identifiability.
- Glossary Word chỉ có một bảng 3 cột, dùng citation tích hợp và không chứa Paper ID/Evidence ID.

## Equation and table preservation

- OMML baseline: 5 + 4 + 6 + 0 + 0 = **15**; tích hợp: **15**; giữ nguyên subtree OMML và hai delimiter `m:d` của điều kiện trị tuyệt đối Coulomb.
- Bảng khoa học baseline: 5; tích hợp: 5. Glossary baseline: 5; tích hợp: 1 master glossary.
- M13 Eq. (4) không xuất hiện; không thêm luật cấu thành MP1 mới.

## Scientific consistency decisions

- Chuỗi lập luận được giữ: Coulomb → dính–trượt → hai cận tham chiếu → đại lượng M–κ/F–δ/T–θ và vòng trễ → bất định/nhận dạng → tiêu chí chọn mô hình → H0b trước H1.
- Full slip không bị đồng nhất với ma sát bằng không hoặc uốn dây độc lập; perfect stick không bị đồng nhất vô điều kiện với composite action.
- E, B/EI và K; áp suất nguồn, áp suất tại mẫu, lực pháp tuyến, traction; hiệu chuẩn và kiểm chứng độc lập; CI và bất định mở rộng được tách biệt.
- H0b giữ trạng thái `NOT_FALSIFIED_LIVE_COMPETITOR`; H1 giữ `INSUFFICIENT_EVIDENCE`; các quyết định topology, normal-force proxy, miền TiNi, metric chính và quy tắc bất định vẫn pending.
- Không phát hiện mâu thuẫn khoa học bắt buộc phải tự quyết; chỉ áp dụng editorial reconciliation có kiểm soát.

## Remaining limitations

- `WORD_RENDER_VALIDATION: NOT_VERIFIED`; `MICROSOFT_WORD_VALIDATION: NOT_VERIFIED` vì môi trường không có LibreOffice/Microsoft Word.
- Không tái kiểm toán toàn bộ PDF; không thêm nguồn mới; không sửa §2.3, §2.4 hoặc các output lịch sử.
- Tệp tích hợp đã kiểm tra ZIP/XML tĩnh; cần một lượt xem trực quan bằng Word/LibreOffice trước khi nộp chính thức.


## R1 final remediation (2026-10-19)

- Removed the stale footer “Mục 2.5.1 – Bản thảo nghiên cứu MP1” from the DOCX section properties, footer package part and relationship records. No replacement footer was added.
- Reconciled the seven requested glossary definitions without changing the 67 terminology identities or their provenance: Full slip, Bending rigidity, Parameter compensation, Model calibration, Independent validation, Contact traction and Reference baseline. “Traction tiếp xúc” is now “Ứng suất tiếp xúc”; the definition explicitly distinguishes contact traction from resultant normal contact force and source pressure.
- Removed `MP1_BOUNDS_STATUS assumption-dependent` from the manuscript glossary; the conditional reference limitation remains in natural Vietnamese.
- Set all five subsection headings to Heading 2 under the §2.5 Heading 1, normalized internal headings to Heading 3, normalized body prose to Times New Roman 12 pt, and normalized captions to Caption with keep-with-next.
- Set the §2.5.2 caption keep-with-next and made all table rows non-splitting; table data and five-column structure were preserved.
- Replaced generic traceability locators with claim-level paragraph, equation, table-row or documented merged-claim anchors. All 98 records have a locator and a disposition; no `UNRESOLVED_MAPPING` rows remain. Multi-equation claims list all equations explicitly.
- Source baseline check after R1: 25/25 SHA-256 values unchanged.

R1 visual rendering could not be rerun locally because LibreOffice/soffice is unavailable in this environment. The independently reported pre-R1 render was 24 A4 pages; post-R1 page count is therefore not asserted.

Locator convention: paragraph and table indices in the master CSV are zero-based `python-docx` document order; table-row labels and equation numbers are explicit anchors.
