n = int(input())
flag = False
for i in range(n):
    s = input()
    if s.find("Кот") > -1 or s.find("кот") > -1:
        flag = True
        break
if flag:
    print("МЯУ")
else:
    print("НЕТ")
