d = dict()
n = int(input())
for i in range(n):
    x, y = [int(s) for s in input().split()]
    area = (x // 10 * 10, y // 10 * 10)
    if area not in d:
        d[area] = 1
    else:
        d[area] += 1
print(max(d.values()))
