n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
x = int(input())
weight = 0
for i in range(x):
    row, col = map(int, input().split())
    weight += a[row - 1][col - 1]
    a[row - 1][col - 1] = 0
print(weight)