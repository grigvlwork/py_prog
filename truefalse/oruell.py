n = int(input())
war = "Евразия"
peace = "Остазия"
for i in range(n):
    com = input()
    if com == "С кем война?":
        print(war)
    elif com == "С кем мир?":
        print(peace)
    else:
        war, peace = peace, war
