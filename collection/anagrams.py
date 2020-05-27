n = int(input())
words = dict()
words_index = list()
for i in range(n):
    word = input().lower()
    if word not in words_index:
        words_index.append(word)
        index = len(words_index) - 1
    else:
        index = words_index.index(word)
    key = tuple(sorted(list(word)))
    if key not in words.keys():
        words[key] = [index]
    else:
        if word not in words[key]:
            words[key].append(index)
print('\n'.join(sorted([' '.join(sorted([words_index[s] for s in words[k]]))
                        for k in words.keys() if len(words[k]) > 1])))
