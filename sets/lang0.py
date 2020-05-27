engl = set()
germ = set()
num_e = int(input())
num_g = int(input())
for _ in range(num_e):
    engl.add(input())
for _ in range(num_g):
    germ.add(input())
if len(engl) + len(germ) - 2 * len(engl.intersection(germ)) > 0:
    print(len(engl) + len(germ) - 2 * len(engl.intersection(germ)))
else:
    print('NO')

