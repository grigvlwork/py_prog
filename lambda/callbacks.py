def ask_password(login, password, success, failure):
    login = login.lower()
    password = password.lower()
    vowels = 'aeiouy'
    log_r = ''.join([k for k in login if k not in vowels])
    pass_r = ''.join([k for k in password if k not in vowels])
    n_vow = 0
    for letter in password:
        if letter in vowels:
            n_vow += 1
    message = ''
    if n_vow != 3 and log_r != pass_r:
        message = 'Everything is wrong'
    elif n_vow != 3:
        message = 'Wrong number of vowels'
    elif log_r != pass_r:
        message = 'Wrong consonants'
    if len(message) == 0:
        success(login)
    else:
        failure(login, message)


def main(login, password):
    ask_password(login, password, lambda login: print('Привет,', login + '!'),
                 lambda login, err: print('Кто-то пытался притвориться пользователем ' + login +
                                          ', но в пароле допустил ошибку:', err.upper() + '.'))
