# W04: Tái Kiểm chứng T1 và Sửa đổi Sai sót Thực tế về Carboni (T1 Re-Audit & Carboni PDF Factual Correction)

**Worker ID:** W04  
**Mục tiêu:** Tái kiểm chứng toàn diện mối đe dọa T1 (tiếp xúc và ma sát trượt nội tại giữa các dây NiTi), đồng thời đính chính triệt để sai sót dữ liệu thực tế tại packet W08 liên quan đến cấu hình S2a trong bài báo của Carboni et al. (2014/2015) theo phê bình G05 của Astra.  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Đính chính Sai sót Thực tế Cấu hình Carboni (G05 Remediation)

### 1.1. Bản chất Sai sót trong Packet Cũ (W08-E01)
Trong packet W08 ở giai đoạn trước, tác giả packet đã trích dẫn bài báo của Carboni et al. (2014/2015, DOI: 10.1061/(ASCE)EM.1943-7889.0000852) và khẳng định rằng: *"Cấu hình S2a trong nghiên cứu của Carboni đã chứng minh chuyển pha siêu đàn hồi của dây NiTi dưới điều kiện uốn thuần túy (pure bending)"*.

Astra đã phát hiện ra lỗ hổng này (G05) và cảnh báo: Việc gán chuyển pha siêu đàn hồi của NiTi cho cấu hình S2a là một sai sót sự thật nghiêm trọng, làm sai lệch bằng chứng cơ học.

### 1.2. Xác minh Trực tiếp từ Toàn văn PDF (A1-2015 / `d9966f2f5e`)
Đối soát trực tiếp tệp PDF `data/papers/verification/MP1-V002/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf` tại Trang 9–10 và Bảng 4 (**Table 4**):

```text
Table 4. List of Considered Device Configurations with the Rope Types, Rope Number, Rope Length, and Displacement Amplitudes in the Cyclic Tests
---------------------------------------------------------------------------------------------------------
Configuration    PSG Type    L (mm)    n    SSG Type    L (mm)    n    Displacement Amplitudes (mm)
---------------------------------------------------------------------------------------------------------
S1a              NiTi7        56       8      ---        ---     ---   ±10, ±12.5, ±15, ±17.5, ±20
S2a              ST49        100       8      ---        ---     ---   ±5, ±10, ±15, ±20
S3a              NiTi19       80       8     NiTi1       103      4    ±10, ±15, ±20, ±25
S3b              ST49        100       8     NiTi7        63      2    ±5, ±10, ±15, ±20
S3c              ST49        100       8     NiTi1        63      2    ±5, ±10, ±15, ±20
---------------------------------------------------------------------------------------------------------
```

Trích dẫn toàn văn từ văn bản của tác giả (Trang 9, cột 2):
1. **Về cấu hình S2a:**
   > *"a steel wire rope formed by 1 + 6 strands, each made of 1 + 6 wires for a total number of 49 wires and a diameter equal to 6.0 mm (ST49)... The restoring force assumed for the identification of Assembly S2a is obtained using Eq. (15), with r = 1, in which the hysteretic force z is governed by the evolution law of the BW model given by Eq. (1)."*
   -> **Sự thật khoa học:** Cấu hình **S2a hoàn toàn là cáp thép (ST49)**, không hề chứa dây NiTi! Lực phục hồi của S2a được mô hình hóa bằng mô hình Bouc-Wen (BW) cổ điển đại diện cho hiện tượng trượt ma sát khô thuần túy, không có bất kỳ hiện tượng chuyển pha Martensite nào!
2. **Về cấu hình S1a:**
   > *"In Fig. 13, the hysteretic cycles for Configuration S1a and the associated identifications are shown... The constitutive behavior is characterized by a strong hardening and a distinct pinching at the origin. The first is caused by the geometric stretching effect that originates in the strand from having locked the horizontal displacement of b2 (Fig. 7)... The Nitinol strands are subjected to a tension-bending state of stress. This stress state determines the phase transitions in the individual Nitinol wires... The pinching is caused by the return to the austenitic phase toward the end of the unloading branches."*
   -> **Sự thật khoa học:** Cấu hình chứa tao cáp NiTi 7 sợi là **S1a**, nhưng S1a chịu trạng thái ứng suất **kéo - uốn kết hợp (tension-bending state of stress)** do cơ cấu ngàm khóa dịch chuyển ngang của các thanh $b_2$, sinh ra hiệu ứng kéo căng hình học (geometric stretching). Chuyển pha xảy ra do trạng thái kéo - uốn này, KHÔNG PHẢI uốn thuần túy (pure bending)!

### 1.3. Hành động Khắc phục (Action Taken)
- Loại bỏ hoàn toàn khẳng định sai lệch về S2a khỏi chuỗi bằng chứng.
- Đính chính rõ ràng: Trong Carboni 2015, hiện tượng trễ thắt (pinched hysteresis) kết hợp giữa chuyển pha siêu đàn hồi và ma sát trượt chỉ được xác nhận trên cấu hình **S1a** (và dòng S3 kết hợp) dưới trạng thái tải kéo - uốn kết hợp có kéo căng hình học lớn, chứ không phải dưới uốn thuần túy.

