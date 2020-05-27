d = dict()
code = ''
text = input().split()
for word in text:
    if word not in d:
        d[word] = 1
        code = code + ' ' + '1'
    else:
        d[word] += 1
        code = code + ' ' + str(d[word])
print(code.strip())
