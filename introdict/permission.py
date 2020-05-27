n = int(input())
perm = list()
for i in range(n):
    perm.append(input())
n = int(input())
for i in range(n):
    query = input()
    for p in perm:
        if p + '/' == query[:len(p) + 1] or p == query:
            print("YES")
            break
    else:
        print("NO")
