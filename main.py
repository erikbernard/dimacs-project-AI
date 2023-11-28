import random
from construir_grafo_m import *
from bfs_m import bfs
from dfs_m import dfs
from ucs_m import ucs
from A_star_m import A_star_harvesine, A_star_euclidian_distance
import csv


if __name__ == "__main__":
    arquivo_coordenadas = 'data/USA-road-d.W.co'
    arquivo_grafo = "data/USA-road-d.W.gr"
    graph = read_DIMACS_graph(arquivo_grafo)
    verticle_to_coordinates, coordinates_to_verticle = read_DIMACS_coordinates(arquivo_coordenadas)
    dict_graph = construir_dicionario(verticle_to_coordinates, graph)

    resultados = [['run', 'inicio_aleatorio', 'destino_aleatorio', 'algoritimo', 'nos_expandidos', 'memoria_usada', 'fator_de_ramificacao', 'tempo_execucao']]

    for i in range(2):
        coordinates = list(coordinates_to_verticle.keys())
        random_start = random.choice(coordinates)
        random_end = random.choice(coordinates)
        start_node  = graph[coordinates_to_verticle[random_start]][0]
        end_node = graph[coordinates_to_verticle[random_end]][0]

        print(f'run: {i+1}\nstart: {random_start}\nend: {random_end}\n')

        caminho_bfs, no_expandidos_bfs, memoria_usada_bfs, ramificacao_bfs, tempo_bfs = bfs(dict_graph, random_start, random_end, 10)
        resultados.append([str(i+1), str(random_start), str(random_end), 'BFS', str(no_expandidos_bfs), str(memoria_usada_bfs), str(ramificacao_bfs), str(tempo_bfs)])

        caminho_dfs, no_expandidos_dfs, memoria_usada_dfs, ramificacao_dfs, tempo_dfs = dfs(dict_graph, random_start, random_end, 10)
        resultados.append([str(i+1), str(random_start), str(random_end), 'DFS', str(no_expandidos_dfs), str(memoria_usada_dfs), str(ramificacao_dfs), str(tempo_dfs)])

        caminho_ucs, no_expandidos_ucs, memoria_usada_ucs, ramificacao_ucs, tempo_ucs = ucs(dict_graph, random_start, random_end, 10)
        resultados.append([str(i+1), str(random_start), str(random_end), 'UCS', str(no_expandidos_ucs), str(memoria_usada_ucs), str(ramificacao_ucs), str(tempo_ucs)])

        caminho_A_star_harvesine, no_expandidos_A_star_harvesine, memoria_usada_A_star_harvesine, ramificacao_A_star_harvesine, tempo_bfs_A_star_harvesine = A_star_harvesine(start_node, end_node, graph,  verticle_to_coordinates, 90)
        resultados.append([str(i+1), str(random_start), str(random_end), 'A_star_harvesine', str(no_expandidos_A_star_harvesine), str(memoria_usada_A_star_harvesine), str(ramificacao_A_star_harvesine), str(tempo_bfs_A_star_harvesine)])

        caminho_A_star_euclidian_distance, no_expandidos_A_star_euclidian_distance, memoria_usada_A_star_euclidian_distance, ramificacao_A_star_euclidian_distance, tempo_A_star_euclidian_distance = A_star_euclidian_distance(start_node, end_node, graph,  verticle_to_coordinates, 90)
        resultados.append([str(i+1), str(random_start), str(random_end), 'A_star_euclidian_distance', str(no_expandidos_A_star_euclidian_distance), str(memoria_usada_A_star_euclidian_distance), str(ramificacao_A_star_euclidian_distance), str(tempo_A_star_euclidian_distance)])

    with open('result_dataset.csv', mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for linha in resultados:
            escritor_csv.writerow(linha)