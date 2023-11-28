from time import time
import sys


def dfs(graph, origem, destino, tempo_limite=10):
    tempo_execucao = time()
    pilha = [(origem, [origem], 0)]
    visitados = set()
    no_filho_exp = 0
    no_expandidos = 0

    while pilha:
        no, caminho, profundidade = pilha.pop()
        visitados.add(no)

        if no == destino:
            break

        #  if profundidade < limite_profundidade:
        for dest, _ in graph[no]:
            if dest not in visitados:
                pilha.append((dest, caminho + [dest], profundidade + 1))
                no_filho_exp += 1
        no_expandidos = no_expandidos + 1

        if (time() - tempo_execucao) > tempo_limite:
            break

    fator_ramificacao = no_filho_exp / no_expandidos if no_expandidos > 0 else 0
    memoria_usada = sys.getsizeof(pilha) + sys.getsizeof(visitados)

    return visitados, no_expandidos, memoria_usada, fator_ramificacao, (time() - tempo_execucao)
