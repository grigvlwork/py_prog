pi = 3.141592653589793
n = int(input())
summ = 0.0
for i in range(1, n + 1):
    summ += 1 / (i * i)
print(pi * pi / summ)
