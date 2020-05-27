a = list(map(int, input().split()))
k = int(input())
t = min(map(lambda x: abs(x - k), a))
for s in a:
    if abs(s - k) == t:
        print(s)
        break
