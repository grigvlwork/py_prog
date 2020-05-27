n = int(input())
table = [['0'] * n for _ in range(n)]
for i in range(1, n):
    line = input().split()
    for j in range(len(line)):
        table[i][j] = line[j]
        table[j][i] = table[i][j]
for row in table:
    print(' '.join(row))
