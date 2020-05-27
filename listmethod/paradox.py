from statistics import median
from statistics import mode

united = list()
mods = ""
medians = ""
n = int(input())
for i in range(n):
    s = [int(k) for k in input().split()]
    united.extend(s)
    mods += str(mode(s)) + " "
    medians += str(median(s)) + " "
print(medians)
print(mods)
print(median([int(s) for s in medians.split()]))
print(mode([int(s) for s in mods.split()]))
print(median(united))
print(mode(united))
