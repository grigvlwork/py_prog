def makelevel(n):
    for i in range(1, n + 2):
        print('*' * i)


def tree(n):
    for i in range(1, n + 1):
        makelevel(i)


tree(int(input()))
