s = input()
hl = s.find('h')
hr = s.rfind('h')
print(s[0:hl + 1] + s[hl + 1:hr].replace('h', 'H') + s[hr:])