# CS: Python, Regex + Txt Editing + Advanced Strings exercices by Marcokistan 2026

#---------------------------------------------------------------------------------

"""You have a text file containing student IDs (DNI) and names separated by semicolons (one per line), and a dictionary in memory with grades where the key is the DNI.
Write a function called generar_informe_notas (generate_grade_report) that receives the filename and the dictionary. The function must cross-reference the data: for
each student in the file, look up their grade in the dictionary and write a line in a new file with the format "Student: Grade". If a student is not in the dictionary,
write "Student: NO GRADE". At the end, write "Total students:" followed by the total number processed."""

import pathlib # Es mejor usar la librería pathlib
from pathlib import Path
import re

ruta_texto = Path.home() / "Desktop" / "Fichero" / "DNI_Nombre.txt"
ruta_escritura = Path.home() / "Desktop" / "Fichero" / "file1.txt"

# Diccionario de alumnos: Clave (DNI) y Valor (Nota float)
notas_alumnos = {
    "12345678A": 8.5,
    "87654321B": 9.2,
    "11223344C": 6.7,
    "55667788D": 4.5,
    "99887766E": 7.8,
    "22334455F": 5.9,
    "66778899G": 3.4,
    "33445566H": 8.1,
    "00112233J": 10.0,
    "44556677K": 6.2,
    "77889900L": 7.4,
    "55443322M": 9.5,
    "99001122N": 4.0,
    "33221100P": 5.0,
    "88779955Q": 6.8,
    "22114433R": 7.2,
    "66554411S": 2.5
}

def generar_informe_notas(entrada,salida,dic):
    lista_de_nombres = []
    lista_de_DNI = []
    argumento_nombres = r"(?<=(;))([a-zA-z áíóúéÁÉÍÓÚñ])+"
    argumento_DNI = r"(\d)+\w(?=(;))"
    texto = ""
    with open(entrada , "r" , encoding="utf-8") as f:
        texto = f.read()
    for coincidencia_nombres in re.finditer(argumento_nombres, texto):
        coincidencia_unraw_nombres = coincidencia_nombres.group(0)
        lista_de_nombres.append(coincidencia_unraw_nombres)
    for coincidencia_DNI in re.finditer(argumento_DNI, texto):
        coincidencia_unraw_DNI = coincidencia_DNI.group(0)
        lista_de_DNI.append(coincidencia_unraw_DNI)
    indice = 0
    for elemento in lista_de_nombres:
        try:
            nota = dic[lista_de_DNI[indice]]
            with open(salida, "a", encoding="utf-8") as g:
                g.write(f"{elemento:<40}Nota:{nota}\n")
            indice += 1
        except:
            with open(salida, "a", encoding="utf-8") as g:
                g.write(f"{elemento:<40}Nota:SIN NOTA\n")
    return "completado"


print(generar_informe_notas(ruta_texto,ruta_escritura,notas_alumnos))

