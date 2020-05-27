word = input()
n = int(input())
symbol = input()
if n > len(word) or len(symbol) > 1 or n < 1:
    print("ОШИБКА")
elif word[n - 1] == symbol:
    print("ДА")
else:
    print("НЕТ")
