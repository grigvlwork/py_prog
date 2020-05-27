from random import choice, seed


def make_bingo():
    nums = set([i for i in range(1, 76)])
    seed()
    t = list()
    for i in range(5):
        n = list()
        for j in range(5):
            if i != 2 or j != 2:
                z = choice(list(nums))
                n.append(z)
                nums.remove(z)
            else:
                n.append(0)
        t.append(tuple(n))
    return tuple(t)
