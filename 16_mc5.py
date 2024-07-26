#Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas
#escribe una función que encuentre el camino más corto entre dos nodos especificados usando cualquier método que prefieras.

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

nodo_inicial = 'A'
nodo_final = 'F'
cola = [[nodo_inicial]]
visitados = []

while cola:
    camino = cola.pop(0)
    nodo = camino[-1]
    if nodo not in visitados:
        vecinos = grafo[nodo]
        for vecino in vecinos:
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            cola.append(nuevo_camino)
            if vecino == nodo_final:
                print("Camino mas corto:", nuevo_camino)
                cola = []
                break
        visitados.append(nodo)

