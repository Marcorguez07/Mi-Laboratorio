# DOCUMENTO DE ESTUDIO
# MARCOKISTAN 2026

# CLASES

""" En python prácticamente todo, excepto las funciones, las llamadas y control-
adores de control... son clases.

Las variables apuntan a un objeto, en nuestra cabeza la sintaxis es:
variable = objeto

Sin embargo, esto no es del todo correcto, si es cierto que apuntan a un objeto,
pero, el objeto esta generado por una clase, asi que se podria decir que, las
variables solo estan apuntando a objetos de clases, o para resumir, a clases.

Los int, bool, str, todos estos son clases.

LA PROGRAMACIÓN ORIENTADA A OBJETOS, nos permite crear nuestras propias clases,
con las cuales nuestras variables pueden apuntar a ellas para crear objetos
de esas mismas clases"""

class prueba:
    def __init__(self, nombre): # todas las funciones escritas dentro de una clase se llaman metodos
        self._nombre = nombre

variable_cualquiera = prueba(Pepe)

# Esta es la clase más simple posible, el parametro self es VITAL, ya que representa una orden
# interna de solo afectar a la variable DEL OBJETO ACTUALMENTE SELECCIONADO, y evitar las otras
# clases.

# Una manera interesante de ver esto, es imaginandose que self toma el valor del nom
# bre del objeto actualmente seleccionado. Internamente ocurre así.

######################################

# GETTERS Y SETTERS

# Son formas automaticas de obtener/settear un dato dependiendo de la necesidad
# el getter se ejecutará siempre que se pida leer un dato, y setter siempre se ejecutará
# cuando se necesite modificar.

# el getter se llama escribiendo exclusivamente -> @property
# el setter se llama escribiendo el metodo nombrado en el getter, seguido de .setter

class prueba_un_poco_mejor:
    def __init__(self, nombre): # todas las funciones escritas dentro de una clase se llaman metodos
        self._nombre = nombre
    @property
    def av_nombre(self): # ESTE ES EL GETTER
        return self._nombre
    @av_nombre.setter
    def av_nombre(self, valor_para_modificar): # ESTE ES EL SETTER
        self._nombre = valor_para_modificar

# ATRIBUTOS Y METODOS DE CLASE

# Los atributos de clase son simplemente variables dadas a todos los objetos de una clase, sin más.

# ATRIBUTOS DE CLASE SOLO EJECUTADOS UNA VEZ: ya que python es un lenguaje interpretado, lee
# linea a linea, cuando se topa con una clase, la lee y guarda en su memoria los atributos
# pero no ejecuta la clase todavía, esto nos sirve para ejecutar, dentro de una clase misma
# atributos que solo se llamarán una vez, lo que nos permite declarar variables GLOBALES dentro
# de una clase, sin necesidad de ponerlos en el scope global del programa.
# Al crear una objeto con esa clase, el objeto ejecuta el metodo init, nunca va a ejecutar estos
# atributos globales.

# los metodos de clase son especiales, una vez ejecutado en un solo objeto, se ejecuta en todos los de esa clase

# para crear uno, escribimos -> @classmethod
# el metodo, no puede tener el parametro objeto (self), debera tener el parametro clase (cls).
# el parametro objeto, nosotros le podemos dar el nombre que queramos, a diferencia del
# parametro clase.

#######################################

# METODOS SHINY

# REPRESENTACIÓN INFORMAL: Sirve para que cuando hagamos print al objeto, nos imprima esto en vez
# de su dirección en memoria.

    def __str__(self):
        return f"hola"
        

variable_cualquiera = prueba(Pepe)
