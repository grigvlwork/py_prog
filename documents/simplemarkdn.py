from docx import Document

def markdown_to_docx(text):
    doc = Document()
    text_list = text.split('\n')
    for paragraph in text_list:
        
    doc.save('res.docx')

