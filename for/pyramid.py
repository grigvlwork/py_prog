n = int(input())
stars = 1
for i in range(n):
    print(" " * (n - i - 1) + "*" * stars)
    stars += 2
