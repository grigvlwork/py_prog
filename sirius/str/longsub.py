s = input()
if len(s) == 1:
    print(s)
else:
    maxlen = max_l = max_r = -1
    for i in range(len(s) - 1):
        r = s.rfind(s[i])
        if r > i: 
            if len(s[i:r + 1]) > maxlen:
                maxlen = len(s[i:r + 1])
                max_l = i
                max_r = r
    if maxlen > -1:
        print(s[max_l:max_r + 1])
    else:
        print(s[0])
