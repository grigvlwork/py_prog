n = int(input())
if n <= 1:
    print("НЕТ")
    exit(0)
set1 = list()
for i in range(n):
    set1.append(int(input()))
num = int(input())
flag = False
for i in range(n - 1):
    for j in range(i + 1, n):
        if set1[i] * set1[j] == num:
            flag = True
            break
    if flag:
        break
if flag:
    print("ДА")
else:
    print("НЕТ")
