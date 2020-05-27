m = int(input())
n = int(input())
lang1 = set()
lang2 = set()
for i in range(m + n):
    pupil = input()
    if pupil not in lang1:
        lang1.add(pupil)
    else:
        lang2.add(pupil)
amnt = len(lang1.difference(lang2))
if amnt > 0:
    print(amnt)
else:
    print("NO")
