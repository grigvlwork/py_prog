n = int(input())
k = int(input())
table = list()
for i in range(n):
    row = list()
    for j in range(k):
        row.append(input())
    table.append(row)
for row in table:
    print("\t".join(row))
