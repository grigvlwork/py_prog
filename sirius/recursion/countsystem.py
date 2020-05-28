def countsystem(p, n):
    if n == 0 :
        return
    else:
        countsystem(p, n // p)
        print(n % p, end='')

p = int(input())
n = int(input())
print(str(n) + '(10)=', end='')
countsystem(p, n) 
print('(' + str(p) + ')')