#Árbol binario de búsqueda (BST): Implementa solo la inserción en un árbol binario de búsqueda para 5 elementos.

class Nodo:
    def __init__(self, valor):
        self.izquierdo = None
        self.derecho = None
        self.valor = valor

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    else:
        if valor < raiz.valor:
            raiz.izquierdo = insertar(raiz.izquierdo, valor)
        else:
            raiz.derecho = insertar(raiz.derecho, valor)
    return raiz

valores = [10, 5, 15, 3, 7]
raiz = None
for valor in valores:
    raiz = insertar(raiz, valor)

def preorden(nodo):
    if nodo:
        print(nodo.valor)
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

preorden(raiz)
