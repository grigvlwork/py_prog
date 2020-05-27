from math import sqrt


def discriminant(a, b, c):
    return b * b - 4 * a * c


def larger_root(p, q):
    disc = discriminant(1, p, q)
    return (sqrt(disc) - p) / 2


def smaller_root(p, q):
    disc = discriminant(1, p, q)
    return (-p - sqrt(disc)) / 2


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))


