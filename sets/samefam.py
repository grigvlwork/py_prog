n = int(input())
fam1 = set()
fam2 = set()
for i in range(n):
    emp = input()
    if emp not in fam1:
        fam1.add(emp)
    else:
        fam2.add(emp)
print(n - len(fam1.difference(fam2)))
