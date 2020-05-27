s = input()
odd = set()
even = set()
n = 0
while ' ' in s:
    message, key = s.upper().split()
    delimiter = key[0]
    words = set(message.split(delimiter))
    if n % 2 == 1:
        odd = odd.union(words)
    else:
        even = even.union(words)
    s = input()
    n += 1
print('\n'.join(list(even - odd)))
