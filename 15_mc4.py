# Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Implementar BFS
nodo_inicial = 'A'
cola = [nodo_inicial]
visitados = []

while cola:
    nodo = cola.pop(0)
    if nodo not in visitados:
        visitados.append(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                cola.append(vecino)

print("Recorrido BFS:", visitados)
