import streamlit as st
import yaml
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

#######################
languages = ["Español 🚴🏻‍♂️","English 🏊🏻‍♂️","Français 🏄🏻‍♂️","Deutsch 🤸🏻‍♀️"]
with st.sidebar:
    for _ in range(14):
        st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### LANGUAGE")
    first_two_languages = languages[:2]
    cols = st.columns(2)
    for idx, language in enumerate(first_two_languages):
        if cols[idx].button(language):
            st.session_state.selected_language = language

    last_two_languages = languages[2:]
    cols = st.columns(2)
    for idx, language in enumerate(last_two_languages):
        if cols[idx].button(language):
            st.session_state.selected_language = language
##################

with open('lang.yaml', 'r', encoding='utf-8') as file:
    languages = yaml.safe_load('lang.yaml')

current_page = 'page1'
selected_language = st.session_state.selected_language
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Español 🚴🏻‍♂️"

messages = languages[selected_language]
st.title(messages[current_page]["greeting"])
