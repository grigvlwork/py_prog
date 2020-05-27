from random import choice, seed, shuffle
from itertools import product, permutations


def generate_password(m):
    chars = 'qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM23456789'
    little = 'qwertyuipasdfghjkzxcvbnm'
    big = 'QWERTYUPASDFGHJKLZXCVBNM'
    digits = '23456789'
    seed()
    if m < 8:
        p = choice(little) + choice(big) + choice(digits) + \
            ''.join([choice(chars) for _ in range(m - 3)])
        while len(list(p)) != len(set(list(p))):
            p = choice(little) + choice(big) + choice(digits) + \
                ''.join([choice(chars) for _ in range(m - 3)])
    else:
        c = set(chars)
        p = choice(little) + choice(big) + choice(digits) 
        for sym in p:
            c.remove(sym)
        for i in range(m - 3):
            n = choice(list(c))
            p += n
            c.remove(n)
    p = list(p)
    shuffle(p)
    return ''.join(p)


def main(n, m):
    seed()
    little = list('qwertyuipasdfghjkzxcvbnm')
    shuffle(little)
    big = list('QWERTYUPASDFGHJKLZXCVBNM')
    shuffle(big)
    digits = list('23456789')
    shuffle(digits)
    passwords = []
    if m == 3:
        t = [list(i) for i in product(little, big, digits)]
        t1 = list()
        i = 0
        while len(t1) < n:
            t1.extend([list(p) for p in permutations(t[i])])
            i += 1
        t1 = t1[:n]
        shuffle(t1)
        passwords = [''.join(i) for i in t1]
    else:
        passwords = [generate_password(m) for _ in range(n)]
    return passwords


print(*main(10, 10))
