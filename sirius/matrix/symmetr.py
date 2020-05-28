n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    flag = True
    for j in range(i, n):
        if a[i][j] != a[j][i]:
            flag = False
            break
    if not flag:
        print('NO')
        break
else:
    print('YES')
    
