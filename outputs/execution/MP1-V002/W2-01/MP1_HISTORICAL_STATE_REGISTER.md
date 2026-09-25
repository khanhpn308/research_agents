# MP1 — Sổ Đăng ký Trạng thái Lịch sử (Historical State Register)

> **Mã quy trình:** `MP1-E1-W2-01`  
> **Phiên bản:** Canonical State Reconstruction V2  
> **Ngày lập:** 2026-09-25  
> **Nguyên tắc cốt lõi:** State-at-Time Rule — Phản ánh chính xác những gì được tin tưởng, bằng chứng tồn tại, và quyết định tại từng thời điểm lịch sử; không viết lại quá khứ bằng hiểu biết hiện tại.

---

## 1. Bảng Tổng quan 16 Trạng thái Lịch sử (States S01–S16)

| State ID | Giai đoạn / Ngày | Git Commit | Vòng kiểm chứng | Sự kiện Lịch sử | Trạng thái Claim tại thời điểm | Quyết định tại thời điểm | Bị thay thế? | Trạng thái Canonical hiện tại |
|:---:|:---:|:---:|:---:|:---|:---|:---|:---:|:---:|
| **S01** | Phase 10 (2026-09-22) | `0fdbf89fea7f1cd18c64db93c1029c5e499e5a9f` | MP1-PRE | Mentor đề xuất kiến trúc hệ thống | `PROPOSED_ALTERNATIVE` | Mở MP1 dưới dạng hướng thay thế | Có (bởi S04) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S02** | Phase 10/11 (2026-09-22) | `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79` | MP1-V001 | Phân rã kiến trúc thành C1–C8 | `ACTIVE_CLAIMS_C1_TO_C8` | Lập kế hoạch kiểm chứng V001 | Có (bởi S04) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S03** | Phase 11 (2026-09-22) | `3d152e951711a15d9f86946df99f22785a8be9a4` | MP1-V001 | Thiết lập ma trận 10 bài V001 | `UNDER_AUDIT` | Chạy runner kiểm chứng V001 | Có (bởi S04) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S04** | Phase 11 (2026-09-22) | `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7` | MP1-V001 | Kết luận MP1-V001 audit | `C1-C4 CLOSED, C8 PREEMPTED` | `PIVOT_TO_MECHANICS_CORE` | Có (bởi S06) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S05** | Phase 12/13 (2026-09-22) | `8494d02ff7c1c57184ab5770baf006bc79d4ddbb` | MP1-V002 | Xác lập Targets T1, T2, T3 | `TARGETS_T1_T2_T3_ACTIVE` | Khởi động citation chasing V002 | Có (bởi S06) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S06** | Phase 14 (2026-09-24) | `e9685a65263635cffd4d946e8763c3417b59eb0d` | MP1-V002 | Audit 8 bài báo toàn văn đầu tiên | `SUBSTANTIALLY_NARROWED` | Đóng T1, giữ T2, hẹp T3 | Có (bởi S08) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S07** | Phase 15 (2026-09-24) | `748c943afecae0a0d1157eaa6ab192ed55aeb57f` | MP1-V002 | Sàng lọc 187 trích dẫn | `METADATA_SCREENED` | Nạp Reedlunn 2013 và Fang 2019 | Có (bởi S08) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S08** | Phase 16–18 (2026-09-25) | `5bb0c9087b638d132e7f915a1f0fc662fd30ca21` | MP1-V002 | Audit ma trận 10 bài báo | `SUBSTITUTION_INSUFFICIENT` | Giữ nguyên mechanics core | Có (bởi S10) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S09** | Phase 22 St.1 (2026-09-25) | `af9e7a59b101ac68334eadc9ede33b1b48236622` | MP1-V002 | Xuất 11 mechanics trace packets | `TRACE_PACKETS_EMITTED` | Chuyển giao phản biện Astra | Có (bởi S10) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S10** | Phase 22 St.2 (2026-09-25) | `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d` | MP1-V002 | Astra phản biện 12 lỗ hổng G01–G12 | `CRITICALLY_CHALLENGED` | Chấp nhận 100% phản biện | Có (bởi S12) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S11** | Phase 22 St.2/3 (2026-09-25) | `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d` | MP1-V002 | Khóa ma trận 16 bài toàn văn | `16_PAPERS_INGESTED` | Cố định ma trận tại commit HEAD | Có (bởi S12) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S12** | Phase 22 St.3 (2026-09-25) | `3a216d680b6e5d4c263121afee0577ac86e530ac` | MP1-V002 | Ban hành Remediation & Báo cáo 24Ch | `REMEDIATED_CORE_FORMULATED` | H0a bác bỏ, H0b giữ; P3 hạ cấp | Có (bởi S13) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S13** | Phase 23 (2026-09-25) | `313cdf2e5e0f6fae5383f83f631787a9fa1a88a9` | MP1-V002 | Đóng phủ sóng trích dẫn 15/15 | `COVERAGE_CLOSED_NO_KILL` | Đạt điều kiện dừng (stop condition) | Có (bởi S14) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S14** | Phase 24 (2026-09-25) | `73b635433237f2682accd4b7799c566fe1e80871` | MP1-V002 | Final MP1-V002 Adjudication | `SURVIVES_TARGETED_CITATION_CHASE` | Đủ điều kiện so sánh liên hướng | Có (bởi S15) | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S15** | Phase 25 (2026-09-25) | `bccdb5e21ac825d2f116957bb6768c734eda35e4` | CROSS-DIR | Phán quyết liên hướng D1/M1 vs MP1 | `D1_M1_SELECTED` | Khóa D1/M1 có điều kiện; lưu trữ MP1 | Không | `CLOSED_ARCHIVED_ALTERNATIVE` |
| **S16** | Phase 26/Curr (2026-09-25) | `0ade68e73d93c38618b366a000ac7a01215a3936` | CANONICAL | Trạng thái chuẩn hóa & Kickoff V2 | `CLOSED_ARCHIVED_VIABLE_ALT` | Cố định ranh giới; chạy W2-01 | Không | `CLOSED_ARCHIVED_ALTERNATIVE` |

