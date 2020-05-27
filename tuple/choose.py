n = int(input())
pupils = list()
for i in range(n):
    pupils.append(input())
for line in pupils:
    print(line)
print("")
for line in pupils:
    if line.split()[1] == "4" or line.split()[1] == "5":
        print(line)

