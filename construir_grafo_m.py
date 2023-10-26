def ler_arquivo_coordenadas(arquivo_coordenadas):
    coordenadas = {}

    with open(arquivo_coordenadas, 'r') as arquivo:
        for linha in arquivo:
            if linha.startswith('v'):
                partes = linha.strip().split()
                node_id = int(partes[1])
                latitude = int(partes[3]) / 1000000
                longitude = int(partes[2]) / 1000000
                coordenadas[node_id] = (latitude, longitude)

    return coordenadas

def ler_arquivo_grafo(arquivo_grafo):
    grafo = {}

    with open(arquivo_grafo, 'r') as arquivo:
        for linha in arquivo:
            if linha.startswith('a'):
                partes = linha.strip().split()
                node_id_origem = int(partes[1])
                node_id_destino = int(partes[2])
                distancia = int(partes[3])

                if node_id_origem not in grafo:
                    grafo[node_id_origem] = {}
                grafo[node_id_origem][node_id_destino] = distancia

    return grafo


def construir_grafo(arquivo_coordenadas, arquivo_grafo):
    coordenadas = ler_arquivo_coordenadas(arquivo_coordenadas)
    grafo = ler_arquivo_grafo(arquivo_grafo)
    node = 1
    grafo_final = []

    for node_id, vizinhos in grafo.items():
        for vizinho_id in vizinhos.keys():
            distancia = vizinhos[vizinho_id]
            coordenadas_origem = coordenadas.get(node_id)
            coordenadas_destino = coordenadas.get(vizinho_id)
            node= node+1

            # grafo_final.append({f"Origem: {node_id}, Coordenadas: {coordenadas_origem}, Destino: {vizinho_id}, Coordenadas: {coordenadas_destino}, Distância: {distancia}"})
            grafo_final.append(
              {
                      'Origem':node_id,
                      'Destino':vizinho_id,
                      'distancia': distancia,
                      'coordenada_origem': coordenadas_origem,
                      'coordenada_destino': coordenadas_destino
              }
            )
    return grafo_final

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
                graph[source].append([target, weight])
    return graph

def read_DIMACS_coordinates(file_path):
    verticle_to_coordinates = {}
    coordinates_to_verticle = {}

    file = open(file_path, 'r')
    lines = file.read().splitlines()
    for line in lines:
        if line.startswith('c'):
            continue  # Ignorar comentários
        elif line.startswith('p'):
            parts = line.split()
            num_nodes = int(parts[4])
            for i in range(1, num_nodes + 1):
                verticle_to_coordinates[i] = []
        elif line.startswith('v'):
            parts = line.split()
            verticle = int(parts[1])
            lat = int(parts[3]) / 1000000
            lon = int(parts[2]) / 1000000
            verticle_to_coordinates[verticle].append((lat, lon))
            coordinates_to_verticle[(lat, lon)] = verticle
    return verticle_to_coordinates, coordinates_to_verticle