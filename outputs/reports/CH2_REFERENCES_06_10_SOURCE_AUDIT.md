# Tiếp nối audit: tài liệu tham khảo [6]–[10]

**Phạm vi:** tiếp tục từ bản audit [1]–[5], dùng cùng bản nháp và cùng master traceability. Các excerpt dưới đây được chép từ trường `source_fragment`/anchor hiện có; locator được giữ đúng như trace ghi. Đây là dấu dẫn để mở PDF, chưa phải xác nhận độc lập từng câu từ PDF.

| Ref | Nguồn | DOI | Claim/anchor duy nhất | PDF đóng gói |
|---:|---|---|---:|---|
| [6] | M. Russo, S. M. H. Sadati, X. Dong, A. Mohammad, I. D. Walker, C. Bergeles, K. Xu & D. A. Axinte (2023), “Continuum Robots: An Overview” | 10.1002/aisy.202200367 | 2 | `06_M03__2023-Russo-Continuum Robots An Overview.pdf` |
| [7] | H. Jeon, Q. N. Le, S. Jeong, S. Jang, H. Jung, H. Chang, H. J. Pandya & Y. Kim (2022), “Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism” | 10.1109/lra.2022.3174363 | 21 | `07_M31__2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf` |
| [8] | Y. Zhang, J. Wang, G. Ye & R. Xu (2018), “Bending Stiffness of Parallel Wire Cables Including Interfacial Slips among Wires” | 10.1061/(asce)st.1943-541x.0002171 | 12 | `08_M22__2018-Bending Stiffness of Parallel Wire Cables.pdf` |
| [9] | Y. S. Narang, J. J. Vlassak & R. D. Howe (2018), “Mechanically Versatile Soft Machines through Laminar Jamming” | 10.1002/adfm.201707136 | 13 | `09_2018-Mechanically Versatile Soft Machines through Laminar.pdf` |
| [10] | F. Caruso, G. Mantriota, V. Moramarco & G. Reina (2023), “Layer jamming: Modeling and experimental validation” | 10.1016/j.ijmecsci.2023.108325 | 5 | `10_2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf` |

## [6] M. Russo, S. M. H. Sadati, X. Dong, A. Mohammad, I. D. Walker, C. Bergeles, K. Xu & D. A. Axinte (2023), “Continuum Robots: An Overview”

**CH2-S2-R0003-A01 — mục 2.2.1.** Để mô tả hình dạng, có thể thay thân vật lý bằng một đường trục cùng trường định hướng tiết diện dọc thân; trong biểu diễn thanh Cosserat được Russo và cộng sự trình bày, đường trục đi qua trọng tâm tiết diện và được tham số hóa theo chiều dài cung ở cấu hình ban đầu [6].

- **Locator PDF trong trace:** §3.1.3, đoạn trước Eqs. (6)–(8). **Trạng thái trace:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Excerpt/anchor đã lưu:** “A Cosserat rod is defined by its centerline”
- **Ranh giới/ghi chú:** Đoạn PDF đã đọc trực tiếp; không dùng locator M03-E02 trang 3 bị sai.

**CH2-S2-R0028-A01 — mục 2.2.1.** Với giả thiết Euler–Bernoulli thông thường, tiết diện giữ vuông góc với đường trục nên bỏ qua biến dạng cắt; mô tả thanh cho phép tiết diện nghiêng so với tiếp tuyến có thể giữ biến dạng cắt [6].

- **Locator PDF trong trace:** §3.1.3, đoạn rigid cross section. **Trạng thái trace:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Excerpt/anchor đã lưu:** “not necessarily normal to the tangent”
- **Ranh giới/ghi chú:** Phân biệt động học tiết diện; không suy cùng một luật vật liệu cho các lý thuyết.


## [7] H. Jeon, Q. N. Le, S. Jeong, S. Jang, H. Jung, H. Chang, H. J. Pandya & Y. Kim (2022), “Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism”

**CH2-S2-R0022-A01 — mục 2.2.1.** Trong thí nghiệm của Jeon và cộng sự, độ cứng robot được lấy từ độ dốc lực cản–chuyển vị của đĩa đầu, còn độ cứng uốn được suy ra bằng xấp xỉ dầm công xôn [7].

- **Locator PDF trong trace:** §IV-B, đoạn stiffness slope và Eq. (10). **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Excerpt/anchor đã lưu:** “The stiffness is the slope of the resistive force vs. displacement graph”
- **Ranh giới/ghi chú:** Thí nghiệm riêng với đĩa đầu, góc uốn nhỏ; không chuyển công thức sang MP1.

**CH2-S4-R0055-A01 — mục 2.4.3.** Cơ cấu của Jeon và cộng sự [7] cung cấp một tiền lệ trực tiếp cho đường truyền lực này. Thân robot có lõi polyuretan nhiệt dẻo (TPU) ở giữa và tám dây siêu đàn hồi bố trí xung quanh, đi qua các đĩa dẫn hướng. Các dây chỉ cố định tại đế nên có thể trượt qua những đĩa còn lại khi thân uốn. Một ống cao su bao quanh đoạn trung tâm, còn lò xo SMA quấn bên ngoài ống. Khi nung nóng, lò xo có xu hướng phục hồi về đường kính trong đã ghi nhớ nhỏ hơn. Sự phục hồi bị ống và các dây cản lại tạo tác dụng siết hướng kính, ép cao su vào dây và hạn chế chuyển động trượt. Lõi TPU và ống cao su có vai trò riêng trong cấu trúc này. Bề mặt điều biến ma sát được khảo sát là tiếp xúc dây với cao su, chưa phải bằng chứng cho cơ chế kẹt giữa các dây trong một bó dây.

