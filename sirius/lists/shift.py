a = input().split()
t = a[-1]
for i in range(len(a) - 1, 0, -1):
    a[i] = a[i - 1]
a[0] = t
print(*a)