# CS: Python, Regex + Txt Editing + Advanced Strings exercices by Marcokistan 2026

#---------------------------------------------------------------------------------

"""Exercise 2

You have a text file that includes email addresses mixed with other words. Write a function called recuperar_correos (recover_emails) that receives an input filename
and an output filename. The function must find all valid email addresses (format: letters, numbers, dots, or hyphens, followed by @, followed by a domain with at
least one dot). In the output file, write them one per line, left-aligned in a field of 30 characters, followed by the text "OK". At the end, write the line
"Total emails:" followed by the total number of addresses found."""

import pathlib # Es mejor usar la librería pathlib
from pathlib import Path
import re

ruta_texto = Path.home() / "Desktop" / "Fichero" / "texto.txt"
ruta_escritura = Path.home() / "Desktop" / "Fichero" / "file1.txt"

def recuperar_correos(entrada,salida):
    guardar_texto = ""
    numerodecorreos = 0
    with open(entrada, "r", encoding="utf-8") as f:
        guardar_texto = f.read()
    argumento = r"(\w|[\.%_-])+(?=(@(\w|[%_-])+(\.)+(\w)+))@(\w|[%_-])+\.(\w)+"
    for coincidencia in re.finditer(argumento, guardar_texto):
        numerodecorreos += 1
        with open(salida, "a", encoding="utf-8") as g:
            converted_coincidencia = coincidencia.group(0)
            g.write(f"{converted_coincidencia:<50}")
            g.write("OK\n")
    with open(salida, "a", encoding="utf-8") as l:
        l.write(f"num de correos: {numerodecorreos}")
    return "Completado!"

print(recuperar_correos(ruta_texto,ruta_escritura))
