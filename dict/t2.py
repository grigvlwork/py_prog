phonebook = dict()
n = int(input())
for i in range(n):
    phone, name = input().split()
    if name in phonebook:
        phonebook[name].append(phone)
    else:
        phonebook[name] = [phone]
m = int(input())
for i in range(m):
    name = input()
    if name in phonebook:
        print(*phonebook[name])
    else:
        print('Нет в телефонной книге')

