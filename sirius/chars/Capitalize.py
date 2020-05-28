def Capitalize(S):
    res = ''
    if S[0].isalpha():
        res += S[0].upper()
    else:
        res += S[0]
    for i in range(1, len(S)):
        if not S[i-1].isalpha() and S[i].isalpha():
            res += S[i].upper()
        elif S[i-1].isalpha() and S[i].isalpha():
            res += S[i].lower()
        else:
            res += S[i]
    return res

print(Capitalize(input()))