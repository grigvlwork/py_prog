from sys import stdin

descriptions = dict()
for line in stdin.readlines():
    desc, pers = line.replace('\n', '').split(' - ')
    if pers in descriptions:
        descriptions[pers].add(desc)
    else:
        a = set()
        a.add(desc)
        descriptions[pers] = a
for key, value in descriptions.items():
    print(key + ':', '; '.join(value))
