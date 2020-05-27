lens = sorted([float(len(input())) for _ in range(3)])
if abs(lens[1] / lens[0] - lens[2] / lens[1]) < 0.0000001 \
        and (lens[0] < lens[1] < lens[2]):
    print('YES')
else:
    print('NO')
