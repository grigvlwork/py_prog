k = -1
s = input()
i = 1
while s != "СТОП":
    if s.find("Кот") > -1 or s.find("кот") > -1:
        k = i
        break
    s = input()
    i += 1
print(k)
