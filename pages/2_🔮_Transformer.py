import streamlit as st
from io import StringIO

# Establecer el layout, importar los logos y titulo de la barra lateral
st.set_page_config(page_title="Transformador", layout="wide")
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


# Configuracion de los idiomas y de sus respectivos mensajes
languages = {
    "Español 🚴🏻‍♂️": {
        ##### TITULOS #####
        "title": """# 🔮 Transformador de .json a atributos de interés""",
        "part1_subtitle": """## 1) Sube el fichero .json""",
        ##### SUBIDA DE ARCHIVOS #####
        "upload_label": """Elige un fichero""",
        "upload_help": """Sube un fichero .json para que la IA extraiga el tipo de documento, las clases, campos, y sus respectivos formatos.""",
        ##### GENERADOR #####
        "part2_subtitle": """## 2) Deja que la IA haga su magia""",
        "gen_button": """Ejecutar IA""",
        "gen_run": """Generando...""",
        "gen_success": """Se ha guardado el json con éxito en formato .txt""",
        "gen_exception": """Sube primero el archivo.""",
        "footer": """Desarrollado con ❤️ usando Streamlit"""
    },

    "English 🏊🏻‍♂️": {
        ##### TITULOS #####
        "title": """# 🔮 JSON to Attributes of Interest Transformer""",
        "part1_subtitle": """## 1) Upload the .json file""",
        ##### SUBIDA DE ARCHIVOS #####
        "upload_label": """Choose a file""",
        "upload_help": """Upload a .json file for the AI to extract document type, classes, fields, and their respective formats.""",
        ##### GENERADOR #####
        "part2_subtitle": """## 2) Let the AI work its magic""",
        "gen_button": """Run AI""",
        "gen_run": """Generating...""",
        "gen_success": """JSON successfully saved in .txt format""",
        "gen_exception": """Upload the file first.""",
        "footer": """Developed with ❤️ using Streamlit"""
    },

    "Français 🏄🏻‍♂️": {
        ##### TITULOS #####
        "title": """# 🔮 Transformateur de JSON en attributs d'intérêt""",
        "part1_subtitle": """## 1) Téléchargez le fichier .json""",
        ##### SUBIDA DE ARCHIVOS #####
        "upload_label": """Choisissez un fichier""",
        "upload_help": """Téléchargez un fichier .json pour que l'IA extrait le type de document, les classes, les champs et leurs formats respectifs.""",
        ##### GENERADOR #####
        "part2_subtitle": """## 2) Laissez l'IA faire sa magie""",
        "gen_button": """Exécuter l'IA""",
        "gen_run": """En cours de génération...""",
        "gen_success": """JSON enregistré avec succès au format .txt""",
        "gen_exception": """Téléchargez d'abord le fichier.""",
        "footer": """Développé avec ❤️ en utilisant Streamlit"""
    },

    "Deutsch 🤸🏻‍♀️": {
        ##### TITULOS #####
        "title": """# 🔮 JSON zu Interessensattributen Transformer""",
        "part1_subtitle": """## 1) Laden Sie die .json Datei hoch""",
        ##### SUBIDA DE ARCHIVOS #####
        "upload_label": """Wählen Sie eine Datei aus""",
        "upload_help": """Laden Sie eine .json Datei hoch, damit die KI den Dokumenttyp, Klassen, Felder und ihre entsprechenden Formate extrahieren kann.""",
        ##### GENERADOR #####
        "part2_subtitle": """## 2) Lassen Sie die KI ihre Magie wirken""",
        "gen_button": """KI ausführen""",
        "gen_run": """Generiere...""",
        "gen_success": """JSON erfolgreich im .txt Format gespeichert""",
        "gen_exception": """Laden Sie zuerst die Datei hoch.""",
        "footer": """Entwickelt mit ❤️ unter Verwendung von Streamlit"""
    }
}

# Initialize session state for language selection
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Español 🚴🏻‍♂️"
selected_language = st.session_state.selected_language
messages = languages[st.session_state.selected_language]


##### HEADERS #####
# Dividir la pantalla en tres columnas, contenido-espacio-logo
col1, col2, col3 = st.columns([0.80, 0.05, 0.15])
with col1:
    # Escribir los titulos de la pestaña
    st.write(messages["title"])
    st.write(messages["part1_subtitle"])
with col3:
    # Mostar el logo de Babel en la esquina superior derecha
    st.image(logo, width=200) 

# Crear el boton para subir el fichero .json
uploaded_file = st.file_uploader(label=messages["upload_label"], help=messages["upload_help"])
if uploaded_file is not None:
    # Leer el fichero como un string
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

# Separar el primer subtitulo del segundo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)

# Escribir el segundo subtitulo
st.write(messages["part2_subtitle"])
try:
    # Crear el boton de ejecucion
    if st.button(messages["gen_button"], type="secondary"):
        st.write(messages["gen_run"])
        st.write(messages["gen_success"])
except: st.write(messages["gen_exception"])

### FOOTER ###
# Añadir una linea separadora final con un pequeño comentario sobre el desarrollo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
st.markdown(f"""<hr><small>{messages["footer"]}</small>""", unsafe_allow_html=True)