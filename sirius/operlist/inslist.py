a = list(map(int, input().split()))
k, c = list(map(int, input().split()))
a.insert(k, c)
print(*a)
