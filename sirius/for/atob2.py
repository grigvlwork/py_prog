a = int(input())
b = int(input())
if a < b:
    s = 1
else:
    s = -1
for i in range(a, b, s):
    print(i, end=" ")
print(b)