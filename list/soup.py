soup = ("щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански")
n = int(input())
for i in range(n):
    print(soup[i % 5])
