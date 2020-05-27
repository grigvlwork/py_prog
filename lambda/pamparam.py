def vawels_only(word):
    vawels = 'еыаоэяуиюё'
    new_word = ''
    for letter in word:
        if letter in vawels:
            new_word += letter
    return new_word


rhymes = sorted([len(k) for k in list(map(vawels_only, input().split(' ')))])
if rhymes[0] == rhymes[-1]:
    print('Парам пам-пам')
else:
    print('Пам парам')

