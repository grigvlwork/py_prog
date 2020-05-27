d = dict()
n = int(input())
for i in range(n):
    line = input()
    word = line[:line.find(' ')]
    description = line[line.find(' ') + 1:]
    d[word] = description
n = int(input())
for i in range(n):
    word = input()
    if word not in d:
        print('Нет в словаре')
    else:
        print(d[word])
