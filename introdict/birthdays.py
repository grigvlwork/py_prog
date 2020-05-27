n = int(input())
d = dict()
for i in range(n):
    row = input().split()
    name = row[0]
    month = row[2]
    if month not in d:
        d[month] = [name]
    else:
        d[month].append(name)
n = int(input())
for i in range(n):
    month = input()
    if month not in d:
        print('')
    else:
        d[month].sort()
        print(' '.join(d[month]))
