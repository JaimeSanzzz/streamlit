import streamlit as st
import time

st.set_page_config(page_title="Pruebas", layout="wide")
logo = "babel.png"
short_logo = "babel_short.png"
st.logo(logo, icon_image=short_logo)
st.sidebar.markdown("BABEL Sistemas de Información ©2024")

### ESTILO CSS ###
# Definir el estilo css de los headers 2 y 3 para que sea el color corporativo
st.markdown("""
    <style>
    .stMarkdown h2, h3 {
        color: #FFA500;
    }
    </style>
    """, unsafe_allow_html=True)

# Define the available languages and their corresponding messages
languages = {
    "Español 🚴🏻‍♂️": {
        "greeting": "Hola, ¡bienvenido a mi aplicación!",
        "instruction": "Por favor, selecciona un idioma de los botones a continuación."
    },
    "English 🏊🏻‍♂️": {
        "greeting": "Hello, welcome to my app!",
        "instruction": "Please select a language from the buttons below."
    },
    "Français 🏄🏻‍♂️": {
        "greeting": "Bonjour, bienvenue sur mon application!",
        "instruction": "Veuillez sélectionner une langue parmi les boutons ci-dessous."
    },
    "Deutsch 🤸🏻‍♀️": {
        "greeting": "Hallo, wilkommen auf mein App!",
        "instruction": "Bitte wählen Sie eine Sprache auf den folgenden Tasten."
    }
}

# Initialize session state for language selection
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Español 🚴🏻‍♂️"

with st.sidebar:
    for _ in range(14):
        st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### LANGUAGE")
    first_two_languages = list(languages.items())[:2]
    cols = st.columns(2)
    for idx, (language, _) in enumerate(first_two_languages):
        if cols[idx].button(language):
            st.session_state.selected_language = language

    last_two_languages = list(languages.items())[2:]
    cols = st.columns(2)
    for idx, (language, _) in enumerate(last_two_languages):
        if cols[idx].button(language):
            st.session_state.selected_language = language

# Get the messages for the selected language
messages = languages[st.session_state.selected_language]
st.title(messages["greeting"])
st.write(messages["instruction"])