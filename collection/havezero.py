from sys import stdin
from functools import reduce

print(reduce(lambda x, y: x * y,
             [reduce(lambda x, y: x * y,
                     [int(k) for k in w.split()]) for w in stdin]) == 0)
