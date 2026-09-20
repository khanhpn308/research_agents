# Paper Card — Zhang et al. (2025), *A continuum-based model for a layer jamming beam*

> Source coverage: Full paper
> Extraction confidence: Mixed
> Locator mode: page-grounded
> Primary analytical lens: methods
> Secondary analytical lens: None
> Context verification: Paper-only
> Card completeness: Complete relative to supplied source

Nguồn được phân tích là PDF 10 trang trong repository. Script chuẩn bị nguồn xác nhận chỉ số trang PDF đáng tin cậy, nhưng không tự nhận diện được chú thích hình; vì vậy Hình 1–7 và các phương trình trung tâm đã được kiểm tra trực quan trên các trang render. Các nhận định về lịch sử lĩnh vực và tính mới chỉ phản ánh cách bài báo tự định vị, chưa phải kiểm chứng độc lập.

## Cách đọc các nhãn nguồn gốc

Các nhãn dưới đây cho biết **nội dung đến từ đâu và đã được kiểm chứng đến mức nào**. Chúng không phải thuật ngữ của Zhang et al.; đây là hệ thống truy xuất bằng chứng dùng trong Paper Card.

| Nhãn | Ý nghĩa | Bằng chứng cần có | Không nên hiểu là |
|---|---|---|---|
| `[Paper]` | Tác giả bài báo trực tiếp phát biểu, báo cáo hoặc sử dụng nội dung này | Chỉ dẫn tới trang, mục, hình, bảng hoặc phương trình trong PDF | Nội dung chắc chắn đúng hoặc đã được kiểm chứng độc lập |
| `[Paper-framed; external verification not performed]` | Lịch sử lĩnh vực, đánh giá prior work hoặc vị trí đóng góp được trình bày theo cách của chính bài báo | Chỉ dẫn tới phần bài báo đưa ra cách định vị đó | Tuyên bố “đầu tiên”, “mới” hoặc “chưa ai làm” đã được xác nhận bằng tìm kiếm tài liệu độc lập |
| `[External]` | Nội dung được hỗ trợ bởi một nguồn nằm ngoài bài báo đang đọc | Trích dẫn hoặc đường dẫn trực tiếp tới nguồn ngoài | Nội dung do Zhang et al. báo cáo trong bài này |
| `[Analysis]` | Suy luận của Agent từ một hoặc nhiều bằng chứng đã được chỉ rõ | Lập luận giải thích được và chỉ dẫn tới cơ sở trong nguồn | Phát biểu nguyên văn hoặc kết luận trực tiếp của tác giả |
| `[Hypothesis]` | Giải thích hoặc dự đoán có thể kiểm tra và cũng có thể bị bác bỏ | Phép thử đề xuất, kết quả kỳ vọng và điều kiện bác bỏ | Kết luận đã được chứng minh hoặc một đóng góp đã xác nhận là mới |
| `[User]` | Quyết định, nhận định hoặc mối liên hệ do người dùng hay bối cảnh dự án cung cấp | Phát biểu của người dùng hoặc tài liệu dự án liên quan | Nội dung xuất phát từ bài Zhang hoặc đã được bài báo chứng minh |

### Cách đọc chỉ dẫn vị trí nguồn

- `[Paper: PDF p. 4, Eq. 5]`: nội dung có thể truy ngược tới **trang thứ 4 của tệp PDF**, phương trình (5).
- `[Paper: PDF p. 7, Figure 6]`: nội dung có thể truy ngược tới **trang thứ 7 của tệp PDF**, Hình 6.
- `PDF p. N` luôn là số thứ tự trang trong tệp PDF, không mặc nhiên là số trang in của tạp chí.
- Một câu có nhãn `[Paper]` nhưng không có kiểm chứng bên ngoài vẫn chỉ là **nội dung được bài báo báo cáo**. Muốn dùng làm khẳng định trong luận văn, cần đánh giá xem thiết kế lý thuyết, FEA hoặc thí nghiệm có thực sự hỗ trợ mức độ mạnh của câu đó hay không.

Các nhãn này được giữ trong ghi chú nghiên cứu để tránh trộn lẫn bằng chứng với suy luận. Khi viết luận văn hoặc bài báo chính thức, thông thường bỏ nhãn và thay bằng câu văn học thuật cùng trích dẫn phù hợp.

## Sổ thuật ngữ

| Thuật ngữ chuẩn | Định nghĩa lần đầu | Biến thể trong nguồn | Quyết định sử dụng |
|---|---|---|---|
| layer jamming structure (LJS) | kết cấu kẹt lớp | LJSs | Dùng `LJS` cho kết cấu |
| continuum-based layer jamming model (CLJM) | mô hình kẹt lớp dựa trên môi trường liên tục | continuum-based model; continuum layer jamming model; một số chú thích dùng `LJM` | Dùng `CLJM` cho mô hình của bài báo |
| full-jamming state | trạng thái kẹt hoàn toàn | jamming state | Giữ `full-jamming` khi nói về trạng thái tiết diện |
| half-slipping state | trạng thái trượt một phần ở vùng giữa tiết diện | partial slip có thể được dùng trong diễn giải | Dùng thuật ngữ gốc `half-slipping` |
| full-slipping state | trạng thái giới hạn mà vùng trượt chiếm các giao diện bên trong, còn lớp ngoài cùng vẫn là vùng kẹt | full slip | Dùng thuật ngữ gốc và nêu rõ không phải toàn bộ mọi điểm đều trượt |
| $s,y$ | tọa độ dọc đường trung tâm và tọa độ theo chiều cao dầm | — | Giữ ký hiệu của bài báo |
| $\sigma,\tau$ | ứng suất pháp dọc lớp và ứng suất tiếp giữa lớp | — | Không đồng nhất $\sigma$ với áp suất tiếp xúc theo $y$ |
| $p,\mu$ | áp suất chân không và hệ số ma sát | pressure; friction coefficient | Giữ $p,\mu$ |
| $y_s$ | ranh giới giữa vùng trượt và vùng kẹt trên nửa tiết diện | sliding boundary | Giữ $y_s$ |

