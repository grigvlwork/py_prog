n = int(input())
z = int(input())
k = 0
while z != 0:
    if z > n:
        k += 1
    n, z = z, int(input())
print(k) 