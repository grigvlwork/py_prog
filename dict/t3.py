tree = dict()
family = set()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    if parent in tree:
        tree[parent].append(child)
    else:
        tree[parent] = [child]
    family.add(child)
    family.add(parent)
for person in sorted(family):
    p1 = person
    k = 0
    flag = True
    while flag:
        flag = False
        for t in tree:
            if p1 in tree[t]:
                flag = True
                k += 1
                p1 = t
                break
        else:
            print(person, k)
