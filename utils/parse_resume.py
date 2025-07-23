from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file using pdfminer.six
    """
    try:
        text = extract_text(pdf_file)
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""
