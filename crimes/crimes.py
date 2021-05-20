import csv

data = []
crstat = dict()
with open("crimes.csv", "r", encoding="utf-8") as file_object:
    for row in csv.reader(file_object):
        if row[2][6:10] == "2005":
            if row[5] in crstat:
                crstat[row[5]] += 1
            else:
                crstat[row[5]] = 1
for key in crstat:
    print(key, crstat[key])
