s = input().lower()
s = list(s)
s.sort()
curc = s[0]
curl = 1
maxc = s[0]
maxl = 1
for i in range(1, len(s)):
    if s[i] != curc:
        if curl > maxl:
            maxc = curc
            maxl = curl
        curc = s[i]
        curl = 1
    else:
        curl += 1
print(maxl)
