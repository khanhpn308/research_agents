from pathlib import Path
import json, re, zipfile
from docx import Document
from docx.shared import Cm, Pt, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT

ROOT = Path('/home/khanh/projects/mechanical-research-agents')
out_docx = ROOT / 'docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx'
out_docx.parent.mkdir(parents=True, exist_ok=True)

# Source-ID to IEEE reference number: assigned by first appearance in the chapter.
ref_order = {
    'S01': 1, 'S15': 2, 'S02': 3, 'S03': 4, 'S18': 5, 'S04': 6,
    'S22': 7, 'S06': 8, 'V-W02': 9, 'S05a': 10, 'S05b': 11,
    'S07': 12, 'S11': 13, 'S13': 14, 'S12': 15, 'S09': 16,
    'S10': 17, 'S17': 18,
}

# Each entry is (kind, payload). Kinds: h1, h2, h3, p, eq, table, note.
items = []
def H1(t): items.append(('h1', t))
def H2(t): items.append(('h2', t))
def H3(t): items.append(('h3', t))
def P(t, claims=None): items.append(('p', (t, claims or [])))
def EQ(t): items.append(('eq', t))
def NOTE(t): items.append(('note', t))
def TABLE(title, headers, rows, note=None): items.append(('table', (title, headers, rows, note)))

H1('CHƯƠNG 2. TỔNG QUAN NGHIÊN CỨU VÀ CƠ SỞ KHOA HỌC')

H2('2.1. Giới thiệu chương')
P('Chương này xây dựng cơ sở khoa học cho hướng MP1-R: đặc trưng hóa đáp ứng uốn phụ thuộc áp suất của một bó dây TiNi xác định, trong đó nguồn áp suất do lò xo SMA dẫn động chỉ được xem là một thành phần tích hợp tùy chọn. Mục đích của tổng quan không phải là chứng minh một cơ chế mới từ sự kết hợp các linh kiện, mà là xác định những quan hệ cơ học đã được thiết lập, những suy luận chỉ có giá trị trong phạm vi kiến trúc cụ thể, và các quan sát cần thiết để phân biệt vật liệu, tiếp xúc, ma sát và động lực nguồn áp suất.')
P('Mạch lập luận được tổ chức theo năm chủ đề: kiến trúc giam giữ và đường truyền áp suất; cơ học tiếp xúc, ma sát và dính–trượt; nhiệt–cơ TiNi; phân rã nguồn kích thích khỏi đáp ứng kết cấu; và vai trò của mô hình đối chứng. Các nguồn được dùng theo ranh giới bằng chứng của Phase 3–5. Nguồn tương tự chỉ cung cấp cơ sở so sánh cơ học, không được chuyển thành bằng chứng trực tiếp cho bó TiNi của MP1-R. Vì vậy, các từ như “đã thiết lập”, “có cơ sở tham chiếu” và “chưa được xác định” trong chương này biểu thị các mức suy luận khác nhau.')
P('Phần cuối chương tổng hợp chuỗi nhân quả từ áp suất đến đáp ứng uốn, chỉ ra mắt xích yếu nhất là ánh xạ từ phản lực hướng tâm đến lực pháp tuyến cục bộ tại các tiếp diện wire–wire và wire–sleeve. Trên cơ sở đó, chương dẫn đến một câu hỏi nghiên cứu chính và hai câu hỏi phụ, đồng thời giữ nguyên ba trạng thái giả thuyết H0a-R, H0b-R và H1-R mà không chọn trước một kết quả.')

H2('2.2. Cơ chế thay đổi độ cứng dựa trên giam giữ và áp suất')
P('Trong các kết cấu biến đổi độ cứng, “giam giữ” mô tả việc thay đổi khả năng trượt hoặc chuyển vị tương đối giữa nhiều phần tử bằng một tải pháp tuyến, một màng bao, một lớp hạt, hoặc một cơ cấu khóa. Kết quả đo được thường là đáp ứng của toàn bộ cụm, chẳng hạn lực–độ võng hoặc mô men–độ cong. Do đó, sự thay đổi của đáp ứng kết cấu không tự nó xác định lực pháp tuyến cục bộ hay tiếp diện chi phối.')
P('Bai và cộng sự đã khảo sát bộ chấp hành mềm dùng bó dây hoặc sợi không kim loại trong một bao kín, với so sánh trạng thái hút chân không và nhả giam giữ. Công trình này cho thấy ma sát giữa các phần tử có thể làm thay đổi khả năng chịu uốn và xoắn của một kiến trúc wire-jamming [1]. Tuy nhiên, vật liệu, bao bọc và đường tải của nghiên cứu khác với bó dây TiNi chịu áp suất hướng ra ngoài; lực giữa các sợi, lực màng và ảnh hưởng của đóng gói không được tách độc lập. Vì vậy, nguồn này thiết lập khả năng điều chỉnh độ cứng theo kiến trúc, chứ không cung cấp hệ số chuyển áp suất–lực cho MP1-R.')
P('Tổng quan của Caro và Carmichael phân loại các cơ chế khóa của kết cấu laminar-jamming và nhấn mạnh sự khác nhau giữa hút chân không, kẹp khí dương, ma sát và can thiệp hình học [2]. Giá trị của nguồn này là định vị thuật ngữ và chỉ ra rằng cùng một từ “jamming” có thể bao hàm các đường truyền lực khác nhau. Do đây là bài tổng quan, nguồn chỉ được dùng để định hướng phân loại; các kết luận định lượng về ứng suất, độ cứng hoặc hiệu quả thiết bị phải truy về bài nghiên cứu gốc.')
P('Liu và cộng sự trình bày một kết cấu biến đổi độ cứng dựa trên giam giữ áp suất dương của môi trường hạt trong một túi hoặc khoang, kèm các kiểm tra ảnh hưởng của hình học và áp suất [3]. Trong cấu hình đó, áp suất làm thay đổi trạng thái tiếp xúc giữa hạt và biên bao, nhưng đáp ứng đo được vẫn là đáp ứng tổng hợp của hạt, túi và kết cấu đỡ. Kết quả này chứng minh rằng áp suất dương có thể được sử dụng để điều chỉnh đáp ứng uốn trong một kiến trúc cụ thể; nó không chứng minh một quan hệ áp suất–độ cứng phổ quát, cũng không chứng minh áp suất tại nguồn bằng lực pháp tuyến giữa các dây.')
P('Zhang và Yao xây dựng mô hình cho một chuỗi sợi chịu giam giữ áp suất dương, trong đó các trạng thái dính, trượt một phần và trượt hoàn toàn được mô tả bằng tham số hiệu dụng và ngưỡng ma sát [4]. Mô hình và thí nghiệm của họ là một tương đồng gần về mặt cơ học vì đều liên quan đến sợi, áp suất và đáp ứng uốn. Tuy vậy, hệ của họ sử dụng sợi nylon liên kết bằng khớp cứng và một bàng quang tạo áp suất; MP1-R dùng bó TiNi, hình học bó và các tiếp diện wire–wire/wire–sleeve chưa được đồng nhất. Hơn nữa, một phần tham số của mô hình được nhận dạng từ đáp ứng kết cấu. Vì vậy, [4] hỗ trợ câu hỏi về hiệu lực của mô hình và nhu cầu đo áp suất gần mẫu, nhưng không cho phép chuyển trực tiếp các hệ số sang TiNi.')
P('Zhang, Yao, Zhao và Wei dùng mô hình liên tục cho dầm layer-jamming bằng các lớp PVC chịu hút chân không. Mô hình mô tả ngưỡng trượt kiểu Coulomb, phân vùng dính–trượt và trường ứng suất trong dầm, sau đó so sánh biến dạng toàn cục với mô phỏng phần tử hữu hạn và một mẫu nhiều lớp [5]. Nguồn này là tương tự lý thuyết–cơ học trong miền vật liệu PVC và giam giữ chân không. Nó không phải bằng chứng cho jamming sợi áp suất dương, TiNi, đo lực pháp tuyến cục bộ hoặc kiểm chứng MP1-R. Đặc biệt, tác giả thừa nhận các giới hạn liên quan đến ứng suất pháp tuyến ngang, hiệu ứng đầu mút và sai lệch vùng trượt khi độ cong lớn; các giới hạn này củng cố nhu cầu kiểm tra đường truyền lực thay vì giả định một quan hệ áp suất–tiếp xúc.')
TABLE('Bảng 2.1. So sánh các đường truyền giam giữ trong các kiến trúc đã được thẩm định',
      ['Kiến trúc', 'Tác nhân giam giữ', 'Đáp ứng chính', 'Giới hạn khi chuyển sang MP1-R'],
      [
          ['Bó dây/sợi không kim loại [1]', 'Hút chân không qua bao mềm', 'Lực–độ võng, mô men–góc xoắn', 'Không phải TiNi; tiếp diện và lực màng chưa tách độc lập'],
          ['Giam giữ hạt [3]', 'Áp suất dương làm nén môi trường hạt', 'Uốn của cụm hạt–túi', 'Lực hạt–biên và độ mềm túi phụ thuộc kiến trúc'],
          ['Giam giữ sợi [4]', 'Bàng quang áp suất dương và thành phản lực', 'Nhánh dính–trượt và tải tới hạn', 'Tham số hiệu dụng và phản lực cục bộ chưa được đo độc lập'],
          ['Layer-jamming liên tục [5]', 'Hút chân không giữa các lớp PVC', 'Ứng suất, vùng trượt và tải–độ võng', 'Tương tự cơ học; không phải bó sợi áp suất dương hoặc TiNi'],
          ['MP1-R', 'Áp suất gần mẫu và phản lực hướng tâm dự kiến', 'Mô men–độ cong, trượt cục bộ và biến thiên theo trạng thái TiNi', 'Ánh xạ áp suất–phản lực–lực pháp tuyến chưa được xác định'],
      ], 'Các dòng đầu là bằng chứng trực tiếp trong phạm vi từng kiến trúc; dòng MP1-R là miền cần kiểm chứng, không phải kết quả đã có.')
