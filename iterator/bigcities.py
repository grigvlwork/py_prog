import sys

# lines = [line for line in sys.stdin if len(line) > 0]
lines = []
for i in range(7):
    lines.append(input())
intervals = dict()
for line in lines:
    name, population = line.split()[0], int(line.split()[2])
    left = (population // 100000) * 100 if population % 100000 > 0 else \
        (population // 100000 + 1) * 100
    right = (population // 100000 + 1) * 100 if population % 100000 > 0 else \
        (population // 100000 + 2) * 100
    print(name, left, right)
