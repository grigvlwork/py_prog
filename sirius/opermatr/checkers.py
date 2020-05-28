a = [[0 for i in range(8)] for j in range(8)]
col, row = list(map(int, input().split()))
a[row - 1][col - 1] = 1
for i in range(row, 8):
    for j in range(8):
        if j - 1 > -1:
            a[i][j] += a[i - 1][j - 1]
        if j + 1 < 8:
            a[i][j] += a[i - 1][j + 1]
print(sum(a[7]))

        
