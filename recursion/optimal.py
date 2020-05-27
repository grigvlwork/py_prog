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
    global relations, weights
    if len(verts) < 2:
        return []
    elif len(verts) == 2:
        if begin in verts and end in verts and end in relations[begin]:
            return [begin, end]
        else:
            return []
    else:
        all_ways = list()
        for vert in verts:
            if vert == end and vert in relations[begin]:
                all_ways.append([begin, end])
            elif vert in relations[begin]:
                temp_vert = verts.copy()
                if begin in temp_vert:
                    temp_vert.remove(begin)
                # temp_vert.remove(vert)
                temp_way = way(vert, end, temp_vert)
                if len(temp_way) > 0:
                    all_ways.append(temp_way)
        if len(all_ways) > 0:
            min_way = all_ways[0]
            min_len_way = len_way(min_way)
            for i in range(1, len(all_ways)):
                temp_way = all_ways[i]
                if len_way(temp_way) < min_len_way:
                    min_len_way = len_way(temp_way)
                    min_way = temp_way
            if len(min_way) > 0:
                if begin in min_way:
                    return min_way
                else:
                    return [begin] + min_way
            else:
                return []
        else:
            return []


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
    weights[(end, begin)] = weight
    s = input()
begin, end = [int(k) for k in s.split()]
# vertices.remove(begin)
optimal = way(begin, end, vertices)
# optimal = [begin] + optimal
print(', '.join([str(k) for k in optimal]))
# 1 2 10
# 2 5 6
# 2 3 1
# 3 4 1
# 4 5 2
# 1 5

# 1 2 1
# 2 3 2
# 3 4 3
# 2 4
