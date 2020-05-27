text = input().split()
d = dict()
res = []
for word in text:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
    res.append(d[word])
print(*res)

