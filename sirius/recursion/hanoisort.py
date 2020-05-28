from sys import setrecursionlimit


def h(n, x, y):
    if n == 1:
        print(1, x, y)
    else:
        h(n-1, x, 6-x-y)
        print(n, x, y)
        h(n-1, 6-x-y, y)


setrecursionlimit(10 ** 9)
n = int(input())
s = 2 + (1 - n % 2)
h(n, 1, s)
for i in range(n - 1, 0, -1):
    t = 5 - s
    h(i, s, t)
    s = t
