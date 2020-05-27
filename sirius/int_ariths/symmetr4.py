n = int(input())
t = n // 1000
h = n // 100 % 10
d = n // 10 % 10
e = n % 10
print(1 - n // 100 + e * 10 +d)