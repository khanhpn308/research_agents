"""Curated source passages for Chapter 2; no changes to scientific artifacts."""
import json
from collections import defaultdict
from pathlib import Path

OUT = Path(__file__).resolve().parent
CACHE = json.loads((OUT / 'pdf_text_geometry.json').read_text())
UNITS = []
COUNTERS = defaultdict(int)


def add(sid, page, spans, role, idea, claims, boundary):
    """spans: (block_id, start_line, exclusive_end), None end = all remaining."""
    COUNTERS[sid] += 1
    blocks = {b['block_id']: b for b in CACHE[sid]['pages'][page-1]['blocks']}
    selected = []
    for block_id, start, end in spans:
        block = blocks[block_id]
        end = len(block['lines']) if end is None else end
        assert 0 <= start < end <= len(block['lines']), (sid, page, block_id, start, end)
        selected.append({'block_id': block_id, 'line_start': start, 'line_end_exclusive': end})
    UNITS.append({
        'highlight_id': f'{sid}-H{COUNTERS[sid]:02}', 'source_work_id': sid,
        'pdf_page': page, 'selections': selected, 'role': role,
        'idea_vi': idea, 'claim_ids': [f'CH2C{i:03}' for i in claims],
        'wording_boundary_vi': boundary,
    })


# Yellow: reported findings/descriptions. Blue: methods/models. Orange: scope/assumptions.
add('S01', 4, [(1,4,None)], 'LIMITATION_SCOPE',
    'Vật liệu kraft, hemp, nylon; đường kính, cách xếp và trượt theo chu vi phụ thuộc cấu hình.',
    [5,10], 'Không phải bằng chứng TiNi; lựa chọn hình học và vật liệu giới hạn phép chuyển kết quả.')
add('S01', 5, [(4,0,5)], 'METHOD_MODEL',
    'Bao kín, đường chân không và dây; giam giữ được điều chỉnh bằng áp suất chân không.',
    [4,5,7,10,55], 'Áp suất điều khiển hệ giam giữ đã thử; không cho lực pháp tuyến cục bộ MP1-R.')
add('S01', 5, [(5,0,10)], 'METHOD_MODEL',
    'Mô hình giới hạn dây độc lập khi nhả chân không và dầm chung khi giam giữ.',
    [5,10], 'Hai trạng thái là giả thiết mô hình, không phải phép đo độc lập từng tiếp diện.')
add('S01', 7, [(3,0,13)], 'METHOD_MODEL',
    'Thử uốn ba điểm và xoắn để đánh giá kết cấu wire-jamming.',
    [5,10], 'Đại lượng và điều kiện gá của nghiên cứu gốc phải được giữ khi so sánh.')
add('S01', 8, [(2,0,15)], 'FINDING',
    'Áp suất chân không và chiều dày làm thay đổi đường lực–độ võng, điểm chuyển tiếp và tỷ số F/δ.',
    [4,5,7,10,55], 'Kết quả riêng của bao dây/sợi không kim loại; không suy ra quan hệ áp suất–độ cứng phổ quát.')
add('S01', 9, [(2,0,None)], 'METHOD_MODEL',
    'Diễn giải ba miền trước trượt, chuyển tiếp và sau trượt trên đường lực–độ võng.',
    [5,10], 'Đây là đường khái niệm để diễn giải đáp ứng; không chứng minh trường trượt cục bộ MP1-R.')
add('S01', 9, [(3,0,19)], 'FINDING',
    'Phép xoắn và so sánh mô men–góc quay cho thấy đáp ứng phụ thuộc trạng thái giam giữ, vật liệu và chiều dày.',
    [5,10], 'Kết quả xoắn của kết cấu wire-jamming gốc; không phải bằng chứng TiNi hoặc lực tiếp xúc cục bộ MP1-R.')

add('S02', 2, [(8,0,None),(10,0,None)], 'METHOD_MODEL',
    'Túi cao su bơm phồng truyền lực đến hạt, trong khi ống vải ngoài hạn chế giãn nở.',
    [4,7,11,19,55,56,57,58,59], 'Đường truyền lực của kiến trúc hạt–túi–ống; chưa xác định lực pháp tuyến dây–dây.')
add('S02', 3, [(10,0,None)], 'FINDING',
    'So sánh uốn túi riêng, giam giữ áp suất âm và giam giữ áp suất dương.',
    [4,7,11,55], 'Chỉ so sánh trong các mẫu và điều kiện thí nghiệm của bài báo.')
