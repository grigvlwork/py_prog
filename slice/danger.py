n = int(input())
for i in range(n):
    word = input()
    if word[:3] == "Не " or word[:3] == "не ":
        print(word[3:])
    else:
        print(word)
