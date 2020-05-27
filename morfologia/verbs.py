from pymorphy2 import MorphAnalyzer

m = MorphAnalyzer()
w = input()
wp = m.parse(w)[0]
if wp.tag.POS == 'INFN' or wp.tag.POS == 'VERB':
    print('Прошедшее время:')
    print(wp.inflect({'masc', 'past'}).word)
    print(wp.inflect({'femn', 'past'}).word)
    print(wp.inflect({'neut', 'past'}).word)
    print(wp.inflect({'plur', 'past'}).word)
    print('Настоящее время:')
    print(wp.inflect({'sing', '1per'}).word)
    print(wp.inflect({'plur', '1per'}).word)
    print(wp.inflect({'sing', '2per'}).word)
    print(wp.inflect({'plur', '2per'}).word)
    print(wp.inflect({'sing', '3per'}).word)
    print(wp.inflect({'plur', '3per'}).word)

else:
    print('Не глагол')
