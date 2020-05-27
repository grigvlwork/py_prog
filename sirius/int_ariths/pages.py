k = int(input())
n = int(input())
p = (n + (k - n % k) % k) // k
num = k - (k - n % k) % k
print(p, num)