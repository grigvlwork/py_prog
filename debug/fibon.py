k = int(input())
if k > 0:
    a = 1
    b = 1
    print(1)
    print(1)
    c = a + b
    while c <= k:
        print(c)
        a, b = b, c
        c = a + b
