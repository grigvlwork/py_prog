a, b, c = sorted([float(s) for s in input().split()])
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    if c * c == (a * a + b * b):
        print(0)
    elif (b * b + a * a - c * c) / (2 * a * b) > 0:
        print(1)
    else:
        print(2)
else:
    print(-1)
