page1 = set()
page2 = set()
num = input()
while num:
    page1.add(num)
    num = input()
num = input()
while num:
    page2.add(num)
    num = input()
inter = page1.intersection(page2)
if len(inter) > 0:
    for num in inter:
        print(num)
else:
    print("EMPTY")
