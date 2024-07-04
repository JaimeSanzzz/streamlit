import streamlit as st
import json

# Establecer el layout, importar los logos y titulo de la barra lateral
st.set_page_config(page_title="Generador", layout="wide")
logo = "babel.png"
short_logo = "babel_short.png"
st.logo(logo, icon_image=short_logo)     
st.sidebar.markdown("BABEL Sistemas de Información ©2024")

# Configuracion de los idiomas y de sus respectivos mensajes
languages = {
    "Español 🚴🏻‍♂️": {
        ##### TITULOS #####
        "title": """# 📝 Generador de plantillas""",
        "part1_subtitle": """## 1) Define la plantilla de tu documento""",

        ##### 1 DOCUMENTO #####
        "step1": """#### PASO 1: Introduce el tipo de documento:""",
        "doc_options": ['','Hospitales', 'Aseguradoras', 'Bancos', 'Hacienda', 'Contratos de trabajo', 'Certificados médicos', 'Estados de cuenta', 'Reportes financieros', 
                    'Escrituras', 'Títulos de propiedad', 'Permisos', 'Licencias de conducir', 'Documentos legales', 'Declaraciones de impuestos', 'Informes médicos', 
                    'Pólizas de seguro', 'Recetas médicas', 'Solicitudes de crédito', 'Actas de nacimiento', 'Testamentos', 'Documentos de viaje', 'Certificados de estudio', 
                    'Facturas médicas', 'Añadir otro tipo de documento'],
        "doc_label": """Documento""",
        "doc_help": """Elige uno de los tipos de documento propuestos o customiza el tuyo propio clickeando sobre 'Otros'.""",
        "doc_other": """Añadir otro tipo de documento""",
        "doc_custom_count": """Introduce el número de tipos de documento:""",
        "doc_custom_text": """Especifica el tipo de documento""",
        "custom_exception": """Introduce un número válido.""",
        "selection": """Has seleccionado: """,

        ##### 2 CLASES #####
        "step2": """#### PASO 2: Introduce la clase de documento:""",
        "clas_options": ['','Protección de datos', 'Consentimiento', 'Cuestionario', 'Autorización de pago', 'Contrato', 'Factura', 'Comprobante de pago', 'Declaración jurada',
                      'Certificado', 'Informe', 'Recibo', 'Solicitud', 'Aviso legal', 'Acuerdo de confidencialidad', 'Política de privacidad', 'Acta', 'Licencia', 
                      'Documento de identidad', 'Registro', 'Carta de recomendación', 'Plan de proyecto', 'Manual de usuario', 'Instructivo', 'Añadir otras clases'],
        "clas_label": """Clases""",
        "clas_help": """Selecciona uno o múltiples clases de documento. Si necesitas más (o customizables) clickea sobre 'Otros', y define cuantos necesitas y procede a escribirlos.""",
        "clas_other": """Añadir otras clases""",
        "clas_custom_count": """Introduce el número de clases de documento que quieras añadir""",
        "clas_custom_help": """Escribe, por ejemplo, 2 y pulsa enter""",
        "clas_custom_text": """Especifica la clase de documento""",

        ##### 3 CAMPOS #####
        "step3": f"""#### PASO 3: Elige los campos de interés:""",
        "camp_options": ['','Nombre completo', 'DNI ', 'NHC ', 'Fecha de nacimiento', 'Dirección', 'Teléfono', 'Correo electrónico', 'Número de seguro social', 
                        'Número de cuenta bancaria', 'Número de póliza de seguro', 'Código postal', 'Estado civil', 'Género', 'Ocupación', 'Nacionalidad', 
                        'Lugar de nacimiento', 'Fecha de ingreso', 'Cargo', 'Departamento', 'Número de empleado', 'Licencia de conducir', 'Pasaporte', 'Firma', 
                        'Fecha de emisión', 'Fecha de vencimiento', 'Añadir otros campos'],
        "camp_label": """Campos""",
        "camp_help": """Elige uno o múltiples campos de interés. Si necesitas más (o customizables) clickea sobre 'Otros', y define cuantos necesitas y procede a escribirlos.""",
        "camp_other": """Añadir otros campos""",
        "camp_custom_count": """Introduce el número de campos que quieras añadir""",
        "camp_custom_help": """Escribe, por ejemplo, 2 y pulsa enter""",
        "camp_custom_text": """Especifica el campo""",

        ##### 4 FORMATOS #####
        "step4": """#### PASO 4: Define los formatos de los campos:""",
        "form_options": ['DD/MM/YYYY','012345678A', '+00-000-000-000', 'usuario@dominio.com', '1234 ABC', '000-0-00-000000-0', 'HH:MM', 
                          'Calle, Número, Ciudad, Código Postal, País', 'Añadir otros formatos'],
        "form_label": """Define el formato de """,
        "form_help": """ """,

        ##### GENERADOR #####
        "part2_subtitle": """## 2) Genera el fichero json""",
        "gen_button": """Generar""",
        "gen_run": """Generando...""",
        "gen_success": """Se ha guardado el json con éxito en formato .txt""",
        "gen_exception": """Termina de seleccionar los 4 pasos.""",
        "footer": """Desarrollado con ❤️ usando Streamlit"""
    },

    "English 🏊🏻‍♂️": {
        ##### TITULOS #####
        "title": """# 📝 Template Generator""",
        "part1_subtitle": """## 1) Define your document template""",

        ##### 1 DOCUMENTO #####
        "step1": """#### STEP 1: Enter the type of document:""",
        "doc_options": ["", "Hospitals", "Insurance Companies", "Banks", "Tax Office", "Employment Contracts", "Medical Certificates", "Account Statements", "Financial Reports", 
                "Deeds", "Property Titles", "Permits", "Driver's Licenses", "Legal Documents", "Tax Declarations", "Medical Reports", 
                "Insurance Policies", "Prescriptions", "Credit Applications", "Birth Certificates", "Wills", "Travel Documents", "Certificates of Study", 
                "Medical Invoices", "Add another type of document"],
        "doc_label": """Document""",
        "doc_help": """Choose one of the suggested document types or customize your own by clicking on 'Other'.""",
        "doc_other": """Add another type of document""",
        "doc_custom_count": """Enter the number of document types:""",
        "doc_custom_text": """Specify the document type""",
        "custom_exception": """Enter a valid number.""",
        "selection": """You have selected: """,

        ##### 2 CLASES #####
        "step2": """#### STEP 2: Enter the document class:""",
        "clas_options": ["", "Data Protection", "Consent", "Questionnaire", "Payment Authorization", "Contract", "Invoice", "Payment Receipt", "Affidavit",
                        "Certificate", "Report", "Receipt", "Request", "Legal Notice", "Confidentiality Agreement", "Privacy Policy", "Minutes", "License", 
                        "Identity Document", "Registry", "Letter of Recommendation", "Project Plan", "User Manual", "Instructions", "Add other classes"],
        "clas_label": """Classes""",
        "clas_help": """Select one or multiple document classes. If you need more (or customizable ones), click on 'Other' and define how many you need, then proceed to write them.""",
        "clas_other": """Add other classes""",
        "clas_custom_count": """Enter the number of document classes you want to add""",
        "clas_custom_help": """Type, for example, 2 and press enter""",
        "clas_custom_text": """Specify the document class""",


        ##### 3 CAMPOS #####
        "step3": f"""#### STEP 3: Choose the fields of interest:""",
        "camp_options": ["", "Full Name", "ID Number", "Medical Record Number", "Date of Birth", "Address", "Phone Number", "Email", "Social Security Number", 
                        "Bank Account Number", "Insurance Policy Number", "Postal Code", "Marital Status", "Gender", "Occupation", "Nationality", 
                        "Place of Birth", "Date of Admission", "Position", "Department", "Employee Number", "Driver's License", "Passport", "Signature", 
                        "Issue Date", "Expiration Date", "Add other fields"],
        "camp_label": """Fields""",
        "camp_help": """Select one or multiple fields of interest. If you need more (or customizable ones), click on 'Other' and define how many you need, then proceed to write them.""",
        "camp_other": """Add other fields""",
        "camp_custom_count": """Enter the number of fields you want to add""",
        "camp_custom_help": """Type, for example, 2 and press enter""",
        "camp_custom_text": """Specify the field""",

        ##### 4 FORMATOS #####
        "step4": """#### STEP 4: Define the field formats:""",
        "form_options": ["DD/MM/YYYY", "012345678A", "+00-000-000-000", "user@example.com", "1234 ABC", "000-0-00-000000-0", "HH:MM", 
                        "Street, Number, City, Postal Code, Country", "Add other formats"],
        "form_label": """Define the format of """,
        "form_help": """ """,

        ##### GENERADOR #####
        "part2_subtitle": """## 2) Generate the JSON file""",
        "gen_button": """Generate""",
        "gen_run": """Generating...""",
        "gen_success": """JSON file successfully saved in .txt format""",
        "gen_exception": """Complete all 4 steps.""",
        "footer": """Developed with ❤️ using Streamlit""",
    },

    "Français 🏄🏻‍♂️": {
        ##### TITULOS #####
        "title": """# 📝 Générateur de Modèles""",
        "part1_subtitle": """## 1) Définissez votre modèle de document""",
        
        ##### 1 DOCUMENTO #####
        "step1": """#### ÉTAPE 1: Entrez le type de document:""",
        "doc_options": ["", "Hôpitaux", "Compagnies d'Assurance", "Banques", "Bureau des Impôts", "Contrats de Travail", "Certificats Médicaux", "Relevés de Compte", "Rapports Financiers", 
                "Actes", "Titres de Propriété", "Permis", "Permis de Conduire", "Documents Juridiques", "Déclarations Fiscales", "Rapports Médicaux", 
                "Polices d'Assurance", "Ordonnances", "Demandes de Crédit", "Certificats de Naissance", "Testaments", "Documents de Voyage", "Certificats d'Études", 
                "Factures Médicales", "Ajouter un autre type de document"],
        "doc_label": """Document""",
        "doc_help": """Choisissez l'un des types de documents suggérés ou personnalisez le vôtre en cliquant sur 'Autre'.""",
        "doc_other": """Ajouter un autre type de document""",
        "doc_custom_count": """Entrez le nombre de types de documents:""",
        "doc_custom_text": """Spécifiez le type de document""",
        "custom_exception": """Entrez un nombre valide.""",
        "selection": """Vous avez sélectionné : """,

        ##### 2 CLASES #####
        "step2": """#### ÉTAPE 2: Entrez la classe de document:""",
        "clas_options": ["", "Protection des Données", "Consentement", "Questionnaire", "Autorisation de Paiement", "Contrat", "Facture", "Reçu de Paiement", "Déclaration sous Serment",
                        "Certificat", "Rapport", "Reçu", "Demande", "Avis Juridique", "Accord de Confidentialité", "Politique de Confidentialité", "Procès-Verbal", "Licence", 
                        "Document d'Identité", "Registre", "Lettre de Recommandation", "Plan de Projet", "Manuel d'Utilisateur", "Instructions", "Ajouter d'autres classes"],
        "clas_label": """Classes""",
        "clas_help": """Sélectionnez une ou plusieurs classes de documents. Si vous en avez besoin de plus (ou personnalisées), cliquez sur 'Autre' et définissez combien vous en avez besoin, puis procédez à les écrire.""",
        "clas_other": """Ajouter d'autres classes""",
        "clas_custom_count": """Entrez le nombre de classes de documents que vous souhaitez ajouter""",
        "clas_custom_help": """Tapez, par exemple, 2 et appuyez sur Entrée""",
        "clas_custom_text": """Spécifiez la classe de document""",

        ##### 3 CAMPOS #####
        "step3": f"""#### ÉTAPE 3: Choisissez les champs d'intérêt:""",
        "camp_options": ["", "Nom Complet", "Numéro d'Identité", "Numéro de Dossier Médical", "Date de Naissance", "Adresse", "Numéro de Téléphone", "Email", "Numéro de Sécurité Sociale", 
                        "Numéro de Compte Bancaire", "Numéro de Police d'Assurance", "Code Postal", "État Civil", "Genre", "Profession", "Nationalité", 
                        "Lieu de Naissance", "Date d'Admission", "Poste", "Département", "Numéro d'Employé", "Permis de Conduire", "Passeport", "Signature", 
                        "Date d'Émission", "Date d'Expiration", "Ajouter d'autres champs"],
        "camp_label": """Champs""",
        "camp_help": """Sélectionnez un ou plusieurs champs d'intérêt. Si vous en avez besoin de plus (ou personnalisés), cliquez sur 'Autre' et définissez combien vous en avez besoin, puis procédez à les écrire.""",
        "camp_other": """Ajouter d'autres champs""",
        "camp_custom_count": """Entrez le nombre de champs que vous souhaitez ajouter""",
        "camp_custom_help": """Tapez, par exemple, 2 et appuyez sur Entrée""",
        "camp_custom_text": """Spécifiez le champ""",

        ##### 4 FORMATOS #####
        "step4": """#### ÉTAPE 4: Définissez les formats de champs:""",
        "form_options": ["JJ/MM/AAAA", "012345678A", "+00-000-000-000", "utilisateur@exemple.com", "1234 ABC", "000-0-00-000000-0", "HH:MM", 
                        "Rue, Numéro, Ville, Code Postal, Pays", "Ajouter d'autres formats"],
        "form_label": """Définir le format de """,
        "form_help": """ """,

        ##### GENERADOR #####
        "part2_subtitle": """## 2) Générer le fichier JSON""",
        "gen_button": """Générer""",
        "gen_run": """Génération...""",
        "gen_success": """Fichier JSON enregistré avec succès au format .txt""",
        "gen_exception": """Complétez les 4 étapes.""",
        "footer": """Développé avec ❤️ en utilisant Streamlit""",
    },

    "Deutsch 🤸🏻‍♀️": {
        ##### TITULOS #####
        "title": """# 📝 Vorlagengenerator""",
        "part1_subtitle": """## 1) Definieren Sie Ihre Dokumentvorlage""",

        ##### 1 DOCUMENTO #####
        "step1": """#### SCHRITT 1: Geben Sie den Dokumenttyp ein:""",
        "doc_options": ["", "Krankenhäuser", "Versicherungsgesellschaften", "Banken", "Finanzamt", "Arbeitsverträge", "Ärztliche Atteste", "Kontoauszüge", "Finanzberichte", 
                "Urkunden", "Eigentumstitel", "Genehmigungen", "Führerscheine", "Rechtsdokumente", "Steuererklärungen", "Ärztliche Berichte", 
                "Versicherungspolicen", "Rezepte", "Kreditanträge", "Geburtsurkunden", "Testamente", "Reisedokumente", "Studienbescheinigungen", 
                "Arztrechnungen", "Weitere Dokumenttypen hinzufügen"],
        "doc_label": """Dokument""",
        "doc_help": """Wählen Sie einen der vorgeschlagenen Dokumenttypen oder passen Sie Ihren eigenen an, indem Sie auf 'Andere' klicken.""",
        "doc_other": """Weitere Dokumenttypen hinzufügen""",
        "doc_custom_count": """Geben Sie die Anzahl der Dokumenttypen ein:""",
        "doc_custom_text": """Spezifizieren Sie den Dokumenttyp""",
        "custom_exception": """Geben Sie eine gültige Nummer ein.""",
        "selection": """Sie haben ausgewählt: """,

        ##### 2 CLASES #####
        "step2": """#### SCHRITT 2: Geben Sie die Dokumentklasse ein:""",
        "clas_options": ["", "Datenschutz", "Einwilligung", "Fragebogen", "Zahlungsermächtigung", "Vertrag", "Rechnung", "Zahlungsbeleg", "Eidesstattliche Erklärung",
                        "Zertifikat", "Bericht", "Beleg", "Antrag", "Rechtlicher Hinweis", "Vertraulichkeitsvereinbarung", "Datenschutzrichtlinie", "Protokoll", "Lizenz", 
                        "Identitätsdokument", "Register", "Empfehlungsschreiben", "Projektplan", "Benutzerhandbuch", "Anweisungen", "Weitere Klassen hinzufügen"],
        "clas_label": """Klassen""",
        "clas_help": """Wählen Sie eine oder mehrere Dokumentklassen aus. Wenn Sie mehr benötigen (oder anpassbare), klicken Sie auf 'Andere' und definieren Sie, wie viele Sie benötigen, und schreiben Sie diese dann.""",
        "clas_other": """Weitere Klassen hinzufügen""",
        "clas_custom_count": """Geben Sie die Anzahl der Dokumentklassen ein, die Sie hinzufügen möchten""",
        "clas_custom_help": """Geben Sie zum Beispiel 2 ein und drücken Sie Enter""",
        "clas_custom_text": """Spezifizieren Sie die Dokumentklasse""",

        ##### 3 CAMPOS #####
        "step3": f"""#### SCHRITT 3: Wählen Sie die interessierenden Felder:""",
        "camp_options": ["", "Vollständiger Name", "Ausweisnummer", "Krankenaktennummer", "Geburtsdatum", "Adresse", "Telefonnummer", "E-Mail", "Sozialversicherungsnummer", 
                        "Bankkontonummer", "Versicherungsscheinnummer", "Postleitzahl", "Familienstand", "Geschlecht", "Beruf", "Nationalität", 
                        "Geburtsort", "Aufnahmedatum", "Position", "Abteilung", "Mitarbeiternummer", "Führerschein", "Pass", "Unterschrift", 
                        "Ausstellungsdatum", "Ablaufdatum", "Weitere Felder hinzufügen"],
        "camp_label": """Felder""",
        "camp_help": """Wählen Sie ein oder mehrere interessierende Felder aus. Wenn Sie mehr benötigen (oder anpassbare), klicken Sie auf 'Andere' und definieren Sie, wie viele Sie benötigen, und schreiben Sie diese dann.""",
        "camp_other": """Weitere Felder hinzufügen""",
        "camp_custom_count": """Geben Sie die Anzahl der Felder ein, die Sie hinzufügen möchten""",
        "camp_custom_help": """Geben Sie zum Beispiel 2 ein und drücken Sie Enter""",
        "camp_custom_text": """Spezifizieren Sie das Feld""",

        ##### 4 FORMATOS #####
        "step4": """#### SCHRITT 4: Definieren Sie die Feldformate:""",
        "form_options": ["TT/MM/JJJJ", "012345678A", "+00-000-000-000", "benutzer@beispiel.com", "1234 ABC", "000-0-00-000000-0", "HH:MM", 
                        "Straße, Nummer, Stadt, Postleitzahl, Land", "Weitere Formate hinzufügen"],
        "form_label": """Definieren Sie das Format von """,
        "form_help": """ """,

        ##### GENERATOR #####
        "part2_subtitle": """## 2) Generieren Sie die JSON-Datei""",
        "gen_button": """Generieren""",
        "gen_run": """Generierung...""",
        "gen_success": """JSON-Datei erfolgreich im .txt-Format gespeichert""",
        "gen_exception": """Vervollständigen Sie alle 4 Schritte.""",
        "footer": """Entwickelt mit ❤️ unter Verwendung von Streamlit""",
    }
}

