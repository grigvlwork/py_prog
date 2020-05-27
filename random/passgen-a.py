from random import choice, seed, shuffle
from itertools import product


def generate_password(m):
    chars = 'qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM23456789'
    seed()
    if m < 8:
        p = ''.join([choice(chars) for _ in range(m)])
        while len(p) > len(set(p)):
            p = ''.join([choice(chars) for _ in range(m)])
    else:
        c = set(chars)
        p = ''
        for i in range(m):
            n = choice(list(c))
            p += n
            c.remove(n)
    return p


def main(n, m):
    chars = set('qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM23456789')
    passwords = []
    if m == 1:
        for i in range(n):
            c = choice(list(chars))
            chars.remove(c)
            passwords.append(c)
    elif m == 2:
        c1 = c2 = list(chars)
        t = [list(i) for i in product(c1, c2)]
        shuffle(t)
        passwords = [''.join(list(i)) for i in t if len(i) == len(set(i))][:n]
    else:
        passwords = [generate_password(m) for _ in range(n)]
    return passwords