P('So sánh trên cho thấy từ “áp suất” chỉ mô tả biến kích thích ở một vị trí nào đó trong hệ. Để suy ra biến dạng uốn, cần biết áp suất tác động lên màng hoặc thành nào, thành đó tạo phản lực ra sao, phản lực phân bố lên các phần tử thế nào, và các tiếp diện có trượt hay không. Vì vậy, MP1-R không đặt mục tiêu tìm một quy luật áp suất–độ cứng chung; mục tiêu phù hợp hơn là đặc trưng hóa quan hệ trong một tiết diện, vật liệu và lịch sử tải đã khóa.')

H2('2.3. Cơ học tiếp xúc, ma sát và dính–trượt trong kết cấu nhiều phần tử')
P('Tại một tiếp diện, lực tiếp tuyến do ma sát thường được giới hạn bởi lực pháp tuyến và hệ số ma sát. Dạng bất đẳng thức Coulomb tối thiểu có thể viết là:')
EQ('F_t ≤ μN                                                        (2.1)')
P('Trong đó F_t là lực tiếp tuyến, μ là hệ số ma sát hiệu dụng và N là lực pháp tuyến tại tiếp diện. Phương trình (2.1) không nói áp suất chất lưu bằng N. Giữa hai đại lượng còn có màng hoặc thành phản lực, hình học đóng gói, biến dạng cục bộ, điều kiện đầu mút và phân bố tải. Đây là lý do một đồng hồ đo áp suất ở nguồn không đủ để xác định lực tiếp xúc hoặc lực ma sát trong bó dây.')
P('Trong mô hình sợi áp suất dương, Zhang và Yao giới hạn lực cắt hoặc ngưỡng trượt bằng một tham số liên quan đến áp suất, nhưng phản lực thành và tiếp diện sợi–thành vẫn là một phần của giả thiết kiến trúc [4]. Vì vậy, kết quả của họ phù hợp với diễn giải “áp suất có thể điều kiện hóa khả năng trượt” trong hệ đã xác định. Nó không chứng minh rằng mọi cấu hình bó dây đều có cùng phân bố N, cũng không chứng minh ma sát là cơ chế duy nhất của mọi nhánh uốn.')
P('Trong mô hình layer-jamming liên tục, Zhang và cộng sự phân biệt ứng suất pháp tuyến dọc trục với ứng suất cắt giữa các lớp, dùng ngưỡng ma sát phụ thuộc tích μp để mô tả vùng trượt [5]. Cách mô tả này hữu ích cho MP1-R ở cấp độ mô hình: một mô hình đối chứng có thể cần các trạng thái dính, trượt một phần và trượt hoàn toàn. Tuy nhiên, p trong mô hình PVC là áp suất giam giữ của kiến trúc đó; nó không phải phép đo trực tiếp N của một tiếp diện wire–wire hoặc wire–sleeve trong bó TiNi.')
P('Barsi, Carboni và Lacarbonara phát triển mô hình cơ học cho dây cáp ngắn và kiểm tra các giới hạn độ cứng bằng thí nghiệm uốn [8]. Công trình này cho thấy các giả thiết về biến dạng dây, trạng thái tiếp xúc và điều kiện đầu mút có thể tạo ra các cận trên hoặc cận dưới cho độ cứng đo được. Tuy nhiên, bài báo không cung cấp một luật dự đoán đầy đủ cho chu kỳ trễ hoặc nghiệm phân bố áp suất–tiếp xúc. Do đó, nó phù hợp làm đối thủ giới hạn độ cứng, không phải bằng chứng rằng một mô hình ma sát đã giải thích toàn bộ MP1-R.')
P('Vahidi và cộng sự trình bày mô hình và đáp ứng cơ học của các dây cáp SMA đơn và kép xoắn [9]. Nguồn này cung cấp tiền lệ cho việc kết hợp mô hình vật liệu TiNi với tiếp xúc trong dây cáp, nhưng phạm vi tải, hình học và điều kiện biên là khác với bó chịu uốn ngang và áp suất gần mẫu. Sự tồn tại của một mô hình tiếp xúc–vật liệu như vậy chỉ cho phép MP1-R dùng nó hoặc một dạng tương đương làm mô hình đối chứng; nó không chứng minh mô hình đó đủ chính xác cho tiết diện mới.')
P('Các đại lượng đo cũng cần được giữ tách biệt. Độ dốc lực–độ võng là tỷ số giữa lực ngoài và chuyển vị; độ cứng uốn M–κ là tỷ số giữa mô men và độ cong; tổn hao DMA là đại lượng phụ thuộc tần số và nhiệt độ; diện tích vòng trễ là công cơ học tổng hợp trên một chu kỳ. Những đại lượng này có thể cùng thay đổi khi ma sát hoặc chuyển pha xuất hiện, nhưng không thể được thay thế cho nhau hoặc gán trực tiếp cho một lực ma sát cục bộ. Các tổng quan về cơ cấu biến đổi độ cứng cũng cho thấy thuật ngữ độ cứng thường được dùng cho những đại lượng có thứ nguyên và phép đo khác nhau, do đó MP1-R phải khai báo rõ đại lượng được sử dụng [18].')
TABLE('Bảng 2.2. Kỷ luật diễn giải các đại lượng cơ học',
      ['Đại lượng', 'Định nghĩa vận hành', 'Có thể suy ra', 'Không được suy ra trực tiếp'],
      [
          ['Độ dốc F–δ', 'Biến thiên lực ngoài theo độ võng', 'Đáp ứng tổng hợp của cụm trong miền tải', 'M–κ hoặc tổn hao cục bộ'],
          ['Độ cứng M–κ', 'Mô men chia cho độ cong trong miền xác định', 'Độ cứng uốn của mẫu/đoạn mẫu', 'Lực pháp tuyến hoặc tiếp diện chi phối'],
          ['Tổn hao DMA', 'Đáp ứng động theo tần số/nhiệt độ', 'Thay đổi vật liệu–cấu trúc trong điều kiện DMA', 'Phần năng lượng riêng do ma sát'],
          ['Công vòng trễ', 'Tích phân lực hoặc mô men theo chu kỳ', 'Tổng tiêu tán trong phép đo', 'Tỷ phần riêng của chuyển pha, trượt hoặc sleeve'],
          ['Lực trượt giao diện', 'Lực cần để tạo chuyển động tương đối có kiểm soát', 'Điện trở của phép thử giao diện', 'μ và N riêng rẽ nếu chưa có hiệu chuẩn độc lập'],
      ], 'Các định nghĩa này được dùng để tránh gộp các thước đo không tương đương khi so sánh liên nghiên cứu.')
