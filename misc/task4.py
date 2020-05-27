n = int(input())
marshrut = sorted([int(s) for s in input().split()])
ropes = list()
i = 0
for hook in range(n - 1):
    ropes.append(marshrut[hook + 1] - marshrut[hook])
hook = 1
print(ropes)
while hook < len(ropes) - 2:
    max1 = max(ropes[hook], ropes[hook + 1])
    max2 = max(ropes[hook + 1], ropes[hook + 2])
    if max1 >= max2:
        if ropes[hook] == max1:
            ropes[hook] = 0
            hook += 1
        else:
            ropes[hook + 1] = 0
            hook += 2
    else:
        if ropes[hook + 1] == max2:
            ropes[hook + 1] = 0
            hook += 2
        else:
            ropes[hook + 2] = 0
            hook += 3
minLen = 0
for i in range(len(ropes)):
    minLen += ropes[i]
print(minLen)
print(ropes)
