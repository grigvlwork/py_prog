n = int(input())
teams = list()
for i in range(n):
    name = input()
    score = int(input())
    teams.append((score, name))
teams.sort(reverse=True)
finalists = list()
for i in range(n // 2 + n % 2):
    finalists.append(teams[i][1])
finalists.sort()
for team in finalists:
    print(team)
nofinal = list()
for i in range(n // 2 + n % 2, n):
    nofinal.append(teams[i][1])
nofinal.sort()
for team in nofinal:
    print(team)
