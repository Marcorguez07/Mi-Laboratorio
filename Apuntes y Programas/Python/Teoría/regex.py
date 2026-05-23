# Regex Study Document

# By Marcokistan 2026, ULPGC CS student.

# Regex nos permite buscar palabras o patrones en una string

# ----------------------------------------------------------

# --------- Teoría

# FLAGS: Metodos de Busqueda

# - No flag: Encuentra solo la primera aparición
# - Global: incluye todas las apariciones
# - Case Insensitive: NO importan las mayusculas o minusculas
# - Multiline: permite que el motor de busqueda trate a cada linea de forma individual

# Las regex se escriben dentro del intervalo //. Los tokens son las palabras,
# caracteres o letras que queremos buscar.

# OPERADORES, ASOCIADORES Y SELECTORES, (OP),(AC) y (SE)

#-----OPERADORES FIJOS (VAN DESPUES DEL TOKEN)
# + -> 1 O más del token, a+ -> aaaaaaa (incluye todas las a)
# ? -> Opcional token, incluye un token opcional (una letra)
# * -> Expande el operador ? para incluir 1 o más del token opcional, si no encuentra no pasa nada.
#-----OPERADORES FIJOS (VAN ENTRE TOKEN Y TOKEN)
# | -> Operador Booleano OR, hay que tener en cuenta que en REGEX actua como AND por que es un motor de inclusión.
#-----OPERADORES LIBRES (Se pueden poner DETRAS o DELANTE, y su posicionamiento importa)
# . -> Incluye un carácter, NO puede incluir NEWLINES, si incluyese un solo NEWLINE toda la selección se cancela
# [] -> Significa set y cada letra añadida itera
# () -> Nos permite agrupar
# (?<=("newtoken")) -> Va detras del TOKEN y permite incluir una palabra SI Y SOLO SI la expresion que esta detras es NEWTOKEN., cambiar "=" por "!" la invierte.
# (?=("newtoken")) -> Va despues del TOKEN y permite incluir una palabra SI Y SOLO SI la expresion que esta despues es NEWTOKEN., cambiar "=" por "!" la invierte.
#-----SELECTORES
# \w -> Devuelve cualquier LETRA o NÚMERO, W mayuscula hace lo contrario 
# \s -> Devuelve todos los espacios, S mayuscula hace lo contrario
# \d -> Devuelve cualquier digito, SOLO digitos.
#-----ASOCIADORES
# {} -> Significa rango, nos permite encontrar un patron con un número determinado de cáracteres. Es importante por que si no las funciones de busqueda solo nos incluiran el primer carácter.

# ------------- PYTHON IMPLEMENTACIÓN

import re # importamos libreria EXPRESIONES REGULARES

# se importa una string, por ejemplo:

string1 = """En el vasto universo de la comunicación digital, la gestión de datos se ha vuelto fundamental. Imagina que estás auditando una base de datos antigua y encuentras fragmentos de registros como este: "El usuario juan.perez23@gmail.com inició sesión a las 09:00 AM". Sin embargo, no todos los registros son tan limpios. A veces, la información se mezcla con notas al pie, como cuando el coordinador técnico, cuyo correo es soporte.tecnico.ayuda@gmail.com, menciona que hubo un error en el servidor 404.
Es común encontrar errores de formato. Por ejemplo, alguien podría escribir usuario@gmail sin el dominio completo, o quizás error-de-envio@gmail.co olvidando la última letra. Estos casos no deberían ser capturados por una regex estricta de Gmail. Por otro lado, tenemos contactos legítimos que usan puntos o guiones, tales como maria_luz_99@gmail.com o el siempre confiable test-user.123@gmail.com, quienes enviaron sus reportes a tiempo.
Durante la convención de tecnología, se distribuyeron volantes con direcciones de otros proveedores, como contacto.empresa@outlook.com y ventas.globales@yahoo.es. Estos son correos válidos, pero si tu objetivo es solo filtrar Gmail, tu patrón de búsqueda debe ser preciso. Incluso podrías toparte con cadenas extrañas como info@gmail.com.ar, que aunque contiene la cadena buscada, pertenece a un dominio regional diferente.
Finalmente, para cerrar este registro, el administrador del sistema dejó una nota: "Para cualquier duda adicional, contactar a coordinacion.general.2024@gmail.com o revisar el log interno". No olvides que la estructura local de un correo puede ser compleja, permitiendo caracteres como el signo más, por ejemplo: mi.nombre+etiqueta@gmail.com. ¡Buena suerte con tu filtrado!"""

# Para buscar con expresiones regulares usamos funciones especiales de la libreria "re" importada, aunque primero necesitamos establecer nuestro argumento de busqueda en sí

patron1 = r"" # el patron va dentro de r"". 

# re.search("patron1, string1") #Esta es una funcion de busqueda, que solo pilla la primera coincidencia
# re.findall() # busca TODAS las coincidencias, representa la FLAG global, que en python no existe. NO ACONSEJO USAR ESTA EN PYTHON.
# re.finditer() # la mas parecida a regex.

# Si queremos aplicar flags reales, se le pasa como tercer parametro a la función de busqueda.

#------------------------------------------------

patrondebusqueda = r"(\w|[\.%_])+(?=(@gmail\.com))@gmail.com"
# esta es la mejor manera de buscar, iterando a todas las coincidencias, el grupo 0 SIEMPRE es LA AGRUPACIÓN completa.
for coincidencia in re.finditer(patrondebusqueda, string1):
    print(coincidencia.group(0))
