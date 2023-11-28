from collections import deque
from time import time
import sys

def bfs(graph, origem, destino, tempo_limite=10):
    tempo_execucao = time()
    fila = deque()
    visitados = set()
    fila.append((origem, [origem]))
    no_filho_exp = 0
    no_expandidos = 0

    while fila:
        no, caminho = fila.popleft()
        visitados.add(no)

        if no == destino:
            break

        for dest, _ in graph[no]:
            if dest not in visitados:
                fila.append((dest, caminho + [dest]))
                no_filho_exp += 1
            no_expandidos = no_expandidos + 1

        if (time() - tempo_execucao) > tempo_limite:
            break

    fator_ramificacao = no_filho_exp / no_expandidos
    memoria_usada = sys.getsizeof(fila) + sys.getsizeof(visitados)

    return visitados, no_expandidos, memoria_usada, fator_ramificacao, (time() - tempo_execucao)
