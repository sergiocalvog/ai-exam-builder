import fitz  # PyMuPDF

def extract_text_from_pdf(file_path_or_bytes):
    """
    Extracts text from a PDF file.
    """
    text = ""
    try:
        if isinstance(file_path_or_bytes, bytes):
            doc = fitz.open(stream=file_path_or_bytes, filetype="pdf")
        else:
            doc = fitz.open(file_path_or_bytes)
            
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None
        
    return text.strip()
