n = int(input())
while str(n)[0] != "1" and n < 1000000000:
    n = n * int(str(n)[0])
print(n)
