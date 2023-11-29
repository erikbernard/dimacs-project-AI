# dimacs-project-AI
Para esta atividade você deverá utilizar as seguintes instâncias da base DIMACS
(http://www.diag.uniroma1.it/~challenge9/download.shtml):
1- Oeste Americano
2- Centro Americano
3- Leste Americano
4- Todo o Estados Unidos
## O que seu trabalho deverá fazer:
### O usuário poderá escolher um dos 3 primeiros mapas acima (Todo Estados Unidos
só se conseguir).
### Dado a escolha do mapa, o usuário irá colocar uma coordenada geográfica de
origem e destino (latitude e longitude, considere que o usuário irá colocar um dos
pontos da base DIMACS como entrada, podendo ser inteiros)
### Seu trabalho deverá calcular uma rota entre os dois pontos usando os seguintes
algoritmos:
 - Busca em Largura
 - Busca em profundidade (podendo ser o limitado)
 - Busca de custo uniforme
 - A*
 - IDA* (optativo)
### Para o algoritmo A* considere pelos menos duas heurísticas:
  - Linha reta entre as duas coordenadas (heurística “terra plana”);
  - Distância Haversine;
  - Outra heurística que você ache interessante.
### Seu programa deverá executar cada um dos algoritmos mencionados e ao fim
deverá imprimir as seguintes métricas:
  - Quantidade de nós expandidos;
  -  Fator de ramificação médio;
  -  Tempo para encontrar a solução;
  -  Quantidade de memória alocada para a execução.
### Você poderá colocar um limite de tempo máximo de execução. Por exemplo, 5
minutos.
### Crie um relatório com 50 pontos de origem e destinos aleatórios pontos 50 aleatórios
e faça uma tabela de comparação com as métricas.
