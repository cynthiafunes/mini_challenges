# Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros 
# utilizando cualquier método de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección).

def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

lista_enteros = [50, 30, 60, 40, 70]
ordenamiento_seleccion(lista_enteros)
print("Lista ordenada:", lista_enteros) 
