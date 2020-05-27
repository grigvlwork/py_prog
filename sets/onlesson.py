m = int(input())
n = int(input())
set1 = set()
for i in range(n):
    set1.add(input())
for i in range(m - 1):
    n = int(input())
    set2 = set()
    for j in range(n):
        set2.add(input())
    set1 = set1.intersection(set2)
for pupil in set1:
    print(pupil)