---

## 2. Chi tiết Từng Trạng thái Lịch sử

### S01 — Mentor Proposal (Phase 10)
- **Ngày:** 2026-09-22 10:52:38 +0700
- **Commit:** `0fdbf89fea7f1cd18c64db93c1029c5e499e5a9f`
- **Vòng kiểm chứng:** `MP1-PRE`
- **Tệp nguồn:** `docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md`
- **Sự kiện:** Mentor đề xuất hướng nghiên cứu thay thế: bó dây NiTi siêu đàn hồi + giam giữ áp suất dương + kẹt ma sát giữa các dây + biến đổi độ cứng uốn + nguồn áp suất xi lanh/piston dẫn động bằng SMA tùy chọn.
- **Quan điểm khoa học tại thời điểm:** Tổ hợp hệ thống được xem là có tiềm năng tính mới ở cấp độ thiết bị tích hợp.
- **Bằng chứng tại thời điểm:** Đề xuất dạng lời/phác thảo của mentor; tập khám phá 54 bài báo ban đầu.
- **Quyết định tại thời điểm:** Không bác bỏ hoặc bảo vệ theo cảm tính; mở MP1 như một hướng thay thế cần kiểm chứng độc lập theo quy tắc falsification. Giữ nguyên D1/M1 làm baseline.
- **Tính chất:** Đã bị thay thế (`later_superseded = true` bởi S04).
- **Diễn giải được sửa sau này:** Lắp ghép thiết bị không tự tạo tính mới; từng thành phần đều đã có tiền nhiệm trực tiếp.

---

