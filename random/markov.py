from swift import words
from random import choice

sw = dict()
words_index = list()


def lookup(word):
    global words_index
    if word in words_index:
        return words_index.index(word)
    else:
        words_index.append(word)
        return len(words_index) - 1


def init():
    global words, sw
    for i in range(len(words) - 2):
        w1 = lookup(words[i])
        w2 = lookup(words[i + 1])
        if (w1, w2) not in sw:
            sw[(w1, w2)] = [lookup(words[i + 2])]
        else:
            sw[(w1, w2)].append(lookup(words[i + 2]))


def text(n):
    global sw, words_index
    w1, w2 = choice(list(sw.keys()))
    text = words_index[w1] + ' ' + words_index[w2]
    for i in range(1, n):
        w3 = choice(sw[(w1, w2)])
        while (w2, w3) not in sw.keys():
            w3 = choice(sw[(w1, w2)])
        text += ' ' + words_index[w3]
        w1, w2 = w2, w3
    return text


init()
print(text(1000))
