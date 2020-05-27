def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    a = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            a[j][i] = matrix[i][j]
    matrix.clear()
    for line in a:
        matrix.append(line)
