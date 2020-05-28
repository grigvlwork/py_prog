n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
max_row = 0
max_col = 0
max_el = a[0][0] 
for i in range(n):
    if max(a[i]) > max_el:
        max_el = max(a[i])
        max_row = i
        max_col = a[i].index(max_el)
print(max_row, max_col)