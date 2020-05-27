print("Ваше любимое время года? Зима(1), Весна(2), Лето(3), Осень(4)")
ans = int(input())
summary = 0
if ans > 0 and ans < 5:
    summary += ans
else:
    print("Ошибка ввода")
    exit(0)
print("Ваше любимое занятие? Спорт(1), Программирование(2), Чтение(3), Игры(4)")
ans = int(input())
if 0 < ans < 5:
    summary += ans
else:
    print("Ошибка ввода")
    exit(0)
if summary == 2 or summary == 3:
    print("Вы любите спорт")
elif summary == 4:
    print("Вы любите программировать весной")
elif summary == 5:
    print("Вы любите почитать книги зимой")
elif summary == 6:
    print("Вы любите программировать осенью")
else:
    print("Вы любите игры")
