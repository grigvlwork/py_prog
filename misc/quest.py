print("Вы находитесь на развилке дорог, куда вы пойдете? Направо(1), налево(2) или прямо(3)")
ans = input()
if ans == "1":
    print("Вы встретили волка и он съел вашего коня.")
elif ans == "2":
    print("Вы встретили разбойников и они вас ограбили.")
elif ans == "3":
    print("Вы подходите к пещере вы войдете(1), или нет(2)?")
    ans2 = input()
    if ans2 == "1":
        print("Вы победили хозяина пещеры и нашли сокровище!")
    elif ans2 == "2":
        print("Вы возвратились домой ни с чем")
    else:
        print("Ошибка при вводе ответа")
else:
    print("Ошибка при вводе ответа")
