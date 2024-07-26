#Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos.

pila = []

pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
pila.append(5)

print("Elementos de la pila:")
while pila:
    print(pila.pop())

cola = []

cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)
cola.append(5)

print("Elementos de la cola:")
while cola:
    print(cola.pop(0))