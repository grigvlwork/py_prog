n = int(input())
field = list()
for i in range(n):
    field.append(list(input()))
for row in field:
    if "".join(row).find("xxx") > -1:
        print("x")
        exit(0)
    elif "".join(row).find("ooo") > -1:
        print("o")
        exit(0)
for c in range(n):
    col = ""
    for r in range(n):
        col += field[r][c]
    if col.find("xxx") > -1:
        print("x")
        exit(0)
    elif col.find("ooo") > -1:
        print("o")
        exit(0)
print("-")