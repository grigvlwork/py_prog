n = int(input())
a1 = int(input())
s = 0
for i in range(n - 1):
    a2 = int(input())
    s += a1 * a2
    a1 = a2
print(s)
