# Trạng thái MP1 và bước xác minh tiếp theo

> Cập nhật theo các artifact MP1-V002/W02, WR1, WR1-S01 và WR1-S02 hiện có trong repository (26/09/2026). Đây là note giải thích trạng thái; không thay thế registry hay các verification round lịch sử.

## Kết luận hiện tại

MP1 **chưa được chốt chính thức** thành tên đề tài luận văn hoặc hướng luận văn cuối cùng.

MP1 hiện là **conditional candidate / viable alternative**. Hướng này đã được thu hẹp thành một bài toán phân biệt mô hình, nhưng scientific gate vẫn `BLOCKED`:

- `H0a`: mô hình đàn hồi thay thế với mô đun hằng — `REFUTED_IN_TRANSFORMATION_REGIME`.
- `H0b`: mô hình NiTi có xét chuyển pha + tiếp xúc/ma sát Coulomb — `NOT_FALSIFIED / LIVE COMPETITOR`.
- `H1`: cần một định luật ghép cặp cấu thành–tiếp xúc mới — `INSUFFICIENT_EVIDENCE`.

Quyết định cấp dự án vẫn là D1/M1 `LOCK_WITH_FEASIBILITY_GATE` ở mức lịch sử; MP1 chưa thay thế D1/M1. So sánh D1–MP1 cuối cùng cũng chưa được thực hiện.

## Tên và câu hỏi đang có

Tên tiếng Anh trong hồ sơ cũ là:

> *Modeling and Experimental Characterization of Pressure-Controlled Bending Mechanics in Superelastic NiTi Wire Bundles*

Bản tiếng Việt:

> *Mô hình hóa và đặc trưng thực nghiệm cơ học uốn của bó dây NiTi siêu đàn hồi dưới áp suất giam giữ điều khiển.*

Đây chỉ là **title draft lịch sử**, chưa phải tên được phê duyệt. Phần đã tương đối ổn định là hướng câu hỏi:

> Trong miền áp suất, độ cong và nhiệt độ có thể thực hiện, nơi trượt giữa các dây và chuyển pha NiTi cùng tồn tại, mô hình NiTi có xét chuyển pha kết hợp tiếp xúc Coulomb (`H0b`), được hiệu chuẩn độc lập và khóa tham số, có dự đoán đúng đáp ứng mô men–độ cong, độ cứng uốn tiếp tuyến, vòng trễ và các quan sát cục bộ trên dữ liệu held-out hay không? Nếu thất bại có hệ thống và sai số gắn với các cơ chế cục bộ đã đo độc lập, khi đó mới mở bài toán kiểm tra một luật ghép cặp mới (`H1`).

Đây là **câu hỏi làm việc có thể bác bỏ**, chưa phải kết luận rằng `H1` là mới hoặc cần thiết.

## Đã xác minh đến đâu

1. Giao thức citation chase MP1-V002 đã đóng `15/15` nhánh (`9/9` backward, `6/6` forward), nhưng đây chỉ là protocol closure, không phải bằng chứng vắng prior art trên toàn thế giới.
2. W02 đã loại bỏ novelty ở cấp độ ghép phần cứng rộng và giữ lại mechanics/model-discrimination core.
3. WR1 đã hoàn tất routing. Tám gap khoa học vẫn mở.
4. WR1-S01 đã hoàn thành phân tích công thức, đang chờ human review. Kết quả là `EXISTING_FORMULATION_SUFFICIENT_IN_PRINCIPLE`; điều này chưa chứng minh mô hình đủ chính xác cho specimen MP1.
5. WR1-S02 mới hoàn thành chuẩn bị pilot. Chưa có thí nghiệm áp suất, chưa chứng minh đồng thời slip–transformation, chưa kiểm tra được sensing kín, nhiệt độ/rate/history hoặc tính toàn vẹn mẫu.

## Việc cần làm tiếp theo để xác minh và thu hẹp

### Bước 1 — ký review S01

Kiểm tra và phê duyệt formulation crosswalk, giả định áp dụng, H0b specification và phân chia calibration/validation. Nếu formulation công bố đã chứa coupling cần viện dẫn, phải rút claim H1; không được dựng luật mới chỉ vì implementation khó.

### Bước 2 — chạy pilot S02 ở quy mô nhỏ

Trước khi nạp áp suất phải chọn đúng lot dây, cuff/membrane, feedthrough và giới hạn an toàn. Pilot phải kiểm tra:

- miền hoạt động an toàn và lặp lại trong (p)–κ–(T);
- kênh đo slip tương đối giữa dây, đã hiệu chỉnh khỏi clamp/membrane/rigid-body motion;
- bằng chứng chuyển pha NiTi được hiệu chuẩn theo cùng lot;
- hai tín hiệu có cùng vùng thời gian/không gian;
- rò khí, nhiễu, biến dạng do sensor/marker, nhiệt độ, tốc độ và lịch sử chu kỳ.

Nếu không có miền đồng tồn tại hoặc không có kênh quan sát phân biệt được cơ chế, phải `STOP` hoặc `NARROW`, không tiếp tục bảo vệ H1.

### Bước 3 — nếu S02 đạt, làm S03–S04

- **S03:** kiểm tra identifiability; xác định slip, transformation, thermal, ovalization, membrane và fixture có thể tách được dưới mức nhiễu thực tế không.
- **S04:** hiệu chuẩn độc lập NiTi, ma sát, membrane, hình học/prestrain, compliance và quan hệ áp suất buồng (p) với lực tiếp xúc nội bộ (f_n). Không được đặt (f_n=pA) nếu chưa có transfer map hoặc bound có uncertainty.

### Bước 4 — khóa H0b trước held-out test

Ở S05 phải khóa version code, parameter file, uncertainty budget, metric và tolerance trước khi thu dữ liệu held-out. Không fit lại tham số trên held-out data.

### Bước 5 — phân loại kết quả S06–S07

- **A:** H0b đạt — dừng claim cần H1 trong miền đó.
- **B:** H0b thất bại có hệ thống, vượt tolerance và khớp các quan sát cục bộ độc lập — chỉ khi đó mới mở formulation/test H1 mới.
- **C:** dữ liệu không nhận dạng được hoặc uncertainty lớn — thu hẹp câu hỏi về predictive validity hoặc thiết kế lại phép đo.

## Quyết định cần tránh

Không gọi MP1 là “đề tài đã chốt”, không gọi `SURVIVES_TARGETED_CITATION_CHASE` là “đã chứng minh novelty”, và không suy ra `H1` đúng chỉ vì `H0a` đã bị bác bỏ.

## Provenance chính

- `outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json`
- `outputs/execution/MP1-V002/W2/MP1_W02_BLOCKING_GAP_REGISTER.json`
- `outputs/execution/MP1-V002/WR1/MP1_WR1_FINAL_STATE.json`
- `outputs/execution/MP1-V002/WR1/S01/MP1_S01_EXECUTION_RECEIPT.json`
- `outputs/execution/MP1-V002/WR1/S02/MP1_S02_PREPARATION_RECEIPT.json`
- `docs/reports/MP1_MENTOR_NARROWING_REPORT_2026-09-26.md`

