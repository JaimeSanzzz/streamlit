import streamlit as st
import json

# Establecer el layout, importar los logos y titulo de la barra lateral
st.set_page_config(page_title="Generador", layout="wide")
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
    st.write("# 📝 Generador de plantillas")
    st.write('## 1) Define la plantilla de tu documento')
with col3:
    # Mostar el logo de Babel en la esquina superior derecha
    st.image(logo, width=200) 


# Dividir la pantalla en dos columnas, documento-clase
col1, col2 = st.columns(2)
with col1:
##### 1 DOCUMENTO #####
    st.markdown("#### PASO 1: Introduce el tipo de documento:")
    # Definir las opciones de la dropdown list 
    options_docu = ['','Hospitales', 'Aseguradoras', 'Bancos', 'Hacienda', 'Contratos de trabajo', 'Certificados médicos', 'Estados de cuenta', 'Reportes financieros', 
                    'Escrituras', 'Títulos de propiedad', 'Permisos', 'Licencias de conducir', 'Documentos legales', 'Declaraciones de impuestos', 'Informes médicos', 
                    'Pólizas de seguro', 'Recetas médicas', 'Solicitudes de crédito', 'Actas de nacimiento', 'Testamentos', 'Documentos de viaje', 'Certificados de estudio', 
                    'Facturas médicas', 'Añadir otro tipo de documento']
    # Crear la dropdown list con un boton de ayuda
    select_docu = st.selectbox(label='', options=options_docu, help="Elige uno de los tipos de documento propuestos o customiza el tuyo propio clickeando sobre 'Otros'.")
    # Extender las opciones si se selecciona Otros
    if select_docu == 'Otros':
        # Introducir el numero de otros tipos deseados
        custom_option_count = st.text_input('Introduce el número de tipos de documento:')
        try:
            custom_option_count = int(custom_option_count)
            counter = 1
            custom_docu_list = []
            # Desplegar una secuencia de cajas donde se puede escribir el tipo de documento customizado
            for i in range(custom_option_count):
                custom_docu = st.text_input(f'Especifica el tipo de documento {counter}:')
                custom_docu_list.append(custom_docu)
                counter += 1
            st.write(f'Has seleccionado: {custom_docu_list}')
        except: "Introduce un número válido."
    else:
        st.write(f'Has seleccionado: [{select_docu}]')
    
with col2:
##### 2 CLASE #####
    st.markdown("#### PASO 2: Introduce la clase de documento:")
    options_clase = ['','Protección de datos', 'Consentimiento', 'Cuestionario', 'Autorización de pago', 'Contrato', 'Factura', 'Comprobante de pago', 'Declaración jurada',
                      'Certificado', 'Informe', 'Recibo', 'Solicitud', 'Aviso legal', 'Acuerdo de confidencialidad', 'Política de privacidad', 'Acta', 'Licencia', 
                      'Documento de identidad', 'Registro', 'Carta de recomendación', 'Plan de proyecto', 'Manual de usuario', 'Instructivo', 'Añadir otras clases']
    select_clase = st.multiselect(label='Clases', options=options_clase, placeholder="", help="Selecciona uno o múltiples clases de documento. Si necesitas más (o customizables) clickea sobre 'Otros', y define cuantos necesitas y procede a escribirlos.")
    if "Otros" in select_clase:
        custom_option_count = st.text_input(label="Introduce el número de clases de documento que quieras añadir", help="Escribe, por ejemplo, 2 y pulsa enter")
        try:
            custom_option_count = int(custom_option_count)
            counter = 1
            custom_clase_list = []
            for i in range(custom_option_count):
                custom_clase = st.text_input(f'Especifica la clase de documento {counter}:')
                custom_clase_list.append(custom_clase)
                counter += 1
            select_clase.extend(custom_clase_list)
            select_clase.remove("Otros")
            st.write(f'Has seleccionado: {select_clase}')
        except: "Introduce un número válido."
    else:
        st.write(f'Has seleccionado: {select_clase}')
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)


