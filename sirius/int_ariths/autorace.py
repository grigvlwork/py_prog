n = int(input())
m = int(input())
d = (m + (n - m % n) % n) // n 
print(d)