P('Khi chuyển từ trạng thái dính sang trượt, độ cứng biểu kiến có thể giảm, tăng theo nhánh hoặc tạo vòng trễ tùy đường tải và điều kiện biên. Vì vậy, “ma sát tồn tại” chỉ là mệnh đề cấp thấp. Cần phân biệt bốn câu hỏi: ma sát có hiện diện hay không; lực pháp tuyến cục bộ có được biết hay không; tiếp diện chi phối đã được nhận dạng hay chưa; và cơ chế của toàn bộ vòng trễ đã được phân rã hay chưa. Bằng chứng Phase 3 chỉ cho phép trả lời chắc chắn câu hỏi đầu trong các kiến trúc liên quan; ba câu sau vẫn là vấn đề nhận dạng đối với MP1-R.')

H2('2.4. Nhận dạng tương tác wire–wire và wire–sleeve')
P('Bó dây MP1-R có ít nhất hai họ tiếp diện có thể tạo điện trở: tiếp xúc giữa các dây và tiếp xúc giữa dây với sleeve hoặc thành phản lực. Ngoài ra, chuyển động ở đầu mút, biến dạng sleeve và thay đổi packing có thể tạo đáp ứng giống trượt. Vì thế, một đường cong uốn toàn cục không đủ để xác định tiếp diện nào chi phối.')
P('Jeon và cộng sự dùng lò xo SMA để thay đổi lực ép lên vùng dây–ống cao su, đồng thời đo lực kéo một dây và đáp ứng uốn của robot nhiều sống [6]. Phép kéo một dây tạo thêm quan sát giao diện ngoài đường cong uốn, nhưng lực đo vẫn là tích hợp của ma sát và tải pháp tuyến cùng các tổn hao phụ. Hơn nữa, chuyển pha của lò xo tác động khác với trạng thái của dây kết cấu. Nguồn này là tiền lệ trực tiếp cho phép đo giao diện wire–sleeve và cho lập luận rằng cần quan sát độc lập; nó không xác định trước đóng góp của wire–wire trong MP1-R.')
P('Liu sử dụng các mẫu cáp được cắt chọn lọc để kích thích trượt giữa các lớp dây kề nhau và đo lực cản trượt tĩnh [7]. Cách tách lớp này chứng minh rằng có thể thiết kế một phép thử hướng tới tiếp diện nội bộ thay vì chỉ đo đáp ứng toàn cáp. Tuy nhiên, lực pháp tuyến và áp suất trung bình trong thí nghiệm được suy ra bằng hệ số ma sát mượn từ tài liệu và diện tích tiếp xúc xấp xỉ; chúng không được hiệu chuẩn độc lập. Nguồn này vì vậy là tương đồng phương pháp, không phải lời giải cho ánh xạ áp suất–N của MP1-R.')
P('Hai họ bằng chứng trên dẫn đến một kết luận thận trọng. Nhận dạng wire–wire so với wire–sleeve là yêu cầu nhận dạng hệ thống và thiết kế thí nghiệm, không phải một khoảng trống tri thức khoa học đã được chứng minh. Nếu có các ràng buộc giao diện độc lập, phép đo có thể xác định hoặc giới hạn đóng góp của từng đường. Nếu không, kết quả đúng phải là báo cáo “không nhận dạng được” thay vì gán một nhánh toàn cục cho trượt cục bộ.')
P('Tương tự, một nhánh lực–độ võng hoặc vòng trễ chỉ có thể được gắn với khởi phát trượt khi nó đồng thời phù hợp với quan sát trượt tương đối, biến dạng dây hoặc chuyển động sleeve/đầu mút. Khi các kênh cục bộ không có, nhãn “chuyển tiếp cấu trúc” chỉ nên được giữ ở mức hiện tượng học.')

H2('2.5. Đặc tính nhiệt–cơ của TiNi trong kết cấu dây')
P('TiNi (NiTi) là hợp kim nhớ hình có thể thể hiện siêu đàn hồi, biến đổi mô đun biểu kiến và trễ cơ học khi trạng thái pha thay đổi. Tuy nhiên, vật liệu được gọi là TiNi không đồng nghĩa với việc chuyển pha hoạt động trong mọi miền biến dạng, nhiệt độ và lịch sử tải. Do đó, trạng thái vật liệu phải được kiểm tra trên cùng lô dây và trong miền mà phép uốn MP1-R thực sự tiếp cận.')
P('Reedlunn, Daly và Shaw đo đáp ứng gần đẳng nhiệt của các cáp TiNi có cấu trúc 7×7 và 1×27, đồng thời dùng DIC, ảnh nhiệt và các mẫu thành phần để quan sát đáp ứng phụ thuộc trạng thái [10], [11]. Hai phần của nghiên cứu tạo bằng chứng mạnh cho miền kéo–xoắn của các cáp đã khảo sát: mô đun không đổi không mô tả đầy đủ mọi miền chuyển pha hoạt động. Tuy vậy, các phép thử không phải là uốn bó dưới áp suất ngoài; vì thế, ngưỡng chuyển pha và tỷ phần tổn hao không được chuyển nguyên vẹn sang MP1-R.')
P('Kang và cộng sự phát triển mô hình phần tử hữu hạn cho cáp TiNi siêu đàn hồi và đưa vào biến đổi vật liệu phụ thuộc pha [12]. Trong cấu hình được thẩm định, tiếp xúc được đơn giản hóa và ma sát Coulomb không được triển khai như một quan sát độc lập. Nguồn này chứng minh sự tồn tại của mô hình vật liệu–cáp có xét chuyển pha, nhưng không chứng minh mô hình đó đã mô tả tương tác ma sát–áp suất trong bó MP1-R.')
P('Carboni và Lacarbonara khảo sát vòng trễ của dây cáp hỗn hợp NiTiNOL–thép trong một bộ hấp thụ dao động [13]. Tác giả liên hệ đáp ứng với cả ma sát và chuyển pha, nhưng phép đo tổng hợp không phân tách độc lập hai nguồn tiêu tán. Liu và cộng sự cũng báo cáo khả năng giảm chấn phụ thuộc nhiệt độ và hình học trong vi sợi TiNi bện bằng DMA và chu kỳ nhiệt [14]. Các kết quả này hữu ích để lập danh sách biến kiểm soát, song tổn hao DMA không thể được đồng nhất với công ma sát trong phép uốn chậm của bó dây.')
P('Narjabadifam và cộng sự kết hợp thử nghiệm dây cáp thép với mô phỏng dây cáp SMA [15]. Phần thử nghiệm vật lý chủ yếu cung cấp đối chiếu cho dây thép, còn đáp ứng SMA được đánh giá bằng mô hình số và các tham số vật liệu tương ứng. Vì vậy, nguồn này hỗ trợ cách xây dựng mô hình tiếp xúc và kiểm tra điều kiện biên, nhưng không thể được trích dẫn như một kiểm chứng thực nghiệm độc lập cho chuyển pha của dây TiNi trong uốn áp suất.')
P('Từ các nguồn trên, trạng thái TiNi và ma sát cần được xem là hai nhánh giải thích cạnh tranh nhưng có thể đồng thời hiện diện. Một biến thiên độ cứng theo nhiệt độ hoặc lịch sử có thể do vật liệu, tiếp xúc, hoặc thay đổi hình học gây ra. Chỉ khi nhiệt độ, biến dạng cục bộ, lịch sử chu kỳ và các đóng góp giao diện được quan sát đồng thời mới có thể phân rã chúng ở mức đủ cho một tuyên bố cơ chế.')

