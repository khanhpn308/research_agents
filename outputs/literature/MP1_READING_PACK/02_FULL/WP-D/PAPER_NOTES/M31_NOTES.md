# M31 — Paper Note

## A. Bibliographic information
Jeon et al. (2022), *Towards a Snake-Like Flexible Robot With Variable Stiffness Using an SMA Spring-Based Friction Change Mechanism*. DOI: 10.1109/LRA.2022.3174363. Canonical PDF: `data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf`.

## B. Research problem
Thiết kế robot phẫu thuật nhiều backbone có thể đổi stiffness bằng lực siết của SMA spring. [M31-E01]

## C. Physical mechanism and system
Robot gồm backbone trung tâm, tám super-elastic wires, đĩa acrylic, ống TPU/rubber và SMA spring quấn ngoài. Nung SMA làm giảm đường kính ghi nhớ và tăng lực kẹp lên rubber tube, từ đó tăng wire–tube friction. [M31-E01, M31-E02]

## D. Mechanical models and assumptions
Mô hình work–energy của cantilever tách elastic energy và friction work; sliding length được tính từ hình học cung tròn tám wire. Các phương trình chính là (1)–(10), với `s` và `δ` từ Eqs. (3)–(6), và `EI` từ Eqs. (9)–(10). [M31-E03–E05, M31-E07]

## E. Experimental methods
Đo friction trên một wire ở ba đường kính backbone và hai trạng thái SMA; đo force–displacement của robot bằng force sensor với end-disk displacement 5 mm, mỗi case 10 lần. Nhiệt được theo dõi bằng infrared camera. [M31-E06–E08]

## F. Important equations and figures
Fig. 3; Eqs. (1)–(10); Fig. 4/Table I cho friction; Fig. 5/Table II–III cho stiffness và validation; Fig. 6 cho thermal behavior. Xem `EQUATION_REGISTRY.md` và `FIGURE_TABLE_REGISTRY.md`.

## G. Quantitative findings and validation
Stiffness austenite/martensite lần lượt là 0.31/0.21, 0.34/0.22 và 0.41/0.29 N/mm; ratios 1.45, 1.50, 1.41. Sai số modeled–experimental EI là 3.5%, 3.1%, 5.4%. [M31-E07]

## H. Limitations and counterevidence
Cooling ambient khoảng 60 s; không có temperature control thời gian thực; stiffness ratio còn nhỏ; circular-arc/sliding assumptions có thể sai hơn khi uốn lớn; friction được dùng ở dạng mean state value. [M31-E08]

## I. Relevance to Chapter 1–2 and RQs
Nguồn này hỗ trợ C2.4.3 về SMA điều biến friction và C2.5 về work–energy/observable stiffness. Không được chuyển wire–rubber-tube interface thành wire–wire hoặc layer-jamming interface của MP1.

## J. Reading route
Đọc Fig. 1–3 → Eqs. (1)–(10) → Fig. 4/Table I → Fig. 5/Table II–III → Fig. 6 → limitations.

## K. Evidence index and suggested reading route
Evidence: M31-E01–M31-E08. Primary: E01–E07; counterevidence: E08.
