import fitz  # PyMuPDF
import config

# INFORMATION
# This file extracts the text from the PDF per page and
# returns a list that contains the chunks for each page at the matching index.

# -------------------------INFORMATION-------------------------- #
# This script searches in the embeddings for chunks of the PDF
# similar to the prompt given by the user.
# -------------------------------------------------------------- #

chunk_granularity = config.CHUNK_GRANULARITY  # Define chunk size from config

def get_chunk_array(pdf_path):
    """
    Extracts text from the PDF file and returns a list of text chunks.
    Each chunk corresponds to a part of a page.
    """
    document = fitz.open(pdf_path)
    chunks = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text("text")
        if text.strip():  # Avoid empty pages
            chunks.extend(chunk_text(text.replace("\n", " "), page_num))

    return chunks

def chunk_text(text, page_num):
    """
    Splits the extracted text into smaller chunks based on `chunk_granularity`.
    Each chunk is labeled with the corresponding page number.
    """
    chunks = []
    
    for i in range(0, len(text), chunk_granularity):
        chunk = text[i:i + chunk_granularity]
        chunk_with_page_info = f"Auf Seite {page_num + 1} steht:\n{chunk}"
        chunks.append(chunk_with_page_info)
    
    return chunks

# Beispielaufruf
if __name__ == "__main__":
    pdf_path = "data/ressources/Handbuch-Light_Einmalzahlungen-in-Beziehungen-mit-Serienlieferungen_v1.2.pdf"
    chunks = get_chunk_array(pdf_path)
    
    for page in chunks:
        print(page)