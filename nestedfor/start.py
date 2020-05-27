n = int(input())
for i in range(n):
    for j in range(i, -1, -1):
        print("Осталось секунд:", j)
    print("Пуск", i + 1)