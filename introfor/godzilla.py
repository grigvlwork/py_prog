n = int(input())
a = int(input())
b = int(input())
nod1 = a
nod2 = b
while nod1 != nod2:
    if nod1 > nod2:
        nod1 -= nod2
    else:
        nod2 -= nod1
a = a // nod1
b = b // nod1
for i in range(n - 1):
    c = int(input())
    d = int(input())
    numerator = a * d + b * c
    denominator = b * d
    nod1 = numerator
    nod2 = denominator
    while nod1 != nod2:
        if nod1 > nod2:
            nod1 -= nod2
        else:
            nod2 -= nod1
    a = numerator // nod1
    b = denominator // nod1
print(str(a) + "/" + str(b))
