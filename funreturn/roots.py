from math import sqrt


def roots_of_quadratic_equation(a, b, c):
    if a == b == c == 0:
        return ['all']
    if a == b == 0:
        return []
    if a == 0:
        return [-c / b]
    if b == 0:
        if c / a > 0:
            return [-sqrt(c / a), sqrt(c / a)]
        else:
            return []
    d = b * b - 4 * a * c
    if d == 0:
        return [-b / (2 * a)]
    elif d > 0:
        return [(-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)]
    return []

