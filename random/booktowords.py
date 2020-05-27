def book_to_words(filename):
    words = []
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    puncts = '.,;:-!?'
    nums = '01234567890'
    bracks = '()[]"'
    f_input = open(filename, 'r')
    f_output = open('words_' + filename, 'w')
    type_of_word = 'text'
    word = ''
    for line in f_input:
        for c in line:
            if len(word) == 0:
                if c in alph or c in nums:
                    word += c
                    type_of_word = 'text' if c in alph else 'number'
                elif c in puncts or c in bracks:
                    words.append(c)
                elif c == '\n':
                    words.append('#n')
            else:
                if c == ' ':
                    words.append(word)
                    word = ''
                elif c == '\n':
                    words.append(word)
                    words.append('#n')
                    word = ''
                elif c in puncts or c in bracks:
                    words.append(word)
                    words.append(c)
                    word = ''
                elif (type_of_word == 'text' and c in alph) or \
                        (type_of_word == 'number' and c in nums):
                    word += c
                elif (type_of_word == 'text' and c in nums) or \
                        (type_of_word == 'number' and c in alph):
                    words.append(word)
                    word = c
                    type_of_word = 'text' if c in alph else 'number'
    content = ("words = ['" + "', '".join(words) + "']")
    f_output.write(content)
    f_input.close()
    f_output.close()
       

book_to_words('Kniga.txt')