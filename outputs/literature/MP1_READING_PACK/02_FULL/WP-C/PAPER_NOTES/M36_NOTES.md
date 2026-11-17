# M36 — Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments

- **Canonical PDF:** `data/chap1-2_citations/M36__2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf`
- **SHA-256:** `40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3`
- **Identity:** Biagio Carboni and Walter Lacarbonara, 2016; Journal of Engineering Mechanics, Vol. 142, No. 5, 04016016; DOI: `10.1061/(ASCE)EM.1943-7889.0001072`
- **Extraction status:** `NEW_FULL_TEXT`
- **Mapped sections:** C2.4; C2.4.1; C2.4.2; C2.5; C2.5.3
- **Evidence records:** M36-E01; M36-E04; M36-E10; M36-E19

---

## A. Section objective

Nghiên cứu thiết bị giảm chấn thụ động (nonlinear tuned mass damper - TMD) ứng dụng hiện tượng trễ thắt nút (pinched hysteresis) của dây cáp uốn kết hợp sợi NiTiNOL và thép; mô hình hóa hiện tượng học bằng mô hình Bouc–Wen cải tiến kết hợp tối ưu hóa tiến hóa vi phân (differential evolution) và kiểm chứng trên bàn rung cho khung nhà 5 tầng.

## B. Concept and terminology notes

Mixed NiTiNOL–steel wire rope; cyclic bending; pinched hysteresis; modified Bouc–Wen model; differential evolution (DE) algorithm; equivalent damping ratio; resonance tuning; tuned mass damper (TMD).

## C. Evidence with precise source locators

All claims below are `AUTHOR_RESULT` or `COUNTEREVIDENCE` and are anchored to the canonical PDF physical pages. The package records in `EVIDENCE_RECORDS.jsonl` carry the claim-level provenance.

- **M36-E01 (p. 1, Abstract, NOT_APPLICABLE):** A passive absorber uses mixed NiTiNOL–steel rope bending; interwire friction plus phase transformation produces pinched hysteresis. Anchor: “mixed wire ropes are assembled in a mechanical device”. Status: `VERIFIED_FULL_TEXT`.
- **M36-E04 (p. 4, Quasi-static characterization, Fig. 2–5; Eqs. (1)–(7)):** Quasi-static MTS tests at 0.066 Hz characterize restoring-force loops; a modified Bouc–Wen model with exponential pinching is identified by differential evolution. Anchor: “The equivalent damping ratio, associated with experimental”. Status: `VERIFIED_FULL_TEXT`.
- **M36-E10 (p. 10, Optimization, Fig. 10–14; FRCs):** After optimization, equivalent damping and resonance frequency become nearly constant over a displacement-amplitude range, with slight detuning at lower excitations. Anchor: “pinched hysteresis provides an equivalent damping ratio and resonance frequency”. Status: `VERIFIED_FULL_TEXT`.
- **M36-E19 (p. 19, Shaking-table validation, Figs. 21–27; Tables 7–9):** Five-storey scaled-frame tests with the TMD report top-floor displacement reductions of about 38.32–69.12% and acceleration reductions of about 39.08–72.13% for 0.023–0.045g base inputs. Anchor: “comparison between controlled and uncontrolled responses”. Status: `VERIFIED_FULL_TEXT`.

## D. Important equations and figures

Mô hình Bouc–Wen cải tiến có thành phần thắt nút hàm mũ Eqs. (1)–(7); phương trình chuyển động TMD Eqs. (8)–(19); Figs. 2–5 (vòng lặp lực–chuyển vị uốn tĩnh); Figs. 10–14 (đáp ứng tần số FRCs và hệ số cản tương đương); Figs. 21–27 (đáp ứng bàn rung); Tables 1–9.

## E. Experimental and quantitative findings

