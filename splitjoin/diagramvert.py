s1 = [int(s) for s in input().split()]
print("*" * (len(s1) + 2))
print("*" + " " * len(s1) + "*")
height = max(s1)
for i in range(height):
    print("*", end="")
    for j in range(len(s1)):
        if s1[j] >= height - i:
            print("*", end="")
        else:
            print(" ", end="")
    print("*")
