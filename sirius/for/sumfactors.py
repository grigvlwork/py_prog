s = 0
f = 1
for i in range(1, int(input()) + 1):
    f *= i
    s += f
print(s)