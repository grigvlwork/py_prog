matrix = list()
totals = list()
s = [int(k) for k in input().split()]
matrix.append(s)
totals.append(sum(s))
n = len(s)
for i in range(n - 1):
    s = [int(k) for k in input().split()]
    matrix.append(s)
    totals.append(sum(s))
for i in range(n):
    totals.append(sum([matrix[k][i] for k in range(n)]))
totals = list(map(lambda x: True if x - totals[0] == 0 else False, totals))
print('YES' if all(totals) else 'NO')
