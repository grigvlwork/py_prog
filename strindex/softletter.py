word1 = input()
if word1[-1] == "ь":
    if word1[-2] == input()[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")
else:
    if word1[-1] == input()[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")
