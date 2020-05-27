d = int(input())
m = int(input())
y = int(input())
if m > 2:
    m -= 2
else:
    m += 10
    y -= 1
c = y // 100
y = y % 100
dow = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
print(dow % 7)
