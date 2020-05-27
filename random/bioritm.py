from datetime import datetime
from math import sin, pi


def bio(p, t):
    return sin((2 * pi * t) / p) * 100


dt1 = datetime.strptime(input(), "%d.%m.%Y")
dt2 = datetime.strptime(input(), "%d.%m.%Y")
delta = dt2 - dt1
print(bio(23, delta.days))
print(bio(28, delta.days))
print(bio(33, delta.days))
