from math import *
a, b, c = [float(s) for s in input().split()]
if a == 0 and b == 0 and c == 0:
    print("MANY SOLUTIONS")
else:
    d = b * b - 4 * a * c
    if (d < 0) or (a == 0):
        print("NO SOLUTION")
    elif d == 0:
        print('{0:.3f}'.format(round(-b / (2 * a), 3)))
    else:
        print('{0:.3f}'.format(round((-b + sqrt(d)) / (2 * a), 3)), '{0:.3f}'.format(round((-b - sqrt(d)) / (2 * a), 3)))
