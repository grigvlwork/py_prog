a = dict()
b = set()
n = int(input())
for i in range(n - 1):
    x, y = input().split()
    if y in a:
        a[y].append(x)
    else:
        a[y] = [x]
    b.add(x)
    b.add(y)
for x in sorted(b):
    k = 0
    x1 = x
    p = 1
    while p != 0:
        p = 0
        for y in a:
            if x1 in a[y]:
                p = y
        if p != 0:
            k += 1
            x1 = p
    print(x, k)