Thí nghiệm uốn quasi-static trên máy MTS ở tần số 0.066 Hz với 4 đoạn cáp hỗn hợp NiTi-ST61 (mỗi cáp gồm 61 sợi đường kính 0.63 mm, đường kính cáp 5.7 mm; tỷ lệ thể tích NiTi/thép xấp xỉ 1:2); thử nghiệm bàn rung một chiều trên mô hình khung thép 5 tầng nặng 677 kg với gia tốc nền 0.023–0.045g.

Nhận dạng tham số mô hình Bouc–Wen đạt sai số MSE dưới 0.37% so với vòng lặp thực nghiệm [M36-E04]. Thiết bị TMD giúp giảm 38.32% đến 69.12% chuyển vị đỉnh và giảm 39.08% đến 72.13% gia tốc đỉnh của khung nhà [M36-E19].

## F. Cross-paper comparisons

- **So sánh với M24 (Barsi, Carboni, Lacarbonara 2025):**
  - Cùng nhóm tác giả nghiên cứu cơ học cáp kim loại dưới tải uốn chu kỳ. M24 đi sâu vào bản chất cấu tạo vi mô (constitutive contact mechanics) để suy ra các cận độ cứng giải tích (eigenstrain stick/slip bounds) trong uốn thuần túy. Ngược lại, M36 sử dụng mô hình hiện tượng học vĩ mô (phenomenological Bouc–Wen) nhằm mô tả trọn vẹn diện tích tiêu tán năng lượng và hình dạng thắt nút (pinched hysteresis) phục vụ bài toán động lực học công trình.
- **So sánh với M28 (Narjabadifam et al. 2024):**
  - M36 thực hiện thí nghiệm vật lý thực tế trên bàn rung cho một thiết bị TMD uốn hoàn chỉnh dùng cáp hỗn hợp NiTi–thép; trong khi phần địa chấn và phản ứng động của cáp NiTi trong M28 hoàn toàn là mô phỏng số Abaqus dưới kích động El Centro.
- **So sánh với M23 (Zhang et al. 2021):**
  - M23 giải bài toán uốn tĩnh đơn điệu của bó dây thép song song bằng phương pháp dầm phân lớp giải tích với liên kết trượt tuyến tính (không có hysteresis, không có tiêu tán chu kỳ). M36 khảo sát uốn chu kỳ biên độ lớn, làm xuất hiện rõ rệt sự kết hợp giữa biến dạng trễ siêu đàn hồi của sợi NiTi và ma sát trượt giữa các sợi dây.

## G. Limitations and counterevidence

1. **Bản chất hiện tượng học (Phenomenological formulation) [M36-E04]:** Mô hình Bouc–Wen cải tiến là mô hình khớp đường cong thực nghiệm (curve-fitting), không xuất phát từ định luật tiếp xúc hay cơ học vi mô giữa các sợi dây.
2. **Hiện tượng lệch cộng hưởng ở biên độ nhỏ (Low-amplitude detuning) [M36-E10]:** Độ cứng tương đương và hệ số cản chỉ duy trì ổn định trong một dải biên độ kích động nhất định; ở mức kích động thấp, thiết bị bị lệch tần số cộng hưởng thiết kế.
3. **Ảnh hưởng ma sát ký sinh:** Ma sát lăn tại cơ cấu dẫn hướng con lăn của TMD đóng góp vào phản lực cản đo được, không hoàn toàn chỉ do ma sát nội tại giữa các sợi cáp.
4. **Phạm vi kiểm chứng giới hạn:** Thí nghiệm động lực học chỉ thực hiện với kích động điều hòa một chiều ở nhiệt độ phòng, chưa kiểm chứng với dao động băng rộng ngẫu nhiên hay dải biến thiên nhiệt độ rộng.

## H. Relevance to MP1

