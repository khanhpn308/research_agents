# Framework Guide — Đọc và sử dụng Evidence JSON

Ngày: 26-09-2026. Phạm vi: cấu trúc evidence đang có trong 27 nguồn MP1 đã kiểm tra, không phải đề xuất thay đổi schema.

## 1. Mục đích

Evidence JSON giúp trả lời bốn câu hỏi: **bằng chứng lấy từ đâu, được trích xuất bằng gì, bài nghiên cứu làm gì, và bằng chứng hỗ trợ đến mức nào**.

Đây là bản trích xuất có cấu trúc để tìm và đối chiếu thông tin, không thay thế PDF gốc. File evidence không phải final novelty verdict.

## 2. Cấu trúc tổng thể

```text
evidence.json
├── source    Thông tin PDF nguồn và provenance
├── model     Model AI thực hiện trích xuất
├── usage     Thống kê token của lần trích xuất
└── paper     Nội dung khoa học được trích xuất
```

Trong 27 evidence MP1 đã kiểm tra, cả bốn trường cấp cao này đều tồn tại. Bên trong `paper` có 23 trường được giải thích dưới đây. Đây là mô tả dữ liệu quan sát được, không khẳng định mọi phiên bản pipeline tương lai phải giống hệt.

## 3. Thông tin nguồn — `source`

| Trường | Ý nghĩa |
|---|---|
| `paper_id` | Mã định danh bài trong repository, nối PDF, evidence và các lần kiểm chứng |
| `filename` | Tên file PDF nguồn |
| `sha256` | Dấu vân tay của PDF, dùng kiểm tra đúng bản file đã được xử lý |
| `page_count` | Số trang của PDF |
| `char_count` | Số ký tự văn bản được ghi nhận trong quá trình xử lý PDF |
| `source_type` | Loại nguồn trong pipeline, chẳng hạn `seed` hoặc `verification` |
| `verification_id` | Vòng kiểm chứng gắn với nguồn, ví dụ `MP1-V001`; không có nghĩa bài chỉ được dùng ở vòng đó |

Khi copy PDF/evidence sang `data/final/MP1/`, không đổi `verification_id` chỉ vì bản sao nằm ở một bước sử dụng khác. SHA256 khớp xác nhận cùng nội dung file, **không xác nhận diễn giải khoa học trong evidence là đúng**.

## 4. Thông tin trích xuất — `model` và `usage`

| Trường | Ý nghĩa |
|---|---|
| `model` | Model AI được ghi nhận đã thực hiện trích xuất |
| `usage.prompt_tokens` | Số token đầu vào được báo cáo |
| `usage.completion_tokens` | Số token đầu ra được provider báo cáo |
| `usage.total_tokens` | Tổng token được báo cáo |
| `usage.thinking_tokens` | Token reasoning nếu provider có cung cấp |
| `usage.cache_read_tokens` | Token đầu vào được đọc từ cache |

Đây là thông tin vận hành, không phải bằng chứng bài đúng hoặc đề tài mới. Các bộ đếm có thể phụ thuộc provider; không tự cộng lại các trường như thể tất cả đều là các phần độc lập.

## 5. Thông tin thư mục trong `paper`

| Trường | Ý nghĩa | Kiểu dữ liệu quan sát được |
|---|---|---|
| `title` | Tên bài | Chuỗi |
| `authors` | Danh sách tác giả | Danh sách chuỗi |
| `year` | Năm công bố được trích xuất | Chuỗi, ví dụ `"2026"` |
| `doi` | Định danh DOI | Chuỗi |

Cần phân biệt online-first và năm issue nếu khác nhau. DOI để trống không đồng nghĩa chắc chắn bài không có DOI. Không dùng năm trong filename thay metadata đã xác minh.

## 6. Bài nghiên cứu vấn đề gì?