H2('2.6. Phân biệt cơ chế vật liệu và cơ chế tiếp xúc')
P('Ba trạng thái giả thuyết được giữ trong MP1-R. H0a-R xem đáp ứng chủ yếu do trạng thái nhiệt–cơ của TiNi. H0b-R xem các cơ học thông thường gồm tiếp xúc, ma sát, dính–trượt, điều kiện biên và mô hình vật liệu có xét chuyển pha có thể giải thích đáp ứng mà không cần một luật cấu thành mới. H1-R chỉ được xem là khả năng có điều kiện: một tương tác áp suất–tiếp xúc–vật liệu bổ sung được nhận dạng và cần thiết sau khi H0a-R, H0b-R và các nhiễu hình học đã được khóa.')
P('Phase 4 đánh giá H0a-R và H0b-R đều PLAUSIBLE, còn H1-R NOT_YET_DISTINGUISHABLE. Trạng thái này phù hợp với bằng chứng: TiNi có thể biến đổi theo trạng thái trong miền đã thử [10]–[14], trong khi các mô hình tiếp xúc, ma sát và giới hạn độ cứng đã tồn tại [4], [5], [8], [9], [12]. Không có nguồn nào trong biên đã thẩm định buộc phải chọn H1-R. Vì vậy, luận văn phải được thiết kế để vẫn có kết quả hợp lệ khi H0b-R dự đoán tốt hoặc khi chuyển pha không hoạt động trong miền uốn tiếp cận.')
P('Hệ quả phương pháp là mô hình đối chứng phải được khóa trước khi thử nghiệm giữ lại. Việc không tìm thấy một phương trình viết đúng cho tiết diện MP1-R không phải bằng chứng rằng cơ học hiện có không đủ. Một mô hình bổ sung chỉ có thể được xem xét nếu sai số trên dữ liệu giữ lại lặp lại, vượt qua bất định đo, tồn tại trên đường tải dành riêng cho kiểm tra, và có biến trạng thái nhận dạng được thay vì chỉ tái khớp tham số.')

H2('2.7. SMA như nguồn dẫn động tạo áp suất')
P('SMA dùng để dẫn động nguồn áp suất là một vấn đề khác với TiNi dùng làm phần tử chịu lực. Pierce và Mascaro đã trình bày một bơm chất lỏng được dẫn động bởi dây SMA, trong đó chuyển vị của bộ chấp hành được liên kết với động lực nhiệt–lưu chất và thể tích dịch chuyển [16]. Nguồn này thiết lập tiền lệ SMA–chất lỏng, nhưng kiến trúc bơm và điều kiện làm mát không phải nguồn áp suất lò xo–piston của MP1-R.')
P('Huynh và cộng sự tích hợp một vi bơm với hệ jamming có thể chuyển trạng thái, đồng thời phân biệt ảnh hưởng áp suất lên uốn và giới hạn của việc suy ra áp suất tại cụm từ hiệu chuẩn riêng [17]. Nguồn này cho thấy nguồn áp suất, mạch lưu chất và kết cấu jamming có thể được tích hợp, nhưng không chứng minh khả năng tái tạo đáp ứng của một bó TiNi hoặc một piston do lò xo SMA dẫn động.')
P('Jeon và cộng sự cung cấp thêm một ví dụ trong đó SMA thay đổi lực ép tại giao diện dây–cao su [6]. Trong trường hợp đó, SMA là bộ điều biến ma sát của cơ cấu robot, không phải bằng chứng rằng dây kết cấu đã chuyển pha theo cùng lịch sử nhiệt. MP1-R vì vậy phải ghi riêng nhiệt độ, lực–hành trình, tốc độ đáp ứng và lịch sử của lò xo SMA; không được dùng kết quả của lò xo làm đại diện trực tiếp cho trạng thái của dây TiNi.')

H2('2.8. Tách nguồn kích thích và đáp ứng kết cấu')
P('Đề xuất Bench A dùng nguồn áp suất ngoài có kiểm soát để đặc trưng hóa kết cấu trước. Mục đích của Bench A là tạo một can thiệp áp suất đã biết gần mẫu, đo mô men–độ cong hoặc đại lượng độ cứng khai báo, và kiểm soát nhiệt độ, lịch sử tải, packing, sleeve và chuyển động đầu mút. Đây là cách tách câu hỏi “kết cấu phản ứng ra sao khi áp suất được áp đặt” khỏi câu hỏi “nguồn áp suất tạo ra áp suất như thế nào”.')
P('Bench B dùng lò xo SMA, piston và mạch chất lưu để kiểm tra nguồn tích hợp. Các nguồn SMA–chất lỏng [16] và hệ vi bơm–jamming [17] cho thấy việc ghép bộ chấp hành với mạch chất lưu là khả thi về nguyên tắc, nhưng các thông số động, tổn thất seal, độ mềm mạch và trễ nhiệt phụ thuộc thiết kế. Vì vậy, Bench B cần được kiểm tra trên cùng thước đo áp suất gần mẫu, không được suy ra từ áp suất nguồn duy nhất.')
P('Khi hai bench được so sánh ở áp suất, nhiệt độ, tải, lịch sử và hình học tương ứng, sự phù hợp của đáp ứng tích hợp với đáp ứng từ Bench A có thể hỗ trợ kết luận về khả năng tích hợp. Nếu hai đáp ứng khác nhau ở điều kiện chưa ghép cặp, khác biệt đó chỉ chỉ ra một vấn đề nguồn hoặc truyền áp suất; nó không chứng minh H1-R. Tách bench là lý do thiết kế cho nhận dạng, không phải một tuyên bố mới lạ về kiến trúc.')

H2('2.9. Các mô hình cơ học hiện có và vai trò của mô hình đối chứng')
P('Các bằng chứng đã thẩm định cung cấp nhiều lớp mô hình đối chứng. Mô hình sợi áp suất dương của Zhang và Yao mô tả các nhánh trượt và dùng các tham số hiệu dụng [4]. Mô hình layer-jamming liên tục của Zhang và cộng sự cung cấp cách mô tả vùng dính–trượt và trường ứng suất trong một dầm nhiều lớp [5]. Mô hình dây cáp của Barsi và cộng sự cung cấp cận độ cứng trong các giả thiết hình học và vật liệu cụ thể [8]. Vahidi và cộng sự, Kang và cộng sự cùng các công trình liên quan cung cấp tiền lệ kết hợp biến đổi vật liệu và tiếp xúc ở cấp cáp [9], [12].')
P('Các mô hình này không có cùng phạm vi. Chúng khác về vật liệu, số phần tử, cách tạo áp suất, điều kiện đầu mút, định nghĩa độ cứng, và mức độ quan sát lực tiếp xúc. Do đó, MP1-R không nên trộn các tham số của chúng thành một “mô hình chuẩn” duy nhất. Mô hình đối chứng cần được khóa với một cấu trúc rõ ràng: biến vào là áp suất gần mẫu, nhiệt độ, lịch sử tải và hình học; đầu ra là đường M–κ hoặc chỉ số độ cứng đã khai báo; tham số được nhận dạng trên tập hiệu chuẩn; đánh giá cuối cùng dùng đường tải dành riêng và bất định đo.')
P('Một quy trình như vậy phân biệt hiệu chỉnh với kiểm chứng. Nếu mô hình phù hợp với các đường giữ lại trong giới hạn đã định, H0b-R được hỗ trợ và đây là một kết quả hợp lệ về miền hiệu lực của cơ học thông thường. Nếu mô hình không phù hợp, cần kiểm tra trước các khả năng rò rỉ tham số, chuyển động sleeve, nhiệt độ, packing, sai khác áp suất nguồn–mẫu và sai số đo. Chỉ phần dư lặp lại sau các kiểm soát này mới tạo cơ sở có điều kiện cho H1-R; sự thất bại của một giản lược đơn lẻ không đủ để yêu cầu luật cấu thành mới.')

