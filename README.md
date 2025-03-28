# 🎓 myTutor
Dieses Projekt implementiert einen Chatbot, der mit der OpenAI-Schnittstelle verbunden ist und auf Basis von PDF-Dokumenten arbeitet. Es verwendet Vektorisierung und eine Vektordatenbank, um relevante Informationen aus den PDF-Dokumenten zu extrahieren und in seine Antworten zu integrieren.

## Projektstruktur

Die Projektstruktur ist wie folgt aufgebaut:

```
myTutor/
│── app.py                       # Streamlit UI
│── config.py                    # Konfiguration (API-Keys, Parameter)
│── poc_chat.py                  # Test-Minianwendung (teste API Keys)
│── requirements.txt             # Abhängigkeiten
│── start_app.py                 # Skript zum Starten der Anwendung auf der PDP
│
├── backend/                     # Backend-Logik
│   │── __init__.py
│   │── pdf_loader.py            # PDF-Dateien laden und Text extrahieren
│   │── text_splitter.py         # Texte in sinnvolle Abschnitte chunking
│   │── embedder.py              # OpenAI Embeddings für den Kontext
│   │── retriever.py             # Ähnlichkeitsabfrage zu den Chunks
│   │── chat.py                  # Kommunikation mit OpenAI Chat API
│
├── systemprompts/               # Ordner für alle Systemprompts
│   │── system_prompt_bgb.txt    # Systemprompt für BIC
│   │── system_prompt_vitara.txt # Systemprompt für Einmalzahlung
│
└── utils/                       # Hilfsfunktionen
    └── util_functions.py        # Sonstige Hilfsfunktionen

```

## Installation

Um das Projekt lokal auszuführen, folge diesen Schritten:

### 1. Repository klonen:
```bash
git clone https://github.com/moritz-rsth/myTutor.git
cd myTutor
```

### 2. Virtuelle Umgebung erstellen (optional, aber empfohlen):
```bash
python -m venv venv
source venv/bin/activate  # Für Mac/Linux
venv\Scripts\activate     # Für Windows
```

### 3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

### 4. Anwendung starten:
```bash
streamlit run app.py
```

## Interface

Hier sind einige Screenshots des Interfaces, um einen Eindruck der Benutzeroberfläche zu vermitteln:

![Interface Screenshot 1](images/interface_1.png)  
*Hauptseite des Chatbots mit Eingabefeld und Antwortbereich.*

![Interface Screenshot 2](images/interface_2.png)  
*Beispiel einer Konversation mit dem Chatbot, basierend auf PDF-Inhalten.*

## Beiträge & Verbesserungsvorschläge

Wir freuen uns über Beiträge und Verbesserungsvorschläge! Wenn du Ideen hast, wie wir das Projekt verbessern können, oder Fehler gefunden hast, folge diesen Schritten:

1. **Forke das Repository** auf GitHub.
2. Erstelle einen neuen **Branch** für deine Änderungen:
   ```bash
   git checkout -b dein-branch-name
   ```
3. Mache deine Änderungen und **committe** sie:
   ```bash
   git commit -m "Beschreibe deine Änderungen"
   ```
4. **Pushe** deine Änderungen in dein geforktes Repository:
   ```bash
   git push origin dein-branch-name
   ```
5. Erstelle einen **Pull Request** im originalen Repository und beschreibe deine Änderungen detailliert.

Falls du Fragen hast oder Hilfe benötigst, öffne einfach ein **Issue** im Repository. Ich werde uns so schnell wie möglich darum kümmern.
