n = int(input())
k = 0
while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n -= 1
    k += 1
print(k)
