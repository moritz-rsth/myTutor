import os
import faiss
import numpy as np
import config
from .text_chunker import get_chunk_array
from .embedder import embed_text, embed_pdf
from utils import get_pdf_path, get_embedding_path

# -------------------------INFORMATION-------------------------- #
# This script searches in the embeddings for chunks of the PDF
# similar to the prompt given by the user.
# -------------------------------------------------------------- #

def load_or_create_faiss_index(embedding_path, pdf_path):
    """
    Load a FAISS index if it exists, otherwise create it from the PDF.
    """
    if not os.path.exists(embedding_path):
        print(f"Embedding file not found. Creating new embeddings from: {pdf_path}")
        embed_pdf(pdf_path, embedding_path)

    index = faiss.read_index(embedding_path)
    return index

def retrieve_similar_chunks(prompt, index, text_chunks, top_k=3):
    """
    Retrieve the top_k most relevant text chunks based on the given prompt.
    """
    prompt_embedding = np.array([embed_text(prompt)]).astype('float32')
    distances, indices = index.search(prompt_embedding, top_k)

    similar_chunks = []
    for i in indices[0]:
        if i < len(text_chunks):  # Avoid out-of-bounds errors
            similar_chunks.append(f"{len(similar_chunks) + 1}. Relevante Zusatzinformation: {text_chunks[int(i)]}")

    return similar_chunks

def get_context_info(prompt, topic):
    """
    Get relevant context chunks for a given prompt and topic.
    """
    embedding_path = get_embedding_path(topic)
    pdf_path = get_pdf_path(topic)
    
    index = load_or_create_faiss_index(embedding_path, pdf_path)
    
    # Extract text chunks from the PDF
    text_chunks = get_chunk_array(pdf_path)
    
    # Retrieve the most similar chunks
    similar_chunks = retrieve_similar_chunks(prompt, index, text_chunks)

    print(f"Anzahl ähnlicher Chunks: {len(similar_chunks)}")
    for i, chunk in enumerate(similar_chunks, start=1):
        print(f"Ähnlichstes Chunk {i}:\n{chunk}\n")

    return similar_chunks
