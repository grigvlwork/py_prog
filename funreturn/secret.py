def print_document(pages):
    for page in pages:
        if page[:8] == 'Секретно':
            print('Дальнейшие материалы засекречены')
            return
        else:
            print(page)
    print('Напечатано без купюр')


#print_document(["Обычная страница", "И еще страница", "Секретно Вот этот вот текст не показывать", "Никому", "Никогда"])
#print_document(["Пустой трёп", "который", "никому не интересен"])
