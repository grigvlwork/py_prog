a = list()
for i in range(3):
    a.append(int(input()))
a.sort(reverse=True)
for i in range(3):
    print(a[i])