## 01. Thông tin cơ bản

- **[Paper] Tiêu đề:** *A continuum-based model for a layer jamming beam*. [Paper: PDF p. 1]
- **[Paper] Tác giả:** Shuai Zhang, Jiantao Yao, Wumian Zhao và Chunjie Wei; School of Mechanical Engineering, Yanshan University, Trung Quốc. [Paper: PDF p. 1]
- **[Paper] Tạp chí:** *Mechanical Sciences*, tập 16, trang 821–830, năm 2025. [Paper: PDF p. 1]
- **[Paper] DOI:** `10.5194/ms-16-821-2025`. [Paper: PDF p. 1]
- **[Paper] Ngày xuất bản:** 18 tháng 11 năm 2025. [Paper: PDF p. 1]
- **Loại bài:** bài phương pháp/mô hình cơ học, kèm đối chiếu FEA và thí nghiệm.
- **Lĩnh vực:** layer jamming, cơ học dầm, ma sát tiếp xúc, môi trường liên tục, độ cứng biến đổi.
- **[Paper] Mã nguồn:** không được cung cấp trong PDF.
- **[Paper] Dữ liệu:** tuyên bố Data availability ghi “No data were generated or used”, mặc dù bài trình bày kết quả FEA và đo thực nghiệm; không có bộ dữ liệu kèm theo được chỉ ra. [Paper: PDF p. 9]
- **Ngày đọc:** 21-09-2026.
- **[User] Vai trò trong đề tài:** đây là mô hình rút gọn M1 mà dự án dự kiến đánh giá bằng mô hình toàn lớp R và thí nghiệm E.

## 02. Tóm tắt một câu

**[Paper]** Bài báo thay thế chồng lớp rời rạc bằng một môi trường liên tục đàn–dẻo chịu giới hạn ma sát Coulomb, từ đó suy ra phân bố ứng suất, ranh giới trượt và biến dạng của dầm ở ba trạng thái tiết diện, rồi cho thấy mức phù hợp định tính/đồ thị với FEA và một thí nghiệm tải–độ võng trong phạm vi khảo sát. [Paper: PDF pp. 1–8, Eqs. 1–20, Figures 1–7]

## 03. Câu hỏi nghiên cứu

### Vấn đề cụ thể

**[Paper]** Các mô hình trước thường biểu diễn từng lớp riêng và trở nên bất tiện khi số lớp lớn; đồng thời tác giả cho rằng chúng chưa mô tả đủ chi tiết phân bố ứng suất và biến dạng khi trượt đáng kể. [Paper: PDF pp. 1–2, Introduction]

### Vì sao quan trọng

**[Paper]** Một mô hình liên tục có thể cung cấp trường ứng suất và dự đoán biến dạng với biểu diễn gọn hơn cho LJS nhiều lớp, phục vụ thiết kế kết cấu có độ cứng biến đổi. [Paper: PDF pp. 1–2]

### Câu hỏi tái dựng

> Có thể coi một LJS gồm nhiều lớp mỏng là một dầm liên tục đàn–dẻo, dùng giới hạn $|\tau|=\mu p$ để mô tả sự chuyển từ kẹt sang trượt, và từ đó dự đoán hợp lý ứng suất cùng biến dạng so với FEA và thí nghiệm hay không?

## 04. Bối cảnh và đường phát triển nghiên cứu

> **[Paper-framed; external verification not performed]** Bảng này tái hiện lịch sử theo phần Introduction của bài báo, không xác nhận độc lập quyền ưu tiên hay tính đầy đủ của tổng quan.

| Giai đoạn/cách tiếp cận | Điểm mạnh theo cách bài báo trình bày | Giới hạn theo cách bài báo trình bày | Vị trí của CLJM |
|---|---|---|---|
| Mô hình mô men quán tính tương đương $I=b(n\delta)^3/12$ và $I=bn\delta^3/12$ | Phân biệt hai giới hạn giống khối rắn và lớp trượt tự do | Không cho trường ứng suất/trượt tiến triển chi tiết | CLJM hướng tới trường ứng suất liên tục và các trạng thái trung gian [Paper: PDF p. 2] |
| Narang và cộng sự: mô hình hai lớp dựa trên Euler–Bernoulli, có tiêu chí chuyển trạng thái | Mô tả cơ học và chuyển trạng thái | Mở rộng nhiều lớp bằng FE | CLJM thay biểu diễn rời rạc bằng trường liên tục [Paper: PDF p. 2] |
| Caruso và cộng sự: mô hình nhiều lớp dạng tổng và mô hình uốn ba điểm | Xử lý dầm nhiều lớp và trượt tiến triển | Bài báo cho rằng vẫn mang tính layer-by-layer và khó khi số lớp lớn | CLJM lấy giới hạn $\delta/h\ll1$ [Paper: PDF p. 2] |
| Dầm composite có tương tác không hoàn toàn | Cung cấp nền tảng cho interlayer slip | Bài báo cho rằng chưa đủ cho LJS có trượt lớn | CLJM dùng vật liệu liên tục đặc biệt với luật chảy ma sát [Paper: PDF p. 2] |

**[Analysis]** Định vị thực chất của bài không phải “phát hiện ra interlayer slip”, mà là một phép liên tục hóa kèm luật đàn–dẻo lý tưởng để giảm biểu diễn rời rạc và cho trường ứng suất theo chiều cao. Tính mới của định vị này chưa được kiểm tra ngoài tài liệu mà bài tự trích dẫn.

## 05. Những điểm nghẽn cốt lõi mà bài báo nêu

