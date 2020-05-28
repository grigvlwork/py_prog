n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
p, q = map(int, input().split())
for i in range(n):
    a[i][p],a[i][q] = a[i][q], a[i][p]
for row in a:
    print(*row) 