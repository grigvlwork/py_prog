line = sorted(list("".join(input().split()).lower()))
maxl = length = 1
maxc = c = line[0]
for i in range(1, len(line)):
    if c != line[i]:
        if maxl < length:
            maxl = length
            maxc = c
        length = 1
        c = line[i]
    else:
        length += 1
print(maxc)

