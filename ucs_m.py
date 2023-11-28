import sys
from heapq import heappush, heappop
from time import time

def ucs(graph, origem, destino, tempo_limite=10):
    tempo_execucao = time()
    fila_prioridade = [(0, origem, [origem])]
    visitados = set()
    no_filho_exp = 0 
    no_expandidos = 0

    while fila_prioridade:
        custo, no, caminho = heappop(fila_prioridade)
        visitados.add(no)

        if no == destino:
            break

        for dest, custo_dest in graph[no]:
            if dest not in visitados:
                novo_custo = custo + custo_dest
                heappush(fila_prioridade, (novo_custo, dest, caminho + [dest]))
                no_filho_exp += 1
        no_expandidos = no_expandidos + 1

        if (time() - tempo_execucao) > tempo_limite:
            break

    fator_ramificacao = no_filho_exp / no_expandidos
    memoria_usada = sys.getsizeof(fila_prioridade) + sys.getsizeof(visitados)

    return visitados, no_expandidos, memoria_usada, fator_ramificacao, (time() - tempo_execucao)
