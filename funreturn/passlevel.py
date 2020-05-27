def password_level(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    upp = 0
    low = 0
    dig = 0
    for c in password:
        if c.isdigit():
            dig = 1
        if c.isupper():
            upp = 1
        if c.islower():
            low = 1
    level = upp + low + dig
    if level == 1:
        return 'Ненадежный пароль'
    if level == 2:
        return 'Слабый пароль'
    return 'Надежный пароль'
