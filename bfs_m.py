from collections import deque
import time
import sys

def bfs(list_dict, origem, destino, tempo_limite=300):
    tempo_execucao = time.time()
    fila = deque()
    visitados = set()
    fila.append((origem, [origem]))
    memoria_usada = sys.getsizeof(visitados) + sys.getsizeof(fila)

    no_expandidos = 0
    while fila:
        no, caminho = fila.popleft()
        visitados.add(no)

        if no == destino:
            return caminho, no_expandidos, memoria_usada

        for dicionario in list_dict:
            if dicionario['coordenada_origem'] == no and dicionario['coordenada_destino'] not in visitados:
                fila.append((dicionario['coordenada_destino'], caminho + [dicionario['coordenada_destino']]))
                memoria_usada += sys.getsizeof(dicionario['coordenada_destino'])
                no_expandidos += 1

        if time.time() - tempo_execucao > tempo_limite:
                    return None, no_expandidos, memoria_usada

    return None, no_expandidos, memoria_usada