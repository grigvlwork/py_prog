message = input()
index = int(input()) - 1
if len(message) < index + 1 or index < 0:
    print('ОШИБКА')
else:
    print(message[index])

