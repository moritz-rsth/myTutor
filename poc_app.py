import streamlit as st
from openai import AzureOpenAI
import config


# -------------------------INFORMATION-------------------------- #
# Dieses Skript ist eine einfache Streamlit-App zur Interaktion mit einem KI-Chatbot.
# Es überprüft die API-Verbindung zu Azure OpenAI.
# -------------------------------------------------------------- #


# Zugriff auf LLM API Zugangsdaten
llm_api_key = config.LLM_API_KEY
llm_api_endpoint = config.LLM_API_ENDPOINT
llm_api_name = config.LLM_API_NAME
llm_api_version = config.LLM_API_VERSION

# Langer System-Prompt
SYSTEM_PROMPT = (
    "Du bist ein hilfreicher AI-Assistent, der sich auf technische Fragen spezialisiert. "
    "Du beantwortest Fragen mit detaillierten, gut strukturierten und hilfreichen Antworten. "
    "Falls eine Frage nicht klar formuliert ist, stell eine Rückfrage, um Missverständnisse zu vermeiden."
)

# Streamlit UI-Konfiguration
st.set_page_config(page_title="AI Chat POC", page_icon="🤖")
st.title("AI Chat POC")
st.write("💬 Dies ist ein einfacher Chatbot mit einem langen System-Prompt.")

# Initialisiere den Chat-Verlauf in der Session State
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": SYSTEM_PROMPT}]

# Zeigt den bisherigen Chat-Verlauf an
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Nutzer-Eingabe
user_input = st.chat_input("Stelle eine Frage ...")

if user_input:
    # Zeige die Nutzerfrage im Chat
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Speichere die Nutzerfrage im Chat-Verlauf
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # API-Aufruf an Azure OpenAI
    with st.spinner("KI denkt nach ..."):
        client = AzureOpenAI(
            api_key=llm_api_key, 
            azure_endpoint=llm_api_endpoint, 
            api_version=llm_api_version
        )
        
        chat_completion = client.chat.completions.create(
            messages=st.session_state["messages"],
            model=llm_api_name
        )
        
        assistant_reply = chat_completion.choices[0].message.content

        # Speichere die KI-Antwort im Chat-Verlauf
        st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})

        # Zeige die KI-Antwort im Chat
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)