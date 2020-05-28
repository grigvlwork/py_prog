n, m = list(map(int, input().split())) 
a = [[i * m + j for j in range(m)] for i in range(n)]
for row in a:
    print(*row) 