dec_counter_camp, form_counter_camp = 0, 0
select_camp_global, select_form_global = [],[]
for idx, e in enumerate(select_clase):
    st.markdown(f"### {e}")
    col3, col4 = st.columns(2)
    with col3:
    ##### 3 CAMPOS #####
        dec_counter_camp += 1
        st.markdown(f"#### PASO 3.{str(dec_counter_camp)}: Elige los campos de interés:")
        options_camp = ['','Nombre completo', 'DNI ', 'NHC ', 'Fecha de nacimiento', 'Dirección', 'Teléfono', 'Correo electrónico', 'Número de seguro social', 
                        'Número de cuenta bancaria', 'Número de póliza de seguro', 'Código postal', 'Estado civil', 'Género', 'Ocupación', 'Nacionalidad', 
                        'Lugar de nacimiento', 'Fecha de ingreso', 'Cargo', 'Departamento', 'Número de empleado', 'Licencia de conducir', 'Pasaporte', 'Firma', 
                        'Fecha de emisión', 'Fecha de vencimiento', 'Añadir otros campos']
        key_camp = f"select_camp_{idx}"
        select_camp = st.multiselect(key=key_camp, label=f'Campos - {e}', options=options_camp, placeholder="", help="Elige uno o múltiples campos de interés. Si necesitas más (o customizables) clickea sobre 'Otros', y define cuantos necesitas y procede a escribirlos.")
        if "Otros" in select_camp:
            # Dejar un par de espacios entre la primera y segunda filas
            st.write("")
            st.write("")
            st.write("")
            custom_option_count = st.text_input(label="Introduce el número de campos que quieras añadir", help="Escribe, por ejemplo, 2 y pulsa enter")
            try:
                custom_option_count = int(custom_option_count)
                counter = 1
                custom_camp_list = []
                for i in range(custom_option_count):
                    custom_camp = st.text_input(f'Especifica el campo {counter}:')
                    custom_camp_list.append(custom_camp)
                    counter += 1
                select_camp.extend(custom_camp_list)
                select_camp.remove("Otros")
                select_camp_global.append(select_camp)
                st.write(f'Has seleccionado: {select_camp}')
            except ValueError: st.write("Introduce un número válido.")
        else:
            st.write(f'Has seleccionado: {select_camp}')
            select_camp_global.append(select_camp)

    with col4:
    ##### 4 FORMATOS #####
        form_counter_camp += 1
        st.markdown(f"#### PASO 4.{str(dec_counter_camp)}: Define los formatos de los campos:")
        options_format = ['DD/MM/YYYY','012345678A', '+00-000-000-000', 'usuario@dominio.com', '1234 ABC', '000-0-00-000000-0', 'HH:MM', 
                          'Calle, Número, Ciudad, Código Postal, País', 'Añadir otros formatos']
        multiple_formats = []
        for field_idx, camp in enumerate(select_camp):
            key_form = f"select_form_{idx}_{field_idx}"
            select_form = st.multiselect(key=key_form, label=f'Define el formato de {camp}:', options=options_format, placeholder="", help="Define uno o más formatos de cada campo de interés respectivamente en la casilla correspondiente.")
            st.write(f'Has seleccionado: {select_form}')
            multiple_formats.append(select_form)
        select_form_global.append(multiple_formats)
    st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
    

##### GENERACIÓN DEL DICCIONARIO COMO .json #####
st.write('## 2) Genera el fichero json')
if st.button('Generar', type="secondary"):
    if len(select_docu) > 0 and len(select_clase) > 0  and len(select_camp_global) > 0 and len(select_form_global) > 0:
        json_dict = {}
        camp_form_dict_global = []
        for e in range(len(select_camp_global)):
            zipper = zip(select_camp_global[e], select_form_global[e])
            camp_form_dict = dict(zipper)
            camp_form_dict_global.append(camp_form_dict)
        for e in select_clase:
            json_dict[e] = camp_form_dict_global[select_clase.index(e)]
        st.write("Generando...")
        master_json_dict = {}
        master_json_dict[select_docu] = json_dict
        st.write(master_json_dict)
        dict_string = json.dumps(master_json_dict, indent=4, ensure_ascii=False)
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(dict_string)
        st.success("Se ha guardado el json con éxito en formato .txt")
    else: st.write("Termina de seleccionar los 4 pasos.")




### FOOTER ###
# Añadir una linea separadora final con un pequeño comentario sobre el desarrollo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
st.markdown("""
    <hr>
    <small>Desarrollado con ❤️ usando Streamlit</small>
    """, unsafe_allow_html=True)