### S02 — Claim Decomposition C1–C8 (Phase 10/11)
- **Ngày:** 2026-09-22 10:52:41 +0700
- **Commit:** `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`
- **Vòng kiểm chứng:** `MP1-V001`
- **Tệp nguồn:** `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
- **Sự kiện:** Phân rã kiến trúc thành 8 khẳng định độc lập C1–C8:
  - C1: Kẹt sợi/dây kim loại tạo biến đổi độ cứng.
  - C2: Kẹt bằng áp suất dương.
  - C3: Kết hợp SMA và jamming trong cùng thiết bị.
  - C4: Nguồn áp suất tích hợp/nhỏ gọn.
  - C5: Dây NiTi siêu đàn hồi tự thân làm môi trường ma sát trượt.
  - C6: Áp suất dương trực tiếp giam giữ bó dây NiTi.
  - C7: Ghép cặp siêu đàn hồi NiTi, trượt ma sát, áp suất và độ cứng uốn.
  - C8: Cơ cấu xi lanh/piston SMA cấp áp suất kẹt.
- **Quan điểm khoa học tại thời điểm:** Việc phân rã giúp phát hiện chính xác khẳng định nào đã có tiền nhiệm và khẳng định nào còn mở.
- **Quyết định tại thời điểm:** Lập ma trận bằng chứng toàn văn để kiểm tra độc lập từng claim.
- **Tính chất:** Đã bị thay thế (`later_superseded = true` bởi S04).

---

### S03 — MP1-V001 Evidence Matrix (Phase 11)
- **Ngày:** 2026-09-22 12:33:22 +0700
- **Commit:** `3d152e951711a15d9f86946df99f22785a8be9a4`
- **Vòng kiểm chứng:** `MP1-V001`
- **Tệp nguồn:** `outputs/verification/MP1-V001/verification_matrix.json`
- **Sự kiện:** Nạp 10 bài báo toàn văn PDF vào ma trận kiểm chứng V001 (Bai 2022, Liu 2021, Zhang & Yao 2026, Takashima lineage, Huynh 2022, Wang 2024,...).
- **Quan điểm khoa học tại thời điểm:** 10 bài báo toàn văn này đủ để đối chiếu trực tiếp với các khẳng định C1–C8.
- **Quyết định tại thời điểm:** Kích hoạt runner đối kháng tự động để đánh giá mức độ tiền nhiệm.
- **Tính chất:** Đã bị thay thế (`later_superseded = true` bởi S04).

---

### S04 — MP1-V001 Audit Closure (Phase 11)
- **Ngày:** 2026-09-22 16:00:18 +0700
- **Commit:** `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7`
- **Vòng kiểm chứng:** `MP1-V001`
- **Tệp nguồn:** `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- **Sự kiện:** Hoàn thành thẩm định MP1-V001, ra phán quyết `PIVOT_TO_MECHANICS_CORE`.
- **Kết quả claim tại thời điểm:**
  - C1 (kẹt dây): `closed` (Bai 2022, Zhang & Yao 2026).
  - C2 (áp suất dương): `closed` (Liu 2021, Zhang & Yao 2026).
  - C3 (SMA + jamming): `closed` (Takashima 2010–2015, Matsumoto 2022).
  - C4 (nguồn nhỏ gọn): `closed` (Huynh 2022, Wang 2024).
  - C8 (piston SMA): `substantially_preempted` (thay thế bộ chấp hành, không có tính mới cơ học).
  - C5, C6, C7: `open_in_supplied_corpus`.
- **Quan điểm khoa học tại thời điểm:** Tính mới cấp kiến trúc hệ thống đã bị phá hủy hoàn toàn. Đề tài chỉ còn cơ hội nếu cơ học tiếp xúc lõi (C5–C7) đứng vững.
- **Quyết định tại thời điểm:** `PIVOT_TO_MECHANICS_CORE` với độ tin cậy cao (`confidence = high`). Rút lui khỏi mọi tuyên bố lắp ghép thiết bị.

---

