n = int(input())
d = dict()
p = ',.!?:; '
for i in range(n):
    row = input()
    j = 0
    word = ''
    for k in range(len(row)):
        if row[k] not in p:
            word = word + row[k]
        else:
            if len(word) > 0:
                word = word.lower()
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1
            word = ''
    if len(word) > 0:
        word = word.lower()
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
m = list(d.items())
m.sort(key=lambda d: (-d[1], d[0]))
for row in m:
    print(row[0][:1].upper() + row[0][1:])
