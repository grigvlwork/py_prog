n = int(input())
classes = list()
for i in range(n):
    pupils = int(input())
    scores = list()
    for j in range(pupils):
        scores.append(int(input().split()[1]))
    classes.append(any([k == 5 for k in scores]))
print('ДА' if all(classes) else 'НЕТ')