- **Locator PDF trong trace:** M31:2–3; Secs.II.A–II.B; Fig.1. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0056-A01 — mục 2.4.3.** Cơ cấu của Jeon và cộng sự [7] cung cấp một tiền lệ trực tiếp cho đường truyền lực này. Thân robot có lõi polyuretan nhiệt dẻo (TPU) ở giữa và tám dây siêu đàn hồi bố trí xung quanh, đi qua các đĩa dẫn hướng. Các dây chỉ cố định tại đế nên có thể trượt qua những đĩa còn lại khi thân uốn. Một ống cao su bao quanh đoạn trung tâm, còn lò xo SMA quấn bên ngoài ống. Khi nung nóng, lò xo có xu hướng phục hồi về đường kính trong đã ghi nhớ nhỏ hơn. Sự phục hồi bị ống và các dây cản lại tạo tác dụng siết hướng kính, ép cao su vào dây và hạn chế chuyển động trượt. Lõi TPU và ống cao su có vai trò riêng trong cấu trúc này. Bề mặt điều biến ma sát được khảo sát là tiếp xúc dây với cao su, chưa phải bằng chứng cho cơ chế kẹt giữa các dây trong một bó dây.

- **Locator PDF trong trace:** M31:2–3; Sec.II.A; Fig.1d–f. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0056-A02 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:2–3; Sec.II.A; Fig.1d–f. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0057-A01 — mục 2.4.3.** Giá trị của nghiên cứu [7] nằm ở việc đo lực trượt riêng bên cạnh đáp ứng uốn của toàn thân. Trong phép thử ma sát, một dây được kéo qua ống cao su, còn bảy dây được giữ cố định. Hành trình kéo là 5 mm với tốc độ 10 mm/phút; mỗi cấu hình đường kính và trạng thái pha được lặp lại mười lần. Phép thử này cho phép quan sát trực tiếp lực cản kéo dây khi thay đổi trạng thái của lò xo SMA. Tuy nhiên, lực kéo đo được là kết quả của tiếp xúc trong cấu hình thử cụ thể, không phải phép đo riêng lực kẹp của lò xo hoặc lực pháp tuyến cục bộ. Khi chưa xác định độc lập tải ép, cũng không thể dùng lực kéo để suy ra duy nhất hệ số ma sát. Giá trị đỉnh hoặc trung bình trên hành trình thử chỉ đặc trưng cho quy trình đó, chưa đủ để coi là giới hạn chống trượt chung của cơ cấu [7].

- **Locator PDF trong trace:** M31:5–6; Sec.IV.A; Fig.4;TableI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0058-A01 — mục 2.4.3.** Cơ cấu của Jeon và cộng sự [7] cung cấp một tiền lệ trực tiếp cho đường truyền lực này. Thân robot có lõi polyuretan nhiệt dẻo (TPU) ở giữa và tám dây siêu đàn hồi bố trí xung quanh, đi qua các đĩa dẫn hướng. Các dây chỉ cố định tại đế nên có thể trượt qua những đĩa còn lại khi thân uốn. Một ống cao su bao quanh đoạn trung tâm, còn lò xo SMA quấn bên ngoài ống. Khi nung nóng, lò xo có xu hướng phục hồi về đường kính trong đã ghi nhớ nhỏ hơn. Sự phục hồi bị ống và các dây cản lại tạo tác dụng siết hướng kính, ép cao su vào dây và hạn chế chuyển động trượt. Lõi TPU và ống cao su có vai trò riêng trong cấu trúc này. Bề mặt điều biến ma sát được khảo sát là tiếp xúc dây với cao su, chưa phải bằng chứng cho cơ chế kẹt giữa các dây trong một bó dây.

- **Locator PDF trong trace:** M31:5–6; Sec.IV.A; Fig.4c–e;TableI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0058-A02 — mục 2.4.3.** Giá trị của nghiên cứu [7] nằm ở việc đo lực trượt riêng bên cạnh đáp ứng uốn của toàn thân. Trong phép thử ma sát, một dây được kéo qua ống cao su, còn bảy dây được giữ cố định. Hành trình kéo là 5 mm với tốc độ 10 mm/phút; mỗi cấu hình đường kính và trạng thái pha được lặp lại mười lần. Phép thử này cho phép quan sát trực tiếp lực cản kéo dây khi thay đổi trạng thái của lò xo SMA. Tuy nhiên, lực kéo đo được là kết quả của tiếp xúc trong cấu hình thử cụ thể, không phải phép đo riêng lực kẹp của lò xo hoặc lực pháp tuyến cục bộ. Khi chưa xác định độc lập tải ép, cũng không thể dùng lực kéo để suy ra duy nhất hệ số ma sát. Giá trị đỉnh hoặc trung bình trên hành trình thử chỉ đặc trưng cho quy trình đó, chưa đủ để coi là giới hạn chống trượt chung của cơ cấu [7].

- **Locator PDF trong trace:** M31:5–6; Sec.IV.A; Fig.4c–e;TableI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0058-A03 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:5–6; Sec.IV.A; Fig.4c–e;TableI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0059-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:5–6; Sec.IV.B; Fig.5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0060-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:6; Sec.IV.B; Eq.10 (omitted). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0061-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:3–5,7; Sec.III;Sec.V; Fig.3;Eqs.1–9 (omitted). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0062-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:6–7; Secs.IV.B/V; TablesII–III. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0063-A01 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:3,5–7; Secs.II.B;IV introduction;IV.C/V; Fig.6. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0064-A01 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:6–7; Sec.IV.C/V; Fig.6b–c. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0065-A01 — mục 2.4.3.** Điều kiện nhiệt giới hạn cách diễn giải khả năng điều khiển của cơ cấu này. Jeon và cộng sự [7] điều chỉnh thủ công dòng điện để duy trì nhiệt độ lò xo khoảng 50–60 °C, theo dõi bằng ảnh hồng ngoại; trạng thái martensit được xét ở nhiệt độ môi trường khoảng 23 °C. Trong thử nghiệm nhiệt riêng với dòng điện 0,5 A, thời gian nung từ 25 lên 60 °C được báo cáo khoảng 18 s, còn thời gian chuyển trạng thái khi làm nguội tự nhiên khoảng 60 s. Các thời gian này thuộc lò xo và điều kiện truyền nhiệt của nguyên mẫu, không phải tốc độ chuyển mạch chung của cơ cấu SMA. Nhiệt độ hồng ngoại tại lò xo cũng không chứng minh các phần tử chịu tải có cùng nhiệt độ. Khi nguội, tác dụng siết giảm; điều đó chưa chứng minh ma sát triệt tiêu hoặc lò xo tự trở lại hoàn toàn đường kính ban đầu. Nghiên cứu chưa nhận dạng đầy đủ vòng trễ của độ cứng hoặc lực tiếp xúc theo nhiệt độ, và chưa sử dụng phản hồi nhiệt độ thời gian thực để điều khiển cơ cấu [7].

