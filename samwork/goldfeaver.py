n = int(input())
amount = 0
sum_gold = 0
sum_silv = 0
for i in range(n):
    color = input()
    value = float(input())
    if 'золот' in color and value > 50:
        amount += 1
        sum_gold += value
        break
    elif 'золот' in color and value > 1:
        amount += 1
        sum_gold += value
    elif 'серебр' in color and value > 1:
        amount += 1
        sum_silv += value
print(amount)
print(sum_silv)
print(sum_gold)

