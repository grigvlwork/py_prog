a = input()
b = sorted([int(a[0]), int(a[1]), int(a[2])])
if (b[0] + b[2]) / 2 == b[1]:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")
