def f():
    global a
    b = 2
    a, b = b, a
    print(a, b, end=" ")
a = 1
b = 2
f()
print(a, b, end=" ")
