d = dict()
s = input()
for ch in s:
    if d.get(ch) is not None:
        d[ch] += 1
    else:
        d[ch] = 1
listKeys = sorted(d.keys())
for ch in listKeys:
    print(ch, '{0:.2f}'.format(100 * d[ch] / len(s)))
