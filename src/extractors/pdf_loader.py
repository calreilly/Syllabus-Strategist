import pypdf
from pathlib import Path

def load_pdf_text(pdf_path: str) -> str:
    """
    Extracts full text from a PDF file.
    """
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found at {pdf_path}")
    
    reader = pypdf.PdfReader(path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    
    full_text = "\n".join(text)
    return full_text

if __name__ == "__main__":
    # Test with a dummy file if run directly
    print("PDF Loader Utility")
