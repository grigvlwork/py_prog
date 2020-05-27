n = int(input())
first_set = list()
for i in range(n):
    first_set.append(input())
k = int(input())
for i in range(k):
    second_set = list()
    m = int(input())
    for j in range(m):
        second_set.append(first_set[int(input()) - 1])
    first_set = second_set
for item in first_set:
    print(item)
