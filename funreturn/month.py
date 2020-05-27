def month_name(n, lang):
    month_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август',
                'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    month_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                'september', 'october', 'november', 'december']
    if lang == 'ru':
        return month_ru[n - 1]
    return month_en[n - 1]
