# Búsqueda en lista ordenada: Implementa una función de búsqueda binaria 
# que determine si un número está en una lista ordenada de 10 elementos.

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
objetivo = 15
resultado = busqueda_binaria(lista, objetivo)

if resultado == True:
    print(f"El numero {objetivo} está en la lista")
else:
    print(f"El numero {objetivo} no está en la lista")
