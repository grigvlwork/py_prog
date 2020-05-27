s = input()
n, k = [int(m) for m in input().split()]
print(sum([int(m) ** 2 for m in s.split()][n:k + 1]))