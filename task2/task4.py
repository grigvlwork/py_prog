def get_words_with_strange_symbols(words):
    alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alph2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-'"
    d = dict()
    for w in words:
        for ch in w:
            if not ((ch in alph) or (ch in alph2)):
                if d.get(ch) is None:
                    a = set()
                    a.add(w)
                    d[ch] = a
                else:
                    d[ch].add(w)
    return d