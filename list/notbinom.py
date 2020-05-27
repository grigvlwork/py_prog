n = int(input())
fond = list()
for i in range(n):
    fond.append(int(input()))
for i in range(n - 1):
    print(fond[i] + fond[i + 1])
