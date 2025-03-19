import openai
import config
from .text_chunker import get_chunk_array
import faiss
import numpy as np

# -------------------------INFORMATION-------------------------- #
# This script searches in the embeddings for chunks of the PDF
# similar to the prompt given by the user.
# -------------------------------------------------------------- #

# Zugriff auf Embedding API Zugangsdaten
embedding_api_key = config.EMBEDDING_API_KEY
embedding_api_name = config.EMBEDDING_API_NAME

# Setze den OpenAI API-Schlüssel
openai.api_key = embedding_api_key

# Erstellt ein Embedding für einen Text (Anfrage an OpenAI)
def embed_text(text):
    try:
        response = openai.Embedding.create(
            input=[text],
            model=embedding_api_name
        )
        return response['data'][0]['embedding']
    except Exception as e:
        print(f"Etwas ist schief gelaufen bei der Erstellung des Embeddings: {e}")
        raise

# Funktion zur Verarbeitung von PDFs und Erstellen von Embeddings
def embed_pdf(pdf_path, embedding_path):
    text_chunks = get_chunk_array(pdf_path)  # PDF in Text-Chunks aufteilen
    embeddings = np.array([embed_text(chunk) for chunk in text_chunks]).astype('float32')
    print(embeddings)
    
    # Dimension der Embeddings ermitteln
    dimension = embeddings.shape[1]  # Dimension der Embeddings
    index = faiss.IndexFlatL2(dimension)  # FAISS Index erstellen (IndexFlatL2 für einfache Ähnlichkeitsberechnungen)

    # Embeddings zum FAISS Index hinzufügen
    index.add(embeddings)
    
    # FAISS Index speichern
    faiss.write_index(index, embedding_path)
    print("Embeddings erfolgreich erstellt und gespeichert!")
