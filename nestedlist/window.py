n = int(input())
bottles = list()
for i in range(n):
    bottles.append(int(input()))
minml = int(input())
maxml = int(input())
print("\n".join([str(p) for p in bottles if p >= minml and p <= maxml]))
