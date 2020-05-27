n = int(input())
field = list()
for i in range(n):
    row = list()
    for j in range(n):
        row.append(int(input()))
    field.append(row)
k = int(input())
for i in range(k):
    col = int(input())
    row = int(input())
    for x in range(row - 1, row + 2):
        for y in range(col - 1, col + 2):
            if x in range(n) and y in range(n):
                if x == row and y == col:
                    field[x][y] = max(0, field[x][y] - 8)
                else:
                    field[x][y] = max(0, field[x][y] - 4)
for row in field:
    print(" ".join([str(a) for a in row]))