add('S02', 4, [(4,0,None),(5,0,None)], 'FINDING',
    'Độ cứng suy từ đáp ứng uốn tăng theo áp suất trong phạm vi thí nghiệm.',
    [4,7,11,55], 'Tác giả báo cáo quan hệ gần tỷ lệ trong hệ hạt đã thử; không phải định luật cho MP1-R.')
add('S02', 4, [(9,0,None)], 'LIMITATION_SCOPE',
    'Các mẫu, vỏ ngoài và điều kiện đóng gói được kiểm soát trong phép khảo sát hình học.',
    [7,11,58], 'Phản ứng áp suất phụ thuộc hình học, ống bao và vật liệu hạt.')
add('S02', 4, [(10,0,None)], 'LIMITATION_SCOPE',
    'Tác giả giải thích khả năng suy giảm truyền lực tới các hạt ngoài.',
    [19,56,58,59], 'Giải thích suy luận của tác giả; không phải đo trực tiếp trường lực tiếp xúc.')

add('S03', 3, [(6,0,None),(7,0,None),(8,0,None)], 'METHOD_MODEL',
    'Ba trạng thái dính, chuyển tiếp trượt một phần và trượt toàn phần của bó sợi.',
    [4,8,12,22,31,36,44,52,56,61,62], 'Trạng thái cơ học theo mô hình; phép đo tổng thể không tự xác định trượt cục bộ.')
add('S03', 3, [(9,0,None)], 'METHOD_MODEL',
    'Ngưỡng ứng suất ma sát μp và điều kiện bắt đầu trượt theo mô hình Euler–Bernoulli.',
    [17,18,19,20,31,44,52,56,60,61], 'Dạng ứng suất μp là giả thiết truyền áp của mô hình; không đồng nhất p với N tại tiếp xúc dây.')
add('S03', 5, [(19,0,None)], 'LIMITATION_SCOPE',
    'Túi áp suất nén bó sợi về phía thành phản lực; tiết diện hữu hiệu được xấp xỉ.',
    [8,12,19,20,56,57,58,59], 'Phản lực, phần tiết diện bị nén và tham số hình học phụ thuộc kiến trúc.')
add('S03', 7, [(4,0,None)], 'METHOD_MODEL',
    'Mẫu chuỗi gồm 700 sợi nylon và túi chịu áp suất dương.',
    [4,8,12,55], 'Không phải TiNi; chỉ một cấu hình sợi và prototype trong phép kiểm chứng.')
add('S03', 7, [(12,0,None)], 'METHOD_MODEL',
    'Hồi quy tuyến tính từng đoạn đường F–δ để xác định tải chuyển tiếp và độ cứng các nhánh.',
    [8,12,24,25,30,36], 'Chỉ số chuyển tiếp toàn cục; không phải phép đo trực tiếp thời điểm trượt từng tiếp diện.')
add('S03', 9, [(6,0,None)], 'LIMITATION_SCOPE',
    'Mô đun hiệu dụng E được nhận dạng từ thí nghiệm uốn ở p = 0, không từ thử vật liệu độc lập.',
    [8,12,20,24,25,26,30,52], 'E đã hiệu chỉnh ở cấp hệ; không xem việc dùng lại dữ liệu nhận dạng là kiểm chứng độc lập.')
add('S03', 9, [(9,0,None)], 'LIMITATION_SCOPE',
    'Hệ số ma sát hiệu dụng được nhận dạng từ hồi quy tải trượt toàn phần theo áp suất.',
    [8,12,17,18,19,20,56,59,60], 'μ là tham số hiệu dụng theo mô hình; không tách độc lập μ và trường lực N.')
add('S03', 11, [(5,0,None)], 'FINDING',
    'Tải chuyển tiếp và độ cứng miền trượt tăng theo áp suất; miền dính tương đối ít nhạy áp suất.',
    [4,8,12,22,24,25,26,30,31,44,52,55,56,62], 'Kết luận chỉ cho prototype và miền áp suất đã thử; không áp dụng nguyên trạng cho TiNi.')
add('S03', 11, [(6,0,None)], 'LIMITATION_SCOPE',
    'Luật chuyển tiếp hiện tượng luận, một prototype và mô đun E nhận dạng là các giới hạn của bài.',
    [8,12,20,31,36,44,52,55,56,59,62], 'Giới hạn tính tổng quát và nhận dạng; không phải bằng chứng mô hình thông thường đã thất bại.')
