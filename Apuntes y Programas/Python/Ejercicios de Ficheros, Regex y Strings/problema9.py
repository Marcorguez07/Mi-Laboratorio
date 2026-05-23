# CS: Python, Regex + Txt Editing + Advanced Strings exercices by Marcokistan 2026

#---------------------------------------------------------------------------------

""" You have a text file that includes IP addresses in the format num.num.num.num (where each num is between 0 and 255). Write a function called recuperar_ips (recover_ips)
that receives an input filename and an output filename. The function must find all valid IP addresses and write them to the output file, one per line,
left-aligned in a field of 15 characters, followed by the text "IP". At the end, write "Total IPs:" followed by the total number found."""

import pathlib # Es mejor usar la librería pathlib
from pathlib import Path
import re

ruta_texto = Path.home() / "Desktop" / "Fichero" / "texto.txt"
ruta_escritura = Path.home() / "Desktop" / "Fichero" / "file1.txt"

def recuperar_ips(entrada, salida):
    texto = ""
    numero_de_ips = 0
    with open(entrada, "r", encoding="utf-8") as f:
        texto = f.read()
    argumento = r"(\d)+\.(\d)+\.(\d)+\.(\d)+"
    for coincidencia in re.finditer(argumento, texto):
        coincidencia_unraw = coincidencia.group(0)
        numero_de_ips += 1
        with open(salida, "a", encoding="utf-8") as g:
            g.write(f"{coincidencia_unraw:<15}IP\n")
    with open(salida, "a", encoding="utf-8") as l:
            l.write(f"Total IPS: {numero_de_ips}")
    return "completado"

print(recuperar_ips(ruta_texto,ruta_escritura))
