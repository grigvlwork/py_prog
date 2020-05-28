a = list(map(int, input().split()))
i = 0
amnt_pair = 0
while i < len(a):
    k = 1
    j = i + 1
    while j < len(a):
        if a[i] == a[j]:
            k += 1
            a.pop(j)
        else:
            j += 1
    if k > 1:
        a.pop(i)
        amnt_pair += k * (k - 1) // 2
    else:
        i += 1
print(amnt_pair)