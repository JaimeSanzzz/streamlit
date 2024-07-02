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


##### HEADERS #####
# Dividir la pantalla en tres columnas, contenido-espacio-logo
col1, col2, col3 = st.columns([0.80, 0.05, 0.15])
with col1:
    # Escribir los titulos de la pestaña
    st.write("# 🔮 Transformador de .json a atributos de interés")
    st.write('## 1) Sube el fichero .json')
with col3:
    # Mostar el logo de Babel en la esquina superior derecha
    st.image(logo, width=200) 

# Crear el boton para subir el fichero .json
uploaded_file = st.file_uploader(label="Elige un fichero", help="Sube un fichero .json para que la IA extraiga el tipo de documento, las clases, campos, y sus respectivos formatos.")
if uploaded_file is not None:
    # Leer el fichero como un string
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

# Separar el primer subtitulo del segundo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)

# Escribir el segundo subtitulo
st.write('## 2) Deja que la IA haga su magia')
try:
    # Crear el boton de ejecucion
    if st.button('Ejecutar IA', type="secondary"):
        st.write('Generando...')
except: st.write("Sube primero el archivo.")

### FOOTER ###
# Añadir una linea separadora final con un pequeño comentario sobre el desarrollo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
st.markdown("""
    <hr>
    <small>Desarrollado con ❤️ usando Streamlit</small>
    """, unsafe_allow_html=True)