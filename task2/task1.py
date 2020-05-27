s = input().split(";")
if len(s) == 4:
    print(s[0] + ';', s[3] + ';', s[2] + ';', s[1])
else:
    print(s[0] + ';', s[4] + ';', s[2] + ';', s[3] + ';', s[1])
