from sys import setrecursionlimit

allowed = {
    (1,2): True,
    (2,1): False,
    (2,3): True,
    (3,2): False,
    (3,1): True,
    (1,3): False,
}
 
def move(n, x, y):
    if n > 0:
        z = 6 - x - y
        if allowed[(x,y)]:
            move(n-1, x, z)
            print(n, x, y)
            move(n-1, z, y)
        else:
            move(n-1, x, y)
            print(n, x, z)
            move(n-1, y, x)
            print(n, z, y)
            move(n-1, x, y)
            
setrecursionlimit(10 ** 9)
n = int(input())
move(n,1,3)