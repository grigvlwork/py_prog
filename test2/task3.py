import numpy as np


def f(s):
    p = 1
    for t in s:
        if t < 0:
            p *= t
    return p


a = list()
n = int(input())
for i in range(n):
    a.append([int(k) for k in input().split()])
a = np.transpose(a)
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if f(a[i]) < f(a[j]):
            a[i], a[j] = a[j], a[i].copy()
        elif f(a[i]) == f(a[j]) and list(a[i]) < list(a[j]):
            a[i], a[j] = a[j], a[i].copy()
a = np.transpose(a)
for t in a:
    print('\t'.join([str(x) for x in t]))