### S05 — Mechanics Core & Targets T1–T3 (Phase 12/13)
- **Ngày:** 2026-09-22 10:52:43 +0700
- **Commit:** `8494d02ff7c1c57184ab5770baf006bc79d4ddbb`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`
- **Sự kiện:** Thiết lập giao thức tra cứu trích dẫn có mục tiêu MP1-V002, định nghĩa 3 mục tiêu kiểm chứng đối kháng:
  - **T1:** Dây NiTi tiếp xúc và trượt ma sát tương đối tạo độ cứng uốn.
  - **T2:** Áp suất dương ngoài nén hướng kính bó dây kim loại/NiTi, làm đổi lực pháp tuyến và độ cứng uốn.
  - **T3:** Ghép cặp phản ứng siêu đàn hồi NiTi với tiếp xúc/trượt, áp suất giam giữ, trễ và độ cứng.
  - **Parameter-substitution kill test:** Nếu khung lý thuyết sợi đàn hồi hiện hữu chỉ cần thay thế tham số vật liệu NiTi là đủ mô tả, mechanics core bị loại bỏ.
- **Quan điểm khoa học tại thời điểm:** Ba mục tiêu này cô lập câu hỏi cơ học duy nhất còn sống sót.
- **Quyết định tại thời điểm:** Dừng tìm kiếm diện rộng; tiến hành tra cứu trích dẫn xuôi/ngược có mục tiêu quanh các anchor papers.

---

### S06 — Initial 8-Paper Full-Text Audit (Phase 14)
- **Ngày:** 2026-09-24 18:38:12 +0700
- **Commit:** `e9685a65263635cffd4d946e8763c3417b59eb0d`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`
- **Sự kiện:** Thẩm định tập 8 bài báo toàn văn đầu tiên trong V002.
- **Kết quả claim tại thời điểm:**
  - Trạng thái: `SUBSTANTIALLY_NARROWED`.
  - T1: `closed_by_full_text` (cáp, bó sợi và bện NiTi có tiếp xúc ma sát nội đã được nghiên cứu sâu trong Carboni, Vahidi,...).
  - T2: `open_in_current_full_text_set` (chưa thấy thí nghiệm uốn bó dây NiTi dưới áp suất giam giữ chủ động biến thiên).
  - T3: `substantially_preempted` (sự kết hợp giữa chuyển pha NiTi và ma sát tiếp xúc đã được mô hình hóa).
- **Quyết định tại thời điểm:** Thu hẹp đề tài vào miền uốn bó dây dưới áp suất giam giữ điều khiển.

---

### S07 — Citation Metadata Triage (Phase 15)
- **Ngày:** 2026-09-24 23:20:06 +0700
- **Commit:** `748c943afecae0a0d1157eaa6ab192ed55aeb57f`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `docs/project/RESEARCH_LOG.md`
- **Sự kiện:** Sàng lọc siêu dữ liệu 187 bản ghi trích dẫn (178 bản ghi duy nhất). Phân loại: 0 kill trực tiếp, 12 bài tiềm năng, 85 giữ siêu dữ liệu, 81 loại trừ.
- **Quyết định tại thời điểm:** Không tải ồ ạt 12 bài; chỉ nâng cấp 2 bài đánh trực tiếp vào bài toán thay thế tham số: Reedlunn et al. (2013, Part II) và Fang et al. (2019).

---

### S08 — 10-Paper Matrix Audit (Phases 16–18)
- **Ngày:** 2026-09-25 00:34:17 +0700
- **Commit:** `5bb0c9087b638d132e7f915a1f0fc662fd30ca21`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `docs/project/MP1-V002_CURRENT_HANDOFF.md`
- **Sự kiện:** Chạy lại audit trên ma trận 10 bài báo toàn văn.
- **Kết quả claim tại thời điểm:**
  - Bài toán thay thế tham số: `insufficient` (`existing_elastic_fiber_model_appears_sufficient = false`, `niti_requires_distinct_constitutive_contact_coupling = false`).
  - Chưa đủ bằng chứng để bác bỏ hoàn toàn, cũng chưa đủ bằng chứng để khẳng định luật ghép cặp mới.
