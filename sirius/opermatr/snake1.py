n, m = list(map(int, input().split())) 
a = [[i + j * n for j in range(m)] for i in range(n)]
for row in a:
    print(*row) 