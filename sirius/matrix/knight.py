a = [['.'] * 8 for i in range(8)]
row = int(input()) - 1
col = int(input()) - 1
a[row][col] = 'K'
for i in range(8):
    for j in range(8):
        if abs(row - i) * abs(col - j) == 2:
            a[i][j] = '*'
for row in a:
    print(*row)
