# N — количество вершин;
# S — номер стартовой вершины (отсчитывая от нуля);
# matrix — матрица смежности исходного графа, где несуществующие рёбра имеют бесконечный вес;
# В данном случае бесконечность равна 1000000;
def dijkstra(n, s, matrix):
    valid = [True] * n
    weight = [1000000] * n
    weight[s] = 0
    for i in range(n):
        min_weight = 1000001
        id_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                id_min_weight = i
        for i in range(n):
            if weight[id_min_weight] + matrix[id_min_weight][i] < weight[i]:
                weight[i] = weight[id_min_weight] + matrix[id_min_weight][i]
        valid[id_min_weight] = False
    return weight


graph_matr = []
graph_edges = []
in_data = [int(s) for s in input().split()]
while len(in_data) == 3:
    graph_edges.append(in_data)
    in_data = [int(s) for s in input().split()]
begin = in_data[0]
end = in_data[1]
max_edge = -1
for row in graph_edges:
    max_edge = max(graph_edges[0], graph_edges[1], max_edge)
graph_matr = [1000000 * (max_edge + 1) for _ in range(max_edge + 1)]
for row in graph_edges:
    graph_matr[graph_edges[0]][graph_edges[1]] = graph_edges[2]
print(dijkstra(max_edge, begin, graph_matr)[end])
