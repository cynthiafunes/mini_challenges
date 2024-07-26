# Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Implementar DFS
nodo_inicial = 'A'
pila = [nodo_inicial]
visitados = []

while pila:
    nodo = pila.pop()
    if nodo not in visitados:
        visitados.append(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                pila.append(vecino)

print("Recorrido DFS:", visitados)