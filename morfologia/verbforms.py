from pymorphy2 import MorphAnalyzer
from sys import stdin

s = stdin.read().lower()
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя \n'
m = MorphAnalyzer()
words = ''.join([i for i in s if i in alf]).split()
k = 0
for i in words:
    if m.parse(i)[0].normal_form in ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']:
        k += 1
print(k)
