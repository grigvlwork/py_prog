def splitnum(n, k):
    if n == 0 and k == 0:
        return 1
    elif n != 0 and k == 0:
        return 0
    elif k > n:
        return splitnum(n, n)
    else:
        return splitnum(n, k - 1) + splitnum(n - k, k)

n = int(input())
print(splitnum(n, n))