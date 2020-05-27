a = input()
b = input()
if (a.find("@") == -1) and (b.find("@") != -1):
    print("OK")
if a.find("@") != -1:
    print("Некорректный логин")
else:
    if b.find("@") == -1:
        print("Некорректный адрес")
