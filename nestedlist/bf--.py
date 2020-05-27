ring = [0 for i in range(30000)]
program = list(input())
pos = 0
for op in program:
    if op == "+":
        ring[pos] = (ring[pos] + 1) % 256
    elif op == "-":
        ring[pos] = (256 + ring[pos] - 1) % 256
    elif op == ">":
        pos = (pos + 1) % 30000
    elif op == "<":
        pos = (30000 + pos - 1) % 30000
    else:
        print(ring[pos])
