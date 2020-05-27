def take_large_banknotes(banknotes):
    large = list()
    for b in banknotes:
        if b > 10:
            large.append(b)
    return large


