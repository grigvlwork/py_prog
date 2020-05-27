def criteria(word):
    vowels = 'уеыаоэяиюё'
    n = 0
    for i in range(len(word)):
        if word[i] in vowels and i % 2 == 0:
            n += 1
    return n


text = input().lower().split()
a = list()
for word in text:
    a.append([word, criteria(word)])
a.sort(key=lambda x: (x[1], x[0]))
print('\n'.join([x[0] for x in a]))
