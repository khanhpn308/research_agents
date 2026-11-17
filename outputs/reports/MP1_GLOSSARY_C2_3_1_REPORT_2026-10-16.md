# Báo cáo glossary đề xuất cho §2.3.1

Phạm vi bằng chứng: M05, M06, M09, M10 trong Writing Evidence Pack; không bổ sung nguồn ngoài bốn PDF này và Writing Evidence Pack. Các evidence record đều ghi `VERIFIED_FULL_TEXT`; diễn giải khái quát được đánh dấu `INFERENCE/TERMINOLOGY`.

| English | Tiếng Việt | Định nghĩa cơ học | Ngữ cảnh | Trạng thái | Ghi chú dịch |
|---|---|---|---|---|---|
| variable stiffness | độ cứng biến thiên | Khả năng thay đổi đáp ứng lực–biến dạng hoặc mô men–góc khi đổi trạng thái/cơ chế. | M05-E01; M09-E02; M10-E01/E02 | VERIFIED_FULL_TEXT | Dùng “độ cứng biến thiên”; “điều biến độ cứng” khi nhấn mạnh điều khiển. |
| stiffness | độ cứng | Đại lượng phụ thuộc observable và điều kiện biên; không đồng nhất E, K và EI. | M09-E02; M10-E02; pack M04-E02/E03 | VERIFIED_FULL_TEXT trong pack | Phân biệt độ cứng hệ với mô đun E. |
| rigidity / bending rigidity | độ cứng vững / độ cứng uốn (EI) | Khả năng chống uốn; EI khác K và E. | pack M04-E02; đối chiếu M05/M06 | VERIFIED_FULL_TEXT cho EI trong pack | Chỉ dùng nếu §2.3.1 có EI. |
| compliance | tính mềm dẻo (compliance) | Khả năng dễ biến dạng; nghịch đảo của stiffness chỉ trong cùng observable và điều kiện biên. | M05-E01; pack M04 | INFERENCE/TERMINOLOGY | Không dịch chính là “tuân thủ”. |
| jamming | cơ chế kẹt/khóa | Chuyển sang trạng thái cản trượt/tăng ma sát do nén hoặc tăng lực tiếp xúc. | M05-E02; M06-E01/E02; M09-E01/E03; M10-E01 | VERIFIED_FULL_TEXT | “Kẹt” cho cơ chế, “khóa” cho trạng thái. |
| frictional locking | khóa bằng ma sát | Ma sát tại interface hạn chế trượt tương đối, tăng sức kháng uốn/tải. | M06-E02/E04; M09-E03 | VERIFIED_FULL_TEXT | Có thể rút gọn thành “khóa ma sát”. |
| fibre/filament jamming | kẹt sợi/filament | Sợi/bó sợi song song bị ép trong màng kín khí, tăng ma sát tiếp xúc. | M05-E02, p.10 | VERIFIED_FULL_TEXT | Không gộp với wire jamming. |
| wire/rope jamming | kẹt dây/thừng | Dây/thừng trong envelope bị nén; tiếp xúc dây–dây và dây–vỏ phụ thuộc layout/đường kính. | M09-E01, p.4 | VERIFIED_FULL_TEXT | Giữ “wire” riêng với “fibre”. |
| laminar/layer jamming | kẹt lớp/laminar | Chồng tấm mỏng; locked cho phép uốn cùng nhau, unlocked cho phép trượt/uốn tương đối. | M05-E03; M06-E01 | VERIFIED_FULL_TEXT | “Kẹt lớp” là tên chính. |
| granular jamming | kẹt hạt | Hạt trong bladder–sleeve bị nén/giới hạn, tăng độ cứng hiệu dụng. | M10-E01, p.2 | VERIFIED_FULL_TEXT | Ghi rõ positive-pressure khi có. |
| interfacial slip | trượt liên diện | Trượt tương đối giữa hai môi trường/lớp; tách pre-, transition-, full/post-slip. | M06-E04; M09-E03 | VERIFIED_FULL_TEXT; local slip chưa được đo trực tiếp | “Trượt tại mặt tiếp xúc” dùng khi giải thích. |
| contact mechanics | cơ học tiếp xúc | Quan hệ hình học–lực pháp tuyến–ma sát–trượt tại interface. | M05-E03; M06-E02; M09-E01 | VERIFIED_FULL_TEXT về phạm vi/giới hạn; định nghĩa rộng là INFERENCE | Không tuyên bố constitutive law chung. |

## Kiểm tra citation/reference

- Mỗi dòng phải có paper ID, evidence ID và PDF page/section.
- Đối chiếu metadata: M05 DOI `10.1016/j.rcim.2024.102811`; M06 `10.3390/act13020064`; M09 `10.3390/app12073582`; M10 `10.1109/LRA.2021.3097255`.
- Giữ nhãn `VERIFIED_FULL_TEXT`; mọi định nghĩa compliance/contact mechanics khái quát hoặc EI lấy từ pack phải ghi `INFERENCE/TERMINOLOGY` nếu không có locator trực tiếp trong bốn PDF.
- Không gộp topology/pressure: fibre ≠ wire/rope ≠ layer ≠ granular; positive-pressure M10 ≠ vacuum M06.
- Claims về slip chỉ theo trạng thái nguồn nêu; không nâng thành đo local slip hoặc định luật vật liệu phổ quát.

## Cấu trúc bảng Word

`English term | Tiếng Việt chuẩn | Định nghĩa cơ học ngắn | Ngữ cảnh/ranh giới áp dụng | Trạng thái xác minh | Nguồn (paper_id–evidence_id, locator)`.

Dùng bảng ngang A4, 9–10 pt, lặp hàng tiêu đề; chú thích dưới bảng định nghĩa `VERIFIED_FULL_TEXT` và `INFERENCE/TERMINOLOGY`. Thêm cảnh báo: không đồng nhất E, K, EI và không chuyển pressure path giữa các topology.
