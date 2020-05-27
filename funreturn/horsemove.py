def strcort(c):
    s = 'ABCDEFGH'
    return s[c[0] - 1] + str(c[1])


def cortstr(s):
    row = ord(s[0]) - ord('A') + 1
    col = int(s[1])
    return (row, col)


def infield(t):
    if t[0] in range(1, 9) and t[1] in range(1, 9):
        return True
    return False


def possible_turns(cell):
    d = [-2, -1, 1, 2]
    pos = cortstr(cell)
    moves = list()
    for i in d:
        for j in d:
            if abs(i) != abs(j):
                pret = (pos[0] + i, pos[1] + j)
                if infield(pret):
                    moves.append(strcort(pret))
    moves.sort()
    return moves

