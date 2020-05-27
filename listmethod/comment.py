n = int(input()[1:])
for i in range(n):
    s = input()
    if s.find("#") > -1:
        print(s[:s.find("#")].rstrip())
    else:
        print(s.rstrip())
