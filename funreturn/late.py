def minstr(s):
    return int(s[:s.find(':')]) * 60 + int(s[s.find(':') + 1:])


def late(now, classes, bus):
    buss = [t for t in bus if t >= 5]
    nom = minstr(now)
    clam = minstr(classes)
    if len(buss) == 0:
        return 'Опоздание'
    if clam - nom < buss[0] + 15:
        return 'Опоздание'
    else:
        i = 0
        while (clam - nom <= buss[i] + 15) and (i < len(buss)):
            i += 1
        if clam - nom <= buss[i] + 15:
            return 'Выйти через ' + str(buss[i] - 5) + ' минут'
        else:
            return 'Выйти через ' + str(buss[i - 1] - 5) + ' минут'
