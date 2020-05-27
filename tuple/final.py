n = int(input())
chart = list()
for i in range(n):
    name = input()
    score = int(input())
    chart.append((score, name))
chart.sort(reverse=True)
final = chart[:n // 2 + n % 2 + 1][1]
final = list(final)
print(final)
