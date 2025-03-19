import config

# Kürzt Chat-Historie auf die letzten 2 Chat-Antworten (ohne Systemprompt)
def extract_history(chat_history):
    # Letzten 3 Nachrichten hinzufügen
    chat_history = chat_history[-4:]
    return chat_history

# Getter für die topic-abhängigen Variablen in der config
def get_pdf_path(topic):
    return config.PDF_PATH_BGB if topic == "BGB" else config.PDF_PATH_VITARA

def get_embedding_path(topic):
    return config.EMBEDDING_PATH_BGB if topic == "BGB" else config.EMBEDDING_PATH_VITARA

def get_system_prompt(topic):
    return config.SYSTEM_PROMPT_BGB if topic == "BGB" else None