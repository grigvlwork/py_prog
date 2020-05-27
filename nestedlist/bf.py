ring = [0 for i in range(30000)]
program = list(input())
stack = list()
pos_data = 0
pos_prog = 0
while pos_prog < len(program):
    op = program[pos_prog]
    if op == "+":
        ring[pos_data] = (ring[pos_data] + 1) % 256
    elif op == "-":
        ring[pos_data] = (256 + ring[pos_data] - 1) % 256
    elif op == ">":
        pos_data = (pos_data + 1) % 30000
    elif op == "<":
        pos_data = (30000 + pos_data - 1) % 30000
    elif op == ".":
        print(ring[pos_data])
    elif op == "[":
        if ring[pos_data] == 0:
            while program[pos_prog] != "]":
                pos_prog += 1
        else:
            stack.append(pos_prog)
    elif op == "]":
        pos_prog = stack.pop()
        continue
    pos_prog += 1
