def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        k = power(a, n // 2)
        return  k * k
    else:
        return a * power(a, n - 1)

print(power(float(input()), int(input())))