# Initialize session state for language selection
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Español 🚴🏻‍♂️"
selected_language = st.session_state.selected_language
messages = languages[st.session_state.selected_language]


### ESTILO CSS ###
# Definir el estilo css de los headers 2 y 3 para que sea el color corporativo
st.markdown("""
    <style>
    .stMarkdown h2, h3 {
        color: #FFA500;
    }
    </style>
    """, unsafe_allow_html=True)


##### TITULOS #####
# Dividir la pantalla en tres columnas, contenido-espacio-logo
col1, col2, col3 = st.columns([0.80, 0.05, 0.15])
with col1:
    # Escribir los titulos de la pestaña
    st.write(messages["title"])
    st.write(messages["part1_subtitle"])
with col3:
    # Mostar el logo de Babel en la esquina superior derecha
    st.image(logo, width=200) 


# Dividir la pantalla en dos columnas, documento-clase
col1, col2 = st.columns(2)
with col1:
##### 1 DOCUMENTO #####
    st.markdown(messages["step1"])
    # Definir las opciones de la dropdown list 
    options_docu = messages["doc_options"]
    # Crear la dropdown list con un boton de ayuda
    select_docu = st.selectbox(label=messages["doc_label"], options=options_docu, help=messages["doc_help"])
    # Extender las opciones si se selecciona Otros
    if select_docu == messages["doc_other"]:
        # Introducir el numero de otros tipos deseados
        custom_option_count = st.text_input(messages["doc_custom_count"])
        try:
            custom_option_count = int(custom_option_count)
            counter = 1
            custom_docu_list = []
            # Desplegar una secuencia de cajas donde se puede escribir el tipo de documento customizado
            for i in range(custom_option_count):
                custom_docu = st.text_input(messages["doc_options"+f"{counter}:"])
                custom_docu_list.append(custom_docu)
                counter += 1
            st.write(messages["selection"]+f"{custom_docu_list}")
        except: st.write(messages["custom_exception"])
    else:
        st.write(messages["selection"]+f"[{select_docu}]")
    