add('S03', 3, [(25,0,None)], 'METHOD_MODEL',
    'Mô men M, mô đun hiệu dụng E và mô men quán tính tương đương liên hệ với bán kính cong của bó sợi.',
    [24,26,30], 'Quan hệ M–độ cong trong mô hình uốn; khác độ dốc lực–độ võng ở một gá cụ thể.')

add('S15', 1, [(29,0,None)], 'LIMITATION_SCOPE',
    'Tổng quan giới hạn ở laminar jamming; loại trừ particle jamming và fiber jamming.',
    [6], 'Chỉ dùng làm bối cảnh tổng quan, không thay thế bằng chứng thực nghiệm sơ cấp.')
add('S15', 3, [(5,0,None)], 'FINDING',
    'Phân loại cơ chế biến đổi độ cứng: ma sát, cản trở cơ học và nhóm khác.',
    [6], 'Phân loại của bài tổng quan kết cấu nhiều lớp; không phải một thí nghiệm MP1-R.')

add('S18', 2, [(4,0,None)], 'LIMITATION_SCOPE',
    'Giả thiết liên tục cần lớp đủ mỏng so với chiều cao và số lớp đủ lớn.',
    [9,13,21,31,44,52,55,69], 'Mô hình tương tự dầm nhiều lớp; không tự chuyển sang bó dây TiNi.')
add('S18', 2, [(9,0,None)], 'METHOD_MODEL',
    'Ứng suất dọc trục σ và ứng suất cắt τ trong mô hình dầm nhiều lớp.',
    [9,13,21,52], 'Ứng suất dọc trục khác lực pháp tuyến liên lớp; không đồng nhất hai đại lượng.')
add('S18', 3, [(2,0,None)], 'METHOD_MODEL',
    'Bỏ qua biến dạng pháp tuyến liên lớp; ngưỡng Coulomb μp dùng áp suất chân không.',
    [9,13,17,18,19,21,22,31,36,44,52,56,58,59,60,61], 'Layer-jamming hút chân không; đây là giả thiết mô hình, không bằng chứng fiber-jamming áp suất dương.')
add('S18', 8, [(7,0,8)], 'METHOD_MODEL',
    'Mẫu màng PVC chứa 20 lớp PVC, gá dầm và đo tải–độ võng.',
    [9,13,21,44,52,55,56,58], 'Bằng chứng cơ học tương tự trong cấu hình PVC, không phải kiểm chứng trực tiếp MP1-R.')
add('S18', 8, [(7,8,None)], 'FINDING',
    'Đường tải–độ võng tính toán được so với thực nghiệm ở một mức áp suất 60 kPa.',
    [9,13,21,22,31,44,52,55,56,62,69], 'Áp suất chân không theo định nghĩa của bài; phù hợp trong điều kiện mẫu đã thử.')
add('S18', 8, [(4,0,None),(8,0,None)], 'LIMITATION_SCOPE',
    'Bỏ qua ứng suất pháp tuyến theo chiều cao và hiệu ứng biên gây sai khác vùng trượt.',
    [9,13,21,31,36,44,52,56,59,61,62,69], 'Giới hạn liên tục và biên; không chứng minh lực pháp tuyến cục bộ của MP1-R.')
add('S18', 9, [(2,0,None)], 'LIMITATION_SCOPE',
    'Mô hình phù hợp hơn xa biên và trong miền trượt một phần; FEA được đề nghị ở trạng thái cực hạn.',
    [9,13,22,31,44,52,55,62,69], 'Mức phù hợp mô hình có giới hạn; chưa kiểm tra dự đoán trên đường tải dành riêng của MP1-R.')
add('S18', 3, [(1,0,8)], 'METHOD_MODEL',
    'Đoạn nối từ trang trước định nghĩa τ là ma sát liên lớp; biến dạng kéo dọc lớp và trượt liên lớp khác nhau.',
    [9,13,21,52], 'Ứng suất dọc lớp và ma sát liên lớp không phải cùng một đại lượng.')

add('S06', 3, [(8,0,None)], 'LIMITATION_SCOPE',
    'Mô hình dây cáp ngắn được tuyến tính hóa trong giả thiết biến dạng vô cùng bé.',
    [22,31,44,52,55,56,61,69], 'Mô hình giới hạn đáp ứng cơ học; không phải luật ma sát/chuyển pha mới cho TiNi.')
add('S06', 4, [(57,0,14),(59,2,None)], 'METHOD_MODEL',
    'Giới hạn dính hoàn toàn, dính một phần và trượt toàn phần; dính nguyên khối có thể quá cứng.',
    [22,31,44,52,55,56,61,62,69], 'Các trạng thái lý tưởng có giả thiết chuyển động dây riêng; phải kiểm chứng trước khi chuyển kiến trúc.')
