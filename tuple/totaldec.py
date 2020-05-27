n = int(input())
squad = list()
for i in range(n):
    squad.append(input())
k = int(input())
dead = list()
while len(dead) < n:
    new_squad = list()
    if k < len(squad):
        for i in range(len(squad)):
            if i % k == 0:
                dead.append(squad[i])
            else:
                new_squad.append(squad[i])
    else:
        for i in range(len(squad)):
            dead.append(squad[i])
    squad = new_squad
for soldier in dead:
    print(soldier)
