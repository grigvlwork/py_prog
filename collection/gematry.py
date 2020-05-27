from sys import stdin


def gem(word):
    total = 0
    for letter in word.upper():
        total += ord(letter) - ord('A') + 1
    return total


words = [w.replace('\n', '') for w in stdin]
gematry = [gem(w) for w in words]
print('\n'.join([k[1] for k in sorted(zip(gematry, words),
                                      key=lambda z: (z[0], z[1]))]))
