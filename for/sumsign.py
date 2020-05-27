n = int(input())
sign = 1
summ = 0
for i in range(n):
    summ += sign * int(input())
    sign *= -1
print(summ)
