allowed = "abcdefghijklmnopqrstuvwxyz0123456789_"
flag = True
word = input()
for i in range(len(word)):
    if allowed.find(word[i]) == -1:
        flag = False
        break
if flag:
    print("OK")
else:
    print("Неверный символ:", word[i])
