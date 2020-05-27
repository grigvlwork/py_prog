n = int(input())
set1 = list()
for i in range(n):
    set1.append(int(input()))
set1.sort(reverse=True)
for item in set1:
    print(item)
