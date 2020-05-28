def CaseChange(c):
    if c.isupper():
        return c.lower()
    elif c.islower():
        return c.upper()
    else:
        return c

print(CaseChange('A'))
print(CaseChange('a'))
print(CaseChange('1'))