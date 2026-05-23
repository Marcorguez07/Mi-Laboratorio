# CS: Dictionaries by Marcokistan 2026

#---------------------------------------------------------------------------------

# Si tuviera que resumir los diccionarios, diría que son secuencias con un
# nivel de acceso más sencillo y fácil de entender.

# Los diccionarios tienen KEYS y VALORES. Los keys señalan directamente a los valores.

#Las KEYS van entre "", acompañadas de un : que señala AL valor, despues se añade la coma y será el siguiente valor del indice.

Diccionario1 = {}
Diccionario1["hola"] = 3
hola = Diccionario1.pop("hola")
print(hola)
print(Diccionario1)

#Si se desea crear un diccionario a partir de elementos de una lista o una tupla, es mejor crear el diccionario de la forma: var = dict(x)
#Si queremos pasarle una lista por ejemplo:

nuevalista = [(1,2),(2,1),(3,1)] #NOTA: Para crear un diccionario el diccionario necesita añadir un valor KEY asi que la unica manera de pasar una lista a un dict
# es agrupando en pares. Esto significa que solo podemos pasar listas de listas o de tuplas. El valor de indice 0 de cada tupla o lista se convertira en KEY mientras
#el valor 1 en el indice será el elemento señalado.
d = dict(nuevalista)
print(d)

# Es posible iterar sobre un diccionario, nos dará los valores en claves.
for iterado in d:
    print(iterado)

#Cuando las claves son strings, se pueden usar como "parámetros por nombre" en dict():
    
g = dict(Michael=77, Peter=66, Patrick=82)
print(g)
print(g["Peter"])

########################
# Conjuntos

#Si tuviera que resumir los conjuntos yo diría que son secuencias a las que
# se les puede aplicar lógica de conjuntos y que no permiten elementos repetidos

# para crear un conjunto se usa ([, excepto si usamos una string directamente.

conjunto1 = set(["1","2","3","4"])
conjunto2 = set(["2","3","5","6"])
print(type(conjunto1))
print("Muchas operaciones aqui")

a = conjunto1 | conjunto2 # Unión, junta los elementos de cada set
b = conjunto1 & conjunto2 # Disyunción, solo imprime los elementos que estan en ambos
c = conjunto1 ^ conjunto2 # Diferencia simetrica, es una unión que excluye a los que se encuentran en ambos
d = conjunto1 - conjunto2 # Diferencia, imprimirá los elementos de conjunto1 que no esten presentes en conjunto2

print(a)
print(b)
print(c)
print(d)

# Nos va a dar cada operacion en un orden aleatorio, por que un conjunto NUNCA
# es ordenado.

conjunto3 = set("playa")
print(conjunto3)

# Es posible iterar sobre un conjunto, nos devolverá cada elemento, como si fuese una secuencia.

for iterado in conjunto3:
    print(iterado)

# la "a" se repite dos veces en la palabra "playa", el conjunto 3 solo es un grupo
# de caracteres, por lo que la "a" solo aparecerá una vez.

# -------------------------------------------------------
# Obtención de datos en Diccionarios/conjuntos

# Es posible comprobar si una key existe en un Diccionario, usando el metodo .get(), para que si no encuentra la key nos devuelva None
# en vez de KeyError

Dict = {hello: "123"}
Dict.get(hola)

#SI la clave no existe y no queremos que nos devuelva NONE, tambien podemos especificar un valor que nos devuelva.

#En cuanto al tamaño de un diccionario/conjunto, el tamaño de un diccionario/conjunto se puede averiguar usando len().



