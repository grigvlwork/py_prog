n = int(input())
s = list()
diffs = list()
for i in range(n):
    s.append(int(input()))
for i in range(n):
    for j in range(n):
        if s[i] - s[j] not in diffs:
            diffs.append(s[i] - s[j])
diffs.sort()
for d in diffs:
    print(d)
