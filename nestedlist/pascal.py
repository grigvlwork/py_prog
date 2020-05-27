n = int(input())
pas = [[0, 1, 0]]
for i in range(n - 1):
    row = list()
    row.append(0)
    for j in range(1, len(pas[i])):
        row.append(pas[i][j - 1] + pas[i][j])
    row.append(0)
    pas.append(row)
for r in pas:
    for j in range(len(r)):
        if r[j] > 0:
            print(r[j], end=" ")
    print("")
