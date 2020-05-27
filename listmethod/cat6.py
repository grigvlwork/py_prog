n = int(input())
for i in range(n):
    s = input()
    if s.find("кот") > -1:
        print(i + 1, s.find("кот") + 1)
