import numpy as np


def super_sort(rows, cols):
    a = np.random.randint(1, 100, size=(rows, cols))
    b = a.copy()
    b = b.transpose()
    for i in range(cols):
        if i % 2 == 0:
            b[i] = sorted(b[i])
        else:
            b[i] = sorted(b[i], reverse=True)
    b = b.transpose()
    return a, b
