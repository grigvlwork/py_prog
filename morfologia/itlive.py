from pymorphy2 import MorphAnalyzer
from sys import stdin

m = MorphAnalyzer()
for w in stdin:
    wp = m.parse(w.lower())[0]
    if wp.tag.POS == 'NOUN':
        if 'anim' in wp.tag:
            print('Живое')
        else:
            print('Не живое')
    else:
        print('Не существительное')
