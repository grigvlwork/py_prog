n = int(input())
flag = False
for i in range(n):
    s = input()
    if s.find("Кот") > -1 or s.find("кот") > -1:
        flag = True
    if s.find("Пёс") > -1 or s.find("пёс") > -1:
        flag = False
if flag:
    print("МЯУ")
else:
    print("НЕТ")
