from random import randint

scoring = dict()
scoring['Яблочко'] = 50
scoring['Зеленое кольцо'] = 25
ring = dict()
ring[1] = 8
ring[2] = 6
ring[3] = 42
ring[20] = 50
for i in range(4, 20):
    ring[i] = randint(1, 60)
scoring['Внешнее_кольцо'] = ring
ring = dict()
ring[1] = 2
ring[2] = 16
ring[3] = 56
ring[20] = 3
for i in range(4, 20):
    ring[i] = randint(1, 60)
scoring['Внутреннее_кольцо'] = ring


def score(*args):
    if len(args) == 1:
        return scoring[args[0]]
    else:
        return scoring[args[0]][args[1]]


