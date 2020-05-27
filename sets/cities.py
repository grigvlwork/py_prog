n = int(input())
city = set()
for i in range(n):
    city.add(input())
new_city = input()
if new_city in city:
    print("TRY ANOTHER")
else:
    print("OK")
