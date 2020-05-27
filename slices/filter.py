n = int(input())
for i in range(n):
    word = input()
    if word[:2] == "%%":
        print(word[2:])
    elif word[:4] != "####":
        print(word)
