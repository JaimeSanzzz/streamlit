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


##### HEADERS #####
# Dividir la pantalla en tres columnas, contenido-espacio-logo
col1, col2, col3 = st.columns([0.80, 0.05, 0.15])
with col1:
    # Escribir la bienvenida a la app 
    st.write("# 👋🏼 ¡Bienvenido a la app!")
    st.markdown(
        """
        <div style="font-size:20px;"> 
        Esta aplicación web sirve para generar plantillas de los datos de interés a extraer de un documento. 
        Funciona de la siguiente manera: has de seleccionar un tipo de documento, una clase, los campos relevantes y su formato correspondiente.
        Dicha parametrización se realiza desde la segunda pestaña de esta app. 
        </div>
        """, unsafe_allow_html=True
        )
    # Escribir la guia de la app 
    st.write("")
    st.markdown(
        """
        <div style="font-size:18px;"> 
        Para ayudarte a entender el funcionamiento de la app, aquí tienes una demo y una colección de preguntas que te pueden interesar. 
        Si tienes alguna duda adicional que no queda respondida puedas contactar con el equipo de Exponential Technologies.
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
        st.markdown("## Visualiza una demostración")
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
    st.markdown('## Preguntas Frecuentes')
    st.write('')
    st.write('')
    st.write('')
    st.markdown(
        """
        - *¿Puedo seleccionar más de un tipo de documento?*  
        **Si estás interesado en más de un tipo de documento, la mejor solución consiste en que rellenes la plantilla para el primer tipo, y luego para el segundo.**
        
        - *¿Hay algún límite en el número de campos de interés?*  
        **No, puedes escoger tantos como desees, además puedes customizar los tuyos propios mediante la opción 'Otros'.**
        
        - *¿Cómo puedo definir el formato de un campo si existe más de una posibilidad?*  
        **Por cada campo escoge todos los formatos que apliquen, no te limites a poner solo el más común.**

        - *¿Tengo que introducir los campos y su formato en el mismo orden para que concuerden?*  
        **A medida que vayas seleccionando los campos se te irán habriendo ventanas específicas para que introduzcas su formato correspondiente.**
        """
    )



### FOOTER ###
# Añadir una linea separadora final con un pequeño comentario sobre el desarrollo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
st.markdown("""
    <hr>
    <small>Desarrollado con ❤️ usando Streamlit</small>
    """, unsafe_allow_html=True)