| Điểm nghẽn | Biểu hiện | Nguyên nhân/giải thích của tác giả | Bằng chứng trong bài |
|---|---|---|---|
| Số lớp lớn | Mô hình từng lớp tạo nhiều đại lượng và phép tổng | Khi $\delta/h\ll1$, hiệu ứng rời rạc được cho là nhỏ | [Paper: PDF p. 2, Section 2] |
| Cần mô tả trượt tiến triển | Tiết diện chuyển full-jamming → half-slipping → full-slipping | Ứng suất tiếp đạt giới hạn Coulomb trước ở vùng giữa tiết diện | [Paper: PDF pp. 3–4, Figures 1 and 3, Eqs. 3–9] |
| Quan hệ ứng suất–biến dạng trượt không đơn trị | Ở yielding, $\tau=\mu p$ trong khi biến dạng trượt có thể tiếp tục tăng | Trượt được đồng nhất với biến dạng dẻo không thuận nghịch | [Paper: PDF p. 3, Figure 1b–c] |
| Tải lớn/hình học thay đổi | Nội lực phụ thuộc cấu hình cong hiện tại | Mỗi bước dùng giả thiết biến dạng nhỏ rồi cập nhật gia tăng | [Paper: PDF p. 6, Algorithm, Eqs. 19–20] |

## 06. Ý tưởng cốt lõi

1. **Phương pháp bề mặt — [Paper]:** coi chồng lớp là dầm cong bằng môi trường liên tục khi lớp rất mỏng và số lớp lớn. [Paper: PDF p. 2, Figure 1a]
2. **Cơ chế trung tâm — [Paper]:** coi vùng chưa trượt là đàn hồi và vùng đạt $|\tau|=\mu p$ là yielding/plastic sliding; vị trí $y_s$ chia tiết diện thành vùng trượt ở giữa và vùng kẹt phía ngoài. [Paper: PDF pp. 3–4, Figures 1 and 3, Eqs. 3–9]
3. **Cầu nối tới biến dạng — [Paper]:** tính nội lực vùng kẹt và mô men quán tính còn hoạt động $I_J(y_s)$, sau đó tích phân $M/(EI_J)$ theo chiều dài trong thuật toán gia tăng. [Paper: PDF pp. 5–6, Eqs. 10–20, Algorithm]
4. **Bài học khái quát — [Analysis]:** độ cứng giảm không được gán trực tiếp bằng một hệ số kinh nghiệm; nó xuất hiện do vùng kẹt co lại khi $y_s$ tăng. Đây là phép biến trạng thái trượt vi mô thành một đại lượng tiết diện dùng trong mô hình dầm.

## 07. Tổng quan phương pháp

### Đầu vào

- **[Paper]** Hình học $L,h,b$, mô đun Young $E$, hệ số ma sát $\mu$, áp suất $p(s)$, tải phân bố hoặc tải tương đương $q(s)$, cấu hình ban đầu $\theta^0(s)$, chiều dày lớp $\delta$, cùng tham số bước lặp của thuật toán. [Paper: PDF pp. 2–6, Eqs. 1–20 and Algorithm]

### Đầu ra

- **[Paper]** Nội lực $N,Q,M$; phân bố $\tau(y,s)$ và $\sigma(y,s)$; ranh giới $y_s$; trạng thái full-jamming/half-slipping/full-slipping; góc/biến dạng dầm $\theta(s)$ và đường tải–độ võng. [Paper: PDF pp. 3–8]

### Chuỗi xử lý

```text
hình học + vật liệu + μp + tải + cấu hình hiện tại
→ cân bằng dầm cong: N(s), Q(s), M(s)
→ so Q với Q_slip và Q_max
→ xác định trạng thái tiết diện và y_s(s)
→ tính τ(y,s)
→ tính σ(y,s), N_J(s), M_J(s)
→ tính I_J(y_s)
→ tích phân Δθ = ∫ M/(E I_J) ds
→ cập nhật hình học và tăng tải
→ lặp đến tải đích
```

### Giả định chính

- **[Paper]** $\delta/h\ll1$, các đại lượng có thể xem là liên tục theo $y$; bài nêu $n\gtrsim10$ là hữu hiệu trong thực tế dựa trên so sánh FEA của họ. [Paper: PDF p. 2]
- **[Paper]** Trạng thái ứng suất phẳng kiểu Euler–Bernoulli; bỏ qua biến dạng pháp giữa lớp. [Paper: PDF pp. 2–3]
- **[Paper]** Áp suất tiếp xúc do chân không là $p$, giới hạn ma sát không đổi theo Coulomb là $\mu p$; không có phần áp suất bổ sung do biến dạng đàn hồi theo phương giữa lớp. [Paper: PDF p. 3]
- **[Paper]** Bán kính cong lớn hơn nhiều chiều cao dầm khi dùng phân bố ứng suất tiếp của dầm thẳng. [Paper: PDF pp. 3–4, Eq. 3]
- **[Paper]** Mỗi bước gia tăng thỏa biến dạng nhỏ, dù tổng biến dạng có thể lớn. [Paper: PDF p. 6, Algorithm]

### Huấn luyện, công cụ ngoài và feedback loop

- **Huấn luyện:** Not applicable; đây không phải mô hình học máy.
- **Công cụ kiểm chứng — [Paper]:** Abaqus với phần tử CPS4R cho FEA; máy kéo cho thí nghiệm tải–độ võng. [Paper: PDF pp. 6–8]
- **Feedback loop — [Paper]:** cấu hình $\theta^k$ cập nhật nội lực và mức trượt cho bước kế tiếp; bước tải được điều chỉnh để giới hạn độ thay đổi chuyển vị. [Paper: PDF p. 6, Algorithm]

## 08. Phân rã các mô-đun cốt lõi

