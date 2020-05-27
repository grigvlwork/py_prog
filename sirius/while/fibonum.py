n = int(input())
a = b = 1
num = 2
while b != n and b < n:
    a, b = b, a + b
    num += 1
if b == n:
    print(num)
else:
    print(-1)
