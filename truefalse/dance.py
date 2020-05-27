patience = int(input())
errors = 0
right = 0
count = ["раз", "два", "три", "четыре"]
while errors < patience:
    say = input()
    if say != count[right % 4]:
        print("Правильных отсчётов было " + str(right) + ", но теперь вы ошиблись.")
        errors += 1
        right = 0
    else:
        right += 1
print("На сегодня хватит.")
