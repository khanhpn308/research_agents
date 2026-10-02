# MP1 — PDF theo từng bước suy luận và kiểm chứng

## Mục đích

Tập hợp bản sao PDF đã được sử dụng hoặc viện dẫn trong chuỗi MP1 đến các output WR1/S01/S02 hiện có. Đây là kho đọc, không phải quyết định khoa học mới. `manifest.json` là chỉ mục máy đọc đầy đủ, gồm số lượng, nguồn gốc, SHA256, đường dẫn bản sao và bằng chứng tham chiếu theo từng bước.

## Cấu trúc

Kết quả tập hợp ngày 26-09-2026: **27 PDF nguồn riêng biệt, 456 bản sao trong 25 nhóm bước**, tổng dung lượng PDF 2.679.830.038 bytes (khoảng 2,68 GB). Bộ rà đã kiểm tra nội dung 389 artifacts và đối chiếu 317 PDF trong `data/`. Không thiếu PDF nguồn cho 27 papers được xác định.

| Thư mục | Vai trò |
|---|---|
| `MP1-V001/canonical/` | Corpus và nguồn của architecture audit C1–C8 |
| `MP1-V001/runs/` | Nguồn được đưa vào/viện dẫn trong run có actual model output |
| `MP1-V002/canonical/` | Corpus mechanics và các nguồn baseline được viện dẫn trong outputs V002 |
| `MP1-V002/runs/` | Các run audit có raw output, bao gồm các pha corpus 8/10/13/16 bài và final adjudication; có thể kèm nguồn V001 trong baseline |
| `03_trace_packets/` | Các nguồn gắn với 11 packets chuẩn bị evidence |
| `04_astra_critique/` | Nguồn được critique gọi tên hoặc định danh |
| `05_remediation/` | Các nguồn được dùng/viện dẫn khi sửa logic và evidence |
| `06_W02/W2-01/` … `W2-09/` | Tái dựng, claim/target/hypothesis, paper roles, provenance, K-tests và red-team; có kiểm tra cả output của workers con |
| `06_W02/W2/` | Macro-stage closeout và các nguồn của synthesis |
| `07_WR1/routing/` | Workflow routing; có thể chỉ có README nếu không có paper được định danh trực tiếp |
| `07_WR1/S01/` | Existing-formulation audit và strongest H0b |
| `07_WR1/S02/` | Nguồn trực tiếp của pilot preparation; không phải pilot đã được chạy |
| `08_current_reports/` | Nguồn được viện dẫn trong các báo cáo MP1 phục vụ dựng lại lịch sử/trình bày |

Mỗi bước có `README.md` riêng để mở PDF và tìm artifact nguồn. Cùng một bài có thể xuất hiện ở nhiều bước: đó là bản sao có chủ đích, không phải nhiều paper độc lập. Giữ nguyên tên PDF gốc; năm trong filename có thể khác publication year, nên dùng DOI/paper_id trong manifest để nhận diện.

## Cách xác định nguồn

Không chọn PDF chỉ vì nằm trong `data/papers/verification/MP1-*`. Nội dung artifacts được rà để tìm paper_id, exact title, exact PDF filename hoặc tác giả có thể định danh rõ trong ngữ cảnh MP1. Sau đó resolve PDF theo SHA256 từ evidence trên toàn bộ PDF trong `data/`, không phụ thuộc thư mục tải xuống.

Trong manifest:

- `papers`: paper_id, title, authors, year/DOI như evidence hiện có, đường dẫn gốc và các bản nguồn trùng hash.
- `copies`: từng bước, đường dẫn đích, hash và `usage_evidence`.
- `usage_evidence`: artifact, cách match, role, dòng và excerpt giúp truy nguyên.
- `inspected_artifacts`: danh sách các output/input đã đọc bằng bộ rà và hash tại lúc tạo kho.
- `out_of_scope_references`: các tên nguồn ngoài corpus MP1 xuất hiện trong bảng metadata/citation provenance, được giữ để kiểm tra chứ không tự nâng thành full-text scientific evidence.
- `validation`: kết quả hash bản sao và kiểm tra các file nguồn/registry/evidence/output không đổi.

`supplied_in_saved_prompt` nghĩa là evidence của paper được đưa vào model input; **không chứng minh model mở PDF trực tiếp**. `referenced_in_output` nghĩa là output dùng/nhắc nguồn; cũng không tự chứng minh đã đọc toàn văn ở riêng bước đó. Các bước tái sử dụng upstream analysis có thể không có PDF mới; không tự cộng toàn bộ corpus vào một bước chỉ vì bước đó xảy ra sau.

Số PDF trong một run có thể lớn hơn `paper_count` của round vì prompt chứa cả baseline V001. Số bản sao không phải số nghiên cứu độc lập. Prepared-only run không có actual output không được tạo thư mục run đã hoàn thành.

## Giới hạn khoa học và bảo toàn

Các bản sao giữ nguyên nội dung, kể cả khi một historical summary diễn giải sai paper. Những corrections như Carboni S2a/S1a, Vahidi Souza model, Kang smooth contact và Barsi stiffness bounds vẫn phải đọc trong successor output; không sửa PDF hoặc rewrite historical verdict để làm kho này nhất quán giả tạo.

H0b vẫn chưa được kiểm chứng forward prediction trên hệ MP1; S02 mới preparation. Việc có kho `final` không đóng scientific gate, không xác lập H1 và không phê duyệt đề tài.

Các references mới chỉ được metadata screening, các bibliography citations bên trong một primary paper chưa được dự án sử dụng, và thiết bị/tài liệu dự kiến tìm trong tương lai không tự trở thành PDF đã sử dụng. Không tải tài liệu mới trong tác vụ này.

## Kiểm tra

Mỗi PDF được copy vật lý, không dùng symlink/hardlink; SHA256 bản sao phải bằng SHA256 nguồn đã ghi. Các file nguồn và registry/evidence/outputs không được di chuyển, sửa hoặc register lại. Chưa commit kho này.
