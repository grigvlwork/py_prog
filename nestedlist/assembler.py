indexes = [int(i) - 1 for i in input().split()]
words = [p.lower() for p in input().split()]
text = ""
for i in indexes:
    text += words[i] + " "
text = text[0].upper() + text[1:]
print(text)
