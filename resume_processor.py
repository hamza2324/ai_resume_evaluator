import pdfplumber
from docx import Document

def extract_text(filepath):
    """
    Extract text from PDF or DOCX resume
    """
    if filepath.endswith('.pdf'):
        text = ''
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
        return text
    elif filepath.endswith('.docx'):
        doc = Document(filepath)
        return '\n'.join([para.text for para in doc.paragraphs])
    else:
        return ''
