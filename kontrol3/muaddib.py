from sys import stdin

a = dict()
for line in stdin:
    if ' # ' in line:
        t = line.replace('\n', '').split(' # ')
        if t[1] in a:
            a[t[1]].append([t[0], t[2]])
        else:
            a[t[1]] = [[t[0], t[2]]]
    else:
        name = line.replace('\n', '')
        t = a[name]
        t.sort(key=lambda x: x[0], reverse=True)
        for row in t:
            print(row[0], '(' + row[1] + ')')
        break
