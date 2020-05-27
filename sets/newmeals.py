m = int(input())
all_meal = set()
for i in range(m):
    all_meal.add(input())
n = int(input())
for i in range(n):
    k = int(input())
    set1 = set()
    for j in range(k):
        set1.add(input())
    all_meal = all_meal.difference(set1)
for meal in all_meal:
    print(meal)
