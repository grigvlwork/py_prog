k = 0
s = input()
minh = 200
maxh = 0
while s != "!":
    if 150 <= int(s) <= 190:
        k += 1
        minh = min(minh, int(s))
        maxh = max(maxh, int(s))
    s = input()
print(k)
print(minh, maxh)
