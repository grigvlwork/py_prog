a = list(map(int, input().split()))
k = int(input())
num = 1
for i in a:
    if k > i:
        break
    num += 1
print(num)
