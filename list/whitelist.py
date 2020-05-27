n = int(input())
white = list()
for i in range(n):
    white.append(input())
n = int(input())
for i in range(n):
    query = input()
    if query in white:
        print(query)
