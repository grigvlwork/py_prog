relations = list()
weights = dict()
optimal = list()


def len_way(verts):
    global weights
    total = 0
    for i in range(len(verts) - 1):
        total += weights[(verts[i], verts[i + 1])]
    return total


def way(begin, end, verts):
    global relations, weights, optimal
    new_vert = verts.copy()
    if begin in new_vert:
        new_vert.remove(begin)
    min_path = 9999999999999
    paths = [min_path for k in range(max(verts) + 1)]
    for vert in new_vert:
        if vert == end and vert in relations[begin]:
            paths[vert] = weights[(begin, end)]
        elif vert in relations[begin]:
            paths[vert] = weights[(begin, vert)] + way(vert, end, new_vert)
    for i in range(len(paths)):
        if paths[i] == min(paths):
            optimal.append(i)
            break
    return min(paths)


vertices = set()
s = input()
while len(s.split()) > 2:
    begin, end, weight = [int(k) for k in s.split()]
    while begin > len(relations) - 1 or end > len(relations) - 1:
        t = set()
        relations.append(t)
    relations[begin].add(end)
    relations[end].add(begin)
    vertices.add(begin)
    vertices.add(end)
    weights[(begin, end)] = weight
    s = input()
begin, end = [int(k) for k in s.split()]
vertices.remove(begin)
k = way(begin, end, vertices)
optimal.append(begin)
optimal = optimal[::-1]
print(', '.join([str(k) for k in optimal]))
# 1 2 1
# 2 3 2
# 3 4 3
# 2 4