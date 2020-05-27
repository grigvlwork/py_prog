rows = int(input())
cols = int(input())
table = list()
for i in range(rows):
    row = list()
    for j in range(cols):
        row.append(input())
    if i != 0 and i != rows - 1:
        row.sort()
    table.append(row)
for row in table:
    print("\t".join(row))
