alp_large = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alp_small = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def encrypt_caesar(*args):
    if len(args) == 1:
        msg = args[0]
        shift = 3
    else:
        msg = args[0]
        shift = args[1]
        if abs(shift) > 32:
            shift %= 33
    encrypted = ''
    for letter in msg:
        if letter in alp_large:
            pos = alp_large.find(letter)
            if 0 < pos + shift < 33:
                encrypted += alp_large[pos + shift]
            elif pos + shift < 0:
                encrypted += alp_large[33 + pos + shift]
            else:
                encrypted += alp_large[(pos + shift) % 33]
        elif letter in alp_small:
            pos = alp_small.find(letter)
            if 0 < pos + shift < 33:
                encrypted += alp_small[pos + shift]
            elif pos + shift < 0:
                encrypted += alp_small[33 + pos + shift]
            else:
                encrypted += alp_small[(pos + shift) % 33]
        else:
            encrypted += letter
    return encrypted


def decrypt_caesar(*args):
    if len(args) == 1:
        msg = args[0]
        shift = 3
    else:
        msg = args[0]
        shift = args[1]
        if abs(shift) > 32:
            shift %= 33
    decrypted = ''
    for letter in msg:
        if letter in alp_large:
            pos = alp_large.find(letter)
            if 0 < pos - shift < 33:
                decrypted += alp_large[pos - shift]
            elif pos - shift < 0:
                decrypted += alp_large[33 + pos - shift]
            else:
                decrypted += alp_large[(pos - shift) % 33]
        elif letter in alp_small:
            pos = alp_small.find(letter)
            if 0 < pos - shift < 33:
                decrypted += alp_small[pos - shift]
            elif pos - shift < 0:
                decrypted += alp_small[33 + pos - shift]
            else:
                decrypted += alp_small[(pos - shift) % 33]
        else:
            decrypted += letter
    return decrypted


