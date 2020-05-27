def hz(word):
    t = ''
    c = dict()
    for letter in word:
        if letter in c:
            c[letter] += 1
        else:
            c[letter] = 1
    for key in sorted(c.keys()):
        t += key + str(c[key])
    return t


n = int(input())
words = dict()
for i in range(n):
    word = input().lower()
    key = hz(word)
    if key not in words.keys():
        words[key] = [word]
    else:
        if word not in words[key]:
            words[key].append(word)
anagrams = list()
for key in words.keys():
    if len(words[key]) > 1:
        anagrams.append(' '.join(sorted([w for w in words[key]])))
print('\n'.join(sorted(anagrams, key=lambda x: x[:11])))
