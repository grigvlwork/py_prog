n = int(input())
m = int(input())
pix = []
for i in range(n):
    line = input()[::2]
    if i % 2 == 0:
        pix.append(line)
for l in pix:
    print(l)
