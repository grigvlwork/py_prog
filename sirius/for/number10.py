a = int(input())
for i in range(9):
    print(a % 10, end=" ")
    a //=10
print(a)