def IsPalindrome(S):
    return S.upper() == S.upper()[::-1]

if IsPalindrome(input()):
    print('YES')
else:
    print('NO')