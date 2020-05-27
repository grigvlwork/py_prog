from random import seed, random


def in_circle(x, y):
    if x * x + y * y < 1:
        return True
    else:
        return False


n = 100000
seed()
circle_points = 0
for i in range(n):
    if in_circle(random(), random()):
        circle_points += 1
print(4 * circle_points / n)
