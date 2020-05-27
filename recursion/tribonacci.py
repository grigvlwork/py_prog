def tribonacci(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


# for i in range(10):
#     print(tribonacci(i))
