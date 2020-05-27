''' 
Минимальный простой делитель
Дано целое число, не меньшее 2. Выведите его наименьший простой 
делитель.

Входные данные

Вводится целое положительное число N≤2∗10^9.

Выходные данные

Выведите ответ на задачу.

Примеры
Ввод
    Вывод
15
    3
'''

n = int(input())
if n % 10 in (0, 2, 4, 6, 8):
    print(2)
else:
    divisor = 3
    while n % divisor != 0 and divisor < n / 2:
        divisor += 2
        if n % divisor == 0:
            div2 = 3
            flag = divisor % div2 != 0
            while div2 < divisor / 2 and flag:
                div2 += 2
                flag = divisor % div2 != 0
            if not flag:
                divisor += 2
    if n % divisor != 0:
        print(n)
    else:
        print(divisor)
