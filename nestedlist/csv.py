r = int(input())
csv = list()
for i in range(r):
    csv.append(input().split(","))
n = int(input())
for i in range(n):
    rc = [int(k) for k in input().split(",")]
    print(csv[rc[0]][rc[1]])
