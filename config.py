import os
from dotenv import load_dotenv

# -------------------------INFORMATION-------------------------- #
# This script loads environment variables from a .env file, retrieves 
# API keys and paths for both LLM and Embedding APIs, and reads system 
# prompts from text files. It also includes a debugging section to print 
# out the loaded variables for verification.
# -------------------------------------------------------------- #

# Lade die Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Hilfsfunktion, um den System-Prompt aus einer Datei zu lesen
def load_system_prompt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except Exception as e:
        print(f"Could not read the system prompt in {file_path}: {e}")
        return ""

# LLM API Zugangsdaten
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_ENDPOINT = os.getenv("LLM_API_ENDPOINT")
LLM_API_NAME = os.getenv("LLM_API_NAME")
LLM_API_VERSION = os.getenv("LLM_API_VERSION")

# Embedding API Zugangsdaten
EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY")
EMBEDDING_API_ENDPOINT = os.getenv("EMBEDDING_API_ENDPOINT")
EMBEDDING_API_NAME = os.getenv("EMBEDDING_API_NAME")
EMBEDDING_API_VERSION = os.getenv("EMBEDDING_API_VERSION")

# Ressourcen
SYSTEM_PROMPT_VITARA = load_system_prompt("system_prompt_vitara.txt")
SYSTEM_PROMPT_BGB = load_system_prompt("system_prompt_bgb.txt")

PDF_PATH_VITARA = os.getenv("PDF_PATH_VITARA")
PDF_PATH_BGB = os.getenv("PDF_PATH_BGB")

EMBEDDING_PATH_VITARA = os.getenv("EMBEDDING_PATH_VITARA")
EMBEDDING_PATH_BGB = os.getenv("EMBEDDING_PATH_BGB")

CHUNK_GRANULARITY = int(os.getenv("CHUNK_GRANULARITY", 1000))  # Standardwert 1, falls nicht gesetzt

# Debugging: Prüfen, ob alle Variablen geladen wurden
if True:
    print("LLM API Zugangsdaten:")
    print(f"LLM_API_KEY: {LLM_API_KEY}")
    print(f"LLM_API_ENDPOINT: {LLM_API_ENDPOINT}")
    print(f"LLM_API_NAME: {LLM_API_NAME}")
    print(f"LLM_API_VERSION: {LLM_API_VERSION}")

    print("\nEmbedding API Zugangsdaten:")
    print(f"EMBEDDING_API_KEY: {EMBEDDING_API_KEY}")
    print(f"EMBEDDING_API_ENDPOINT: {EMBEDDING_API_ENDPOINT}")
    print(f"EMBEDDING_API_NAME: {EMBEDDING_API_NAME}")
    print(f"EMBEDDING_API_VERSION: {EMBEDDING_API_VERSION}")

    print("\nRessourcen:")
    print("Vitara:")
    print(f"SYSTEM_PROMPT: {SYSTEM_PROMPT_VITARA}")
    print(f"PDF_PATH: {PDF_PATH_VITARA}")
    print(f"EMBEDDING_PATH: {EMBEDDING_PATH_VITARA}")

    print("\nBGB:")
    print(f"SYSTEM_PROMPT: {SYSTEM_PROMPT_BGB}")
    print(f"PDF_PATH: {PDF_PATH_BGB}")
    print(f"EMBEDDING_PATH: {EMBEDDING_PATH_BGB}")

    print(f"\nCHUNK_GRANULARITY: {CHUNK_GRANULARITY}")