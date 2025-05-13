# Вариант 2
# Алгоритм Дейкстры


import sys

# ============================================


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]

def algoritm_d(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    predudushie_nodes = {}
    infinity_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = infinity_value
    shortest_path[start_node] = 0
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                predudushie_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)
    return predudushie_nodes, shortest_path

def print_result(predudushie_nodes, shortest_path, start_node, end_node):
    path = []
    node = end_node
    print("Начало: ", start_node)
    print("Конец: ", end_node)

    print("Наикратчайшая длина и наикратчайший маршрут: {}.".format(shortest_path[end_node]))
    while node != start_node:
        path.append(node)
        node = predudushie_nodes[node]
        path.append(start_node)

        print(" -> ".join(reversed(path)))

# Вершины
nodes = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16',
         'v17', 'v18', 'v19', 'v20', 'v21']

init_graph = {}
for node in nodes:
    init_graph[node] = {}

# Рёбра
init_graph['v1']['v2'] = 3
init_graph['v1']['v3'] = 65
init_graph['v1']['v4'] = 70
init_graph['v2']['v3'] = 70
init_graph['v2']['v4'] = 2
init_graph['v3']['v4'] = 78
init_graph['v3']['v5'] = 6
init_graph['v3']['v6'] = 77
init_graph['v4']['v6'] = 1
init_graph['v4']['v5'] = 78
init_graph['v5']['v13'] = 5
init_graph['v5']['v6'] = 75
init_graph['v5']['v21'] = 70
init_graph['v5']['v8'] = 76
init_graph['v6']['v7'] = 1
init_graph['v6']['v21'] = 77
init_graph['v7']['v21'] = 78
init_graph['v7']['v9'] = 1
init_graph['v7']['v12'] = 77
init_graph['v8']['v14'] = 4
init_graph['v8']['v21'] = 6
init_graph['v9']['v10'] = 7
init_graph['v9']['v12'] = 70
init_graph['v10']['v11'] = 5
init_graph['v10']['v12'] = 80
init_graph['v11']['v12'] = 4
init_graph['v12']['v8'] = 5
init_graph['v13']['v15'] = 4
init_graph['v15']['v16'] = 4
init_graph['v15']['v17'] = 7
init_graph['v16']['v17'] = 2
init_graph['v17']['v18'] = 1
init_graph['v17']['v19'] = 3
init_graph['v18']['v19'] = 1
init_graph['v19']['v14'] = 7
init_graph['v14']['v20'] = 4
init_graph['v19']['v20'] = 2

# Начальная вершина
start_node = nodes[0]
# Конечная вершина
end_node = nodes[-1]

graph = Graph(nodes, init_graph)
predudushie_nodes, shortest_path = algoritm_d(graph=graph, start_node='v1')
print_result(predudushie_nodes, shortest_path, start_node='v1', end_node='v3')

# ==============================================
