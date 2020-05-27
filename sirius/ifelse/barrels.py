a = int(input()) 
n = a % 100
if n == 0 or 4 < n < 21:
    print(a, 'bochek')
elif n % 10 == 1:
    print(a, 'bochka')
elif 1 < n % 10 < 5:
    print(a, 'bochki')
else:
    print(a, 'bochek')

