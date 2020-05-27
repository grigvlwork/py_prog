n = int(input())
text = list()
for i in range(n):
    text.append(input())
n = int(input())
for i in range(n):
    print(text[int(input()) - 1])
