m = int(input())
n = int(input())
k = int(input())
lang1 = set()
lang2 = set()
lang3 = set()
for i in range(m + n + k):
    pupil = input()
    if pupil not in lang1:
        lang1.add(pupil)
    elif pupil not in lang2:
        lang2.add(pupil)
    else:
        lang3.add(pupil)
amount = 0
for pupil in lang1:
    if pupil in lang2 and pupil not in lang3:
        amount += 1
if amount > 0:
    print(amount)
else:
    print("NO")