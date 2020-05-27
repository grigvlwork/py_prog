s = input().split()
for i in range(0, len(s)):
    if (i + 1) % 3 == 0:
        print(s[i], end=" ")
