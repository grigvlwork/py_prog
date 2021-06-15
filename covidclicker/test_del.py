from math import sin, cos, pi, sqrt


def left_corner(angle, center, radius, delta):
    while angle > 2 * pi:
        angle -= 2 * pi
    if angle == 0:
        return center[0] - 5, center[1] - radius - delta
    elif angle == pi:
        return center[0] - 5, center[1] + radius
    elif angle == pi / 2:
        return center[0] - radius - delta, center[1] - 5
    elif angle == 3 * pi / 2:
        return center[0] + radius, center[1] - 5
    elif 0 < angle < pi / 2:
        x1 = center[0] - radius * sin(angle)
        y1 = center[1] - radius * cos(angle)
        x2 = center[0] - (radius + delta) * sin(angle)
        y2 = center[1] - (radius + delta) * cos(angle)
        k = - (y1 - y2) / (x1 - x2)
        k2 = - 1 / k
        b2 = y2 - k2 * x2
        A = 1 + k2 * k2
        B = -2 * (1 + y2 - b2)
        C = x2 * x2 + (b2 - y2) ** 2 - 25
        D = B * B - 4 * A * C
        if D >= 0:
            x_min = min((-B + sqrt(D)) / (2 * A), (-B + sqrt(D)) / (2 * A))
            x_max = max((-B + sqrt(D)) / (2 * A), (-B + sqrt(D)) / (2 * A))
            y = k2 * x_max + b2
            return x_min, y
    return 0, 0

print(left_corner(pi / 4, (120, 120), 80, 40))




# f = open('mathtables.py', 'w')
# a = dict()
# for i in range(361):
#     a[i * pi / 180] = [sin(i * pi / 180), cos(i * pi / 180)]
# text = "sc_table = " + str(a)
#
# f.write(text)
# f.close()