| Trường | Ý nghĩa | Câu hỏi giúp trả lời |
|---|---|---|
| `research_problem` | Vấn đề hoặc hạn chế bài muốn xử lý | Vì sao cần nghiên cứu? |
| `research_objective` | Mục tiêu cụ thể của bài | Tác giả định làm gì? |
| `robot_type` | Loại robot hoặc cấu trúc ứng dụng | Hệ được nghiên cứu hoặc ứng dụng vào đâu? |
| `stiffness_mechanism` | Cơ chế tạo hoặc thay đổi độ cứng | Vì sao độ cứng thay đổi? |
| `actuation` | Cách tác động/điều khiển hệ | Hệ được kích hoạt bằng gì? |

Ba trường đầu là chuỗi; `stiffness_mechanism` và `actuation` là danh sách trong dữ liệu đã kiểm tra.

**Cơ chế độ cứng khác cơ cấu tác động.** Ví dụ minh họa: khí nén có thể là cách tác động, còn contact–friction là cơ chế khiến độ cứng thay đổi. Không coi hai trường này là từ đồng nghĩa.

## 7. Mô hình và giả thiết

| Trường | Ý nghĩa |
|---|---|
| `modeling_methods` | Danh sách phương pháp mô hình hóa: analytical beam model, FEM, mô hình hiện tượng học… |
| `constitutive_assumptions` | Danh sách giả thiết về ứng xử vật liệu/cơ học được ghi nhận: đàn hồi tuyến tính, luật NiTi, Coulomb friction… |

Dữ liệu hiện có đôi khi đưa cả giả thiết hình học hoặc beam theory vào `constitutive_assumptions`. Tên trường không bảo đảm mọi mục đều là giả thiết cấu thành vật liệu theo nghĩa hẹp. Khi phân tích chuyên sâu, phải tách material law, kinematics, contact law và boundary conditions theo nội dung nguồn thực tế.

## 8. Ba nhóm biến cần phân biệt

| Trường | Ý nghĩa | Ví dụ minh họa cho phép thử bó dây |
|---|---|---|
| `independent_variables` | Các biến chủ động thay đổi | Áp suất, mức uốn |
| `dependent_variables` | Các đại lượng đáp ứng được đo/tính | Lực, độ cứng, trượt tương đối |
| `control_variables` | Các yếu tố giữ cố định hoặc kiểm soát để so sánh công bằng | Vật liệu dây, chiều dài mẫu, nhiệt độ, tốc độ tải |

Cả ba trường là danh sách. Ví dụ trên chỉ minh họa phân loại, không phải protocol đã được thực hiện. Cùng một đại lượng có thể là independent variable trong nghiên cứu này nhưng là control variable trong nghiên cứu khác.

## 9. Thí nghiệm và kết quả

| Trường | Ý nghĩa |
|---|---|
| `experimental_setup` | Mẫu, apparatus, cảm biến, cách gá và cách tạo tải |
| `performance_metrics` | Tiêu chí dùng đánh giá: độ cứng, sai số dự đoán, năng lượng tiêu tán… |
| `main_results` | Những kết quả chính được trích xuất từ bài |

Cả ba trường là danh sách. Phân biệt **đo đại lượng gì** (`dependent_variables`) với **dùng đại lượng nào để đánh giá** (`performance_metrics`).

Không suy từ một kết quả nằm trong `main_results` rằng nó đã được independent experimental validation: cần kiểm tra kết quả là analytical, numerical, fitted hay measured, và dữ liệu nào đã được dùng để calibration.

## 10. Bằng chứng liên quan — `evidence_relevant_to_topic`

Đây là danh sách các phát biểu được chọn vì liên quan đến câu hỏi nghiên cứu của dự án. Mỗi mục có ba trường:

| Trường con | Ý nghĩa |
|---|---|
| `claim` | Phát biểu cụ thể được rút từ nguồn |
| `evidence_type` | Loại hỗ trợ cho phát biểu: analytical, numerical, experimental, background hoặc mô tả kết hợp |
| `page_numbers` | Danh sách trang được ghi để truy ngược PDF |

Ví dụ cấu trúc minh họa, **không phải một claim hoặc page locator thực tế**:

```json
{
  "claim": "Nội dung phát biểu được trích xuất",
  "evidence_type": "experimental",
  "page_numbers": []
}
```

