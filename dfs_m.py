import time
import sys

def dfs(list_dict, origem, destino, limite_profundidade,tempo_limite=300):
    tempo_execucao = time.time()
    pilha = [(origem, [origem], 0)]
    visitados = set()
    memoria_usada = sys.getsizeof(visitados) + sys.getsizeof(pilha)

    no_expandidos = 0
    while pilha:
        no, caminho, profundidade = pilha.pop()
        visitados.add(no)

        if no == destino:
            return caminho, no_expandidos, memoria_usada

        if profundidade < limite_profundidade:
            for dicionario in list_dict:
                if dicionario['coordenada_origem'] == no and dicionario['coordenada_destino'] not in visitados:
                    pilha.append((dicionario['coordenada_destino'], caminho + [dicionario['coordenada_destino']], profundidade + 1))
                    memoria_usada += sys.getsizeof(dicionario['coordenada_destino'])
                    no_expandidos += 1

        if time.time() - tempo_execucao > tempo_limite:
            return None, no_expandidos, memoria_usada

    return None, no_expandidos, memoria_usada
