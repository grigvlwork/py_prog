import numpy as np


def make_ﬁeld(size):
    a = np.zeros((size, size)).astype(np.int8)
    for i in range(size):
        for j in range(size):
            a[i, j] = (i + j + 1) % 2
    return a

# print(make_ﬁeld(5))