- **Locator PDF trong trace:** M31:7; Sec.V Discussion/Conclusion; Limitations paragraph. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0076-A02 — mục 2.4.3.** Giá trị của nghiên cứu [7] nằm ở việc đo lực trượt riêng bên cạnh đáp ứng uốn của toàn thân. Trong phép thử ma sát, một dây được kéo qua ống cao su, còn bảy dây được giữ cố định. Hành trình kéo là 5 mm với tốc độ 10 mm/phút; mỗi cấu hình đường kính và trạng thái pha được lặp lại mười lần. Phép thử này cho phép quan sát trực tiếp lực cản kéo dây khi thay đổi trạng thái của lò xo SMA. Tuy nhiên, lực kéo đo được là kết quả của tiếp xúc trong cấu hình thử cụ thể, không phải phép đo riêng lực kẹp của lò xo hoặc lực pháp tuyến cục bộ. Khi chưa xác định độc lập tải ép, cũng không thể dùng lực kéo để suy ra duy nhất hệ số ma sát. Giá trị đỉnh hoặc trung bình trên hành trình thử chỉ đặc trưng cho quy trình đó, chưa đủ để coi là giới hạn chống trượt chung của cơ cấu [7].

- **Locator PDF trong trace:** M31:2–3,5–6; Mechanical pathway synthesis; No equation. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S4-R0077-A01 — mục 2.4.3.** Đáp ứng uốn trong [7] được đo bằng lực ngang và chuyển vị đầu tự do, với hành trình 5 mm và tốc độ 10 mm/phút, cũng lặp lại mười lần. Độ dốc quan hệ lực với độ võng biểu thị độ cứng kết cấu trong phép thử uốn. Đại lượng này khác mô đun đàn hồi của vật liệu; độ cứng uốn tương đương EI còn được suy ra qua quan hệ dầm công xôn với giả thiết góc nhỏ. Mô hình năng lượng của tác giả mô tả chuyển động trượt theo cung tròn và sử dụng lực ma sát trung bình của một dây để tính đóng góp của tám dây. Sự phù hợp với dữ liệu trên cùng nguyên mẫu hỗ trợ cách giải thích rằng việc cản trượt làm tăng khả năng chịu uốn. Nó chưa xác nhận độc lập phân bố lực tiếp xúc hoặc khả năng mô tả mọi lịch sử tải. Do đó, phép đo lực kéo là mắt xích thực nghiệm bổ sung để nối cơ chế tiếp xúc với đáp ứng kết cấu, còn sự tăng độ dốc lực với độ võng tự nó chưa nhận dạng đầy đủ cơ chế ma sát.

- **Locator PDF trong trace:** M31:5–7;M32:7–8;M37:4–6; Cross-study observable comparison; Original comparison table. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S6-R0047-A01 — mục 2.6.1.** Vai trò chấp hành của SMA đã được khai thác trong một cơ cấu khác, nơi lò xo SMA bao quanh ống cao su để điều chỉnh tương tác với các dây ngoại vi [7].

