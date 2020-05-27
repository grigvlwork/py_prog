n = int(input())
purchases = list()
for i in range(n):
    name = input()
    amount = input()
    purchases.append(name + " " + amount)
for i in range(n - 1, -1, -1):
    print(purchases[i])
