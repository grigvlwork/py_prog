def remain(n):
    r = 0
    i = 1
    while i * i <= n:
        r = n - i * i
        i += 1
    return r


p = int(input())
v = int(input())
rp = remain(p)
rv = remain(v)
rpv = remain(p + v)
if rp + rv < rpv:
    print('Petya leaves paint to himself')
elif rp + rv > rpv:
    print('Petya gives paint to Vasya')
else:
    print('Equal')
