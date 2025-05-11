import os
import pdfplumber
import docx

def extract_text(file_path, file_bytes):
    ext = file_path.rsplit('.', 1)[-1].lower()
    if ext == "pdf":
        with pdfplumber.open(file_bytes) as pdf:
            return ''.join([p.extract_text() for p in pdf.pages if p.extract_text()])
    elif ext == "docx":
        doc = docx.Document(file_bytes)
        return ' '.join([para.text for para in doc.paragraphs])
    elif ext == "txt":
        return file_bytes.read().decode('utf-8')
    else:
        raise ValueError("Unsupported file type")