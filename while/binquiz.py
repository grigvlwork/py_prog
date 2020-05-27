a = 1
b = 1000
c = 500
print(c)
ans = input()
while ans != "=":
    if ans == ">":
        a = c
    else:
        b = c
    c = (a + b) // 2
    print(c)
    ans = input()
