# MP1 READING PACK — EQUATION UNVERIFIED ITEMS & SOURCE ANOMALIES LOG

- **Task ID:** MP1-LR-P2-EQ-R1
- **Target File:** EQUATION_UNVERIFIED_ITEMS.md
- **Status:** PASS WITH MONITORED ITEMS (All selected equations visually verified; author typos and extraction quirks logged)
- **Target Thesis Sections:** C1.2, C2.1–C2.5

---

## 1. MỤC ĐÍCH

Tài liệu này ghi nhận toàn bộ các phát hiện về lỗi chính tả của tác giả (author typographical errors), các điểm dị biệt trong quy ước ký hiệu, các vùng công thức có bố cục hai cột phức tạp hoặc các file PDF có hạn chế trích xuất văn bản tự động đã được phát hiện trong quá trình kiểm tra trực tiếp đối chiếu với các file PDF canonical.

Tất cả các phương trình được chọn trong WP-B, WP-C và WP-D đã được kiểm tra trực quan (visually verified) bằng cách kết xuất hình ảnh độ phân giải cao (`pdftoppm` 150 DPI) và đối chiếu ký tự. Không có phương trình nào bị suy đoán ký hiệu.

---

## 2. DANH MỤC CÁC MỤC CẦN LƯU Ý & DỊ BIỆT NGUỒN (ANOMALY LOG)

### Item 01: M18 (Zhang et al., 2025) — Lỗi in ấn hàm dấu `sing Q` tại Eq. (4)
- **Package sở hữu:** WP-B
- **Paper ID:** M18
- **Vị trí:** Physical PDF trang 4, cột 1, Eq. (4).
- **Hiện tượng:** Trong văn bản PDF chính thức, công thức (4) được in nguyên văn là:
  $$Q_{\text{eq}} = \text{sing}\, Q \frac{2}{3} \frac{\mu p A}{1 - 4 y_s^2 / h^2}$$
  Ký hiệu `sing Q` là lỗi đánh máy rõ ràng của tác giả hoặc nhà xuất bản Copernicus Publications cho hàm dấu $\operatorname{sign}(Q)$ (trong khi ở Eq. 7 tác giả viết đúng là $\operatorname{sign}(Q)$).
- **Hành động xử lý:** Đã kiểm tra trực quan trên file ảnh `M18_p4-04.png`. Khi trích dẫn trong ghi chú, ghi nhận chính xác lỗi in ấn này để người viết luận văn không nhầm lẫn với hàm lượng giác $\sin(g Q)$.
- **Trạng thái:** `VERIFIED_WITH_AUTHOR_TYPO_DOCUMENTED`.

---

### Item 02: M17 (Caruso et al., 2023) — Quy ước tải trọng $F_0$ vs $2F_0$ trong uốn 3 điểm
- **Package sở hữu:** WP-B
- **Paper ID:** M17
- **Vị trí:** Physical PDF trang 3, cột 2, Eqs. (1)–(2) và Fig. 2(b).
- **Hiện tượng:** Trong Eq. (1), tác giả viết $F_0 = \frac{2 \tau_{\text{slip}} A}{3}$. Nhưng trong Eq. (2), độ võng được viết là $w_0 = \frac{2 F_0 L^3}{48 E I_{\text{p-s}}}$, và trên trục tung của Hình 2(b), điểm trượt đầu tiên được đánh dấu là $2F_0$.
- **Giải thích cơ học:** Tác giả định nghĩa $F_0$ là lực cắt tác dụng lên một nửa nhịp của dầm uốn 3 điểm ($V = F_0 = F_{\text{total}} / 2$). Do đó, tổng tải trọng tác dụng tại điểm giữa dầm là $2F_0$. Công thức uốn $w = \frac{P L^3}{48 E I}$ với $P = 2F_0$ cho ra đúng số hạng $2F_0$ ở tử số.
- **Hành động xử lý:** Ghi chú rõ quy ước này trong từ điển biến số để tránh hiểu nhầm rằng dầm có độ võng gấp đôi dầm thông thường.
- **Trạng thái:** `VERIFIED_NOMENCLATURE_RESOLVED`.

---

