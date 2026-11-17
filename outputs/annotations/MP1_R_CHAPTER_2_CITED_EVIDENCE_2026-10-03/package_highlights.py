"""Package checked PDF copies, without changing research/source artifacts."""
import hashlib
import json
import zipfile
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
ARCHIVE = OUT / 'MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip'
REG = json.loads((OUT / 'HIGHLIGHT_REGISTER.json').read_text())
VALIDATION = json.loads((OUT / 'VALIDATION.json').read_text())


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


assert VALIDATION['pdf_sources'] == 18
assert VALIDATION['highlight_annotations_added'] == 92
assert sha(ROOT / REG['chapter_docx_path']) == REG['chapter_docx_sha256']
assert sha(ROOT / REG['claim_traceability_path']) == REG['claim_traceability_sha256']
for src in REG['sources']:
    assert sha(ROOT / src['original_pdf_path']) == src['original_sha256']
    assert sha(ROOT / src['highlighted_pdf_path']) == src['highlighted_sha256']

VALIDATION['visual_checks'] = {
    'status': 'SIX_SELECTED_PAGES_VISUALLY_CHECKED',
    'pages': [
        {'source_work_id':'S03', 'pdf_page':9},
        {'source_work_id':'S07', 'pdf_page':6},
        {'source_work_id':'S22', 'pdf_page':71},
        {'source_work_id':'S04', 'pdf_page':5},
        {'source_work_id':'S01', 'pdf_page':9},
        {'source_work_id':'S09', 'pdf_page':9},
    ],
    'result': 'Selected lines align; underlying text remains readable',
    'all_highlighted_pages_visually_checked': False,
}
(OUT / 'VALIDATION.json').write_text(json.dumps(VALIDATION,ensure_ascii=False,indent=2)+'\n')

REPORT = f'''# Bàn giao — PDF highlight trích dẫn Chương 2 MP1-R

Trạng thái công việc: **COMPLETED**.

Đầu ra gồm **18 bản PDF** chứa **92 vùng tô sáng**, ghi chú tiếng Việt và đối chiếu về mục Chương 2. Đã tiếp tục từ checkpoint ngày 2026-10-03 và bổ sung S01-H07 (kết quả xoắn) cùng S09-H05 (kết quả bơm thực nghiệm).

## File bàn giao

- Gói ZIP: [{ARCHIVE.name}]({ARCHIVE.name}).
- [README.md](README.md): liên kết từng PDF, ý được tô, trang PDF và cách đọc màu.
- [HIGHLIGHT_REGISTER.json](HIGHLIGHT_REGISTER.json): chi tiết 92 vùng tô.
- [CLAIM_SOURCE_MAP.json](CLAIM_SOURCE_MAP.json): 53 mục ý có nguồn, 145 cặp ý–nguồn.
- [VALIDATION.json](VALIDATION.json): kiểm tra PDF và bảo toàn đầu vào.
- `PACKAGE_VALIDATION.json` (lưu riêng bên ngoài ZIP): kết quả kiểm tra ZIP và hash gói bàn giao.

## Cách đọc

Vàng: kết quả/mô tả nguồn. Xanh: phương pháp/mô hình. Cam: giả thiết, phạm vi và giới hạn. Mỗi annotation có ghi chú; mở bảng Comments/Annotations của trình đọc PDF để xem. Số trang là thứ tự trang PDF tính từ 1.

## Kiểm tra

Đã mở lại đủ 18 PDF, kiểm tra đủ 92 annotation mới, bảo toàn số trang và văn bản. Đã xem trực quan sáu trang đại diện, gồm hai trang có phần bổ sung sau checkpoint; không tuyên bố đã xem mọi trang được tô.

Hash của 18 PDF gốc và file traceability Phase 6 không đổi. DOCX Chương 2 giữ nguyên, SHA-256:

`{REG['chapter_docx_sha256']}`

## Ranh giới chứng cứ

Đoạn tổng hợp và suy luận về MP1-R không phải câu kết luận nguyên văn của một bài. Bảng đối chiếu phân biệt các đoạn tìm được cho thành phần phát biểu, bằng chứng nền cộng suy luận, định nghĩa thước đo và hỗ trợ một phần. **11 cặp hàng–nguồn chỉ là bối cảnh cấp bảng**, không trực tiếp chứng minh riêng hàng tương ứng. Không tạo highlight không liên quan để ép độ phủ.

Không thay đổi nội dung khoa học, không thêm nguồn, không tìm kiếm tài liệu và không thực hiện Phase 7. Công việc hoàn tất ở việc tô sáng và bàn giao tài liệu.
'''
(OUT / 'DELIVERY_REPORT.md').write_text(REPORT)

files = [OUT / 'README.md', OUT / 'DELIVERY_REPORT.md',
         OUT / 'HIGHLIGHT_REGISTER.json', OUT / 'CLAIM_SOURCE_MAP.json',
         OUT / 'VALIDATION.json', OUT / 'inputs.json', OUT / 'curated_passages.json']
files += sorted((OUT / 'pdf').glob('*.pdf'))
assert len(files) == 25
with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in files:
        z.write(p, p.relative_to(OUT).as_posix())
with zipfile.ZipFile(ARCHIVE) as z:
    assert z.testzip() is None
    names = z.namelist()
    assert len([x for x in names if x.endswith('.pdf')]) == 18
    assert set(names) == {p.relative_to(OUT).as_posix() for p in files}
    for p in files:
        assert hashlib.sha256(z.read(p.relative_to(OUT).as_posix())).hexdigest() == sha(p)

package_check = {
    'schema_version':'1.0', 'status':'PASS',
    'archive_path':str(ARCHIVE.relative_to(ROOT)), 'archive_sha256':sha(ARCHIVE),
    'archive_size_bytes':ARCHIVE.stat().st_size, 'file_count':len(files), 'pdf_count':18,
    'highlights':92, 'zip_crc_check':'PASS', 'all_members_match_saved_files':True,
    'original_pdf_files_unchanged':True, 'docx_unchanged':True,
    'scientific_artifacts_modified':False,
    'note':'Package validation is outside the archive to avoid self-referential hashes.',
}
(OUT / 'PACKAGE_VALIDATION.json').write_text(json.dumps(package_check,ensure_ascii=False,indent=2)+'\n')
assert (OUT / 'DELIVERY_REPORT.md').read_text() == REPORT
print(json.dumps(package_check,ensure_ascii=False))
