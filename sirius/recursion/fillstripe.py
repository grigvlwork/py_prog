from sys import setrecursionlimit
a = list()


def fill(n):
    global a
    #print(a)
    if n == 1:
        if a[0] == 0:
            print(1, end=' ')
            a[0] == 1
        else:
            return
    elif n == 2:
        if a[0] == a[1] == 0:
            print('1 2', end=' ')
            a[0] = 1
            a[1] = 1
        elif a[0] == 0 and a[1] == 1:
            print('1', end=' ')
            a[0] = 1
        elif a[0] == 1 and a[1] == 0:
            print('2', end=' ')
            a[1] = 1
        elif a[0] == 1 and a[1] == 1:
            return
    else:
        fill(n - 1)
        if len(a) == sum(a):
            return
        clear(n - 2)
        print(n, end=' ')
        a[n - 1] = 1
        fill(n - 1)


def clear(n):
    global a
    #print(a)
    if n == 1:
        if a[0] == 0:
            return
        else:
            print('-1', end=' ')
            a[0] = 0
    elif n == 2:
        if a[0] == a[1] == 0:
            return
        elif a[0] == 0 and a[1] == 1:
            print('1 -2 -1', end=' ')
            a[1] = 0
        elif a[0] == 1 and a[1] == 0:
            print('-1', end=' ')
            a[0] = 0
        elif a[0] == 1 and a[1] == 1:
            print('-2 -1', end=' ')
            a[0] = 0
            a[1] = 0
    else:
        fill(n - 1)
        if len(a) == sum(a):
            return
        clear(n - 2)
        print(-1 * n, end=' ')
        a[n - 1] = 0
        clear(n - 1)


setrecursionlimit(10 ** 9)
n = int(input())
a = [0] * n
fill(n)
#print(a)
