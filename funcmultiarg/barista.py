ingredients = list()
required = dict()
required['Эспрессо'] = [1, 0, 0]
required['Капучино'] = [1, 3, 0]
required['Кофе по-венски'] = [1, 0, 2]
required['Латте Маккиато'] = [1, 2, 1]
required['Маккиато'] = [2, 1, 0]
required['Кон Панна'] = [1, 0, 1]


def choose_coffee(*preferences):
    global ingredients, required
    for drink in preferences:
        flag = True
        for i in range(3):
            if required[drink][i] > ingredients[i]:
                flag = False
        if flag:
            for i in range(3):
                ingredients[i] -= required[drink][i]
            return drink
    return 'К сожалению, не можем предложить Вам напиток'
