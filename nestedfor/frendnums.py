def sumdiv(n):
    summ = 1
    for j in range(2, n // 2 + 1):
        if n % j == 0:
            summ += j
    return summ


sums = dict()
for i in range(2, 10001):
    sums[i] = sumdiv(i)
for i in range(2, 10000):
    for j in range(i + 1, 10001):
        if i == sums[j] and j == sums[i]:
            print(i, j)
