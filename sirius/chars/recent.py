s = input().upper()
t = sorted([[i, s.count(i)] for i in set(s) if i.isalpha()], 
           reverse=True, key=lambda x: x[1])
max_l = t[0][1]
s = ''.join(sorted([i[0] for i in t if i[1] == max_l]))
print(s)
print(max_l)
