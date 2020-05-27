morse_code_en = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----'}
morse_code_ru = {'А': '.-', 'Б': '-...', 'Ц': '-.-.', 'Д': '-..', 'Е': '.',
              'Ф': '..-.', 'Г': '--.', 'Х': '....', 'И': '..', 'Й': '.---',
              'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
              'П': '.--.', 'Щ': '--.-', 'Р': '.-.', 'С': '...', 'Т': '-',
              'У': '..-', 'Ж': '...-', 'В': '.--', 'Ь': '-..-', 'Ы': '-.--',
              'З': '--..', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----', 'Ч': '---.', 'Ш': '----', 
              'Ъ': '--.--', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}
language = 'en'

def encode_to_morse(text):
    global morse_code_en, morse_code_ru, language
    message = ''
    if language == 'en':
        for letter in text.upper():
            message += morse_code_en[letter] + ' '
        return message.strip()
    else:
        for letter in text.upper():
            message += morse_code_ru[letter] + ' '
        return message.strip()        
   

def decode_from_morse(code):
    global morse_code_en, morse_code_ru, language
    message = ''
    if language == 'en':
        for coded_letter in code.split():
            for key, value in morse_code_en:
                if value == coded_letter:
                    message += 
        return message.strip()    