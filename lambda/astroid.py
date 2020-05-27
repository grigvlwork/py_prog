from math import sin, cos, sqrt, pi


def astro_x(x):
    return cos(x) ** 3


def astro_y(y):
    return sin(y) ** 3


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


left = 0
right = 2 * pi
n = 3
delta = (left + right) / n
x1 = astro_x(left)
y1 = astro_y(left)
x2 = astro_x(left + delta)
y2 = astro_y(left + delta)
while abs(distance(0.75, 0, x1, y1) - distance(0.75, 0, x2, y2)) > 0.0001:
    n *= 3
    delta = (left + right) / n
    x1 = astro_x(left)
    y1 = astro_y(left)
    x2 = astro_x(left + delta)
    y2 = astro_y(left + delta)
t = left
min_dist = 2
while t < right:
    temp_dist = distance(0.75, 0, astro_x(t), astro_y(t))
    if temp_dist < min_dist:
        min_dist = temp_dist
    t += delta
print(min_dist)
