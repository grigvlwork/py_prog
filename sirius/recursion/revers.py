def rev():
    n = int(input())
    if n == 0:
        print(n)
        return
    else:
        rev()
        print(n)

rev()