| Mô-đun | Chức năng | Vì sao cần | Đầu vào → đầu ra | Bằng chứng hỗ trợ | Nếu bỏ/thay đổi |
|---|---|---|---|---|---|
| Cân bằng dầm cong | Tính $N,Q,M$ theo cấu hình và tải | Liên kết tải ngoài với trạng thái mỗi tiết diện | $q,\theta\to N,Q,M$ | [Paper: PDF p. 3, Figure 2, Eqs. 1–2] | **[Analysis]** Không thể xác định trượt theo vị trí dọc dầm |
| Luật chảy Coulomb | Phân biệt kẹt và trượt | Tạo tiêu chí vật lý đơn giản cho chuyển trạng thái | $\tau,\mu,p\to$ elastic/yielding | [Paper: PDF p. 3, Figure 1b–c] | **[Analysis]** Mất cơ chế tạo vùng trượt; thay luật ma sát có thể đổi ranh giới hiệu lực |
| Phân bố $\tau$ và ranh giới $y_s$ | Xác định ba trạng thái tiết diện | Chuyển lực cắt thành hình học vùng trượt | $Q,\mu,p,b,h,\delta\to\tau,y_s$ | [Paper: PDF p. 4, Figure 3, Eqs. 3–9] | **[Analysis]** Không tính được độ cứng hữu hiệu thay đổi theo trượt |
| Phân tích $\sigma$, $N_J,M_J$ | Bảo toàn lực/mô men giữa vùng kẹt và trượt | Cần nội lực thực sự được vùng kẹt truyền | $N,M,y_s,\tau\to\sigma,N_J,M_J$ | [Paper: PDF pp. 5–6, Figures 4–5, Eqs. 10–18] | **[Analysis]** Dùng toàn tiết diện sẽ đánh giá quá cao khả năng chịu uốn sau trượt |
| Quan hệ độ cong vùng kẹt | Tính thay đổi góc từ $M/(EI_J)$ | Liên kết trạng thái tiết diện với biến dạng toàn cục | $M,E,y_s\to I_J,\Delta\theta$ | [Paper: PDF p. 6, Eqs. 19–20] | **[Analysis]** Không tạo được đường tải–độ võng |
| Thuật toán gia tăng | Cập nhật hình học và tải | Nội lực phụ thuộc hình dạng; quan hệ trượt không đơn trị | trạng thái $k\to k+1$ | [Paper: PDF p. 6, Algorithm] | **[Analysis]** Không xử lý nhất quán tải lớn theo cách bài đề xuất |

Không có thí nghiệm ablation cô lập từng mô-đun. FEA và thí nghiệm kiểm tra đầu ra tích hợp của toàn mô hình, nên vai trò riêng của từng giả định vẫn chủ yếu là suy luận cơ học thay vì bằng chứng loại-bỏ-thành-phần.

## 09. Công thức và ký hiệu thiết yếu

### 9.1. Cân bằng dầm cong

**[Paper]**

$$
\frac{dN}{ds}=-Q\theta'-q_s=-\frac{Q}{r}-q_s,\qquad
\frac{dQ}{ds}=N\theta'+q_y=\frac{N}{r}+q_y,\qquad
\frac{dM}{ds}=Q.
$$

Trong đó $N,Q,M$ là lực dọc, lực cắt và mô men; $q_s,q_y$ là thành phần tải phân bố; $\theta'=1/r$. Công thức tạo trường nội lực dùng cho phân tích trượt. [Paper: PDF p. 3, Eq. 1]

### 9.2. Phân bố ứng suất tiếp khi full-jamming

**[Paper]**

$$
\tau(y,Q)=\frac{3Q}{2A}\left(1-\frac{4y^2}{h^2}\right),\qquad A=bh.
$$

Đây là phân bố parabol của tiết diện chữ nhật, được dùng xấp xỉ cho dầm cong khi $r\gg h$. [Paper: PDF p. 4, Eq. 3]

### 9.3. Hai ngưỡng lực cắt

**[Paper]**

$$
Q_{\mathrm{slip}}=\frac{2}{3}\mu pbh,
$$

$$
Q_{\max}=\frac{\mu pb\left(3h^2-6\delta h+4\delta^2\right)}{3(h-\delta)}.
$$

$Q_{\mathrm{slip}}$ là lúc $\tau$ ở giữa tiết diện chạm $\mu p$; $Q_{\max}$ là lúc $y_s=h/2-\delta$, tức vùng kẹt chỉ còn các dải ngoài cùng dày $\delta$. [Paper: PDF p. 4, Eqs. 5–6]

### 9.4. Luật trạng thái tiết diện

**[Paper]** $y_s=0$ khi $|Q|<Q_{\mathrm{slip}}$; $y_s$ tăng theo biểu thức từng đoạn của Eq. (9) khi $Q_{\mathrm{slip}}\le |Q|<Q_{\max}$; và $y_s=h/2-\delta$ khi $|Q|\ge Q_{\max}$. Trong vùng trượt $|y|\le y_s$, $\tau=\operatorname{sign}(Q)\mu p$; vùng kẹt dùng phân bố parabol đã co giãn hoặc đa thức biên tùy trạng thái. [Paper: PDF p. 4, Eqs. 7–9]

**Trực giác:** lực cắt càng lớn thì vùng đạt giới hạn ma sát càng lan từ trục trung hòa ra ngoài; phần tiết diện còn truyền uốn như một khối giảm dần.

### 9.5. Cân bằng ứng suất pháp trong vùng trượt

**[Paper]**

$$
\frac{\partial\sigma_S}{\partial s}+\frac{\partial\tau_S}{\partial y}=0.
$$

Vì bài giả thiết $\tau_S=\operatorname{sign}(Q)\mu p$ không đổi theo $y$, nên $\partial\tau_S/\partial y=0$ và $\sigma_S$ được vận chuyển dọc vùng trượt theo cấu trúc hình học của $y_s(s)$. [Paper: PDF p. 5, Eq. 13 and Figure 5]

### 9.6. Biến dạng từ vùng kẹt còn lại

**[Paper]**

$$
\Delta\theta(s)=\int_0^s\frac{M}{EI_J}\,d\xi,
$$

$$
I_J=
\begin{cases}
\dfrac{bh^3}{12}, & y_s=0,\\[4pt]
\dfrac{2b}{3}\left[\left(\dfrac h2\right)^3-y_s^3\right], & y_s\ne0.
\end{cases}
$$

