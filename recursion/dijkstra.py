# Рассмотрим реализацию алгоритм Дейкстры с восстановлением ответа на графе,
# хранимым в виде списка смежности на языке Python. Набор вершин, смежных с
# вершиной i будет храниться в множестве w[i]. Также необходимо хранить веса
# ребер, будем считать, что для хранения весов ребер используется словарь
# weight, где ключом является кортеж из двух вершин. То есть вес ребра из
# i в j хранится в элементе weight[i, j] словаря весов.


graph_edges = list()
weight = dict()
w = list()
in_data = [int(s) for s in input().split()]
while len(in_data) == 3:
    graph_edges.append(in_data)
    weight[graph_edges[0], graph_edges[1]] = graph_edges[2]
    max_vertex = max(graph_edges[0], graph_edges[1])
    while len(w) < max_vertex + 1:
        s = set()
        w.append(s)
    w[graph_edges[0]].append(graph_edges[1])
    w[graph_edges[1]].append(graph_edges[0])
    in_data = [int(s) for s in input().split()]
begin = in_data[0]
end = in_data[1]
start = begin

INF = 10000000000
n = max_vertex
dist = [INF] * n
dist[start] = 0
prev = [None] * n
used = [False] * n
min_dist = 0
min_vertex = start
while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in w[i]:
        if dist[i] + weight[i, j] < dist[j]:
            dist[j] = dist[i] + weight[i, j]
            prev[j] = i
    min_dist = INF
    for i in range(n):
        if not used[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_vertex = i
