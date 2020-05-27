translated_text = ''


def translate(text):
    global translated_text
    translated_text = ''
    vowels = 'аоеиуюыэёюя'
    for letter in text:
        if not letter.isalpha():
            translated_text += ' '
        elif letter.lower() not in vowels:
            translated_text += letter
    while '  ' in translated_text:
        translated_text = translated_text.replace('  ', ' ')
    translated_text = translated_text.strip()

