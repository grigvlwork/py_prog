a = list(map(int, input().split()))
max_x = a.count(a[0])
max_i = 0
for i in range(1, len(a)):
    if a.count(a[i]) > max_x:
        max_x = a.count(a[i])
        max_i = i
print(a[max_i])
