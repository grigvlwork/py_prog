n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(1, n):
    a[i][0] += a[i - 1][0]
for j in range(1, m):
    a[0][j] += a[0][j - 1]
for i in range(1, n):
    for j in range(1, m):
        a[i][j] += max(a[i][j - 1], a[i - 1][j]) 
print(a[-1][-1])
x = n - 1
y = m - 1
way = []
while x != 0 or y != 0:
    up = a[x - 1][y] if x > 0 else -1
    left = a[x][y - 1] if y > 0 else -1
    if up > left:
        way.append('D')
        x -= 1
    else:
        way.append('R')
        y -= 1
way = way[::-1]
print(*way)