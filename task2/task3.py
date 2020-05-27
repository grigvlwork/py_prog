a = "0123"
unlucky = int(input())
lucky = int(input())
k = 0
while int(a) < 9999:
    if (int(a[0]) < int(a[3])) and (str(unlucky) not in a) and (str(lucky) in a) and \
            ("3" not in a) and (("5" in a and "7" in a) or ("5" in a and "9" in a) or ( \
            "7" in a and "9" in a):
        k += 1
    a = str(int(a) + 1)
    if len(a) == 3:
        a = "0" + a
print(k)