add('S06', 6, [(4,0,None),(6,0,9)], 'METHOD_MODEL',
    'Chu kỳ lực–chuyển vị, nhánh dùng nhận dạng độ cứng nhỏ nhất/lớn nhất và ảnh hưởng ổn định chu kỳ.',
    [22,24,25,28,30,31,55,62], 'Độ cứng theo lực–chuyển vị ở điều kiện gá đã nêu; công vòng trễ vẫn là đại lượng tổng hợp.')
add('S06', 8, [(35,0,None)], 'LIMITATION_SCOPE',
    'Dây cáp thử là thép AISI 304 và có bước xoắn đo trên mẫu.',
    [22,44,52,55], 'Không phải thử nghiệm TiNi hoặc bó dây chịu áp suất.')
add('S06', 8, [(68,0,None),(69,0,None)], 'FINDING',
    'So sánh thực nghiệm: trượt toàn phần dự đoán giới hạn mềm; dính một phần phù hợp giới hạn cứng hơn.',
    [22,24,25,26,31,44,52,55,56,62,69], 'Dính hoàn toàn dự đoán quá cao; kiểm chứng giới hạn độ cứng trong mẫu thép đã thử.')
add('S06', 9, [(4,0,None)], 'LIMITATION_SCOPE',
    'Kết quả phụ thuộc chiều dài và điều kiện biên, đặc biệt khi mẫu ngắn hơn bước xoắn.',
    [22,31,44,52,55,56,61,62,69], 'Hiệu ứng biên giới hạn phép chuyển mô hình; không được xem hình học khác là cơ chế mới.')

add('V-W02', 3, [(1,0,14)], 'METHOD_MODEL',
    'Mô phỏng cáp SMA bằng mô hình vật liệu Souza và UMAT; so sánh với dữ liệu sẵn có.',
    [23,39,42,44,52,55,69], 'Nghiên cứu số về cáp chịu tải dọc trục; không phải thử nghiệm bó TiNi chịu áp suất.')
add('V-W02', 4, [(20,0,None)], 'METHOD_MODEL',
    'Mô hình thép có tương tác tiếp xúc pháp tuyến và tiếp tuyến, với ma sát được ấn định.',
    [23,39,42,44,52,55,69], 'Lớp kiểm chứng cáp thép khác mô phỏng SMA; không suy lực N từ chỉ tên vật liệu.')
add('V-W02', 5, [(16,0,None)], 'METHOD_MODEL',
    'Mô hình SMA dùng Souza/UMAT và hệ số ma sát dây khoảng 0,115.',
    [23,39,42,44,52,55,69], 'Cho thấy chuyển pha và tiếp xúc cùng có thể được đưa vào mô hình thông thường; chưa phân bổ tiêu tán MP1-R.')
add('V-W02', 5, [(25,0,12)], 'FINDING',
    'Mô phỏng siêu đàn hồi được so với dữ liệu thực nghiệm cáp; báo cáo sai khác có giới hạn.',
    [23,39,42,44,52,55,69], 'Dữ liệu thực nghiệm dùng đối chiếu từ nghiên cứu trước; kết quả không chứng minh luật ghép áp suất mới.')

add('S13', 1, [(13,0,None)], 'METHOD_MODEL',
    'Mẫu vi sợi bện và bện kép; DMA đo giảm chấn và mô đun theo nhiệt độ/tần số.',
    [24,27,30,40,42,44,68], 'Đại lượng DMA không phải độ cứng uốn tĩnh hoặc công ma sát tại từng tiếp diện.')
add('S13', 4, [(2,0,21)], 'FINDING',
    'Đáp ứng mô đun và tanδ của vi sợi bện trong miền nhiệt độ khảo sát; kiểm tra chu kỳ nhiệt.',
    [24,27,30,40,42,44,68], 'Giảm chấn tổng hợp trong cấu trúc bện; không chứng minh chuyển pha chi phối vòng trễ MP1-R.')
add('S13', 4, [(3,0,None)], 'LIMITATION_SCOPE',
    'Tác giả diễn giải giảm chấn bằng biến dạng cấu trúc, chuyển pha cục bộ và vi trượt tại tiếp xúc.',
    [27,28,30,40,42,44,68], 'Diễn giải cơ chế tổng hợp; không có phép phân tách định lượng độc lập các tỷ phần cho MP1-R.')
