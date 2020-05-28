def f(a):
    global b
    b += 3
    print(a + b)
b = 2
f(b)
