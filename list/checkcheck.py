n, total = [int(s) for s in input().split()]
error = ""
for i in range(n):
    line = input().split()
    if int(line[0]) * int(line[1][1:]) != int(line[2][1:]):
        error += str(i + 1) + " "
    total -= int(line[0]) * int(line[1][1:])
print(total)
print(error)
