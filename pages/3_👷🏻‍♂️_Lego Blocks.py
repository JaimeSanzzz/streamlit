import streamlit as st
import json

# Establecer el layout, importar los logos y titulo de la barra lateral
st.set_page_config(page_title="Lego Blocks", layout="wide")
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
        "title": """# 👷🏻‍♂️ Bloques de Lego""",
        "subtitle": """## Elige los bloques que quieras en tu pipeline""",
        ##### SELECCION DE BLOQUES #####
        "options": ['','VERDADERO','FALSO'],
        "head1": """#### ANÁLISIS DE DOCUMENTOS:""",
        "head2": """#### DETECCIÓN DE FIRMAS:""",
        "head3": """#### VALIDACIÓN DE DNI:""",
        "head4": """#### VALIDACIÓN DE CALLE:""",
        "head5": """#### RESUMEN DE CONTENIDOS:""",
        "head6": """#### ANÁLISIS DE SENTIMIENTOS:""",
        "head7": """#### DETECCIÓN DE FRAUDE:""",
        "head8": """#### INTERPRETACIÓN DE RESULTADOS:""",
        "head9": """#### OTRO:""",
        "help": """Elige si deseas, o no, incluir este bloque en tu pipeline.""",
        "blocks": """["Analisis de documentos", "Deteccion de firmas", "Validación de DNI", "Validación de calle", "Resumen de contenidos", 
                      "Analisis de sentimientos", "Deteccion de fraude", "Interpretacion de resultados", "Otro"]""",
        ##### GENERADOR #####
        "gen_button": """Generar""",
        "gen_run": """Generando...""",
        "gen_success": """"Se han guardado los bloques con éxito en formato .txt""",
        "gen_exception": """"Termina de seleccionar todos los bloques.""",
        "footer": """Desarrollado con ❤️ usando Streamlit"""
    },

    "English 🏊🏻‍♂️": {
        ##### TITULOS #####
        "title": """# 👷🏻‍♂️ Lego Blocks""",
        "subtitle": """## Choose the blocks you want to include in your pipeline""",
        ##### SELECCION DE BLOQUES #####
        "options": ['','TRUE','FALSE'],
        "head1": """#### DOCUMENT ANALYSIS:""",
        "head2": """#### SIGNATURE DETECTION:""",
        "head3": """#### ID VALIDATION:""",
        "head4": """#### ADDRESS VALIDATION:""",
        "head5": """#### CONTENT SUMMARIZATION:""",
        "head6": """#### SENTIMENT ANALYSIS:""",
        "head7": """#### FRAUD DETECTION:""",
        "head8": """#### RESULT INTERPRETATION:""",
        "head9": """#### OTHER:""",
        "help": """Choose whether or not to include this block in your pipeline.""",
        "blocks": """["Document Analysis", "Signature Detection", "ID Validation", "Address Validation", "Content Summarization", 
                    "Sentiment Analysis", "Fraud Detection", "Result Interpretation", "Other"]""",
        ##### GENERADOR #####
        "gen_button": """Generate""",
        "gen_run": """Generating...""",
        "gen_success": """"Blocks successfully saved in .txt format""",
        "gen_exception": """"Finish selecting all blocks.""",
        "footer": """Developed with ❤️ using Streamlit"""
    },

    "Français 🏄🏻‍♂️": {
        ##### TITULOS #####
        "title": """# 👷🏻‍♂️ Blocs Lego""",
        "subtitle": """## Choisissez les blocs que vous souhaitez dans votre pipeline""",
        ##### SELECCION DE BLOQUES #####
        "options": ['','VRAI','FAUX'],
        "head1": """#### ANALYSE DE DOCUMENTS:""",
        "head2": """#### DÉTECTION DE SIGNATURES:""",
        "head3": """#### VALIDATION D'IDENTITÉ:""",
        "head4": """#### VALIDATION D'ADRESSE:""",
        "head5": """#### RÉSUMÉ DE CONTENU:""",
        "head6": """#### ANALYSE DE SENTIMENTS:""",
        "head7": """#### DÉTECTION DE FRAUDE:""",
        "head8": """#### INTERPRÉTATION DES RÉSULTATS:""",
        "head9": """#### AUTRE:""",
        "help": """Choisissez si vous souhaitez inclure ou non ce bloc dans votre pipeline.""",
        "blocks": """["Analyse de documents", "Détection de signatures", "Validation d'identité", "Validation d'adresse", "Résumé de contenu", 
                    "Analyse de sentiments", "Détection de fraude", "Interprétation des résultats", "Autre"]""",
        ##### GENERADOR #####
        "gen_button": """Générer""",
        "gen_run": """Génération en cours...""",
        "gen_success": """"Blocs enregistrés avec succès au format .txt""",
        "gen_exception": """"Terminez la sélection de tous les blocs.""",
        "footer": """Développé avec ❤️ en utilisant Streamlit"""
    },

    "Deutsch 🤸🏻‍♀️": {
        ##### TITULOS #####
        "title": """# 👷🏻‍♂️ Lego-Blöcke""",
        "subtitle": """## Wählen Sie die Blöcke aus, die Sie in ihrer Pipeline haben möchten""",
        ##### SELECCION DE BLOQUES #####
        "options": ['','WAHR','FALSCH'],
        "head1": """#### DOKUMENTENANALYSE:""",
        "head2": """#### SIGNATURERKENNUNG:""",
        "head3": """#### ID VALIDIERUNG:""",
        "head4": """#### ADRESSE VALIDIERUNG:""",
        "head5": """#### INHALTSZUSAMMENFASSUNG:""",
        "head6": """#### STIMMUNGSANALYSE:""",
        "head7": """#### BETRUGSERKENNUNG:""",
        "head8": """#### ERGEBNISINTERPRETATION:""",
        "head9": """#### ANDERES:""",
        "help": """Wählen Sie aus, ob Sie diesen Block in ihre Pipeline aufnehmen möchten oder nicht.""",
        "blocks": """["Dokumentenanalyse", "Signaturerkennung", "ID-Validierung", "Adressvalidierung", "Inhaltszusammenfassung", 
                    "Stimmungsanalyse", "Betrugserkennung", "Ergebnisinterpretation", "Andere"]""",
        ##### GENERADOR #####
        "gen_button": """Generieren""",
        "gen_run": """Generiere...""",
        "gen_success": """"Blöcke erfolgreich im .txt-Format gespeichert""",
        "gen_exception": """"Wählen Sie alle Blöcke aus.""",
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
    st.write(messages["subtitle"])
with col3:
    # Mostar el logo de Babel en la esquina superior derecha
    st.image(logo, width=200) 


##### LEGO BLOCKS #####
col1, col2, col3 = st.columns(3)
## ANALISIS DE DOCUMENTOS ##
options = messages["options"]
with col1:
    st.markdown(messages["head1"])
    select_block1 = st.selectbox(label="block-1", options=options, help=messages["help"], label_visibility='hidden')
## DETECCION DE FIRMAS ##
with col2:
    st.markdown(messages["head2"])
    select_block2 = st.selectbox(label="block-2", options=options, help=messages["help"], label_visibility='hidden')
## RESUMEN DE CONTENIDOS ##
with col3:
    st.markdown(messages["head3"])
    select_block3 = st.selectbox(label="block-3", options=options, help=messages["help"], label_visibility='hidden')


col4, col5, col6 = st.columns(3)
## ANALISIS DE SENTIMIENTOS ##
with col4:
    st.markdown(messages["head4"])
    select_block4 = st.selectbox(label="block-4", options=options, help=messages["help"], label_visibility='hidden')
## DETECCION DE FRAUDE ##
with col5:
    st.markdown(messages["head5"])
    select_block5 = st.selectbox(label="block-5", options=options, help=messages["help"], label_visibility='hidden')
## INTERPRETACION DE RESULTADOS ##
with col6:
    st.markdown(messages["head6"])
    select_block6 = st.selectbox(label="block-6", options=options, help=messages["help"], label_visibility='hidden')


col7, col8, col9 = st.columns(3)
## ANALISIS DE SENTIMIENTOS ##
with col7:
    st.markdown(messages["head7"])
    select_block7 = st.selectbox(label="block-7", options=options, help=messages["help"], label_visibility='hidden')
## DETECCION DE FRAUDE ##
with col8:
    st.markdown(messages["head8"])
    select_block8 = st.selectbox(label="block-8", options=options, help=messages["help"], label_visibility='hidden')
## DETECCION DE FRAUDE ##
with col9:
    st.markdown(messages["head9"])
    select_block9 = st.selectbox(label="block-9", options=options, help=messages["help"], label_visibility='hidden')

# Definir los nombres de los bloques y las opciones seleccionadas
block_names = messages["blocks"]
block_options = [select_block1, select_block2, select_block3, select_block4, select_block5, select_block6, select_block7, select_block8, select_block9]


##### GENERACIÓN DE LOS BLOQUES EN FORMATO .txt #####
if st.button(messages["gen_button"], type="secondary"):
    # Checkear que se han seleccionado todos los bloques
    if len(select_block1) > 0 and len(select_block2) > 0  and len(select_block3) > 0 and len(select_block4) > 0 and len(select_block5) > 0 and len(select_block6) > 0:
        # Juntar los nombres y las opciones de los bloques por parejas
        zipper = zip(block_names, block_options)
        # Transformarlo en un diccionario
        block_dict = dict(zipper)
        st.write(messages["gen_run"])
        # Mostrar el diccionario en pantalla
        st.write(block_dict)
        # Guardar el diccionario como .txt
        dict_string = json.dumps(block_dict, indent=4, ensure_ascii=False)
        # Especificar el encoding utf-8 para evitar problemas con los acentos españoles, y guardar el diccionario como .txt
        with open('.txt/blocks.txt', 'w', encoding='utf-8') as file:
            file.write(dict_string)
        st.success(messages["gen_success"])
    else: st.write(messages["gen_exception"])


### FOOTER ###
# Añadir una linea separadora final con un pequeño comentario sobre el desarrollo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
st.markdown(f"""<hr><small>{messages["footer"]}</small>""", unsafe_allow_html=True)