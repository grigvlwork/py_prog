word = input()
maxlen = 0
for i in range(1, len(word) + 1):
    if word.find("о" * i) > -1:
        maxlen = i
    else:
        break
print(maxlen)
