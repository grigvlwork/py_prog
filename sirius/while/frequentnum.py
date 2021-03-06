'''Самое частое число в последовательности
Последовательность состоит из натуральных чисел, причем какое-то из 
чисел составляет более половины от общего числа членов последовательности. 
Найдите это число.
Для решения этой задачи запрещено использование массивов и списков.
Входные данные
На вход подается последовательность натуральных чисел, заканчивающаяся 
нулём. Его обрабатывать не нужно. Гарантируется, что все числа не 
превосходят 10^9.
Выходные данные
Выведите ответ на задачу.
Примеры
Ввод Вывод
4    
6
6
2
6
0
     6

1
2
3
1
2
3
4
1
2
3
1
0
'''
c1 = c2 = c3 = a1 = a2 = a3 = 0
x1 = int(input())
x2 = int(input())
while  x2 != 0:
    if x1 == x2:
        if a1 < 2:
            c1 = x1
            a1 = 2
        elif a2 < 2:
            c2 = x1
            a2 = 2 
        elif a3 < 2:
            c3 = x1
            a3 = 2 
        else:
            if x1 == c1:
                a1 += 1
            elif x1 == c2:
                a2 += 1
            elif x1 == c3:
                a3 += 1
    else:
        if a1 < 1:
            c1, c2 = x1, x2
            a1 = a2 = 1
        elif a3 < 1:
            c3 = x2
            a3 = 1 
        else:
            if x2 == c1:
                a1 += 1
            elif x2 == c2:
                a2 += 1
            elif x2 == c3:
                a3 += 1
    flag = False
    if a1 < a2:
        a1, a2 = a2, a1
        c1, c2 = c2, c1
        flag = True
    if a2 < a3:
        a2, a3 = a3, a2
        c2, c3 = c3, c2
        flag = True
    if a1 < a2:
        a1, a2 = a2, a1
        c1, c2 = c2, c1
        flag = True
    if flag:
        a3 = c3 = 0
    x1, x2 = x2, int(input())
print(c1)