Một mục nằm trong trường này chưa chắc là kết quả thực nghiệm trực tiếp. Nó có thể là background mà bài đang dẫn từ nguồn khác. Cần kiểm tra loại bằng chứng và trang nguồn trước khi coi đó là primary evidence.

`page_numbers` không mặc nhiên phân biệt printed page và số trang PDF. Nếu chuẩn bị citation chính thức, phải đối chiếu hệ đánh số. Không tự tạo equation/figure/section number khi JSON không lưu.

## 11. Giới hạn, suy luận và hướng tiếp theo

| Trường | Ý nghĩa | Cảnh báo |
|---|---|---|
| `limitations_stated_by_authors` | Giới hạn được ghi là do tác giả trực tiếp nêu | Cần kiểm tra đúng wording và scope trong bài |
| `limitations_inferred` | Giới hạn do người/model phân tích suy ra | Không gán thành kết luận của tác giả |
| `future_work` | Hướng nghiên cứu tiếp theo được trích xuất | Future work năm trước không chứng minh vấn đề vẫn mở hiện nay |
| `possible_gap_implications` | Suy luận về ảnh hưởng của bài đối với gap dự án | Không phải bằng chứng xác nhận novelty |
| `confidence` | Mức tự đánh giá độ tin cậy của bản trích xuất | Không phải confidence đề tài mới; không bảo đảm trích xuất không sai |

Bốn trường đầu là danh sách, `confidence` là chuỗi trong dữ liệu đã kiểm tra. Không phải mọi mục trong chúng đều có page locator riêng.

## 12. Quy trình đọc một evidence JSON

1. Kiểm tra `source`: đúng paper_id, đúng PDF và đúng bản nguồn hay chưa?
2. Đọc `research_problem` và `research_objective`: phân biệt vấn đề tác giả nêu với điều tác giả thực sự thực hiện.
3. Đọc `modeling_methods`, `constitutive_assumptions` và các nhóm biến để xác định scope.
4. Đọc setup, metrics và results; tách calibration, numerical verification và experimental validation.
5. Với claim quan trọng, dùng `evidence_relevant_to_topic.page_numbers` để mở PDF và kiểm tra.
6. Giữ riêng giới hạn tác giả nêu, suy luận của extractor và giả thuyết gap của dự án.
7. Nếu successor audit đã phát hiện lỗi trích xuất, đọc correction và PDF; không dùng confidence cao hoặc JSON parse thành công để bỏ qua lỗi đó.

Trong kết quả phân tích, phân biệt `VERIFIED FULL TEXT`, `METADATA ONLY` và `INFERENCE`. Schema hiện tại không tự cung cấp một nhãn chuẩn hóa như vậy cho mọi câu; người phân tích vẫn phải xác định mức bằng chứng.

## 13. Framework này không bảo đảm điều gì?

File đúng schema hoặc validate thành công không bảo đảm mọi claim đúng nội dung. Có đủ `page_numbers` cũng chưa chứng minh page đó hỗ trợ cách diễn giải đang dùng. Đặc biệt, cấu trúc hiện tại chưa phải kho trích dẫn nguyên văn, phương trình hoặc causal evidence đầy đủ cho từng claim.

Đối với MP1, không biến `limitations_inferred` hoặc `possible_gap_implications` thành “khoảng trống đã được chứng minh”. Evidence phải đi qua đối chiếu nguồn và adversarial reasoning trước khi hỗ trợ một quyết định novelty.

## 14. Nguồn minh họa và phạm vi kiểm tra

- [Evidence Zhang & Yao 2026 — paper_id 3aa8790db0](<../../data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json>): ví dụ cấu trúc thực tế.
- [Manifest 27 nguồn MP1 và các bản sao](../../data/final/MP1/manifest.json): cung cấp đường dẫn evidence/PDF đã đối chiếu.
- [Hướng dẫn kho MP1](../../data/final/MP1/README.md): phân biệt bản sao theo bước với corpus và verdict.

Tài liệu này giải thích framework và cách đọc, không sửa schema, không chạy extraction, không thay đổi registry hoặc scientific state.
