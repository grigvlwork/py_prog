from math import sin, cos, pi, sqrt


def left_corner(angle, center, radius, delta):
    n = int(angle / (2 * pi))
    angle -= 2 * pi * n
    if angle == 0:
        return center[0] - 5, center[1] - radius - delta
    elif angle == pi:
        return center[0] - 5, center[1] + radius
    elif angle == pi / 2:
        return center[0] - radius - delta, center[1] - 5
    elif angle == 3 * pi / 2:
        return center[0] + radius, center[1] - 5
    elif 0 < angle < pi / 2:
        x = center[0] - (radius + delta) * sin(angle)
        y = center[1] - (radius + delta) * cos(angle)
        dx = 5 * cos(angle)
        dy = 5 * sin(angle)
        return x - dx, y - dy
    elif pi / 2 < angle < pi:
        angle = pi - angle
        x = center[0] - (radius + delta) * sin(angle)
        y1 = center[1] - radius * cos(angle)
        dx = 5 * cos(angle)
        dy = 5 * sin(angle)
        return x - dx, y1 - dy
    elif pi < angle < 3 * pi / 2:
        angle = 3 * pi / 2 - angle
        x1 = center[0] + radius * cos(angle)
        y1 = center[1] + radius * sin(angle)
        dx = 5 * sin(angle)
        dy = 5 * cos(angle)
        return x1 - dx, y1 - dy
    else:
        angle = 2 * pi - angle
        y = center[1] - (radius + delta) * cos(angle)
        x1 = center[0] + radius  * sin(angle)
        dx = 5 * cos(angle)
        dy = 5 * sin(angle)
        return x1 - dx, y - dy



print(left_corner(pi / 3, (120, 120), 80, 40))

# f = open('mathtables.py', 'w')
# a = dict()
# for i in range(361):
#     a[i * pi / 180] = [sin(i * pi / 180), cos(i * pi / 180)]
# text = "sc_table = " + str(a)
#
# f.write(text)
# f.close()