- **Quyết định tại thời điểm:** Duy trì mechanics core; chuẩn bị các gói trích xuất cơ học chi tiết (trace packets).

---

### S09 — Stage 1 Mechanics Trace Packets (Phase 22 Stage 1)
- **Ngày:** 2026-09-25 15:28:00 +0700
- **Commit:** `af9e7a59b101ac68334eadc9ede33b1b48236622`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/00_PACKET_MANIFEST.md`
- **Sự kiện:** Gemini Flash trích xuất 11 gói bằng chứng truy vết cơ học (W01–W11) đối soát chi tiết từng khẳng định.
- **Quyết định tại thời điểm:** Chuyển giao toàn bộ 11 gói bằng chứng sang GPT-5.6 Astra để phản biện khoa học đối kháng.
- **Lưu ý lịch sử:** Gói W08 chứa lỗi thực tế gán chuyển pha NiTi cho cấu hình cáp thép S2a của Carboni.

---

### S10 — Stage 2 Astra Adversarial Critique (Phase 22 Stage 2)
- **Ngày:** 2026-09-25 16:06:18 +0700
- **Commit:** `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md`
- **Sự kiện:** GPT-5.6 Astra công bố báo cáo phản biện độc lập với 12 lỗ hổng trọng yếu G01–G12:
  - **G01:** H0 chưa nhất quán (đánh đồng mô-đun hằng với mô hình NiTi cấu thành + tiếp xúc đã biết).
  - **G02:** Áp suất chủ động P3 bị ngộ nhận là nguyên lý cơ học mới thay vì điều kiện biên tải trọng.
  - **G03:** Chưa chứng minh chuyển pha và trượt giữa các dây cùng tồn tại trong miền vận hành.
  - **G04:** Đáp ứng uốn vĩ mô không thể nhận diện riêng rẽ các cơ chế.
  - **G05:** W08 gán sai vật liệu Carboni (S2a là cáp thép ST49, S1a mới là NiTi).
  - **G06:** Đánh đồng mô hình toán, khớp số liệu và kiểm chứng nhân quả.
  - **G07:** Dùng kết quả rút gọn động học của Reedlunn vượt quá phạm vi.
  - **G08:** Nguy cơ bù trừ tham số khi khớp đường cong uốn (Fang 2019).
  - **G09:** Chưa kiểm chứng sự truyền áp suất buồng sang lực pháp tuyến tiếp xúc.
  - **G10:** Chưa đạt điều kiện dừng trích dẫn nhưng diễn đạt như thể chỉ còn thiếu áp suất.
  - **G11:** Mâu thuẫn trạng thái giữa tệp audit JSON (ghi `established`) và handoff (ghi `insufficient`).
  - **G12:** Chưa chuẩn hóa định nghĩa độ cứng uốn (tiếp tuyến vs cát tuyến vs động học).
- **Quyết định tại thời điểm:** Tiếp thu toàn diện 100% phản biện của Astra, không phòng thủ; mở đợt tổng hiệu chỉnh Stage 3.

---

### S11 — Reconciled 16-Paper Full-Text Matrix (Phase 22 Stage 2/3)
- **Ngày:** 2026-09-25 16:06:18 +0700
- **Commit:** `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `outputs/verification/MP1-V002/verification_matrix.json`
- **Sự kiện:** Khóa chính thức quy mô ma trận kiểm chứng tại **16 bài báo toàn văn PDF**, giải quyết dứt điểm mâu thuẫn trạng thái G11.
- **Danh mục 16 bài:** Reedlunn I (2013), Reedlunn II (2013), Carboni (2016), Fang (2019), Ting-Long (2021), Falcetelli (2024), Barsi (2025), Kang (2020), Carboni (2015), Niu (2023), Vahidi (2022), de Paula (2021), Xin Liu (2013), Tjahjanto (2017), Liu (2026), Silva (2022).
- **Quyết định tại thời điểm:** Đặt toàn bộ phân tích khoa học trên nền tảng 16 bài báo này.

