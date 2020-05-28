a = list(map(int, input().split()))
i = 0
while i < len(a):
    k = 0
    j = i + 1
    while j < len(a):
        if a[i] == a[j]:
            k = 1
            a.pop(j)
        else:
            j += 1
    if k == 1:
        a.pop(i)
    else:
        i += 1
print(*a)
