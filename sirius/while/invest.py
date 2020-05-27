x = int(input())
p = int(input()) / 100
y = int(input())
year = 0
while x < y:
    x = int(x * (1 + p) * 100) / 100 
    year += 1
print(year)
