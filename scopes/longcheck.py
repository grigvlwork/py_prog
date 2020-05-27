check = list()
num_check = 0


def add_item(itemName, itemCost):
    global check
    check.append([itemName, itemCost])


def print_receipt():
    global check, num_check
    if len(check) > 0:
        total = 0
        num_check += 1
        print('Чек', str(num_check) + '.' + ' Всего предметов:', len(check))
        for line in check:
            print(line[0], '-', line[1])
            total += line[1]
        print('Итого:', total)
        print('-----')
        check = list()
