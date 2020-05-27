def palindrome(s):
    t = s.lower()
    t = t.replace(' ', '')
    if t == t[::-1]:
        return 'Палиндром'
    return 'Не палиндром'
