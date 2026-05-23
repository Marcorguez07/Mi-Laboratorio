# CS: Python, Regex + Txt Editing + Advanced Strings exercices by Marcokistan 2026

#---------------------------------------------------------------------------------

"""Exercise 1

You have a list of integers.

Write a function called guardar_enteros (save_integers) that receives the list and two filenames. The function must write the even numbers to the first file and the odd numbers to the second, one per line, right-aligned in a field of 6 characters.

Write another function called leer_enteros (read_integers) that receives the names of two files. It must read the files and return a list of strings formed by concatenating
an even number from the first file with an odd number from the second. If one file ends before the other, continue with the remaining file until the end is reached."""


import pathlib # Es mejor usar la librería pathlib
from pathlib import Path
lista_de_enteros = ["1","2","3","4","5","6","7","8","9","10"]
def leer_enteros(y,z):
    rango = 0
    nuevalista = []
    ruta_par = Path.home() / "Desktop" / "Fichero" / f"{y}"
    ruta_impar = Path.home() / "Desktop" / "Fichero" / f"{z}"
    with open(ruta_par, "r", encoding="utf-8") as f:
        lista_de_pares = f.readlines()
    with open(ruta_impar, "r", encoding="utf-8") as g:
        lista_de_impares = g.readlines()
    maxiter_par = len(lista_de_pares)
    maxiter_impar = len(lista_de_impares)
    for elemento in lista_de_pares:
        rango += 1
        try:
            elementoconcat = elemento.strip() + lista_de_impares[rango].strip()
            nuevalista.append(elementoconcat)
        except:
            nuevalista.append(elemento.strip())
    return nuevalista
def guardar_enteros(x,y,z):
    ruta_par = Path.home() / "Desktop" / "Fichero" / f"{y}"
    ruta_impar = Path.home() / "Desktop" / "Fichero" / f"{z}"
    for elemento in x:
        if int(elemento) % 2 != 0:
            with open(ruta_impar, "a", encoding="utf-8") as f:
                f.write(f"{elemento:>6}\n")
        else:
            with open(ruta_par, "a", encoding="utf-8") as g:
                g.write(f"{elemento:>6}\n")
                listaconcatenada = leer_enteros(y,z)
    return listaconcatenada

print(guardar_enteros(lista_de_enteros,"file1.txt","file2.txt"))
