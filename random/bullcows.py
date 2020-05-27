from random import choice

history = list()
hidden_num = 0
all_nums = set()


def list_from_num(number):
    return list(str(number))


def answer(hidden_number, try_number):
    bulls = 0
    cows = 0
    for i in range(4):
        if try_number[i] == hidden_number[i]:
            bulls += 1
        elif try_number[i] in hidden_number:
            cows += 1
    return (cows, bulls)


def check_new_number(new_number):
    global hidden_num, history
    for move in history:
        if answer(list_from_num(hidden_num), list_from_num(new_number)) != \
                (move[1], move[2]):
            break
    else:
        return True
    return False


def init():
    global history, hidden_num, all_nums
    all_nums = set([i for i in range(1234, 9877)
                    if len(list(str(i))) == len(set(str(i)))])
    history = list()
    hidden_num = choice(list(all_nums))
    all_nums.remove(hidden_num)


def change_num():
    global history, hidden_num, all_nums
    if len(all_nums) == 0:
        return False
    else:
        i = choice(list(all_nums))
        all_nums.remove(i)
        while not check_new_number(i) and len(all_nums) > 0:
            i = choice(list(all_nums))
            all_nums.remove(i)
        if check_new_number(i):
            hidden_num = i
            return True
        return False


def game():
    new_game = True
    old_cows = 5
    old_bulls = 5
    change = True
    init()
    while new_game:
        try_number = input(
            'Введите четырехзначное число:')
        new_cows, new_bulls = answer(list_from_num(
            hidden_num), list_from_num(try_number))
        history.append([try_number, new_cows, new_bulls])
        print('Cows:', new_cows, 'Bulls:', new_bulls)
        if (new_cows > old_cows or new_bulls > old_bulls) and (new_bulls < 4):
            if change:
                change = change_num()
        elif new_bulls == 4:
            print('You win!')
            print('It takes', len(history), 'steps')
            if input('Once again?(y/n)') == 'n':
                new_game = False
            else:
                init()
        old_cows, old_bulls = new_cows, new_bulls


game()
