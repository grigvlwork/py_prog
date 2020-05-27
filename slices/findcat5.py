n = int(input())
for i in range(n):
    word = input()
    if word.find("кот") > -1:
        print(i + 1, word.find("кот") + 1)