add('S13', 4, [(4,0,None)], 'FINDING',
    'Số dây và mật độ điểm tiếp xúc được so sánh với mức giảm chấn của các vi sợi bện.',
    [27,40,42,44], 'Quan hệ trong mẫu vi sợi bện đã thử; không phải khảo sát áp suất của MP1-R.')

add('S17', 2, [(17,0,None)], 'LIMITATION_SCOPE',
    'Bài tổng quan cảnh báo các giá trị độ cứng ở nghiên cứu khác nhau có thể khác thứ nguyên.',
    [24,25,26,27,28,30], 'Chỉ hỗ trợ thận trọng về đại lượng/đơn vị; không chứng minh toàn bộ công thức trong bảng Chương 2.')

add('S04', 2, [(7,0,None)], 'METHOD_MODEL',
    'Các dây khung, ống cao su và lò xo SMA quấn ngoài có vai trò cơ học khác nhau.',
    [32,33,34,48], 'Lò xo SMA điều biến lực ép, các dây chịu lực là phần kết cấu; không phải piston MP1-R.')
add('S04', 3, [(1,3,28)], 'METHOD_MODEL',
    'Thay đổi trạng thái nhiệt của lò xo SMA làm thay đổi lực siết theo chu vi.',
    [33,48,60], 'Cơ chế tại tiếp diện dây–cao su của robot gốc; không đồng nhất với truyền áp suất chất lưu.')
add('S04', 5, [(11,0,None)], 'METHOD_MODEL',
    'Kéo một dây trong ống cao su; bảy dây còn lại được cố định để đo lực cản trượt.',
    [29,32,33,34,35,48,60,67], 'Lực cản được đo; phép thử không tách riêng hệ số ma sát và lực pháp tuyến.')
add('S04', 5, [(9,0,None)], 'LIMITATION_SCOPE',
    'Thử nghiệm điều chỉnh nhiệt độ lò xo và phân biệt trạng thái martensite/austenite.',
    [33,48], 'Trạng thái được nói ở đây là lò xo dẫn động, không phải xác nhận chuyển pha của dây kết cấu MP1-R.')
add('S04', 6, [(3,0,10)], 'FINDING',
    'Lực cản trượt đo được cao hơn khi lò xo ở trạng thái austenite, phụ thuộc đường kính khung.',
    [29,32,33,34,35,48,60,67], 'So sánh lực cản tiếp diện đã được kích thích; không chứng minh wire–wire chi phối MP1-R.')
add('S04', 6, [(7,9,23)], 'FINDING',
    'Phép uốn robot dùng độ dốc lực cản–chuyển vị; so sánh các đường kính và trạng thái lò xo.',
    [33,48,62], 'Đáp ứng tổng thể của robot; chưa phải phân bổ cơ chế tiêu tán và N cục bộ.')
add('S04', 7, [(3,0,None)], 'FINDING',
    'Mô hình độ cứng uốn từ công ma sát được so với thử nghiệm của robot.',
    [33,48,62], 'Công ma sát dùng dữ liệu phép kéo riêng; mức phù hợp trong cấu hình và miền tải đó.')
add('S04', 7, [(9,0,15)], 'LIMITATION_SCOPE',
    'Giới hạn làm nguội, điều khiển nhiệt và giả thiết cung tròn khi tính chiều dài trượt.',
    [33,35,48,62,67], 'Không coi mô hình trượt toàn cục là đo trực tiếp từng tiếp diện hoặc luật ghép mới.')

add('S22', 66, [(18,0,None),(19,0,None),(20,0,None),(21,0,None),(22,0,None),(23,0,None),(24,0,None)], 'METHOD_MODEL',
    'Mẫu cáp cắt chọn lọc để cô lập trượt giữa lớp thứ nhất–thứ hai hoặc thứ hai–thứ ba.',
    [29,32,34,35,67], 'Đây là phép thử giữa các lớp cáp; không phải phép thử dây–ống bao hoặc đo mọi tiếp xúc.')
add('S22', 66, [(25,0,None),(26,0,None),(27,0,None)], 'METHOD_MODEL',
    'Nén các mẫu để gây trượt liên lớp; máy Instron ghi lực ma sát tĩnh.',
    [29,32,34,35,67], 'Đại lượng quan sát là lực cản trượt, không phải lực pháp tuyến đo trực tiếp.')
