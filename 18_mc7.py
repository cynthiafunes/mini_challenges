#Piloto de eventos (Priority Queue): Implementa una cola de prioridad utilizando una lista 
# para insertar y eliminar 5 elementos.

cola_prioridad = []

def insertar(cola, elemento, prioridad):
    cola.append((prioridad, elemento))
    cola.sort(reverse=True)  # Ordenar por prioridad

def eliminar(cola):
    return cola.pop(0)

insertar(cola_prioridad, 'A', 1)
insertar(cola_prioridad, 'B', 3)
insertar(cola_prioridad, 'C', 2)
insertar(cola_prioridad, 'D', 5)
insertar(cola_prioridad, 'E', 4)

print(eliminar(cola_prioridad))
print(eliminar(cola_prioridad))
print(eliminar(cola_prioridad))
print(eliminar(cola_prioridad))
print(eliminar(cola_prioridad))