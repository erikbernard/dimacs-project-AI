from construir_grafo_m import construir_grafo
from bfs_m import bfs
from dfs_m import dfs
from ucs_m import ucs


if __name__ == "__main__":
    arquivo_coordenadas = 'data/USA-road-d.NY.co'
    arquivo_grafo = "data/USA-road-d.NY.gr"

    list_dict = construir_grafo(arquivo_coordenadas, arquivo_grafo)
    origem = (41.085396, -73.530767)
    destino = (41.086098, -73.530538)
    # caminho, no_expandidos, memoria_usada = bfs(list_dict, origem, destino)
    caminho, no_expandidos, memoria_usada = dfs(list_dict, origem, destino, 4)
    # caminho, no_expandidos, memoria_usada = ucs(list_dict, origem, destino)

    print("Caminho:", caminho)
    print("Quantidade de nós expandidos:", no_expandidos)
    print("Quantidade de memória alocada:", memoria_usada, "bytes")
  