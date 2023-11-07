from heapq import heappush, heappop
from time import time
from sys import getsizeof

def ucs(list_dict, origem, destino, tempo_limite=10):
    tempo_execucao = time()
    fila_prioridade = [(0, origem, [origem])]
    visitados = set()
    memoria_usada = getsizeof(visitados) + getsizeof(fila_prioridade)

    sum_fator_ramificacao = 0
    no_expandidos = 0
    while fila_prioridade:
        custo, no, caminho = heappop(fila_prioridade)
        visitados.add(no)

        if no == destino:
            return visitados, no_expandidos, memoria_usada, (sum_fator_ramificacao/len(visitados)), (time() - tempo_execucao )

        for dicionario in list_dict:
            if dicionario['coordenada_origem'] == no and dicionario['coordenada_destino'] not in visitados:
                novo_custo = custo + dicionario['distancia']
                heappush(fila_prioridade, (novo_custo, dicionario['coordenada_destino'], caminho + [dicionario['coordenada_destino']]))
                memoria_usada += getsizeof(dicionario['coordenada_destino'])
                no_expandidos += 1
                sum_fator_ramificacao += 1

        if (time() - tempo_execucao )> tempo_limite:
            break

    return None, no_expandidos, memoria_usada, (sum_fator_ramificacao/len(visitados)), (time() - tempo_execucao )