---

### S12 — Stage 3 Scientific Remediation (Phase 22 Stage 3)
- **Ngày:** 2026-09-25 16:29:55 +0700
- **Commit:** `3a216d680b6e5d4c263121afee0577ac86e530ac`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md`, `docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md`
- **Sự kiện:** Hoàn thành 11 báo cáo worker W01–W11, ma trận đối soát G01–G12, và báo cáo tổng thể 24 chương.
- **Các sửa đổi khoa học then chốt:**
  1. Tách $H_0$ thành 3 tầng: $H_{0a}$ (mô-đun hằng: Bác bỏ — `REFUTED`), $H_{0b}$ (khung lý thuyết NiTi cấu thành + tiếp xúc Coulomb hiện hữu: Chưa bị bác bỏ — `NOT FALSIFIED`), $H_1$ (luật ghép cặp mới: Chưa có bằng chứng — `INSUFFICIENT`).
  2. Hạ cấp áp suất chủ động $P_3$: chỉ là giao thức điều khiển thực nghiệm (boundary condition), không phải nguyên lý cơ học mới.
  3. Sửa chữa 100% lỗi Carboni 2015: S2a = ST49 thép, S1a = NiTi7 chịu kéo-uốn kết hợp.
  4. Hiệu chỉnh bảo thủ Reedlunn 2013 và Fang 2019; thiết lập thang bậc 5 tầng độ tin cậy mô hình.
  5. Thừa nhận điều kiện dừng trích dẫn chưa đạt (`stop_condition_satisfied = false`).
- **Quyết định tại thời điểm:** Không tuyên bố MP1 đã sống sót hoàn toàn; bắt buộc phải xử lý hai nhánh trích dẫn ngược B11 và B12 trước khi tiến hành adjudication.

---

### S13 — Stage 4 Citation Coverage Closure (Phase 23)
- **Ngày:** 2026-09-25 16:27:35 +0700
- **Commit:** `313cdf2e5e0f6fae5383f83f631787a9fa1a88a9`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `outputs/verification/MP1-V002/citation_coverage.json`, `outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md`
- **Sự kiện:** Hoàn thành sàng lọc 22 tài liệu trích dẫn ngược của B11 (Kang et al. 2020) và 46 tài liệu của B12 (Barsi et al. 2025). Tổng cộng 68 bản ghi thô (67 bản ghi duy nhất). Không phát hiện bài báo nào tiêu diệt trực tiếp chuỗi cơ học uốn bó dây NiTi dưới áp suất giam giữ.
- **Trạng thái trích dẫn đạt được:**
  - Trích dẫn ngược (backward): `9/9` đã duyệt.
  - Trích dẫn xuôi (forward): `6/6` đã duyệt.
  - Tổng số hướng: `15/15` hoàn tất (`100%`).
  - `stop_condition.satisfied = true`, `search_cutoff_date = 2026-09-25`.
- **Quyết định tại thời điểm:** Dừng quy trình tra cứu trích dẫn; chuyển giao hồ sơ sang Final Adjudication Gate.

---

### S14 — Stage 5 Final MP1-V002 Adjudication (Phase 24)
- **Ngày:** 2026-09-25 16:36:09 +0700
- **Commit:** `73b635433237f2682accd4b7799c566fe1e80871`
- **Vòng kiểm chứng:** `MP1-V002`
- **Tệp nguồn:** `outputs/verification/MP1-V002/FINAL_ADJUDICATION.json`, `FINAL_ADJUDICATION.md`
- **Sự kiện:** Mô hình GPT-6 Sol High chạy thẩm định phán quyết cuối cùng cho MP1-V002 (Run ID: `20260925T093414Z`).
- **Phán quyết chính thức:**
  ```text
  protocol_outcome           = SURVIVES_TARGETED_CITATION_CHASE
  confidence                 = high
  direct_kill_found          = false
  citation_coverage_closed   = true
  msc_topic_readiness        = READY_FOR_CROSS_DIRECTION_COMPARISON
  astra_escalation_required  = false
  ```
- **Phạm vi bảo toàn:** MP1 sống sót trong phạm vi giao thức V002 dưới dạng một câu hỏi phân biệt mô hình hẹp đối kháng với $H_{0b}$. Không chứng minh tính mới phổ quát.
- **Quyết định tại thời điểm:** Đủ điều kiện đưa vào so sánh đối đầu trực tiếp với D1/M1.

---

### S15 — Stage 6 Final Cross-Direction Adjudication (Phase 25)
- **Ngày:** 2026-09-25 16:43:07 +0700
- **Commit:** `bccdb5e21ac825d2f116957bb6768c734eda35e4`
- **Vòng kiểm chứng:** `CROSS-DIRECTION`
- **Tệp nguồn:** `outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json`, `FINAL_DIRECTION_ADJUDICATION.md`
- **Sự kiện:** So sánh đối đầu giữa D1/M1 và MP1 trên 18 tiêu chí khoa học, khả thi và rủi ro thực thi luận văn Thạc sĩ.
- **Phán quyết liên hướng:**
  ```text
  selected_direction = D1_M1
  decision           = LOCK_WITH_FEASIBILITY_GATE
  confidence         = medium
  ```
- **Lý do lựa chọn D1/M1:**
  1. D1/M1 có mô hình cụ thể $M_1$ (Zhang et al. 2025) để đánh giá miền hiệu lực; MP1 chưa khóa được cặp mô hình cụ thể.
  2. D1/M1 ít tầng ghép cặp gây nhiễu; MP1 đối mặt với sự bất định nghiêm trọng về miền cùng tồn tại chuyển pha + trượt.
  3. Gánh nặng đo đạc của D1/M1 khả thi hơn; MP1 đòi hỏi đo đạc vi mô (DIC/FBG/ảnh nhiệt) để tránh thoái hóa về $H_{0b}$.
  4. Kết quả phủ định của D1/M1 vẫn tạo ra giá trị khoa học (bản đồ hiệu lực); trong khi nếu $H_{0b}$ giải thích được MP1 thì tính mới bị triệt tiêu hoàn toàn.
- **Định vị của MP1:** Lưu trữ như một **phương án thay thế có giá trị khoa học** (`viable alternative`), không bị bác bỏ về mặt học thuật, nhưng không được chọn làm hướng luận văn chính.

---

### S16 — Canonical HEAD State & Kickoff V2 (Phase 26 / Current)
- **Ngày:** 2026-09-25 16:58:43 +0700 / 21:24:12 +0700
- **Commit:** `0ade68e73d93c38618b366a000ac7a01215a3936` (HEAD) + working tree kickoff
- **Vòng kiểm chứng:** `CANONICAL_HEAD`
- **Tệp nguồn:** `docs/project/research_state.json`, `outputs/execution/MP1-V002/MP1_EXECUTION_KICKOFF_V2.md`
- **Sự kiện:** Đồng bộ toàn diện repository state; ban hành MP1 Kickoff V2 ghi nhận 4 làm rõ C-01 đến C-04; khởi động Worker W2-01 ở chế độ read-only.
- **Trạng thái canonical hiện tại:**
  - Hướng nghiên cứu được chọn: `D1_M1` (`LOCK_WITH_FEASIBILITY_GATE`).
  - MP1: `closed_archived_viable_alternative`.
  - Phủ sóng trích dẫn: Đóng hoàn toàn (15/15).
  - Tìm kiếm diện rộng: Đóng hoàn toàn.
- **Quyết định tại thời điểm:** Khóa phạm vi; chỉ thực hiện tái cấu trúc lịch sử và dòng dõi khoa học ở chế độ read-only.

---

## 3. Các Diễn giải Bị Thay thế và Được Hiệu chỉnh

### 3.1. Các Diễn giải Bị Thay thế (Superseded Interpretations)
1. **Tính mới cấp tổ hợp kiến trúc (C1–C8):** Ban đầu tại S01 được xem là có thể bảo vệ; đã bị thay thế hoàn toàn tại S04 bởi phán quyết `PIVOT_TO_MECHANICS_CORE` khi phát hiện các công trình tiền nhiệm trực tiếp.
2. **Áp suất giam giữ chủ động P3 là nguyên lý cơ học mới:** Ban đầu tại S05/S06 được coi là yếu tố cốt lõi phân biệt MP1 với cáp thông thường; đã bị thay thế tại S12 thành một điều kiện biên điều khiển thực nghiệm (boundary condition).
3. **Phép thử thay thế tham số nhị phân H0 vs H1:** Ban đầu tại S05/S08 được đóng khung như một bài toán đối đầu trực tiếp; đã bị thay thế tại S12 bởi cấu trúc 3 tầng $H_{0a}$ (bác bỏ), $H_{0b}$ (chưa bị bác bỏ), và $H_1$ (chưa có bằng chứng).
4. **Trạng thái điều kiện dừng trích dẫn mở (`satisfied = false`):** Đúng tại thời điểm Stage 3 (S12); đã bị thay thế tại Stage 4 (S13) khi các nhánh B11 và B12 được sàng lọc hoàn tất (15/15).
5. **Quy mô ma trận kiểm chứng 8 bài và 10 bài:** Là các trạng thái snapshot tạm thời (S06, S08); đã bị thay thế chính thức tại S11 bởi ma trận 16 bài báo toàn văn.
6. **MP1 là đề tài luận văn ứng viên đang hoạt động:** Được xác nhận đủ điều kiện tại S14; đã bị thay thế tại S15 khi phán quyết liên hướng chọn D1/M1 và lưu trữ MP1 làm phương án dự phòng.

### 3.2. Các Diễn giải Được Hiệu chỉnh (Corrected Interpretations)
1. **Sai sót cấu hình vật liệu Carboni 2015:** Gói trích xuất W08 (S09) khẳng định cấu hình S2a chứng minh chuyển pha NiTi dưới uốn thuần; phản biện Astra G05 (S10) và rà soát W04 (S12) đã đối soát trực tiếp Bảng 4 trong tệp PDF gốc và đính chính: S2a là cáp thép ST49 thuần ma sát; S1a mới là cáp NiTi7 chịu ứng suất kéo-uốn kết hợp. Suy luận sai đã được bóc tách hoàn toàn khỏi chuỗi bằng chứng.
2. **Rút gọn động học của Reedlunn 2013:** Ban đầu được dùng để lập luận rằng cáp NiTi thất bại do thiếu luật ghép cặp mới; hiệu chỉnh Stage 3 (S12) làm rõ nguyên nhân sai số trong mô hình Costello là do bỏ qua uốn/xoắn cục bộ ở góc bện dốc, không phải bằng chứng về một định luật cấu thành mới cho bó dây thẳng.
3. **Hiện tượng bù trừ tham số của Fang 2019:** Bổ sung cảnh báo nghiêm ngặt về tính không duy nhất của tham số khi khớp đường cong trễ uốn vĩ mô, thiết lập nguyên tắc khóa tham số độc lập trước khi đánh giá mô hình.
4. **Nhãn `established` trong tệp kiểm chứng JSON:** Giải tỏa xung đột trạng thái G11 bằng việc làm rõ nhãn này chỉ áp dụng cho việc bác bỏ mô hình đàn hồi sơ đẳng $H_{0a}$; trạng thái giữa $H_{0b}$ và $H_1$ là chưa đủ bằng chứng (`insufficient`).
5. **Định nghĩa độ cứng uốn:** Chuẩn hóa tường minh 3 đại lượng: độ cứng tiếp tuyến $D_{\text{tan}}$, cát tuyến $D_{\text{sec}}$, và động học $D_{\text{dyn}}$ theo từng nhánh tải và lịch sử biến dạng.
