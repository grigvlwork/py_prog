a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if ((a1 == a2 and b1 != b2) or (a1 != a2 and b1 == b2)):
    print('YES')
else:
    print('NO')
