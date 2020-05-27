book = dict()
n = int(input())
for i in range(n):
    number, name = input().split()
    if name in book:
        book[name] = book[name] + " " + number
    else:
        book[name] = number
m = int(input())
for i in range(m):
    name = input()
    if name in book:
        print(book[name])
    else:
        print("Нет в телефонной книге")
