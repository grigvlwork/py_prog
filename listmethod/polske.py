line = input().split()
stek = list()
for i in range(len(line)):
    if line[i] == "+":
        stek[-2] = stek[-2] + stek[-1]
        stek = stek[:-1]
    elif line[i] == "-":
        stek[-2] = stek[-2] - stek[-1]
        stek = stek[:-1]
    elif line[i] == "*":
        stek[-2] = stek[-2] * stek[-1]
        stek = stek[:-1]
    else:
        stek.append(int(line[i]))
print(stek[0])
