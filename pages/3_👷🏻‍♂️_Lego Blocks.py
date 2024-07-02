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


##### HEADERS #####
# Dividir la pantalla en tres columnas, contenido-espacio-logo
col1, col2, col3 = st.columns([0.80, 0.05, 0.15])
with col1:
    # Escribir los titulos de la pestaña
    st.write("# 👷🏻‍♂️ Lego Blocks")
    st.write('## Elige los bloques que quieres en tu pipeline')
with col3:
    # Mostar el logo de Babel en la esquina superior derecha
    st.image(logo, width=200) 


##### LEGO BLOCKS #####
col1, col2, col3 = st.columns(3)
## ANALISIS DE DOCUMENTOS ##
with col1:
    st.markdown("#### ANÁLISIS DE DOCUMENTOS:")
    options_block1 = ['','TRUE','FALSE']
    select_block1 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir el análisis de documentos en tu pipeline.")
## DETECCION DE FIRMAS ##
with col2:
    st.markdown("#### DETECCIÓN DE FIRMAS:")
    options_block2 = ['','TRUE','FALSE']
    select_block2 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir la detección de firmas en tu pipeline.")
## RESUMEN DE CONTENIDOS ##
with col3:
    st.markdown("#### RESUMEN DE CONTENIDOS:")
    options_block3 = ['','TRUE','FALSE']
    select_block3 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir el resumen de contenidos en tu pipeline.")


col4, col5, col6 = st.columns(3)
## ANALISIS DE SENTIMIENTOS ##
with col4:
    st.markdown("#### ANÁLISIS DE SENTIMIENTOS:")
    options_block4 = ['','TRUE','FALSE']
    select_block4 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir el análisis de sentimientos en tu pipeline.")
## DETECCION DE FRAUDE ##
with col5:
    st.markdown("#### DETECCIÓN DE FRAUDE:")
    options_block5 = ['','TRUE','FALSE']
    select_block5 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir la detección de fraude en tu pipeline.")
## INTERPRETACION DE RESULTADOS ##
with col6:
    st.markdown("#### INTERPRETACIÓN DE RESULTADOS:")
    options_block6 = ['','TRUE','FALSE']
    select_block6 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir la interpretación de resultados en tu pipeline.")


col7, col8, col9 = st.columns(3)
## ANALISIS DE SENTIMIENTOS ##
with col7:
    st.markdown("#### VALIDACIÓN DE DNI:")
    options_block7 = ['','TRUE','FALSE']
    select_block7 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir la validación de dni en tu pipeline.")
## DETECCION DE FRAUDE ##
with col8:
    st.markdown("#### VALIDACIÓN DE CALLE:")
    options_block8 = ['','TRUE','FALSE']
    select_block8 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir la validación de calle en tu pipeline.")
## DETECCION DE FRAUDE ##
with col8:
    st.markdown("#### OTRO:")
    options_block9 = ['','TRUE','FALSE']
    select_block9 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir otro en tu pipeline.")

# Definir los nombres de los bloques y las opciones seleccionadas
block_names = ["Analisis de documentos", "Deteccion de firmas", "Resumen de contenidos", "Analisis de sentimientos", 
               "Deteccion de fraude", "Interpretacion de resultados", "Validación de DNI", "Validación de calle", "Otro"]
block_options = [select_block1, select_block2, select_block3, select_block4, select_block5, select_block6, select_block7, select_block8, select_block9]


##### GENERACIÓN DE LOS BLOQUES EN FORMATO .txt #####
if st.button('Generar', type="secondary"):
    # Checkear que se han seleccionado todos los bloques
    if len(select_block1) > 0 and len(select_block2) > 0  and len(select_block3) > 0 and len(select_block4) > 0 and len(select_block5) > 0 and len(select_block6) > 0:
        # Juntar los nombres y las opciones de los bloques por parejas
        zipper = zip(block_names, block_options)
        # Transformarlo en un diccionario
        block_dict = dict(zipper)
        st.write("Generando...")
        # Mostrar el diccionario en pantalla
        st.write(block_dict)
        # Guardar el diccionario como .txt
        dict_string = json.dumps(block_dict, indent=4, ensure_ascii=False)
        # Especificar el encoding utf-8 para evitar problemas con los acentos españoles, y guardar el diccionario como .txt
        with open('.txt/blocks.txt', 'w', encoding='utf-8') as file:
            file.write(dict_string)
        st.success("Se han guardado los bloques con éxito en formato .txt")
    else: st.write("Termina de seleccionar todos los bloques.")
