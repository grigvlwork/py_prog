from words_kniga import words
from random import choice
# import pickle


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
    for i in range(len(words) - 3):
        w1 = lookup(words[i])
        w2 = lookup(words[i + 1])
        w3 = lookup(words[i + 2])
        if (w1, w2, w3) not in sw:
            sw[(w1, w2, w3)] = [lookup(words[i + 3])]
        else:
            sw[(w1, w2, w3)].append(lookup(words[i + 3]))
    '''with open('sw.pickle', 'wb') as f:
        pickle.dump(sw, f)
        close()
    with open('words_index.pickle', 'wb') as f:
        pickle.dump(words_index, f)
        close()'''
    # with open('sw.pickle', 'rb') as f:
    #    sw = pickle.load(f)
    # with open('words_index.pickle', 'rb') as f:
    #    words_index = pickle.load(f)
    #    print(sw)


def word_or_return(word):
    if word == '#n':
        return '\n'
    else:
        return word


def text(n):
    global sw, words_index
    w1, w2, w3 = choice(list(sw.keys()))
    text = word_or_return(words_index[w1]) + ' ' \
        + word_or_return(words_index[w2]) + word_or_return(words_index[w3])
    for i in range(1, n):
        w4 = choice(sw[(w1, w2, w3)])
        while (w2, w3, w4) not in sw.keys():
            w3 = choice(sw[(w1, w2, w3)])
        text += ' ' + word_or_return(words_index[w4])
        w1, w2, w3 = w2, w3, w4
    return text


init()
f = open('enoh_new.txt', 'w')
f.write(text(25000))
f.close()
