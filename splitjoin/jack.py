n = int(input())
tituls = list()
for i in range(n):
    tit1 = input()
    line = ""
    while tit1 != "*":
        line += tit1 + " "
        tit1 = input()
    tituls.append("-".join(line.split()))
tituls = tituls[::-1]
print(", ".join(tituls))
