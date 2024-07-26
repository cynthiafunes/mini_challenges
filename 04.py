#Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente

def ordenar_lista(lista):
    lista_temporal = []

    while lista:
        actual = lista.pop()  
        while lista_temporal and lista_temporal[-1] > actual:
            lista.append(lista_temporal.pop())
        lista_temporal.append(actual)
    return lista_temporal

entrada_usuario = input("Ingrese los números separados por espacios: ")
numeros = [int(numero) for numero in entrada_usuario.split()]

numeros_ordenados = ordenar_lista(numeros)
print("Lista ordenada:", numeros_ordenados)