with col2:
##### 2 CLASES #####
    st.markdown(messages["step2"])
    options_clase = messages["clas_options"]
    select_clase = st.multiselect(label=messages["clas_label"], options=options_clase, placeholder="", help=messages["clas_help"])
    if messages["clas_other"] in select_clase:
        custom_option_count = st.text_input(label=messages["clas_custom_count"], help=messages["clas_custom_help"])
        try:
            custom_option_count = int(custom_option_count)
            counter = 1
            custom_clase_list = []
            for i in range(custom_option_count):
                custom_clase = st.text_input(messages["clas_custom_text"]+f"{counter}:")
                custom_clase_list.append(custom_clase)
                counter += 1
            select_clase.extend(custom_clase_list)
            select_clase.remove(messages["clas_other"])
            st.write(messages["selection"]+f"{select_clase}")
        except: st.write(messages["custom_exception"])
    else:
        st.write(messages["selection"]+f"{select_clase}")
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)


dec_counter_camp, form_counter_camp = 0, 0
select_camp_global, select_form_global = [],[]
for idx, e in enumerate(select_clase):
    st.markdown(f"### {e}")
    col3, col4 = st.columns(2)
    with col3:
    ##### 3 CAMPOS #####
        dec_counter_camp += 1
        st.markdown(messages["step3"])
        options_camp = messages["camp_options"]
        key_camp = f"select_camp_{idx}"
        select_camp = st.multiselect(key=key_camp, label=messages["clas_label"]+f' - {e}', options=options_camp, placeholder="", help=messages["camp_help"])
        if messages["camp_other"] in select_camp:
            # Dejar un par de espacios entre la primera y segunda filas
            st.write("") 
            st.write("") 
            st.write("") 
            custom_option_count = st.text_input(label=messages["camp_custom_count"], help=messages["camp_custom_help"])
            try:
                custom_option_count = int(custom_option_count)
                counter = 1
                custom_camp_list = []
                for i in range(custom_option_count):
                    custom_camp = st.text_input(messages["camp_custom_text"]+f"{counter}:")
                    custom_camp_list.append(custom_camp)
                    counter += 1
                select_camp.extend(custom_camp_list)
                select_camp.remove(messages["camp_other"])
                select_camp_global.append(select_camp)
                st.write(messages["selection"]+f"{select_camp}")
            except ValueError: st.write(messages["custom_exception"])
        else:
            st.write(messages["selection"]+f"{select_camp}")
            select_camp_global.append(select_camp)

    with col4:
    ##### 4 FORMATOS #####
        #form_counter_camp += 1 ###SOS###
        st.markdown(messages["step4"])
        options_format = messages["form_options"]
        multiple_formats = []
        for field_idx, camp in enumerate(select_camp):
            key_form = f"select_form_{idx}_{field_idx}"
            select_form = st.multiselect(key=key_form, label=messages["form_label"]+f"{camp}:", options=options_format, placeholder="", help="Define uno o más formatos de cada campo de interés respectivamente en la casilla correspondiente.")
            st.write(messages["selection"]+f"{select_form}")
            multiple_formats.append(select_form)
        select_form_global.append(multiple_formats)
    st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
    

##### GENERACIÓN DEL DICCIONARIO COMO .json #####
st.write(messages["part2_subtitle"])
if st.button(messages["gen_button"], type="secondary"):
    if len(select_docu) > 0 and len(select_clase) > 0  and len(select_camp_global) > 0 and len(select_form_global) > 0:
        json_dict = {}
        camp_form_dict_global = []
        for e in range(len(select_camp_global)):
            zipper = zip(select_camp_global[e], select_form_global[e])
            camp_form_dict = dict(zipper)
            camp_form_dict_global.append(camp_form_dict)
        for e in select_clase:
            json_dict[e] = camp_form_dict_global[select_clase.index(e)]
        st.write(messages["gen_run"])
        master_json_dict = {}
        master_json_dict[select_docu] = json_dict
        st.write(master_json_dict)
        dict_string = json.dumps(master_json_dict, indent=4, ensure_ascii=False)
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(dict_string)
        st.success(messages["gen_success"])
    else: st.write(messages["gen_exception"])



### FOOTER ###
# Añadir una linea separadora final con un pequeño comentario sobre el desarrollo
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
st.markdown(f"""<hr><small>{messages["footer"]}</small>""", unsafe_allow_html=True)