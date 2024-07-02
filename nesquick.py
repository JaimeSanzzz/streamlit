import json

with open('blocks.txt', 'r', encoding="utf-8") as file:
    file_contents = file.read()
json_data = json.loads(file_contents)
print(json_data)

flujoBlock1 = json_data["Analisis de documentos"]
flujoBlock2 = json_data["Deteccion de firmas"]
flujoBlock3 = json_data["Resumen de contenidos"]
flujoBlock4 = json_data["Analisis de sentimientos"]
flujoBlock5 = json_data["Deteccion de fraude"]
flujoBlock6 = json_data["Interpretacion de resultados"]

if flujoBlock1 == "TRUE":
    print("# CORRER TODO EL BLOQUE 1")
else: 
    print("# PASAR AL BLOQUE 2")
 
if flujoBlock2 == "TRUE":
    print("# CORRER TODO EL BLOQUE 2")
else: 
    print("# PASAR AL BLOQUE 3")