---

## 2. Tái Kiểm chứng Mối đe dọa T1 (T1 Re-Audit)

### 2.1. Tuyên bố và Phạm vi Đe dọa của T1
- **Mục tiêu đe dọa:** Khẳng định cho rằng "chưa có nghiên cứu nào xem xét dây NiTi như một tập hợp các sợi có tiếp xúc cơ học, lực ma sát và chuyển động trượt tương đối nội tại".
- **Phán quyết kiểm chứng:** `CLOSED` / `PREEMPTED`. Khẳng định tính mới này đã bị tiền nhiệm đóng hoàn toàn.

### 2.2. Bằng chứng Toàn văn Xác lập (Strongest Evidence)
Tập tài liệu kiểm chứng tại HEAD cung cấp bằng chứng áp đảo rằng tiếp xúc và ma sát giữa các dây NiTi đã được nghiên cứu sâu sắc:

1. **Vahidi et al. (2022, `53200aa0c6`):**
   - Thiết lập mô hình phần tử hữu hạn 3D chi tiết cho cáp NiTi xoắn đơn (1x27) và xoắn kép (7x7) có kích thước lên đến 185.300 phần tử.
   - Sử dụng mô hình cấu thành Auricchio-Petrini cho vật liệu siêu đàn hồi tích hợp qua chương trình con Abaqus UMAT.
   - Thiết lập thuật toán tiếp xúc bề mặt - bề mặt thực (true surface-to-surface contact) với định luật ma sát trượt Coulomb giữa các dây NiTi với hệ số ma sát $\mu = 0.115$.
   - Chứng minh ma sát giữa các dây gây ra sự phân bố lại ứng suất và tiêu tán năng lượng trượt đáng kể.

2. **Kang et al. (2020, `56793dea9b`):**
   - Xây dựng mô hình phần tử hữu hạn tăng lượng cho cáp siêu đàn hồi NiTi, giải quyết tương tác tiếp xúc phi tuyến kép: phi tuyến vật liệu chuyển pha (thay đổi mô-đun đàn hồi giữa Austenite $E_A$ và Martensite $E_M$) và phi tuyến tiếp xúc ma sát giữa các dây khi chịu tải kéo uốn.

3. **Reedlunn et al. (2013 Part II, `fac21c950e`):**
   - Đo đạc thực nghiệm các cấu phần cáp 1x7, 1x19, 7x7 và 1x27 NiTi.
   - Sử dụng ảnh kính hiển vi điện tử quét (SEM) tại Hình 8 để phát hiện các vết lõm tiếp xúc cơ học (contact indentations) giữa các lớp dây do áp lực tạo hình khi bện cáp, chứng minh sự tập trung ứng suất tiếp xúc kích hoạt các mầm chuyển pha Martensite cục bộ.

4. **Silva et al. (2022, `6dd1ca94d1`):**
   - Nghiên cứu vi cáp NiTi chịu tải động lực học chu kỳ, chứng minh ma sát trượt nội tại giữa các vi sợi tạo ra sự gia nhiệt ma sát (frictional self-heating), làm dịch chuyển mức ứng suất kích hoạt chuyển pha thông qua quan hệ Clausius-Clapeyron.

5. **Falcetelli et al. (2024, `1c81b2d35c`):**
   - Thử nghiệm trực tiếp so sánh cáp thép và cáp NiTi cùng bước xoắn, phân tích sự tương tác giữa trượt ma sát giữa các sợi và cơ chế tiêu tán trễ của vật liệu.

### 2.3. Giới hạn Hiệu lực Còn lại của T1 (Residual Caveat)
Việc T1 đóng khẳng định tính mới ở cấp độ nguyên lý tồn tại không đồng nghĩa với việc:
- Mọi giao diện tiếp xúc trong một bó dây NiTi tùy ý đều đã được đo đạc trường trượt cục bộ bằng thực nghiệm (hầu hết các nghiên cứu chỉ đo lực - biến dạng vĩ mô hoặc dùng mô hình số).
- Mọi mô hình tiếp xúc đều dự đoán hoàn hảo biến dạng trượt khi có sự can thiệp của áp suất giam giữ chủ động bên ngoài.

Tuy nhiên, đối với câu hỏi khoa học nền tảng: *"Sự tồn tại của tiếp xúc và ma sát trượt giữa các dây NiTi có phải là một khám phá mới của đề tài không?"* -> Câu trả lời dứt khoát là **KHÔNG**.

---

## 3. Kết luận của Worker W04

1. Đã đính chính triệt để sai sót về cấu hình Carboni: S2a là cáp thép thuần ma sát; S1a mới là cáp NiTi chịu kéo - uốn kết hợp.
2. T1 được xác nhận đóng vững chắc (`CLOSED`): Hiện tượng tiếp xúc, áp lực pháp tuyến và ma sát trượt giữa các dây hợp kim nhớ hình NiTi đã có tiền nhiệm lý thuyết và thực nghiệm phong phú trong cơ học cáp.
