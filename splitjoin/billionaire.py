magaz = input().split(";")
filter = list()
for n in magaz:
    filter.append(",".join([s for s in n.split(",") if int(s) >= 1000000000]))
print("\n".join(filter))