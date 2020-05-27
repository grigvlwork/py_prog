name = ''


def polite_input(invitation):
    global name
    if name == '':
        name = input('Как вас зовут?' + '\n')
    return input(name + ', ' + invitation + '\n')
