rows = int(input())
columns = int(input())
table = list()
for i in range(rows):
    row = list()
    for j in range(columns):
        row.append(input())
    table.append(row)
for r in table:
    print("\t".join(r))
print("")
for c in range(columns):
    for r in range(rows):
        print(table[r][c], end="\t")
    print("")