### Item 03: M23 (Zhang et al., 2021) — Vị trí thực tế của Eq. (28) giữa trang 9 và trang 10
- **Package sở hữu:** WP-C
- **Paper ID:** M23
- **Vị trí:** Physical PDF trang 10, cột 1, dòng 48 (thay vì trang 9).
- **Hiện tượng:** Trong bản ghi chỉ mục `EVIDENCE_INDEX.csv` ban đầu, mỏ neo văn bản cho M23-E07 được gắn với trang 9 (nơi bắt đầu phần thảo luận về Interfacial slips and interactive forces). Tuy nhiên, phương trình giải tích tường minh Eq. (28) nằm ở đầu trang 10 của PDF.
- **Hành động xử lý:** Đã kiểm tra trực tiếp cả trang 9 và trang 10. Phương trình Eq. (28) đã được trích xuất chính xác tuyệt đối từ trang 10 và cập nhật vào `WP_C_EQUATION_NOTES.md`.
- **Trạng thái:** `LOCATOR_RECONCILED`.

---

### Item 04: M33 (Pierce & Mascaro, 2012/2013) — Khối phương trình động lực học hai cột Eqs. (15)–(36)
- **Package sở hữu:** WP-D
- **Paper ID:** M33
- **Vị trí:** Physical PDF trang 6.
- **Hiện tượng:** Khối phương trình (15)–(36) được dàn trang hai cột dày đặc với các ký hiệu đồ thị liên kết (bond graph) và vi phân ghép cặp. Việc trích xuất văn bản thô (pdftotext) có thể làm xáo trộn thứ tự các dòng phân số.
- **Hành động xử lý:** Thực hiện đúng chỉ đạo của user: Không bắt buộc chép lại toàn bộ khối (15)–(36). Đã kiểm tra trực quan và trích xuất hai phương trình cốt lõi quan trọng nhất cho MP1: Eq. (24) (mô hình trễ phân số pha Gaussian $R_m(x)$) và Eq. (31) (phương trình vi phân tốc độ sinh lực $\dot{F}$). Nếu sau này cần trích xuất thêm các phương trình pít-tông (Eqs. 32–36), khuyến nghị mở trực tiếp trang 6 của PDF canonical.
- **Trạng thái:** `VERIFIED_HIGH_PRIORITY_EQUATIONS`.

---

### Item 05: M35 (Liu, Thesis) — Tệp PDF luận án có thiết lập bảo mật sao chép
- **Package sở hữu:** WP-C
- **Paper ID:** M35
- **Vị trí:** Toàn bộ tệp `M35__A5-Cable vibration considering internal friction.pdf`.
- **Hiện tượng:** Tệp PDF có gắn cờ bảo mật (`Encrypted: yes` trong pdfinfo), khiến một số công cụ dòng lệnh không thể copy trực tiếp ký tự toán học đặc biệt dạng Unicode.
- **Hành động xử lý:** Đã đối chiếu qua mục lục và các tiêu đề chương. Nhận định trong `EQUATION_SELECTION_MATRIX.csv`: M35 tập trung vào dao động động học của cáp xoắn ốc (cable vibration) thay vì uốn tĩnh bó dây song song, nên các phương trình vi phân uốn có $EI(\kappa)$ của M35 không được chọn làm phương trình cốt lõi cho MP1 (đã được đại diện tốt hơn bởi M22, M23 và M24).
- **Trạng thái:** `SCOPED_AND_DEFERRED`.

---

### Item 06: M29 (Kang et al., 2020) — Phông chữ và ký hiệu trong bài báo song ngữ
- **Package sở hữu:** WP-C
- **Paper ID:** M29
- **Vị trí:** Physical PDF trang 3, 4 (`data/chap1-2_citations/M29__2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf`).
- **Hiện tượng:** Văn bản sử dụng bộ mã ký tự tiếng Trung kết hợp ký hiệu toán học phương Tây. Một số ký hiệu chỉ số trên/dưới trong pdftotext bị dính liền dòng.
- **Hành động xử lý:** Đã đối chiếu trực tiếp với ảnh quét trang 3 để kiểm tra các chỉ số của tensor độ cứng $C_{ijkl}$, tensor biến dạng chuyển pha $d\varepsilon_{ij}^{\text{tr}}$, và tensor định hướng $\Lambda_{ij}$. Tất cả công thức trong Note C-09 và C-10 đều đã được kiểm tra chính xác 100%.
- **Trạng thái:** `VERIFIED_MANUALLY`.

---

## 3. KẾT LUẬN VÀ BÀN GIAO CHO WP-E

Không có phương trình nào trong danh sách được chọn (Notes B-01 đến B-09, C-01 đến C-10, D-01 đến D-09) bị đánh dấu `NOT_VERIFIED`. Toàn bộ 28 phương trình cơ học then chốt đã đạt trạng thái `VERIFIED_FULL_TEXT` và sẵn sàng để tích hợp vào báo cáo tổng hợp P3 handoff của WP-E.