- **Cơ chế hình thành vòng lặp trễ uốn (C2.4, C2.4.1, C2.4.2, C2.5, C2.5.3):** M36 là bằng chứng trực tiếp cho thấy uốn bó dây có chứa sợi NiTi dưới tác dụng của ma sát giữa các sợi sẽ tạo ra vòng lặp trễ pinched hysteresis đặc trưng.
- **Phương pháp nhận dạng tham số vòng lặp uốn:** Cung cấp thuật toán tối ưu hóa tiến hóa vi phân (DE) đã được kiểm chứng để nhận dạng tham số mô hình từ dữ liệu uốn thực nghiệm của máy kéo nén MTS, có thể áp dụng trực tiếp cho việc xử lý số liệu thí nghiệm uốn của bó dây TiNi trong MP1.
- **Ranh giới áp dụng:** M36 nghiên cứu cáp hỗn hợp thép-NiTi với ma sát thụ động trong thiết bị TMD; MP1 tập trung vào bó dây TiNi thuần túy có ma sát điều khiển chủ động bằng áp suất dương từ piston.

## I. Reading route

1. **Abstract & Sec. 1 (pp. 1–2):** Nắm ý tưởng kết hợp hiệu ứng siêu đàn hồi của sợi NiTi với ma sát trượt giữa các sợi cáp để tạo pinched hysteresis.
2. **Sec. 2 (pp. 2–5, Figs. 2–5):** Đọc kỹ sơ đồ thí nghiệm uốn tĩnh chu kỳ trên máy MTS, quan sát hình dạng vòng lặp pinched hysteresis và các phương trình Bouc–Wen cải tiến Eqs. (1)–(7).
3. **Sec. 3 (pp. 5–8):** Nắm quy trình nhận dạng tham số bằng giải thuật tiến hóa vi phân (DE).
4. **Sec. 4 (pp. 8–13, Figs. 10–14):** Khảo sát đồ thị đáp ứng tần số (FRCs) và sự phụ thuộc của hệ số cản/tần số riêng tương đương vào biên độ dao động.
5. **Sec. 5 (pp. 14–20, Figs. 21–27, Tables 7–9):** Xem kết quả kiểm chứng giảm chấn thực tế trên mô hình khung 5 tầng đặt trên bàn rung.

## J. Questions for human writing

1. **Mô hình hóa vòng lặp lực–độ võng uốn chu kỳ (C2.4.1, C2.5.3):** Khi phân tích thí nghiệm uốn chu kỳ của bó dây TiNi trong MP1, nên ưu tiên dùng mô hình hiện tượng học Bouc–Wen (như M36) để mô tả nhanh pinched hysteresis hay xây dựng mô hình tiếp xúc vi mô từng sợi?
2. **Đóng góp của ma sát so với chuyển pha SMA (C2.4.2, C2.5):** Trong vòng lặp pinched hysteresis của bó dây TiNi, làm thế nào để tách biệt phần năng lượng tiêu tán do chuyển pha siêu đàn hồi của bản thân vật liệu TiNi với phần tiêu tán do ma sát trượt giữa các sợi dây dưới áp suất piston?
3. **Ảnh hưởng của áp suất tiếp xúc lên hình dạng vòng lặp (C2.5.3):** Khi tăng áp suất piston dẫn động bằng lò xo SMA trong MP1, diện tích vòng lặp pinched hysteresis và độ cứng uốn secant thay đổi như thế nào so với trường hợp cáp uốn thụ động trong M36?

## K. Unresolved evidence

1. Bộ tham số mô hình Bouc–Wen trong M36 được tối ưu hóa cho cấu hình cáp xoắn hỗn hợp NiTi-thép ở nhiệt độ phòng; không thể áp dụng trực tiếp cho bó dây TiNi thẳng có gia nhiệt điều khiển pha của MP1.
2. Thí nghiệm uốn trong M36 áp dụng cho đoạn cáp ngắn uốn cong qua con lăn; ranh giới truyền lực và phân bố ứng suất khác với cấu hình ngàm-tự do hoặc uốn 3 điểm của bó dây MP1.
