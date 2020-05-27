st = input()
way = st[0]
pos = 0
for i in range(1, len(st)):
    if st[i] == ">":
        pos += 1
        way += st[0]
    elif st[i] == "V":
        print(way)
        way = " " * pos + st[0]
    elif st[i] == "<":
        pos -= 1
        new_way = ""
        for j in range(len(way)):
            if j == pos:
                new_way += st[0]
            else:
                new_way += way[j]
        way = new_way
print(way)
