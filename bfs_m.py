from collections import deque
from time import time
from sys import getsizeof

def bfs(list_dict, origem, destino, tempo_limite=10):
    tempo_execucao = time()
    fila = deque()
    visitados = set()
    fila.append((origem, [origem]))
    memoria_usada = getsizeof(visitados) + getsizeof(fila)

    no_expandidos = 0
    while fila:
        no, caminho = fila.popleft()
        visitados.add(no)

        if no == destino:
            return visitados, no_expandidos, memoria_usada

        for dicionario in list_dict:
            if dicionario['coordenada_origem'] == no and dicionario['coordenada_destino'] not in visitados:
                fila.append((dicionario['coordenada_destino'], caminho + [dicionario['coordenada_destino']]))
                memoria_usada += getsizeof(dicionario['coordenada_destino'])
                no_expandidos += 1

        if (time() - tempo_execucao )> tempo_limite:
            break

    return None, no_expandidos, memoria_usada