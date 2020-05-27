n = int(input())
a = int(input())
print(0)
summ = a
k = 1
for i in range(n - 1):
    a = int(input())
    if a > summ / k:
        print(">")
    elif a < summ / k:
        print("<")
    else:
        print("0")
    summ += a
    k += 1
