word1 = input()
word2 = input()
bull = 0
cow = 0
for i in range(len(word1)):
    if word1[i] == word2[i]:
        bull += 1
    elif word1.find(word2[i]) > -1:
        cow += 1
print(bull, cow)
