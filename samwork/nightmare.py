n = int(input())
iron = 0
steel = 0
for i in range(n):
    m = int(input())
    for j in range(m):
        thing = input()
        if 6 < len(thing) < 22 and ('чугун' in thing or 'стал' in thing) and ('пух' not in thing)\
           and len(thing) % 4 != 0:
            if 'чугун' in thing:
                iron += 1
            elif 'стал' in thing:
                steel += 1
print(iron / n, steel / n)
print(iron + steel)

        
