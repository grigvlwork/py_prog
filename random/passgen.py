from random import choice, seed, shuffle
from itertools import product


def generate_password(m):
    chars = 'qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM23456789'
    seed()
    return ''.join([choice(chars) for _ in range(m)])


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
        passwords = [''.join(list(i)) for i in t][:n]
    else:
        passwords = [generate_password(m) for _ in range(n)]
    return passwords


print(main(3000, 2))