$I_J$ là mô men quán tính của hai vùng kẹt ngoài. Khi $y_s$ tăng, $I_J$ giảm và độ cong tăng. [Paper: PDF p. 6, Eqs. 19–20]

## 10. Thiết kế kiểm chứng và chuỗi bằng chứng

### 10.1. Kiểm kê nguồn bằng chứng

#### Hình chính

| Hình | Vai trò trong lập luận | Nguồn |
|---|---|---|
| Figure 1 | Định nghĩa phép liên tục hóa, miền ứng suất $\tau$–$\sigma$, và chu trình loading/yielding/unloading | [Paper: PDF p. 2, Figure 1] |
| Figure 2 | Thiết lập nội lực của phần tử dầm cong để suy ra Eqs. 1–2 | [Paper: PDF p. 3, Figure 2] |
| Figure 3 | Minh họa full-jamming, half-slipping và full-slipping trên tiết diện | [Paper: PDF p. 4, Figure 3] |
| Figure 4 | Xây dựng phân bố $\sigma$ trong vùng kẹt khi $\delta\to0$ | [Paper: PDF p. 5, Figure 4] |
| Figure 5 | Biến đổi tích phân theo $y$ sang tích phân theo $s$ trong vùng trượt | [Paper: PDF p. 5, Figure 5] |
| Figure 6 | So sánh trường $\sigma,\tau$ của CLJM với FEA 10 và 25 lớp ở ba mức tải/trạng thái | [Paper: PDF p. 7, Figure 6; PDF p. 8, discussion] |
| Figure 7 | Thiết bị thí nghiệm và đường tải–độ võng của mẫu 20 lớp ở 60 kPa | [Paper: PDF p. 8, Figure 7] |

#### Bảng

**[Paper]** Không có bảng chính trong PDF.

#### Nhóm phương trình và vai trò

| Phương trình | Vai trò | Nguồn |
|---|---|---|
| Equation 1; Equation 2 | Cân bằng và nghiệm nội lực dầm cong | [Paper: PDF p. 3] |
| Equation 3; Equation 4 | Phân bố $\tau$ đàn hồi và lực cắt tương đương ở ranh giới trượt | [Paper: PDF p. 4] |
| Equation 5; Equation 6; Equation 7; Equation 8; Equation 9 | Ngưỡng chuyển trạng thái, luật $\tau$ từng đoạn và $y_s(Q)$ | [Paper: PDF p. 4] |
| Equation 10; Equation 11; Equation 12 | Phân bố $\sigma$, cân bằng $N,M$, và mô men vùng kẹt | [Paper: PDF p. 5] |
| Equation 13; Equation 14; Equation 15; Equation 16; Equation 17; Equation 18 | Cân bằng ứng suất và lan truyền nội lực pháp trong vùng trượt | [Paper: PDF pp. 5–6] |
| Equation 19; Equation 20 | Góc quay và mô men quán tính vùng kẹt | [Paper: PDF p. 6] |
| Algorithm | Thuật toán tải gia tăng và cập nhật hình học | [Paper: PDF p. 6] |

### 10.2. Cấu hình FEA

- **[Paper]** Dầm công xôn: dài 40 mm, bề rộng 20 mm, cao 5 mm; 10 và 25 lớp. [Paper: PDF pp. 6–8]
- **[Paper]** Abaqus, phần tử CPS4R cạnh 0,1 mm; $E=0.3$ GPa, $\mu=0.5$, áp suất 0,1 MPa. [Paper: PDF p. 8]
- **[Paper]** Lực tập trung được phân bố đều lên đầu tự do của từng lớp để hỗ trợ hội tụ. [Paper: PDF p. 8]
- **[Paper]** Hình 6 dùng tải 3 N, 4 N và 5,5 N để minh họa full-jamming, half-slipping và full-slipping. [Paper: PDF p. 7, Figure 6]

### 10.3. Cấu hình thí nghiệm

- **[Paper]** Mẫu gồm 20 tấm PVC trong màng PVC mềm; kích thước 100 mm × 20 mm × 5 mm. [Paper: PDF p. 8]
- **[Paper]** Khung gá trượt tự do trên ray để loại ràng buộc ngang; máy kéo đo quan hệ tải–độ võng. [Paper: PDF p. 8, Figure 7a]
- **[Paper]** Áp suất 60 kPa; đường giải tích dùng $E=755$ MPa và $\mu=0.55$. [Paper: PDF p. 8]
- **[Paper]** Dữ liệu thực nghiệm được trình bày bằng trung bình và vùng $\pm1\sigma$, nhưng PDF không nêu rõ số mẫu/lần lặp trong phần mô tả này. [Paper: PDF p. 8, Figure 7b]

### 10.4. Ma trận claim–evidence

| Thử nghiệm/phân tích | Tuyên bố được kiểm tra | So sánh và điều kiện | Kết quả báo cáo | Kết luận được hỗ trợ | Kết luận mạnh hơn chưa được hỗ trợ | Nguồn |
|---|---|---|---|---|---|---|
| FEA full-jamming | Vùng kẹt có thể dùng phân bố đàn hồi liên tục | CLJM so với FEA 10/25 lớp, 3 N; các vị trí dọc dầm | Phù hợp tốt ở đoạn giữa; sai khác rõ gần đầu $s=1$ mm và phụ thuộc số lớp | CLJM mô tả hợp lý trường ứng suất ở một số tiết diện xa biên trong cấu hình khảo sát | Không chứng minh mọi $n\ge10$, mọi hình học hoặc mọi vị trí đều đạt một sai số định trước | [Paper: PDF pp. 7–8, Figure 6a] |
| FEA half-slipping | CLJM mô tả được vùng trượt một phần | CLJM so với FEA ở tải 4 N | Sai khác nhỏ ở đoạn giữa, nhưng CLJM dự đoán vùng trượt rộng hơn FEA | Cơ chế và dạng trường có tính phù hợp định tính/đồ thị trong trường hợp khảo sát | Không chứng minh ranh giới $y_s$ có độ chính xác định lượng hay luật $\mu p$ đầy đủ | [Paper: PDF pp. 7–8, Figure 6b] |
| FEA full-slipping | CLJM vẫn mô tả được trạng thái tải cao | CLJM so với FEA ở 5,5 N | Sai khác đáng kể của $\tau$ trong vùng kẹt; vùng trượt CLJM vẫn rộng hơn | Bài xác định được một chế độ breakdown liên quan dầm cong và ứng suất pháp bị bỏ qua | Không hỗ trợ tuyên bố chính xác cao dưới tải cực trị/full-slipping | [Paper: PDF pp. 7–8, Figure 6c] |
| Thí nghiệm tải–độ võng | Thuật toán cho đáp ứng biến dạng toàn cục hợp lý | Mẫu PVC 20 lớp, 60 kPa; giải tích so với trung bình $\pm1\sigma$ | Đường giải tích nằm trong vùng $\pm1\sigma$ | Mô hình phù hợp với đường tải–độ võng của cấu hình cụ thể này | Không xác lập miền hiệu lực theo $n,p$, tải, vật liệu hoặc khả năng dự báo ngoài cấu hình đã dùng | [Paper: PDF p. 8, Figure 7b] |