- **Locator PDF trong trace:** {"M31-E01": "§II.A; Fig. 1"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “The core of the proposed stiffness control mechanism is the frictional force”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0123-A01 — mục 2.6.2.** Một phản chứng đối với nhận định rằng các nghiên cứu chỉ đo đáp ứng toàn cục xuất hiện trong cơ cấu SMA của Jeon và cộng sự: tác giả kéo riêng một dây trong ống cao su để đo ma sát, tách khỏi thử uốn [7].

- **Locator PDF trong trace:** {"M31-E06": ["§IV.A Friction Force Characterization; Fig. 4; Table I"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “A single wire is attached; friction force tests were repeated ten times”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0165-A01 — mục 2.6.3.** Jeon và cộng sự đã đo riêng lực cản khi kéo một dây qua ống cao su trong cơ cấu siết bằng lò xo SMA [7].

- **Locator PDF trong trace:** {"M31-E01": ["§II-A; Fig.1"], "M31-E06": ["§IV-A; Fig.4; TableI"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “CSV chỉ có nội dung finding tóm tắt, không có quote anchor.”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0220-A01 — mục 2.6.4.** Jeon và cộng sự đã bổ sung phép kéo một dây tương đối với ống cao su để đo lực cản riêng, bên cạnh phép đánh giá độ cứng toàn cơ cấu [7].

- **Locator PDF trong trace:** {"M31-E06":[{"physical_pages":[5],"printed_pages":["6586"],"exact_locator":"IV. Experiment Setup and Result; A. Friction Force Characterization; Fig.4","anchor":"repeated ten times"},{"physical_pages":[6],"printed_pages":["6587"],"exact_locator":"IV.A continued; TableI; IV.B Stiffness Characterization of the Robot; TableII","anchor":"slope of the resistive force"}],"M31-E07":[{"physical_pages":[6],"printed_pages":["6587"],"exact_locator":"IV.A continued; TableI; IV.B Stiffness Characterization of the Robot; TableII","anchor":"slope of the resistive force"},{"physical_pages":[7],"printed_pages":["6588"],"exact_locator":"IV.B continued; TableIII","anchor":"modeled ﬂexural rigidity"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “CSV chỉ có nội dung finding tóm tắt, không có quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.


## [8] Y. Zhang, J. Wang, G. Ye & R. Xu (2018), “Bending Stiffness of Parallel Wire Cables Including Interfacial Slips among Wires”

**CH2-S2-R0031-A01 — mục 2.2.1.** Mô hình cáp dây song song của Zhang và cộng sự dùng các lớp tương đương có cùng độ võng và độ cong, không cho tách lớp, nhưng vẫn cho phép trượt dọc tương đối tại giao diện [8].

- **Locator PDF trong trace:** Modeling and Formulation, assumptions 1–3. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Excerpt/anchor đã lưu:** “Slip is allowed at each interface”
- **Ranh giới/ghi chú:** Cáp được thay bằng lớp chữ nhật bảo toàn chiều cao/diện tích; không phải hình học dây tròn MP1.

**CH2-S2-R0032-A01 — mục 2.2.1.** Nguồn còn đưa vào độ cứng trượt đã hiệu chuẩn và nêu rõ tương tác ma sát thực phức tạp hơn giả thiết giao diện tuyến tính [8].

- **Locator PDF trong trace:** Eq. (4) và đoạn giới hạn ngay sau. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Excerpt/anchor đã lưu:** “not elastic because of the friction among wires”
- **Ranh giới/ghi chú:** Độ cứng trượt của giao diện khác K lực–chuyển vị của toàn cơ cấu.

**CH2-S2-R0033-A01 — mục 2.2.1.** Ví dụ này cho thấy cùng độ võng ngang không đồng nghĩa cùng biến dạng dọc của mọi phần tử; giả thiết tiết diện liên hợp hoàn toàn cần được kiểm tra khi có chuyển vị tương đối [8].

- **Locator PDF trong trace:** Assumptions 2–3; PDF3 Eqs. (4)–(5). **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE_WITH_REGISTERED_ID`.
- **Excerpt/anchor đã lưu:** “Each rectangular layer has the same curvature and deflection”
- **Ranh giới/ghi chú:** Suy từ cấu trúc biến của mô hình, không khẳng định MP1 đã có trượt.

**CH2-S2-R0035-A01 — mục 2.2.1.** Tuy nhiên, mô hình dầm hiệu dụng vẫn có thể biểu diễn đáp ứng tổng thể trong một miền được kiểm chứng; mô hình cáp có xét trượt trong [8] là một ví dụ về khả năng giữ ảnh hưởng trượt trong phép quy giản dầm.

- **Locator PDF trong trace:** Abstract, equivalent bending stiffness. **Trạng thái trace:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Excerpt/anchor đã lưu:** “equivalent bending stiffness (EBS)”
- **Ranh giới/ghi chú:** Nguồn hiệu chuẩn với thử nghiệm trong tài liệu; không chứng minh tính phổ quát hoặc độ đúng MP1.

**CH2-S2-R0037-A01 — mục 2.2.1.** Một đường cong tổng thể phù hợp chưa đủ để xác định duy nhất sự phân bố tiếp xúc và trượt bên trong, vì mô hình có thể gộp chúng vào tham số hiệu dụng [8].

- **Locator PDF trong trace:** Đoạn giới hạn/hiệu chuẩn ngay sau Eq. (4). **Trạng thái trace:** `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID`.
- **Excerpt/anchor đã lưu:** “calibrated”
- **Ranh giới/ghi chú:** Suy luận về khả năng nhận dạng, không phải phép chứng minh tính không duy nhất do tác giả M22 thực hiện.

**CH2-S2-R0071-A01 — mục 2.2.2.** Slip được xác định bằng chuyển vị tương đối theo phương tiếp tuyến giữa hai phía giao diện đã chọn; trong mô hình cáp dây song song, Zhang và cộng sự biểu diễn độ trượt qua các chuyển vị dọc và góc xoay của lớp tương đương [8].

- **Locator PDF trong trace:** Eqs. (4)–(5) and explanatory text. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “The slip has a relation with the axial displacements and deflec-”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S4-R0021-A02 — mục 2.4.2.** Trong mô hình của Zhang và cộng sự năm 2018 [8], mỗi hàng dây được thay bằng một lớp chữ nhật, bảo toàn tổng chiều cao và diện tích dây của hàng. Các lớp có chung độ võng và độ cong, không tách nhau theo phương đứng hoặc phương ngang, nhưng có thể trượt tương đối dọc trục. Lực tương tác tại mặt phân cách được giả thiết tỷ lệ tuyến tính với độ trượt thông qua tham số k. Cách quy đổi này giữ lại khả năng truyền lực giữa các hàng dây trong một mô hình dầm, đồng thời lược bỏ mô tả riêng từng vùng tiếp xúc cong của dây tròn. Nghiên cứu xét tải phân bố ngang đều hoặc lực tập trung giữa nhịp cùng lực kéo dọc trục, với các ví dụ dầm tựa đơn.

- **Locator PDF trong trace:** Physical PDF M22:2–3; Modeling and Formulation; Fig.1; Eqs.4–8 (not reproduced). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0022-A01 — mục 2.4.2.** Tham số độ cứng chống trượt k trong [8] là sức cản tương đương được hiệu chỉnh từ quan hệ lực và chuyển vị uốn của các mẫu Chen dưới những mức lực kéo dọc trục. Tham số này bao hàm ảnh hưởng của vỏ bảo vệ, sự siết giữ và hiệu ứng Poisson. Do đó, k không phải hệ số ma sát, không phải áp suất pháp tại tiếp xúc và không tạo thành một quy luật liên hệ giữa áp suất với ma sát. Việc nghiệm của mô hình phù hợp với nghiệm không gian trạng thái hoặc các trường hợp giới hạn cổ điển kiểm tra tính nhất quán của lời giải toán học. Phần đối chiếu thực nghiệm lại dựa trên dữ liệu đã công bố; đó không phải một thí nghiệm mới do nhóm tác giả thực hiện.

- **Locator PDF trong trace:** Physical PDF M22:3,7; Governing Differential Equations; Calibration of Slip Rigidity; Eq.4; Eq.37 and accompanying prose. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0023-A01 — mục 2.4.2.** Trong mô hình của Zhang và cộng sự năm 2018 [8], mỗi hàng dây được thay bằng một lớp chữ nhật, bảo toàn tổng chiều cao và diện tích dây của hàng. Các lớp có chung độ võng và độ cong, không tách nhau theo phương đứng hoặc phương ngang, nhưng có thể trượt tương đối dọc trục. Lực tương tác tại mặt phân cách được giả thiết tỷ lệ tuyến tính với độ trượt thông qua tham số k. Cách quy đổi này giữ lại khả năng truyền lực giữa các hàng dây trong một mô hình dầm, đồng thời lược bỏ mô tả riêng từng vùng tiếp xúc cong của dây tròn. Nghiên cứu xét tải phân bố ngang đều hoặc lực tập trung giữa nhịp cùng lực kéo dọc trục, với các ví dụ dầm tựa đơn.

- **Locator PDF trong trace:** Physical PDF M22:1,4–5; Abstract; Numerical Examples; Fig.3; Table1; Figs.4–5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0023-A02 — mục 2.4.2.** Tham số độ cứng chống trượt k trong [8] là sức cản tương đương được hiệu chỉnh từ quan hệ lực và chuyển vị uốn của các mẫu Chen dưới những mức lực kéo dọc trục. Tham số này bao hàm ảnh hưởng của vỏ bảo vệ, sự siết giữ và hiệu ứng Poisson. Do đó, k không phải hệ số ma sát, không phải áp suất pháp tại tiếp xúc và không tạo thành một quy luật liên hệ giữa áp suất với ma sát. Việc nghiệm của mô hình phù hợp với nghiệm không gian trạng thái hoặc các trường hợp giới hạn cổ điển kiểm tra tính nhất quán của lời giải toán học. Phần đối chiếu thực nghiệm lại dựa trên dữ liệu đã công bố; đó không phải một thí nghiệm mới do nhóm tác giả thực hiện.

- **Locator PDF trong trace:** Physical PDF M22:1,4–5; Abstract; Numerical Examples; Fig.3; Table1; Figs.4–5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S6-R0027-A01 — mục 2.6.1.** Đối với cáp thép gồm các dây song song, mô hình dầm phân lớp đã đưa tương tác chống trượt vào mô tả độ cứng uốn tương đương [8].

- **Locator PDF trong trace:** {"M22-E01": "Abstract; Modeling and formulation", "M22-E02": "Model of laminated beam with interfacial slips; Eqs. (1)–(9)"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “idealized as laminated beams including interlayer slips; Slip is allowed at each interface”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0115-A01 — mục 2.6.2.** Trong nghiên cứu cáp thép gồm dây song song, tương tác và trượt giữa các thành phần đã được đưa vào mô hình dầm phân lớp, nên không thể xem mọi mô hình cáp là bỏ qua tương tác dây [8].

- **Locator PDF trong trace:** {"M22-E01": ["Abstract; Abstract; direct page/anchor controls"], "M22-E02": ["Modeling and formulation; Eqs. (1)–(9); direct page/anchor controls", "Modeling and formulation; Eqs. (1)–(9); direct page/anchor controls"], "M22-E04": ["Calibration; Eq. (37); direct page/anchor controls", "Calibration; Eq. (37); direct page/anchor controls"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “Each rectangular layer has the same curvature and deflection; Each rectangular layer has the same curvature and deflection; The initial slip”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.


## [9] Y. S. Narang, J. J. Vlassak & R. D. Howe (2018), “Mechanically Versatile Soft Machines through Laminar Jamming”

**CH2-S2-R0061-A01 — mục 2.2.2.** Jamming được hiểu ở cấp kết cấu là sự tăng ràng buộc chuyển động tương đối giữa các phần tử, nhờ đó tương tác ma sát có thể làm chúng truyền tải cùng nhau mạnh hơn [9].

- **Locator PDF trong trace:** Abstract. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “a structural phenomenon in which a laminate of compliant strips becomes strongly coupled through friction”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0064-A01 — mục 2.2.2.** Trong cấu trúc laminar của Narang và cộng sự, trạng thái đã hút chân không vẫn có thể chuyển từ miền tiền trượt sang miền có trượt khi tải tăng [9].

- **Locator PDF trong trace:** §2.1 and Fig. 1. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “all layers have slipped along the full length of their interfaces”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0077-A01 — mục 2.2.2.** Trượt vẫn có thể truyền lực ma sát; Narang và cộng sự còn thu được lực cản tiêu tán trong miền full slip [9].

- **Locator PDF trong trace:** §2.1; Fig. 2. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “full-slip damping force was given succinctly by”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S3-R0016-A01 — mục Introduction / Fig. 1.** Đối chiếu với kẹt lớp/tấm của Narang và cộng sự cho thấy điểm chung chủ yếu nằm ở sự chuyển tiếp giữa trạng thái dính và trượt [9]. Trong chồng lớp, khi lực cắt dọc vượt giới hạn ma sát, trượt khởi phát tại một số vùng và làm giảm độ cứng; nguồn mô tả các miền tiền-trượt, chuyển tiếp và trượt hoàn toàn. Kết quả này cung cấp một tương tự cơ học để đặt câu hỏi về ngưỡng trượt và điều kiện biên, nhưng không phải bằng chứng trực tiếp cho kẹt dây hoặc kẹt sợi. Các đại lượng độ cứng của chồng lớp giấy, dây/cáp và mô-đun sợi không tự động cùng nghĩa, vì chúng được đo trên hình học, cách xếp phần tử và điều kiện tải khác nhau.

- **Locator PDF trong trace:** Fig. 1. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** M07 là laminar-sheet comparator, không phải direct wire/fiber evidence và không chuyển ngưỡng sang MP1.

**CH2-S3-R0032-A01 — mục Experiments.** Nghiên cứu của Narang và cộng sự cung cấp đối chứng thực nghiệm–mô phỏng cho cấu hình kẹt lớp chân không. Các mẫu gồm 5, 10, 15 và 20 lớp, được khảo sát ở các độ lớn chân không 0, 24, 47 và 71 kPa bằng phép uốn ba điểm; đường lực–độ võng được dùng để đánh giá độ cứng [9]. Tác giả phân biệt miền trước trượt, miền chuyển tiếp và miền trượt hoàn toàn. Trong miền chuyển tiếp, trượt khởi phát tại những vùng mà ứng suất cắt giao diện đạt sức kháng ma sát cực đại rồi lan truyền theo tải. Mô hình phần tử hữu hạn và thí nghiệm đạt hệ số xác định nhỏ nhất R² = 0,9879 trong tập được báo cáo. Kết quả cho thấy mô hình có thể phù hợp tốt trong cấu hình đã kiểm tra, nhưng không chứng minh rằng cùng một biểu diễn trượt vẫn đúng khi số lớp tăng cao hơn hoặc khi trường áp suất không đồng đều; hơn nữa, đây là bằng chứng về áp suất âm, không phải áp suất dương.

- **Locator PDF trong trace:** Fig.3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Chỉ là bằng chứng kẹt lớp chân không, không phải positive pressure.

**CH2-S3-R0033-A01 — mục Experiments.** Nghiên cứu của Narang và cộng sự cung cấp đối chứng thực nghiệm–mô phỏng cho cấu hình kẹt lớp chân không. Các mẫu gồm 5, 10, 15 và 20 lớp, được khảo sát ở các độ lớn chân không 0, 24, 47 và 71 kPa bằng phép uốn ba điểm; đường lực–độ võng được dùng để đánh giá độ cứng [9]. Tác giả phân biệt miền trước trượt, miền chuyển tiếp và miền trượt hoàn toàn. Trong miền chuyển tiếp, trượt khởi phát tại những vùng mà ứng suất cắt giao diện đạt sức kháng ma sát cực đại rồi lan truyền theo tải. Mô hình phần tử hữu hạn và thí nghiệm đạt hệ số xác định nhỏ nhất R² = 0,9879 trong tập được báo cáo. Kết quả cho thấy mô hình có thể phù hợp tốt trong cấu hình đã kiểm tra, nhưng không chứng minh rằng cùng một biểu diễn trượt vẫn đúng khi số lớp tăng cao hơn hoặc khi trường áp suất không đồng đều; hơn nữa, đây là bằng chứng về áp suất âm, không phải áp suất dương.

- **Locator PDF trong trace:** Fig.3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Độ khớp không chứng minh ngoại suy số lớp cao hoặc áp suất không đều.

**CH2-S5-R0005-A01 — mục §2.5.1.** Narang, Vlassak và Howe nghiên cứu chồng lớp giấy trong bao hút chân không. Ở trạng thái không hút, các lớp uốn gần như độc lập; khi hút, ma sát ghép các lớp thành một phần tử chịu uốn. Hình 1 của nguồn mô tả miền pre-slip, miền chuyển tiếp và miền full-slip. Trong pre-slip, các lớp được mô tả là dính kết, độ cứng lớn và gần như không tiêu tán năng lượng. Khi tải tăng, ứng suất cắt dọc tại một số vùng giao diện đạt giới hạn do hệ số ma sát và gradient áp suất quyết định; các vùng đó trượt và độ cứng giảm. Trong full-slip, nguồn gọi là mọi lớp đã trượt dọc theo toàn bộ chiều dài giao diện, nên độ cứng kết cấu đạt mức thấp nhất trong mô hình. Đây là mô tả cơ học của chồng lớp giấy dưới tải uốn, không phải phép đo trực tiếp tt(x) hay pn(x) trên từng giao diện [9].

- **Locator PDF trong trace:** Introduction/Fig. 1. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không đo trực tiếp traction cục bộ hay p_n(x).

**CH2-S5-R0006-A01 — mục §2.5.1.** Mô hình hai lớp của cùng nghiên cứu dùng dầm Euler–Bernoulli, cấu hình công xôn ngàm–tự do và tải phân bố để theo dõi vùng trượt. Vùng này được dự đoán khởi phát gần đầu ngàm rồi phát triển về phía đầu tự do khi tải tăng; mô hình phần tử hữu hạn hai lớp tái hiện vùng trượt dự đoán. Các mô phỏng nhiều lớp cho phép tiếp xúc ma sát đồng thời ở các giao diện và có phân tích biến dạng lớn, trong khi thí nghiệm uốn ba điểm ghi lực–độ võng ở 5, 10, 15 và 20 lớp, với các mức chân không 0, 24, 47 và 71 kPa. Mức phù hợp cao giữa mô phỏng và lực–độ võng chỉ kiểm chứng đáp ứng kết cấu trong kiến trúc đã xét; hệ số ma sát không được đo trực tiếp với độ chính xác độc lập [9].

- **Locator PDF trong trace:** Analytical model/Fig. 2; Experiments/Fig. 3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Validation của đáp ứng kiến trúc, không phải luật tiếp xúc MP1.

**CH2-S5-R0023-A01 — mục §2.5.2.** Narang, Vlassak và Howe dùng mô hình hai lớp công xôn ngàm–tự do với tải phân bố đều. Vùng trượt được dự đoán khởi phát gần đầu ngàm rồi lan về phía tự do khi tải tăng; mô hình phần tử hữu hạn hai lớp tái hiện vùng này. Kết quả cho thấy một cấu trúc có thể đồng thời chứa vùng dính và vùng trượt, nên không thể dùng một trạng thái full-slip cục bộ để suy ra cận dây độc lập cho toàn tiết diện [9].

- **Locator PDF trong trace:** Analytical model/Fig.2/SI. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không cung cấp cận MP1; topology là laminar paper.

**CH2-S5-R0040-A01 — mục §2.5.3.** Trong thí nghiệm của Narang và cộng sự, các mẫu chồng lớp giấy được uốn ba điểm và biểu diễn bằng lực ngang–độ võng. Hình 3 so sánh 5, 10, 15 và 20 lớp ở 71 kPa, các mức chân không 0, 24, 47 và 71 kPa với 20 lớp, cùng các giá trị hệ số ma sát chỉ trong phần tử hữu hạn. Đường thực nghiệm là trung bình với dải ±1 độ lệch chuẩn; độ lệch cực đại được báo cáo là 0,24 N và R² nhỏ nhất giữa phần tử hữu hạn với thực nghiệm là 0,9879. Đây là kiểm tra đáp ứng kết cấu trong cấu hình lớp giấy; không phải nhận dạng trực tiếp hệ số ma sát, lực pháp tuyến cục bộ hay vị trí trượt [9].

- **Locator PDF trong trace:** Experiments/Fig.3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không đo local slip/traction/μ thực nghiệm.

**CH2-S5-R0081-A01 — mục §2.5.5.** Nhóm mô hình dầm giải tích hoặc elastica giữ lại cân bằng lực–mô men và các điều kiện biên để tạo ra một mô tả cơ học có thể diễn giải. Narang, Vlassak và Howe phát triển mô hình elastica hai lớp công xôn, dùng ma sát Coulomb tại giao diện; vùng trượt bắt đầu gần ngàm và mở rộng về phía đầu tự do khi tải tăng. Mô hình dự đoán hình dạng elastica, độ cứng, năng lượng tiêu tán, lực chuyển tiếp và chiều dài vùng trượt. Hai lớp được đối chiếu bằng mô hình phần tử hữu hạn, còn các cấu hình nhiều lớp được mô phỏng và so sánh với thí nghiệm uốn ba điểm trong phạm vi 5–20 lớp và áp suất chân không 0–71 kPa [9]. Bài báo nêu rằng mô hình FE không dùng tham số khớp, nhưng hệ số ma sát trong khảo sát số là đầu vào được quy định; các đường thực nghiệm theo hệ số ma sát không được thu thập do khó điều chỉnh chính xác. Do đó, đây là bằng chứng mạnh cho tính diễn giải của cơ chế trượt trong kiến trúc lớp giấy đã xét, đồng thời là đối chiếu FE–thực nghiệm có phạm vi, chứ không phải kiểm chứng độc lập cho bó dây TiNi hoặc cho cấu hình dây–ống bao.

- **Locator PDF trong trace:** PDF physical p.3, Fig. 2 and Sec. 2.1 Analytical Modeling. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Not a TiNi wire/sleeve validation

**CH2-S5-R0082-A01 — mục §2.5.5.** Nhóm mô hình dầm giải tích hoặc elastica giữ lại cân bằng lực–mô men và các điều kiện biên để tạo ra một mô tả cơ học có thể diễn giải. Narang, Vlassak và Howe phát triển mô hình elastica hai lớp công xôn, dùng ma sát Coulomb tại giao diện; vùng trượt bắt đầu gần ngàm và mở rộng về phía đầu tự do khi tải tăng. Mô hình dự đoán hình dạng elastica, độ cứng, năng lượng tiêu tán, lực chuyển tiếp và chiều dài vùng trượt. Hai lớp được đối chiếu bằng mô hình phần tử hữu hạn, còn các cấu hình nhiều lớp được mô phỏng và so sánh với thí nghiệm uốn ba điểm trong phạm vi 5–20 lớp và áp suất chân không 0–71 kPa [9]. Bài báo nêu rằng mô hình FE không dùng tham số khớp, nhưng hệ số ma sát trong khảo sát số là đầu vào được quy định; các đường thực nghiệm theo hệ số ma sát không được thu thập do khó điều chỉnh chính xác. Do đó, đây là bằng chứng mạnh cho tính diễn giải của cơ chế trượt trong kiến trúc lớp giấy đã xét, đồng thời là đối chiếu FE–thực nghiệm có phạm vi, chứ không phải kiểm chứng độc lập cho bó dây TiNi hoặc cho cấu hình dây–ống bao.

- **Locator PDF trong trace:** PDF physical p.3, Sec. 2.1–2.2 and SI Governing Equations. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** High-layer extrapolation and homogeneous pressure limits

**CH2-S5-R0083-A01 — mục §2.5.5.** Nhóm mô hình dầm giải tích hoặc elastica giữ lại cân bằng lực–mô men và các điều kiện biên để tạo ra một mô tả cơ học có thể diễn giải. Narang, Vlassak và Howe phát triển mô hình elastica hai lớp công xôn, dùng ma sát Coulomb tại giao diện; vùng trượt bắt đầu gần ngàm và mở rộng về phía đầu tự do khi tải tăng. Mô hình dự đoán hình dạng elastica, độ cứng, năng lượng tiêu tán, lực chuyển tiếp và chiều dài vùng trượt. Hai lớp được đối chiếu bằng mô hình phần tử hữu hạn, còn các cấu hình nhiều lớp được mô phỏng và so sánh với thí nghiệm uốn ba điểm trong phạm vi 5–20 lớp và áp suất chân không 0–71 kPa [9]. Bài báo nêu rằng mô hình FE không dùng tham số khớp, nhưng hệ số ma sát trong khảo sát số là đầu vào được quy định; các đường thực nghiệm theo hệ số ma sát không được thu thập do khó điều chỉnh chính xác. Do đó, đây là bằng chứng mạnh cho tính diễn giải của cơ chế trượt trong kiến trúc lớp giấy đã xét, đồng thời là đối chiếu FE–thực nghiệm có phạm vi, chứ không phải kiểm chứng độc lập cho bó dây TiNi hoặc cho cấu hình dây–ống bao.

- **Locator PDF trong trace:** PDF physical p.4, Fig. 3 and Sec. 2.2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Values not transferable to TiNi bundle


## [10] F. Caruso, G. Mantriota, V. Moramarco & G. Reina (2023), “Layer jamming: Modeling and experimental validation”

**CH2-S2-R0074-A01 — mục 2.2.2.** Phải nêu rõ phạm vi ấy: mô hình Caruso và cộng sự vẫn giữ một miền ngoài gối tựa liên kết với nhau trong khi miền giữa các gối đã trượt [10].

- **Locator PDF trong trace:** §2.1, internal/external region approximation. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “the external region will remain cohesive”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0081-A01 — mục 2.2.2.** Các miền tiền trượt, trượt một phần và trượt toàn phần hữu ích để diễn giải một số mô hình layer jamming, nhưng không đặt ra ba ngưỡng tải tách bạch cho mọi kiến trúc [10].

- **Locator PDF trong trace:** Fig. 1 caption. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “the shear stress at each interface remains below the static friction limit”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S3-R0045-A01 — mục Secs.5.1–5.3.** Các kết quả của Caruso và cộng sự minh họa rõ quan hệ giữa điều kiện thử và mức độ kiểm chứng. Với mẫu chữ nhật, b = 6 cm, L = 18 cm và lớp giấy dày 0,1 mm, bốn cấu hình 8, 12, 16 và 20 lớp được thử ở 68 kPa; cấu hình 20 lớp được thử thêm ở 24 và 48 kPa, mỗi điều kiện lặp ba lần [10]. Phép uốn ba điểm ghi lực–độ võng và năng lượng tiêu tán; mô hình giải tích, phần tử hữu hạn và thí nghiệm được so sánh trong cùng miền hình học. Mô hình mô tả được sự lan truyền trượt và xu hướng thay đổi độ cứng, nhưng sai lệch tăng ở độ võng lớn do mô hình giải tích bỏ qua áp suất và ứng suất tiếp xúc phát sinh tại gối đỡ. Vì vậy, kết quả này xác lập một miền kiểm chứng cụ thể, không phải luật phổ quát theo số lớp.

- **Locator PDF trong trace:** Fig.4. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Mẫu chữ nhật, uốn ba điểm, giấy/TPU và biên đỡ cụ thể.

**CH2-S3-R0046-A01 — mục Secs.5.1–6.** Các kết quả của Caruso và cộng sự minh họa rõ quan hệ giữa điều kiện thử và mức độ kiểm chứng. Với mẫu chữ nhật, b = 6 cm, L = 18 cm và lớp giấy dày 0,1 mm, bốn cấu hình 8, 12, 16 và 20 lớp được thử ở 68 kPa; cấu hình 20 lớp được thử thêm ở 24 và 48 kPa, mỗi điều kiện lặp ba lần [10]. Phép uốn ba điểm ghi lực–độ võng và năng lượng tiêu tán; mô hình giải tích, phần tử hữu hạn và thí nghiệm được so sánh trong cùng miền hình học. Mô hình mô tả được sự lan truyền trượt và xu hướng thay đổi độ cứng, nhưng sai lệch tăng ở độ võng lớn do mô hình giải tích bỏ qua áp suất và ứng suất tiếp xúc phát sinh tại gối đỡ. Vì vậy, kết quả này xác lập một miền kiểm chứng cụ thể, không phải luật phổ quát theo số lớp.

- **Locator PDF trong trace:** Fig.4–5;Conclusion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không chứng minh luật số lớp phổ quát hoặc chuyển sang bó dây.

**CH2-S5-R0024-A01 — mục §2.5.2.** Caruso và cộng sự mở rộng mô tả cho bốn lớp trong uốn ba điểm. Với hình chữ nhật gồm bốn lớp, giao diện trung tâm đạt giới hạn ma sát trước, sau đó các giao diện ngoài lần lượt trượt. Các phương trình ngưỡng và mô men quán tính trong nguồn gắn với chiều dày lớp, áp suất chân không, hệ số ma sát, nhịp và điều kiện gối; thí nghiệm và phần tử hữu hạn kiểm tra đường lực–độ võng trong cấu hình đó. Trật tự trung tâm–ra ngoài vì thế là thông tin về một topology lớp cụ thể, không phải điều kiện tổng quát cho packing dây TiNi [10].

- **Locator PDF trong trace:** Figs.1–2; Sec.2.1 Eqs.(1–15). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Trật tự trung tâm–ngoài không phổ quát cho packing dây.

## Nhận xét audit [6]–[10]

- **[6] Russo et al.** Trace định vị hai ý ở §3.1.3: biểu diễn Cosserat và giả thiết tiết diện/biến dạng cắt. Đây là tổng quan/mô tả mô hình; không cung cấp thông số hoặc xác nhận trực tiếp cho MP1. Locator hiện thiếu số trang vật lý.
- **[7] Jeon et al.** Nguồn được dùng rộng ở §2.4.3 và đối chiếu §2.6: cấu trúc robot, biến đổi lực ma sát bởi SMA, phép kéo dây riêng và phép thử uốn. Đây là cơ cấu khác với bó dây TiNi MP1; cần giữ rõ khác biệt giữa lực kéo giao diện, độ dốc lực–độ võng và EI suy ra. Một số locator trong trace có số trang/figure/table, một số chỉ có mã “M31”.
- **[8] Zhang et al.** Hỗ trợ mô hình dầm cáp dây song song có trượt giao diện; tham số `k` là độ cứng trượt hiệu dụng được hiệu chuẩn theo nguồn, không đồng nhất với hệ số ma sát hoặc áp suất pháp. Các locator ghi mục/phương trình và một phần số PDF, chưa chuẩn hóa physical page cho từng claim.
- **[9] Narang et al.** Cung cấp tiền lệ laminar jamming, miền pre-slip/transition/full-slip và mô hình/đối chiếu thực nghiệm cho chồng lớp. Không chuyển ngưỡng hoặc tham số sang bó dây. Một số dòng có physical page (ví dụ p.3–4); các dòng khác chỉ ghi section/figure.
- **[10] Caruso et al.** Hỗ trợ mô hình và thực nghiệm layer-jamming trong topology lớp cụ thể; không biến thứ tự trượt của bốn lớp thành luật tổng quát. Trace có 5 claim narrative sau khi bỏ dòng `NOT_APPLICABLE`; một số locator chỉ ghi section/figure và chưa nêu physical page.
- Dù các PDF [6]–[10] có trong thư mục đóng gói, vòng này vẫn dựa trên traceability có sẵn để nối ý và locator; chưa trích xuất/đối chiếu trực tiếp mọi câu từ PDF. Chưa gắn nhãn `VERIFIED FULL TEXT` mới.


---

