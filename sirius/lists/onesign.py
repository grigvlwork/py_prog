a = list(map(int, input().split()))
k = 0
for i in range(len(a) - 1):
    if a[i] * a[i + 1] > 0:
        print(a[i], a[i + 1])
        break
