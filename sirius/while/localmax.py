z1 = int(input())
if z1 == 0:
    print(0)
else:
    z2 = int(input())
    if z2 == 0:
        print(0)
    else:
        z3 = int(input())
        k = 0
        while z3 != 0:
            if z1 < z2 > z3:
                k += 1
            z1, z2, z3 = z2, z3, int(input())
        print(k) 