H2('2.10. Tổng hợp bằng chứng và giới hạn suy luận')
P('Chuỗi nhân quả làm khung cho MP1-R được viết như sau: áp suất chất lưu → đáp ứng màng hoặc vỏ → phản lực hướng tâm → lực pháp tuyến cục bộ → khả năng truyền ma sát → trạng thái trượt → đáp ứng uốn. Các nguồn liên quan hỗ trợ từng đoạn ở mức khác nhau, nhưng không nguồn nào thiết lập toàn bộ chuỗi trong bó TiNi của MP1-R.')
TABLE('Bảng 2.3. Trạng thái bằng chứng của chuỗi nhân quả MP1-R',
      ['Liên kết', 'Trạng thái', 'Cơ sở và giới hạn'],
      [
          ['Áp suất chất lưu → đáp ứng màng/vỏ', 'SUPPORTED / MODEL-DEPENDENT', 'Các hệ áp suất dương và bơm–jamming cho thấy đường áp suất phụ thuộc bao, túi và mạch; chưa có ánh xạ chung cho MP1-R [3], [4], [17].'],
          ['Màng/vỏ → phản lực hướng tâm', 'MODEL-DEPENDENT', 'Phản lực phụ thuộc độ mềm, hình học, packing và điều kiện đầu mút; cần đo biến dạng hoặc đặt cận.'],
          ['Phản lực hướng tâm → lực pháp tuyến wire–wire/wire–sleeve', 'NOT_ESTABLISHED', 'Không được suy ra từ đồng hồ áp suất; đây là mắt xích yếu nhất cần nhận dạng bằng quan sát độc lập.'],
          ['Lực pháp tuyến → khả năng ma sát', 'ESTABLISHED IN PRINCIPLE', 'Bất đẳng thức Coulomb cung cấp cơ sở mô hình, nhưng μ và N hiệu dụng của từng tiếp diện chưa được tách.'],
          ['Khả năng ma sát → trạng thái trượt', 'SUPPORTED / MODEL-DEPENDENT', 'Các mô hình sợi và layer-jamming có nhánh dính–trượt; ngưỡng cụ thể phụ thuộc vật liệu và điều kiện biên [4], [5].'],
          ['Trạng thái trượt → đáp ứng uốn', 'SUPPORTED CONNECTION', 'Các nghiên cứu wire/fiber/layer cho thấy trạng thái trượt liên quan đến lực–độ võng hoặc mô men–độ cong [1], [4], [5], [8].'],
          ['Đáp ứng uốn → quy kết cơ chế', 'INFERRED ONLY', 'Đáp ứng toàn cục cần được kết hợp với trượt cục bộ, nhiệt độ và chuyển động biên; uốn toàn cục không xác định tiếp diện chi phối.'],
      ], 'Mắt xích “phản lực hướng tâm → lực pháp tuyến cục bộ” là critical weakest link được giữ nguyên từ Phase 4.')
P('Bảng 2.3 cho phép phân biệt điều đã được thiết lập với liên hệ có thể bảo vệ và vấn đề chưa xác định. Sự hiện diện của hiệu ứng áp suất hoặc ma sát trong một kiến trúc liên quan không làm cho lực tiếp xúc cục bộ của MP1-R trở thành đại lượng đã biết. Tương tự, một mô hình dự đoán được một nhánh toàn cục không tự động chứng minh phân bố trượt tại từng dây.')

H2('2.11. Những vấn đề chưa được xác định và nhu cầu đặc trưng hóa cho MP1-R')
P('Phase 5 không phê duyệt một khoảng trống tri thức khoa học ở cấp độ G1. Các vấn đề còn lại được phân loại bảo thủ thành hai nhóm đặc trưng hóa thực nghiệm, năm yêu cầu nhận dạng hệ thống, một nhu cầu xác nhận kỹ thuật nguồn và một nhu cầu xác nhận tích hợp. Cách gọi này quan trọng: việc quan hệ chưa được thiết lập cho một cấu hình cụ thể không đồng nghĩa quan hệ đó chưa được biết trong khoa học nói chung.')
P('Thứ nhất, tiết diện, mặt phản lực, packing và các ứng viên wire–wire/wire–sleeve phải được cố định trước khi diễn giải dữ liệu. Đây là tiền đề dự án, không phải khoảng trống. Sau khi hình học được khóa, MP1-R cần xác định hoặc đặt cận cho truyền áp suất đến lực tiếp xúc cục bộ, đồng thời tách ảnh hưởng của sleeve, packing, đầu mút và chuyển động phản lực. Đây là yêu cầu nhận dạng hệ thống; kết quả có thể là một ánh xạ định lượng hoặc một cận không đủ để nhận dạng duy nhất.')
P('Thứ hai, đóng góp của wire–wire, wire–sleeve và chuyển động sleeve/đầu mút phải được kiểm tra bằng các quan sát độc lập. S04 và S22 cho thấy các phép thử giao diện có thể được xây dựng ở những hệ khác nhau [6], [7], nhưng không có bằng chứng rằng chỉ một đường cong uốn toàn cục sẽ phân biệt được các tiếp diện trong MP1-R. Nếu các phép thử độc lập không khả thi, tính không nhận dạng được phải được xem là kết quả phương pháp chứ không phải thất bại của luận văn.')
P('Thứ ba, hoạt tính chuyển pha của cùng lô TiNi trong miền biến dạng, nhiệt độ và lịch sử thực tế phải được đặc trưng. Bằng chứng từ cáp kéo–xoắn và vi sợi cho thấy trạng thái TiNi có thể ảnh hưởng đáp ứng trong các miền đã khảo sát [10]–[14], nhưng chưa xác định hoạt tính đó trong miền uốn áp suất của MP1-R. Các phép đo vật liệu và nhiệt độ vì vậy phục vụ diễn giải, không phải để giả định trước rằng chuyển pha chi phối vòng trễ.')
P('Thứ tư, mô hình tiếp xúc/ma sát và vật liệu có xét chuyển pha phải được kiểm tra trên dữ liệu giữ lại. Câu hỏi là mô hình hiện có dự đoán được đường áp suất–độ cong đã khóa trong giới hạn bất định hay không. Một phần dư lặp lại chỉ trở nên liên quan đến H1-R sau khi kiểm soát các biến hình học, biên, nhiệt và giao diện. Nhu cầu này là đặc trưng hóa hiệu lực mô hình, không phải tuyên bố rằng mô hình thông thường đã bị bác bỏ.')
P('Cuối cùng, nguồn SMA–piston cần được đặc trưng hóa về miền áp suất–thể tích có thể đạt và hồi phục, sau đó so sánh với Bench A dưới điều kiện ghép cặp. Đây là nhu cầu xác nhận kỹ thuật và tích hợp. Khác biệt của một lò xo, piston hoặc đường ống so với nghiên cứu trước không tự nó là cơ chế khoa học mới.')
TABLE('Bảng 2.4. Bản đồ vấn đề còn lại và cách diễn đạt được phép',
      ['Vấn đề', 'Phân loại chính', 'Cách diễn đạt được phép'],
      [
          ['Ánh xạ áp suất–tiếp xúc', 'Nhận dạng hệ thống / đặc trưng hóa', 'Quan hệ truyền áp suất đến tiếp xúc cục bộ được xác định hoặc đặt cận cho cấu hình đã định.'],
          ['Wire–wire so với wire–sleeve', 'Nhận dạng hệ thống', 'Đóng góp giao diện được nhận dạng hoặc báo cáo là không nhận dạng được dưới các quan sát hiện có.'],
          ['Hoạt tính chuyển pha cùng lô', 'Đặc trưng hóa thực nghiệm', 'Nghiên cứu đặc trưng hóa xem chuyển pha có hoạt động trong miền tiếp cận hay không.'],
          ['Độ đủ của mô hình đối chứng', 'Đặc trưng hóa / phân biệt mô hình', 'Đánh giá khả năng dự đoán của mô hình khóa trên các đường giữ lại.'],
          ['Nguồn SMA–piston', 'Xác nhận kỹ thuật và tích hợp', 'Đặc trưng hóa miền vận hành và kiểm tra đáp ứng tích hợp dưới điều kiện ghép cặp.'],
      ], 'Các phân loại trên không phải là tuyên bố về khoảng trống văn liệu rộng hơn MP1-R.')

