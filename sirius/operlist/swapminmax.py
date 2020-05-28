a = list(map(int, input().split()))
n = a.index(max(a))
k = a.index(min(a))
a[n], a[k] = a[k], a[n]
print(*a)