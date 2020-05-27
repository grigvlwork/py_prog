n = int(input())
fond = list()
for i in range(n):
    fond.append(int(input()))
print(sum(fond[int(input()) - 1:int(input())]))