add('S22', 71, [(14,0,None),(15,0,None),(23,0,None),(24,0,None),(25,0,None),(26,0,None)], 'LIMITATION_SCOPE',
    'Áp lực và lực pháp tuyến suy từ lực ma sát, hệ số ma sát tham khảo và diện tích tiếp xúc giả định.',
    [29,34,35,59,67], 'Hệ số 0,74 mượn từ nguồn tham khảo; không xem bảng N là đo trực tiếp lực tiếp xúc.')
add('S22', 74, [(11,0,None),(12,0,None),(13,0,None),(14,0,None),(15,0,None),(16,0,None),(17,0,None),(18,0,None)], 'LIMITATION_SCOPE',
    'Tác giả nêu vết xước, vết lõm, bước xoắn và xấp xỉ diện tích gây sai số suy áp lực.',
    [29,34,35,59,67], 'Giới hạn suy lực N từ lực cản là bộ phận của bằng chứng; không được bỏ khi chuyển kết quả.')
add('S22', 65, [(18,0,None),(19,0,None),(20,0,None)], 'LIMITATION_SCOPE',
    'Tác giả đề nghị thí nghiệm chính xác hơn và dùng phim chỉ thị áp lực để xác định áp lực liên lớp.',
    [34,35,59,67], 'Chưa thiết lập một phép đo độc lập trường lực pháp tuyến của bó dây MP1-R.')
add('S22', 67, [(5,0,1)], 'METHOD_MODEL',
    'Đoạn nối từ trang trước: bộ ghi vẽ đường lực của phép thử trượt liên lớp.',
    [29,32,34,35,67], 'Đọc cùng trang PDF 66; lực ghi là lực cản trượt, không phải phép đo N độc lập.')

add('S05a', 2, [(1,0,None)], 'METHOD_MODEL',
    'Chuyển pha martensite thuận nghịch do nhiệt hoặc ứng suất; trạng thái phụ thuộc vật liệu và xử lý nhiệt–cơ.',
    [37,38,42,44,55,68], 'Danh tính TiNi không tự xác nhận chuyển pha hoạt động trong miền uốn thực tế.')
add('S05a', 6, [(0,0,14)], 'METHOD_MODEL',
    'Thử kéo dọc trục với đầu kẹp chống xoay; đo lực, độ giãn và mô men.',
    [38,42,44,55,68], 'Thử kéo cáp khác uốn bó dây chịu áp suất; điều kiện biên cần được giữ khi diễn giải.')
add('S05a', 6, [(1,0,12),(3,0,3)], 'METHOD_MODEL',
    'Đo nhiệt hồng ngoại/cặp nhiệt điện và đo trường biến dạng bằng DIC.',
    [38,42,44,55,68], 'Đây là quan sát trạng thái trong phép thử gốc; không phải dữ liệu cùng lô TiNi của MP1-R.')
add('S05a', 9, [(7,0,4)], 'FINDING',
    'Trường nhiệt và biến dạng của cáp 7×7 cho thấy mặt chuyển pha lan truyền.',
    [37,38,42,44,55,68], 'Chuyển pha được nhận diện trong miền thử kéo gần đẳng nhiệt đã khảo sát.')
add('S05a', 17, [(1,0,15),(2,0,None),(3,0,7)], 'FINDING',
    'Cáp 7×7 và 1×27 có đáp ứng gần đẳng nhiệt khác nhau; hoạt động chuyển pha và front phụ thuộc cấu trúc.',
    [37,38,42,44,55,68], 'Không chuyển kết luận kéo cáp sang giả định chuyển pha chi phối vòng trễ uốn MP1-R.')

add('S05b', 3, [(4,0,None)], 'LIMITATION_SCOPE',
    'Phân rã cáp thành mẫu thành phần; bài chủ yếu thực nghiệm và mô tả, chưa xây dựng mô hình kết cấu chi tiết.',
    [37,38,42,44,55,68], 'Bằng chứng mẫu thành phần không phải phép phân chia ma sát/chuyển pha cho mọi cấu hình.')
add('S05b', 7, [(10,0,7)], 'FINDING',
    'So sánh dây lõi, tao lõi 1×7 và cáp 7×7 ở tốc độ gần đẳng nhiệt.',
    [37,38,42,44,55,68], 'Giá trị vật liệu/cáp trong phép kéo kiểm soát; chưa biết trạng thái cùng lô dây MP1-R.')
add('S05b', 33, [(2,0,4)], 'LIMITATION_SCOPE',
    'Hiệu đáp ứng giữa mẫu thành phần có ích nhưng không thay thế phép đo trực tiếp và có thể khuếch đại sai số.',
    [38,42,44,68], 'Phép trừ đáp ứng không mặc nhiên phân tách được chuyển pha và ma sát.')
