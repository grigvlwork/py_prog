from docx import Document
import codecs


def markdown_to_docx(text):
    f_in = codecs.open(text, encoding="utf-8")
    doc = Document()
    lines = f_in.readlines()
    f_in.close()
    for line in lines:
        if '<body>' in line:
            begin = lines.index(line) + 1
        if '</body>' in line:
            end = lines.index(line)
    lines = lines[begin:end]
    for line in lines:
        doc.add_paragraph(line)
    doc.save('res.docx')


markdown_to_docx('test01-utf.html')
