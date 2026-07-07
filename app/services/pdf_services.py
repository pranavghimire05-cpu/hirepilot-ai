import fitz

def extract_text_from_pdf(file):
    pdf_bytes = file.file.read()
    document = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
        )
    text = ""
    for page in document:
        text += page.get_text()
    return{
        "pages": len(document),
        "text": text
    }