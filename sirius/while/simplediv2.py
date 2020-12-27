a = int(input())
if a % 2 == 0:
    print(2)
else:   
    i = 3
    while i * i <= a: 
        if a % i == 0:
            print(i)
            break
        i += 2
    else:
        print(a)