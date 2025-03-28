import openai
from .retriever import get_context_info
import config
from utils import get_system_prompt

# -------------------------INFORMATION-------------------------- #
# This Python script utilizes the OpenAI API to interact with a language 
# model and generate responses based on user input and chat history. 
# It includes a function to retrieve relevant context information, build 
# a conversation history, and send a request to the API for generating 
# a response tailored to the user’s topic and input.
# -------------------------------------------------------------- #

# Zugriff auf LLM API Zugangsdaten
llm_api_key = config.LLM_API_KEY
llm_api_name = config.LLM_API_NAME

# OpenAI API Setup
openai.api_key = llm_api_key

def get_response(messages):
    try:
        # API-Anfrage an OpenAI
        chat_completion = openai.ChatCompletion.create(
            model=llm_api_name,
            messages=messages
        )
        return chat_completion['choices'][0]['message']['content']
    except Exception as e:
        print(f"Fehler bei der Anfrage: {e}")
        return None

def chat_with_assistant(user_input, chat_history, topic):
    # Holen der ähnlichen Chunks
    context_info = get_context_info(user_input, topic)
    
    # Systemprompt + History + Context + jetziger Prompt
    messages = [{"role": "system", "content": get_system_prompt(topic)}]
    
    if chat_history:
        messages.extend(chat_history)
    
    # Kontextinformationen separat hinzufügen
    messages.append({"role": "user", "content": f"Kontextinformationen: {context_info}"})
    
    # User-Prompt hinzufügen
    messages.append({"role": "user", "content": user_input})
    
    print(f"Current message: {messages}")
    
    # Holen der Antwort vom LLM
    assistant_reply = get_response(messages)
    return assistant_reply