add('S05b', 33, [(6,0,16)], 'FINDING',
    'Các mẫu thành phần có đáp ứng siêu đàn hồi và độ mềm phụ thuộc góc xoắn, cấu trúc lớp.',
    [37,38,42,44,55,68], 'Kết quả thực nghiệm vật liệu phụ thuộc kiến trúc và miền tải; không suy hiện tượng MP1-R khi chưa đo.')
add('S05b', 34, [(1,3,6)], 'LIMITATION_SCOPE',
    'Trong các phép thử được báo cáo, trượt tương đối giữa dây ít hoặc không đáng kể ngay cả ở biến dạng lớn.',
    [37,38,42,44,55,68], 'Bằng chứng cụ thể cho phương án vật liệu; không giả định mọi cáp TiNi đều trượt hoặc đều không trượt.')

add('S09', 2, [(10,0,13),(11,0,None)], 'METHOD_MODEL',
    'Dây SMA điều khiển đòn bẩy và buồng bơm; chất lưu nóng/lạnh tạo chu kỳ co–giãn.',
    [37,46,50,55], 'Tiền lệ SMA–chất lưu; khác lò xo SMA–piston và không kiểm chứng nguồn áp suất MP1-R.')
add('S09', 3, [(3,0,10),(4,0,None)], 'METHOD_MODEL',
    'Các tham số nhiệt, dây, buồng bơm và áp suất ảnh hưởng lực, thời gian và đầu ra chất lưu.',
    [37,46,50,55], 'Nguồn áp suất cần khảo sát ở tải kết nối; không chỉ theo đặc tính không tải.')
add('S09', 5, [(3,0,None),(5,0,None)], 'METHOD_MODEL',
    'Mô hình động ghép chuyển pha/đường nhiệt của SMA với mạch chất lưu và buồng bơm.',
    [37,46,50,55], 'Mô hình của bơm gốc; không phải luật truyền áp suất–tiếp xúc của MP1-R.')
add('S09', 8, [(12,0,None)], 'METHOD_MODEL',
    'Prototype thực dùng để so sánh thí nghiệm với mô phỏng, có tái tuần hoàn và cấp nhiệt liên tục.',
    [46,50,55], 'Chứng minh có triển khai bơm SMA gốc; không chứng minh cấu hình MP1-R tích hợp đã hoạt động.')
add('S09', 9, [(9,0,None)], 'FINDING',
    'Kết quả bơm thực nghiệm được so với mô phỏng và có đầu ra chất lưu khi hỗ trợ gia nhiệt điện.',
    [46,50,55], 'Tiền lệ SMA–chất lưu ở điều kiện thử của bơm gốc; không xác nhận miền tải kết nối của nguồn lò xo–piston MP1-R.')

add('S07', 1, [(27,0,None),(28,0,None),(29,0,None),(30,0,None),(31,0,None),(32,0,None),(33,0,None),(34,0,None),(35,0,None),(36,0,None)], 'METHOD_MODEL',
    'Tóm tắt tiếng Anh: UMAT SMA xét biến thiên mô đun trong chuyển pha, mô phỏng cáp siêu đàn hồi và so sánh dữ liệu.',
    [39,42,44,52,69], 'Tóm tắt được đối chiếu với các đoạn phương pháp/giới hạn trong thân bài tiếng Trung; không dùng riêng làm bằng chứng cơ học.')
add('S07', 4, [(84,0,None)], 'METHOD_MODEL',
    'Thân bài dùng tiếp xúc trơn giữa các tao và mô hình ràng buộc đầu cáp.',
    [39,42,44,52,69], 'Tiếp xúc trơn trong mô hình Kang khác mô hình tiếp xúc ma sát của Vahidi.')
add('S07', 5, [(6,0,None)], 'METHOD_MODEL',
    'Tham số NiTi có mô đun austenite và martensite riêng; trạng thái vật liệu được đưa vào mô hình.',
    [39,42,44,52,69], 'Giá trị tham số nguồn gốc theo tài liệu của tác giả; không mặc định cho cùng lô TiNi MP1-R.')
add('S07', 6, [(24,0,None),(25,0,None)], 'LIMITATION_SCOPE',
    'Thân bài nêu bỏ qua ma sát giữa các tao để bảo đảm hội tụ gây sai khác ứng suất với thí nghiệm.',
    [39,42,44,52,69], 'Hạn chế mô hình cụ thể; không phải chứng cứ cần luật cấu thành mới cho MP1-R.')

