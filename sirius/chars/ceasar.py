# A - 65 Z - 90  a - 97 z - 122

def CaesarCipherChar(c, k):
    if ord(c) in range(65, 91):
        return chr(65 + (ord(c) - 39 + k) % 26)
    elif ord(c) in range(97, 123):
        return chr(97 + (ord(c) - 71 + k) % 26)
    else:
        return c

def CaesarCipher(S, k):
    t = ''
    for c in S:
        t += CaesarCipherChar(c, k)
    return t

print(CaesarCipher(input(), 3))