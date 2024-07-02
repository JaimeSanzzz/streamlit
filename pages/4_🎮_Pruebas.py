import streamlit as st
import time


st.set_page_config(page_title="Pruebas", layout="wide")
logo = "babel.png"
short_logo = "babel_short.png"
st.logo(logo, icon_image=short_logo)
st.sidebar.markdown("BABEL Sistemas de Información ©2024")



# Title of the app
st.title("My Streamlit App")

# Create a button to show help
if st.button("Need Help?"):
    with st.expander("Help Information"):
        st.write("""
            ## Help Information
            Here you can provide detailed information about how to use the app, common issues, and FAQs.
            - **Step 1:** Do this first.
            - **Step 2:** Then do this.
            - **FAQ 1:** Answer to the frequently asked question.
            - **Contact:** For further assistance, contact support@example.com.
        """)

# Main content of your app
st.write("Main app content goes here.")


col1, col2, col3 = st.columns([0.33, 0.33, 0.33])
with col1:
    st.write("# HEADER 1")
    st.write("## HEADER 2")
    st.write("### HEADER 3")
    st.write("#### HEADER 4")
    st.write("##### HEADER 5")
    st.write("###### HEADER 6")
    st.write("NORMAL TEXT")
    st.write("Normal text")
    st.write("**Bold text**")
    st.write("*Italic text*")
    st.write("`ddd`")
    st.write("")
    st.write("")
    st.write("")
with col2:
    st.markdown("<h1 style='font-size:24px;'>This is a heading</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px;'>This is a paragraph with larger text.</p>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
with col3:
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)


st.markdown("""
    <hr style="border:2px dotted blue;">
    <hr style="border:0.5px dashed #FFA500;">
    <hr style="border:0.2px dashed #FFA500;">
    <hr style="border:2px double green;">
    <hr style="border:2px groove orange;">
    <hr style="border:2px ridge purple;">
    <hr style="border:2px inset pink;">
    <hr style="border:2px outset brown;">
    """, unsafe_allow_html=True)

st.markdown("""<hr style="border:0.2px dashed #FFA500;">""", unsafe_allow_html=True)


##### LEGO BLOCKS #####
col1, col2, col3 = st.columns(3)
## ANALISIS DE DOCUMENTOS ##
with col1:
    st.markdown("#### ANÁLISIS DE DOCUMENTOS:")
    options_block1 = ['TRUE','FALSE']
    select_block1 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir el análisis de documentos en tu pipeline.")
## ANALISIS DE DOCUMENTOS ##
with col2:
    st.markdown("#### DETECCIÓN DE FIRMAS:")
    options_block2 = ['TRUE','FALSE']
    select_block2 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir la detección de firmas en tu pipeline.")
## ANALISIS DE DOCUMENTOS ##
with col3:
    st.markdown("#### RESUMEN DE CONTENIDOS:")
    options_block3 = ['TRUE','FALSE']
    select_block3 = st.selectbox(label='', options=options_block1, help="Elige si deseas o no incluir el resumen de contenidos en tu pipeline.")