H2('2.12. Định hướng nghiên cứu của luận văn')
P('Từ tổng quan trên, câu hỏi nghiên cứu chính được khóa ở dạng: với hình học bó TiNi, lô vật liệu và lịch sử tải cố định, áp suất gần mẫu thay đổi đáp ứng uốn như thế nào, và mô hình tiếp xúc/ma sát/chuyển pha thông thường đã khóa dự đoán các đường áp suất–độ cong giữ lại chính xác đến đâu? Câu hỏi này gắn đặc trưng hóa định lượng với phân biệt mô hình, không yêu cầu H1-R phải đúng.')
P('Câu hỏi phụ thứ nhất hỏi đường điện trở nào có thể được nhận dạng hoặc đặt cận: wire–wire, wire–sleeve hay chuyển động sleeve/đầu mút. Câu hỏi phụ thứ hai hỏi TiNi cùng lô có chuyển pha trong miền biến dạng–nhiệt độ–lịch sử được tiếp cận hay không, và cần kiểm soát trạng thái vật liệu nào để diễn giải đáp ứng. Hai câu hỏi phụ này định nghĩa gánh nặng quan sát cho các tuyên bố cơ chế; chúng không biến mọi kết quả chưa đo được thành khoảng trống khoa học.')
P('Đóng góp chính được giới hạn ở đặc trưng hóa định lượng đáp ứng uốn phụ thuộc áp suất của cấu hình bó TiNi đã định, cùng với một mô hình đối chứng thông thường được khóa và kiểm tra trên các đường giữ lại. Đóng góp thứ cấp có thể là nhận dạng giao diện/trượt cục bộ và kiểm tra dự đoán của mô hình. Đặc trưng hóa nguồn SMA–piston và xác nhận tích hợp là các nhiệm vụ hỗ trợ. Một hạng tử áp suất–tiếp xúc–vật liệu bổ sung chỉ là mở rộng có điều kiện khi phần dư giữ lại lặp lại, nhận dạng được và cải thiện dự đoán vượt qua việc tái khớp tham số.')
P('Vì vậy, tiêu đề làm việc được điều chỉnh thành “Đặc trưng hóa ứng xử uốn phụ thuộc áp suất của bó dây TiNi với nguồn áp suất dẫn động bằng lò xo SMA”. Cách gọi này mô tả đối tượng và nguồn kích thích mà không giả định trước rằng ma sát đã được điều khiển hoặc tiếp diện chi phối đã được chứng minh. Kết quả không có hiệu ứng áp suất, kết quả cho thấy H0b đủ, hoặc kết quả cho thấy chuyển pha không hoạt động đều có thể tạo thành kết luận khoa học hợp lệ trong phạm vi đã khóa.')

H1('TÀI LIỆU THAM KHẢO')
refs = [
'[1] M. Bai et al., “Detachable soft actuators with tunable stiffness based on wire jamming,” Applied Sciences, vol. 12, no. 7, Art. no. 3582, 2022, doi: 10.3390/app12073582.',
'[2] F. Caro and M. G. Carmichael, “A review of mechanisms to vary the stiffness of laminar jamming structures and their applications in robotics,” Actuators, vol. 13, no. 2, Art. no. 64, 2024, doi: 10.3390/act13020064.',
'[3] T. Liu et al., “A positive pressure jamming based variable stiffness structure and its application on wearable robots,” IEEE Robotics and Automation Letters, vol. 6, no. 4, pp. 8078–8085, 2021, doi: 10.1109/LRA.2021.3097255.',
'[4] S. Zhang and J. Yao, “A variable stiffness omnidirectional chain based on positive-pressure fiber jamming,” Mechanical Sciences, vol. 17, 2026, doi: 10.5194/ms-17-481-2026.',
'[5] S. Zhang, J. Yao, W. Zhao, and C. Wei, “A continuum-based model for a layer jamming beam,” Mechanical Sciences, vol. 16, pp. 821–830, 2025, doi: 10.5194/ms-16-821-2025.',
'[6] J. Jeon et al., “Towards a snake-like flexible robot with variable stiffness using an SMA spring-based friction change mechanism,” IEEE Robotics and Automation Letters, 2022, doi: 10.1109/LRA.2022.3174363.',
'[7] X. Liu, “Cable vibration considering internal friction,” M.S. thesis, Department of Mechanical Engineering, University of Hawaiʻi, Aug. 2004.',
'[8] A. Barsi, A. Carboni, and L. Lacarbonara, “A new mechanical model of short wire ropes: Theory and experimental validation,” Engineering Structures, 2025, doi: 10.1016/j.engstruct.2024.119217.',
'[9] M. Vahidi et al., “Mechanical response of single and double-helix SMA wire ropes,” Mechanics of Advanced Materials and Structures, 2022, doi: 10.1080/15376494.2021.1955313.',
'[10] C. Reedlunn, S. H. Daly, and J. S. Shaw, “Superelastic shape memory alloy cables: Part I – Isothermal tension experiments,” International Journal of Solids and Structures, 2013, doi: 10.1016/j.ijsolstr.2013.03.013.',
'[11] C. Reedlunn, S. H. Daly, and J. S. Shaw, “Superelastic shape memory alloy cables: Part II – Subcomponent isothermal responses,” International Journal of Solids and Structures, 2013, doi: 10.1016/j.ijsolstr.2013.03.015.',
'[12] J. Kang et al., “Finite element method for mechanical behavior of shape memory alloy superelastic cables,” Journal of Mechanical Engineering, 2020, doi: 10.3901/JME.2020.14.065.',
'[13] A. Carboni and L. Lacarbonara, “Nonlinear vibration absorber with pinched hysteresis: Theory and experiments,” Journal of Engineering Mechanics, 2016, doi: 10.1061/(ASCE)EM.1943-7889.0001072.',
'[14] L. Liu et al., “High damping capacity with a wide temperature window in braided NiTi microfilaments,” Materials Letters, 2026, Art. no. 141544, doi: 10.1016/j.matlet.2026.141544.',
'[15] M. Narjabadifam et al., “Experimental-numerical assessment of mechanical behavior of laboratory-made steel and NiTi shape memory alloy wire ropes,” Buildings, vol. 14, no. 6, Art. no. 1567, 2024, doi: 10.3390/buildings14061567.',
'[16] R. Pierce and M. G. Mascaro, “A biologically inspired wet shape memory alloy actuated robotic pump,” IEEE/ASME Transactions on Mechatronics, 2013, doi: 10.1109/TMECH.2012.2211032.',
'[17] T. Huynh et al., “Soft actuator with switchable stiffness using a micropump-activated jamming system,” Sensors and Actuators A: Physical, 2022, Art. no. 113449, doi: 10.1016/j.sna.2022.113449.',
'[18] B. Lin, S. Song, and J. Wang, “Variable stiffness methods of flexible robots for minimally invasive surgery: A review,” Bio-Design and Manufacturing, 2024, doi: 10.1016/j.birob.2024.100168.',
]
for r in refs: items.append(('ref', r))

# Build DOCX.
doc = Document()
sec = doc.sections[0]
sec.page_width = Mm(210); sec.page_height = Mm(297)
sec.top_margin = Cm(3.0); sec.bottom_margin = Cm(3.0)
sec.left_margin = Cm(3.5); sec.right_margin = Cm(2.0)
sec.header_distance = Cm(1.3); sec.footer_distance = Cm(1.3)

# Helpers for OOXML language and page fields.
def set_run_font(run, size=13, bold=False, italic=False):
    run.font.name = 'Times New Roman'
    run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    run.font.size = Pt(size)
    run.bold = bold; run.italic = italic
    lang = run._element.get_or_add_rPr().find(qn('w:lang'))
    if lang is None:
        lang = OxmlElement('w:lang'); run._element.get_or_add_rPr().append(lang)
    lang.set(qn('w:val'), 'vi-VN')

def set_para_spacing(p, line=1.5, first=True, after=0, before=0):
    fmt=p.paragraph_format
    fmt.line_spacing=line
    fmt.space_after=Pt(after); fmt.space_before=Pt(before)
    fmt.first_line_indent=Cm(1.0) if first else Cm(0)
    p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY

