from docx import Document # pip install python-docx

def extract_text_with_numbering(docx_file, txt_file):
    doc = Document(docx_file)
    with open(txt_file, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            print(para._element.xml)
            if para.style.name.startswith('List'):
                f.write(f"{para.text}\n")
            else:
                f.write(f"{para.text}\n")

# Usage
extract_text_with_numbering('test.docx', 'output.txt')