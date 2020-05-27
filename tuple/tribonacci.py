n = int(input())
a = [1, 1, 1]
for i in range(3, n):
    a.append(a[i - 1] + a[i - 2] + a[i - 3])
print(*a[:n])

