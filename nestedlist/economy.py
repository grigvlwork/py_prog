n = int(input())
tab = list()
for i in range(n - 1):
    tab.append([int(s) for s in input().split()])
a, b = [int(s) for s in input().split()]
old_a = a
a, b = min(a, b), max(a, b)
price = tab[b - 1][a]
min_price = price
min_index = old_a
for j in range(n):
    price_changed = min_price
    if j != a and j != b:
        if j < a:
            price_changed = tab[a - 1][j] + tab[b - 1][j]
        elif j > b:
            price_changed = tab[j - 1][a] + tab[j - 1][b]
        else:
            price_changed = tab[j - 1][a] + tab[b - 1][j]
    if price_changed < min_price:
        min_price = price_changed
        min_index = j
print(min_index)
