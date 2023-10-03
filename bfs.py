from collections import deque

def read_DIMACS_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('c'):
                continue  # Ignorar comentários
            elif line.startswith('p'):
                parts = line.split()
                num_nodes = int(parts[2])
                for i in range(1, num_nodes + 1):
                    graph[i] = []
            elif line.startswith('a'):
                parts = line.split()
                source = int(parts[1])
                target = int(parts[2])
                weight = int(parts[3])
                graph[source].append((target, weight))
    return graph

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        if current_node == end:
            return path
        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node]
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

    return None


if __name__ == "__main__":
    file_path = "USA-road-d.NY.gr"   # Coloque o caminho correto para o arquivo
    graph = read_DIMACS_graph(file_path)

    source_node = 1  # Escolha o nó de origem
    target_node = 1000  # Escolha o nó de destino

    shortest_path = bfs_shortest_path(graph, source_node, target_node)
    if shortest_path:
        print("Caminho mais curto:", shortest_path)
    else:
        print("F Família: ")
