def change(x, y): 
    if len(x) == 0 and len(y) == 0:
        direction = 0 
    elif len(x) == 0 and len(y) != 0:
        t = y.pop(0)
        x.append(t)
        direction = -1
    elif len(y) == 0 and len(x) != 0:
        t = x.pop(0)
        y.append(t)
        direction = 1
    elif x[0] > y[0]:
        t = y.pop(0)
        x.insert(0, t)
        direction = -1
    else:
        t = x.pop(0)
        y.insert(0, t)
        direction = 1
    return x, y, direction

n = int(input())
a = list(range(1, n + 1))
b = []
c = []
t = a.pop(0)
c.insert(0, t)
print(1, 1, 3)
while len(c) < n:
    a, b, d = change(a, b)
    if d == 1:
        print(b[0], 1, 2)
    elif d == -1:
        print(a[0], 2, 1)
    t = c.pop(0)
    a.insert(0, t)
    print(1, 3, 1)
    b, c, d = change(b, c)
    if d == 1:
        print(c[0], 2, 3)
    elif d == -1:
        print(b[0], 3, 2)
    t = a.pop(0)
    c.insert(0, t)
    print(1, 1, 3)



