#Eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.

lista = [1, 2, 3, 2, 4, 5, 6, 5, 7, 8]

nueva_lista = []
for elemento in lista:
    if elemento not in nueva_lista:
        nueva_lista.append(elemento)

print("Lista sin duplicados:", nueva_lista)