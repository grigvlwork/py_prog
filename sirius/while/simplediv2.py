from math import sqrt

a = int(input())
if a % 10 in (0, 2, 4, 6, 8):
    print(2)
elif a % 10 == 5:
    print(5)
elif sum(map(int, list(str(a)))) % 3 == 0:
    print(3)
else:
    flag = True
    for i in range(3, int(sqrt(a)), 2): 
        for j in range(5, int(sqrt(i)), 2):
            if i % j == 0:
                break
        else:
            if a % i == 0:
                print(i)
                flag = False
                break
    if flag:
        print

