s = input()
n = int(s[0])
for i in range(1, len(s), 2):
    if s[i] == '+':
        n += int(s[i + 1])
    else:
        n -= int(s[i + 1])
print(n)
