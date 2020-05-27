flag = True
while flag:
    pass1 = input()
    pass2 = input()
    flag = False
    if len(pass1) < 8:
        print("Короткий!")
        flag = True
    elif pass1.find("123") > -1:
        print("Простой!")
        flag = True
    elif pass1 != pass2:
        print("Различаются.")
        flag = True
    else:
        print("OK")