def add_page_field(p):
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run()
    set_run_font(r, 12)
    for tag, text in [('w:fldChar', None), ('w:instrText', ' PAGE '), ('w:fldChar', None)]:
        el = OxmlElement(tag)
        if tag == 'w:fldChar':
            el.set(qn('w:fldCharType'), 'begin' if text is None and not p._p.findall('.//' + qn('w:fldChar')) else 'end')
        else:
            el.set(qn('xml:space'), 'preserve'); el.text = text
        r._r.append(el)
    # Replace with an explicit editable PAGE field.
    r._r.clear_content()
    el=OxmlElement('w:fldChar'); el.set(qn('w:fldCharType'),'begin'); r._r.append(el)
    instr=OxmlElement('w:instrText'); instr.set(qn('xml:space'),'preserve'); instr.text=' PAGE '; r._r.append(instr)
    el=OxmlElement('w:fldChar'); el.set(qn('w:fldCharType'),'separate'); r._r.append(el)
    t=OxmlElement('w:t'); t.text='1'; r._r.append(t)
    el=OxmlElement('w:fldChar'); el.set(qn('w:fldCharType'),'end'); r._r.append(el)

a=sec.header.paragraphs[0]
add_page_field(a)
# Set page number start = 1.
pg = OxmlElement('w:pgNumType'); pg.set(qn('w:start'), '1'); sec._sectPr.append(pg)

styles=doc.styles
normal=styles['Normal']; normal.font.name='Times New Roman'; normal._element.rPr.rFonts.set(qn('w:eastAsia'),'Times New Roman'); normal.font.size=Pt(13)
normal.paragraph_format.line_spacing=1.5; normal.paragraph_format.first_line_indent=Cm(1.0); normal.paragraph_format.space_after=Pt(0)
for name,size,bold,align in [('Heading 1',16,True,WD_ALIGN_PARAGRAPH.CENTER),('Heading 2',13,True,WD_ALIGN_PARAGRAPH.LEFT),('Heading 3',13,True,WD_ALIGN_PARAGRAPH.LEFT)]:
    st=styles[name]; st.font.name='Times New Roman'; st._element.rPr.rFonts.set(qn('w:eastAsia'),'Times New Roman'); st.font.size=Pt(size); st.font.bold=bold
    st.paragraph_format.space_before=Pt(12 if name!='Heading 1' else 0); st.paragraph_format.space_after=Pt(6); st.paragraph_format.line_spacing=1.5; st.paragraph_format.keep_with_next=True
    st.paragraph_format.first_line_indent=Cm(0); st.paragraph_format.alignment=align

