import os

import fitz
from docx import Document


def extract_text_from_pdf(file_path):
    text_lines = []
    with fitz.open(file_path) as doc:
        for page in doc:
            text_lines.append(page.get_text())
    return "\n".join(text_lines).strip()


def extract_text_from_docx(file_path):
    document = Document(file_path)
    text_lines = [paragraph.text for paragraph in document.paragraphs if paragraph.text.strip()]
    return "\n".join(text_lines).strip()


def extract_text_from_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    if extension == ".pdf":
        return extract_text_from_pdf(file_path)
    if extension == ".docx":
        return extract_text_from_docx(file_path)
    return ""
