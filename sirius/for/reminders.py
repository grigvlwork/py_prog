a = int(input())
b = int(input())
c = int(input())
d = int(input())
dif = (c + d - a % d) % d 
for i in range(a + dif, b + 1, d):
    print(i)