### 10.5. Baseline, metric, uncertainty và fairness

- **Baseline chính:** FEA rời rạc 10/25 lớp cho trường ứng suất; dữ liệu thực nghiệm cho tải–độ võng.
- **Metric:** chủ yếu là so sánh đường cong/trường ứng suất bằng đồ thị; bài không công bố một metric sai số tổng hợp hoặc ngưỡng chấp nhận định trước. [Paper: PDF pp. 7–8, Figures 6–7]
- **Uncertainty:** thí nghiệm hiển thị $\pm1\sigma$, nhưng không thấy số lần lặp, quy trình ước lượng tham số, hoặc propagation uncertainty trong nguồn. [Paper: PDF p. 8]
- **Compute budget/chi phí:** không được định lượng.
- **Oracle inputs/calibration:** $E$ và $\mu$ được đưa vào mô hình; nguồn không làm rõ trong phần kết quả liệu chúng được đo độc lập, lấy từ tài liệu hay hiệu chỉnh bằng chính đường cong kiểm chứng. [Paper: PDF p. 8]

## 11. Diễn giải đúng kết luận

- **Phạm vi nhiệm vụ — [Paper]:** dầm LJS chịu uốn, mô tả ứng suất và biến dạng trong ba trạng thái tiết diện. [Paper: PDF pp. 2–6]
- **End-to-end:** mô hình tạo được đường tải–độ võng từ hình học, vật liệu, áp suất, ma sát và tải thông qua thuật toán gia tăng; tuy vậy việc xác định các tham số vật liệu/ma sát không được mô tả như một pipeline độc lập. [Paper: PDF pp. 6–8]
- **Biên hình học:** phân bố ứng suất tiếp cơ sở giả thiết $r\gg h$; sai số tăng khi đoạn dầm ở full-slipping hành xử như dầm cong rõ rệt. [Paper: PDF pp. 4 and 8]
- **Biên không gian:** vùng trung tâm dầm phù hợp hơn vùng gần đầu/ràng buộc. [Paper: PDF pp. 8–9]
- **Biên trạng thái:** bài tự kết luận mô hình phù hợp nhất ở partial slip và kém tin cậy hơn khi full-slipping. [Paper: PDF pp. 8–9]
- **Biên layer count:** bài nêu $n\gtrsim10$, nhưng nguồn chỉ cho so sánh FEA ở 10 và 25 lớp cùng biểu diễn continuum-based 50 lớp, không cung cấp quét $n$ hay sai số theo $n$. [Paper: PDF pp. 2, 7–8, Figure 6]
- **Biên thực nghiệm:** một cấu hình 20 lớp, một áp suất 60 kPa và một hệ vật liệu PVC. [Paper: PDF p. 8, Figure 7]
- **Chi phí:** bài gọi CLJM đơn giản và hiệu quả tính toán nhưng không báo thời gian chạy hay scaling so với FEA. [Paper: PDF p. 9]

**Phát biểu kết luận đã giới hạn:** **[Analysis]** Nguồn hỗ trợ rằng CLJM có thể tái tạo hợp lý dạng trường ứng suất ở một số tiết diện xa biên và đường tải–độ võng của một mẫu cụ thể; nguồn đồng thời cho thấy sai lệch có hệ thống ở vùng biên, trong độ rộng vùng trượt và ở full-slipping. Nguồn chưa đủ để kết luận một ngưỡng phổ quát $n\ge10$, độ chính xác “cao” theo metric định lượng, hay hiệu lực trên toàn không gian $n$–$p$–mức uốn.

## 12. Các giới hạn được tác giả thừa nhận rõ ràng

| Giới hạn | Biểu hiện cụ thể | Hướng tương lai do tác giả nêu | Nguồn |
|---|---|---|---|
| Bỏ qua ứng suất pháp theo phương $y$ | CLJM dự đoán vùng trượt rộng hơn FEA vì ứng suất pháp có thể làm tăng ngưỡng ứng suất tiếp | Mô hình chi tiết hơn cho hiệu ứng này được hàm ý là cần thiết | [Paper: PDF p. 8] |
| Không mô tả end/constraint effects | Phân bố $\tau$ gần đầu dầm, ví dụ $s=1$ mm, lệch khỏi parabol và phụ thuộc số lớp | Bổ sung boundary correction factors | [Paper: PDF p. 8] |
| Xấp xỉ dầm thẳng trong vùng kẹt khi full-slipping | Sai khác đáng kể của $\tau$ giữa FEA và CLJM dưới tải 5,5 N | Xử lý độ cong chi tiết hơn trong vùng kẹt | [Paper: PDF p. 8] |
| Độ tin cậy giảm ở tải cực trị/full-slipping và gần biên | Tác giả khuyến nghị FEA cho kiểm chứng cuối cùng ở các trường hợp này | Dùng FEA cho final verification; phát triển correction/model refinement | [Paper: PDF pp. 8–9] |

