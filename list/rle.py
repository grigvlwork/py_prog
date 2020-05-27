line = input()
rle = list()
sym = line[0]
amount = 1
for i in range(1, len(line)):
    if sym == line[i]:
        amount += 1
    else:
        rle.append(str(amount) + " " + sym)
        sym = line[i]
        amount = 1
rle.append(str(amount) + " " + sym)
for r in rle:
    print(r)
