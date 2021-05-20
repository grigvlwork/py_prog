import json
from sys import stdin
from collections import defaultdict

data = json.load(stdin)
parents = defaultdict(list)
classes = set()
for row in data:
    classes.add(row['name'])
    if row['parents']:
        for par in row['parents']:
            parents[par].append(row['name'])
            classes.add(par)
for x in sorted(classes):
    k = 0
    x1 = x
    p = 1
    while p != 0:
        p = 0
        for y in parents:
            if x1 in parents[y]:
                p = y
        if p != 0:
            k += 1
            x1 = p
    print(x, k)


