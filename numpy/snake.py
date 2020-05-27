import numpy as np


def snake(rows, cols):
    a = np.arange(1, rows * cols + 1).reshape(rows, cols)
    for i in range(rows):
        if i % 2 == 1:
            a[i] = a[i][::-1]
    return a

# print(snake(5, 7))