## 13. Phân tích phản biện

| Quan sát **[Analysis]** | Vấn đề hoặc giải thích thay thế | Vì sao quan trọng | Cách kiểm tra | Cơ sở |
|---|---|---|---|---|
| Mốc $n\gtrsim10$ chưa phải miền hiệu lực định lượng | Hai điểm FEA 10/25 lớp không đủ xác định hội tụ theo $n$; sự phù hợp còn phụ thuộc $p$, tải, $\delta/h$, vị trí và output | Đây là mệnh đề trung tâm của phép liên tục hóa | Quét $n$ có kiểm soát, tính lỗi của tải–võng, $y_s$, $\tau$, $\sigma$; đặt tolerance trước khi xem kết quả | [Paper: PDF pp. 2, 7–8, Figure 6] |
| “Strong agreement/high accuracy” chủ yếu dựa trên đồ thị | Không có norm lỗi, confidence interval cho lỗi mô hình, hoặc acceptance threshold | Không thể chuyển trực tiếp thành quyết định thiết kế | Số hóa/cung cấp dữ liệu, báo $L_2/L_\infty$ field error và output-specific relative/absolute error | [Paper: PDF pp. 1, 7–9] |
| Thực nghiệm không kiểm tra cơ chế trượt nội bộ | Đường tải–độ võng có thể phù hợp dù $y_s$ hoặc trường ứng suất sai do bù sai số tham số | Global agreement không xác nhận đúng cơ chế | Đo chuyển vị tương đối giữa lớp/DIC hoặc marker ở cạnh, so onset và front propagation | [Paper: PDF p. 8, Figure 7] |
| Tách calibration–validation không rõ | $E=755$ MPa và $\mu=0.55$ có thể là đo độc lập hoặc giá trị hiệu chỉnh; nguồn không nói rõ tại phần kết quả | Nếu fitted trên cùng đường cong, Figure 7 yếu hơn như bằng chứng dự báo | Đo $E,\mu$ độc lập; khóa tham số trước validation; dùng cấu hình held-out | [Paper: PDF p. 8] |
| Áp suất tiếp xúc được lý tưởng hóa bằng $p$ đồng đều | Pressure redistribution, lift-off hoặc contact loss có thể đổi giới hạn ma sát cục bộ | Có thể là cơ chế làm CLJM sai khi cong lớn/gần biên | FEA contact đầy đủ và đo/ước lượng contact pressure; bật/tắt separation để quy trách nhiệm sai số | [Paper: PDF p. 3; PDF p. 8] |
| Mô hình gọi là giới hạn $\delta\to0$ nhưng vẫn giữ $\delta$ trong $Q_{\max}$ và $y_s=h/2-\delta$ | $\delta$ hoạt động như regularization cho hai lớp biên; ý nghĩa asymptotic chưa được chứng minh trong nguồn | Ảnh hưởng trực tiếp tới full-slipping và phụ thuộc số lớp | Phân tích giới hạn $\delta/h\to0$, so mô hình với nhiều $n$, kiểm tra hội tụ $Q_{\max}$ và đáp ứng | [Paper: PDF pp. 2 and 4, Eqs. 6 and 9] |
| Luật đàn–dẻo nêu unloading nhưng kiểm chứng là tải đơn điệu | Irreversibility/hysteresis không được kiểm tra trực tiếp | Luật trạng thái có thể thiếu memory, stick–slip hoặc ma sát động | Thử chu kỳ tải–dỡ ở nhiều biên độ; so vòng hysteresis và residual slip | [Paper: PDF p. 3, Figure 1c; PDF p. 8, Figure 7] |
| Tuyên bố Data availability không ăn khớp cách diễn đạt thông thường | Bài hiển thị dữ liệu đo và FEA nhưng tuyên bố không dữ liệu nào được tạo/dùng | Làm giảm khả năng tái lập và kiểm tra số liệu | Công bố dữ liệu thô, số lần lặp, mã CLJM và input Abaqus | [Paper: PDF pp. 7–9] |

## 14. Kiến thức rút ra

### Các ứng viên kiến thức do Agent rút ra

1. **[Analysis] Trượt bắt đầu ở giữa chiều cao tiết diện, không phải ở bề mặt tự do.** Trong mô hình, $\tau(y)$ parabol và cực đại tại $y=0$, nên vùng trượt lan từ trung tâm ra ngoài. [Paper: PDF p. 4, Eq. 3 and Figure 3]
2. **[Analysis] “Full-slipping” là tên trạng thái giới hạn, không có nghĩa toàn bộ tiết diện đều chảy.** Hai dải ngoài cùng vẫn được giữ là vùng kẹt với bề dày liên quan $\delta$. [Paper: PDF p. 4, Figure 3c and Eq. 9]
3. **[Analysis] Áp suất chân không đi vào mô hình chủ yếu qua ngưỡng ma sát $\mu p$.** Vì vậy mô hình dự đoán các ngưỡng $Q_{\mathrm{slip}}$ và $Q_{\max}$ tăng gần tuyến tính theo $p$ nếu $\mu$ không đổi. [Paper: PDF p. 4, Eqs. 5–6]
4. **[Analysis] Độ mềm tăng do mất dần vùng tiết diện truyền uốn như một khối.** $I_J$ giảm theo $y_s$, biến cơ chế slip thành độ cong tăng. [Paper: PDF p. 6, Eqs. 19–20]
5. **[Analysis] Một mô hình có thể đúng ở output toàn cục nhưng sai ở trường cục bộ.** Figure 7 cho tải–võng phù hợp, trong khi Figure 6 cho sai lệch vùng trượt và ứng suất ở biên/full-slip. [Paper: PDF pp. 7–8, Figures 6–7]
6. **[Analysis] Kiểm chứng mô hình rút gọn cần tách ba lớp:** cân bằng toàn cục, chuyển trạng thái/trượt, và trường ứng suất cục bộ; một lớp bằng chứng không thay thế hai lớp còn lại.

