"""
Lê texto de um arquivo PDF, linha a linha.
"""

import fitz  # pip install pymupdf

with fitz.open("file-sample_150kB.pdf") as doc:
    for page in doc:
        text = page.get_text()
        print(text)
