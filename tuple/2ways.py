s = int(input())
params = list()
for i in range(s):
    k = int(input())
    params.append([k, k])
n = int(input())
for i in range(n):
    brother = int(input()) - 1
    param = int(input())
    value = int(input())
    params[param][brother] += value
match = 0
for i in range(s):
    if params[i][0] == params[i][1]:
        match += 1
for i in range(2):
    for j in range(s):
        print(params[j][i], end=" ")
    print("")
print(match)