## 15. Liên hệ với kiến thức hiện có

> Context mode: **Paper-only**. Không có tìm kiếm ngoài được thực hiện trong Paper Card này.

- **[Paper]** CLJM kế thừa cân bằng Euler–Bernoulli/dầm cong, kết hợp với một analog đàn–dẻo mà giới hạn chảy được đặt bởi ma sát Coulomb. [Paper: PDF pp. 2–6]
- **[Paper-framed; external verification not performed]** Bài tự nối với Narang cho dầm hai lớp, Caruso cho mô hình nhiều lớp, và lý thuyết dầm composite tương tác không hoàn toàn. [Paper: PDF p. 2]
- **[User]** Trong kiến trúc nghiên cứu hiện tại, CLJM chính là M1; mô hình interface-resolving/full-layer là R và thí nghiệm là E.
- **[Analysis]** Figure 6 đã cung cấp một nguyên mẫu rất hẹp của phép so M1–R: M1 so với FEA rời rạc 10/25 lớp. Phần còn thiếu để thành nghiên cứu miền hiệu lực là metric lỗi định lượng, quét tham số có thiết kế, tolerance đặt trước, kiểm chứng thực nghiệm tại cả vùng dự đoán đúng và vùng dự đoán sai.
- **[Analysis]** Các breakdown mà chính bài nêu—end effects, bỏ qua normal contact stress, curved-beam behavior ở full-slip—là các cơ chế ứng viên để mô hình R kiểm tra, nhưng chưa nên coi là danh sách đầy đủ.

## 16. Các ý tưởng nghiên cứu

### 16.1. Ứng viên do Agent đề xuất: Bản đồ hiệu lực định lượng, phụ thuộc output, của CLJM

- **Nguồn gốc:** bài nêu $n\gtrsim10$ và “high accuracy”, nhưng đồng thời cho sai lệch ở biên/full-slip mà không đưa metric hoặc tolerance. [Paper: PDF pp. 2, 7–9]
- **[Hypothesis]** Với tolerance đặt trước, miền CLJM đạt yêu cầu cho độ võng toàn cục sẽ rộng hơn miền đạt yêu cầu cho ranh giới trượt $y_s$ và trường ứng suất; không tồn tại một ngưỡng layer count duy nhất bảo đảm mọi output.
- **Delta so với bài:** thay kiểm tra vài cấu hình bằng bản đồ lỗi theo $n$, $p$ và mức uốn/trạng thái; báo riêng lỗi của $w$, $K/EI_{\mathrm{eff}}$, $Q_{\mathrm{slip}}$, $y_s$ và trường ứng suất.
- **Phương pháp ban đầu:** tái tạo M1; xây R với từng lớp, contact, Coulomb friction và separation có kiểm soát; verification mesh/contact; đặt tolerance trước; quét không gian tối thiểu và chọn điểm sát ranh giới cho E.
- **Kiểm chứng (Validation):** so M1–R trên cùng hình học/tham số; dùng lỗi tương đối khi mẫu số ổn định và lỗi tuyệt đối/chuẩn hóa gần zero; dùng E kiểm tra ít nhất một điểm predicted-valid và một predicted-invalid.
- **Kết quả kỳ vọng:** các miền valid/invalid khác nhau theo output.
- **Kết quả bác bỏ giả thuyết:** mọi output có cùng ranh giới trong độ phân giải và uncertainty đã định, hoặc R/E cho thấy không thể phân biệt model-form error với sai số tham số.
- **Nguy cơ thất bại (Failure modes):** (1) R chưa đủ độc lập hoặc chưa verified; (2) tham số $\mu,p,E$ không định danh được; (3) thí nghiệm không quan sát được $y_s$; (4) miền khảo sát quá nhỏ nên chỉ lặp lại Figure 6.
- **Trạng thái đổi mới (Innovation status):** `unverified`; cần tiếp tục audit prior art theo protocol của dự án, không được gọi là mới chỉ từ bài này.

### 16.2. Ứng viên do Agent đề xuất: Quy trách nhiệm cơ chế breakdown thay vì chỉ đo sai số

- **Nguồn gốc:** tác giả quy sai lệch cho normal stress bị bỏ qua, end effects và curved-beam behavior, nhưng chưa tách riêng đóng góp của từng cơ chế. [Paper: PDF p. 8]
- **[Hypothesis]** Sai số CLJM ở half-slipping chủ yếu do contact-pressure redistribution, còn sai số ở full-slipping chủ yếu do xấp xỉ shear distribution của dầm thẳng; end effects chi phối trong một chiều dài biên có thể chuẩn hóa theo $h$ hoặc $L$.
- **Delta so với bài:** dùng một hierarchy của R, lần lượt bật/tắt pressure redistribution, separation, geometric nonlinearity và curvature/contact effects để phân rã sai số.
- **Phương pháp ban đầu:** thiết kế các cặp mô phỏng chỉ khác một cơ chế, giữ mesh/friction/hình học như nhau; đo thay đổi trong $y_s$, $\tau$, tải–võng và chiều dài vùng biên.
- **Kiểm chứng (Validation):** ablation cơ học trong R cộng với đo cạnh/DIC ở vài cấu hình đại diện; yêu cầu một cơ chế dự đoán đúng cả dấu và độ lớn thay đổi.
- **Kết quả bác bỏ giả thuyết:** sai số không giảm khi bổ sung cơ chế được cho là chi phối, hoặc các cơ chế tương tác quá mạnh để định danh riêng.
- **Nguy cơ thất bại (Failure modes):** (1) mô hình contact gây confounding số học; (2) dữ liệu thực nghiệm không đủ độ phân giải; (3) normal pressure không đo được; (4) hierarchy của R thay đổi nhiều giả định cùng lúc.
- **Trạng thái đổi mới (Innovation status):** `unverified`; đây là giả thuyết cần kiểm tra và cần prior-art search riêng.