# Add a simple TOC field after title? Omit to keep standalone chapter clean.
for kind,payload in items:
    if kind=='h1':
        p=doc.add_paragraph(style='Heading 1'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run(payload); set_run_font(r,16,True)
    elif kind=='h2':
        p=doc.add_paragraph(style='Heading 2'); r=p.add_run(payload); set_run_font(r,13,True)
    elif kind=='h3':
        p=doc.add_paragraph(style='Heading 3'); r=p.add_run(payload); set_run_font(r,13,True)
    elif kind=='p':
        text, claims = payload
        p=doc.add_paragraph(style='Normal'); set_para_spacing(p,1.5,True)
        r=p.add_run(text); set_run_font(r,13)
    elif kind=='eq':
        p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.line_spacing=1.5; p.paragraph_format.space_after=Pt(0); p.paragraph_format.first_line_indent=Cm(0)
        r=p.add_run(payload); set_run_font(r,13)
    elif kind=='note':
        p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.LEFT; p.paragraph_format.line_spacing=1.0; p.paragraph_format.first_line_indent=Cm(0); p.paragraph_format.space_after=Pt(6)
        r=p.add_run(payload); set_run_font(r,10,italic=True)
    elif kind=='table':
        title, headers, rows, note=payload
        p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.first_line_indent=Cm(0); p.paragraph_format.space_before=Pt(6); p.paragraph_format.space_after=Pt(3)
        r=p.add_run(title); set_run_font(r,11,True)
        table=doc.add_table(rows=1, cols=len(headers)); table.style='Table Grid'; table.alignment=WD_TABLE_ALIGNMENT.CENTER
        hdr=table.rows[0].cells
        for i,h in enumerate(headers):
            hdr[i].text=''; hdr[i].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            pp=hdr[i].paragraphs[0]; pp.alignment=WD_ALIGN_PARAGRAPH.CENTER; pp.paragraph_format.line_spacing=1.0; pp.paragraph_format.first_line_indent=Cm(0)
            rr=pp.add_run(h); set_run_font(rr,10.5,True)
        for row in rows:
            cells=table.add_row().cells
            for i,val in enumerate(row):
                cells[i].text=''; cells[i].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP
                pp=cells[i].paragraphs[0]; pp.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY; pp.paragraph_format.line_spacing=1.0; pp.paragraph_format.first_line_indent=Cm(0); pp.paragraph_format.space_after=Pt(0)
                rr=pp.add_run(val); set_run_font(rr,10.5)
        if note:
            p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.LEFT; p.paragraph_format.line_spacing=1.0; p.paragraph_format.first_line_indent=Cm(0); p.paragraph_format.space_after=Pt(6)
            r=p.add_run('Ghi chú: '+note); set_run_font(r,10,italic=True)
    elif kind=='ref':
        p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.left_indent=Cm(0.75); p.paragraph_format.first_line_indent=Cm(-0.75); p.paragraph_format.line_spacing=1.0; p.paragraph_format.space_after=Pt(3)
        r=p.add_run(payload); set_run_font(r,11)

# Document metadata.
doc.core_properties.title='Chương 2 — Tổng quan nghiên cứu và cơ sở khoa học MP1-R'
doc.core_properties.subject='Evidence-controlled literature review for MP1-R'
doc.core_properties.author='MP1-R research workflow'
doc.core_properties.keywords='MP1-R, TiNi, variable stiffness, friction, pressure, IEEE'
doc.save(out_docx)

# Build traceability from a controlled claim register.
trace = [
 {'claim_id':'C2-001','chapter_subsection':'2.2','claim':'Wire/fiber jamming can change whole-assembly bending or torsional response in tested architectures.','source_ids':['S01'],'ieee_reference_numbers':[1],'evidence_status':'STRONG within tested nonmetallic vacuum architecture','classification':'direct','phase4_propositions':['RP001'],'phase5_mapping':['CONTRIB01'],'wording_boundary':'Do not transfer to TiNi or universal pressure–stiffness law.','audit_status':'PASS'},
 {'claim_id':'C2-002','chapter_subsection':'2.2','claim':'Jamming mechanisms differ by vacuum, positive pressure, material and boundary architecture.','source_ids':['S15','S02','S03','S18'],'ieee_reference_numbers':[2,3,4,5],'evidence_status':'synthesis with analogue restrictions','classification':'synthesis','phase4_propositions':['RP001','RP002','RP015'],'phase5_mapping':['GAP02'],'wording_boundary':'Architecture-scoped only.','audit_status':'PASS'},
 {'claim_id':'C2-003','chapter_subsection':'2.2','claim':'Positive-pressure fiber-chain systems provide a model/mechanistic precedent for pressure-conditioned branches, but local contact force is not independently established.','source_ids':['S03'],'ieee_reference_numbers':[4],'evidence_status':'MODERATE','classification':'direct plus bounded inference','phase4_propositions':['RP003','RP016'],'phase5_mapping':['GAP02','GAP08'],'wording_boundary':'No pressure=N equality.','audit_status':'PASS'},
 {'claim_id':'C2-004','chapter_subsection':'2.2','claim':'S18 is a vacuum PVC layer-jamming continuum analogue, not positive-pressure fiber or TiNi evidence.','source_ids':['S18'],'ieee_reference_numbers':[5],'evidence_status':'MODERATE analogue-only for MP1-R','classification':'analogy','phase4_propositions':['RP015','RP019'],'phase5_mapping':['GAP08'],'wording_boundary':'No direct MP1-R validation.','audit_status':'PASS'},
 {'claim_id':'C2-005','chapter_subsection':'2.3','claim':'Friction capacity depends on normal force and friction coefficient; pressure is not local normal force.','source_ids':['S03','S18'],'ieee_reference_numbers':[4,5],'evidence_status':'model-supported, configuration-bounded','classification':'synthesis/inference','phase4_propositions':['RP004','RP016'],'phase5_mapping':['GAP02'],'wording_boundary':'Do not infer N from source gauge alone.','audit_status':'PASS'},
 {'claim_id':'C2-006','chapter_subsection':'2.3','claim':'Short-rope models can provide stiffness bounds without providing a full hysteresis or contact-pressure law.','source_ids':['S06'],'ieee_reference_numbers':[8],'evidence_status':'MODERATE','classification':'direct','phase4_propositions':['RP006','RP007'],'phase5_mapping':['GAP08'],'wording_boundary':'Bounds only.','audit_status':'PASS'},
 {'claim_id':'C2-007','chapter_subsection':'2.4','claim':'Wire–sleeve sliding resistance can be measured as an independent observable, but it does not identify wire–wire dominance.','source_ids':['S04'],'ieee_reference_numbers':[6],'evidence_status':'MODERATE','classification':'direct/analogue','phase4_propositions':['RP009','RP013'],'phase5_mapping':['GAP04','GAP05'],'wording_boundary':'Global bending alone is insufficient.','audit_status':'PASS'},
 {'claim_id':'C2-008','chapter_subsection':'2.4','claim':'Selective internal cable-layer specimens provide a method precedent for internal-interface resistance, with inferred rather than directly measured N.','source_ids':['S22'],'ieee_reference_numbers':[7],'evidence_status':'MODERATE method analogue','classification':'direct analogue','phase4_propositions':['RP013','RP018'],'phase5_mapping':['GAP04'],'wording_boundary':'No simultaneous sleeve separation.','audit_status':'PASS'},
 {'claim_id':'C2-009','chapter_subsection':'2.5','claim':'Same-lot NiTi cables show state-sensitive response in tested tension/rotation domains, but transfer to pressure-conditioned bending is not established.','source_ids':['S05a','S05b'],'ieee_reference_numbers':[10,11],'evidence_status':'STRONG within tested domains','classification':'direct plus bounded transfer','phase4_propositions':['RP010','RP011'],'phase5_mapping':['GAP06','GAP07'],'wording_boundary':'No assumption of active transformation.','audit_status':'PASS'},
 {'claim_id':'C2-010','chapter_subsection':'2.5','claim':'Transformation-aware cable models exist, but friction/contact implementation and MP1-R adequacy remain separate questions.','source_ids':['S07','V-W02'],'ieee_reference_numbers':[12,9],'evidence_status':'MODERATE analogue','classification':'synthesis','phase4_propositions':['RP011','RP019'],'phase5_mapping':['GAP08','GAP09'],'wording_boundary':'No new law requirement.','audit_status':'PASS'},
 {'claim_id':'C2-011','chapter_subsection':'2.5','claim':'Mixed-rope and braided-NiTi studies support coexistence of material and interface effects, but do not partition aggregate loss.','source_ids':['S11','S13'],'ieee_reference_numbers':[13,14],'evidence_status':'MODERATE interpretive analogue','classification':'synthesis','phase4_propositions':['RP012'],'phase5_mapping':['GAP07'],'wording_boundary':'Loop work/DMA loss not a unique mechanism fraction.','audit_status':'PASS'},
 {'claim_id':'C2-012','chapter_subsection':'2.7','claim':'SMA-to-fluid actuation has precedent, but an exact SMA-spring/piston envelope remains an engineering characterization task.','source_ids':['S09','S10'],'ieee_reference_numbers':[16,17],'evidence_status':'MODERATE','classification':'direct precedent plus bounded inference','phase4_propositions':['RP014','RP020'],'phase5_mapping':['GAP10','GAP11'],'wording_boundary':'No mechanism novelty from geometry alone.','audit_status':'PASS'},
 {'claim_id':'C2-013','chapter_subsection':'2.10','claim':'The critical weakest link is the mapping from radial reaction to local wire–wire/wire–sleeve normal forces.','source_ids':['S02','S03','S18'],'ieee_reference_numbers':[3,4,5],'evidence_status':'NOT_ESTABLISHED for MP1-R','classification':'inference bounded by evidence','phase4_propositions':['RP016','RP017'],'phase5_mapping':['GAP02','GAP03'],'wording_boundary':'Keep as live uncertainty.','audit_status':'PASS'},
 {'claim_id':'C2-014','chapter_subsection':'2.12','claim':'The approved contribution is pressure-conditioned TiNi-bundle bending characterization with a locked conventional model-discrimination baseline.','source_ids':[],'ieee_reference_numbers':[],'evidence_status':'Phase 5 boundary','classification':'authorized synthesis','phase4_propositions':[],'phase5_mapping':['CONTRIB01','CONTRIB02'],'wording_boundary':'No scientific knowledge-gap or first-ever claim.','audit_status':'PASS'},
]
trace_path=ROOT/'outputs/plans/MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY_2026-10-02.json'
trace_path.parent.mkdir(parents=True, exist_ok=True)
trace_doc={
 'schema_version':'1.0','artifact_type':'MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY','date':'2026-10-02','chapter_docx':str(out_docx.relative_to(ROOT)),
 'authority_inputs':[
  'outputs/plans/MP1_R_PHASE_5_PHASE_6_HANDOFF_2026-10-02.json',
  'docs/literature/MP1_R_PHASE_5_RESEARCH_GAP_AND_CONTRIBUTION_ADJUDICATION_2026-10-02.md',
  'docs/literature/MP1_R_PHASE_4_RECONCILED_SYNTHESIS_2026-10-02.md',
  'docs/literature/MP1_R_PHASE_3_METHODOLOGICAL_APPRAISAL_AND_EVIDENCE_INTEGRITY_2026-10-02.md'],
 'claim_count':len(trace),'claims':trace,'validation':{'all_claims_have_boundary':True,'all_literature_claims_have_source_or_phase_authority':True,'s20_cited':False,'s19_s21_cited':False,'s18_restricted':True,'author_year_citations':False}
}
trace_path.write_text(json.dumps(trace_doc,ensure_ascii=False,indent=2))

reopen_path=ROOT/'outputs/plans/MP1_R_PHASE_6_SOURCE_REOPEN_LOG_2026-10-02.json'
reopen_doc={'schema_version':'1.0','artifact_type':'MP1_R_PHASE_6_SOURCE_REOPEN_LOG','date':'2026-10-02','total_reopened_sources':0,'reopened_source_ids':[],'reopen_entries':[],'basis':'No original papers were reopened; the chapter uses the validated Phase 3–5 evidence boundary only.','validation':{'broad_literature_searches':0,'new_sources_added':0,'original_papers_reopened':0}}
reopen_path.write_text(json.dumps(reopen_doc,ensure_ascii=False,indent=2))

# Count text/citations from all body items.
body_text='\n'.join(payload[0] if kind=='p' else payload for kind,payload in items if kind in ('p','eq','note'))
used_nums=sorted({int(x) for x in re.findall(r'\[(\d+)\]', body_text)})
# Check no citation number exceeds reference list and all refs are cited.
ref_nums=list(range(1,len(refs)+1))
assert used_nums == ref_nums, (used_nums, ref_nums)
assert not re.search(r'\([A-Z][^)]*,\s*20\d\d\)', body_text)
assert 'S20' not in body_text and 'S19' not in body_text and 'S21' not in body_text
assert 'first' not in body_text.lower()  # no English novelty claim in Vietnamese body

# Save generation metrics for the drafting report.
metrics={'chapter_sections':12,'in_text_citations':len(re.findall(r'\[(?:\d+)(?:[–,-]\d+)*\]',body_text)), 'unique_references':len(refs),'body_characters':len(body_text),'body_words':len(body_text.split()),'reference_order':ref_order}
(ROOT/'outputs/plans/MP1_R_PHASE_6_DRAFT_METRICS.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2))
print(json.dumps({'docx':str(out_docx),'traceability':str(trace_path),'reopen_log':str(reopen_path),'metrics':metrics},ensure_ascii=False,indent=2))
