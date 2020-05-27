mail_template = 'To: %(email)s\n' + \
                'Здравствуйте, %(name)s!\n' + \
                'Были бы рады видеть вас на встрече начинающих программистов в %(place)s,\n' + \
                'которая пройдет %(date_meet)s.'


def spamgen(**mail_args):
    global mail_template
    return mail_template % mail_args


print(spamgen(email='John@yandex.ru', name='John', place='Горностай',
              date_meet='20.11.2019'))
print(spamgen(email='Anna@yandex.ru', name='Anna', place='Горностай',
              date_meet='20.11.2019'))