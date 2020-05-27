n = int(input())
a = list(map(int, input().split()))
minl = 0
minr = 1
mindif = abs(a[minl] - a[minr])
for i in range(1, len(a) - 1):
    for j in range(i + 1, len(a)):
        if abs(a[i] - a[j]) < mindif:
            minl = i
            minr = j
            mindif = abs(a[i] - a[j])
print(minl, minr)

