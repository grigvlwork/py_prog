def pattern(word):
    patn = ''
    for letter in word:
        if letter in vowels:
            patn += '*'
        else:
            patn += '-'
    return patn


vowels = 'уеыаоэяиюэ'
word_pattern = input()
pat = pattern(word_pattern)
vowel_amount = pat.count('*')
n = int(input())
for i in range(n):
    word = input()
    pat_new = pattern(word)
    if pat_new.count('*') == vowel_amount:
        flag = True
        for j in range(len(pat)):
            if pat[j] == '*' and pat_new[j] != '*':
                flag = False
                break
        if flag:
            print(word)
