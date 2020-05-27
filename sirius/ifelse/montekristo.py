a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if d > e:
    d, e = e, d
if d <= b and e <= c:
    print('YES')
else:
    print('NO')
