cols = int(input())
rows = int(input())
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(j / i, end=" ")
    print("")
