n = int(input())
days = dict()
for i in range(n):
    name, date, month = input().split()
    date = int(date)
    if month not in days:
        days[month] = list()
        days[month].append([name, date])
    else:
        days[month].append([name, date])
m = int(input())
for i in range(m):
    month = input()
    if month not in days:
        print("")
    else:
        birth = days[month]
        birth.sort(key=lambda d: (d[1], d[0]))
        line = ""
        for row in birth:
            line += row[0] + " " + str(row[1]) + " "
        print(line.strip())
