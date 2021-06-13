import random

class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

random.seed()
a = []
for i in range(10):
    a.append(Number(random.randint(0, 100)))
print(*a)
i = 0
while i < len(a):
    if a[i].num > 50:
        a.remove(a[i])
    else:
        i += 1
print(*a)
