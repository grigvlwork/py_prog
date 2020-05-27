m = int(input())
ingreds = set()
for i in range(m):
    ingreds.add(input())
m = int(input())
for i in range(m):
    receipt = input()
    k = int(input())
    flag = True
    for j in range(k):
        if input() not in ingreds:
            flag = False
    if flag:
        print(receipt)
