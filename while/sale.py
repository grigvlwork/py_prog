s = float(input())
total = 0
while s > 0:
    if s > 1000:
        total += s * 0.95
    else:
        total += s
    s = float(input())
print(total)
