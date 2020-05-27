def horiz(field):
    new_field = list()
    for row in field:
        new_field.append(row[::-1])
    return new_field


def vert(field):
    new_field = list()
    for i in range(len(field)):
        new_field.append(field[len(field) - i - 1])
    return new_field


def trans(field):
    new_field = [['.'] * len(field) for _ in range(len(field))]
    for i in range(len(field)):
        for j in range(len(field)):
            new_field[i][j] = field[j][i]
    return new_field


def vert_horiz(field):
    return vert(horiz(field))


def horiz_trans(field):
    return trans(horiz(field))


def vert_trans(field):
    return trans(vert(field))


def ref2trans(field):
    return trans(vert(horiz(field)))


def print_field(field):
    for row in field:
        print(''.join(row))


field = [['x', 'x', 'x', '.'],
         ['.', '.', '.', '.'],
         ['x', '.', 'x', 'x'],
         ['x', '.', '.', '.'], ]

print_field(field)
print('')
print_field(horiz(field))
print('')
print_field(vert(field))
print('')
print_field(trans(field))
print('')
print_field(vert_horiz(field))
print('')
print_field(horiz_trans(field))
print('')
print_field(vert_trans(field))
print('')
print_field(ref2trans(field))
