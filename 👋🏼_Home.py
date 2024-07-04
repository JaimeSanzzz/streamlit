import streamlit as st

# Establecer el layout, importar los logos y titulo de la barra lateral
st.set_page_config(page_title="Inicio", layout="wide")
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
        "greeting": """# 👋🏼 ¡Bienvenido a la app!""",
        "introduction": """Esta aplicación web sirve para generar plantillas de los datos de interés a extraer de un documento. 
                           Funciona de la siguiente manera: has de seleccionar un tipo de documento, una clase, los campos relevantes y su formato correspondiente.
                           Dicha parametrización se realiza desde la segunda pestaña de esta app.""",
        "guide": """Para ayudarte a entender el funcionamiento de la app, aquí tienes una demo y una colección de preguntas que te pueden interesar. 
                    Si tienes alguna duda adicional que no queda respondida puedas contactar con el equipo de Exponential Technologies.""",
        "demo": """Visualiza una demostración""",
        "faq": """Preguntas Frecuentes""",
        "questions": """
                - *¿Puedo seleccionar más de un tipo de documento?*  
                **Si estás interesado en más de un tipo de documento, la mejor solución consiste en que rellenes la plantilla para el primer tipo, y luego para el segundo.**
                
                - *¿Hay algún límite en el número de campos de interés?*  
                **No, puedes escoger tantos como desees, además puedes customizar los tuyos propios mediante la opción 'Otros'.**
                
                - *¿Cómo puedo definir el formato de un campo si existe más de una posibilidad?*  
                **Por cada campo escoge todos los formatos que apliquen, no te limites a poner solo el más común.**

                - *¿Tengo que introducir los campos y su formato en el mismo orden para que concuerden?*  
                **A medida que vayas seleccionando los campos se te irán habriendo ventanas específicas para que introduzcas su formato correspondiente.**
                """,
        "footer": """Desarrollado con ❤️ usando Streamlit""",
    },

    "English 🏊🏻‍♂️": {
        "greeting": "# 👋🏼 Welcome to the app!",
        "introduction": """This web application is used to generate templates for the data of interest to be extracted from a 
                          document. It works as follows: you must select a document type, a class, the relevant fields, and 
                          their corresponding format. This parameterization is done from the second tab of this app.""",
        "guide": """In order to help you grasp the functioning of the app, take a look at the demo and FAQ below.
                    Should you have additional questions, please don't hesitate to get in touch with the ExTech team.""",
        "demo": """Watch a demo""",
        "faq": """FAQ""",
        "questions": """
                - *Can I select more than one type of document?*
                **If you are interested in more than one type of document, the best solution is to fill out the template for the first type, and then for the second.**

                - *Is there a limit on the number of fields of interest?*
                **No, you can choose as many as you like, and you can also customize your own using the 'Others' option.**

                - *How can I define the format of a field if there are multiple possibilities?*
                **For each field, choose all applicable formats; don't just limit yourself to the most common one.**

                - *Do I have to enter the fields and their format in the same order for them to match?*
                **As you select the fields, specific windows will open for you to enter their corresponding format.**
                """,
        "footer": """Developed with ❤️ using Streamlit""",
        
    },

    "Français 🏄🏻‍♂️": {
        "greeting": "# 👋🏼 Bienvenue sur la application!",
        "introduction": """Cette application web sert à générer des modèles des données d'intérêt à extraire d'un document.
                          Elle fonctionne de la manière suivante : vous devez sélectionner un type de document, une classe,
                          les champs pertinents et leur format correspondant. Cette paramétrisation se fait depuis le deuxième onglet de cette application.""",
        "guide": """Pour vous aider à comprendre comment fonctionne l'application, vous trouverez ici une démo et une collection de questions fréquentes.
                    Si vous avez d'autres questions, n'hésitez pas à contacter l'équipe ExTech""",
        "demo": """Regardez uné demo""",
        "faq": """Foire Aux Questions""",
        "questions": """
            - *Puis-je sélectionner plus d'un type de document?*
            **Si vous êtes intéressé par plusieurs types de documents, la meilleure solution est de remplir le modèle pour le premier type, puis pour le deuxième.**
            
            - *Y a-t-il une limite au nombre de champs d'intérêt ?
            **Non, vous pouvez en choisir autant que vous le souhaitez, et vous pouvez également personnaliser les vôtres avec l'option 'Autres'.**

            - *Comment puis-je définir le format d'un champ s'il existe plusieurs possibilités ?
            **Pour chaque champ, choisissez tous les formats applicables ; ne vous limitez pas au plus courant.**

            - *Dois-je entrer les champs et leur format dans le même ordre pour qu'ils concordent ?
            **Au fur et à mesure que vous sélectionnez les champs, des fenêtres spécifiques s'ouvriront pour que vous saisissiez leur format correspondant.**
            """,
        "footer": """Développé avec ❤️ en utilisant Streamlit""",
    },

    "Deutsch 🤸🏻‍♀️": {
        "greeting": "# 👋🏼 Wilkommen auf der App!",
        "introduction": """Diese Webanwendung dient dazu, Vorlagen für die interessierenden Daten zu erstellen, die aus einem Dokument 
                          extrahiert werden sollen. Sie funktioniert folgendermaßen: Sie müssen einen Dokumententyp, eine Klasse, die 
                          relevanten Felder und ihr entsprechendes Format auswählen. Diese Parametrisierung erfolgt auf dem zweiten Tab dieser App.""",
        "guide": """Um Ihnen zu helfen die App zu verstehen, finden Sie hier unten eine Demo und einige häufig gestellte Fragen.
                    Sollten Sie weitere Fragen haben, kontaktieren Sie bitte das ExTech Team.""",
        "demo": """Schauen Sie sich eine Demo an""",
        "faq": """Häufig Gestellte Fragen""",
        "questions": """
            - *Kann ich mehr als einen Dokumententyp auswählen?*
            **Wenn Sie an mehr als einem Dokumententyp interessiert sind, ist die beste Lösung, das Template für den ersten Typ auszufüllen und dann für den zweiten.**

            - *Gibt es eine Begrenzung für die Anzahl der interessierenden Felder?*
            **Nein, Sie können so viele wählen, wie Sie möchten, und Sie können auch Ihre eigenen mit der Option 'Andere' anpassen.**

            - *Wie kann ich das Format eines Feldes definieren, wenn es mehrere Möglichkeiten gibt?*
            **Wählen Sie für jedes Feld alle anwendbaren Formate aus; beschränken Sie sich nicht nur auf das häufigste.**

            - *Muss ich die Felder und ihr Format in derselben Reihenfolge eingeben, damit sie übereinstimmen?*
            **Wenn Sie die Felder auswählen, werden spezifische Fenster geöffnet, in denen Sie ihr entsprechendes Format eingeben können.**
            """,
        "footer": """Entwickelt mit ❤️ unter Verwendung von Streamlit""",
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


##### HEADERS #####
# Dividir la pantalla en tres columnas, contenido-espacio-logo
col1, col2, col3 = st.columns([0.80, 0.05, 0.15])
with col1:
    # Escribir la bienvenida a la app 
    st.write(messages["greeting"])
    st.markdown(
        f"""
        <div style="font-size:20px;"> 
        {messages["introduction"]}
        </div>
        """, unsafe_allow_html=True
        )
    # Escribir la guia de la app 
    st.write("")
    st.markdown(
        f"""
        <div style="font-size:18px;"> 
        {messages["guide"]}
        </div>
        """, unsafe_allow_html=True
        )    

with col3:
    # Mostar el logo de Babel en la esquina superior derecha
    st.image('babel.png', width=200) 


##### DEMO #####
# Dejar un par de espacios entre la primera y segunda filas
st.write('')
st.write('')
# Dividir la pantalla en tres columnas, demo-espacio-preguntas
col4, col5, col6 = st.columns([0.475, 0.025, 0.475])
with col4:
    # Checkear si el estado de sesion esta activo
    if 'demo_active' not in st.session_state:
        st.session_state.demo_active = False
    # Definir un container para mostrar la demo
    with st.container():
        st.markdown(f"## {messages["demo"]}")
        # Mostrar el boton de play demo si la sesion no esta activa 
        if not st.session_state.demo_active:
            if st.button("Play demo 🎶", type='secondary'):
                # Cambiar el estado de sesion y correr demo
                st.session_state.demo_active = True
                st.experimental_rerun()
            # Dejar la imagen portada de la demo de fondo
            st.image("demo_cover.png")
        # Mostrar el boton de close demo si la sesion esta activa 
        else:
            if st.button("Close demo 🛑"):
                # Cambiar el estado de sesion y parar demo
                st.session_state.demo_active = False
                st.experimental_rerun()
            # Dejar la imagen portada de la demo de fondo
            st.image("demo.gif", use_column_width=True)


##### Q&A #####
with col6:
    # Dejar espacios vacios y definir una serie de preguntas frecuentes
    st.markdown(f'## {messages["faq"]}')
    st.write('')
    st.write('')
    st.write('')
    st.markdown(messages["questions"])



### FOOTER ###
# Añadir una linea separadora final con un pequeño comentario sobre el desarrollo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
st.markdown(f"""
    <hr>
    <small>{messages["footer"]}</small>
    """, unsafe_allow_html=True)