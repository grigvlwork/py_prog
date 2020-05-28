def toNum(s):
    return ord(s[0]) - ord('a'), int(s[1])

def is_correct(move1, move2):
    x1, y1 = toNum(move1)
    x2, y2 = toNum(move2)
    return abs(x1 - x2) < 2 and abs(y1 - y2) < 2

if is_correct(input(), input()):
    print('YES')
else:
    print('NO')

