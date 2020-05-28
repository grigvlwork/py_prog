n, m = list(map(int, input().split())) 
a = [[i * m + j + 1 for j in range(m)] if i % 2 == 0 
     else [i * m + j + 1 for j in range(m)][::-1] 
     for i in range(n) ]
for row in a:
    print(*row) 