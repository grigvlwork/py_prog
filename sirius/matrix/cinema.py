n, m = map(int, input().split())
a = [input().replace(' ', '') for i in range(n)]
k = '0' * int(input())
for i in range(n):
    if k in a[i]:
        print(i + 1)
        break
else:
    print(0)