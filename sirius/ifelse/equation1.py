a = int(input())
b = int(input())
if a == b == 0:
    print('INF')
elif a == 0 and b != 0:
    print('NO')
else:
    if -b / a == -b // a:
        print(-b // a)
    else:
        print('NO')
