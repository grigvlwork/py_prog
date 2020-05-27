a = set()
while True:
    s = input().split(":")
    if s[0] == "заказала":
        a.add(s[1])
        print("хорошо")
    else:
        if s[1] in a:
            a.remove(s[1])
            print("хорошо")
        else:
            print("когда ты успела это заказать?")
    if len(a) == 0:
        print("Остановись, мгновенье! Ты прекрасно!")
        break
while True:
    try:
        s = input()
    except EOFError:
        break
