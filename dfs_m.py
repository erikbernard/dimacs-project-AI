from time import time
from sys import getsizeof

def dfs(list_dict, origem, destino, limite_profundidade,tempo_limite=10):
    tempo_execucao = time()
    pilha = [(origem, [origem], 0)]
    visitados = set()
    memoria_usada = getsizeof(visitados) + getsizeof(pilha)

    sum_fator_ramificacao = 0
    no_expandidos = 0
    while pilha:
        no, caminho, profundidade = pilha.pop()
        visitados.add(no)

        if no == destino:
            return visitados, no_expandidos, memoria_usada, (sum_fator_ramificacao/len(visitados)), (time() - tempo_execucao )

        if profundidade < limite_profundidade:
            for dicionario in list_dict:
                if dicionario['coordenada_origem'] == no and dicionario['coordenada_destino'] not in visitados:
                    pilha.append((dicionario['coordenada_destino'], caminho + [dicionario['coordenada_destino']], profundidade + 1))
                    memoria_usada += getsizeof(dicionario['coordenada_destino'])
                    no_expandidos += 1
                    sum_fator_ramificacao += 1

        if (time() - tempo_execucao )> tempo_limite:
            break

    return None, no_expandidos, memoria_usada, (sum_fator_ramificacao/len(visitados)), (time() - tempo_execucao )
