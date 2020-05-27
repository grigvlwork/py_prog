a = list()
n = int(input())
a.append([0 for j in range(n)])
for i in range(n - 1):
    line = [int(s) for s in input().split()]
    for j in range(n - i - 1):
        line.append(0)
    a.append(line)
for i in range(n):
    for j in range(i + 1, n):
        a[i][j] = a[j][i]
for i in range(n):
    for j in range(i + 1, n):
        flag = False
        for k in range(n):
            if k != i and k != j and a[i][j] > a[i][k] + a[k][j]:
                flag = True
                break
        if flag:
            print(i, j)
