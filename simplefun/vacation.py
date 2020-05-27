a = input()
b = input()
if (a != b) and ((a == "Тула" and b != "Пенза") or (a != "Тула" and b == "Пенза")):
    print("ДА")
else:
    print("НЕТ")
