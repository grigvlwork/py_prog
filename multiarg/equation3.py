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


def solve(*coefficients):
    if len(coefficients) == 1:
        return roots_of_quadratic_equation(0, 0, coefficients[0])
    elif len(coefficients) == 2:
        return roots_of_quadratic_equation(0, coefficients[0], coefficients[1])
    elif len(coefficients) == 3:
        return roots_of_quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
    else:
        return None


coeffs = [float(k) for k in input().split()]
print(' '.join([str(k) for k in solve(*coeffs)]))
