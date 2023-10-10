import heapq
import time
import sys

def ucs(list_dict, origem, destino, tempo_limite=300):
    tempo_execucao = time.time()
    fila_prioridade = [(0, origem, [origem])]
    visitados = set()
    memoria_usada = sys.getsizeof(visitados) + sys.getsizeof(fila_prioridade)

    no_expandidos = 0
    while fila_prioridade:
        custo, no, caminho = heapq.heappop(fila_prioridade)
        visitados.add(no)

        if no == destino:
            return caminho, no_expandidos, memoria_usada

        for dicionario in list_dict:
            if dicionario['coordenada_origem'] == no and dicionario['coordenada_destino'] not in visitados:
                novo_custo = custo + dicionario['distancia']
                heapq.heappush(fila_prioridade, (novo_custo, dicionario['coordenada_destino'], caminho + [dicionario['coordenada_destino']]))
                memoria_usada += sys.getsizeof(dicionario['coordenada_destino'])
                no_expandidos += 1

        if time.time() - tempo_execucao > tempo_limite:
            return None, no_expandidos, memoria_usada

    return None, no_expandidos, memoria_usada


