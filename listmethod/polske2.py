def fact(n):
    f = 1
    for j in range(1, n + 1):
        f *= j
    return f


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
    elif line[i] == "/":
        stek[-2] = stek[-2] // stek[-1]
        stek = stek[:-1]
    elif line[i] == "~":
        stek[-1] = - stek[-1]
    elif line[i] == "!":
        stek[-1] = fact(stek[-1])
    elif line[i] == "#":
        stek.append(stek[-1])
    elif line[i] == "@":
        stek[-3], stek[-2], stek[-1] = stek[-2], stek[-1], stek[-3]
    else:
        stek.append(int(line[i]))
print(stek[0])
