word = input()
maxword = word
minword = word
while word != "стоп":
    if len(word) > len(maxword):
        maxword = word
    if len(word) < len(minword):
        minword = word
    word = input()
flag = True
for i in range(len(minword)):
    if maxword.find(minword[i]) == -1:
        flag = False
if flag:
    print("ДА")
else:
    print("НЕТ")
