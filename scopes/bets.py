bets = [0 for _ in range(10)]


def do_bet(horse, bet):
    global bets
    if 0 < horse < 11:
        if bet > 0 and bets[horse - 1] == 0:
            print('Ваша ставка в размере', bet, 'на лошадь', horse, 'принята')
            bets[horse - 1] = bet
            return
    print('Что-то пошло не так, попробуйте еще раз')
