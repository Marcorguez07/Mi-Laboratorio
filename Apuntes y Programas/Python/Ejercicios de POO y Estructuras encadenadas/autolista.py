# Auto - encadenador de estructuras
# Marcokistan 2026

# Tu creas los objetos y los juntará automaticamente

class Node:
    head = True
    beforedato = None
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        if Node.head == True:
            Node.beforedato = self
            Node.head = False
        else:
            Node.beforedato.siguiente = self
            Node.beforedato = self


nodo1 = Node("Manzana")
nodo2 = Node("Pera")
nodo3 = Node("Plátano")
nodo4 = Node("Manzana")
nodo5 = Node("Pera")
nodo6 = Node("Plátano")
nodo7 = Node("Manzana")
nodo8 = Node("Pera")
nodo9 = Node("Plátano")

print(nodo1.siguiente)
print(nodo2.siguiente)
print(nodo3.siguiente)
print(nodo4.siguiente)
print(nodo5.siguiente)
print(nodo6.siguiente)
print(nodo7.siguiente)
print(nodo8.siguiente)
print(nodo9.siguiente)


            
            
    
