#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#------------------------------------CODIGO-------------------------------------
import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(graph):
    mst = nx.Graph()  # Grafo para el árbol de expansión mínima
    visited = set()   # Conjunto de nodos visitados
    edges = []        # Lista de aristas a considerar

    # Elegimos un nodo arbitrario como el nodo inicial
    start_node = list(graph.nodes())[0]
    visited.add(start_node)
    for neighbor, weight in graph[start_node].items():
        edges.append((weight['weight'], start_node, neighbor))
    
    while edges:
        # Ordenar aristas por peso y seleccionar la arista con el menor peso
        edges.sort()
        weight, u, v = edges.pop(0)

        if v not in visited:
            visited.add(v)
            mst.add_edge(u, v, weight=weight)

            for next_neighbor, next_weight in graph[v].items():
                if next_neighbor not in visited:
                    edges.append((next_weight['weight'], v, next_neighbor))

    return mst

def draw_graph(graph, title):
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

# Crear un grafo de ejemplo
graph = nx.Graph()
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6)
]

graph.add_weighted_edges_from(edges)

# Calcular el Árbol de Expansión Mínima usando el algoritmo de Prim
mst = prim_mst(graph)

# Dibujar el grafo original
draw_graph(graph, "Grafo Original")

# Dibujar el Árbol de Expansión Mínima
draw_graph(mst, "Árbol de Expansión Mínima (Prim)")