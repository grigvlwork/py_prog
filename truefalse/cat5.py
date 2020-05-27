k = -1
amnt = 0
s = input()
i = 1
while s != "СТОП":
    if s.find("Кот") > -1 or s.find("кот") > -1:
        if k == -1:
            k = i
        amnt += 1
    s = input()
    i += 1
print(amnt, k)
