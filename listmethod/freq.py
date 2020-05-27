line = list("".join(input().split())).sort()
maxl = 1
length = 1
c = line[0]
maxc = c
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
