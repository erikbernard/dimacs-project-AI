import random
from construir_grafo_m import *
from bfs_m import bfs
from dfs_m import dfs
from ucs_m import ucs
from A_star_m import A_star_harvesine, A_star_euclidian_distance


if __name__ == "__main__":
    arquivo_coordenadas = 'data/USA-road-d.W.co'
    arquivo_grafo = "data/USA-road-d.W.gr"
    graph = read_DIMACS_graph(arquivo_grafo)
    verticle_to_coordinates, coordinates_to_verticle = read_DIMACS_coordinates(arquivo_coordenadas)
    list_dict = construir_grafo(arquivo_coordenadas, arquivo_grafo)

    for i in range(50):
        coordinates = list(coordinates_to_verticle.keys())
        random_start = random.choice(coordinates)
        random_end = random.choice(coordinates)
        start_node  = graph[coordinates_to_verticle[random_start]][0]
        end_node = graph[coordinates_to_verticle[random_end]][0]

        caminho_bfs, no_expandidos_bfs, memoria_usada_bfs = bfs(list_dict, random_start, random_end, 30)
        caminho_dfs, no_expandidos_dfs, memoria_usada_dfs = dfs(list_dict, random_start, random_end, 30)
        caminho_ucs, no_expandidos_ucs, memoria_usada_ucs = ucs(list_dict, random_start, random_end, 30)
        caminho_A_star_harvesine, no_expandidos_A_star_harvesine, memoria_usada_A_star_harvesine = A_star_harvesine(start_node, end_node, graph,  verticle_to_coordinates, 30)
        caminho_A_star_euclidian_distance, no_expandidos_A_star_euclidian_distance, memoria_usada_A_star_euclidian_distance = A_star_euclidian_distance(start_node, end_node, graph,  verticle_to_coordinates, 30)

        print("Rodada : " + str(i) + " " + "Partida : " + str(random_start) + " " + "Chegada : " + str(random_end))

        # print("Rodada : " + str(i) + " " + "Caminho bfs:", caminho_bfs)
        print("Rodada : " + str(i) + " " + "Quantidade de nós expandidos bfs:", no_expandidos_bfs)
        print("Rodada : " + str(i) + " " + "Quantidade de memória alocada bfs:", memoria_usada_bfs, "bytes")
    
        # print("Rodada : " + str(i) + " " + "Caminho dfs:", caminho_dfs)
        print("Rodada : " + str(i) + " " + "Quantidade de nós expandidos dfs:", no_expandidos_dfs)
        print("Rodada : " + str(i) + " " + "Quantidade de memória alocada dfs:", memoria_usada_dfs, "bytes")

        # print("Rodada : " + str(i) + " " + "Caminho ucs:", caminho_ucs)
        print("Rodada : " + str(i) + " " + "Quantidade de nós expandidos ucs:", no_expandidos_ucs)
        print("Rodada : " + str(i) + " " + "Quantidade de memória alocada ucs:", memoria_usada_ucs, "bytes")
        
        # print("Rodada : " + str(i) + " " + "Caminho A* Harvesine:", caminho_A_star_harvesine)
        print("Rodada : " + str(i) + " " + "Quantidade de nós expandidos A* Harvesine:", no_expandidos_A_star_harvesine)
        print("Rodada : " + str(i) + " " + "Quantidade de memória alocada A* Harvesine:", memoria_usada_A_star_harvesine, "bytes")
        
        # print("Rodada : " + str(i) + " " + "Caminho A* Distância euclidiana:", caminho_A_star_euclidian_distance)
        print("Rodada : " + str(i) + " " + "Quantidade de nós expandidos A* Distância euclidiana:", no_expandidos_A_star_euclidian_distance)
        print("Rodada : " + str(i) + " " + "Quantidade de memória alocada A* Distância euclidiana:", memoria_usada_A_star_euclidian_distance, "bytes")