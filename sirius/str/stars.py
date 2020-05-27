s = input()
t = ''
for i in range(len(s) - 1):
    t += s[i] + '*'
t += s[-1]
print(t)