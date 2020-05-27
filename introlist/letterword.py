n = int(input())
text = list()
for i in range(n):
    text.append(input())
n = int(input())
for st in text:
    if n - 1 < len(st):
        print(st[n - 1], end="")
