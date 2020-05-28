n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[i][n - i - 1] = '*'
    a[i][n // 2] = '*'
    a[n // 2][i] = '*'
for row in a:
    print(*row)
