n = int(input())
k = 0
while n >= 2:
    if n % 2 == 0:
        n //= 2
        k += 1
    else:
        break
if n < 2:
    print(k)
else:
    print("НЕТ")
