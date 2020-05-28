n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(*row) 