# CS: Python, Regex + Txt Editing + Advanced Strings exercices by Marcokistan 2026

#---------------------------------------------------------------------------------

"""Exercise 4
You have a text file that includes dates in the format dd/mm/yyyy. Write a function called normalizar_fechas (normalize_dates) that receives an input filename and
an output filename. The function must find all valid dates from 01/01/2000 onwards (inclusive) and write them into the output file in yyyy-mm-dd format,
one per line, right-aligned in a field of 12 characters. At the end, write "Total dates:" followed by the total number found."""


import pathlib # Es mejor usar la librería pathlib
from pathlib import Path
import re

ruta_entrada = Path.home() / "Desktop" / "Fichero" / "texto.txt"
ruta_salida = Path.home() / "Desktop" / "Fichero" / "file1.txt"

def normalizar_fechas(entrada,salida):
    argumento = r"\d{2}-\d{2}-20\d{2}"
    numero_de_fechas = 0
    guardar_texto = ""
    with open(entrada, "r", encoding="utf-8") as reading:
        guardar_texto = reading.read()
    for coincidencia in re.finditer(argumento, guardar_texto):
        numero_de_fechas += 1
        with open(salida, "a" , encoding="utf-8") as f:
            #print(coincidencia)
            coincidencia_unraw = coincidencia.group(0)
            año = coincidencia_unraw[6:]
            mes = coincidencia_unraw[3:5]
            dia = coincidencia_unraw[0:2]
            fecha_nueva = f"{año}-{mes}-{dia}"
            f.write(f"{fecha_nueva:>12}\n")
    with open(salida, "a" , encoding="utf-8") as g:
        g.write(f"Total fechas: {numero_de_fechas}")
    return "completado"

print(normalizar_fechas(ruta_entrada,ruta_salida))


        
