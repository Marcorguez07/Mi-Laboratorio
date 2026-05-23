# CS: Python, Regex + Txt Editing + Advanced Strings exercices by Marcokistan 2026

#---------------------------------------------------------------------------------

"""Exercise 8
You have a list of tuples, where each tuple contains (name, age). There may be duplicate names.

Write a function called guardar_personas (save_people) that receives the list and a filename. The function must write each person on a line with the format
"<Name> - <Age> years". People who have already been written to the file should not be written again.
Write another function called leer_personas (read_people) that receives a filename, reads it, and returns a list of tuples with the data."""

import pathlib # Es mejor usar la librería pathlib
from pathlib import Path
import re

lista_personas = [("Marco",18),("Furius",3),("Zenon",600),("Marco",16),("Carlitos",4000)]

#ruta_entrada = Path.home() / "Desktop" / "Fichero" / "texto.txt"
ruta_salida = Path.home() / "Desktop" / "Fichero" / "file1.txt"

def leer_personas(entrada):
    texto = ""
    with open(entrada, "r", encoding="utf-8") as f:
        texto = f.read()
    busqueda_nombres = r"(?<=(\<))([a-zA-Z]+)"
    busqueda_edad = r"(\d)+"
    lista_de_nombres = []
    lista_de_edades = []
    for coincidencia_nombres in re.finditer(busqueda_nombres, texto):
        coincidencia_unraw = coincidencia_nombres.group(0)
        lista_de_nombres.append(coincidencia_unraw)
    for coincidencia_edades in re.finditer(busqueda_edad, texto):
        coincidencia_unraw2 = coincidencia_edades.group(0)
        lista_de_edades.append(coincidencia_unraw2)
    indice = 0
    lista_final = []
    for elemento in lista_de_nombres:
        lista_final.append((elemento, lista_de_edades[indice]))
        indice += 1
        print(lista_final)
        print(indice)
    return lista_final

def guardar_personas(lista,salida):
    lista_auxiliar = []
    for tupla in lista:
        nombre = tupla[0]
        edad = tupla[1]
        if nombre in lista_auxiliar:
            pass
        else:
            lista_auxiliar.append(nombre)
            with open(salida, "a",encoding="utf-8") as f:
                f.write(f"<{nombre}>-<{edad}>años\n")
    lista_corregida = leer_personas(salida)
    return lista_corregida

print(guardar_personas(lista_personas,ruta_salida))

