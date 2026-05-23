# Ficheros de Texto Study Document

# By Marcokistan 2026, ULPGC CS student.

# Es posible leer y editar documentos de texto directamente en python, tambien es posible crearlos.

# -------------------------------------------------------------------------------------------------

# Lo primero que requerimos hacer es abrir un archivo de texto, un fichero basicamente. Para ello necesitamos conocer donde se encuentra, especificando su ruta.

import pathlib # Es mejor usar la librería pathlib
from pathlib import Path

ruta = Path.home() / "Desktop" / "pruebapython.txt"
string_añadir = "Hey!!"

# With es la funcion que usamos para abrir y cerrar automaticamente un documento.

#Modo de apertura:

# a -> append, añadir texto a la ultima linea
# w -> write, sobreescribe el documento, si no existe dicho documento lo crea
# r -> read, lee el documento

#Funciones

# .write -> permite escribir
# .read -> permite leer todo de una, es mala practica usar esto en documentos grandes

# .readline() -> Es para usar with como un bucle, cada uso de esta función baja una linea.
# .readlines() -> devuelve una lista en la que cada elemento es una linea formato string. SUPER UTIL!!!!!

# depende del modo de apertura estas funciones harán cosas diferentes.

#Encoding

#El español incluye carácteres especiales como la Ñ y las tildes, necesitamos siempre especificar el encoding en el tercer parametro de open().

# formato: with -> open() -> as "variable interna referencia al archivo"

if ruta.exists(): # si no existe que no haga nada
    with open(ruta, "a", encoding="utf-8") as f: # with abre el documento y lo cierra automaticamente al terminar la linea, incluso si hay un error lo cual es muy eficiente para no crashear.
        f.write(string_añadir)
        #print(f.read())
    with open(ruta, "r", encoding="utf-8") as f: # with abre el documento y lo cierra automaticamente al terminar la linea, incluso si hay un error lo cual es muy eficiente para no crashear.
        #f.write(string_añadir)
        print(f.read())

# ITERAR EN UN ARCHIVO DE TEXTO MOSTRARÁ LINEA A LINEA.

if ruta.exists(): # si no existe que no haga nada.
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            print(linea.strip()) # STRIP sirve por que si no los cambios de linea pueden afectar al FOR, recomiento siempre añadir los strip cuando iteremos.
