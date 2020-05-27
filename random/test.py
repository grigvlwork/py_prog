n = int(input())    # количество элементов
a = []
for i in range(n):  # считываем элементы списка
    a.append(input())
# Сортировка пузырьком:
a.sort()
a.sort(key=lambda x: x[-1])
for k in a:
	print(k)
