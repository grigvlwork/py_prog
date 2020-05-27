pass1 = input()
pass2 = input()
if len(pass1) < 8:
    print("Короткий!")
elif pass1.find("123") > -1:
    print("Простой!")
elif pass1 != pass2:
    print("Различаются.")
else:
    print("OK")
