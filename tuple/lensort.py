n = int(input())
lines = list()
for i in range(n):
    lines.append(input())
lines.sort()
for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(lines[j]) > len(lines[j + 1]):
            lines[j], lines[j + 1] = lines[j + 1], lines[j]
        elif len(lines[j]) == len(lines[j + 1]) and lines[j] > lines[j + 1]:
            lines[j], lines[j + 1] = lines[j + 1], lines[j]
for l in (lines):
    print(l)
