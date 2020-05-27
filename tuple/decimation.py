n = int(input())
squad = list()
for i in range(n):
    squad.append(input())
k = int(input())
m = int(input())
for i in range(m):
    not_exec = list()
    for j in range(len(squad)):
        if j % k != (k - 1):
            not_exec.append(squad[j])
    squad = not_exec
for sol in squad:
    print(sol)
