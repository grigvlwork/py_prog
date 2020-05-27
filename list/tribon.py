a = [1, 1, 1]
n = int(input())
if n < 4:
    for i in range(n):
        print(a[i], end=" ")
else:
    for i in a:
        print(i, end=" ")
    for i in range(n - 3):
        new = a[0] + a[1] + a[2]
        a[0], a[1], a[2] = a[1], a[2], new
        print(a[2], end=" ")
