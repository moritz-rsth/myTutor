import streamlit as st
from PIL import Image
from backend import chat_with_assistant
from utils import extract_history

# -------------------------INFORMATION-------------------------- #
# This script searches in the embeddings for chunks of the PDF
# similar to the prompt given by the user.
# -------------------------------------------------------------- #

# Konfigurieren der Seiten-Einstellungen
st.set_page_config(
    page_title="myTutor",
    page_icon="🎓",
    initial_sidebar_state="auto",
    menu_items={
        'Report a bug': None,
        'About': None,
        'Get Help': None
    }
)

# Sidebar Logo
logo = Image.open("data/images/Logo.png")
st.sidebar.image(logo, use_container_width=True)

# Mapping für die Topic-Variable
mapping = {
    "Suzuki Vitara Anleitung": "Vitara",
    "Bürgerliches Gesetzbuch (BGB)": "BGB"
}

# Sidebar Navigation
st.sidebar.title("Assistent auswählen")
topic = mapping.get(
    st.sidebar.radio("Thema", ["Suzuki Vitara Anleitung", "Bürgerliches Gesetzbuch (BGB)"])
)

# Main Page
st.title("🎓 myTutor")
st.write("🚀 myTutor beantwortet Fragen basierend auf Info-PDFs.")

# Chat-Verlauf initialisieren
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Zeigt den bisherigen Chat-Verlauf
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Nutzer-Eingabe
user_input = st.chat_input("Stelle eine Frage ...")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # KI antwortet
    with st.spinner("🔎 KI denkt nach..."):
        assistant_reply = chat_with_assistant(
            user_input, extract_history(st.session_state["messages"]), topic
        )
    
    st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)