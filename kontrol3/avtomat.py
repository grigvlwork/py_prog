n = int(input())
for i in range(100, 1000):
    r1 = i // 100
    r2 = i // 10 % 10
    r3 = i % 10
    if r1 + r2 <= r2 + r3:
        p = int(str(r1 + r2) + str(r2 + r3))
    else:
        p = int(str(r2 + r3) + str(r1 + r2))
    if p == n:
        print(i)
        break