add('S11', 2, [(6,0,8)], 'LIMITATION_SCOPE',
    'Bộ hấp thụ dùng cáp hỗn hợp NiTiNOL–thép; trạng thái siêu đàn hồi ở nhiệt độ môi trường đã nêu.',
    [40,42,44], 'Không phải bó dây TiNi thuần chịu giam giữ bằng áp suất.')
add('S11', 4, [(3,0,None)], 'METHOD_MODEL',
    'Mô hình Bouc–Wen sửa đổi cộng phần đàn hồi tuyến tính và lực trễ.',
    [40,42,44], 'Mô hình hiện tượng luận của đáp ứng tổng hợp; không nhận dạng riêng tỷ phần ma sát/chuyển pha.')
add('S11', 4, [(20,0,None)], 'FINDING',
    'Chu kỳ thí nghiệm có thắt vòng trễ ở biên độ cao; tác giả diễn giải bằng ma sát giữa dây và chuyển pha NiTiNOL.',
    [40,42,44], 'Sự đồng tồn tại và diễn giải trong cáp hỗn hợp không chứng minh cơ chế chi phối MP1-R.')

add('S12', 5, [(4,0,None)], 'LIMITATION_SCOPE',
    'Thử kéo vật lý để xác định tính chất dây thép dùng trong mô hình.',
    [41,42,52,55,69], 'Không mô tả thử dây thép là thực nghiệm TiNi.')
add('S12', 6, [(2,0,None)], 'LIMITATION_SCOPE',
    'Cấu trúc thép được đưa lên bàn rung trong phần thí nghiệm.',
    [41,42,52,55,69], 'Phần thực nghiệm vật lý này là thép; phần SMA cần đọc cùng phương pháp mô phỏng.')
add('S12', 10, [(10,0,10)], 'METHOD_MODEL',
    'ABAQUS dùng tiếp xúc mặt–mặt, ma sát penalty, hard contact và các ràng buộc đầu cáp.',
    [41,42,52,55,69], 'Các hệ số và ràng buộc là đầu vào mô hình; không phải đo tiếp xúc cục bộ MP1-R.')
add('S12', 13, [(5,0,None)], 'LIMITATION_SCOPE',
    'Mô hình cáp SMA được so sánh với dữ liệu số và thực nghiệm của nghiên cứu trước.',
    [41,42,52,55,69], 'Đối chiếu dữ liệu trước không phải thí nghiệm SMA mới trong công trình này.')

add('S10', 4, [(2,0,None)], 'METHOD_MODEL',
    'Áp suất dương để uốn; áp suất âm để giam giữ hạt và điều chỉnh độ cứng.',
    [47,50,57], 'Hai chức năng áp suất riêng trong vi bơm ECF; không phải nguồn dẫn động SMA.')
add('S10', 6, [(9,0,None)], 'LIMITATION_SCOPE',
    'Không đo được áp suất/lưu lượng trong actuator đã tích hợp; hiệu chỉnh vi bơm bằng thử riêng không dòng/không tải.',
    [47,50,57], 'Phân biệt áp suất nguồn hiệu chỉnh với áp suất thực gần mẫu; chưa xác nhận tải kết nối MP1-R.')
add('S10', 7, [(4,0,None)], 'METHOD_MODEL',
    'Thử uốn đo lực và độ võng đầu bằng gá công xôn để đánh giá độ cứng chuyển đổi.',
    [47,50], 'Đại lượng uốn tổng thể trong actuator gốc, không đo lực pháp tuyến liên hạt hoặc liên dây.')
add('S10', 8, [(2,0,5)], 'LIMITATION_SCOPE',
    'Bài báo không đo trực tiếp áp suất âm bên trong hệ tích hợp và dùng hiệu chỉnh riêng để chọn điện áp.',
    [47,50,57], 'Không gọi các mức áp suất suy từ hiệu chỉnh là phép đo áp suất gần mẫu trong hệ tích hợp.')
add('S10', 8, [(4,0,None)], 'FINDING',
    'Kết quả uốn của actuator mềm tăng lực cản khi kích hoạt giam giữ hạt bằng áp suất âm.',
    [47,50], 'Tăng lực uốn trong actuator gốc; không chứng minh TiNi, SMA hoặc jamming bằng áp suất dương.')

(OUT / 'curated_passages.json').write_text(json.dumps(UNITS, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'passages': len(UNITS), 'by_source': dict(COUNTERS)}, ensure_ascii=False))
